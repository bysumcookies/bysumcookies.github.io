"""Validate built routes, assets and SEO metadata before deployment."""
from html.parser import HTMLParser
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"
BASE = "https://bysumcookies.github.io"
REQUIRED = (
    "index.html", "all/index.html", "about/index.html",
    "categories/index.html", "tags/index.html", "archives/index.html",
    "topics/network/index.html", "topics/security/index.html",
    "topics/aws/index.html", "topics/portfolio/index.html",
    "topics/certification/index.html", "posts/protocol-1/index.html",
    "search.json", "assets/img/brand/og-image.png",
    "sitemap.xml", "feed.xml", "robots.txt",
)

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.tables = 0
        self.canonicals = []
        self.feed_links = []
        self.og_urls = []
        self.descriptions = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table":
            self.tables += 1
        if tag == "link":
            if attrs.get("rel") == "canonical":
                self.canonicals.append(attrs.get("href", ""))
            if attrs.get("rel") == "alternate" and attrs.get("type") == "application/atom+xml":
                self.feed_links.append(attrs.get("href", ""))
        if tag == "meta":
            if attrs.get("property") == "og:url":
                self.og_urls.append(attrs.get("content", ""))
            if attrs.get("name") == "description":
                self.descriptions.append(attrs.get("content", ""))
        for key in ("src", "href", "srcset", "content"):
            value = attrs.get(key, "")
            if not value:
                continue
            if key == "content" and not value.startswith("/assets/"):
                continue
            vals = [s.strip().split()[0] for s in value.split(",")] if key == "srcset" else [value]
            for link in vals:
                parsed = urlsplit(link)
                if (link.startswith("/") and not link.startswith("//") and
                    parsed.path.startswith(("/assets/", "/favicon", "/apple-touch-icon"))):
                    self.assets.append(unquote(parsed.path.lstrip("/")))

def expected_url(relative):
    if relative == "index.html":
        return BASE + "/"
    if relative.endswith("/index.html"):
        return BASE + "/" + relative[:-len("index.html")]
    return BASE + "/" + relative

def main():
    errors = []
    for relative in REQUIRED:
        if not (SITE / relative).is_file():
            errors.append(f"Missing expected output: {relative}")
    for html in SITE.rglob("*.html"):
        relative = html.relative_to(SITE).as_posix()
        parser = PageParser()
        parser.feed(html.read_text(encoding="utf-8"))
        for asset in parser.assets:
            if not (SITE / asset).is_file():
                errors.append(f"{relative} references missing {asset}")
        if relative != "refresh.html":
            canonical = expected_url(relative)
            if parser.canonicals != [canonical]:
                errors.append(f"{relative} canonical: {parser.canonicals}, expected {canonical}")
            if parser.og_urls != [canonical]:
                errors.append(f"{relative} og:url: {parser.og_urls}, expected {canonical}")
            if parser.feed_links != [BASE + "/feed.xml"]:
                errors.append(f"{relative} feed discovery missing or duplicate")
            if len(parser.descriptions) != 1 or not parser.descriptions[0].strip():
                errors.append(f"{relative} needs one nonempty description")
        if relative == "posts/protocol-1/index.html" and parser.tables != 15:
            errors.append(f"Protocol article has {parser.tables} tables, expected 15")
    try:
        sitemap = ET.parse(SITE / "sitemap.xml")
        urls = {el.text for el in sitemap.iter() if el.tag.endswith("}loc") or el.tag == "loc"}
        for url in (BASE + "/", BASE + "/posts/protocol-1/", BASE + "/all/", BASE + "/about/"):
            if url not in urls:
                errors.append(f"Sitemap is missing {url}")
        if BASE + "/refresh.html" in urls:
            errors.append("Refresh helper must not be included in sitemap")
    except (ET.ParseError, OSError) as exc:
        errors.append(f"Sitemap XML is invalid: {exc}")
    try:
        feed = ET.parse(SITE / "feed.xml")
        root = feed.getroot()
        if not root.tag.endswith("}feed"):
            errors.append("Feed must be an Atom feed")
        if not any(e.tag.endswith("}entry") for e in root):
            errors.append("Feed is missing published posts")
    except (ET.ParseError, OSError) as exc:
        errors.append(f"Atom feed XML is invalid: {exc}")
    robots = SITE / "robots.txt"
    if robots.is_file() and f"Sitemap: {BASE}/sitemap.xml" not in robots.read_text():
        errors.append("robots.txt does not reference sitemap")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Routes, SEO metadata, canonical URLs, sitemap, Atom feed and assets verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
