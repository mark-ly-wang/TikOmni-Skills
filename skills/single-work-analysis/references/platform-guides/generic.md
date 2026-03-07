# 其他平台单作品分析指引

## 目标

把陌生平台的单作品映射到统一作品卡字段字典，再完成单作品分析。

## 最小映射清单

- `work_modality`
- `title`
- `caption_raw`
- `platform_work_id`
- `platform_author_id`
- `author_handle`
- `source_url`
- `share_url`
- 视频作品的 `video_download_url`
- 互动指标：点赞、评论、收藏、分享、播放

## 视频作品额外要求

- 如果有平台字幕，映射到 `subtitle_raw`，再统一到 `asr_raw`。
- 如果没有字幕，必须先确保 `video_download_url`，再调用 ASR。

## 当前参考实现

- 旧单体 skill 的现有实现可作为参考源码：
  - `skills/tikomni-skill/scripts/platform/`
  - `skills/tikomni-skill/scripts/core/`
