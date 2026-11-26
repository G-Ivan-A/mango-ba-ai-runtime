"""Offline checks of tests/opencode_smoke.py (RFC-RT-002, Э4; BL-192).

The smoke itself needs an OpenCode binary and runs in CI (job opencode). These
tests pin how it reads the model request, so that a change in the client's
prompt shape fails here and not silently there.
"""

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


if __name__ == "__main__":
    unittest.main()
