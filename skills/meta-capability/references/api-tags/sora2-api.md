# Sora2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/sora2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`17`
- 常见能力：作品详情 / 主页/账号 / 通用能力 / 评论 / 详情 / 下载/媒体
- 常见入参：`cursor`, `user_id`, `post_id`, `post_url`, `task_id`, `prompt`, `orientation`, `media_id`, `comment_id`, `eager_views`
- 标签说明：**(Sora2 接口/Sora2 API endpoints)**

## 路由列表

### `POST /api/u1/v1/sora2/create_video`

- 能力：作品详情
- 入参：无
- 请求体：application/json: `prompt*`:string, `orientation`:string, `media_id`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`create_video_api_v1_sora2_create_video_post`

### `GET /api/u1/v1/sora2/get_cameo_leaderboard`

- 能力：通用能力
- 入参：query: `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_cameo_leaderboard_api_v1_sora2_get_cameo_leaderboard_get`

### `GET /api/u1/v1/sora2/get_comment_replies`

- 能力：评论
- 入参：query: `comment_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_comment_replies_api_v1_sora2_get_comment_replies_get`

### `GET /api/u1/v1/sora2/get_feed`

- 能力：通用能力
- 入参：query: `cursor`, `eager_views`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_feed_api_v1_sora2_get_feed_get`

### `GET /api/u1/v1/sora2/get_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `post_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_post_comments_api_v1_sora2_get_post_comments_get`

### `GET /api/u1/v1/sora2/get_post_detail`

- 能力：作品详情 / 详情
- 入参：query: `post_id`, `post_url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_post_detail_api_v1_sora2_get_post_detail_get`

### `GET /api/u1/v1/sora2/get_post_remix_list`

- 能力：作品详情
- 入参：query: `post_id`, `post_url`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_post_remix_list_api_v1_sora2_get_post_remix_list_get`

### `GET /api/u1/v1/sora2/get_task_detail`

- 能力：详情
- 入参：query: `task_id`, `generation_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_task_detail_api_v1_sora2_get_task_detail_get`

### `GET /api/u1/v1/sora2/get_task_status`

- 能力：通用能力
- 入参：query: `task_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_task_status_api_v1_sora2_get_task_status_get`

### `GET /api/u1/v1/sora2/get_user_cameo_appearances`

- 能力：主页/账号
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_cameo_appearances_api_v1_sora2_get_user_cameo_appearances_get`

### `GET /api/u1/v1/sora2/get_user_followers`

- 能力：主页/账号
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_followers_api_v1_sora2_get_user_followers_get`

### `GET /api/u1/v1/sora2/get_user_following`

- 能力：主页/账号
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_following_api_v1_sora2_get_user_following_get`

### `GET /api/u1/v1/sora2/get_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_posts_api_v1_sora2_get_user_posts_get`

### `GET /api/u1/v1/sora2/get_user_profile`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_profile_api_v1_sora2_get_user_profile_get`

### `GET /api/u1/v1/sora2/get_video_download_info`

- 能力：作品详情 / 下载/媒体
- 入参：query: `post_id`, `post_url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_download_info_api_v1_sora2_get_video_download_info_get`

### `GET /api/u1/v1/sora2/search_users`

- 能力：搜索 / 主页/账号
- 入参：query: `username*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_users_api_v1_sora2_search_users_get`

### `POST /api/u1/v1/sora2/upload_image`

- 能力：媒体上传/公网URL
- 入参：无
- 请求体：multipart/form-data: `file*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`upload_image_api_v1_sora2_upload_image_post`
