# TikHub-Downloader-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tikhub-downloader-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`2`
- 常见能力：下载/媒体
- 常见入参：无
- 标签说明：**(TikHub下载器接口/TikHub-Downloader-API endpoints)**

## 路由列表

### `GET /api/u1/v1/tikhub/downloader/redirect_download`

- 能力：下载/媒体
- 入参：无
- 请求体：无
- 成功响应：无成功响应声明
- operationId：`redirect_download_api_v1_tikhub_downloader_redirect_download_get`

### `GET /api/u1/v1/tikhub/downloader/version`

- 能力：下载/媒体
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `latest_version`:string, `update_date`:string, `download_url`:string, `latest_download_url_win`:string, `latest_download_url_mac`:string, `upload_note`:string
- operationId：`update_check_api_v1_tikhub_downloader_version_get`
