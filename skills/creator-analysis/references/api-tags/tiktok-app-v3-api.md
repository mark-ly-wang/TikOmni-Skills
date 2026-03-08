# TikTok-App-V3-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-app-v3-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`75`
- 常见能力：作品详情 / 电商 / 主页/账号 / 搜索 / 直播 / 详情
- 常见入参：`count`, `offset`, `keyword`, `sort_type`, `cursor`, `region`, `sec_user_id`, `user_id`, `room_id`, `seller_id`
- 标签说明：**(TikTok-App-V3-API数据接口（当前最新版本）/TikTok-App-V3-API (Current latest version))**

## 路由列表

### `POST /api/u1/v1/tiktok/app/v3/TTencrypt_algorithm`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `url`:string, `data`:string, `device_info`{...}
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`TTencrypt_algorithm_api_v1_tiktok_app_v3_TTencrypt_algorithm_post`

### `GET /api/u1/v1/tiktok/app/v3/add_video_play_count`

- 能力：作品详情
- 入参：query: `aweme_type*`, `item_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get`

### `GET /api/u1/v1/tiktok/app/v3/check_live_room_online`

- 能力：直播
- 入参：query: `room_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get`

### `POST /api/u1/v1/tiktok/app/v3/check_live_room_online_batch`

- 能力：直播
- 入参：无
- 请求体：application/json: `room_ids`[string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post`

### `POST /api/u1/v1/tiktok/app/v3/encrypt_decrypt_login_request`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `username`:string, `password`:string, `mode`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post`

### `POST /api/u1/v1/tiktok/app/v3/fetch_content_translate`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `trg_lang`:string, `src_content`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post`

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_info`

- 能力：创作者
- 入参：query: `creator_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights`

- 能力：搜索 / 创作者 / 数据分析
- 入参：query: `offset`, `limit`, `tab`, `language_filters`, `category_filters`, `creator_source`, `force_refresh`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_detail`

- 能力：搜索 / 创作者 / 详情 / 数据分析
- 入参：query: `query_id_str*`, `time_range`, `start_date`, `end_date`, `dimension_list`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_trend`

- 能力：搜索 / 热点/榜单 / 创作者 / 数据分析
- 入参：query: `query_id_str*`, `from_tab_path`, `query_analysis_required`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_videos`

- 能力：搜索 / 创作者 / 作品详情 / 数据分析
- 入参：query: `keyword*`, `offset`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_showcase_product_list`

- 能力：创作者 / 电商
- 入参：query: `kol_id*`, `count`, `next_scroll_param`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_general_search_result`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_detail`

- 能力：详情 / 话题
- 入参：query: `ch_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_search_result`

- 能力：搜索 / 话题
- 入参：query: `keyword*`, `offset`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_video_list`

- 能力：作品详情 / 话题
- 入参：query: `ch_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get`

### `POST /api/u1/v1/tiktok/app/v3/fetch_home_feed`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: `cookie`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post`

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_daily_rank`

- 能力：直播
- 入参：query: `anchor_id`, `room_id`, `rank_type`, `region_type`, `gap_interval`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_ranking_list`

- 能力：直播
- 入参：query: `room_id*`, `anchor_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_info`

- 能力：直播
- 入参：query: `room_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list`

- 能力：电商 / 直播
- 入参：query: `room_id*`, `author_id*`, `page_size`, `offset`, `region`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list_v2`

- 能力：电商 / 直播
- 入参：query: `room_id*`, `author_id*`, `page_size`, `offset`, `region`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_live_search_result`

- 能力：搜索 / 直播
- 入参：query: `keyword*`, `offset`, `count`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_location_search`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get`

### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video`

- 能力：作品详情
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post`

### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video_v2`

- 能力：作品详情
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post`

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_chart_list`

- 能力：音乐/音频
- 入参：query: `scene`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_detail`

- 能力：详情 / 音乐/音频
- 入参：query: `music_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_search_result`

- 能力：搜索 / 音乐/音频
- 入参：query: `keyword*`, `offset`, `count`, `filter_by`, `sort_type`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_music_video_list`

- 能力：作品详情 / 音乐/音频
- 入参：query: `music_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url`

- 能力：作品详情
- 入参：query: `share_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2`

- 能力：作品详情
- 入参：query: `share_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v2`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v3`

- 能力：作品详情
- 入参：query: `aweme_id*`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail`

- 能力：详情 / 电商
- 入参：query: `product_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v2`

- 能力：详情 / 电商
- 入参：query: `product_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v3`

- 能力：详情 / 电商
- 入参：query: `product_id*`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v4`

- 能力：详情 / 电商
- 入参：query: `product_id*`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_id_by_share_link`

- 能力：电商
- 入参：query: `share_link*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_review`

- 能力：电商
- 入参：query: `product_id*`, `cursor`, `size`, `filter_id`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_product_search`

- 能力：搜索 / 电商
- 入参：query: `keyword*`, `cursor`, `count`, `sort_type`, `customer_review_four_star`, `have_discount`, `min_price`, `max_price`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_share_qr_code`

- 能力：通用能力
- 入参：query: `object_id*`, `schema_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_share_short_link`

- 能力：通用能力
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home`

- 能力：主页/账号 / 电商
- 入参：query: `page_id*`, `seller_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home_page_list`

- 能力：主页/账号 / 电商
- 入参：query: `seller_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_id_by_share_link`

- 能力：电商
- 入参：query: `share_link*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_info`

- 能力：电商
- 入参：query: `shop_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_category`

- 能力：电商
- 入参：query: `seller_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list`

- 能力：电商
- 入参：query: `seller_id*`, `scroll_params`, `page_size`, `sort_field`, `sort_order`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list_v2`

- 能力：电商
- 入参：query: `seller_id*`, `scroll_params`, `page_size`, `sort_field`, `sort_order`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_recommend`

- 能力：电商
- 入参：query: `seller_id*`, `scroll_param`, `page_size`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_similar_user_recommendations`

- 能力：主页/账号
- 入参：query: `sec_uid*`, `page_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_country_by_username`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_follower_list`

- 能力：主页/账号
- 入参：query: `user_id`, `sec_user_id`, `count`, `min_time`, `page_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_following_list`

- 能力：主页/账号
- 入参：query: `user_id`, `sec_user_id`, `count`, `min_time`, `page_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_like_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `sec_user_id*`, `max_cursor`, `counts`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_music_list`

- 能力：主页/账号 / 音乐/音频
- 入参：query: `sec_uid*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `sec_user_id`, `unique_id`, `max_cursor`, `count`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v2`

- 能力：主页/账号 / 作品详情
- 入参：query: `sec_user_id`, `unique_id`, `max_cursor`, `count`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v3`

- 能力：主页/账号 / 作品详情
- 入参：query: `sec_user_id`, `unique_id`, `max_cursor`, `count`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_repost_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `offset`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_user_search_result`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `offset`, `count`, `user_search_follower_count`, `user_search_profile_type`, `user_search_other_pref`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comment_replies`

- 能力：评论 / 作品详情
- 入参：query: `item_id*`, `comment_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comments`

- 能力：评论 / 作品详情
- 入参：query: `aweme_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_video_search_result`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get`

### `GET /api/u1/v1/tiktok/app/v3/fetch_webcast_user_info`

- 能力：主页/账号
- 入参：query: `user_id`, `sec_user_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get`

### `GET /api/u1/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username`

- 能力：主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get`

### `GET /api/u1/v1/tiktok/app/v3/handler_user_profile`

- 能力：主页/账号
- 入参：query: `user_id`, `sec_user_id`, `unique_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get`

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search`

- 能力：搜索
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get`

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message`

- 能力：通用能力
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get`

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_user_profile`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get`

### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_video_detail`

- 能力：作品详情 / 详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get`

### `GET /api/u1/v1/tiktok/app/v3/search_follower_list`

- 能力：搜索
- 入参：query: `user_id*`, `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get`

### `GET /api/u1/v1/tiktok/app/v3/search_following_list`

- 能力：搜索
- 入参：query: `user_id*`, `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_following_list_api_v1_tiktok_app_v3_search_following_list_get`
