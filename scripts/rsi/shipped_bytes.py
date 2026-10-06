"""Bytes a visitor downloads: the committed size at HEAD of the files the site serves.

GitHub Pages (CNAME, .nojekyll) serves the repo root. Counted: index.html, the assets/ images the page
and its social card load, and the crawler/agent files (robots.txt, sitemap.xml, llms*.txt, pricing.md,
which sitemap.xml lists). Not counted: dot-folders, scripts/, docs/, README.md, and the JPEG/PNG masters
in assets/ that scripts/optimize-images.py turns into the <name>-<width>.webp / logo-90.png copies the
page actually uses. A master is an assets/ jpg/png that has a derived assets/<stem>-<digits>.* sibling
and that index.html does not reference; it is an edit source, not something a visitor downloads, so
deleting it must not count as a win. A file index.html does load (og.jpg, icon128.png) always counts.

Prints shipped_bytes=<n> and index_html_bytes=<n>.
"""
import re
import subprocess

SERVED = (".html", ".css", ".js", ".mjs", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico",
          ".woff", ".woff2", ".json", ".webmanifest", ".xml", ".txt")
SERVED_PAGES = ("pricing.md",)  # served on purpose and listed in sitemap.xml; other .md files are repo docs
MASTER_EXT = (".jpg", ".jpeg", ".png")
DERIVED = re.compile(r"^assets/(.+)-\d+\.[A-Za-z0-9]+$")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, check=True).stdout


listing = git("ls-tree", "-r", "-l", "-z", "HEAD")
files = {}
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    if size == "-":
        continue
    files[path] = int(size)

index_text = git("show", "HEAD:index.html").decode("utf-8", "replace") if "index.html" in files else ""

# Stems that have generated copies (shot-panel -> shot-panel-640.webp, logo -> logo-90.png).
derived_from = set()
for path in files:
    m = DERIVED.match(path)
    if m:
        derived_from.add(m.group(1))


def is_master(path):
    if not path.startswith("assets/") or not path.lower().endswith(MASTER_EXT):
        return False
    if path in index_text:  # the page loads it, so a visitor downloads it
        return False
    stem = path[len("assets/"):].rsplit(".", 1)[0]
    return stem in derived_from


total = 0
index_bytes = 0
for path, size in files.items():
    parts = path.split("/")
    if any(p.startswith(".") for p in parts):
        continue
    if parts[0] in ("scripts", "docs"):
        continue
    if path == "index.html":
        index_bytes = size
    if is_master(path):
        continue
    if path.lower().endswith(SERVED) or path in SERVED_PAGES:
        total += size
print(f"shipped_bytes={total}")
print(f"index_html_bytes={index_bytes}")
