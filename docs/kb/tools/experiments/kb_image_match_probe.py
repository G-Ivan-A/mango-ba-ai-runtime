"""Probe: map existing docs/kb/<doc>/images/* files back to PDF image placements.

Usage: python experiments/kb_image_match_probe.py DOC_DIR PDF
"""
import hashlib, io, re, sys
from pathlib import Path
import pymupdf
from PIL import Image

doc_dir, pdf = Path(sys.argv[1]), pymupdf.open(sys.argv[2])
LINK = re.compile(r"!\[[^\]]*?стр\. (\d+)\]\(\.\./images/([^)]+)\)")
def h(img): return hashlib.md5(img.convert("RGB").tobytes()).hexdigest()
cache = {}
def page_hashes(p):
    if p not in cache:
        res = []
        for x in pdf[p - 1].get_images(full=True):
            try:
                pix = pymupdf.Pixmap(pdf, x[0])
                if pix.n - pix.alpha > 3: pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
                res.append((x[0], h(Image.open(io.BytesIO(pix.tobytes("png"))))))
            except Exception as e: res.append((x[0], str(e)))
        cache[p] = res
    return cache[p]
ok = miss = 0
for md in sorted((doc_dir / "sections").glob("*.md")):
    for page, name in LINK.findall(md.read_text()):
        fh = h(Image.open(doc_dir / "images" / name))
        cands = [x for x, hh in page_hashes(int(page)) if hh == fh]
        if not cands:
            for d in (-1, 1):
                if 0 < int(page) + d <= pdf.page_count:
                    cands = [x for x, hh in page_hashes(int(page) + d) if hh == fh] or cands
        if cands: ok += 1
        else: miss += 1; print("MISS", md.name, page, name)
print("matched", ok, "missed", miss)
