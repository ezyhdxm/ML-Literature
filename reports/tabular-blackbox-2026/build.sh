#!/usr/bin/env bash
set -euo pipefail
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
HERE="$(cd "$(dirname "$0")" && pwd)"
pandoc "$HERE/report.md" \
  --from='markdown+fenced_divs+link_attributes+raw_html' \
  --to=html5 \
  --standalone \
  --toc --toc-depth=2 \
  --mathjax='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js' \
  --css=style.css \
  --metadata title="现代 Tabular Data：弱假设、黑盒与 GBM 文献地图" \
  -o "$HERE/report.html"
echo "Built $HERE/report.html"
