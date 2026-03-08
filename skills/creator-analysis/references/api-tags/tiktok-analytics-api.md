# TikTok-Analytics-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-analytics-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`4`
- 常见能力：数据分析 / 评论 / 创作者 / 作品详情
- 常见入参：`item_id`, `content_category`, `user_id`
- 标签说明：**(TikTok数据分析接口/TikTok-Analytics-API data analysis endpoints)**

## 路由列表

### `GET /api/u1/v1/tiktok/analytics/detect_fake_views`

- 能力：数据分析
- 入参：query: `item_id*`, `content_category`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`detect_fake_views_api_v1_tiktok_analytics_detect_fake_views_get`

### `GET /api/u1/v1/tiktok/analytics/fetch_comment_keywords`

- 能力：评论 / 数据分析
- 入参：query: `item_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_comment_keywords_api_v1_tiktok_analytics_fetch_comment_keywords_get`

### `GET /api/u1/v1/tiktok/analytics/fetch_creator_info_and_milestones`

- 能力：创作者 / 数据分析
- 入参：query: `user_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_info_and_milestones_api_v1_tiktok_analytics_fetch_creator_info_and_milestones_get`

### `GET /api/u1/v1/tiktok/analytics/fetch_video_metrics`

- 能力：作品详情 / 数据分析
- 入参：query: `item_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_metrics_api_v1_tiktok_analytics_fetch_video_metrics_get`
