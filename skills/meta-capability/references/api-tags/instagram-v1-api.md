# Instagram-V1-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/instagram-v1-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`29`
- 常见能力：主页/账号 / 作品详情 / 通用能力 / 评论 / 下载/媒体 / 话题
- 常见入参：`user_id`, `max_id`, `count`, `end_cursor`, `media_id`, `username`, `page`, `min_id`, `location_id`, `post_url`
- 标签说明：**(Instagram V1数据接口（优先使用V1接口，V2接口仅在V1接口无法满足需求时使用）/Instagram-V1-API endpoints (Prefer using V1 endpoints, V2 endpoints are only for use when V1 endpoints cannot meet the requirements))**

## 路由列表

### `GET /api/u1/v1/instagram/v1/fetch_cities`

- 能力：通用能力
- 入参：query: `country_code*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_cities_api_v1_instagram_v1_fetch_cities_get`

### `GET /api/u1/v1/instagram/v1/fetch_comment_replies`

- 能力：评论
- 入参：query: `media_id*`, `comment_id*`, `min_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_comment_replies_api_v1_instagram_v1_fetch_comment_replies_get`

### `GET /api/u1/v1/instagram/v1/fetch_explore_sections`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_explore_sections_api_v1_instagram_v1_fetch_explore_sections_get`

### `GET /api/u1/v1/instagram/v1/fetch_hashtag_posts`

- 能力：作品详情 / 话题
- 入参：query: `hashtag*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_posts_api_v1_instagram_v1_fetch_hashtag_posts_get`

### `GET /api/u1/v1/instagram/v1/fetch_location_info`

- 能力：通用能力
- 入参：query: `location_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_location_info_api_v1_instagram_v1_fetch_location_info_get`

### `GET /api/u1/v1/instagram/v1/fetch_location_posts`

- 能力：作品详情
- 入参：query: `location_id*`, `tab`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_location_posts_api_v1_instagram_v1_fetch_location_posts_get`

### `GET /api/u1/v1/instagram/v1/fetch_locations`

- 能力：通用能力
- 入参：query: `city_id*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_locations_api_v1_instagram_v1_fetch_locations_get`

### `GET /api/u1/v1/instagram/v1/fetch_music_posts`

- 能力：作品详情 / 音乐/音频
- 入参：query: `music_id`, `music_url`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_posts_api_v1_instagram_v1_fetch_music_posts_get`

### `GET /api/u1/v1/instagram/v1/fetch_post_by_id`

- 能力：作品详情
- 入参：query: `post_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_by_id_api_v1_instagram_v1_fetch_post_by_id_get`

### `GET /api/u1/v1/instagram/v1/fetch_post_by_url`

- 能力：作品详情
- 入参：query: `post_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_by_url_api_v1_instagram_v1_fetch_post_by_url_get`

### `GET /api/u1/v1/instagram/v1/fetch_post_by_url_v2`

- 能力：作品详情
- 入参：query: `post_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_by_url_v2_api_v1_instagram_v1_fetch_post_by_url_v2_get`

### `GET /api/u1/v1/instagram/v1/fetch_post_comments_v2`

- 能力：评论 / 作品详情
- 入参：query: `media_id*`, `sort_order`, `min_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comments_v2_api_v1_instagram_v1_fetch_post_comments_v2_get`

### `GET /api/u1/v1/instagram/v1/fetch_related_profiles`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_related_profiles_api_v1_instagram_v1_fetch_related_profiles_get`

### `GET /api/u1/v1/instagram/v1/fetch_search`

- 能力：搜索
- 入参：query: `query*`, `select`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_api_v1_instagram_v1_fetch_search_get`

### `GET /api/u1/v1/instagram/v1/fetch_section_posts`

- 能力：作品详情
- 入参：query: `section_id*`, `count`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_section_posts_api_v1_instagram_v1_fetch_section_posts_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_about_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_about_info_api_v1_instagram_v1_fetch_user_about_info_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_by_id_api_v1_instagram_v1_fetch_user_info_by_id_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_id_v2`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_by_id_v2_api_v1_instagram_v1_fetch_user_info_by_id_v2_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_by_username_api_v1_instagram_v1_fetch_user_info_by_username_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v2`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_by_username_v2_api_v1_instagram_v1_fetch_user_info_by_username_v2_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_info_by_username_v3`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_by_username_v3_api_v1_instagram_v1_fetch_user_info_by_username_v3_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `count`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_posts_api_v1_instagram_v1_fetch_user_posts_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_posts_v2`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `count`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_posts_v2_api_v1_instagram_v1_fetch_user_posts_v2_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_reels`

- 能力：主页/账号
- 入参：query: `user_id*`, `count`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_reels_api_v1_instagram_v1_fetch_user_reels_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_reposts`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_reposts_api_v1_instagram_v1_fetch_user_reposts_get`

### `GET /api/u1/v1/instagram/v1/fetch_user_tagged_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `count`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_tagged_posts_api_v1_instagram_v1_fetch_user_tagged_posts_get`

### `GET /api/u1/v1/instagram/v1/media_id_to_shortcode`

- 能力：下载/媒体
- 入参：query: `media_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`media_id_to_shortcode_api_v1_instagram_v1_media_id_to_shortcode_get`

### `GET /api/u1/v1/instagram/v1/shortcode_to_media_id`

- 能力：下载/媒体
- 入参：query: `shortcode*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`shortcode_to_media_id_api_v1_instagram_v1_shortcode_to_media_id_get`

### `GET /api/u1/v1/instagram/v1/user_id_to_username`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`user_id_to_username_api_v1_instagram_v1_user_id_to_username_get`
