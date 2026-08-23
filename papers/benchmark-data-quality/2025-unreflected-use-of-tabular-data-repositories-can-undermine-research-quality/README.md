# Unreflected Use of Tabular Data Repositories Can Undermine Research Quality

- **Year:** 2025
- **Venue:** ICLR 2025 MLDPR Workshop — Spotlight
- **Category:** Benchmark / data quality
- **Priority:** S — 必读
- **Status:** Workshop spotlight / preprint
- **Survey score:** 96
- **Tags:** benchmark hygiene, OpenML, preprocessing, baselines
- **Paper / official page:** https://arxiv.org/html/2503.09159v1

## Why it is in the reading list

做 literature review 和内部 benchmark 前先读。它解释了为什么“某深度模型平均赢 GBDT”常在更严谨的切分、调参与预处理下消失。

## Survey summary

### Problem

为什么很多 tabular SOTA 结论可能来自数据仓库用法错误，而非真正算法优势。

### Method

复盘近期代表性研究，归纳不当 model selection、忽视强 baseline 与 preprocessing 错误等陷阱。

### Data / empirical evidence

用 OpenML 上的具体案例说明仓库元数据和默认任务设置会诱导研究者得出脆弱结论。

### Assumption boundary

方法论与案例研究，无分布假设。

### Million-row feasibility

与规模无关；能直接提高百万行实验的可信度。

### Financial time-series fit

极高。金融数据更不允许盲用仓库默认 split，必须按时间、实体和标签窗口设计评估。

### Rubric

- **A 弱假设:** ●●●●●
- **B 黑盒/GBM:** ●●●●●
- **S 可扩展:** ●●●●●
- **T 金融时序:** ●●●●●
- **E 证据质量:** ●●●○○

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
