# TikTok-Creator-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tiktok-creator-api.md`
- Full contract: [`api-contracts/tiktok-creator-api.md`](../api-contracts/tiktok-creator-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `14`
- Common capabilities: creators / content details / analytics / commerce / livestream / details
- Default auth: Header `Authorization` Bearer
- Common inputs: `cookie`, `proxy`, `start_date`, `item_id`, `page`, `product_id`, `end_date`, `count`, `offset`, `item_ids`
- Tag description: **(TikTok创作者数据和账号收益数据接口/TikTok-Creator-API data and account revenue data endpoints)**

## Routes

### `POST /api/u1/v1/tiktok/creator/get_account_health_status`

- Summary: 获取创作者账号健康状态/Get Creator Account Health Status
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_account_health_status_api_v1_tiktok_creator_get_account_health_status_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-health-status`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-health-status)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |

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

### `POST /api/u1/v1/tiktok/creator/get_account_insights_overview`

- Summary: 获取创作者账号概览/Get Creator Account Overview
- Capabilities: creators / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_account_insights_overview_api_v1_tiktok_creator_get_account_insights_overview_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-insights-overview`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-insights-overview)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |

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

### `POST /api/u1/v1/tiktok/creator/get_account_violation_list`

- Summary: 获取创作者账号违规记录列表/Get Creator Account Violation Record List
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_account_violation_list_api_v1_tiktok_creator_get_account_violation_list_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-violation-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-violation-list)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `page`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| page | integer | No | 页码/Page Number |

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

### `POST /api/u1/v1/tiktok/creator/get_creator_account_info`

- Summary: 获取创作者账号信息/Get Creator Account Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creator_account_info_api_v1_tiktok_creator_get_creator_account_info_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-creator-account-info`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-creator-account-info)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |

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

### `POST /api/u1/v1/tiktok/creator/get_live_analytics_summary`

- Summary: 获取创作者直播概览/Get Creator Live Overview
- Capabilities: creators / analytics / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_live_overview_api_v1_tiktok_creator_get_live_analytics_summary_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-live-analytics-summary`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-live-analytics-summary)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |

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

### `POST /api/u1/v1/tiktok/creator/get_product_analytics_list`

- Summary: 获取创作者商品列表分析/Get Creator Product List Analytics
- Capabilities: creators / commerce / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_analytics_list_api_v1_tiktok_creator_get_product_analytics_list_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-analytics-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-analytics-list)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string, `end_date`:string, `page`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 开始日期，如 '2025-04-01'/ Start Date, e.g. '2025-04-01' |
| end_date | string | No | 结束日期，如 '2025-05-01'/ End Date, e.g. '2025-05-01' |
| page | integer | No | 页码/Page Number |

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

### `POST /api/u1/v1/tiktok/creator/get_product_related_videos`

- Summary: 获取同款商品关联视频/Get Product Related Videos
- Capabilities: creators / content details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_related_videos_api_v1_tiktok_creator_get_product_related_videos_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-related-videos`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-related-videos)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | Yes | 视频 ID/Video ID |
| product_id | string | Yes | 商品 ID/Product ID |

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

### `POST /api/u1/v1/tiktok/creator/get_showcase_product_list`

- Summary: 获取橱窗商品列表/Get Showcase Product List
- Capabilities: creators / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_showcase_product_list_api_v1_tiktok_creator_get_showcase_product_list_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-showcase-product-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-showcase-product-list)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `count`:integer, `offset`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| count | integer | No | 每页数量/Page Size |
| offset | integer | No | 偏移量/Offset |

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

### `POST /api/u1/v1/tiktok/creator/get_video_analytics_summary`

- Summary: 获取创作者视频概览/Get Creator Video Overview
- Capabilities: creators / content details / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_analytics_summary_api_v1_tiktok_creator_get_video_analytics_summary_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-analytics-summary`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-analytics-summary)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |

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

### `POST /api/u1/v1/tiktok/creator/get_video_associated_product_list`

- Summary: 获取视频关联商品列表/Get Video Associated Product List
- Capabilities: creators / content details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_associated_product_list_api_v1_tiktok_creator_get_video_associated_product_list_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-associated-product-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-associated-product-list)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string, `item_ids*`[string]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_ids | array<string> | Yes | 视频 ID 列表/Video ID List |

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

### `POST /api/u1/v1/tiktok/creator/get_video_audience_stats`

- Summary: 获取视频受众分析数据/Get Video Audience Analysis Data
- Capabilities: creators / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_audience_stats_api_v1_tiktok_creator_get_video_audience_stats_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-audience-stats`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-audience-stats)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | Yes | 视频 ID/Video ID |

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

### `POST /api/u1/v1/tiktok/creator/get_video_detailed_stats`

- Summary: 获取视频详细分段统计数据/Get Video Detailed Statistics
- Capabilities: creators / content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_detailed_stats_api_v1_tiktok_creator_get_video_detailed_stats_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-detailed-stats`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-detailed-stats)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | Yes | 视频 ID/Video ID |

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

### `POST /api/u1/v1/tiktok/creator/get_video_list_analytics`

- Summary: 获取创作者视频列表分析/Get Creator Video List Analytics
- Capabilities: creators / content details / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_list_api_v1_tiktok_creator_get_video_list_analytics_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-list-analytics`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-list-analytics)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string, `page`:integer, `rules`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| page | integer | No | 页码/Page Number |
| rules | string | No | 列表排序规则，默认按发布时间排序/ List sorting rule, default is by publish time |

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

### `POST /api/u1/v1/tiktok/creator/get_video_to_product_stats`

- Summary: 获取视频与商品关联统计数据/Get Video-Product Association Statistics
- Capabilities: creators / content details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_to_product_stats_api_v1_tiktok_creator_get_video_to_product_stats_post`
- Full contract: [`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-to-product-stats`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-to-product-stats)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | No | 用户 Cookie 字符串/User Cookie String |
| proxy | string | No | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | No | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | Yes | 视频 ID/Video ID |
| product_id | string | Yes | 商品 ID/Product ID |

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
