#!/usr/bin/env python3
"""QA: broken internal links, duplicate titles/descriptions/H1, thin pages. Run after build.py."""
import os
import re
import sys
from collections import defaultdict

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_site")
titles, descs, h1s = defaultdict(list), defaultdict(list), defaultdict(list)
broken, thin = [], []
words_total = []

pages = {}
for root, _, files in os.walk(OUT):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            rel = "/" + os.path.relpath(p, OUT).replace("index.html", "")
            pages[rel] = open(p, encoding="utf-8").read()

for rel, doc in pages.items():
    noindex = "noindex" in doc[:3000]
    t = re.search(r"<title>(.*?)</title>", doc).group(1)
    d = re.search(r'<meta name="description" content="(.*?)">', doc).group(1)
    h = re.search(r"<h1[^>]*>(.*?)</h1>", doc, re.S)
    if not noindex:
        titles[t].append(rel); descs[d].append(rel)
        if h:
            h1s[h.group(1)].append(rel)
    main = re.search(r"<main.*?</main>", doc, re.S).group(0)
    text = re.sub(r"<script.*?</script>|<[^>]+>", " ", main, flags=re.S)
    n = len(text.split())
    words_total.append(n)
    if n < 600 and not noindex and rel not in ("/privacy-policy/", "/terms/"):
        thin.append((n, rel))
    for href in re.findall(r'href="(/[^"#?]*)', doc):
        if href.startswith("/assets/") or href.endswith((".svg", ".xml", ".txt")):
            continue
        if href not in pages:
            broken.append((rel, href))

dup = lambda m: {k: v for k, v in m.items() if len(v) > 1}
print("pages: %d   avg words in <main>: %d   min: %d" % (len(pages), sum(words_total) / len(words_total), min(words_total)))
for name, m in (("titles", titles), ("descriptions", descs), ("h1", h1s)):
    dd = dup(m)
    print("duplicate %s: %d" % (name, len(dd)))
    for k, v in list(dd.items())[:5]:
        print("   ", k[:80], v[:3])
print("broken internal links: %d" % len(broken))
for b in broken[:15]:
    print("   ", b)
print("thin pages (<600 words): %d" % len(thin))
for t in sorted(thin)[:10]:
    print("   ", t)
long_titles = [t for t in titles if len(t) > 70]
print("titles > 70 chars: %d" % len(long_titles))
for t in long_titles[:5]:
    print("   ", len(t), t)
sys.exit(1 if broken or dup(titles) else 0)
