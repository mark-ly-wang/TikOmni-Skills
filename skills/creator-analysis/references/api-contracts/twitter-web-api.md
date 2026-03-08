# Twitter-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/twitter-web-api.md`](../api-tags/twitter-web-api.md)
- Current contract file: `api-contracts/twitter-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `13`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(Twitter Web数据接口/Twitter-Web-API endpoints)**

## Route Contracts

<a id="get-api-u1-v1-twitter-web-fetch-latest-post-comments"></a>
### `GET /api/u1/v1/twitter/web/fetch_latest_post_comments`

- Summary: 获取最新的推文评论/Get the latest tweet comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取最新的推文评论
> ### 参数:
> - tweet_id: 推文ID
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
> ### 返回:
> - 推文评论
>
> # [English]
> ### Purpose:
> - Get the latest tweet comments
> ### Parameters:
> - tweet_id: Tweet ID
> - cursor: Cursor, default is None, used for paging, obtained from the last request
> ### Return:
> - Tweet comments
>
> # [示例/Example]
> tweet_id = "1808168603721650364"
> cursor = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | Yes | 推文ID/Tweet ID | None | 1808168603721650364 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-post-comments"></a>
### `GET /api/u1/v1/twitter/web/fetch_post_comments`

- Summary: 获取评论/Get comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取推文下的评论
> ### 参数:
> - tweet_id: 推文ID
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
> ### 返回:
> - 评论
>
> # [English]
> ### Purpose:
> - Get comments under the tweet
> ### Parameters:
> - tweet_id: Tweet ID
> - cursor: Cursor, default is None, used for paging, obtained from the last request
> ### Return:
> - Comments
>
> # [示例/Example]
> tweet_id = "1808168603721650364"
> cursor = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | Yes | 推文ID/Tweet ID | None | 1835124037934367098 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-retweet-user-list"></a>
### `GET /api/u1/v1/twitter/web/fetch_retweet_user_list`

- Summary: 转推用户列表/ReTweet User list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取转推用户列表
> ### 参数:
> - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
> ### 返回:
> - 转推用户列表
>
> # [English]
> ### Purpose:
> - Get ReTweet User list
> ### Parameters:
> - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364
> - cursor: Cursor, default is None, used for paging, obtained from the last request
> ### Return:
> - ReTweet User list
>
> # [示例/Example]
> tweet_id = "1808168603721650364"
> cursor = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | Yes | 推文ID/Tweet ID | None | 1835124037934367098 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-search-timeline"></a>
### `GET /api/u1/v1/twitter/web/fetch_search_timeline`

- Summary: 搜索/Search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索
> ### 参数:
> - keyword: 搜索关键字
> - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
> ### 返回:
> - 搜索结果
>
> # [English]
> ### Purpose:
> - Search
> ### Parameters:
> - keyword: Search keyword
> - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists
> - cursor: Cursor, default is None, used for paging, obtained from the last request
> ### Return:
> - Search results
>
> # [示例/Example]
> keyword = "Elon Musk"
> search_type = "Top"
> cursor = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键字/Search Keyword | None | Elon Musk | None |
| search_type | query | string | No | 搜索类型/Search Type | Top | Top | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-trending"></a>
### `GET /api/u1/v1/twitter/web/fetch_trending`

- Summary: 趋势/Trending
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_trending_api_v1_twitter_web_fetch_trending_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取趋势
> ### 参数:
> - country: 国家，默认为UnitedStates，其他可选值见下方
>     - China
>     - India
>     - Japan
>     - Russia
>     - Germany
>     - Indonesia
>     - Brazil
>     - France
>     - UnitedKingdom
>     - Turkey
>     - Italy
>     - Mexico
>     - SouthKorea
>     - Canada
>     - Spain
>     - SaudiArabia
>     - Egypt
>     - Australia
>     - Poland
>     - Iran
>     - Pakistan
>     - Vietnam
>     - Nigeria
>     - Bangladesh
>     - Netherlands
>     - Argentina
>     - Philippines
>     - Malaysia
>     - Colombia
>     - UniteArabEmirates
>     - Romania
>     - Belgium
>     - Switzerland
>     - Singapore
>     - Sweden
>     - Norway
>     - Austria
>     - Kazakhstan
>     - Algeria
>     - Chile
>     - Czechia
>     - Peru
>     - Iraq
>     - Israel
>     - Ukraine
>     - Denmark
>     - Portugal
>     - Hungary
>     - Greece
>     - Finland
>     - NewZealand
>     - Belarus
>     - Slovakia
>     - Serbia
>     - Lithuania
>     - Luxembourg
>     - Estonia
>
> ### 返回:
> - 趋势
>
> # [English]
> ### Purpose:
> - Get Trending
> ### Parameters:
> - country: Country, default is UnitedStates, other optional values are as follows
>     - China
>     - India
>     - Japan
>     - Russia
>     - Germany
>     - Indonesia
>     - Brazil
>     - France
>     - UnitedKingdom
>     - Turkey
>     - Italy
>     - Mexico
>     - SouthKorea
>     - Canada
>     - Spain
>     - SaudiArabia
>     - Egypt
>     - Australia
>     - Poland
>     - Iran
>     - Pakistan
>     - Vietnam
>     - Nigeria
>     - Bangladesh
>     - Netherlands
>     - Argentina
>     - Philippines
>     - Malaysia
>     - Colombia
>     - UniteArabEmirates
>     - Romania
>     - Belgium
>     - Switzerland
>     - Singapore
>     - Sweden
>     - Norway
>     - Austria
>     - Kazakhstan
>     - Algeria
>     - Chile
>     - Czechia
>     - Peru
>
> ### Return:
> - Trending
>
> # [示例/Example]
> country = "UnitedStates"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| country | query | string | No | 国家/Country | UnitedStates | UnitedStates | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-tweet-detail"></a>
### `GET /api/u1/v1/twitter/web/fetch_tweet_detail`

- Summary: 获取单个推文数据/Get single tweet data
- Capabilities: details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个推文数据
> ### 参数:
> - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的 1808168603721650364。
> ### 返回:
> - 推文数据
>
> # [English]
> ### Purpose:
> - Get single tweet data
> ### Parameters:
> - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364
> ### Return:
> - Tweet data
>
> # [示例/Example]
> tweet_id = "1808168603721650364"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | Yes | 推文ID/Tweet ID | None | 1808168603721650364 | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-followers"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_followers`

- Summary: 用户粉丝/User Followers
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户粉丝
> ### 参数:
> - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
> ### 返回:
> - 用户粉丝
>
> # [English]
> ### Purpose:
> - Get User Followers
> ### Parameters:
> - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk
> - cursor: Cursor, default is None, used for paging, obtained from the last request
> ### Return:
> - User Followers
>
> # [示例/Example]
> screen_name = "elonmusk"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | Yes | 用户名/Screen Name | None | elonmusk | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-followings"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_followings`

- Summary: 用户关注/User Followings
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户关注
> ### 参数:
> - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
> ### 返回:
> - 用户关注
>
> # [English]
> ### Purpose:
> - Get User Followings
> ### Parameters:
> - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk
> - cursor: Cursor, default is None, used for paging, obtained from the last request
> ### Return:
> - User Followings
>
> # [示例/Example]
> screen_name = "elonmusk"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | Yes | 用户名/Screen Name | None | elonmusk | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-highlights-tweets"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_highlights_tweets`

- Summary: 获取用户高光推文/Get user highlights tweets
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户高光推文
> ### 参数:
> - userId: 用户ID
> - count: 数量，默认为20
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
>     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value
> ### 返回:
> - 用户高光推文
>
> # [English]
> ### Purpose:
> - Get user highlights tweets
> ### Parameters:
> - userId: User ID
> - count: Count, default is 20
> - cursor: Cursor, default is None, used for paging, obtained from the last request
>     - JSONPath: $.data.data.user.result.timeline_v2.timeline.instructions.[1].entries.[-1].content.value
> ### Return:
> - User highlights tweets
>
> # [示例/Example]
> userId = "44196397"
> count = 20
> cursor = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| userId | query | string | Yes | 用户ID/User ID | None | 44196397 | None |
| count | query | integer | No | 数量/Count | 20 | 20 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-media"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_media`

- Summary: 获取用户媒体/Get user media
- Capabilities: profiles / accounts / media / download
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_media_api_v1_twitter_web_fetch_user_media_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户媒体
> ### 参数:
> - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
> - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的 `next_cursor` 获取
> ### 返回:
> - 用户媒体
>
> # [English]
> ### Purpose:
> - Get user media
> ### Parameters:
> - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk
> - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.
> - cursor: Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request
> ### Return:
> - User media
>
> # [示例/Example]
> screen_name = "elonmusk"
> cursor = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | Yes | 用户名/Screen Name | None | elonmusk | None |
| rest_id | query | integer | No | 用户ID/User ID | None | 44196397 | None |
| cursor | query | string | No | 翻页游标/Page Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-post-tweet"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_post_tweet`

- Summary: 获取用户发帖/Get user post
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户发帖
> ### 参数:
> - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
> - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中的JSON中获取。
> ### 返回:
> - 用户发帖
>
> # [English]
> ### Purpose:
> - Get user post
> ### Parameters:
> - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk
> - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.
> - cursor: Cursor, default is None, used for paging, obtained from the JSON in the last request.
>
> # [示例/Example]
> screen_name = "elonmusk"
> rest_id = 44196397
> cursor = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | No | 用户名/Screen Name | None | elonmusk | None |
| rest_id | query | integer | No | 用户ID/User ID | None | 44196397 | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-profile"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_profile`

- Summary: 获取用户资料/Get user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户资料
> ### 参数:
> - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
> - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。
> ### 返回:
> - 用户资料
>
> # [English]
> ### Purpose:
> - Get user profile
> ### Parameters:
> - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk
> - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.
> ### Return:
> - User profile
>
> # [示例/Example]
> screen_name = "elonmusk"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | No | 用户名/Screen Name | None | elonmusk | None |
| rest_id | query | integer | No | 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the user name will be ignored) | None | 44196397 | None |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-tweet-replies"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_tweet_replies`

- Summary: 获取用户推文回复/Get user tweet replies
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户推文回复
> ### 参数:
> - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
> - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
> ### 返回:
> - 用户推文回复
>
> # [English]
> ### Purpose:
> - Get user tweet replies
> ### Parameters:
> - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk
> - cursor: Cursor, default is None, used for paging, obtained from the last request
> ### Return:
> - User tweet replies
>
> # [示例/Example]
> screen_name = "elonmusk"
> cursor = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | Yes | 用户名/Screen Name | None | elonmusk | None |
| cursor | query | string | No | 游标/Cursor | None | None | None |

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
