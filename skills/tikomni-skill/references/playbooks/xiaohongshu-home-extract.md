# Xiaohongshu Home Extract Playbook

## 1. Input

1. `user_id` or homepage/share URL.
2. Optional: `limit`, `pages_max`.

## 2. Fixed Steps

1. If input is not `user_id`, resolve it first:
   - `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`
2. Fetch author profile:
   - Primary: `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`
   - Fallback: `GET /api/u1/v1/xiaohongshu/app/get_user_info`
3. Fetch homepage posts:
   - Primary: `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`
   - Fallback: `GET /api/u1/v1/xiaohongshu/app/get_user_notes`
4. Prefer `has_more + cursor` for pagination; when unstable, last `note_id` may be used as cursor candidate.
5. Defaults: `limit=20`, `pages_max=50`.

## 3. Copy Extraction Sub-Rules

1. Batch per-item transcript extraction is enabled by default in homepage flow.
2. Xiaohongshu copy extraction is subtitle-first:
   - Check `subtitle_url` or `video_info_v2.media.video.subtitles`
   - If subtitle is unavailable, run U2 submit/query

## 4. Output

1. Must include subtitle-hit status, U2 fallback status, and final text source.
2. Write final output to markdown artifacts.
