# Kuaishou-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/kuaishou-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`13`
- 常见能力：作品详情 / 主页/账号 / 热点/榜单 / 评论 / 直播 / 通用能力
- 常见入参：`pcursor`, `photo_id`, `user_id`, `share_link`, `board_type`, `share_text`, `url`, `root_comment_id`
- 标签说明：**(快手Web数据接口/Kuaishou-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/kuaishou/web/fetch_get_user_id`

- 能力：主页/账号
- 入参：query: `share_link*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_get_user_id_api_v1_kuaishou_web_fetch_get_user_id_get`

### `GET /api/u1/v1/kuaishou/web/fetch_kuaishou_hot_list_v1`

- 能力：热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_kuaishou_hot_list_v1_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v1_get`

### `GET /api/u1/v1/kuaishou/web/fetch_kuaishou_hot_list_v2`

- 能力：热点/榜单
- 入参：query: `board_type`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_kuaishou_hot_list_v2_api_v1_kuaishou_web_fetch_kuaishou_hot_list_v2_get`

### `GET /api/u1/v1/kuaishou/web/fetch_one_video`

- 能力：作品详情
- 入参：query: `share_text*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get`

### `GET /api/u1/v1/kuaishou/web/fetch_one_video_by_url`

- 能力：作品详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get`

### `GET /api/u1/v1/kuaishou/web/fetch_one_video_comment`

- 能力：评论 / 作品详情
- 入参：query: `photo_id*`, `pcursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get`

### `GET /api/u1/v1/kuaishou/web/fetch_one_video_sub_comment`

- 能力：评论 / 作品详情
- 入参：query: `photo_id*`, `pcursor`, `root_comment_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_sub_comment_api_v1_kuaishou_web_fetch_one_video_sub_comment_get`

### `GET /api/u1/v1/kuaishou/web/fetch_one_video_v2`

- 能力：作品详情
- 入参：query: `photo_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get`

### `GET /api/u1/v1/kuaishou/web/fetch_user_collect`

- 能力：主页/账号
- 入参：query: `user_id*`, `pcursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_collect_api_v1_kuaishou_web_fetch_user_collect_get`

### `GET /api/u1/v1/kuaishou/web/fetch_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get`

### `GET /api/u1/v1/kuaishou/web/fetch_user_live_replay`

- 能力：主页/账号 / 直播
- 入参：query: `user_id*`, `pcursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_live_replay_api_v1_kuaishou_web_fetch_user_live_replay_get`

### `GET /api/u1/v1/kuaishou/web/fetch_user_post`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `pcursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_api_v1_kuaishou_web_fetch_user_post_get`

### `GET /api/u1/v1/kuaishou/web/generate_share_short_url`

- 能力：通用能力
- 入参：query: `photo_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`generate_share_short_url_api_v1_kuaishou_web_generate_share_short_url_get`
