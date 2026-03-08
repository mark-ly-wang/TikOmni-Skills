# Xiaohongshu-Web-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/xiaohongshu-web-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`18`
- 常见能力：作品详情 / 主页/账号 / 通用能力 / 评论 / 搜索 / 热点/榜单
- 常见入参：`note_id`, `user_id`, `cursor`, `page`, `keywords`, `short_url`, `sort_type`, `note_type`, `comment_id`
- 标签说明：**(小红书Web V2数据接口/Xiaohongshu-Web-V2-API data endpoints)** - 第三优先/Third choice

## 路由列表

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes`

- 能力：作品详情
- 入参：query: `note_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_feed_notes_api_v1_xiaohongshu_web_v2_fetch_feed_notes_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v2`

- 能力：作品详情
- 入参：query: `note_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_feed_notes_v2_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v2_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v3`

- 能力：作品详情
- 入参：query: `short_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_feed_notes_v3_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v3_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v4`

- 能力：作品详情
- 入参：query: `note_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_feed_notes_v4_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v4_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_feed_notes_v5`

- 能力：作品详情
- 入参：query: `note_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_feed_notes_v5_api_v1_xiaohongshu_web_v2_fetch_feed_notes_v5_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_follower_list`

- 能力：通用能力
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_follower_list_api_v1_xiaohongshu_web_v2_fetch_follower_list_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_following_list`

- 能力：通用能力
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_following_list_api_v1_xiaohongshu_web_v2_fetch_following_list_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_notes_api_v1_xiaohongshu_web_v2_fetch_home_notes_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_home_notes_app`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_notes_app_api_v1_xiaohongshu_web_v2_fetch_home_notes_app_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_hot_list`

- 能力：热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_list_api_v1_xiaohongshu_web_v2_fetch_hot_list_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_note_comments`

- 能力：评论 / 作品详情
- 入参：query: `note_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_note_comments_api_v1_xiaohongshu_web_v2_fetch_note_comments_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_note_image`

- 能力：作品详情
- 入参：query: `note_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_note_image_api_v1_xiaohongshu_web_v2_fetch_note_image_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_product_list`

- 能力：电商
- 入参：query: `user_id*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_list_api_v1_xiaohongshu_web_v2_fetch_product_list_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_search_notes`

- 能力：搜索 / 作品详情
- 入参：query: `keywords*`, `page`, `sort_type`, `note_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_notes_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_search_users`

- 能力：搜索 / 主页/账号
- 入参：query: `keywords*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_notes_api_v1_xiaohongshu_web_v2_fetch_search_users_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_sub_comments`

- 能力：评论
- 入参：query: `note_id*`, `comment_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_sub_comments_api_v1_xiaohongshu_web_v2_fetch_sub_comments_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_get`

### `GET /api/u1/v1/xiaohongshu/web_v2/fetch_user_info_app`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_xiaohongshu_web_v2_fetch_user_info_app_get`
