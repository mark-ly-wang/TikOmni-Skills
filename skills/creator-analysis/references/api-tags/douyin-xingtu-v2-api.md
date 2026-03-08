# Douyin-Xingtu-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-xingtu-v2-api.md`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md`](../api-contracts/douyin-xingtu-v2-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`21`
- 常见能力：创作者 / 通用能力 / 热点/榜单 / 评论 / 详情 / 主页/账号
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`o_author_id`, `platform_source`, `limit`, `platform_channel`, `author_id`, `only_assign`, `flow_type`, `page`, `qualifier`, `period`
- 标签说明：**(抖音星图V2数据接口/Douyin-Xingtu-V2-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_base_info`

- 摘要：获取创作者基本信息/Get Author Base Info
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_base_info_api_v1_douyin_xingtu_v2_get_author_base_info_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-base-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-base-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | 是 | 创作者ID/Creator author ID |
| platform_source | query | integer | 否 | 平台来源/Platform source |
| platform_channel | query | integer | 否 | 平台渠道/Platform channel |
| recommend | query | boolean | 否 | 是否返回推荐信息/Whether to return recommendation info |
| need_sec_uid | query | boolean | 否 | 是否返回sec_uid/Whether to return sec_uid |
| need_linkage_info | query | boolean | 否 | 是否返回联动信息/Whether to return linkage info |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_business_card_info`

- 摘要：获取创作者商业卡片信息/Get Author Business Card Info
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_business_card_info_api_v1_douyin_xingtu_v2_get_author_business_card_info_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-business-card-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-business-card-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | 是 | 创作者ID/Creator author ID |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_content_hot_keywords`

- 摘要：获取创作者内容热词/Get Author Content Hot Keywords
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_content_hot_keywords_api_v1_douyin_xingtu_v2_get_author_content_hot_keywords_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-content-hot-keywords`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-content-hot-keywords)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| author_id | query | string | 是 | 创作者ID/Creator author ID |
| keyword_type | query | integer | 否 | 热词类型/Keyword type |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_hot_comment_tokens`

- 摘要：获取创作者评论热词/Get Author Hot Comment Tokens
- 能力：评论 / 热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_hot_comment_tokens_api_v1_douyin_xingtu_v2_get_author_hot_comment_tokens_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-hot-comment-tokens`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-hot-comment-tokens)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| author_id | query | string | 是 | 创作者ID/Creator author ID |
| num | query | integer | 否 | 返回热词数量/Number of hot tokens |
| without_emoji | query | boolean | 否 | 是否排除emoji/Whether to exclude emoji |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_local_info`

- 摘要：获取创作者位置信息/Get Author Local Info
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_local_info_api_v1_douyin_xingtu_v2_get_author_local_info_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-local-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-local-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | 是 | 创作者ID/Creator author ID |
| platform_source | query | integer | 否 | 平台来源/Platform source |
| platform_channel | query | integer | 否 | 平台渠道/Platform channel |
| time_range | query | integer | 否 | 时间范围(天)/Time range in days |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_market_fields`

- 摘要：获取达人广场筛选字段/Get Author Market Fields
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_market_fields_api_v1_douyin_xingtu_v2_get_author_market_fields_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-market-fields`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-market-fields)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| market_scene | query | integer | 否 | 市场场景，1=默认场景/Market scene, 1=default |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_show_items`

- 摘要：获取创作者视频列表/Get Author Show Items
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_show_items_api_v1_douyin_xingtu_v2_get_author_show_items_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-show-items`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-show-items)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | 是 | 创作者ID/Creator author ID |
| platform_source | query | integer | 否 | 平台来源/Platform source |
| platform_channel | query | integer | 否 | 平台渠道/Platform channel |
| limit | query | integer | 否 | 返回数量/Result limit |
| only_assign | query | boolean | 否 | 仅看指派视频/Only show assigned videos |
| flow_type | query | integer | 否 | 流量类型/Flow type |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_author_spread_info`

- 摘要：获取创作者传播价值/Get Author Spread Info
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_author_spread_info_api_v1_douyin_xingtu_v2_get_author_spread_info_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-spread-info`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-author-spread-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| o_author_id | query | string | 是 | 创作者ID/Creator author ID |
| platform_source | query | integer | 否 | 平台来源/Platform source |
| platform_channel | query | integer | 否 | 平台渠道/Platform channel |
| type | query | integer | 否 | 视频类型，1=个人视频/Video type, 1=personal video |
| flow_type | query | integer | 否 | 流量类型/Flow type |
| only_assign | query | boolean | 否 | 仅看指派视频/Only assigned videos |
| range | query | integer | 否 | 时间范围，2=近30天，3=近90天/Time range, 2=last 30 days, 3=last 90 days |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_content_trend_guide`

- 摘要：获取内容趋势指南/Get Content Trend Guide
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_content_trend_guide_api_v1_douyin_xingtu_v2_get_content_trend_guide_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-content-trend-guide`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-content-trend-guide)

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_demander_mcn_list`

- 摘要：搜索MCN机构列表/Get Demander MCN List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_demander_mcn_list_api_v1_douyin_xingtu_v2_get_demander_mcn_list_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-demander-mcn-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-demander-mcn-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| mcn_name | query | string | 否 | MCN机构名称，支持模糊搜索/MCN name, supports fuzzy search |
| page | query | integer | 否 | 页码/Page number |
| limit | query | integer | 否 | 每页数量/Page size |
| order_by | query | string | 否 | 排序方式/Sort by |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_excellent_case_category_list`

- 摘要：获取优秀行业分类列表/Get Excellent Case Category List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_excellent_case_category_list_api_v1_douyin_xingtu_v2_get_excellent_case_category_list_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-excellent-case-category-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-excellent-case-category-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| platform_source | query | integer | 否 | 平台来源/Platform source |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_detail`

- 摘要：获取星图IP活动详情/Get IP Activity Detail
- 能力：详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ip_activity_detail_api_v1_douyin_xingtu_v2_get_ip_activity_detail_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-detail`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | query | integer | 是 | 活动ID，从get_ip_activity_list获取/Activity ID from get_ip_activity_list |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ip_activity_industry_list`

- 摘要：获取星图IP日历行业列表/Get IP Activity Industry List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ip_activity_industry_list_api_v1_douyin_xingtu_v2_get_ip_activity_industry_list_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-industry-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ip-activity-industry-list)

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

### `POST /api/u1/v1/douyin/xingtu_v2/get_ip_activity_list`

- 摘要：获取星图IP日历活动列表/Get IP Activity List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ip_activity_list_api_v1_douyin_xingtu_v2_get_ip_activity_list_post`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-ip-activity-list`](../api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-ip-activity-list)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`query_start_time*`:string, `query_end_time*`:string, `industry_id_list`[string], `category_list`[integer], `status_list`[integer]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query_start_time | string | 是 | 查询开始时间戳/Query start timestamp |
| query_end_time | string | 是 | 查询结束时间戳/Query end timestamp |
| industry_id_list | array<string> | 否 | 行业ID列表/Industry ID list |
| category_list | array<integer> | 否 | IP类型列表/IP category list |
| status_list | array<integer> | 否 | IP状态列表/IP status list |

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

### `POST /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog`

- 摘要：获取短剧演员热榜分类/Get Playlet Actor Rank Catalog
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_playlet_actor_rank_catalog_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_catalog_post`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-catalog`](../api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-catalog)

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_playlet_actor_rank_list`

- 摘要：获取短剧演员热榜/Get Playlet Actor Rank List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_playlet_actor_rank_list_api_v1_douyin_xingtu_v2_get_playlet_actor_rank_list_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-playlet-actor-rank-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| category | query | string | 否 | 分类/Category |
| name | query | string | 否 | 榜单名称/Ranking name |
| qualifier | query | string | 否 | 达人类型，空字符串=不限/Actor type, empty=all |
| period | query | integer | 否 | 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly |
| date | query | string | 否 | 统计日期，格式YYYYMMDD/Date, format YYYYMMDD |
| limit | query | integer | 否 | 返回数量/Result limit |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_catalog`

- 摘要：获取星图热榜分类/Get Ranking List Catalog
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ranking_list_catalog_api_v1_douyin_xingtu_v2_get_ranking_list_catalog_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-catalog`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-catalog)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| codes | query | string | 否 | 分类代码，默认为空字符串/Classification codes, default is empty string |
| biz_scene | query | string | 否 | 业务场景/Business scene |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_ranking_list_data`

- 摘要：获取星图达人商业榜数据/Get Ranking List Data
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_ranking_list_data_api_v1_douyin_xingtu_v2_get_ranking_list_data_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-data`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-ranking-list-data)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| code | query | integer | 否 | 榜单类型代码/Ranking type code |
| qualifier | query | string | 否 | 榜单分类ID，从get_ranking_list_catalog获取/Category qualifier_id |
| version | query | string | 否 | 版本/Version |
| period | query | integer | 否 | 统计周期，7=周榜，30=月榜/Period, 7=weekly, 30=monthly |
| date | query | string | 否 | 统计日期，格式YYYYMMDD/Date, format YYYYMMDD |
| limit | query | integer | 否 | 返回数量/Result limit |

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

### `POST /api/u1/v1/douyin/xingtu_v2/get_recommend_for_star_authors`

- 摘要：获取相似创作者推荐/Get Recommend Similar Star Authors
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_recommend_for_star_authors_api_v1_douyin_xingtu_v2_get_recommend_for_star_authors_post`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-recommend-for-star-authors`](../api-contracts/douyin-xingtu-v2-api.md#post-api-u1-v1-douyin-xingtu-v2-get-recommend-for-star-authors)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`author_ids*`[string], `similar_type`:string, `page`:integer, `limit`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| author_ids | array<string> | 是 | 创作者ID列表/List of creator author IDs |
| similar_type | string | 否 | 相似类型/Similarity type |
| page | integer | 否 | 页码/Page number |
| limit | integer | 否 | 每页数量/Page size |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_resource_list`

- 摘要：获取营销活动案例/Get Resource List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_resource_list_api_v1_douyin_xingtu_v2_get_resource_list_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-resource-list`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-resource-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| resource_id | query | integer | 是 | 资源ID/Resource ID |

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

### `GET /api/u1/v1/douyin/xingtu_v2/get_user_profile_qrcode`

- 摘要：获取用户主页二维码/Get User Profile QRCode
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_user_profile_qrcode_api_v1_douyin_xingtu_v2_get_user_profile_qrcode_get`
- 完整契约：[`api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-user-profile-qrcode`](../api-contracts/douyin-xingtu-v2-api.md#get-api-u1-v1-douyin-xingtu-v2-get-user-profile-qrcode)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| core_user_id | query | string | 否 | 用户核心ID(与sec_uid二选一)/User core ID (pick one with sec_uid) |
| sec_uid | query | string | 否 | 用户sec_uid(与core_user_id二选一)/User sec_uid (pick one with core_user_id) |

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
