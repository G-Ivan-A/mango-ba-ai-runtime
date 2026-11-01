"""Render uniform-classified images with and without alpha to check they are truly empty."""
import io, sys, pymupdf
from PIL import Image, ImageStat
out = sys.argv[1]; n = 0
for f in sys.argv[2:]:
    d = pymupdf.open(f)
    for pno, p in enumerate(d):
        for im in p.get_image_info(xrefs=True):
            if im["width"] > 1000 and im["height"] > 2000: continue
            pix = pymupdf.Pixmap(d, im["xref"])
            base = pymupdf.Pixmap(pymupdf.csRGB, pix) if (pix.alpha or pix.n > 3) else pix
            img = Image.open(io.BytesIO(base.tobytes("png")))
            if ImageStat.Stat(img.convert("L")).stddev[0] < 1:
                n += 1
                if n <= 6:
                    p.get_pixmap(clip=pymupdf.Rect(im["bbox"]) + (-5, -5, 5, 5), dpi=150).save(f"{out}/u{n}.png")
                    print(n, pno + 1, f[-12:], im["width"], im["height"], pix.alpha, d.extract_image(im["xref"]).get("smask"))
print("total", n)
