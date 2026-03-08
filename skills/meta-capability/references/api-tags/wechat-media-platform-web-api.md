# WeChat-Media-Platform-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/wechat-media-platform-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`10`
- 常见能力：作品详情 / 评论 / 详情 / 评论回复
- 常见入参：`url`, `comment_id`, `offset`, `buffer`, `content_id`, `ghid`, `sogou_url`
- 标签说明：**(微信公众号Web数据接口/WeChat-Media-Platform-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_ad`

- 能力：作品详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_ad_api_v1_wechat_mp_web_fetch_mp_article_ad_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_list`

- 能力：评论 / 作品详情
- 入参：query: `url*`, `comment_id`, `buffer`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_comment_list_api_v1_wechat_mp_web_fetch_mp_article_comment_list_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_comment_reply_list`

- 能力：评论 / 评论回复 / 作品详情
- 入参：query: `url`, `comment_id*`, `content_id*`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_comment_reply_list_api_v1_wechat_mp_web_fetch_mp_article_comment_reply_list_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_html`

- 能力：作品详情 / 详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_detail_html_api_v1_wechat_mp_web_fetch_mp_article_detail_html_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_detail_json`

- 能力：作品详情 / 详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_detail_json_api_v1_wechat_mp_web_fetch_mp_article_detail_json_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_list`

- 能力：作品详情
- 入参：query: `ghid*`, `offset`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_list_api_v1_wechat_mp_web_fetch_mp_article_list_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_read_count`

- 能力：作品详情
- 入参：query: `url*`, `comment_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_read_count_api_v1_wechat_mp_web_fetch_mp_article_read_count_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url`

- 能力：作品详情
- 入参：query: `sogou_url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_url_api_v1_wechat_mp_web_fetch_mp_article_url_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_article_url_conversion`

- 能力：作品详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_article_url_conversion_api_v1_wechat_mp_web_fetch_mp_article_url_conversion_get`

### `GET /api/u1/v1/wechat_mp/web/fetch_mp_related_articles`

- 能力：作品详情
- 入参：query: `url*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`fetch_mp_related_articles_api_v1_wechat_mp_web_fetch_mp_related_articles_get`
