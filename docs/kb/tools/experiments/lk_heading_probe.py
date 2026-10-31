"""Probe span fonts of numbered heading-like lines in LK manual PDFs."""
import re, sys, collections, pymupdf
pat = re.compile(r"^(Раздел \d+\.|\d+(\.\d+)*\.?)\s+\S")
stats = collections.Counter()
for f in sys.argv[1:]:
    d = pymupdf.open(f)
    for pno, p in enumerate(d):
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                t = "".join(s["text"] for s in l["spans"]).strip()
                if pat.match(t) and "...." not in t:
                    s = l["spans"][0]
                    key = (round(s["size"], 1), s["font"])
                    stats[key] += 1
                    if stats[key] <= 2: print(pno + 1, key, t[:80])
print(stats.most_common(30))
