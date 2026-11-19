"""Validate public routes, asset references, and migrated table structure."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
REQUIRED = (
    "index.html", "all/index.html", "about/index.html",
    "categories/index.html", "tags/index.html", "archives/index.html",
    "topics/network/index.html", "topics/security/index.html",
    "topics/aws/index.html", "topics/portfolio/index.html",
    "topics/certification/index.html", "posts/protocol-1/index.html",
    "search.json", "assets/img/brand/og-image.png",
)

class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.tables = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table":
            self.tables += 1
        for key in ("src", "href", "srcset", "content"):
            val = attrs.get(key, "")
            if not val:
                continue
            if key == "content" and not val.startswith("/assets/"):
                continue
            vals = [s.strip().split()[0] for s in val.split(",")] if key == "srcset" else [val]
            for link in vals:
                parsed = urlsplit(link)
                if (link.startswith("/") and not link.startswith("//")
                        and parsed.path.startswith(("/assets/", "/favicon", "/apple-touch-icon"))):
                    self.assets.append(unquote(parsed.path.lstrip("/")))

def main():
    errors = []
    for relative in REQUIRED:
        if not (SITE / relative).is_file():
            errors.append(f"Missing expected output: {relative}")
    for html in SITE.rglob("*.html"):
        parser = AssetParser()
        parser.feed(html.read_text(encoding="utf-8"))
        for asset in parser.assets:
            if not (SITE / asset).is_file():
                errors.append(f"{html.relative_to(SITE)} references missing {asset}")
        if html.relative_to(SITE).as_posix() == "posts/protocol-1/index.html":
            if parser.tables != 15:
                errors.append(f"Protocol article has {parser.tables} tables, expected 15")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Site routes, local assets, and migrated tables verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
