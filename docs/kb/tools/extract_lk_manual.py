"""Extract the multi-part LK VATS manual PDF into docs/kb/mango-lk-manual/.

Usage (PDFs stay on the operator's workstation, they are not committed):

    python docs/kb/tools/extract_lk_manual.py PART1.pdf PART2.pdf [--out docs/kb/mango-lk-manual]

Requirements: pymupdf, pdfplumber, tiktoken, Pillow and the ``tesseract``
binary with the ``rus`` and ``eng`` language packs (OCR of illustrations).

What the script does:
* splits the text into sections by numbered PDF headings (the PDF parts have
  no outline), checking that every entry of the printed table of contents
  is found;
* keeps text and illustrations in reading order;
* drops decorative images (the page template with the MANGO OFFICE logo and
  uniform rectangles) and keeps every image that carries product information;
* writes for each kept illustration a text description: section, page,
  the manual text it belongs to, caption and OCR of the visible UI text;
* re-reads the same pages with pdfplumber to confirm critical tokens.
"""

import argparse
import datetime
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

import pdfplumber
import pymupdf
import tiktoken
from PIL import Image, ImageStat

DOC = "mango-lk-manual"
DOC_CODE = "LK"
DOC_TITLE = "Виртуальная АТС MANGO OFFICE - Справочник абонента"
DOC_VERSION = "1.25"
SRC_DIR = f"kb/sources/{DOC}"
SRC_NAMES = ["LK_manual_v-125-1-280.pdf", "LK_manual_v-125-281-566.pdf"]
ENC = tiktoken.get_encoding("cl100k_base")
TODAY = datetime.date.today().isoformat()

NUM_HEAD = re.compile(r"^(\d+(?:\.\d+)+)\.?\s+(\S.*)$")
PART_HEAD = re.compile(r"^Раздел\s+(\d+)\.\s*(.*)$")
TOC_LINE = re.compile(r"^(Раздел\s+\d+\.|\d+(?:\.\d+)*\.?)\s*(.*?)\s*\.{3,}\s*(\d+)\s*$")
CAPTION = re.compile(r"^(Рис(унок|\.)\s*\d*|Рисунок)", re.I)
# Unnumbered headings: the titles the v1.23 PDF outline had as separate
# sections. A line matches only if it is styled as a heading (heading colour,
# bold or a size above body text), so mentions inside body text do not split.
UNNUMBERED = {t.casefold() for t in [
    'Демо-версия ВАТС',
    'Главная страница пользователя',
    'Персональная карточка сотрудника',
    'Виджет «Лента звонков»',
    'Виджет «Сотрудники»',
    'Виджет «Блок кнопок быстрых коммуникаций»',
    'Виджет «Настройки личной защиты»',
    'Виджет «Аналитика»',
    'Виджет «Коллтрекинг»',
    'Виджеты Бухгалтера',
    'Приложение «Личный кабинет»',
    'Начало работы',
    'Блокировка ВАТС',
    'Отчет «Пропущенные звонки»',
    'Отчет «Причины пропущенных звонков»',
    'Отчет «Время ожидания»',
    'Отчет «Длительность разговора»',
    'Отчет «Количество перезвонов по пропущенным звонкам»',
    'Отчет «Насколько быстро сотрудники пытаются перезвонить»',
    'Отчет «Распределение звонков по регионам»',
    'Отчет «Качественные звонки»',
    'Отчет «В какое время лучше совершать звонки»',
    'Отчет «Исходящий обзвон»',
    'Отчет «Количество пропущенных вызовов»',
    'Отчет «В какое время теряются звонки»',
    'Отчет «Сколько клиенты готовы ждать на линии»',
    'Отчет «Сколько звонков принято быстро»',
    'Отчет «Средняя продолжительность»',
    'Отчет «Время ожидания ответа»',
    'Отчет «Время обслуживания вызова»',
    'Отчет «Сколько сотрудников решают проблему клиента»',
    'Отчет «Сколько звонков требуется клиенту для решения проблемы»',
    'Отчет «Распределение звонков по пунктам голосового меню»',
    'Обратный звонок',
    'Лидогенерация',
    'Чат на сайте',
    'ВКонтакте',
    'WhatsApp',
    'Telegram',
    'MAX',
    'НАЗАНАЧЕНИЕ КАНАЛА MAX',
    'КАК ПОДКЛЮЧИТЬ КАНАЛ MAX',
    'Клиентское приложение',
    'Е-mail',
    'Aвито',
    'Авито Работа',
    'БЛОК ВИЗУАЛИЗАЦИИ',
    'БЛОК ТАБЛИЦЫ',
    'Блок «Контекстная реклама»',
    'Блок «Органический трафик»',
    'Добавление номеров',
    'Добавление сотрудников',
    'Удаление номеров и сотрудников вне карусели',
    'Когда лучше использовать правило «По маске»',
    'Когда лучше использовать правило «По региону»',
    'Доступ к ИИ-инструментам Контакт-центра',
    'Шаг 1. Подключение к LDAP-серверу',
    'Шаг 2. Сопоставление атрибутов',
    'Шаг 3. Сопоставление сотрудников',
    'Шаг 4. Настройка синхронизации',
    'Резервирование',
]}
HEADING_COLORS = {4347235, 2375520, 4408131}

TR = dict(zip("абвгдеёзийклмнопрстуфхцыэ", "abvgdeezijklmnoprstufhcye"))
TR.update({"ж": "zh", "ч": "ch", "ш": "sh", "щ": "sch", "ю": "yu", "я": "ya", "ъ": "", "ь": "", "й": "y"})


def slug(text, limit=40):
    s = "".join(TR.get(c, c) for c in text.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:limit].strip("-") or "razdel"


def norm(text):
    return re.sub(r"\s+", " ", text.replace(" ", " ")).strip()


def ntoks(text):
    return len(ENC.encode(text))


def page_ranges(pages):
    pages = sorted(set(pages))
    return f"{pages[0]}-{pages[-1]}" if pages[0] != pages[-1] else str(pages[0])


# ---------------------------------------------------------------- reading

def read_toc(doc):
    toc = []
    for pno in range(1, 7):
        text = doc[pno].get_text()
        buf = ""
        for line in text.splitlines():
            line = norm(line)
            if not line:
                continue
            buf = f"{buf} {line}".strip() if buf else line
            m = TOC_LINE.match(buf)
            if m:
                toc.append((m.group(1).rstrip("."), norm(m.group(2)), int(m.group(3))))
                buf = ""
            elif not re.match(r"^(Раздел\s+\d+\.|\d+(\.\d+)*)", buf):
                buf = ""
    return toc


def line_items(page, gpage):
    """Return reading-order items: ('text', y, str, size, font) and ('image', y, info)."""
    items = []
    d = page.get_text("dict", sort=True)
    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        for ln in b["lines"]:
            text = norm("".join(s["text"] for s in ln["spans"]))
            if not text:
                continue
            sp = max(ln["spans"], key=lambda s: len(s["text"].strip()))
            items.append({"kind": "text", "y": ln["bbox"][1], "x": ln["bbox"][0], "text": text,
                          "size": round(sp["size"], 1), "font": sp["font"], "color": sp["color"], "block": id(b)})
    for im in page.get_image_info(hashes=True, xrefs=True):
        items.append({"kind": "image", "y": im["bbox"][1], "x": im["bbox"][0], "info": im})
    items.sort(key=lambda i: (round(i["y"]), i["x"]))
    # drop the running page number (first/last short numeric line)
    texts = [i for i in items if i["kind"] == "text"]
    drop = {id(i) for i in texts[:2] + texts[-2:] if i["text"] == str(gpage)}
    items = [i for i in items if id(i) not in drop]
    return items


def is_heading(item):
    t, size, font = item["text"], item["size"], item["font"]
    m = PART_HEAD.match(t)
    if m and size >= 16:
        return m.group(1), t
    m = NUM_HEAD.match(t)
    # In this manual every multi-level number at the start of a line is a heading
    # (checked against the printed TOC and the v1.23 outline); the caller also
    # requires the numbers to grow monotonically.
    if m and "...." not in t and len(t) < 160 and re.match(r"[A-ZА-ЯЁ«\"G]", m.group(2)):
        return m.group(1), t
    # numbered steps of «Как подключить канал MAX» (bold, own colour; used only there)
    m = re.match(r"^(\d{1,2})\.\s+[A-ZА-ЯЁ]", t)
    if m and "Bold" in font and item["color"] == 2565927:
        return "", t
    styled = item["color"] in HEADING_COLORS or "Bold" in font or size >= 12
    if styled and t.casefold().rstrip(".") in UNNUMBERED:
        return "", t
    return None


def num_key(num):
    return tuple(int(x) for x in num.split(".")) if num else None


# ---------------------------------------------------------------- images

def load_image(doc, xref):
    """Return the image composited onto white (content may live in the SMask)."""
    pix = pymupdf.Pixmap(doc, xref)
    if pix.n - pix.alpha > 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, img).convert("RGB")
    return img


def classify(doc, img, info, page_count_by_hash, total_pages):
    w, h = info["width"], info["height"]
    if page_count_by_hash[info["digest"]] > total_pages * 0.5:
        return "decorative", "фирменный шаблон страницы (логотип MANGO OFFICE, контакты, линии)"
    stat = ImageStat.Stat(img.convert("L"))
    if stat.stddev[0] < 1.0:
        # In this manual every such image is a shadow/backing frame that
        # contains a separate screenshot (verified: 207 of 207).
        return "decorative", "однотонная подложка-тень под снимком экрана (снимок сохранён отдельно)"
    if w < 8 or h < 8:
        return "decorative", "служебный элемент менее 8 пикселей"
    return "content", ""


def ocr(img):
    if img.width < 80 or img.height < 30:
        return ""
    scale = 2 if img.width < 900 else 1
    im = img.convert("RGB").resize((img.width * scale, img.height * scale))
    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        im.save(f.name)
        try:  # one thread per call: parallel runs otherwise oversubscribe OpenMP
            out = subprocess.run(["tesseract", f.name, "-", "-l", "rus+eng", "--psm", "11"],
                                 capture_output=True, text=True, check=False, timeout=120,
                                 env={**os.environ, "OMP_THREAD_LIMIT": "1"}).stdout
        except subprocess.TimeoutExpired:
            out = ""
    words = []
    for line in out.splitlines():
        line = norm(line)
        # keep lines that look like words, drop OCR noise
        if len(line) >= 2 and sum(c.isalnum() for c in line) >= max(2, len(line) * 0.6):
            words.append(line)
    seen, uniq = set(), []
    for wd in words:
        if wd.casefold() not in seen:
            seen.add(wd.casefold())
            uniq.append(wd)
    text = "; ".join(uniq)
    return text[:600] + ("…" if len(text) > 600 else "")


def kind_of(w, h):
    if w <= 64 and h <= 64:
        return "Пиктограмма (значок элемента интерфейса)"
    if w <= 200 and h <= 120:
        return "Фрагмент интерфейса (кнопка, переключатель или поле)"
    return "Снимок экрана / схема Личного кабинета"


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdfs", nargs="+")
    ap.add_argument("--out", default=f"docs/kb/{DOC}")
    ap.add_argument("--no-ocr", action="store_true")
    args = ap.parse_args()
    out = Path(args.out)
    docs = [pymupdf.open(p) for p in args.pdfs]
    shas = [hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in args.pdfs]
    toc = read_toc(docs[0])
    edition = norm(re.search(r"v\s*[\d.]+\s*\|\s*[\d.]+", docs[0][1].get_text()).group(0))

    # global page numbering: part1 1..N1, part2 continues
    pages = []
    g = 0
    for part, d in enumerate(docs, 1):
        for local, p in enumerate(d, 1):
            g += 1
            pages.append((part, local, g, p))
    total = len(pages)
    hash_pages = Counter()
    for _, _, gp, p in pages:
        for im in {i["digest"] for i in p.get_image_info(hashes=True)}:
            hash_pages[im] += 1

    # ---- walk pages, split into sections
    sections = [{"num": "—", "heading": "Титульная часть", "title": "Титульная часть", "items": []}]
    seen_keys = set()
    toc_start_page = max(t[2] for t in toc[:1]) if toc else 6
    for part, local, gp, p in pages:
        for it in line_items(p, gp):
            it.update(part=part, local=local, page=gp, pageobj=p)
            if it["kind"] == "text" and gp >= toc_start_page:
                h = is_heading(it)
                if h:
                    num, text = h
                    key = num_key(num)
                    if key is None or (key, text) not in seen_keys:
                        if key is not None:
                            seen_keys.add((key, text))
                        title = text if not num else norm(re.sub(r"^(Раздел\s+\d+\.|\d+(\.\d+)*\.?)\s*", "", text))
                        if title.isupper():
                            title = title.capitalize()
                        sections.append({"num": num or (sections[-1]["num"]), "heading": text,
                                         "title": title, "items": [], "y_size": it["size"],
                                         "start": gp, "unnumbered": not num, "color": it["color"]})
                        continue
            # heading continuation line (wrapped heading)
            s = sections[-1]
            if (it["kind"] == "text" and not s["items"] and s.get("y_size") and it["size"] == s["y_size"]
                    and it["color"] == s.get("color") and s["color"] in HEADING_COLORS
                    and not NUM_HEAD.match(it["text"]) and it["text"][:1].islower()):
                s["heading"] += " " + it["text"]
                s["title"] += " " + it["text"]
                continue
            s["items"].append(it)

    # ---- TOC coverage check
    found = {s["num"] for s in sections}
    missing = [t for t in toc if t[0] not in found and not t[0].startswith("Раздел")]
    missing += [t for t in toc if t[0].startswith("Раздел") and t[0].split()[1].rstrip(".") not in found]
    if missing:
        print("TOC entries without heading:", missing, file=sys.stderr)

    # ---- write output
    if out.exists():
        shutil.rmtree(out)
    (out / "sections").mkdir(parents=True)
    (out / "images").mkdir()
    plumbers = [pdfplumber.open(p) for p in args.pdfs]
    plumb_cache = {}
    rows, meta_sections, verify_sections, audit = [], [], [], []
    image_count = decorative_count = 0
    total_tokens = 0
    critical_re = re.compile(r"https?://\S+|[a-z]+_[a-z_]+|\b\d{3,}\b|\b[A-Za-z][A-Za-z0-9-]{2,}\b")
    for order, s in enumerate(sections):
        nn = f"{order:02d}"
        fname = f"{nn}-{slug(s['title'])}"
        spages = sorted({i["page"] for i in s["items"]} | ({s["start"]} if s.get("start") else set())) or [1]
        refs = []
        for part in sorted({i["part"] for i in s["items"]} or {1}):
            gps = [i["page"] for i in s["items"] if i["part"] == part] or spages
            lps = [i["local"] for i in s["items"] if i["part"] == part] or spages
            refs.append({"source_pdf": f"{SRC_DIR}/{SRC_NAMES[part - 1]}", "part": part,
                         "pages": page_ranges(lps), "global_pages": page_ranges(gps)})
        sec_label = s["num"]
        body, para, prev_block = [], [], None
        img_k = 0
        context_text = ""

        def flush():
            nonlocal para
            if para:
                body.append(" ".join(para))
            para = []

        items = s["items"]
        for idx, it in enumerate(items):
            if it["kind"] == "text":
                if it["block"] != prev_block:
                    flush()
                para.append(it["text"])
                prev_block = it["block"]
                continue
            flush()
            prev_block = None
            info = it["info"]
            try:
                img = load_image(it["pageobj"].parent, info["xref"])
            except Exception as exc:  # noqa: BLE001 - report and skip unreadable xref
                audit.append((sec_label, it["page"], "unreadable", str(exc)))
                continue
            cls, why = classify(it["pageobj"].parent, img, info, hash_pages, total)
            if cls == "decorative":
                decorative_count += 1
                audit.append((sec_label, it["page"], "decorative", why))
                continue
            img_k += 1
            image_count += 1
            iname = f"{fname}-{img_k}.png"
            img.save(out / "images" / iname, optimize=True)
            prev_text = (body[-1] if body else context_text)
            nxt = next((j["text"] for j in items[idx + 1:] if j["kind"] == "text"), "")
            caption = nxt if CAPTION.match(nxt) else (para[-1] if para and CAPTION.match(para[-1]) else "")
            ocr_text = "" if args.no_ocr else ocr(img)
            anchor = norm(prev_text)[-160:] if prev_text else "начало раздела"
            kind = kind_of(img.width, img.height)
            label = caption or f"{kind}, стр. {it['page']}"
            desc = [f"> **Описание иллюстрации {DOC_CODE}-§{sec_label}-{img_k}** "
                    f"(к §{sec_label} «{s['title']}», стр. {it['page']}; {img.width}×{img.height} px). "
                    f"{kind}.",
                    f"> Относится к тексту руководства: «…{anchor}»."]
            if caption:
                desc.append(f"> Подпись в руководстве: «{caption}».")
            if ocr_text:
                desc.append(f"> Текст на изображении (OCR, требует сверки): {ocr_text}")
            elif kind.startswith("Пиктограмма"):
                desc.append("> Текста на изображении нет; назначение значка — см. текст, к которому он относится.")
            body.append(f"![{label}](../images/{iname})\n\n" + "\n".join(desc))
        flush()
        if body:
            context_text = body[-1]
        text_only = " ".join(b for b in body if not b.startswith("!["))
        hint = next((b for b in body if not b.startswith("![") and len(b) > 20), "—")
        hint = norm(hint).replace("|", "/")[:90] if hint != "—" else "—"

        # ---- cross-engine verification
        crit = sorted(set(critical_re.findall(text_only)))
        ptext = ""
        for gp in range(max(1, spages[0] - 1), min(total, spages[-1] + 1) + 1):
            if gp not in plumb_cache:
                part, local = pages[gp - 1][0], pages[gp - 1][1]
                plumb_cache[gp] = re.sub(r"\s+", "", plumbers[part - 1].pages[local - 1].extract_text() or "")
            ptext += plumb_cache[gp]
        ptext_n = re.sub(r"\s+", "", ptext)
        unconfirmed = [c for c in crit if re.sub(r"\s+", "", c) not in ptext_n]
        verify_sections.append({"file": f"sections/{fname}.md", "critical_tokens": len(crit),
                                "unconfirmed": unconfirmed, "pages": page_ranges(spages), "title": s["title"]})

        pages_s = page_ranges(spages)
        src_pages = "; ".join(f"ч.{r['part']}: {r['pages']}" for r in refs)
        trace = ", ".join(f"ч.{r['part']} `{r['source_pdf']}` с.{r['pages']}" for r in refs)
        heading_md = "#" * min(6, 1 + (s["num"].count(".") if s["num"] not in ("—",) else 0))
        title_line = f"{s['num']}. {s['title']}" if s["num"] not in ("—",) and not s.get("unnumbered") else s["title"]
        content = "\n\n".join(body)
        if unconfirmed:
            content += ("\n\n<!-- kb-verify:start -->\n\n> ❓ **ТРЕБУЕТСЯ ПРОВЕРКА**: токены не подтверждены вторым "
                        f"движком (pdfplumber) на стр. {pages_s}: " + ", ".join(f"`{u}`" for u in unconfirmed[:30])
                        + "\n\n<!-- kb-verify:end -->")
        tokens = ntoks(content)
        total_tokens += tokens
        fm = {
            "id": f"{DOC}-{fname}", "doc_code": DOC_CODE, "doc_title": DOC_TITLE, "doc_version": DOC_VERSION,
            "section": s["num"] if s["num"] != "—" else "0", "pdf_section": s["num"], "title": s["title"],
            "pdf_heading": s["heading"], "pages": pages_s, "source": refs[0]["source_pdf"],
            "source_part": ",".join(str(r["part"]) for r in refs), "source_pages": src_pages,
        }
        lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" if k not in ("id", "doc_code", "source") else f"{k}: {v}"
                           for k, v in fm.items()]
        lines += ["source_refs: '" + json.dumps(refs, ensure_ascii=False, separators=(",", ":")) + "'",
                  'extracted_by: "pymupdf ' + pymupdf.VersionBind + '"', 'token_method: "tiktoken:cl100k_base"',
                  f"tokens: {tokens}", f"images: {img_k}", "status: extracted", "ai-generated: true", "---",
                  f"{heading_md} {title_line}", "",
                  f"> Трассировка: PDF §{s['num']} · сквозные стр. {pages_s} · источники: {trace}.", "", content, ""]
        (out / "sections" / f"{fname}.md").write_text("\n".join(lines))
        rows.append(f"| {s['num']} | {s['title']} | [sections/{fname}.md](sections/{fname}.md) | {pages_s} | "
                    f"{src_pages.replace('ч.', 'ч.').replace(': ', ' с.')} | {tokens} | {hint} |")
        meta_sections.append({"file": f"sections/{fname}.md", "number": s["num"], "order": nn, "pages": pages_s,
                              "pdf_heading": s["heading"], "pdf_section": s["num"], "source_refs": refs,
                              "title": s["title"], "tokens": tokens, "images": img_k})

    checked = sum(v["critical_tokens"] for v in verify_sections)
    unconf = sum(len(v["unconfirmed"]) for v in verify_sections)
    ratio = 1 - unconf / checked if checked else 1
    sources = [{"order": i + 1, "page_count": d.page_count, "source_pdf": f"{SRC_DIR}/{SRC_NAMES[i]}",
                "source_sha256": shas[i]} for i, d in enumerate(docs)]
    index = f"""---
product_taxonomy_ref: taxonomy/products.yaml#classes
product_ids: [voice-ucaas]
type: kb-source-index
doc_code: {DOC_CODE}
doc_title: "{DOC_TITLE}"
doc_version: "{DOC_VERSION}"
doc_edition: "{edition}"
status: extracted
ai-generated: true
source_document: "{', '.join(SRC_NAMES)}"
extraction_date: "{TODAY}"
model_used: "PyMuPDF {pymupdf.VersionBind} + pdfplumber {pdfplumber.__version__} + tesseract OCR (rus+eng)"
confidence_level: "requires_review"
pages_covered: "1-{total}"
---

# {DOC_TITLE} — индекс БЗ (карта разделов)

> Источник: справочник абонента v{DOC_VERSION} (редакция `{edition}`), две PDF-части:
> ч.1 `{SRC_DIR}/{SRC_NAMES[0]}` (с.1-{docs[0].page_count}) и ч.2 `{SRC_DIR}/{SRC_NAMES[1]}`
> (сквозные с.{docs[0].page_count + 1}-{total}). Исходные PDF в репозитории не хранятся.
> Токены: tiktoken:cl100k_base. Это **карта поиска** для агента (ADR-007 R2): найди раздел по
> колонке «Когда обращаться», открой только его файл, процитируй стабильным адресом.

> Перекрёстная проверка критических данных: [`verification.md`](verification.md). Описание
> иллюстраций и отбор изображений: [`IMAGES.md`](IMAGES.md).

## Как цитировать

`[{DOC_CODE}, §<номер>, с.<страница>]` — формат проекта (issue #109);
плюс адрес чанка `docs/kb/{DOC}/sections/<file>#<якорь>` (ADR-007 R3).

## Иллюстрации

Каждая содержательная иллюстрация в разделе сопровождается блоком
`> **Описание иллюстрации {DOC_CODE}-§<раздел>-<n>**`: тип изображения, страница, фрагмент текста
руководства, к которому относится иллюстрация, подпись и распознанный (OCR) текст интерфейса.
OCR-текст — вспомогательный: факты цитируются по тексту руководства.

## Разделы

| № PDF | Раздел | Файл | Стр. | Источник | Токены | Когда обращаться |
| --- | --- | --- | --- | --- | ---: | --- |
""" + "\n".join(rows) + "\n"
    (out / "index.md").write_text(index)
    meta = {
        "doc_code": DOC_CODE, "doc_title": DOC_TITLE, "doc_version": DOC_VERSION, "doc_edition": edition,
        "extracted_by": f"pymupdf {pymupdf.VersionBind}", "image_extractor": f"pymupdf {pymupdf.VersionBind}",
        "image_description": "context + caption + tesseract OCR (rus+eng)",
        "image_count": image_count, "images_dropped_decorative": decorative_count,
        "note": "Справочник абонента виртуальной АТС MANGO OFFICE. Руководство пользователя по настройке и использованию облачной телефонии.",
        "page_count": total, "part_count": len(docs), "processing_mode": "multi-part",
        "section_count": len(sections),
        "section_source": "numbered PDF headings (font/number heuristics) checked against printed TOC",
        "toc_entries": len(toc), "toc_entries_missing": [list(m) for m in missing],
        "sections": meta_sections, "source_document": DOC,
        "source_pdfs": [x["source_pdf"] for x in sources], "source_set": DOC, "sources": sources,
        "token_method": "tiktoken:cl100k_base", "tokens_index": ntoks(index), "tokens_total": total_tokens,
        "verification": {"method": "cross-engine (PyMuPDF -> pdfplumber re-read of the same pages ±1)",
                         "critical_tokens_checked": checked, "critical_tokens_unconfirmed": unconf,
                         "confirmed_ratio": round(ratio, 4), "confidence_level": "requires_review",
                         "extraction_date": TODAY},
    }
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    vrows = [f"| [{v['title']}]({v['file']}) | {v['pages']} | {len(v['unconfirmed'])} |"
             for v in verify_sections if v["unconfirmed"]]
    (out / "verification.md").write_text(f"""---
type: kb-verification-report
doc_code: {DOC_CODE}
source_document: "{', '.join(SRC_NAMES)}"
extraction_date: "{TODAY}"
confidence_level: "requires_review"
pages_covered: "1-{total}"
status: verified
ai-generated: true
---

# Отчёт перекрёстной проверки — {DOC_TITLE} v{DOC_VERSION}

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
| Уровень доверия | **requires_review** |

## Разделы, требующие ручной сверки

| Раздел | Стр. | Не подтверждено |
| --- | --- | ---: |
""" + ("\n".join(vrows) or "| — | — | 0 |") + """

Не подтверждённые токены перечислены в самих разделах в блоках
`<!-- kb-verify:start -->` … `<!-- kb-verify:end -->`.
""")
    reasons = Counter(a[3] for a in audit if a[2] == "decorative")
    (out / "IMAGES.md").write_text(f"""---
type: kb-image-audit
doc_code: {DOC_CODE}
extraction_date: "{TODAY}"
ai-generated: true
---

# Иллюстрации справочника ЛК ВАТС v{DOC_VERSION}

| Метрика | Значение |
| --- | ---: |
| Размещений изображений в PDF | {image_count + decorative_count} |
| Сохранено содержательных иллюстраций (с текстовым описанием) | {image_count} |
| Не сохранено как оформление | {decorative_count} |

## Что не сохранено и почему

| Причина | Размещений |
| --- | ---: |
""" + "\n".join(f"| {r} | {c} |" for r, c in reasons.most_common()) + """

Фирменный шаблон страницы (логотип MANGO OFFICE, телефон 8 800 555 55 22, адрес
www.mango-office.ru, декоративные линии) — одно и то же изображение на каждой
странице; сведений о функциональности системы не несёт, проверено визуально.

## Как описана каждая сохранённая иллюстрация

Сразу под ссылкой на изображение в разделе стоит блок
`> **Описание иллюстрации LK-§<раздел>-<n>**` с полями:

* тип (снимок экрана / схема, фрагмент интерфейса, пиктограмма), страница, размер;
* «Относится к тексту руководства» — фрагмент текста, непосредственно
  предшествующего иллюстрации в руководстве;
* подпись (`Рис. …`), если она есть в руководстве;
* «Текст на изображении (OCR)» — надписи интерфейса, распознанные tesseract
  (rus+eng); OCR может содержать ошибки, факты цитируются по тексту руководства.

Пиктограммы действий (например, значки положительного и отрицательного
показателя) сохранены: они помогают узнать элемент управления, их назначение
объяснено в тексте, к которому они относятся.
""")
    print(json.dumps({"sections": len(sections), "toc": len(toc), "missing": missing, "images": image_count,
                      "decorative": decorative_count, "tokens": total_tokens, "unconfirmed": unconf,
                      "checked": checked}, ensure_ascii=False))


if __name__ == "__main__":
    main()
