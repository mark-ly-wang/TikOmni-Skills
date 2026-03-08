# Threads-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/threads-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`11`
- 常见能力：主页/账号 / 作品详情 / 搜索 / 详情 / 评论
- 常见入参：`end_cursor`, `user_id`, `post_id`, `query`, `url`, `username`
- 标签说明：**(Threads Web数据接口/Threads-Web-API endpoints)**

## 路由列表

### `GET /api/u1/v1/threads/web/fetch_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `post_id*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comments_api_v1_threads_web_fetch_post_comments_get`

### `GET /api/u1/v1/threads/web/fetch_post_detail`

- 能力：作品详情 / 详情
- 入参：query: `post_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_api_v1_threads_web_fetch_post_detail_get`

### `GET /api/u1/v1/threads/web/fetch_post_detail_v2`

- 能力：作品详情 / 详情
- 入参：query: `post_id`, `url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_v2_api_v1_threads_web_fetch_post_detail_v2_get`

### `GET /api/u1/v1/threads/web/fetch_user_info`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_threads_web_fetch_user_info_get`

### `GET /api/u1/v1/threads/web/fetch_user_info_by_id`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_by_id_api_v1_threads_web_fetch_user_info_by_id_get`

### `GET /api/u1/v1/threads/web/fetch_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_posts_api_v1_threads_web_fetch_user_posts_get`

### `GET /api/u1/v1/threads/web/fetch_user_replies`

- 能力：主页/账号
- 入参：query: `user_id*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_replies_api_v1_threads_web_fetch_user_replies_get`

### `GET /api/u1/v1/threads/web/fetch_user_reposts`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_reposts_api_v1_threads_web_fetch_user_reposts_get`

### `GET /api/u1/v1/threads/web/search_profiles`

- 能力：搜索 / 主页/账号
- 入参：query: `query*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_profiles_api_v1_threads_web_search_profiles_get`

### `GET /api/u1/v1/threads/web/search_recent`

- 能力：搜索
- 入参：query: `query*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_recent_api_v1_threads_web_search_recent_get`

### `GET /api/u1/v1/threads/web/search_top`

- 能力：搜索
- 入参：query: `query*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_top_api_v1_threads_web_search_top_get`
