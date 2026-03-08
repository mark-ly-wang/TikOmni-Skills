# Temp-Mail-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/temp-mail-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`3`
- 常见能力：通用能力
- 常见入参：`token`, `message_id`
- 标签说明：**(临时邮箱接口/Temp-Mail-API endpoints)**

## 路由列表

### `GET /api/u1/v1/temp_mail/v1/get_email_by_id`

- 能力：通用能力
- 入参：query: `token*`, `message_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get`

### `GET /api/u1/v1/temp_mail/v1/get_emails_inbox`

- 能力：通用能力
- 入参：query: `token*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_emails_api_v1_temp_mail_v1_get_emails_inbox_get`

### `GET /api/u1/v1/temp_mail/v1/get_temp_email_address`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get`
