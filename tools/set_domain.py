#!/usr/bin/env python3
"""Zet de site om naar een eigen domein (bijv. als dehaasstyling.nl naar GitHub Pages wijst).

Gebruik:  python3 tools/set_domain.py dehaasstyling.nl
Vervangt de huidige basis-URL in alle SEO-bestanden, zet de <base> van 404.html goed
en schrijft het CNAME-bestand. Daarna: committen, pushen en in GitHub > Settings > Pages
"Enforce HTTPS" aanzetten.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OLD = re.compile(r"https://(?:julian08100\.github\.io/dehaasstyling|(?:www\.)?dehaasstyling\.nl)/")
FILES = ["index.html", "privacy.html", "robots.txt", "sitemap.xml", "llms.txt", "README.md"]

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    domain = sys.argv[1].strip().removeprefix("https://").strip("/")
    new = f"https://{domain}/"
    for name in FILES:
        p = ROOT / name
        s = p.read_text(encoding="utf-8")
        t = OLD.sub(new, s)
        if t != s:
            p.write_text(t, encoding="utf-8")
            print("bijgewerkt:", name)
    p = ROOT / "404.html"
    p.write_text(p.read_text(encoding="utf-8").replace('<base href="/dehaasstyling/">', '<base href="/">'), encoding="utf-8")
    (ROOT / "CNAME").write_text(domain + "\n", encoding="utf-8")
    print("CNAME geschreven:", domain)

if __name__ == "__main__":
    main()
