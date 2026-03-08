# Instagram-V2-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/instagram-v2-api.md`](../api-tags/instagram-v2-api.md)
- Current contract file: `api-contracts/instagram-v2-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `27`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(Instagram V2数据接口（若V1接口的功能无法满足需求时使用，稳定性不如V1接口）/Instagram-V2-API endpoints (Use when V1 endpoints cannot meet the requirements, stability is not as good as V1 endpoints))**

## Route Contracts

<a id="get-api-u1-v1-instagram-v2-fetch-comment-replies"></a>
### `GET /api/u1/v1/instagram/v2/fetch_comment_replies`

- Summary: 获取评论回复/Get comment replies
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_comment_replies_api_v1_instagram_v2_fetch_comment_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取评论的回复列表
> - 需要先通过fetch_post_comments获取评论ID
> - 支持分页获取
> ### 参数:
> - code_or_url: 帖子Shortcode或完整URL
> - comment_id: 评论ID
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 回复列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get list of replies to a comment
> - Need to get comment ID from fetch_post_comments first
> - Support pagination
> ### Parameters:
> - code_or_url: Post shortcode or full URL
> - comment_id: Comment ID
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of replies
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> code_or_url = "DRhvwVLAHAG"
> comment_id = "18067775592012345"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code_or_url | query | string | Yes | 帖子Shortcode或URL/Post shortcode or URL | None | DRhvwVLAHAG | None |
| comment_id | query | string | Yes | 评论ID/Comment ID | None | 18067775592012345 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-hashtag-posts"></a>
### `GET /api/u1/v1/instagram/v2/fetch_hashtag_posts`

- Summary: 获取话题帖子/Get hashtag posts
- Capabilities: content details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_posts_api_v1_instagram_v2_fetch_hashtag_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定话题标签下的帖子列表
> - 支持按热门、最新或仅Reels筛选
> - 支持分页获取
> ### 参数:
> - keyword: 话题关键词（不含#号）
> - feed_type: 帖子类型，"top"（热门）、"recent"（最新）或"reels"（仅Reels），默认top
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 帖子列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts under specified hashtag
> - Support filtering by top, recent, or reels only
> - Support pagination
> ### Parameters:
> - keyword: Hashtag keyword (without #)
> - feed_type: Feed type "top", "recent", or "reels", default top
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of posts
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> keyword = "cat"
> feed_type = "top"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 话题关键词（不含#号）/Hashtag keyword (without #) | None | cat | None |
| feed_type | query | string | No | 帖子类型: top(热门), recent(最新), reels(仅Reels)/Feed type: top, recent, or reels | top | None | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-highlight-stories"></a>
### `GET /api/u1/v1/instagram/v2/fetch_highlight_stories`

- Summary: 获取精选故事详情/Get highlight stories
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_highlight_stories_api_v1_instagram_v2_fetch_highlight_stories_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定精选（Highlight）中的所有故事
> - 需要先通过fetch_user_highlights获取精选ID
> ### 参数:
> - highlight_id: 精选ID（可带或不带"highlight:"前缀）
> ### 返回:
> - `data.items`: 故事列表，包含图片/视频URL、发布时间等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get all stories in a specific highlight
> - Need to get highlight ID from fetch_user_highlights first
> ### Parameters:
> - highlight_id: Highlight ID (with or without "highlight:" prefix)
> ### Return:
> - `data.items`: List of stories with image/video URLs, publish time, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> highlight_id = "17895069621772257"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| highlight_id | query | string | Yes | 精选ID/Highlight ID | None | 17895069621772257 | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-location-posts"></a>
### `GET /api/u1/v1/instagram/v2/fetch_location_posts`

- Summary: 获取地点帖子/Get location posts
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_location_posts_api_v1_instagram_v2_fetch_location_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定地点的帖子列表
> - 地点ID可通过search_locations获取
> - 支持分页获取
> ### 参数:
> - location_id: 地点ID
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 帖子列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts at specified location
> - Location ID can be obtained from search_locations
> - Support pagination
> ### Parameters:
> - location_id: Location ID
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of posts
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> location_id = "331004901"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| location_id | query | string | Yes | 地点ID/Location ID | None | 331004901 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-music-posts"></a>
### `GET /api/u1/v1/instagram/v2/fetch_music_posts`

- Summary: 获取音乐帖子/Get music posts
- Capabilities: content details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_posts_api_v1_instagram_v2_fetch_music_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取使用指定音乐的帖子列表
> - 音频ID可从帖子详情中获取
> - 支持分页获取
> ### 参数:
> - audio_canonical_id: 音频ID
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 帖子列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts using specified music
> - Audio ID can be obtained from post details
> - Support pagination
> ### Parameters:
> - audio_canonical_id: Audio ID
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of posts
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> audio_canonical_id = "564058920086577"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| audio_canonical_id | query | string | Yes | 音频ID/Audio ID | None | 564058920086577 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-post-comments"></a>
### `GET /api/u1/v1/instagram/v2/fetch_post_comments`

- Summary: 获取帖子评论/Get post comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_api_v1_instagram_v2_fetch_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取帖子的评论列表
> - 支持按最新或热门排序
> - 支持分页获取
> ### 参数:
> - code_or_url: 帖子Shortcode或完整URL
> - sort_by: 排序方式，"recent"（最新）或"popular"（热门），默认recent
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 评论列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get list of comments on the post
> - Support sorting by recent or popular
> - Support pagination
> ### Parameters:
> - code_or_url: Post shortcode or full URL
> - sort_by: Sort by "recent" or "popular", default recent
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of comments
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> code_or_url = "DRhvwVLAHAG"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code_or_url | query | string | Yes | 帖子Shortcode或URL/Post shortcode or URL | None | DRhvwVLAHAG | None |
| sort_by | query | string | No | 排序方式: recent(最新) 或 popular(热门)/Sort by: recent or popular | recent | recent | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-post-info"></a>
### `GET /api/u1/v1/instagram/v2/fetch_post_info`

- Summary: 获取帖子详情/Get post info
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_info_api_v1_instagram_v2_fetch_post_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram帖子的详细信息
> - 支持Shortcode或完整URL
> ### 参数:
> - code_or_url: 帖子Shortcode或完整URL
> ### 返回:
> - `data`: 帖子详情，包含媒体资源、描述、点赞数、评论数等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get detailed information of Instagram post
> - Support shortcode or full URL
> ### Parameters:
> - code_or_url: Post shortcode or full URL
> ### Return:
> - `data`: Post details including media, caption, likes, comments, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> code_or_url = "DRhvwVLAHAG"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code_or_url | query | string | Yes | 帖子Shortcode或URL/Post shortcode or URL | None | DRhvwVLAHAG | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-post-likes"></a>
### `GET /api/u1/v1/instagram/v2/fetch_post_likes`

- Summary: 获取帖子点赞列表/Get post likes
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_likes_api_v1_instagram_v2_fetch_post_likes_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取帖子的点赞用户列表
> - 支持分页获取
> ### 参数:
> - code_or_url: 帖子Shortcode或完整URL
> - end_cursor: 分页游标，从上一次响应获取
> ### 返回:
> - `data.items`: 点赞用户列表
> - `end_cursor`: 下一页游标
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get list of users who liked the post
> - Support pagination
> ### Parameters:
> - code_or_url: Post shortcode or full URL
> - end_cursor: Pagination cursor from previous response
> ### Return:
> - `data.items`: List of users who liked
> - `end_cursor`: Next page cursor
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> code_or_url = "DRhvwVLAHAG"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code_or_url | query | string | Yes | 帖子Shortcode或URL/Post shortcode or URL | None | DRhvwVLAHAG | None |
| end_cursor | query | string | No | 分页游标/Pagination cursor | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-similar-users"></a>
### `GET /api/u1/v1/instagram/v2/fetch_similar_users`

- Summary: 获取相似用户/Get similar users
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_similar_users_api_v1_instagram_v2_fetch_similar_users_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取与指定用户相似的用户推荐列表
> - 基于Instagram的推荐算法
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> ### 返回:
> - `data.items`: 相似用户列表
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get recommended similar users
> - Based on Instagram's recommendation algorithm
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> ### Return:
> - `data.items`: List of similar users
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-followers"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_followers`

- Summary: 获取用户粉丝/Get user followers
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_followers_api_v1_instagram_v2_fetch_user_followers_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的粉丝列表
> - 支持分页获取
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 粉丝列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get list of followers of Instagram user
> - Support pagination
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of followers
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-following"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_following`

- Summary: 获取用户关注/Get user following
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_following_api_v1_instagram_v2_fetch_user_following_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户关注的用户列表
> - 支持分页获取
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 关注列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get list of users that Instagram user is following
> - Support pagination
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of following
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-highlights"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_highlights`

- Summary: 获取用户精选/Get user highlights
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_highlights_api_v1_instagram_v2_fetch_user_highlights_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的精选故事（Highlights）列表
> - 精选是用户保存的故事合集
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> ### 返回:
> - `data.items`: 精选列表，包含精选ID、标题、封面等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get Instagram user's highlights list
> - Highlights are saved story collections
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> ### Return:
> - `data.items`: List of highlights with ID, title, cover, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-info"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_info`

- Summary: 获取用户信息/Get user info
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_info_api_v1_instagram_v2_fetch_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户的详细信息
> - 支持通过用户名或用户ID查询
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> ### 返回:
> - `data`: 用户信息，包含用户名、头像、简介、粉丝数、关注数、帖子数等
> - 此接口会返回用户的关于信息，包括国家，加入时间，是否认证等信息。
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get detailed Instagram user information
> - Support query by username or user ID
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> ### Return:
> - `data`: User info including username, avatar, bio, followers, following, posts count, etc.
> - This endpoint returns user's about info including country, join date, verification status, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-posts"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_posts`

- Summary: 获取用户帖子/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_api_v1_instagram_v2_fetch_user_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户发布的帖子列表
> - 支持分页获取
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 帖子列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get list of posts published by Instagram user
> - Support pagination
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of posts
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-reels"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_reels`

- Summary: 获取用户Reels/Get user reels
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_reels_api_v1_instagram_v2_fetch_user_reels_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户发布的Reels短视频列表
> - 支持分页获取
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: Reels列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get list of Reels published by Instagram user
> - Support pagination
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of reels
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-stories"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_stories`

- Summary: 获取用户故事/Get user stories
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_stories_api_v1_instagram_v2_fetch_user_stories_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Instagram用户当前发布的故事（Stories）
> - 故事在24小时后过期
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> ### 返回:
> - `data.items`: 故事列表，包含图片/视频URL、发布时间等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get current stories published by Instagram user
> - Stories expire after 24 hours
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> ### Return:
> - `data.items`: List of stories with image/video URLs, publish time, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |

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

<a id="get-api-u1-v1-instagram-v2-fetch-user-tagged-posts"></a>
### `GET /api/u1/v1/instagram/v2/fetch_user_tagged_posts`

- Summary: 获取用户被标记的帖子/Get user tagged posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_tagged_posts_api_v1_instagram_v2_fetch_user_tagged_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取其他用户标记了该用户的帖子列表
> - 支持分页获取
> ### 参数:
> - username: 用户名（与user_id二选一）
> - user_id: 用户ID（与username二选一）
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 帖子列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get posts where the user is tagged by others
> - Support pagination
> ### Parameters:
> - username: Username (either username or user_id required)
> - user_id: User ID (either username or user_id required)
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of posts
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> username = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | No | 用户名/Username | None | instagram | None |
| user_id | query | string | No | 用户ID/User ID | None | 18527 | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-general-search"></a>
### `GET /api/u1/v1/instagram/v2/general_search`

- Summary: 综合搜索/General search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `general_search_api_v1_instagram_v2_general_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词进行Instagram综合搜索
> - 支持分页获取
> ### 参数:
> - keyword: 搜索关键词
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: 综合搜索结果列表，包含用户、帖子、Reels等
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Perform general search on Instagram by keyword
> - Support pagination
> ### Parameters:
> - keyword: Search keyword
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of general search results including users, posts, reels, etc.
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> keyword = "cat"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | cat | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-media-id-to-shortcode"></a>
### `GET /api/u1/v1/instagram/v2/media_id_to_shortcode`

- Summary: Media ID转Shortcode/Convert media ID to shortcode
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `media_id_to_shortcode_api_v1_instagram_v2_media_id_to_shortcode_get`

#### Notes

> # [中文]
> ### 用途:
> - 将Instagram帖子的Media ID转换为Shortcode
> - Shortcode可用于构建帖子URL：instagram.com/p/{shortcode}/
> ### 参数:
> - media_id: 帖子的Media ID
> ### 返回:
> - `status`: 转换状态
> - `media_id`: 原始Media ID
> - `shortcode`: 转换后的Shortcode
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Convert Instagram post media ID to shortcode
> - Shortcode can be used to construct post URL: instagram.com/p/{shortcode}/
> ### Parameters:
> - media_id: Post media ID
> ### Return:
> - `status`: Conversion status
> - `media_id`: Original media ID
> - `shortcode`: Converted shortcode
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> media_id = "3774507992167247878"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| media_id | query | string | Yes | 帖子Media ID/Post media ID | None | 3774507992167247878 | None |

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

<a id="get-api-u1-v1-instagram-v2-search-by-coordinates"></a>
### `GET /api/u1/v1/instagram/v2/search_by_coordinates`

- Summary: 根据坐标搜索地点/Search locations by coordinates
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_by_coordinates_api_v1_instagram_v2_search_by_coordinates_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据GPS坐标搜索附近的Instagram地点
> ### 参数:
> - latitude: 纬度
> - longitude: 经度
> ### 返回:
> - `data.items`: 附近地点列表，包含名称、地址、分类等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Search nearby Instagram locations by GPS coordinates
> ### Parameters:
> - latitude: Latitude
> - longitude: Longitude
> ### Return:
> - `data.items`: List of nearby locations with name, address, category, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> latitude = 40.7
> longitude = -74

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| latitude | query | number | Yes | 纬度/Latitude | None | 40.7 | None |
| longitude | query | number | Yes | 经度/Longitude | None | -74 | None |

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

<a id="get-api-u1-v1-instagram-v2-search-hashtags"></a>
### `GET /api/u1/v1/instagram/v2/search_hashtags`

- Summary: 搜索话题标签/Search hashtags
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_hashtags_api_v1_instagram_v2_search_hashtags_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索Instagram话题标签
> ### 参数:
> - keyword: 搜索关键词
> ### 返回:
> - `data.items`: 话题标签列表，包含名称、帖子数量等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Search Instagram hashtags by keyword
> ### Parameters:
> - keyword: Search keyword
> ### Return:
> - `data.items`: List of hashtags with name, post count, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> keyword = "cat"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | cat | None |

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

<a id="get-api-u1-v1-instagram-v2-search-locations"></a>
### `GET /api/u1/v1/instagram/v2/search_locations`

- Summary: 搜索地点/Search locations
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_locations_api_v1_instagram_v2_search_locations_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索Instagram地点
> ### 参数:
> - keyword: 搜索关键词（地点名称、城市等）
> ### 返回:
> - `data.items`: 地点列表，包含名称、地址、坐标等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Search Instagram locations by keyword
> ### Parameters:
> - keyword: Search keyword (location name, city, etc.)
> ### Return:
> - `data.items`: List of locations with name, address, coordinates, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> keyword = "paris"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | paris | None |

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

<a id="get-api-u1-v1-instagram-v2-search-music"></a>
### `GET /api/u1/v1/instagram/v2/search_music`

- Summary: 搜索音乐/Search music
- Capabilities: search / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_music_api_v1_instagram_v2_search_music_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索Instagram上可用的音乐
> ### 参数:
> - keyword: 搜索关键词
> ### 返回:
> - `data.items`: 音乐列表，包含标题、艺术家、时长、音频ID等
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Search available music on Instagram by keyword
> ### Parameters:
> - keyword: Search keyword
> ### Return:
> - `data.items`: List of music with title, artist, duration, audio ID, etc.
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> keyword = "happy"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | happy | None |

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

<a id="get-api-u1-v1-instagram-v2-search-reels"></a>
### `GET /api/u1/v1/instagram/v2/search_reels`

- Summary: 搜索Reels/Search reels
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_reels_api_v1_instagram_v2_search_reels_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索Instagram Reels短视频
> - 支持分页获取
> ### 参数:
> - keyword: 搜索关键词
> - pagination_token: 分页token，从上一次响应获取
> ### 返回:
> - `data.items`: Reels列表
> - `pagination_token`: 下一页token
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Search Instagram Reels by keyword
> - Support pagination
> ### Parameters:
> - keyword: Search keyword
> - pagination_token: Pagination token from previous response
> ### Return:
> - `data.items`: List of reels
> - `pagination_token`: Next page token
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> keyword = "cat"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | cat | None |
| pagination_token | query | string | No | 分页token/Pagination token | None | None | None |

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

<a id="get-api-u1-v1-instagram-v2-search-users"></a>
### `GET /api/u1/v1/instagram/v2/search_users`

- Summary: 搜索用户/Search users
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_users_api_v1_instagram_v2_search_users_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据关键词搜索Instagram用户
> ### 参数:
> - keyword: 搜索关键词
> ### 返回:
> - `data.items`: 用户列表
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Search Instagram users by keyword
> ### Parameters:
> - keyword: Search keyword
> ### Return:
> - `data.items`: List of users
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> keyword = "instagram"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | instagram | None |

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

<a id="get-api-u1-v1-instagram-v2-shortcode-to-media-id"></a>
### `GET /api/u1/v1/instagram/v2/shortcode_to_media_id`

- Summary: Shortcode转Media ID/Convert shortcode to media ID
- Capabilities: media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `shortcode_to_media_id_api_v1_instagram_v2_shortcode_to_media_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 将Instagram帖子的Shortcode转换为Media ID
> - Shortcode是帖子URL中的唯一标识，如 instagram.com/p/DRhvwVLAHAG/ 中的 DRhvwVLAHAG
> ### 参数:
> - shortcode: 帖子的Shortcode
> ### 返回:
> - `status`: 转换状态
> - `shortcode`: 原始Shortcode
> - `media_id`: 转换后的Media ID
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Convert Instagram post shortcode to media ID
> - Shortcode is the unique identifier in post URL, e.g., DRhvwVLAHAG in instagram.com/p/DRhvwVLAHAG/
> ### Parameters:
> - shortcode: Post shortcode
> ### Return:
> - `status`: Conversion status
> - `shortcode`: Original shortcode
> - `media_id`: Converted media ID
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> shortcode = "DRhvwVLAHAG"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shortcode | query | string | Yes | 帖子Shortcode/Post shortcode | None | DRhvwVLAHAG | None |

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

<a id="get-api-u1-v1-instagram-v2-user-id-to-username"></a>
### `GET /api/u1/v1/instagram/v2/user_id_to_username`

- Summary: 用户ID转用户信息/Get user info by user ID
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `user_id_to_username_api_v1_instagram_v2_user_id_to_username_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过Instagram用户ID获取用户信息
> - 可用于将用户ID转换为用户名及获取完整用户资料
> ### 参数:
> - user_id: 用户ID
> ### 返回:
> - `pk`/`pk_id`: 用户ID
> - `username`: 用户名
> - `full_name`: 用户全名
> - `is_private`: 是否私密账户
> - `is_verified`: 是否已认证
> - `profile_pic_url`: 头像URL
> - `biography`: 个人简介
> - `follower_count`: 粉丝数
> - `following_count`: 关注数
> - `media_count`: 帖子数
> ### 价格:
> - 0.002 USD/请求
>
> # [English]
> ### Purpose:
> - Get user info by Instagram user ID
> - Can be used to convert user ID to username and get full profile
> ### Parameters:
> - user_id: User ID
> ### Return:
> - `pk`/`pk_id`: User ID
> - `username`: Username
> - `full_name`: Full name
> - `is_private`: Whether account is private
> - `is_verified`: Whether account is verified
> - `profile_pic_url`: Profile picture URL
> - `biography`: Bio
> - `follower_count`: Followers count
> - `following_count`: Following count
> - `media_count`: Posts count
> ### Price:
> - 0.002 USD/request
>
> # [示例/Example]
> user_id = "18527"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 18527 | None |

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
