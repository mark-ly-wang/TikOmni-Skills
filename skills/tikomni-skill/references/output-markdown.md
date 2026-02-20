# Output Markdown Rules

## 1. Output Directory Source

Use runtime config as source of truth:

1. `references/runtime-config.md` (EN)
2. `references/runtime-config.zh-CN.md` (ZH)

If runtime config is missing, use the fallback template below.

## 2. Fallback Directory Template

```text
docs/skill-output/
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
---
```
