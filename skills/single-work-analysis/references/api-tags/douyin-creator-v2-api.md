# Douyin-Creator-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-creator-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`14`
- 常见能力：创作者 / 下载/媒体 / 搜索 / 热点/榜单 / 直播
- 常见入参：`cookie`, `item_id`, `start_date`, `end_date`, `genres`, `primary_verticals`, `fields`, `need_long_article`, `metric_type`, `count`
- 标签说明：**(抖音创作者V2数据接口（需要用户Cookie，可获取作品流量总览等数据）/Douyin-Creator-V2-API data endpoints (Requires user Cookie, can get item traffic overview data))**

## 路由列表

### `POST /api/u1/v1/douyin/creator_v2/fetch_author_diagnosis`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_author_diagnosis_api_v1_douyin_creator_v2_fetch_author_diagnosis_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_analysis_involved_vertical_api_v1_douyin_creator_v2_fetch_item_analysis_involved_vertical_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_item_performance`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string], `metric_type`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_analysis_item_performance_api_v1_douyin_creator_v2_fetch_item_analysis_item_performance_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_overview`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string]
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_analysis_overview_api_v1_douyin_creator_v2_fetch_item_analysis_overview_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_others`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `item_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_audience_others_api_v1_douyin_creator_v2_fetch_item_audience_others_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_portrait`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `item_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_audience_portrait_api_v1_douyin_creator_v2_fetch_item_audience_portrait_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_danmaku_analysis`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `item_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_danmaku_analysis_api_v1_douyin_creator_v2_fetch_item_danmaku_analysis_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `count`:integer, `order_by`:integer, `fields`:string, `need_cooperation`:boolean, `start_time*`:integer, `end_time*`:integer, `need_long_article`:boolean, ...
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_list_api_v1_douyin_creator_v2_fetch_item_list_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list_download`

- 能力：创作者 / 下载/媒体
- 入参：无
- 请求体：application/json: `cookie*`:string, `min_cursor*`:integer, `max_cursor*`:integer, `type_filters`[integer], `need_long_article`:boolean
- 成功响应：200 application/json: 无结构声明
- operationId：`fetch_item_list_download_api_v1_douyin_creator_v2_fetch_item_list_download_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_overview_data`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `ids*`:string, `fields`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_overview_data_api_v1_douyin_creator_v2_fetch_item_overview_data_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_play_source`

- 能力：创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `item_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_play_source_api_v1_douyin_creator_v2_fetch_item_play_source_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_search_keyword`

- 能力：搜索 / 创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `item_id*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_search_keyword_api_v1_douyin_creator_v2_fetch_item_search_keyword_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_watch_trend`

- 能力：热点/榜单 / 创作者
- 入参：无
- 请求体：application/json: `cookie*`:string, `item_id*`:string, `analysis_type`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_item_watch_trend_api_v1_douyin_creator_v2_fetch_item_watch_trend_post`

### `POST /api/u1/v1/douyin/creator_v2/fetch_live_room_history_list`

- 能力：创作者 / 直播
- 入参：无
- 请求体：application/json: `cookie*`:string, `start_date*`:string, `end_date*`:string, `limit`:integer, `need_living`:integer, `download`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_room_history_list_api_v1_douyin_creator_v2_fetch_live_room_history_list_post`
