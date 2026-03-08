# Douyin-Creator-V2-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/douyin-creator-v2-api.md`
- Full contract: [`api-contracts/douyin-creator-v2-api.md`](../api-contracts/douyin-creator-v2-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `14`
- Common capabilities: creators / media / download / search / trends / rankings / livestream
- Default auth: Header `Authorization` Bearer
- Common inputs: `cookie`, `item_id`, `start_date`, `end_date`, `genres`, `primary_verticals`, `fields`, `need_long_article`, `metric_type`, `count`
- Tag description: **(抖音创作者V2数据接口（需要用户Cookie，可获取作品流量总览等数据）/Douyin-Creator-V2-API data endpoints (Requires user Cookie, can get item traffic overview data))**

## Routes

### `POST /api/u1/v1/douyin/creator_v2/fetch_author_diagnosis`

- Summary: 获取创作者账号诊断/Fetch author diagnosis
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_author_diagnosis_api_v1_douyin_creator_v2_fetch_author_diagnosis_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-author-diagnosis`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-author-diagnosis)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical`

- Summary: 获取作品垂类标签/Fetch item analysis involved vertical
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_analysis_involved_vertical_api_v1_douyin_creator_v2_fetch_item_analysis_involved_vertical_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-involved-vertical`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-involved-vertical)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `start_date*`:string, `end_date*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| start_date | string | Yes | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) |
| end_date | string | Yes | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_item_performance`

- Summary: 获取投稿表现数据/Fetch item analysis item performance
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_analysis_item_performance_api_v1_douyin_creator_v2_fetch_item_analysis_item_performance_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-item-performance`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-item-performance)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string], `metric_type`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| start_date | string | Yes | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) |
| end_date | string | Yes | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) |
| genres | array<integer> | No | 体裁类型列表/Genres list: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 |
| primary_verticals | array<string> | Yes | 垂类标签列表/Primary verticals list (从involved_vertical接口获取) |
| metric_type | integer | No | 指标类型/Metric type: 1=播放量(Views), 2=点赞量(Likes), 3=评论量(Comments), 4=分享量(Shares) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_analysis_overview`

- Summary: 获取投稿分析概览/Fetch item analysis overview
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_analysis_overview_api_v1_douyin_creator_v2_fetch_item_analysis_overview_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-overview`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-analysis-overview)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `start_date*`:string, `end_date*`:string, `genres`[integer], `primary_verticals*`[string]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| start_date | string | Yes | 开始日期(格式YYYYMMDD)/Start date (format YYYYMMDD) |
| end_date | string | Yes | 结束日期(格式YYYYMMDD)/End date (format YYYYMMDD) |
| genres | array<integer> | No | 体裁类型列表/Genres list: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 |
| primary_verticals | array<string> | Yes | 垂类标签列表/Primary verticals list (从involved_vertical接口获取) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_others`

- Summary: 获取作品观众其他数据分析/Fetch item audience others analysis
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_audience_others_api_v1_douyin_creator_v2_fetch_item_audience_others_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-others`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-others)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `item_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| item_id | string | Yes | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_audience_portrait`

- Summary: 获取作品观众数据分析/Fetch item audience portrait
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_audience_portrait_api_v1_douyin_creator_v2_fetch_item_audience_portrait_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-portrait`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-audience-portrait)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `item_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| item_id | string | Yes | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_danmaku_analysis`

- Summary: 获取作品弹幕分析/Fetch item bullet analysis
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_danmaku_analysis_api_v1_douyin_creator_v2_fetch_item_danmaku_analysis_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-danmaku-analysis`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-danmaku-analysis)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `item_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| item_id | string | Yes | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list`

- Summary: 获取投稿作品列表/Fetch item list
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_list_api_v1_douyin_creator_v2_fetch_item_list_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `count`:integer, `order_by`:integer, `fields`:string, `need_cooperation`:boolean, `start_time*`:integer, `end_time*`:integer, `need_long_article`:boolean, ...

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| count | integer | No | 每页数量/Count per page (最多100条) |
| order_by | integer | No | 排序方式/Order by (1-26): 1=发布时间↓(新到旧), 2=发布时间↑(旧到新), 3=播放量↓, 4=播放量↑, 5=点赞量↓, 6=点赞量↑, 7=评论量↓, 8=评论量↑, 9=分享量↓, 10=分享量↑, 11=收… |
| fields | string | No | 需要返回的字段/Fields to return |
| need_cooperation | boolean | No | 是否需要合作信息/Need cooperation info |
| start_time | integer | Yes | 开始时间戳(毫秒)/Start time timestamp (milliseconds) |
| end_time | integer | Yes | 结束时间戳(毫秒)/End time timestamp (milliseconds) |
| need_long_article | boolean | No | 是否包含长图文/Include long articles |
| cursor | integer | No | 分页游标/Pagination cursor (可选) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_list_download`

- Summary: 导出投稿作品列表/Download item list
- Capabilities: creators / media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_list_download_api_v1_douyin_creator_v2_fetch_item_list_download_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list-download`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-list-download)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `min_cursor*`:integer, `max_cursor*`:integer, `type_filters`[integer], `need_long_article`:boolean

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| min_cursor | integer | Yes | 最小游标(开始时间戳,毫秒)/Min cursor (start timestamp in milliseconds) |
| max_cursor | integer | Yes | 最大游标(结束时间戳,毫秒)/Max cursor (end timestamp in milliseconds) |
| type_filters | array<integer> | No | 体裁类型过滤/Type filters: 1=1min以内视频, 2=1-3min视频, 3=3-5min视频, 4=5min+视频, 5=图文, 8=长图文 |
| need_long_article | boolean | No | 是否包含长图文/Include long articles |

#### Success Response

##### `200 application/json`

- Schema summary: No declared structure

No field table

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_overview_data`

- Summary: 获取作品总览数据/Fetch item overview data
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_overview_data_api_v1_douyin_creator_v2_fetch_item_overview_data_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-overview-data`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-overview-data)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `ids*`:string, `fields`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| ids | string | Yes | 作品ID列表,多个ID用逗号分隔/Item IDs, separated by comma |
| fields | string | No | 需要返回的字段,多个字段用逗号分隔/Fields to return, separated by comma. 可选值: metrics(指标),review(审核),play_info(播放信息),dou_plus(抖+),integr… |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_play_source`

- Summary: 获取作品流量来源统计/Fetch item play source statistics
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_play_source_api_v1_douyin_creator_v2_fetch_item_play_source_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-play-source`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-play-source)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `item_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| item_id | string | Yes | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_search_keyword`

- Summary: 获取作品搜索关键词统计/Fetch item search keywords statistics
- Capabilities: search / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_search_keyword_api_v1_douyin_creator_v2_fetch_item_search_keyword_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-search-keyword`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-search-keyword)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `item_id*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| item_id | string | Yes | 作品ID/Item ID |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_item_watch_trend`

- Summary: 获取作品观看趋势分析/Fetch item watch trend analysis
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_item_watch_trend_api_v1_douyin_creator_v2_fetch_item_watch_trend_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-watch-trend`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-item-watch-trend)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `item_id*`:string, `analysis_type`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| item_id | string | Yes | 作品ID/Item ID |
| analysis_type | integer | No | 分析类型/Analysis type: 1=留存分析(Retention), 2=点赞分析(Like), 7=跳出分析(Bounce) |

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

### `POST /api/u1/v1/douyin/creator_v2/fetch_live_room_history_list`

- Summary: 获取直播场次历史记录/Fetch live room history list
- Capabilities: creators / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_room_history_list_api_v1_douyin_creator_v2_fetch_live_room_history_list_post`
- Full contract: [`api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-live-room-history-list`](../api-contracts/douyin-creator-v2-api.md#post-api-u1-v1-douyin-creator-v2-fetch-live-room-history-list)

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie*`:string, `start_date*`:string, `end_date*`:string, `limit`:integer, `need_living`:integer, `download`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| cookie | string | Yes | 用户Cookie/User Cookie |
| start_date | string | Yes | 开始日期(格式YYYY-MM-DD)/Start date (format YYYY-MM-DD) |
| end_date | string | Yes | 结束日期(格式YYYY-MM-DD)/End date (format YYYY-MM-DD) |
| limit | integer | No | 每页数量限制/Limit per page (最多400条) |
| need_living | integer | No | 是否包含正在直播的场次/Include living rooms: 0=不包含, 1=包含 |
| download | integer | No | 是否下载/Download: 0=不下载, 1=下载 |

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
