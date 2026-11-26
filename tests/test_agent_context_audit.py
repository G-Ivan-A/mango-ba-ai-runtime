"""Guards of RFC-RT-002 (issue #25): stage-1 contracts and the audit log.

The RFC is analysis only. These checks keep what it relies on true until the
owner decides otherwise (decisions Р-RT-1…N):

* every runtime path that stage-1 consumers read (task 1,
  G-Ivan-A/mango_ba_prompts#492) still exists;
* no client-specific context package is added without a decision; the
  skills mirror .agents/skills/<name>/SKILL.md is allowed by the owner's
  decision on Р-RT-3 B (BL-192, runtime #27);
* the audit log is in place, names the RFC it supports and was produced by
  the current audit script. The RFC itself lives in the RFC registry of
  G-Ivan-A/mango_ba_prompts (docs/rfc/2026-11-runtime-universal-agent-context.md):
  this repository keeps no organisational materials (compilation-manifest.yaml,
  section «discarded») and the task forbids changing its structure.
"""

import re
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
        # AGENTS.md is the single entry; .agents is the skills mirror (owner
        # decision on Р-RT-3 B, BL-192). Its content is guarded separately:
        # only .agents/skills/<name>/SKILL.md byte-equal to skills/ (test_skills_mirror.py).
        allowed = {"AGENTS.md", ".agents"}
        for marker, client in audit.CLIENT_MARKERS:
            if marker in allowed:
                continue
            with self.subTest(marker=marker):
                present = marker in files or any(f.startswith(marker + "/") for f in files)
                self.assertFalse(present, f"{marker} ({client}) needs an owner decision, RFC-RT-002")

    def test_agents_dir_is_only_skills_mirror(self):
        under = {f for f in tracked() if f.startswith(".agents/")}
        stray = {f for f in under if not re.fullmatch(r"\.agents/skills/[a-z0-9]+(-[a-z0-9]+)*/SKILL\.md", f)}
        self.assertEqual(stray, set(), "only the generated skills mirror may live under .agents (Р-RT-3 B)")

    def test_skills_fit_agent_skills_mirror(self):
        """RFC-RT-002 option «mirror <name>/SKILL.md» relies on this without editing skill texts."""
        for path in sorted(f for f in tracked() if f.startswith("skills/")):
            text = (ROOT / path).read_text(encoding="utf-8")
            name = audit.frontmatter(text).get("name", "")
            description = " ".join(audit.block_value(text, "description").split())
            with self.subTest(skill=path):
                self.assertEqual(name, Path(path).stem)
                self.assertRegex(name, audit.SKILL_NAME.pattern)
                self.assertLessEqual(len(name), 64)
                self.assertTrue(1 <= len(description) <= 1024, len(description))
                self.assertLess(text.count("\n"), 500)


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
