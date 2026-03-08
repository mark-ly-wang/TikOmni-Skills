# Hybrid-Parsing Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/hybrid-parsing.md`
- Full contract: [`api-contracts/hybrid-parsing.md`](../api-contracts/hybrid-parsing.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `1`
- Common capabilities: content details
- Default auth: Header `Authorization` Bearer
- Common inputs: `url`, `minimal`, `base64_url`
- Tag description: **(混合解析单个视频接口/Hybrid-Parsing endpoints)**

## Routes

### `GET /api/u1/v1/hybrid/video_data`

- Summary: 混合解析单一视频接口/Hybrid parsing single video endpoint
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `hybrid_parsing_single_video_api_v1_hybrid_video_data_get`
- Full contract: [`api-contracts/hybrid-parsing.md#get-api-u1-v1-hybrid-video-data`](../api-contracts/hybrid-parsing.md#get-api-u1-v1-hybrid-video-data)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| url | query | string | Yes | None |
| minimal | query | boolean | No | 是否返回最小数据/Whether to return minimal data |
| base64_url | query | boolean | No | 是否Base64编码提交URL/Base64 encoding URL |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 |
| message | string | No | Response message (EN-US) \| 响应消息 (English) |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) |
| support | string | No | Support message \| 支持消息 |
| time | string | No | The time the response was generated \| 生成响应的时间 |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL |

- Fields truncated: this layer shows only the first `12` rows.
