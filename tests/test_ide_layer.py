"""Model-free checks of the IDE layer of the stage-1 processes (BL-192 Э5).

The layer is opencode.json, .opencode/agents/ and .opencode/commands/
(RFC-RT-003 §6–§7 and ADR-020 of G-Ivan-A/mango_ba_prompts, owner decisions
Р-RT-10…Р-RT-21). These tests evaluate its permission rules the way the
client does and pin what the decisions rely on:

* writes go only to work/ (Р-RT-14); the reviewer writes nothing;
* only the orchestrator asks the BA and delegates, and only to its two
  subagents (Р-RT-11);
* web, external directories and scripted tool calls are denied; MCP servers
  are disabled, read is ask, write is deny, an unknown tool is deny (Р-RT-15);
* every command starts the orchestrator; the orchestrator is fail-closed
  without the stage-1 gate map (Р-RT-12, Р-RT-17).

Rule semantics follow OpenCode 1.19.6 (`Permission.evaluate`): rules are
the config `permission` in key order, then the agent `permission`; the last
rule whose permission and pattern match wins; no match is `ask`. A pattern
`*` matches any text, `/` included. OpenCode 2.4.2 translates the same object
into its `permissions` list in the same order (checked live by
tests/opencode_smoke.py).
"""

import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "opencode.json"
AGENTS_DIR = ROOT / ".opencode/agents"
COMMANDS_DIR = ROOT / ".opencode/commands"
GATE_MAP = "ssot/mango_ba_prompts/docs/ba-processes/bcreq-ide-gates.json"

ORCHESTRATOR = "bcreq-orchestrator"
SUBAGENTS = ("bcreq-step", "bcreq-reviewer")
# Built-in agents of the client share the config rules (no agent rules here).
BUILTIN = "build"
ALL = (ORCHESTRATOR, *SUBAGENTS, BUILTIN)

# What the gate map of the spoke (BCREQ-IDE-GATES 0.1) declares; checked
# against the map itself once the stage-1 SSOT is in ssot/ (M2).
COMMANDS = {"a-in": "A-IN", "a-core": "A-CORE", "a-work": "A-WORK", "a-release": "A-RELEASE"}
HUMAN_GATES = ("Г-С1", "Г-W", "Выпуск")
LOG_FIELDS = ("code", "type", "outcome", "who", "when", "locator", "version",
              "question_id", "model_recommendation", "divergence")
TECHNICAL_STEPS = ("Ш-0", "AIN-01", "AIN-03", "AIN-04", "AIN-05", "AIN-06", "AIN-07",
                   "AIN-08", "AIN-09", "AIN-10", "AIN-12", "AIN-15", "AIN-19", "AIN-22")
FAIL_CLOSED = "ACCESS_GAP: карта гейтов этапа 1 — SSOT этапа 1 не передан в runtime"

MCP_SERVERS = ("jira", "confluence", "web")
WRITE_TOOLS = ("create_issue", "update_issue", "delete_page", "add_comment", "edit_page",
               "transition_issue", "upload_attachment", "remove_label", "assign_issue",
               "move_page", "batch_create", "post_message", "put_page", "set_status")
READ_TOOLS = {"jira": ("get_issue", "search", "list_projects"),
              "confluence": ("get_page", "search", "list_spaces"),
              "web": ("search", "fetch", "read")}


def front(text: str) -> tuple[dict, str]:
    """Frontmatter of an agent or command file (nested maps by indent) and its body."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.index("\n---\n", 4)
    root: dict = {}
    stack = [(-1, root)]
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, value = line.strip().partition(":")
        key, value = key.strip().strip('"'), value.strip().strip('"')
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if value:
            parent[key] = {"true": True, "false": False}.get(value, value)
        else:
            parent[key] = {}
            stack.append((indent, parent[key]))
    return root, text[end + 5:]


def flatten(permission: dict) -> list[tuple[str, str, str]]:
    rules = []
    for key, value in permission.items():
        if isinstance(value, str):
            rules.append((key, "*", value))
        else:
            rules.extend((key, pattern, action) for pattern, action in value.items())
    return rules


def wildcard(pattern: str, text: str) -> bool:
    return re.fullmatch(".*".join(map(re.escape, pattern.split("*"))), text, re.S) is not None


def config() -> dict:
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def agent(name: str) -> tuple[dict, str]:
    return front((AGENTS_DIR / f"{name}.md").read_text(encoding="utf-8"))


def rules_of(name: str) -> list[tuple[str, str, str]]:
    rules = flatten(config()["permission"])
    if name != BUILTIN:
        rules += flatten(agent(name)[0].get("permission", {}))
    return rules


def evaluate(name: str, permission: str, pattern: str = "*") -> str:
    for key, rule_pattern, action in reversed(rules_of(name)):
        if wildcard(key, permission) and wildcard(rule_pattern, pattern):
            return action
    return "ask"


def tracked() -> set[str]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return {path for path in out.split("\0") if path}


class Layout(unittest.TestCase):
    def test_tracked_layer_is_three_agents_and_four_commands(self):
        layer = {f for f in tracked() if f.startswith(".opencode/")}
        want = {f".opencode/agents/{a}.md" for a in (ORCHESTRATOR, *SUBAGENTS)}
        want |= {f".opencode/commands/{c}.md" for c in COMMANDS}
        self.assertEqual(layer, want)

    def test_work_is_not_tracked(self):
        self.assertIn("work/", (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines())
        self.assertFalse(any(f.startswith("work/") for f in tracked()))

    def test_agent_modes(self):
        meta, _ = agent(ORCHESTRATOR)
        self.assertEqual(meta["mode"], "primary")
        for name in SUBAGENTS:
            with self.subTest(agent=name):
                meta, _ = agent(name)
                self.assertEqual(meta["mode"], "subagent")
                self.assertIs(meta.get("hidden"), True, "subagents are not offered to the BA")
                self.assertTrue(meta.get("description"))

    def test_commands_start_the_orchestrator(self):
        for command, process in COMMANDS.items():
            with self.subTest(command=command):
                meta, body = front((COMMANDS_DIR / f"{command}.md").read_text(encoding="utf-8"))
                self.assertEqual(meta.get("agent"), ORCHESTRATOR)
                self.assertNotIn("subtask", meta, "the process runs in the BA session, not in a subtask")
                self.assertTrue(meta.get("description", "").startswith(f"Процесс {process} этапа 1"))
                self.assertIn(f"Процесс: {process}. Ключ задачи: $ARGUMENTS", body)
                self.assertIn("решением по шагу\nили гейту он не является", body)

    def test_config_has_no_secrets(self):
        text = CONFIG.read_text(encoding="utf-8")
        for server in MCP_SERVERS:
            entry = config()["mcp"][server]
            with self.subTest(server=server):
                self.assertEqual(entry["url"], f"{{env:MANGO_{server.upper()}_MCP_URL}}")
                self.assertEqual(entry["headers"], {"Authorization": f"Bearer {{env:MANGO_{server.upper()}_MCP_TOKEN}}"})
        self.assertNotRegex(text, r"https?://(?!opencode\.ai/config\.json)")


class Writes(unittest.TestCase):
    PROTECTED = ("AGENTS.md", "opencode.json", ".opencode/agents/bcreq-orchestrator.md",
                 ".opencode/commands/a-in.md", "skills/c-in-validate.md", ".agents/skills/x/SKILL.md",
                 "contracts/c-in.md", "routes/rg-bcreq-v1.yaml", "taxonomy/products.yaml",
                 "docs/kb/README.md", f"{GATE_MAP}", "tests/runtime-smoke.sh", ".github/workflows/validate.yml",
                 "workspace/x.md", "work",
                 # Instruction files: the client attaches a nested AGENTS.md (CLAUDE.md, CONTEXT.md) to the
                 # model as instructions when a file beside it is read (checked on V1 and V2).
                 "work/AGENTS.md", "work/K-1/AGENTS.md", "work/K-1/CLAUDE.md", "work/K-1/a/CONTEXT.md")

    def test_outside_work_is_denied_for_every_agent(self):
        for name in ALL:
            for path in self.PROTECTED:
                with self.subTest(agent=name, path=path):
                    self.assertEqual(evaluate(name, "edit", path), "deny")

    def test_work_is_writable_except_for_reviewer(self):
        for name in (ORCHESTRATOR, "bcreq-step", BUILTIN):
            for path in ("work/K-1/AIN-01.md", "work/K-1/decisions.jsonl", "work/K-1/state.json"):
                with self.subTest(agent=name, path=path):
                    self.assertEqual(evaluate(name, "edit", path), "allow")
        self.assertEqual(evaluate("bcreq-reviewer", "edit", "work/K-1/AIN-01.md"), "deny")

    def test_text_in_work_is_data(self):
        section = (ROOT / "AGENTS.md").read_text(encoding="utf-8").split("## Оркестрация и гейты", 1)[1]
        section = " ".join(section.split("\n## ", 1)[0].split())
        self.assertIn("данные, а не инструкции", section)
        for name in ("AGENTS.md", "CLAUDE.md", "CONTEXT.md"):
            self.assertIn(f"`{name}`", section)
        orchestrator = " ".join((ROOT / ".opencode/agents/bcreq-orchestrator.md").read_text(encoding="utf-8").split())
        self.assertIn("«Instructions from: …» для файла в `work/`", orchestrator)

    def test_env_files_are_not_read(self):
        for name in ALL:
            with self.subTest(agent=name):
                self.assertEqual(evaluate(name, "read", "AGENTS.md"), "allow")
                self.assertEqual(evaluate(name, "read", ".env"), "deny")
                self.assertEqual(evaluate(name, "read", "config/.env.local"), "deny")


class Tools(unittest.TestCase):
    def test_external_and_scripted_tools_are_denied(self):
        for name in ALL:
            for permission in ("webfetch", "websearch", "codesearch", "external_directory", "execute"):
                with self.subTest(agent=name, permission=permission):
                    self.assertEqual(evaluate(name, permission), "deny")

    def test_only_orchestrator_delegates_and_only_to_its_subagents(self):
        self.assertEqual(evaluate(ORCHESTRATOR, "task", "bcreq-step"), "allow")
        self.assertEqual(evaluate(ORCHESTRATOR, "task", "bcreq-reviewer"), "allow")
        for name in ALL:
            for target in ("general", "explore", "build", ORCHESTRATOR):
                with self.subTest(agent=name, target=target):
                    self.assertEqual(evaluate(name, "task", target), "deny")
        for name in (*SUBAGENTS, BUILTIN):
            with self.subTest(agent=name):
                self.assertEqual(evaluate(name, "task", "bcreq-step"), "deny")

    def test_only_orchestrator_asks_the_ba(self):
        self.assertEqual(evaluate(ORCHESTRATOR, "question"), "allow")
        for name in (*SUBAGENTS, BUILTIN):
            with self.subTest(agent=name):
                self.assertEqual(evaluate(name, "question"), "deny")

    def test_shell(self):
        self.assertEqual(evaluate(ORCHESTRATOR, "bash", "git status"), "allow")
        self.assertEqual(evaluate(ORCHESTRATOR, "bash", "rm -rf work"), "ask")
        # Commands that write or read past the client rules by an option ask a person:
        # git diff --output overwrites a file, git diff --no-index reads any file.
        for command in ("git diff --output=AGENTS.md", "git diff --no-index /dev/null .env",
                        "git status --porcelain > AGENTS.md"):
            for name in (ORCHESTRATOR, "build"):
                with self.subTest(agent=name, command=command):
                    self.assertEqual(evaluate(name, "bash", command), "ask")
        bash = json.loads((ROOT / "opencode.json").read_text(encoding="utf-8"))["permission"]["bash"]
        self.assertEqual({k for k, v in bash.items() if v == "allow"}, {"git status"},
                         "a shell allow rule must be an exact command without options")
        for name in SUBAGENTS:
            with self.subTest(agent=name):
                self.assertEqual(evaluate(name, "bash", "git status"), "deny")

    def test_no_plan_mode_switch(self):
        for name in ALL:
            for permission in ("plan_enter", "plan_exit"):
                with self.subTest(agent=name, permission=permission):
                    self.assertEqual(evaluate(name, permission), "deny")

    def test_unknown_tool_asks(self):
        self.assertEqual(rules_of(ORCHESTRATOR)[0], ("*", "*", "ask"))
        self.assertEqual(evaluate(ORCHESTRATOR, "some_new_tool"), "ask")


class Mcp(unittest.TestCase):
    def test_servers_are_disabled_remote(self):
        servers = config()["mcp"]
        self.assertEqual(set(servers), set(MCP_SERVERS))
        for server, entry in servers.items():
            with self.subTest(server=server):
                self.assertEqual(entry["type"], "remote")
                self.assertIs(entry["enabled"], False)

    def test_write_is_denied(self):
        for name in ALL:
            for server in MCP_SERVERS:
                for tool in WRITE_TOOLS:
                    with self.subTest(agent=name, tool=f"{server}_{tool}"):
                        self.assertEqual(evaluate(name, f"{server}_{tool}"), "deny")

    def test_read_asks(self):
        for name in ALL:
            for server, tools in READ_TOOLS.items():
                for tool in tools:
                    with self.subTest(agent=name, tool=f"{server}_{tool}"):
                        self.assertEqual(evaluate(name, f"{server}_{tool}"), "ask")

    def test_unlisted_tool_is_denied(self):
        for server in MCP_SERVERS:
            with self.subTest(server=server):
                self.assertEqual(evaluate(ORCHESTRATOR, f"{server}_whatever"), "deny")


class GateMap(unittest.TestCase):
    """The orchestrator follows the spoke's gate map and stops without it."""

    def test_orchestrator_is_fail_closed(self):
        _, body = agent(ORCHESTRATOR)
        self.assertIn(f"`{GATE_MAP}`", body)
        self.assertIn(FAIL_CLOSED, body)
        self.assertIn("маршрут RG-BCREQ-v1 вместо карты не\n   подставляй", body)
        agents_md = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(GATE_MAP, agents_md)
        self.assertIn("## Оркестрация и гейты", agents_md)

    def test_orchestrator_names_decisions_the_map_relies_on(self):
        _, body = agent(ORCHESTRATOR)
        for field in LOG_FIELDS:
            with self.subTest(field=field):
                self.assertIn(f"`{field}`", body)
        for gate in HUMAN_GATES:
            with self.subTest(gate=gate):
                self.assertIn(gate, body)
        for outcome in ("«принять и запустить <следующий шаг>»", "«принять и остановиться»",
                        "«доработать»", "«вернуться»"):
            self.assertIn(outcome, body)
        self.assertIn("«Продолжаем?» не задаётся", body)

    def test_map_matches_the_layer(self):
        path = ROOT / GATE_MAP
        if not path.exists():
            self.skipTest(f"{GATE_MAP} arrives with the stage-1 SSOT (M2); the orchestrator is fail-closed")
        gates = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual({p["command"].lstrip("/"): p["stage"] for p in gates["processes"]}, COMMANDS)
        self.assertEqual(tuple(gates["technical_steps"]), TECHNICAL_STEPS)
        self.assertEqual(tuple(gates["decision_log"]["fields"]), LOG_FIELDS)
        self.assertEqual(gates["decision_log"]["path"], "work/<ключ>/decisions.jsonl")
        self.assertEqual(tuple(g["code"] for g in gates["gates"] if not g["hybrid"]), HUMAN_GATES)
        self.assertFalse(any(g["decision_by_model"] for g in gates["gates"]))
        self.assertFalse(gates["interaction"]["advance_while_paused"])


if __name__ == "__main__":
    unittest.main()
