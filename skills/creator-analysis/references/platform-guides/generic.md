# 其他平台创作者分析指引

## 目标

把陌生平台映射到统一作者卡与作品卡 contract，再完成 creator 分析。

## 最小映射清单

作者侧：

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

作品侧：

- 统一作品卡字段字典中的必保字段
- 视频作品的 `video_download_url`

## 当前参考实现

- 旧单体 skill 的现有实现可作为参考源码：
  - `skills/tikomni-skill/scripts/author_home/`
  - `skills/tikomni-skill/scripts/core/`
