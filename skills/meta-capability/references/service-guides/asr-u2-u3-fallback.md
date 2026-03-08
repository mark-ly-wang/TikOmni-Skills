# U2 ASR 与 U3 公网 URL Fallback

## 用途

- 这个 guide 用于视频 ASR 主路径和超时 fallback，不用于文本作品。
- 默认必须先走 U2 ASR；U3 只能作为 fallback，不允许直接绕过 U2。
- 当 U1 详情接口返回的是无水印下载链接或下载链接，但该链接可能不是公网可读 URL 时，用本 guide 判断何时转入 U3。
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`

## 固定策略

1. 先调用 U1 详情接口，拿到 `video_download_url`、无水印下载链接或其他可直接下载媒体链接。
2. 直接用该链接提交 U2 ASR，不允许默认先走 U3。
3. 90 秒仍未返回完整结果，只进入软观察，不切换主路径。
4. 120 秒（2 分钟）仍未返回结果或未返回完整结果，判定源链接大概率不是公网可读 URL，才允许进入 U3 fallback。
5. U3 完成后必须拿公网可读 URL，再次提交 U2 ASR。
6. 如果 U3 或二次 U2 仍失败，保留事实卡并返回 `incomplete`；不要伪造主文本或分析结论。

## 场景补充

- 单作品：对当前作品单独执行这条链路。
- Creator 批量：只对 120 秒后仍未成功的子集走 U3 fallback，不要把整批已成功项重新上传。

## 路由事实

### U2 提交 ASR 任务

- 说明：默认主路径。先用 U1 返回的无水印下载链接或下载链接直接提交 ASR，不允许先走 U3。
- Tag：[`ASR-API`](../api-tags/asr-api.md)
- Route：`POST /api/u2/v1/services/audio/asr/transcription`
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- 入参：无
- 请求体：application/json: `input*`{`file_urls*`[string(uri)]}
- 成功响应：200 application/json: `request_id*`:string, `output*`{`task_id*`:string, `task_status*`:string, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, `results`[object]}, `usage`{...}
- 完整契约：[`api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription`](../api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription)

### U2 轮询任务状态

- 说明：用于观察任务完成度。90 秒仍未完成时进入软观察，120 秒（2 分钟）仍无结果时触发 U3 fallback。
- Tag：[`ASR-API`](../api-tags/asr-api.md)
- Route：`POST /api/u2/v1/tasks/{task_id}`
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- 入参：path: `task_id*`
- 请求体：无
- 成功响应：200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`task_id*`:string}, `data*`{`task_id*`:string, `task_status*`:string | null, `platform_task_status*`:string, `is_fully_succeeded*`:boolean, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, ...}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- 完整契约：[`api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id`](../api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id)

### U3 申请上传/中转

- 说明：仅在 U2 超过 120 秒仍无结果时使用。它的目标是把私有或非公网可读源链接转成公网可读 URL。
- Tag：[`Media-Ingest-API`](../api-tags/media-ingest-api.md)
- Route：`POST /api/u3/v1/uploads`
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- 入参：无
- 请求体：application/json: `provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer
- 成功响应：200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer}, `data*`{`upload_id*`:string, `provider*`:string, `upload_method*`:string, `upload_url*`:string, `upload_headers*`{...}, `upload_expires_at*`:string, `file_ttl_seconds*`:integer}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- 完整契约：[`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads)

### U3 完成上传并获取公网 URL

- 说明：完成后应拿到公网可读 URL，再次回调 U2 ASR。若仍失败，则保留事实卡并返回 incomplete。
- Tag：[`Media-Ingest-API`](../api-tags/media-ingest-api.md)
- Route：`POST /api/u3/v1/uploads/{upload_id}/complete`
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- 入参：path: `upload_id*`
- 请求体：application/json: 动态对象
- 成功响应：200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`upload_id*`:string}, `data*`{`upload_id*`:string, `provider*`:string, `file_url*`:string, `file_expires_at*`:string}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- 完整契约：[`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete)

## 执行备注

- 本 guide 只定义路由选择和 fallback 顺序，不替代各平台自己的 detail route 选择。
- U1 来源 route 由平台决定，例如抖音/小红书的 detail route；本 guide 只要求优先使用它们返回的下载链接。
- 如果平台已直接返回可用 `subtitle_raw`，优先直接映射为 `asr_raw`，不必再走 U2/U3。
