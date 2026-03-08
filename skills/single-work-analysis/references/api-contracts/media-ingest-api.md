# Media-Ingest-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/media-ingest-api.md`](../api-tags/media-ingest-api.md)
- Current contract file: `api-contracts/media-ingest-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `2`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(媒体中转接口 / media ingest endpoints)**

## Route Contracts

<a id="post-api-u3-v1-uploads"></a>
### `POST /api/u3/v1/uploads`

- Summary: u3 create upload
- Capabilities: media upload / public URL
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u3CreateUpload`

#### Notes

> 创建本地文件直传会话。需要 `Authorization: Bearer <API_KEY>`。返回一次性 PUT upload_url；客户端完成上传后，再调用 complete 接口换取 24 小时 file_url / Create a direct-upload session for a local file. Requires `Authorization: Bearer <API_KEY>`. Returns a short-lived PUT upload_url. After upload succeeds, call complete to obtain a 24-hour file_url.

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| provider | string enum[r2, oss] | Yes | Storage provider used for the temporary upload session. Use `oss` for mainland China networks and `r2` for global/overseas networks / 上传会话使用的存储提供方。中国大陆网络建议使用 `oss`，海外网络建议使用 `r2`。 | None | oss | enum[r2, oss] |
| file_name | string | Yes | Original local file name for the upload session / 本地文件原始文件名。 | None | sample.mov | None |
| content_type | string | Yes | Declared MIME type. Must match the platform allowlist. Current default allowlist: `audio/mpeg`, `audio/mp4`, `audio/wav`, `audio/x-wav`, `audio/webm`, `video/mp4`, `video/quicktim… | None | video/quicktime | None |
| size_bytes | integer | Yes | Declared file size in bytes / 声明的文件大小（字节）。 | None | 7340032 | None |

#### Success Response

##### `200 application/json`

- Schema summary: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer}, `data*`{`upload_id*`:string, `provider*`:string, `upload_method*`:string, `upload_url*`:string, `upload_headers*`{...}, `upload_expires_at*`:string, `file_ttl_seconds*`:integer}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| time | string | Yes | None | None | None | None |
| time_stamp | integer | Yes | None | None | None | None |
| time_zone | string | Yes | None | None | America/Los_Angeles | None |
| params | object | Yes | None | None | None | None |
| params.provider | string enum[r2, oss] | Yes | None | None | None | enum[r2, oss] |
| params.file_name | string | Yes | None | None | None | None |
| params.content_type | string | Yes | None | None | None | None |
| params.size_bytes | integer | Yes | None | None | None | None |
| data | object | Yes | None | None | None | None |
| data.upload_id | string | Yes | None | None | None | None |
| data.provider | string enum[r2, oss] | Yes | None | None | None | enum[r2, oss] |
| data.upload_method | string enum[PUT] | Yes | None | None | None | enum[PUT] |
| data.upload_url | string(uri) | Yes | None | None | None | None |
| data.upload_headers | object | Yes | None | None | None | None |
| data.upload_expires_at | string(date-time) | Yes | None | None | None | None |
| data.file_ttl_seconds | integer | Yes | Lifetime of the file_url returned by completeUpload / completeUpload 返回 file_url 的有效秒数。 | None | 86400 | None |
| code | integer | Yes | None | None | 200 | None |
| request_id | string | Yes | None | None | None | None |
| message | string | Yes | None | None | Request successful | None |
| message_zh | string | Yes | None | None | 请求成功 | None |
| router | string | Yes | None | None | None | None |

<a id="post-api-u3-v1-uploads-upload-id-complete"></a>
### `POST /api/u3/v1/uploads/{upload_id}/complete`

- Summary: u3 complete upload
- Capabilities: media upload / public URL
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u3CompleteUpload`

#### Notes

> 确认上传完成并签发 file_url。需要 `Authorization: Bearer <API_KEY>`。file_url 默认 24 小时有效，可直接传给 u2 submit / Finalize the upload session and issue file_url. Requires `Authorization: Bearer <API_KEY>`. The file_url is valid for 24 hours by default and can be passed directly to u2 submit.

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| upload_id | path | string | Yes | None | None | None | None |

#### Request Body

- required: No

##### `application/json`

- Schema summary: dynamic object

No field table

#### Success Response

##### `200 application/json`

- Schema summary: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`upload_id*`:string}, `data*`{`upload_id*`:string, `provider*`:string, `file_url*`:string, `file_expires_at*`:string}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| time | string | Yes | None | None | None | None |
| time_stamp | integer | Yes | None | None | None | None |
| time_zone | string | Yes | None | None | America/Los_Angeles | None |
| params | object | Yes | None | None | None | None |
| params.upload_id | string | Yes | None | None | None | None |
| data | object | Yes | None | None | None | None |
| data.upload_id | string | Yes | None | None | None | None |
| data.provider | string enum[r2, oss] | Yes | None | None | None | enum[r2, oss] |
| data.file_url | string(uri) | Yes | None | None | None | None |
| data.file_expires_at | string(date-time) | Yes | None | None | None | None |
| code | integer | Yes | None | None | 200 | None |
| request_id | string | Yes | None | None | None | None |
| message | string | Yes | None | None | Request successful | None |
| message_zh | string | Yes | None | None | 请求成功 | None |
| router | string | Yes | None | None | None | None |
