# Xigua-App-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/xigua-app-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`7`
- 常见能力：作品详情 / 主页/账号 / 评论 / 搜索
- 常见入参：`item_id`, `user_id`, `offset`, `max_behot_time`, `count`, `keyword`, `order_type`, `min_duration`, `max_duration`
- 标签说明：**(西瓜视频App V2数据接口/Xigua-App-V2-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/xigua/app/v2/fetch_one_video`

- 能力：作品详情
- 入参：query: `item_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get`

### `GET /api/u1/v1/xigua/app/v2/fetch_one_video_play_url`

- 能力：作品详情
- 入参：query: `item_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get`

### `GET /api/u1/v1/xigua/app/v2/fetch_one_video_v2`

- 能力：作品详情
- 入参：query: `item_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v2_api_v1_xigua_app_v2_fetch_one_video_v2_get`

### `GET /api/u1/v1/xigua/app/v2/fetch_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get`

### `GET /api/u1/v1/xigua/app/v2/fetch_user_post_list`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `max_behot_time`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get`

### `GET /api/u1/v1/xigua/app/v2/fetch_video_comment_list`

- 能力：评论 / 作品详情
- 入参：query: `item_id*`, `offset`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get`

### `GET /api/u1/v1/xigua/app/v2/search_video`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `offset`, `order_type`, `min_duration`, `max_duration`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_video_api_v1_xigua_app_v2_search_video_get`
