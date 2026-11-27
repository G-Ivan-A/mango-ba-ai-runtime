"""Offline checks of tests/opencode_smoke.py (RFC-RT-002, Э4; BL-192).

The smoke itself needs an OpenCode binary and runs in CI (job opencode). These
tests pin how it reads the model request, so that a change in the client's
prompt shape fails here and not silently there.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

import opencode_smoke as smoke  # noqa: E402

V1_SYSTEM = """Skills provide specialized instructions.
<available_skills>
  <skill>
    <name>alpha-skill</name>
    <description>Используй,
      когда нужно.</description>
    <location>/repo/.agents/skills/alpha-skill/SKILL.md</location>
  </skill>
</available_skills>"""

V2_SYSTEM = """<available_skills>
  <skill>
    <id>alpha-skill</id>
    <name>Alpha</name>
    <description>Используй, когда нужно.</description>
  </skill>
</available_skills>
Instructions from: /repo/AGENTS.md"""


class OfferedSkills(unittest.TestCase):
    def test_v1_name_and_location(self):
        request = {"messages": [{"role": "system", "content": V1_SYSTEM}], "tools": [{}]}
        self.assertEqual(smoke.offered_skills(request), {
            "alpha-skill": ("Используй, когда нужно.", "/repo/.agents/skills/alpha-skill/SKILL.md")})

    def test_v2_id_wins_over_display_name(self):
        request = {"messages": [{"role": "system", "content": [{"type": "text", "text": V2_SYSTEM}]}]}
        self.assertEqual(smoke.offered_skills(request), {"alpha-skill": ("Используй, когда нужно.", "")})

    def test_skills_in_tool_description(self):
        request = {"messages": [], "tools": [{"function": {"name": "skill", "description": V1_SYSTEM}}]}
        self.assertIn("alpha-skill", smoke.offered_skills(request))

    def test_no_skills(self):
        self.assertEqual(smoke.offered_skills({"messages": [{"role": "user", "content": "x"}]}), {})


class RouteSkills(unittest.TestCase):
    def test_eleven_with_descriptions(self):
        skills = smoke.route_skills()
        self.assertEqual(sorted(skills), sorted(p.stem for p in (ROOT / "skills").glob("*.md")))
        self.assertEqual(len(skills), 11)
        for name, description in skills.items():
            with self.subTest(name=name):
                self.assertTrue(description.startswith("Используй"), description)


class IsolatedEnv(unittest.TestCase):
    def test_user_config_is_not_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = smoke.isolated_env(Path(tmp) / "home", 4242)
            self.assertEqual(env["HOME"], str(Path(tmp) / "home"))
            self.assertTrue(env["XDG_CONFIG_HOME"].startswith(env["HOME"]))
            config = (Path(tmp) / "home/.config/opencode/opencode.json").read_text(encoding="utf-8")
            self.assertIn('"baseURL": "http://127.0.0.1:4242/v1"', config)
            self.assertIn('"model": "smoke/m"', config)


class Permissions(unittest.TestCase):
    def test_wildcard(self):
        self.assertTrue(smoke.wildcard("work/**", "work/K-1/AIN-01.md"))
        self.assertTrue(smoke.wildcard("*", "a/b"))
        self.assertTrue(smoke.wildcard("jira_*get*", "jira_get_issue"))
        self.assertFalse(smoke.wildcard("work/**", "AGENTS.md"))
        self.assertFalse(smoke.wildcard("git diff*", "git status"))
        self.assertTrue(smoke.wildcard("a.b", "a.b"))
        self.assertFalse(smoke.wildcard("a.b", "axb"))

    def test_last_match_wins_and_default_is_ask(self):
        rules = [("*", "*", "allow"), ("edit", "*", "deny"), ("edit", "work/**", "allow")]
        self.assertEqual(smoke.decide(rules, "edit", "work/x.md"), "allow")
        self.assertEqual(smoke.decide(rules, "edit", "AGENTS.md"), "deny")
        self.assertEqual(smoke.decide(rules, "read", "x"), "allow")
        self.assertEqual(smoke.decide([], "read", "x"), "ask")

    def test_client_rules_v1_and_v2(self):
        self.assertEqual(smoke.client_rules([{"permission": "edit", "pattern": "*", "action": "deny"}]),
                         [("edit", "*", "deny")])
        self.assertEqual(smoke.client_rules([{"action": "shell", "resource": "git status", "effect": "allow"}]),
                         [("shell", "git status", "allow")])
        self.assertEqual(smoke.client_rules([]), [])

    def test_expected_decisions_follow_the_config(self):
        """What the smoke expects from the client is what the layer files say (tests/test_ide_layer.py)."""
        import test_ide_layer as layer
        for agent, permission, pattern, action in smoke.expected_decisions():
            with self.subTest(agent=agent, permission=permission, pattern=pattern):
                self.assertEqual(layer.evaluate(agent, permission, pattern), action)

    def test_expected_decisions_cover_every_agent(self):
        agents = {row[0] for row in smoke.expected_decisions()}
        self.assertEqual(agents, {*smoke.LAYER_AGENTS, "build"})


class WriteProbe(unittest.TestCase):
    def chunks(self, properties):
        body = smoke.write_calls({"id": "x"}, {"parameters": {"properties": properties}},
                                 ("/p/AGENTS.md", "/p/work/K/probe.md"), {})
        lines = [line[6:] for line in body.decode().split("\n\n") if line.startswith("data: {")]
        return [json.loads(line) for line in lines]

    def test_v1_file_path_key(self):
        calls = self.chunks({"filePath": {}, "content": {}})[0]["choices"][0]["delta"]["tool_calls"]
        self.assertEqual([json.loads(c["function"]["arguments"])["filePath"] for c in calls],
                         ["/p/AGENTS.md", "/p/work/K/probe.md"])
        self.assertEqual({c["function"]["name"] for c in calls}, {"write"})

    def test_v2_path_key_and_finish_reason(self):
        chunks = self.chunks({"path": {}, "content": {}})
        self.assertIn("path", json.loads(chunks[0]["choices"][0]["delta"]["tool_calls"][0]["function"]["arguments"]))
        self.assertEqual(chunks[1]["choices"][0]["finish_reason"], "tool_calls")

    def test_layer_project_has_no_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = smoke.layer_project(Path(tmp))
            self.assertTrue((project / "opencode.json").is_file())
            self.assertTrue((project / ".opencode/agents/bcreq-orchestrator.md").is_file())
            self.assertFalse((project / "work").exists())


if __name__ == "__main__":
    unittest.main()
