# 小红书单作品指引

## 先读什么

- 先读 `references/api-capability-catalog.md` 中 `Xiaohongshu-App-V2-API`、`Xiaohongshu-App-API`、`Xiaohongshu-Web-V2-API`、`Xiaohongshu-Web-API`。
- 当前仓库的已验证路由链是 `APP_V2 -> APP_V1 -> WEB_V2 -> WEB_V7`，并根据笔记类型选 detail route。

## 优先资源

- 标题：`title`
- 文案：`desc` / `content`
- 作品 ID：`note_id`
- 作者 ID：平台作者 ID
- 作者 handle：可读账号标识
- 视频作品优先检查平台原生字幕，再决定是否调用外部 ASR

## 当前优先路由链

1. 主路由：
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`
   - 典型入参：`note_id` 或 `share_text`
   - 用途：按内容类型拿最完整的笔记详情。
2. Fallback 1：`GET /api/u1/v1/xiaohongshu/app/get_note_info`
   - 典型入参：`note_id` 或 `share_text`
3. Fallback 2：
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2`
     - 必填入参：`note_id`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3`
     - 必填入参：`short_url`
4. Fallback 3：`GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`
   - 典型入参：`note_id` 或 `share_text`
5. 视频转写：
   - `POST /api/u2/v1/services/audio/asr/transcription`
   - `POST /api/u2/v1/tasks/{task_id}`

## 需要落到的统一字段

- 必保：`platform`、`platform_work_id`、`platform_author_id`、`author_handle`、`title`、`caption_raw`、`work_modality`
- 指标：`digg_count`、`comment_count`、`collect_count`、`share_count`、`play_count`
- 链路：`source_url`、`share_url`、`cover_image`
- 视频额外：`video_download_url`、`asr_raw`

## 选路规则

- 用户只给短链时，优先尝试从 `share_text` 解析 `note_id`；解析失败再走 `short_url` 专用 WEB_V2 route。
- 已经知道 `note_id` 时，优先走 `note_id` 直查，不要先绕分享链。
- 视频笔记优先使用平台原生字幕；只有字幕缺失且存在 `video_download_url` 时才触发 U2 ASR。

## 当前可运行实现

- `skills/single-work-analysis/scripts/platform/xiaohongshu/`
