# OpenFE: Automated Feature Generation with Expert-level Performance

- **Year:** 2023
- **Venue:** ICML 2023
- **Category:** Feature engineering
- **Priority:** S — 必读
- **Status:** Peer-reviewed
- **Survey score:** 91
- **Tags:** GBDT, AutoFE, search, tabular
- **Paper / official page:** https://proceedings.mlr.press/v202/zhang23ay.html
- **Code:** https://github.com/IIIS-Li-Group/OpenFE

## Why it is in the reading list

这是最贴近“GBM + 弱假设 + 真正可落地”的自动特征工程论文。生产中应限制操作语法、在时间安全的 proxy sample 上搜索，再把获胜特征物化到全量数据。

## Survey summary

### Problem

如何在不手工穷举的情况下，从算术、聚合、频数与分组变换中找到真正改善下游模型的特征。

### Method

“feature boosting”把候选特征看成可逐步加入的弱学习器，并以 coarse-to-fine 两阶段筛选削减搜索空间；天然围绕树模型评估。

### Data / empirical evidence

在 10 个公开 benchmark 与 2 个 Kaggle 竞赛上验证；论文报告 OpenFE 加简单基线在两场竞赛中分别超过约 99.3% 与 99.6% 的参赛队伍。

### Assumption boundary

不假设 Y 的参数分布；主要风险不是统计假设，而是候选空间、验证切分与数据泄漏。

### Million-row feasibility

可做百万行，但不要在全量上反复生成全部候选；建议 1%–10% 时间分层样本、多保真评估与延迟物化。

### Financial time-series fit

高。可把操作限制为 lag、rolling、cross-sectional rank、issuer/group aggregation，并用严格 walk-forward 接受特征。

### Rubric

- **A 弱假设:** ●●●●●
- **B 黑盒/GBM:** ●●●●●
- **S 可扩展:** ●●●●○
- **T 金融时序:** ●●●●○
- **E 证据质量:** ●●●●●

## My questions

<!-- Write questions below. Keep this heading so follow-up tooling can find it reliably. -->

- 

## My thoughts

<!-- Write your interpretation, objections, connections, or experiment ideas below. -->

- 

## Experiments / implementation ideas

- 

## Assistant follow-up

<!-- Future answers can be added here, or linked to a standalone report under reports/. -->

_No follow-up yet._
