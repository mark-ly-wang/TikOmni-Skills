# Douyin-App-V3-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-app-v3-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`47`
- 常见能力：作品详情 / 搜索 / 主页/账号 / 详情 / 热点/榜单 / 音乐/音频
- 常见入参：`count`, `cursor`, `keyword`, `aweme_id`, `sec_user_id`, `offset`, `sort_type`, `publish_time`, `filter_duration`, `aweme_ids`
- 标签说明：**(抖音-App-V3数据接口（当前最新版本）/Douyin-App-V3-API (Current latest version))**

## 路由列表

### `GET /api/u1/v1/douyin/app/v3/add_video_play_count`

- 能力：作品详情
- 入参：query: `aweme_type*`, `item_id*`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list_detail`

- 能力：搜索 / 热点/榜单 / 详情
- 入参：query: `category_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_general_search_result`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`, `content_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_detail`

- 能力：详情 / 话题
- 入参：query: `ch_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_search_result`

- 能力：搜索 / 话题
- 入参：query: `keyword*`, `offset`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_video_list`

- 能力：作品详情 / 话题
- 入参：query: `ch_id*`, `cursor`, `sort_type`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_hot_search_list`

- 能力：搜索 / 热点/榜单
- 入参：query: `board_type`, `board_sub_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_live_hot_search_list`

- 能力：搜索 / 热点/榜单 / 直播
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_live_search_result`

- 能力：搜索 / 直播
- 入参：query: `keyword*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get`

### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video`

- 能力：作品详情
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post`

### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url`

- 能力：作品详情
- 入参：无
- 请求体：application/json: `aweme_ids`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post`

### `GET /api/u1/v1/douyin/app/v3/fetch_multi_video_statistics`

- 能力：作品详情
- 入参：query: `aweme_ids*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get`

### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_v2`

- 能力：作品详情
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post`

### `GET /api/u1/v1/douyin/app/v3/fetch_music_detail`

- 能力：详情 / 音乐/音频
- 入参：query: `music_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_music_hot_search_list`

- 能力：搜索 / 热点/榜单 / 音乐/音频
- 入参：query: `chart_type`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_music_search_result`

- 能力：搜索 / 音乐/音频
- 入参：query: `keyword*`, `offset`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_music_video_list`

- 能力：作品详情 / 音乐/音频
- 入参：query: `music_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`

- 能力：作品详情
- 入参：query: `share_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v2`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v3`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_series_detail`

- 能力：详情
- 入参：query: `series_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_series_video_list`

- 能力：作品详情
- 入参：query: `series_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_share_info_by_share_code`

- 能力：通用能力
- 入参：query: `share_code*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_user_fans_list`

- 能力：主页/账号
- 入参：query: `sec_user_id`, `max_time`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_user_following_list`

- 能力：主页/账号
- 入参：query: `sec_user_id`, `max_time`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_user_like_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `sec_user_id*`, `max_cursor`, `counts`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `sec_user_id*`, `max_cursor`, `count`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_user_search_result`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `offset`, `count`, `douyin_user_fans`, `douyin_user_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_user_series_list`

- 能力：主页/账号
- 入参：query: `user_id`, `sec_user_id`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_comment_replies`

- 能力：评论 / 作品详情
- 入参：query: `item_id*`, `comment_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_comments`

- 能力：评论 / 作品详情
- 入参：query: `aweme_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url`

- 能力：作品详情
- 入参：query: `aweme_id`, `share_url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_detail`

- 能力：作品详情 / 详情
- 入参：query: `mix_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_post_list`

- 能力：作品详情
- 入参：query: `mix_id*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `offset`, `count`, `sort_type`, `publish_time`, `filter_duration`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result_v2`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `sort_type`, `publish_time`, `filter_duration`, `page`, `search_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get`

### `GET /api/u1/v1/douyin/app/v3/fetch_video_statistics`

- 能力：作品详情
- 入参：query: `aweme_ids*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get`

### `GET /api/u1/v1/douyin/app/v3/generate_douyin_short_url`

- 能力：通用能力
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get`

### `GET /api/u1/v1/douyin/app/v3/generate_douyin_video_share_qrcode`

- 能力：作品详情
- 入参：query: `object_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get`

### `GET /api/u1/v1/douyin/app/v3/handler_user_profile`

- 能力：主页/账号
- 入参：query: `sec_user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get`

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_keyword_search`

- 能力：搜索
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get`

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_send_private_message`

- 能力：通用能力
- 入参：query: `uid*`, `sec_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get`

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_user_profile`

- 能力：主页/账号
- 入参：query: `uid*`, `sec_uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get`

### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_video_detail`

- 能力：作品详情 / 详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get`

### `GET /api/u1/v1/douyin/app/v3/register_device`

- 能力：通用能力
- 入参：query: `proxy`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`register_device_api_v1_douyin_app_v3_register_device_get`
