"""Shared helpers for KB illustrations: loading, decorative check, OCR, description.

Used by ``extract_kb_doc.py`` (new documents) and ``describe_kb_images.py``
(adding descriptions to images of documents already in the KB). The format of
the description block is the one introduced for the LK manual (issue #8):

    > **Описание иллюстрации <CODE>-§<section>-<n>** (к §<section> «<title>», стр. <p>; WxH px). <kind>.
    > Относится к тексту руководства: «…<preceding manual text>».
    > Подпись в руководстве: «Рис. …».                       (if any)
    > Текст на изображении (OCR, требует сверки): …          (if any)

Requirements: pymupdf, Pillow and the ``tesseract`` binary with ``rus`` and
``eng`` language packs (set ``TESSERACT`` to override the binary path).
"""

import io
import os
import re
import shutil
import subprocess
import tempfile

import pymupdf
from PIL import Image, ImageStat

CAPTION = re.compile(r"^(Рис(унок|\.)\s*\d*|Рисунок)", re.I)
DESC_HEAD = "> **Описание иллюстрации "
TESSERACT = os.environ.get("TESSERACT") or shutil.which("tesseract") or "/home/linuxbrew/.linuxbrew/bin/tesseract"


def norm(text):
    return re.sub(r"\s+", " ", (text or "").replace(" ", " ")).strip()


def load_image(doc, xref):
    """Return the image of ``xref`` composited onto white (content may live in the SMask)."""
    pix = pymupdf.Pixmap(doc, xref)
    if pix.n - pix.alpha > 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, img).convert("RGB")
    return img


def load_with_mask(doc, xref, smask):
    """Like ``load_image`` but applies a soft mask stored as a separate xref."""
    if not smask:
        return load_image(doc, xref)
    try:
        pix = pymupdf.Pixmap(pymupdf.Pixmap(doc, xref), pymupdf.Pixmap(doc, smask))
    except Exception:  # noqa: BLE001 - fall back to the base image
        return load_image(doc, xref)
    if pix.n - pix.alpha > 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGBA")
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    return Image.alpha_composite(bg, img).convert("RGB")


def is_uniform(img):
    return ImageStat.Stat(img.convert("L")).stddev[0] < 1.0


def optimize_save(img, path):
    """Save losslessly with the smallest of: RGB PNG, palette PNG (when <=256 colours exact)."""
    img = img.convert("RGB") if img.mode not in ("RGB", "L") else img
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    best = buf.getvalue()
    colors = img.getcolors(256)
    if colors is not None:  # exact palette conversion, no quality loss
        pal = img.convert("P", palette=Image.ADAPTIVE, colors=len(colors))
        if set(c for _, c in pal.convert("RGB").getcolors(256)) == set(c for _, c in colors):
            b2 = io.BytesIO()
            pal.save(b2, "PNG", optimize=True)
            if len(b2.getvalue()) < len(best):
                best = b2.getvalue()
    with open(path, "wb") as f:
        f.write(best)
    return len(best)


def ocr(img):
    if img.width < 80 or img.height < 30 or not TESSERACT or not os.path.exists(TESSERACT):
        return ""
    scale = 2 if img.width < 900 else 1
    im = img.convert("RGB").resize((img.width * scale, img.height * scale))
    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        im.save(f.name)
        out = subprocess.run([TESSERACT, f.name, "-", "-l", "rus+eng", "--psm", "11"],
                             capture_output=True, text=True, check=False).stdout
    words = []
    for line in out.splitlines():
        line = norm(line)
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
    return "Снимок экрана / схема"


def describe(code, sec, k, title, page, img, anchor, caption, ocr_text):
    kind = kind_of(img.width, img.height)
    anchor = norm(anchor)
    anchor = ("«…" + anchor[-160:] + "»") if anchor else "начало раздела"
    lines = [f"{DESC_HEAD}{code}-§{sec}-{k}** (к §{sec} «{title}», стр. {page}; "
             f"{img.width}×{img.height} px). {kind}.",
             f"> Относится к тексту руководства: {anchor}."]
    if caption:
        lines.append(f"> Подпись в руководстве: «{norm(caption)}».")
    if ocr_text:
        lines.append(f"> Текст на изображении (OCR, требует сверки): {ocr_text}")
    elif kind.startswith("Пиктограмма") or kind.startswith("Фрагмент"):
        lines.append("> Текста на изображении нет; назначение элемента — см. текст, к которому он относится.")
    label = norm(caption) if caption else f"{kind}, стр. {page}"
    return label.replace("[", "(").replace("]", ")"), "\n".join(lines)
