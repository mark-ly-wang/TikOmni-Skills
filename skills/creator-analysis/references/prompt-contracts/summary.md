# Prompt Contract · 总结（summary）

## Inputs
- `topic_score`
- `style_score`
- `hook_score`
- `structure_score`
- `cta_score`
- 各模块 `gaps`

## Method (stable)
1. 计算 5 模块平均分。
2. 结论分级：
   - `>=4.2`：可直接复用
   - `3.4~4.19`：可用但需小幅优化
   - `<3.4`：需重写关键模块
3. 选择最低 1-2 个模块，输出针对性建议（优先 gaps）。

## Output Format
- `结论`：`综合评分 X/5，判定为“...”`
- `建议`：最多 3 条，短句、可执行。

## Constraints
- 只输出“结论+建议”，不再拆“好/差/改写”。
- 建议必须指向具体模块。

## Fallback / Data-insufficient
- 若分数无法计算：输出“数据不足，需先完成5模块分析”。
- 若无 gaps：输出“继续做A/B测试验证Hook与CTA”。
