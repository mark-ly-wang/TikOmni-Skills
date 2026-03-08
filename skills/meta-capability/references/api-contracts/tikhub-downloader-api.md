# TikHub-Downloader-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/tikhub-downloader-api.md`](../api-tags/tikhub-downloader-api.md)
- 当前契约文件：`api-contracts/tikhub-downloader-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`2`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(TikHub下载器接口/TikHub-Downloader-API endpoints)**

## 路由契约

<a id="get-api-u1-v1-tikhub-downloader-redirect-download"></a>
### `GET /api/u1/v1/tikhub/downloader/redirect_download`

- 摘要：重定向到最新版本的下载链接 / Redirect to the latest version download link
- 能力：下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`redirect_download_api_v1_tikhub_downloader_redirect_download_get`

#### 说明

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

#### 参数

无

#### 请求体

无

#### 成功响应

无成功响应声明

<a id="get-api-u1-v1-tikhub-downloader-version"></a>
### `GET /api/u1/v1/tikhub/downloader/version`

- 摘要：检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates
- 能力：下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`update_check_api_v1_tikhub_downloader_version_get`

#### 说明

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

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`latest_version`:string, `update_date`:string, `download_url`:string, `latest_download_url_win`:string, `latest_download_url_mac`:string, `upload_note`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| latest_version | string | 否 | 无 | 1.0.0 | 无 | 无 |
| update_date | string | 否 | 无 | 2025-03-17 | 无 | 无 |
| download_url | string | 否 | 无 | https://github.com/TikHub/TikHub-Multi-Functional-Downloader/releases/tag/V1.0.0 | 无 | 无 |
| latest_download_url_win | string | 否 | 无 | https://github.com/TikHub/TikHub-Multi-Functional-Downloader/releases/download/… | 无 | 无 |
| latest_download_url_mac | string | 否 | 无 | https://github.com/TikHub/TikHub-Multi-Functional-Downloader/archive/refs/tags/… | 无 | 无 |
| upload_note | string | 否 | 无 | Bug fixes and performance improvements | 无 | 无 |
