"""One-off fix (issue #12): restore the original PNG bytes from git HEAD when the
re-encoded file is larger but has exactly the same pixels."""
import io, subprocess, sys
from PIL import Image

def pixels(b):
    im = Image.open(io.BytesIO(b)).convert("RGB")
    return im.size, im.tobytes()

restored = saved = 0
for d in sys.argv[1:]:
    files = subprocess.run(["git", "diff", "--name-only", "--", f"{d}/images"], capture_output=True, text=True).stdout.split()
    for f in files:
        if not f.endswith(".png"):
            continue
        try:
            old = subprocess.run(["git", "show", f"HEAD:{f}"], capture_output=True, check=True).stdout
            new = open(f, "rb").read()
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
        if len(old) < len(new) and pixels(old) == pixels(new):
            open(f, "wb").write(old)
            restored += 1
            saved += len(new) - len(old)
print({"restored": restored, "saved_kb": round(saved / 1024)})
