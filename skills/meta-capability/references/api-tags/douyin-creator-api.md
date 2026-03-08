# Douyin-Creator-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-creator-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`16`
- 常见能力：创作者 / 热点/榜单 / 话题 / 详情 / 音乐/音频 / 搜索
- 常见入参：`billboard_tag`, `order_key`, `time_filter`, `limit`, `offset`, `category_id`, `order`, `activity_id`, `start_time`, `end_time`
- 标签说明：**(抖音创作者数据接口/Douyin-Creator-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_detail`

- 能力：创作者 / 详情
- 入参：query: `activity_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_activity_detail_api_v1_douyin_creator_fetch_creator_activity_detail_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_activity_list`

- 能力：创作者
- 入参：query: `start_time*`, `end_time*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_activity_list_api_v1_douyin_creator_fetch_creator_activity_list_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_content_category`

- 能力：创作者
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_content_category_api_v1_douyin_creator_fetch_creator_content_category_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_content_course`

- 能力：创作者
- 入参：query: `category_id*`, `order`, `limit`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_content_course_api_v1_douyin_creator_fetch_creator_content_course_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_challenge_billboard`

- 能力：热点/榜单 / 创作者 / 话题
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_hot_challenge_billboard_api_v1_douyin_creator_fetch_creator_hot_challenge_billboard_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_course`

- 能力：热点/榜单 / 创作者
- 入参：query: `order`, `limit`, `offset`, `category_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_hot_course_api_v1_douyin_creator_fetch_creator_hot_course_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_music_billboard`

- 能力：热点/榜单 / 创作者 / 音乐/音频
- 入参：query: `billboard_tag`, `order_key`, `time_filter`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_hot_music_billboard_api_v1_douyin_creator_fetch_creator_hot_music_billboard_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_props_billboard`

- 能力：热点/榜单 / 创作者
- 入参：query: `billboard_tag`, `order_key`, `time_filter`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_hot_props_billboard_api_v1_douyin_creator_fetch_creator_hot_props_billboard_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_spot_billboard`

- 能力：热点/榜单 / 创作者
- 入参：query: `billboard_tag`, `hot_search_type`, `city_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_hot_spot_billboard_api_v1_douyin_creator_fetch_creator_hot_spot_billboard_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_hot_topic_billboard`

- 能力：热点/榜单 / 创作者 / 话题
- 入参：query: `billboard_tag`, `order_key`, `time_filter`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_hot_topic_billboard_api_v1_douyin_creator_fetch_creator_hot_topic_billboard_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_billboard`

- 能力：热点/榜单 / 创作者
- 入参：query: `billboard_tag`, `order_key`, `time_filter`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_material_center_billboard_api_v1_douyin_creator_fetch_creator_material_center_billboard_get`

### `GET /api/u1/v1/douyin/creator/fetch_creator_material_center_config`

- 能力：创作者
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_creator_material_center_config_api_v1_douyin_creator_fetch_creator_material_center_config_get`

### `GET /api/u1/v1/douyin/creator/fetch_industry_category_config`

- 能力：创作者
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_industry_category_config_api_v1_douyin_creator_fetch_industry_category_config_get`

### `GET /api/u1/v1/douyin/creator/fetch_mission_task_list`

- 能力：创作者
- 入参：query: `cursor`, `limit`, `mission_type`, `tab_scene`, `industry_lv1`, `industry_lv2`, `platform_channel`, `pay_type`, `greater_than_cost_progress`, `publish_time_start`, `quick_selector_scene`, `keyword`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mission_task_list_api_v1_douyin_creator_fetch_mission_task_list_get`

### `GET /api/u1/v1/douyin/creator/fetch_user_search`

- 能力：搜索 / 创作者 / 主页/账号
- 入参：query: `user_name*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_api_v1_douyin_creator_fetch_user_search_get`

### `GET /api/u1/v1/douyin/creator/fetch_video_danmaku_list`

- 能力：创作者 / 作品详情
- 入参：query: `item_id*`, `count`, `offset`, `order_type`, `is_blocked`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_danmaku_list_api_v1_douyin_creator_fetch_video_danmaku_list_get`
