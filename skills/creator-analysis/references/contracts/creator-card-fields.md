# 作者卡字段字典

## 固定展示字段

- `platform`
- `platform_author_id`
- `author_handle`
- `nickname`
- `ip_location`
- `signature`
- `avatar_url`
- `fans_count`
- `liked_count`
- `collected_count`
- `works_count`
- `verified`
- `snapshot_at`

## 关键规则

- 作者卡是作者级事实承载体。
- 作者级分析正文来自 `author_analysis_v2`，不是来自平台原始过程字段。
- 平台原生 ID 只留在内部引用层，不进入最终作者卡正文。
