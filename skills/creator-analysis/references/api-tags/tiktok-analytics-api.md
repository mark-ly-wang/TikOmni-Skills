# TikTok-Analytics-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tiktok-analytics-api.md`
- Full contract: [`api-contracts/tiktok-analytics-api.md`](../api-contracts/tiktok-analytics-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `4`
- Common capabilities: analytics / comments / creators / content details
- Default auth: Header `Authorization` Bearer
- Common inputs: `item_id`, `content_category`, `user_id`
- Tag description: **(TikTok数据分析接口/TikTok-Analytics-API data analysis endpoints)**

## Routes

### `GET /api/u1/v1/tiktok/analytics/detect_fake_views`

- Summary: 检测视频虚假流量分析/Detect fake views in video
- Capabilities: analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `detect_fake_views_api_v1_tiktok_analytics_detect_fake_views_get`
- Full contract: [`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-detect-fake-views`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-detect-fake-views)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |
| content_category | query | string | No | 内容分类/Content category, options: default, entertainment, education, product, verified_large |

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

### `GET /api/u1/v1/tiktok/analytics/fetch_comment_keywords`

- Summary: 获取视频评论关键词分析/Get comment keywords analysis
- Capabilities: comments / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_comment_keywords_api_v1_tiktok_analytics_fetch_comment_keywords_get`
- Full contract: [`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-comment-keywords`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-comment-keywords)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/analytics/fetch_creator_info_and_milestones`

- Summary: 获取创作者信息和里程碑数据/Get creator info and milestones
- Capabilities: creators / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_info_and_milestones_api_v1_tiktok_analytics_fetch_creator_info_and_milestones_get`
- Full contract: [`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-creator-info-and-milestones`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-creator-info-and-milestones)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户id/User id |

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

### `GET /api/u1/v1/tiktok/analytics/fetch_video_metrics`

- Summary: 获取作品的统计数据/Get video metrics
- Capabilities: content details / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_metrics_api_v1_tiktok_analytics_fetch_video_metrics_get`
- Full contract: [`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-video-metrics`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-video-metrics)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id |

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
