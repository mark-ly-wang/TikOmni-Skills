# Output Markdown Rules

## 1. Output Directory Source

Use runtime config as source of truth:

1. `./runtime-config.md`
2. User-provided config path (if explicitly provided)

If runtime config is missing, use the fallback template below.

## 2. Fallback Directory Template

```text
tikomni-output/
  _runs/
  _errors/
  douyin/home/
  xiaohongshu/home/
```

## 3. Required Artifacts Per Run

1. `run-<timestamp>.md`: routing, params, fallback trace.
2. `result-<timestamp>.md`: final extraction output.
3. `error-<timestamp>.md`: failure detail (optional).

## 4. Required Frontmatter Fields

```yaml
---
title: ""
platform: ""
intent: ""
request_id: ""
source_endpoints: []
fallback_used: false
generated_at: ""
tags: []
rate_limit_wait_ms: 0
retry_attempt: 0
fallback_trigger_reason: ""
asr_source: "xhs_subtitle|u2|fallback_none"
---
```

## 5. Author Card Required Sections
- 作者画像
- 商业分析
- 对标分析
- 评分（business_score / benchmark_gap_score）
- 风格雷达（style_radar）
- 核心矛盾（core_contradictions）
- 建议动作（recommendations）
