# ASR-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/asr-api.md`
- Full contract: [`api-contracts/asr-api.md`](../api-contracts/asr-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `2`
- Common capabilities: ASR / transcription / audio / media / general
- Default auth: Header `Authorization` Bearer
- Common inputs: `input`, `task_id`
- Tag description: **(ASR 异步任务接口 / ASR async task endpoints)**
- Related service guide: [`service-guides/asr-u2-u3-fallback.md`](../service-guides/asr-u2-u3-fallback.md)

## Routes

### `POST /api/u2/v1/services/audio/asr/transcription`

- Summary: u2 submit
- Capabilities: ASR / transcription / audio / media
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u2Submit`
- Full contract: [`api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription`](../api-contracts/asr-api.md#post-api-u2-v1-services-audio-asr-transcription)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `input*`{`file_urls*`[string(uri)]}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| input | object | Yes | None |
| input.file_urls | array<string(uri)> | Yes | 批量提交 URL，单次范围 1..100；大批量建议优先单次批量提交，避免拆分大量单条 submit / Batch submit URLs, range 1..100 per request. For large workloads,… |

#### Success Response

##### `200 application/json`

- Schema summary: `request_id*`:string, `output*`{`task_id*`:string, `task_status*`:string, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, `results`[object]}, `usage`{...}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| request_id | string | Yes | None |
| output | object | Yes | None |
| output.task_id | string | Yes | None |
| output.task_status | string | Yes | Submit usually returns PENDING/RUNNING. Final status should be checked via query endpoint. |
| output.submit_time | string | No | None |
| output.scheduled_time | string | No | None |
| output.end_time | string | No | None |
| output.task_metrics | object | No | None |
| output.results | array<object> | No | None |
| usage | object | No | None |

### `POST /api/u2/v1/tasks/{task_id}`

- Summary: u2 query
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u2Query`
- Full contract: [`api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id`](../api-contracts/asr-api.md#post-api-u2-v1-tasks-task-id)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| task_id | path | string | Yes | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`task_id*`:string}, `data*`{`task_id*`:string, `task_status*`:string | null, `platform_task_status*`:string, `is_fully_succeeded*`:boolean, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, ...}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| time | string | Yes | Platform response time (America/Los_Angeles). |
| time_stamp | integer | Yes | Unix timestamp in seconds. |
| time_zone | string | Yes | None |
| params | object | Yes | None |
| params.task_id | string | Yes | None |
| data | object | Yes | None |
| data.task_id | string | Yes | None |
| data.task_status | string \| null | Yes | 任务状态快照（用于兼容任务状态枚举）。完成判定请使用 platform_task_status + pending_count / Task status snapshot. Use platform_task_status + pend… |
| data.platform_task_status | string enum[PENDING, PARTIAL_SUCCEEDED, SUCCEEDED, FAILED] | Yes | 批量条目的平台聚合状态 / Aggregated platform status across all input.file_urls items. |
| data.is_fully_succeeded | boolean | Yes | 仅当全部条目成功且 pending_count=0 时为 true / True only when all items succeed and pending_count is 0. |
| data.submit_time | string | No | None |
| data.scheduled_time | string | No | None |

- Fields truncated: this layer shows only the first `12` rows.
