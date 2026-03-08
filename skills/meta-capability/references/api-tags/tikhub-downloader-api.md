# TikHub-Downloader-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tikhub-downloader-api.md`
- Full contract: [`api-contracts/tikhub-downloader-api.md`](../api-contracts/tikhub-downloader-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `2`
- Common capabilities: media / download
- Default auth: Header `Authorization` Bearer
- Common inputs: None
- Tag description: **(TikHub下载器接口/TikHub-Downloader-API endpoints)**

## Routes

### `GET /api/u1/v1/tikhub/downloader/redirect_download`

- Summary: 重定向到最新版本的下载链接 / Redirect to the latest version download link
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `redirect_download_api_v1_tikhub_downloader_redirect_download_get`
- Full contract: [`api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-redirect-download`](../api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-redirect-download)

#### Parameters

None

#### Request Body

None

#### Success Response

No declared success response

### `GET /api/u1/v1/tikhub/downloader/version`

- Summary: 检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `update_check_api_v1_tikhub_downloader_version_get`
- Full contract: [`api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-version`](../api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-version)

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `latest_version`:string, `update_date`:string, `download_url`:string, `latest_download_url_win`:string, `latest_download_url_mac`:string, `upload_note`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| latest_version | string | No | None |
| update_date | string | No | None |
| download_url | string | No | None |
| latest_download_url_win | string | No | None |
| latest_download_url_mac | string | No | None |
| upload_note | string | No | None |
