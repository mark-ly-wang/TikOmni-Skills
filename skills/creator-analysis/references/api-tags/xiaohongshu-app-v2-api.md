# Xiaohongshu-App-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/xiaohongshu-app-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`21`
- 常见能力：作品详情 / 电商 / 搜索 / 详情 / 主页/账号 / 创作者
- 常见入参：`source`, `share_text`, `cursor`, `note_id`, `page`, `keyword`, `search_id`, `sku_id`, `user_id`, `tab`
- 标签说明：**(小红书App V2数据接口/Xiaohongshu-App-V2-API data endpoints)** ⭐ 推荐优先使用/Recommended first choice - 稳定性最高、功能最全/Most stable and feature-rich

## 路由列表

### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed`

- 能力：热点/榜单 / 创作者
- 入参：query: `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_creator_hot_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_hot_inspiration_feed_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_inspiration_feed`

- 能力：创作者
- 入参：query: `cursor`, `tab`, `source`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_creator_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_inspiration_feed_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`

- 能力：作品详情 / 详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_image_note_detail_api_v1_xiaohongshu_app_v2_get_image_note_detail_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`

- 能力：作品详情 / 详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_mixed_note_detail_api_v1_xiaohongshu_app_v2_get_mixed_note_detail_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_comments`

- 能力：评论 / 作品详情
- 入参：query: `note_id`, `share_text`, `cursor`, `index`, `sort_strategy`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_comments_api_v1_xiaohongshu_app_v2_get_note_comments_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_sub_comments`

- 能力：评论 / 作品详情
- 入参：query: `note_id`, `share_text`, `comment_id*`, `cursor`, `index`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_sub_comments_api_v1_xiaohongshu_app_v2_get_note_sub_comments_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_detail`

- 能力：详情 / 电商
- 入参：query: `sku_id*`, `source`, `pre_page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_detail_api_v1_xiaohongshu_app_v2_get_product_detail_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_recommendations`

- 能力：电商
- 入参：query: `sku_id*`, `cursor_score`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_recommendations_api_v1_xiaohongshu_app_v2_get_product_recommendations_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_review_overview`

- 能力：电商
- 入参：query: `sku_id*`, `tab`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_review_overview_api_v1_xiaohongshu_app_v2_get_product_review_overview_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_reviews`

- 能力：电商
- 入参：query: `sku_id*`, `page`, `sort_strategy_type`, `share_pics_only`, `from_page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_reviews_api_v1_xiaohongshu_app_v2_get_product_reviews_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_feed`

- 能力：话题
- 入参：query: `page_id*`, `sort`, `cursor_score`, `last_note_id`, `last_note_ct`, `session_id`, `first_load_time`, `source`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_topic_feed_api_v1_xiaohongshu_app_v2_get_topic_feed_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_info`

- 能力：话题
- 入参：query: `page_id*`, `source`, `note_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_topic_info_api_v1_xiaohongshu_app_v2_get_topic_info_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_faved_notes`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id`, `share_text`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_faved_notes_api_v1_xiaohongshu_app_v2_get_user_faved_notes_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`

- 能力：主页/账号
- 入参：query: `user_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_info_api_v1_xiaohongshu_app_v2_get_user_info_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id`, `share_text`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_posted_notes_api_v1_xiaohongshu_app_v2_get_user_posted_notes_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`

- 能力：作品详情 / 详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_note_detail_api_v1_xiaohongshu_app_v2_get_video_note_detail_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/search_groups`

- 能力：搜索
- 入参：query: `keyword*`, `page_no`, `search_id`, `source`, `is_recommend`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_groups_api_v1_xiaohongshu_app_v2_search_groups_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/search_images`

- 能力：搜索
- 入参：query: `keyword*`, `page`, `search_id`, `search_session_id`, `word_request_id`, `source`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_images_api_v1_xiaohongshu_app_v2_search_images_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/search_notes`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `page`, `sort_type`, `note_type`, `time_filter`, `search_id`, `search_session_id`, `source`, `ai_mode`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_notes_api_v1_xiaohongshu_app_v2_search_notes_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/search_products`

- 能力：搜索 / 电商
- 入参：query: `keyword*`, `page`, `search_id`, `source`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_products_api_v1_xiaohongshu_app_v2_search_products_get`

### `GET /api/u1/v1/xiaohongshu/app_v2/search_users`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `page`, `search_id`, `source`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_users_api_v1_xiaohongshu_app_v2_search_users_get`
