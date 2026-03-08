# YouTube-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/youtube-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`21`
- 常见能力：作品详情 / 主页/账号 / 搜索 / 评论 / 热点/榜单 / 字幕/转写
- 常见入参：`continuation_token`, `language_code`, `country_code`, `channel_id`, `video_id`, `need_format`, `search_query`, `sort_by`, `lang`, `time_zone`
- 标签说明：**(YouTube Web数据接口/YouTube-Web-API endpoints)**

## 路由列表

### `GET /api/u1/v1/youtube/web/get_channel_description`

- 能力：主页/账号
- 入参：query: `channel_id`, `continuation_token`, `language_code`, `country_code`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_description_api_v1_youtube_web_get_channel_description_get`

### `GET /api/u1/v1/youtube/web/get_channel_id`

- 能力：主页/账号
- 入参：query: `channel_name*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_id_api_v1_youtube_web_get_channel_id_get`

### `GET /api/u1/v1/youtube/web/get_channel_id_v2`

- 能力：主页/账号
- 入参：query: `channel_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_id_v2_api_v1_youtube_web_get_channel_id_v2_get`

### `GET /api/u1/v1/youtube/web/get_channel_info`

- 能力：主页/账号
- 入参：query: `channel_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_info_api_v1_youtube_web_get_channel_info_get`

### `GET /api/u1/v1/youtube/web/get_channel_short_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `channel_id*`, `continuation_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_short_videos_api_v1_youtube_web_get_channel_short_videos_get`

### `GET /api/u1/v1/youtube/web/get_channel_url`

- 能力：主页/账号
- 入参：query: `channel_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_url_api_v1_youtube_web_get_channel_url_get`

### `GET /api/u1/v1/youtube/web/get_channel_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `channel_id*`, `continuation_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_videos_api_v1_youtube_web_get_channel_videos_get`

### `GET /api/u1/v1/youtube/web/get_channel_videos_v2`

- 能力：主页/账号 / 作品详情
- 入参：query: `channel_id*`, `lang`, `sortBy`, `contentType`, `nextToken`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_videos_v2_api_v1_youtube_web_get_channel_videos_v2_get`

### `GET /api/u1/v1/youtube/web/get_channel_videos_v3`

- 能力：主页/账号 / 作品详情
- 入参：query: `channel_id*`, `language_code`, `country_code`, `continuation_token`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_channel_videos_v3_api_v1_youtube_web_get_channel_videos_v3_get`

### `GET /api/u1/v1/youtube/web/get_general_search`

- 能力：搜索
- 入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `duration`, `content_type`, `feature`, `sort_by`, `continuation_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_general_search_api_v1_youtube_web_get_general_search_get`

### `GET /api/u1/v1/youtube/web/get_relate_video`

- 能力：作品详情
- 入参：query: `video_id*`, `continuation_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_relate_video_api_v1_youtube_web_get_relate_video_get`

### `GET /api/u1/v1/youtube/web/get_shorts_search`

- 能力：搜索
- 入参：query: `search_query*`, `language_code`, `country_code`, `time_zone`, `upload_time`, `sort_by`, `continuation_token`, `filter_mixed_content`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_shorts_search_api_v1_youtube_web_get_shorts_search_get`

### `GET /api/u1/v1/youtube/web/get_trending_videos`

- 能力：热点/榜单 / 作品详情
- 入参：query: `language_code`, `country_code`, `section`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_trending_videos_api_v1_youtube_web_get_trending_videos_get`

### `GET /api/u1/v1/youtube/web/get_video_comment_replies`

- 能力：评论 / 作品详情
- 入参：query: `continuation_token*`, `language_code`, `country_code`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_comment_replies_api_v1_youtube_web_get_video_comment_replies_get`

### `GET /api/u1/v1/youtube/web/get_video_comments`

- 能力：评论 / 作品详情
- 入参：query: `video_id*`, `language_code`, `country_code`, `sort_by`, `continuation_token`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_comments_api_v1_youtube_web_get_video_comments_get`

### `GET /api/u1/v1/youtube/web/get_video_info`

- 能力：作品详情
- 入参：query: `video_id*`, `url_access`, `lang`, `videos`, `audios`, `subtitles`, `related`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_info_api_v1_youtube_web_get_video_info_get`

### `GET /api/u1/v1/youtube/web/get_video_info_v2`

- 能力：作品详情
- 入参：query: `video_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_info_v2_api_v1_youtube_web_get_video_info_v2_get`

### `GET /api/u1/v1/youtube/web/get_video_info_v3`

- 能力：作品详情
- 入参：query: `video_id*`, `language_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_info_v3_api_v1_youtube_web_get_video_info_v3_get`

### `GET /api/u1/v1/youtube/web/get_video_subtitles`

- 能力：字幕/转写 / 作品详情
- 入参：query: `subtitle_url*`, `format`, `fix_overlap`, `target_lang`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`api_get_video_subtitles_api_v1_youtube_web_get_video_subtitles_get`

### `GET /api/u1/v1/youtube/web/search_channel`

- 能力：搜索 / 主页/账号
- 入参：query: `channel_id*`, `search_query*`, `language_code`, `country_code`, `continuation_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_channel_api_v1_youtube_web_search_channel_get`

### `GET /api/u1/v1/youtube/web/search_video`

- 能力：搜索 / 作品详情
- 入参：query: `search_query*`, `language_code`, `order_by`, `country_code`, `continuation_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_video_api_v1_youtube_web_search_video_get`
