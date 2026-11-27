"""The copier tests/build_ssot_transfer.py is fail-closed and repeatable (RFC-RT-003 §12.7).

No network and no access to the private spoke: a local git repository is
built from the copy in ssot/ as a stand-in for the spoke, the manifest and
link map are re-pinned to its commit, and the journal of a temporary runtime
root pins them. Then:

* a clean transfer is installed, and a second run changes no byte (НФТ-5);
* one changed byte at source_commit refuses the whole transfer, ssot/ of
  the runtime root stays as it was (НФТ-2);
* a manifest the journal does not pin is refused before any byte is copied.
"""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_ssot_transfer as build  # noqa: E402
from test_ssot_transfer import (COPY_DIR, JOURNAL, LINK_MAP_COPY, MANIFEST_COPY, ORCHESTRATOR, ROOT,
                                SSOT, sha256)  # noqa: E402

GIT = ["git", "-c", "user.name=ssot-test", "-c", "user.email=ssot-test@example.invalid",
       "-c", "commit.gpgsign=false", "-c", "core.autocrlf=false"]


def tree_bytes(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


class Copier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="ssot-build-")
        cls.base = Path(cls.tmp.name)
        cls.manifest = json.loads((ROOT / MANIFEST_COPY).read_bytes())
        cls.link_map_text = (ROOT / LINK_MAP_COPY).read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def spoke(self, name: str, change: str | None = None) -> tuple[Path, str]:
        """A stand-in spoke: the artifacts at one commit, the re-pinned manifest and link map on top."""
        repo = self.base / name
        shutil.copytree(ROOT / COPY_DIR, repo)
        if change:
            path = repo / change
            path.write_bytes(path.read_bytes() + b" ")
        run = lambda *args: subprocess.run([*GIT, "-C", str(repo), *args], check=True,  # noqa: E731
                                           capture_output=True, text=True).stdout.strip()
        run("init", "-q")
        run("add", "-A")
        run("commit", "-q", "-m", "artifacts")
        commit = run("rev-parse", "HEAD")
        old = self.manifest["source_commit"]
        m = json.loads(json.dumps(self.manifest).replace(old, commit))
        contracts = repo / "docs/contracts"
        contracts.mkdir(parents=True, exist_ok=True)
        (contracts / "ssot-stage1-handoff-manifest.json").write_text(
            json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (contracts / "ssot-stage1-link-map.json").write_text(self.link_map_text.replace(old, commit),
                                                             encoding="utf-8")
        run("add", "-A")
        run("commit", "-q", "-m", "manifest")
        return repo, commit

    def runtime(self, name: str, repo: Path, commit: str) -> Path:
        """A runtime root whose journal pins the manifest and link map of the stand-in spoke."""
        root = self.base / name
        (root / SSOT).mkdir(parents=True)
        (root / ORCHESTRATOR).parent.mkdir(parents=True)
        shutil.copyfile(ROOT / ORCHESTRATOR, root / ORCHESTRATOR)
        journal = (ROOT / JOURNAL).read_text(encoding="utf-8")
        contracts = repo / "docs/contracts"
        for old, new in ((self.manifest["source_commit"], commit),
                         (sha256((ROOT / MANIFEST_COPY).read_bytes()),
                          sha256((contracts / "ssot-stage1-handoff-manifest.json").read_bytes())),
                         (sha256((ROOT / LINK_MAP_COPY).read_bytes()),
                          sha256((contracts / "ssot-stage1-link-map.json").read_bytes()))):
            journal = journal.replace(old, new)
        (root / JOURNAL).write_text(journal, encoding="utf-8")
        return root

    def transfer(self, repo: Path, root: Path) -> None:
        with tempfile.TemporaryDirectory(dir=self.base) as stage:
            build.assemble(repo, "HEAD", root, Path(stage))
            build.install(Path(stage), root)

    def test_clean_transfer_is_installed_and_repeatable(self):
        repo, commit = self.spoke("spoke-clean")
        root = self.runtime("rt-clean", repo, commit)
        self.transfer(repo, root)
        first = tree_bytes(root)
        self.assertEqual(sum(1 for p in first if p.startswith(COPY_DIR + "/")), len(self.manifest["artifacts"]))
        self.transfer(repo, root)
        self.assertEqual(tree_bytes(root), first)

    def test_one_changed_byte_refuses_the_whole_transfer(self):
        changed = self.manifest["artifacts"][len(self.manifest["artifacts"]) // 2]["path"]
        repo, commit = self.spoke("spoke-changed", change=changed)
        root = self.runtime("rt-changed", repo, commit)
        before = tree_bytes(root)
        with tempfile.TemporaryDirectory(dir=self.base) as stage:
            with self.assertRaises(build.TransferError) as caught:
                build.assemble(repo, "HEAD", root, Path(stage))
        self.assertIn(f"изменённый файл {COPY_DIR}/{changed}", str(caught.exception))
        self.assertEqual(tree_bytes(root), before)
        self.assertFalse((root / COPY_DIR).exists())

    def test_manifest_not_pinned_by_the_journal_is_refused(self):
        repo, commit = self.spoke("spoke-unpinned")
        root = self.runtime("rt-unpinned", repo, commit)
        (repo / "docs/contracts/ssot-stage1-handoff-manifest.json").write_text("{}\n", encoding="utf-8")
        subprocess.run([*GIT, "-C", str(repo), "commit", "-qam", "other manifest"], check=True)
        with tempfile.TemporaryDirectory(dir=self.base) as stage:
            with self.assertRaises(build.TransferError) as caught:
                build.assemble(repo, "HEAD", root, Path(stage))
            self.assertFalse((Path(stage) / COPY_DIR).exists())
        self.assertIn("не равен журналу", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
