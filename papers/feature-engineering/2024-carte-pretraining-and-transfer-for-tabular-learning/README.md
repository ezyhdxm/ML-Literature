# CARTE: Pretraining and Transfer for Tabular Learning

- **Year:** 2024
- **Venue:** ICML 2024
- **Category:** Feature engineering
- **Priority:** B — 选择性阅读
- **Status:** Peer-reviewed
- **Survey score:** 69
- **Tags:** pretraining, semantic columns, transfer, deep tabular
- **Paper / official page:** https://proceedings.mlr.press/v235/kim24d.html

## Why it is in the reading list

对纯数值高频表不是默认方案；对 issuer 名称、行业文本、产品描述等语义字段是值得保留的 challenger。

## Survey summary

### Problem

不同表的列语义和实体值如何迁移，尤其在小样本、含文本或高基数实体时。

### Method

把表行构造成实体关系表示，利用预训练语言表征与图式聚合做跨表预训练和迁移。

### Data / empirical evidence

在多种含语义实体的 tabular benchmark 上验证，报告在小样本与迁移场景优于从头训练的树/深度基线。

### Assumption boundary

不强设 Y 分布，但依赖文本编码器知识与表中可读语义。

### Million-row feasibility

预训练和实体编码较重；百万行可离线缓存 embedding，再与 GBDT 结合。

### Financial time-series fit

中高。适合债券 issuer、行业、条款文本的表示学习，但必须做时间截断以避免预训练语料的未来知识污染。

### Rubric

- **A 弱假设:** ●●●●○
- **B 黑盒/GBM:** ●●●○○
- **S 可扩展:** ●●●○○
- **T 金融时序:** ●●●○○
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
