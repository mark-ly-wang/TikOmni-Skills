# 其他平台单作品分析指引

## 目标

把陌生平台的单作品映射到统一作品卡字段字典，再完成单作品分析。

## 先读什么

- 先读 `references/api-capability-catalog.md`，找到对应平台 tag。
- 优先筛 `detail / post / note / video / article / comment / download / subtitle` 相关 route。
- 再决定是否需要额外找评论、字幕、媒体下载或作者补充接口。

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

## 选路规则

- detail route 至少要能稳定拿到 `platform_work_id`、主文本、作者标识和媒体/封面其一。
- 视频作品如果 detail route 不返回字幕，必须继续找字幕 route 或可用下载链接，再进入 ASR。
- 同一个平台若同时有 App / Web / V2 / V3 路由，优先选择字段更全、稳定性更高的版本，并记录 fallback。
- 不要因为某条 route 能返回一点信息，就跳过对必保字段的核验。

## 视频作品额外要求

- 如果有平台字幕，映射到 `subtitle_raw`，再统一到 `asr_raw`。
- 如果没有字幕，必须先确保 `video_download_url`，再调用 ASR。

## 当前可运行实现

- `skills/single-work-analysis/scripts/platform/`
- `skills/single-work-analysis/scripts/core/`
