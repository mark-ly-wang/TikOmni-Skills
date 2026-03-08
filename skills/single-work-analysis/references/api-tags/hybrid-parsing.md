# Hybrid-Parsing 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/hybrid-parsing.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T03:50:06+00:00`
- 路由数：`1`
- 常见能力：作品详情
- 常见入参：`url`, `minimal`, `base64_url`
- 标签说明：**(混合解析单个视频接口/Hybrid-Parsing endpoints)**

## 路由列表

### `GET /api/u1/v1/hybrid/video_data`

- 能力：作品详情
- 入参：query: `url*`, `minimal`, `base64_url`
- 请求体：无
- 成功响应：200 application/json: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...
- operationId：`hybrid_parsing_single_video_api_v1_hybrid_video_data_get`
