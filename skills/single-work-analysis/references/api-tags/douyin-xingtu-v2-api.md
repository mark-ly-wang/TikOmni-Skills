# Douyin-Xingtu-V2-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/douyin-xingtu-v2-api.md`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md`](../api-contracts/douyin-xingtu-v2-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `21`
- Common capabilities: creators / general / trends / rankings / comments / details / profiles / accounts
- Default auth: Header `Authorization` Bearer
- Common inputs: `o_author_id`, `platform_source`, `limit`, `platform_channel`, `author_id`, `only_assign`, `flow_type`, `page`, `qualifier`, `period`
- Tag description: **(抖音星图V2数据接口/Douyin-Xingtu-V2-API data endpoints)**

## Routes

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_base_info`

- Summary: 获取创作者基本信息/Get Author Base Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-base-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-base-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID |
| platform_source | query | integer | No | 平台来源/Platform source |
| platform_channel | query | integer | No | 平台渠道/Platform channel |
| recommend | query | boolean | No | 是否返回推荐信息/Whether to return recommendation info |
| need_sec_uid | query | boolean | No | 是否返回sec_uid/Whether to return sec_uid |
| need_linkage_info | query | boolean | No | 是否返回联动信息/Whether to return linkage info |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_business_card_info`

- Summary: 获取创作者商业卡片信息/Get Author Business Card Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-business-card-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-business-card-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_content_hot_keywords`

- Summary: 获取创作者内容热词/Get Author Content Hot Keywords
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-content-hot-keywords`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-content-hot-keywords)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| author_id | query | string | Yes | 创作者ID/Creator author ID |
| keyword_type | query | integer | No | 热词类型/Keyword type |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_hot_comment_tokens`

- Summary: 获取创作者评论热词/Get Author Hot Comment Tokens
- Capabilities: comments / trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-hot-comment-tokens`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-hot-comment-tokens)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| author_id | query | string | Yes | 创作者ID/Creator author ID |
| num | query | integer | No | 返回热词数量/Number of hot tokens |
| without_emoji | query | boolean | No | 是否排除emoji/Whether to exclude emoji |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_local_info`

- Summary: 获取创作者位置信息/Get Author Local Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-local-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-local-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID |
| platform_source | query | integer | No | 平台来源/Platform source |
| platform_channel | query | integer | No | 平台渠道/Platform channel |
| time_range | query | integer | No | 时间范围(天)/Time range in days |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_market_fields`

- Summary: 获取达人广场筛选字段/Get Author Market Fields
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-market-fields`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-market-fields)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| market_scene | query | integer | No | 市场场景，1=默认场景/Market scene, 1=default |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_show_items`

- Summary: 获取创作者视频列表/Get Author Show Items
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-show-items`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-show-items)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID |
| platform_source | query | integer | No | 平台来源/Platform source |
| platform_channel | query | integer | No | 平台渠道/Platform channel |
| limit | query | integer | No | 返回数量/Result limit |
| only_assign | query | boolean | No | 仅看指派视频/Only show assigned videos |
| flow_type | query | integer | No | 流量类型/Flow type |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_spread_info`

- Summary: 获取创作者传播价值/Get Author Spread Info
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-spread-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-spread-info)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | Yes | 创作者ID/Creator author ID |
| platform_source | query | integer | No | 平台来源/Platform source |
| platform_channel | query | integer | No | 平台渠道/Platform channel |
| type | query | integer | No | 视频类型，1=个人视频/Video type, 1=personal video |
| flow_type | query | integer | No | 流量类型/Flow type |
| only_assign | query | boolean | No | 仅看指派视频/Only assigned videos |
| range | query | integer | No | 时间范围，2=近30天，3=近90天/Time range, 2=last 30 days, 3=last 90 days |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_content_trend_guide`

- Summary: 获取内容趋势指南/Get Content Trend Guide
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-content-trend-guide`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-content-trend-guide)

#### Parameters

None

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_demander_mcn_list`

- Summary: 搜索MCN机构列表/Get Demander MCN List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-demander-mcn-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-demander-mcn-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| mcn_name | query | string | No | MCN机构名称，支持模糊搜索/MCN name, supports fuzzy search |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Page size |
| order_by | query | string | No | 排序方式/Sort by |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_excellent_case_category_list`

- Summary: 获取优秀行业分类列表/Get Excellent Case Category List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-excellent-case-category-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-excellent-case-category-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| platform_source | query | integer | No | 平台来源/Platform source |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_detail`

- Summary: 获取星图IP活动详情/Get IP Activity Detail
- Capabilities: details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-detail`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | query | integer | Yes | 活动ID，从get_ip_activity_list获取/Activity ID from get_ip_activity_list |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_industry_list`

- Summary: 获取星图IP日历行业列表/Get IP Activity Industry List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-industry-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-industry-list)

#### Parameters

None

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

### `POST /api/u1/v1/douyin/xingtu_v2/get_ip_activity_list`

- Summary: 获取星图IP日历活动列表/Get IP Activity List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-ip-activity-list`](../api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-ip-activity-list)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `query_start_time*`:string, `query_end_time*`:string, `industry_id_list`[string], `category_list`[integer], `status_list`[integer]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| query_start_time | string | Yes | 查询开始时间戳/Query start timestamp |
| query_end_time | string | Yes | 查询结束时间戳/Query end timestamp |
| industry_id_list | array<string> | No | 行业ID列表/Industry ID list |
| category_list | array<integer> | No | IP类型列表/IP category list |
| status_list | array<integer> | No | IP状态列表/IP status list |

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

### `POST /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog`

- Summary: 获取短剧演员热榜分类/Get Playlet Actor Rank Catalog
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-catalog`](../api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-catalog)

#### Parameters

None

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_list`

- Summary: 获取短剧演员热榜/Get Playlet Actor Rank List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| category | query | string | No | 分类/Category |
| name | query | string | No | 榜单名称/Ranking name |
| qualifier | query | string | No | 达人类型，空字符串=不限/Actor type, empty=all |
| period | query | integer | No | 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly |
| date | query | string | No | 统计日期，格式YYYYMMDD/Date, format YYYYMMDD |
| limit | query | integer | No | 返回数量/Result limit |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_catalog`

- Summary: 获取星图热榜分类/Get Ranking List Catalog
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-catalog`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-catalog)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| codes | query | string | No | 分类代码，默认为空字符串/Classification codes, default is empty string |
| biz_scene | query | string | No | 业务场景/Business scene |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_data`

- Summary: 获取星图达人商业榜数据/Get Ranking List Data
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-data`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-data)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| code | query | integer | No | 榜单类型代码/Ranking type code |
| qualifier | query | string | No | 榜单分类ID，从get_ranking_list_catalog获取/Category qualifier_id |
| version | query | string | No | 版本/Version |
| period | query | integer | No | 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly |
| date | query | string | No | 统计日期，格式YYYYMMDD/Date, format YYYYMMDD |
| limit | query | integer | No | 返回数量/Result limit |

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

### `POST /api/u1/v1/douyin/xingtu_v2/get_recommend_for_star_authors`

- Summary: 获取相似创作者推荐/Get Recommend Similar Star Authors
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-recommend-for-star-authors`](../api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-recommend-for-star-authors)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `author_ids*`[string], `similar_type`:string, `page`:integer, `limit`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| author_ids | array<string> | Yes | 创作者ID列表/List of creator author IDs |
| similar_type | string | No | 相似类型/Similarity type |
| page | integer | No | 页码/Page number |
| limit | integer | No | 每页数量/Page size |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_resource_list`

- Summary: 获取营销活动案例/Get Resource List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-resource-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-resource-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| resource_id | query | integer | Yes | 资源ID/Resource ID |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_user_profile_qrcode`

- Summary: 获取用户主页二维码/Get User Profile QRCode
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get`
- Full contract: [`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-user-profile-qrcode`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-user-profile-qrcode)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| core_user_id | query | string | No | 用户核心ID(与sec_uid二选一)/User core ID (pick one with sec_uid) |
| sec_uid | query | string | No | 用户sec_uid(与core_user_id二选一)/User sec_uid (pick one with core_user_id) |

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
