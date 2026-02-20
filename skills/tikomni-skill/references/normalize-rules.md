# Normalize Rules

## 1. Goal

Produce stable `raw + normalized` output to absorb upstream response drift.

## 2. Envelope Compatibility

1. Support `payload.data` structure.
2. Support Tikomni flattened non-2xx detail fields at top level.
3. Support TikHub-like envelope: `code/message/request_id/router/data`.

## 3. Suggested Unified Schema

```json
{
  "meta": {
    "platform": "",
    "intent": "",
    "endpoint": "",
    "request_id": ""
  },
  "status": {
    "http_status": 200,
    "code": 200,
    "message": "",
    "message_zh": ""
  },
  "normalized": {
    "author": {},
    "items": [],
    "text": "",
    "raw_data": {}
  }
}
```

## 4. Homepage Extraction Key Fields

1. Douyin author: `sec_uid`, `unique_id`, `nickname`, `signature`, `follower_count`.
2. Douyin items: `platform_work_id`, `title/desc`, `duration_ms`, `video_down_url`, metrics.
3. Xiaohongshu author: `user_id/red_id/xsec_token`, `nickname`, `fans/follows`.
4. Xiaohongshu items: `note_id`, `title/desc`, `subtitle_url`, `duration_ms`, metrics.
