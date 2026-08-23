---
title: "现代 Tabular Data：弱假设、黑盒与 GBM 文献地图"
subtitle: "Feature engineering · uncertainty · feature importance · model comparison"
date: "2026-08-23"
lang: zh-CN
---

> **Repository convention.** This overview is the editable source for the survey-level narrative. The 80 paper folders under [`papers/`](../../papers/README.md) are the durable paper-by-paper notebooks. Write questions and thoughts there; do not edit the generated HTML by hand.

## Scope and filtering rule

这份 literature map 刻意避开以 linear regression、GAM、kernel/local smoothing、Gaussian process 或精确参数响应分布为核心的路线。保留的方法应尽量满足：

- **assumption-lean**：不要求把 $P(Y\mid X)$ 指定为 Gaussian/Poisson/Gamma 等简单族；
- **black-box compatible**：能包裹 LightGBM/CatBoost/XGBoost 或其他任意预测器；
- **adaptive**：允许 heteroskedasticity、distribution shift、online recalibration 或 model multiplicity；
- **scalable**：至少有合理路径扩展到 $10^6$ 行、数百列；
- **financially defensible**：可以用 point-in-time、walk-forward、rolling/weighted calibration 改造成金融 time-series pipeline。

2023+ 是主搜索区间；少量更早论文只在它们仍然构成现代方法的不可替代基础时保留，例如 CatBoost ordered boosting、CQR、ACI、TreeSHAP 与 conditional-coverage impossibility results。

## Rubric

每篇文献按五个维度做 1–5 分定性评价：

| 维度 | 5 分 | 3 分 | 1 分 |
|---|---|---|---|
| **A — assumption leanness** | 任意序列/分布或仅极弱条件 | 需要 mixing / exchangeability /额外 residual model | 强参数响应、因果图或精确条件生成器 |
| **B — black-box / GBM fit** | post-hoc / plug-in / tree-native | 需额外 learner | architecture-specific / linear-only |
| **S — scale readiness** | 一遍/少量遍历、成熟 GBDT | 抽样或有限重训可做 | 全量多次重训/高阶组合爆炸 |
| **T — finance temporal fit** | 显式 online/nonexchangeable/temporal | 可改 rolling split | 纯 iid/static 且难改 |
| **E — evidence quality** | 强 peer review + broad benchmark/code | peer reviewed but narrow | 新预印本/弱验证 |

综合分只用于阅读排序，不是“统计显著性”：

$$
\text{Score}=0.25A+0.20B+0.20S+0.25T+0.10E.
$$

## Main conclusions

### 1. Feature engineering: search must be downstream-loss driven

**OpenFE (ICML 2023)** 是目前最接近“GBM-native + assumption-lean + production-relevant”的 AutoFE 主线。核心不是生成尽可能多的 algebra，而是 coarse-to-fine 地用下游预测增益筛候选。百万行时，推荐把搜索限制在时间安全的 operator grammar，在时间分层 proxy sample 上做 multi-fidelity search，缓存中间量，最后只物化获胜特征。

LLM 路线更适合做 **candidate generator**，不适合做最终裁判。CAAFE、FeatLLM、LLM-FE 的价值主要在语义先验、规则生成和 agent harness；而 *Large Language Models Engineer Too Many Simple Features for Tabular Data* 的负面结果提醒我们：LLM 会偏爱简单算术，反而不擅长主动提出真正重要的 group/time aggregation。因此金融 harness 应显式提供 lag、rolling、issuer/dealer aggregation、cross-sectional rank 等受控 operator，并自动拒绝 point-in-time leakage。

另一个关键结论来自 data-centric benchmark：**模型比较必须固定数据 pipeline**。否则“换模型”的收益很可能只是 preprocessing/feature engineering 差异。

### 2. Uncertainty: separate static coverage, drift calibration and full distributions

生产基线应从

$$
\text{quantile LightGBM/CatBoost} + \text{CQR}
$$

开始。它计算便宜、对 heteroskedasticity 友好、与现有 GBM pipeline 完全兼容。但 CQR 的经典 finite-sample guarantee 是 marginal coverage，不能写成每个 bond/issuer/tenor/liquidity state 都有精确 conditional coverage。

持续漂移时，主线是 ACI → Conformal PID → decaying-step online conformal → Gradient Equilibrium / online risk control。它们的共同工程优势是：**保留主预测器，只在线维护一个很轻的 calibration state**，比频繁重训 GBDT 便宜得多。

如果目标需要多峰、偏态或完整情景分布，**Treeffuser (NeurIPS 2024)** 是最值得研究的 GBDT-native probabilistic model：用 gradient-boosted trees 学 conditional diffusion/flow score。它明显比 CQR 重，因此更适合 scenario generation、multimodal execution price 或下游优化，而不是所有预测都默认使用。

### 3. Feature importance: answer three different questions separately

不要把所有方法压成一个“feature importance ranking”。至少区分：

1. **TreeSHAP**：当前 fitted model 如何分配预测贡献？
2. **Grouped LOCO**：拿掉一组信息后，未来预测损失多少？
3. **Rashomon consensus**：换一个几乎同样准确的模型，结论还成立吗？

相关特征下，unrestricted permutation 会构造分布外样本；SHAP 的 credit allocation 也不等于信息价值。对金融模型，更可靠的单位通常是 feature family：quotes、trades、curve/rates、static bond characteristics、issuer/sector、liquidity/size、temporal/regime。对这些组做 LOCO，再用多个近优模型和多个未来窗口检查 attribution stability，比对 600+ 列逐列排名更可信。

### 4. Model comparison: GBDT stays the floor, not the ideology

2023–2026 的大规模 benchmark 并没有支持“deep/foundation models 已普遍替代 GBDT”。更稳健的结论是：

- 强 LightGBM/CatBoost/XGBoost defaults 仍应是 tabular baseline floor；
- TabPFN/TabICL/TabM 等可作为 challenger，尤其在小样本、语义丰富或特定 pretraining 场景；
- **TabReD** 比传统 iid OpenML benchmark 更接近金融工业数据，因为它显式包含 temporal shift 和 high-dimensional processed features；
- benchmark hygiene、HPO budget、preprocessing 与 split 往往足以改变“谁赢了”。

*The Limits of Assumption-Free Tests for Algorithm Performance* 给 model comparison 设了理论底线：比较两个已经 fitted 的 predictor，与声称“learning algorithm A 普遍优于 B”不是同一件事。在完全 black-box、无稳定性等额外条件时，后者存在强 information-theoretic limitations。因此金融报告更诚实的表述是：

> Model A 在这些预先指定的未来窗口、成本函数与市场状态下优于 Model B。

而不是“LightGBM algorithm 在总体上显著优于所有 challenger”。

## Recommended reading path

### Tier S — first pass

**Feature engineering**

- [OpenFE](../../papers/feature-engineering/2023-openfe-automated-feature-generation-with-expert-level-performance/README.md)
- [CatBoost ordered boosting](../../papers/feature-engineering/2018-catboost-unbiased-boosting-with-categorical-features/README.md)
- [Data-centric tabular evaluation](../../papers/benchmark-data-quality/2024-a-data-centric-perspective-on-evaluating-machine-learning-models-for-tabular-data/README.md)

**Uncertainty**

- [Conformal Prediction: A Gentle Introduction](../../papers/uncertainty/2023-conformal-prediction-a-gentle-introduction/README.md)
- [CQR](../../papers/uncertainty/2019-conformalized-quantile-regression/README.md)
- [Conformal Prediction Beyond Exchangeability](../../papers/uncertainty/2023-conformal-prediction-beyond-exchangeability/README.md)
- [Conformal PID](../../papers/uncertainty/2023-conformal-pid-control-for-time-series-prediction/README.md)
- [Online conformal with decaying steps](../../papers/uncertainty/2024-online-conformal-prediction-with-decaying-step-sizes/README.md)
- [Gradient Equilibrium](../../papers/uncertainty/2025-gradient-equilibrium-in-online-learning-theory-and-applications/README.md)
- [Treeffuser](../../papers/uncertainty/2024-treeffuser-probabilistic-predictions-via-conditional-diffusions-with-gradient-boosted-tree/README.md)
- [Limits of distribution-free conditional predictive inference](../../papers/uncertainty/2021-limits-of-distribution-free-conditional-predictive-inference/README.md)

**Feature importance**

- [TreeSHAP](../../papers/feature-importance/2020-consistent-individualized-feature-attribution-for-tree-ensembles-treeshap/README.md)
- [Shapley vs LOCO](../../papers/feature-importance/2024-feature-importance-a-closer-look-at-shapley-values-and-loco/README.md)
- [Permutation forces extrapolation](../../papers/feature-importance/2021-unrestricted-permutation-forces-extrapolation-variable-importance-requires-at-least-one-mo/README.md)
- [Rashomon consensus](../../papers/feature-importance/2023-partial-order-in-chaos-consensus-on-feature-attributions-in-the-rashomon-set/README.md)

**Model comparison**

- [When Do Neural Nets Outperform Boosted Trees?](../../papers/model-comparison/2023-when-do-neural-nets-outperform-boosted-trees-on-tabular-data/README.md)
- [Better by Default](../../papers/model-comparison/2024-better-by-default-strong-pre-tuned-mlps-and-boosted-trees-on-tabular-data/README.md)
- [TabReD](../../papers/model-comparison/2025-tabred-a-benchmark-of-tabular-machine-learning-in-the-wild/README.md)
- [TabArena](../../papers/model-comparison/2025-tabarena-a-living-benchmark-for-machine-learning-on-tabular-data/README.md)
- [Limits of assumption-free algorithm tests](../../papers/model-comparison/2026-the-limits-of-assumption-free-tests-for-algorithm-performance/README.md)

## Full library

The complete curated set contains **80 papers/resources**:

- Feature engineering: **12**
- Uncertainty: **28**
- Feature importance: **15**
- Model comparison: **22**
- Benchmark / data quality: **3**

Every item has its own reading folder with paper link, priority, survey score, and editable sections for your questions and thoughts:

**[Open the full paper-by-paper library →](../../papers/README.md)**

## How we iterate this repository

When reading a paper, edit its `README.md`:

```markdown
## My questions

- Why does this guarantee remain valid under ...?
- Can the method be implemented with LightGBM without retraining ...?

## My thoughts

- I suspect this fails when ...

## Experiments / implementation ideas

- Compare rolling CQR vs PID on ...
```

In a later chat, ask ChatGPT to pull `ezyhdxm/ML-Literature`, inspect the notes, and answer them. The answer can either be appended under `## Assistant follow-up` or expanded into a new standalone report under `reports/<topic>/`.

This makes the repository a research notebook rather than a static bibliography.
