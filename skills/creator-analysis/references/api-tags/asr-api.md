# ASR-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/asr-api.md`
- 完整契约：[`api-contracts/asr-api.md`](../api-contracts/asr-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`2`
- 常见能力：ASR/字幕转写 / 音频/媒体 / 通用能力
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`input`, `task_id`
- 标签说明：**(ASR 异步任务接口 / ASR async task endpoints)**
- 相关组合 guide：[`service-guides/asr-u2-u3-fallback.md`](../service-guides/asr-u2-u3-fallback.md)

## 路由列表

### `POST /api/u2/v1/services/audio/asr/transcription`

- 摘要：u2 submit
- 能力：ASR/字幕转写 / 音频/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u2Submit`
- 完整契约：[`api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription`](../api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`input*`{`file_urls*`[string(uri)]}

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | object | 是 | 无 |
| input.file_urls | array<string(uri)> | 是 | 批量提交 URL，单次范围 1..100；大批量建议优先单次批量提交，避免拆分大量单条 submit / Batch submit URLs, range 1..100 per request. For large workloads,… |

#### 成功响应

##### `200 application/json`

- Schema 摘要：`request_id*`:string, `output*`{`task_id*`:string, `task_status*`:string, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, `results`[object]}, `usage`{...}

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request_id | string | 是 | 无 |
| output | object | 是 | 无 |
| output.task_id | string | 是 | 无 |
| output.task_status | string | 是 | Submit usually returns PENDING/RUNNING. Final status should be checked via query endpoint. |
| output.submit_time | string | 否 | 无 |
| output.scheduled_time | string | 否 | 无 |
| output.end_time | string | 否 | 无 |
| output.task_metrics | object | 否 | 无 |
| output.results | array<object> | 否 | 无 |
| usage | object | 否 | 无 |

### `POST /api/u2/v1/tasks/{task_id}`

- 摘要：u2 query
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u2Query`
- 完整契约：[`api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id`](../api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| task_id | path | string | 是 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`task_id*`:string}, `data*`{`task_id*`:string, `task_status*`:string | null, `platform_task_status*`:string, `is_fully_succeeded*`:boolean, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, ...}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | string | 是 | Platform response time (America/Los_Angeles). |
| time_stamp | integer | 是 | Unix timestamp in seconds. |
| time_zone | string | 是 | 无 |
| params | object | 是 | 无 |
| params.task_id | string | 是 | 无 |
| data | object | 是 | 无 |
| data.task_id | string | 是 | 无 |
| data.task_status | string \| null | 是 | 任务状态快照（用于兼容任务状态枚举）。完成判定请使用 platform_task_status + pending_count / Task status snapshot. Use platform_task_status + pend… |
| data.platform_task_status | string enum[PENDING, PARTIAL_SUCCEEDED, SUCCEEDED, FAILED] | 是 | 批量条目的平台聚合状态 / Aggregated platform status across all input.file_urls items. |
| data.is_fully_succeeded | boolean | 是 | 仅当全部条目成功且 pending_count=0 时为 true / True only when all items succeed and pending_count is 0. |
| data.submit_time | string | 否 | 无 |
| data.scheduled_time | string | 否 | 无 |

- 字段已截断：当前层仅展示前 `12` 行。
