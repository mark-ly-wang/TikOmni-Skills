# TikTok-Creator-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-creator-api.md`
- 完整契约：[`api-contracts/tiktok-creator-api.md`](../api-contracts/tiktok-creator-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`14`
- 常见能力：创作者 / 作品详情 / 数据分析 / 电商 / 直播 / 详情
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`cookie`, `proxy`, `start_date`, `item_id`, `page`, `product_id`, `end_date`, `count`, `offset`, `item_ids`
- 标签说明：**(TikTok创作者数据和账号收益数据接口/TikTok-Creator-API data and account revenue data endpoints)**

## 路由列表

### `POST /api/u1/v1/tiktok/creator/get_account_health_status`

- 摘要：获取创作者账号健康状态/Get Creator Account Health Status
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_account_health_status_api_v1_tiktok_creator_get_account_health_status_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-health-status`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-health-status)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |

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

### `POST /api/u1/v1/tiktok/creator/get_account_insights_overview`

- 摘要：获取创作者账号概览/Get Creator Account Overview
- 能力：创作者 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_account_insights_overview_api_v1_tiktok_creator_get_account_insights_overview_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-insights-overview`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-insights-overview)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |

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

### `POST /api/u1/v1/tiktok/creator/get_account_violation_list`

- 摘要：获取创作者账号违规记录列表/Get Creator Account Violation Record List
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_account_violation_list_api_v1_tiktok_creator_get_account_violation_list_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-violation-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-account-violation-list)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `page`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| page | integer | 否 | 页码/Page Number |

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

### `POST /api/u1/v1/tiktok/creator/get_creator_account_info`

- 摘要：获取创作者账号信息/Get Creator Account Info
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_creator_account_info_api_v1_tiktok_creator_get_creator_account_info_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-creator-account-info`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-creator-account-info)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |

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

### `POST /api/u1/v1/tiktok/creator/get_live_analytics_summary`

- 摘要：获取创作者直播概览/Get Creator Live Overview
- 能力：创作者 / 数据分析 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_live_overview_api_v1_tiktok_creator_get_live_analytics_summary_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-live-analytics-summary`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-live-analytics-summary)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |

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

### `POST /api/u1/v1/tiktok/creator/get_product_analytics_list`

- 摘要：获取创作者商品列表分析/Get Creator Product List Analytics
- 能力：创作者 / 电商 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_analytics_list_api_v1_tiktok_creator_get_product_analytics_list_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-analytics-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-analytics-list)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `end_date`:string, `page`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 开始日期，如 '2025-04-01'/ Start Date, e.g. '2025-04-01' |
| end_date | string | 否 | 结束日期，如 '2025-05-01'/ End Date, e.g. '2025-05-01' |
| page | integer | 否 | 页码/Page Number |

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

### `POST /api/u1/v1/tiktok/creator/get_product_related_videos`

- 摘要：获取同款商品关联视频/Get Product Related Videos
- 能力：创作者 / 作品详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_product_related_videos_api_v1_tiktok_creator_get_product_related_videos_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-related-videos`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-product-related-videos)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | 是 | 视频 ID/Video ID |
| product_id | string | 是 | 商品 ID/Product ID |

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

### `POST /api/u1/v1/tiktok/creator/get_showcase_product_list`

- 摘要：获取橱窗商品列表/Get Showcase Product List
- 能力：创作者 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_showcase_product_list_api_v1_tiktok_creator_get_showcase_product_list_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-showcase-product-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-showcase-product-list)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `count`:integer, `offset`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| count | integer | 否 | 每页数量/Page Size |
| offset | integer | 否 | 偏移量/Offset |

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

### `POST /api/u1/v1/tiktok/creator/get_video_analytics_summary`

- 摘要：获取创作者视频概览/Get Creator Video Overview
- 能力：创作者 / 作品详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_analytics_summary_api_v1_tiktok_creator_get_video_analytics_summary_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-analytics-summary`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-analytics-summary)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |

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

### `POST /api/u1/v1/tiktok/creator/get_video_associated_product_list`

- 摘要：获取视频关联商品列表/Get Video Associated Product List
- 能力：创作者 / 作品详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_associated_product_list_api_v1_tiktok_creator_get_video_associated_product_list_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-associated-product-list`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-associated-product-list)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_ids*`[string]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_ids | array<string> | 是 | 视频 ID 列表/Video ID List |

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

### `POST /api/u1/v1/tiktok/creator/get_video_audience_stats`

- 摘要：获取视频受众分析数据/Get Video Audience Analysis Data
- 能力：创作者 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_audience_stats_api_v1_tiktok_creator_get_video_audience_stats_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-audience-stats`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-audience-stats)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | 是 | 视频 ID/Video ID |

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

### `POST /api/u1/v1/tiktok/creator/get_video_detailed_stats`

- 摘要：获取视频详细分段统计数据/Get Video Detailed Statistics
- 能力：创作者 / 作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_detailed_stats_api_v1_tiktok_creator_get_video_detailed_stats_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-detailed-stats`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-detailed-stats)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | 是 | 视频 ID/Video ID |

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

### `POST /api/u1/v1/tiktok/creator/get_video_list_analytics`

- 摘要：获取创作者视频列表分析/Get Creator Video List Analytics
- 能力：创作者 / 作品详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_list_api_v1_tiktok_creator_get_video_list_analytics_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-list-analytics`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-list-analytics)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `page`:integer, `rules`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| page | integer | 否 | 页码/Page Number |
| rules | string | 否 | 列表排序规则，默认按发布时间排序/ List sorting rule, default is by publish time |

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

### `POST /api/u1/v1/tiktok/creator/get_video_to_product_stats`

- 摘要：获取视频与商品关联统计数据/Get Video-Product Association Statistics
- 能力：创作者 / 作品详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_video_to_product_stats_api_v1_tiktok_creator_get_video_to_product_stats_post`
- 完整契约：[`api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-to-product-stats`](../api-contracts/tiktok-creator-api.md#post-api-u1-v1-tiktok-creator-get-video-to-product-stats)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie`:string, `proxy`:string, `start_date`:string, `item_id*`:string, `product_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 否 | 用户 Cookie 字符串/User Cookie String |
| proxy | string | 否 | 可选 HTTP 代理地址/Optional HTTP Proxy Address |
| start_date | string | 否 | 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' |
| item_id | string | 是 | 视频 ID/Video ID |
| product_id | string | 是 | 商品 ID/Product ID |

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
