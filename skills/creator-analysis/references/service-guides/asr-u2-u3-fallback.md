# U2 ASR and U3 Public URL Fallback

## Purpose

- This guide defines the primary ASR path and timeout fallback for video tasks. It does not apply to text-only works.
- Always try U2 ASR first. U3 is fallback-only and must not bypass U2 by default.
- If a U1 detail route returns a no-watermark download link or another download URL that may not be publicly readable, use this guide to decide when to switch to U3.
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`

## Fixed Policy

1. Call a U1 detail route first and collect `video_download_url`, a no-watermark download URL, or another directly downloadable media URL.
2. Submit that URL to U2 ASR directly. Do not start with U3.
3. If there is still no complete result after 90 seconds, stay in soft observation and keep the primary path unchanged.
4. If there is still no result or still no complete result after 120 seconds, treat the source URL as likely not publicly readable and only then allow U3 fallback.
5. After U3 completes, obtain a public URL and submit it to U2 ASR again.
6. If U3 or the second U2 attempt still fails, keep the fact card and return `incomplete`. Do not fabricate the main text or any analysis conclusion.

## Scenario Notes

- Single content task: run this flow only for the current item.
- Creator batch task: apply U3 fallback only to the subset that still has no result after 120 seconds. Do not re-upload items that already succeeded.

## Route Facts

### Submit U2 ASR job

- Purpose: Default primary path. Submit the no-watermark or download URL returned by U1 directly to U2 ASR. Do not start with U3.
- Tag: [`ASR-API`](../api-tags/asr-api.md)
- Route: `POST /api/u2/v1/services/audio/asr/transcription`
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- Parameters: None
- Request body: application/json: `input*`{`file_urls*`[string(uri)]}
- Success response: 200 application/json: `request_id*`:string, `output*`{`task_id*`:string, `task_status*`:string, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, `results`[object]}, `usage`{...}
- Full contract: [`api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription`](../api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription)

### Poll U2 job status

- Purpose: Observe job completion. Stay in soft observation after 90 seconds. Trigger U3 fallback only if there is still no result after 120 seconds.
- Tag: [`ASR-API`](../api-tags/asr-api.md)
- Route: `POST /api/u2/v1/tasks/{task_id}`
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- Parameters: path: `task_id*`
- Request body: None
- Success response: 200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`task_id*`:string}, `data*`{`task_id*`:string, `task_status*`:string | null, `platform_task_status*`:string, `is_fully_succeeded*`:boolean, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, ...}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- Full contract: [`api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id`](../api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id)

### Request U3 upload / relay

- Purpose: Use only if U2 still has no result after 120 seconds. Its purpose is to convert a private or non-publicly-readable source link into a public URL.
- Tag: [`Media-Ingest-API`](../api-tags/media-ingest-api.md)
- Route: `POST /api/u3/v1/uploads`
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- Parameters: None
- Request body: application/json: `provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer
- Success response: 200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer}, `data*`{`upload_id*`:string, `provider*`:string, `upload_method*`:string, `upload_url*`:string, `upload_headers*`{...}, `upload_expires_at*`:string, `file_ttl_seconds*`:integer}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- Full contract: [`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads)

### Complete U3 upload and get a public URL

- Purpose: Completion should return a public URL. Submit that URL to U2 ASR again. If it still fails, keep the fact card and return incomplete.
- Tag: [`Media-Ingest-API`](../api-tags/media-ingest-api.md)
- Route: `POST /api/u3/v1/uploads/{upload_id}/complete`
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- Parameters: path: `upload_id*`
- Request body: application/json: dynamic object
- Success response: 200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`upload_id*`:string}, `data*`{`upload_id*`:string, `provider*`:string, `file_url*`:string, `file_expires_at*`:string}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- Full contract: [`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete)

## Execution Notes

- This guide only defines route order and fallback order. It does not replace platform-specific detail-route selection.
- The U1 source route depends on the platform, for example a Douyin or Xiaohongshu detail route. This guide only requires using the returned download URL first.
- If the platform already returns usable `subtitle_raw`, map it directly to `asr_raw` instead of calling U2 or U3.
