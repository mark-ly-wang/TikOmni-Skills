# Douyin-Search-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-search-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`20`
- 常见能力：搜索 / 话题 / 主页/账号 / 作品详情 / 直播 / 音乐/音频
- 常见入参：`keyword`, `cursor`, `search_id`, `sort_type`, `publish_time`, `filter_duration`, `content_type`, `backtrace`, `douyin_user_fans`, `douyin_user_type`
- 标签说明：**(抖音搜索数据接口（当前最新版，请优先使用此目录下的接口而不是其他目录下的搜索接口）/Douyin-Search-API data endpoints (Current latest version, please use the interfaces in this directory first instead of the search interfaces in other directories))**

## 路由列表

### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v1`

- 能力：搜索 / 话题
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_challenge_search_v1_api_v1_douyin_search_fetch_challenge_search_v1_post`

### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v2`

- 能力：搜索 / 话题
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_challenge_search_v2_api_v1_douyin_search_fetch_challenge_search_v2_post`

### `POST /api/u1/v1/douyin/search/fetch_challenge_suggest`

- 能力：搜索 / 话题
- 入参：无
- 请求体：application/json: `keyword`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_challenge_suggest_api_v1_douyin_search_fetch_challenge_suggest_post`

### `POST /api/u1/v1/douyin/search/fetch_discuss_search`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_discuss_search_api_v1_douyin_search_fetch_discuss_search_post`

### `POST /api/u1/v1/douyin/search/fetch_experience_search`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_experience_search_api_v1_douyin_search_fetch_experience_search_post`

### `POST /api/u1/v1/douyin/search/fetch_general_search_v1`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_v1_api_v1_douyin_search_fetch_general_search_v1_post`

### `POST /api/u1/v1/douyin/search/fetch_general_search_v2`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_v2_api_v1_douyin_search_fetch_general_search_v2_post`

### `POST /api/u1/v1/douyin/search/fetch_general_search_v3`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_v3_api_v1_douyin_search_fetch_general_search_v3_post`

### `POST /api/u1/v1/douyin/search/fetch_image_search`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_image_search_api_v1_douyin_search_fetch_image_search_post`

### `POST /api/u1/v1/douyin/search/fetch_image_search_v3`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword*`:string, `cursor`:integer, `search_id`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_image_search_v3_api_v1_douyin_search_fetch_image_search_v3_post`

### `POST /api/u1/v1/douyin/search/fetch_live_search_v1`

- 能力：搜索 / 直播
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_live_search_v1_api_v1_douyin_search_fetch_live_search_v1_post`

### `POST /api/u1/v1/douyin/search/fetch_multi_search`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_multi_search_api_v1_douyin_search_fetch_multi_search_post`

### `POST /api/u1/v1/douyin/search/fetch_music_search`

- 能力：搜索 / 音乐/音频
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_music_search_api_v1_douyin_search_fetch_music_search_post`

### `POST /api/u1/v1/douyin/search/fetch_school_search`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_school_search_api_v1_douyin_search_fetch_school_search_post`

### `POST /api/u1/v1/douyin/search/fetch_search_suggest`

- 能力：搜索
- 入参：无
- 请求体：application/json: `keyword`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_suggest_api_v1_douyin_search_fetch_search_suggest_post`

### `POST /api/u1/v1/douyin/search/fetch_user_search`

- 能力：搜索 / 主页/账号
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `douyin_user_fans`:string, `douyin_user_type`:string, `search_id`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_api_v1_douyin_search_fetch_user_search_post`

### `POST /api/u1/v1/douyin/search/fetch_user_search_v2`

- 能力：搜索 / 主页/账号
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_v2_api_v1_douyin_search_fetch_user_search_v2_post`

### `POST /api/u1/v1/douyin/search/fetch_video_search_v1`

- 能力：搜索 / 作品详情
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_v1_api_v1_douyin_search_fetch_video_search_v1_post`

### `POST /api/u1/v1/douyin/search/fetch_video_search_v2`

- 能力：搜索 / 作品详情
- 入参：无
- 请求体：application/json: `keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_v2_api_v1_douyin_search_fetch_video_search_v2_post`

### `POST /api/u1/v1/douyin/search/fetch_vision_search`

- 能力：搜索
- 入参：无
- 请求体：application/json: `image_uri*`:string, `cursor`:integer, `search_id`:string, `search_source`:string, `detection`:string, `detection_index`:integer, `user_query`:string, `aweme_id`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_vision_search_api_v1_douyin_search_fetch_vision_search_post`
