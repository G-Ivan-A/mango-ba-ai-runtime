"""Build the compact document and section navigation maps and section TOCs from KB indexes.

Run ``python docs/kb/build_map.py`` after adding or replacing a manual.
Run ``python docs/kb/build_map.py --check`` to verify committed maps.
Only the Python standard library is required.
"""

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / "docs/kb"
SECTION_LINK = re.compile(r"\[sections/([^]\n]+)\]\(sections/([^)]*)\)")
TOC_FIELDS = ("section", "title", "file")

# Search words are routing hints, not product facts. Product IDs come from the
# frontmatter of each index and must exist in taxonomy/products.yaml#classes.
ALIASES = {
    "api-server-client": ["API Сервер-клиент", "Server-client API", "WebSocket", "интеграция клиента"],
    "cov-robot-fil": ["голосовой робот", "чат-бот", "фильтр вызовов", "сценарий робота"],
    "integration-1c": ["1С", "управление торговлей", "интеграция АТС"],
    "integration-amocrm": ["amoCRM", "интеграция CRM"],
    "integration-bitrix24": ["Битрикс24", "Bitrix24", "интеграция CRM"],
    "integration-ident": ["IDENT", "стоматология", "медицинская CRM", "интеграция CRM"],
    "integration-bpmsoft": ["BPMSoft", "интеграция CRM"],
    "lk-vats-sso": ["SSO", "единый вход", "авторизация", "IdP"],
    "mango-cc-manual": ["контакт-центр", "оператор", "очередь обращений", "CC"],
    "mango-lk-manual": ["личный кабинет", "ВАТС", "настройка телефонии"],
    "mdialogi-api": ["Манго Диалоги", "MDialogi", "API сообщений"],
    "mtalker": ["Mango Talker", "софтфон", "мобильное приложение"],
    "quality-management": ["контроль качества", "оценка звонков", "бланк оценки"],
    "rolevaya-model-vats": ["роли", "права доступа", "ВАТС"],
    "sip-trunk": ["SIP TRUNK", "SIP-транк", "внешняя АТС"],
    "speech-analytics": ["речевая аналитика", "распознавание", "офлайн скоринг"],
    "wallboard": ["Wallboard", "табло", "рейтинг операторов", "показатели в реальном времени"],
    "vpbx-api": ["API ВАТС", "API КЦ", "вебхук", "звонки"],
}


def frontmatter(text):
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    block = text.split("---\n", 2)[1]
    result = {}
    for line in block.splitlines():
        if ": " not in line:
            continue
        key, raw = line.split(": ", 1)
        if raw.startswith('"'):
            result[key] = json.loads(raw)
        elif raw.startswith("[") and raw.endswith("]"):
            result[key] = [value.strip() for value in raw[1:-1].split(",") if value.strip()]
        else:
            result[key] = raw
    return result


def section_rows(index_text, directory):
    rows = []
    for line in index_text.splitlines():
        match = SECTION_LINK.search(line)
        if not match:
            continue
        if match.group(1) != match.group(2):
            raise ValueError(f"link label and target differ: {line}")
        before = line[: match.start()].split("|")
        after = line[match.end() :].split("|")
        if len(before) < 4 or len(after) < 6:
            raise ValueError(f"invalid section row: {line}")
        file_path = directory / "sections" / match.group(2)
        if not file_path.is_file():
            raise ValueError(f"missing section: {file_path}")
        meta = frontmatter(file_path.read_text(encoding="utf-8"))
        hint = "|".join(after[4:-1]).strip()
        rows.append(
            {
                "id": meta["id"],
                "section": before[1].strip(),
                "title": "|".join(before[2:-1]).strip(),
                "hint": "" if hint == "—" else hint,
                "pages": after[1].strip(),
                "tokens": int(after[3].strip()),
                "path": file_path.relative_to(ROOT).as_posix(),
            }
        )
    actual = set((directory / "sections").glob("*.md"))
    listed = {ROOT / row["path"] for row in rows}
    if actual != listed or len(rows) != len(listed):
        raise ValueError(f"section coverage differs in {directory}: {len(actual)} files, {len(rows)} rows")
    return rows


def toc_text(rows):
    """Render one tab-separated line per section, in map order and without quoting.

    A section map of a large manual does not fit into one file read of a chat
    model, and the model has no file search; the TOC always fits (RFC-RT-001, РТ-7).
    """
    lines = ["\t".join(TOC_FIELDS)]
    for row in rows:
        section, title = (row[field].replace("\t", " ") for field in ("section", "title"))
        lines.append(f"{section}\t{title}\t{Path(row['path']).name}")
    return "\n".join(lines) + "\n"


def json_text(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def build():
    taxonomy = (ROOT / "taxonomy/products.yaml").read_text(encoding="utf-8")
    class_ids = set(re.findall(r"\{id: ([a-z-]+), name:", taxonomy))
    documents = []
    outputs = {}
    for index in sorted(KB.glob("**/index.md")):
        directory = index.parent
        if not (directory / "sections").is_dir():
            continue  # multi-document package index; leaf indexes follow
        index_text = index.read_text(encoding="utf-8")
        meta = frontmatter(index_text)
        product_ids = meta.get("product_ids")
        if meta.get("product_taxonomy_ref") != "taxonomy/products.yaml#classes":
            raise ValueError(f"missing product taxonomy reference: {index}")
        if not product_ids or not set(product_ids) <= class_ids:
            raise ValueError(f"missing or unknown product_ids: {index}: {product_ids}")
        relative = directory.relative_to(KB)
        document_id = "--".join(relative.parts)
        group_id = relative.parts[0]
        rows = section_rows(index_text, directory)
        map_path = KB / "maps" / f"{document_id}.json"
        toc_path = KB / "maps" / f"{document_id}.toc.tsv"
        outputs[map_path] = json_text(
            {
                "document_id": document_id,
                "index": index.relative_to(ROOT).as_posix(),
                "product_ids": product_ids,
                "sections": rows,
            }
        )
        outputs[toc_path] = toc_text(rows)
        documents.append(
            {
                "id": document_id,
                "group_id": group_id,
                "title": meta["doc_title"],
                "version": meta["doc_version"],
                "product_ids": product_ids,
                "aliases": ALIASES.get(group_id, []),
                "index": index.relative_to(ROOT).as_posix(),
                "sections_map": map_path.relative_to(ROOT).as_posix(),
                "sections_toc": toc_path.relative_to(ROOT).as_posix(),
                "section_count": len(rows),
            }
        )
    outputs[KB / "MAP.json"] = json_text(
        {
            "schema_version": 1,
            "taxonomy_ref": "taxonomy/products.yaml#classes",
            "generated_by": "docs/kb/build_map.py",
            "navigation": {
                "select_document": "Match question terms and known product class against title, aliases and product_ids; open only the selected sections_toc.",
                "select_section": "Open sections_toc first: one read gives the whole section list as tab-separated section, title and file, without quoting. Choose sections by title and open each file at sections/<file> next to the document index, then adjacent rows only if context is needed. Open a row of sections_map only when its hint, pages or tokens are needed.",
                "retrieval_if_insufficient": [
                    "Search other rows of the same sections_toc.",
                    "Search other documents in the same group_id.",
                    "Search documents with overlapping product_ids, then all document titles and aliases.",
                    "If local KB still lacks evidence, follow taxonomy/source-tiers.yaml and record the missing source or question.",
                ],
            },
            "documents": documents,
        }
    )
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if committed maps are out of date")
    args = parser.parse_args()
    outputs = build()
    stale = []
    for path, text in outputs.items():
        content = text.encode("utf-8")
        if args.check:
            if not path.is_file() or path.read_bytes() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    if args.check:
        unexpected = set((KB / "maps").glob("*")) - set(outputs)
        stale.extend(str(path.relative_to(ROOT)) for path in sorted(unexpected))
    if stale:
        print("Stale KB maps or section TOCs: " + ", ".join(stale), file=sys.stderr)
        return 1
    documents = (len(outputs) - 1) // 2
    print(f"{'Checked' if args.check else 'Built'} {documents} document maps, {documents} section TOCs and MAP.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
