# Media-Ingest-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/media-ingest-api.md`
- 完整契约：[`api-contracts/media-ingest-api.md`](../api-contracts/media-ingest-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`2`
- 常见能力：媒体上传/公网URL
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`provider`, `file_name`, `content_type`, `size_bytes`, `upload_id`
- 标签说明：**(媒体中转接口 / media ingest endpoints)**
- 相关组合 guide：[`service-guides/asr-u2-u3-fallback.md`](../service-guides/asr-u2-u3-fallback.md)

## 路由列表

### `POST /api/u3/v1/uploads`

- 摘要：u3 create upload
- 能力：媒体上传/公网URL
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u3CreateUpload`
- 完整契约：[`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| provider | string enum[r2, oss] | 是 | Storage provider used for the temporary upload session. Use `oss` for mainland China networks and `r2` for global/overs… |
| file_name | string | 是 | Original local file name for the upload session / 本地文件原始文件名。 |
| content_type | string | 是 | Declared MIME type. Must match the platform allowlist / 声明的 MIME 类型，必须命中平台白名单。 |
| size_bytes | integer | 是 | Declared file size in bytes / 声明的文件大小（字节）。 |

#### 成功响应

##### `200 application/json`

- Schema 摘要：`time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer}, `data*`{`upload_id*`:string, `provider*`:string, `upload_method*`:string, `upload_url*`:string, `upload_headers*`{...}, `upload_expires_at*`:string, `file_ttl_seconds*`:integer}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | string | 是 | 无 |
| time_stamp | integer | 是 | 无 |
| time_zone | string | 是 | 无 |
| params | object | 是 | 无 |
| params.provider | string enum[r2, oss] | 是 | 无 |
| params.file_name | string | 是 | 无 |
| params.content_type | string | 是 | 无 |
| params.size_bytes | integer | 是 | 无 |
| data | object | 是 | 无 |
| data.upload_id | string | 是 | 无 |
| data.provider | string enum[r2, oss] | 是 | 无 |
| data.upload_method | string enum[PUT] | 是 | 无 |

- 字段已截断：当前层仅展示前 `12` 行。

### `POST /api/u3/v1/uploads/{upload_id}/complete`

- 摘要：u3 complete upload
- 能力：媒体上传/公网URL
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u3CompleteUpload`
- 完整契约：[`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| upload_id | path | string | 是 | 无 |

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：动态对象

无字段表

#### 成功响应

##### `200 application/json`

- Schema 摘要：`time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`upload_id*`:string}, `data*`{`upload_id*`:string, `provider*`:string, `file_url*`:string, `file_expires_at*`:string}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | string | 是 | 无 |
| time_stamp | integer | 是 | 无 |
| time_zone | string | 是 | 无 |
| params | object | 是 | 无 |
| params.upload_id | string | 是 | 无 |
| data | object | 是 | 无 |
| data.upload_id | string | 是 | 无 |
| data.provider | string enum[r2, oss] | 是 | 无 |
| data.file_url | string(uri) | 是 | 无 |
| data.file_expires_at | string(date-time) | 是 | 无 |
| code | integer | 是 | 无 |
| request_id | string | 是 | 无 |

- 字段已截断：当前层仅展示前 `12` 行。
