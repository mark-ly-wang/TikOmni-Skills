# Weibo-Web-V2-API 路由详情

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 当前 tag 文件：`api-tags/weibo-web-v2-api.md`
- 完整契约：[`api-contracts/weibo-web-v2-api.md`](../api-contracts/weibo-web-v2-api.md)
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`33`
- 常见能力：搜索 / 主页/账号 / 作品详情 / 通用能力 / 热点/榜单 / 评论
- 默认认证：请求头 `Authorization` Bearer
- 常见入参：`page`, `uid`, `query`, `id`, `max_id`, `count`, `since_id`, `q`, `keyword`, `cursor`
- 标签说明：**(新浪微博 Web V2 数据接口/Weibo-Web-V2-API data endpoints)**

## 路由列表

### `GET /api/u1/v1/weibo/web_v2/check_allow_comment_with_pic`

- 摘要：检查微博是否允许带图评论/Check if Weibo allows image comments
- 能力：评论
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-check-allow-comment-with-pic`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-check-allow-comment-with-pic)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | query | string | 是 | 微博ID/Weibo ID |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_advanced_search`

- 摘要：微博高级搜索/Weibo Advanced Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-advanced-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-advanced-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| q | query | string | 是 | 搜索关键词/Search keyword |
| search_type | query | string | 否 | 搜索类型/Search type: all(全部), hot(热门), original(原创), verified(认证用户), media(媒体), viewpoint(观点) |
| include_type | query | string | 否 | 包含类型/Include type: all(全部), pic(含图片), video(含视频), music(含音乐), link(含短链) |
| timescope | query | string | 否 | 时间范围/Time scope (custom:start:end) |
| page | query | integer | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_ai_related_search`

- 摘要：微博AI搜索内容扩展/Weibo AI Search Content Extension
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-ai-related-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-ai-related-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_ai_search`

- 摘要：微博智能搜索/Weibo AI Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-ai-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-ai-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_all_groups`

- 摘要：获取所有分组信息/Get all groups information
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-all-groups`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-all-groups)

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

### `GET /api/u1/v1/weibo/web_v2/fetch_city_list`

- 摘要：地区省市映射/Region City List
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-city-list`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-city-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| normalized | query | boolean | 否 | 是否返回标准化结构（省份列表+城市数组）/Whether to return normalized structure |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_entertainment_ranking`

- 摘要：获取微博文娱榜单/Get Weibo entertainment ranking
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-entertainment-ranking`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-entertainment-ranking)

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

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_ranking_timeline`

- 摘要：获取微博热门榜单时间轴/Get hot ranking timeline
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-ranking-timeline`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-ranking-timeline)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| ranking_type | query | string | 是 | 榜单类型：hour=小时榜，yesterday=昨日榜，day_before=前日榜，week=周榜，male=男榜，female=女榜/Ranking type: hour=hourly, yesterday=yesterday, da… |
| since_id | query | string | 否 | 分页标识，默认为0/Pagination identifier, default is 0 |
| max_id | query | string | 否 | 最大ID，默认为0/Max ID, default is 0 |
| count | query | integer | 否 | 获取数量，默认10/Count, default is 10 |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search`

- 摘要：获取微博热搜榜单/Get Weibo hot search ranking
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-search)

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

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_index`

- 摘要：获取微博热搜词条(10条)/Get Weibo hot search index (10 items)
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-search-index`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-search-index)

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

### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_summary`

- 摘要：获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items)
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-search-summary`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-hot-search-summary)

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

### `GET /api/u1/v1/weibo/web_v2/fetch_life_ranking`

- 摘要：获取微博生活榜单/Get Weibo life ranking
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-life-ranking`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-life-ranking)

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

### `GET /api/u1/v1/weibo/web_v2/fetch_pic_search`

- 摘要：图片搜索/Weibo picture search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-pic-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-pic-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_post_comments`

- 摘要：获取微博评论/Get Weibo comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-post-comments`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-post-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | query | string | 是 | 微博ID/Weibo ID |
| count | query | integer | 否 | 评论数量/Number of comments |
| max_id | query | string | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_post_detail`

- 摘要：获取单个作品数据/Get single post data
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-post-detail`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-post-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | query | string | 是 | 作品id/Post id |
| is_get_long_text | query | string | 否 | 是否获取长微博全文/Whether to get the full text of long Weibo posts (true/false) |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_post_sub_comments`

- 摘要：获取微博子评论/Get Weibo sub-comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-post-sub-comments`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-post-sub-comments)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | query | string | 是 | 主评论ID/Comment ID |
| count | query | integer | 否 | 子评论数量/Number of sub-comments |
| max_id | query | string | 否 | 分页标识/Page identifier |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_realtime_search`

- 摘要：实时搜索/Weibo Realtime Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-realtime-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-realtime-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_similar_search`

- 摘要：获取微博相似搜索词推荐/Get Weibo similar search recommendations
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-similar-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-similar-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_social_ranking`

- 摘要：获取微博社会榜单/Get Weibo social ranking
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-social-ranking`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-social-ranking)

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

### `GET /api/u1/v1/weibo/web_v2/fetch_topic_search`

- 摘要：话题搜索/Weibo topic search
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-topic-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-topic-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_basic_info`

- 摘要：获取用户基本信息/Get user basic information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-basic-info`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-basic-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_fans`

- 摘要：获取用户粉丝列表/Get user fans list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-fans`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-fans)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID |
| page | query | integer | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_following`

- 摘要：获取用户关注列表/Get user following list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-following`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-following)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID |
| page | query | integer | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_info`

- 摘要：获取用户信息/Get user information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-info`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-info)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 否 | 用户id/User id |
| custom | query | string | 否 | 自定义微博用户名/Custom Weibo username |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_original_posts`

- 摘要：获取微博用户原创微博数据/Get Weibo user original posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-original-posts`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-original-posts)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id |
| page | query | integer | 否 | 页数/Page number |
| since_id | query | string | 否 | 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_posts`

- 摘要：获取微博用户文章数据/Get Weibo user posts
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-posts`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-posts)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id |
| page | query | integer | 否 | 页数/Page number |
| feature | query | integer | 否 | 特征值，控制返回数据的数量和字段：0=返回10条基础数据，1=返回20条扩展数据，2=返回20条图片相关数据，3=返回20条视频相关数据，字段逐级增加/Feature type: 0=10 basic posts, 1=20 extend… |
| since_id | query | string | 否 | 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_recommend_timeline`

- 摘要：获取微博主页推荐时间轴/Get user recommend timeline
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-recommend-timeline`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-recommend-timeline)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| refresh | query | integer | 否 | 刷新类型，0=正常刷新，1=强制刷新/Refresh type, 0=normal refresh, 1=force refresh |
| group_id | query | string | 否 | 分组ID/Group ID |
| containerid | query | string | 否 | 容器ID/Container ID |
| extparam | query | string | 否 | 扩展参数/Extended parameters |
| max_id | query | string | 否 | 最大ID/Max ID |
| count | query | integer | 否 | 获取数量/Count |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_search`

- 摘要：用户搜索/User search
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 否 | 搜索关键词/Query（提供则视为“全部”搜索；留空则仅应用高级筛选参数） |
| page | query | integer | 否 | 页码/Page |
| region | query | string | 否 | 地区编码，从 /city_list 获取/Region code from /city_list |
| auth | query | string | 否 | 认证类型 org_vip(机构)/per_vip(个人)/ord(普通)/Auth type |
| gender | query | string | 否 | 性别 man / women / Gender |
| age | query | string | 否 | 年龄段 18y/22y/29y/39y/40y / Age bucket |
| nickname | query | string | 否 | 昵称筛选/Nickname filter |
| tag | query | string | 否 | 标签筛选/Tag filter |
| school | query | string | 否 | 学校筛选/School filter |
| work | query | string | 否 | 公司筛选/Company filter |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_detail`

- 摘要：获取用户微博视频收藏夹详情/Get user video collection detail
- 能力：主页/账号 / 作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-detail`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-detail)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cid | query | string | 是 | 收藏夹ID/Collection ID |
| cursor | query | string | 否 | 分页游标/Pagination cursor |
| tab_code | query | integer | 否 | 排序方式：0=默认，1=最热，2=最新/Sort type: 0=default, 1=hottest, 2=latest |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_list`

- 摘要：获取用户微博视频收藏夹列表/Get user video collection list
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-list`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_list`

- 摘要：获取微博用户全部视频/Get user all videos
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-video-list`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-user-video-list)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID |
| cursor | query | string | 否 | 分页游标/Pagination cursor |

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

### `GET /api/u1/v1/weibo/web_v2/fetch_video_search`

- 摘要：视频搜索（热门/全部）/Weibo video search (hot/all)
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-video-search`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-fetch-video-search)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词/Search keyword |
| mode | query | string | 否 | 搜索模式：hot=热门 / all=全部 |
| page | query | integer | 否 | 页码/Page number |

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

### `GET /api/u1/v1/weibo/web_v2/search_user_posts`

- 摘要：搜索用户微博/Search user posts
- 能力：搜索 / 主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`
- 完整契约：[`api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-search-user-posts`](../api-contracts/weibo-web-v2-api.md#get-api-u1-v1-weibo-web-v2-search-user-posts)

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID/User ID |
| q | query | string | 是 | 搜索关键词/Search keyword |
| page | query | integer | 否 | 页数/Page number |
| starttime | query | integer | 是 | 开始时间戳/Start timestamp |
| endtime | query | integer | 是 | 结束时间戳/End timestamp |
| hasori | query | integer | 否 | 是否包含原创微博，1=包含，0=不包含/Include original posts, 1=include, 0=exclude |
| hasret | query | integer | 否 | 是否包含转发微博，1=包含，0=不包含/Include retweets, 1=include, 0=exclude |
| hastext | query | integer | 否 | 是否包含文字微博，1=包含，0=不包含/Include text posts, 1=include, 0=exclude |
| haspic | query | integer | 否 | 是否包含图片微博，1=包含，0=不包含/Include image posts, 1=include, 0=exclude |
| hasvideo | query | integer | 否 | 是否包含视频微博，1=包含，0=不包含/Include video posts, 1=include, 0=exclude |
| hasmusic | query | integer | 否 | 是否包含音乐微博，1=包含，0=不包含/Include music posts, 1=include, 0=exclude |

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
