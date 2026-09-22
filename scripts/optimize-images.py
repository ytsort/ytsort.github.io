"""Build the responsive WebP copies of the screenshots and the small logo index.html uses.

Deterministic; re-run after replacing a master in assets/.   python scripts/optimize-images.py
Needs Pillow with WebP support.

Why (measured 2026-09-22, phone on slow 4G): the four 1280x800 JPEG screenshots (97-143 KB
each) went to every screen at full size, and the 480 px logo is drawn at 30 CSS px. Each shot
now has 640/960/1280 px WebP copies for srcset (a phone takes the 640 or 960 one; a desktop
still gets 1280), and the logo a 90 px copy (3x of 30). The JPEG/PNG masters stay: og.jpg
and the masters are what social cards and future edits use.
"""

import os

from PIL import Image

ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
SHOTS = ["shot-panel", "shot-dark", "shot-settings", "shot-stats"]
WIDTHS = [640, 960, 1280]

if __name__ == "__main__":
    for name in SHOTS:
        src = os.path.join(ASSETS, name + ".jpg")
        im = Image.open(src).convert("RGB")
        sizes = []
        for w in WIDTHS:
            x = im if im.width <= w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            dst = os.path.join(ASSETS, f"{name}-{w}.webp")
            x.save(dst, "WEBP", quality=85, method=6)
            sizes.append(f"{w}w {os.path.getsize(dst) // 1024} KB")
        print(f"{name}.jpg {os.path.getsize(src) // 1024} KB -> " + ", ".join(sizes))
    logo = Image.open(os.path.join(ASSETS, "logo.png")).convert("RGBA").resize((90, 90), Image.LANCZOS)
    logo.save(os.path.join(ASSETS, "logo-90.png"), "PNG", optimize=True)
    print(f"logo.png -> logo-90.png {os.path.getsize(os.path.join(ASSETS, 'logo-90.png')) // 1024} KB")
