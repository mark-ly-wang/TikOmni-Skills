# TikHub-Downloader-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/tikhub-downloader-api.md`](../api-tags/tikhub-downloader-api.md)
- Current contract file: `api-contracts/tikhub-downloader-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `2`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(TikHub下载器接口/TikHub-Downloader-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-tikhub-downloader-redirect-download"></a>
### `GET /api/u1/v1/tikhub/downloader/redirect_download`

- Summary: 重定向到最新版本的下载链接 / Redirect to the latest version download link
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `redirect_download_api_v1_tikhub_downloader_redirect_download_get`

#### Notes

> # [中文]
>
> ### 用途说明:
>
> - 该接口用于检测客户端操作系统，并重定向到相应的 GitHub Release 直链，方便用户请求后直接开始下载最新版本的文件。
>
> ### 参数说明:
>
> - 无参数。
>
> ### 返回结果:
>
> - Windows 用户：重定向到 `.exe` 下载地址。
> - Mac 用户：重定向到 `.zip` 下载地址。
> - 其他用户：重定向到 GitHub Release 页面。
>
> # [English]
>
> ### Purpose:
>
> - This endpoint detects the client operating system and redirects to the corresponding GitHub Release direct link, allowing users to start downloading the latest version file immediately.
>
> ### Parameter Description:
>
> - No parameters.
>
> ### Return Result:
>
> - Windows users: Redirect to `.exe` download URL.
> - Mac users: Redirect to `.zip` download URL.
> - Other users: Redirect to the GitHub Release page.

#### Parameters

None

#### Request Body

None

#### Success Response

No declared success response

<a id="get-api-u1-v1-tikhub-downloader-version"></a>
### `GET /api/u1/v1/tikhub/downloader/version`

- Summary: 检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `update_check_api_v1_tikhub_downloader_version_get`

#### Notes

> # [中文]
>
> ### 用途说明:
>
> - 检查TikHub下载器的版本更新。
>
> ### 参数说明:
>
> - 无参数。
>
> ### 返回结果:
>
> - `latest_version`: 最新版本号。
> - `update_date`: 更新日期。
> - `download_url`: 下载链接。
> - `upload_note`: 更新说明。
>
> # [English]
>
> ### Purpose:
>
> - Check for TikHub Downloader version updates.
>
> ### Parameter Description:
>
> - No parameters.
>
> ### Return Result:
>
> - `latest_version`: Latest version number.
> - `update_date`: Update date.
> - `download_url`: Download link.
> - `upload_note`: Update note.

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `latest_version`:string, `update_date`:string, `download_url`:string, `latest_download_url_win`:string, `latest_download_url_mac`:string, `upload_note`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| latest_version | string | No | None | 1.0.0 | None | None |
| update_date | string | No | None | 2025-03-17 | None | None |
| download_url | string | No | None | https://github.com/TikHub/TikHub-Multi-Functional-Downloader/releases/tag/V1.0.0 | None | None |
| latest_download_url_win | string | No | None | https://github.com/TikHub/TikHub-Multi-Functional-Downloader/releases/download/… | None | None |
| latest_download_url_mac | string | No | None | https://github.com/TikHub/TikHub-Multi-Functional-Downloader/archive/refs/tags/… | None | None |
| upload_note | string | No | None | Bug fixes and performance improvements | None | None |
