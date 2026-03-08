# TikTok-Analytics-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/tiktok-analytics-api.md`
- 完整契约：[`api-contracts/tiktok-analytics-api.md`](../api-contracts/tiktok-analytics-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`4`
- 常见能力：数据分析 / 评论 / 创作者 / 作品详情
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`item_id`, `content_category`, `user_id`
- 标签说明：**(TikTok数据分析接口/TikTok-Analytics-API data analysis endpoints)**

## 路由列表

### `GET /api/u1/v1/tiktok/analytics/detect_fake_views`

- 摘要：检测视频虚假流量分析/Detect fake views in video
- 能力：数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`detect_fake_views_api_v1_tiktok_analytics_detect_fake_views_get`
- 完整契约：[`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-detect-fake-views`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-detect-fake-views)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id |
| content_category | query | string | 否 | 内容分类/Content category, options: default, entertainment, education, product, verified_large |

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

### `GET /api/u1/v1/tiktok/analytics/fetch_comment_keywords`

- 摘要：获取视频评论关键词分析/Get comment keywords analysis
- 能力：评论 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_comment_keywords_api_v1_tiktok_analytics_fetch_comment_keywords_get`
- 完整契约：[`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-comment-keywords`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-comment-keywords)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id |

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

### `GET /api/u1/v1/tiktok/analytics/fetch_creator_info_and_milestones`

- 摘要：获取创作者信息和里程碑数据/Get creator info and milestones
- 能力：创作者 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_creator_info_and_milestones_api_v1_tiktok_analytics_fetch_creator_info_and_milestones_get`
- 完整契约：[`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-creator-info-and-milestones`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-creator-info-and-milestones)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 用户id/User id |

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

### `GET /api/u1/v1/tiktok/analytics/fetch_video_metrics`

- 摘要：获取作品的统计数据/Get video metrics
- 能力：作品详情 / 数据分析
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_metrics_api_v1_tiktok_analytics_fetch_video_metrics_get`
- 完整契约：[`api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-video-metrics`](../api-contracts/tiktok-analytics-api.md#get-api-u1-v1-tiktok-analytics-fetch-video-metrics)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id |

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
