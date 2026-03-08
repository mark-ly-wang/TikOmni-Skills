# Weibo-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/weibo-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`11`
- 常见能力：主页/账号 / 搜索 / 作品详情 / 评论 / 热点/榜单 / 通用能力
- 常见入参：`page`, `max_id`, `post_id`, `uid`, `channel_name`, `cid`, `mid`, `max_id_type`, `keyword`, `search_type`
- 标签说明：**(新浪微博Web数据接口/Weibo-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/weibo/web/fetch_channel_feed`

- 能力：主页/账号
- 入参：query: `channel_name`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_channel_feed_api_v1_weibo_web_fetch_channel_feed_get`

### `GET /api/u1/v1/weibo/web/fetch_comment_replies`

- 能力：评论
- 入参：query: `cid*`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_comment_replies_api_v1_weibo_web_fetch_comment_replies_get`

### `GET /api/u1/v1/weibo/web/fetch_config_list`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_config_list_api_v1_weibo_web_fetch_config_list_get`

### `GET /api/u1/v1/weibo/web/fetch_hot_search`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_api_v1_weibo_web_fetch_hot_search_get`

### `GET /api/u1/v1/weibo/web/fetch_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `post_id*`, `mid*`, `max_id`, `max_id_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comments_api_v1_weibo_web_fetch_post_comments_get`

### `GET /api/u1/v1/weibo/web/fetch_post_detail`

- 能力：作品详情 / 详情
- 入参：query: `post_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get`

### `GET /api/u1/v1/weibo/web/fetch_search`

- 能力：搜索
- 入参：query: `keyword*`, `page`, `search_type`, `time_scope`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_api_v1_weibo_web_fetch_search_get`

### `GET /api/u1/v1/weibo/web/fetch_search_topics`

- 能力：搜索 / 话题
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_topics_api_v1_weibo_web_fetch_search_topics_get`

### `GET /api/u1/v1/weibo/web/fetch_trend_top`

- 能力：热点/榜单
- 入参：query: `containerid*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_trend_top_api_v1_weibo_web_fetch_trend_top_get`

### `GET /api/u1/v1/weibo/web/fetch_user_info`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_weibo_web_fetch_user_info_get`

### `GET /api/u1/v1/weibo/web/fetch_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`, `page`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get`
