# Toutiao-App-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/toutiao-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`5`
- 常见能力：作品详情 / 主页/账号 / 评论
- 常见入参：`group_id`, `offset`, `user_profile_url`, `user_id`
- 标签说明：**(今日头条App数据接口/Toutiao-App-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/toutiao/app/get_article_info`

- 能力：作品详情
- 入参：query: `group_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_article_info_api_v1_toutiao_app_get_article_info_get`

### `GET /api/u1/v1/toutiao/app/get_comments`

- 能力：评论
- 入参：query: `group_id*`, `offset*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_comments_api_v1_toutiao_app_get_comments_get`

### `GET /api/u1/v1/toutiao/app/get_user_id`

- 能力：主页/账号
- 入参：query: `user_profile_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_id_api_v1_toutiao_app_get_user_id_get`

### `GET /api/u1/v1/toutiao/app/get_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_info_api_v1_toutiao_app_get_user_info_get`

### `GET /api/u1/v1/toutiao/app/get_video_info`

- 能力：作品详情
- 入参：query: `group_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_info_api_v1_toutiao_app_get_video_info_get`
