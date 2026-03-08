# Validated Route Chains

## Contents

- [Purpose](#purpose)
- [Single Content](#single-content)
- [Creator Profiles](#creator-profiles)
- [Other Platforms](#other-platforms)

## Purpose

- This file records only the preferred route chains that already have script support and have been validated in this repository.
- It does not replace `api-capability-index.md` + `api-tags/*.md` + `api-contracts/*.md`. The first two provide discovery and route summaries, the third provides full contracts, and this file answers the narrower question: which chain should be tried first.
- When the user target is already clear, prefer the chains listed here. Only go back to the index and tag files when the validated chain is insufficient.

## Single Content

### Douyin Single Content

1. `GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`
   - Required input: `share_url`
2. `GET /api/u1/v1/douyin/web/fetch_one_video_by_share_url`
   - Required input: `share_url`
3. `POST /api/u2/v1/services/audio/asr/transcription`
   - Key request-body field: `input.file_urls[]`
4. `POST /api/u2/v1/tasks/{task_id}`
   - Path parameter: `task_id`

ASR timeout fallback:

- After 90 seconds, stay in soft observation only.
- After 120 seconds, if there is still no result, do not declare failure immediately. Follow `service-guides/asr-u2-u3-fallback.md`, use U3 fallback, and then retry U2.

Required output targets:

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

### Xiaohongshu Single Content

1. `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`
2. `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`
3. `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`
   - Typical input: `note_id` or `share_text`
4. `GET /api/u1/v1/xiaohongshu/app/get_note_info`
5. `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2`
   - Required input: `note_id`
6. `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3`
   - Required input: `short_url`
7. `GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`
8. `POST /api/u2/v1/services/audio/asr/transcription`
9. `POST /api/u2/v1/tasks/{task_id}`

ASR timeout fallback:

- After 90 seconds, stay in soft observation only.
- After 120 seconds, if there is still no result, do not declare failure immediately. Follow `service-guides/asr-u2-u3-fallback.md`, use U3 fallback, and then retry U2.

Required output targets:

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

## Creator Profiles

### Douyin Creator Profile

1. `GET /api/u1/v1/douyin/web/get_sec_user_id`
   - OpenAPI-required input: `url`
2. `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
   - Required input: `sec_user_id`
3. `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
   - Required input: `sec_user_id`
   - Common pagination parameters: `max_cursor`, `count`, `sort_type`

Required author-card fields:

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

Required profile-post fields:

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

### Xiaohongshu Creator Profile

1. `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
   - OpenAPI-required input: `share_link`
2. Profile cascade:
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_info`
3. Posts cascade:
   - `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`
   - `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
   - `GET /api/u1/v1/xiaohongshu/app/get_user_notes`

Required author-card fields:

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

Required profile-post fields:

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

## Other Platforms

- Start with `api-capability-index.md` to find the relevant platform tag, then read the relevant `api-tags/*.md`. If the field definitions are still not precise enough, continue into the relevant `api-contracts/*.md`.
- For a single content item, prefer a detail route first, then add media, subtitle, or comment routes as needed.
- For a creator profile, prefer a profile route plus a posts route. Do not stop at a single segment of data.
- Declare a platform or object infeasible only when the full catalog still cannot provide routes that satisfy the required output fields.
