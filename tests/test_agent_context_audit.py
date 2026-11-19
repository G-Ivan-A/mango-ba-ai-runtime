"""Guards of RFC-RT-002 (issue #25): stage-1 contracts and the audit log.

The RFC is analysis only. These checks keep what it relies on true until the
owner decides otherwise (decisions Р-RT-1…N):

* every runtime path that stage-1 consumers read (task 1,
  G-Ivan-A/mango_ba_prompts#492) still exists;
* no client-specific context package is added without a decision;
* the audit log is in place, names the RFC it supports and was produced by
  the current audit script. The RFC itself lives in the RFC registry of
  G-Ivan-A/mango_ba_prompts (docs/rfc/2026-11-runtime-universal-agent-context.md):
  this repository keeps no organisational materials (compilation-manifest.yaml,
  section «discarded») and the task forbids changing its structure.
"""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

import agent_context_audit as audit  # noqa: E402

LOG = ROOT / "tests/agent_context_audit.log"


def tracked() -> set[str]:
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return {path for path in out.split("\0") if path}


class StageOneContracts(unittest.TestCase):
    def test_protected_paths_exist(self):
        files = tracked()
        for path in audit.DEPS_PATHS:
            clean = path.strip("/")
            with self.subTest(path=path):
                self.assertTrue(
                    clean == "" or clean in files or any(f.startswith(clean + "/") for f in files),
                    f"{path} is read by stage-1 consumers (#492) and must not move",
                )

    def test_no_client_package_without_decision(self):
        files = tracked()
        allowed = {"AGENTS.md"}
        for marker, client in audit.CLIENT_MARKERS:
            if marker in allowed:
                continue
            with self.subTest(marker=marker):
                present = marker in files or any(f.startswith(marker + "/") for f in files)
                self.assertFalse(present, f"{marker} ({client}) needs an owner decision, RFC-RT-002")


class AuditLog(unittest.TestCase):
    def test_log_names_the_rfc(self):
        first = LOG.read_text(encoding="utf-8").splitlines()[0]
        self.assertIn("RFC-RT-002", first)

    def test_log_matches_script_version(self):
        first = LOG.read_text(encoding="utf-8").splitlines()[0]
        self.assertTrue(first.endswith(f"версия скрипта {audit.AUDIT_VERSION}"), first)

    def test_audit_runs_offline(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tests/agent_context_audit.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("## 6. Приём SSOT этапа 1", result.stdout)


if __name__ == "__main__":
    unittest.main()
