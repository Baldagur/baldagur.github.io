# baldagur.github.io

Carlos's tools site, live at https://baldagur.github.io

- `index.html`: the home page. Each tool is one card.
- `tools/<slug>/index.html`: the published tool pages.
- `img/`: card thumbnails.
- `_source/`: each tool's HTML as saved from claude.ai, plus `add-tool.py`, which builds `tools/<slug>/index.html` from it. Folders starting with `_` are not published.

To update a tool: replace `_source/<slug>.html`, then run `python3 _source/add-tool.py _source/<slug>.html` and push.
