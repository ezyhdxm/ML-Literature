# A Data-Centric Perspective on Evaluating Machine Learning Models for Tabular Data

- **Year:** 2024
- **Venue:** NeurIPS 2024 Datasets & Benchmarks
- **Category:** Benchmark / data quality
- **Priority:** S — 必读
- **Status:** Peer-reviewed
- **Survey score:** 100
- **Tags:** feature engineering, benchmark, data-centric, GBDT
- **Paper / official page:** https://proceedings.neurips.cc/paper_files/paper/2024/hash/ae00e5ce7142d02e30a8235ede1ec6fc-Abstract-Datasets_and_Benchmarks_Track.html

## Why it is in the reading list

对你最重要的结论之一：模型比较必须固定并记录 data pipeline；否则“换模型”的收益可能只是 preprocessing 差异。

## Survey summary

### Problem

公开 benchmark 常用“原始表”比较模型，但真实竞赛/工业性能很大部分来自领域预处理与特征工程。

### Method

为 10 个 Kaggle 数据集构建专家级数据处理版本，重新比较树模型和神经网络的排名与差距。

### Data / empirical evidence

研究显示经过高质量 FE 后，模型排名与性能间距会明显变化；树模型和神经网络都受益，单纯比较 architecture 容易误判。

### Assumption boundary

经验 benchmark；对分布不作强假设。

### Million-row feasibility

结论对百万行完全适用；特征物化与 pipeline 复现需工程投入。

### Financial time-series fit

极高。金融 alpha/fair-value 项目里，point-in-time 数据整理通常比模型架构更决定结果。

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
