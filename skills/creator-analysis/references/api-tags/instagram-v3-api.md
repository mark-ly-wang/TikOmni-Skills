# Instagram-V3-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/instagram-v3-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`26`
- 常见能力：主页/账号 / 作品详情 / 评论 / 搜索 / 通用能力 / 话题
- 常见入参：`user_id`, `username`, `url`, `first`, `after`, `query`, `media_id`, `code`, `max_id`, `comment_id`
- 标签说明：**(Instagram V3数据接口/Instagram-V3-API endpoints)**

## 路由列表

### `GET /api/u1/v1/instagram/v3/bulk_translate_comments`

- 能力：评论
- 入参：query: `comment_ids*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`bulk_translate_comments_api_v1_instagram_v3_bulk_translate_comments_get`

### `GET /api/u1/v1/instagram/v3/general_search`

- 能力：搜索
- 入参：query: `query*`, `next_max_id`, `rank_token`, `enable_metadata`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`general_search_api_v1_instagram_v3_general_search_get`

### `GET /api/u1/v1/instagram/v3/get_comment_replies`

- 能力：评论
- 入参：query: `media_id`, `code`, `url`, `comment_id*`, `min_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_comment_replies_api_v1_instagram_v3_get_comment_replies_get`

### `GET /api/u1/v1/instagram/v3/get_explore`

- 能力：通用能力
- 入参：query: `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_explore_api_v1_instagram_v3_get_explore_get`

### `GET /api/u1/v1/instagram/v3/get_highlight_stories`

- 能力：通用能力
- 入参：query: `highlight_id*`, `reel_ids`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_highlight_stories_api_v1_instagram_v3_get_highlight_stories_get`

### `GET /api/u1/v1/instagram/v3/get_location_info`

- 能力：通用能力
- 入参：query: `location_id*`, `show_nearby`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_location_info_api_v1_instagram_v3_get_location_info_get`

### `GET /api/u1/v1/instagram/v3/get_location_posts`

- 能力：作品详情
- 入参：query: `location_id*`, `tab`, `page_size_override`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_location_posts_api_v1_instagram_v3_get_location_posts_get`

### `GET /api/u1/v1/instagram/v3/get_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `media_id`, `code`, `url`, `min_id`, `sort_order`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_post_comments_api_v1_instagram_v3_get_post_comments_get`

### `GET /api/u1/v1/instagram/v3/get_post_info`

- 能力：作品详情
- 入参：query: `media_id`, `url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_post_info_api_v1_instagram_v3_get_post_info_get`

### `GET /api/u1/v1/instagram/v3/get_post_info_by_code`

- 能力：作品详情
- 入参：query: `code`, `url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_post_info_by_code_api_v1_instagram_v3_get_post_info_by_code_get`

### `GET /api/u1/v1/instagram/v3/get_post_oembed`

- 能力：作品详情
- 入参：query: `url*`, `hidecaption`, `maxwidth`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_post_oembed_api_v1_instagram_v3_get_post_oembed_get`

### `GET /api/u1/v1/instagram/v3/get_recommended_reels`

- 能力：通用能力
- 入参：query: `first`, `after`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_recommended_reels_api_v1_instagram_v3_get_recommended_reels_get`

### `GET /api/u1/v1/instagram/v3/get_user_about`

- 能力：主页/账号
- 入参：query: `user_id`, `username`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_about_api_v1_instagram_v3_get_user_about_get`

### `GET /api/u1/v1/instagram/v3/get_user_brief`

- 能力：主页/账号
- 入参：query: `user_id*`, `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_brief_api_v1_instagram_v3_get_user_brief_get`

### `GET /api/u1/v1/instagram/v3/get_user_followers`

- 能力：主页/账号
- 入参：query: `user_id`, `username`, `count`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_followers_api_v1_instagram_v3_get_user_followers_get`

### `GET /api/u1/v1/instagram/v3/get_user_following`

- 能力：主页/账号
- 入参：query: `user_id`, `username`, `count`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_following_api_v1_instagram_v3_get_user_following_get`

### `GET /api/u1/v1/instagram/v3/get_user_highlights`

- 能力：主页/账号
- 入参：query: `user_id`, `username`, `first`, `after`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_highlights_api_v1_instagram_v3_get_user_highlights_get`

### `GET /api/u1/v1/instagram/v3/get_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `username`, `user_id`, `first`, `after`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_posts_api_v1_instagram_v3_get_user_posts_get`

### `GET /api/u1/v1/instagram/v3/get_user_profile`

- 能力：主页/账号
- 入参：query: `user_id`, `username`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_profile_api_v1_instagram_v3_get_user_profile_get`

### `GET /api/u1/v1/instagram/v3/get_user_reels`

- 能力：主页/账号
- 入参：query: `user_id`, `username`, `first`, `after`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_reels_api_v1_instagram_v3_get_user_reels_get`

### `GET /api/u1/v1/instagram/v3/get_user_stories`

- 能力：主页/账号
- 入参：query: `user_id`, `username`, `reel_ids`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_stories_api_v1_instagram_v3_get_user_stories_get`

### `GET /api/u1/v1/instagram/v3/get_user_tagged_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id`, `username`, `first`, `after`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_tagged_posts_api_v1_instagram_v3_get_user_tagged_posts_get`

### `GET /api/u1/v1/instagram/v3/search_hashtags`

- 能力：搜索 / 话题
- 入参：query: `query*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_hashtags_api_v1_instagram_v3_search_hashtags_get`

### `GET /api/u1/v1/instagram/v3/search_places`

- 能力：搜索
- 入参：query: `query*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_places_api_v1_instagram_v3_search_places_get`

### `GET /api/u1/v1/instagram/v3/search_users`

- 能力：搜索 / 主页/账号
- 入参：query: `query*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_users_api_v1_instagram_v3_search_users_get`

### `GET /api/u1/v1/instagram/v3/translate_comment`

- 能力：评论
- 入参：query: `comment_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`translate_comment_api_v1_instagram_v3_translate_comment_get`
