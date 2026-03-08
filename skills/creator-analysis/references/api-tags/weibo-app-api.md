# Weibo-App-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/weibo-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`20`
- 常见能力：主页/账号 / 作品详情 / 搜索 / 详情 / 热点/榜单 / 评论
- 常见入参：`uid`, `page`, `since_id`, `status_id`, `query`, `count`, `max_id`, `category`, `search_type`, `sort_type`
- 标签说明：**(新浪微博APP数据接口/Weibo-App-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/weibo/app/fetch_ai_smart_search`

- 能力：搜索
- 入参：query: `query*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get`

### `GET /api/u1/v1/weibo/app/fetch_home_recommend_feed`

- 能力：主页/账号
- 入参：query: `page`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get`

### `GET /api/u1/v1/weibo/app/fetch_hot_search`

- 能力：搜索 / 热点/榜单
- 入参：query: `category`, `page`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get`

### `GET /api/u1/v1/weibo/app/fetch_hot_search_categories`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get`

### `GET /api/u1/v1/weibo/app/fetch_search_all`

- 能力：搜索
- 入参：query: `query*`, `page`, `search_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_all_api_v1_weibo_app_fetch_search_all_get`

### `GET /api/u1/v1/weibo/app/fetch_status_comments`

- 能力：评论
- 入参：query: `status_id*`, `max_id`, `sort_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get`

### `GET /api/u1/v1/weibo/app/fetch_status_detail`

- 能力：详情
- 入参：query: `status_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get`

### `GET /api/u1/v1/weibo/app/fetch_status_likes`

- 能力：通用能力
- 入参：query: `status_id*`, `attitude_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get`

### `GET /api/u1/v1/weibo/app/fetch_status_reposts`

- 能力：作品详情
- 入参：query: `status_id*`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get`

### `GET /api/u1/v1/weibo/app/fetch_user_album`

- 能力：主页/账号
- 入参：query: `uid*`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_album_api_v1_weibo_app_fetch_user_album_get`

### `GET /api/u1/v1/weibo/app/fetch_user_articles`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get`

### `GET /api/u1/v1/weibo/app/fetch_user_audios`

- 能力：主页/账号 / 音频/媒体
- 入参：query: `uid*`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get`

### `GET /api/u1/v1/weibo/app/fetch_user_info`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_weibo_app_fetch_user_info_get`

### `GET /api/u1/v1/weibo/app/fetch_user_info_detail`

- 能力：主页/账号 / 详情
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get`

### `GET /api/u1/v1/weibo/app/fetch_user_profile_feed`

- 能力：主页/账号
- 入参：query: `uid*`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get`

### `GET /api/u1/v1/weibo/app/fetch_user_super_topics`

- 能力：主页/账号 / 话题
- 入参：query: `uid*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get`

### `GET /api/u1/v1/weibo/app/fetch_user_timeline`

- 能力：主页/账号
- 入参：query: `uid*`, `page`, `filter_type`, `month`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get`

### `GET /api/u1/v1/weibo/app/fetch_user_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get`

### `GET /api/u1/v1/weibo/app/fetch_video_detail`

- 能力：作品详情 / 详情
- 入参：query: `mid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get`

### `GET /api/u1/v1/weibo/app/fetch_video_featured_feed`

- 能力：作品详情
- 入参：query: `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get`
