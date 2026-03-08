# Xiaohongshu-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/xiaohongshu-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`17`
- 常见能力：作品详情 / 主页/账号 / 搜索 / 评论 / 通用能力 / 电商
- 常见入参：`note_id`, `share_text`, `cookie`, `proxy`, `lastCursor`, `user_id`, `keyword`, `page`, `xsec_token`, `sort`
- 标签说明：**(小红书Web数据接口/Xiaohongshu-Web-API data endpoints)** - 第四优先/Fourth choice

## 路由列表

### `POST /api/u1/v1/xiaohongshu/web/get_home_recommend`

- 能力：主页/账号
- 入参：无
- 请求体：application/json: `feed_type`:string, `need_filter_image`:boolean, `cursor_score`:string, `cookie`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_home_recommend_api_v1_xiaohongshu_web_get_home_recommend_post`

### `GET /api/u1/v1/xiaohongshu/web/get_note_comment_replies`

- 能力：评论 / 作品详情
- 入参：query: `note_id*`, `comment_id*`, `lastCursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_comment_replies_api_v1_xiaohongshu_web_get_note_comment_replies_get`

### `GET /api/u1/v1/xiaohongshu/web/get_note_comments`

- 能力：评论 / 作品详情
- 入参：query: `note_id*`, `lastCursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_comments_api_v1_xiaohongshu_web_get_note_comments_get`

### `GET /api/u1/v1/xiaohongshu/web/get_note_id_and_xsec_token`

- 能力：作品详情
- 入参：query: `share_text*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_id_and_xsec_token_api_v1_xiaohongshu_web_get_note_id_and_xsec_token_get`

### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v2`

- 能力：作品详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_info_v2_api_v1_xiaohongshu_web_get_note_info_v2_get`

### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v4`

- 能力：作品详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_info_v4_api_v1_xiaohongshu_web_get_note_info_v4_get`

### `POST /api/u1/v1/xiaohongshu/web/get_note_info_v5`

- 能力：作品详情
- 入参：无
- 请求体：application/json: `note_id`:string, `xsec_token`:string, `cookie`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_info_v5_api_v1_xiaohongshu_web_get_note_info_v5_post`

### `GET /api/u1/v1/xiaohongshu/web/get_note_info_v7`

- 能力：作品详情
- 入参：query: `note_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_note_info_v7_api_v1_xiaohongshu_web_get_note_info_v7_get`

### `GET /api/u1/v1/xiaohongshu/web/get_product_info`

- 能力：电商
- 入参：query: `share_text`, `item_id`, `xsec_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_info_api_v1_xiaohongshu_web_get_product_info_get`

### `GET /api/u1/v1/xiaohongshu/web/get_user_info`

- 能力：主页/账号
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_info_api_v1_xiaohongshu_web_get_user_info_get`

### `GET /api/u1/v1/xiaohongshu/web/get_user_info_v2`

- 能力：主页/账号
- 入参：query: `user_id`, `share_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_info_v2_api_v1_xiaohongshu_web_get_user_info_v2_get`

### `GET /api/u1/v1/xiaohongshu/web/get_user_notes_v2`

- 能力：主页/账号 / 作品详情
- 入参：query: `user_id*`, `lastCursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_user_notes_api_v1_xiaohongshu_web_get_user_notes_v2_get`

### `GET /api/u1/v1/xiaohongshu/web/get_visitor_cookie`

- 能力：通用能力
- 入参：query: `proxy`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_visitor_cookie_api_v1_xiaohongshu_web_get_visitor_cookie_get`

### `GET /api/u1/v1/xiaohongshu/web/search_notes`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `page`, `sort`, `noteType`, `noteTime`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_notes_api_v1_xiaohongshu_web_search_notes_get`

### `GET /api/u1/v1/xiaohongshu/web/search_notes_v3`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `page`, `sort`, `noteType`, `noteTime`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_notes_v3_api_v1_xiaohongshu_web_search_notes_v3_get`

### `GET /api/u1/v1/xiaohongshu/web/search_users`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_users_api_v1_xiaohongshu_web_search_users_get`

### `POST /api/u1/v1/xiaohongshu/web/sign`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `path`:string, `data`{...}, `cookie`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`sign_api_v1_xiaohongshu_web_sign_post`
