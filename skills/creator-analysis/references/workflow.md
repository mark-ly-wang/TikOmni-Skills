# Creator 工作流

## 主流程

1. 获取作者事实字段。
2. 获取作品集合并为每个作品落事实卡。
3. 对视频作品执行批量 ASR。
4. 将 `analysis_eligibility=incomplete` 的作品排除出后续分析。
5. 做全量聚合、分桶与抽样。
6. 对 sampled works 执行一次批量 explanations。
7. 生成 `author_analysis_v2`。
8. 输出作者卡、作品卡和聚合结论。

## 必守规则

- 不做逐条作品 LLM deep analysis。
- `sampled_work_explanations` 只来自一次批量阶段。
- `author_analysis_v2` 是正式作者级主输出。
