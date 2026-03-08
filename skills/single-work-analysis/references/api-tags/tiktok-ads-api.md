# TikTok-Ads-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-ads-api.md`
- 完整契约：[`api-contracts/tiktok-ads-api.md`](../api-contracts/tiktok-ads-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`31`
- 常见能力：广告 / 搜索 / 详情 / 创作者 / 电商 / 话题
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`limit`, `page`, `country_code`, `period`, `keyword`, `period_type`, `industry`, `order_by`, `rank_type`, `material_id`
- 标签说明：**(TikTok广告创意中心数据接口/TikTok-Ads-Creative-Center-API endpoints)**

## 路由列表

### `GET /api/u1/v1/tiktok/ads/get_ad_interactive_analysis`

- 摘要：获取广告互动分析/Get ad interactive analysis
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ad_interactive_analysis_api_v1_tiktok_ads_get_ad_interactive_analysis_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-interactive-analysis`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-interactive-analysis)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| material_id | query | string | 是 | 广告素材ID/Ad material ID |
| metric_type | query | string | 否 | 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain) |
| period_type | query | integer | 否 | 时间范围(天)/Period type (days) |

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

### `GET /api/u1/v1/tiktok/ads/get_ad_keyframe_analysis`

- 摘要：获取广告关键帧分析/Get ad keyframe analysis
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ad_keyframe_analysis_api_v1_tiktok_ads_get_ad_keyframe_analysis_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-keyframe-analysis`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-keyframe-analysis)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| material_id | query | string | 是 | 广告素材ID/Ad material ID |
| metric | query | string | 否 | 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt, convert_cnt, play_retain_cnt) |

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

### `GET /api/u1/v1/tiktok/ads/get_ad_percentile`

- 摘要：获取广告百分位数据/Get ad percentile data
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ad_percentile_api_v1_tiktok_ads_get_ad_percentile_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-percentile`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ad-percentile)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| material_id | query | string | 是 | 广告素材ID/Ad material ID |
| metric | query | string | 否 | 分析指标/Analysis metric (ctr_percentile, time_attr_conversion_rate_percentile, click_cnt_percentile, time_attr_convert_cnt… |
| period_type | query | integer | 否 | 时间范围(天)/Time period (days) |

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

### `GET /api/u1/v1/tiktok/ads/get_ads_detail`

- 摘要：获取单个广告详情/Get single ad detail
- 能力：详情 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ads_detail_api_v1_tiktok_ads_get_ads_detail_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ads-detail`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-ads-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ads_id | query | string | 是 | 广告ID/Ad ID |

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

### `GET /api/u1/v1/tiktok/ads/get_creative_patterns`

- 摘要：获取创意模式排行榜/Get creative pattern rankings
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_creative_patterns_api_v1_tiktok_ads_get_creative_patterns_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creative-patterns`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creative-patterns)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| first_industry_id | query | string | 否 | 一级行业ID/First industry ID |
| period_type | query | string | 否 | 时间周期类型/Period type (week, month) |
| order_field | query | string | 否 | 排序字段/Order field (ctr, play_over_rate) |
| order_type | query | string | 否 | 排序方式/Sort order (desc, asc) |
| week | query | string | 否 | 特定周（可选）/Specific week (optional) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |

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

### `GET /api/u1/v1/tiktok/ads/get_creator_filters`

- 摘要：获取创作者筛选器/Get creator filters
- 能力：创作者 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_creator_filters_api_v1_tiktok_ads_get_creator_filters_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-filters)

#### 参数

无

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

### `GET /api/u1/v1/tiktok/ads/get_creator_list`

- 摘要：获取创作者列表/Get creator list
- 能力：创作者 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_creator_list_api_v1_tiktok_ads_get_creator_list_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-creator-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| sort_by | query | string | 否 | 排序方式/Sort by (follower, engagement, avg_views) |
| creator_country | query | string | 否 | 创作者国家/Creator country |
| audience_country | query | string | 否 | 受众国家/Audience country |
| audience_count | query | integer | 否 | 受众数量筛选/Audience count filter |
| keyword | query | string | 否 | 关键词/Keyword |

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

### `GET /api/u1/v1/tiktok/ads/get_hashtag_creator`

- 摘要：获取标签创作者信息/Get hashtag creator info
- 能力：创作者 / 广告 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_hashtag_creator_api_v1_tiktok_ads_get_hashtag_creator_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-creator`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-creator)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| hashtag | query | string | 是 | 标签名称，不包含#符号/Hashtag name (without # symbol) |

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

### `GET /api/u1/v1/tiktok/ads/get_hashtag_filters`

- 摘要：获取标签筛选器/Get hashtag filters
- 能力：广告 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_hashtag_filters_api_v1_tiktok_ads_get_hashtag_filters_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-filters)

#### 参数

无

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

### `GET /api/u1/v1/tiktok/ads/get_hashtag_list`

- 摘要：获取热门标签列表/Get popular hashtags list
- 能力：广告 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_hashtag_list_api_v1_tiktok_ads_get_hashtag_list_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-hashtag-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| country_code | query | string | 否 | 国家代码/Country code |
| sort_by | query | string | 否 | 排序方式/Sort by (popular, new) |
| industry_id | query | string | 否 | 行业ID/Industry ID |
| filter_by | query | string | 否 | 筛选条件/Filter (new_on_board) |

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_details`

- 摘要：获取关键词详细信息/Get keyword details
- 能力：详情 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_keyword_details_api_v1_tiktok_ads_get_keyword_details_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-details`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-details)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 否 | 关键词（可选）/Keyword (optional) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| country_code | query | string | 否 | 国家代码/Country code |
| order_by | query | string | 否 | 排序字段/Sort field |
| order_type | query | string | 否 | 排序方式/Sort order (desc, asc) |
| industry | query | string | 否 | 行业ID/Industry ID |
| objective | query | string | 否 | 广告目标/Ad objective |
| keyword_type | query | string | 否 | 关键词类型/Keyword type |

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_filters`

- 摘要：获取关键词筛选器/Get keyword filters
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_keyword_filters_api_v1_tiktok_ads_get_keyword_filters_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-filters)

#### 参数

无

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_insights`

- 摘要：获取关键词洞察数据/Get keyword insights data
- 能力：广告 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_keyword_insights_api_v1_tiktok_ads_get_keyword_insights_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-insights`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-insights)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| period | query | integer | 否 | 时间段（天）/Time period (days, 7/30/120/180) |
| country_code | query | string | 否 | 国家代码/Country code |
| order_by | query | string | 否 | 排序字段/Sort field (post, ctr, click_rate, etc.) |
| order_type | query | string | 否 | 排序方式/Sort order (desc, asc) |
| industry | query | string | 否 | 行业ID/Industry ID |
| objective | query | string | 否 | 广告目标/Ad objective |
| keyword_type | query | string | 否 | 关键词类型/Keyword type |
| keyword | query | string | 否 | 关键词/Keyword |

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

### `GET /api/u1/v1/tiktok/ads/get_keyword_list`

- 摘要：获取关键词列表/Get keyword list
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_keyword_list_api_v1_tiktok_ads_get_keyword_list_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-keyword-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 否 | 关键词/Keyword |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| country_code | query | string | 否 | 国家代码/Country code |
| industry | query | string | 否 | 行业ID列表，逗号分隔/Industry IDs, comma separated |

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

### `GET /api/u1/v1/tiktok/ads/get_popular_trends`

- 摘要：获取流行趋势视频/Get popular trend videos
- 能力：热点/榜单 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_popular_trends_api_v1_tiktok_ads_get_popular_trends_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-popular-trends`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-popular-trends)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| order_by | query | string | 否 | 排序字段/Order by (vv, like, comment, repost) |
| country_code | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_product_detail`

- 摘要：获取产品详细信息/Get product detail
- 能力：详情 / 电商 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_detail_api_v1_tiktok_ads_get_product_detail_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-detail`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | query | string | 是 | 产品类目ID/Product category ID |
| last | query | integer | 否 | 最近天数/Last days |
| ecom_type | query | string | 否 | 电商类型/E-commerce type |
| period_type | query | string | 否 | 时间类型/Period type |
| country_code | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_product_filters`

- 摘要：获取产品筛选器/Get product filters
- 能力：电商 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_filters_api_v1_tiktok_ads_get_product_filters_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-filters)

#### 参数

无

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

### `GET /api/u1/v1/tiktok/ads/get_product_metrics`

- 摘要：获取产品指标数据/Get product metrics
- 能力：电商 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_metrics_api_v1_tiktok_ads_get_product_metrics_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-metrics`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-product-metrics)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | query | string | 是 | 产品类目ID/Product category ID |
| last | query | integer | 否 | 最近天数/Last days |
| metrics | query | string | 否 | 指标类型，逗号分隔/Metrics types, comma separated |
| ecom_type | query | string | 否 | 电商类型/E-commerce type |
| period_type | query | string | 否 | 时间类型/Period type |
| country_code | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_query_suggestions`

- 摘要：获取查询建议/Get query suggestions
- 能力：搜索 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_query_suggestions_api_v1_tiktok_ads_get_query_suggestions_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-query-suggestions`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-query-suggestions)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| count | query | integer | 否 | 建议数量/Suggestion count |
| scenario | query | integer | 否 | 场景类型/Scenario type |

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

### `GET /api/u1/v1/tiktok/ads/get_recommended_ads`

- 摘要：获取推荐广告/Get recommended ads
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_recommended_ads_api_v1_tiktok_ads_get_recommended_ads_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-recommended-ads`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-recommended-ads)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| material_id | query | string | 是 | 广告素材ID/Ad material ID |
| industry | query | string | 否 | 行业ID/Industry ID |
| country_code | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_related_keywords`

- 摘要：获取相关关键词/Get related keywords
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_related_keywords_api_v1_tiktok_ads_get_related_keywords_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-related-keywords`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-related-keywords)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 否 | 目标关键词/Target keyword |
| period | query | integer | 否 | 时间段（天）/Time period (days, 7/30/120) |
| country_code | query | string | 否 | 国家/地区代码/Country code |
| rank_type | query | string | 否 | 排名类型/Rank type (popular: 热门, breakout: 突破性) |
| content_type | query | string | 否 | 内容类型/Content type (keyword, hashtag) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_detail`

- 摘要：获取音乐详情/Get sound detail
- 能力：详情 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_sound_detail_api_v1_tiktok_ads_get_sound_detail_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-detail`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| clip_id | query | string | 是 | 音乐ID/Sound clip ID |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| country_code | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_filters`

- 摘要：获取音乐筛选器/Get sound filters
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_sound_filters_api_v1_tiktok_ads_get_sound_filters_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-filters`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-filters)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| rank_type | query | string | 否 | 排行类型/Rank type (popular, surging) |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_rank_list`

- 摘要：获取热门音乐排行榜/Get popular sound rankings
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_sound_rank_list_api_v1_tiktok_ads_get_sound_rank_list_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-rank-list`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-rank-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| rank_type | query | string | 否 | 排行类型/Rank type (popular, surging) |
| new_on_board | query | boolean | 否 | 是否只看新上榜/Only new on board |
| commercial_music | query | boolean | 否 | 是否商业音乐/Commercial music only |
| country_code | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/get_sound_recommendations`

- 摘要：获取音乐推荐/Get sound recommendations
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_sound_recommendations_api_v1_tiktok_ads_get_sound_recommendations_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-recommendations`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-sound-recommendations)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| clip_id | query | string | 是 | 参考音乐ID/Reference sound clip ID |
| limit | query | integer | 否 | 推荐数量/Number of recommendations |

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

### `GET /api/u1/v1/tiktok/ads/get_top_ads_spotlight`

- 摘要：获取热门广告聚光灯/Get top ads spotlight
- 能力：广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_top_ads_spotlight_api_v1_tiktok_ads_get_top_ads_spotlight_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-ads-spotlight`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-ads-spotlight)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| industry | query | string | 否 | 行业ID/Industry ID |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |

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

### `GET /api/u1/v1/tiktok/ads/get_top_products`

- 摘要：获取热门产品列表/Get top products list
- 能力：电商 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_top_products_api_v1_tiktok_ads_get_top_products_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-products`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-get-top-products)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| last | query | integer | 否 | 最近天数/Last days |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| country_code | query | string | 否 | 国家代码/Country code |
| first_ecom_category_id | query | string | 否 | 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma separated |
| ecom_type | query | string | 否 | 电商类型/E-commerce type (l3) |
| period_type | query | string | 否 | 时间类型/Period type (last) |
| order_by | query | string | 否 | 排序字段/Sort field (post, ctr, cvr) |
| order_type | query | string | 否 | 排序方式/Sort order (desc, asc) |

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

### `GET /api/u1/v1/tiktok/ads/search_ads`

- 摘要：搜索广告/Search ads
- 能力：搜索 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_ads_api_v1_tiktok_ads_search_ads_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-ads`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-ads)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| objective | query | integer | 否 | 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户 7:产品销售) |
| like | query | integer | 否 | 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%) |
| period | query | integer | 否 | 时间段/Time period (days) |
| industry | query | string | 否 | 行业ID/Industry ID |
| keyword | query | string | 否 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| order_by | query | string | 否 | 排序方式/Sort by (for_you, likes) |
| country_code | query | string | 否 | 国家代码/Country code |
| ad_format | query | integer | 否 | 广告格式/Ad format (1:视频) |
| ad_language | query | string | 否 | 广告语言/Ad language |
| search_id | query | string | 否 | 搜索ID（可选）/Search ID (optional) |

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

### `GET /api/u1/v1/tiktok/ads/search_creators`

- 摘要：搜索创作者/Search creators
- 能力：搜索 / 创作者 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_creators_api_v1_tiktok_ads_search_creators_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-creators`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-creators)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| sort_by | query | string | 否 | 排序方式/Sort by (follower, avg_views) |
| creator_country | query | string | 否 | 创作者国家/Creator country |

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

### `GET /api/u1/v1/tiktok/ads/search_sound`

- 摘要：搜索音乐/Search sounds
- 能力：搜索 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_sound_api_v1_tiktok_ads_search_sound_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| rank_type | query | string | 否 | 排行类型/Rank type (popular, surging) |
| new_on_board | query | boolean | 否 | 是否只看新上榜/Only new on board |
| commercial_music | query | boolean | 否 | 是否商业音乐/Commercial music only |
| country_code | query | string | 否 | 国家代码/Country code |

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

### `GET /api/u1/v1/tiktok/ads/search_sound_hint`

- 摘要：搜索音乐提示/Search sound hints
- 能力：搜索 / 广告
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_sound_hint_api_v1_tiktok_ads_search_sound_hint_get`
- 完整契约：[`api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound-hint`](../api-contracts/tiktok-ads-api.md#get-api-u1-v1-tiktok-ads-search-sound-hint)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |
| period | query | integer | 否 | 时间范围（天）/Time period (days) |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Items per page |
| rank_type | query | string | 否 | 排行类型/Rank type (popular, surging) |
| country_code | query | string | 否 | 国家代码/Country code |
| filter_by_checked | query | boolean | 否 | 是否只看已验证/Only verified |
| commercial_music | query | boolean | 否 | 是否商业音乐/Commercial music only |

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
