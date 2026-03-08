# TikTok-Creator-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-creator-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`14`
- 常见能力：创作者 / 作品详情 / 数据分析 / 电商 / 直播 / 详情
- 常见入参：`cookie`, `proxy`, `start_date`, `item_id`, `page`, `product_id`, `end_date`, `count`, `offset`, `item_ids`
- 标签说明：**(TikTok创作者数据和账号收益数据接口/TikTok-Creator-API data and account revenue data endpoints)**

## 路由列表

### `POST /api/u1/v1/tiktok/creator/get_account_health_status`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_account_health_status_api_v1_tiktok_creator_get_account_health_status_post`

### `POST /api/u1/v1/tiktok/creator/get_account_insights_overview`

- 能力：创作者 / 数据分析
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_account_insights_overview_api_v1_tiktok_creator_get_account_insights_overview_post`

### `POST /api/u1/v1/tiktok/creator/get_account_violation_list`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `page`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_account_violation_list_api_v1_tiktok_creator_get_account_violation_list_post`

### `POST /api/u1/v1/tiktok/creator/get_creator_account_info`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_creator_account_info_api_v1_tiktok_creator_get_creator_account_info_post`

### `POST /api/u1/v1/tiktok/creator/get_live_analytics_summary`

- 能力：创作者 / 数据分析 / 直播
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_live_overview_api_v1_tiktok_creator_get_live_analytics_summary_post`

### `POST /api/u1/v1/tiktok/creator/get_product_analytics_list`

- 能力：创作者 / 电商 / 数据分析
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `end_date`:string, `page`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_analytics_list_api_v1_tiktok_creator_get_product_analytics_list_post`

### `POST /api/u1/v1/tiktok/creator/get_product_related_videos`

- 能力：创作者 / 作品详情 / 电商
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_product_related_videos_api_v1_tiktok_creator_get_product_related_videos_post`

### `POST /api/u1/v1/tiktok/creator/get_showcase_product_list`

- 能力：创作者 / 电商
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `count`:integer, `offset`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_showcase_product_list_api_v1_tiktok_creator_get_showcase_product_list_post`

### `POST /api/u1/v1/tiktok/creator/get_video_analytics_summary`

- 能力：创作者 / 作品详情 / 数据分析
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_analytics_summary_api_v1_tiktok_creator_get_video_analytics_summary_post`

### `POST /api/u1/v1/tiktok/creator/get_video_associated_product_list`

- 能力：创作者 / 作品详情 / 电商
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_ids*`[string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_associated_product_list_api_v1_tiktok_creator_get_video_associated_product_list_post`

### `POST /api/u1/v1/tiktok/creator/get_video_audience_stats`

- 能力：创作者 / 作品详情
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_audience_stats_api_v1_tiktok_creator_get_video_audience_stats_post`

### `POST /api/u1/v1/tiktok/creator/get_video_detailed_stats`

- 能力：创作者 / 作品详情 / 详情
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_detailed_stats_api_v1_tiktok_creator_get_video_detailed_stats_post`

### `POST /api/u1/v1/tiktok/creator/get_video_list_analytics`

- 能力：创作者 / 作品详情 / 数据分析
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `page`:integer, `rules`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_list_api_v1_tiktok_creator_get_video_list_analytics_post`

### `POST /api/u1/v1/tiktok/creator/get_video_to_product_stats`

- 能力：创作者 / 作品详情 / 电商
- 入参：无
- 请求体：application/json: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_to_product_stats_api_v1_tiktok_creator_get_video_to_product_stats_post`
