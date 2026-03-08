# 当前已验证路由链

## 目录

- [用途](#用途)
- [单作品](#单作品)
- [创作者主页](#创作者主页)
- [其他平台](#其他平台)

## 用途

- 本文档只记录当前仓库已经有脚本实现并验证过的优先路由链。
- 它不替代 `api-capability-index.md` + `api-tags/*.md` + `api-contracts/*.md`；前两者负责目录和路由摘要，后者负责完整契约，这里是“优先怎么调”。
- 当用户目标已经很明确时，优先走这里列出的路由链；只有链路不满足时再回索引和对应 tag 文件找补充 route。

## 单作品

### 抖音单作品

1. `GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`
   - 必填入参：`share_url`
2. `GET /api/u1/v1/douyin/web/fetch_one_video_by_share_url`
   - 必填入参：`share_url`
3. `POST /api/u2/v1/services/audio/asr/transcription`
   - 请求体关键字段：`input.file_urls[]`
4. `POST /api/u2/v1/tasks/{task_id}`
   - 路径参数：`task_id`

ASR 超时 fallback：

- 90 秒仍未完成时只做软观察。
- 120 秒（2 分钟）仍无结果时，不直接判失败；按 `service-guides/asr-u2-u3-fallback.md` 走 U3 fallback，再回调 U2。

必保输出目标：

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
- `video_download_url`
- `asr_raw`

### 小红书单作品

1. `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`
2. `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`
3. `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`
   - 典型入参：`note_id` 或 `share_text`
4. `GET /api/u1/v1/xiaohongshu/app/get_note_info`
5. `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2`
   - 必填入参：`note_id`
6. `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3`
   - 必填入参：`short_url`
7. `GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`
8. `POST /api/u2/v1/services/audio/asr/transcription`
9. `POST /api/u2/v1/tasks/{task_id}`

ASR 超时 fallback：

- 90 秒仍未完成时只做软观察。
- 120 秒（2 分钟）仍无结果时，不直接判失败；按 `service-guides/asr-u2-u3-fallback.md` 走 U3 fallback，再回调 U2。

必保输出目标：

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
- `video_download_url`
- `asr_raw`

## 创作者主页

### 抖音创作者主页

1. `GET /api/u1/v1/douyin/web/get_sec_user_id`
   - OpenAPI 必填入参：`url`
2. `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
   - 必填入参：`sec_user_id`
3. `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
   - 必填入参：`sec_user_id`
   - 常用分页参数：`max_cursor`、`count`、`sort_type`

作者卡必保字段：

- `platform_author_id`
- `author_handle`
- `nickname`
- `ip_location`
- `signature`
- `avatar_url`
- `fans_count`
- `liked_count`
- `works_count`
- `verified`

主页作品必保字段：

- `platform_work_id`
- `title`
- `caption_raw`
- `published_date`
- `digg_count`
- `comment_count`
- `collect_count`
- `share_count`
- `play_count`
- `video_download_url`

### 小红书创作者主页

1. `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
   - OpenAPI 必填入参：`share_link`
2. Profile 级联：
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_info`
3. Posts 级联：
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_notes`

作者卡必保字段：

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

主页作品必保字段：

- `platform_work_id`
- `title`
- `caption_raw`
- `published_date`
- `digg_count`
- `comment_count`
- `collect_count`
- `share_count`
- `play_count`
- `video_download_url`

## 其他平台

- 先在 `api-capability-index.md` 里找对应平台 tag，再读对应 `api-tags/*.md`；若字段定义仍不够精确，再继续读对应 `api-contracts/*.md`。
- 单作品优先找 detail route，再补 media/subtitle/comment route。
- 创作者主页优先找 profile route + posts route 的组合，不要只拿单段数据。
- 只有当全量目录里找不到可满足必保字段的 route 时，才宣告当前平台或当前对象不可行。
