# Douyin-Billboard-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/douyin-billboard-api.md`
- 完整契约：[`api-contracts/douyin-billboard-api.md`](../api-contracts/douyin-billboard-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`31`
- 常见能力：热点/榜单 / 搜索 / 话题 / 详情 / 评论 / 作品详情
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`page_size`, `date_window`, `page`, `keyword`, `tags`, `sec_uid`, `option`, `page_num`, `end_date`, `start_date`
- 标签说明：**(抖音热点榜数据接口/Douyin-Billboard-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/douyin/billboard/fetch_city_list`

- 摘要：获取中国城市列表/Fetch Chinese city list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_city_list_api_v1_douyin_billboard_fetch_city_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-city-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-city-list)

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

### `GET /api/u1/v1/douyin/billboard/fetch_content_tag`

- 摘要：获取垂类内容标签/Fetch vertical content tags
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_content_tag_api_v1_douyin_billboard_fetch_content_tag_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-content-tag`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-content-tag)

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list`

- 摘要：获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_fans_interest_account_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_account_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-account-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-account-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list`

- 摘要：获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_fans_interest_search_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_search_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-search-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-search-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list`

- 摘要：获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics
- 能力：热点/榜单 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_fans_interest_topic_list_api_v1_douyin_billboard_fetch_hot_account_fans_interest_topic_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-topic-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-interest-topic-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_fans_portrait_list`

- 摘要：获取粉丝画像/Fetch fan portrait
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_fans_portrait_list_api_v1_douyin_billboard_fetch_hot_account_fans_portrait_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-portrait-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-fans-portrait-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_id |
| option | query | integer | 否 | 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 8 兴趣标签分析 百分比 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_item_analysis_list`

- 摘要：获取账号作品分析-上周/Fetch account work analysis - last week
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_item_analysis_list_api_v1_douyin_billboard_fetch_hot_account_item_analysis_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-item-analysis-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-item-analysis-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_id |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_account_list`

- 摘要：获取热门账号/Fetch hot account list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-account-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-account-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`date_window`:integer, `page_num`:integer, `page_size`:integer, `query_tag`{...}

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date_window | integer | 否 | 时间窗口，格式 小时，默认24小时 |
| page_num | integer | 否 | 页码，默认1 |
| page_size | integer | 否 | 每页数量，默认10 |
| query_tag | object | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_search_list`

- 摘要：搜索用户名或抖音号/Fetch account search list
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_search_list_api_v1_douyin_billboard_fetch_hot_account_search_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-search-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-search-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索的用户名或抖音号 |
| cursor | query | integer | 是 | 游标，默认空 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_account_trends_list`

- 摘要：获取账号粉丝数据趋势/Fetch account fan data trend
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_account_trends_list_api_v1_douyin_billboard_fetch_hot_account_trends_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-trends-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-account-trends-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_id |
| option | query | integer | 否 | 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量 |
| date_window | query | integer | 否 | 时间窗口，1 按小时 2 按天 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_calendar_detail`

- 摘要：获取活动日历详情/Fetch activity calendar detail
- 能力：热点/榜单 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_calendar_detail_api_v1_douyin_billboard_fetch_hot_calendar_detail_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-calendar-detail`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-calendar-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| calendar_id | query | string | 是 | 活动id |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_calendar_list`

- 摘要：获取活动日历/Fetch activity calendar
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-calendar-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-calendar-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`city_code`:string, `category_code`:string, `end_date`:integer, `start_date`:integer

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| city_code | string | 否 | 城市编码，从城市列表获取，空为全部 |
| category_code | string | 否 | 热点榜分类编码，从热点榜分类获取，空为全部 |
| end_date | integer | 否 | 快照结束时间 格式10位时间戳 |
| start_date | integer | 否 | 快照开始时间 格式10位时间戳 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_category_list`

- 摘要：获取热点榜分类/Fetch hot list category
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_category_list_api_v1_douyin_billboard_fetch_hot_category_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-category-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-category-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| billboard_type | query | string | 是 | 榜单类型 |
| snapshot_time | query | string | 否 | 快照时间 格式yyyyMMddHHmmss |
| start_date | query | string | 否 | 快照开始时间 格式yyyyMMdd |
| end_date | query | string | 否 | 快照结束时间 格式yyyyMMdd |
| keyword | query | string | 否 | 热点搜索词 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_challenge_list`

- 摘要：获取挑战热榜/Fetch hot challenge list
- 能力：热点/榜单 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_challenge_list_api_v1_douyin_billboard_fetch_hot_challenge_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-challenge-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-challenge-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | query | integer | 是 | 页码 |
| page_size | query | integer | 是 | 每页数量 |
| keyword | query | string | 否 | 热点搜索词 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_city_list`

- 摘要：获取同城热点榜/Fetch city hot list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_city_list_api_v1_douyin_billboard_fetch_hot_city_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-city-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-city-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | query | integer | 是 | 页码 |
| page_size | query | integer | 是 | 每页数量 |
| order | query | string | 是 | 排序方式 |
| city_code | query | string | 否 | 城市编码，从城市列表获取，空为全部 |
| sentence_tag | query | string | 否 | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 |
| keyword | query | string | 否 | 热点搜索词 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_comment_word_list`

- 摘要：获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight
- 能力：评论 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_comment_word_list_api_v1_douyin_billboard_fetch_hot_comment_word_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-comment-word-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-comment-word-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_item_trends_list`

- 摘要：获取作品数据趋势/Fetch post data trend
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_item_trends_list_api_v1_douyin_billboard_fetch_hot_item_trends_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-item-trends-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-item-trends-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 否 | 作品id |
| option | query | integer | 否 | 选项，7 点赞量 8 分享量 9 评论量 |
| date_window | query | integer | 否 | 时间窗口，1 按小时 2 按天 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_rise_list`

- 摘要：获取上升热点榜/Fetch rising hot list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_rise_list_api_v1_douyin_billboard_fetch_hot_rise_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-rise-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-rise-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | query | integer | 是 | 页码 |
| page_size | query | integer | 是 | 每页数量 |
| order | query | string | 是 | 排序方式 |
| sentence_tag | query | string | 否 | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 |
| keyword | query | string | 否 | 热点搜索词 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_fan_list`

- 摘要：获取高涨粉率榜/Fetch high fan rate list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_high_fan_list_api_v1_douyin_billboard_fetch_hot_total_high_fan_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-fan-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-fan-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | 是 | 无 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_like_list`

- 摘要：获取高点赞率榜/Fetch high like rate list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_high_like_list_api_v1_douyin_billboard_fetch_hot_total_high_like_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-like-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-like-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | 是 | 无 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_play_list`

- 摘要：获取高完播率榜/Fetch high completion rate list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_high_play_list_api_v1_douyin_billboard_fetch_hot_total_high_play_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-play-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-play-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | 是 | 无 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_search_list`

- 摘要：获取热度飙升的搜索榜/Fetch search list with rising popularity
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-search-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-search-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page_num | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| keyword | string | 否 | 搜索关键字 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_high_topic_list`

- 摘要：获取热度飙升的话题榜/Fetch topic list with rising popularity
- 能力：热点/榜单 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_high_topic_list_api_v1_douyin_billboard_fetch_hot_total_high_topic_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-topic-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-high-topic-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | 是 | 无 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list`

- 摘要：获取内容词详情/Fetch content word details
- 能力：热点/榜单 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_hot_word_detail_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_detail_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-detail-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-detail-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键字 |
| word_id | query | string | 是 | 内容词id |
| query_day | query | integer | 是 | 查询日期，格式为YYYYMMDD，需为当日 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_hot_word_list`

- 摘要：获取全部热门内容词/Fetch all hot content words
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_hot_word_list_api_v1_douyin_billboard_fetch_hot_total_hot_word_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-hot-word-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page_num | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| keyword | string | 否 | 搜索关键字 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_total_list`

- 摘要：获取热点总榜/Fetch total hot list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_list_api_v1_douyin_billboard_fetch_hot_total_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-total-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | query | integer | 是 | 页码 |
| page_size | query | integer | 是 | 每页数量 |
| type | query | string | 是 | 快照类型 snapshot 按时刻查看 range 按时间范围 |
| snapshot_time | query | string | 否 | 快照时间 格式yyyyMMddHHmmss |
| start_date | query | string | 否 | 快照开始时间 格式yyyyMMdd |
| end_date | query | string | 否 | 快照结束时间 格式yyyyMMdd |
| sentence_tag | query | string | 否 | 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 |
| keyword | query | string | 否 | 热点搜索词 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_low_fan_list`

- 摘要：获取低粉爆款榜/Fetch low fan explosion list
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-low-fan-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-low-fan-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | 是 | 无 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_search_list`

- 摘要：获取搜索热榜/Fetch search hot list
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_search_list_api_v1_douyin_billboard_fetch_hot_total_search_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-search-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-search-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page_num`:integer, `page_size`:integer, `date_window`:integer, `keyword`:string

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page_num | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| keyword | string | 否 | 搜索关键字 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_topic_list`

- 摘要：获取话题热榜/Fetch topic hot list
- 能力：热点/榜单 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_topic_list_api_v1_douyin_billboard_fetch_hot_total_topic_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-topic-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-topic-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page`:integer, `page_size`:integer, `date_window`:integer, `tags`[object]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | integer | 否 | 页码 |
| page_size | integer | 否 | 每页数量 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| tags | array<object> | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | 是 | 无 |

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

### `POST /api/u1/v1/douyin/billboard/fetch_hot_total_video_list`

- 摘要：获取视频热榜/Fetch video hot list
- 能力：热点/榜单 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_total_video_list_api_v1_douyin_billboard_fetch_hot_total_video_list_post`
- 完整契约：[`api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-video-list`](../api-contracts/douyin-billboard-api.md#post-api-u1-v1-douyin-billboard-fetch-hot-total-video-list)

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：`page`:integer, `page_size`:integer, `date_window`:integer, `sub_type`:integer, `tags`[object]

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| page | integer | 否 | 页码，默认1 |
| page_size | integer | 否 | 每页数量，默认10 |
| date_window | integer | 否 | 时间窗口，1 按小时 2 按天 |
| sub_type | integer | 否 | 榜单分类，1001 视频总榜 1002 低粉爆款 1003 高完播率 1004 高涨粉率 1005 高点赞率 |
| tags | array<object> | 否 | 子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]} |
| tags[] | object | 是 | 无 |

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

### `GET /api/u1/v1/douyin/billboard/fetch_hot_user_portrait_list`

- 摘要：获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only
- 能力：热点/榜单 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_user_portrait_list_api_v1_douyin_billboard_fetch_hot_user_portrait_list_get`
- 完整契约：[`api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-user-portrait-list`](../api-contracts/douyin-billboard-api.md#get-api-u1-v1-douyin-billboard-fetch-hot-user-portrait-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id |
| option | query | integer | 否 | 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布 |

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
