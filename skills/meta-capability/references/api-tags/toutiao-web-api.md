# Toutiao-Web-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/toutiao-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`2`
- 常见能力：作品详情
- 常见入参：`aweme_id`
- 标签说明：**(今日头条Web数据接口/Toutiao-Web-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/toutiao/web/get_article_info`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_article_info_api_v1_toutiao_web_get_article_info_get`

### `GET /api/u1/v1/toutiao/web/get_video_info`

- 能力：作品详情
- 入参：query: `aweme_id*`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`get_video_info_api_v1_toutiao_web_get_video_info_get`
