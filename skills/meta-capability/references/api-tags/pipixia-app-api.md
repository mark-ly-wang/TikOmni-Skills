# PiPiXia-App-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/pipixia-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`17`
- 常见能力：作品详情 / 主页/账号 / 搜索 / 详情 / 热点/榜单 / 话题
- 常见入参：`cursor`, `cell_id`, `user_id`, `cell_type`, `hashtag_id`, `feed_count`, `offset`, `hashtag_request_type`, `hashtag_sort_type`, `page`
- 标签说明：**(皮皮虾App数据接口/PiPiXia-App-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/pipixia/app/fetch_hashtag_detail`

- 能力：详情 / 话题
- 入参：query: `hashtag_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_detail_api_v1_pipixia_app_fetch_hashtag_detail_get`

### `GET /api/u1/v1/pipixia/app/fetch_hashtag_post_list`

- 能力：作品详情 / 话题
- 入参：query: `hashtag_id*`, `cursor`, `feed_count`, `hashtag_request_type`, `hashtag_sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hashtag_post_list_api_v1_pipixia_app_fetch_hashtag_post_list_get`

### `GET /api/u1/v1/pipixia/app/fetch_home_feed`

- 能力：主页/账号
- 入参：query: `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_feed_api_v1_pipixia_app_fetch_home_feed_get`

### `GET /api/u1/v1/pipixia/app/fetch_home_short_drama_feed`

- 能力：主页/账号
- 入参：query: `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_short_drama_feed_api_v1_pipixia_app_fetch_home_short_drama_feed_get`

### `GET /api/u1/v1/pipixia/app/fetch_hot_search_board_detail`

- 能力：搜索 / 热点/榜单 / 详情
- 入参：query: `block_type*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_board_detail_api_v1_pipixia_app_fetch_hot_search_board_detail_get`

### `GET /api/u1/v1/pipixia/app/fetch_hot_search_board_list`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_board_list_api_v1_pipixia_app_fetch_hot_search_board_list_get`

### `GET /api/u1/v1/pipixia/app/fetch_hot_search_words`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_words_api_v1_pipixia_app_fetch_hot_search_words_get`

### `GET /api/u1/v1/pipixia/app/fetch_increase_post_view_count`

- 能力：作品详情
- 入参：query: `cell_id*`, `cell_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_increase_post_view_count_api_v1_pipixia_app_fetch_increase_post_view_count_get`

### `GET /api/u1/v1/pipixia/app/fetch_post_comment_list`

- 能力：评论 / 作品详情
- 入参：query: `cell_id*`, `cell_type`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comment_list_api_v1_pipixia_app_fetch_post_comment_list_get`

### `GET /api/u1/v1/pipixia/app/fetch_post_detail`

- 能力：作品详情 / 详情
- 入参：query: `cell_id*`, `cell_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_api_v1_pipixia_app_fetch_post_detail_get`

### `GET /api/u1/v1/pipixia/app/fetch_post_statistics`

- 能力：作品详情
- 入参：query: `cell_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_statistics_api_v1_pipixia_app_fetch_post_statistics_get`

### `GET /api/u1/v1/pipixia/app/fetch_search`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `search_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_api_v1_pipixia_app_fetch_search_get`

### `GET /api/u1/v1/pipixia/app/fetch_short_url`

- 能力：通用能力
- 入参：query: `original_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_short_url_api_v1_pipixia_app_fetch_short_url_get`

### `GET /api/u1/v1/pipixia/app/fetch_user_follower_list`

- 能力：主页/账号
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follower_list_api_v1_pipixia_app_fetch_user_follower_list_get`

### `GET /api/u1/v1/pipixia/app/fetch_user_following_list`

- 能力：主页/账号
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_following_list_api_v1_pipixia_app_fetch_user_following_list_get`

### `GET /api/u1/v1/pipixia/app/fetch_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_pipixia_app_fetch_user_info_get`

### `GET /api/u1/v1/pipixia/app/fetch_user_post_list`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `cursor`, `feed_count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_list_api_v1_pipixia_app_fetch_user_post_list_get`
