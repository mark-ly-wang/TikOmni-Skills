# Douyin-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`76`
- 常见能力：主页/账号 / 作品详情 / 通用能力 / 直播 / 搜索 / 电商
- 常见入参：`count`, `cookie`, `refresh_index`, `keyword`, `sec_user_id`, `cursor`, `room_id`, `offset`, `aweme_id`, `max_cursor`
- 标签说明：**(抖音Web数据接口/Douyin-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/web/douyin_live_room`

- 能力：直播
- 入参：query: `live_room_url*`, `danmaku_type*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`douyin_live_room_api_v1_douyin_web_douyin_live_room_get`

### `GET /api/u1/v1/douyin/web/encrypt_uid_to_sec_user_id`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get`

### `GET /api/u1/v1/douyin/web/fetch_batch_user_profile_v1`

- 能力：主页/账号
- 入参：query: `sec_user_ids*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get`

### `GET /api/u1/v1/douyin/web/fetch_batch_user_profile_v2`

- 能力：主页/账号
- 入参：query: `sec_user_ids*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get`

### `GET /api/u1/v1/douyin/web/fetch_cartoon_aweme`

- 能力：通用能力
- 入参：query: `count*`, `refresh_index`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get`

### `POST /api/u1/v1/douyin/web/fetch_challenge_posts`

- 能力：作品详情 / 话题
- 入参：无
- 请求体：application/json: `challenge_id`:string, `sort_type`:integer, `cursor`:integer, `count`:integer, `cookie`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post`

### `GET /api/u1/v1/douyin/web/fetch_douyin_web_guest_cookie`

- 能力：通用能力
- 入参：query: `user_agent*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get`

### `GET /api/u1/v1/douyin/web/fetch_food_aweme`

- 能力：通用能力
- 入参：query: `count*`, `refresh_index`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get`

### `GET /api/u1/v1/douyin/web/fetch_game_aweme`

- 能力：通用能力
- 入参：query: `count*`, `refresh_index`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get`

### `GET /api/u1/v1/douyin/web/fetch_general_search_result`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`, `search_range`, `content_type`, `search_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get`

### `GET /api/u1/v1/douyin/web/fetch_home_feed`

- 能力：主页/账号
- 入参：query: `count`, `refresh_index`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get`

### `GET /api/u1/v1/douyin/web/fetch_hot_search_result`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get`

### `GET /api/u1/v1/douyin/web/fetch_knowledge_aweme`

- 能力：通用能力
- 入参：query: `count*`, `refresh_index`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get`

### `GET /api/u1/v1/douyin/web/fetch_live_gift_ranking`

- 能力：直播
- 入参：query: `room_id*`, `rank_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get`

### `GET /api/u1/v1/douyin/web/fetch_live_im_fetch`

- 能力：直播
- 入参：query: `room_id*`, `user_unique_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get`

### `GET /api/u1/v1/douyin/web/fetch_live_room_product_result`

- 能力：电商 / 直播
- 入参：query: `room_id*`, `author_id*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get`

### `GET /api/u1/v1/douyin/web/fetch_live_search_result`

- 能力：搜索 / 直播
- 入参：query: `keyword*`, `offset`, `count`, `search_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get`

### `POST /api/u1/v1/douyin/web/fetch_multi_video`

- 能力：作品详情
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post`

### `POST /api/u1/v1/douyin/web/fetch_multi_video_high_quality_play_url`

- 能力：作品详情
- 入参：无
- 请求体：application/json: `aweme_ids`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post`

### `GET /api/u1/v1/douyin/web/fetch_music_aweme`

- 能力：音乐/音频
- 入参：query: `count*`, `refresh_index`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get`

### `GET /api/u1/v1/douyin/web/fetch_one_video`

- 能力：作品详情
- 入参：query: `aweme_id*`, `need_anchor_info`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_douyin_web_fetch_one_video_get`

### `GET /api/u1/v1/douyin/web/fetch_one_video_by_share_url`

- 能力：作品详情
- 入参：query: `share_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get`

### `GET /api/u1/v1/douyin/web/fetch_one_video_danmaku`

- 能力：作品详情
- 入参：query: `item_id*`, `duration*`, `end_time*`, `start_time*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get`

### `GET /api/u1/v1/douyin/web/fetch_one_video_v2`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get`

### `GET /api/u1/v1/douyin/web/fetch_product_coupon`

- 能力：电商
- 入参：query: `product_id*`, `shop_id*`, `price*`, `author_id*`, `sec_user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get`

### `GET /api/u1/v1/douyin/web/fetch_product_detail`

- 能力：详情 / 电商
- 入参：query: `product_id*`, `aweme_id`, `room_id`, `sec_user_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get`

### `GET /api/u1/v1/douyin/web/fetch_product_review_list`

- 能力：电商
- 入参：query: `product_id*`, `shop_id*`, `cursor`, `count`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get`

### `GET /api/u1/v1/douyin/web/fetch_product_review_score`

- 能力：电商
- 入参：query: `product_id*`, `shop_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get`

### `GET /api/u1/v1/douyin/web/fetch_product_sku_list`

- 能力：电商
- 入参：query: `product_id*`, `author_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get`

### `POST /api/u1/v1/douyin/web/fetch_query_user`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_query_user_api_v1_douyin_web_fetch_query_user_post`

### `GET /api/u1/v1/douyin/web/fetch_related_posts`

- 能力：作品详情
- 入参：query: `aweme_id*`, `refresh_index`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get`

### `POST /api/u1/v1/douyin/web/fetch_search_challenge`

- 能力：搜索 / 话题
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `count`:integer, `cookie`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post`

### `GET /api/u1/v1/douyin/web/fetch_series_aweme`

- 能力：通用能力
- 入参：query: `offset*`, `count*`, `content_type*`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get`

### `POST /api/u1/v1/douyin/web/fetch_user_collection_videos`

- 能力：主页/账号 / 作品详情
- 入参：无
- 请求体：application/json: `cookie*`:string, `max_cursor`:integer, `counts`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post`

### `POST /api/u1/v1/douyin/web/fetch_user_collects`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: `max_cursor`:integer, `counts`:integer, `cookie*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post`

### `GET /api/u1/v1/douyin/web/fetch_user_collects_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `collects_id*`, `max_cursor`, `counts`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get`

### `GET /api/u1/v1/douyin/web/fetch_user_fans_list`

- 能力：主页/账号
- 入参：query: `sec_user_id`, `max_time`, `count`, `source_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get`

### `GET /api/u1/v1/douyin/web/fetch_user_following_list`

- 能力：主页/账号
- 入参：query: `sec_user_id`, `max_time`, `count`, `source_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get`

### `POST /api/u1/v1/douyin/web/fetch_user_like_videos`

- 能力：主页/账号 / 作品详情
- 入参：无
- 请求体：application/json: `sec_user_id*`:string, `max_cursor`:integer, `counts`:integer, `cookie`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post`

### `GET /api/u1/v1/douyin/web/fetch_user_live_info_by_uid`

- 能力：主页/账号 / 直播
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get`

### `GET /api/u1/v1/douyin/web/fetch_user_live_videos`

- 能力：主页/账号 / 作品详情 / 直播
- 入参：query: `webcast_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get`

### `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id`

- 能力：主页/账号 / 作品详情 / 直播
- 入参：query: `room_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get`

### `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id_v2`

- 能力：主页/账号 / 作品详情 / 直播
- 入参：query: `room_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get`

### `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_sec_uid`

- 能力：主页/账号 / 作品详情 / 直播
- 入参：query: `sec_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get`

### `GET /api/u1/v1/douyin/web/fetch_user_mix_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `mix_id*`, `max_cursor`, `counts`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get`

### `GET /api/u1/v1/douyin/web/fetch_user_post_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `sec_user_id*`, `max_cursor`, `count`, `filter_type`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get`

### `GET /api/u1/v1/douyin/web/fetch_user_profile_by_short_id`

- 能力：主页/账号
- 入参：query: `short_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get`

### `GET /api/u1/v1/douyin/web/fetch_user_profile_by_uid`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get`

### `GET /api/u1/v1/douyin/web/fetch_user_search_result`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `offset`, `count`, `douyin_user_fans`, `douyin_user_type`, `search_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get`

### `GET /api/u1/v1/douyin/web/fetch_user_search_result_v2`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get`

### `GET /api/u1/v1/douyin/web/fetch_user_search_result_v3`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `cursor`, `douyin_user_type`, `douyin_user_fans`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get`

### `GET /api/u1/v1/douyin/web/fetch_video_channel_result`

- 能力：主页/账号 / 作品详情
- 入参：query: `tag_id*`, `count`, `refresh_index`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get`

### `GET /api/u1/v1/douyin/web/fetch_video_comment_replies`

- 能力：评论 / 作品详情
- 入参：query: `item_id*`, `comment_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get`

### `GET /api/u1/v1/douyin/web/fetch_video_comments`

- 能力：评论 / 作品详情
- 入参：query: `aweme_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get`

### `GET /api/u1/v1/douyin/web/fetch_video_high_quality_play_url`

- 能力：作品详情
- 入参：query: `aweme_id`, `share_url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get`

### `GET /api/u1/v1/douyin/web/fetch_video_search_result`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`, `search_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get`

### `GET /api/u1/v1/douyin/web/fetch_video_search_result_v2`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `sort_type`, `publish_time`, `filter_duration`, `page`, `search_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get`

### `POST /api/u1/v1/douyin/web/generate_a_bogus`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `url*`:string, `data*`:string, `user_agent*`:string, `index_0`:integer, `index_1`:integer, `index_2`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post`

### `GET /api/u1/v1/douyin/web/generate_real_msToken`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_real_msToken_api_v1_douyin_web_generate_real_msToken_get`

### `GET /api/u1/v1/douyin/web/generate_s_v_web_id`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_s_v_web_id_api_v1_douyin_web_generate_s_v_web_id_get`

### `GET /api/u1/v1/douyin/web/generate_ttwid`

- 能力：通用能力
- 入参：query: `user_agent`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_ttwid_api_v1_douyin_web_generate_ttwid_get`

### `GET /api/u1/v1/douyin/web/generate_verify_fp`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get`

### `GET /api/u1/v1/douyin/web/generate_wss_xb_signature`

- 能力：通用能力
- 入参：query: `user_agent*`, `room_id*`, `user_unique_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get`

### `POST /api/u1/v1/douyin/web/generate_x_bogus`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `url*`:string, `user_agent*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post`

### `POST /api/u1/v1/douyin/web/get_all_aweme_id`

- 能力：通用能力
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post`

### `POST /api/u1/v1/douyin/web/get_all_sec_user_id`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post`

### `POST /api/u1/v1/douyin/web/get_all_webcast_id`

- 能力：通用能力
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post`

### `GET /api/u1/v1/douyin/web/get_aweme_id`

- 能力：通用能力
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_aweme_id_api_v1_douyin_web_get_aweme_id_get`

### `GET /api/u1/v1/douyin/web/get_sec_user_id`

- 能力：主页/账号
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get`

### `GET /api/u1/v1/douyin/web/get_webcast_id`

- 能力：通用能力
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_webcast_id_api_v1_douyin_web_get_webcast_id_get`

### `GET /api/u1/v1/douyin/web/handler_shorten_url`

- 能力：通用能力
- 入参：query: `target_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get`

### `GET /api/u1/v1/douyin/web/handler_user_profile`

- 能力：主页/账号
- 入参：query: `sec_user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_user_profile_api_v1_douyin_web_handler_user_profile_get`

### `GET /api/u1/v1/douyin/web/handler_user_profile_v2`

- 能力：主页/账号
- 入参：query: `unique_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get`

### `GET /api/u1/v1/douyin/web/handler_user_profile_v3`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get`

### `GET /api/u1/v1/douyin/web/handler_user_profile_v4`

- 能力：主页/账号
- 入参：query: `sec_user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get`

### `GET /api/u1/v1/douyin/web/webcast_id_2_room_id`

- 能力：通用能力
- 入参：query: `webcast_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`webcast_id_2_room_id_api_v1_douyin_web_webcast_id_2_room_id_get`
