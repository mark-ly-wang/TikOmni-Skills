# TikTok-Ads-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/tiktok-ads-api.md`
- Full contract: [`api-contracts/tiktok-ads-api.md`](../api-contracts/tiktok-ads-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `31`
- Common capabilities: ads / search / details / creators / commerce / topics
- Default auth: Header `Authorization` Bearer
- Common inputs: `limit`, `page`, `country_code`, `period`, `keyword`, `period_type`, `industry`, `order_by`, `rank_type`, `material_id`
- Tag description: **(TikTok广告创意中心数据接口/TikTok-Ads-Creative-Center-API endpoints)**

## Routes

### `GET /api/u1/v1/tiktok/ads/get_ad_interactive_analysis`

- Summary: 获取广告互动分析/Get ad interactive analysis
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-interactive-analysis`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-interactive-analysis)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| material_id | query | string | Yes | 广告素材ID/Ad material ID |
| metric_type | query | string | No | 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain) |
| period_type | query | integer | No | 时间范围(天)/Period type (days) |

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

### `GET /api/u1/v1/tiktok/ads/get_ad_keyframe_analysis`

- Summary: 获取广告关键帧分析/Get ad keyframe analysis
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-keyframe-analysis`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-keyframe-analysis)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| material_id | query | string | Yes | 广告素材ID/Ad material ID |
| metric | query | string | No | 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt, convert_cnt, play_retain_cnt) |

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

### `GET /api/u1/v1/tiktok/ads/get_ad_percentile`

- Summary: 获取广告百分位数据/Get ad percentile data
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-percentile`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-percentile)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| material_id | query | string | Yes | 广告素材ID/Ad material ID |
| metric | query | string | No | 分析指标/Analysis metric (ctr_percentile, time_attr_conversion_rate_percentile, click_cnt_percentile, time_attr_convert_cnt… |
| period_type | query | integer | No | 时间范围(天)/Time period (days) |

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

### `GET /api/u1/v1/tiktok/ads/get_ads_detail`

- Summary: 获取单个广告详情/Get single ad detail
- Capabilities: details / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ads-detail`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ads-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| ads_id | query | string | Yes | 广告ID/Ad ID |

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

### `GET /api/u1/v1/tiktok/ads/get_creative_patterns`

- Summary: 获取创意模式排行榜/Get creative pattern rankings
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creative-patterns`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creative-patterns)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| first_industry_id | query | string | No | 一级行业ID/First industry ID |
| period_type | query | string | No | 时间周期类型/Period type (week, month) |
| order_field | query | string | No | 排序字段/Order field (ctr, play_over_rate) |
| order_type | query | string | No | 排序方式/Sort order (desc, asc) |
| week | query | string | No | 特定周（可选）/Specific week (optional) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |

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

### `GET /api/u1/v1/tiktok/ads/get_creator_filters`

- Summary: 获取创作者筛选器/Get creator filters
- Capabilities: creators / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-filters)

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

### `GET /api/u1/v1/tiktok/ads/get_creator_list`

- Summary: 获取创作者列表/Get creator list
- Capabilities: creators / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creator_list_api_v1_tiktok_ads_get_creator_list_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| sort_by | query | string | No | 排序方式/Sort by (follower, engagement, avg_views) |
| creator_country | query | string | No | 创作者国家/Creator country |
| audience_country | query | string | No | 受众国家/Audience country |
| audience_count | query | integer | No | 受众数量筛选/Audience count filter |
| keyword | query | string | No | 关键词/Keyword |

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

### `GET /api/u1/v1/tiktok/ads/get_hashtag_creator`

- Summary: 获取标签创作者信息/Get hashtag creator info
- Capabilities: creators / ads / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-creator`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-creator)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| hashtag | query | string | Yes | 标签名称，不包含#符号/Hashtag name (without # symbol) |

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

### `GET /api/u1/v1/tiktok/ads/get_hashtag_filters`

- Summary: 获取标签筛选器/Get hashtag filters
- Capabilities: ads / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-filters)

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

### `GET /api/u1/v1/tiktok/ads/get_hashtag_list`

- Summary: 获取热门标签列表/Get popular hashtags list
- Capabilities: ads / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| country_code | query | string | No | 国家代码/Country code |
| sort_by | query | string | No | 排序方式/Sort by (popular, new) |
| industry_id | query | string | No | 行业ID/Industry ID |
| filter_by | query | string | No | 筛选条件/Filter (new_on_board) |

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_details`

- Summary: 获取关键词详细信息/Get keyword details
- Capabilities: details / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-details`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-details)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | No | 关键词（可选）/Keyword (optional) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| country_code | query | string | No | 国家代码/Country code |
| order_by | query | string | No | 排序字段/Sort field |
| order_type | query | string | No | 排序方式/Sort order (desc, asc) |
| industry | query | string | No | 行业ID/Industry ID |
| objective | query | string | No | 广告目标/Ad objective |
| keyword_type | query | string | No | 关键词类型/Keyword type |

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_filters`

- Summary: 获取关键词筛选器/Get keyword filters
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-filters)

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_insights`

- Summary: 获取关键词洞察数据/Get keyword insights data
- Capabilities: ads / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-insights`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-insights)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| period | query | integer | No | 时间段（天）/Time period (days, 7/30/120/180) |
| country_code | query | string | No | 国家代码/Country code |
| order_by | query | string | No | 排序字段/Sort field (post, ctr, click_rate, etc.) |
| order_type | query | string | No | 排序方式/Sort order (desc, asc) |
| industry | query | string | No | 行业ID/Industry ID |
| objective | query | string | No | 广告目标/Ad objective |
| keyword_type | query | string | No | 关键词类型/Keyword type |
| keyword | query | string | No | 关键词/Keyword |

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_list`

- Summary: 获取关键词列表/Get keyword list
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | No | 关键词/Keyword |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| country_code | query | string | No | 国家代码/Country code |
| industry | query | string | No | 行业ID列表，逗号分隔/Industry IDs, comma separated |

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

### `GET /api/u1/v1/tiktok/ads/get_popular_trends`

- Summary: 获取流行趋势视频/Get popular trend videos
- Capabilities: trends / rankings / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-popular-trends`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-popular-trends)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| order_by | query | string | No | 排序字段/Order by (vv, like, comment, repost) |
| country_code | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_product_detail`

- Summary: 获取产品详细信息/Get product detail
- Capabilities: details / commerce / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_detail_api_v1_tiktok_ads_get_product_detail_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-detail`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | query | string | Yes | 产品类目ID/Product category ID |
| last | query | integer | No | 最近天数/Last days |
| ecom_type | query | string | No | 电商类型/E-commerce type |
| period_type | query | string | No | 时间类型/Period type |
| country_code | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_product_filters`

- Summary: 获取产品筛选器/Get product filters
- Capabilities: commerce / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_filters_api_v1_tiktok_ads_get_product_filters_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-filters)

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

### `GET /api/u1/v1/tiktok/ads/get_product_metrics`

- Summary: 获取产品指标数据/Get product metrics
- Capabilities: commerce / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-metrics`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-metrics)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| id | query | string | Yes | 产品类目ID/Product category ID |
| last | query | integer | No | 最近天数/Last days |
| metrics | query | string | No | 指标类型，逗号分隔/Metrics types, comma separated |
| ecom_type | query | string | No | 电商类型/E-commerce type |
| period_type | query | string | No | 时间类型/Period type |
| country_code | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_query_suggestions`

- Summary: 获取查询建议/Get query suggestions
- Capabilities: search / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-query-suggestions`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-query-suggestions)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| count | query | integer | No | 建议数量/Suggestion count |
| scenario | query | integer | No | 场景类型/Scenario type |

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

### `GET /api/u1/v1/tiktok/ads/get_recommended_ads`

- Summary: 获取推荐广告/Get recommended ads
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-recommended-ads`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-recommended-ads)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| material_id | query | string | Yes | 广告素材ID/Ad material ID |
| industry | query | string | No | 行业ID/Industry ID |
| country_code | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_related_keywords`

- Summary: 获取相关关键词/Get related keywords
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-related-keywords`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-related-keywords)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | No | 目标关键词/Target keyword |
| period | query | integer | No | 时间段（天）/Time period (days, 7/30/120) |
| country_code | query | string | No | 国家/地区代码/Country code |
| rank_type | query | string | No | 排名类型/Rank type (popular: 热门, breakout: 突破性) |
| content_type | query | string | No | 内容类型/Content type (keyword, hashtag) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_detail`

- Summary: 获取音乐详情/Get sound detail
- Capabilities: details / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-detail`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| clip_id | query | string | Yes | 音乐ID/Sound clip ID |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| country_code | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_filters`

- Summary: 获取音乐筛选器/Get sound filters
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-filters)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| rank_type | query | string | No | 排行类型/Rank type (popular, surging) |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_rank_list`

- Summary: 获取热门音乐排行榜/Get popular sound rankings
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-rank-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-rank-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| rank_type | query | string | No | 排行类型/Rank type (popular, surging) |
| new_on_board | query | boolean | No | 是否只看新上榜/Only new on board |
| commercial_music | query | boolean | No | 是否商业音乐/Commercial music only |
| country_code | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_recommendations`

- Summary: 获取音乐推荐/Get sound recommendations
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-recommendations`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-recommendations)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| clip_id | query | string | Yes | 参考音乐ID/Reference sound clip ID |
| limit | query | integer | No | 推荐数量/Number of recommendations |

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

### `GET /api/u1/v1/tiktok/ads/get_top_ads_spotlight`

- Summary: 获取热门广告聚光灯/Get top ads spotlight
- Capabilities: ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-ads-spotlight`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-ads-spotlight)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| industry | query | string | No | 行业ID/Industry ID |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |

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

### `GET /api/u1/v1/tiktok/ads/get_top_products`

- Summary: 获取热门产品列表/Get top products list
- Capabilities: commerce / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_top_products_api_v1_tiktok_ads_get_top_products_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-products`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-products)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| last | query | integer | No | 最近天数/Last days |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| country_code | query | string | No | 国家代码/Country code |
| first_ecom_category_id | query | string | No | 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma separated |
| ecom_type | query | string | No | 电商类型/E-commerce type (l3) |
| period_type | query | string | No | 时间类型/Period type (last) |
| order_by | query | string | No | 排序字段/Sort field (post, ctr, cvr) |
| order_type | query | string | No | 排序方式/Sort order (desc, asc) |

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

### `GET /api/u1/v1/tiktok/ads/search_ads`

- Summary: 搜索广告/Search ads
- Capabilities: search / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_ads_api_v1_tiktok_ads_search_ads_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-ads`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-ads)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| objective | query | integer | No | 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户 7:产品销售) |
| like | query | integer | No | 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%) |
| period | query | integer | No | 时间段/Time period (days) |
| industry | query | string | No | 行业ID/Industry ID |
| keyword | query | string | No | 搜索关键词/Search keyword |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| order_by | query | string | No | 排序方式/Sort by (for_you, likes) |
| country_code | query | string | No | 国家代码/Country code |
| ad_format | query | integer | No | 广告格式/Ad format (1:视频) |
| ad_language | query | string | No | 广告语言/Ad language |
| search_id | query | string | No | 搜索ID（可选）/Search ID (optional) |

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

### `GET /api/u1/v1/tiktok/ads/search_creators`

- Summary: 搜索创作者/Search creators
- Capabilities: search / creators / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_creators_api_v1_tiktok_ads_search_creators_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-creators`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-creators)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| sort_by | query | string | No | 排序方式/Sort by (follower, avg_views) |
| creator_country | query | string | No | 创作者国家/Creator country |

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

### `GET /api/u1/v1/tiktok/ads/search_sound`

- Summary: 搜索音乐/Search sounds
- Capabilities: search / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_sound_api_v1_tiktok_ads_search_sound_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| rank_type | query | string | No | 排行类型/Rank type (popular, surging) |
| new_on_board | query | boolean | No | 是否只看新上榜/Only new on board |
| commercial_music | query | boolean | No | 是否商业音乐/Commercial music only |
| country_code | query | string | No | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/search_sound_hint`

- Summary: 搜索音乐提示/Search sound hints
- Capabilities: search / ads
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get`
- Full contract: [`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound-hint`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound-hint)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword |
| period | query | integer | No | 时间范围（天）/Time period (days) |
| page | query | integer | No | 页码/Page number |
| limit | query | integer | No | 每页数量/Items per page |
| rank_type | query | string | No | 排行类型/Rank type (popular, surging) |
| country_code | query | string | No | 国家代码/Country code |
| filter_by_checked | query | boolean | No | 是否只看已验证/Only verified |
| commercial_music | query | boolean | No | 是否商业音乐/Commercial music only |

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
