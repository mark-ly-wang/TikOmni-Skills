# Bilibili-App-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/bilibili-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`11`
- 常见能力：通用能力 / 主页/账号 / 作品详情 / 搜索 / 评论回复 / 详情
- 常见入参：`av_id`, `bv_id`, `page`, `idx`, `next_offset`, `ps`, `keyword`, `page_size`, `order`, `user_id`
- 标签说明：**(哔哩哔哩App数据接口/Bilibili-App-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/bilibili/app/fetch_bangumi_tab`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_bangumi_tab_api_v1_bilibili_app_fetch_bangumi_tab_get`

### `GET /api/u1/v1/bilibili/app/fetch_cinema_tab`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_cinema_tab_api_v1_bilibili_app_fetch_cinema_tab_get`

### `GET /api/u1/v1/bilibili/app/fetch_home_feed`

- 能力：主页/账号
- 入参：query: `idx`, `flush`, `pull`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_feed_api_v1_bilibili_app_fetch_home_feed_get`

### `GET /api/u1/v1/bilibili/app/fetch_one_video`

- 能力：作品详情
- 入参：query: `av_id`, `bv_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_bilibili_app_fetch_one_video_get`

### `GET /api/u1/v1/bilibili/app/fetch_popular_feed`

- 能力：通用能力
- 入参：query: `idx`, `last_param`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_popular_feed_api_v1_bilibili_app_fetch_popular_feed_get`

### `GET /api/u1/v1/bilibili/app/fetch_reply_detail`

- 能力：评论回复 / 详情
- 入参：query: `root*`, `av_id`, `bv_id`, `next_offset`, `ps`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_reply_detail_api_v1_bilibili_app_fetch_reply_detail_get`

### `GET /api/u1/v1/bilibili/app/fetch_search_all`

- 能力：搜索
- 入参：query: `keyword*`, `page`, `page_size`, `order`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_all_api_v1_bilibili_app_fetch_search_all_get`

### `GET /api/u1/v1/bilibili/app/fetch_search_by_type`

- 能力：搜索
- 入参：query: `keyword*`, `search_type`, `page`, `page_size`, `order`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_by_type_api_v1_bilibili_app_fetch_search_by_type_get`

### `GET /api/u1/v1/bilibili/app/fetch_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_bilibili_app_fetch_user_info_get`

### `GET /api/u1/v1/bilibili/app/fetch_user_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `post_filter`, `page`, `ps`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_videos_api_v1_bilibili_app_fetch_user_videos_get`

### `GET /api/u1/v1/bilibili/app/fetch_video_comments`

- 能力：评论 / 作品详情
- 入参：query: `av_id`, `bv_id`, `mode`, `next_offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_comments_api_v1_bilibili_app_fetch_video_comments_get`
