# Markdown 输出规则

## 1. 输出目录来源

输出目录以运行时配置为准：

1. `references/runtime-config.md`（英文）
2. `references/runtime-config.zh-CN.md`（中文）

若运行时配置缺失，则使用下方兜底模板。

## 2. 兜底目录模板

```text
docs/skill-output/
  _runs/
  _errors/
  douyin/home/
  xiaohongshu/home/
```

## 3. 每次执行最小产物

1. `run-<timestamp>.md`：路由、参数、fallback 轨迹。
2. `result-<timestamp>.md`：最终提取结果。
3. `error-<timestamp>.md`：失败详情（可选）。

## 4. frontmatter 最小字段

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
