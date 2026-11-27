"""OpenCode initialisation smoke for this repository (RFC-RT-002, Э4; BL-192).

Checks, without a model run of the route, that an OpenCode client started in
this repository

1. (V1) lists exactly the 11 route skills in `opencode debug skill`, each
   found in the mirror .agents/skills/<name>/SKILL.md;
2. (V1, V2) sends AGENTS.md to the model in full as project instructions and
   offers it the 11 skills with the descriptions of skills/<name>.md;
3. (control) offers none of them in a copy of AGENTS.md and skills/ without
   the mirror: discovery comes from the mirror, not from the flat layout;
4. (V1, V2) loads the IDE layer of the stage-1 processes (BL-192 Э5): the
   three agents with their modes, the four commands bound to the orchestrator
   (V1), the effective permissions the client computes for each agent, and,
   in a copy of the repository, writes the model asks for: AGENTS.md is
   refused, also through work/<key>/../../, and work/<key>/ is written.

Steps 2 and 4 need a model request. The script starts a local mock of an
OpenAI-compatible endpoint, records the request and answers «ok» (in step 4 it first asks for two writes): no real model
is called and no key is used. OpenCode runs with an isolated HOME and XDG
directories, so the user's global config, skills and sessions are not read.
The provider package @ai-sdk/openai-compatible is installed by OpenCode itself
on first use (network access to the npm registry).

    npm install --prefix /tmp/oc opencode-ai@1.19.6        # line V1
    npm install --prefix /tmp/oc2 @opencode/cli@2.4.2      # line V2
    python3 tests/opencode_smoke.py --opencode /tmp/oc/node_modules/.bin/opencode

The OpenCode version is chosen by the caller; pinning it is BL-132 of
G-Ivan-A/mango_ba_prompts. Exit code 0 means every check passed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

import agent_context_audit as audit  # noqa: E402

PROMPT = "перечисли навыки"
AGENTS_TITLE = "# AGENTS.md: системный промпт исполнения маршрута RG-BCREQ-v1"

# IDE layer (BL-192 Э5): agent -> (mode, hidden); command -> process.
LAYER_AGENTS = {"bcreq-orchestrator": ("primary", False), "bcreq-step": ("subagent", True),
                "bcreq-reviewer": ("subagent", True)}
LAYER_COMMANDS = {"a-in": "A-IN", "a-core": "A-CORE", "a-work": "A-WORK", "a-release": "A-RELEASE"}
ORCHESTRATOR_TITLE = "# Оркестратор процессов этапа 1"
PROBE_KEY = "SMOKE-1"
# A protected file, the same file through work/ (the client resolves the path), a file in work/.
PROBE_WRITES = ("AGENTS.md", f"work/{PROBE_KEY}/../../AGENTS.md", f"work/{PROBE_KEY}/probe.md")
# V2 renames permissions when it translates the V1 `permission` object.
V2_NAMES = {"bash": "shell", "task": "subagent"}


def expected_decisions() -> list[tuple[str, str, str, str]]:
    """(agent, permission, pattern, action) the IDE layer must produce in the client."""
    rows = []
    for agent in (*LAYER_AGENTS, "build"):
        orchestrator, reviewer = agent == "bcreq-orchestrator", agent == "bcreq-reviewer"
        rows += [
            (agent, "edit", "AGENTS.md", "deny"),
            (agent, "edit", ".opencode/agents/bcreq-orchestrator.md", "deny"),
            (agent, "edit", "ssot/mango_ba_prompts/docs/ba-processes/bcreq-ide-gates.json", "deny"),
            (agent, "edit", f"work/{PROBE_KEY}/AIN-01.md", "deny" if reviewer else "allow"),
            (agent, "read", ".env", "deny"),
            (agent, "webfetch", "*", "deny"),
            (agent, "websearch", "*", "deny"),
            (agent, "external_directory", "/etc/hosts", "deny"),
            (agent, "execute", "*", "deny"),
            (agent, "task", "general", "deny"),
            (agent, "task", "bcreq-step", "allow" if orchestrator else "deny"),
            (agent, "question", "*", "allow" if orchestrator else "deny"),
            (agent, "jira_create_issue", "*", "deny"),
            (agent, "confluence_update_page", "*", "deny"),
            (agent, "jira_get_issue", "*", "ask"),
        ]
        if agent in ("bcreq-step", "bcreq-reviewer"):
            rows.append((agent, "bash", "git status", "deny"))
        if orchestrator:
            rows += [(agent, "bash", "git status", "allow"), (agent, "bash", "rm -rf work", "ask")]
    return rows


def wildcard(pattern: str, text: str) -> bool:
    """OpenCode wildcard: `*` is any text (including `/`), `?` one character."""
    regex = "".join(".*" if c == "*" else "." if c == "?" else re.escape(c) for c in pattern)
    return re.fullmatch(regex, text, re.S) is not None


def decide(rules: list[tuple[str, str, str]], permission: str, pattern: str) -> str:
    """Last matching (permission, pattern, action) rule wins; no match is ask."""
    for rule_permission, rule_pattern, action in reversed(rules):
        if wildcard(rule_permission, permission) and wildcard(rule_pattern, pattern):
            return action
    return "ask"


def client_rules(entries: list[dict]) -> list[tuple[str, str, str]]:
    """Rules as the client prints them: V1 {permission, pattern, action}, V2 {action, resource, effect}."""
    if entries and "effect" in entries[0]:
        return [(e["action"], e["resource"], e["effect"]) for e in entries]
    return [(e["permission"], e["pattern"], e["action"]) for e in entries]


def route_skills() -> dict[str, str]:
    """Skill name -> normalised description from skills/<name>.md."""
    skills = {}
    for path in sorted((ROOT / "skills").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        skills[audit.frontmatter(text)["name"]] = " ".join(audit.block_value(text, "description").split())
    return skills


class MockModel(BaseHTTPRequestHandler):
    """Minimal OpenAI-compatible chat completions endpoint that records requests."""

    requests: list[dict] = []
    # Step 4: absolute paths the model asks to write before it answers.
    writes: tuple[str, ...] = ()

    def log_message(self, *args):
        pass

    def _send(self, status: int, ctype: str, body: bytes):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send(200, "application/json", json.dumps({"object": "list", "data": [{"id": "m", "object": "model"}]}).encode())

    def do_POST(self):
        raw = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        request = json.loads(raw or b"{}")
        MockModel.requests.append(request)
        base = {"id": "smoke", "created": int(time.time()), "model": "m"}
        usage = {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}
        tools = {t.get("function", {}).get("name"): t.get("function", {}) for t in request.get("tools", [])}
        answered = any(m.get("role") == "tool" for m in request.get("messages", []))
        if MockModel.writes and request.get("stream") and "write" in tools and not answered:
            self._send(200, "text/event-stream", write_calls(base, tools["write"], MockModel.writes, usage))
        elif request.get("stream"):
            chunks = [
                {**base, "object": "chat.completion.chunk",
                 "choices": [{"index": 0, "delta": {"role": "assistant", "content": "ok"}, "finish_reason": None}]},
                {**base, "object": "chat.completion.chunk",
                 "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]},
                {**base, "object": "chat.completion.chunk", "choices": [], "usage": usage},
            ]
            body = b"".join(b"data: " + json.dumps(c).encode() + b"\n\n" for c in chunks) + b"data: [DONE]\n\n"
            self._send(200, "text/event-stream", body)
        else:
            self._send(200, "application/json", json.dumps({
                **base, "object": "chat.completion", "usage": usage,
                "choices": [{"index": 0, "message": {"role": "assistant", "content": "ok"}, "finish_reason": "stop"}],
            }).encode())


def write_calls(base: dict, write_tool: dict, paths: tuple[str, ...], usage: dict) -> bytes:
    """A streamed answer that calls the client's write tool once per path."""
    properties = write_tool.get("parameters", {}).get("properties", {})
    key = "filePath" if "filePath" in properties else "path"  # V1 filePath, V2 path
    calls = [{"index": i, "id": f"call_{i}", "type": "function",
              "function": {"name": "write", "arguments": json.dumps({key: path, "content": "probe\n"})}}
             for i, path in enumerate(paths)]
    chunks = [
        {**base, "object": "chat.completion.chunk",
         "choices": [{"index": 0, "delta": {"role": "assistant", "tool_calls": calls}, "finish_reason": None}]},
        {**base, "object": "chat.completion.chunk", "choices": [{"index": 0, "delta": {}, "finish_reason": "tool_calls"}]},
        {**base, "object": "chat.completion.chunk", "choices": [], "usage": usage},
    ]
    return b"".join(b"data: " + json.dumps(c).encode() + b"\n\n" for c in chunks) + b"data: [DONE]\n\n"


def isolated_env(home: Path, port: int) -> dict[str, str]:
    config = home / ".config" / "opencode"
    config.mkdir(parents=True)
    (config / "opencode.json").write_text(json.dumps({
        "$schema": "https://opencode.ai/config.json",
        "autoupdate": False,
        "share": "disabled",
        "provider": {"smoke": {
            "npm": "@ai-sdk/openai-compatible",
            "name": "smoke",
            "options": {"baseURL": f"http://127.0.0.1:{port}/v1", "apiKey": "smoke"},
            "models": {"m": {"name": "m"}},
        }},
        "model": "smoke/m",
        "small_model": "smoke/m",
    }, indent=2), encoding="utf-8")
    env = {k: v for k, v in os.environ.items() if not k.startswith(("OPENCODE", "XDG_"))}
    env.update({
        "HOME": str(home),
        "XDG_CONFIG_HOME": str(home / ".config"),
        "XDG_DATA_HOME": str(home / ".local" / "share"),
        "XDG_CACHE_HOME": str(home / ".cache"),
        "XDG_STATE_HOME": str(home / ".local" / "state"),
        "OPENCODE_DISABLE_AUTOUPDATE": "1",
    })
    return env


def text_of(request: dict) -> str:
    return json.dumps(request, ensure_ascii=False)


def system_of(request: dict) -> str:
    parts = []
    for message in request.get("messages", []):
        if message.get("role") == "system":
            content = message.get("content")
            parts.append(content if isinstance(content, str) else json.dumps(content, ensure_ascii=False))
    return "\n".join(parts)


SKILL_BLOCK = re.compile(r"<skill>(.*?)</skill>", re.S)


def offered_skills(request: dict) -> dict[str, tuple[str, str]]:
    """Skills the client offers the model: name -> (description, location or "")."""
    text = ""
    for message in request.get("messages", []):
        content = message.get("content")
        text += (content if isinstance(content, str) else json.dumps(content, ensure_ascii=False)) + "\n"
    for tool in request.get("tools", []):
        text += str(tool.get("function", {}).get("description", "")) + "\n"
    skills = {}
    for block in SKILL_BLOCK.findall(text):
        field = lambda tag: (re.search(rf"<{tag}>(.*?)</{tag}>", block, re.S) or [None, ""])[1]
        # V2 names a skill by <id> (and a display <name>); V1 only by <name>.
        key = field("id").strip() or field("name").strip()
        skills[key] = (" ".join(field("description").split()), field("location").strip())
    return skills


def run_client(opencode: str, major: int, cwd: Path, env: dict, timeout: int) -> tuple[subprocess.CompletedProcess, dict]:
    """One prompt through the client; returns the process and the recorded main request."""
    MockModel.requests.clear()
    if major >= 2:
        cmd = [opencode, "run", "--standalone", "--archived", "-m", "smoke/m", PROMPT]
    else:
        cmd = [opencode, "run", "--pure", "-m", "smoke/m", PROMPT]
    # V2 takes the project directory from $PWD, not from the process cwd.
    proc = subprocess.run(cmd, cwd=cwd, env={**env, "PWD": str(cwd)}, capture_output=True, text=True,
                          stdin=subprocess.DEVNULL, timeout=timeout)
    main = [r for r in MockModel.requests if PROMPT in text_of(r) and r.get("tools")]
    return proc, (main[-1] if main else {})


def control_project(base: Path) -> Path:
    """AGENTS.md and the flat skills/ without the mirror: what clients saw before Э1."""
    project = base / "control"
    (project / "skills").mkdir(parents=True)
    (project / "AGENTS.md").write_bytes((ROOT / "AGENTS.md").read_bytes())
    for path in (ROOT / "skills").glob("*.md"):
        (project / "skills" / path.name).write_bytes(path.read_bytes())
    subprocess.run(["git", "init", "-q", str(project)], check=True)
    return project


def layer_project(base: Path) -> Path:
    """A copy of the repository files (no work/) for the write probe of step 4."""
    project = base / "layer"
    listed = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT,
                            capture_output=True, text=True, check=True).stdout
    for rel in filter(None, listed.split("\0")):
        source = ROOT / rel
        if source.is_file() and not rel.startswith("work/"):
            (project / rel).parent.mkdir(parents=True, exist_ok=True)
            (project / rel).write_bytes(source.read_bytes())
    subprocess.run(["git", "init", "-q", str(project)], check=True)
    return project


def debug_json(opencode: str, args: list[str], env: dict, timeout: int):
    proc = subprocess.run([opencode, "debug", *args], cwd=ROOT, env={**env, "PWD": str(ROOT)},
                          capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=timeout)
    try:
        return json.loads(proc.stdout), ""
    except json.JSONDecodeError:
        return None, (proc.stderr or proc.stdout)[-500:]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="OpenCode initialisation smoke (RFC-RT-002, Э4)")
    parser.add_argument("--opencode", required=True, help="path to the opencode executable (V1 or V2)")
    parser.add_argument("--timeout", type=int, default=240, help="seconds per opencode call")
    parser.add_argument("--no-control", action="store_true", help="skip the control run without the mirror")
    parser.add_argument("--no-layer", action="store_true", help="skip the IDE layer checks (step 4)")
    args = parser.parse_args(argv)

    want = route_skills()
    failures = 0

    def check(ok: bool, label: str, detail: str = "") -> None:
        nonlocal failures
        print(f"{'ok' if ok else 'not ok'} - {label}" + (f": {detail}" if detail and not ok else ""))
        failures += 0 if ok else 1

    version = subprocess.run([args.opencode, "--version"], capture_output=True, text=True, timeout=args.timeout)
    version_text = (version.stdout or version.stderr).strip()
    found = re.search(r"(\d+)\.\d+\.\d+", version_text)
    major = int(found[1]) if found else 1
    print(f"# opencode {version_text} (line V{major})")

    server = ThreadingHTTPServer(("127.0.0.1", 0), MockModel)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    home = Path(tempfile.mkdtemp(prefix="opencode-smoke-"))
    env = isolated_env(home, server.server_address[1])
    try:
        # 1. V1 only: the client's own skill list, with file locations.
        if major < 2:
            listed = subprocess.run([args.opencode, "debug", "skill", "--pure"], cwd=ROOT, env=env,
                                    capture_output=True, text=True, timeout=args.timeout)
            try:
                entries = json.loads(listed.stdout)
            except json.JSONDecodeError:
                entries = None
            check(listed.returncode == 0 and isinstance(entries, list), "opencode debug skill returns a list",
                  (listed.stderr or listed.stdout)[-500:])
            project = {e.get("name"): str(e.get("location", "")) for e in entries or []
                       if str(e.get("location", "")).startswith(str(ROOT))}
            check(set(project) == set(want), f"debug skill lists the {len(want)} route skills", f"{sorted(project)}")
            for name in want:
                location = project.get(name, "")
                rel = Path(location).relative_to(ROOT).as_posix() if location else ""
                check(rel == f".agents/skills/{name}/SKILL.md", f"debug skill finds {name} in the mirror", rel)

        # 2. AGENTS.md reaches the model as instructions, the 11 skills are offered.
        proc, request = run_client(args.opencode, major, ROOT, env, args.timeout)
        check(proc.returncode == 0 and bool(request), "opencode run reaches the mock model",
              (proc.stderr or proc.stdout)[-500:])
        system = system_of(request)
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        check(f"Instructions from: {ROOT / 'AGENTS.md'}" in system, "AGENTS.md is loaded as project instructions")
        body = agents.split("\n---\n", 1)[-1].strip()
        check(AGENTS_TITLE in system and body in system, "AGENTS.md reaches the model in full",
              f"{len(system)} bytes of system prompt")
        offered = offered_skills(request)
        for name, description in want.items():
            got_description, location = offered.get(name, ("", ""))
            check(name in offered, f"skill {name} is offered to the model")
            check(got_description == description, f"skill {name} keeps its description")
            if location:
                rel = Path(location).relative_to(ROOT).as_posix() if location.startswith(str(ROOT)) else location
                check(rel == f".agents/skills/{name}/SKILL.md", f"skill {name} is read from the mirror", rel)
        foreign = [n for n, (_, loc) in offered.items() if n not in want and loc.startswith(str(ROOT))]
        check(not foreign, "no other project skills are offered", f"{foreign}")

        # 3. Control: without the mirror the client offers none of the route skills.
        if not args.no_control:
            _, request = run_client(args.opencode, major, control_project(home), env, args.timeout)
            seen = sorted(set(want) & set(offered_skills(request)))
            check(bool(request) and not seen, "control without the mirror offers no route skills", f"{seen}")

        # 4. IDE layer of the stage-1 processes (BL-192 Э5).
        if not args.no_layer:
            rules = {}
            if major < 2:
                config, error = debug_json(args.opencode, ["config", "--pure"], env, args.timeout)
                commands = (config or {}).get("command") or {}
                check(set(LAYER_AGENTS) <= set((config or {}).get("agent") or {}),
                      "debug config has the three layer agents", error)
                for command, process in LAYER_COMMANDS.items():
                    entry = commands.get(command) or {}
                    check(entry.get("agent") == "bcreq-orchestrator", f"/{command} starts bcreq-orchestrator", f"{entry}")
                    check(f"Процесс: {process}. Ключ задачи: $ARGUMENTS" in entry.get("template", ""),
                          f"/{command} passes {process} and the task key")
                for name in (*LAYER_AGENTS, "build"):
                    agent, error = debug_json(args.opencode, ["agent", name, "--pure"], env, args.timeout)
                    agent = agent or {}
                    if name in LAYER_AGENTS:
                        check(agent.get("mode") == LAYER_AGENTS[name][0], f"agent {name} is {LAYER_AGENTS[name][0]}",
                              error or f"{agent.get('mode')}")
                    rules[name] = client_rules(agent.get("permission") or [])
            else:
                # V2 has no command list to print; its loader is checked by the TUI test runs (M6).
                agents, error = debug_json(args.opencode, ["agents", "--standalone"], env, args.timeout)
                by_id = {a.get("id"): a for a in agents or []}
                for name, (mode, hidden) in LAYER_AGENTS.items():
                    agent = by_id.get(name) or {}
                    check((agent.get("mode"), bool(agent.get("hidden"))) == (mode, hidden),
                          f"agent {name} is {mode}{', hidden' if hidden else ''}",
                          error or f"{agent.get('mode')}, hidden={agent.get('hidden')}")
                for name in (*LAYER_AGENTS, "build"):
                    rules[name] = client_rules((by_id.get(name) or {}).get("permissions") or [])
            for agent, permission, pattern, action in expected_decisions():
                name = V2_NAMES.get(permission, permission) if major >= 2 else permission
                got = decide(rules.get(agent, []), name, pattern)
                check(got == action, f"{agent}: {name} {pattern} is {action}", got)

            project = layer_project(home)
            before = (project / "AGENTS.md").read_bytes()
            MockModel.requests.clear()
            MockModel.writes = tuple(str(project / rel) for rel in PROBE_WRITES)
            if major >= 2:
                cmd = [args.opencode, "run", "--standalone", "--archived", "-m", "smoke/m",
                       "--agent", "bcreq-orchestrator", PROBE_KEY]
            else:
                cmd = [args.opencode, "run", "--pure", "-m", "smoke/m", "--command", "a-in", PROBE_KEY]
            try:
                proc = subprocess.run(cmd, cwd=project, env={**env, "PWD": str(project)}, capture_output=True,
                                      text=True, stdin=subprocess.DEVNULL, timeout=args.timeout)
            finally:
                MockModel.writes = ()
            sent = [r for r in MockModel.requests if r.get("tools")]
            check(proc.returncode == 0 and bool(sent), "the orchestrator run reaches the mock model",
                  (proc.stderr or proc.stdout)[-500:])
            check(any(ORCHESTRATOR_TITLE in system_of(r) for r in sent), "the model gets the orchestrator prompt")
            if major < 2:
                check(any(f"Процесс: A-IN. Ключ задачи: {PROBE_KEY}" in text_of(r) for r in sent),
                      "/a-in passes the process and the key to the model")
            results = [m for r in sent for m in r.get("messages", []) if m.get("role") == "tool"]
            check(len(results) >= len(PROBE_WRITES), "the client answers every write call", f"{len(results)}")
            check((project / "AGENTS.md").read_bytes() == before,
                  f"writes to AGENTS.md and {PROBE_WRITES[1]} are refused")
            written = project / PROBE_WRITES[-1]
            check(written.is_file() and written.read_text(encoding="utf-8") == "probe\n",
                  f"a write to {PROBE_WRITES[-1]} is done")
            check(sorted(p.relative_to(project).as_posix() for p in (project / "work").rglob("*") if p.is_file())
                  == [PROBE_WRITES[-1]], "nothing else is written to work/")
    finally:
        server.shutdown()
        subprocess.run(["rm", "-rf", str(home)], check=False)

    print(f"# {'passed' if failures == 0 else f'failed: {failures} check(s)'}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
