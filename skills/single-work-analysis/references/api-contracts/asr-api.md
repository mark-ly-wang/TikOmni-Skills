# ASR-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/asr-api.md`](../api-tags/asr-api.md)
- 当前契约文件：`api-contracts/asr-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`2`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(ASR 异步任务接口 / ASR async task endpoints)**

## 路由契约

<a id="post-api-u2-v1-services-audio-asr-transcription"></a>
### `POST /api/u2/v1/services/audio/asr/transcription`

- 摘要：u2 submit
- 能力：ASR/字幕转写 / 音频/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u2Submit`

#### 说明

> 创建异步转写任务。单次请求支持 1..100 条 input.file_urls；大批量建议优先批量 submit，避免拆分大量单条 submit。submit 返回 200 仅表示已受理，最终状态请以 query 判定 / Create async transcription task. One request accepts 1..100 input.file_urls. For large workloads, prefer batch submit instead of many single submits. Submit 200 only means accepted; final status must be judged via query endpoint.

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`input*`{`file_urls*`[string(uri)]}

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| input | object | 是 | 无 | 无 | 无 | 无 |
| input.file_urls | array<string(uri)> | 是 | 批量提交 URL，单次范围 1..100；大批量建议优先单次批量提交，避免拆分大量单条 submit / Batch submit URLs, range 1..100 per request. For large workloads, prefer one batch submit over many single submits. | 无 | 无 | 无 |

#### 成功响应

##### `200 application/json`

- Schema 摘要：`request_id*`:string, `output*`{`task_id*`:string, `task_status*`:string, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, `results`[object]}, `usage`{...}

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| request_id | string | 是 | 无 | 无 | 无 | 无 |
| output | object | 是 | 无 | 无 | 无 | 无 |
| output.task_id | string | 是 | 无 | 无 | 无 | 无 |
| output.task_status | string | 是 | Submit usually returns PENDING/RUNNING. Final status should be checked via query endpoint. | 无 | PENDING | 无 |
| output.submit_time | string | 否 | 无 | 无 | 无 | 无 |
| output.scheduled_time | string | 否 | 无 | 无 | 无 | 无 |
| output.end_time | string | 否 | 无 | 无 | 无 | 无 |
| output.task_metrics | object | 否 | 无 | 无 | 无 | 无 |
| output.results | array<object> | 否 | 无 | 无 | 无 | 无 |
| output.results[] | object | 是 | 无 | 无 | 无 | 无 |
| usage | object | 否 | 无 | 无 | 无 | 无 |

<a id="post-api-u2-v1-tasks-task-id"></a>
### `POST /api/u2/v1/tasks/{task_id}`

- 摘要：u2 query
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u2Query`

#### 说明

> 查询任务状态。网关保留上游 task_status，并返回平台聚合状态。若客户端不轮询，平台也会在后台持续 reconcile 直到拿到终态并完成结算。判定规则：全部成功=platform_task_status=SUCCEEDED 且 pending_count=0；部分成功=PARTIAL_SUCCEEDED 且 pending_count=0；失败=FAILED 且 pending_count=0；处理中=pending_count>0。sentences/full_text 仅在全部成功时返回 / Query task status. The gateway preserves the upstream task_status and also returns platform aggregate status. Even if clients stop polling, the platform continues background reconcile until the task reaches a terminal state and billing is settled. Completion rules: SUCCEEDED => platform_task_status=SUCCEEDED and pending_count=0; PARTIAL => PARTIAL_SUCCEEDED and pending_count=0; FAILED => FAILED and pending_count=0; in-progress => pending_count>0. sentences/full_text are returned only when all items succeed.

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| task_id | path | string | 是 | 无 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`task_id*`:string}, `data*`{`task_id*`:string, `task_status*`:string | null, `platform_task_status*`:string, `is_fully_succeeded*`:boolean, `submit_time`:string, `scheduled_time`:string, `end_time`:string, `task_metrics`{...}, ...}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| time | string | 是 | Platform response time (America/Los_Angeles). | 无 | 无 | 无 |
| time_stamp | integer | 是 | Unix timestamp in seconds. | 无 | 无 | 无 |
| time_zone | string | 是 | 无 | 无 | America/Los_Angeles | 无 |
| params | object | 是 | 无 | 无 | 无 | 无 |
| params.task_id | string | 是 | 无 | 无 | 无 | 无 |
| data | object | 是 | 无 | 无 | 无 | 无 |
| data.task_id | string | 是 | 无 | 无 | 无 | 无 |
| data.task_status | string \| null | 是 | 任务状态快照（用于兼容任务状态枚举）。完成判定请使用 platform_task_status + pending_count / Task status snapshot. Use platform_task_status + pending_count for completion judgment. | 无 | SUCCEEDED | 无 |
| data.platform_task_status | string enum[PENDING, PARTIAL_SUCCEEDED, SUCCEEDED, FAILED] | 是 | 批量条目的平台聚合状态 / Aggregated platform status across all input.file_urls items. | 无 | PARTIAL_SUCCEEDED | enum[PENDING, PARTIAL_SUCCEEDED, SUCCEEDED, FAILED] |
| data.is_fully_succeeded | boolean | 是 | 仅当全部条目成功且 pending_count=0 时为 true / True only when all items succeed and pending_count is 0. | 无 | 无 | 无 |
| data.submit_time | string | 否 | 无 | 无 | 无 | 无 |
| data.scheduled_time | string | 否 | 无 | 无 | 无 | 无 |
| data.end_time | string | 否 | 无 | 无 | 无 | 无 |
| data.task_metrics | object | 否 | 无 | 无 | 无 | 无 |
| data.duration_sec | integer | 是 | 计费总时长（仅统计成功条目，单位秒）/ Billable total duration in seconds from succeeded items only. | 无 | 无 | 无 |
| data.input_count | integer | 是 | 无 | 无 | 无 | 无 |
| data.succeeded_count | integer | 是 | 无 | 无 | 无 | 无 |
| data.failed_count | integer | 是 | 无 | 无 | 无 | 无 |
| data.pending_count | integer | 是 | 无 | 无 | 无 | 无 |
| data.items | array<object> | 是 | 条目级状态列表，按 item_index 对齐 input.file_urls 顺序 / Per-item status aligned with input.file_urls order by item_index. | 无 | 无 | 无 |
| data.items[] | object | 是 | 无 | 无 | 无 | 无 |
| data.items[].item_index | integer | 是 | 无 | 无 | 无 | 无 |
| data.items[].task_status | string \| null | 是 | 无 | 无 | 无 | 无 |
| data.items[].transcription_url | string \| null(uri) | 否 | 无 | 无 | 无 | 无 |
| data.items[].duration_sec | integer \| null | 否 | 无 | 无 | 无 | 无 |
| data.items[].error_code | string \| null | 否 | 无 | 无 | 无 | 无 |
| data.items[].error_message | string \| null | 否 | 无 | 无 | 无 | 无 |
| data.sentences | array<object> | 否 | 仅在 platform_task_status=SUCCEEDED 时返回 / Returned only when platform_task_status is SUCCEEDED. | 无 | 无 | 无 |
| data.sentences[] | object | 是 | 无 | 无 | 无 | 无 |
| data.sentences[].sentence_id | integer | 是 | 无 | 无 | 无 | 无 |
| data.sentences[].text | string | 是 | 无 | 无 | 无 | 无 |
| data.full_text | string | 否 | 仅在 platform_task_status=SUCCEEDED 时返回 / Returned only when platform_task_status is SUCCEEDED. | 无 | 无 | 无 |
| code | integer | 是 | 无 | 无 | 200 | 无 |
| request_id | string | 是 | 无 | 无 | 无 | 无 |
| message | string | 是 | 无 | 无 | Request successful | 无 |
| message_zh | string | 是 | 无 | 无 | 请求成功 | 无 |
| router | string | 是 | 无 | 无 | 无 | 无 |
