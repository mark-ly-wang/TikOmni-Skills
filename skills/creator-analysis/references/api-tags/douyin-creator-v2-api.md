# Douyin-Creator-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-creator-v2-api.md`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md`](../api-contracts/douyin-creator-v2-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`14`
- 常见能力：创作者 / 下载/媒体 / 搜索 / 热点/榜单 / 直播
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`cookie`, `item_id`, `start_date`, `end_date`, `genres`, `primary_verticals`, `fields`, `need_long_article`, `metric_type`, `count`
- 标签说明：**(抖音创作者V2数据接口（需要用户Cookie，可获取作品流量总览等数据）/Douyin-Creator-V2-API data endpoints (Requires user Cookie, can get item traffic overview data))**

## 路由列表

### `POST /api/u1/v1/douyin/creator_v2/fetch_author_diagnosis`

- 摘要：获取创作者账号诊断/Fetch author diagnosis
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_author_diagnosis_api_v1_douyin_creator_v2_fetch_author_diagnosis_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-author-diagnosis`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-author-diagnosis)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical`

- 摘要：获取作品垂类标签/Fetch item analysis involved vertical
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_analysis_involved_vertical_api_v1_douyin_creator_v2_fetch_item_analysis_involved_vertical_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-involved-vertical`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-involved-vertical)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| start_date | string | 是 | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) |
| end_date | string | 是 | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_item_performance`

- 摘要：获取投稿表现数据/Fetch item analysis item performance
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_analysis_item_performance_api_v1_douyin_creator_v2_fetch_item_analysis_item_performance_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-item-performance`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-item-performance)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string], `metric_type`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| start_date | string | 是 | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) |
| end_date | string | 是 | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) |
| genres | array<integer> | 否 | 体裁类型列表/Genres list: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 |
| primary_verticals | array<string> | 是 | 垂类标签列表/Primary verticals list (从involved_vertical接口获取) |
| metric_type | integer | 否 | 指标类型/Metric type: 1=播放量(Views), 2=点赞量(Likes), 3=评论量(Comments), 4=分享量(Shares) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_overview`

- 摘要：获取投稿分析概览/Fetch item analysis overview
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_analysis_overview_api_v1_douyin_creator_v2_fetch_item_analysis_overview_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-overview`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-overview)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| start_date | string | 是 | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) |
| end_date | string | 是 | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) |
| genres | array<integer> | 否 | 体裁类型列表/Genres list: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 |
| primary_verticals | array<string> | 是 | 垂类标签列表/Primary verticals list (从involved_vertical接口获取) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_others`

- 摘要：获取作品观众其他数据分析/Fetch item audience others analysis
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_audience_others_api_v1_douyin_creator_v2_fetch_item_audience_others_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-others`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-others)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| item_id | string | 是 | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_portrait`

- 摘要：获取作品观众数据分析/Fetch item audience portrait
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_audience_portrait_api_v1_douyin_creator_v2_fetch_item_audience_portrait_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-portrait`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-portrait)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| item_id | string | 是 | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_danmaku_analysis`

- 摘要：获取作品弹幕分析/Fetch item bullet analysis
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_danmaku_analysis_api_v1_douyin_creator_v2_fetch_item_danmaku_analysis_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-danmaku-analysis`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-danmaku-analysis)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| item_id | string | 是 | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list`

- 摘要：获取投稿作品列表/Fetch item list
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_list_api_v1_douyin_creator_v2_fetch_item_list_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `count`:integer, `order_by`:integer, `fields`:string, `need_cooperation`:boolean, `start_time*`:integer, `end_time*`:integer, `need_long_article`:boolean, ...

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| count | integer | 否 | 每页数量/Count per page (最多100条) |
| order_by | integer | 否 | 排序方式/Order by (1-26): 1=发布时间↓(新到旧), 2=发布时间↑(旧到新), 3=播放量↓, 4=播放量↑, 5=点赞量↓, 6=点赞量↑, 7=评论量↓, 8=评论量↑, 9=分享量↓, 10=分享量↑, 11=收… |
| fields | string | 否 | 需要返回的字段/Fields to return |
| need_cooperation | boolean | 否 | 是否需要合作信息/Need cooperation info |
| start_time | integer | 是 | 开始时间戳(毫秒)/Start time timestamp (milliseconds) |
| end_time | integer | 是 | 结束时间戳(毫秒)/End time timestamp (milliseconds) |
| need_long_article | boolean | 否 | 是否包含长图文/Include long articles |
| cursor | integer | 否 | 分页游标/Pagination cursor (可选) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list_download`

- 摘要：导出投稿作品列表/Download item list
- 能力：创作者 / 下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_list_download_api_v1_douyin_creator_v2_fetch_item_list_download_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list-download`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list-download)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `min_cursor*`:integer, `max_cursor*`:integer, `type_filters`[integer], `need_long_article`:boolean

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| min_cursor | integer | 是 | 最小游标(开始时间戳,毫秒)/Min cursor (start timestamp in milliseconds) |
| max_cursor | integer | 是 | 最大游标(结束时间戳,毫秒)/Max cursor (end timestamp in milliseconds) |
| type_filters | array<integer> | 否 | 体裁类型过滤/Type filters: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 |
| need_long_article | boolean | 否 | 是否包含长图文/Include long articles |

#### 成功响应

##### `200 application/json`

- Schema 摘要：无结构声明

无字段表

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_overview_data`

- 摘要：获取作品总览数据/Fetch item overview data
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_overview_data_api_v1_douyin_creator_v2_fetch_item_overview_data_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-overview-data`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-overview-data)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `ids*`:string, `fields`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| ids | string | 是 | 作品ID列表,多个ID用逗号分隔/Item IDs, separated by comma |
| fields | string | 否 | 需要返回的字段,多个字段用逗号分隔/Fields to return, separated by comma. 可选值: metrics(指标),review(审核),play_info(播放信息),dou_plus(抖+),integr… |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_play_source`

- 摘要：获取作品流量来源统计/Fetch item play source statistics
- 能力：创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_play_source_api_v1_douyin_creator_v2_fetch_item_play_source_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-play-source`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-play-source)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| item_id | string | 是 | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_search_keyword`

- 摘要：获取作品搜索关键词统计/Fetch item search keywords statistics
- 能力：搜索 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_search_keyword_api_v1_douyin_creator_v2_fetch_item_search_keyword_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-search-keyword`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-search-keyword)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| item_id | string | 是 | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_watch_trend`

- 摘要：获取作品观看趋势分析/Fetch item watch trend analysis
- 能力：热点/榜单 / 创作者
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_item_watch_trend_api_v1_douyin_creator_v2_fetch_item_watch_trend_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-watch-trend`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-watch-trend)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `item_id*`:string, `analysis_type`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| item_id | string | 是 | 作品ID/Item ID |
| analysis_type | integer | 否 | 分析类型/Analysis type: 1=留存分析(Retention), 2=点赞分析(Like), 7=跳出分析(Bounce) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_live_room_history_list`

- 摘要：获取直播场次历史记录/Fetch live room history list
- 能力：创作者 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_room_history_list_api_v1_douyin_creator_v2_fetch_live_room_history_list_post`
- 完整契约：[`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-live-room-history-list`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-live-room-history-list)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `start_date*`:string, `end_date*`:string, `limit`:integer, `need_living`:integer, `download`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cookie | string | 是 | 用户Cookie/User Cookie |
| start_date | string | 是 | 开始日期(格式YYYY-MM-DD)/Start date (format YYYY-MM-DD) |
| end_date | string | 是 | 结束日期(格式YYYY-MM-DD)/End date (format YYYY-MM-DD) |
| limit | integer | 否 | 每页数量限制/Limit per page (最多400条) |
| need_living | integer | 否 | 是否包含正在直播的场次/Include living rooms: 0=不包含, 1=包含 |
| download | integer | 否 | 是否下载/Download: 0=不下载, 1=下载 |

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
