# Douyin-Billboard-API Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/douyin-billboard-api.md`
- Full contract: [`api-contracts/douyin-billboard-api.md`](../api-contracts/douyin-billboard-api.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `31`
- Common capabilities: trends / rankings / search / topics / details / comments / content details
- Default auth: Header `Authorization` Bearer
- Common inputs: `page_size`, `date_window`, `page`, `keyword`, `tags`, `sec_uid`, `option`, `page_num`, `end_date`, `start_date`
- Tag description: **(抖音热点榜数据接口/Douyin-Billboard-API data endpoints)**

## Routes

### `GET /api/u1/v1/douyin/billboard/fetch_city_list`

- Summary: 获取中国城市列表/Fetch Chinese city list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-city-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-city-list)

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

### `GET /api/u1/v1/douyin/billboard/fetch_content_tag`

- Summary: 获取垂类内容标签/Fetch vertical content tags
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-content-tag`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-content-tag)

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list`

- Summary: 获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-account-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-account-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list`

- Summary: 获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-search-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-search-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list`

- Summary: 获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-topic-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-topic-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_portrait_list`

- Summary: 获取粉丝画像/Fetch fan portrait
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-portrait-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-portrait-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id |
| option | query | integer | No | 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 8 兴趣标签分析 百分比 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_item_analysis_list`

- Summary: 获取账号作品分析-上周/Fetch account work analysis - last week
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-item-analysis-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-item-analysis-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_account_list`

- Summary: 获取热门账号/Fetch hot account list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-account-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-account-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `date_window`:integer, `page_num`:integer, `page_size`:integer, `query_tag`{...}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| date_window | integer | No | 时间窗口，格式 小时，默认24小时 |
| page_num | integer | No | 页码，默认1 |
| page_size | integer | No | 每页数量，默认10 |
| query_tag | object | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_search_list`

- Summary: 搜索用户名或抖音号/Fetch account search list
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-search-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-search-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索的用户名或抖音号 |
| cursor | query | integer | Yes | 游标，默认空 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_trends_list`

- Summary: 获取账号粉丝数据趋势/Fetch account fan data trend
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-trends-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-trends-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_id |
| option | query | integer | No | 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量 |
| date_window | query | integer | No | 时间窗口，1 按小时 2 按天 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_calendar_detail`

- Summary: 获取活动日历详情/Fetch activity calendar detail
- Capabilities: trends / rankings / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-calendar-detail`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-calendar-detail)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| calendar_id | query | string | Yes | 活动id |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_calendar_list`

- Summary: 获取活动日历/Fetch activity calendar
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-calendar-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-calendar-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `city_code`:string, `category_code`:string, `end_date`:integer, `start_date`:integer

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| city_code | string | No | 城市编码，从城市列表获取，空为全部 |
| category_code | string | No | 热点榜分类编码，从热点榜分类获取，空为全部 |
| end_date | integer | No | 快照结束时间 格式10位时间戳 |
| start_date | integer | No | 快照开始时间 格式10位时间戳 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_category_list`

- Summary: 获取热点榜分类/Fetch hot list category
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-category-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-category-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| billboard_type | query | string | Yes | 榜单类型 |
| snapshot_time | query | string | No | 快照时间 格式yyyyMMddHHmmss |
| start_date | query | string | No | 快照开始时间 格式yyyyMMdd |
| end_date | query | string | No | 快照结束时间 格式yyyyMMdd |
| keyword | query | string | No | 热点搜索词 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_challenge_list`

- Summary: 获取挑战热榜/Fetch hot challenge list
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-challenge-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-challenge-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 |
| page_size | query | integer | Yes | 每页数量 |
| keyword | query | string | No | 热点搜索词 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_city_list`

- Summary: 获取同城热点榜/Fetch city hot list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-city-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-city-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 |
| page_size | query | integer | Yes | 每页数量 |
| order | query | string | Yes | 排序方式 |
| city_code | query | string | No | 城市编码，从城市列表获取，空为全部 |
| sentence_tag | query | string | No | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 |
| keyword | query | string | No | 热点搜索词 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_comment_word_list`

- Summary: 获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight
- Capabilities: comments / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-comment-word-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-comment-word-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_item_trends_list`

- Summary: 获取作品数据趋势/Fetch post data trend
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-item-trends-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-item-trends-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | No | 作品id |
| option | query | integer | No | 选项，7 点赞量 8 分享量 9 评论量 |
| date_window | query | integer | No | 时间窗口，1 按小时 2 按天 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_rise_list`

- Summary: 获取上升热点榜/Fetch rising hot list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-rise-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-rise-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 |
| page_size | query | integer | Yes | 每页数量 |
| order | query | string | Yes | 排序方式 |
| sentence_tag | query | string | No | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 |
| keyword | query | string | No | 热点搜索词 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_fan_list`

- Summary: 获取高涨粉率榜/Fetch high fan rate list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-fan-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-fan-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | Yes | None |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_like_list`

- Summary: 获取高点赞率榜/Fetch high like rate list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-like-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-like-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | Yes | None |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_play_list`

- Summary: 获取高完播率榜/Fetch high completion rate list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-play-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-play-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | Yes | None |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_search_list`

- Summary: 获取热度飙升的搜索榜/Fetch search list with rising popularity
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-search-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-search-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page_num | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| keyword | string | No | 搜索关键字 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_topic_list`

- Summary: 获取热度飙升的话题榜/Fetch topic list with rising popularity
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-topic-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-topic-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | Yes | None |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list`

- Summary: 获取内容词详情/Fetch content word details
- Capabilities: trends / rankings / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-detail-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-detail-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键字 |
| word_id | query | string | Yes | 内容词id |
| query_day | query | integer | Yes | 查询日期，格式为YYYYMMDD，需为当日 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_list`

- Summary: 获取全部热门内容词/Fetch all hot content words
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page_num | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| keyword | string | No | 搜索关键字 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_list`

- Summary: 获取热点总榜/Fetch total hot list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| page | query | integer | Yes | 页码 |
| page_size | query | integer | Yes | 每页数量 |
| type | query | string | Yes | 快照类型 snapshot 按时刻查看 range 按时间范围 |
| snapshot_time | query | string | No | 快照时间 格式yyyyMMddHHmmss |
| start_date | query | string | No | 快照开始时间 格式yyyyMMdd |
| end_date | query | string | No | 快照结束时间 格式yyyyMMdd |
| sentence_tag | query | string | No | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 |
| keyword | query | string | No | 热点搜索词 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_low_fan_list`

- Summary: 获取低粉爆款榜/Fetch low fan explosion list
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-low-fan-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-low-fan-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | Yes | None |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_search_list`

- Summary: 获取搜索热榜/Fetch search hot list
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-search-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-search-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page_num | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| keyword | string | No | 搜索关键字 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_topic_list`

- Summary: 获取话题热榜/Fetch topic hot list
- Capabilities: trends / rankings / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-topic-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-topic-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page | integer | No | 页码 |
| page_size | integer | No | 每页数量 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | Yes | None |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_video_list`

- Summary: 获取视频热榜/Fetch video hot list
- Capabilities: trends / rankings / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post`
- Full contract: [`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-video-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-video-list)

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `page`:integer, `page_size`:integer, `date_window`:integer, `sub_type`:integer, `tags`[object]

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| page | integer | No | 页码，默认1 |
| page_size | integer | No | 每页数量，默认10 |
| date_window | integer | No | 时间窗口，1 按小时 2 按天 |
| sub_type | integer | No | 榜单分类，1001 视频总榜 1002 低粉爆款 1003 高完播率 1004 高涨粉率 1005 高点赞率 |
| tags | array<object> | No | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | Yes | None |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_user_portrait_list`

- Summary: 获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only
- Capabilities: trends / rankings / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get`
- Full contract: [`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-user-portrait-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-user-portrait-list)

#### Parameters

| Field | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id |
| option | query | integer | No | 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 |

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
