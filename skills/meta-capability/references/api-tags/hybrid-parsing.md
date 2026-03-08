# Hybrid-Parsing 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/hybrid-parsing.md`
- 完整契约：[`api-contracts/hybrid-parsing.md`](../api-contracts/hybrid-parsing.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`1`
- 常见能力：作品详情
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`url`, `minimal`, `base64_url`
- 标签说明：**(混合解析单个视频接口/Hybrid-Parsing endpoints)**

## 路由列表

### `GET /api/u1/v1/hybrid/video_data`

- 摘要：混合解析单一视频接口/Hybrid parsing single video endpoint
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`hybrid_parsing_single_video_api_v1_hybrid_video_data_get`
- 完整契约：[`api-contracts/hybrid-parsing.md#get-api-u1-v1-hybrid-video-data`](../api-contracts/hybrid-parsing.md#get-api-u1-v1-hybrid-video-data)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | query | string | 是 | 无 |
| minimal | query | boolean | 否 | 是否返回最小数据/Whether to return minimal data |
| base64_url | query | boolean | 否 | 是否Base64编码提交URL/Base64 encoding URL |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | 否 | Support message \| 支持消息 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL |

- 字段已截断：当前层仅展示前 `12` 行。
