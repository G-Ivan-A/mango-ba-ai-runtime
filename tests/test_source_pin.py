"""Checks that compilation provenance pins the model source repository, not the Hub.

Ш3.5 (Hub backlog B-248): the meta-model source moved from the Hub to
ba-ai-metamodel with history. The package keeps one source address in
compilation-manifest.yaml and one commit per skill in compiled_from.
"""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SSOT = "https://github.com/G-Ivan-A/ba-ai-metamodel"
SHA = re.compile(r"^[0-9a-f]{40}$")


class SourcePinTest(unittest.TestCase):
    def test_manifest_pins_source_repository_commit(self):
        text = (ROOT / "compilation-manifest.yaml").read_text(encoding="utf-8")
        keys = dict(
            re.findall(r"^(source_ssot|source_commit|hub_ssot|hub_commit):\s*(\S+)", text, re.M)
        )
        self.assertEqual(keys.get("source_ssot"), SOURCE_SSOT)
        self.assertRegex(keys.get("source_commit", ""), SHA)
        self.assertNotIn("hub_ssot", keys)
        self.assertNotIn("hub_commit", keys)
        self.assertIn("recompilation: смена source_commit", text)

    def test_every_skill_pins_source_commit(self):
        skills = sorted((ROOT / "skills").glob("*.md"))
        self.assertTrue(skills)
        for skill in skills:
            with self.subTest(skill=skill.name):
                text = skill.read_text(encoding="utf-8")
                match = re.search(r"^compiled_from: \{ source_commit: (\S+?),", text, re.M)
                self.assertIsNotNone(match, "compiled_from must start with source_commit")
                self.assertRegex(match.group(1), SHA)
                self.assertNotIn("hub_commit", text)


if __name__ == "__main__":
    unittest.main()
