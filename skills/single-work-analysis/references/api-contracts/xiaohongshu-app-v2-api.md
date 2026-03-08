# Xiaohongshu-App-V2-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/xiaohongshu-app-v2-api.md`](../api-tags/xiaohongshu-app-v2-api.md)
- Current contract file: `api-contracts/xiaohongshu-app-v2-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `21`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(小红书App V2数据接口/Xiaohongshu-App-V2-API data endpoints)** ⭐ 推荐优先使用/Recommended first choice - 稳定性最高、功能最全/Most stable and feature-rich

## Route Contracts

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-creator-hot-inspiration-feed"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed`

- Summary: 获取创作者热点灵感列表/Get creator hot inspiration feed
- Capabilities: trends / rankings / creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creator_hot_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_hot_inspiration_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者中心的热点创作灵感流，使用游标分页
> ### 参数:
> - cursor: 分页游标，首次请求留空，翻页时传入上一次响应中返回的 cursor 值（如 "1", "2"...）
> ### 返回:
> - 热点灵感列表数据
> ### 翻页说明:
> - 首次请求：cursor 留空
> - 翻页请求：传入上一次响应中返回的 cursor 值
>
> # [English]
> ### Purpose:
> - Get creator center hot inspiration feed, using cursor pagination
> ### Parameters:
> - cursor: Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "1", "2"...)
> ### Return:
> - Hot inspiration feed data
> ### Pagination Guide:
> - First request: leave cursor empty
> - Next page: pass cursor value from previous response
>
> # [示例/Example]
> cursor=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-creator-inspiration-feed"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_creator_inspiration_feed`

- Summary: 获取创作者推荐灵感列表/Get creator inspiration feed
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_creator_inspiration_feed_api_v1_xiaohongshu_app_v2_get_creator_inspiration_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者中心的推荐创作灵感流，使用游标分页
> ### 参数:
> - cursor: 分页游标，首次请求留空，翻页时传入上一次响应中返回的 cursor 值（如 "r_1", "r_2"...）
> - tab: 标签类型，默认 0
> - source: 来源，默认 "creator_center"
> ### 返回:
> - 推荐灵感列表数据
> ### 翻页说明:
> - 首次请求：cursor 留空
> - 翻页请求：传入上一次响应中返回的 cursor 值
>
> # [English]
> ### Purpose:
> - Get creator center recommended inspiration feed, using cursor pagination
> ### Parameters:
> - cursor: Pagination cursor, leave empty for first request, pass cursor value from previous response (e.g. "r_1", "r_2"...)
> - tab: Tab type, default 0
> - source: Source, default "creator_center"
> ### Return:
> - Recommended inspiration feed data
> ### Pagination Guide:
> - First request: leave cursor empty
> - Next page: pass cursor value from previous response
>
> # [示例/Example]
> cursor=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request | None | None | None |
| tab | query | integer | No | 标签类型/Tab type | 0 | 0 | None |
| source | query | string | No | 来源/Source | creator_center | creator_center | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-image-note-detail"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_image_note_detail`

- Summary: 获取图文笔记详情/Get image note detail
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_image_note_detail_api_v1_xiaohongshu_app_v2_get_image_note_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取图文笔记的完整详情数据
> ### 接口优先级:
> - ⭐ 小红书接口推荐优先级: `App V2（本接口）` > `App` > `Web V2` > `Web`
> ### 参数:
> - note_id: 笔记ID，如 "697c0eee000000000a03c308"
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 图文笔记详情数据，包含笔记内容、图片列表、作者信息、互动数据等
>
> # [English]
> ### Purpose:
> - Get full detail data of an image note
> ### API Priority:
> - ⭐ Xiaohongshu API priority: `App V2 (this)` > `App` > `Web V2` > `Web`
> ### Parameters:
> - note_id: Note ID, e.g. "697c0eee000000000a03c308"
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Image note detail data, including note content, image list, author info, interaction data, etc.
>
> # [示例/Example]
> note_id="697c0eee000000000a03c308"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 697c0eee000000000a03c308 | None |
| share_text | query | string | No | 分享链接/Share link | None | http://xhslink.com/o/8GqargIxrko | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-mixed-note-detail"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_mixed_note_detail`

- Summary: 获取首页推荐流笔记详情/Get mixed note detail from feed
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_mixed_note_detail_api_v1_xiaohongshu_app_v2_get_mixed_note_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 从首页推荐流中获取指定笔记的详情
> - 返回的数据结构与图文/视频接口不同，包含推荐流上下文信息
> ### 参数:
> - note_id: 笔记ID（可选），如 "697c0eee000000000a03c308"，为空则返回首页推荐流数据
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 推荐流笔记详情数据，包含推荐流上下文信息
>
> # [English]
> ### Purpose:
> - Get note detail from homepage feed
> - The returned data structure differs from image/video endpoints, including feed context info
> ### Parameters:
> - note_id: Note ID (optional), e.g. "697c0eee000000000a03c308", returns homepage feed data if empty
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Feed note detail data, including feed context info
>
> # [示例/Example]
> note_id="697c0eee000000000a03c308"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 697c0eee000000000a03c308 | None |
| share_text | query | string | No | 分享链接/Share link | None | http://xhslink.com/o/8GqargIxrko | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-note-comments"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_comments`

- Summary: 获取笔记评论列表/Get note comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_comments_api_v1_xiaohongshu_app_v2_get_note_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定笔记的评论列表，支持分页和多种排序方式
> ### 参数:
> - note_id: 笔记ID，如 "697c0eee000000000a03c308"
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> - cursor: 分页游标，首次请求留空，翻页时传入上一次响应中返回的 cursor 值
> - index: 评论索引，首次请求传 0，翻页时传入上一次响应中返回的 index 值
> - sort_strategy: 排序策略
>     - "default": 默认排序（推荐）
>     - "latest_v2": 按时间倒序（最新）
>     - "like_count": 按点赞数排序（最热）
> ### 返回:
> - 评论数据对象，包含评论列表、分页游标等
> ### 翻页说明:
> - 首次请求：cursor留空，index传0
> - 翻页请求：传入上一次响应中返回的 cursor 和 index 值
>
> # [English]
> ### Purpose:
> - Get comment list for a specified note, supports pagination and multiple sort strategies
> ### Parameters:
> - note_id: Note ID, e.g. "697c0eee000000000a03c308"
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> - cursor: Pagination cursor, leave empty for first request, pass cursor value from previous response for next page
> - index: Comment index, pass 0 for first request, pass index value from previous response for next page
> - sort_strategy: Sort strategy
>     - "default": Default sort (recommended)
>     - "latest_v2": Sort by time descending (latest)
>     - "like_count": Sort by like count (most popular)
> ### Return:
> - Comments data object, including comment list, pagination cursor, etc.
> ### Pagination Guide:
> - First request: leave cursor empty, pass index as 0
> - Next page: pass cursor and index values from previous response
>
> # [示例/Example]
> note_id="697c0eee000000000a03c308"
> sort_strategy="default"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 697c0eee000000000a03c308 | None |
| share_text | query | string | No | 分享链接/Share link | None | http://xhslink.com/o/8GqargIxrko | None |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request | None | None | None |
| index | query | integer | No | 评论索引，首次请求传0/Comment index, pass 0 for first request | 0 | 0 | None |
| sort_strategy | query | string | No | 排序策略/Sort strategy: default, latest_v2, like_count | default | default | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-note-sub-comments"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_note_sub_comments`

- Summary: 获取笔记二级评论列表/Get note sub comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_note_sub_comments_api_v1_xiaohongshu_app_v2_get_note_sub_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定笔记某条评论下的子评论（回复）列表，使用游标分页
> ### 参数:
> - note_id: 笔记ID，如 "699916e6000000001d0253da"
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> - comment_id: 父评论ID（必需），如 "699fb9930000000008030db6"
> - cursor: 分页游标，首次请求留空，翻页时从上一次响应的 `$.data.data.cursor` 中提取 `cursor` 字段的值
> - index: 分页索引，首次请求传 1，翻页时从上一次响应的 `$.data.data.cursor` 中提取 `index` 字段的值
> ### 返回:
> - 子评论数据对象，包含子评论列表、分页游标等
> ### 翻页说明:
> - 响应中的 `$.data.data.cursor` 是一个 JSON 对象，示例: `{"cursor":"69a0c134000000000c00910d","index":3}`
> - 首次请求：cursor留空，index传1
> - 翻页请求：从 `$.data.data.cursor` 中提取 `cursor` 和 `index` 分别传入对应参数
>
> # [English]
> ### Purpose:
> - Get sub-comment (reply) list under a specific comment of a note, using cursor pagination
> ### Parameters:
> - note_id: Note ID, e.g. "699916e6000000001d0253da"
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> - comment_id: Parent comment ID (required), e.g. "699fb9930000000008030db6"
> - cursor: Pagination cursor, leave empty for first request, extract `cursor` value from `$.data.cursor` of previous response for next page
> - index: Pagination index, pass 1 for first request, extract `index` value from `$.data.cursor` of previous response for next page
> ### Return:
> - Sub-comments data object, including sub-comment list, pagination cursor, etc.
> ### Pagination Guide:
> - The `$.data.data.cursor` in response is a JSON object, e.g. `{"cursor":"69a0c134000000000c00910d","index":3}`
> - First request: leave cursor empty, pass index as 1
> - Next page: extract `cursor` and `index` from `$.data.data.cursor` and pass them as corresponding parameters
>
> # [示例/Example]
> note_id="699916e6000000001d0253da"
> comment_id="699fb9930000000008030db6"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 699916e6000000001d0253da | None |
| share_text | query | string | No | 分享链接/Share link | None | http://xhslink.com/o/8GqargIxrko | None |
| comment_id | query | string | Yes | 父评论ID/Parent comment ID | None | 699fb9930000000008030db6 | None |
| cursor | query | string | No | 分页游标，首次留空，翻页时从$.data.data.cursor中提取cursor值/Pagination cursor, leave empty for first request, extract cursor from $.data.cursor for next page | None | None | None |
| index | query | integer | No | 分页索引，首次传1，翻页时从$.data.data.cursor中提取index值/Pagination index, pass 1 for first request, extract index from $.data.cursor for next page | 1 | 1 | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-product-detail"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_detail`

- Summary: 获取商品详情/Get product detail
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_detail_api_v1_xiaohongshu_app_v2_get_product_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过 SKU ID 获取商品的详细信息，包括价格、规格、库存、商品描述等
> ### 参数:
> - sku_id: 商品 SKU ID（必需），如 "669ddd44e05f3700011067ed"
> - source: 来源，默认 "mall_search"
> - pre_page: 前置页面，默认 "mall_search"
> ### 返回:
> - 商品详情数据，包含价格、规格、库存、商品描述等
>
> # [English]
> ### Purpose:
> - Get product detail by SKU ID, including price, specifications, stock, description, etc.
> ### Parameters:
> - sku_id: Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"
> - source: Source, default "mall_search"
> - pre_page: Previous page, default "mall_search"
> ### Return:
> - Product detail data, including price, specifications, stock, description, etc.
>
> # [示例/Example]
> sku_id="669ddd44e05f3700011067ed"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID | None | 669ddd44e05f3700011067ed | None |
| source | query | string | No | 来源/Source | mall_search | mall_search | None |
| pre_page | query | string | No | 前置页面/Previous page | mall_search | mall_search | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-product-recommendations"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_recommendations`

- Summary: 获取商品推荐列表/Get product recommendations
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_recommendations_api_v1_xiaohongshu_app_v2_get_product_recommendations_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据商品 SKU ID 获取相关推荐商品列表，使用游标分页
> ### 参数:
> - sku_id: 商品 SKU ID（必需），如 "669ddd44e05f3700011067ed"
> - cursor_score: 分页游标，首次请求留空，翻页时传入上一次响应中返回的 cursor_score 值
> - region: 地区，默认 "US"
> ### 返回:
> - 推荐商品列表数据
> ### 翻页说明:
> - 首次请求：cursor_score 留空
> - 翻页请求：传入上一次响应中返回的 cursor_score 值
>
> # [English]
> ### Purpose:
> - Get recommended products list by SKU ID, using cursor pagination
> ### Parameters:
> - sku_id: Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"
> - cursor_score: Pagination cursor, leave empty for first request, pass cursor_score value from previous response for next page
> - region: Region, default "US"
> ### Return:
> - Recommended products list data
> ### Pagination Guide:
> - First request: leave cursor_score empty
> - Next page: pass cursor_score value from previous response
>
> # [示例/Example]
> sku_id="669ddd44e05f3700011067ed"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID | None | 669ddd44e05f3700011067ed | None |
| cursor_score | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request | None | None | None |
| region | query | string | No | 地区/Region | US | US | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-product-review-overview"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_review_overview`

- Summary: 获取商品评论总览/Get product review overview
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_review_overview_api_v1_xiaohongshu_app_v2_get_product_review_overview_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品的评论统计信息，包括评分分布、好评率、评论标签等
> ### 参数:
> - sku_id: 商品 SKU ID（必需），如 "669ddd44e05f3700011067ed"
> - tab: 标签类型，默认 2
> ### 返回:
> - 商品评论总览数据，包含评分分布、好评率、评论标签等
>
> # [English]
> ### Purpose:
> - Get product review statistics, including rating distribution, positive rate, review tags, etc.
> ### Parameters:
> - sku_id: Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"
> - tab: Tab type, default 2
> ### Return:
> - Product review overview data, including rating distribution, positive rate, review tags, etc.
>
> # [示例/Example]
> sku_id="669ddd44e05f3700011067ed"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID | None | 669ddd44e05f3700011067ed | None |
| tab | query | integer | No | 标签类型/Tab type | 2 | 2 | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-product-reviews"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_product_reviews`

- Summary: 获取商品评论列表/Get product reviews
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_product_reviews_api_v1_xiaohongshu_app_v2_get_product_reviews_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品的用户评论列表，支持分页、排序和筛选有图评论
> ### 参数:
> - sku_id: 商品 SKU ID（必需），如 "669ddd44e05f3700011067ed"
> - page: 页码，从 0 开始
> - sort_strategy_type: 排序策略
>     - 0: 综合排序（默认）
>     - 1: 最新排序
> - share_pics_only: 仅看有图评论，0=否, 1=是
> - from_page: 来源页面，默认 "score_page"
> ### 返回:
> - 商品评论列表数据
> ### 翻页说明:
> - page 从 0 开始递增
>
> # [English]
> ### Purpose:
> - Get product user reviews list, supports pagination, sorting, and filtering reviews with images
> ### Parameters:
> - sku_id: Product SKU ID (required), e.g. "669ddd44e05f3700011067ed"
> - page: Page number, start from 0
> - sort_strategy_type: Sort strategy
>     - 0: General sort (default)
>     - 1: Latest sort
> - share_pics_only: Show reviews with images only, 0=no, 1=yes
> - from_page: From page, default "score_page"
> ### Return:
> - Product reviews list data
> ### Pagination Guide:
> - page starts from 0 and increments
>
> # [示例/Example]
> sku_id="669ddd44e05f3700011067ed"
> page=0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sku_id | query | string | Yes | 商品SKU ID/Product SKU ID | None | 669ddd44e05f3700011067ed | None |
| page | query | integer | No | 页码，从0开始/Page number, start from 0 | 0 | 0 | None |
| sort_strategy_type | query | integer | No | 排序策略：0=综合排序, 1=最新排序/Sort strategy: 0=general, 1=latest | 0 | 0 | None |
| share_pics_only | query | integer | No | 仅看有图评论：0=否, 1=是/Show reviews with images only: 0=no, 1=yes | 0 | 0 | None |
| from_page | query | string | No | 来源页面/From page | score_page | score_page | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-topic-feed"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_feed`

- Summary: 获取话题笔记列表/Get topic feed
- Capabilities: topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_topic_feed_api_v1_xiaohongshu_app_v2_get_topic_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定话题下的笔记列表，支持按最热或最新排序，使用游标分页
> ### 参数:
> - page_id: 话题页面ID（必需），如 "5c1cc866febed9000184b7c1"
> - sort: 排序方式
>     - "trend": 最热（默认）
>     - "time": 最新
> - cursor_score: 分页游标分数，翻页时传入上一页最后一个 item 的 cursor_score
> - last_note_id: 上一页最后一条笔记ID，翻页时传入
> - last_note_ct: 上一页最后一条笔记创建时间，翻页时传入
> - session_id: 会话ID，翻页时保持一致
> - first_load_time: 首次加载时间戳，翻页时保持一致
> - source: 来源，默认 "normal"
> ### 返回:
> - 话题笔记列表数据
> ### 翻页说明:
> - 首次请求：只传 page_id 和 sort，其余留空
> - 翻页请求：取上一次响应最后一个 item 的字段:
>     - cursor_score ← items[-1].cursor_score
>     - last_note_id ← items[-1].id
>     - last_note_ct ← items[-1].create_time
> - 建议同时回传 session_id 和 first_load_time 保持会话一致
>
> # [English]
> ### Purpose:
> - Get notes list under a specified topic, supports sorting by trending or latest, using cursor pagination
> ### Parameters:
> - page_id: Topic page ID (required), e.g. "5c1cc866febed9000184b7c1"
> - sort: Sort type
>     - "trend": Trending (default)
>     - "time": Latest
> - cursor_score: Pagination cursor score, pass last item's cursor_score from previous response
> - last_note_id: Last note ID from previous page
> - last_note_ct: Last note create time from previous page
> - session_id: Session ID, keep consistent for pagination
> - first_load_time: First load timestamp, keep consistent for pagination
> - source: Source, default "normal"
> ### Return:
> - Topic notes list data
> ### Pagination Guide:
> - First request: only pass page_id and sort, leave others empty
> - Next page: pass fields from last item of previous response:
>     - cursor_score ← items[-1].cursor_score
>     - last_note_id ← items[-1].id
>     - last_note_ct ← items[-1].create_time
> - Recommended to also pass session_id and first_load_time for session consistency
>
> # [示例/Example]
> page_id="5c1cc866febed9000184b7c1"
> sort="trend"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page_id | query | string | Yes | 话题页面ID/Topic page ID | None | 5c1cc866febed9000184b7c1 | None |
| sort | query | string | No | 排序方式/Sort: trend(最热), time(最新) | trend | trend | None |
| cursor_score | query | string | No | 分页游标分数，翻页时传入/Pagination cursor score for next page | None | None | None |
| last_note_id | query | string | No | 上一页最后一条笔记ID，翻页时传入/Last note ID from previous page | None | None | None |
| last_note_ct | query | string | No | 上一页最后一条笔记创建时间，翻页时传入/Last note create time from previous page | None | None | None |
| session_id | query | string | No | 会话ID，翻页时保持一致/Session ID, keep consistent for pagination | None | None | None |
| first_load_time | query | string | No | 首次加载时间戳，翻页时保持一致/First load timestamp, keep consistent for pagination | None | None | None |
| source | query | string | No | 来源/Source | normal | normal | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-topic-info"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_topic_info`

- Summary: 获取话题详情/Get topic info
- Capabilities: topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_topic_info_api_v1_xiaohongshu_app_v2_get_topic_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定话题的详细信息，包括话题名称、浏览量、讨论数、分享信息等
> ### 参数:
> - page_id: 话题页面ID（必需），如 "5c1cc866febed9000184b7c1"
> - source: 来源，默认 "normal"
> - note_id: 来源笔记ID，从笔记跳转到话题时传入（可选）
> ### 返回:
> - 话题详情数据，包含 page_info（名称/浏览量/讨论数）、tabs、share_info 等
>
> # [English]
> ### Purpose:
> - Get topic detail info, including topic name, view count, discussion count, share info, etc.
> ### Parameters:
> - page_id: Topic page ID (required), e.g. "5c1cc866febed9000184b7c1"
> - source: Source, default "normal"
> - note_id: Source note ID, pass when jumping from note to topic (optional)
> ### Return:
> - Topic detail data, including page_info (name/view count/discussion count), tabs, share_info, etc.
>
> # [示例/Example]
> page_id="5c1cc866febed9000184b7c1"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page_id | query | string | Yes | 话题页面ID/Topic page ID | None | 5c1cc866febed9000184b7c1 | None |
| source | query | string | No | 来源/Source | normal | normal | None |
| note_id | query | string | No | 来源笔记ID，从笔记跳转到话题时传入/Source note ID, pass when jumping from note to topic | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-user-faved-notes"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_faved_notes`

- Summary: 获取用户收藏笔记列表/Get user faved notes
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_faved_notes_api_v1_xiaohongshu_app_v2_get_user_faved_notes_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户公开收藏的笔记列表，使用游标分页
> ### 参数:
> - user_id: 用户ID，如 "5a8cf39111be10466d285d6b"
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`user_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`user_id`为准。
> - cursor: 分页游标，首次请求留空，翻页时传入上一页列表中最后一条笔记的 note_id
> ### 返回:
> - 用户收藏笔记列表数据，包含笔记基本信息和分页信息
> ### 翻页说明:
> - 首次请求：cursor留空
> - 翻页请求：传入上一页列表中最后一条笔记的 note_id
>
> # [English]
> ### Purpose:
> - Get list of notes faved by a specified user, using cursor pagination
> ### Parameters:
> - user_id: User ID, e.g. "5a8cf39111be10466d285d6b"
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `user_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `user_id` shall prevail.
> - cursor: Pagination cursor, leave empty for first request, pass last note_id from previous page for next page
> ### Return:
> - User faved notes list data, including basic note info and pagination info
> ### Pagination Guide:
> - First request: leave cursor empty
> - Next page: pass last note_id from previous page
>
> # [示例/Example]
> user_id="5a8cf39111be10466d285d6b"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 5a8cf39111be10466d285d6b | None |
| share_text | query | string | No | 分享链接/Share link | None | https://xhslink.com/a/EZ4M9TwMA6c3 | None |
| cursor | query | string | No | 分页游标，首次请求留空，翻页时传入上一页最后一条笔记的note_id/Pagination cursor, leave empty for first request, pass last note_id from previous page for next page | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-user-info"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_info`

- Summary: 获取用户信息/Get user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_info_api_v1_xiaohongshu_app_v2_get_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的详细信息
> ### 参数:
> - user_id: 用户ID，如 "61b46d790000000010008153"
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`user_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`user_id`为准。
> ### 返回:
> - 用户详细信息，包含昵称、头像、简介、粉丝数、关注数、笔记数等
>
> # [English]
> ### Purpose:
> - Get detailed info of a specified user
> ### Parameters:
> - user_id: User ID, e.g. "61b46d790000000010008153"
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `user_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `user_id` shall prevail.
> ### Return:
> - User detailed info, including nickname, avatar, bio, follower count, following count, note count, etc.
>
> # [示例/Example]
> user_id="61b46d790000000010008153"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 61b46d790000000010008153 | None |
| share_text | query | string | No | 分享链接/Share link | None | https://xhslink.com/m/3ZSCJZAMz0a | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-user-posted-notes"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_user_posted_notes`

- Summary: 获取用户笔记列表/Get user posted notes
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_posted_notes_api_v1_xiaohongshu_app_v2_get_user_posted_notes_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户已发布的笔记列表，使用游标分页
> ### 参数:
> - user_id: 用户ID，如 "61b46d790000000010008153"
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`user_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`user_id`为准。
> - cursor: 分页游标，首次请求留空，翻页时传入上一次响应中返回的 cursor 值
>     - 通常cursor取值方式为notes列表的最后一条笔记的 note_id
>     - JSON路径示例: `$.data.data.notes[-1].cursor`
> ### 返回:
> - 用户笔记列表数据，包含笔记基本信息和分页信息
> ### 翻页说明:
> - 首次请求：cursor留空
> - 翻页请求：传入上一次响应中返回的 cursor 值
>
> # [English]
> ### Purpose:
> - Get list of notes posted by a specified user, using cursor pagination
> ### Parameters:
> - user_id: User ID, e.g. "61b46d790000000010008153"
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `user_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `user_id` shall prevail.
> - cursor: Pagination cursor, leave empty for first request, pass cursor value from previous response for next page
>     - The cursor is usually the note_id of the last note in the notes list
>     - JSON path example: `$.data.data.notes[-1].cursor`
> ### Return:
> - User posted notes list data, including basic note info and pagination info
> ### Pagination Guide:
> - First request: leave cursor empty
> - Next page: pass cursor value from previous response
>
> # [示例/Example]
> user_id="61b46d790000000010008153"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID | None | 61b46d790000000010008153 | None |
| share_text | query | string | No | 分享链接/Share link | None | http://xhslink.com/o/8GqargIxrko | None |
| cursor | query | string | No | 分页游标，首次请求留空/Pagination cursor, leave empty for first request | None | None | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-get-video-note-detail"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/get_video_note_detail`

- Summary: 获取视频笔记详情/Get video note detail
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_video_note_detail_api_v1_xiaohongshu_app_v2_get_video_note_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取视频笔记的完整详情数据
> ### 参数:
> - note_id: 笔记ID，如 "697c0eee000000000a03c308"
> - share_text: 小红书分享链接（支持APP和Web端分享链接）
> - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
> ### 返回:
> - 视频笔记详情数据，包含视频播放地址、封面图、作者信息、互动数据等
>
> # [English]
> ### Purpose:
> - Get full detail data of a video note
> ### Parameters:
> - note_id: Note ID, e.g. "697c0eee000000000a03c308"
> - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
> - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both are carried, `note_id` shall prevail.
> ### Return:
> - Video note detail data, including video play URL, cover image, author info, interaction data, etc.
>
> # [示例/Example]
> note_id="697c0eee000000000a03c308"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| note_id | query | string | No | 笔记ID/Note ID | None | 697c0eee000000000a03c308 | None |
| share_text | query | string | No | 分享链接/Share link | None | http://xhslink.com/o/8GqargIxrko | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-search-groups"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/search_groups`

- Summary: 搜索群聊/Search groups
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_groups_api_v1_xiaohongshu_app_v2_search_groups_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索小红书群聊列表，支持分页
> ### 参数:
> - keyword: 搜索关键词（必需），如 "上海"
> - page_no: 页码，从 0 开始
> - search_id: 搜索ID，翻页时传入首次搜索返回的值
> - source: 来源，默认 "unifiedSearchGroup"
> - is_recommend: 是否推荐，0=否, 1=是
> ### 返回:
> - 搜索结果数据，包含群聊列表和分页信息
> ### 翻页说明:
> - 首次请求：search_id 留空（自动生成），page_no 传 0
> - 翻页请求：传入首次搜索返回的 search_id，page_no 递增
>
> # [English]
> ### Purpose:
> - Search Xiaohongshu groups by keyword, supports pagination
> ### Parameters:
> - keyword: Search keyword (required), e.g. "上海"
> - page_no: Page number, start from 0
> - search_id: Search ID, pass value from first search response for pagination
> - source: Source, default "unifiedSearchGroup"
> - is_recommend: Is recommend, 0=no, 1=yes
> ### Return:
> - Search result data, including group list and pagination info
> ### Pagination Guide:
> - First request: leave search_id empty (auto-generated), page_no pass 0
> - Next page: pass search_id from first search response, increment page_no
>
> # [示例/Example]
> keyword="上海"
> page_no=0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | 上海 | None |
| page_no | query | integer | No | 页码，从0开始/Page number, start from 0 | 0 | 0 | None |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination | None | None | None |
| source | query | string | No | 来源/Source | unifiedSearchGroup | unifiedSearchGroup | None |
| is_recommend | query | integer | No | 是否推荐：0=否, 1=是/Is recommend: 0=no, 1=yes | 0 | 0 | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-search-images"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/search_images`

- Summary: 搜索图片/Search images
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_images_api_v1_xiaohongshu_app_v2_search_images_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索小红书图片，每页返回 20 条结果，支持分页
> ### 参数:
> - keyword: 搜索关键词（必需），如 "壁纸"
> - page: 页码，从 1 开始
> - search_id: 搜索ID，翻页时传入首次搜索返回的值
> - search_session_id: 搜索会话ID，翻页时传入首次搜索返回的值
> - word_request_id: 词请求ID，翻页时传入首次搜索返回的值
> - source: 来源，默认 "explore_feed"
> ### 返回:
> - 搜索结果数据，包含图片列表和分页信息
> ### 翻页说明:
> - 首次请求：只传keyword和page
> - 翻页请求：传入首次搜索返回的 search_id、search_session_id 和 word_request_id
>
> # [English]
> ### Purpose:
> - Search Xiaohongshu images by keyword, returns 20 results per page, supports pagination
> ### Parameters:
> - keyword: Search keyword (required), e.g. "壁纸"
> - page: Page number, start from 1
> - search_id: Search ID, pass value from first search response for pagination
> - search_session_id: Search session ID, pass value from first search response for pagination
> - word_request_id: Word request ID, pass value from first search response for pagination
> - source: Source, default "explore_feed"
> ### Return:
> - Search result data, including image list and pagination info
> ### Pagination Guide:
> - First request: only pass keyword and page
> - Next page: pass search_id, search_session_id, and word_request_id from first search response
>
> # [示例/Example]
> keyword="壁纸"
> page=1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | 壁纸 | None |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 | 1 | 1 | None |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination | None | None | None |
| search_session_id | query | string | No | 搜索会话ID，翻页时传入首次搜索返回的值/Search session ID for pagination | None | None | None |
| word_request_id | query | string | No | 词请求ID，翻页时传入首次搜索返回的值/Word request ID for pagination | None | None | None |
| source | query | string | No | 来源/Source | explore_feed | explore_feed | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-search-notes"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/search_notes`

- Summary: 搜索笔记/Search notes
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_notes_api_v1_xiaohongshu_app_v2_search_notes_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索小红书笔记，支持多种排序方式、笔记类型筛选和发布时间筛选
> ### 参数:
> - keyword: 搜索关键词（必需），如 "美食推荐"
> - page: 页码，从 1 开始
> - sort_type: 排序方式
>     - "general": 综合排序（默认）
>     - "time_descending": 按时间倒序（最新）
>     - "popularity_descending": 按点赞数排序（最多点赞）
>     - "comment_descending": 按评论数排序（最多评论）
>     - "collect_descending": 按收藏数排序（最多收藏）
>     - "english_preferred": 英文优先
> - note_type: 笔记类型筛选
>     - "不限": 所有类型（默认）
>     - "视频笔记": 仅视频
>     - "普通笔记": 仅图文
>     - "直播笔记": 仅直播
> - time_filter: 发布时间筛选
>     - "不限": 所有时间（默认）
>     - "一天内": 24小时内
>     - "一周内": 7天内
>     - "半年内": 6个月内
> - search_id: 搜索ID，翻页时传入首次搜索返回的值
> - search_session_id: 搜索会话ID，翻页时传入首次搜索返回的值
> - source: 来源，默认 "explore_feed"
> - ai_mode: AI模式，0=关闭, 1=开启
> ### 返回:
> - 搜索结果数据，包含笔记列表和分页信息
> ### 翻页说明:
> - 首次请求：只传keyword和page
> - 翻页请求：传入首次搜索返回的 search_id 和 search_session_id
>
> # [English]
> ### Purpose:
> - Search Xiaohongshu notes by keyword, supports multiple sort types, note type filters, and time filters
> ### Parameters:
> - keyword: Search keyword (required), e.g. "美食推荐"
> - page: Page number, start from 1
> - sort_type: Sort type
>     - "general": General sort (default)
>     - "time_descending": Sort by time descending (latest)
>     - "popularity_descending": Sort by like count (most liked)
>     - "comment_descending": Sort by comment count (most commented)
>     - "collect_descending": Sort by collect count (most collected)
>     - "english_preferred": English preferred
> - note_type: Note type filter
>     - "不限": All types (default)
>     - "视频笔记": Video notes only
>     - "普通笔记": Image notes only
>     - "直播笔记": Live notes only
> - time_filter: Time filter
>     - "不限": All time (default)
>     - "一天内": Within 24 hours
>     - "一周内": Within 7 days
>     - "半年内": Within 6 months
> - search_id: Search ID, pass value from first search response for pagination
> - search_session_id: Search session ID, pass value from first search response for pagination
> - source: Source, default "explore_feed"
> - ai_mode: AI mode, 0=off, 1=on
> ### Return:
> - Search result data, including note list and pagination info
> ### Pagination Guide:
> - First request: only pass keyword and page
> - Next page: pass search_id and search_session_id from first search response
>
> # [示例/Example]
> keyword="美食推荐"
> page=1
> sort_type="general"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | 美食推荐 | None |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 | 1 | 1 | None |
| sort_type | query | string | No | 排序方式/Sort type | general | general | None |
| note_type | query | string | No | 笔记类型/Note type: 不限, 视频笔记, 普通笔记, 直播笔记 | 不限 | 不限 | None |
| time_filter | query | string | No | 发布时间筛选/Time filter: 不限, 一天内, 一周内, 半年内 | 不限 | 不限 | None |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination | None | None | None |
| search_session_id | query | string | No | 搜索会话ID，翻页时传入首次搜索返回的值/Search session ID for pagination | None | None | None |
| source | query | string | No | 来源/Source | explore_feed | explore_feed | None |
| ai_mode | query | integer | No | AI模式：0=关闭, 1=开启/AI mode: 0=off, 1=on | 0 | 0 | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-search-products"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/search_products`

- Summary: 搜索商品/Search products
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_products_api_v1_xiaohongshu_app_v2_search_products_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索小红书商品，每页返回 20 条结果，支持分页
> ### 参数:
> - keyword: 搜索关键词（必需），如 "手机壳"
> - page: 页码，从 1 开始
> - search_id: 搜索ID，翻页时传入首次搜索返回的值
> - source: 来源，默认 "explore_feed"
> ### 返回:
> - 搜索结果数据，包含商品列表和分页信息
> ### 翻页说明:
> - 首次请求：只传keyword和page
> - 翻页请求：传入首次搜索返回的 search_id
>
> # [English]
> ### Purpose:
> - Search Xiaohongshu products by keyword, returns 20 results per page, supports pagination
> ### Parameters:
> - keyword: Search keyword (required), e.g. "手机壳"
> - page: Page number, start from 1
> - search_id: Search ID, pass value from first search response for pagination
> - source: Source, default "explore_feed"
> ### Return:
> - Search result data, including product list and pagination info
> ### Pagination Guide:
> - First request: only pass keyword and page
> - Next page: pass search_id from first search response
>
> # [示例/Example]
> keyword="手机壳"
> page=1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | 手机壳 | None |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 | 1 | 1 | None |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination | None | None | None |
| source | query | string | No | 来源/Source | explore_feed | explore_feed | None |

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

<a id="get-api-u1-v1-xiaohongshu-app-v2-search-users"></a>
### `GET /api/u1/v1/xiaohongshu/app_v2/search_users`

- Summary: 搜索用户/Search users
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_users_api_v1_xiaohongshu_app_v2_search_users_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索小红书用户，每页返回 20 条结果，支持分页
> ### 参数:
> - keyword: 搜索关键词（必需），如 "美食博主"
> - page: 页码，从 1 开始
> - search_id: 搜索ID，翻页时传入首次搜索返回的值
> - source: 来源，默认 "explore_feed"
> ### 返回:
> - 搜索结果数据，包含用户列表和分页信息
> ### 翻页说明:
> - 首次请求：只传keyword和page
> - 翻页请求：传入首次搜索返回的 search_id
>
> # [English]
> ### Purpose:
> - Search Xiaohongshu users by keyword, returns 20 results per page, supports pagination
> ### Parameters:
> - keyword: Search keyword (required), e.g. "美食博主"
> - page: Page number, start from 1
> - search_id: Search ID, pass value from first search response for pagination
> - source: Source, default "explore_feed"
> ### Return:
> - Search result data, including user list and pagination info
> ### Pagination Guide:
> - First request: only pass keyword and page
> - Next page: pass search_id from first search response
>
> # [示例/Example]
> keyword="美食博主"
> page=1

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | 美食博主 | None |
| page | query | integer | No | 页码，从1开始/Page number, start from 1 | 1 | 1 | None |
| search_id | query | string | No | 搜索ID，翻页时传入首次搜索返回的值/Search ID for pagination | None | None | None |
| source | query | string | No | 来源/Source | explore_feed | explore_feed | None |

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
