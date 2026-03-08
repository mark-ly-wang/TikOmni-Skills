# Twitter-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/twitter-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`13`
- 常见能力：主页/账号 / 作品详情 / 评论 / 搜索 / 热点/榜单 / 详情
- 常见入参：`cursor`, `screen_name`, `tweet_id`, `rest_id`, `keyword`, `search_type`, `country`, `userId`, `count`
- 标签说明：**(Twitter Web数据接口/Twitter-Web-API endpoints)**

## 路由列表

### `GET /api/u1/v1/twitter/web/fetch_latest_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `tweet_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get`

### `GET /api/u1/v1/twitter/web/fetch_post_comments`

- 能力：评论 / 作品详情
- 入参：query: `tweet_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get`

### `GET /api/u1/v1/twitter/web/fetch_retweet_user_list`

- 能力：主页/账号
- 入参：query: `tweet_id*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get`

### `GET /api/u1/v1/twitter/web/fetch_search_timeline`

- 能力：搜索
- 入参：query: `keyword*`, `search_type`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get`

### `GET /api/u1/v1/twitter/web/fetch_trending`

- 能力：热点/榜单
- 入参：query: `country`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_trending_api_v1_twitter_web_fetch_trending_get`

### `GET /api/u1/v1/twitter/web/fetch_tweet_detail`

- 能力：详情
- 入参：query: `tweet_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get`

### `GET /api/u1/v1/twitter/web/fetch_user_followers`

- 能力：主页/账号
- 入参：query: `screen_name*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get`

### `GET /api/u1/v1/twitter/web/fetch_user_followings`

- 能力：主页/账号
- 入参：query: `screen_name*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get`

### `GET /api/u1/v1/twitter/web/fetch_user_highlights_tweets`

- 能力：主页/账号
- 入参：query: `userId*`, `count`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get`

### `GET /api/u1/v1/twitter/web/fetch_user_media`

- 能力：主页/账号 / 下载/媒体
- 入参：query: `screen_name*`, `rest_id`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_media_api_v1_twitter_web_fetch_user_media_get`

### `GET /api/u1/v1/twitter/web/fetch_user_post_tweet`

- 能力：主页/账号 / 作品详情
- 入参：query: `screen_name`, `rest_id`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get`

### `GET /api/u1/v1/twitter/web/fetch_user_profile`

- 能力：主页/账号
- 入参：query: `screen_name`, `rest_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get`

### `GET /api/u1/v1/twitter/web/fetch_user_tweet_replies`

- 能力：主页/账号
- 入参：query: `screen_name*`, `cursor`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get`
