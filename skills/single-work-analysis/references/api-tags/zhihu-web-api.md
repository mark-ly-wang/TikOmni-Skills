# Zhihu-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/zhihu-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`32`
- 常见能力：搜索 / 主页/账号 / 作品详情 / 通用能力 / 评论 / 热点/榜单
- 常见入参：`offset`, `limit`, `keyword`, `user_url_token`, `search_hash_id`, `article_id`, `order_by`, `message_content`, `message_id`, `show_all_topics`
- 标签说明：**(知乎Web数据接口/Zhihu-Web-API endpoints)**

## 路由列表

### `GET /api/u1/v1/zhihu/web/fetch_ai_search`

- 能力：搜索
- 入参：query: `message_content*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get`

### `GET /api/u1/v1/zhihu/web/fetch_ai_search_result`

- 能力：搜索
- 入参：query: `message_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get`

### `GET /api/u1/v1/zhihu/web/fetch_article_search_v3`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `offset`, `limit`, `show_all_topics`, `search_source`, `search_hash_id`, `vertical`, `sort`, `time_interval`, `vertical_info`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get`

### `GET /api/u1/v1/zhihu/web/fetch_column_article_detail`

- 能力：作品详情 / 详情
- 入参：query: `article_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get`

### `GET /api/u1/v1/zhihu/web/fetch_column_articles`

- 能力：作品详情
- 入参：query: `column_id*`, `limit`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get`

### `GET /api/u1/v1/zhihu/web/fetch_column_comment_config`

- 能力：评论
- 入参：query: `article_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get`

### `GET /api/u1/v1/zhihu/web/fetch_column_recommend`

- 能力：通用能力
- 入参：query: `article_id*`, `limit`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get`

### `GET /api/u1/v1/zhihu/web/fetch_column_relationship`

- 能力：通用能力
- 入参：query: `article_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get`

### `GET /api/u1/v1/zhihu/web/fetch_column_search_v3`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `limit`, `search_hash_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get`

### `GET /api/u1/v1/zhihu/web/fetch_comment_v5`

- 能力：评论
- 入参：query: `answer_id*`, `order_by`, `limit`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get`

### `GET /api/u1/v1/zhihu/web/fetch_ebook_search_v3`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `limit`, `search_hash_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get`

### `GET /api/u1/v1/zhihu/web/fetch_hot_list`

- 能力：热点/榜单
- 入参：query: `limit`, `desktop`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get`

### `GET /api/u1/v1/zhihu/web/fetch_hot_recommend`

- 能力：热点/榜单
- 入参：query: `offset`, `page_number`, `session_token`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get`

### `GET /api/u1/v1/zhihu/web/fetch_preset_search`

- 能力：搜索
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get`

### `GET /api/u1/v1/zhihu/web/fetch_question_answers`

- 能力：通用能力
- 入参：query: `question_id*`, `cursor`, `limit`, `offset`, `order`, `session_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get`

### `GET /api/u1/v1/zhihu/web/fetch_recommend_followees`

- 能力：通用能力
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get`

### `GET /api/u1/v1/zhihu/web/fetch_salt_search_v3`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `limit`, `search_hash_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get`

### `POST /api/u1/v1/zhihu/web/fetch_scholar_search_v3`

- 能力：搜索
- 入参：query: `keyword*`, `offset`, `limit`
- 请求体：application/json: 动态对象
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post`

### `GET /api/u1/v1/zhihu/web/fetch_search_recommend`

- 能力：搜索
- 入参：无
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get`

### `GET /api/u1/v1/zhihu/web/fetch_search_suggest`

- 能力：搜索
- 入参：query: `keyword*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get`

### `GET /api/u1/v1/zhihu/web/fetch_sub_comment_v5`

- 能力：评论
- 入参：query: `comment_id*`, `order_by`, `limit`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get`

### `GET /api/u1/v1/zhihu/web/fetch_topic_search_v3`

- 能力：搜索 / 话题
- 入参：query: `keyword*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_follow_collections`

- 能力：主页/账号
- 入参：query: `user_url_token*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_follow_columns`

- 能力：主页/账号
- 入参：query: `user_url_token*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_follow_questions`

- 能力：主页/账号
- 入参：query: `user_url_token*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_follow_topics`

- 能力：主页/账号 / 话题
- 入参：query: `user_url_token*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_followees`

- 能力：主页/账号
- 入参：query: `user_url_token*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_followers`

- 能力：主页/账号
- 入参：query: `user_url_token*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_info`

- 能力：主页/账号
- 入参：query: `user_url_token*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_info_api_v1_zhihu_web_fetch_user_info_get`

### `GET /api/u1/v1/zhihu/web/fetch_user_search_v3`

- 能力：搜索 / 主页/账号
- 入参：query: `keyword*`, `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get`

### `GET /api/u1/v1/zhihu/web/fetch_video_list`

- 能力：作品详情
- 入参：query: `offset`, `limit`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_list_api_v1_zhihu_web_fetch_video_list_get`

### `GET /api/u1/v1/zhihu/web/fetch_video_search_v3`

- 能力：搜索 / 作品详情
- 入参：query: `keyword*`, `limit`, `offset`, `search_hash_id`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get`
