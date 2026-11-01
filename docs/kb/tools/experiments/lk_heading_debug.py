"""List numbered heading candidates vs. v1.23 outline numbers."""
import re, sys, pymupdf
old = set()
for l in open("/tmp/old_headings.txt"):
    m = re.match(r"^(\d+(?:\.\d+)+)", l)
    if m: old.add(m.group(1))
pat = re.compile(r"^(\d+(?:\.\d+)+)\.?\s+(\S.*)$")
g = 0; seen = set()
for f in sys.argv[1:]:
    for p in pymupdf.open(f):
        g += 1
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                t = "".join(s["text"] for s in l["spans"]).strip()
                m = pat.match(t)
                if m and "...." not in t and g > 5:
                    sp = max(l["spans"], key=lambda s: len(s["text"].strip()))
                    seen.add(m.group(1))
                    print(g, round(sp["size"],1), sp["font"], "OLD" if m.group(1) in old else "new", t[:70])
print("old numbers not seen:", sorted(old - seen))
