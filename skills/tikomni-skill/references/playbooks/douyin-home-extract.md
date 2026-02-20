# Douyin Home Extract Playbook

## 1. Input

1. `sec_user_id` or homepage/share URL.
2. Optional: `limit`, `pages_max`, `sort_type`.

## 2. Fixed Steps

1. If input is not `sec_user_id`, resolve it first:
   - `GET /api/u1/v1/douyin/web/get_sec_user_id`
2. Fetch author profile:
   - `GET /api/u1/v1/douyin/app/v3/handler_user_profile`
3. Fetch homepage posts:
   - `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`
4. Continue pagination only when `has_more == 1` and `max_cursor` is valid.
5. Defaults: `sort_type=0`, `count<=20`, `limit=20`, `pages_max=50`.

## 3. Copy Extraction Sub-Rules

1. Batch per-item transcript extraction is enabled by default in homepage flow.
2. Transcription only runs for items with `video_model=video` and `13s < duration_ms <= 15min`.
3. Douyin copy extraction always uses U2:
   - `POST /api/u2/v1/services/audio/asr/transcription`
   - `GET /api/u2/v1/tasks/{task_id}`

## 4. Output

1. Include author summary, items, pagination trace, endpoint chain, and `request_id`.
2. Write final output to markdown artifacts.
