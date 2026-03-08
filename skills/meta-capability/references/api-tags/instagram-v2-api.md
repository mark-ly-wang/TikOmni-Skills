# Instagram-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/instagram-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`27`
- 常见能力：主页/账号 / 作品详情 / 搜索 / 评论 / 话题 / 音乐/音频
- 常见入参：`pagination_token`, `user_id`, `username`, `keyword`, `code_or_url`, `comment_id`, `feed_type`, `highlight_id`, `location_id`, `audio_canonical_id`
- 标签说明：**(Instagram V2数据接口（若V1接口的功能无法满足需求时使用，稳定性不如V1接口）/Instagram-V2-API endpoints (Use when V1 endpoints cannot meet the requirements, stability is not as good as V1 endpoints))**

## 路由列表

### `GET /api/u1/v1/instagram/v2/fetch_comment_replies`

- 能力：评论
- 入参：query: `code_or_url*`, `comment_id*`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get`

### `GET /api/u1/v1/instagram/v2/fetch_hashtag_posts`

- 能力：作品详情 / 话题
- 入参：query: `keyword*`, `feed_type`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get`

### `GET /api/u1/v1/instagram/v2/fetch_highlight_stories`

- 能力：通用能力
- 入参：query: `highlight_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get`

### `GET /api/u1/v1/instagram/v2/fetch_location_posts`

- 能力：作品详情
- 入参：query: `location_id*`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get`

### `GET /api/u1/v1/instagram/v2/fetch_music_posts`

- 能力：作品详情 / 音乐/音频
- 入参：query: `audio_canonical_id*`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get`

### `GET /api/u1/v1/instagram/v2/fetch_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `code_or_url*`, `sort_by`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get`

### `GET /api/u1/v1/instagram/v2/fetch_post_info`

- 能力：作品详情
- 入参：query: `code_or_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_info_api_v1_instagram_v2_fetch_post_info_get`

### `GET /api/u1/v1/instagram/v2/fetch_post_likes`

- 能力：作品详情
- 入参：query: `code_or_url*`, `end_cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get`

### `GET /api/u1/v1/instagram/v2/fetch_similar_users`

- 能力：主页/账号
- 入参：query: `username`, `user_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_followers`

- 能力：主页/账号
- 入参：query: `username`, `user_id`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_following`

- 能力：主页/账号
- 入参：query: `username`, `user_id`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_following_api_v1_instagram_v2_fetch_user_following_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_highlights`

- 能力：主页/账号
- 入参：query: `username`, `user_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_info`

- 能力：主页/账号
- 入参：query: `username`, `user_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_instagram_v2_fetch_user_info_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `username`, `user_id`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_reels`

- 能力：主页/账号
- 入参：query: `username`, `user_id`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_stories`

- 能力：主页/账号
- 入参：query: `username`, `user_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get`

### `GET /api/u1/v1/instagram/v2/fetch_user_tagged_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `username`, `user_id`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get`

### `GET /api/u1/v1/instagram/v2/general_search`

- 能力：搜索
- 入参：query: `keyword*`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`general_search_api_v1_instagram_v2_general_search_get`

### `GET /api/u1/v1/instagram/v2/media_id_to_shortcode`

- 能力：下载/媒体
- 入参：query: `media_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get`

### `GET /api/u1/v1/instagram/v2/search_by_coordinates`

- 能力：搜索
- 入参：query: `latitude*`, `longitude*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get`

### `GET /api/u1/v1/instagram/v2/search_hashtags`

- 能力：搜索 / 话题
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_hashtags_api_v1_instagram_v2_search_hashtags_get`

### `GET /api/u1/v1/instagram/v2/search_locations`

- 能力：搜索
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_locations_api_v1_instagram_v2_search_locations_get`

### `GET /api/u1/v1/instagram/v2/search_music`

- 能力：搜索 / 音乐/音频
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_music_api_v1_instagram_v2_search_music_get`

### `GET /api/u1/v1/instagram/v2/search_reels`

- 能力：搜索
- 入参：query: `keyword*`, `pagination_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_reels_api_v1_instagram_v2_search_reels_get`

### `GET /api/u1/v1/instagram/v2/search_users`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_users_api_v1_instagram_v2_search_users_get`

### `GET /api/u1/v1/instagram/v2/shortcode_to_media_id`

- 能力：下载/媒体
- 入参：query: `shortcode*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get`

### `GET /api/u1/v1/instagram/v2/user_id_to_username`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`user_id_to_username_api_v1_instagram_v2_user_id_to_username_get`
