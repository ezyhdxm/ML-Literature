# ML Literature

A living literature notebook for modern machine learning research. The initial collection focuses on **assumption-lean / adaptive / black-box tabular ML**, especially GBDT-compatible feature engineering, uncertainty, feature importance, and model comparison.

## Current report

- [Editable Markdown source](reports/tabular-blackbox-2026/report.md)
- [Generated HTML](reports/tabular-blackbox-2026/report.html)
- [Paper-by-paper reading folders](papers/README.md) — 80 papers

## Workflow

1. **Edit the survey:** modify `reports/tabular-blackbox-2026/report.md`.
2. **HTML rebuild:** GitHub Actions rebuilds `report.html` with Pandoc + MathJax after changes to the report source/CSS/build script.
3. **Read a paper:** open its folder under `papers/<topic>/<year-slug>/README.md`.
4. **Write questions/thoughts:** use `## My questions`, `## My thoughts`, and `## Experiments / implementation ideas`.
5. **Iterate with ChatGPT:** ask ChatGPT to pull this repo and review your notes. It can answer inline under `## Assistant follow-up` or create a new standalone report under `reports/`.

### Important convention

Do not edit generated `report.html` by hand. `report.md` is the editable survey source; paper folders are the durable reading notebooks.

## Local build

Requires Pandoc:

```bash
bash reports/tabular-blackbox-2026/build.sh
```

The generated report uses MathJax for LaTeX math.
