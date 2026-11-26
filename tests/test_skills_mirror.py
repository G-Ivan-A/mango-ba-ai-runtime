"""Guard of the skills mirror .agents/skills/<name>/SKILL.md (RFC-RT-002, Р-RT-3 B, BL-192 Э1).

skills/<name>.md stays the only source. The mirror must hold exactly one
SKILL.md per skill, byte-for-byte equal by sha256, and nothing else. Fix a
failure with `python3 tests/build_skills_mirror.py`, never by editing the mirror.
"""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

import build_skills_mirror as mirror  # noqa: E402


def tracked() -> set[str]:
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return {path for path in out.split("\0") if path}


class MirrorInSync(unittest.TestCase):
    def test_eleven_skills_mirrored(self):
        want = mirror.expected()
        self.assertEqual(len(want), 11)
        for path in want:
            with self.subTest(path=path):
                self.assertRegex(path, r"^\.agents/skills/[a-z0-9]+(-[a-z0-9]+)*/SKILL\.md$")

    def test_sha256_equals_source(self):
        for path, data in mirror.expected().items():
            source = ROOT / "skills" / f"{Path(path).parent.name}.md"
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), f"{path} is missing")
                self.assertEqual(mirror.sha256((ROOT / path).read_bytes()), mirror.sha256(source.read_bytes()))

    def test_no_drift(self):
        self.assertEqual(mirror.drift(), [])

    def test_mirror_is_tracked_and_only_mirror(self):
        under = {f for f in tracked() if f.startswith(".agents/")}
        self.assertEqual(under, set(mirror.expected()))

    def test_directory_equals_name(self):
        for path in mirror.expected():
            text = (ROOT / path).read_text(encoding="utf-8")
            with self.subTest(path=path):
                self.assertIn(f"\nname: {Path(path).parent.name}\n", text)


class MirrorGuardCatchesDrift(unittest.TestCase):
    """Mutations: the guard must notice each way the mirror can drift."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(ROOT / "skills", self.tmp / "skills")
        mirror.build(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_build_is_clean(self):
        self.assertEqual(mirror.drift(self.tmp), [])
        self.assertEqual(mirror.build(self.tmp), [])

    def test_hand_edit(self):
        path = self.tmp / next(iter(mirror.expected(self.tmp)))
        path.write_bytes(path.read_bytes() + b"\n")
        self.assertTrue(any(p.startswith("sha256 ") for p in mirror.drift(self.tmp)))

    def test_source_edit_without_rebuild(self):
        src = sorted((self.tmp / "skills").glob("*.md"))[0]
        src.write_bytes(src.read_bytes().replace(b"\n", b"\r\n"))
        self.assertTrue(any(p.startswith("sha256 ") for p in mirror.drift(self.tmp)))

    def test_missing_and_extra(self):
        first = self.tmp / sorted(mirror.expected(self.tmp))[0]
        first.unlink()
        (self.tmp / ".agents/skills/foreign").mkdir()
        (self.tmp / ".agents/skills/foreign/SKILL.md").write_text("---\nname: foreign\n---\n")
        problems = mirror.drift(self.tmp)
        self.assertTrue(any(p.startswith("missing ") for p in problems))
        self.assertTrue(any(p.startswith("extra ") for p in problems))
        mirror.build(self.tmp)
        self.assertEqual(mirror.drift(self.tmp), [])
        self.assertFalse((self.tmp / ".agents/skills/foreign").exists())

    def test_symlink(self):
        path = self.tmp / sorted(mirror.expected(self.tmp))[0]
        source = self.tmp / "skills" / f"{path.parent.name}.md"
        path.unlink()
        path.symlink_to(source)
        self.assertTrue(any(p.startswith("symlink ") for p in mirror.drift(self.tmp)))


if __name__ == "__main__":
    unittest.main()
