# Twitter-Web-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/twitter-web-api.md`](../api-tags/twitter-web-api.md)
- 当前契约文件：`api-contracts/twitter-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`13`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(Twitter Web数据接口/Twitter-Web-API endpoints)**

## 路由契约

<a id="get-api-u1-v1-twitter-web-fetch-latest-post-comments"></a>
### `GET /api/u1/v1/twitter/web/fetch_latest_post_comments`

- 摘要：获取最新的推文评论/Get the latest tweet comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_latest_post_comments_api_v1_twitter_web_fetch_latest_post_comments_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | 是 | 推文ID/Tweet ID | 无 | 1808168603721650364 | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-post-comments"></a>
### `GET /api/u1/v1/twitter/web/fetch_post_comments`

- 摘要：获取评论/Get comments
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_post_comments_api_v1_twitter_web_fetch_post_comments_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | 是 | 推文ID/Tweet ID | 无 | 1835124037934367098 | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-retweet-user-list"></a>
### `GET /api/u1/v1/twitter/web/fetch_retweet_user_list`

- 摘要：转推用户列表/ReTweet User list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_retweet_user_list_api_v1_twitter_web_fetch_retweet_user_list_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | 是 | 推文ID/Tweet ID | 无 | 1835124037934367098 | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-search-timeline"></a>
### `GET /api/u1/v1/twitter/web/fetch_search_timeline`

- 摘要：搜索/Search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_timeline_api_v1_twitter_web_fetch_search_timeline_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键字/Search Keyword | 无 | Elon Musk | 无 |
| search_type | query | string | 否 | 搜索类型/Search Type | Top | Top | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-trending"></a>
### `GET /api/u1/v1/twitter/web/fetch_trending`

- 摘要：趋势/Trending
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_trending_api_v1_twitter_web_fetch_trending_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| country | query | string | 否 | 国家/Country | UnitedStates | UnitedStates | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-tweet-detail"></a>
### `GET /api/u1/v1/twitter/web/fetch_tweet_detail`

- 摘要：获取单个推文数据/Get single tweet data
- 能力：详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_tweet_detail_api_v1_twitter_web_fetch_tweet_detail_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tweet_id | query | string | 是 | 推文ID/Tweet ID | 无 | 1808168603721650364 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-followers"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_followers`

- 摘要：用户粉丝/User Followers
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_followers_api_v1_twitter_web_fetch_user_followers_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | 是 | 用户名/Screen Name | 无 | elonmusk | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-followings"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_followings`

- 摘要：用户关注/User Followings
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_followings_api_v1_twitter_web_fetch_user_followings_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | 是 | 用户名/Screen Name | 无 | elonmusk | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-highlights-tweets"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_highlights_tweets`

- 摘要：获取用户高光推文/Get user highlights tweets
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_highlights_tweets_api_v1_twitter_web_fetch_user_highlights_tweets_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| userId | query | string | 是 | 用户ID/User ID | 无 | 44196397 | 无 |
| count | query | integer | 否 | 数量/Count | 20 | 20 | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-media"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_media`

- 摘要：获取用户媒体/Get user media
- 能力：主页/账号 / 下载/媒体
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_media_api_v1_twitter_web_fetch_user_media_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | 是 | 用户名/Screen Name | 无 | elonmusk | 无 |
| rest_id | query | integer | 否 | 用户ID/User ID | 无 | 44196397 | 无 |
| cursor | query | string | 否 | 翻页游标/Page Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-post-tweet"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_post_tweet`

- 摘要：获取用户发帖/Get user post
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_post_tweet_api_v1_twitter_web_fetch_user_post_tweet_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | 否 | 用户名/Screen Name | 无 | elonmusk | 无 |
| rest_id | query | integer | 否 | 用户ID/User ID | 无 | 44196397 | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-profile"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_profile`

- 摘要：获取用户资料/Get user profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_profile_api_v1_twitter_web_fetch_user_profile_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | 否 | 用户名/Screen Name | 无 | elonmusk | 无 |
| rest_id | query | integer | 否 | 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the user name will be ignored) | 无 | 44196397 | 无 |

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

<a id="get-api-u1-v1-twitter-web-fetch-user-tweet-replies"></a>
### `GET /api/u1/v1/twitter/web/fetch_user_tweet_replies`

- 摘要：获取用户推文回复/Get user tweet replies
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_tweet_replies_api_v1_twitter_web_fetch_user_tweet_replies_get`

#### 说明

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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| screen_name | query | string | 是 | 用户名/Screen Name | 无 | elonmusk | 无 |
| cursor | query | string | 否 | 游标/Cursor | 无 | 无 | 无 |

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
