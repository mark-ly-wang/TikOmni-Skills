# Xiaohongshu-App-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/xiaohongshu-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`12`
- 常见能力：作品详情 / 主页/账号 / 评论 / 电商 / 搜索 / 通用能力
- 常见入参：`note_id`, `session_id`, `share_link`, `start`, `share_text`, `sort`, `user_id`, `keyword`, `page`, `search_id`
- 标签说明：**(小红书App数据接口/Xiaohongshu-App-API data endpoints)** - 第二优先/Second choice

## 路由列表

### `GET /api/u1/v1/xiaohongshu/app/extract_share_info`

- 能力：通用能力
- 入参：query: `share_link*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`extract_share_info_api_v1_xiaohongshu_app_extract_share_info_get`

### `GET /api/u1/v1/xiaohongshu/app/get_note_comments`

- 能力：评论 / 作品详情
- 入参：query: `note_id*`, `start`, `sort_strategy`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_comments_api_v1_xiaohongshu_app_get_note_comments_get`

### `GET /api/u1/v1/xiaohongshu/app/get_note_info`

- 能力：作品详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_info_v1_api_v1_xiaohongshu_app_get_note_info_get`

### `GET /api/u1/v1/xiaohongshu/app/get_note_info_v2`

- 能力：作品详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_info_v2_api_v1_xiaohongshu_app_get_note_info_v2_get`

### `GET /api/u1/v1/xiaohongshu/app/get_notes_by_topic`

- 能力：作品详情 / 话题
- 入参：query: `page_id*`, `first_load_time*`, `sort`, `session_id`, `last_note_ct`, `last_note_id`, `cursor_score`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_notes_by_topic_api_v1_xiaohongshu_app_get_notes_by_topic_get`

### `GET /api/u1/v1/xiaohongshu/app/get_product_detail`

- 能力：详情 / 电商
- 入参：query: `sku_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_detail_api_v1_xiaohongshu_app_get_product_detail_get`

### `GET /api/u1/v1/xiaohongshu/app/get_sub_comments`

- 能力：评论
- 入参：query: `note_id*`, `comment_id*`, `start`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sub_comments_api_v1_xiaohongshu_app_get_sub_comments_get`

### `GET /api/u1/v1/xiaohongshu/app/get_user_id_and_xsec_token`

- 能力：主页/账号
- 入参：query: `share_link*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_id_and_xsec_token_api_v1_xiaohongshu_app_get_user_id_and_xsec_token_get`

### `GET /api/u1/v1/xiaohongshu/app/get_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_info_api_v1_xiaohongshu_app_get_user_info_get`

### `GET /api/u1/v1/xiaohongshu/app/get_user_notes`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_notes_api_v1_xiaohongshu_app_get_user_notes_get`

### `GET /api/u1/v1/xiaohongshu/app/search_notes`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `page*`, `search_id`, `session_id`, `sort_type`, `filter_note_type`, `filter_note_time`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_notes_api_v1_xiaohongshu_app_search_notes_get`

### `GET /api/u1/v1/xiaohongshu/app/search_products`

- 能力：搜索 / 电商
- 入参：query: `keyword*`, `page*`, `search_id`, `session_id`, `sort`, `scope`, `service_guarantee`, `min_price`, `max_price`, `super_promotion`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_products_api_v1_xiaohongshu_app_search_products_get`
