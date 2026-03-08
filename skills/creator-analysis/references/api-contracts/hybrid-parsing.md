# Hybrid-Parsing Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/hybrid-parsing.md`](../api-tags/hybrid-parsing.md)
- Current contract file: `api-contracts/hybrid-parsing.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `1`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(混合解析单个视频接口/Hybrid-Parsing endpoints)**

## Route Contracts

<a id="get-api-u1-v1-hybrid-video-data"></a>
### `GET /api/u1/v1/hybrid/video_data`

- Summary: 混合解析单一视频接口/Hybrid parsing single video endpoint
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `hybrid_parsing_single_video_api_v1_hybrid_video_data_get`

#### Notes

> # [中文]
> ### 用途:
> - 该接口用于解析抖音/TikTok单一视频的数据。
> ### 参数:
> - `url`: 视频链接、分享链接、分享文本。
> ### 返回:
> - `data`: 视频数据。
>
> # [English]
> ### Purpose:
> - This endpoint is used to parse data of a single Douyin/TikTok video.
> ### Parameters:
> - `url`: Video link, share link, or share text.
> ### Returns:
> - `data`: Video data.
>
> # [Example]
> url = "https://v.douyin.com/L4FJNR3/"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | None | None | https://v.douyin.com/L4FJNR3/ | None |
| minimal | query | boolean | No | 是否返回最小数据/Whether to return minimal data | false | None | None |
| base64_url | query | boolean | No | 是否Base64编码提交URL/Base64 encoding URL | false | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |
