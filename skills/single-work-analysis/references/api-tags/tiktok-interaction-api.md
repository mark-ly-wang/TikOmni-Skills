# TikTok-Interaction-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-interaction-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`7`
- 常见能力：通用能力 / 评论 / 作品详情 / 评论回复
- 常见入参：`cookie`, `device_id`, `iid`, `proxy`, `aweme_id`, `text`, `api_key`, `invite_code`, `user_id`, `sec_user_id`
- 标签说明：**(TikTok交互类接口（不在提供该业务）/TikTok-Interaction-API (This service is no longer available))**

## 路由列表

### `GET /api/u1/v1/tiktok/interaction/apply`

- 能力：通用能力
- 入参：query: `api_key*`, `invite_code*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`apply_for_scope_api_v1_tiktok_interaction_apply_get`

### `POST /api/u1/v1/tiktok/interaction/collect`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`collect_api_v1_tiktok_interaction_collect_post`

### `POST /api/u1/v1/tiktok/interaction/follow`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `user_id`:string, `sec_user_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`follow_api_v1_tiktok_interaction_follow_post`

### `POST /api/u1/v1/tiktok/interaction/forward`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`forward_api_v1_tiktok_interaction_forward_post`

### `POST /api/u1/v1/tiktok/interaction/like`

- 能力：通用能力
- 入参：无
- 请求体：application/json: `aweme_id`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`like_api_v1_tiktok_interaction_like_post`

### `POST /api/u1/v1/tiktok/interaction/post_comment`

- 能力：评论 / 作品详情
- 入参：无
- 请求体：application/json: `aweme_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`post_comment_api_v1_tiktok_interaction_post_comment_post`

### `POST /api/u1/v1/tiktok/interaction/reply_comment`

- 能力：评论 / 评论回复
- 入参：无
- 请求体：application/json: `aweme_id`:string, `reply_id`:string, `text`:string, `cookie`:string, `device_id`:string, `iid`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`reply_comment_api_v1_tiktok_interaction_reply_comment_post`
