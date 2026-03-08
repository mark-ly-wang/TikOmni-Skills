# TikHub-User-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tikhub-user-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`6`
- 常见能力：主页/账号
- 常见入参：`endpoint`, `request_per_day`
- 标签说明：**(TikHub用户数据接口/TikHub-User-API endpoints)**

## 路由列表

### `GET /api/u1/v1/tikhub/user/calculate_price`

- 能力：主页/账号
- 入参：query: `endpoint*`, `request_per_day`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`calculate_price_api_v1_tikhub_user_calculate_price_get`

### `GET /api/u1/v1/tikhub/user/get_all_endpoints_info`

- 能力：主页/账号
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get`

### `GET /api/u1/v1/tikhub/user/get_endpoint_info`

- 能力：主页/账号
- 入参：query: `endpoint*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get`

### `GET /api/u1/v1/tikhub/user/get_tiered_discount_info`

- 能力：主页/账号
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get`

### `GET /api/u1/v1/tikhub/user/get_user_daily_usage`

- 能力：主页/账号
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get`

### `GET /api/u1/v1/tikhub/user/get_user_info`

- 能力：主页/账号
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `router`:string, `api_key_data*`{`api_key_name*`:string, `api_key_scopes*`[], `created_at*`:string, `expires_at*`:string, `api_key_status*`:integer}, `user_data*`{`email*`:string, `balance*`:number, `free_credit*`:number, `email_verified*`:boolean, `account_disabled*`:boolean, `is_active*`:boolean}
- operationId：`get_user_info_api_v1_tikhub_user_get_user_info_get`
