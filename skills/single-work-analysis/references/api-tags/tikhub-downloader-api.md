# TikHub-Downloader-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tikhub-downloader-api.md`
- 完整契约：[`api-contracts/tikhub-downloader-api.md`](../api-contracts/tikhub-downloader-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`2`
- 常见能力：下载/媒体
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：无
- 标签说明：**(TikHub下载器接口/TikHub-Downloader-API endpoints)**

## 路由列表

### `GET /api/u1/v1/tikhub/downloader/redirect_download`

- 摘要：重定向到最新版本的下载链接 / Redirect to the latest version download link
- 能力：下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`redirect_download_api_v1_tikhub_downloader_redirect_download_get`
- 完整契约：[`api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-redirect-download`](../api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-redirect-download)

#### 参数

无

#### 请求体

无

#### 成功响应

无成功响应声明

### `GET /api/u1/v1/tikhub/downloader/version`

- 摘要：检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates
- 能力：下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`update_check_api_v1_tikhub_downloader_version_get`
- 完整契约：[`api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-version`](../api-contracts/tikhub-downloader-api.md#get-api-u1-v1-tikhub-downloader-version)

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`latest_version`:string, `update_date`:string, `download_url`:string, `latest_download_url_win`:string, `latest_download_url_mac`:string, `upload_note`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| latest_version | string | 否 | 无 |
| update_date | string | 否 | 无 |
| download_url | string | 否 | 无 |
| latest_download_url_win | string | 否 | 无 |
| latest_download_url_mac | string | 否 | 无 |
| upload_note | string | 否 | 无 |
