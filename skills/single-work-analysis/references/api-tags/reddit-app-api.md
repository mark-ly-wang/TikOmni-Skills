# Reddit-APP-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/reddit-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`24`
- 常见能力：通用能力 / 主页/账号 / 作品详情 / 评论 / 搜索 / 详情
- 常见入参：`need_format`, `after`, `sort`, `username`, `subreddit_name`, `subreddit_id`, `post_id`, `filter_posts`, `include_comment_id`, `comment_id`
- 标签说明：**(Reddit APP数据接口/Reddit-APP-API endpoints)**

## 路由列表

### `GET /api/u1/v1/reddit/app/check_subreddit_muted`

- 能力：通用能力
- 入参：query: `subreddit_id*`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get`

### `GET /api/u1/v1/reddit/app/fetch_comment_replies`

- 能力：评论
- 入参：query: `post_id*`, `cursor*`, `sort_type`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get`

### `GET /api/u1/v1/reddit/app/fetch_community_highlights`

- 能力：通用能力
- 入参：query: `subreddit_id*`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get`

### `GET /api/u1/v1/reddit/app/fetch_dynamic_search`

- 能力：搜索
- 入参：query: `query*`, `search_type`, `sort`, `time_range`, `safe_search`, `allow_nsfw`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get`

### `GET /api/u1/v1/reddit/app/fetch_games_feed`

- 能力：通用能力
- 入参：query: `sort`, `time`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get`

### `GET /api/u1/v1/reddit/app/fetch_home_feed`

- 能力：主页/账号
- 入参：query: `sort`, `filter_posts`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get`

### `GET /api/u1/v1/reddit/app/fetch_news_feed`

- 能力：通用能力
- 入参：query: `subtopic_ids`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get`

### `GET /api/u1/v1/reddit/app/fetch_popular_feed`

- 能力：通用能力
- 入参：query: `sort`, `time`, `filter_posts`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get`

### `GET /api/u1/v1/reddit/app/fetch_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `post_id*`, `sort_type`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get`

### `GET /api/u1/v1/reddit/app/fetch_post_details`

- 能力：作品详情 / 详情
- 入参：query: `post_id*`, `include_comment_id`, `comment_id`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_details_api_v1_reddit_app_fetch_post_details_get`

### `GET /api/u1/v1/reddit/app/fetch_post_details_batch`

- 能力：作品详情 / 详情
- 入参：query: `post_ids*`, `include_comment_id`, `comment_id`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get`

### `GET /api/u1/v1/reddit/app/fetch_post_details_batch_large`

- 能力：作品详情 / 详情
- 入参：query: `post_ids*`, `include_comment_id`, `comment_id`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get`

### `GET /api/u1/v1/reddit/app/fetch_search_typeahead`

- 能力：搜索
- 入参：query: `query*`, `safe_search`, `allow_nsfw`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get`

### `GET /api/u1/v1/reddit/app/fetch_subreddit_feed`

- 能力：通用能力
- 入参：query: `subreddit_name*`, `sort`, `filter_posts`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get`

### `GET /api/u1/v1/reddit/app/fetch_subreddit_info`

- 能力：通用能力
- 入参：query: `subreddit_name`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get`

### `GET /api/u1/v1/reddit/app/fetch_subreddit_post_channels`

- 能力：主页/账号 / 作品详情
- 入参：query: `subreddit_name`, `sort`, `range`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get`

### `GET /api/u1/v1/reddit/app/fetch_subreddit_settings`

- 能力：通用能力
- 入参：query: `subreddit_id*`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get`

### `GET /api/u1/v1/reddit/app/fetch_subreddit_style`

- 能力：通用能力
- 入参：query: `subreddit_name`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get`

### `GET /api/u1/v1/reddit/app/fetch_trending_searches`

- 能力：搜索 / 热点/榜单
- 入参：query: `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get`

### `GET /api/u1/v1/reddit/app/fetch_user_active_subreddits`

- 能力：主页/账号
- 入参：query: `username*`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get`

### `GET /api/u1/v1/reddit/app/fetch_user_comments`

- 能力：评论 / 主页/账号
- 入参：query: `username*`, `sort`, `page_size`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get`

### `GET /api/u1/v1/reddit/app/fetch_user_posts`

- 能力：主页/账号 / 作品详情
- 入参：query: `username*`, `sort`, `after`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get`

### `GET /api/u1/v1/reddit/app/fetch_user_profile`

- 能力：主页/账号
- 入参：query: `username*`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get`

### `GET /api/u1/v1/reddit/app/fetch_user_trophies`

- 能力：主页/账号
- 入参：query: `username*`, `need_format`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get`
