"""Copy the stage-1 SSOT of mango_ba_prompts into ssot/ (M2, BL-185…BL-188), fail-closed.

Needs a local clone of G-Ivan-A/mango_ba_prompts (the spoke is private, the
bytes are never restored from memory, cache or a fork). Reads the handoff
manifest and the link map at --ref (main of the spoke), checks their sha256
against the values the journal ssot/TRANSFERS.md pins, then takes every
artifact with `git show <source_commit>:<path>` — not from HEAD.

The copy is assembled in a temporary directory and checked there with the
guard of tests/test_ssot_transfer.py. Only a copy without a single error
replaces ssot/mango_ba_prompts/ and the two copies of the manifest and link
map; on any error ssot/ stays as it was (no partial copy). Running it again
on the same inputs leaves `git diff` empty.

    python3 tests/build_ssot_transfer.py --source /path/to/mango_ba_prompts
    python3 tests/build_ssot_transfer.py --source /path/to/mango_ba_prompts --check

The journal row of a new transfer is written by hand first (it names the
owner's publication decision and the runtime PR); the script refuses to copy
bytes that the journal does not pin. It prints only paths, counts and sha256.
"""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_ssot_transfer import (COPY_DIR, JOURNAL, LINK_MAP_COPY, MANIFEST_COPY,  # noqa: E402
                                ORCHESTRATOR, ROOT, SSOT, journal_rows, sha256, transfer_errors)

SPOKE_MANIFEST = "docs/contracts/ssot-stage1-handoff-manifest.json"
SPOKE_LINK_MAP = "docs/contracts/ssot-stage1-link-map.json"


class TransferError(Exception):
    pass


def git(source: Path, *args: str) -> bytes:
    res = subprocess.run(["git", "-C", str(source), *args], capture_output=True)
    if res.returncode:
        raise TransferError(f"git {' '.join(args)}: {res.stderr.decode('utf-8', 'replace').strip()}")
    return res.stdout


def assemble(source: Path, ref: str, root: Path, stage: Path) -> dict:
    """Write the transfer under stage/ssot and return its summary; raise on any mismatch."""
    rows = journal_rows((root / JOURNAL).read_text(encoding="utf-8"))
    if not rows:
        raise TransferError(f"{JOURNAL}: нет строки передачи; сначала запишите её (решение о публикации, PR)")
    pin = rows[-1]
    manifest_bytes = git(source, "show", f"{ref}:{SPOKE_MANIFEST}")
    link_map_bytes = git(source, "show", f"{ref}:{SPOKE_LINK_MAP}")
    for name, data, column in (("манифест", manifest_bytes, "sha256 манифеста"),
                               ("карта ссылок", link_map_bytes, "sha256 карты ссылок")):
        if sha256(data) != pin[column]:
            raise TransferError(f"{name} на {ref}: sha256 {sha256(data)} не равен журналу {pin[column]}")
    m = json.loads(manifest_bytes)
    commit = m["source_commit"]
    if git(source, "cat-file", "-t", commit).strip() != b"commit":
        raise TransferError(f"source_commit {commit} не найден в клоне спицы")

    (stage / SSOT).mkdir(parents=True)
    shutil.copyfile(root / JOURNAL, stage / JOURNAL)
    (stage / MANIFEST_COPY).write_bytes(manifest_bytes)
    (stage / LINK_MAP_COPY).write_bytes(link_map_bytes)
    (stage / ORCHESTRATOR).parent.mkdir(parents=True)
    shutil.copyfile(root / ORCHESTRATOR, stage / ORCHESTRATOR)
    for a in m["artifacts"]:
        entry = git(source, "ls-tree", commit, "--", a["path"]).decode("utf-8").split()
        if entry[:2] != ["100644", "blob"]:
            raise TransferError(f"{a['path']}: на {commit[:8]} не обычный файл 100644 ({entry[:2]})")
        out = stage / COPY_DIR / a["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(git(source, "show", f"{commit}:{a['path']}"))
    errors = transfer_errors(stage)
    if errors:
        raise TransferError("сверка копии:\n  " + "\n  ".join(errors))
    return {"version": m["version"], "source_commit": commit, "artifacts": len(m["artifacts"]),
            "bytes": sum(a["bytes"] for a in m["artifacts"]), "manifest_sha256": sha256(manifest_bytes)}


def install(stage: Path, root: Path) -> None:
    """Replace the copy as a whole: the directory and both reference copies."""
    fresh = root / SSOT / ".incoming"
    shutil.rmtree(fresh, ignore_errors=True)
    shutil.copytree(stage / COPY_DIR, fresh)
    shutil.rmtree(root / COPY_DIR, ignore_errors=True)
    fresh.rename(root / COPY_DIR)
    for rel in (MANIFEST_COPY, LINK_MAP_COPY):
        shutil.copyfile(stage / rel, root / rel)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", required=True, type=Path, help="local clone of G-Ivan-A/mango_ba_prompts")
    parser.add_argument("--ref", default="origin/main", help="ref of the spoke to read the manifest and link map at")
    parser.add_argument("--check", action="store_true", help="compare with ssot/ without writing; exit 1 on drift")
    args = parser.parse_args(argv)
    with tempfile.TemporaryDirectory(prefix="ssot-transfer-") as tmp:
        stage = Path(tmp)
        try:
            summary = assemble(args.source.resolve(), args.ref, ROOT, stage)
        except TransferError as exc:
            print(f"FAIL: {exc}\n{SSOT}/ не изменён", file=sys.stderr)
            return 1
        print(f"манифест {summary['version']} (sha256 {summary['manifest_sha256']}), "
              f"source_commit {summary['source_commit']}: {summary['artifacts']} артефактов, "
              f"{summary['bytes']} байт, сверка OK")
        if args.check:
            drift = [rel for rel in (MANIFEST_COPY, LINK_MAP_COPY)
                     if not (ROOT / rel).is_file() or (ROOT / rel).read_bytes() != (stage / rel).read_bytes()]
            if not drift and transfer_errors(ROOT):
                drift.append(COPY_DIR)
            print("ssot/ равен спице" if not drift else f"ssot/ расходится со спицей: {drift}")
            return 1 if drift else 0
        install(stage, ROOT)
    errors = transfer_errors(ROOT)
    print(f"{COPY_DIR}/ заменён, сверка в runtime: {'OK' if not errors else errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
