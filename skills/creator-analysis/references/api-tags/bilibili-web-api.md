# Bilibili-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/bilibili-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`30`
- 常见能力：作品详情 / 主页/账号 / 直播 / 详情 / 通用能力 / 评论
- 常见入参：`bv_id`, `uid`, `pn`, `cid`, `dynamic_id`, `order`, `room_id`, `a_id`, `c_id`, `url`
- 标签说明：**(哔哩哔哩Web数据接口/Bilibili-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/bilibili/web/bv_to_aid`

- 能力：通用能力
- 入参：query: `bv_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_bilibili_web_bv_to_aid_get`

### `GET /api/u1/v1/bilibili/web/fetch_all_live_areas`

- 能力：直播
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_all_live_areas_get`

### `GET /api/u1/v1/bilibili/web/fetch_collect_folders`

- 能力：通用能力
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_collect_folders_get`

### `GET /api/u1/v1/bilibili/web/fetch_com_popular`

- 能力：通用能力
- 入参：query: `pn`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_com_popular_get`

### `GET /api/u1/v1/bilibili/web/fetch_comment_reply`

- 能力：评论 / 评论回复
- 入参：query: `bv_id*`, `pn`, `rpid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_comment_reply_get`

### `GET /api/u1/v1/bilibili/web/fetch_dynamic_detail`

- 能力：详情
- 入参：query: `dynamic_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_dynamic_detail_api_v1_bilibili_web_fetch_dynamic_detail_get`

### `GET /api/u1/v1/bilibili/web/fetch_dynamic_detail_v2`

- 能力：详情
- 入参：query: `dynamic_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_dynamic_detail_v2_api_v1_bilibili_web_fetch_dynamic_detail_v2_get`

### `GET /api/u1/v1/bilibili/web/fetch_general_search`

- 能力：搜索
- 入参：query: `keyword*`, `order*`, `page*`, `page_size*`, `duration`, `pubtime_begin_s`, `pubtime_end_s`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_general_search_api_v1_bilibili_web_fetch_general_search_get`

### `GET /api/u1/v1/bilibili/web/fetch_get_user_id`

- 能力：主页/账号
- 入参：query: `share_link*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_get_user_id_api_v1_bilibili_web_fetch_get_user_id_get`

### `GET /api/u1/v1/bilibili/web/fetch_hot_search`

- 能力：搜索 / 热点/榜单
- 入参：query: `limit*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_api_v1_bilibili_web_fetch_hot_search_get`

### `GET /api/u1/v1/bilibili/web/fetch_live_room_detail`

- 能力：详情 / 直播
- 入参：query: `room_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_live_room_detail_get`

### `GET /api/u1/v1/bilibili/web/fetch_live_streamers`

- 能力：直播
- 入参：query: `area_id*`, `pn`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_live_streamers_get`

### `GET /api/u1/v1/bilibili/web/fetch_live_videos`

- 能力：作品详情 / 直播
- 入参：query: `room_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_live_videos_get`

### `GET /api/u1/v1/bilibili/web/fetch_one_video`

- 能力：作品详情
- 入参：query: `bv_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_bilibili_web_fetch_one_video_get`

### `GET /api/u1/v1/bilibili/web/fetch_one_video_v2`

- 能力：作品详情
- 入参：query: `a_id*`, `c_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v2_api_v1_bilibili_web_fetch_one_video_v2_get`

### `GET /api/u1/v1/bilibili/web/fetch_one_video_v3`

- 能力：作品详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_v3_api_v1_bilibili_web_fetch_one_video_v3_get`

### `GET /api/u1/v1/bilibili/web/fetch_user_collection_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `folder_id*`, `pn`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_collection_videos_api_v1_bilibili_web_fetch_user_collection_videos_get`

### `GET /api/u1/v1/bilibili/web/fetch_user_dynamic`

- 能力：主页/账号
- 入参：query: `uid*`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_user_dynamic_get`

### `GET /api/u1/v1/bilibili/web/fetch_user_post_videos`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`, `pn`, `order`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_videos_api_v1_bilibili_web_fetch_user_post_videos_get`

### `GET /api/u1/v1/bilibili/web/fetch_user_profile`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_user_profile_get`

### `GET /api/u1/v1/bilibili/web/fetch_user_relation_stat`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_relation_stat_api_v1_bilibili_web_fetch_user_relation_stat_get`

### `GET /api/u1/v1/bilibili/web/fetch_user_up_stat`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_up_stat_api_v1_bilibili_web_fetch_user_up_stat_get`

### `GET /api/u1/v1/bilibili/web/fetch_video_comments`

- 能力：评论 / 作品详情
- 入参：query: `bv_id*`, `pn`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_collect_folders_api_v1_bilibili_web_fetch_video_comments_get`

### `GET /api/u1/v1/bilibili/web/fetch_video_danmaku`

- 能力：作品详情
- 入参：query: `cid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_bilibili_web_fetch_video_danmaku_get`

### `GET /api/u1/v1/bilibili/web/fetch_video_detail`

- 能力：作品详情 / 详情
- 入参：query: `aid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_detail_api_v1_bilibili_web_fetch_video_detail_get`

### `GET /api/u1/v1/bilibili/web/fetch_video_parts`

- 能力：作品详情
- 入参：query: `bv_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_bilibili_web_fetch_video_parts_get`

### `GET /api/u1/v1/bilibili/web/fetch_video_play_info`

- 能力：作品详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_play_info_api_v1_bilibili_web_fetch_video_play_info_get`

### `GET /api/u1/v1/bilibili/web/fetch_video_playurl`

- 能力：作品详情
- 入参：query: `bv_id*`, `cid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_one_video_api_v1_bilibili_web_fetch_video_playurl_get`

### `GET /api/u1/v1/bilibili/web/fetch_video_subtitle`

- 能力：字幕/转写 / 作品详情
- 入参：query: `a_id*`, `c_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_subtitle_api_v1_bilibili_web_fetch_video_subtitle_get`

### `POST /api/u1/v1/bilibili/web/fetch_vip_video_playurl`

- 能力：作品详情
- 入参：无
- 请求体：application/json: `bv_id*`:string, `cid*`:string, `cookie*`:string
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_vip_video_playurl_api_v1_bilibili_web_fetch_vip_video_playurl_post`
