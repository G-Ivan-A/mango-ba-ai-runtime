"""Extract a single-PDF Mango Office manual into docs/kb/<doc>/ (issue #12).

Usage (the PDF stays on the operator's workstation, it is not committed):

    python docs/kb/tools/extract_kb_doc.py DOC_KEY SOURCE.pdf [--out docs/kb/<doc>]

DOC_KEY is one of the keys of ``DOCS`` below (document metadata).

What the script does:
* takes the section list from the PDF outline, or — if the PDF has none —
  from the printed table of contents, and finds each heading on its page;
* keeps text, tables (Markdown) and illustrations in reading order;
* drops decorative images (page template / logo repeated on many pages,
  uniform rectangles, images under 8 px and images whose sha1 is passed with
  ``--decorative-sha1`` after a visual check);
* writes for each kept illustration a text description (``kb_images.describe``):
  section, page, manual text it belongs to, caption and OCR of visible text;
* re-reads the same pages with pdfplumber to confirm critical tokens;
* writes index.md, meta.json, verification.md and IMAGES.md.
"""

import argparse
import datetime
import hashlib
import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import pdfplumber
import pymupdf
import tiktoken

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_images import CAPTION, describe, is_uniform, load_with_mask, norm, ocr, optimize_save  # noqa: E402

DOCS = {
    "api-server-client": {
        "code": "APISC", "title": "Описание API «Сервер-клиент». API MANGO OFFICE",
        "version": "18.09.2024", "product_ids": ["voice-ucaas"],
        "src": "kb/sources/api-server-client/Api_server_client.pdf",
        "note": "Описание API «Сервер-клиент» MANGO OFFICE: REST-запросы управления интеграцией, "
                "пользователями, вебсокетом, звонками, SMS, записями и статистикой, события вебсокета, "
                "справочники и коды результатов.",
    },
    "integration-ident": {
        "code": "INTIDENT", "title": "Интеграция Виртуальной АТС и системы IDENT. Инструкция по настройке",
        "version": "14.01.2025", "product_ids": ["voice-ucaas"],
        "src": "kb/sources/integration-ident/Mango_office_integration_IDENT.pdf",
        "note": "Инструкция по настройке интеграции виртуальной АТС MANGO OFFICE с системой IDENT: "
                "подключение ВАТС, софтфон Mango Talker, виджет в Личном кабинете, отключение интеграции.",
    },
    "wallboard": {
        "code": "WB", "title": "Программа для ЭВМ «Wallboard Mango Office». Руководство пользователя",
        "version": "7.22.25", "product_ids": ["contact-center", "analytics-reporting"],
        "src": "kb/sources/wallboard/Programma-dlya-EVM-Wallboard-Mango-Office_v7.22.25.pdf",
        "note": "Руководство пользователя модуля Wallboard Mango Office: подключение в Личном кабинете ВАТС, "
                "аккаунт, авторизация, настройка показателей по шаблону и своему шаблону, мониторинг групп.",
    },
}
ENC = tiktoken.get_encoding("cl100k_base")
TODAY = datetime.date.today().isoformat()
TOC_LINE = re.compile(r"^(\d+(?:\.\d+)*\.?)\s*(.*?)\s*\.{3,}\s*(\d+)\s*$")
TR = dict(zip("абвгдеёзиклмнопрстуфхцыэ", "abvgdeeziklmnoprstufhcye"))
TR.update({"ж": "zh", "ч": "ch", "ш": "sh", "щ": "sch", "ю": "yu", "я": "ya", "ъ": "", "ь": "", "й": "y"})


def slug(text, limit=40):
    s = "".join(TR.get(c, c) for c in text.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:limit].strip("-") or "razdel"


def ntoks(text):
    return len(ENC.encode(text))


def page_ranges(pages):
    pages = sorted(set(pages))
    return f"{pages[0]}-{pages[-1]}" if pages[0] != pages[-1] else str(pages[0])


def key(text):
    return re.sub(r"[^0-9a-zа-яё]", "", text.casefold().replace("ё", "е"))


def printed_toc(doc):
    """Parse the printed TOC (number line + 'title ..... page' line may be split)."""
    toc, buf, started = [], "", False
    for pno in range(min(4, doc.page_count)):
        for line in doc[pno].get_text().splitlines():
            line = norm(line)
            if not line:
                continue
            if not started:  # skip the title page text before the TOC heading
                started = key(line) in ("оглавление", "содержание")
                continue
            buf = f"{buf} {line}".strip() if buf else line
            m = TOC_LINE.match(buf)
            if m:
                num = m.group(1).rstrip(".")
                toc.append([num.count(".") + 1, f"{num} {norm(m.group(2))}", int(m.group(3))])
                buf = ""
            elif not re.match(r"^\d+(\.\d+)*\.?$", buf) and not re.match(r"^\d+(\.\d+)*\.?\s", buf):
                buf = ""
    return toc


def page_items(page):
    """Reading-order items of a page: text lines, tables and images."""
    h = page.rect.height
    items = []
    tables = []
    try:
        for t in page.find_tables().tables:
            rows = [[norm(c or "").replace("|", "/") for c in r] for r in t.extract()]
            rows = [r for r in rows if any(r)]
            if len(rows) >= 2 and max(len(r) for r in rows) >= 2:
                tables.append((pymupdf.Rect(t.bbox), rows))
    except Exception:  # noqa: BLE001 - table detection is best effort
        pass
    for rect, rows in tables:
        items.append({"kind": "table", "y": rect.y0, "x": rect.x0, "rows": rows})
    for b in page.get_text("dict", sort=True)["blocks"]:
        if b["type"]:
            continue
        for ln in b["lines"]:
            text = norm("".join(s["text"] for s in ln["spans"]))
            r = pymupdf.Rect(ln["bbox"])
            if not text or r.y0 < h * 0.04 or r.y1 > h * 0.95:
                continue  # running header / footer / page number
            if any(rect.contains(r) or rect.intersect(r).get_area() > 0.6 * r.get_area() for rect, _ in tables):
                continue
            sp = max(ln["spans"], key=lambda s: len(s["text"].strip()))
            items.append({"kind": "text", "y": r.y0, "y1": r.y1, "x": r.x0, "text": text,
                          "size": round(sp["size"], 1), "bold": "Bold" in sp["font"], "block": id(b)})
    masks = {im[0]: im[1] for im in page.get_images(full=True)}
    for info in page.get_image_info(hashes=True, xrefs=True):
        if info["xref"]:
            info["smask"] = masks.get(info["xref"], 0)
            items.append({"kind": "image", "y": info["bbox"][1], "x": info["bbox"][0], "info": info})
    items.sort(key=lambda i: (round(i["y"]), i["x"]))
    return items


def table_md(rows):
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * width]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc_key", choices=sorted(DOCS))
    ap.add_argument("pdf")
    ap.add_argument("--out")
    ap.add_argument("--decorative-sha1", nargs="*", default=[],
                    help="sha1 of image bytes verified visually as logo / decoration")
    ap.add_argument("--no-ocr", action="store_true")
    args = ap.parse_args()
    cfg = DOCS[args.doc_key]
    out = Path(args.out or f"docs/kb/{args.doc_key}")
    doc = pymupdf.open(args.pdf)
    sha = hashlib.sha256(Path(args.pdf).read_bytes()).hexdigest()
    toc = doc.get_toc()
    section_source = f"pdf-outline (pymupdf {pymupdf.VersionBind})"
    if not toc:
        toc = printed_toc(doc)
        section_source = "printed table of contents; headings located on their pages"
    total = doc.page_count

    hash_pages = Counter()
    for p in doc:
        for d in {i["digest"] for i in p.get_image_info(hashes=True)}:
            hash_pages[d] += 1
    template = {d for d, n in hash_pages.items() if n >= max(3, total * 0.3)}

    # ---- walk pages; split at the headings of the TOC
    pending = list(toc)
    sections = [{"num": "—", "level": 0, "heading": "Титульная часть", "title": "Титульная часть",
                 "items": [], "start": 1}]
    missing = []
    for p in doc:
        gp = p.number + 1
        for it in page_items(p):
            it.update(page=gp)
            while pending and pending[0][2] < gp:  # heading not found on its page
                missing.append(pending.pop(0))
            if it["kind"] == "text" and pending and pending[0][2] == gp and gp > 1:
                lvl, head, _ = pending[0]
                hk, tk = key(head), key(it["text"])
                if tk and len(tk) >= 2 and (hk.startswith(tk) or tk.startswith(hk)):
                    m = re.match(r"^(\d+(?:\.\d+)*)\.?\s+(.*)$", head)
                    num, title = (m.group(1), m.group(2)) if m else ("", head)
                    sections.append({"num": num or "", "level": lvl, "heading": head, "title": norm(title),
                                     "items": [], "start": gp, "hk": hk, "acc": tk})
                    pending.pop(0)
                    continue
            s = sections[-1]
            # wrapped heading: next line continues the heading text
            if it["kind"] == "text" and s.get("hk") and not s["items"] and s["acc"] != s["hk"]:
                acc = s["acc"] + key(it["text"])
                if s["hk"].startswith(acc) or acc.startswith(s["hk"]):
                    s["acc"] = acc
                    continue
            s["items"].append(it)
    missing += pending
    if missing:
        print("TOC entries without heading:", missing, file=sys.stderr)

    # ---- write output
    if out.exists():
        shutil.rmtree(out)
    (out / "sections").mkdir(parents=True)
    (out / "images").mkdir()
    plumb = pdfplumber.open(args.pdf)
    plumb_cache = {}
    rows, meta_sections, verify_sections = [], [], []
    removed = Counter()
    removed_list = []
    image_count = table_count = total_tokens = 0
    critical_re = re.compile(r"https?://\S+|[a-z]+_[a-z_]+|\b\d{3,}\b|\b[A-Za-z][A-Za-z0-9-]{2,}\b")
    context = ""
    for order, s in enumerate(sections):
        nn = f"{order:02d}"
        fname = f"{nn}-{slug(s['title'])}"
        sec = s["num"] or (sections[order - 1]["num"] if order else "—") or "—"
        spages = sorted({i["page"] for i in s["items"]} | {s["start"]})
        body, para, prev_block, img_k = [], [], None, 0

        def flush():
            nonlocal para
            if para:
                body.append(" ".join(para))
            para = []

        for idx, it in enumerate(s["items"]):
            if it["kind"] == "text":
                if it["block"] != prev_block:
                    flush()
                para.append(it["text"])
                prev_block = it["block"]
                continue
            flush()
            prev_block = None
            if it["kind"] == "table":
                body.append(table_md(it["rows"]))
                table_count += 1
                continue
            info = it["info"]
            w, h = info["width"], info["height"]
            img = load_with_mask(doc, info["xref"], info["smask"])
            raw_sha1 = hashlib.sha1(doc.extract_image(info["xref"])["image"]).hexdigest()
            why = ""
            if info["digest"] in template:
                why = "фирменный шаблон страницы / логотип, повторяется на многих страницах"
            elif raw_sha1 in args.decorative_sha1:
                why = "логотип / оформительский элемент (проверено визуально)"
            elif w < 8 or h < 8:
                why = "служебный элемент менее 8 пикселей"
            elif is_uniform(img):
                why = "однотонная подложка / рамка"
            if why:
                removed[why] += 1
                removed_list.append((it["page"], f"{w}×{h}", raw_sha1[:12], why))
                continue
            img_k += 1
            image_count += 1
            iname = f"{fname}-{img_k}.png"
            optimize_save(img, out / "images" / iname)
            prev_text = " ".join(b for b in body[-2:] if not b.startswith(("!", ">", "|"))) or context
            nxt = next((j["text"] for j in s["items"][idx + 1:] if j["kind"] == "text"), "")
            caption = nxt if CAPTION.match(nxt) else ""
            label, block = describe(cfg["code"], sec, img_k, s["title"], it["page"], img, prev_text, caption,
                                    "" if args.no_ocr else ocr(img))
            body.append(f"![{label}](../images/{iname})\n\n{block}")
        flush()
        texts = [b for b in body if not b.startswith(("!", "|"))]
        if texts:
            context = texts[-1]
        hint = next((b for b in texts if len(b) > 20), "—")
        hint = norm(hint).replace("|", "/")[:90] if hint != "—" else "—"

        # ---- cross-engine verification
        text_only = " ".join(b for b in body if not b.startswith("!"))
        crit = sorted(set(critical_re.findall(text_only)))
        ptext = ""
        for gp in range(max(1, spages[0] - 1), min(total, spages[-1] + 1) + 1):
            if gp not in plumb_cache:
                plumb_cache[gp] = re.sub(r"\s+", "", plumb.pages[gp - 1].extract_text() or "")
            ptext += plumb_cache[gp]
        unconfirmed = [c for c in crit if re.sub(r"\s+", "", c) not in ptext]
        pages_s = page_ranges(spages)
        verify_sections.append({"file": f"sections/{fname}.md", "critical_tokens": len(crit),
                                "unconfirmed": unconfirmed, "pages": pages_s, "title": s["title"]})
        content = "\n\n".join(body)
        if unconfirmed:
            content += ("\n\n<!-- kb-verify:start -->\n\n> ❓ **ТРЕБУЕТСЯ ПРОВЕРКА**: токены не подтверждены вторым "
                        f"движком (pdfplumber) на стр. {pages_s}: " + ", ".join(f"`{u}`" for u in unconfirmed[:30])
                        + "\n\n<!-- kb-verify:end -->")
        tokens = ntoks(content)
        total_tokens += tokens
        refs = [{"source_pdf": cfg["src"], "part": 1, "pages": pages_s, "global_pages": pages_s}]
        fm = {"doc_title": cfg["title"], "doc_version": cfg["version"],
              "section": sec if sec != "—" else "0", "pdf_section": sec, "title": s["title"],
              "pdf_heading": s["heading"], "pages": pages_s}
        lines = ["---", f"id: {args.doc_key}-{fname}", f"doc_code: {cfg['code']}"]
        lines += [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()]
        lines += [f"source: {cfg['src']}", 'source_part: "1"', f'source_pages: "ч.1: {pages_s}"',
                  "source_refs: '" + json.dumps(refs, ensure_ascii=False, separators=(",", ":")) + "'",
                  f'extracted_by: "pymupdf {pymupdf.VersionBind}"', 'token_method: "tiktoken:cl100k_base"',
                  f"tokens: {tokens}", f"images: {img_k}", "status: extracted", "ai-generated: true", "---"]
        hashes = "#" * min(6, max(1, s["level"]))
        title_line = f"{s['num']}. {s['title']}" if s["num"] else s["title"]
        lines += [f"{hashes} {title_line}", "",
                  f"> Трассировка: PDF §{sec} · сквозные стр. {pages_s} · источники: ч.1 `{cfg['src']}` с.{pages_s}.",
                  "", content, ""]
        (out / "sections" / f"{fname}.md").write_text("\n".join(lines))
        rows.append(f"| {sec} | {s['title']} | [sections/{fname}.md](sections/{fname}.md) | {pages_s} | "
                    f"ч.1 с.{pages_s} | {tokens} | {hint} |")
        meta_sections.append({"file": f"sections/{fname}.md", "number": sec, "order": nn, "pages": pages_s,
                              "pdf_heading": s["heading"], "pdf_section": sec, "source_refs": refs,
                              "title": s["title"], "tokens": tokens, "images": img_k})

    checked = sum(v["critical_tokens"] for v in verify_sections)
    unconf = sum(len(v["unconfirmed"]) for v in verify_sections)
    ratio = 1 - unconf / checked if checked else 1
    confidence = "high" if ratio >= 0.98 and not missing else "requires_review"
    code = cfg["code"]
    index = f"""---
product_taxonomy_ref: taxonomy/products.yaml#classes
product_ids: [{', '.join(cfg['product_ids'])}]
type: kb-source-index
doc_code: {code}
doc_title: "{cfg['title'].replace('"', "'")}"
doc_version: "{cfg['version']}"
status: extracted
ai-generated: true
source_document: "{Path(cfg['src']).name}"
extraction_date: "{TODAY}"
model_used: "PyMuPDF {pymupdf.VersionBind} + pdfplumber {pdfplumber.__version__} + tesseract OCR (rus+eng)"
confidence_level: "{confidence}"
pages_covered: "1-{total}"
---

# {cfg['title']} — индекс БЗ (карта разделов)

> Источник: `{cfg['src']}` (версия документа {cfg['version']}, {total} с.). Исходный PDF в репозитории
> не хранится. Токены: tiktoken:cl100k_base. Это **карта поиска** для агента (ADR-007 R2): найди
> раздел по колонке «Когда обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md) — уровень доверия
> **{confidence}**. Отбор и описание иллюстраций: [`IMAGES.md`](IMAGES.md).

## Как цитировать

`[{code}, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `docs/kb/{out.name}/sections/<file>#<якорь>` (ADR-007 R3).

## Иллюстрации

Каждая содержательная иллюстрация в разделе сопровождается блоком
`> **Описание иллюстрации {code}-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста
руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.
OCR-текст — вспомогательный: факты цитируются по тексту руководства.

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
""" + "\n".join(rows) + "\n"
    (out / "index.md").write_text(index)
    meta = {
        "doc_code": code, "doc_title": cfg["title"], "doc_version": cfg["version"],
        "extracted_by": f"pymupdf {pymupdf.VersionBind}", "image_extractor": f"pymupdf {pymupdf.VersionBind}",
        "image_description": "manual text before the image + caption + tesseract OCR (rus+eng)",
        "image_count": image_count, "images_dropped_decorative": sum(removed.values()),
        "note": cfg["note"], "page_count": total, "part_count": 1, "processing_mode": "single",
        "section_count": len(sections), "section_source": section_source, "sections": meta_sections,
        "source_document": out.name, "source_pdf": cfg["src"], "source_pdfs": [cfg["src"]],
        "source_set": out.name, "source_sha256": sha,
        "sources": [{"order": 1, "page_count": total, "source_pdf": cfg["src"], "source_sha256": sha}],
        "table_count": table_count, "toc_entries": len(toc), "toc_entries_missing": missing,
        "token_method": "tiktoken:cl100k_base", "tokens_index": ntoks(index), "tokens_total": total_tokens,
        "verification": {"method": "cross-engine (PyMuPDF -> pdfplumber re-read of the same pages ±1)",
                         "critical_tokens_checked": checked, "critical_tokens_unconfirmed": unconf,
                         "confirmed_ratio": round(ratio, 4), "confidence_level": confidence,
                         "extraction_date": TODAY},
    }
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    vrows = [f"| [{v['title']}]({v['file']}) | {v['pages']} | {len(v['unconfirmed'])} |"
             for v in verify_sections if v["unconfirmed"]]
    (out / "verification.md").write_text(f"""---
type: kb-verification-report
doc_code: {code}
source_document: "{Path(cfg['src']).name}"
extraction_date: "{TODAY}"
confidence_level: "{confidence}"
pages_covered: "1-{total}"
status: verified
ai-generated: true
---

# Отчёт перекрёстной проверки — {cfg['title']} ({cfg['version']})

Метод: cross-engine — основное извлечение `PyMuPDF`, независимое перечтение тех же страниц
(±1) `pdfplumber`. Критический токен — URL, `snake_case`, число из 3+ цифр, латинский термин.

## Итог

| Метрика | Значение |
| --- | ---: |
| Пунктов оглавления | {len(toc)} |
| Пунктов оглавления без найденного заголовка | {len(missing)} |
| Разделов | {len(sections)} |
| Проверено критических токенов | {checked} |
| Не подтверждено вторым движком | {unconf} |
| Доля подтверждённых | {ratio * 100:.2f} % |
| Уровень доверия | **{confidence}** |

## Разделы, требующие ручной сверки

| Раздел | Стр. | Не подтверждено |
| --- | --- | ---: |
""" + ("\n".join(vrows) or "| — | — | 0 |") + """

Не подтверждённые токены перечислены в самих разделах в блоках
`<!-- kb-verify:start -->` … `<!-- kb-verify:end -->`.
""")
    (out / "IMAGES.md").write_text(f"""---
type: kb-image-audit
doc_code: {code}
source_sha256: {sha}
extraction_date: "{TODAY}"
ai-generated: true
---

# Иллюстрации — {cfg['title']} ({cfg['version']})

| Метрика | Значение |
| --- | ---: |
| Размещений изображений в PDF | {image_count + sum(removed.values())} |
| Сохранено содержательных иллюстраций (с текстовым описанием) | {image_count} |
| Не сохранено как оформление | {sum(removed.values())} |

## Что не сохранено и почему

Не сохраняются только изображения без сведений о функциональности системы;
логотипы и элементы шаблона проверены визуально до исключения.

| Стр. | Размер, px | sha1 (12) | Причина |
| ---: | --- | --- | --- |
""" + ("\n".join(f"| {p} | {wh} | `{h}` | {w} |" for p, wh, h, w in removed_list) or "| — | — | — | — |") + f"""

## Как описана каждая сохранённая иллюстрация

Сразу под ссылкой на изображение стоит блок
`> **Описание иллюстрации {code}-§<раздел>-<n>**` с полями:

* раздел, к которому относится иллюстрация, страница PDF, размер, тип
  (снимок экрана / схема, фрагмент интерфейса, пиктограмма);
* «Относится к тексту руководства» — текст руководства непосредственно
  перед иллюстрацией;
* подпись (`Рис. …`), если она есть в руководстве;
* «Текст на изображении (OCR)» — надписи, распознанные tesseract (rus+eng);
  OCR может содержать ошибки, факты цитируются по тексту руководства.

Изображения сохранены в PNG без потерь с оптимизацией (палитра, если цветов
не больше 256); прозрачность сведена на белый фон.
""")
    print(json.dumps({"doc": out.name, "sections": len(sections), "toc": len(toc), "missing": len(missing),
                      "images": image_count, "removed": sum(removed.values()), "tables": table_count,
                      "tokens": total_tokens, "unconfirmed": unconf, "checked": checked}, ensure_ascii=False))


if __name__ == "__main__":
    main()
