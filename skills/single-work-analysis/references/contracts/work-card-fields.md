# 统一作品卡字段字典

## 最终作品卡展示字段

- `platform`
- `platform_work_id`
- `platform_author_id`
- `author_handle`
- `title`
- `caption_raw`
- `work_modality`
- `published_date`
- `digg_count`
- `comment_count`
- `collect_count`
- `share_count`
- `play_count`
- `cover_image`
- `source_url`
- `share_url`
- `primary_text`

## 视频作品额外展示字段

- `asr_raw`
- `video_download_url`

## 关键语义

- `caption_raw` 是作者自己写的描述/文案/正文，不是字幕，不是 ASR 原文。
- `primary_text` 是主展示文本与主分析文本：
  - 视频：`primary_text = asr_clean`
  - 文本：`primary_text = caption_raw`
- `video_download_url` 对视频作品是必保字段，默认即无水印下载链接。
- `subtitle_raw` 只是采集层来源字段，不进入最终作品卡正文。

## 缺失值规则

- 缺失的数值字段在展示层统一显示 `N/A`。
- 平台明确返回 `0` 时保留 `0`。
- `published_date` 统一按展示时区生成，默认 `Asia/Shanghai`。
