# Kuaishou-App-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/kuaishou-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`20`
- 常见能力：作品详情 / 热点/榜单 / 主页/账号 / 搜索 / 通用能力 / 直播
- 常见入参：`pcursor`, `user_id`, `subTabId`, `subTabName`, `keyword`, `magic_face_id`, `photo_id`, `page`, `boardType`, `boardId`
- 标签说明：**(快手App数据接口/Kuaishou-App-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/kuaishou/app/fetch_brand_top_list`

- 能力：通用能力
- 入参：query: `subTabId`, `subTabName`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get`

### `GET /api/u1/v1/kuaishou/app/fetch_hot_board_categories`

- 能力：热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get`

### `GET /api/u1/v1/kuaishou/app/fetch_hot_board_detail`

- 能力：热点/榜单 / 详情
- 入参：query: `boardType`, `boardId`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get`

### `GET /api/u1/v1/kuaishou/app/fetch_hot_search_person`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get`

### `GET /api/u1/v1/kuaishou/app/fetch_live_top_list`

- 能力：直播
- 入参：query: `subTabId`, `subTabName`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get`

### `GET /api/u1/v1/kuaishou/app/fetch_magic_face_hot`

- 能力：热点/榜单
- 入参：query: `magic_face_id*`, `pcursor`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get`

### `GET /api/u1/v1/kuaishou/app/fetch_magic_face_usage`

- 能力：通用能力
- 入参：query: `magic_face_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get`

### `GET /api/u1/v1/kuaishou/app/fetch_one_user_v2`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get`

### `GET /api/u1/v1/kuaishou/app/fetch_one_video`

- 能力：作品详情
- 入参：query: `photo_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get`

### `GET /api/u1/v1/kuaishou/app/fetch_one_video_by_url`

- 能力：作品详情
- 入参：query: `share_text*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get`

### `GET /api/u1/v1/kuaishou/app/fetch_one_video_comment`

- 能力：评论 / 作品详情
- 入参：query: `photo_id*`, `pcursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get`

### `GET /api/u1/v1/kuaishou/app/fetch_shopping_top_list`

- 能力：电商
- 入参：query: `subTabId`, `subTabName`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get`

### `GET /api/u1/v1/kuaishou/app/fetch_user_hot_post`

- 能力：热点/榜单 / 主页/账号 / 作品详情
- 入参：query: `user_id*`, `pcursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get`

### `GET /api/u1/v1/kuaishou/app/fetch_user_live_info`

- 能力：主页/账号 / 直播
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get`

### `GET /api/u1/v1/kuaishou/app/fetch_user_post_v2`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `pcursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get`

### `GET /api/u1/v1/kuaishou/app/fetch_videos_batch`

- 能力：作品详情
- 入参：query: `photo_ids*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get`

### `GET /api/u1/v1/kuaishou/app/generate_kuaishou_share_link`

- 能力：通用能力
- 入参：query: `shareObjectId*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get`

### `GET /api/u1/v1/kuaishou/app/search_comprehensive`

- 能力：搜索
- 入参：query: `keyword*`, `pcursor`, `sort_type`, `publish_time`, `duration`, `search_scope`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get`

### `GET /api/u1/v1/kuaishou/app/search_user_v2`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_user_v2_api_v1_kuaishou_app_search_user_v2_get`

### `GET /api/u1/v1/kuaishou/app/search_video_v2`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_video_v2_api_v1_kuaishou_app_search_video_v2_get`
