# TikTok-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`58`
- 常见能力：通用能力 / 主页/账号 / 直播 / 作品详情 / 搜索 / 详情
- 常见入参：`count`, `cursor`, `cookie`, `secUid`, `url`, `keyword`, `search_id`, `user_agent`, `offset`, `coverFormat`
- 标签说明：**(TikTok-Web-API数据接口/TikTok-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/tiktok/web/decrypt_strData`

- 能力：通用能力
- 入参：query: `encrypted_data*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`decrypt_strData_api_v1_tiktok_web_decrypt_strData_get`

### `GET /api/u1/v1/tiktok/web/device_register`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`device_register_api_v1_tiktok_web_device_register_get`

### `GET /api/u1/v1/tiktok/web/encrypt_strData`

- 能力：通用能力
- 入参：query: `data*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`encrypt_strData_api_v1_tiktok_web_encrypt_strData_get`

### `GET /api/u1/v1/tiktok/web/fetch_batch_check_live_alive`

- 能力：直播
- 入参：query: `room_ids*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get`

### `GET /api/u1/v1/tiktok/web/fetch_check_live_alive`

- 能力：直播
- 入参：query: `room_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get`

### `GET /api/u1/v1/tiktok/web/fetch_explore_post`

- 能力：作品详情
- 入参：query: `categoryType`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get`

### `GET /api/u1/v1/tiktok/web/fetch_general_search`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `search_id`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_api_v1_tiktok_web_fetch_general_search_get`

### `POST /api/u1/v1/tiktok/web/fetch_gift_name_by_id`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `gift_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post`

### `POST /api/u1/v1/tiktok/web/fetch_gift_names_by_ids`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `gift_ids*`[string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post`

### `POST /api/u1/v1/tiktok/web/fetch_home_feed`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: `count`:integer, `cookie`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post`

### `GET /api/u1/v1/tiktok/web/fetch_live_gift_list`

- 能力：直播
- 入参：query: `room_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get`

### `GET /api/u1/v1/tiktok/web/fetch_live_im_fetch`

- 能力：直播
- 入参：query: `room_id*`, `user_unique_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get`

### `GET /api/u1/v1/tiktok/web/fetch_live_recommend`

- 能力：直播
- 入参：query: `related_live_tag*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get`

### `GET /api/u1/v1/tiktok/web/fetch_post_comment`

- 能力：评论 / 作品详情
- 入参：query: `aweme_id*`, `cursor`, `count`, `current_region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get`

### `GET /api/u1/v1/tiktok/web/fetch_post_comment_reply`

- 能力：评论 / 评论回复 / 作品详情
- 入参：query: `item_id*`, `comment_id*`, `cursor`, `count`, `current_region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get`

### `GET /api/u1/v1/tiktok/web/fetch_post_detail`

- 能力：作品详情 / 详情
- 入参：query: `itemId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get`

### `GET /api/u1/v1/tiktok/web/fetch_post_detail_v2`

- 能力：作品详情 / 详情
- 入参：query: `itemId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get`

### `GET /api/u1/v1/tiktok/web/fetch_search_keyword_suggest`

- 能力：搜索
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get`

### `GET /api/u1/v1/tiktok/web/fetch_search_live`

- 能力：搜索 / 直播
- 入参：query: `keyword*`, `count`, `offset`, `search_id`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_live_api_v1_tiktok_web_fetch_search_live_get`

### `GET /api/u1/v1/tiktok/web/fetch_search_photo`

- 能力：搜索 / 热点/榜单
- 入参：query: `keyword*`, `count`, `offset`, `search_id`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get`

### `GET /api/u1/v1/tiktok/web/fetch_search_user`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `cursor`, `search_id`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_user_api_v1_tiktok_web_fetch_search_user_get`

### `GET /api/u1/v1/tiktok/web/fetch_search_video`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `count`, `offset`, `search_id`, `cookie`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_video_api_v1_tiktok_web_fetch_search_video_get`

### `GET /api/u1/v1/tiktok/web/fetch_sso_login_auth`

- 能力：通用能力
- 入参：query: `device_id*`, `verifyFp*`, `region*`, `proxy*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get`

### `GET /api/u1/v1/tiktok/web/fetch_sso_login_qrcode`

- 能力：通用能力
- 入参：query: `device_id*`, `region*`, `proxy*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get`

### `GET /api/u1/v1/tiktok/web/fetch_sso_login_status`

- 能力：通用能力
- 入参：query: `token*`, `device_id*`, `verifyFp*`, `region*`, `proxy*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get`

### `GET /api/u1/v1/tiktok/web/fetch_tag_detail`

- 能力：详情
- 入参：query: `tag_name*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get`

### `GET /api/u1/v1/tiktok/web/fetch_tag_post`

- 能力：作品详情
- 入参：query: `challengeID*`, `count`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get`

### `GET /api/u1/v1/tiktok/web/fetch_tiktok_live_data`

- 能力：直播
- 入参：query: `live_room_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get`

### `GET /api/u1/v1/tiktok/web/fetch_tiktok_web_guest_cookie`

- 能力：通用能力
- 入参：query: `user_agent*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get`

### `GET /api/u1/v1/tiktok/web/fetch_trending_post`

- 能力：热点/榜单 / 作品详情
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get`

### `GET /api/u1/v1/tiktok/web/fetch_trending_searchwords`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_collect`

- 能力：主页/账号
- 入参：query: `cookie*`, `secUid*`, `cursor`, `count`, `coverFormat`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_fans`

- 能力：主页/账号
- 入参：query: `secUid*`, `count`, `maxCursor`, `minCursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_follow`

- 能力：主页/账号
- 入参：query: `secUid*`, `count`, `maxCursor`, `minCursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_like`

- 能力：主页/账号
- 入参：query: `secUid*`, `cursor`, `count`, `coverFormat`, `post_item_list_request_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_like_api_v1_tiktok_web_fetch_user_like_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_live_detail`

- 能力：主页/账号 / 详情 / 直播
- 入参：query: `uniqueId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_mix`

- 能力：主页/账号
- 入参：query: `mixId*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_play_list`

- 能力：主页/账号
- 入参：query: `secUid*`, `cursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_post`

- 能力：主页/账号 / 作品详情
- 入参：query: `secUid*`, `cursor`, `count`, `coverFormat`, `post_item_list_request_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_api_v1_tiktok_web_fetch_user_post_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_profile`

- 能力：主页/账号
- 入参：query: `uniqueId`, `secUid`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get`

### `GET /api/u1/v1/tiktok/web/fetch_user_repost`

- 能力：主页/账号 / 作品详情
- 入参：query: `secUid*`, `cursor`, `count`, `coverFormat`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get`

### `GET /api/u1/v1/tiktok/web/generate_fingerprint`

- 能力：通用能力
- 入参：query: `browser_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get`

### `GET /api/u1/v1/tiktok/web/generate_hashed_id`

- 能力：通用能力
- 入参：query: `email*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get`

### `GET /api/u1/v1/tiktok/web/generate_real_msToken`

- 能力：通用能力
- 入参：query: `random_strData`, `browser_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_real_msToken_api_v1_tiktok_web_generate_real_msToken_get`

### `GET /api/u1/v1/tiktok/web/generate_ttwid`

- 能力：通用能力
- 入参：query: `user_agent`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_ttwid_api_v1_tiktok_web_generate_ttwid_get`

### `GET /api/u1/v1/tiktok/web/generate_webid`

- 能力：通用能力
- 入参：query: `cookie`, `user_agent`, `url`, `referer`, `user_unique_id`, `app_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_webid_api_v1_tiktok_web_generate_webid_get`

### `POST /api/u1/v1/tiktok/web/generate_xbogus`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `url*`:string, `user_agent*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_xbogus_api_v1_tiktok_web_generate_xbogus_post`

### `POST /api/u1/v1/tiktok/web/generate_xgnarly`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `url*`:string, `user_agent*`:string, `body`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post`

### `POST /api/u1/v1/tiktok/web/generate_xgnarly_and_xbogus`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `url*`:string, `body`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post`

### `POST /api/u1/v1/tiktok/web/get_all_aweme_id`

- 能力：通用能力
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post`

### `POST /api/u1/v1/tiktok/web/get_all_sec_user_id`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post`

### `POST /api/u1/v1/tiktok/web/get_all_unique_id`

- 能力：通用能力
- 入参：无
- 请求体：application/json: [string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post`

### `GET /api/u1/v1/tiktok/web/get_aweme_id`

- 能力：通用能力
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_aweme_id_api_v1_tiktok_web_get_aweme_id_get`

### `GET /api/u1/v1/tiktok/web/get_live_room_id`

- 能力：直播
- 入参：query: `live_room_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_live_room_id_api_v1_tiktok_web_get_live_room_id_get`

### `GET /api/u1/v1/tiktok/web/get_sec_user_id`

- 能力：主页/账号
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get`

### `GET /api/u1/v1/tiktok/web/get_unique_id`

- 能力：通用能力
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_unique_id_api_v1_tiktok_web_get_unique_id_get`

### `GET /api/u1/v1/tiktok/web/get_user_id`

- 能力：主页/账号
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_id_api_v1_tiktok_web_get_user_id_get`

### `GET /api/u1/v1/tiktok/web/tiktok_live_room`

- 能力：直播
- 入参：query: `live_room_url*`, `danmaku_type*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get`
