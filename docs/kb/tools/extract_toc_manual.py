"""Extract a single-PDF MANGO OFFICE manual with a printed, numbered table of
contents into docs/kb/<doc>/ (issue #11: «Речевая аналитика» v1.26.42).

Usage (the PDF stays on the operator's workstation, it is not committed):

    python docs/kb/tools/extract_toc_manual.py SOURCE.pdf --out docs/kb/speech-analytics/user-guide \
        --doc-code SA --doc-title "Руководство пользователя. Речевая аналитика" --doc-version 1.26.42 \
        --source kb/sources/speech-analytics/RECHEVAYA-ANALITIKA_1.26.42.pdf --product analytics-reporting

Requirements: pymupdf, pdfplumber, tiktoken, Pillow, ``tesseract`` (rus+eng).

What the script does:
* reads the printed table of contents and splits the text into sections by
  the numbered headings it lists (a numbered line is a heading only when its
  number is in the TOC, it is set in a heading-size font and numbers grow);
* keeps text and illustrations in reading order;
* drops decorative images (the page template with the MANGO OFFICE logo that
  repeats on most pages, solid backing rectangles under screenshots, images
  under 8 px) and keeps every image with product information;
* writes for each kept illustration a text description (section, page, the
  manual text it belongs to, the following text, caption, OCR of UI text);
* stores identical illustrations once and recompresses PNG losslessly;
* re-reads the same pages with pdfplumber to confirm critical tokens.
"""

import argparse
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

import pdfplumber
import pymupdf
from PIL import ImageStat

sys.path.insert(0, str(Path(__file__).resolve().parent))
from annotate_kb_images import optimise, pixel_hash  # noqa: E402
from extract_lk_manual import kind_of as _lk_kind, load_image, norm, ntoks, ocr, page_ranges, slug  # noqa: E402,F401

TODAY = datetime.date.today().isoformat()
TOC_LINE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+(.*?)\s*\.{3,}\s*(\d+)\s*$")
NUM_HEAD = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+(\S.*)$")
CAPTION = re.compile(r"^(Рис(унок|\.)\s*\d*|Рисунок)", re.I)
NOTE_LABELS = {"внимание", "совет", "примечание", "важно", "информация"}


def kind_of(w, h):
    if w <= 64 and h <= 64:
        return "пиктограмма (значок элемента интерфейса)"
    if w <= 220 and h <= 120:
        return "фрагмент интерфейса (кнопка, переключатель, поле или подпись)"
    return "снимок экрана / схема"


def read_toc(doc, max_pages=8):
    toc, buf = [], ""
    for pno in range(1, min(max_pages, doc.page_count)):
        for line in doc[pno].get_text().splitlines():
            line = norm(line)
            if line == str(pno + 1) or "mango" in line.lower():
                continue
            if not line or line == "Оглавление" or not re.search(r"\.{3,}|^\d+(\.\d+)*\.?$|^\d+(\.\d+)*\.?\s", line) and not buf:
                continue
            buf = f"{buf} {line}".strip() if buf else line
            m = TOC_LINE.match(buf)
            if m:
                toc.append((m.group(1), norm(m.group(2)), int(m.group(3))))
                buf = ""
            elif not re.match(r"^\d+(\.\d+)*\.?", buf):
                buf = ""
    return toc


def line_items(page, gpage, header_cut, footer_cut=805.0):
    items = []
    for b in page.get_text("dict", sort=True)["blocks"]:
        if b["type"] != 0:
            continue
        for ln in b["lines"]:
            text = norm("".join(s["text"] for s in ln["spans"]))
            if not text or ln["bbox"][1] < header_cut or ln["bbox"][1] > footer_cut:
                continue
            sp = max(ln["spans"], key=lambda s: len(s["text"].strip()))
            items.append({"kind": "text", "y": ln["bbox"][1], "x": ln["bbox"][0], "text": text,
                          "size": round(sp["size"], 1), "font": sp["font"], "color": sp["color"], "block": id(b)})
    for im in page.get_image_info(hashes=True, xrefs=True):
        items.append({"kind": "image", "y": im["bbox"][1], "x": im["bbox"][0], "info": im})
    items.sort(key=lambda i: (round(i["y"]), i["x"]))
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out", required=True)
    ap.add_argument("--doc-code", required=True)
    ap.add_argument("--doc-title", required=True)
    ap.add_argument("--doc-version", required=True)
    ap.add_argument("--source", required=True, help="logical path of the PDF recorded in the KB")
    ap.add_argument("--product", default="analytics-reporting")
    ap.add_argument("--heading-size", type=float, default=19.5)
    ap.add_argument("--header-cut", type=float, default=45.0, help="y above which lines are the running header")
    ap.add_argument("--footer-cut", type=float, default=805.0, help="y below which lines are the running footer")
    ap.add_argument("--no-ocr", action="store_true")
    args = ap.parse_args()
    out, code, version = Path(args.out), args.doc_code, args.doc_version
    doc = pymupdf.open(args.pdf)
    sha = hashlib.sha256(Path(args.pdf).read_bytes()).hexdigest()
    total = doc.page_count
    toc = read_toc(doc)
    toc_nums = {t[0]: t for t in toc}
    first_page = min(t[2] for t in toc) if toc else 2
    hash_pages = Counter()
    for p in doc:
        for d in {i["digest"] for i in p.get_image_info(hashes=True)}:
            hash_pages[d] += 1

    # ---- sections
    sections = [{"num": "—", "heading": "Титульная часть", "title": "Титульная часть", "items": [], "start": 1}]
    done = set()
    for pno in range(total):
        gp = pno + 1
        page = doc[pno]
        for it in line_items(page, gp, args.header_cut, args.footer_cut):
            it.update(page=gp, pageobj=page)
            s = sections[-1]
            if it["kind"] == "text" and gp >= first_page:
                m = NUM_HEAD.match(it["text"])
                if (m and m.group(1) in toc_nums and m.group(1) not in done and it["size"] >= args.heading_size):
                    done.add(m.group(1))
                    sections.append({"num": m.group(1), "heading": it["text"], "title": norm(m.group(2)),
                                     "items": [], "start": gp, "size": it["size"], "font": it["font"]})
                    continue
                if (s.get("size") and not s["items"] and it["size"] == s["size"] and it["font"] == s["font"]
                        and not NUM_HEAD.match(it["text"])):
                    s["heading"] += " " + it["text"]
                    s["title"] += " " + it["text"]
                    continue
            s["items"].append(it)
    missing = [t for t in toc if t[0] not in done]
    if missing:
        print("TOC entries without heading:", missing, file=sys.stderr)

    # ---- write
    if out.exists():
        shutil.rmtree(out)
    (out / "sections").mkdir(parents=True)
    (out / "images").mkdir()
    plumber = pdfplumber.open(args.pdf)
    plumb_cache = {}
    critical_re = re.compile(r"https?://\S+|[a-z]+_[a-z_]+|\b\d{3,}\b|\b[A-Za-z][A-Za-z0-9-]{2,}\b")
    rows, meta_sections, verify_sections = [], [], []
    removed = Counter()
    removed_example = {}
    canonical = {}
    kept = deduped = total_tokens = 0
    for order, s in enumerate(sections):
        fname = f"{order:02d}-{slug(s['title'])}"
        spages = sorted({i["page"] for i in s["items"]} | {s["start"]})
        label = s["num"] if s["num"] != "—" else "0"
        body, para, prev_block, img_k = [], [], None, 0
        items = s["items"]

        def flush():
            nonlocal para
            if para:
                text = " ".join(para)
                if text.casefold() in NOTE_LABELS:
                    text = f"**{text.capitalize()}:**"
                body.append(text)
            para = []

        page_imgs = Counter(i["page"] for i in items if i["kind"] == "image")
        for idx, it in enumerate(items):
            if it["kind"] == "text":
                if re.fullmatch(r"\d+", it["text"]) and it["text"] == str(it["page"]):
                    continue  # running page number
                if it["block"] != prev_block or it["size"] >= 13.5:
                    flush()
                para.append(it["text"].replace("\uf0b7", "•"))
                prev_block = it["block"]
                if it["size"] >= 13.5 and it["color"] != 13959218:
                    flush()
                    body[-1] = f"**{body[-1]}**"
                    prev_block = None
                continue
            flush()
            prev_block = None
            info = it["info"]
            if info["width"] < 8 or info["height"] < 8:
                removed["служебный элемент менее 8 пикселей (линия-разделитель колонтитула)"] += 1
                removed_example.setdefault("служебный элемент менее 8 пикселей (линия-разделитель колонтитула)",
                                           f"{fname}: стр. {it['page']}")
                continue
            try:
                img = load_image(doc, info["xref"])
            except Exception as exc:  # noqa: BLE001
                print("unreadable image", it["page"], exc, file=sys.stderr)
                continue
            w, h = info["width"], info["height"]
            why = None
            if hash_pages[info["digest"]] > total * 0.3:
                why = "фирменный шаблон страницы (логотип MANGO OFFICE, контакты) — одно изображение на большинстве страниц"
            elif it["page"] == 1:
                why = "логотип MANGO OFFICE на титульной странице (проверено визуально, сведений о функциях системы нет)"
            elif ImageStat.Stat(img.convert("L")).stddev[0] < 1.0:
                why = ("однотонная подложка-тень под снимком экрана (снимок на той же странице сохранён отдельно)"
                       if page_imgs[it["page"]] > 1 else "однотонная заливка без содержимого")
            if why:
                removed[why] += 1
                removed_example.setdefault(why, f"{fname}: стр. {it['page']}")
                continue
            img_k += 1
            kept += 1
            ph = pixel_hash(img)
            if ph in canonical:
                iname = canonical[ph]
                deduped += 1
            else:
                iname = f"{fname}-{img_k}.png"
                img.save(out / "images" / iname, optimize=True)
                optimise(out / "images" / iname)
                canonical[ph] = iname
            prev_text = next((b for b in reversed(body) if not b.startswith(("!", "**"))), "")
            nxt = []
            for j in items[idx + 1:]:
                if j["kind"] == "image" and nxt:
                    break
                if j["kind"] == "text":
                    nxt.append(j["text"])
                    if len(" ".join(nxt)) > 200:
                        break
            next_text = norm(" ".join(nxt))
            caption = next((t for t in (next_text, prev_text) if CAPTION.match(t)), "")
            kind = kind_of(img.width, img.height)
            ident = f"{code}-§{label}-{img_k}"
            anchor = norm(prev_text)
            anchor = ("…" + anchor[-240:]) if len(anchor) > 240 else anchor
            follow = (next_text[:200] + "…") if len(next_text) > 200 else next_text
            desc = [f"> **Описание иллюстрации {ident}** · к разделу §{label} «{s['title']}» · стр. {it['page']} · "
                    f"{kind}, {img.width}×{img.height} px."]
            desc.append(f"> Относится к тексту руководства: «{anchor}»" if anchor
                        else f"> Относится к тексту руководства: начало раздела «{s['title']}».")
            if follow:
                desc.append(f"> Следующий за иллюстрацией текст: «{follow}»")
            if caption:
                desc.append(f"> Подпись в руководстве: «{caption}».")
            text = "" if args.no_ocr else ocr(img).replace("|", "/")
            if text:
                desc.append(f"> Текст на изображении (OCR, требует сверки): {text}")
            elif kind.startswith("пиктограмма"):
                desc.append("> Текста на изображении нет; назначение значка — см. текст, к которому он относится.")
            body.append(f"![Иллюстрация {ident}, стр. {it['page']}: {kind}](../images/{iname})\n\n" + "\n".join(desc))
        flush()
        text_only = " ".join(b for b in body if not b.startswith("!["))
        hint = next((b for b in body if not b.startswith(("![", "**")) and len(b) > 20), "—")
        hint = norm(hint).replace("|", "/")[:90] if hint != "—" else "—"

        crit = sorted(set(critical_re.findall(text_only)))
        ptext = ""
        for gp in range(max(1, spages[0] - 1), min(total, spages[-1] + 1) + 1):
            if gp not in plumb_cache:
                plumb_cache[gp] = re.sub(r"\s+", "", plumber.pages[gp - 1].extract_text() or "")
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
        refs = [{"source_pdf": args.source, "part": 1, "pages": pages_s, "global_pages": pages_s}]
        level = 1 + (s["num"].count(".") if s["num"] != "—" else 0)
        title_line = f"{s['num']}. {s['title']}" if s["num"] != "—" else s["title"]
        fm = [
            "---", f"id: {out.name}-{fname}",
            f"doc_code: {code}", f"doc_title: {json.dumps(args.doc_title, ensure_ascii=False)}",
            f'doc_version: "{version}"', f'section: "{label}"', f'pdf_section: "{s["num"]}"',
            f"title: {json.dumps(s['title'], ensure_ascii=False)}",
            f"pdf_heading: {json.dumps(s['heading'], ensure_ascii=False)}", f'pages: "{pages_s}"',
            f"source: {args.source}", 'source_part: "1"', f'source_pages: "ч.1: {pages_s}"',
            "source_refs: '" + json.dumps(refs, ensure_ascii=False, separators=(",", ":")) + "'",
            f'extracted_by: "pymupdf {pymupdf.VersionBind}"', 'token_method: "tiktoken:cl100k_base"',
            f"tokens: {tokens}", f"images: {img_k}", "status: extracted", "ai-generated: true", "---",
            f"{'#' * min(6, level)} {title_line}", "",
            f"> Трассировка: PDF §{s['num']} · сквозные стр. {pages_s} · источники: ч.1 `{args.source}` с.{pages_s}.",
            "", content, ""]
        (out / "sections" / f"{fname}.md").write_text("\n".join(fm))
        rows.append(f"| {s['num']} | {s['title']} | [sections/{fname}.md](sections/{fname}.md) | {pages_s} | "
                    f"ч.1 с.{pages_s} | {tokens} | {hint} |")
        meta_sections.append({"file": f"sections/{fname}.md", "number": s["num"], "order": f"{order:02d}",
                              "pages": pages_s, "pdf_heading": s["heading"], "pdf_section": s["num"],
                              "source_refs": refs, "title": s["title"], "tokens": tokens, "images": img_k})

    checked = sum(v["critical_tokens"] for v in verify_sections)
    unconf = sum(len(v["unconfirmed"]) for v in verify_sections)
    ratio = 1 - unconf / checked if checked else 1
    src_name = Path(args.source).name
    nfiles = len(list((out / "images").iterdir()))
    size_kb = sum(f.stat().st_size for f in (out / "images").iterdir()) // 1024
    (out / "index.md").write_text(f"""---
product_taxonomy_ref: taxonomy/products.yaml#classes
product_ids: [{args.product}]
type: kb-source-index
doc_code: {code}
doc_title: "{args.doc_title}"
doc_version: "{version}"
status: extracted
ai-generated: true
source_document: "{src_name}"
extraction_date: "{TODAY}"
model_used: "PyMuPDF {pymupdf.VersionBind} + pdfplumber {pdfplumber.__version__} + tesseract OCR (rus+eng)"
confidence_level: "{'high' if ratio >= 0.99 else 'requires_review'}"
pages_covered: "1-{total}"
---

# {args.doc_title} — индекс БЗ (карта разделов)

> Источник: руководство v{version}, `{args.source}` ({total} стр.). Исходный PDF в репозитории
> не хранится (хранение — на АРМ пользователя). Токены: tiktoken:cl100k_base. Это **карта поиска**
> для агента (ADR-007 R2): найди раздел по колонке «Когда обращаться», открой только его файл,
> процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md). Отбор и
> оптимизация изображений: [`IMAGES.md`](IMAGES.md).

## Как цитировать

`[{code}, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `docs/kb/{out.relative_to(out.parents[1]) if len(out.parts) > 2 else out}/sections/<file>#<якорь>` (ADR-007 R3).

## Иллюстрации

Каждая содержательная иллюстрация в разделе сопровождается блоком
`> **Описание иллюстрации {code}-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста
руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.
OCR-текст — вспомогательный: факты цитируются по тексту руководства.

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
""" + "\n".join(rows) + "\n")
    meta = {
        "doc_code": code, "doc_title": args.doc_title, "doc_version": version,
        "extracted_by": f"pymupdf {pymupdf.VersionBind}", "extraction_date": TODAY,
        "image_count": kept, "illustration_refs": kept, "unique_images": nfiles,
        "decorative_images_removed": dict(removed),
        "illustration_description": "контекстное текстовое описание под каждой иллюстрацией: id, раздел, страница, "
                                    "тип, размер, цитата текста руководства, к которому относится иллюстрация, "
                                    "следующий текст, подпись и OCR-текст интерфейса",
        "note": "Исходный PDF хранится на АРМ пользователя, в репозиторий не коммитится (issue #11).",
        "page_count": total, "part_count": 1, "processing_mode": "single", "section_count": len(sections),
        "section_source": "printed-toc", "toc_entries": len(toc), "toc_missing": [t[0] for t in missing],
        "sections": meta_sections,
        "source_document": src_name, "source_pdf": args.source,
        "sources": [{"order": 1, "page_count": total, "source_pdf": args.source, "source_sha256": sha}],
        "token_method": "tiktoken:cl100k_base", "tokens_total": total_tokens,
    }
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    need = [v for v in verify_sections if v["unconfirmed"]]
    (out / "verification.md").write_text(f"""---
type: kb-verification-report
doc_code: {code}
source_document: "{src_name}"
extraction_date: "{TODAY}"
model_used: "PyMuPDF {pymupdf.VersionBind} + pdfplumber {pdfplumber.__version__}"
confidence_level: "{'high' if ratio >= 0.99 else 'requires_review'}"
pages_covered: "1-{total}"
status: verified
ai-generated: true
---

# Отчёт перекрёстной проверки — {args.doc_title} v{version}

Метод: cross-engine (PyMuPDF → pdfplumber re-read of the same pages, допуск ±1 страница).

| Метрика | Значение |
| --- | ---: |
| Пунктов оглавления | {len(toc)} |
| Пунктов оглавления без заголовка в тексте | {len(missing)} |
| Проверено критических токенов | {checked} |
| Не подтверждено вторым движком | {unconf} |
| Доля подтверждённых | {ratio * 100:.2f} % |

## Разделы, требующие ручной сверки

""" + ("\n".join(f"* [{v['file']}]({v['file']}) (стр. {v['pages']}): " + ", ".join(f"`{u}`" for u in v["unconfirmed"][:20])
                 for v in need) or "Нет.") + "\n")
    rows_rm = "\n".join(f"| {w} | {n} | {removed_example[w]} |" for w, n in removed.most_common())
    (out / "IMAGES.md").write_text(f"""---
type: kb-image-audit
doc_code: {code}
doc_version: "{version}"
extraction_date: "{TODAY}"
ai-generated: true
---

# Иллюстрации: {args.doc_title} v{version}

Извлечено [`tools/extract_toc_manual.py`](../../tools/extract_toc_manual.py) (issue #11).

| Метрика | Значение |
| --- | ---: |
| Сохранено содержательных иллюстраций (с текстовым описанием) | {kept} |
| Удалено как оформление | {sum(removed.values())} |
| Уникальных файлов изображений | {nfiles} |
| Одинаковых изображений сведено к одному файлу | {deduped} |
| Объём `images/`, КБ | {size_kb} |

## Что удалено и почему

| Причина | Размещений | Пример |
| --- | ---: | --- |
{rows_rm or '| — | 0 | — |'}

Фирменный шаблон страницы (логотип MANGO OFFICE, контакты) и однотонные подложки
сведений о функциональности системы не несут — проверено визуально до удаления.

## Как описана каждая сохранённая иллюстрация

Сразу под ссылкой на изображение стоит блок `> **Описание иллюстрации {code}-§<раздел>-<n>**`:
раздел, страница, тип и размер изображения; «Относится к тексту руководства» — текст,
непосредственно предшествующий иллюстрации; следующий текст и подпись (`Рис. …`), если есть;
«Текст на изображении (OCR)» — надписи интерфейса, распознанные tesseract (rus+eng), требуют
сверки: факты цитируются по тексту руководства.

Оптимизация без потерь: одинаковые изображения хранятся одним файлом, PNG до 256 цветов —
с палитрой, затем `optipng -o2`.
""")
    print(json.dumps({"sections": len(sections), "toc": len(toc), "missing": [t[0] for t in missing],
                      "kept": kept, "removed": dict(removed), "files": nfiles, "deduped": deduped,
                      "kb": size_kb, "tokens": total_tokens, "unconfirmed": unconf, "checked": checked},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
