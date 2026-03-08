# WeChat-Channels-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/wechat-channels-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`9`
- 常见能力：主页/账号 / 搜索 / 评论 / 热点/榜单 / 直播 / 作品详情
- 常见入参：`keywords`, `id`, `username`, `lastBuffer`, `comment_id`, `session_buffer`, `last_buffer`, `page`, `exportId`
- 标签说明：**(微信视频号数据接口/WeChat-Channels-API data endpoints)**

## 路由列表

### `POST /api/u1/v1/wechat_channels/fetch_comments`

- 能力：评论 / 主页/账号
- 入参：无
- 请求体：application/json: `id*`:string, `lastBuffer`:string, `comment_id`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_comments_api_v1_wechat_channels_fetch_comments_post`

### `POST /api/u1/v1/wechat_channels/fetch_default_search`

- 能力：搜索 / 主页/账号
- 入参：无
- 请求体：application/json: `keywords*`:string, `session_buffer`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_default_search_api_v1_wechat_channels_fetch_default_search_post`

### `POST /api/u1/v1/wechat_channels/fetch_home_page`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: `username*`:string, `last_buffer`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_page_api_v1_wechat_channels_fetch_home_page_post`

### `GET /api/u1/v1/wechat_channels/fetch_hot_words`

- 能力：热点/榜单 / 主页/账号
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_words_api_v1_wechat_channels_fetch_hot_words_get`

### `GET /api/u1/v1/wechat_channels/fetch_live_history`

- 能力：主页/账号 / 直播
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_history_api_v1_wechat_channels_fetch_live_history_get`

### `GET /api/u1/v1/wechat_channels/fetch_search_latest`

- 能力：搜索 / 主页/账号
- 入参：query: `keywords*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_latest_api_v1_wechat_channels_fetch_search_latest_get`

### `GET /api/u1/v1/wechat_channels/fetch_search_ordinary`

- 能力：搜索 / 主页/账号
- 入参：query: `keywords*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_ordinary_api_v1_wechat_channels_fetch_search_ordinary_get`

### `GET /api/u1/v1/wechat_channels/fetch_user_search`

- 能力：搜索 / 主页/账号
- 入参：query: `keywords*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_api_v1_wechat_channels_fetch_user_search_get`

### `GET /api/u1/v1/wechat_channels/fetch_video_detail`

- 能力：主页/账号 / 作品详情 / 详情
- 入参：query: `id`, `exportId`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_detail_api_v1_wechat_channels_fetch_video_detail_get`
