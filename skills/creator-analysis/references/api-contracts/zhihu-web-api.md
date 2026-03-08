# Zhihu-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/zhihu-web-api.md`](../api-tags/zhihu-web-api.md)
- Current contract file: `api-contracts/zhihu-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `32`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(知乎Web数据接口/Zhihu-Web-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-zhihu-web-fetch-ai-search"></a>
### `GET /api/u1/v1/zhihu/web/fetch_ai_search`

- Summary: 获取知乎AI搜索/Get Zhihu AI Search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_ai_search_api_v1_zhihu_web_fetch_ai_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎AI搜索
> ### 参数:
> - message_content: 搜索内容
> ### 返回:
> - 知乎AI搜索消息ID，用于请求搜索结果
>
> # [English]
> ### Purpose:
> - Get Zhihu AI Search
> ### Parameters:
> - message_content: Search Content
> ### Returns:
> - Zhihu AI Search Message ID for requesting search results
>
> # [示例/Example]
> message_content = "deepseek"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| message_content | query | string | Yes | 搜索内容/Search Content | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-ai-search-result"></a>
### `GET /api/u1/v1/zhihu/web/fetch_ai_search_result`

- Summary: 获取知乎AI搜索结果/Get Zhihu AI Search Result
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_ai_search_result_api_v1_zhihu_web_fetch_ai_search_result_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎AI搜索结果
> ### 参数:
> - message_id: 消息ID
> ### 返回:
> - 知乎AI搜索结果
>
> # [English]
> ### Purpose:
> - Get Zhihu AI Search Result
> ### Parameters:
> - message_id: Message ID
> ### Returns:
> - Zhihu AI Search Result
>
> # [示例/Example]
> message_id = "5f8b4f4a-0b7c-4d1b-8c4f-2e5c0d6c1b9d"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| message_id | query | string | Yes | 消息ID/Message ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-article-search-v3"></a>
### `GET /api/u1/v1/zhihu/web/fetch_article_search_v3`

- Summary: 获取知乎文章搜索V3/Get Zhihu Article Search V3
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_article_search_v3_api_v1_zhihu_web_fetch_article_search_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎文章搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - offset: 偏移量
> - limit: 每页文章数量
> - show_all_topics: 显示所有主题，
>     - 0 不显示话题
>     - 1 显示话题
> - search_source: 搜索来源
>     - Filter 过滤参数生效
>     - Normal 为普通结果
> - search_hash_id: 搜索哈希ID，用于过滤重复搜索结果
> - vertical: 空 不限类型
>     - answer 只看回答
>     - article 只看文章
>     - zvideo 只看视频
> - sort: 空 综合排序
>     - upvoted_count 最多赞同
>     - created_time 最新发布
> - time_interval: 时间间隔
>     - 空 不限时间
>     - a_day 一天内
>     - a_week 一周内
>     - a_month 一个月内
>     - three_months 三个月内
>     - half_a_year 半年内
>     - a_year 一年内
> - vertical_info: 垂类信息
>     - 0,0,0,0,0,0,0,0,0,0,0,0 不限类型，不会设置勿填
> ### 返回:
> - 知乎文章搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu Article Search V3
> ### Parameters:
> - keyword: Search Keywords
> - offset: Offset
> - limit: Number of articles per page
> - show_all_topics: Show all topics
>     - 0 Do not show topics
>     - 1 Show topics
> - search_source: Search Source
>     - Filter parameter takes effect
>     - Normal is normal result
> - search_hash_id: Search Hash ID, used to filter duplicate search results
> - vertical: Empty unlimited type
>     - answer only see answers
>     - article only see articles
>     - zvideo only see videos
> - sort: Empty comprehensive sorting
>     - upvoted_count most upvoted
>     - created_time latest release
> - time_interval: Time interval
>     - Empty unlimited time
>     - a_day within a day
>     - a_week within a week
>     - a_month within a month
>     - three_months within three months
>     - half_a_year within half a year
>     - a_year within a year
> - vertical_info: Vertical information
>     - 0,0,0,0,0,0,0,0,0,0,0,0 unlimited type, do not set do not fill
> ### Returns:
> - Zhihu Article Search V3
>
> # [示例/Example]
> # 默认搜索，综合排序，不限时间
> keyword = "deepseek"
> offset = "0"
> limit = "20"
> show_all_topics = 0
> search_source = "Normal"
> search_hash_id = ""
> vertical = ""
> sort = ""
> time_interval = ""
> vertical_info = ""
>
> # 只看回答，最多赞同，三月内
> keyword = "deepseek"
> offset = "0"
> limit = "20"
> show_all_topics = 0
> search_source = "Filter"
> search_hash_id = ""
> vertical = "answer"
> sort = "upvoted_count"
> time_interval = "three_months"
> vertical_info = "0,0,0,0,0,0,0,0,0,0,0,0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页文章数量/Number of articles per page | 20 | None | None |
| show_all_topics | query | integer | No | 显示所有主题/Show all topics | 0 | None | None |
| search_source | query | string | No | 搜索来源/Search Source | Normal | None | None |
| search_hash_id | query | string | No | 搜索哈希ID/Search Hash ID | None | None | None |
| vertical | query | string | No | 垂类/Vertical Type | None | None | None |
| sort | query | string | No | 排序/Sort | None | None | None |
| time_interval | query | string | No | 时间间隔/Time Interval | None | None | None |
| vertical_info | query | string | No | 垂类信息/Vertical Info | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-column-article-detail"></a>
### `GET /api/u1/v1/zhihu/web/fetch_column_article_detail`

- Summary: 获取知乎专栏文章详情/Get Zhihu Column Article Detail
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_column_article_detail_api_v1_zhihu_web_fetch_column_article_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎专栏文章详情
> ### 参数:
> - article_id: 文章ID
> ### 返回:
> - 知乎专栏文章详情
>
> # [English]
> ### Purpose:
> - Get Zhihu Column Article Detail
> ### Parameters:
> - article_id: Article ID
> ### Returns:
> - Zhihu Column Article Detail
>
> # [示例/Example]
> article_id = "669214677"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| article_id | query | string | Yes | 文章ID/Article ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-column-articles"></a>
### `GET /api/u1/v1/zhihu/web/fetch_column_articles`

- Summary: 获取知乎专栏文章列表/Get Zhihu Column Articles
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_column_articles_api_v1_zhihu_web_fetch_column_articles_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎专栏文章列表
> ### 参数:
> - column_id: 专栏ID
> - limit: 每页文章数量
> - offset: 偏移量
> ### 返回:
> - 知乎专栏文章列表
>
> # [English]
> ### Purpose:
> - Get Zhihu Column Articles
> ### Parameters:
> - column_id: Column ID
> - limit: Number of articles per page
> - offset: Offset
> ### Returns:
> - Zhihu Column Articles
>
> # [示例/Example]
> column_id = "zhangjiawei"
> limit = "10"
> offset = "0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| column_id | query | string | Yes | 专栏ID/Column ID | None | None | None |
| limit | query | string | No | 每页文章数量/Number of articles per page | 10 | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-column-comment-config"></a>
### `GET /api/u1/v1/zhihu/web/fetch_column_comment_config`

- Summary: 获取知乎专栏评论区配置/Get Zhihu Column Comment Config
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_column_comment_config_api_v1_zhihu_web_fetch_column_comment_config_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎专栏评论区配置
> ### 参数:
> - article_id: 文章ID
> ### 返回:
> - 知乎专栏评论区配置
>
> # [English]
> ### Purpose:
> - Get Zhihu Column Comment Config
> ### Parameters:
> - article_id: Article ID
> ### Returns:
> - Zhihu Column Comment Config
>
> # [示例/Example]
> article_id = "669214677"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| article_id | query | string | Yes | 文章ID/Article ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-column-recommend"></a>
### `GET /api/u1/v1/zhihu/web/fetch_column_recommend`

- Summary: 获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_column_recommend_api_v1_zhihu_web_fetch_column_recommend_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎相似专栏推荐
> ### 参数:
> - article_id: 文章ID
> - limit: 每页专栏数量
> - offset: 偏移量
> ### 返回:
> - 知乎相似专栏推荐
>
> # [English]
> ### Purpose:
> - Get Zhihu Similar Column Recommend
> ### Parameters:
> - article_id: Article ID
> - limit: Number of columns per page
> - offset: Offset
> ### Returns:
> - Zhihu Similar Column Recommend
>
> # [示例/Example]
> article_id = "669214677"
> limit = "12"
> offset = "0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| article_id | query | string | Yes | 文章ID/Article ID | None | None | None |
| limit | query | string | No | 每页专栏数量/Number of columns per page | 12 | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-column-relationship"></a>
### `GET /api/u1/v1/zhihu/web/fetch_column_relationship`

- Summary: 获取知乎专栏文章互动关系/Get Zhihu Column Article Relationship
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_column_relationship_api_v1_zhihu_web_fetch_column_relationship_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎专栏文章互动关系
> ### 参数:
> - article_id: 文章ID
> ### 返回:
> - 知乎专栏互动关系
>
> # [English]
> ### Purpose:
> - Get Zhihu Column Relationship
> ### Parameters:
> - article_id: Article ID
> ### Returns:
> - Zhihu Column Relationship
>
> # [示例/Example]
> article_id = "669214677"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| article_id | query | string | Yes | 文章ID/Article ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-column-search-v3"></a>
### `GET /api/u1/v1/zhihu/web/fetch_column_search_v3`

- Summary: 获取知乎专栏搜索V3/Get Zhihu Column Search V3
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_column_search_v3_api_v1_zhihu_web_fetch_column_search_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎专栏搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - offset: 偏移量
> - limit: 每页专栏数量
> - search_hash_id: 搜索哈希ID
> ### 返回:
> - 知乎专栏搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu Column Search V3
> ### Parameters:
> - keyword: Search Keywords
> - offset: Offset
> - limit: Number of columns per page
> - search_hash_id: Search Hash ID
> ### Returns:
> - Zhihu Column Search V3
>
> # [示例/Example]
> keyword = "deepseek"
> limit = "20"
> offset = "0"
> search_hash_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页专栏数量/Number of columns per page | 20 | None | None |
| search_hash_id | query | string | No | 搜索哈希ID/Search Hash ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-comment-v5"></a>
### `GET /api/u1/v1/zhihu/web/fetch_comment_v5`

- Summary: 获取知乎评论区V5/Get Zhihu Comment V5
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_comment_v5_api_v1_zhihu_web_fetch_comment_v5_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎评论区V5
> ### 参数:
> - answer_id: 回答ID
> - order_by: 排序
>     - score 最热排序
>     - ts 最新排序
> - limit: 每页评论数量
> - offset: 偏移量/页码
> ### 返回:
> - 知乎评论区V5
>
> # [English]
> ### Purpose:
> - Get Zhihu Comment V5
> ### Parameters:
> - answer_id: Answer ID
> - order_by: Sort
>     - score Hottest Sort
>     - ts Latest Sort
> - limit: Number of comments per page
> - offset: Offset/Page Number
> ### Returns:
> - Zhihu Comment V5
>
> # [示例/Example]
> answer_id = "89226347214"
> order_by = "score"
> limit = "20"
> offset = "" # 1739257701_11108372663_0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| answer_id | query | string | Yes | 回答ID/Answer ID | None | None | None |
| order_by | query | string | No | 排序/Sort | score | None | None |
| limit | query | string | No | 每页评论数量/Number of comments per page | 20 | None | None |
| offset | query | string | No | 偏移量/Offset | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-ebook-search-v3"></a>
### `GET /api/u1/v1/zhihu/web/fetch_ebook_search_v3`

- Summary: 获取知乎电子书搜索V3/Get Zhihu Ebook Search V3
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_ebook_search_v3_api_v1_zhihu_web_fetch_ebook_search_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎电子书搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - offset: 偏移量
> - limit: 每页电子书数量
> - search_hash_id: 搜索哈希ID
> ### 返回:
> - 知乎电子书搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu Ebook Search V3
> ### Parameters:
> - keyword: Search Keywords
> - offset: Offset
> - limit: Number of ebooks per page
> - search_hash_id: Search Hash ID
> ### Returns:
> - Zhihu Ebook Search V3
>
> # [示例/Example]
> keyword = "deepseek"
> limit = "20"
> offset = "0"
> search_hash_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页电子书数量/Number of ebooks per page | 20 | None | None |
| search_hash_id | query | string | No | 搜索哈希ID/Search Hash ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-hot-list"></a>
### `GET /api/u1/v1/zhihu/web/fetch_hot_list`

- Summary: 获取知乎首页热榜/Get Zhihu Hot List
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_list_api_v1_zhihu_web_fetch_hot_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎首页热榜
> ### 参数:
> - limit: 每页文章数量
> - desktop: 是否为桌面端
> ### 返回:
> - 知乎首页热榜
>
> # [English]
> ### Purpose:
> - Get Zhihu Hot List
> ### Parameters:
> - limit: Number of articles per page
> - desktop: Is it a desktop
> ### Returns:
> - Zhihu Hot List
>
> # [示例/Example]
> limit = "50"
> desktop = "true"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| limit | query | string | No | 每页文章数量/Number of articles per page | 50 | None | None |
| desktop | query | string | No | 是否为桌面端/Is it a desktop | true | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-hot-recommend"></a>
### `GET /api/u1/v1/zhihu/web/fetch_hot_recommend`

- Summary: 获取知乎首页推荐/Get Zhihu Hot Recommend
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_recommend_api_v1_zhihu_web_fetch_hot_recommend_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎首页推荐
> ### 参数:
> - offset: 偏移量
> - page_number: 页码
> - session_token: 会话令牌
> ### 返回:
> - 知乎首页推荐
>
> # [English]
> ### Purpose:
> - Get Zhihu Hot Recommend
> ### Parameters:
> - offset: Offset
> - page_number: Page Number
> - session_token: Session Token
>
> # [示例/Example]
> offset = "0"
> page_number = "1"
> session_token = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| page_number | query | string | No | 页码/Page Number | 1 | None | None |
| session_token | query | string | No | 会话令牌/Session Token | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-preset-search"></a>
### `GET /api/u1/v1/zhihu/web/fetch_preset_search`

- Summary: 获取知乎搜索预设词/Get Zhihu Preset Search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_preset_search_api_v1_zhihu_web_fetch_preset_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎搜索预设词
> ### 参数:
> - 无
> ### 返回:
> - 知乎搜索预设词
>
> # [English]
> ### Purpose:
> - Get Zhihu Preset Search
> ### Parameters:
> - None
> ### Returns:
> - Zhihu Preset Search

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-question-answers"></a>
### `GET /api/u1/v1/zhihu/web/fetch_question_answers`

- Summary: 获取知乎问题回答列表/Get Zhihu Question Answers
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_question_answers_api_v1_zhihu_web_fetch_question_answers_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎问题的回答列表
> ### 参数:
> - question_id: 问题ID
> - cursor: 分页游标，用于获取下一页数据，从返回的字段里提取
> - limit: 每页回答数量，默认5
> - offset: 偏移量，默认0
> - order: 排序方式，default=默认排序，updated=按时间排序
> - session_id: 会话ID，用于分页时保持状态，从返回的字段里提取
> ### 返回:
> - 知乎问题回答列表数据
>
> # [English]
> ### Purpose:
> - Get Zhihu Question Answers List
> ### Parameters:
> - question_id: Question ID
> - cursor: Pagination cursor for next page, extracted from response fields
> - limit: Number of answers per page, default 5
> - offset: Offset, default 0
> - order: Sort order, default=default sort, updated=sort by time
> - session_id: Session ID for pagination state, extracted from response fields
> ### Returns:
> - Zhihu Question Answers List Data
>
> # [示例/Example]
> question_id = "37811449"
> cursor = ""
> limit = 5
> offset = 0
> order = "default"  # 或 "updated" 按时间排序
> session_id = ""
>
> # 获取下一页 (Get next page):
> cursor = "d88f09569eba20b966bcf15076977430"
> offset = 1
> session_id = "1757928778451769939"
>
> # 按时间排序 (Sort by time):
> order = "updated"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| question_id | query | string | Yes | 问题ID/Question ID | None | None | None |
| cursor | query | string | No | 分页游标/Pagination cursor | None | None | None |
| limit | query | integer | No | 每页回答数量/Number of answers per page | 5 | None | None |
| offset | query | integer | No | 偏移量/Offset | 0 | None | None |
| order | query | string | No | 排序方式：default=默认排序，updated=按时间排序/Sort order: default=default sort, updated=sort by time | default | None | None |
| session_id | query | string | No | 会话ID/Session ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-recommend-followees"></a>
### `GET /api/u1/v1/zhihu/web/fetch_recommend_followees`

- Summary: 获取知乎推荐关注列表/Get Zhihu Recommend Followees
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_recommend_followees_api_v1_zhihu_web_fetch_recommend_followees_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎推荐关注列表
> ### 参数:
> - 无
> ### 返回:
> - 知乎推荐关注列表
>
> # [English]
> ### Purpose:
> - Get Zhihu Recommend Followees
> ### Parameters:
> - None
> ### Returns:
> - Zhihu Recommend Followees

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-salt-search-v3"></a>
### `GET /api/u1/v1/zhihu/web/fetch_salt_search_v3`

- Summary: 获取知乎盐选内容搜索V3/Get Zhihu Salt Search V3
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_salt_search_v3_api_v1_zhihu_web_fetch_salt_search_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎盐选内容搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - offset: 偏移量
> - limit: 每页内容数量
> - search_hash_id: 搜索哈希ID
> ### 返回:
> - 知乎盐选内容搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu Salt Search V3
> ### Parameters:
> - keyword: Search Keywords
> - offset: Offset
> - limit: Number of contents per page
> - search_hash_id: Search Hash ID
> ### Returns:
> - Zhihu Salt Search V3
>
> # [示例/Example]
> keyword = "deepseek"
> limit = "20"
> offset = "0"
> search_hash_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页内容数量/Number of contents per page | 20 | None | None |
| search_hash_id | query | string | No | 搜索哈希ID/Search Hash ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="post-api-u1-v1-zhihu-web-fetch-scholar-search-v3"></a>
### `POST /api/u1/v1/zhihu/web/fetch_scholar_search_v3`

- Summary: 获取知乎论文搜索V3/Get Zhihu Scholar Search V3
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎论文搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - offset: 偏移量
> - limit: 每页论文数量
> - filter_fields: 过滤字段
> ### 返回:
> - 知乎论文搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu Scholar Search V3
> ### Parameters:
> - keyword: Search Keywords
> - offset: Offset
> - limit: Number of papers per page
> - filter_fields: Filter Fields
> ### Returns:
> - Zhihu Scholar Search V3
>
> # [示例/Example]
> keyword = "人工智能"
> offset = "0"
> limit = "25"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页论文数量/Number of papers per page | 25 | None | None |

#### Request Body

- required: No

##### `application/json`

- Schema summary: dynamic object

No field table

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-search-recommend"></a>
### `GET /api/u1/v1/zhihu/web/fetch_search_recommend`

- Summary: 获取知乎搜索发现/Get Zhihu Search Recommend
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_recommend_api_v1_zhihu_web_fetch_search_recommend_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎搜索发现
> ### 参数:
> - 无
> ### 返回:
> - 知乎搜索发现
>
> # [English]
> ### Purpose:
> - Get Zhihu Search Recommend
> ### Parameters:
> - None
> ### Returns:
> - Zhihu Search Recommend

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-search-suggest"></a>
### `GET /api/u1/v1/zhihu/web/fetch_search_suggest`

- Summary: 知乎搜索预测词/Get Zhihu Search Suggest
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_suggest_api_v1_zhihu_web_fetch_search_suggest_get`

#### Notes

> # [中文]
> ### 用途:
> - 知乎搜索预测词
> ### 参数:
> - keyword: 搜索关键词
> ### 返回:
> - 知乎搜索预测词
>
> # [English]
> ### Purpose:
> - Get Zhihu Search Suggest
> ### Parameters:
> - keyword: Search Keywords
> ### Returns:
> - Zhihu Search Suggest
>
> # [示例/Example]
> keyword = "deepseek"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-sub-comment-v5"></a>
### `GET /api/u1/v1/zhihu/web/fetch_sub_comment_v5`

- Summary: 获取知乎子评论区V5/Get Zhihu Sub Comment V5
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_sub_comment_v5_api_v1_zhihu_web_fetch_sub_comment_v5_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎子评论区V5
> ### 参数:
> - comment_id: 评论ID
> - order_by: 排序
>     - score 最热排序
>     - ts 最新排序
> - limit: 每页评论数量
> - offset: 偏移量/页码
> ### 返回:
> - 知乎子评论区V5
>
> # [English]
> ### Purpose:
> - Get Zhihu Sub Comment V5
> ### Parameters:
> - comment_id: Comment ID
> - order_by: Sort
>     - score Hottest Sort
>     - ts Latest Sort
> - limit: Number of comments per page
> - offset: Offset/Page Number
> ### Returns:
> - Zhihu Sub Comment V5
>
> # [示例/Example]
> comment_id = "11100789728"
> order_by = "score"
> limit = "20"
> offset = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| comment_id | query | string | Yes | 评论ID/Comment ID | None | None | None |
| order_by | query | string | No | 排序/Sort | score | None | None |
| limit | query | string | No | 每页评论数量/Number of comments per page | 20 | None | None |
| offset | query | string | No | 偏移量/Offset | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-topic-search-v3"></a>
### `GET /api/u1/v1/zhihu/web/fetch_topic_search_v3`

- Summary: 获取知乎话题搜索V3/Get Zhihu Topic Search V3
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_topic_search_v3_api_v1_zhihu_web_fetch_topic_search_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎话题搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - offset: 偏移量
> - limit: 每页话题数量
> ### 返回:
> - 知乎话题搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu Topic Search V3
> ### Parameters:
> - keyword: Search Keywords
> - offset: Offset
> - limit: Number of topics per page
> ### Returns:
> - Zhihu Topic Search V3
>
> # [示例/Example]
> keyword = "deepseek"
> offset = "0"
> limit = "25"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页话题数量/Number of topics per page | 25 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-follow-collections"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_follow_collections`

- Summary: 获取知乎用户关注的收藏/Get Zhihu User Follow Collections
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follow_collections_api_v1_zhihu_web_fetch_user_follow_collections_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户关注的收藏
> ### 参数:
> - user_url_token: 用户ID
> - offset: 偏移量
> - limit: 每页收藏数量
> ### 返回:
> - 知乎用户关注的收藏
>
> # [English]
> ### Purpose:
> - Get Zhihu User Follow Collections
> ### Parameters:
> - user_url_token: User ID
> - offset: Offset
> - limit: Number of collections per page
> ### Returns:
> - Zhihu User Follow Collections
>
> # [示例/Example]
> user_url_token = "ming-he-43-93"
> offset = "0"
> limit = "20"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_url_token | query | string | Yes | 用户ID/User ID | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页收藏数量/Number of collections per page | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-follow-columns"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_follow_columns`

- Summary: 获取知乎用户订阅的专栏/Get Zhihu User Columns
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follow_columns_api_v1_zhihu_web_fetch_user_follow_columns_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户订阅的专栏
> ### 参数:
> - user_url_token: 用户ID
> - offset: 偏移量
> - limit: 每页专栏数量
> ### 返回:
> - 知乎用户订阅的专栏
>
> # [English]
> ### Purpose:
> - Get Zhihu User Columns
> ### Parameters:
> - user_url_token: User ID
> - offset: Offset
> - limit: Number of columns per page
> ### Returns:
> - Zhihu User Columns
>
> # [示例/Example]
> user_url_token = "ming-he-43-93"
> offset = "0"
> limit = "20"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_url_token | query | string | Yes | 用户ID/User ID | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页专栏数量/Number of columns per page | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-follow-questions"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_follow_questions`

- Summary: 获取知乎用户关注的问题/Get Zhihu User Follow Questions
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follow_questions_api_v1_zhihu_web_fetch_user_follow_questions_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户关注的问题
> ### 参数:
> - user_url_token: 用户ID
> - offset: 偏移量
> - limit: 每页问题数量
> ### 返回:
> - 知乎用户关注的问题
>
> # [English]
> ### Purpose:
> - Get Zhihu User Follow Questions
> ### Parameters:
> - user_url_token: User ID
> - offset: Offset
> - limit: Number of questions per page
> ### Returns:
> - Zhihu User Follow Questions
>
> # [示例/Example]
> user_url_token = "ming-he-43-93"
> offset = "0"
> limit = "20"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_url_token | query | string | Yes | 用户ID/User ID | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页问题数量/Number of questions per page | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-follow-topics"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_follow_topics`

- Summary: 获取知乎用户关注的话题/Get Zhihu User Follow Topics
- Capabilities: profiles / accounts / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follow_topics_api_v1_zhihu_web_fetch_user_follow_topics_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户关注的话题
> ### 参数:
> - user_url_token: 用户ID
> - offset: 偏移量
> - limit: 每页话题数量
> ### 返回:
> - 知乎用户关注的话题
>
> # [English]
> ### Purpose:
> - Get Zhihu User Follow Topics
> ### Parameters:
> - user_url_token: User ID
> - offset: Offset
> - limit: Number of topics per page
> ### Returns:
> - Zhihu User Follow Topics
>
> # [示例/Example]
> user_url_token = "ming-he-43-93"
> offset = "0"
> limit = "20"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_url_token | query | string | Yes | 用户ID/User ID | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页话题数量/Number of topics per page | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-followees"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_followees`

- Summary: 获取知乎用户关注列表/Get Zhihu User Following
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_followees_api_v1_zhihu_web_fetch_user_followees_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户关注列表
> ### 参数:
> - user_url_token: 用户ID
> - offset: 偏移量
> - limit: 每页用户数量
> ### 返回:
> - 知乎用户关注列表
>
> # [English]
> ### Purpose:
> - Get Zhihu User Following
> ### Parameters:
> - user_url_token: User ID
> - offset: Offset
> - limit: Number of users per page
> ### Returns:
> - Zhihu User Following
>
> # [示例/Example]
> user_url_token = "ming-he-43-93"
> offset = "0"
> limit = "20"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_url_token | query | string | Yes | 用户ID/User ID | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页用户数量/Number of users per page | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-followers"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_followers`

- Summary: 获取知乎用户粉丝列表/Get Zhihu User Followers
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_followers_api_v1_zhihu_web_fetch_user_followers_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户粉丝列表
> ### 参数:
> - user_url_token: 用户ID
> - offset: 偏移量
> - limit: 每页用户数量
> ### 返回:
> - 知乎用户粉丝列表
>
> # [English]
> ### Purpose:
> - Get Zhihu User Followers
> ### Parameters:
> - user_url_token: User ID
> - offset: Offset
> - limit: Number of users per page
> ### Returns:
> - Zhihu User Followers
>
> # [示例/Example]
> user_url_token = "ming-he-43-93"
> offset = "0"
> limit = "20"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_url_token | query | string | Yes | 用户ID/User ID | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页用户数量/Number of users per page | 20 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-info"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_info`

- Summary: 获取知乎用户信息/Get Zhihu User Info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_zhihu_web_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户信息
> ### 参数:
> - user_url_token: 用户ID
> ### 返回:
> - 知乎用户信息
>
> # [English]
> ### Purpose:
> - Get Zhihu User Info
> ### Parameters:
> - user_url_token: User ID
> ### Returns:
> - Zhihu User Info
>
> # [示例/Example]
> user_url_token = "ming-he-43-93"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_url_token | query | string | Yes | 用户ID/User ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-user-search-v3"></a>
### `GET /api/u1/v1/zhihu/web/fetch_user_search_v3`

- Summary: 获取知乎用户搜索V3/Get Zhihu User Search V3
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_v3_api_v1_zhihu_web_fetch_user_search_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎用户搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - offset: 偏移量
> - limit: 每页用户数量
> ### 返回:
> - 知乎用户搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu User Search V3
> ### Parameters:
> - keyword: Search Keywords
> - offset: Offset
> - limit: Number of users per page
> ### Returns:
> - Zhihu User Search V3
>
> # [示例/Example]
> keyword = "deepseek"
> offset = "0"
> limit = "25"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页用户数量/Number of users per page | 25 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-video-list"></a>
### `GET /api/u1/v1/zhihu/web/fetch_video_list`

- Summary: 获取知乎首页视频榜/Get Zhihu Video List
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_list_api_v1_zhihu_web_fetch_video_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎首页视频榜
> ### 参数:
> - offset: 偏移量
> - limit: 每页视频数量
> ### 返回:
> - 知乎首页视频榜
>
> # [English]
> ### Purpose:
> - Get Zhihu Video List
> ### Parameters:
> - offset: Offset
> - limit: Number of videos per page
> ### Returns:
> - Zhihu Video List
>
> # [示例/Example]
> offset = ""
> limit = "12"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| limit | query | string | No | 每页视频数量/Number of videos per page | 12 | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |

<a id="get-api-u1-v1-zhihu-web-fetch-video-search-v3"></a>
### `GET /api/u1/v1/zhihu/web/fetch_video_search_v3`

- Summary: 获取知乎视频搜索V3/Get Zhihu Video Search V3
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_v3_api_v1_zhihu_web_fetch_video_search_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取知乎视频搜索V3
> ### 参数:
> - keyword: 搜索关键词
> - limit: 每页视频数量
> - offset: 偏移量
> - search_hash_id: 搜索哈希ID
> ### 返回:
> - 知乎视频搜索V3
>
> # [English]
> ### Purpose:
> - Get Zhihu Video Search V3
> ### Parameters:
> - keyword: Search Keywords
> - limit: Number of videos per page
> - offset: Offset
> - search_hash_id: Search Hash ID
> ### Returns:
> - Zhihu Video Search V3
>
> # [示例/Example]
> keyword = "deepseek"
> limit = "20"
> offset = "0"
> search_hash_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search Keywords | None | None | None |
| limit | query | string | No | 每页视频数量/Number of videos per page | 20 | None | None |
| offset | query | string | No | 偏移量/Offset | 0 | None | None |
| search_hash_id | query | string | No | 搜索哈希ID/Search Hash ID | None | None | None |

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `code`:integer, `request_id`:string, `message`:string, `message_zh`:string, `support`:string, `time`:string, `time_stamp`:integer, `time_zone`:string, ...

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| code | integer | No | HTTP status code \| HTTP状态码 | 200 | None | None |
| request_id | string | No | Unique request identifier \| 唯一请求标识符 | None | None | None |
| message | string | No | Response message (EN-US) \| 响应消息 (English) | Request successful. This request will incur a charge. | None | None |
| message_zh | string | No | Response message (ZH-CN) \| 响应消息 (中文) | 请求成功，本次请求将被计费。 | None | None |
| support | string | No | Support message \| 支持消息 | Discord: https://discord.gg/aMEAS8Xsvz | None | None |
| time | string | No | The time the response was generated \| 生成响应的时间 | None | None | None |
| time_stamp | integer | No | The timestamp the response was generated \| 生成响应的时间戳 | None | None | None |
| time_zone | string | No | The timezone of the response time \| 响应时间的时区 | America/Los_Angeles | None | None |
| docs | string | No | Link to the API Swagger documentation for this endpoint \| 此端点的 API Swagger 文档链接 | None | None | None |
| cache_message | string | No | Cache message (EN-US) \| 缓存消息 (English) | This request will be cached. You can access the cached result directly using th… | None | None |
| cache_message_zh | string | No | Cache message (ZH-CN) \| 缓存消息 (中文) | 本次请求将被缓存，你可以使用下面的 URL 直接访问缓存结果，有效期为 24 小时，访问缓存不会产生额外费用。 | None | None |
| cache_url | string | No | The URL to access the cached result \| 访问缓存结果的 URL | None | None | None |
| router | string | No | The endpoint that generated this response \| 生成此响应的端点 | None | None | None |
| params | dynamic object | No | The parameters used in the request \| 请求中使用的参数 | None | None | None |
| data | null | No | The response data \| 响应数据 | None | None | None |
