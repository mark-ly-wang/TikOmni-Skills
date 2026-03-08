# Weibo-App-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/weibo-app-api.md`](../api-tags/weibo-app-api.md)
- 当前契约文件：`api-contracts/weibo-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`20`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(新浪微博APP数据接口/Weibo-App-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-weibo-app-fetch-ai-smart-search"></a>
### `GET /api/u1/v1/weibo/app/fetch_ai_smart_search`

- 摘要：AI智搜/AI Smart Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_ai_smart_search_api_v1_weibo_app_fetch_ai_smart_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 使用微博AI智搜功能进行搜索，返回AI增强的搜索结果。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码，从1开始（默认1）
> ### 返回:
> - AI智搜结果，包含AI增强的搜索内容
> ### 注意:
> - 此接口为AI增强搜索，返回结果经过AI处理
>
> # [English]
> ### Purpose:
> - Use Weibo AI Smart Search to search, return AI-enhanced search results.
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number, starts from 1 (default 1)
> ### Return:
> - AI smart search results, including AI-enhanced search content
> ### Note:
> - This is AI-enhanced search, results are processed by AI
>
> # [示例/Example]
> query = "人工智能"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词 | 无 | 人工智能 | 无 |
| page | query | integer | 否 | 页码 | 1 | 1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-home-recommend-feed"></a>
### `GET /api/u1/v1/weibo/app/fetch_home_recommend_feed`

- 摘要：获取首页推荐Feed流/Get home recommend feed
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_home_recommend_feed_api_v1_weibo_app_fetch_home_recommend_feed_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博首页推荐Feed流。
> ### 参数:
> - page: 页码，首页不传或传空，第二页传"2"，依次递增
> - count: 每页数量，默认15，最大50
> ### 返回:
> - 首页推荐Feed流数据
> ### 注意:
> - 推荐内容基于热门话题和热点事件
>
> # [English]
> ### Purpose:
> - Get the home recommend feed from Weibo.
> ### Parameters:
> - page: Page number, don't pass for first page, pass "2" for second page, and so on
> - count: Items per page, default 15, max 50
> ### Return:
> - Home recommend feed data
> ### Note:
> - Recommended content based on hot topics and trending events
>
> # [示例/Example]
> page = None  # First page
> count = 15

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page | query | string | 否 | 页码，首页不传，第二页传2 | 无 | 无 | 无 |
| count | query | integer | 否 | 每页数量 | 15 | 15 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-hot-search"></a>
### `GET /api/u1/v1/weibo/app/fetch_hot_search`

- 摘要：获取热搜榜/Get hot search
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_api_v1_weibo_app_fetch_hot_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博热搜榜，支持多个分类。
> ### 参数:
> - category: 热搜分类
>     - mineband: 我的热搜
>     - realtimehot: 实时热搜（默认）
>     - social: 社会热搜
>     - fun: 文娱热搜
>     - technologynav: 科技热搜
>     - lifenav: 生活热搜
>     - region: 同城热搜
>     - sportnav: 体育热搜
>     - gamenav: ACG热搜
> - page: 页码，从1开始（默认1）
> - count: 每页数量，默认20，最大50
> ### 返回:
> - 热搜榜数据，包含热搜词条、热度等
> ### 注意:
> - 热搜榜实时更新
>
> # [English]
> ### Purpose:
> - Get Weibo hot search ranking, supports multiple categories.
> ### Parameters:
> - category: Hot search category
>     - mineband: My hot search
>     - realtimehot: Realtime hot search (default)
>     - social: Social hot search
>     - fun: Entertainment hot search
>     - technologynav: Technology hot search
>     - lifenav: Life hot search
>     - region: Local hot search
>     - sportnav: Sports hot search
>     - gamenav: ACG hot search
> - page: Page number, starts from 1 (default 1)
> - count: Items per page, default 20, max 50
> ### Return:
> - Hot search ranking data, including search terms, popularity, etc.
> ### Note:
> - Hot search ranking updates in real-time
>
> # [示例/Example]
> category = "realtimehot"
> page = 1
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category | query | string | 否 | 热搜分类: mineband=我的, realtimehot=热搜, social=社会, fun=文娱, technologynav=科技, lifenav=生活, region=同城, sportnav=体育, gamenav=ACG | realtimehot | realtimehot | 无 |
| page | query | integer | 否 | 页码 | 1 | 1 | 无 |
| count | query | integer | 否 | 每页数量 | 20 | 20 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-hot-search-categories"></a>
### `GET /api/u1/v1/weibo/app/fetch_hot_search_categories`

- 摘要：获取热搜分类列表/Get hot search categories
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_categories_api_v1_weibo_app_fetch_hot_search_categories_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博热搜榜的所有可用分类列表。
> ### 参数:
> - 无
> ### 返回:
> - 热搜分类列表数据，包含各分类名称和标识
> ### 注意:
> - 返回的分类可用于 fetch_hot_search 接口的 category 参数
>
> # [English]
> ### Purpose:
> - Get all available hot search category list from Weibo.
> ### Parameters:
> - None
> ### Return:
> - Hot search category list data, including category names and identifiers
> ### Note:
> - Returned categories can be used for category parameter in fetch_hot_search endpoint
>
> # [示例/Example]
> # No parameters required

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-search-all"></a>
### `GET /api/u1/v1/weibo/app/fetch_search_all`

- 摘要：综合搜索/Comprehensive search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_all_api_v1_weibo_app_fetch_search_all_get`

#### 说明

> # [中文]
> ### 用途:
> - 在微博中进行综合搜索，返回相关内容。支持多种搜索类型。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码，从1开始（默认1）
> - search_type: 搜索类型
>     - 1: 综合（默认）
>     - 61: 实时
>     - 3: 用户
>     - 64: 视频
>     - 63: 图片
>     - 62: 关注
>     - 60: 热门
>     - 21: 全网
>     - 38: 话题
>     - 98: 超话
>     - 92: 地点
>     - 97: 商品
> ### 返回:
> - 搜索结果列表，包含微博内容、作者信息、图片、视频等
> ### 注意:
> - 搜索结果按相关度排序
> - 仅使用 page 参数进行翻页
>
> # [English]
> ### Purpose:
> - Comprehensive search in Weibo, return related content. Supports multiple search types.
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number, starts from 1 (default 1)
> - search_type: Search type
>     - 1: General/All (default)
>     - 61: Realtime
>     - 3: Users
>     - 64: Videos
>     - 63: Images
>     - 62: Following
>     - 60: Hot
>     - 21: Whole network
>     - 38: Topics
>     - 98: Super topics
>     - 92: Places/Locations
>     - 97: Products/Goods
> ### Return:
> - Search result list, including post content, author info, images, videos, etc.
> ### Note:
> - Search results sorted by relevance
> - Only use page parameter for pagination
>
> # [示例/Example]
> query = "NVIDIA"
> page = 1
> search_type = 1  # General search
> # search_type = 3  # Search users
> # search_type = 64  # Search videos

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | 是 | 搜索关键词 | 无 | NVIDIA | 无 |
| page | query | integer | 否 | 页码 | 1 | 1 | 无 |
| search_type | query | integer | 否 | 搜索类型: 1=综合, 61=实时, 3=用户, 64=视频, 63=图片, 62=关注, 60=热门, 21=全网, 38=话题, 98=超话, 92=地点, 97=商品 | 1 | 1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-status-comments"></a>
### `GET /api/u1/v1/weibo/app/fetch_status_comments`

- 摘要：获取微博评论/Get post comments
- 能力：评论
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_status_comments_api_v1_weibo_app_fetch_status_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定微博的一级评论列表（也适用于视频评论）。
> ### 参数:
> - status_id: 微博ID或视频ID（必填）
> - max_id: 翻页游标，首次请求不传，后续请求使用返回的max_id值
> - sort_type: 评论排序类型
>     - 0: 按热度排序（默认）
>     - 1: 按时间排序
> ### 返回:
> - 评论列表数据，包含评论内容、评论者信息、点赞数等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 每次返回约20条评论
> - 当没有更多评论时，max_id 为空或相同
>
> # [English]
> ### Purpose:
> - Get the first-level comment list of specified post (also works for video comments).
> ### Parameters:
> - status_id: Post ID or Video ID (required)
> - max_id: Pagination cursor, don't pass for first request, use returned max_id for subsequent requests
> - sort_type: Comment sort type
>     - 0: Sort by popularity (default)
>     - 1: Sort by time
> ### Return:
> - Comment list data, including comment content, commenter info, likes count, etc.
> - Contains max_id field for pagination
> ### Note:
> - About 20 comments per page
> - When no more comments, max_id is empty or same
>
> # [示例/Example]
> status_id = "5258708168476831"
> max_id = None  # First page
> sort_type = "0"  # Sort by popularity

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| status_id | query | string | 是 | 微博ID | 无 | 5258708168476831 | 无 |
| max_id | query | string | 否 | 翻页游标 | 无 | 无 | 无 |
| sort_type | query | string | 否 | 排序类型: 0=按热度排序, 1=按时间排序 | 0 | 0 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-status-detail"></a>
### `GET /api/u1/v1/weibo/app/fetch_status_detail`

- 摘要：获取微博详情/Get post detail
- 能力：详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_status_detail_api_v1_weibo_app_fetch_status_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定微博的详细信息。
> ### 参数:
> - status_id: 微博ID（必填）
> ### 返回:
> - 微博详细数据，包含完整文本、图片、视频、点赞数、评论数、转发数等
> ### 注意:
> - 如果微博已被删除或设置为私密，可能无法获取
>
> # [English]
> ### Purpose:
> - Get detailed information of specified post.
> ### Parameters:
> - status_id: Post ID (required)
> ### Return:
> - Post detailed data, including full text, images, videos, likes, comments, reposts count, etc.
> ### Note:
> - May not be available if post has been deleted or set to private
>
> # [示例/Example]
> status_id = "5016922058656962"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| status_id | query | string | 是 | 微博ID | 无 | 5016922058656962 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-status-likes"></a>
### `GET /api/u1/v1/weibo/app/fetch_status_likes`

- 摘要：获取微博点赞列表/Get post likes
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_status_likes_api_v1_weibo_app_fetch_status_likes_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定微博的点赞列表（也适用于视频点赞）。
> ### 参数:
> - status_id: 微博ID或视频ID（必填）
> - attitude_type: 点赞类型筛选
>     - 0: 全部（默认）
>     - 1: 点赞
>     - 2: 开心
>     - 3: 惊讶
>     - 4: 伤心
>     - 5: 愤怒
>     - 6: 打赏
>     - 8: 抱抱
> ### 返回:
> - 点赞列表数据，包含点赞者信息、点赞类型等
> ### 注意:
> - 每次返回约50条点赞记录
>
> # [English]
> ### Purpose:
> - Get the like list of specified post (also works for video likes).
> ### Parameters:
> - status_id: Post ID or Video ID (required)
> - attitude_type: Like type filter
>     - 0: All (default)
>     - 1: Like
>     - 2: Happy
>     - 3: Surprise
>     - 4: Sad
>     - 5: Angry
>     - 6: Reward
>     - 8: Hug
> ### Return:
> - Like list data, including liker info, like type, etc.
> ### Note:
> - About 50 likes per page
>
> # [示例/Example]
> status_id = "5016922058656962"
> attitude_type = "0"  # All types

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| status_id | query | string | 是 | 微博ID | 无 | 5016922058656962 | 无 |
| attitude_type | query | string | 否 | 点赞类型: 0=全部, 1=点赞, 2=开心, 3=惊讶, 4=伤心, 5=愤怒, 6=打赏, 8=抱抱 | 0 | 0 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-status-reposts"></a>
### `GET /api/u1/v1/weibo/app/fetch_status_reposts`

- 摘要：获取微博转发列表/Get post reposts
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_status_reposts_api_v1_weibo_app_fetch_status_reposts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定微博的转发列表（也适用于视频转发）。
> ### 参数:
> - status_id: 微博ID或视频ID（必填）
> - max_id: 翻页游标，首次请求不传，后续请求使用返回的max_id值
> ### 返回:
> - 转发列表数据，包含转发内容、转发者信息等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 每次返回约20条转发
> - 当没有更多转发时，max_id 为空或相同
>
> # [English]
> ### Purpose:
> - Get the repost list of specified post (also works for video reposts).
> ### Parameters:
> - status_id: Post ID or Video ID (required)
> - max_id: Pagination cursor, don't pass for first request, use returned max_id for subsequent requests
> ### Return:
> - Repost list data, including repost content, reposter info, etc.
> - Contains max_id field for pagination
> ### Note:
> - About 20 reposts per page
> - When no more reposts, max_id is empty or same
>
> # [示例/Example]
> status_id = "5016922058656962"
> max_id = None  # First page

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| status_id | query | string | 是 | 微博ID | 无 | 5016922058656962 | 无 |
| max_id | query | string | 否 | 翻页游标 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-album"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_album`

- 摘要：获取用户相册/Get user album
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_album_api_v1_weibo_app_fetch_user_album_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的相册内容。
> ### 参数:
> - uid: 用户ID（必填）
> - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值
> ### 返回:
> - 用户相册数据，包含图片列表等信息
> ### 注意:
> - 如果用户设置了隐私保护，可能无法获取相册
> - 使用游标翻页（since_id），不使用页码翻页
>
> # [English]
> ### Purpose:
> - Get the album content of specified user.
> ### Parameters:
> - uid: User ID (required)
> - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests
> ### Return:
> - User album data, including image list, etc.
> ### Note:
> - If user has set privacy protection, album may not be available
> - Uses cursor pagination (since_id), not page numbers
>
> # [示例/Example]
> uid = "7648703289"
> since_id = None  # First page
> # since_id = "5012154263666753_4990205358511630|1034:4990204960768042_20240328_-1"  # Next page

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 7648703289 | 无 |
| since_id | query | string | 否 | 翻页游标 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-articles"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_articles`

- 摘要：获取用户文章列表/Get user articles
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_articles_api_v1_weibo_app_fetch_user_articles_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户发布的文章列表。
> ### 参数:
> - uid: 用户ID（必填）
> - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值
> ### 返回:
> - 用户文章列表数据
> ### 注意:
> - 如果用户没有发布过文章，返回空列表
> - 使用游标翻页（since_id），不使用页码翻页
>
> # [English]
> ### Purpose:
> - Get the article list published by specified user.
> ### Parameters:
> - uid: User ID (required)
> - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests
> ### Return:
> - User article list data
> ### Note:
> - If user has not published any articles, returns empty list
> - Uses cursor pagination (since_id), not page numbers
>
> # [示例/Example]
> uid = "1725941200"
> since_id = None  # First page

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 1725941200 | 无 |
| since_id | query | string | 否 | 翻页游标 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-audios"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_audios`

- 摘要：获取用户音频列表/Get user audios
- 能力：主页/账号 / 音频/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_audios_api_v1_weibo_app_fetch_user_audios_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户发布的音频列表。
> ### 参数:
> - uid: 用户ID（必填）
> - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值
> ### 返回:
> - 用户音频列表数据
> ### 注意:
> - 如果用户没有发布过音频，返回空列表
> - 使用游标翻页（since_id），不使用页码翻页
>
> # [English]
> ### Purpose:
> - Get the audio list published by specified user.
> ### Parameters:
> - uid: User ID (required)
> - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests
> ### Return:
> - User audio list data
> ### Note:
> - If user has not published any audios, returns empty list
> - Uses cursor pagination (since_id), not page numbers
>
> # [示例/Example]
> uid = "1725941200"
> since_id = None  # First page

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 1725941200 | 无 |
| since_id | query | string | 否 | 翻页游标 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-info"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_info`

- 摘要：获取用户信息/Get user information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_api_v1_weibo_app_fetch_user_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博用户的基本信息，包括昵称、头像、简介、关注数、粉丝数等。
> ### 参数:
> - uid: 用户ID（必填）
> ### 返回:
> - 用户基本信息数据
> ### 注意:
> - 如果用户设置了隐私保护，部分信息可能无法获取
>
> # [English]
> ### Purpose:
> - Get basic information of Weibo users, including nickname, avatar, bio, following count, followers count, etc.
> ### Parameters:
> - uid: User ID (required)
> ### Return:
> - User basic information data
> ### Note:
> - Some information may not be available if user has set privacy protection
>
> # [示例/Example]
> uid = "7648703289"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 7648703289 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-info-detail"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_info_detail`

- 摘要：获取用户详细信息/Get user detail information
- 能力：主页/账号 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_info_detail_api_v1_weibo_app_fetch_user_info_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博用户的详细信息，比基本信息更加完整，包括认证信息、标签、等级等。
> ### 参数:
> - uid: 用户ID（必填）
> ### 返回:
> - 用户详细信息数据
> ### 注意:
> - 如果用户设置了隐私保护，部分信息可能无法获取
>
> # [English]
> ### Purpose:
> - Get detailed information of Weibo users, more complete than basic info, including verification info, tags, level, etc.
> ### Parameters:
> - uid: User ID (required)
> ### Return:
> - User detailed information data
> ### Note:
> - Some information may not be available if user has set privacy protection
>
> # [示例/Example]
> uid = "7648703289"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 7648703289 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-profile-feed"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_profile_feed`

- 摘要：获取用户主页动态/Get user profile feed
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_profile_feed_api_v1_weibo_app_fetch_user_profile_feed_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户主页的动态流。
> ### 参数:
> - uid: 用户ID（必填）
> - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值
> ### 返回:
> - 用户主页动态数据
> ### 注意:
> - 如果用户设置了隐私保护，可能无法获取动态
> - 使用游标翻页（since_id），不使用页码翻页
>
> # [English]
> ### Purpose:
> - Get the profile feed of specified user.
> ### Parameters:
> - uid: User ID (required)
> - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests
> ### Return:
> - User profile feed data
> ### Note:
> - If user has set privacy protection, feed may not be available
> - Uses cursor pagination (since_id), not page numbers
>
> # [示例/Example]
> uid = "6580994757"
> since_id = None  # First page
> # since_id = "2|1769360821762|5258923930289595,,,,,,1768788000,,,,,-1,-1"  # Next page

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 6580994757 | 无 |
| since_id | query | string | 否 | 翻页游标 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-super-topics"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_super_topics`

- 摘要：获取用户参与的超话列表/Get user super topics
- 能力：主页/账号 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_super_topics_api_v1_weibo_app_fetch_user_super_topics_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户参与的超话列表。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从1开始（默认1）
> ### 返回:
> - 用户参与的超话列表数据
> ### 注意:
> - 如果用户设置了隐私保护，可能无法获取超话列表
>
> # [English]
> ### Purpose:
> - Get the super topics list that user participated in.
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 1 (default 1)
> ### Return:
> - User's super topics list data
> ### Note:
> - If user has set privacy protection, super topics list may not be available
>
> # [示例/Example]
> uid = "7648703289"
> page = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 7648703289 | 无 |
| page | query | integer | 否 | 页码 | 1 | 1 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-timeline"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_timeline`

- 摘要：获取用户发布的微博/Get user timeline
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_timeline_api_v1_weibo_app_fetch_user_timeline_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户发布的微博列表，支持分页和多种内容筛选。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从1开始（默认1）
> - filter_type: 筛选类型（默认"all"）
>     - all: 全部微博
>     - original: 原创微博
>     - likes: 她/他的赞
>     - video: 视频微博
>     - pic: 图片微博
>     - location: 签到足迹
>     - month: 按时间筛选（需要同时传入month参数）
> - month: 时间筛选参数，格式YYYYMMDD（仅当filter_type=month时使用）
> ### 返回:
> - 微博列表数据，包含微博内容、图片、视频等信息
> ### 注意:
> - 如果用户设置了隐私保护，可能无法获取微博列表
> - 每页返回数量约为20条微博
> - 使用时间筛选时必须同时指定filter_type=month和month参数
>
> # [English]
> ### Purpose:
> - Get the list of posts published by specified user, support pagination and multiple content filters.
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 1 (default 1)
> - filter_type: Filter type (default "all")
>     - all: All posts
>     - original: Original posts
>     - likes: Liked posts
>     - video: Video posts
>     - pic: Picture posts
>     - location: Location check-in posts
>     - month: Filter by time (must pass month parameter)
> - month: Time filter parameter, format YYYYMMDD (only used when filter_type=month)
> ### Return:
> - Post list data, including post content, images, videos, etc.
> ### Note:
> - If user has set privacy protection, post list may not be available
> - About 20 posts per page
> - When using time filter, must specify both filter_type=month and month parameter
>
> # [示例/Example]
> uid = "7648703289"
> page = 1
> filter_type = "all"
> # or filter_type = "video" for videos only
> # or filter_type = "month" with month = "20251010" for time filter

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 7648703289 | 无 |
| page | query | integer | 否 | 页码 | 1 | 1 | 无 |
| filter_type | query | string | 否 | 筛选类型 | all | all | 无 |
| month | query | string | 否 | 时间筛选(YYYYMMDD格式) | 无 | 20251010 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-user-videos"></a>
### `GET /api/u1/v1/weibo/app/fetch_user_videos`

- 摘要：获取用户视频列表/Get user videos
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_videos_api_v1_weibo_app_fetch_user_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户发布的视频列表（瀑布流展示）。
> ### 参数:
> - uid: 用户ID（必填）
> - since_id: 翻页游标，初次请求不传，后续请求使用返回的since_id值
> ### 返回:
> - 视频列表数据，包含视频标题、封面、播放量等信息
> - 包含 moreInfo.params.since_id 字段用于翻页
> ### 注意:
> - 只返回包含视频的微博
> - 使用游标翻页（since_id），不使用页码翻页
>
> # [English]
> ### Purpose:
> - Get the video list published by specified user (waterfall layout).
> ### Parameters:
> - uid: User ID (required)
> - since_id: Pagination cursor, don't pass for first request, use returned since_id for subsequent requests
> ### Return:
> - Video list data, including video title, cover, views, etc.
> - Contains moreInfo.params.since_id field for pagination
> ### Note:
> - Only returns posts with videos
> - Uses cursor pagination (since_id), not page numbers
>
> # [示例/Example]
> # First page
> uid = "7648703289"
> since_id = None
>
> # Next page (use since_id from previous response)
> # since_id = "4763250669650541"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户ID | 无 | 7648703289 | 无 |
| since_id | query | string | 否 | 翻页游标 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-video-detail"></a>
### `GET /api/u1/v1/weibo/app/fetch_video_detail`

- 摘要：获取视频详情/Get video detail
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_detail_api_v1_weibo_app_fetch_video_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个视频的详细信息，包括视频播放地址。
> - **重要**: 从微博视频链接（如 https://weibo.com/tv/show/1034:5232127105761312）获取真实视频ID的必需步骤
> ### 参数:
> - mid: 视频微博ID或链接中的ID（必填）
> ### 返回:
> - 视频详细数据，包含视频播放地址、封面、时长、标题等
> - **items[0].data.idstr**: 真实的视频微博ID，可用于获取评论等操作
> ### 注意:
> - 返回的视频地址可能有时效性
> - 支持获取高清视频地址
> - **获取评论前必须先调用此接口**: 链接中的ID不能直接用于获取评论，需要先通过此接口获取 items[0].data.idstr 中的真实ID
>
> # [English]
> ### Purpose:
> - Get detailed information of single video, including video play URL.
> - **Important**: Required step to get real video ID from Weibo video link (e.g., https://weibo.com/tv/show/1034:5232127105761312)
> ### Parameters:
> - mid: Video post ID or ID from link (required)
> ### Return:
> - Video detailed data, including video play URL, cover, duration, title, etc.
> - **items[0].data.idstr**: Real video post ID, can be used for fetching comments
> ### Note:
> - Returned video URL may have expiration time
> - Support getting HD video URL
> - **Must call this API before fetching comments**: ID from link cannot be used directly for comments, must get real ID from items[0].data.idstr first
>
> # [示例/Example]
> mid = "5242977759006596"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mid | query | string | 是 | 视频微博ID | 无 | 5242977759006596 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |

<a id="get-api-u1-v1-weibo-app-fetch-video-featured-feed"></a>
### `GET /api/u1/v1/weibo/app/fetch_video_featured_feed`

- 摘要：获取短视频精选Feed流/Get video featured feed
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_featured_feed_api_v1_weibo_app_fetch_video_featured_feed_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取微博短视频精选页的Feed流。
> ### 参数:
> - page: 页码，首页不传或传空，第二页传"2"，依次递增
> ### 返回:
> - 短视频精选Feed流数据，包含视频列表等
> ### 注意:
> - 每页返回约20条视频
>
> # [English]
> ### Purpose:
> - Get the featured video feed from Weibo video section.
> ### Parameters:
> - page: Page number, don't pass for first page, pass "2" for second page, and so on
> ### Return:
> - Featured video feed data, including video list, etc.
> ### Note:
> - About 20 videos per page
>
> # [示例/Example]
> page = None  # First page
> # page = "2"  # Second page

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page | query | string | 否 | 页码，首页不传，第二页传2 | 无 | 无 | 无 |

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | 否 | HTTP status code \| HTTP状态码 | 200 | 无 | 无 |
| request_id | string | 否 | Unique request identifier \| 唯一请求标识符 | 无 | 无 | 无 |
| message | string | 否 | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | 无 | 无 |
| message_zh | string | 否 | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | 无 | 无 |
| support | string | 否 | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | 无 | 无 |
| time | string | 否 | The time the response was generated \| 生成响应的时间 | 无 | 无 | 无 |
| time_stamp | integer | 否 | The timestamp the response was generated \| 生成响应的时间戳 | 无 | 无 | 无 |
| time_zone | string | 否 | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | 无 | 无 |
| docs | string | 否 | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | 无 | 无 | 无 |
| cache_message | string | 否 | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | 无 | 无 |
| cache_message_zh | string | 否 | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | 无 | 无 |
| cache_url | string | 否 | The URL to access the cached result \| 访问缓存结果的 URL | 无 | 无 | 无 |
| router | string | 否 | The endpoint that generated this response \| 生成此响应的端点 | 无 | 无 | 无 |
| params | 动态对象 | 否 | The parameters used in the request \| 请求中使用的参数 | 无 | 无 | 无 |
| data | null | 否 | The response data \| 响应数据 | 无 | 无 | 无 |
