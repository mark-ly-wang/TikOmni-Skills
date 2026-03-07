# Sampled Work Batch Explanations Prompt Contract

## Goal

对 sampled works 进行一次批量解释，补充单作品层没有的解释性字段。只允许一次批量调用，不允许逐条调用。

## Allowed Inputs

- Sampled works 的统一事实字段
- 作品级结构标签
- 聚合差异信息

## Required Output

顶层输出 `sampled_work_explanations`，以 `platform_work_id` 为 key。

每个 sampled work 必须包含：

- `why_it_worked_or_failed`
- `copyable_elements`
- `non_copyable_elements`
- `emotional_triggers`
- `cognitive_gap`
- `commercial_signal`

## Hard Rules

- 只解释 sampled works，不解释全量作品。
- 不得伪造作品中不存在的商业信号或情绪机制。
- 不得把结果直接写成作者级结论；作者级结论归 `author_analysis_v2`。
