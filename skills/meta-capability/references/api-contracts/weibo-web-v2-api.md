# Weibo-Web-V2-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/weibo-web-v2-api.md`](../api-tags/weibo-web-v2-api.md)
- Current contract file: `api-contracts/weibo-web-v2-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `33`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(新浪微博 Web V2 数据接口/Weibo-Web-V2-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-weibo-web-v2-check-allow-comment-with-pic"></a>
### `GET /api/u1/v1/weibo/web_v2/check_allow_comment_with_pic`

- Summary: 检查微博是否允许带图评论/Check if Weibo allows image comments
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `check_allow_comment_with_pic_api_v1_weibo_web_v2_check_allow_comment_with_pic_get`

#### Notes

> # [中文]
> ### 用途:
> - 检查指定微博是否允许用户在评论时上传图片。
> ### 参数:
> - id: 微博ID（必填）
> ### 返回:
> - result: true表示允许带图评论，false表示不允许
> ### 注意:
> - 不同微博的图片评论权限可能不同
>
> # [English]
> ### Purpose:
> - Check if a specific Weibo post allows image comments.
> ### Parameters:
> - id: Weibo post ID (required)
> ### Return:
> - result: true means image comments allowed, false means not allowed
> ### Note:
> - Different posts may have different image comment permissions
>
> # [示例/Example]
> id = "5092682368025584"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | Yes | 微博ID/Weibo ID | None | 5092682368025584 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-advanced-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_advanced_search`

- Summary: 微博高级搜索/Weibo Advanced Search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_advanced_search_api_v1_weibo_web_v2_fetch_advanced_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 微博高级搜索，支持多维度筛选。
> ### 参数:
> - q: 搜索关键词（必填）
> - search_type: 搜索类型（all/hot/original/verified/media/viewpoint）
> - include_type: 包含类型（all/pic/video/music/link）
> - timescope: 时间范围（格式: custom:开始日期:结束日期，如 custom:2025-09-01-0:2025-09-08-23）
> - page: 页码（默认1）
> ### 返回:
> - 搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等
> ### 注意:
> - 视频播放需设置请求头 Referer=https://weibo.com/
>
> # [English]
> ### Purpose:
> - Weibo advanced search with multi-dimensional filtering.
> ### Parameters:
> - q: Search keyword (required)
> - search_type: Search type (all/hot/original/verified/media/viewpoint)
> - include_type: Include type (all/pic/video/music/link)
> - timescope: Time scope (format: custom:start_date:end_date, e.g. custom:2025-09-01-0:2025-09-08-23)
> - page: Page number (default 1)
> ### Return:
> - Search result list, including post content, author info, images, videos, interaction data
> ### Note:
> - Video playback requires setting header Referer=https://weibo.com/
>
> # [示例/Example]
> q = "python"
> search_type = "hot"
> include_type = "pic"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q | query | string | Yes | 搜索关键词/Search keyword | None | yu7 | None |
| search_type | query | string | No | 搜索类型/Search type: all(全部), hot(热门), original(原创), verified(认证用户), media(媒体), viewpoint(观点) | None | hot | None |
| include_type | query | string | No | 包含类型/Include type: all(全部), pic(含图片), video(含视频), music(含音乐), link(含短链) | None | pic | None |
| timescope | query | string | No | 时间范围/Time scope (custom:start:end) | None | custom:2025-09-01-0:2025-09-08-23 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-ai-related-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_ai_related_search`

- Summary: 微博AI搜索内容扩展/Weibo AI Search Content Extension
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_ai_related_search_api_v1_weibo_web_v2_fetch_ai_related_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取与关键词相关的内容扩展（相关问题、博主推荐、参考博文等）。
> ### 参数:
> - keyword: 搜索关键词（必填，建议使用话题格式#话题名#）
> ### 返回:
> - HTML格式的扩展内容，包含相关问题、博主推荐、参考博文等
> ### 注意:
> - 返回内容为HTML格式，需要进行HTML解析处理
> - HTML结构可能会发生变化，需要做好容错处理
>
> # [English]
> ### Purpose:
> - Get content extensions related to keyword (related questions, blogger recommendations, reference posts).
> ### Parameters:
> - keyword: Search keyword (required, recommend using topic format #TopicName#)
> ### Return:
> - HTML format extension content, including related questions, blogger recommendations, reference posts
> ### Note:
> - Returned content is in HTML format, requires HTML parsing
> - HTML structure may change, need proper error handling
>
> # [示例/Example]
> keyword = "#微博奇遇记#"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | #微博奇遇记# | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-ai-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_ai_search`

- Summary: 微博智能搜索/Weibo AI Search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_ai_search_api_v1_weibo_web_v2_fetch_ai_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过微博AI智能搜索获取搜索结果。
> ### 参数:
> - query: 搜索关键词（必填，建议使用话题格式#话题名#）
> ### 返回:
> - AI搜索结果，包含推荐内容、相关话题等
> ### 注意:
> - AI搜索结果会根据用户行为进行个性化调整
>
> # [English]
> ### Purpose:
> - Get search results through Weibo AI intelligent search.
> ### Parameters:
> - query: Search keyword (required, recommend using topic format #TopicName#)
> ### Return:
> - AI search results, including recommended content, related topics
> ### Note:
> - AI search results are personalized based on user behavior
>
> # [示例/Example]
> query = "#法国#"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | #法国# | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-all-groups"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_all_groups`

- Summary: 获取所有分组信息/Get all groups information
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_all_groups_api_v1_weibo_web_v2_fetch_all_groups_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博平台的所有分组信息，包括默认分组和用户自定义分组。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 分组列表，包含分组ID、名称、容器ID等
> ### 注意:
> - 返回的gid和containerid可用于时间轴接口的参数
> - 分组信息变化不频繁，建议缓存
>
> # [English]
> ### Purpose:
> - Get all group information on Weibo platform, including default and user-defined groups.
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Group list, including group ID, name, container ID, etc.
> ### Note:
> - Returned gid and containerid can be used as parameters for timeline API
> - Group information changes infrequently, recommend caching
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-city-list"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_city_list`

- Summary: 地区省市映射/Region City List
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_city_list_api_v1_weibo_web_v2_fetch_city_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取地区省市映射数据，用于用户搜索等接口的地区筛选参数。
> ### 参数:
> - normalized: 是否返回标准化结构（默认True）
> ### 返回:
> - 省市映射数据，用于fetch_user_search等接口的region参数
> ### 注意:
> - 返回的编码格式为 custom:省代码:市代码，如 custom:11:1
>
> # [English]
> ### Purpose:
> - Get region city mapping data for region filter parameter in user search APIs.
> ### Parameters:
> - normalized: Whether to return normalized structure (default True)
> ### Return:
> - Province-city mapping data, for region parameter in fetch_user_search and other APIs
> ### Note:
> - Returned code format is custom:province_code:city_code, e.g. custom:11:1
>
> # [示例/Example]
> normalized = True

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| normalized | query | boolean | No | 是否返回标准化结构（省份列表+城市数组）/Whether to return normalized structure | true | None | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-entertainment-ranking"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_entertainment_ranking`

- Summary: 获取微博文娱榜单/Get Weibo entertainment ranking
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_entertainment_ranking_api_v1_weibo_web_v2_fetch_entertainment_ranking_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博文娱榜单数据（娱乐圈、影视、综艺等）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 文娱话题列表，包含话题、热度值、排名、分类等
> ### 注意:
> - 建议缓存5-10分钟
>
> # [English]
> ### Purpose:
> - Get Weibo entertainment ranking data (entertainment, film & TV, variety shows).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Entertainment topic list, including topic, heat value, rank, category
> ### Note:
> - Recommend caching for 5-10 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-ranking-timeline"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_ranking_timeline`

- Summary: 获取微博热门榜单时间轴/Get hot ranking timeline
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_ranking_timeline_api_v1_weibo_web_v2_fetch_hot_ranking_timeline_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博平台各种类型的热门榜单内容。
> ### 参数:
> - ranking_type: 榜单类型（必填）
>     - hour: 小时榜
>     - yesterday: 昨日榜
>     - day_before: 前日榜
>     - week: 周榜
>     - male: 男榜
>     - female: 女榜
> - max_id: 翻页游标，首次请求传"0"
> - count: 获取数量（默认10）
> ### 返回:
> - 热门微博列表，包含微博内容、作者信息、互动数据等
> ### 注意:
> - 不同榜单更新频率不同：小时榜实时性最强，周榜影响力较大
>
> # [English]
> ### Purpose:
> - Get various types of hot ranking content from Weibo platform.
> ### Parameters:
> - ranking_type: Ranking type (required)
>     - hour: Hourly ranking
>     - yesterday: Yesterday ranking
>     - day_before: Day before ranking
>     - week: Weekly ranking
>     - male: Male ranking
>     - female: Female ranking
> - max_id: Pagination cursor, pass "0" for first request
> - count: Count (default 10)
> ### Return:
> - Hot post list, including post content, author info, interaction data
> ### Note:
> - Different rankings have different update frequencies: hourly has highest real-time relevance, weekly has high influence
>
> # [示例/Example]
> ranking_type = "hour"
> max_id = "0"
> count = 10

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ranking_type | query | string | Yes | 榜单类型：hour=小时榜，yesterday=昨日榜，day_before=前日榜，week=周榜，male=男榜，female=女榜/Ranking type: hour=hourly, yesterday=yesterday, day_before=day before, week=weekly, male=male ranking, female=… | None | hour | None |
| since_id | query | string | No | 分页标识，默认为0/Pagination identifier, default is 0 | 0 | 0 | None |
| max_id | query | string | No | 最大ID，默认为0/Max ID, default is 0 | 0 | 0 | None |
| count | query | integer | No | 获取数量，默认10/Count, default is 10 | 10 | 10 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search`

- Summary: 获取微博热搜榜单/Get Weibo hot search ranking
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_search_api_v1_weibo_web_v2_fetch_hot_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博实时热搜榜单数据。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 热搜数据，包含realtime（实时热搜）、hotgov等多个板块
> ### 注意:
> - 热搜更新频繁，建议缓存2-5分钟
>
> # [English]
> ### Purpose:
> - Get Weibo real-time hot search ranking data.
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Hot search data, including realtime (real-time hot search), hotgov and other sections
> ### Note:
> - Hot search updates frequently, recommend caching for 2-5 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-search-index"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_index`

- Summary: 获取微博热搜词条(10条)/Get Weibo hot search index (10 items)
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_search_index_api_v1_weibo_web_v2_fetch_hot_search_index_get`

#### Notes

> # [中文]
> ### 用途:
> - 快速获取微博热搜前10条。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 热搜词条列表，包含关键词、热度值、排名等
> ### 注意:
> - 只返回前10条热搜
> - 热搜更新频繁，建议缓存2-5分钟
> - 如需完整热搜，使用fetch_hot_search_summary
>
> # [English]
> ### Purpose:
> - Quickly get top 10 Weibo hot search items.
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Hot search term list, including keyword, popularity value, rank
> ### Note:
> - Only returns top 10 hot search items
> - Hot search updates frequently, recommend caching for 2-5 minutes
> - For complete hot search, use fetch_hot_search_summary
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-hot-search-summary"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_hot_search_summary`

- Summary: 获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items)
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_search_summary_api_v1_weibo_web_v2_fetch_hot_search_summary_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博完整热搜榜单（50条）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 完整热搜列表，包含排名、关键词、标签（热点/沸点/官宣/新）、热度值
> ### 注意:
> - 与fetch_hot_search_index的区别：本接口返回50条，fetch_hot_search_index返回10条
> - rank为0表示置顶内容
> - 建议缓存5-10分钟
>
> # [English]
> ### Purpose:
> - Get complete Weibo hot search ranking (50 items).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Complete hot search list, including rank, keyword, tag (Hot/Boiling/Official/New), heat value
> ### Note:
> - Difference from fetch_hot_search_index: this API returns 50 items, fetch_hot_search_index returns 10 items
> - rank 0 indicates pinned content
> - Recommend caching for 5-10 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-life-ranking"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_life_ranking`

- Summary: 获取微博生活榜单/Get Weibo life ranking
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_life_ranking_api_v1_weibo_web_v2_fetch_life_ranking_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博生活榜单数据（美食、旅游、健康、时尚等）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 生活话题列表，包含话题、热度值、排名、分类等
> ### 注意:
> - 建议缓存5-10分钟
>
> # [English]
> ### Purpose:
> - Get Weibo life ranking data (food, travel, health, fashion).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Life topic list, including topic, heat value, rank, category
> ### Note:
> - Recommend caching for 5-10 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-pic-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_pic_search`

- Summary: 图片搜索/Weibo picture search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_pic_search_api_v1_weibo_web_v2_fetch_pic_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索微博图片内容，按微博ID聚合多图。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码（默认1）
> ### 返回:
> - 图片列表，包含微博ID、缩略图、原图链接、作者信息、图片数量
> ### 注意:
> - 缩略图会自动转换为原图链接
>
> # [English]
> ### Purpose:
> - Search Weibo picture content, aggregated by weibo ID.
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number (default 1)
> ### Return:
> - Image list with weibo ID, thumbnail, large image URL, author info, image count
> ### Note:
> - Thumbnails are automatically converted to large image URLs
>
> # [示例/Example]
> query = "yu7"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | yu7 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-post-comments"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_post_comments`

- Summary: 获取微博评论/Get Weibo comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_api_v1_weibo_web_v2_fetch_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定微博的一级评论列表。
> ### 参数:
> - id: 微博ID（必填）
> - count: 评论数量（默认10）
> - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值
> ### 返回:
> - 评论列表数据，包含评论内容、评论者信息、点赞数等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 当没有更多评论时，max_id 为空
>
> # [English]
> ### Purpose:
> - Get the first-level comment list of specified post.
> ### Parameters:
> - id: Weibo post ID (required)
> - count: Number of comments (default 10)
> - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests
> ### Return:
> - Comment list data, including comment content, commenter info, likes count
> - Contains max_id field for pagination
> ### Note:
> - When no more comments, max_id is empty
>
> # [示例/Example]
> id = "5188973773455957"
> count = 10
> max_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | Yes | 微博ID/Weibo ID | None | 5188973773455957 | None |
| count | query | integer | No | 评论数量/Number of comments | 10 | 10 | None |
| max_id | query | string | No | 页码/Page number | None | None | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-post-detail"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_post_detail`

- Summary: 获取单个作品数据/Get single post data
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_detail_api_v1_weibo_web_v2_fetch_post_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定微博的详细信息，包括内容、作者、互动数据等。
> ### 参数:
> - id: 微博ID（必填）
> - is_get_long_text: 是否获取长微博全文（默认"true"）
> ### 返回:
> - 微博详细数据，包含完整文本、图片、视频、点赞数、评论数、转发数等
>
> # [English]
> ### Purpose:
> - Get detailed information of a specific Weibo post, including content, author, interaction data.
> ### Parameters:
> - id: Weibo post ID (required)
> - is_get_long_text: Whether to get full text of long posts (default "true")
> ### Return:
> - Post detailed data, including full text, images, videos, likes, comments, reposts count
>
> # [示例/Example]
> id = "5092682368025584"
> is_get_long_text = "true"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | Yes | 作品id/Post id | None | 5092682368025584 | None |
| is_get_long_text | query | string | No | 是否获取长微博全文/Whether to get the full text of long Weibo posts (true/false) | true | true | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-post-sub-comments"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_post_sub_comments`

- Summary: 获取微博子评论/Get Weibo sub-comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_sub_comments_api_v1_weibo_web_v2_fetch_post_sub_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定评论的回复（子评论）列表。
> ### 参数:
> - id: 主评论ID（必填）
> - count: 子评论数量（默认10）
> - max_id: 翻页游标，首次请求传空，后续请求使用返回的max_id值
> ### 返回:
> - 子评论列表数据，包含回复内容、回复者信息、点赞数等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 与fetch_post_comments的区别：本接口获取的是评论的回复，而非微博的主评论
>
> # [English]
> ### Purpose:
> - Get the reply (sub-comment) list of a specified comment.
> ### Parameters:
> - id: Main comment ID (required)
> - count: Number of sub-comments (default 10)
> - max_id: Pagination cursor, pass empty for first request, use returned max_id for subsequent requests
> ### Return:
> - Sub-comment list data, including reply content, replier info, likes count
> - Contains max_id field for pagination
> ### Note:
> - Difference from fetch_post_comments: this API gets replies to comments, not main comments of posts
>
> # [示例/Example]
> id = "5201793550385562"
> count = 10
> max_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | query | string | Yes | 主评论ID/Comment ID | None | 5201793550385562 | None |
| count | query | integer | No | 子评论数量/Number of sub-comments | 10 | 10 | None |
| max_id | query | string | No | 分页标识/Page identifier | None | None | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-realtime-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_realtime_search`

- Summary: 实时搜索/Weibo Realtime Search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_realtime_search_api_v1_weibo_web_v2_fetch_realtime_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博实时搜索结果（按时间排序的最新微博）。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码（默认1）
> ### 返回:
> - 实时搜索结果列表，包含微博内容、作者信息、图片、视频、互动数据等
> ### 注意:
> - 视频播放需设置请求头 Referer=https://weibo.com/
> - 返回结构与高级搜索一致
>
> # [English]
> ### Purpose:
> - Get Weibo realtime search results (latest posts sorted by time).
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number (default 1)
> ### Return:
> - Realtime search result list, including post content, author info, images, videos, interaction data
> ### Note:
> - Video playback requires setting header Referer=https://weibo.com/
> - Return structure is same as advanced search
>
> # [示例/Example]
> query = "苹果发布会"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | yu7 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-similar-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_similar_search`

- Summary: 获取微博相似搜索词推荐/Get Weibo similar search recommendations
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_similar_search_api_v1_weibo_web_v2_fetch_similar_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词获取微博推荐的相似搜索词。
> ### 参数:
> - keyword: 搜索关键词（必填，支持话题标签格式如#话题名#）
> ### 返回:
> - 相似搜索词列表，包含推荐词、搜索次数等
> ### 注意:
> - 相似词推荐相对稳定，可缓存15-30分钟
>
> # [English]
> ### Purpose:
> - Get similar search word recommendations based on keyword.
> ### Parameters:
> - keyword: Search keyword (required, supports topic tag format like #TopicName#)
> ### Return:
> - Similar search term list, including suggestion, search count
> ### Note:
> - Similar word recommendations are relatively stable, can cache for 15-30 minutes
>
> # [示例/Example]
> keyword = "#微博奇遇记#"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | #微博奇遇记# | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-social-ranking"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_social_ranking`

- Summary: 获取微博社会榜单/Get Weibo social ranking
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_social_ranking_api_v1_weibo_web_v2_fetch_social_ranking_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博社会榜单数据（时事新闻、社会热点、民生话题等）。
> ### 参数:
> - 无需额外参数
> ### 返回:
> - 社会话题列表，包含话题、热度值、排名、分类等
> ### 注意:
> - 社会热点变化较快，建议缓存2-5分钟
>
> # [English]
> ### Purpose:
> - Get Weibo social ranking data (current affairs, social hotspots, livelihood topics).
> ### Parameters:
> - No additional parameters required
> ### Return:
> - Social topic list, including topic, heat value, rank, category
> ### Note:
> - Social hotspots change rapidly, recommend caching for 2-5 minutes
>
> # [示例/Example]
> # No parameters needed

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-topic-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_topic_search`

- Summary: 话题搜索/Weibo topic search
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_topic_search_api_v1_weibo_web_v2_fetch_topic_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索微博话题，获取话题名称、封面、讨论量、阅读量。
> ### 参数:
> - query: 搜索关键词（必填）
> - page: 页码（默认1）
> ### 返回:
> - 话题列表，包含话题名、封面图、讨论数、阅读数
> ### 注意:
> - 数量单位（万/亿）已转换为整数
>
> # [English]
> ### Purpose:
> - Search Weibo topics, get topic name, cover, discussion count, read count.
> ### Parameters:
> - query: Search keyword (required)
> - page: Page number (default 1)
> ### Return:
> - Topic list with topic name, cover image, discussion count, read count
> ### Note:
> - Count units (万/亿) are converted to integers
>
> # [示例/Example]
> query = "yu7"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | yu7 | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-basic-info"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_basic_info`

- Summary: 获取用户基本信息/Get user basic information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_basic_info_api_v1_weibo_web_v2_fetch_user_basic_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博用户的基本信息（轻量级接口）。
> ### 参数:
> - uid: 用户ID（必填）
> ### 返回:
> - 用户基本信息，包括用户ID、用户名、头像、简介、认证信息
> ### 注意:
> - 与fetch_user_info相比，本接口返回数据更少，响应更快
> - 适合批量用户信息获取和用户卡片展示
>
> # [English]
> ### Purpose:
> - Get basic information of Weibo users (lightweight API).
> ### Parameters:
> - uid: User ID (required)
> ### Return:
> - User basic info, including user ID, username, avatar, bio, verification
> ### Note:
> - Compared to fetch_user_info, this API returns less data with faster response
> - Suitable for batch user info retrieval and user card display
>
> # [示例/Example]
> uid = "7277477906"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id | None | 7277477906 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-fans"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_fans`

- Summary: 获取用户粉丝列表/Get user fans list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_fans_api_v1_weibo_web_v2_fetch_user_fans_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的粉丝列表（谁关注了该用户）。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从0开始（默认0）
> ### 返回:
> - 粉丝用户列表，包含用户名、头像、简介、粉丝数等
> ### 注意:
> - 粉丝列表受用户隐私设置影响
> - page参数从0开始，而不是1
> - 与fetch_user_following的区别：本接口获取谁关注了该用户，fetch_user_following获取用户关注了谁
>
> # [English]
> ### Purpose:
> - Get the fans list of specified user (who follows the user).
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 0 (default 0)
> ### Return:
> - Fans user list, including username, avatar, bio, followers count
> ### Note:
> - Fans list affected by user privacy settings
> - page parameter starts from 0, not 1
> - Difference from fetch_user_following: this API gets who follows the user, fetch_user_following gets who user follows
>
> # [示例/Example]
> uid = "1722594714"
> page = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户ID/User ID | None | 1722594714 | None |
| page | query | integer | No | 页码/Page number | 0 | 0 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-following"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_following`

- Summary: 获取用户关注列表/Get user following list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_following_api_v1_weibo_web_v2_fetch_user_following_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的关注列表（该用户关注了谁）。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从0开始（默认0）
> ### 返回:
> - 关注用户列表，包含用户名、头像、简介、粉丝数等
> ### 注意:
> - 关注列表受用户隐私设置影响
> - page参数从0开始，而不是1
> - 与fetch_user_fans的区别：本接口获取用户关注了谁，fetch_user_fans获取谁关注了该用户
>
> # [English]
> ### Purpose:
> - Get the following list of specified user (who the user follows).
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 0 (default 0)
> ### Return:
> - Following user list, including username, avatar, bio, followers count
> ### Note:
> - Following list affected by user privacy settings
> - page parameter starts from 0, not 1
> - Difference from fetch_user_fans: this API gets who user follows, fetch_user_fans gets who follows the user
>
> # [示例/Example]
> uid = "1722594714"
> page = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户ID/User ID | None | 1722594714 | None |
| page | query | integer | No | 页码/Page number | 0 | 0 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-info"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_info`

- Summary: 获取用户信息/Get user information
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_weibo_web_v2_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博用户的详细信息，包括昵称、头像、简介、关注数、粉丝数等。
> ### 参数:
> - uid: 用户ID（可选，与custom二选一）
> - custom: 自定义用户名（可选，与uid二选一）
> ### 返回:
> - 用户详细信息数据
> ### 注意:
> - uid和custom参数至少需要提供一个
> - 如果同时提供，优先使用uid
> - 建议优先使用uid参数
>
> # [English]
> ### Purpose:
> - Get detailed information of Weibo users, including nickname, avatar, bio, following count, followers count.
> ### Parameters:
> - uid: User ID (optional, choose one with custom)
> - custom: Custom username (optional, choose one with uid)
> ### Return:
> - User detailed information data
> ### Note:
> - At least one of uid and custom must be provided
> - If both provided, uid takes priority
> - It's recommended to use uid parameter first
>
> # [示例/Example]
> uid = "1722594714"
> # or
> custom = "shuqi"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | No | 用户id/User id | None | 1722594714 | None |
| custom | query | string | No | 自定义微博用户名/Custom Weibo username | None | shuqi | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-original-posts"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_original_posts`

- Summary: 获取微博用户原创微博数据/Get Weibo user original posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_original_posts_api_v1_weibo_web_v2_fetch_user_original_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户发布的原创微博列表（排除转发内容）。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从1开始（默认1）
> - since_id: 翻页标识（第一页必须从fetch_user_posts接口获取）
> ### 返回:
> - 原创微博列表，包含微博内容、图片、视频、互动数据等
> ### 注意:
> - 与fetch_user_posts的区别：本接口只返回原创微博，排除转发
> - since_id必须先调用fetch_user_posts获取，第一页必传，后续页面不传
>
> # [English]
> ### Purpose:
> - Get original posts published by specified user (excluding reposts).
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 1 (default 1)
> - since_id: Pagination identifier (first page must get from fetch_user_posts)
> ### Return:
> - Original post list, including content, images, videos, interaction data
> ### Note:
> - Difference from fetch_user_posts: this API only returns original posts, excludes reposts
> - since_id must be obtained from fetch_user_posts first, required for first page, not needed for subsequent pages
>
> # [示例/Example]
> uid = "7277477906"
> page = 1
> since_id = "4924526881242703"  # from fetch_user_posts response

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id | None | 7277477906 | None |
| page | query | integer | No | 页数/Page number | 1 | 1 | None |
| since_id | query | string | No | 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data | None | None | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-posts"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_posts`

- Summary: 获取微博用户文章数据/Get Weibo user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_api_v1_weibo_web_v2_fetch_user_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户发布的微博列表，支持分页和多种数据详细程度。
> ### 参数:
> - uid: 用户ID（必填）
> - page: 页码，从1开始（默认1）
> - feature: 数据特征值（默认0）
>     - 0: 返回10条基础数据
>     - 1: 返回20条扩展数据
>     - 2: 返回20条图片相关数据
>     - 3: 返回20条完整数据
> - since_id: 翻页标识，用于获取下一页数据
> ### 返回:
> - 微博列表数据，包含微博内容、图片、视频等信息
> - 包含 since_id 字段用于翻页
> ### 注意:
> - feature=0性能最佳，feature=3数据最全
>
> # [English]
> ### Purpose:
> - Get the list of posts published by specified user, support pagination and multiple data detail levels.
> ### Parameters:
> - uid: User ID (required)
> - page: Page number, starts from 1 (default 1)
> - feature: Data feature value (default 0)
>     - 0: Return 10 basic posts
>     - 1: Return 20 extended posts
>     - 2: Return 20 image-related posts
>     - 3: Return 20 complete posts
> - since_id: Pagination identifier for next page
> ### Return:
> - Post list data, including post content, images, videos, etc.
> - Contains since_id field for pagination
> ### Note:
> - feature=0 has best performance, feature=3 has most complete data
>
> # [示例/Example]
> uid = "7277477906"
> page = 1
> feature = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id | None | 7277477906 | None |
| page | query | integer | No | 页数/Page number | 1 | 1 | None |
| feature | query | integer | No | 特征值，控制返回数据的数量和字段：0=返回10条基础数据，1=返回20条扩展数据，2=返回20条图片相关数据，3=返回20条视频相关数据，字段逐级增加/Feature type: 0=10 basic posts, 1=20 extended posts, 2=20 image-related posts, 3=20 video-related posts… | 0 | 0 | None |
| since_id | query | string | No | 翻页标识，用于获取下一页数据/Pagination identifier for getting next page data | None | None | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-recommend-timeline"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_recommend_timeline`

- Summary: 获取微博主页推荐时间轴/Get user recommend timeline
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_recommend_timeline_api_v1_weibo_web_v2_fetch_user_recommend_timeline_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取微博主页的推荐时间轴内容，基于用户兴趣展示个性化推荐。
> ### 参数:
> - refresh: 刷新类型（0=正常刷新，1=强制刷新）
> - group_id: 分组ID（可通过fetch_all_groups获取）
> - containerid: 容器ID（通常与group_id相同）
> - extparam: 扩展参数（默认"discover|new_feed"）
> - max_id: 翻页游标，首次请求传"0"
> - count: 获取数量（默认10，建议5-20）
> ### 返回:
> - 推荐微博列表，包含微博内容、作者信息、互动数据等
> - 包含 max_id 字段用于翻页
> ### 注意:
> - 建议先调用fetch_all_groups获取可用分组
>
> # [English]
> ### Purpose:
> - Get recommended timeline content from Weibo homepage, displaying personalized recommendations based on user interests.
> ### Parameters:
> - refresh: Refresh type (0=normal refresh, 1=force refresh)
> - group_id: Group ID (can be obtained through fetch_all_groups)
> - containerid: Container ID (usually same as group_id)
> - extparam: Extended parameters (default "discover|new_feed")
> - max_id: Pagination cursor, pass "0" for first request
> - count: Count (default 10, suggested 5-20)
> ### Return:
> - Recommended post list, including post content, author info, interaction data
> - Contains max_id field for pagination
> ### Note:
> - Recommend calling fetch_all_groups first to get available groups
>
> # [示例/Example]
> refresh = 0
> group_id = "102803"
> containerid = "102803"
> max_id = "0"
> count = 10

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| refresh | query | integer | No | 刷新类型，0=正常刷新，1=强制刷新/Refresh type, 0=normal refresh, 1=force refresh | 0 | 0 | None |
| group_id | query | string | No | 分组ID/Group ID | 102803 | 102803 | None |
| containerid | query | string | No | 容器ID/Container ID | 102803 | 102803 | None |
| extparam | query | string | No | 扩展参数/Extended parameters | discover\|new_feed | discover\|new_feed | None |
| max_id | query | string | No | 最大ID/Max ID | 0 | 0 | None |
| count | query | integer | No | 获取数量/Count | 10 | 10 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_search`

- Summary: 用户搜索/User search
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_api_v1_weibo_web_v2_fetch_user_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索微博用户，支持多种筛选条件。
> ### 参数:
> - query: 搜索关键词（可选）
> - page: 页码（默认1）
> - region: 地区编码，从/fetch_city_list获取（可选）
> - auth: 认证类型 org_vip/per_vip/ord（可选）
> - gender: 性别 man/women（可选）
> - age: 年龄段 18y/22y/29y/39y/40y（可选）
> - nickname: 昵称筛选（可选）
> - tag: 标签筛选（可选）
> - school: 学校筛选（可选）
> - work: 公司筛选（可选）
> ### 返回:
> - 用户列表，包含uid、昵称、头像、粉丝数、主页链接
> ### 注意:
> - 筛选参数过多可能导致无结果
>
> # [English]
> ### Purpose:
> - Search Weibo users with multiple filter options.
> ### Parameters:
> - query: Search keyword (optional)
> - page: Page number (default 1)
> - region: Region code from /fetch_city_list (optional)
> - auth: Auth type org_vip/per_vip/ord (optional)
> - gender: Gender man/women (optional)
> - age: Age bucket 18y/22y/29y/39y/40y (optional)
> - nickname: Nickname filter (optional)
> - tag: Tag filter (optional)
> - school: School filter (optional)
> - work: Company filter (optional)
> ### Return:
> - User list with uid, nickname, avatar, fans count, profile URL
> ### Note:
> - Too many filters may result in no results
>
> # [示例/Example]
> query = "yu7"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | No | 搜索关键词/Query（提供则视为“全部”搜索；留空则仅应用高级筛选参数） | None | yu7 | None |
| page | query | integer | No | 页码/Page | 1 | 1 | None |
| region | query | string | No | 地区编码，从 /city_list 获取/Region code from /city_list | None | custom:11:1 | None |
| auth | query | string | No | 认证类型 org_vip(机构)/per_vip(个人)/ord(普通)/Auth type | None | org_vip | None |
| gender | query | string | No | 性别 man / women / Gender | None | man | None |
| age | query | string | No | 年龄段 18y/22y/29y/39y/40y / Age bucket | None | 22y | None |
| nickname | query | string | No | 昵称筛选/Nickname filter | None | 张三 | None |
| tag | query | string | No | 标签筛选/Tag filter | None | 摄影 | None |
| school | query | string | No | 学校筛选/School filter | None | 清华大学 | None |
| work | query | string | No | 公司筛选/Company filter | None | 字节跳动 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-detail"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_detail`

- Summary: 获取用户微博视频收藏夹详情/Get user video collection detail
- Capabilities: profiles / accounts / content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_video_collection_detail_api_v1_weibo_web_v2_fetch_user_video_collection_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定收藏夹的详细内容，包括视频列表。
> ### 参数:
> - cid: 收藏夹ID（必填，从fetch_user_video_collection_list获取）
> - cursor: 分页游标，首次请求传空，后续使用返回的cursor
> - tab_code: 排序方式（0=默认，1=最热，2=最新）
> ### 返回:
> - 收藏夹信息和视频列表，包含视频标题、封面、时长、播放数等
> - 包含 next_cursor 和 has_more 字段用于翻页
> ### 注意:
> - 不同排序方式的cursor不通用，切换排序需重新开始分页
>
> # [English]
> ### Purpose:
> - Get detailed content of specified collection, including video list.
> ### Parameters:
> - cid: Collection ID (required, get from fetch_user_video_collection_list)
> - cursor: Pagination cursor, pass empty for first request, use returned cursor for subsequent
> - tab_code: Sort type (0=default, 1=hottest, 2=latest)
> ### Return:
> - Collection info and video list, including video title, cover, duration, views
> - Contains next_cursor and has_more fields for pagination
> ### Note:
> - Cursors for different sorting methods are not universal, switching sorting requires restarting pagination
>
> # [示例/Example]
> cid = "4883992307236954"
> cursor = ""
> tab_code = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cid | query | string | Yes | 收藏夹ID/Collection ID | None | 4883992307236954 | None |
| cursor | query | string | No | 分页游标/Pagination cursor | None | None | None |
| tab_code | query | integer | No | 排序方式：0=默认，1=最热，2=最新/Sort type: 0=default, 1=hottest, 2=latest | 0 | 0 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-video-collection-list"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_collection_list`

- Summary: 获取用户微博视频收藏夹列表/Get user video collection list
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_video_collection_list_api_v1_weibo_web_v2_fetch_user_video_collection_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的视频收藏夹列表。
> ### 参数:
> - uid: 用户ID（必填）
> ### 返回:
> - 收藏夹列表，包含收藏夹ID、名称、描述、视频数量等
> ### 注意:
> - 收藏夹列表受用户隐私设置影响
> - 部分用户可能没有创建视频收藏夹
>
> # [English]
> ### Purpose:
> - Get video collection list of specified user.
> ### Parameters:
> - uid: User ID (required)
> ### Return:
> - Collection list, including collection ID, name, description, video count
> ### Note:
> - Collection list affected by user privacy settings
> - Some users may not have created video collections
>
> # [示例/Example]
> uid = "7277477906"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户ID/User ID | None | 7277477906 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-user-video-list"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_user_video_list`

- Summary: 获取微博用户全部视频/Get user all videos
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_video_list_api_v1_weibo_web_v2_fetch_user_video_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户发布的所有视频内容（瀑布流展示）。
> ### 参数:
> - uid: 用户ID（必填）
> - cursor: 翻页游标，初次请求传"0"，后续请求使用返回的next_cursor值
> ### 返回:
> - 视频列表数据，包含视频标题、封面、播放量等信息
> - 包含 next_cursor 和 has_more 字段用于翻页
> ### 注意:
> - 与收藏夹接口的区别：本接口获取用户发布的视频，收藏夹接口获取用户收藏的视频
>
> # [English]
> ### Purpose:
> - Get all videos published by specified user (waterfall layout).
> ### Parameters:
> - uid: User ID (required)
> - cursor: Pagination cursor, pass "0" for first request, use returned next_cursor for subsequent requests
> ### Return:
> - Video list data, including video title, cover, views, etc.
> - Contains next_cursor and has_more fields for pagination
> ### Note:
> - Difference from collection APIs: this API gets user published videos, collection APIs get user collected videos
>
> # [示例/Example]
> uid = "7277477906"
> cursor = "0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户ID/User ID | None | 7277477906 | None |
| cursor | query | string | No | 分页游标/Pagination cursor | 0 | 0 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-fetch-video-search"></a>
### `GET /api/u1/v1/weibo/web_v2/fetch_video_search`

- Summary: 视频搜索（热门/全部）/Weibo video search (hot/all)
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_api_v1_weibo_web_v2_fetch_video_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索微博视频内容，支持热门和全部模式。
> ### 参数:
> - query: 搜索关键词（必填）
> - mode: 搜索模式 hot=热门 / all=全部（默认hot）
> - page: 页码（默认1）
> ### 返回:
> - 视频列表，包含微博ID、作者、内容、视频链接、互动数据
> ### 注意:
> - 播放视频需设置Referer=https://weibo.com/
>
> # [English]
> ### Purpose:
> - Search Weibo video content, supports hot and all modes.
> ### Parameters:
> - query: Search keyword (required)
> - mode: Search mode hot=popular / all=all (default hot)
> - page: Page number (default 1)
> ### Return:
> - Video list with weibo ID, author, content, video URL, interaction data
> ### Note:
> - Video playback requires setting Referer=https://weibo.com/
>
> # [示例/Example]
> query = "yu7"
> mode = "hot"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search keyword | None | yu7 | None |
| mode | query | string | No | 搜索模式：hot=热门 / all=全部 | hot | hot | None |
| page | query | integer | No | 页码/Page number | 1 | 1 | None |

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

<a id="get-api-u1-v1-weibo-web-v2-search-user-posts"></a>
### `GET /api/u1/v1/weibo/web_v2/search_user_posts`

- Summary: 搜索用户微博/Search user posts
- Capabilities: search / profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_user_posts_api_v1_weibo_web_v2_search_user_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 在指定用户的微博中搜索包含特定关键词的内容。
> ### 参数:
> - uid: 用户ID（必填）
> - q: 搜索关键词（必填）
> - page: 页码，从1开始（默认1）
> - starttime: 开始时间戳（可选，Unix时间戳格式）
> - endtime: 结束时间戳（可选，Unix时间戳格式）
> - hasori: 是否包含原创（默认1包含）
> - hasret: 是否包含转发（默认1包含）
> - hastext: 是否包含文字（默认1包含）
> - haspic: 是否包含图片（默认1包含）
> - hasvideo: 是否包含视频（默认1包含）
> - hasmusic: 是否包含音乐（默认1包含）
> ### 返回:
> - 搜索结果列表，包含微博内容、作者信息、互动数据等
> ### 注意:
> - 搜索结果受用户隐私设置影响
> - 时间戳参数使用Unix时间戳格式
>
> # [English]
> ### Purpose:
> - Search for content containing specific keywords in a specified user's posts.
> ### Parameters:
> - uid: User ID (required)
> - q: Search keyword (required)
> - page: Page number, starts from 1 (default 1)
> - starttime: Start timestamp (optional, Unix timestamp format)
> - endtime: End timestamp (optional, Unix timestamp format)
> - hasori: Include original posts (default 1 include)
> - hasret: Include retweets (default 1 include)
> - hastext: Include text posts (default 1 include)
> - haspic: Include image posts (default 1 include)
> - hasvideo: Include video posts (default 1 include)
> - hasmusic: Include music posts (default 1 include)
> ### Return:
> - Search result list, including post content, author info, interaction data
> ### Note:
> - Search results affected by user privacy settings
> - Timestamp parameters use Unix timestamp format
>
> # [示例/Example]
> uid = "7277477906"
> q = "python"
> page = 1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户ID/User ID | None | 7277477906 | None |
| q | query | string | Yes | 搜索关键词/Search keyword | None | python | None |
| page | query | integer | No | 页数/Page number | 1 | 1 | None |
| starttime | query | integer | Yes | 开始时间戳/Start timestamp | None | None | None |
| endtime | query | integer | Yes | 结束时间戳/End timestamp | None | None | None |
| hasori | query | integer | No | 是否包含原创微博，1=包含，0=不包含/Include original posts, 1=include, 0=exclude | 1 | 1 | None |
| hasret | query | integer | No | 是否包含转发微博，1=包含，0=不包含/Include retweets, 1=include, 0=exclude | 1 | 1 | None |
| hastext | query | integer | No | 是否包含文字微博，1=包含，0=不包含/Include text posts, 1=include, 0=exclude | 1 | 1 | None |
| haspic | query | integer | No | 是否包含图片微博，1=包含，0=不包含/Include image posts, 1=include, 0=exclude | 1 | 1 | None |
| hasvideo | query | integer | No | 是否包含视频微博，1=包含，0=不包含/Include video posts, 1=include, 0=exclude | 1 | 1 | None |
| hasmusic | query | integer | No | 是否包含音乐微博，1=包含，0=不包含/Include music posts, 1=include, 0=exclude | 1 | 1 | None |

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
