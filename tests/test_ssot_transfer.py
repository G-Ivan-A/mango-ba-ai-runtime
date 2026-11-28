"""Guard of the pinned stage-1 SSOT copy in ssot/ (M2, BL-185…BL-188).

ssot/mango_ba_prompts/ is a byte copy of the artifacts of the handoff
manifest of G-Ivan-A/mango_ba_prompts at its source_commit (RFC-RT-002 Р-RT-6,
RFC-RT-003 §12 of the spoke). The spoke is private, so the guard works
without network and without the spoke: the copies of the manifest and of the
link map in ssot/ are the reference, the journal ssot/TRANSFERS.md pins them.

* the set of files of the copy equals the manifest, and nothing else is there;
* sha256, size and git blob of every file equal the manifest;
* sha256 of the manifest and link map copies equal the last journal row;
* source_commit of the link map equals the manifest;
* every relative link of the copy either leads to a file of the copy
  (inside) or is recorded in the link map (Р-RT-7 = 7а);
* `sources` of the gate map equal the manifest; the files the IDE layer
  reads are in the transfer.

Negative checks run the same function on a temporary copy: an extra, a
missing and a changed file are caught.

Rebuild the copy (needs read access to the spoke):

    python3 tests/build_ssot_transfer.py --source <clone of mango_ba_prompts>
"""

import hashlib
import json
import posixpath
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SSOT = "ssot"
SOURCE = "mango_ba_prompts"
COPY_DIR = f"{SSOT}/{SOURCE}"
MANIFEST_COPY = f"{SSOT}/{SOURCE}.manifest.json"
LINK_MAP_COPY = f"{SSOT}/{SOURCE}.link-map.json"
JOURNAL = f"{SSOT}/TRANSFERS.md"
SSOT_ENTRIES = {SOURCE, f"{SOURCE}.manifest.json", f"{SOURCE}.link-map.json", "TRANSFERS.md"}
GATE_MAP = "docs/ba-processes/bcreq-ide-gates.json"
ORCHESTRATOR = ".opencode/agents/bcreq-orchestrator.md"
# Files a client reads as instructions; a copy must not bring them (RFC-RT-003 §11.7, case 5).
INSTRUCTION_FILES = {"AGENTS.md", "CLAUDE.md", "CONTEXT.md"}
# Same pattern as the link map builder of the spoke and intake_check in tests/agent_context_audit.py.
MD_LINK = re.compile(r"\]\(([^)\s]+)\)")
JOURNAL_COLUMNS = ("№", "Дата", "Источник", "`source_commit`", "Манифест", "sha256 манифеста",
                   "sha256 карты ссылок", "Артефактов", "Карточки", "Решение о публикации", "PR runtime")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def journal_rows(text: str) -> list[dict]:
    """Rows of the transfers table: the header is JOURNAL_COLUMNS, a row starts with its number."""
    rows, header = [], None
    for line in text.splitlines():
        if not line.startswith("|"):
            header = None  # a table ends at the first line that is not a table row
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if tuple(cells) == JOURNAL_COLUMNS:
            header = cells
        elif header and cells and cells[0].isdigit() and len(cells) == len(header):
            rows.append(dict(zip(header, (c.strip("`") for c in cells))))
    return rows


def scan_links(files: dict[str, bytes], paths: set[str]) -> tuple[dict, list[dict]]:
    """Classify `](target)` links of the .md files the way the link map of the spoke does.

    Returns the counts by class and the records of the links that leave the
    transfer (the link map lists exactly these).
    """
    counts, records = {"absolute/anchor": 0, "inside": 0}, []
    for path in sorted(paths):
        if not path.endswith(".md"):
            continue
        for number, line in enumerate(files[path].decode("utf-8").splitlines(), 1):
            for raw in MD_LINK.findall(line):
                if re.match(r"^[a-z]+:", raw) or raw.startswith("#"):
                    counts["absolute/anchor"] += 1
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(path),
                                                           unquote(raw.partition("#")[0])))
                if target in paths or any(p.startswith(target + "/") for p in paths):
                    counts["inside"] += 1
                    continue
                records.append({"from": path, "line": number, "raw": raw, "target": target})
    return counts, records


def layer_paths(root: Path) -> set[str]:
    """Paths under ssot/mango_ba_prompts/ the orchestrator of the IDE layer names as its sources."""
    text = (root / ORCHESTRATOR).read_text(encoding="utf-8")
    found = set()
    for row in (ln for ln in text.splitlines() if ln.startswith("|") and f"`{COPY_DIR}/" in ln):
        names = re.findall(r"`([^`]+)`", row)
        base = posixpath.dirname(next(n for n in names if n.startswith(COPY_DIR + "/")))
        for name in names:
            if name.startswith(COPY_DIR + "/"):
                found.add(name[len(COPY_DIR) + 1:])
            elif "/" not in name and name.endswith((".md", ".json")):
                found.add(posixpath.join(base, name)[len(COPY_DIR) + 1:])
    return found


def transfer_errors(root: Path = ROOT) -> list[str]:
    """Everything that makes ssot/ under root differ from its manifest, journal and link map."""
    errors: list[str] = []
    for rel in (MANIFEST_COPY, LINK_MAP_COPY, JOURNAL):
        if not (root / rel).is_file():
            errors.append(f"нет {rel}")
    if errors:
        return errors
    manifest_bytes = (root / MANIFEST_COPY).read_bytes()
    link_map_bytes = (root / LINK_MAP_COPY).read_bytes()
    m = json.loads(manifest_bytes)
    lm = json.loads(link_map_bytes)
    commit, transfer = m["source_commit"], m["transfer"]
    artifacts = {a["path"]: a for a in m["artifacts"]}

    # Layout declared by the manifest is the layout of this repository.
    layout = {"target_dir": COPY_DIR + "/", "manifest_copy": MANIFEST_COPY,
              "link_map_copy": LINK_MAP_COPY, "journal": JOURNAL}
    for key, value in layout.items():
        if transfer.get(key) != value:
            errors.append(f"манифест: transfer.{key} = {transfer.get(key)!r}, раскладка runtime — {value!r}")
    if not COMMIT.match(commit):
        errors.append(f"манифест: source_commit {commit!r} не SHA коммита")
    if len(artifacts) != len(m["artifacts"]) or len(artifacts) != m["summary"]["artifacts"]:
        errors.append("манифест: число артефактов не равно summary.artifacts или пути повторяются")
    for a in m["artifacts"]:
        if a["source_commit"] != commit:
            errors.append(f"манифест: {a['path']} снят не с source_commit")

    # Journal: the last row is this transfer and pins both copies.
    rows = journal_rows((root / JOURNAL).read_text(encoding="utf-8"))
    if not rows:
        errors.append(f"{JOURNAL}: нет строк таблицы передач")
    else:
        if [int(r["№"]) for r in rows] != list(range(1, len(rows) + 1)):
            errors.append(f"{JOURNAL}: номера передач не идут подряд с 1")
        last = rows[-1]
        expected = {"№": str(transfer["number"]), "Источник": m["source_repository"],
                    "`source_commit`": commit, "Манифест": m["version"],
                    "sha256 манифеста": sha256(manifest_bytes),
                    "sha256 карты ссылок": sha256(link_map_bytes),
                    "Артефактов": str(len(artifacts)), "Карточки": ", ".join(transfer["cards"])}
        for column, value in expected.items():
            if last[column] != value:
                errors.append(f"{JOURNAL}: в последней строке «{column}» = {last[column]!r}, ожидалось {value!r}")

    # Files of the copy: the same set, the same bytes.
    copy_root = root / COPY_DIR
    if not copy_root.is_dir():
        return errors + [f"нет каталога {COPY_DIR}/"]
    extra_entries = sorted(p.name for p in (root / SSOT).iterdir() if p.name not in SSOT_ENTRIES)
    if extra_entries:
        errors.append(f"{SSOT}/: лишние записи {extra_entries}")
    found, files = set(), {}
    for p in sorted(copy_root.rglob("*")):
        rel = p.relative_to(copy_root).as_posix()
        if p.is_symlink():
            errors.append(f"{COPY_DIR}/{rel}: символическая ссылка")
        elif p.is_file():
            found.add(rel)
    for rel in sorted(found - set(artifacts)):
        errors.append(f"лишний файл {COPY_DIR}/{rel}")
    for rel in sorted(set(artifacts) - found):
        errors.append(f"недостающий файл {COPY_DIR}/{rel}")
    for rel in sorted(found & set(artifacts)):
        data = files[rel] = (copy_root / rel).read_bytes()
        a = artifacts[rel]
        if sha256(data) != a["sha256"] or len(data) != a["bytes"] or git_blob(data) != a["git_blob"]:
            errors.append(f"изменённый файл {COPY_DIR}/{rel}: sha256 не равен манифесту")
        if posixpath.basename(rel) in INSTRUCTION_FILES:
            errors.append(f"{COPY_DIR}/{rel}: файл инструкций клиента в копии")
    if found != set(artifacts):
        return errors

    # Link map: same transfer, and it lists exactly the links that leave the copy.
    for key in ("source_repository", "source_commit", "target_dir"):
        expected_value = COPY_DIR + "/" if key == "target_dir" else m[key]
        if lm.get(key) != expected_value:
            errors.append(f"карта ссылок: {key} = {lm.get(key)!r}, в манифесте — {expected_value!r}")
    counts, outside = scan_links(files, set(artifacts))
    recorded = {(r["from"], r["line"], r["raw"]): r for r in lm["links"]}
    computed = {(r["from"], r["line"], r["raw"]): r for r in outside}
    for key in sorted(set(computed) - set(recorded)):
        errors.append(f"ссылка {key[0]}:{key[1]} ({key[2]}) ведёт вне копии и не записана в карте ссылок")
    for key in sorted(set(recorded) - set(computed)):
        errors.append(f"карта ссылок: {key[0]}:{key[1]} ({key[2]}) нет в копии или ведёт внутрь")
    base = f"https://github.com/{m['source_repository']}/"
    for key in sorted(set(recorded) & set(computed)):
        r = recorded[key]
        if r["target"] != computed[key]["target"]:
            errors.append(f"карта ссылок: {key[0]}:{key[1]} цель {r['target']!r}, в копии — {computed[key]['target']!r}")
        if r["class"] == "outside" and not re.match(
                re.escape(base) + r"(blob|tree)/" + re.escape(commit) + "/" + re.escape(r["target"]) + r"(#|$)",
                r["permalink"] or ""):
            errors.append(f"карта ссылок: {key[0]}:{key[1]} permalink не на source_commit")
    counted = dict(counts)
    for r in lm["links"]:
        counted[r["class"]] = counted.get(r["class"], 0) + 1
    if counted != lm["summary"]["links"]:
        errors.append(f"карта ссылок: счёт ссылок {counted} не равен summary {lm['summary']['links']}")
    # Inside links lead to existing files (or directories) of the copy.
    for path in sorted(p for p in artifacts if p.endswith(".md")):
        for raw in MD_LINK.findall(files[path].decode("utf-8")):
            if re.match(r"^[a-z]+:", raw) or raw.startswith("#"):
                continue
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(raw.partition("#")[0])))
            inside = target in artifacts or any(p.startswith(target + "/") for p in artifacts)
            if inside and not (copy_root / target).exists():
                errors.append(f"ссылка {path} → {target}: цели нет в копии")

    # Gate map of the IDE layer: its sources are the transferred bytes.
    if GATE_MAP not in artifacts:
        errors.append(f"карты гейтов {GATE_MAP} нет в передаче")
    else:
        gates = json.loads(files[GATE_MAP])
        if gates["runtime_path"] != f"{COPY_DIR}/{GATE_MAP}":
            errors.append(f"карта гейтов: runtime_path {gates['runtime_path']!r} не в каталоге копии")
        for path, digest in sorted(gates["sources"].items()):
            if path not in artifacts or artifacts[path]["sha256"] != digest:
                errors.append(f"карта гейтов: источник {path} не совпадает с манифестом")
    if (root / ORCHESTRATOR).is_file():
        for path in sorted(layer_paths(root) - set(artifacts)):
            errors.append(f"оркестратор читает {COPY_DIR}/{path}, а его нет в передаче")
    return errors


class Transfer(unittest.TestCase):
    """The copy in this repository equals its manifest, journal and link map."""

    def test_copy_matches_manifest(self):
        self.assertEqual(transfer_errors(ROOT), [])

    def test_transfer_is_complete(self):
        m = json.loads((ROOT / MANIFEST_COPY).read_bytes())
        self.assertEqual(len(m["artifacts"]), m["summary"]["artifacts"])
        self.assertEqual(sum(m["summary"]["transfer_cards"].values()), len(m["artifacts"]))
        self.assertTrue((ROOT / COPY_DIR / GATE_MAP).is_file())
        self.assertGreater(len(layer_paths(ROOT)), 1)

    def test_git_keeps_bytes(self):
        """Mode 100644, no symlinks, no end-of-line conversion (case 8 and 22 of RFC-RT-003 §12.8)."""
        try:
            listing = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-s", "--", SSOT],
                                     capture_output=True, text=True, check=True).stdout.splitlines()
        except (OSError, subprocess.CalledProcessError) as exc:
            self.skipTest(f"not a git checkout: {exc}")
        if not listing:
            self.skipTest("ssot/ is not in the index yet")
        modes = {line.split()[0] for line in listing}
        self.assertEqual(modes, {"100644"})
        attrs = subprocess.run(["git", "-C", str(ROOT), "check-attr", "text", "--",
                                f"{COPY_DIR}/{GATE_MAP}", JOURNAL],
                               capture_output=True, text=True, check=True).stdout
        self.assertEqual(attrs.count(": text: unset"), 2, attrs)


class NegativeChecks(unittest.TestCase):
    """A changed copy is caught (checked on a temporary copy of ssot/)."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="ssot-guard-")
        cls.base = Path(cls.tmp.name)
        shutil.copytree(ROOT / SSOT, cls.base / "pristine" / SSOT)
        (cls.base / "pristine" / ORCHESTRATOR).parent.mkdir(parents=True)
        shutil.copyfile(ROOT / ORCHESTRATOR, cls.base / "pristine" / ORCHESTRATOR)
        cls.m = json.loads((ROOT / MANIFEST_COPY).read_bytes())

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def setUp(self):
        self.root = self.base / self._testMethodName
        shutil.copytree(self.base / "pristine", self.root)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def assertCaught(self, fragment: str):
        errors = transfer_errors(self.root)
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_pristine_copy_passes(self):
        self.assertEqual(transfer_errors(self.root), [])

    def test_extra_file(self):
        (self.root / COPY_DIR / "prompts" / ".DS_Store").write_bytes(b"\0")
        self.assertCaught(f"лишний файл {COPY_DIR}/prompts/.DS_Store")

    def test_extra_instruction_file(self):
        (self.root / COPY_DIR / "docs" / "AGENTS.md").write_text("# local\n", encoding="utf-8")
        self.assertCaught(f"лишний файл {COPY_DIR}/docs/AGENTS.md")

    def test_extra_entry_in_ssot(self):
        (self.root / SSOT / "README.md").write_text("# local\n", encoding="utf-8")
        self.assertCaught("лишние записи ['README.md']")

    def test_missing_file(self):
        path = self.m["artifacts"][-1]["path"]
        (self.root / COPY_DIR / path).unlink()
        self.assertCaught(f"недостающий файл {COPY_DIR}/{path}")

    def test_changed_byte(self):
        path = self.m["artifacts"][0]["path"]
        target = self.root / COPY_DIR / path
        data = bytearray(target.read_bytes())
        data[len(data) // 2] ^= 0x01
        target.write_bytes(bytes(data))
        self.assertCaught(f"изменённый файл {COPY_DIR}/{path}")

    def test_crlf_checkout(self):
        path = GATE_MAP
        target = self.root / COPY_DIR / path
        target.write_bytes(target.read_bytes().replace(b"\n", b"\r\n"))
        self.assertCaught(f"изменённый файл {COPY_DIR}/{path}")

    def test_manifest_not_in_journal(self):
        manifest = self.root / MANIFEST_COPY
        manifest.write_bytes(manifest.read_bytes() + b"\n")
        self.assertCaught("«sha256 манифеста»")

    def test_link_map_of_another_commit(self):
        path = self.root / LINK_MAP_COPY
        lm = json.loads(path.read_bytes())
        lm["source_commit"] = "0" * 40
        path.write_text(json.dumps(lm, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        self.assertCaught("карта ссылок: source_commit")

    def test_link_out_of_copy_not_in_link_map(self):
        path = self.root / LINK_MAP_COPY
        lm = json.loads(path.read_bytes())
        dropped = lm["links"].pop()
        path.write_text(json.dumps(lm, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        self.assertCaught(f"ссылка {dropped['from']}:{dropped['line']}")

    def test_gate_map_source_differs(self):
        path = self.root / MANIFEST_COPY
        m = json.loads(path.read_bytes())
        gates = json.loads((ROOT / COPY_DIR / GATE_MAP).read_bytes())
        source = next(iter(gates["sources"]))
        next(a for a in m["artifacts"] if a["path"] == source)["sha256"] = "0" * 64
        path.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        self.assertCaught(f"карта гейтов: источник {source}")

    def test_journal_row_missing(self):
        journal = self.root / JOURNAL
        text = journal.read_text(encoding="utf-8")
        journal.write_text("\n".join(ln for ln in text.splitlines() if not ln.startswith("| 1 |")) + "\n",
                           encoding="utf-8")
        self.assertCaught("нет строк таблицы передач")

    def test_whole_copy_missing(self):
        shutil.rmtree(self.root / COPY_DIR)
        self.assertCaught(f"нет каталога {COPY_DIR}/")


class JournalParsing(unittest.TestCase):
    def test_rows_follow_the_header(self):
        header = "| " + " | ".join(JOURNAL_COLUMNS) + " |"
        text = "\n".join(["| 1 | not a row |", "", header, "| --- |",
                          "| 1 | d | s | `c` | 0.2 | `a` | `b` | 3 | BL-1 | r | p |", ""])
        rows = journal_rows(text)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["`source_commit`"], "c")
        self.assertEqual(rows[0]["sha256 манифеста"], "a")


if __name__ == "__main__":
    unittest.main()
