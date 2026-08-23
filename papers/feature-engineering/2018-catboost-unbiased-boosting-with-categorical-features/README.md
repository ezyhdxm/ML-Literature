# CatBoost: Unbiased Boosting with Categorical Features

- **Year:** 2018
- **Venue:** NeurIPS 2018
- **Category:** Feature engineering
- **Priority:** S — 基础必读
- **Status:** Peer-reviewed — older foundation
- **Survey score:** 100
- **Tags:** GBDT, categorical, target leakage, ordered boosting
- **Paper / official page:** https://arxiv.org/abs/1706.09516
- **Code:** https://catboost.ai/

## Why it is in the reading list

虽然早于 2023，却是你筛选标准下不可跳过的旧文献。它提供“特征构造必须 point-in-time/out-of-fold”的最清晰树模型范式。

## Survey summary

### Problem

高基数类别变量的 target encoding 会产生预测偏移与泄漏，普通 boosting 也存在同样的自拟合偏差。

### Method

ordered target statistics 与 ordered boosting：每个样本的编码/梯度只使用排列中更早的样本。

### Data / empirical evidence

在多类公开 tabular 数据上展示类别特征和 boosting 偏差修正带来的稳定优势，后续已成为工业基线。

### Assumption boundary

无参数响应分布假设；依赖随机排列/有序统计设计。

### Million-row feasibility

百万行成熟可用；类别组合和过多 CTR 会增加内存。

### Financial time-series fit

极高。适用于 issuer/dealer/sector 等类别，但真实金融时间应优先用按时间的 ordered encoding，而非随机排列。

### Rubric

- **A 弱假设:** ●●●●●
- **B 黑盒/GBM:** ●●●●●
- **S 可扩展:** ●●●●●
- **T 金融时序:** ●●●●●
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
