"""Generate or check the skills mirror .agents/skills/<name>/SKILL.md (RFC-RT-002, Р-RT-3 B).

skills/<name>.md is the only source of the skills. The mirror is a byte-for-byte
copy in the Agent Skills layout that clients discover natively (OpenCode V1/V2,
Codex, Cursor, Copilot and others read .agents/skills). The mirror is a view,
not a second source: it is never edited by hand and is checked by sha256.

    python3 tests/build_skills_mirror.py          # regenerate the mirror
    python3 tests/build_skills_mirror.py --check  # exit 1 if the mirror drifted

Edit skills/<name>.md, then regenerate; tests/test_skills_mirror.py and
tests/runtime-smoke.sh fail while the mirror differs from skills/.
"""

import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("skills")
MIRROR = Path(".agents/skills")
SKILL_FILE = "SKILL.md"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def expected(root: Path = ROOT) -> dict[str, bytes]:
    """Mirror path (relative to root) -> bytes it must hold."""
    return {
        (MIRROR / src.stem / SKILL_FILE).as_posix(): src.read_bytes()
        for src in sorted((root / SOURCE).glob("*.md"))
    }


def actual(root: Path = ROOT) -> dict[str, bytes]:
    base = root / MIRROR.parts[0]
    if not base.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(base.rglob("*"))
        if path.is_file() or path.is_symlink()
    }


def drift(root: Path = ROOT) -> list[str]:
    """Human-readable differences between the mirror and skills/; empty when in sync."""
    want, have = expected(root), actual(root)
    problems = []
    for path in sorted(want.keys() - have.keys()):
        problems.append(f"missing {path}")
    for path in sorted(have.keys() - want.keys()):
        problems.append(f"extra {path}: the mirror holds only {MIRROR}/<name>/{SKILL_FILE} of {SOURCE}/<name>.md")
    for path in sorted(want.keys() & have.keys()):
        if (root / path).is_symlink():
            problems.append(f"symlink {path}: the mirror is a copy (symlinks break on Windows)")
        elif sha256(want[path]) != sha256(have[path]):
            source = SOURCE / f"{Path(path).parent.name}.md"
            problems.append(f"sha256 {path} != {source}")
    return problems


def build(root: Path = ROOT) -> list[str]:
    """Write the mirror and remove anything else under .agents; return changed paths."""
    want = expected(root)
    changed = []
    for path, data in want.items():
        target = root / path
        if target.is_symlink():
            target.unlink()
        if not target.is_file() or target.read_bytes() != data:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            changed.append(path)
    for path in sorted(actual(root).keys() - want.keys()):
        (root / path).unlink()
        changed.append(path)
    base = root / MIRROR.parts[0]
    for directory in sorted((d for d in base.rglob("*") if d.is_dir()), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()
    return changed


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="only compare, do not write")
    args = parser.parse_args(argv)
    if args.check:
        problems = drift()
        for line in problems:
            print(line, file=sys.stderr)
        print(f"mirror {'drifted' if problems else 'in sync'}: {len(expected())} skills")
        return 1 if problems else 0
    changed = build()
    for path in changed:
        print(f"wrote {path}")
    print(f"mirror built: {len(expected())} skills, {len(changed)} changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
