# ASR-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/asr-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`2`
- 常见能力：ASR/字幕转写 / 音频/媒体 / 通用能力
- 常见入参：`input`, `task_id`
- 标签说明：**(ASR 异步任务接口 / ASR async task endpoints)**
- 相关组合 guide：[`service-guides/asr-u2-u3-fallback.md`](../service-guides/asr-u2-u3-fallback.md)

## 路由列表

### `POST /api/u2/v1/services/audio/asr/transcription`

- 能力：ASR/字幕转写 / 音频/媒体
- 入参：无
- 请求体：application/json: `input*`{`file_urls*`[string]}
- 成功响应：200 application/json: `request_id*`:string, `output*`{`task_id*`:string, `task_status*`:string, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, `results`[object]}, `usage`{...}
- operationId：`u2Submit`

### `POST /api/u2/v1/tasks/{task_id}`

- 能力：通用能力
- 入参：path: `task_id*`
- 请求体：无
- 成功响应：200 application/json: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`task_id*`:string}, `data*`{`task_id*`:string, `task_status*`:['string', 'null'], `platform_task_status*`:string, `is_fully_succeeded*`:boolean, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, ...}, `code*`:integer, `request_id*`:string, `message*`:string, ...
- operationId：`u2Query`
