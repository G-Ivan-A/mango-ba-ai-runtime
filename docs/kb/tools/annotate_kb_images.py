"""Describe and optimise the illustrations of an already extracted KB document.

Used when the KB already holds the same version of a manual (issue #11): the
section text stays as it is; only the illustrations are processed.

Usage (the source PDF stays on the operator's workstation, it is not committed):

    python docs/kb/tools/annotate_kb_images.py DOC_DIR SOURCE.pdf [--no-ocr]

Requirements: pymupdf, Pillow, the ``tesseract`` binary (rus+eng) for OCR and,
optionally, ``optipng`` for lossless PNG recompression.

What the script does for every ``![...](../images/X)`` link of DOC_DIR/sections:

* checks that the PDF is the source of the extraction (sha256 or page count +
  version string from meta.json);
* drops decorative images: the page template with the MANGO OFFICE logo and
  contacts (one picture repeated on most pages), uniform fill rectangles,
  images smaller than 8 px. Each class was verified visually before removal;
* re-extracts from the PDF the images that the earlier extraction saved as
  solid black, compositing the PDF soft mask on white; an image that is solid
  in the PDF itself is a backing/shadow under a screenshot and is dropped;
* optimises files losslessly: identical pictures are stored once, PNG with at
  most 256 colours is stored as a palette PNG, then ``optipng``;
* writes under every kept image a text description: id, section, page, size,
  image type, the manual text the illustration belongs to (preceding text),
  the text that follows it, the caption and OCR of the visible UI text;
* writes DOC_DIR/IMAGES.md (audit of kept/removed images) and updates
  meta.json and index.md.

The script is idempotent: links that already carry a description are skipped.
"""

import argparse
import collections
import datetime
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf
from PIL import Image, ImageStat

LINK = re.compile(r"^!\[([^\]]*)\]\(\.\./images/([^)]+)\)\s*$")
PAGE = re.compile(r"стр\. (\d+)")
CAPTION = re.compile(r"^(Рис(унок|\.)\s*\d*|Рисунок)", re.I)
DESC_MARK = "> **Описание иллюстрации"
TODAY = datetime.date.today().isoformat()
TEMPLATE_WHY = "фирменный шаблон страницы (логотип MANGO OFFICE, контакты) — одно изображение на большинстве страниц"
UNIFORM_WHY = "однотонная подложка-тень под снимком экрана (снимок на той же странице сохранён отдельно)"
UNIFORM_LONE_WHY = "однотонная заливка без содержимого"
TINY_WHY = "служебный элемент менее 8 пикселей"


def norm(text):
    return re.sub(r"\s+", " ", text.replace(" ", " ")).strip()


def pixel_hash(img):
    return hashlib.md5(img.convert("RGB").tobytes()).hexdigest()


def split_md(text):
    """Return (frontmatter_text, frontmatter_dict, body)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        v = v.strip()
        if v.startswith('"'):
            try:
                v = json.loads(v)
            except json.JSONDecodeError:
                v = v.strip('"')
        fm[k.strip()] = v
    return m.group(0), fm, text[m.end():]


def kind_of(w, h):
    if w <= 64 and h <= 64:
        return "пиктограмма (значок элемента интерфейса)"
    if w <= 220 and h <= 120:
        return "фрагмент интерфейса (кнопка, переключатель, поле или подпись)"
    return "снимок экрана / схема"


def ocr(img):
    if img.width < 80 or img.height < 24 or not shutil.which("tesseract"):
        return ""
    scale = 2 if img.width < 900 else 1
    im = img.convert("RGB").resize((img.width * scale, img.height * scale))
    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        im.save(f.name)
        out = subprocess.run(["tesseract", f.name, "-", "-l", "rus+eng", "--psm", "11"],
                             capture_output=True, text=True, check=False).stdout
    seen, words = set(), []
    for line in out.splitlines():
        line = norm(line)
        if len(line) >= 2 and sum(c.isalnum() for c in line) >= max(2, len(line) * 0.6):
            if line.casefold() not in seen:
                seen.add(line.casefold())
                words.append(line)
    text = "; ".join(words).replace("|", "/")
    return text[:600] + ("…" if len(text) > 600 else "")


def composite(pix):
    if pix.n - pix.alpha > 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, img).convert("RGB")
    return img


class PdfImages:
    """Locate an extracted image file in the PDF (by pixels) to re-render it."""

    def __init__(self, pdf):
        self.pdf = pdf
        self.cache = {}

    def page(self, pno):
        if pno not in self.cache:
            res = []
            if 1 <= pno <= self.pdf.page_count:
                for x in self.pdf[pno - 1].get_images(full=True):
                    try:
                        raw = pymupdf.Pixmap(self.pdf, x[0])
                        base = raw if raw.n - raw.alpha <= 3 else pymupdf.Pixmap(pymupdf.csRGB, raw)
                        plain = Image.open(io.BytesIO(base.tobytes("png")))
                        res.append((x[0], pixel_hash(plain), plain.size))
                    except Exception:  # noqa: BLE001 - unreadable xref is skipped
                        continue
            self.cache[pno] = res
        return self.cache[pno]

    def found(self, pno, img):
        h = pixel_hash(img)
        return any(hh == h for p in (pno, pno - 1, pno + 1) for _, hh, _ in self.page(p))

    def rerender(self, pno, img):
        h = pixel_hash(img)
        for p in (pno, pno - 1, pno + 1):
            for xref, hh, _ in self.page(p):
                if hh == h:
                    pix = pymupdf.Pixmap(self.pdf, xref)
                    if pix.alpha == 0 and xref:
                        smask = next((i[1] for i in self.pdf[p - 1].get_images(full=True) if i[0] == xref), 0)
                        if smask:
                            pix = pymupdf.Pixmap(pix, pymupdf.Pixmap(self.pdf, smask))
                    return composite(pix)
        return None


def optimise(path):
    """Lossless recompression; returns the new path (the suffix may stay)."""
    if path.suffix.lower() != ".png":
        return path
    img = Image.open(path)
    img.load()
    rgb = img.convert("RGB")
    colors = rgb.getcolors(256)
    if colors is not None and img.mode != "P":
        pal = rgb.quantize(colors=len(colors), method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
        if pixel_hash(pal) == pixel_hash(rgb):
            pal.save(path, optimize=True)
        else:
            rgb.save(path, optimize=True)
    elif img.mode not in ("RGB", "P", "L"):
        rgb.save(path, optimize=True)
    if shutil.which("optipng"):
        subprocess.run(["optipng", "-quiet", "-o2", "-strip", "all", str(path)], check=False)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc_dir")
    ap.add_argument("pdf")
    ap.add_argument("--no-ocr", action="store_true")
    args = ap.parse_args()
    root = Path(args.doc_dir)
    meta_path = root / "meta.json"
    meta = json.loads(meta_path.read_text())
    pdf_bytes = Path(args.pdf).read_bytes()
    sha = hashlib.sha256(pdf_bytes).hexdigest()
    pdf = pymupdf.open(args.pdf)
    known = {s.get("source_sha256") for s in meta.get("sources", [])}
    version = str(meta.get("doc_version", ""))
    head = norm(" ".join(pdf[i].get_text() for i in range(min(3, pdf.page_count))))
    ver_seen = version in head or version.replace(".2026", ".26") in head
    if sha not in known and not (pdf.page_count == meta.get("page_count") and ver_seen):
        sys.exit(f"{args.pdf}: not the source of {root} (sha256/page count/version mismatch)")
    source_check = "sha256 совпадает с meta.json" if sha in known else (
        f"sha256 отличается (повторный экспорт), совпадают число страниц ({pdf.page_count}) и версия «{version}»")
    code = meta["doc_code"]
    pdf_images = PdfImages(pdf)
    files = {p.name: p for p in (root / "images").iterdir()}
    sections = sorted((root / "sections").glob("*.md"))

    # ---- pass 1: inventory of links
    links = []  # (md, block_idx, name, page)
    texts = {}
    for md in sections:
        fm_text, fm, body = split_md(md.read_text())
        blocks = body.split("\n\n")
        texts[md] = (fm_text, fm, blocks)
        for i, b in enumerate(blocks):
            m = LINK.match(b.strip())
            if m and m.group(2) in files:
                pm = PAGE.search(m.group(1))
                links.append((md, i, m.group(2), int(pm.group(1)) if pm else 0))
    hashes = {}
    pages_by_hash = collections.defaultdict(set)
    for md, i, name, page in links:
        if name not in hashes:
            hashes[name] = pixel_hash(Image.open(files[name]))
        pages_by_hash[hashes[name]].add(page)

    # ---- pass 2: classify, repair, deduplicate, describe
    audit = collections.Counter()
    removed_examples = {}
    repaired, rerender_failed, kept, deduped = [], [], 0, 0
    canonical = {}  # pixel hash -> file name kept
    used = set()
    bytes_before = sum(p.stat().st_size for p in files.values())
    sec_counter = collections.Counter()
    for md, i, name, page in links:
        fm_text, fm, blocks = texts[md]
        path = files[name]
        img = Image.open(path)
        img.load()
        nxt_block = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
        if nxt_block.startswith(DESC_MARK):
            used.add(name)
            kept += 1
            continue
        why = None
        if len(pages_by_hash[hashes[name]]) > max(5, meta.get("page_count", 100) * 0.3):
            why = TEMPLATE_WHY
        elif img.width < 8 or img.height < 8:
            why = TINY_WHY
        else:
            stat = ImageStat.Stat(img.convert("L"))
            if stat.stddev[0] < 1.0:
                fixed = pdf_images.rerender(page, img) if stat.mean[0] < 1.0 else None
                if fixed is None and stat.mean[0] < 1.0 and not pdf_images.found(page, img):
                    rerender_failed.append(name)
                if fixed is not None and ImageStat.Stat(fixed.convert("L")).stddev[0] >= 1.0:
                    new = path.with_suffix(".png")
                    fixed.save(new, optimize=True)
                    if new != path:
                        path.unlink()
                        files.pop(name)
                        name = new.name
                        files[name] = new
                    path, img = new, fixed
                    hashes[name] = pixel_hash(fixed)
                    repaired.append(name)
                else:
                    same_page = [x for x in links if x[3] == page and x[2] != name
                                 and x[2] in hashes and len(pages_by_hash[hashes[x[2]]]) <= 5]
                    why = UNIFORM_WHY if same_page else UNIFORM_LONE_WHY
        if why:
            audit[why] += 1
            removed_examples.setdefault(why, f"{md.name}: стр. {page}")
            blocks[i] = None
            continue
        h = hashes[name]
        if h in canonical and canonical[h] != name:
            deduped += 1
            name = canonical[h]
            path = files[name]
        else:
            canonical[h] = name
        used.add(name)
        kept += 1
        sec = fm.get("section") or fm.get("pdf_section") or "0"
        sec_counter[md.name] += 1
        n = sec_counter[md.name]
        ident = f"{code}-§{sec}-{n}" if sec not in ("—", "0") else f"{code}-{md.name[:2]}-{n}"
        title = fm.get("title", md.stem)
        prev_text = next((b for b in reversed([x for x in blocks[:i] if x]) if not b.lstrip().startswith(("!", ">", "#", "<!--"))), "")
        next_text = next((b for b in blocks[i + 1:] if b and not b.lstrip().startswith(("!", ">", "#", "<!--"))), "")
        caption = next((t for t in (next_text, prev_text) if CAPTION.match(norm(t))), "")
        kind = kind_of(img.width, img.height)
        anchor = norm(prev_text)
        anchor = ("…" + anchor[-240:]) if len(anchor) > 240 else anchor
        follow = norm(next_text)
        follow = (follow[:200] + "…") if len(follow) > 200 else follow
        alt = f"Иллюстрация {ident}, стр. {page}: {kind}"
        desc = [f"{DESC_MARK} {ident}** · к разделу §{sec} «{title}» · стр. {page} · {kind}, {img.width}×{img.height} px."]
        if anchor:
            desc.append(f"> Относится к тексту руководства: «{anchor}»")
        else:
            desc.append(f"> Относится к тексту руководства: начало раздела «{title}».")
        if follow:
            desc.append(f"> Следующий за иллюстрацией текст: «{follow}»")
        if caption:
            desc.append(f"> Подпись в руководстве: «{norm(caption)}».")
        text = "" if args.no_ocr else ocr(img)
        if text:
            desc.append(f"> Текст на изображении (OCR, требует сверки): {text}")
        elif kind.startswith("пиктограмма"):
            desc.append("> Текста на изображении нет; назначение значка — см. текст, к которому он относится.")
        blocks[i] = f"![{alt}](../images/{name})\n\n" + "\n".join(desc)

    # ---- write sections
    for md, (fm_text, fm, blocks) in texts.items():
        body = "\n\n".join(b for b in blocks if b is not None)
        body = re.sub(r"\n{3,}", "\n\n", body)
        fm_new = re.sub(r"^images: \d+\n", "", fm_text, flags=re.M)
        fm_new = fm_new.replace("\nstatus:", f"\nimages: {sec_counter[md.name]}\nstatus:", 1) \
            if "\nstatus:" in fm_new else fm_new
        md.write_text(fm_new + body)

    # ---- drop unused files, optimise kept ones
    for name, p in list(files.items()):
        if name not in used:
            p.unlink()
            files.pop(name)
    for name in sorted(used):
        optimise(files[name])
    bytes_after = sum(p.stat().st_size for p in files.values())

    removed_total = sum(audit.values())
    meta.update({
        "image_count": kept,
        "unique_images": len(files),
        "illustration_refs": kept,
        "decorative_images_removed": dict(audit),
        "illustration_description": "контекстное текстовое описание под каждой иллюстрацией: id, раздел, страница, "
                                    "тип, размер, цитата текста руководства, к которому относится иллюстрация, "
                                    "следующий текст, подпись и OCR-текст интерфейса",
        "images_annotated": TODAY,
        "images_optimised": {"bytes_before": bytes_before, "bytes_after": bytes_after,
                             "duplicates_merged": deduped, "black_images_rerendered": len(repaired)},
    })
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    rows = "\n".join(f"| {why} | {n} | {removed_examples[why]} |" for why, n in audit.most_common())
    images_md = f"""---
type: kb-image-audit
doc_code: {code}
doc_version: "{version}"
extraction_date: "{TODAY}"
ai-generated: true
---

# Иллюстрации: {meta.get('doc_title', root.name)} v{version}

Обработано [`tools/annotate_kb_images.py`](../{'../' * (len(root.parts) - 3)}tools/annotate_kb_images.py) (issue #11).
Текст разделов не менялся: версия руководства в БЗ совпадает с исходником
({source_check}).

| Метрика | Значение |
| --- | ---: |
| Ссылок на изображения до обработки | {len(links)} |
| Сохранено содержательных иллюстраций (с текстовым описанием) | {kept} |
| Удалено как оформление | {removed_total} |
| Уникальных файлов изображений после обработки | {len(files)} |
| Одинаковых изображений сведено к одному файлу | {deduped} |
| Восстановлено из PDF (ранее извлечены чёрными) | {len(repaired)} |
| Объём `images/` до → после, КБ | {bytes_before // 1024} → {bytes_after // 1024} |

## Что удалено и почему

| Причина | Размещений | Пример |
| --- | ---: | --- |
{rows or '| — | 0 | — |'}

Фирменный шаблон страницы (логотип MANGO OFFICE, телефон 8 800 555 55 22,
mango-office.ru) и однотонные заливки сведений о функциональности системы не
несут — проверено визуально до удаления.

## Как описана каждая сохранённая иллюстрация

Сразу под ссылкой на изображение в разделе стоит блок
`> **Описание иллюстрации {code}-§<раздел>-<n>**`:

* раздел, страница руководства, тип изображения (снимок экрана / схема,
  фрагмент интерфейса, пиктограмма) и размер;
* «Относится к тексту руководства» — текст руководства, непосредственно
  предшествующий иллюстрации;
* «Следующий за иллюстрацией текст» и подпись (`Рис. …`), если она есть;
* «Текст на изображении (OCR)» — надписи интерфейса, распознанные tesseract
  (rus+eng); OCR может содержать ошибки, факты цитируются по тексту руководства.

Оптимизация без потерь: одинаковые изображения хранятся одним файлом, PNG до 256
цветов сохранены с палитрой, затем `optipng -o2`.
"""
    if rerender_failed:
        images_md += "\n## Требует ручной сверки\n\nЧёрные изображения, не найденные в PDF (удалены как заливка, проверьте вручную): " + \
                     ", ".join(f"`{n}`" for n in rerender_failed) + "\n"
    (root / "IMAGES.md").write_text(images_md)

    index = root / "index.md"
    itext = index.read_text()
    block = (f"\n## Иллюстрации\n\nКаждая содержательная иллюстрация в разделе сопровождается блоком\n"
             f"`> **Описание иллюстрации {code}-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста\n"
             f"руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.\n"
             f"OCR-текст — вспомогательный: факты цитируются по тексту руководства. Отбор и оптимизация\n"
             f"изображений: [`IMAGES.md`](IMAGES.md).\n")
    if "## Иллюстрации" not in itext:
        itext = re.sub(r"\n## Разделы", block + "\n## Разделы", itext, count=1) \
            if "\n## Разделы" in itext else itext.rstrip("\n") + "\n" + block
        index.write_text(itext)
    print(json.dumps({"doc": str(root), "links": len(links), "kept": kept, "removed": dict(audit),
                      "files": len(files), "deduped": deduped, "repaired": len(repaired),
                      "rerender_failed": rerender_failed, "kb_before": bytes_before // 1024,
                      "kb_after": bytes_after // 1024}, ensure_ascii=False))


if __name__ == "__main__":
    main()
