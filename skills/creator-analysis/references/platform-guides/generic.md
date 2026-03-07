# 其他平台创作者分析指引

## 目标

把陌生平台映射到统一作者卡与作品卡 contract，再完成 creator 分析。

## 先读什么

- 先读 `references/api-capability-catalog.md`，锁定对应平台 tag。
- 优先筛 `user / author / creator / profile / home / channel / posts / notes / videos` 相关 route。
- 再补评论、媒体下载、字幕和额外指标 route。

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

## 选路规则

- 作者主页链路至少要覆盖“作者信息 + 作品列表分页”两段，不要只拿到 profile 就直接做 creator 分析。
- 如果平台存在 profile route 和 posts route 多版本并存，优先选择字段更完整、分页能力更稳定的版本。
- 作品列表 route 必须能稳定给出 `platform_work_id` 和发布时间/互动指标的主体字段，否则不能直接进入抽样和聚合分析。
- 视频作品如果缺字幕且又没有下载链路，要在 route 选择阶段就标记后续 ASR 不可行。

## 当前可运行实现

- `skills/creator-analysis/scripts/author_home/`
- `skills/creator-analysis/scripts/core/`
