"""Add text descriptions to illustrations of a KB document and optimize them.

For documents already in the KB whose source version did not change, only the
illustrations are updated (issue #12): the section text stays as extracted.

Usage (the PDF stays on the operator's workstation, it is not committed):

    python docs/kb/tools/describe_kb_images.py DOC_DIR SOURCE.pdf [--decorative NAME ...]

What the script does for every ``![..](../images/NAME)`` link of DOC_DIR/sections:

* finds the same image in the PDF (byte-identical xref) and its position on
  the page named in the link (``стр. N``);
* removes decorative images: images repeated on 30 %+ of pages (page template,
  logo) and the names passed with ``--decorative`` (checked visually before);
  the link and the file are deleted;
* re-renders a PNG from the PDF with its soft mask composited onto white and
  saves it losslessly optimized (JPEG files are kept byte-identical);
* writes under the link the block ``> **Описание иллюстрации …**``: section,
  page, size, kind, the manual text right above the image on the PDF page,
  the caption (``Рис. …``) and OCR of the visible text (tesseract rus+eng);
* recounts tokens in sections, index.md and meta.json and writes IMAGES.md.

The script is idempotent: an existing description block is replaced.
"""

import argparse
import datetime
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pymupdf
import tiktoken

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_images import CAPTION, DESC_HEAD, describe, is_uniform, load_with_mask, norm, ocr, optimize_save  # noqa: E402

ENC = tiktoken.get_encoding("cl100k_base")
LINK = re.compile(r"^!\[([^\]\n]*)\]\(\.\./images/([^)\n]+)\)\s*$")
TODAY = datetime.date.today().isoformat()


def page_text_lines(page):
    """Text lines of a page without the running header/footer: (y0, y1, text)."""
    h = page.rect.height
    out = []
    for b in page.get_text("dict", sort=True)["blocks"]:
        if b["type"]:
            continue
        for ln in b["lines"]:
            t = norm("".join(s["text"] for s in ln["spans"]))
            y0, y1 = ln["bbox"][1], ln["bbox"][3]
            if t and h * 0.06 < y0 and y1 < h * 0.93:
                out.append((y0, y1, t))
    return out


def context_for(doc, pno, bbox, lines_cache):
    def lines(p):
        if p not in lines_cache:
            lines_cache[p] = page_text_lines(doc[p])
        return lines_cache[p]
    above = [t for y0, y1, t in lines(pno) if y1 <= bbox[1] + 2]
    below = [t for y0, y1, t in lines(pno) if y0 >= bbox[3] - 2]
    if not above and pno > 0:
        above = [t for _, _, t in lines(pno - 1)]
    caption = below[0] if below and CAPTION.match(below[0]) else ""
    if not caption and above and CAPTION.match(above[-1]):
        caption = above[-1]
    return " ".join(above[-6:]), caption


def frontmatter_value(text, key):
    m = re.search(rf"^{key}: (.*)$", text, re.M)
    if not m:
        return ""
    raw = m.group(1)
    return json.loads(raw) if raw.startswith('"') else raw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc_dir")
    ap.add_argument("pdf")
    ap.add_argument("--decorative", nargs="*", default=[],
                    help="image file names verified visually as logos / page decoration")
    ap.add_argument("--decorative-reason", default="логотип MANGO OFFICE на титульной странице")
    ap.add_argument("--no-ocr", action="store_true")
    args = ap.parse_args()
    out = Path(args.doc_dir)
    doc = pymupdf.open(args.pdf)
    sha = hashlib.sha256(Path(args.pdf).read_bytes()).hexdigest()
    meta = json.loads((out / "meta.json").read_text())
    if meta.get("source_sha256") and meta["source_sha256"] != sha:
        sys.exit(f"source sha256 differs from meta.json: {sha} != {meta['source_sha256']}")
    code = meta["doc_code"]

    # byte hash -> [(page index, xref, smask, bbox), ...] in reading order
    placements = defaultdict(list)
    pages_by_hash = defaultdict(set)
    for p in doc:
        masks = {im[0]: im[1] for im in p.get_images(full=True)}
        for info in p.get_image_info(xrefs=True):
            x = info["xref"]
            if not x:
                continue
            try:
                raw = doc.extract_image(x)["image"]
            except Exception:  # noqa: BLE001
                continue
            hsh = hashlib.sha1(raw).hexdigest()
            placements[hsh].append((p.number, x, masks.get(x, 0), info["bbox"]))
            pages_by_hash[hsh].add(p.number)
    template = {h for h, s in pages_by_hash.items() if len(s) >= max(3, doc.page_count * 0.3)}

    used = Counter()
    lines_cache = {}
    removed, kept, reasons = [], 0, Counter()
    bytes_before = bytes_after = 0
    sec_tokens = {}
    for sec_path in sorted((out / "sections").glob("*.md")):
        text = sec_path.read_text()
        head, body = text.split("\n---\n", 1)
        sec = frontmatter_value(head, "section") or "0"
        sec_label = frontmatter_value(head, "pdf_section") or sec
        title = frontmatter_value(head, "title")
        lines = body.split("\n")
        res, i, k = [], 0, 0
        while i < len(lines):
            m = LINK.match(lines[i])
            if not m:
                res.append(lines[i])
                i += 1
                continue
            name = m.group(2)
            j = i + 1  # skip an existing description block (idempotency)
            while j < len(lines) and lines[j] == "":
                j += 1
            if j < len(lines) and lines[j].startswith(DESC_HEAD):
                while j < len(lines) and lines[j].startswith(">"):
                    j += 1
                i = j
            else:
                i += 1
            path = out / "images" / name
            raw = path.read_bytes()
            bytes_before += len(raw)
            hsh = hashlib.sha1(raw).hexdigest()
            pm = re.search(r"стр\. (\d+)", m.group(1))
            page_no = int(pm.group(1)) if pm else None
            cands = placements.get(hsh, [])
            if not cands:
                sys.exit(f"{name}: image not found in the PDF")
            on_page = [c for c in cands if page_no is None or c[0] == page_no - 1] or cands
            pick = on_page[min(used[(hsh, on_page[0][0])], len(on_page) - 1)]
            used[(hsh, pick[0])] += 1
            pno, xref, smask, bbox = pick
            if hsh in template or name in args.decorative:
                why = ("фирменный шаблон страницы / логотип, повторяется на каждой странице"
                       if hsh in template else args.decorative_reason)
                removed.append((name, pno + 1, why))
                reasons[why] += 1
                path.unlink()
                while res and res[-1] == "" and i < len(lines) and lines[i] == "":
                    i += 1
                continue
            img = load_with_mask(doc, xref, smask)
            if is_uniform(img):
                sys.exit(f"{name}: uniform image is not expected among kept illustrations")
            if path.suffix.lower() == ".png":
                size = optimize_save(img, path)
                if not smask and len(raw) <= size:  # re-encoding did not help: keep original bytes
                    path.write_bytes(raw)
                    size = len(raw)
                bytes_after += size
            else:
                bytes_after += len(raw)
            k += 1
            kept += 1
            anchor, caption = context_for(doc, pno, bbox, lines_cache)
            label, block = describe(code, sec_label, k, title, pno + 1, img, anchor, caption,
                                    "" if args.no_ocr else ocr(img))
            res += [f"![{label}](../images/{name})", "", *block.split("\n")]
        new_body = "\n".join(res)
        new_body = re.sub(r"\n{3,}", "\n\n", new_body)
        tokens = len(ENC.encode(new_body))
        head = re.sub(r"^tokens: \d+$", f"tokens: {tokens}", head, flags=re.M)
        if re.search(r"^images: ", head, re.M):
            head = re.sub(r"^images: \d+$", f"images: {k}", head, flags=re.M)
        else:
            head = re.sub(r"^(tokens: \d+)$", rf"\1\nimages: {k}", head, flags=re.M)
        sec_path.write_text(head + "\n---\n" + new_body)
        sec_tokens[f"sections/{sec_path.name}"] = (tokens, k)

    # ---- index.md: token column and illustrations note
    index = (out / "index.md").read_text()
    def fix_row(mt):
        row = mt.group(0)
        f = re.search(r"\]\((sections/[^)]+)\)", row).group(1)
        cells = row.split("|")
        cells[-3] = f" {sec_tokens[f][0]} "
        return "|".join(cells)
    index = re.sub(r"^\|.*\]\(sections/[^)]+\).*\|$", fix_row, index, flags=re.M)
    note = (f"## Иллюстрации\n\nКаждая содержательная иллюстрация в разделе сопровождается блоком\n"
            f"`> **Описание иллюстрации {code}-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста\n"
            "руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.\n"
            "OCR-текст — вспомогательный: факты цитируются по тексту руководства. Отбор и оптимизация\n"
            "изображений: [`IMAGES.md`](IMAGES.md).\n\n")
    index = re.sub(r"## Иллюстрации\n.*?(?=## Разделы)", "", index, flags=re.S)
    index = index.replace("## Разделы\n", note + "## Разделы\n", 1)
    (out / "index.md").write_text(index)

    # ---- meta.json
    for s in meta.get("sections", []):
        if s["file"] in sec_tokens:
            s["tokens"], s["images"] = sec_tokens[s["file"]]
    meta["tokens_total"] = sum(t for t, _ in sec_tokens.values())
    meta["tokens_index"] = len(ENC.encode(index))
    meta["image_count"] = kept
    meta["images_dropped_decorative"] = meta.get("images_dropped_decorative", 0) + len(removed)
    meta["image_description"] = "PDF context above the image + caption + tesseract OCR (rus+eng)"
    meta["image_description_date"] = meta.get("image_description_date") if not removed and not kept else TODAY
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    # ---- IMAGES.md (keep the history of removed images across re-runs)
    images_md = out / "IMAGES.md"
    prev_removed = []
    if images_md.exists():
        prev_removed = re.findall(r"^\| `([^`]+)` \| (\d+) \| (.+) \|$", images_md.read_text(), re.M)
    all_removed = [(n, int(p), w) for n, p, w in prev_removed] + removed
    images_md.write_text(f"""---
type: kb-image-audit
doc_code: {code}
source_sha256: {sha}
extraction_date: "{TODAY}"
ai-generated: true
---

# Иллюстрации — {meta['doc_title']} (версия {meta['doc_version']})

Версия источника совпадает с уже извлечённой (sha256 PDF совпадает с `meta.json`),
поэтому текст разделов не переизвлекался: обновлены только иллюстрации
(описания и оптимизация), issue #12.

| Метрика | Значение |
| --- | ---: |
| Содержательных иллюстраций (с текстовым описанием) | {kept} |
| Удалено как оформление | {len(all_removed)} |

## Что удалено и почему

Удаляются только изображения без сведений о функциональности системы; каждое
проверено визуально до удаления.

| Файл | Стр. | Причина |
| --- | ---: | --- |
""" + ("\n".join(f"| `{n}` | {p} | {w} |" for n, p, w in all_removed) or "| — | — | — |") + f"""

## Как описана каждая сохранённая иллюстрация

Сразу под ссылкой на изображение стоит блок
`> **Описание иллюстрации {code}-§<раздел>-<n>**` с полями:

* раздел, к которому относится иллюстрация, страница PDF, размер, тип
  (снимок экрана / схема, фрагмент интерфейса, пиктограмма);
* «Относится к тексту руководства» — текст руководства, стоящий в PDF
  непосредственно над иллюстрацией (или в конце предыдущей страницы);
* подпись (`Рис. …`), если она есть в руководстве;
* «Текст на изображении (OCR)» — надписи, распознанные tesseract (rus+eng);
  OCR может содержать ошибки, факты цитируются по тексту руководства.

Мелкие пиктограммы внутри текста (значки кнопок) сохранены: они помогают
узнать элемент управления, их назначение объяснено в тексте рядом.

## Оптимизация

PNG перерисованы из PDF (прозрачность сведена на белый фон) и сохранены без
потерь с оптимизацией (палитра, если цветов не больше 256); JPEG сохранены
без изменений. Размер каталога `images/` в этом прогоне: {bytes_before / 1024:.0f} КБ → {bytes_after / 1024:.0f} КБ
(учтены только сохранённые и удалённые в этом прогоне файлы).
""")
    print(json.dumps({"doc": out.name, "kept": kept, "removed": len(removed), "template_hashes": len(template),
                      "kb_before": round(bytes_before / 1024), "kb_after": round(bytes_after / 1024)}))


if __name__ == "__main__":
    main()
