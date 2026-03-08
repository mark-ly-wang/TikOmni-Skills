# YouTube-Web-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/youtube-web-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`16`
- 常见能力：作品详情 / 主页/账号 / 搜索 / 直播 / 评论
- 常见入参：`continuation_token`, `need_format`, `language_code`, `country_code`, `video_id`, `channel_id`, `video_url`, `sort_by`, `channel_url`, `search_query`
- 标签说明：**(YouTube Web V2数据接口/YouTube-Web-V2-API endpoints)**

## 路由列表

### `GET /api/u1/v1/youtube/web_v2/get_channel_description`

- 能力：主页/账号
- 入参：query: `channel_id`, `continuation_token`, `language_code`, `country_code`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_description_api_v1_youtube_web_v2_get_channel_description_get`

### `GET /api/u1/v1/youtube/web_v2/get_channel_id`

- 能力：主页/账号
- 入参：query: `channel_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_id_api_v1_youtube_web_v2_get_channel_id_get`

### `GET /api/u1/v1/youtube/web_v2/get_channel_shorts`

- 能力：主页/账号
- 入参：query: `channel_id`, `channel_url`, `continuation_token`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_shorts_api_v1_youtube_web_v2_get_channel_shorts_get`

### `GET /api/u1/v1/youtube/web_v2/get_channel_url`

- 能力：主页/账号
- 入参：query: `channel_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_url_api_v1_youtube_web_v2_get_channel_url_get`

### `GET /api/u1/v1/youtube/web_v2/get_channel_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `channel_id*`, `language_code`, `country_code`, `continuation_token`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_videos_api_v1_youtube_web_v2_get_channel_videos_get`

### `GET /api/u1/v1/youtube/web_v2/get_general_search`

- 能力：搜索
- 入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `duration`, `content_type`, `feature`, `sort_by`, `continuation_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_general_search_api_v1_youtube_web_v2_get_general_search_get`

### `GET /api/u1/v1/youtube/web_v2/get_related_videos`

- 能力：作品详情
- 入参：query: `video_id`, `video_url`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_related_videos_api_v1_youtube_web_v2_get_related_videos_get`

### `GET /api/u1/v1/youtube/web_v2/get_search_suggestions`

- 能力：搜索
- 入参：query: `keyword*`, `language`, `region`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_search_suggestions_api_v1_youtube_web_v2_get_search_suggestions_get`

### `GET /api/u1/v1/youtube/web_v2/get_shorts_search`

- 能力：搜索
- 入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `sort_by`, `continuation_token`, `filter_mixed_content`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_shorts_search_api_v1_youtube_web_v2_get_shorts_search_get`

### `GET /api/u1/v1/youtube/web_v2/get_signed_stream_url`

- 能力：直播
- 入参：query: `video_id`, `video_url`, `itag*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_signed_stream_url_api_v1_youtube_web_v2_get_signed_stream_url_get`

### `GET /api/u1/v1/youtube/web_v2/get_video_comment_replies`

- 能力：评论 / 作品详情
- 入参：query: `continuation_token*`, `language_code`, `country_code`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_comment_replies_api_v1_youtube_web_v2_get_video_comment_replies_get`

### `GET /api/u1/v1/youtube/web_v2/get_video_comments`

- 能力：评论 / 作品详情
- 入参：query: `video_id*`, `language_code`, `country_code`, `sort_by`, `continuation_token`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_comments_api_v1_youtube_web_v2_get_video_comments_get`

### `GET /api/u1/v1/youtube/web_v2/get_video_info`

- 能力：作品详情
- 入参：query: `video_id*`, `language_code`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_info_api_v1_youtube_web_v2_get_video_info_get`

### `GET /api/u1/v1/youtube/web_v2/get_video_streams`

- 能力：作品详情 / 直播
- 入参：query: `video_id`, `video_url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_streams_api_v1_youtube_web_v2_get_video_streams_get`

### `GET /api/u1/v1/youtube/web_v2/get_video_streams_v2`

- 能力：作品详情 / 直播
- 入参：query: `video_id`, `video_url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_streams_v2_api_v1_youtube_web_v2_get_video_streams_v2_get`

### `GET /api/u1/v1/youtube/web_v2/search_channels`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword`, `continuation_token`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_channels_api_v1_youtube_web_v2_search_channels_get`
