# Lemon8-App-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/lemon8-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`16`
- 常见能力：通用能力 / 主页/账号 / 作品详情 / 搜索 / 话题 / 热点/榜单
- 常见入参：`user_id`, `item_id`, `cursor`, `share_text`, `group_id`, `media_id`, `offset`, `query`, `max_cursor`, `filter_type`
- 标签说明：**(Lemon8 APP数据接口/Lemon8-APP-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/lemon8/app/fetch_discover_banners`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_discover_banners_api_v1_lemon8_app_fetch_discover_banners_get`

### `GET /api/u1/v1/lemon8/app/fetch_discover_tab`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_discover_tab_api_v1_lemon8_app_fetch_discover_tab_get`

### `GET /api/u1/v1/lemon8/app/fetch_discover_tab_information_tabs`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_discover_tab_information_tabs_api_v1_lemon8_app_fetch_discover_tab_information_tabs_get`

### `GET /api/u1/v1/lemon8/app/fetch_hot_search_keywords`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_keywords_api_v1_lemon8_app_fetch_hot_search_keywords_get`

### `GET /api/u1/v1/lemon8/app/fetch_post_comment_list`

- 能力：评论 / 作品详情
- 入参：query: `group_id*`, `item_id*`, `media_id*`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comment_list_api_v1_lemon8_app_fetch_post_comment_list_get`

### `GET /api/u1/v1/lemon8/app/fetch_post_detail`

- 能力：作品详情 / 详情
- 入参：query: `item_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_api_v1_lemon8_app_fetch_post_detail_get`

### `GET /api/u1/v1/lemon8/app/fetch_search`

- 能力：搜索
- 入参：query: `query*`, `max_cursor`, `filter_type`, `order_by`, `search_tab`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_api_v1_lemon8_app_fetch_search_get`

### `GET /api/u1/v1/lemon8/app/fetch_topic_info`

- 能力：话题
- 入参：query: `forum_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_topic_info_api_v1_lemon8_app_fetch_topic_info_get`

### `GET /api/u1/v1/lemon8/app/fetch_topic_post_list`

- 能力：作品详情 / 话题
- 入参：query: `category*`, `max_behot_time`, `category_parameter*`, `hashtag_name*`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_topic_post_list_api_v1_lemon8_app_fetch_topic_post_list_get`

### `GET /api/u1/v1/lemon8/app/fetch_user_follower_list`

- 能力：主页/账号
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follower_list_api_v1_lemon8_app_fetch_user_follower_list_get`

### `GET /api/u1/v1/lemon8/app/fetch_user_following_list`

- 能力：主页/账号
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_following_list_api_v1_lemon8_app_fetch_user_following_list_get`

### `GET /api/u1/v1/lemon8/app/fetch_user_profile`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`handler_user_profile_api_v1_lemon8_app_fetch_user_profile_get`

### `GET /api/u1/v1/lemon8/app/get_item_id`

- 能力：通用能力
- 入参：query: `share_text*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_item_id_api_v1_lemon8_app_get_item_id_get`

### `POST /api/u1/v1/lemon8/app/get_item_ids`

- 能力：通用能力
- 入参：无
- 请求体：application/json: []
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_item_ids_api_v1_lemon8_app_get_item_ids_post`

### `GET /api/u1/v1/lemon8/app/get_user_id`

- 能力：主页/账号
- 入参：query: `share_text*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_id_api_v1_lemon8_app_get_user_id_get`

### `POST /api/u1/v1/lemon8/app/get_user_ids`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: []
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_ids_api_v1_lemon8_app_get_user_ids_post`
