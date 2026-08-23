# Auto-FP: An Experimental Study of Automated Feature Preprocessing for Tabular Data

- **Year:** 2024
- **Venue:** EDBT 2024
- **Category:** Feature engineering
- **Priority:** A — 高优先
- **Status:** Peer-reviewed
- **Survey score:** 76
- **Tags:** preprocessing, AutoML, search, benchmark
- **Paper / official page:** https://openproceedings.org/2024/conf/edbt/AutoFP_EDBT_camera_ready.pdf

## Why it is in the reading list

重要教训是先做强随机/进化 baseline，再上复杂 AutoML。对 GBDT，很多 scaling 并不重要，真正值得搜索的是缺失、类别编码、聚合与异常处理。

## Survey summary

### Problem

自动选择和排序 imputation、scaling、encoding 等 preprocessing pipeline，哪类搜索方法真的有效。

### Method

统一比较随机、进化、bandit、surrogate 等 15 种搜索算法，在 7 类预处理器构成的空间中优化。

### Data / empirical evidence

覆盖 45 个公开数据集与 3 个下游模型。进化类方法平均较强，但简单随机搜索也很有竞争力；不少复杂 surrogate/bandit 并未稳定胜过随机。

### Assumption boundary

经验 benchmark；无 Y 分布假设，但随机切分结论不能直接迁移到金融时序。

### Million-row feasibility

pipeline 搜索会重复扫描数据；百万行建议 sample-fit、全量-transform，并缓存预处理结果。

### Financial time-series fit

中高。需要把时点可用性、训练期拟合统计量冻结和 rolling refit 纳入 pipeline。

### Rubric

- **A 弱假设:** ●●●●●
- **B 黑盒/GBM:** ●●●●○
- **S 可扩展:** ●●●○○
- **T 金融时序:** ●●●○○
- **E 证据质量:** ●●●●○

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
