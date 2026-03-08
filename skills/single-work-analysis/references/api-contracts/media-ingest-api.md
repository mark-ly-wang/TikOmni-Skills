# Media-Ingest-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/media-ingest-api.md`](../api-tags/media-ingest-api.md)
- 当前契约文件：`api-contracts/media-ingest-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`2`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(媒体中转接口 / media ingest endpoints)**

## 路由契约

<a id="post-api-u3-v1-uploads"></a>
### `POST /api/u3/v1/uploads`

- 摘要：u3 create upload
- 能力：媒体上传/公网URL
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u3CreateUpload`

#### 说明

> 创建本地文件直传会话。返回一次性 PUT upload_url；客户端完成上传后，再调用 complete 接口换取 24 小时 file_url / Create a direct-upload session for a local file. Returns a short-lived PUT upload_url. After upload succeeds, call complete to obtain a 24-hour file_url.

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| provider | string enum[r2, oss] | 是 | Storage provider used for the temporary upload session. Use `oss` for mainland China networks and `r2` for global/overseas networks / 上传会话使用的存储提供方。中国大陆网络建议使用 `oss`，海外网络建议使用 `r2`。 | 无 | oss | enum[r2, oss] |
| file_name | string | 是 | Original local file name for the upload session / 本地文件原始文件名。 | 无 | 无 | 无 |
| content_type | string | 是 | Declared MIME type. Must match the platform allowlist / 声明的 MIME 类型，必须命中平台白名单。 | 无 | audio/mpeg | 无 |
| size_bytes | integer | 是 | Declared file size in bytes / 声明的文件大小（字节）。 | 无 | 无 | 无 |

#### 成功响应

##### `200 application/json`

- Schema 摘要：`time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer}, `data*`{`upload_id*`:string, `provider*`:string, `upload_method*`:string, `upload_url*`:string, `upload_headers*`{...}, `upload_expires_at*`:string, `file_ttl_seconds*`:integer}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| time | string | 是 | 无 | 无 | 无 | 无 |
| time_stamp | integer | 是 | 无 | 无 | 无 | 无 |
| time_zone | string | 是 | 无 | 无 | America/Los_Angeles | 无 |
| params | object | 是 | 无 | 无 | 无 | 无 |
| params.provider | string enum[r2, oss] | 是 | 无 | 无 | 无 | enum[r2, oss] |
| params.file_name | string | 是 | 无 | 无 | 无 | 无 |
| params.content_type | string | 是 | 无 | 无 | 无 | 无 |
| params.size_bytes | integer | 是 | 无 | 无 | 无 | 无 |
| data | object | 是 | 无 | 无 | 无 | 无 |
| data.upload_id | string | 是 | 无 | 无 | 无 | 无 |
| data.provider | string enum[r2, oss] | 是 | 无 | 无 | 无 | enum[r2, oss] |
| data.upload_method | string enum[PUT] | 是 | 无 | 无 | 无 | enum[PUT] |
| data.upload_url | string(uri) | 是 | 无 | 无 | 无 | 无 |
| data.upload_headers | object | 是 | 无 | 无 | 无 | 无 |
| data.upload_expires_at | string(date-time) | 是 | 无 | 无 | 无 | 无 |
| data.file_ttl_seconds | integer | 是 | Lifetime of the file_url returned by completeUpload / completeUpload 返回 file_url 的有效秒数。 | 无 | 86400 | 无 |
| code | integer | 是 | 无 | 无 | 200 | 无 |
| request_id | string | 是 | 无 | 无 | 无 | 无 |
| message | string | 是 | 无 | 无 | Request successful | 无 |
| message_zh | string | 是 | 无 | 无 | 请求成功 | 无 |
| router | string | 是 | 无 | 无 | 无 | 无 |

<a id="post-api-u3-v1-uploads-upload-id-complete"></a>
### `POST /api/u3/v1/uploads/{upload_id}/complete`

- 摘要：u3 complete upload
- 能力：媒体上传/公网URL
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`u3CompleteUpload`

#### 说明

> 确认上传完成并签发 file_url。file_url 默认 24 小时有效，可直接传给 u2 submit / Finalize the upload session and issue file_url. The file_url is valid for 24 hours by default and can be passed directly to u2 submit.

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| upload_id | path | string | 是 | 无 | 无 | 无 | 无 |

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：动态对象

无字段表

#### 成功响应

##### `200 application/json`

- Schema 摘要：`time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`upload_id*`:string}, `data*`{`upload_id*`:string, `provider*`:string, `file_url*`:string, `file_expires_at*`:string}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| time | string | 是 | 无 | 无 | 无 | 无 |
| time_stamp | integer | 是 | 无 | 无 | 无 | 无 |
| time_zone | string | 是 | 无 | 无 | America/Los_Angeles | 无 |
| params | object | 是 | 无 | 无 | 无 | 无 |
| params.upload_id | string | 是 | 无 | 无 | 无 | 无 |
| data | object | 是 | 无 | 无 | 无 | 无 |
| data.upload_id | string | 是 | 无 | 无 | 无 | 无 |
| data.provider | string enum[r2, oss] | 是 | 无 | 无 | 无 | enum[r2, oss] |
| data.file_url | string(uri) | 是 | 无 | 无 | 无 | 无 |
| data.file_expires_at | string(date-time) | 是 | 无 | 无 | 无 | 无 |
| code | integer | 是 | 无 | 无 | 200 | 无 |
| request_id | string | 是 | 无 | 无 | 无 | 无 |
| message | string | 是 | 无 | 无 | Request successful | 无 |
| message_zh | string | 是 | 无 | 无 | 请求成功 | 无 |
| router | string | 是 | 无 | 无 | 无 | 无 |
