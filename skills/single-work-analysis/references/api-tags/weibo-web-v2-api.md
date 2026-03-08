# Weibo-Web-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/weibo-web-v2-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`33`
- 常见能力：搜索 / 主页/账号 / 作品详情 / 通用能力 / 热点/榜单 / 评论
- 常见入参：`page`, `uid`, `query`, `id`, `max_id`, `count`, `since_id`, `q`, `keyword`, `cursor`
- 标签说明：**(新浪微博 Web V2 数据接口/Weibo-Web-V2-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/weibo/web_v2/check_allow_comment_with_pic`

- 能力：评论
- 入参：query: `id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_advanced_search`

- 能力：搜索
- 入参：query: `q*`, `search_type`, `include_type`, `timescope`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_ai_related_search`

- 能力：搜索
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_ai_search`

- 能力：搜索
- 入参：query: `query*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_all_groups`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_city_list`

- 能力：通用能力
- 入参：query: `normalized`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_entertainment_ranking`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_ranking_timeline`

- 能力：热点/榜单
- 入参：query: `ranking_type*`, `since_id`, `max_id`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_index`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_summary`

- 能力：搜索 / 热点/榜单
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_life_ranking`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_pic_search`

- 能力：搜索
- 入参：query: `query*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `id*`, `count`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_post_detail`

- 能力：作品详情 / 详情
- 入参：query: `id*`, `is_get_long_text`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_post_sub_comments`

- 能力：评论 / 作品详情
- 入参：query: `id*`, `count`, `max_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_realtime_search`

- 能力：搜索
- 入参：query: `query*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_similar_search`

- 能力：搜索
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_social_ranking`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_topic_search`

- 能力：搜索 / 话题
- 入参：query: `query*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_basic_info`

- 能力：主页/账号
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_fans`

- 能力：主页/账号
- 入参：query: `uid*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_following`

- 能力：主页/账号
- 入参：query: `uid*`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_info`

- 能力：主页/账号
- 入参：query: `uid`, `custom`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_original_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`, `page`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`, `page`, `feature`, `since_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_recommend_timeline`

- 能力：主页/账号
- 入参：query: `refresh`, `group_id`, `containerid`, `extparam`, `max_id`, `count`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_search`

- 能力：搜索 / 主页/账号
- 入参：query: `query`, `page`, `region`, `auth`, `gender`, `age`, `nickname`, `tag`, `school`, `work`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_detail`

- 能力：主页/账号 / 作品详情 / 详情
- 入参：query: `cid*`, `cursor`, `tab_code`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_list`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_list`

- 能力：主页/账号 / 作品详情
- 入参：query: `uid*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get`

### `GET /api/u1/v1/weibo/web_v2/fetch_video_search`

- 能力：搜索 / 作品详情
- 入参：query: `query*`, `mode`, `page`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get`

### `GET /api/u1/v1/weibo/web_v2/search_user_posts`

- 能力：搜索 / 主页/账号 / 作品详情
- 入参：query: `uid*`, `q*`, `page`, `starttime*`, `endtime*`, `hasori`, `hasret`, `hastext`, `haspic`, `hasvideo`, `hasmusic`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`
