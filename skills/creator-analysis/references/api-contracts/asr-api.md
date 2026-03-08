# ASR-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/asr-api.md`](../api-tags/asr-api.md)
- Current contract file: `api-contracts/asr-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `2`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(ASR 异步任务接口 / ASR async task endpoints)**

## Route Contracts

<a id="post-api-u2-v1-services-audio-asr-transcription"></a>
### `POST /api/u2/v1/services/audio/asr/transcription`

- Summary: u2 submit
- Capabilities: ASR / transcription / audio / media
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u2Submit`

#### Notes

> 创建异步转写任务。单次请求支持 1..100 条 input.file_urls；大批量建议优先批量 submit，避免拆分大量单条 submit。submit 返回 200 仅表示已受理，最终状态请以 query 判定 / Create async transcription task. One request accepts 1..100 input.file_urls. For large workloads, prefer batch submit instead of many single submits. Submit 200 only means accepted; final status must be judged via query endpoint.

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `input*`{`file_urls*`[string(uri)]}

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| input | object | Yes | None | None | None | None |
| input.file_urls | array<string(uri)> | Yes | 批量提交 URL，单次范围 1..100；大批量建议优先单次批量提交，避免拆分大量单条 submit / Batch submit URLs, range 1..100 per request. For large workloads, prefer one batch submit over many single submits. | None | None | None |

#### Success Response

##### `200 application/json`

- Schema summary: `request_id*`:string, `output*`{`task_id*`:string, `task_status*`:string, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, `results`[object]}, `usage`{...}

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| request_id | string | Yes | None | None | None | None |
| output | object | Yes | None | None | None | None |
| output.task_id | string | Yes | None | None | None | None |
| output.task_status | string | Yes | Submit usually returns PENDING/RUNNING. Final status should be checked via query endpoint. | None | PENDING | None |
| output.submit_time | string | No | None | None | None | None |
| output.scheduled_time | string | No | None | None | None | None |
| output.end_time | string | No | None | None | None | None |
| output.task_metrics | object | No | None | None | None | None |
| output.results | array<object> | No | None | None | None | None |
| output.results[] | object | Yes | None | None | None | None |
| usage | object | No | None | None | None | None |

<a id="post-api-u2-v1-tasks-task-id"></a>
### `POST /api/u2/v1/tasks/{task_id}`

- Summary: u2 query
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u2Query`

#### Notes

> 查询任务状态。网关保留上游 task_status，并返回平台聚合状态。若客户端不轮询，平台也会在后台持续 reconcile 直到拿到终态并完成结算。判定规则：全部成功=platform_task_status=SUCCEEDED 且 pending_count=0；部分成功=PARTIAL_SUCCEEDED 且 pending_count=0；失败=FAILED 且 pending_count=0；处理中=pending_count>0。sentences/full_text 仅在全部成功时返回 / Query task status. The gateway preserves the upstream task_status and also returns platform aggregate status. Even if clients stop polling, the platform continues background reconcile until the task reaches a terminal state and billing is settled. Completion rules: SUCCEEDED => platform_task_status=SUCCEEDED and pending_count=0; PARTIAL => PARTIAL_SUCCEEDED and pending_count=0; FAILED => FAILED and pending_count=0; in-progress => pending_count>0. sentences/full_text are returned only when all items succeed.

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| task_id | path | string | Yes | None | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`task_id*`:string}, `data*`{`task_id*`:string, `task_status*`:string | null, `platform_task_status*`:string, `is_fully_succeeded*`:boolean, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, ...}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| time | string | Yes | Platform response time (America/Los_Angeles). | None | None | None |
| time_stamp | integer | Yes | Unix timestamp in seconds. | None | None | None |
| time_zone | string | Yes | None | None | America/Los_Angeles | None |
| params | object | Yes | None | None | None | None |
| params.task_id | string | Yes | None | None | None | None |
| data | object | Yes | None | None | None | None |
| data.task_id | string | Yes | None | None | None | None |
| data.task_status | string \| null | Yes | 任务状态快照（用于兼容任务状态枚举）。完成判定请使用 platform_task_status + pending_count / Task status snapshot. Use platform_task_status + pending_count for completion judgment. | None | SUCCEEDED | None |
| data.platform_task_status | string enum[PENDING, PARTIAL_SUCCEEDED, SUCCEEDED, FAILED] | Yes | 批量条目的平台聚合状态 / Aggregated platform status across all input.file_urls items. | None | PARTIAL_SUCCEEDED | enum[PENDING, PARTIAL_SUCCEEDED, SUCCEEDED, FAILED] |
| data.is_fully_succeeded | boolean | Yes | 仅当全部条目成功且 pending_count=0 时为 true / True only when all items succeed and pending_count is 0. | None | None | None |
| data.submit_time | string | No | None | None | None | None |
| data.scheduled_time | string | No | None | None | None | None |
| data.end_time | string | No | None | None | None | None |
| data.task_metrics | object | No | None | None | None | None |
| data.duration_sec | integer | Yes | 计费总时长（仅统计成功条目，单位秒）/ Billable total duration in seconds from succeeded items only. | None | None | None |
| data.input_count | integer | Yes | None | None | None | None |
| data.succeeded_count | integer | Yes | None | None | None | None |
| data.failed_count | integer | Yes | None | None | None | None |
| data.pending_count | integer | Yes | None | None | None | None |
| data.items | array<object> | Yes | 条目级状态列表，按 item_index 对齐 input.file_urls 顺序 / Per-item status aligned with input.file_urls order by item_index. | None | None | None |
| data.items[] | object | Yes | None | None | None | None |
| data.items[].item_index | integer | Yes | None | None | None | None |
| data.items[].task_status | string \| null | Yes | None | None | None | None |
| data.items[].transcription_url | string \| null(uri) | No | None | None | None | None |
| data.items[].duration_sec | integer \| null | No | None | None | None | None |
| data.items[].error_code | string \| null | No | None | None | None | None |
| data.items[].error_message | string \| null | No | None | None | None | None |
| data.sentences | array<object> | No | 仅在 platform_task_status=SUCCEEDED 时返回 / Returned only when platform_task_status is SUCCEEDED. | None | None | None |
| data.sentences[] | object | Yes | None | None | None | None |
| data.sentences[].sentence_id | integer | Yes | None | None | None | None |
| data.sentences[].text | string | Yes | None | None | None | None |
| data.full_text | string | No | 仅在 platform_task_status=SUCCEEDED 时返回 / Returned only when platform_task_status is SUCCEEDED. | None | None | None |
| code | integer | Yes | None | None | 200 | None |
| request_id | string | Yes | None | None | None | None |
| message | string | Yes | None | None | Request successful | None |
| message_zh | string | Yes | None | None | 请求成功 | None |
| router | string | Yes | None | None | None | None |
