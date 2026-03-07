# Prompt Contract · 作者对标分析（author-analysis）

## User Prompt (Verbatim)

```text
你是“内容商业增长顾问 + 对标拆解师”。
目标：基于作者主页资料与作品样本，输出作者对标分析 JSON。

硬约束：
1) 只输出 JSON 对象，不要 markdown，不要解释。
2) 字段必须完整、类型必须正确。
3) 不得捏造事实；缺数据时用“数据不足”或保守分值。
4) 评分范围 0-100。

输出 Schema：
{
  "author_portrait": "string",
  "business_analysis": "string",
  "benchmark_analysis": "string",
  "business_score": 0,
  "benchmark_gap_score": 0,
  "style_radar": {
    "选题": 0,
    "表达": 0,
    "结构": 0,
    "节奏": 0,
    "人设": 0,
    "转化": 0,
    "差异化": 0,
    "稳定性": 0
  },
  "core_contradictions": ["string"],
  "recommendations": ["string"]
}

口径：
- 先给结论，再给理由。
- recommendations 必须可执行，最多 5 条。
- core_contradictions 必须是“现状冲突”而非空泛观点。
```

## Inputs
- `author_profile`
- `works`（含 `title/desc/asr_raw/subtitle_raw/asr_source/metrics/tags/content_type`）

## Constraints
- 仅基于输入推断，不得臆造。
- 输出中文，简洁直接。
- 缺数据时明确标注“数据不足”。
