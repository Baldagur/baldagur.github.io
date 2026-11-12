#!/usr/bin/env python3
"""Turn a tool's HTML (as saved from claude.ai) into a page on the site.

Usage: python3 _source/add-tool.py _source/<slug>.html
Writes tools/<slug>/index.html, tidies the claude.ai wrapper, and adds
an "All tools" link back to the home page.
"""
import pathlib, re, sys

src = pathlib.Path(sys.argv[1])
slug = src.stem
html = src.read_text(encoding="utf-8")

# claude.ai sometimes wraps a full document inside its own skeleton: keep the inner one.
docs = [m.start() for m in re.finditer(r"<!doctype html>", html, re.I)]
if len(docs) > 1:
    html = html[docs[1]:]
    html = re.sub(r"(</html>\s*)</body></html>\s*$", r"\1", html, flags=re.I)

html = re.sub(r'<meta name="claude:[^"]*"[^>]*>\s*', "", html)

back = ('<a href="../../" class="site-back" style="position:fixed;left:12px;'
        'bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:99;'
        'font:600 12px system-ui,sans-serif;text-decoration:none;color:#fff;'
        'background:rgba(20,22,26,.82);padding:6px 11px;border-radius:999px;'
        'backdrop-filter:blur(6px)">&larr; All tools</a>\n')
i = html.lower().rfind("</body>")
html = html[:i] + back + html[i:] if i >= 0 else html + back

out = pathlib.Path(__file__).resolve().parent.parent / "tools" / slug / "index.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html, encoding="utf-8")
print("wrote", out)
