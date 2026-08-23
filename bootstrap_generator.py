from pathlib import Path
import base64, zlib, json

ROOT=Path('.')
b64=''.join(p.read_text().strip() for p in sorted((ROOT/'bootstrap_payload').glob('*.part')))
data=json.loads(zlib.decompress(base64.b64decode(b64)).decode('utf-8'))
papers=data['papers']; categories=data['categories']

report_dir=ROOT/'reports'/'tabular-blackbox-2026'; report_dir.mkdir(parents=True,exist_ok=True)
md=[data['pre'].rstrip(), '', '## 可筛选文献库 {#library}', '', '下面每篇文章都有独立阅读目录。编辑个人问题与想法时，请进入对应的 **Reading notes** 链接。', '', '<div class="paper-filter">', '<label>Search papers <input id="paper-search" type="search" placeholder="title / method / tag / venue"></label>', '<label>Category <select id="paper-category"><option value="">All</option><option>Feature engineering</option><option>Uncertainty</option><option>Feature importance</option><option>Model comparison</option><option>Benchmark / data quality</option></select></label>', '<label>Priority <select id="paper-priority"><option value="">All</option><option>S — 必读</option><option>A — 高优先级</option><option>B — 选择性阅读</option><option>C — 观察名单</option></select></label>', '<span id="paper-count"></span>', '</div>', '']
for cat,catslug in categories.items():
    ps=[p for p in papers if p['category']==cat]
    if not ps: continue
    md += [f'### {cat}','']
    for p in ps:
        attrs=f'.paper-card data-category="{p["category"]}" data-priority="{p["priority"]}" data-year="{p["year"]}" data-score="{p["score"]}"'
        meta=' · '.join(x for x in [p['year'],p['venue'],p['priority'],p['status'],f"score {p['score']}" if p['score'] else ''] if x)
        md += [f'::: {{{attrs}}}', '', f'#### {p["title"]}', '', f'**{meta}**  ', '']
        if p['tags']: md += ['`'+'` · `'.join(p['tags'])+'`','']
        for label,key in [('问题','problem'),('方法','method'),('真实数据与结果','results'),('现实意义','practical'),('假设边界','assumptions'),('百万行可行性','scale'),('金融时序适配','finance')]:
            md += [f'**{label}**  ',p[key],'']
        if p['rubric']:
            md += ['**Rubric**  ',' · '.join(f'{k}: {v}' for k,v in p['rubric'].items()),'']
        links=[]
        if p['paper_url']: links.append(f'[Paper / official page]({p["paper_url"]})')
        if p['code_url']: links.append(f'[Code]({p["code_url"]})')
        links.append(f'[Reading notes](../../papers/{catslug}/{p["slug"]}/README.md)')
        md += [' · '.join(links),'',':::','']
if data.get('back'): md += [data['back'].lstrip()]
(report_dir/'report.md').write_text('\n'.join(md),encoding='utf-8')

(report_dir/'style.css').write_text(''':root { --fg:#172033; --muted:#637083; --bg:#f7f8fb; --card:#fff; --line:#dfe4ea; --accent:#2d5bd1; --accent2:#edf2ff; }
* { box-sizing:border-box; }
body { margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC",Arial,sans-serif; color:var(--fg); background:var(--bg); line-height:1.65; }
body > header, body > main, body > nav#TOC { max-width:1180px; margin:auto; }
body > header { padding:54px 28px 24px; } body > main { padding:0 28px 80px; }
#TOC { background:var(--card); border:1px solid var(--line); border-radius:16px; padding:18px 24px; margin-bottom:28px !important; }
a { color:var(--accent); text-decoration:none; } a:hover{text-decoration:underline;}
h1 { font-size:2.35rem; line-height:1.18; } h2 { margin-top:3rem; border-bottom:1px solid var(--line); padding-bottom:.4rem; } h3 { margin-top:2.2rem; }
blockquote { margin:1.2rem 0; padding:.8rem 1rem; background:#fffbe9; border-left:4px solid #e2b93b; }
.paper-filter { position:sticky; top:0; z-index:5; display:flex; flex-wrap:wrap; gap:12px; align-items:end; padding:14px; margin:18px 0; background:rgba(247,248,251,.95); backdrop-filter:blur(8px); border:1px solid var(--line); border-radius:14px; }
.paper-filter label { display:flex; flex-direction:column; font-size:.78rem; color:var(--muted); gap:4px; }
.paper-filter input,.paper-filter select { min-width:190px; padding:8px 10px; border:1px solid #cdd5df; border-radius:9px; background:white; color:var(--fg); }
#paper-count { margin-left:auto; color:var(--muted); font-size:.9rem; }
.paper-card { background:var(--card); border:1px solid var(--line); border-radius:16px; margin:18px 0; padding:18px 20px 14px; box-shadow:0 4px 18px rgba(18,31,53,.035); }
.paper-card h4 { margin:.1rem 0 .5rem; font-size:1.18rem; } .paper-card p { margin:.45rem 0 .8rem; } .paper-card code { background:var(--accent2); color:#284c9a; padding:2px 5px; border-radius:5px; }
table { width:100%; border-collapse:collapse; background:var(--card); } th,td { border:1px solid var(--line); padding:8px 10px; vertical-align:top; }
pre { overflow:auto; padding:14px; border-radius:12px; background:#111827; color:#e5e7eb; }
@media(max-width:700px){body>header,body>main{padding-left:16px;padding-right:16px}.paper-filter{position:static}.paper-filter input,.paper-filter select{min-width:150px}h1{font-size:1.8rem}}
''',encoding='utf-8')
(report_dir/'filter.js').write_text('''<script>
(function(){ const cards=[...document.querySelectorAll('.paper-card')]; const q=document.getElementById('paper-search'),cat=document.getElementById('paper-category'),pri=document.getElementById('paper-priority'),count=document.getElementById('paper-count'); if(!q||!cat||!pri)return; function apply(){const needle=q.value.trim().toLowerCase();let shown=0;for(const c of cards){const ok=(!needle||c.innerText.toLowerCase().includes(needle))&&(!cat.value||c.dataset.category===cat.value)&&(!pri.value||c.dataset.priority===pri.value);c.style.display=ok?'':'none';if(ok)shown++;}count.textContent=shown+' / '+cards.length+' papers';} q.addEventListener('input',apply);cat.addEventListener('change',apply);pri.addEventListener('change',apply);apply(); })();
</script>\n''',encoding='utf-8')
(report_dir/'build.sh').write_text('''#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
pandoc "$HERE/report.md" --from='markdown+fenced_divs+link_attributes+raw_html' --to=html5 --standalone --toc --toc-depth=2 --mathjax --css=style.css --include-after-body="$HERE/filter.js" --metadata title="现代 Tabular Data：弱假设、黑盒与 GBM 文献地图" -o "$HERE/report.html"
echo "Built $HERE/report.html"
''',encoding='utf-8')

papers_root=ROOT/'papers'; papers_root.mkdir(exist_ok=True)
idx=['# Paper reading folders','', 'Each paper has a stable folder and an editable `README.md`. Put questions and thoughts directly in those sections; later ChatGPT can read the repo, answer them, and either update the note or create a separate deep-dive report.','']
for cat,catslug in categories.items():
    idx += [f'## {cat}','']
    for p in [x for x in papers if x['category']==cat]:
        folder=papers_root/catslug/p['slug']; folder.mkdir(parents=True,exist_ok=True)
        idx.append(f'- [{p["title"]}]({catslug}/{p["slug"]}/README.md) — {p["year"]}, {p["priority"]}, score {p["score"]}')
        note=[f'# {p["title"]}','',f'- **Year:** {p["year"]}',f'- **Venue:** {p["venue"]}',f'- **Category:** {p["category"]}',f'- **Priority:** {p["priority"]}',f'- **Status:** {p["status"]}',f'- **Survey score:** {p["score"]}',f'- **Tags:** {", ".join(p["tags"])}']
        if p['paper_url']: note.append(f'- **Paper / official page:** {p["paper_url"]}')
        if p['code_url']: note.append(f'- **Code:** {p["code_url"]}')
        note += ['','## Why it is in the reading list','',p['practical'],'','## Survey summary','','### Problem','',p['problem'],'','### Method','',p['method'],'','### Data / empirical evidence','',p['results'],'','### Assumption boundary','',p['assumptions'],'','### Million-row feasibility','',p['scale'],'','### Financial time-series fit','',p['finance'],'']
        if p['rubric']: note += ['### Rubric','']+[f'- **{k}:** {v}' for k,v in p['rubric'].items()]+['']
        note += ['## My questions','','<!-- Write questions below. Keep this heading so follow-up tooling can find it reliably. -->','','- ','','## My thoughts','','<!-- Write your interpretation, objections, connections, or experiment ideas below. -->','','- ','','## Experiments / implementation ideas','','- ','','## Assistant follow-up','','<!-- Future answers can be added here, or linked to a standalone report under reports/. -->','','_No follow-up yet._','']
        (folder/'README.md').write_text('\n'.join(note),encoding='utf-8')
    idx.append('')
(papers_root/'README.md').write_text('\n'.join(idx),encoding='utf-8')

(ROOT/'templates').mkdir(exist_ok=True)
(ROOT/'templates'/'paper-notes.md').write_text('''# Paper title

- **Year:**
- **Venue:**
- **Category:**
- **Paper / official page:**
- **Code:**

## Why it is in the reading list

## Survey summary

### Problem

### Method

### Data / empirical evidence

### Assumption boundary

### Million-row feasibility

### Financial time-series fit

## My questions

- 

## My thoughts

- 

## Experiments / implementation ideas

- 

## Assistant follow-up

_No follow-up yet._
''',encoding='utf-8')

(ROOT/'README.md').write_text(f'''# ML Literature

A living literature notebook for modern machine learning research. The initial collection focuses on **assumption-lean / adaptive / black-box tabular ML**, especially GBDT-compatible feature engineering, uncertainty, feature importance, and model comparison.

## Current report

- [Editable Markdown source](reports/tabular-blackbox-2026/report.md)
- [Generated HTML](reports/tabular-blackbox-2026/report.html)
- [Paper-by-paper reading folders](papers/README.md) — {len(papers)} papers

## Workflow

1. **Edit the survey:** modify `reports/tabular-blackbox-2026/report.md`.
2. **HTML rebuild:** GitHub Actions rebuilds `report.html` with Pandoc + MathJax after changes to the report source/CSS/filter script.
3. **Read a paper:** open its folder under `papers/<topic>/<year-slug>/README.md`.
4. **Write questions/thoughts:** use `## My questions`, `## My thoughts`, and `## Experiments / implementation ideas`.
5. **Iterate with ChatGPT:** ask ChatGPT to pull this repo and review your notes. It can answer inline under `## Assistant follow-up` or create a new standalone report under `reports/`.

### Important convention

Do not put personal reading notes directly into generated `report.html`. `report.md` is the editable survey source; paper folders are the durable reading notebooks.

## Local build

Requires Pandoc:

```bash
bash reports/tabular-blackbox-2026/build.sh
```

The generated report uses MathJax for LaTeX math and includes client-side search/filtering over paper cards.
''',encoding='utf-8')
(ROOT/'MANIFEST.md').write_text(f'''# Repository manifest

- Papers: {len(papers)}
- Categories: {len(categories)}
- Editable survey source: `reports/tabular-blackbox-2026/report.md`
- Generated HTML: `reports/tabular-blackbox-2026/report.html`
- Paper folders: `papers/<category>/<paper>/README.md`
''',encoding='utf-8')

wf=ROOT/'.github'/'workflows'; wf.mkdir(parents=True,exist_ok=True)
(wf/'build-tabular-report.yml').write_text('''name: Build tabular literature HTML

on:
  push:
    branches: [main]
    paths:
      - "reports/tabular-blackbox-2026/report.md"
      - "reports/tabular-blackbox-2026/style.css"
      - "reports/tabular-blackbox-2026/filter.js"
      - "reports/tabular-blackbox-2026/build.sh"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build:
    if: github.actor != 'github-actions[bot]'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Pandoc
        run: sudo apt-get update && sudo apt-get install -y pandoc
      - name: Build HTML
        run: bash reports/tabular-blackbox-2026/build.sh
      - name: Commit generated HTML if changed
        run: |
          if git diff --quiet -- reports/tabular-blackbox-2026/report.html; then echo "No generated changes"; exit 0; fi
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add reports/tabular-blackbox-2026/report.html
          git commit -m "build: regenerate tabular literature HTML"
          git push
''',encoding='utf-8')
print(f'Generated {len(papers)} paper folders')
