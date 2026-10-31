"""Count image occurrences (by content hash) across the LK manual PDF parts."""
import hashlib, sys, collections, pymupdf
cnt = collections.Counter(); info = {}; pages = collections.defaultdict(set)
for f in sys.argv[1:]:
    d = pymupdf.open(f)
    for pno, p in enumerate(d):
        for im in p.get_image_info(hashes=True, xrefs=True):
            h = im["digest"].hex(); cnt[h] += 1; pages[h].add((f[-12:], pno + 1))
            info[h] = (im["width"], im["height"], [round(x) for x in im["bbox"]], im["xref"])
print("placements", sum(cnt.values()), "unique", len(cnt))
for h, c in cnt.most_common(25): print(c, len(pages[h]), info[h], sorted(pages[h])[:3])
