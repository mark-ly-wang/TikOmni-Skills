# 抖音单作品指引

## 先读什么

- 先读 `references/api-capability-index.md`，再读 `references/api-tags/douyin-app-v3-api.md` 和 `references/api-tags/douyin-web-api.md`。
- 当前仓库的已验证单作品路由链只覆盖“分享链接 -> 单视频详情 -> 必要时 ASR”。

## 优先资源

- 标题：`title`
- 文案：`desc`
- 作品 ID：`aweme_id`
- 作者 ID：作者稳定 ID
- 作者 handle：`short_id` / `unique_id`
- 视频下载链接：优先无水印下载链接

## 当前优先路由链

1. 主路由：`GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`
   - 必填入参：`share_url`
   - 用途：拿单作品详情、作者基础信息、互动指标、媒体资源。
2. Fallback：`GET /api/u1/v1/douyin/web/fetch_one_video_by_share_url`
   - 必填入参：`share_url`
   - 用途：APP 路由失败或字段不足时兜底。
3. 视频转写：`POST /api/u2/v1/services/audio/asr/transcription`
   - 请求体关键字段：`input.file_urls[]`
   - 轮询：`POST /api/u2/v1/tasks/{task_id}`
   - 用途：平台未直接返回可用字幕时生成 `asr_raw`。

## 需要落到的统一字段

- 必保：`platform`、`platform_work_id`、`platform_author_id`、`author_handle`、`title`、`caption_raw`、`work_modality`
- 指标：`digg_count`、`comment_count`、`collect_count`、`share_count`、`play_count`
- 链路：`source_url`、`share_url`、`cover_image`
- 视频额外：`video_download_url`、`asr_raw`

## 选路规则

- 用户只给分享链接时，直接走上面的主路由链，不要先自行搜索其他 detail route。
- 视频作品优先吃平台原始字幕；只有拿不到可用 `subtitle_raw / asr_raw` 时才调用 U2 ASR。
- 如果 U2 超过 120 秒（2 分钟）仍无结果，按 `references/service-guides/asr-u2-u3-fallback.md` 走 U3 fallback。
- 如果目标只是评论、搜索、榜单，不属于本 guide 的单作品主链，回到 `references/api-capability-index.md` 锁定 tag，再读对应 `references/api-tags/*.md` 重新选 route。

## 当前可运行实现

- `skills/single-work-analysis/scripts/platform/douyin/`
