# Media-Ingest-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/media-ingest-api.md`
- Full contract: [`api-contracts/media-ingest-api.md`](../api-contracts/media-ingest-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `2`
- Common capabilities: media upload / public URL
- Default auth: Header `Authorization` Bearer
- Common inputs: `provider`, `file_name`, `content_type`, `size_bytes`, `upload_id`
- Tag description: **(媒体中转接口 / media ingest endpoints)**
- Related service guide: [`service-guides/asr-u2-u3-fallback.md`](../service-guides/asr-u2-u3-fallback.md)

## Routes

### `POST /api/u3/v1/uploads`

- Summary: u3 create upload
- Capabilities: media upload / public URL
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u3CreateUpload`
- Full contract: [`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| provider | string enum[r2, oss] | Yes | Storage provider used for the temporary upload session. Use `oss` for mainland China networks and `r2` for global/overs… |
| file_name | string | Yes | Original local file name for the upload session / 本地文件原始文件名。 |
| content_type | string | Yes | Declared MIME type. Must match the platform allowlist. Current default allowlist: `audio/mpeg`, `audio/mp4`, `audio/wav… |
| size_bytes | integer | Yes | Declared file size in bytes / 声明的文件大小（字节）。 |

#### Success Response

##### `200 application/json`

- Schema summary: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`provider*`:string, `file_name*`:string, `content_type*`:string, `size_bytes*`:integer}, `data*`{`upload_id*`:string, `provider*`:string, `upload_method*`:string, `upload_url*`:string, `upload_headers*`{...}, `upload_expires_at*`:string, `file_ttl_seconds*`:integer}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| time | string | Yes | None |
| time_stamp | integer | Yes | None |
| time_zone | string | Yes | None |
| params | object | Yes | None |
| params.provider | string enum[r2, oss] | Yes | None |
| params.file_name | string | Yes | None |
| params.content_type | string | Yes | None |
| params.size_bytes | integer | Yes | None |
| data | object | Yes | None |
| data.upload_id | string | Yes | None |
| data.provider | string enum[r2, oss] | Yes | None |
| data.upload_method | string enum[PUT] | Yes | None |

- Fields truncated: this layer shows only the first `12` rows.

### `POST /api/u3/v1/uploads/{upload_id}/complete`

- Summary: u3 complete upload
- Capabilities: media upload / public URL
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `u3CompleteUpload`
- Full contract: [`api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete`](../api-contracts/media-ingest-api.md#post-api-u3-v1-uploads-upload-id-complete)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| upload_id | path | string | Yes | None |

#### Request Body

- required: No

##### `application/json`

- Schema summary: dynamic object

No field table

#### Success Response

##### `200 application/json`

- Schema summary: `time*`:string, `time_stamp*`:integer, `time_zone*`:string, `params*`{`upload_id*`:string}, `data*`{`upload_id*`:string, `provider*`:string, `file_url*`:string, `file_expires_at*`:string}, `code*`:integer, `request_id*`:string, `message*`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| time | string | Yes | None |
| time_stamp | integer | Yes | None |
| time_zone | string | Yes | None |
| params | object | Yes | None |
| params.upload_id | string | Yes | None |
| data | object | Yes | None |
| data.upload_id | string | Yes | None |
| data.provider | string enum[r2, oss] | Yes | None |
| data.file_url | string(uri) | Yes | None |
| data.file_expires_at | string(date-time) | Yes | None |
| code | integer | Yes | None |
| request_id | string | Yes | None |

- Fields truncated: this layer shows only the first `12` rows.
