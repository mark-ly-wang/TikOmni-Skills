# Reddit-APP-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/reddit-app-api.md`](../api-tags/reddit-app-api.md)
- Current contract file: `api-contracts/reddit-app-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `24`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(Reddit APP数据接口/Reddit-APP-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-reddit-app-check-subreddit-muted"></a>
### `GET /api/u1/v1/reddit/app/check_subreddit_muted`

- Summary: 检查版块是否静音/Check if Subreddit is Muted
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `check_subreddit_muted_api_v1_reddit_app_check_subreddit_muted_get`

#### Notes

> # [中文]
> ### 用途:
> - 检查指定Reddit版块是否被当前用户静音
> ### 参数:
> - subreddit_id: 版块ID,格式为"t5_"开头,可从fetch_subreddit_info接口获取
> ### 返回:
> - 静音状态JSON数据,包含:
>   - isMuted: 是否静音的布尔值
>   - subredditId: 版块ID
> ### 注意:
> - **APP接口的ID格式与Web接口不同，需要添加类型前缀**
> - 版块ID前缀: t5_ (例如: t5_2qh0u)
>
> # [English]
> ### Purpose:
> - Check if a specified Reddit subreddit is muted by the current user
> ### Parameters:
> - subreddit_id: Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint
> ### Returns:
> - JSON data of mute status containing:
>   - isMuted: Boolean value indicating if muted
>   - subredditId: Subreddit ID
> ### Note:
> - **APP API ID format differs from Web API, requires type prefix**
> - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)
>
> # [示例/Example]
> subreddit_id="t5_2qh0u"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subreddit_id | query | string | Yes | 版块ID/Subreddit ID (format: t5_xxxxx) | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-comment-replies"></a>
### `GET /api/u1/v1/reddit/app/fetch_comment_replies`

- Summary: 获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments)
- Capabilities: comments
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_comment_replies_api_v1_reddit_app_fetch_comment_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定评论下的回复（二级评论/子评论）
> - 当评论节点有 more.cursor 字段时，使用此接口获取该评论的子评论
> ### 参数:
> - post_id: 帖子ID，格式如 "t3_XXXXXX"
> - cursor: 评论游标，从评论数据的 more.cursor 字段获取，格式如 "commenttree:ex:(xxx)"
> - sort_type: 排序方式，支持CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM
> ### 返回:
> - 指定评论下的回复JSON数据，包含：
>   - 子评论列表
>   - 每个子评论的详细信息（内容、作者、点赞数等）
>   - 分页信息
> ### 使用步骤:
> 1. 先调用 fetch_post_comments 获取帖子的一级评论
> 2. 在返回数据中找到有子评论的节点（childCount > 0）
> 3. 获取该节点的 more.cursor 值
> 4. 使用该 cursor 调用本接口获取子评论
> ### 注意:
> - cursor 值来自评论数据的 more.cursor 字段
> - 路径示例: $.data.postInfoById.commentForest.trees[*].more.cursor
> - cursor 格式类似: "commenttree:ex:(RjiJd"
>
> # [English]
> ### Purpose:
> - Fetch replies (sub-comments/second-level comments) under a specified Reddit APP comment
> - Use this endpoint when a comment node has more.cursor field to get its sub-comments
> ### Parameters:
> - post_id: Post ID, format like "t3_XXXXXX"
> - cursor: Comment cursor from the more.cursor field in comment data, format like "commenttree:ex:(xxx)"
> - sort_type: Sort method, supports CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM
> ### Returns:
> - JSON data of replies under the specified comment, containing:
>   - List of sub-comments
>   - Detailed information for each sub-comment (content, author, upvotes, etc.)
>   - Pagination information
> ### Usage Steps:
> 1. First call fetch_post_comments to get top-level comments
> 2. Find comment nodes with sub-comments (childCount > 0)
> 3. Get the more.cursor value from that node
> 4. Use that cursor to call this endpoint to fetch sub-comments
> ### Note:
> - cursor value comes from the more.cursor field in comment data
> - Path example: $.data.postInfoById.commentForest.trees[*].more.cursor
> - cursor format example: "commenttree:ex:(RjiJd"
>
> # [示例/Example]
> post_id="t3_1qmup73"
> cursor="commenttree:ex:(RjiJd"
> sort_type="CONFIDENCE"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID (e.g., t3_1qmup73) | None | None | None |
| cursor | query | string | Yes | 评论游标/Comment cursor from more.cursor field (e.g., commenttree:ex:(RjiJd) | None | None | None |
| sort_type | query | string | No | 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM | CONFIDENCE | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-community-highlights"></a>
### `GET /api/u1/v1/reddit/app/fetch_community_highlights`

- Summary: 获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_community_highlights_api_v1_reddit_app_fetch_community_highlights_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定社区的精选亮点内容,包括热门帖子和重要公告
> ### 参数:
> - subreddit_id: 版块ID,格式为"t5_"开头,可从fetch_subreddit_info接口获取
> ### 返回:
> - 社区亮点JSON数据,包含:
>   - 精选帖子列表
>   - 置顶公告
>   - 社区重要动态
>   - 推荐内容
> ### 注意:
> - **APP接口的ID格式与Web接口不同，需要添加类型前缀**
> - 版块ID前缀: t5_ (例如: t5_2qh0u)
>
> # [English]
> ### Purpose:
> - Fetch featured highlight content of a specified Reddit APP community, including popular posts and important announcements
> ### Parameters:
> - subreddit_id: Subreddit ID starting with "t5_", can be obtained from fetch_subreddit_info endpoint
> ### Returns:
> - JSON data of community highlights containing:
>   - Featured post list
>   - Pinned announcements
>   - Important community updates
>   - Recommended content
> ### Note:
> - **APP API ID format differs from Web API, requires type prefix**
> - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)
>
> # [示例/Example]
> subreddit_id="t5_2qh0u"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subreddit_id | query | string | Yes | 版块ID/Subreddit ID (format: t5_xxxxx) | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-dynamic-search"></a>
### `GET /api/u1/v1/reddit/app/fetch_dynamic_search`

- Summary: 获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_dynamic_search_api_v1_reddit_app_fetch_dynamic_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 执行Reddit APP动态搜索,支持搜索帖子、社区、评论、媒体和用户
> ### 参数:
> - query: 搜索关键词
> - search_type: 搜索类型,可选值:
>   - post: 搜索帖子(默认)
>   - community: 搜索社区/版块
>   - comment: 搜索评论
>   - media: 搜索媒体(图片/视频/GIF)
>   - people: 搜索用户
> - sort: 排序方式(仅适用于post/comment/media类型),可选值:
>   - RELEVANCE: 相关性
>   - HOT: 热门
>   - TOP: 最受欢迎
>   - NEW: 最新
>   - COMMENTS: 评论数(仅适用于post类型)
> - time_range: 时间范围(仅适用于post/media类型),可选值:
>   - all: 所有时间
>   - year: 去年
>   - month: 上个月
>   - week: 上周
>   - day: 今天
>   - hour: 过去1小时
> - safe_search: 安全搜索设置,"unset"或"strict"
> - allow_nsfw: 是否允许NSFW内容,"0"或"1"
> - after: 分页参数,用于获取下一页结果
> ### 返回:
> - 搜索结果JSON数据,包含:
>   - 匹配的结果列表(根据search_type不同返回不同类型的数据)
>   - 分页信息
> ### 注意:
> - community和people类型不支持sort和time_range参数
> - COMMENTS排序方式仅适用于post类型
> - time_range参数仅适用于post和media类型
>
> # [English]
> ### Purpose:
> - Perform Reddit APP dynamic search, supporting posts, communities, comments, media, and users
> ### Parameters:
> - query: Search keyword
> - search_type: Search type, options:
>   - post: Search posts (default)
>   - community: Search communities/subreddits
>   - comment: Search comments
>   - media: Search media (images/videos/GIFs)
>   - people: Search users
> - sort: Sort method (only for post/comment/media types), options:
>   - RELEVANCE: By relevance
>   - HOT: Hot/trending
>   - TOP: Most popular
>   - NEW: Newest
>   - COMMENTS: By comment count (only for post type)
> - time_range: Time range (only for post/media types), options:
>   - all: All time
>   - year: Past year
>   - month: Past month
>   - week: Past week
>   - day: Today
>   - hour: Past hour
> - safe_search: Safe search setting, "unset" or "strict"
> - allow_nsfw: Allow NSFW content, "0" or "1"
> - after: Pagination parameter for fetching next page
> ### Returns:
> - JSON data of search results containing:
>   - List of matching results (different data types based on search_type)
>   - Pagination information
> ### Notes:
> - community and people types do not support sort and time_range parameters
> - COMMENTS sort option only applies to post type
> - time_range parameter only applies to post and media types
>
> # [示例/Example]
> query="python programming"
> search_type="post"
> sort="RELEVANCE"
> time_range="all"
> safe_search="unset"
> allow_nsfw="0"
> after=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search query | None | None | None |
| search_type | query | string | No | 搜索类型/Search type: post(帖子), community(社区), comment(评论), media(媒体), people(用户) | post | None | None |
| sort | query | string | No | 排序方式(仅适用于post/comment/media)/Sort method (only for post/comment/media): RELEVANCE(相关性), HOT(热门), TOP(最受欢迎), NEW(最新), COMMENTS(评论数,仅post) | None | None | None |
| time_range | query | string | No | 时间范围(仅适用于post/media)/Time range (only for post/media): all(所有时间), year(去年), month(上月), week(上周), day(今天), hour(过去1小时) | None | None | None |
| safe_search | query | string | No | 安全搜索设置/Safe search setting: unset, strict | unset | None | None |
| allow_nsfw | query | string | No | 是否允许NSFW内容/Allow NSFW content: 0, 1 | 0 | None | None |
| after | query | string | No | 分页参数/Pagination parameter | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-games-feed"></a>
### `GET /api/u1/v1/reddit/app/fetch_games_feed`

- Summary: 获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_games_feed_api_v1_reddit_app_fetch_games_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP游戏相关的推荐内容,展示游戏社区的热门帖子
> ### 参数:
> - sort: 排序方式,可选: NEW(最新), HOT(热门), TOP(顶级), RISING(上升中)
> - time: 时间范围,可选: ALL(全部时间), HOUR(一小时), DAY(一天), WEEK(一周), MONTH(一个月), YEAR(一年)
> - after: 分页参数,获取下一页时使用
> ### 返回:
> - 游戏推荐内容JSON数据,包含:
>   - 游戏相关帖子列表
>   - 游戏社区讨论
>   - 游戏新闻和更新
>
> # [English]
> ### Purpose:
> - Fetch gaming-related recommended content on Reddit APP, displaying popular posts from gaming communities
> ### Parameters:
> - sort: Sort method, options: NEW, HOT, TOP, RISING
> - time: Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR
> - after: Pagination parameter for fetching next page
> ### Returns:
> - JSON data of games feed containing:
>   - List of gaming-related posts
>   - Gaming community discussions
>   - Game news and updates
>
> # [示例/Example]
> sort="HOT"
> time="WEEK"
> after=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sort | query | string | No | 排序方式/Sort method: NEW, HOT, TOP, RISING | NEW | None | None |
| time | query | string | No | 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR | ALL | None | None |
| after | query | string | No | 分页参数/Pagination parameter | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-home-feed"></a>
### `GET /api/u1/v1/reddit/app/fetch_home_feed`

- Summary: 获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_feed_api_v1_reddit_app_fetch_home_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP首页推荐内容
> ### 参数:
> - sort: 排序方式，支持HOT, NEW, TOP, BEST, CONTROVERSIAL
> - filter_posts: 过滤掉指定的帖子ID列表，用于排除已获取的帖子，避免重复获取
> - after: 分页参数，获取下一页时使用
> ### 返回:
> - Reddit APP首页推荐内容的JSON数据
>
> # [English]
> ### Purpose:
> - Fetch Reddit APP home feed content
> ### Parameters:
> - sort: Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL
> - filter_posts: List of post IDs to filter out, used to exclude already fetched posts
> - after: Pagination parameter for fetching the next page
> ### Returns:
> - JSON data of Reddit APP home feed content
>
> # [示例/Example]
> sort="BEST"
>
> filter_posts=["t3_1ojjquz","t3_1ohepm2","t3_1ojxzzz","t3_1ojnvca","t3_1oj9dcb","t3_1ojxubp","t3_1oj5x2b"]
>
> after="dDNfMW9qNXgyYg=="

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sort | query | string | No | 排序方式/Sort method: HOT, NEW, TOP, BEST, CONTROVERSIAL | BEST | None | None |
| filter_posts | query | array<Not declared> | No | 过滤掉指定的帖子ID列表/Filter out specified post IDs | None | None | None |
| after | query | string | No | 分页参数/Pagination parameter for fetching next page | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-news-feed"></a>
### `GET /api/u1/v1/reddit/app/fetch_news_feed`

- Summary: 获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_news_feed_api_v1_reddit_app_fetch_news_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP新闻资讯推荐内容,展示最新的新闻和时事讨论
> ### 参数:
> - subtopic_ids: 子话题ID列表,默认["all"]表示所有新闻类别
> - after: 分页参数,获取下一页时使用
> ### 返回:
> - 新闻推荐内容JSON数据,包含:
>   - 新闻帖子列表
>   - 时事讨论
>   - 热点话题
>   - 新闻来源和链接
>
> # [English]
> ### Purpose:
> - Fetch news-related recommended content on Reddit APP, displaying latest news and current affairs discussions
> ### Parameters:
> - subtopic_ids: List of subtopic IDs, default ["all"] means all news categories
> - after: Pagination parameter for fetching next page
> ### Returns:
> - JSON data of news feed containing:
>   - List of news posts
>   - Current affairs discussions
>   - Trending topics
>   - News sources and links
>
> # [示例/Example]
> subtopic_ids=["all"]
> after=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subtopic_ids | query | array<Not declared> | No | 子话题ID列表/Subtopic IDs list | ["all"] | None | None |
| after | query | string | No | 分页参数/Pagination parameter | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-popular-feed"></a>
### `GET /api/u1/v1/reddit/app/fetch_popular_feed`

- Summary: 获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_popular_feed_api_v1_reddit_app_fetch_popular_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP流行/热门推荐内容,展示全站最受欢迎的帖子
> ### 参数:
> - sort: 排序方式,可选: BEST(最佳), HOT(热门), NEW(最新), TOP(顶级), CONTROVERSIAL(有争议), RISING(上升中)
> - time: 时间范围,可选: ALL(全部时间), HOUR(一小时), DAY(一天), WEEK(一周), MONTH(一个月), YEAR(一年)
> - filter_posts: 过滤掉指定的帖子ID列表,用于避免重复获取
> - after: 分页参数,获取下一页时使用
> ### 返回:
> - 流行推荐内容JSON数据,包含:
>   - 热门帖子列表
>   - 帖子详细信息(标题、内容、点赞数、评论数等)
>   - 分页信息(after参数用于下一页)
>
> # [English]
> ### Purpose:
> - Fetch popular/trending recommended content on Reddit APP, displaying the most popular posts site-wide
> ### Parameters:
> - sort: Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING
> - time: Time range, options: ALL, HOUR, DAY, WEEK, MONTH, YEAR
> - filter_posts: List of post IDs to filter out, used to avoid duplicate fetches
> - after: Pagination parameter for fetching next page
> ### Returns:
> - JSON data of popular feed containing:
>   - List of trending posts
>   - Detailed post information (title, content, upvotes, comments, etc.)
>   - Pagination information (after parameter for next page)
>
> # [示例/Example]
> sort="HOT"
> time="DAY"
> filter_posts=[]
> after=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sort | query | string | No | 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING | BEST | None | None |
| time | query | string | No | 时间范围/Time range: ALL, HOUR, DAY, WEEK, MONTH, YEAR | ALL | None | None |
| filter_posts | query | array<Not declared> | No | 过滤帖子ID列表/Filter post IDs | None | None | None |
| after | query | string | No | 分页参数/Pagination parameter | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-post-comments"></a>
### `GET /api/u1/v1/reddit/app/fetch_post_comments`

- Summary: 获取Reddit APP帖子评论/Fetch Reddit APP Post Comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_api_v1_reddit_app_fetch_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定帖子下的评论
> ### 参数:
> - post_id: 帖子ID，格式如 "t3_XXXXXX"
> - sort_type: 排序方式，支持CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM
> - after: 分页参数，获取下一页时使用，在commentForest里的最后一个评论节点中可以找到，例如$.data.postInfoById.commentForest.trees[-1].more.cursor
> ### 返回:
> - 指定帖子下的评论JSON数据
> ### 注意:
> - **APP接口的ID格式与Web接口不同，需要添加类型前缀**
> - 帖子ID前缀: t3_ (例如: t3_1ojnvca)
>
> # [English]
> ### Purpose:
> - Fetch comments under a specified Reddit APP post
> ### Parameters:
> - post_id: Post ID, format like "t3_XXXXXX"
> - sort_type: Sort method, supports HOT, NEW, TOP, BEST, CONTROVERSIAL
> - after: Pagination parameter for fetching the next page, can be found in the last comment node in commentForest, e.g., $.data.postInfoById.commentForest.trees[-1].more.cursor
> ### Returns:
> - JSON data of comments under the specified post
> ### Note:
> - **APP API ID format differs from Web API, requires type prefix**
> - Post ID prefix: t3_ (e.g., t3_1ojnvca)
>
> # [示例/Example]
> post_id="t3_1ojnvca"
>
> sort="CONFIDENCE"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID | None | None | None |
| sort_type | query | string | No | 排序方式/Sort method: CONFIDENCE, NEW, TOP, HOT, CONTROVERSIAL, OLD, RANDOM | CONFIDENCE | None | None |
| after | query | string | No | 分页参数/Pagination parameter for fetching next page | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-post-details"></a>
### `GET /api/u1/v1/reddit/app/fetch_post_details`

- Summary: 获取单个Reddit帖子详情/Fetch Single Reddit Post Details
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_details_api_v1_reddit_app_fetch_post_details_get`

#### Notes

> # [中文]
> ## 用途:
> - 根据帖子ID获取单个帖子详情
> - 可选择性包含特定评论的上下文
>
> ## 参数:
> - post_id: 帖子ID，格式如 "t3_XXXXXX"
> - include_comment_id: 是否包含特定评论ID，默认False
> - comment_id: 评论ID（当include_comment_id为True时使用），格式如 "t1_XXXXXX"
>
> ## 返回:
> - 包含帖子详细信息的数据，包括:
>   - 帖子内容、标题、作者
>   - 统计数据（点赞数、评论数等）
>   - 版块信息
>   - 奖励信息
>   - 媒体资源
>   - 推荐原因等
>
> ## 注意:
> - **APP接口的ID格式与Web接口不同，需要添加类型前缀**
> - 帖子ID前缀: t3_ (例如: t3_1ojnh50)
> - 评论ID前缀: t1_ (例如: t1_abcd123)
>
> ---
>
> # [English]
> ## Purpose:
> - Fetch single post details by post ID
> - Optionally include context for specific comments
>
> ## Parameters:
> - post_id: Post ID, format like "t3_XXXXXX"
> - include_comment_id: Whether to include specific comment ID, default False
> - comment_id: Comment ID (used when include_comment_id is True), format like "t1_XXXXXX"
>
> ## Returns:
> - Data containing detailed post information including:
>   - Post content, title, author
>   - Statistics (upvotes, comment count, etc.)
>   - Subreddit information
>   - Award information
>   - Media resources
>   - Recommendation reasons, etc.
>
> ## Note:
> - **APP API ID format differs from Web API, requires type prefix**
> - Post ID prefix: t3_ (e.g., t3_1ojnh50)
> - Comment ID prefix: t1_ (e.g., t1_abcd123)
>
> # [示例/Example]
> post_id="t3_1ojnh50"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_id | query | string | Yes | 帖子ID/Post ID (e.g., t3_1ojnh50) | None | None | None |
| include_comment_id | query | boolean | No | 是否包含特定评论ID/Include specific comment ID | false | None | None |
| comment_id | query | string | No | 评论ID/Comment ID (when include_comment_id is True) | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-post-details-batch"></a>
### `GET /api/u1/v1/reddit/app/fetch_post_details_batch`

- Summary: 批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5)
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_details_batch_api_v1_reddit_app_fetch_post_details_batch_get`

#### Notes

> # [中文]
> ## 用途:
> - 根据帖子ID列表批量获取帖子详情
> - 支持最多5条帖子的批量查询
> - 可选择性包含特定评论的上下文
>
> ## 参数:
> - post_ids: 帖子ID列表，逗号分隔，格式如 "t3_XXXXXX,t3_YYYYYY"，最多支持5条
> - include_comment_id: 是否包含特定评论ID，默认False
> - comment_id: 评论ID（当include_comment_id为True时使用），格式如 "t1_XXXXXX"
>
> ## 返回:
> - 包含帖子详细信息的数据，包括:
>   - 帖子内容、标题、作者
>   - 统计数据（点赞数、评论数等）
>   - 版块信息
>   - 奖励信息
>   - 媒体资源
>   - 推荐原因等
>
> ## 注意:
> - 最多支持5条帖子的批量查询
> - 超过5条将返回错误
> - **APP接口的ID格式与Web接口不同，需要添加类型前缀**
> - 帖子ID前缀: t3_ (例如: t3_1ojnh50)
> - 评论ID前缀: t1_ (例如: t1_abcd123)
>
> ---
>
> # [English]
> ## Purpose:
> - Fetch post details in batch by post ID list
> - Support batch query for up to 5 posts
> - Optionally include context for specific comments
>
> ## Parameters:
> - post_ids: Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY", max 5 posts
> - include_comment_id: Whether to include specific comment ID, default False
> - comment_id: Comment ID (used when include_comment_id is True), format like "t1_XXXXXX"
>
> ## Returns:
> - Data containing detailed post information including:
>   - Post content, title, author
>   - Statistics (upvotes, comment count, etc.)
>   - Subreddit information
>   - Award information
>   - Media resources
>   - Recommendation reasons, etc.
>
> ## Notes:
> - Maximum 5 posts per batch query
> - Error will be returned if exceeds 5 posts
> - **APP API ID format differs from Web API, requires type prefix**
> - Post ID prefix: t3_ (e.g., t3_1ojnh50)
> - Comment ID prefix: t1_ (e.g., t1_abcd123)
>
> # [示例/Example]
> post_ids="t3_1ojnh50,t3_1ok432f,t3_1nwil8j"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_ids | query | string | Yes | 帖子ID列表，逗号分隔，最多5条/Post IDs comma-separated, max 5 (e.g., t3_1ojnh50,t3_1ok432f) | None | None | None |
| include_comment_id | query | boolean | No | 是否包含特定评论ID/Include specific comment ID | false | None | None |
| comment_id | query | string | No | 评论ID/Comment ID (when include_comment_id is True) | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-post-details-batch-large"></a>
### `GET /api/u1/v1/reddit/app/fetch_post_details_batch_large`

- Summary: 大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30)
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_details_batch_large_api_v1_reddit_app_fetch_post_details_batch_large_get`

#### Notes

> # [中文]
> ## 用途:
> - 根据帖子ID列表大批量获取帖子详情
> - 支持最多30条帖子的批量查询
> - 可选择性包含特定评论的上下文
>
> ## 参数:
> - post_ids: 帖子ID列表，逗号分隔，格式如 "t3_XXXXXX,t3_YYYYYY,..."，最多支持30条
> - include_comment_id: 是否包含特定评论ID，默认False
> - comment_id: 评论ID（当include_comment_id为True时使用），格式如 "t1_XXXXXX"
>
> ## 返回:
> - 包含帖子详细信息的数据，包括:
>   - 帖子内容、标题、作者
>   - 统计数据（点赞数、评论数等）
>   - 版块信息
>   - 奖励信息
>   - 媒体资源
>   - 推荐原因等
>
> ## 注意:
> - 最多支持30条帖子的批量查询
> - 超过30条将返回错误
> - 大批量查询可能需要较长的响应时间
> - **APP接口的ID格式与Web接口不同，需要添加类型前缀**
> - 帖子ID前缀: t3_ (例如: t3_1ojnh50)
> - 评论ID前缀: t1_ (例如: t1_abcd123)
>
> ---
>
> # [English]
> ## Purpose:
> - Fetch post details in large batch by post ID list
> - Support batch query for up to 30 posts
> - Optionally include context for specific comments
>
> ## Parameters:
> - post_ids: Post IDs comma-separated, format like "t3_XXXXXX,t3_YYYYYY,...", max 30 posts
> - include_comment_id: Whether to include specific comment ID, default False
> - comment_id: Comment ID (used when include_comment_id is True), format like "t1_XXXXXX"
>
> ## Returns:
> - Data containing detailed post information including:
>   - Post content, title, author
>   - Statistics (upvotes, comment count, etc.)
>   - Subreddit information
>   - Award information
>   - Media resources
>   - Recommendation reasons, etc.
>
> ## Notes:
> - Maximum 30 posts per batch query
> - Error will be returned if exceeds 30 posts
> - Large batch queries may take longer to respond
> - **APP API ID format differs from Web API, requires type prefix**
> - Post ID prefix: t3_ (e.g., t3_1ojnh50)
> - Comment ID prefix: t1_ (e.g., t1_abcd123)
>
> # [示例/Example]
> post_ids="t3_1ojnh50,t3_1ok432f,t3_1nwil8j,t3_1oj6vn6,t3_1nuenmd,..."

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| post_ids | query | string | Yes | 帖子ID列表，逗号分隔，最多30条/Post IDs comma-separated, max 30 (e.g., t3_1ojnh50,t3_1ok432f,...) | None | None | None |
| include_comment_id | query | boolean | No | 是否包含特定评论ID/Include specific comment ID | false | None | None |
| comment_id | query | string | No | 评论ID/Comment ID (when include_comment_id is True) | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-search-typeahead"></a>
### `GET /api/u1/v1/reddit/app/fetch_search_typeahead`

- Summary: 获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_typeahead_api_v1_reddit_app_fetch_search_typeahead_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP搜索框的自动补全建议,包括推荐的版块、用户和搜索词
> ### 参数:
> - query: 搜索关键词,输入的搜索文本
> - safe_search: 安全搜索设置,可选值为"unset"(未设置)或"strict"(严格模式)
> - allow_nsfw: 是否允许显示NSFW(成人)内容,"0"表示不允许,"1"表示允许
> ### 返回:
> - 搜索建议JSON数据,包含以下类型的建议:
>   - 相关版块(subreddits)
>   - 相关用户(users)
>   - 搜索词建议(search suggestions)
>   - 热门话题(trending topics)
>
> # [English]
> ### Purpose:
> - Fetch autocomplete suggestions for the Reddit APP search box, including recommended subreddits, users, and search terms
> ### Parameters:
> - query: Search keyword, the search text being typed
> - safe_search: Safe search setting, options are "unset" or "strict"
> - allow_nsfw: Whether to allow NSFW (adult) content display, "0" means disallow, "1" means allow
> ### Returns:
> - JSON data of search suggestions containing the following types:
>   - Related subreddits
>   - Related users
>   - Search term suggestions
>   - Trending topics
>
> # [示例/Example]
> query="programming"
> safe_search="unset"
> allow_nsfw="0"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query | query | string | Yes | 搜索关键词/Search query | None | None | None |
| safe_search | query | string | No | 安全搜索设置/Safe search setting: unset, strict | unset | None | None |
| allow_nsfw | query | string | No | 是否允许NSFW内容/Allow NSFW content: 0 or 1 | 0 | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-subreddit-feed"></a>
### `GET /api/u1/v1/reddit/app/fetch_subreddit_feed`

- Summary: 获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_feed_api_v1_reddit_app_fetch_subreddit_feed_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定Reddit版块的Feed内容流,展示该版块的帖子列表
> ### 参数:
> - subreddit_name: 版块名称(不带r/前缀),如"pics", "funny"等
> - sort: 排序方式,可选: BEST(最佳), HOT(热门), NEW(最新), TOP(顶级), CONTROVERSIAL(有争议), RISING(上升中)
> - filter_posts: 过滤掉指定的帖子ID列表
> - after: 分页参数,获取下一页时使用
> ### 返回:
> - 版块Feed JSON数据,包含:
>   - 该版块的帖子列表
>   - 帖子详细信息
>   - 版块元数据
>   - 分页信息
>
> # [English]
> ### Purpose:
> - Fetch feed content stream of a specified Reddit subreddit, displaying the post list of that subreddit
> ### Parameters:
> - subreddit_name: Subreddit name (without r/ prefix), e.g., "pics", "funny"
> - sort: Sort method, options: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING
> - filter_posts: List of post IDs to filter out
> - after: Pagination parameter for fetching next page
> ### Returns:
> - JSON data of subreddit feed containing:
>   - List of posts in the subreddit
>   - Detailed post information
>   - Subreddit metadata
>   - Pagination information
>
> # [示例/Example]
> subreddit_name="AskReddit"
> sort="HOT"
> filter_posts=[]
> after=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subreddit_name | query | string | Yes | 版块名称/Subreddit name | None | None | None |
| sort | query | string | No | 排序方式/Sort method: BEST, HOT, NEW, TOP, CONTROVERSIAL, RISING | BEST | None | None |
| filter_posts | query | array<Not declared> | No | 过滤帖子ID列表/Filter post IDs | None | None | None |
| after | query | string | No | 分页参数/Pagination parameter | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-subreddit-info"></a>
### `GET /api/u1/v1/reddit/app/fetch_subreddit_info`

- Summary: 获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_info_api_v1_reddit_app_fetch_subreddit_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定版块的详细信息,包括版块描述、成员数量、创建时间、规则等元数据
> ### 参数:
> - subreddit_name: 版块名称(不带r/前缀),例如"pics", "funny", "AskReddit"等
> ### 返回:
> - 指定版块的详细信息JSON数据
> # [English]
> ### Purpose:
> - Fetch detailed information of a specified Reddit APP subreddit, including description, subscriber count, creation time, rules, and other metadata
> ### Parameters:
> - subreddit_name: Subreddit name (without r/ prefix), e.g., "pics", "funny", "AskReddit"
> ### Returns:
> - JSON data containing detailed subreddit information
>
> # [示例/Example]
> subreddit_name="pics"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subreddit_name | query | string | No | 版块名称/Subreddit name | pics | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-subreddit-post-channels"></a>
### `GET /api/u1/v1/reddit/app/fetch_subreddit_post_channels`

- Summary: 获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_post_channels_api_v1_reddit_app_fetch_subreddit_post_channels_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定版块的帖子频道信息
> ### 参数:
> - subreddit_name: 版块名称(不带r/前缀)
> - sort: 排序方式，支持HOT, NEW, TOP, CONTROVERSIAL, RISING
> - range: 时间范围，支持HOUR, DAY, WEEK, MONTH, YEAR, ALL
> ### 返回:
> - 指定版块的帖子频道信息JSON数据
>
> # [English]
> ### Purpose:
> - Fetch post channel information of a specified Reddit APP subreddit
> ### Parameters:
> - subreddit_name: Subreddit name
> - sort: Sort method, supports HOT, NEW, TOP, CONTROVERSIAL, RISING
> - range: Time range, supports HOUR, DAY, WEEK, MONTH, YEAR, ALL
> ### Returns:
> - JSON data of post channel information of the specified subreddit
>
> # [示例/Example]
> subreddit_name="pics"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subreddit_name | query | string | No | 版块名称/Subreddit name | pics | None | None |
| sort | query | string | No | 排序方式/Sort method: HOT, NEW, TOP, CONTROVERSIAL, RISING | HOT | None | None |
| range | query | string | No | 时间范围/Time range: HOUR, DAY, WEEK, MONTH, YEAR, ALL | DAY | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-subreddit-settings"></a>
### `GET /api/u1/v1/reddit/app/fetch_subreddit_settings`

- Summary: 获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_settings_api_v1_reddit_app_fetch_subreddit_settings_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定版块的设置信息,包括发帖规则、用户标签设置、审核设置等配置信息
> ### 参数:
> - subreddit_id: 版块ID,格式为t5_开头的唯一标识符,例如"t5_2qh0u"(可从fetch_subreddit_info接口获取版块ID)
> ### 返回:
> - 指定版块的设置信息JSON数据,包含以下主要字段:
>   - subredditType: 版块类型(public/private/restricted)
>   - submissionType: 允许提交的内容类型(any/link/self)
>   - allowImages: 是否允许图片
>   - allowVideos: 是否允许视频
>   - allowPolls: 是否允许投票
>   - suggestedCommentSort: 建议的评论排序方式
>   - spoilersEnabled: 是否启用剧透标记
>   - allowedPostTypes: 允许的帖子类型配置
>   - contentOptions: 内容选项设置
>   - flairSettings: 用户/帖子标签设置
> ### 注意事项:
> - 需要先通过fetch_subreddit_info接口获取版块ID(subreddit.id字段)
> - 版块ID格式必须为"t5_"开头
> - **APP接口的ID格式与Web接口不同，需要添加类型前缀**
> - 版块ID前缀: t5_ (例如: t5_2qh0u)
>
> # [English]
> ### Purpose:
> - Fetch settings information of a specified Reddit APP subreddit, including posting rules, flair settings, moderation settings, and other configurations
> ### Parameters:
> - subreddit_id: Subreddit ID with format starting with t5_, e.g., "t5_2qh0u" (can be obtained from the fetch_subreddit_info endpoint)
> ### Returns:
> - JSON data containing subreddit settings with the following main fields:
>   - subredditType: Subreddit type (public/private/restricted)
>   - submissionType: Allowed submission content types (any/link/self)
>   - allowImages: Whether images are allowed
>   - allowVideos: Whether videos are allowed
>   - allowPolls: Whether polls are allowed
>   - suggestedCommentSort: Suggested comment sort method
>   - spoilersEnabled: Whether spoiler tags are enabled
>   - allowedPostTypes: Allowed post types configuration
>   - contentOptions: Content options settings
>   - flairSettings: User/post flair settings
> ### Notes:
> - You need to first get the subreddit ID (subreddit.id field) via the fetch_subreddit_info endpoint
> - Subreddit ID format must start with "t5_"
> - **APP API ID format differs from Web API, requires type prefix**
> - Subreddit ID prefix: t5_ (e.g., t5_2qh0u)
>
> # [示例/Example]
> subreddit_id="t5_2qh0u"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subreddit_id | query | string | Yes | 版块ID/Subreddit ID (format: t5_xxxxx) | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-subreddit-style"></a>
### `GET /api/u1/v1/reddit/app/fetch_subreddit_style`

- Summary: 获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_subreddit_style_api_v1_reddit_app_fetch_subreddit_style_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定版块的规则和样式信息
> ### 参数:
> - subreddit_name: 版块名称(不带r/前缀)
> ### 返回:
> - 指定版块的规则和样式信息JSON数据
>
> # [English]
> ### Purpose:
> - Fetch rules and style information of a specified Reddit APP subreddit
> ### Parameters:
> - subreddit_name: Subreddit name
> ### Returns:
> - JSON data of rules and style information of the specified subreddit
>
> # [示例/Example]
> subreddit_name="pics"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subreddit_name | query | string | No | 版块名称/Subreddit name | pics | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-trending-searches"></a>
### `GET /api/u1/v1/reddit/app/fetch_trending_searches`

- Summary: 获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_trending_searches_api_v1_reddit_app_fetch_trending_searches_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP当前热门搜索话题和趋势内容
> ### 参数:
> - 无需参数
> ### 返回:
> - 热门搜索JSON数据,包含:
>   - 热门搜索关键词列表
>   - 趋势话题
>   - 每个话题的搜索量和热度
>   - 相关帖子预览
>
> # [English]
> ### Purpose:
> - Fetch currently trending search topics and content on Reddit APP
> ### Parameters:
> - No parameters required
> ### Returns:
> - JSON data of trending searches containing:
>   - List of trending search keywords
>   - Trending topics
>   - Search volume and popularity for each topic
>   - Related post previews
>
> # [示例/Example]
> 无需参数/No parameters required

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-user-active-subreddits"></a>
### `GET /api/u1/v1/reddit/app/fetch_user_active_subreddits`

- Summary: 获取用户活跃的社区列表/Fetch User's Active Subreddits
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_active_subreddits_api_v1_reddit_app_fetch_user_active_subreddits_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户最活跃的Reddit社区列表
> ### 参数:
> - username: Reddit用户名
> ### 返回:
> - 用户活跃社区JSON数据,包含:
>   - 用户最常发帖/评论的社区列表
>   - 每个社区的活跃度信息
>   - 社区基本信息(名称、图标、成员数等)
>
> # [English]
> ### Purpose:
> - Fetch list of Reddit communities where the specified user is most active
> ### Parameters:
> - username: Reddit username
> ### Returns:
> - JSON data of user's active communities containing:
>   - List of communities where user posts/comments most
>   - Activity level in each community
>   - Basic community information (name, icon, member count, etc.)
>
> # [示例/Example]
> username="spez"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-user-comments"></a>
### `GET /api/u1/v1/reddit/app/fetch_user_comments`

- Summary: 获取用户评论列表/Fetch User Comments
- Capabilities: comments / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_comments_api_v1_reddit_app_fetch_user_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户发表的评论列表
> ### 参数:
> - username: Reddit用户名
> - sort: 排序方式,可选值: NEW(最新), TOP(最热), HOT(热门), CONTROVERSIAL(有争议)
> - page_size: 每页返回的评论数量,默认25条
> - after: 分页参数,用于获取下一页
> ### 返回:
> - 用户评论列表JSON数据,包含:
>   - 评论内容
>   - 评论所在的帖子信息
>   - 评论时间
>   - 点赞数
>   - 回复数
>   - 分页信息
>
> # [English]
> ### Purpose:
> - Fetch list of comments posted by the specified user
> ### Parameters:
> - username: Reddit username
> - sort: Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial)
> - page_size: Number of comments per page, default 25
> - after: Pagination parameter for fetching next page
> ### Returns:
> - JSON data of user comments containing:
>   - Comment content
>   - Information about the post where comment was made
>   - Comment timestamp
>   - Upvote count
>   - Reply count
>   - Pagination information
>
> # [示例/Example]
> username="spez"
> sort="NEW"
> page_size=25
> after=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | None | None |
| sort | query | string | No | 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL | NEW | None | None |
| page_size | query | integer | No | 每页数量/Page size (default: 25) | 25 | None | None |
| after | query | string | No | 分页参数/Pagination parameter | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-user-posts"></a>
### `GET /api/u1/v1/reddit/app/fetch_user_posts`

- Summary: 获取用户发布的帖子列表/Fetch User Posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_posts_api_v1_reddit_app_fetch_user_posts_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户发布的帖子列表
> ### 参数:
> - username: Reddit用户名
> - sort: 排序方式,可选值: NEW(最新), TOP(最热), HOT(热门), CONTROVERSIAL(有争议)
> - after: 分页参数,用于获取下一页
> ### 返回:
> - 用户帖子列表JSON数据,包含:
>   - 帖子标题和内容
>   - 发布时间
>   - 所属版块
>   - 点赞数和评论数
>   - 帖子类型(文本/图片/视频/链接)
>   - 媒体内容(如有)
>   - 分页信息
>
> # [English]
> ### Purpose:
> - Fetch list of posts submitted by the specified user
> ### Parameters:
> - username: Reddit username
> - sort: Sort method, options: NEW (newest), TOP (top rated), HOT (hot), CONTROVERSIAL (controversial)
> - after: Pagination parameter for fetching next page
> ### Returns:
> - JSON data of user posts containing:
>   - Post title and content
>   - Submission time
>   - Subreddit
>   - Upvote and comment counts
>   - Post type (text/image/video/link)
>   - Media content (if any)
>   - Pagination information
>
> # [示例/Example]
> username="spez"
> sort="NEW"
> after=""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | None | None |
| sort | query | string | No | 排序方式/Sort method: NEW, TOP, HOT, CONTROVERSIAL | NEW | None | None |
| after | query | string | No | 分页参数/Pagination parameter | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-user-profile"></a>
### `GET /api/u1/v1/reddit/app/fetch_user_profile`

- Summary: 获取Reddit APP用户资料信息/Fetch Reddit APP User Profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_profile_api_v1_reddit_app_fetch_user_profile_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取Reddit APP指定用户的详细资料信息
> ### 参数:
> - username: Reddit用户名(不带u/前缀)
> ### 返回:
> - 用户资料JSON数据,包含:
>   - 用户名和ID
>   - 账号创建时间
>   - Karma值(帖子karma和评论karma)
>   - 头像和横幅图片
>   - 个人简介
>   - 是否验证账号
>   - 徽章和奖励
>   - 关注者数量
>
> # [English]
> ### Purpose:
> - Fetch detailed profile information of a specified Reddit APP user
> ### Parameters:
> - username: Reddit username (without u/ prefix)
> ### Returns:
> - JSON data of user profile containing:
>   - Username and ID
>   - Account creation date
>   - Karma values (post karma and comment karma)
>   - Avatar and banner images
>   - Bio/description
>   - Verification status
>   - Badges and awards
>   - Follower count
>
> # [示例/Example]
> username="spez"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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

<a id="get-api-u1-v1-reddit-app-fetch-user-trophies"></a>
### `GET /api/u1/v1/reddit/app/fetch_user_trophies`

- Summary: 获取用户公开奖杯/Fetch User Public Trophies
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_trophies_api_v1_reddit_app_fetch_user_trophies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定Reddit用户的公开奖杯/成就列表
> ### 参数:
> - username: Reddit用户名(不带u/前缀)
> ### 返回:
> - 用户奖杯JSON数据,包含:
>   - 奖杯列表(trophy list)
>   - 每个奖杯的详细信息:
>     - 奖杯名称
>     - 奖杯描述
>     - 奖杯图标URL
>     - 获得时间
>   - 特殊徽章和成就
>
> # [English]
> ### Purpose:
> - Fetch public trophies/achievements list of a specified Reddit user
> ### Parameters:
> - username: Reddit username (without u/ prefix)
> ### Returns:
> - JSON data of user trophies containing:
>   - Trophy list
>   - Detailed information for each trophy:
>     - Trophy name
>     - Trophy description
>     - Trophy icon URL
>     - Award date
>   - Special badges and achievements
>
> # [示例/Example]
> username="spez"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | None | None |
| need_format | query | boolean | No | 是否需要清洗数据/Whether to clean and format the data | false | None | None |

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
