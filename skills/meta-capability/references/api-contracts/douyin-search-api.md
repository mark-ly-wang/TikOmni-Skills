# Douyin-Search-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/douyin-search-api.md`](../api-tags/douyin-search-api.md)
- 当前契约文件：`api-contracts/douyin-search-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`20`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(抖音搜索数据接口（当前最新版，请优先使用此目录下的接口而不是其他目录下的搜索接口）/Douyin-Search-API data endpoints (Current latest version, please use the interfaces in this directory first instead of the search interfaces in other directories))**

## 路由契约

<a id="post-api-u1-v1-douyin-search-fetch-challenge-search-v1"></a>
### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v1`

- 摘要：获取话题搜索 V1/Fetch hashtag search V1
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_challenge_search_v1_api_v1_douyin_search_fetch_challenge_search_v1_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中的话题（挑战/标签）搜索结果。
> - 根据关键词返回关联的话题列表，包含话题热度、封面、参与人数等信息。
>
> ### 备注:
> - 仅返回话题类型内容。
> - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
> - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。
>
> ### 参数:
> - keyword: 搜索关键词，例如 "美食"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（分页时使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "美食",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `cursor`: 翻页游标（用于下次请求）
> - `has_more`: 是否还有更多数据（1=有，0=无）
> - `challenge_list[]`: 话题列表
>   - `challenge_info`:
>     - `cid`: 话题ID
>     - `cha_name`: 话题名称（如 "#美食探店"）
>     - `desc`: 话题描述（通常为空）
>     - `schema`: 抖音内部跳转链接（schema协议）
>     - `share_info`:
>       - `share_url`: 话题分享H5链接
>       - `share_title`: 分享标题
>       - `share_desc`: 分享描述
>     - `view_count`: 话题总浏览量
>     - `user_count`: 话题参与人数
>     - `hashtag_profile`: 话题封面图URL
>     - `challenge_status`: 话题状态（1=正常，0=异常）
>   - `author`:
>     - `uid`: 创建者用户ID
>     - `nickname`: 创建者昵称
>     - `follower_count`: 粉丝数量
>     - `is_verified`: 是否认证
>     - `region`: 地区
>     - `avatar_thumb.url_list`: 小头像URL列表
>     - `avatar_medium.url_list`: 中头像URL列表
>     - `avatar_larger.url_list`: 高清头像URL列表
>
> - `extra`:
>   - `now`: 当前服务器时间戳（毫秒）
>   - `search_request_id`: 搜索请求唯一ID
>
> # [English]
> ### Purpose:
> - Fetch hashtag/challenge search results from Douyin App.
> - Returns related hashtag topics including name, view count, participants, and cover images.
>
> ### Notes:
> - Only hashtag type content is returned.
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - For pagination, use `cursor` and `search_id` from the last response.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "food"
> - cursor: Pagination cursor (0 for first request)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Under 1 minute
>     - `1-5`: 1-5 minutes
>     - `5-10000`: Over 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Image
>     - `3`: Article
> - search_id: Search ID for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "food",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `cursor`: Cursor for next page
> - `has_more`: Whether more results are available (1=Yes, 0=No)
> - `challenge_list[]`: List of hashtags
>   - `challenge_info`:
>     - `cid`: Challenge ID
>     - `cha_name`: Challenge name (e.g., "#FoodHunt")
>     - `desc`: Challenge description
>     - `schema`: Deep link for Douyin App
>     - `share_info`:
>       - `share_url`: H5 shareable link
>       - `share_title`: Share title
>       - `share_desc`: Share description
>     - `view_count`: Total view count
>     - `user_count`: Total participant count
>     - `hashtag_profile`: Cover image URL
>     - `challenge_status`: Challenge status (1=Normal, 0=Abnormal)
>   - `author`:
>     - `uid`: Author's user ID
>     - `nickname`: Author's nickname
>     - `follower_count`: Follower count
>     - `is_verified`: Verified status
>     - `region`: Region
>     - `avatar_thumb.url_list`: Thumbnail avatar URLs
>     - `avatar_medium.url_list`: Medium avatar URLs
>     - `avatar_larger.url_list`: Large avatar URLs
>
> - `extra`:
>   - `now`: Server timestamp
>   - `search_request_id`: Unique search session ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-challenge-search-v2"></a>
### `POST /api/u1/v1/douyin/search/fetch_challenge_search_v2`

- 摘要：获取话题搜索 V2/Fetch hashtag search V2
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_challenge_search_v2_api_v1_douyin_search_fetch_challenge_search_v2_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中话题(挑战/标签)搜索的结果，使用 V2 版本 API。
> - 支持关键词搜索，返回匹配的话题详情，包括话题名称、话题封面、浏览量、参与人数等。
>
> ### 备注:
> - 本接口专注于搜索话题（Challenge/Hashtag）内容，不包含视频或直播等其他类型。
> - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串，后续翻页请使用上一次返回的 `cursor` 和 `search_id`。
>
> ### 参数:
> - keyword: 搜索关键词，如 "游戏"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（分页时使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "游戏",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `business_data`（话题搜索结果列表）
>   - `data_id`: 结果的唯一编号
>   - `type`: 数据类型（固定为 `2`）
>   - `data.challenge_info`:
>     - `cid`: 话题ID
>     - `cha_name`: 话题名称
>     - `desc`: 话题描述
>     - `schema`: 话题跳转链接（aweme://开头，可跳转抖音 App 内话题详情）
>     - `hashtag_profile`: 话题封面图 URL
>     - `user_count`: 参与人数
>     - `view_count`: 话题浏览量
>     - `challenge_status`: 话题状态（1=正常，其他=异常）
>     - `author`: 创建者信息
>       - `uid`: 创建者抖音用户ID
>       - `nickname`: 昵称
>       - `avatar_thumb.url_list`: 缩略头像URL列表
>       - `is_verified`: 是否认证
>       - `follower_count`: 粉丝数
>     - `share_info`:
>       - `share_url`: 话题分享链接
>       - `share_title`: 分享标题
>       - `share_desc`: 分享描述
>
> # [English]
> ### Purpose:
> - Fetch hashtag/challenge search results from Douyin App using V2 API.
> - Supports searching by keyword and returns detailed challenge information, including name, cover image, view count, and participant count.
>
> ### Notes:
> - This API focuses on searching challenges (hashtags), not including videos or live streams.
> - Set `cursor` to 0 and `search_id` to an empty string for the first request. For pagination, use the cursor and search_id from the last response.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "game"
> - cursor: Pagination cursor (0 for first request)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Under 1 minute
>     - `1-5`: 1-5 minutes
>     - `5-10000`: Over 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Image
>     - `3`: Article
> - search_id: Search ID for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "game",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `business_data` (list of hashtag search results)
>   - `data_id`: Unique identifier for the result
>   - `type`: Data type (fixed `2`)
>   - `data.challenge_info`:
>     - `cid`: Challenge ID
>     - `cha_name`: Challenge name
>     - `desc`: Challenge description
>     - `schema`: Challenge detail schema link (aweme:// schema, used to deep link inside Douyin App)
>     - `hashtag_profile`: URL of the hashtag cover image
>     - `user_count`: Number of participants
>     - `view_count`: Number of views
>     - `challenge_status`: Status (1 = active, others = abnormal)
>     - `author`: Creator info
>       - `uid`: User ID
>       - `nickname`: Nickname
>       - `avatar_thumb.url_list`: Thumbnail avatar URLs
>       - `is_verified`: Whether the creator is verified
>       - `follower_count`: Number of followers
>     - `share_info`:
>       - `share_url`: Shareable URL
>       - `share_title`: Title for sharing
>       - `share_desc`: Description for sharing

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-challenge-suggest"></a>
### `POST /api/u1/v1/douyin/search/fetch_challenge_suggest`

- 摘要：获取话题推荐搜索/Fetch hashtag suggestions
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_challenge_suggest_api_v1_douyin_search_fetch_challenge_suggest_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中话题(挑战/标签)的推荐搜索结果。
> - 根据输入的关键词，返回相关的话题建议列表，包含话题名称、浏览量等信息。
>
> ### 备注:
> - 本接口可用于话题联想推荐场景，如输入关键词实时展示相关热门话题。
> - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
>
> ### 参数:
> - keyword: 搜索关键词，如 "游戏"
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "游戏"
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `sug_list[]`: 推荐话题列表
>   - `cha_name`: 话题名称（如 "#游戏"）
>   - `view_count`: 话题总浏览量
>   - `cid`: 话题ID
>   - `group_id`: 话题关联的群组ID（可以用于跳转）
>   - `tag`: 话题标签分类（0=普通话题，1=流量风向标）
> - `status_code`: 状态码（0=成功）
> - `status_msg`: 状态信息（通常为空）
> - `rid`: 请求ID
> - `words_query_record`:
>   - `info`: 额外信息（目前为空）
>   - `words_source`: 关键词来源（固定"sug"）
>   - `query_id`: 查询ID（通常为空）
> - `extra`:
>   - `now`: 当前服务器时间戳
>   - `logid`: 日志ID
>   - `fatal_item_ids`: 错误项目ID列表（通常为空）
>   - `search_request_id`: 搜索请求ID（通常为空）
> - `log_pb`:
>   - `impr_id`: 曝光ID（日志追踪用）
>
> # [English]
> ### Purpose:
> - Fetch hashtag/challenge suggestions from Douyin App based on the input keyword.
> - Returns a list of related hashtags including name and view count.
>
> ### Notes:
> - Suitable for implementing keyword suggestion features in search bars.
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "game"
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "game"
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `sug_list[]`: List of suggested hashtags
>   - `cha_name`: Hashtag name (e.g., "#game")
>   - `view_count`: Total view count
>   - `cid`: Challenge ID
>   - `group_id`: Associated group ID
>   - `tag`: Tag category (0=normal, 1=hot trend)
> - `status_code`: Status code (0=success)
> - `status_msg`: Status message (usually empty)
> - `rid`: Request ID
> - `words_query_record`:
>   - `info`: Additional info (currently empty)
>   - `words_source`: Words source ("sug")
>   - `query_id`: Query ID (usually empty)
> - `extra`:
>   - `now`: Server timestamp
>   - `logid`: Log ID
>   - `fatal_item_ids`: List of fatal item IDs (usually empty)
>   - `search_request_id`: Search request ID (usually empty)
> - `log_pb`:
>   - `impr_id`: Impression ID (for logging)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词，如 '游戏' / Keyword, e.g., 'game' | 游戏 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-discuss-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_discuss_search`

- 摘要：获取讨论搜索/Fetch discussion search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_discuss_search_api_v1_douyin_search_fetch_discuss_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中讨论区/问答内容的搜索结果。
> - 支持关键词、排序方式、发布时间、内容类型等筛选条件。
>
> ### 备注:
> - 此接口专注于讨论区内容搜索（如问答讨论视频），不包含其他类型的内容。
> - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
> - 返回内容包括视频信息、作者信息、播放信息、互动数据、话题标签等。
>
> ### 参数:
> - keyword: 搜索关键词，例如 "出国留学"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>   - `0`: 综合排序
>   - `1`: 最多点赞
>   - `2`: 最新发布
> - publish_time: 发布时间筛选
>   - `0`: 不限
>   - `1`: 最近一天
>   - `7`: 最近一周
>   - `180`: 最近半年
> - filter_duration: 视频时长筛选
>   - `0`: 不限
>   - `0-1`: 1 分钟以内
>   - `1-5`: 1-5 分钟
>   - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>   - `0`: 不限
>   - `1`: 视频
>   - `2`: 图片
>   - `3`: 文章
> - search_id: 搜索ID（分页时使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "出国留学",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `data`: 搜索结果列表
>   - `type`: 结果类型（一般为 `1`）
>   - `aweme_info`: 视频信息
>     - `aweme_id`: 视频ID
>     - `desc`: 视频描述内容
>     - `author`: 作者信息
>       - `uid`: 用户唯一ID
>       - `nickname`: 用户昵称
>       - `is_verified`: 是否认证用户
>       - `region`: 用户地区
>       - `avatar_thumb.url_list`: 缩略头像列表
>       - `avatar_medium.url_list`: 中等尺寸头像列表
>       - `avatar_larger.url_list`: 高清头像列表
>     - `video`: 视频播放与封面信息
>       - `play_addr.url_list`: 播放地址列表
>       - `cover.url_list`: 视频封面列表
>       - `dynamic_cover.url_list`: 动态封面列表
>       - `origin_cover.url_list`: 原始封面列表
>       - `width`: 视频宽度（像素）
>       - `height`: 视频高度（像素）
>       - `ratio`: 视频分辨率比例（如540p）
>       - `duration`: 视频时长（毫秒）
>       - `download_addr.url_list`: 带水印下载地址
>     - `statistics`: 视频数据
>       - `comment_count`: 评论数
>       - `digg_count`: 点赞数
>       - `share_count`: 分享数
>       - `play_count`: 播放次数
>       - `collect_count`: 收藏次数
>     - `cha_list`: 话题标签
>       - `cha_name`: 标签名称
>       - `share_url`: 标签分享链接
>     - `music`: 音乐信息
>       - `id_str`: 音乐ID
>       - `title`: 音乐标题
>       - `author`: 音乐作者昵称
>       - `play_url.url_list`: 音乐播放链接列表
>     - `status`: 视频状态
>       - `is_delete`: 是否被删除
>       - `is_private`: 是否设为私密
>       - `allow_share`: 是否允许分享
>       - `allow_comment`: 是否允许评论
>     - `share_url`: 视频外部分享链接
>
> # [English]
> ### Purpose:
> - Fetch discussion/Q&A search results from Douyin App.
> - Supports filtering by keyword, sort type, publish time, content type, etc.
>
> ### Notes:
> - This API focuses on discussion and Q&A content, not including other content types.
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - The response includes video details, author info, playback info, statistics, hashtags, etc.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "study abroad"
> - cursor: Pagination cursor (0 for first page, use the last response cursor for subsequent pages)
> - sort_type: Sorting method
>   - `0`: Comprehensive
>   - `1`: Most likes
>   - `2`: Latest
> - publish_time: Publish time filter
>   - `0`: Unlimited
>   - `1`: Last day
>   - `7`: Last week
>   - `180`: Last half year
> - filter_duration: Video duration filter
>   - `0`: Unlimited
>   - `0-1`: Within 1 minute
>   - `1-5`: 1 to 5 minutes
>   - `5-10000`: More than 5 minutes
> - content_type: Content type filter
>   - `0`: Unlimited
>   - `1`: Video
>   - `2`: Picture
>   - `3`: Article
> - search_id: Search ID used for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "study abroad",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `data`: List of search result items
>   - `type`: Result type (usually `1`)
>   - `aweme_info`: Video information
>     - `aweme_id`: Video ID
>     - `desc`: Description
>     - `author`:
>       - `uid`: User ID
>       - `nickname`: User nickname
>       - `is_verified`: Verified user or not
>       - `region`: User region
>       - `avatar_thumb.url_list`: Thumbnail avatar URLs
>       - `avatar_medium.url_list`: Medium avatar URLs
>       - `avatar_larger.url_list`: Large avatar URLs
>     - `video`:
>       - `play_addr.url_list`: Video playback URLs
>       - `cover.url_list`: Video cover URLs
>       - `dynamic_cover.url_list`: Dynamic cover URLs
>       - `origin_cover.url_list`: Original cover URLs
>       - `width`: Width in pixels
>       - `height`: Height in pixels
>       - `ratio`: Resolution ratio (e.g., 540p)
>       - `duration`: Duration in milliseconds
>       - `download_addr.url_list`: Download URLs with watermark
>     - `statistics`:
>       - `comment_count`: Number of comments
>       - `digg_count`: Number of likes
>       - `share_count`: Number of shares
>       - `play_count`: Number of plays
>       - `collect_count`: Number of collections
>     - `cha_list`:
>       - `cha_name`: Hashtag name
>       - `share_url`: Hashtag share link
>     - `music`:
>       - `id_str`: Music ID
>       - `title`: Music title
>       - `author`: Music creator name
>       - `play_url.url_list`: List of music playback URLs
>     - `status`:
>       - `is_delete`: Whether deleted
>       - `is_private`: Whether private
>       - `allow_share`: Allow sharing
>       - `allow_comment`: Allow commenting
>     - `share_url`: External video share link

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-experience-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_experience_search`

- 摘要：获取经验搜索/Fetch experience search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_experience_search_api_v1_douyin_search_fetch_experience_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中经验（知识/教程）内容的搜索结果。
> - 支持通过关键词检索，与经验类内容（如攻略、教程、分享等）相关的视频信息。
>
> ### 备注:
> - 此接口专注于经验类内容，不包含其他类型的内容。
> - 初次请求时，`cursor` 应传 0，`search_id` 传空字符串，翻页时使用上次响应返回的 cursor 和 search_id。
> - 返回的结果中包含视频详情、作者信息、背景音乐、话题标签、播放地址、互动数据等。
>
> ### 参数:
> - keyword: 搜索关键词，例如 "游戏攻略"
> - cursor: 翻页游标，首次请求传 0
> - sort_type: 排序方式
>   - `0`: 综合排序
>   - `1`: 最多点赞
>   - `2`: 最新发布
> - publish_time: 发布时间筛选
>   - `0`: 不限
>   - `1`: 最近一天
>   - `7`: 最近一周
>   - `180`: 最近半年
> - filter_duration: 视频时长筛选
>   - `0`: 不限
>   - `0-1`: 1分钟以内
>   - `1-5`: 1-5分钟
>   - `5-10000`: 5分钟以上
> - content_type: 内容类型筛选（通常固定为视频）
> - search_id: 分页查询时需要传上次响应返回的 `search_id`
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "游戏攻略",
>     "cursor": 0,
>     "sort_type": 0,
>     "publish_time": 0,
>     "filter_duration": 0,
>     "content_type": 1,
>     "search_id": ""
> }
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - business_data: 搜索结果业务数据列表
>   - data_id: 数据块ID
>   - type: 数据类型（如 999 表示内容列表）
>   - data:
>     - height: 显示区域高度
>     - aweme_list: 视频列表
>       - aweme_id: 视频ID
>       - desc: 视频描述内容
>       - create_time: 视频发布时间（时间戳）
>       - author: 作者信息
>         - uid: 作者UID
>         - nickname: 作者昵称
>         - avatar_thumb.url_list: 作者头像缩略图
>         - is_verified: 是否是认证账号
>         - follower_count: 粉丝数
>       - music: 背景音乐信息
>         - id_str: 音乐ID
>         - title: 音乐标题
>         - author: 音乐作者昵称
>       - cha_list: 关联的话题标签列表
>         - cha_name: 话题名称
>       - video: 视频播放信息
>         - play_addr.url_list: 视频播放地址列表
>         - cover.url_list: 视频封面图地址
>         - width: 视频宽度
>         - height: 视频高度
>         - duration: 视频时长（单位毫秒）
>       - statistics: 视频互动数据
>         - digg_count: 点赞数
>         - comment_count: 评论数
>         - share_count: 分享数
>         - play_count: 播放次数
>       - status: 视频状态信息
>         - is_delete: 是否已删除
>         - is_private: 是否私密
>       - share_url: 视频外部分享链接
>
> # [English]
> ### Purpose:
> - Fetch experience (knowledge/tutorial) content search results from Douyin App.
> - Retrieves video results related to knowledge sharing, tutorials, or tips based on the input keyword.
>
> ### Notes:
> - This API focuses on experience-related videos and does not include other content types.
> - Set `cursor` to 0 and `search_id` to an empty string for the first request; for pagination, use the previous cursor and search_id.
> - The response includes rich information such as video details, author profile, background music, hashtags, video URLs, and engagement statistics.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "gaming guide"
> - cursor: Pagination cursor (0 for first page)
> - sort_type: Sorting method
>   - `0`: Comprehensive
>   - `1`: Most likes
>   - `2`: Latest
> - publish_time: Publish time filter
>   - `0`: Unlimited
>   - `1`: Last day
>   - `7`: Last week
>   - `180`: Last half year
> - filter_duration: Video duration filter
>   - `0`: Unlimited
>   - `0-1`: Within 1 minute
>   - `1-5`: 1 to 5 minutes
>   - `5-10000`: More than 5 minutes
> - content_type: Content type filter (usually fixed to video)
> - search_id: Search ID for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "gaming guide",
>     "cursor": 0,
>     "sort_type": 0,
>     "publish_time": 0,
>     "filter_duration": 0,
>     "content_type": 1,
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - business_data: List of business data blocks
>   - data_id: Data block ID
>   - type: Data type (e.g., 999 for content list)
>   - data:
>     - height: Display height
>     - aweme_list: List of videos
>       - aweme_id: Video ID
>       - desc: Video description
>       - create_time: Creation timestamp
>       - author: Author profile
>         - uid: User ID
>         - nickname: User nickname
>         - avatar_thumb.url_list: Thumbnail avatar URLs
>         - is_verified: Whether the author is verified
>         - follower_count: Number of followers
>       - music: Background music information
>         - id_str: Music ID
>         - title: Music title
>         - author: Music author's name
>       - cha_list: Associated hashtags
>         - cha_name: Hashtag name
>       - video: Video playback info
>         - play_addr.url_list: List of video play URLs
>         - cover.url_list: List of video cover image URLs
>         - width: Video width
>         - height: Video height
>         - duration: Video duration in milliseconds
>       - statistics: Video engagement data
>         - digg_count: Number of likes
>         - comment_count: Number of comments
>         - share_count: Number of shares
>         - play_count: Number of plays
>       - status: Video status information
>         - is_delete: Whether the video was deleted
>         - is_private: Whether the video is private
>       - share_url: External share link of the video

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-general-search-v1"></a>
### `POST /api/u1/v1/douyin/search/fetch_general_search_v1`

- 摘要：获取综合搜索 V1/Fetch general search V1
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_v1_api_v1_douyin_search_fetch_general_search_v1_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中综合搜索栏的搜索结果（非单独视频搜索）。
> - 支持关键词、排序方式、发布时间、视频时长、内容类型等筛选条件。
> - 支持翻页查询，通过 `cursor`、`search_id` 和 `backtrace` 分页。
>
> ### 备注:
> - 初次请求时 `cursor` 传入 0，`search_id` 和 `backtrace` 传空字符串。
> - 翻页时需从上一次响应中获取 `cursor`、`search_id` 和 `backtrace` 字段值。
> - 返回的内容包含视频、作者、话题标签、播放信息、音乐、互动数据等丰富信息。
>
> ### 参数:
> - keyword: 搜索关键词，如 "猫咪"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（首次请求传空，翻页时从上次响应获取）
> - backtrace: 翻页回溯标识（首次请求传空，翻页时从上次响应获取）
>
> ### 请求体示例：
> ```json
> payload = {
>   "keyword": "猫咪",
>   "cursor": 0,
>   "sort_type": "0",
>   "publish_time": "0",
>   "filter_duration": "0",
>   "content_type": "0",
>   "search_id": "",
>   "backtrace": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `data`: 搜索结果列表
> - `type`: 结果类型（通常为 `1`）
> - `aweme_info`: 视频详细信息
> - `aweme_id`: 视频ID
> - `desc`: 视频描述内容
> - `author`: 作者信息
>   - `uid`: 用户唯一ID
>   - `nickname`: 用户昵称
>   - `is_verified`: 是否认证用户（True=已认证，False=未认证）
>   - `region`: 用户地区，如 "CN"
>   - `avatar_thumb.url_list`: 缩略头像地址列表
>   - `avatar_medium.url_list`: 中等尺寸头像地址列表
>   - `avatar_larger.url_list`: 高清头像地址列表
> - `music`: 背景音乐信息
>   - `id_str`: 音乐ID
>   - `title`: 音乐标题，如"原创声音"
>   - `author`: 音乐作者昵称
>   - `play_url.url_list`: 音乐播放地址列表
> - `cha_list`: 关联话题标签列表
>   - `cha_name`: 话题名（例如 "#猫宝宝"）
>   - `share_url`: 话题分享链接
> - `video`: 视频播放与封面信息
>   - `play_addr.url_list`: 视频播放地址列表
>   - `cover.url_list`: 视频封面地址列表
>   - `dynamic_cover.url_list`: 动态封面地址列表
>   - `origin_cover.url_list`: 原始封面地址列表
>   - `width`: 视频宽度（像素）
>   - `height`: 视频高度（像素）
>   - `ratio`: 视频分辨率比例（如540p）
>   - `duration`: 视频时长（单位：毫秒）
>   - `download_addr.url_list`: 带水印下载地址
> - `statistics`: 视频统计信息
>   - `comment_count`: 评论数
>   - `digg_count`: 点赞数
>   - `share_count`: 分享数
>   - `play_count`: 播放次数
>   - `collect_count`: 收藏次数
> - `status`: 视频发布状态
>   - `is_delete`: 是否被删除
>   - `is_private`: 是否设为私密
>   - `allow_share`: 是否允许分享
>   - `allow_comment`: 是否允许评论
> - `share_url`: 视频外部分享链接
>
> # [English]
> ### Purpose:
> - Fetch search results from Douyin App's general search tab (not standalone video search).
> - Supports filtering by keyword, sort type, publish time, video duration, and content type.
> - Supports pagination through `cursor`, `search_id`, and `backtrace`.
>
> ### Notes:
> - Set `cursor` to 0, `search_id` and `backtrace` to empty strings for the first request.
> - For pagination, obtain `cursor`, `search_id`, and `backtrace` values from the previous response.
> - The response contains rich information including video details, author info, music, hashtags, playback info, and interaction metrics.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "cat"
> - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent pages)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Within 1 minute
>     - `1-5`: 1 to 5 minutes
>     - `5-10000`: More than 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Picture
>     - `3`: Article
> - search_id: Search ID (empty for first request, obtained from previous response for pagination)
> - backtrace: Backtrace identifier (empty for first request, obtained from previous response for pagination)
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "cat",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": "",
>     "backtrace": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `data`: List of search result items
> - `type`: Result type (usually `1`)
> - `aweme_info`: Video detailed information
> - `aweme_id`: Video ID
> - `desc`: Video description
> - `author`:
>   - `uid`: Author's user ID
>   - `nickname`: Author's nickname
>   - `is_verified`: Whether the author is verified
>   - `region`: Author's region
>   - `avatar_thumb.url_list`: List of thumbnail avatar URLs
>   - `avatar_medium.url_list`: List of medium size avatar URLs
>   - `avatar_larger.url_list`: List of large size avatar URLs
> - `music`:
>   - `id_str`: Music ID
>   - `title`: Music title
>   - `author`: Music creator's name
>   - `play_url.url_list`: List of music play URLs
> - `cha_list`:
>   - `cha_name`: Hashtag name
>   - `share_url`: Hashtag share URL
> - `video`:
>   - `play_addr.url_list`: List of video play URLs
>   - `cover.url_list`: List of cover image URLs
>   - `dynamic_cover.url_list`: List of dynamic cover URLs
>   - `origin_cover.url_list`: List of original cover URLs
>   - `width`: Video width (pixels)
>   - `height`: Video height (pixels)
>   - `ratio`: Resolution ratio (e.g., 540p)
>   - `duration`: Duration in milliseconds
>   - `download_addr.url_list`: List of video download URLs
> - `statistics`:
>   - `comment_count`: Number of comments
>   - `digg_count`: Number of likes
>   - `share_count`: Number of shares
>   - `play_count`: Number of plays
>   - `collect_count`: Number of collects
> - `status`:
>   - `is_delete`: Whether the video is deleted
>   - `is_private`: Whether the video is private
>   - `allow_share`: Whether sharing is allowed
>   - `allow_comment`: Whether commenting is allowed
> - `share_url`: External share link

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-general-search-v2"></a>
### `POST /api/u1/v1/douyin/search/fetch_general_search_v2`

- 摘要：获取综合搜索 V2/Fetch general search V2
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_v2_api_v1_douyin_search_fetch_general_search_v2_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中综合搜索栏的搜索结果（非单独视频搜索）。
> - 此接口稳定性可能不如 V1版本，作为备用接口。
> - 支持关键词、排序方式、发布时间、视频时长、内容类型等筛选条件。
> - 支持翻页查询，通过 `cursor`、`search_id` 和 `backtrace` 分页。
>
> ### 备注:
> - 初次请求时 `cursor` 传入 0，`search_id` 和 `backtrace` 传空字符串。
> - 翻页时需从上一次响应中获取 `cursor`、`search_id` 和 `backtrace` 字段值。
> - 返回的内容包含视频、作者、话题标签、播放信息、音乐、互动数据等丰富信息。
>
> ### 参数:
> - keyword: 搜索关键词，如 "猫咪"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（首次请求传空，翻页时从上次响应获取）
> - backtrace: 翻页回溯标识（首次请求传空，翻页时从上次响应获取）
>
> ### 请求体示例：
> ```json
> payload = {
>   "keyword": "猫咪",
>   "cursor": 0,
>   "sort_type": "0",
>   "publish_time": "0",
>   "filter_duration": "0",
>   "content_type": "0",
>   "search_id": "",
>   "backtrace": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `data`: 搜索结果列表
> - `type`: 结果类型（通常为 `1`）
> - `aweme_info`: 视频详细信息
> - `aweme_id`: 视频ID
> - `desc`: 视频描述内容
> - `author`: 作者信息
>   - `uid`: 用户唯一ID
>   - `nickname`: 用户昵称
>   - `is_verified`: 是否认证用户（True=已认证，False=未认证）
>   - `region`: 用户地区，如 "CN"
>   - `avatar_thumb.url_list`: 缩略头像地址列表
>   - `avatar_medium.url_list`: 中等尺寸头像地址列表
>   - `avatar_larger.url_list`: 高清头像地址列表
> - `music`: 背景音乐信息
>   - `id_str`: 音乐ID
>   - `title`: 音乐标题，如"原创声音"
>   - `author`: 音乐作者昵称
>   - `play_url.url_list`: 音乐播放地址列表
> - `cha_list`: 关联话题标签列表
>   - `cha_name`: 话题名（例如 "#猫宝宝"）
>   - `share_url`: 话题分享链接
> - `video`: 视频播放与封面信息
>   - `play_addr.url_list`: 视频播放地址列表
>   - `cover.url_list`: 视频封面地址列表
>   - `dynamic_cover.url_list`: 动态封面地址列表
>   - `origin_cover.url_list`: 原始封面地址列表
>   - `width`: 视频宽度（像素）
>   - `height`: 视频高度（像素）
>   - `ratio`: 视频分辨率比例（如540p）
>   - `duration`: 视频时长（单位：毫秒）
>   - `download_addr.url_list`: 带水印下载地址
> - `statistics`: 视频统计信息
>   - `comment_count`: 评论数
>   - `digg_count`: 点赞数
>   - `share_count`: 分享数
>   - `play_count`: 播放次数
>   - `collect_count`: 收藏次数
> - `status`: 视频发布状态
>   - `is_delete`: 是否被删除
>   - `is_private`: 是否设为私密
>   - `allow_share`: 是否允许分享
>   - `allow_comment`: 是否允许评论
> - `share_url`: 视频外部分享链接
>
> # [English]
> ### Purpose:
> - Fetch search results from Douyin App's general search tab (not standalone video search).
> - This API may be less stable than V1, serving as a backup.
> - Supports filtering by keyword, sort type, publish time, video duration, and content type.
> - Supports pagination through `cursor`, `search_id`, and `backtrace`.
>
> ### Notes:
> - Set `cursor` to 0, `search_id` and `backtrace` to empty strings for the first request.
> - For pagination, obtain `cursor`, `search_id`, and `backtrace` values from the previous response.
> - The response contains rich information including video details, author info, music, hashtags, playback info, and interaction metrics.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "cat"
> - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent pages)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Within 1 minute
>     - `1-5`: 1 to 5 minutes
>     - `5-10000`: More than 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Picture
>     - `3`: Article
> - search_id: Search ID (empty for first request, obtained from previous response for pagination)
> - backtrace: Backtrace identifier (empty for first request, obtained from previous response for pagination)
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "cat",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": "",
>     "backtrace": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `data`: List of search result items
> - `type`: Result type (usually `1`)
> - `aweme_info`: Video detailed information
> - `aweme_id`: Video ID
> - `desc`: Video description
> - `author`:
>   - `uid`: Author's user ID
>   - `nickname`: Author's nickname
>   - `is_verified`: Whether the author is verified
>   - `region`: Author's region
>   - `avatar_thumb.url_list`: List of thumbnail avatar URLs
>   - `avatar_medium.url_list`: List of medium size avatar URLs
>   - `avatar_larger.url_list`: List of large size avatar URLs
> - `music`:
>   - `id_str`: Music ID
>   - `title`: Music title
>   - `author`: Music creator's name
>   - `play_url.url_list`: List of music play URLs
> - `cha_list`:
>   - `cha_name`: Hashtag name
>   - `share_url`: Hashtag share URL
> - `video`:
>   - `play_addr.url_list`: List of video play URLs
>   - `cover.url_list`: List of cover image URLs
>   - `dynamic_cover.url_list`: List of dynamic cover URLs
>   - `origin_cover.url_list`: List of original cover URLs
>   - `width`: Video width (pixels)
>   - `height`: Video height (pixels)
>   - `ratio`: Resolution ratio (e.g., 540p)
>   - `duration`: Duration in milliseconds
>   - `download_addr.url_list`: List of video download URLs
> - `statistics`:
>   - `comment_count`: Number of comments
>   - `digg_count`: Number of likes
>   - `share_count`: Number of shares
>   - `play_count`: Number of plays
>   - `collect_count`: Number of collects
> - `status`:
>   - `is_delete`: Whether the video is deleted
>   - `is_private`: Whether the video is private
>   - `allow_share`: Whether sharing is allowed
>   - `allow_comment`: Whether commenting is allowed
> - `share_url`: External share link

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-general-search-v3"></a>
### `POST /api/u1/v1/douyin/search/fetch_general_search_v3`

- 摘要：获取综合搜索 V3/Fetch general search V3
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_v3_api_v1_douyin_search_fetch_general_search_v3_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 综合搜索结果（V3版，数据更全）。
> - 支持关键词、排序方式、发布时间、时长、内容类型等筛选。
> - 支持翻页查询，通过 `cursor`、`search_id` 和 `backtrace` 进行分页。
>
> ### 备注:
> - 初次请求时 `cursor` 传 0，`search_id` 和 `backtrace` 传空字符串。
> - 翻页时需从上一次响应中获取 `cursor`、`search_id` 和 `backtrace` 字段值。
> - 返回数据极为详细，包括视频、作者、音乐、话题、播放源、互动统计等信息。
>
> ### 参数:
> - keyword: 搜索关键词，如 "猫咪"
> - cursor: 翻页游标（首次请求传 0）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1分钟以内
>     - `1-5`: 1-5分钟
>     - `5-10000`: 5分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（首次请求传空，翻页时从上次响应获取）
> - backtrace: 翻页回溯标识（首次请求传空，翻页时从上次响应获取）
>
> ### 请求体示例：
> ```json
> payload = {
>   "keyword": "猫咪",
>   "cursor": 0,
>   "sort_type": "0",
>   "publish_time": "0",
>   "filter_duration": "0",
>   "content_type": "0",
>   "search_id": "",
>   "backtrace": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `status_code`: 响应状态码（0为成功）
> - `data[]`: 搜索结果列表
>   - `type`: 结果类型（通常为 `1`）
>   - `aweme_info`: 视频详细信息
>     - 基本信息:
>       - `aweme_id`: 视频ID
>       - `desc`: 视频描述
>       - `create_time`: 发布时间（时间戳）
>     - 作者信息 (`author`):
>       - `uid`: 用户ID
>       - `nickname`: 昵称
>       - `short_id`: 用户短ID
>       - `signature`: 用户签名
>       - `region`: 地区，如 "CN"
>       - `is_verified`: 是否认证
>       - `avatar_thumb.url_list`: 缩略头像
>       - `avatar_medium.url_list`: 中等尺寸头像
>       - `avatar_larger.url_list`: 高清头像
>     - 音乐信息 (`music`):
>       - `id_str`: 音乐ID
>       - `title`: 音乐标题
>       - `author`: 音乐作者
>       - `play_url.url_list`: 音乐播放链接
>       - `duration`: 音乐时长（秒）
>       - `cover_hd.url_list`: 高清封面图
>     - 话题标签 (`cha_list[]`):
>       - `cha_name`: 话题名
>       - `share_url`: 分享链接
>     - 视频播放信息 (`video`):
>       - `play_addr.url_list`: 视频播放链接
>       - `cover.url_list`: 封面图片
>       - `dynamic_cover.url_list`: 动态封面
>       - `origin_cover.url_list`: 原始封面
>       - `duration`: 视频时长（毫秒）
>       - `ratio`: 分辨率比例（如 "720p"）
>       - `bit_rate[]`: 多清晰度播放源
>         - `gear_name`: 清晰度名称（如 "adapt_540_2"）
>         - `bit_rate`: 码率
>         - `play_addr.url_list`: 对应播放链接
>     - 互动统计 (`statistics`):
>       - `comment_count`: 评论数
>       - `digg_count`: 点赞数
>       - `share_count`: 分享数
>       - `play_count`: 播放数
>     - 视频状态 (`status`):
>       - `is_delete`: 是否删除
>       - `is_private`: 是否私密
>       - `allow_share`: 是否允许分享
>       - `allow_comment`: 是否允许评论
>     - 其他字段:
>       - `share_url`: 视频分享链接
>       - `user_digged`: 是否已点赞（0=未点赞，1=已点赞）
>
> # [English]
> ### Purpose:
> - Fetch Douyin App general search results (V3 version, more comprehensive data).
> - Supports filtering by keyword, sort type, publish time, video duration, and content type.
> - Supports pagination via `cursor`, `search_id`, and `backtrace`.
>
> ### Notes:
> - Set `cursor` to 0, `search_id` and `backtrace` to empty strings for the first request.
> - For pagination, obtain `cursor`, `search_id`, and `backtrace` values from the previous response.
> - The response is rich, including video, author, music, hashtags, multiple play sources, and statistics.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "cat"
> - cursor: Pagination cursor (0 for the first page)
> - sort_type: Sort type
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Within 1 minute
>     - `1-5`: 1 to 5 minutes
>     - `5-10000`: Over 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Picture
>     - `3`: Article
> - search_id: Search ID (empty for first request, obtained from previous response for pagination)
> - backtrace: Backtrace identifier (empty for first request, obtained from previous response for pagination)
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "cat",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": "",
>     "backtrace": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `status_code`: Response status code (0 means success)
> - `data[]`: List of search results
>   - `type`: Result type (usually `1`)
>   - `aweme_info`: Video details
>     - Basic Info:
>       - `aweme_id`: Video ID
>       - `desc`: Video description
>       - `create_time`: Publish timestamp
>     - Author (`author`):
>       - `uid`: User ID
>       - `nickname`: Nickname
>       - `short_id`: Short ID
>       - `signature`: Signature
>       - `region`: Region
>       - `is_verified`: Verified or not
>       - `avatar_thumb.url_list`: Thumbnail avatar
>       - `avatar_medium.url_list`: Medium avatar
>       - `avatar_larger.url_list`: Large avatar
>     - Music (`music`):
>       - `id_str`: Music ID
>       - `title`: Music title
>       - `author`: Music creator
>       - `play_url.url_list`: Music play URLs
>       - `duration`: Music duration (seconds)
>       - `cover_hd.url_list`: HD cover images
>     - Hashtags (`cha_list[]`):
>       - `cha_name`: Hashtag name
>       - `share_url`: Share URL
>     - Video (`video`):
>       - `play_addr.url_list`: Video play URLs
>       - `cover.url_list`: Cover images
>       - `dynamic_cover.url_list`: Dynamic cover
>       - `origin_cover.url_list`: Original cover
>       - `duration`: Duration in milliseconds
>       - `ratio`: Resolution (e.g., "720p")
>       - `bit_rate[]`: Multiple quality sources
>         - `gear_name`: Gear name
>         - `bit_rate`: Bit rate
>         - `play_addr.url_list`: Play URLs
>     - Statistics (`statistics`):
>       - `comment_count`: Number of comments
>       - `digg_count`: Number of likes
>       - `share_count`: Number of shares
>       - `play_count`: Number of plays
>     - Status (`status`):
>       - `is_delete`: Whether deleted
>       - `is_private`: Whether private
>       - `allow_share`: Allow sharing or not
>       - `allow_comment`: Allow commenting or not
>     - Other fields:
>       - `share_url`: External share URL
>       - `user_digged`: Whether user liked (0=No, 1=Yes)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-image-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_image_search`

- 摘要：获取图片搜索/Fetch image search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_image_search_api_v1_douyin_search_fetch_image_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中图片内容搜索的结果。
> - 主要返回带有多张图片的帖子（图片合集）。
>
> ### 备注:
> - 仅返回图片类型的内容，适用于图片展示类应用场景。
> - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
> - 翻页时使用上一次响应中的 `cursor` 和 `search_id`。
>
> ### 参数:
> - keyword: 搜索关键词，如 "猫咪"
> - cursor: 翻页游标（首次请求传0）
> - sort_type: 排序方式
>   - `0`: 综合排序
>   - `1`: 最多点赞
>   - `2`: 最新发布
> - publish_time: 发布时间筛选
>   - `0`: 不限
>   - `1`: 最近一天
>   - `7`: 最近一周
>   - `180`: 最近半年
> - filter_duration: 视频时长筛选
>   - `0`: 不限
> - content_type: 内容类型（固定传 2 表示图片内容）
> - search_id: 搜索ID（翻页使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "猫咪",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "2",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `cursor`: 下一页游标
> - `has_more`: 是否还有更多数据（1=有，0=无）
> - `data[]`: 图片内容列表
>   - `aweme_info`:
>     - `aweme_id`: 内容ID
>     - `desc`: 帖子描述文字
>     - `create_time`: 创建时间戳
>     - `author`:
>       - `uid`: 作者ID
>       - `nickname`: 昵称
>       - `is_verified`: 是否认证
>       - `avatar_thumb.url_list`: 缩略头像URL列表
>       - `avatar_medium.url_list`: 中等头像URL列表
>       - `avatar_larger.url_list`: 高清头像URL列表
>     - `image_post_info`:
>       - `images[]`: 图片列表
>         - `url_list`: 图片地址数组（通常包含webp/jpg）
>         - `width`: 图片宽度（像素）
>         - `height`: 图片高度（像素）
>     - `statistics`:
>       - `comment_count`: 评论数
>       - `digg_count`: 点赞数
>       - `share_count`: 分享数
>       - `play_count`: 播放数
>       - `collect_count`: 收藏数
>     - `status`:
>       - `is_delete`: 是否删除
>       - `is_private`: 是否私密
>     - `share_url`: 外部分享链接
>
> - `extra`:
>   - `now`: 当前服务器时间戳
>   - `logid`: 请求日志ID
>   - `search_request_id`: 搜索请求ID
>
> # [English]
> ### Purpose:
> - Fetch image-based search results from Douyin App.
> - Mainly returns posts containing image collections.
>
> ### Notes:
> - Only image posts are returned. Suitable for gallery-style applications.
> - For the first request, set `cursor` to 0 and `search_id` to an empty string.
> - For pagination, use the `cursor` and `search_id` from the last response.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "cat"
> - cursor: Pagination cursor (0 for first request)
> - sort_type: Sorting method
>   - `0`: Comprehensive
>   - `1`: Most likes
>   - `2`: Latest
> - publish_time: Publish time filter
>   - `0`: Unlimited
>   - `1`: Last day
>   - `7`: Last week
>   - `180`: Last half year
> - filter_duration: Video duration filter
>   - `0`: Unlimited
> - content_type: Content type (Fixed to 2 for images)
> - search_id: Search ID for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "cat",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "2",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `cursor`: Cursor for next page
> - `has_more`: Whether there are more results (1=Yes, 0=No)
> - `data[]`: List of image posts
>   - `aweme_info`:
>     - `aweme_id`: Content ID
>     - `desc`: Post description
>     - `create_time`: Creation timestamp
>     - `author`:
>       - `uid`: Author ID
>       - `nickname`: Nickname
>       - `is_verified`: Verified status
>       - `avatar_thumb.url_list`: Thumbnail avatar URLs
>       - `avatar_medium.url_list`: Medium avatar URLs
>       - `avatar_larger.url_list`: High-res avatar URLs
>     - `image_post_info`:
>       - `images[]`: List of images
>         - `url_list`: Image URLs (webp/jpg)
>         - `width`: Width (pixels)
>         - `height`: Height (pixels)
>     - `statistics`:
>       - `comment_count`: Comment count
>       - `digg_count`: Like count
>       - `share_count`: Share count
>       - `play_count`: Play count
>       - `collect_count`: Collect count
>     - `status`:
>       - `is_delete`: Whether deleted
>       - `is_private`: Whether private
>     - `share_url`: Shareable external link
> - `extra`:
>   - `now`: Current server timestamp
>   - `logid`: Request log ID
>   - `search_request_id`: Search session ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-image-search-v3"></a>
### `POST /api/u1/v1/douyin/search/fetch_image_search_v3`

- 摘要：获取图文搜索 V3/Fetch image-text search V3
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_image_search_v3_api_v1_douyin_search_fetch_image_search_v3_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中图文内容搜索的结果。
> - 返回带有多张图片的帖子（aweme_type=68），适用于图文展示类应用场景。
>
> ### 备注:
> - 该接口与 `fetch_image_search` 使用不同的数据源，返回结果可能有所差异。
> - 推荐用于需要高质量图文内容的场景。
> - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
> - 翻页请求时，使用上一次响应返回的 `cursor` 和 `search_id`。
> - 每页返回约 12 条数据。
>
> ### 参数:
> - keyword: 搜索关键词，如 "美食"
> - cursor: 翻页游标（首次请求传 0）
> - search_id: 搜索ID（翻页时使用上次响应中的值）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "美食",
>     "cursor": 0,
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `status_code`: 状态码（0=成功）
> - `business_data[]`: 图文内容列表
>   - `data`:
>     - `aweme_list[]`: 内容列表
>       - `aweme_id`: 内容ID
>       - `aweme_type`: 内容类型（68=图文）
>       - `desc`: 帖子描述文字
>       - `create_time`: 创建时间戳
>       - `author`:
>         - `uid`: 作者ID
>         - `nickname`: 昵称
>         - `avatar_thumb.url_list`: 缩略头像URL列表
>       - `image_post_info`:
>         - `images[]`: 图片列表
>           - `url_list`: 图片地址数组
>           - `width`: 图片宽度（像素）
>           - `height`: 图片高度（像素）
>       - `statistics`:
>         - `comment_count`: 评论数
>         - `digg_count`: 点赞数
>         - `share_count`: 分享数
>         - `collect_count`: 收藏数
>       - `share_url`: 外部分享链接
> - `extra`:
>   - `now`: 当前服务器时间戳
>   - `logid`: 请求日志ID
>
> ---
>
> # [English]
> ### Purpose:
> - Fetch image-text content search results from Douyin App.
> - Returns posts with multiple images (aweme_type=68), suitable for gallery-style applications.
>
> ### Notes:
> - This endpoint uses a different data source than `fetch_image_search`, results may vary.
> - Recommended for scenarios requiring high-quality image-text content.
> - For the first request, set `cursor` to 0 and `search_id` to an empty string.
> - For pagination, use the `cursor` and `search_id` from the last response.
> - Returns approximately 12 items per page.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "food"
> - cursor: Pagination cursor (0 for first request)
> - search_id: Search ID for pagination (use value from previous response)
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "food",
>     "cursor": 0,
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `status_code`: Status code (0=success)
> - `business_data[]`: Image-text content list
>   - `data`:
>     - `aweme_list[]`: Content list
>       - `aweme_id`: Content ID
>       - `aweme_type`: Content type (68=image-text)
>       - `desc`: Post description
>       - `create_time`: Creation timestamp
>       - `author`:
>         - `uid`: Author ID
>         - `nickname`: Nickname
>         - `avatar_thumb.url_list`: Thumbnail avatar URLs
>       - `image_post_info`:
>         - `images[]`: Image list
>           - `url_list`: Image URLs array
>           - `width`: Width (pixels)
>           - `height`: Height (pixels)
>       - `statistics`:
>         - `comment_count`: Comment count
>         - `digg_count`: Like count
>         - `share_count`: Share count
>         - `collect_count`: Collect count
>       - `share_url`: Shareable external link
> - `extra`:
>   - `now`: Current server timestamp
>   - `logid`: Request log ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword*`:string, `cursor`:integer, `search_id`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 是 | 搜索关键词/Search keyword | 无 | 无 | 无 |
| cursor | integer | 否 | 翻页游标/Pagination cursor | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID/Search ID for pagination | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-live-search-v1"></a>
### `POST /api/u1/v1/douyin/search/fetch_live_search_v1`

- 摘要：获取直播搜索 V1/Fetch live search V1
- 能力：搜索 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_search_v1_api_v1_douyin_search_fetch_live_search_v1_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中直播搜索结果。
> - 返回正在直播的房间信息，包括主播资料、直播间封面、观众人数、拉流地址等。
>
> ### 备注:
> - 仅返回直播类型内容。
> - 初次请求时 `cursor` 传0，`search_id` 传空字符串。
> - 翻页请求时，使用上一次响应返回的 `cursor` 和 `search_id`。
>
> ### 参数:
> - keyword: 搜索关键词，如 "游戏"
> - cursor: 翻页游标（首次请求传0）
> - sort_type: 排序方式
>   - `0`: 综合排序
>   - `1`: 最多点赞
>   - `2`: 最新发布
> - publish_time: 发布时间筛选
>   - `0`: 不限
>   - `1`: 最近一天
>   - `7`: 最近一周
>   - `180`: 最近半年
> - filter_duration: 视频时长过滤
>   - `0`: 不限
> - content_type: 内容类型（固定传直播类型）
> - search_id: 搜索ID（翻页时使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "游戏",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "1",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `cursor`: 下一页游标
> - `has_more`: 是否有更多数据（1=有，0=无）
> - `data[]`: 直播房间列表
>   - `type`: 返回内容类型（固定为1）
>   - `lives`:
>     - `aweme_id`: 直播对应的内容ID
>     - `group_id`: 群组ID（与aweme_id类似，可用于跳转）
>     - `author`:
>       - `uid`: 主播用户ID
>       - `nickname`: 主播昵称
>       - `short_id`: 主播短ID
>       - `avatar_thumb.url_list`: 缩略头像URL列表
>       - `avatar_medium.url_list`: 中等头像URL列表
>       - `avatar_larger.url_list`: 高清头像URL列表
>       - `room_id`: 当前直播间ID
>       - `room_cover.url_list`: 直播封面图URL列表
>     - `video`:
>       - `tags[]`: 直播标签（如“游戏”、“聊天”等）
>         - `title`: 标签标题
>         - `url.url_list`: 标签图标URL列表
>     - `rawdata`: 直播详细数据（结构化JSON字符串，可解析得到以下信息）
>       - `title`: 直播标题
>       - `user_count`: 当前在线观众数
>       - `stream_url`: 拉流信息
>         - `flv_pull_url`: 拉流地址列表（不同清晰度）
>           - `SD1`: 标清
>           - `SD2`: 高清
>           - `HD1`: 超清
>           - `FULL_HD1`: 蓝光
>           - `ORIGION`: 原画
>         - `hls_pull_url`: HLS播放地址（部分直播间可能存在）
>       - `cover.url_list`: 直播间封面图
>       - `size`: 分辨率（如1920x1080）
>       - `stats.total_user`: 在线观众数
>
> - `extra`:
>   - `now`: 当前服务器时间戳
>   - `logid`: 请求日志ID
>   - `search_request_id`: 搜索请求唯一ID
>
> # [English]
> ### Purpose:
> - Fetch live stream search results from Douyin App.
> - Returns information about live rooms including streamer profile, cover image, viewer count, and stream URLs.
>
> ### Notes:
> - Only live streaming content is returned.
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - Use the last response's `cursor` and `search_id` for pagination.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "games"
> - cursor: Pagination cursor (0 for first request)
> - sort_type: Sorting method
>   - `0`: Comprehensive
>   - `1`: Most likes
>   - `2`: Latest
> - publish_time: Publish time filter
>   - `0`: Unlimited
>   - `1`: Last day
>   - `7`: Last week
>   - `180`: Last half year
> - filter_duration: Video duration filter
>   - `0`: Unlimited
> - content_type: Content type (fixed for live stream)
> - search_id: Search ID for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "games",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "1",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `cursor`: Cursor for next page
> - `has_more`: Whether there are more results (1=Yes, 0=No)
> - `data[]`: List of live stream rooms
>   - `type`: Result type (fixed to 1)
>   - `lives`:
>     - `aweme_id`: Related content ID
>     - `group_id`: Group ID
>     - `author`:
>       - `uid`: Streamer's user ID
>       - `nickname`: Streamer's nickname
>       - `short_id`: Streamer's short ID
>       - `avatar_thumb.url_list`: Thumbnail avatar URLs
>       - `avatar_medium.url_list`: Medium avatar URLs
>       - `avatar_larger.url_list`: Large avatar URLs
>       - `room_id`: Room ID
>       - `room_cover.url_list`: Room cover image URLs
>     - `video`:
>       - `tags[]`: Live tags (e.g., "Gaming", "Chatting")
>         - `title`: Tag title
>         - `url.url_list`: Tag icon URLs
>     - `rawdata`: Raw live room data (as JSON string)
>       - `title`: Live title
>       - `user_count`: Current viewer count
>       - `stream_url`: Stream URLs
>         - `flv_pull_url`: FLV stream URLs by resolution
>         - `hls_pull_url`: HLS stream URL (optional)
>       - `cover.url_list`: Room cover image
>       - `size`: Resolution (e.g., 1920x1080)
>       - `stats.total_user`: Viewer count
> - `extra`:
>   - `now`: Current server timestamp
>   - `logid`: Request log ID
>   - `search_request_id`: Unique search session ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-multi-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_multi_search`

- 摘要：获取多重搜索/Fetch multi-type search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_search_api_v1_douyin_search_fetch_multi_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中多种类型（视频、用户、音乐、话题等）的综合搜索结果。
>
> ### 备注:
> - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
> - 返回内容丰富，适合搭建搜索聚合页、推荐页等场景。
>
> ### 参数:
> - keyword: 搜索关键词，如 "人工智能"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（分页时使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "人工智能",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `cursor`: 下一页翻页游标
> - `has_more`: 是否还有更多数据（1=有，0=无）
> - `business_data[]`: 搜索结果列表
>   - `data_id`: 结果数据编号
>   - `type`: 结果类型
>     - `1`: 视频（aweme_info）
>     - `2`: 用户（user_info）
>     - `4`: 音乐（music_info）
>     - `6`: 话题（cha_info）
>   - `data`: 具体数据内容，按type类型解析
>     - 如果 type = 1（视频）:
>       - `aweme_info`:
>         - `aweme_id`: 视频ID
>         - `desc`: 视频描述
>         - `author`: 作者信息
>           - `uid`: 用户ID
>           - `nickname`: 用户昵称
>           - `avatar_thumb.url_list`: 小头像
>           - `is_verified`: 是否认证
>           - `region`: 地区
>         - `music`: 音乐信息
>           - `id_str`: 音乐ID
>           - `title`: 音乐标题
>         - `video`: 视频播放与封面信息
>           - `play_addr.url_list`: 播放地址
>           - `cover.url_list`: 封面
>           - `duration`: 视频时长（毫秒）
>         - `statistics`:
>           - `comment_count`: 评论数
>           - `digg_count`: 点赞数
>           - `share_count`: 分享数
>           - `play_count`: 播放数
>         - `status`:
>           - `is_delete`: 是否被删除
>           - `is_private`: 是否私密
>         - `share_url`: 视频外链
>     - 如果 type = 2（用户）:
>       - `user_info`:
>         - `uid`: 用户ID
>         - `nickname`: 用户昵称
>         - `signature`: 个人签名
>         - `follower_count`: 粉丝数
>         - `avatar_thumb.url_list`: 小头像
>         - `region`: 地区
>         - `is_verified`: 是否认证
>     - 如果 type = 4（音乐）:
>       - `music_info`:
>         - `id_str`: 音乐ID
>         - `title`: 音乐标题
>         - `author`: 作者名
>         - `play_url.url_list`: 播放地址
>     - 如果 type = 6（话题）:
>       - `cha_info`:
>         - `cha_name`: 话题名
>         - `desc`: 话题描述
>         - `share_url`: 话题分享链接
>         - `user_count`: 话题参与人数
>         - `view_count`: 话题浏览次数
>
> - `extra`:
>   - `now`: 当前服务器时间戳
>   - `logid`: 请求日志ID
>
> # [English]
> ### Purpose:
> - Fetch multiple types of search results (videos, users, music, hashtags, etc.) from Douyin App.
>
> ### Notes:
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - Suitable for search aggregation pages, discovery modules, and recommendations.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "Artificial Intelligence"
> - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent pages)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Within 1 minute
>     - `1-5`: 1 to 5 minutes
>     - `5-10000`: More than 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Picture
>     - `3`: Article
> - search_id: Search ID used for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "Artificial Intelligence",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `cursor`: Cursor for the next page
> - `has_more`: Whether there are more results (1=Yes, 0=No)
> - `business_data[]`: List of search result items
>   - `data_id`: Data ID
>   - `type`: Result type
>     - `1`: Video (aweme_info)
>     - `2`: User (user_info)
>     - `4`: Music (music_info)
>     - `6`: Hashtag (cha_info)
>   - `data`: Content depending on `type`
>     - if type = 1 (video):
>       - `aweme_info`: Detailed video info
>     - if type = 2 (user):
>       - `user_info`: Detailed user info
>     - if type = 4 (music):
>       - `music_info`: Music details
>     - if type = 6 (hashtag):
>       - `cha_info`: Hashtag details
>
> - `extra`:
>   - `now`: Current server timestamp
>   - `logid`: Request log ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-music-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_music_search`

- 摘要：获取音乐搜索/Fetch music search
- 能力：搜索 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_search_api_v1_douyin_search_fetch_music_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中音乐内容的搜索结果。
> - 支持关键词、排序方式、筛选条件等。
>
> ### 备注:
> - 本接口专注于音乐类内容搜索，不包含其他类型内容。
> - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
> - 返回内容包含音乐基本信息、作者信息、封面、播放地址、标签等。
>
> ### 参数:
> - keyword: 搜索关键词，例如 "游戏背景音乐"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（分页时使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "游戏背景音乐",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `music`: 音乐结果列表
>   - `id_str`: 音乐ID（字符串格式）
>   - `title`: 音乐标题
>   - `author`: 音乐作者昵称
>   - `album`: 所属专辑（如果有）
>   - `play_url.url_list`: 音乐播放地址列表
>   - `duration`: 音乐时长（秒）
>   - `cover_thumb.url_list`: 缩略封面图片列表
>   - `cover_medium.url_list`: 中尺寸封面图片列表
>   - `cover_large.url_list`: 高清封面图片列表
>   - `user_count`: 使用该音乐的作品数量
>   - `is_original`: 是否原创音乐
>   - `is_commerce_music`: 是否为商业授权音乐
>   - `lyric_url`: 歌词文件链接（如果有）
>   - `strong_beat_url.url_list`: 音乐节奏点文件链接
>   - `tags`: 音乐标签
>     - 如：主题（如游戏、Vlog）、情绪（如Funny）、风格（如8-bit, Electronic）
>   - `artists`: 音乐关联的创作者列表（如果有）
>     - `artist_name`: 艺人昵称
>     - `uid`: 艺人UID
>   - `cover_color_hsv`: 封面主色调HSV值
>   - `can_background_play`: 是否支持后台播放
>
> # [English]
> ### Purpose:
> - Fetch music content search results from Douyin App.
> - Supports filtering by keyword, sort type, etc.
>
> ### Notes:
> - This API focuses on music content search, excluding other types.
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - Response includes music basic info, artist info, covers, play URLs, tags, etc.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "game background music"
> - cursor: Pagination cursor (0 for first request)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Under 1 minute
>     - `1-5`: 1 to 5 minutes
>     - `5-10000`: Over 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Image
>     - `3`: Article
> - search_id: Search ID for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "game background music",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `music`: List of music search results
>   - `id_str`: Music ID (as string)
>   - `title`: Music title
>   - `author`: Music author's nickname
>   - `album`: Album name (if any)
>   - `play_url.url_list`: List of music play URLs
>   - `duration`: Duration in seconds
>   - `cover_thumb.url_list`: List of thumbnail cover URLs
>   - `cover_medium.url_list`: List of medium-sized cover URLs
>   - `cover_large.url_list`: List of large-sized cover URLs
>   - `user_count`: Number of videos using this music
>   - `is_original`: Whether it is original music
>   - `is_commerce_music`: Whether it is commercial music
>   - `lyric_url`: Lyrics file URL (if available)
>   - `strong_beat_url.url_list`: Beat timing file URLs
>   - `tags`: Music tags
>     - Themes (e.g., Game, Vlog), Moods (e.g., Funny), Genres (e.g., 8-bit, Electronic)
>   - `artists`: List of associated artists (if any)
>     - `artist_name`: Artist name
>     - `uid`: Artist UID
>   - `cover_color_hsv`: Dominant HSV color of the cover
>   - `can_background_play`: Whether background playback is supported

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-school-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_school_search`

- 摘要：获取学校搜索/Fetch school search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_school_search_api_v1_douyin_search_fetch_school_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中学校信息的搜索结果。
> - 根据关键词返回学校名称列表，常用于用户设置学校资料、兴趣推荐等场景。
>
> ### 备注:
> - 本接口专注于学校信息搜索，仅返回学校的名称字段。
> - 初次请求时 `cursor` 应传 0，分页时使用上一次返回的 `cursor`。
> - 本接口响应体较简单，适合快速检索学校数据。
>
> ### 参数:
> - keyword: 搜索关键词，如学校名称 "北京大学"、地区名 "北京"
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "北京大学"
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `schools[]`: 学校列表
>   - `name`: 学校名称（如 "北京大学"、"北京四中"）
> - `extra`:
>   - `now`: 当前服务器时间戳（毫秒）
>   - `logid`: 请求日志ID
>   - `fatal_item_ids`: 错误项目ID列表（通常为空）
> - `log_pb`:
>   - `impr_id`: 曝光追踪ID（用于链路追踪）
> - `status_code`: 状态码（0=成功）
> - `status_msg`: 状态信息（通常为空）
>
> # [English]
> ### Purpose:
> - Fetch school information search results from Douyin App.
> - Returns a list of school names based on the input keyword, useful for user profile settings, school recommendations, etc.
>
> ### Notes:
> - This API focuses on school information search, and only returns school names.
> - Set `cursor` to 0 for the first request; for pagination, use the cursor from the last response.
> - The response structure is simple and lightweight for fast lookup.
>
> ### Parameters:
> - keyword: Search keyword, e.g., school name "Peking University" or city "Beijing"
>
> ### Example Request Body:
> ```json
> payload = {
>     "keyword": "Peking University"
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `schools[]`: List of schools
>   - `name`: School name (e.g., "Peking University", "Beijing No.4 High School")
> - `extra`:
>   - `now`: Server timestamp in milliseconds
>   - `logid`: Log ID for request tracing
>   - `fatal_item_ids`: List of fatal item IDs (usually empty)
> - `log_pb`:
>   - `impr_id`: Impression ID for tracking
> - `status_code`: Status code (0=success)
> - `status_msg`: Status message (usually empty)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词，如学校名称或所在地区 / Keyword, such as school name or location | 北京 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-search-suggest"></a>
### `POST /api/u1/v1/douyin/search/fetch_search_suggest`

- 摘要：获取搜索关键词推荐/Fetch search keyword suggestions
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_suggest_api_v1_douyin_search_fetch_search_suggest_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中搜索关键词的联想推荐结果。
> - 根据用户输入的关键词，返回相关搜索词建议，用于提升搜索体验。
>
> ### 备注:
> - 通常用于实现搜索框实时推荐（如输入时下拉补全）。
> - 返回的推荐词经过抖音推荐系统内部打分排序。
>
> ### 参数:
> - keyword: 输入的关键词，如 "人工智能"
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "人工智能"
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `status_code`: 状态码（0 表示成功）
> - `status_msg`: 返回信息（一般为空）
> - `rid`: 请求ID
> - `sug_list[]`: 搜索建议列表
>   - `content`: 推荐的搜索关键词（如 "人工智能ai软件免费版下载"）
>   - `sug_type`: 建议类型（一般为空，预留字段）
>   - `pos[]`: 匹配位置（标记关键词在原搜索词中的起止位置）
>     - `begin`: 开始字符位置
>     - `end`: 结束字符位置
>   - `word_record`:
>     - `group_id`: 推荐词组ID
>     - `words_position`: 在本次推荐列表中的位置
>     - `words_content`: 词内容（同 `content`）
>     - `words_source`: 词来源（通常为 "sug"）
>   - `extra_info`:
>     - `client_server_extra`: 附加配置信息（JSON字符串）
>     - `poi_id`: 关联POI ID（通常为空）
>     - `search_params`: 搜索参数（带内部推荐得分）
> - `words_query_record`:
>   - `info`: 附加信息（通常为空）
>   - `words_source`: 推荐来源
>   - `query_id`: 推荐查询ID
> - `extra`:
>   - `now`: 当前服务器时间戳（毫秒）
>   - `logid`: 日志ID
>   - `fatal_item_ids`: 错误项列表（通常为空）
>   - `search_request_id`: 搜索请求ID（通常为空）
> - `log_pb`:
>   - `impr_id`: 曝光日志ID
> - `time_cost`:
>   - `stream_inner`: 内部处理耗时（毫秒）
>   - `server_engine_cost`: 搜索引擎处理耗时（毫秒）
> - `cache_conf`:
>   - `enable`: 是否命中缓存（布尔值）
>
> # [English]
> ### Purpose:
> - Fetch keyword suggestion results from Douyin App.
> - Based on the user's input, returns a list of recommended search keywords to improve search experience.
>
> ### Notes:
> - Typically used for real-time keyword suggestions in the search box.
> - The returned suggestions are scored and sorted internally by Douyin's recommendation system.
>
> ### Parameters:
> - keyword: Input keyword, e.g., "Artificial Intelligence"
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "Artificial Intelligence"
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `status_code`: Status code (0 means success)
> - `status_msg`: Response message (usually empty)
> - `rid`: Request ID
> - `sug_list[]`: List of suggested search keywords
>   - `content`: Suggested keyword (e.g., "AI software free download")
>   - `sug_type`: Suggestion type (usually empty, reserved field)
>   - `pos[]`: Position marking
>     - `begin`: Begin character position
>     - `end`: End character position
>   - `word_record`:
>     - `group_id`: Suggestion group ID
>     - `words_position`: Position in the current suggestion list
>     - `words_content`: The word content (same as `content`)
>     - `words_source`: Word source (typically "sug")
>   - `extra_info`:
>     - `client_server_extra`: Extra client-server config (JSON string)
>     - `poi_id`: Related POI ID (usually empty)
>     - `search_params`: Search parameters (with recommendation scores)
> - `words_query_record`:
>   - `info`: Additional info (usually empty)
>   - `words_source`: Source of suggestions
>   - `query_id`: Suggestion query ID
> - `extra`:
>   - `now`: Current server timestamp (milliseconds)
>   - `logid`: Log ID
>   - `fatal_item_ids`: List of fatal error items (usually empty)
>   - `search_request_id`: Search request ID (usually empty)
> - `log_pb`:
>   - `impr_id`: Impression log ID
> - `time_cost`:
>   - `stream_inner`: Internal stream processing time (milliseconds)
>   - `server_engine_cost`: Server search engine processing time (milliseconds)
> - `cache_conf`:
>   - `enable`: Whether cache was hit (boolean)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 需要联想的关键词/The keyword to be suggested | 人工智能 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-user-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_user_search`

- 摘要：获取用户搜索/Fetch user search
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_api_v1_douyin_search_fetch_user_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中根据关键词搜索到的用户列表。
> - 支持通过粉丝数量、用户类型进行筛选查询。
>
> ### 备注:
> - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
> - 返回的数据仅包含「用户信息」，不包括视频、话题、音乐等内容。
>
> ### 参数:
> - keyword: 搜索关键词，如 "人工智能"
> - cursor: 翻页游标（首次请求传0）
> - douyin_user_fans: 粉丝数量筛选
>   - 为空: 不限
>   - "0_1k": 1000以下
>   - "1k_1w": 1000到1万
>   - "1w_10w": 1万到10万
>   - "10w_100w": 10万到100万
>   - "100w_": 100万以上
> - douyin_user_type: 用户类型筛选
>   - 为空: 不限
>   - "common_user": 普通用户
>   - "enterprise_user": 企业认证用户
>   - "personal_user": 个人认证用户
> - search_id: 搜索ID（翻页使用）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "人工智能",
>     "cursor": 0,
>     "douyin_user_fans": "",
>     "douyin_user_type": "",
>     "search_id": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `cursor`: 下一页游标
> - `has_more`: 是否还有更多数据（1=有，0=无）
> - `user_list[]`: 用户列表
>   - `user_info`:
>     - `uid`: 用户ID
>     - `nickname`: 用户昵称
>     - `gender`: 性别（0=未知，1=男，2=女）
>     - `unique_id`: 抖音号
>     - `sec_uid`: 安全UID
>     - `signature`: 个性签名
>     - `follower_count`: 粉丝数量
>     - `avatar_thumb.url_list`: 小头像地址
>     - `avatar_medium.url_list`: 中头像地址
>     - `avatar_larger.url_list`: 大头像地址
>     - `follow_status`: 是否已关注
>     - `live_status`: 是否正在直播（0=否，1=是）
>     - `enterprise_verify_reason`: 企业认证信息（若有）
>     - `versatile_display`: 抖音号展示文案（例如"抖音号：xxx"）
> - `extra`:
>   - `now`: 当前服务器时间戳
>   - `logid`: 请求日志ID
>   - `search_request_id`: 搜索请求ID
>
> # [English]
> ### Purpose:
> - Fetch a list of users from Douyin App based on search keywords.
> - Supports filtering by fan count and user type.
>
> ### Notes:
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - Only user information is returned. No videos, music, or hashtags.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "AI"
> - cursor: Pagination cursor (0 for first page)
> - douyin_user_fans: Fan count filter
>   - Empty: No limit
>   - "0_1k": Below 1000 fans
>   - "1k_1w": 1,000 to 10,000 fans
>   - "1w_10w": 10,000 to 100,000 fans
>   - "10w_100w": 100,000 to 1,000,000 fans
>   - "100w_": Above 1,000,000 fans
> - douyin_user_type: User type filter
>   - Empty: No limit
>   - "common_user": Regular user
>   - "enterprise_user": Enterprise-verified user
>   - "personal_user": Personal-verified user
> - search_id: Search session ID for pagination
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "AI",
>     "cursor": 0,
>     "douyin_user_fans": "",
>     "douyin_user_type": "",
>     "search_id": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `cursor`: Cursor for next page
> - `has_more`: Whether more data is available (1=Yes, 0=No)
> - `user_list[]`: List of users
>   - `user_info`:
>     - `uid`: User ID
>     - `nickname`: Nickname
>     - `gender`: Gender (0=Unknown, 1=Male, 2=Female)
>     - `unique_id`: Douyin ID
>     - `sec_uid`: Secured UID
>     - `signature`: Personal bio
>     - `follower_count`: Number of followers
>     - `avatar_thumb.url_list`: List of thumbnail avatar URLs
>     - `avatar_medium.url_list`: List of medium avatar URLs
>     - `avatar_larger.url_list`: List of large avatar URLs
>     - `follow_status`: Whether followed
>     - `live_status`: Whether live
>     - `enterprise_verify_reason`: Enterprise verification info (if any)
>     - `versatile_display`: Display text (e.g., "Douyin ID: xxx")
> - `extra`:
>   - `now`: Current server timestamp
>   - `logid`: Request log ID
>   - `search_request_id`: Search request ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `douyin_user_fans`:string, `douyin_user_type`:string, `search_id`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| douyin_user_fans | string | 否 | 粉丝数过滤：空=不限 0_1k=1千以下 1k_5k=1千到5千 5k_10k=5千到1万 10k_100k=1万到10万 100k_1M=10万到100万 1M_=100万以上 / Fans filter: empty=No limit, 0_1k=Under 1k, etc. | 无 | 无 | 无 |
| douyin_user_type | string | 否 | 用户类型过滤：空=不限 300=创作者 900=小店 700=音乐人 800=明星 / User type filter: empty=No limit, 300=Creator, 900=Shop, 700=Musician, 800=Celebrity | 无 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-user-search-v2"></a>
### `POST /api/u1/v1/douyin/search/fetch_user_search_v2`

- 摘要：获取用户搜索 V2/Fetch user search V2
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_v2_api_v1_douyin_search_fetch_user_search_v2_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中根据关键词搜索到的用户列表。
> - 不支持粉丝数量、用户类型筛选查询。
>
> ### 备注:
> - 初次请求 `cursor` 传 0。
> - 返回的数据仅包含「用户信息」，不包括视频、话题、音乐等内容。
>
> ### 参数:
> - keyword: 搜索关键词，如 "人工智能"
> - cursor: 翻页游标（首次请求传0）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "人工智能",
>     "cursor": 0
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `cursor`: 下一页游标
> - `has_more`: 是否还有更多数据（1=有，0=无）
> - `user_list[]`: 用户列表
>   - `user_info`:
>     - `uid`: 用户ID
>     - `nickname`: 用户昵称
>     - `gender`: 性别（0=未知，1=男，2=女）
>     - `unique_id`: 抖音号
>     - `sec_uid`: 安全UID
>     - `signature`: 个性签名
>     - `follower_count`: 粉丝数量
>     - `avatar_thumb.url_list`: 小头像地址
>     - `avatar_medium.url_list`: 中头像地址
>     - `avatar_larger.url_list`: 大头像地址
>     - `follow_status`: 是否已关注
>     - `live_status`: 是否正在直播（0=否，1=是）
>     - `enterprise_verify_reason`: 企业认证信息（若有）
>     - `versatile_display`: 抖音号展示文案（例如"抖音号：xxx"）
> - `extra`:
>   - `now`: 当前服务器时间戳
>   - `logid`: 请求日志ID
>   - `search_request_id`: 搜索请求ID
>
> # [English]
> ### Purpose:
> - Fetch a list of users from Douyin App based on search keywords.
> - Supports filtering by fan count and user type.
>
> ### Notes:
> - Set `cursor` to 0.
> - Only user information is returned. No videos, music, or hashtags.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "AI"
> - cursor: Pagination cursor (0 for first page)
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "AI",
>     "cursor": 0
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `cursor`: Cursor for next page
> - `has_more`: Whether more data is available (1=Yes, 0=No)
> - `user_list[]`: List of users
>   - `user_info`:
>     - `uid`: User ID
>     - `nickname`: Nickname
>     - `gender`: Gender (0=Unknown, 1=Male, 2=Female)
>     - `unique_id`: Douyin ID
>     - `sec_uid`: Secured UID
>     - `signature`: Personal bio
>     - `follower_count`: Number of followers
>     - `avatar_thumb.url_list`: List of thumbnail avatar URLs
>     - `avatar_medium.url_list`: List of medium avatar URLs
>     - `avatar_larger.url_list`: List of large avatar URLs
>     - `follow_status`: Whether followed
>     - `live_status`: Whether live
>     - `enterprise_verify_reason`: Enterprise verification info (if any)
>     - `versatile_display`: Display text (e.g., "Douyin ID: xxx")
> - `extra`:
>   - `now`: Current server timestamp
>   - `logid`: Request log ID
>   - `search_request_id`: Search request ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-video-search-v1"></a>
### `POST /api/u1/v1/douyin/search/fetch_video_search_v1`

- 摘要：获取视频搜索 V1/Fetch video search V1
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_v1_api_v1_douyin_search_fetch_video_search_v1_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中通过关键词搜索到的视频内容。
> - 专注于视频内容的搜索结果，不包含其他类型。
>
> ### 备注:
> - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
> - 返回的视频包含作者信息、播放地址、封面、互动数据等。
> - 同时返回一组关键词推荐 (`guide_search_words`) 用于引导用户继续搜索。
>
> ### 参数:
> - keyword: 搜索关键词，例如 "人工智能"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（分页时使用，从上一次响应获取）
> - backtrace: 翻页回溯标识（分页时使用，从上一次响应获取）
>
> #### 请求体示例：
> ```json
> payload = {
>     "keyword": "人工智能",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": "",
>     "backtrace": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `status_code`: 响应状态码（0表示成功）
> - `cursor`: 下一页的游标
> - `has_more`: 是否还有更多数据（1=有，0=没有）
> - `data[]`: 搜索到的视频内容列表
>   - `type`: 结果类型（通常为 `1`）
>   - `aweme_info`: 视频详细信息
>     - 基本信息:
>       - `aweme_id`: 视频ID
>       - `desc`: 视频描述文字
>       - `create_time`: 发布时间（时间戳）
>     - 作者信息 (`author`):
>       - `uid`: 用户ID
>       - `nickname`: 昵称
>       - `is_verified`: 是否认证
>       - `region`: 地区，如 "CN"
>       - `avatar_thumb.url_list`: 缩略头像列表
>       - `follower_count`: 粉丝数
>       - `enterprise_verify_reason`: 企业认证信息（如"央视新闻"）
>     - 音乐信息 (`music`):
>       - `id_str`: 音乐ID
>       - `title`: 音乐标题
>       - `author`: 音乐作者
>       - `play_url.url_list`: 音乐播放链接
>     - 视频播放信息 (`video`):
>       - `play_addr.url_list`: 视频播放地址（高清）
>       - `cover.url_list`: 视频封面
>       - `dynamic_cover.url_list`: 动态封面
>       - `origin_cover.url_list`: 原始封面
>       - `ratio`: 视频分辨率，如 "720p"
>       - `duration`: 视频时长（单位：毫秒）
>       - `bit_rate[]`: 不同清晰度播放源
>         - `gear_name`: 清晰度名称（如"540_2_2"）
>         - `bit_rate`: 比特率
>         - `play_addr.url_list`: 对应播放地址
>     - 互动数据 (`statistics`):
>       - `comment_count`: 评论数
>       - `digg_count`: 点赞数
>       - `share_count`: 分享数
>       - `play_count`: 播放次数
>     - 视频状态 (`status`):
>       - `is_delete`: 是否删除
>       - `is_private`: 是否私密
>       - `allow_share`: 是否允许分享
>       - `allow_comment`: 是否允许评论
>     - 其他字段:
>       - `share_url`: 视频分享外链
>       - `user_digged`: 用户是否点赞（0=未点赞，1=已点赞）
>
> - `guide_search_words[]`: 推荐的搜索关键词
>   - `id`: 推荐词ID
>   - `word`: 推荐的关键词内容
>   - `type`: 推荐类型（通常为 `recom`）
>   - `query_id`: 推荐请求ID
>
> - `extra`:
>   - `now`: 当前服务器时间戳（毫秒）
>   - `logid`: 日志ID
>
> # [English]
> ### Purpose:
> - Fetch video content search results from Douyin App based on a keyword.
> - This API is focused on video search results only.
>
> ### Notes:
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - Each returned video includes rich details: author, video info, music, statistics, etc.
> - Also returns a set of suggested keywords (`guide_search_words`) for user guidance.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "Artificial Intelligence"
> - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent pages)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Within 1 minute
>     - `1-5`: 1 to 5 minutes
>     - `5-10000`: More than 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Picture
>     - `3`: Article
> - search_id: Search ID used for pagination(obtained from the last response)
> - backtrace: Backtrace identifier used for pagination(obtained from the last response)
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "Artificial Intelligence",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": "",
>     "backtrace": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `status_code`: Response status code (0 = success)
> - `cursor`: Cursor for the next page
> - `has_more`: Whether more data is available (1=Yes, 0=No)
> - `data[]`: List of video search results
>   - `type`: Result type (usually `1`)
>   - `aweme_info`: Detailed video information
>     - Basic info:
>       - `aweme_id`: Video ID
>       - `desc`: Description
>       - `create_time`: Publish timestamp
>     - Author (`author`):
>       - `uid`: User ID
>       - `nickname`: Nickname
>       - `is_verified`: Whether verified
>       - `region`: Region
>       - `avatar_thumb.url_list`: Thumbnail avatars
>       - `follower_count`: Follower count
>       - `enterprise_verify_reason`: Enterprise verification reason
>     - Music (`music`):
>       - `id_str`: Music ID
>       - `title`: Music title
>       - `author`: Music creator
>       - `play_url.url_list`: Music play URLs
>     - Video (`video`):
>       - `play_addr.url_list`: Play URLs
>       - `cover.url_list`: Cover images
>       - `dynamic_cover.url_list`: Dynamic covers
>       - `origin_cover.url_list`: Original covers
>       - `ratio`: Resolution, e.g., "720p"
>       - `duration`: Video duration (ms)
>       - `bit_rate[]`: Multiple resolution sources
>         - `gear_name`: Gear name
>         - `bit_rate`: Bit rate
>         - `play_addr.url_list`: Play URLs
>     - Statistics (`statistics`):
>       - `comment_count`: Number of comments
>       - `digg_count`: Number of likes
>       - `share_count`: Number of shares
>       - `play_count`: Number of plays
>     - Status (`status`):
>       - `is_delete`: Whether deleted
>       - `is_private`: Whether private
>       - `allow_share`: Whether sharing is allowed
>       - `allow_comment`: Whether commenting is allowed
>     - Other fields:
>       - `share_url`: External share link
>       - `user_digged`: Whether liked (0=No, 1=Yes)
>
> - `guide_search_words[]`: Suggested keywords
>   - `id`: Suggestion ID
>   - `word`: Suggested keyword
>   - `type`: Suggestion type (usually `recom`)
>   - `query_id`: Suggestion query ID
>
> - `extra`:
>   - `now`: Current server timestamp
>   - `logid`: Log ID

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-video-search-v2"></a>
### `POST /api/u1/v1/douyin/search/fetch_video_search_v2`

- 摘要：获取视频搜索 V2/Fetch video search V2
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_v2_api_v1_douyin_search_fetch_video_search_v2_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音 App 中通过关键词搜索到的视频内容（V2版本接口）。
> - 相较于 V1，返回字段更加详细，包括作者资料、视频多清晰度播放源、标签列表等。
>
> ### 备注:
> - 初次请求时 `cursor` 传入0，`search_id`传空字符串。
> - 返回的视频内容丰富，可用于推荐展示、内容抓取、智能分析等应用场景。
>
> ### 参数:
> - keyword: 搜索关键词，如 "机器人"
> - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
> - sort_type: 排序方式
>     - `0`: 综合排序
>     - `1`: 最多点赞
>     - `2`: 最新发布
> - publish_time: 发布时间筛选
>     - `0`: 不限
>     - `1`: 最近一天
>     - `7`: 最近一周
>     - `180`: 最近半年
> - filter_duration: 视频时长筛选
>     - `0`: 不限
>     - `0-1`: 1 分钟以内
>     - `1-5`: 1-5 分钟
>     - `5-10000`: 5 分钟以上
> - content_type: 内容类型筛选
>     - `0`: 不限
>     - `1`: 视频
>     - `2`: 图片
>     - `3`: 文章
> - search_id: 搜索ID（分页时使用，从上一次响应获取）
> - backtrace: 翻页回溯标识（分页时使用，从上一次响应获取）
>
> ### 请求体示例：
> ```json
> payload = {
>     "keyword": "机器人",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": "",
>     "backtrace": ""
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `business_data[]`: 搜索返回的数据列表
>   - `data_id`: 数据编号（字符串，如 "0"）
>   - `type`: 数据类型（1=视频）
>   - `data`:
>     - `type`: 同上（1）
>     - `aweme_info`: 视频详细信息
>       - 基础信息:
>         - `aweme_id`: 视频ID
>         - `desc`: 视频描述
>         - `create_time`: 发布时间（时间戳）
>       - 作者信息 (`author`):
>         - `uid`: 用户唯一ID
>         - `short_id`: 用户短ID
>         - `nickname`: 用户昵称
>         - `signature`: 个性签名
>         - `follower_count`: 粉丝数
>         - `is_verified`: 是否认证
>         - `region`: 地区，如 "CN"
>         - `avatar_thumb.url_list`: 小头像URL列表
>         - `avatar_medium.url_list`: 中头像URL列表
>         - `avatar_larger.url_list`: 大头像URL列表
>         - `enterprise_verify_reason`: 企业认证信息（如"店铺账号"）
>       - 背景音乐 (`music`):
>         - `id_str`: 音乐ID
>         - `title`: 音乐标题
>         - `author`: 音乐创作者昵称
>         - `play_url.url_list`: 音乐播放链接列表
>       - 视频播放信息 (`video`):
>         - `play_addr.url_list`: 播放地址列表（支持高清播放）
>         - `cover.url_list`: 封面图片列表
>         - `dynamic_cover.url_list`: 动态封面列表
>         - `origin_cover.url_list`: 原始封面列表
>         - `duration`: 时长（毫秒）
>         - `ratio`: 分辨率（如"720p"）
>         - `bit_rate[]`: 多码率播放信息
>           - `gear_name`: 清晰度名称（如"540_2_2"）
>           - `bit_rate`: 码率（单位bps）
>           - `play_addr.url_list`: 对应清晰度播放地址列表
>       - 标签列表 (`cha_list[]`):
>         - `cha_name`: 话题名（如 "#宇树科技"）
>         - `cid`: 话题ID
>         - `share_url`: 话题分享链接
>       - 统计信息 (`statistics`):
>         - `comment_count`: 评论数
>         - `digg_count`: 点赞数
>         - `share_count`: 分享数
>         - `play_count`: 播放次数
>         - `collect_count`: 收藏次数
>       - 状态信息 (`status`):
>         - `is_delete`: 是否被删除
>         - `is_private`: 是否私密
>         - `allow_share`: 是否允许分享
>         - `allow_comment`: 是否允许评论
>       - 其他字段:
>         - `share_url`: 视频外链
>         - `user_digged`: 当前用户是否点赞（0=否，1=是）
>
> - `cursor`: 翻页游标（用于下次请求）
> - `has_more`: 是否还有更多数据（1=有，0=无）
>
> # [English]
> ### Purpose:
> - Fetch video search results from Douyin App using V2 API version.
> - Compared to V1, returns more detailed information including author details, multi-resolution video sources, and hashtags.
>
> ### Notes:
> - Set `cursor` to 0 and `search_id` to an empty string for the first request.
> - The response contains rich video data, suitable for display, content scraping, or intelligent analysis.
>
> ### Parameters:
> - keyword: Search keyword, e.g., "robot"
> - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent pages)
> - sort_type: Sorting method
>     - `0`: Comprehensive
>     - `1`: Most likes
>     - `2`: Latest
> - publish_time: Publish time filter
>     - `0`: Unlimited
>     - `1`: Last day
>     - `7`: Last week
>     - `180`: Last half year
> - filter_duration: Video duration filter
>     - `0`: Unlimited
>     - `0-1`: Within 1 minute
>     - `1-5`: 1 to 5 minutes
>     - `5-10000`: More than 5 minutes
> - content_type: Content type filter
>     - `0`: Unlimited
>     - `1`: Video
>     - `2`: Picture
>     - `3`: Article
> - search_id: Search ID used for pagination(obtained from the last response)
> - backtrace: Backtrace identifier used for pagination(obtained from the last response)
>
> ### Request Body Example:
> ```json
> payload = {
>     "keyword": "robot",
>     "cursor": 0,
>     "sort_type": "0",
>     "publish_time": "0",
>     "filter_duration": "0",
>     "content_type": "0",
>     "search_id": "",
>     "backtrace": ""
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `business_data[]`: List of returned data items
>   - `data_id`: Data ID (string, e.g., "0")
>   - `type`: Data type (1=Video)
>   - `data`:
>     - `type`: Same as above (1)
>     - `aweme_info`: Detailed video information
>       - Basic Info:
>         - `aweme_id`: Video ID
>         - `desc`: Video description
>         - `create_time`: Creation timestamp
>       - Author Info (`author`):
>         - `uid`: Unique User ID
>         - `short_id`: Short ID
>         - `nickname`: Nickname
>         - `signature`: Bio
>         - `follower_count`: Follower count
>         - `is_verified`: Whether verified
>         - `region`: Region, e.g., "CN"
>         - `avatar_thumb.url_list`: Thumbnail avatar URLs
>         - `avatar_medium.url_list`: Medium avatar URLs
>         - `avatar_larger.url_list`: Large avatar URLs
>         - `enterprise_verify_reason`: Enterprise verification info
>       - Music (`music`):
>         - `id_str`: Music ID
>         - `title`: Music title
>         - `author`: Music creator nickname
>         - `play_url.url_list`: List of play URLs
>       - Video (`video`):
>         - `play_addr.url_list`: Play URLs (supports HD)
>         - `cover.url_list`: Cover images
>         - `dynamic_cover.url_list`: Dynamic covers
>         - `origin_cover.url_list`: Original covers
>         - `duration`: Duration (milliseconds)
>         - `ratio`: Resolution (e.g., "720p")
>         - `bit_rate[]`: Multiple bitrates
>           - `gear_name`: Gear name
>           - `bit_rate`: Bitrate (bps)
>           - `play_addr.url_list`: Play URLs
>       - Hashtags (`cha_list[]`):
>         - `cha_name`: Hashtag name (e.g., "#UnitreeRobot")
>         - `cid`: Hashtag ID
>         - `share_url`: Hashtag share link
>       - Statistics (`statistics`):
>         - `comment_count`: Number of comments
>         - `digg_count`: Number of likes
>         - `share_count`: Number of shares
>         - `play_count`: Number of plays
>         - `collect_count`: Number of collects
>       - Status (`status`):
>         - `is_delete`: Whether deleted
>         - `is_private`: Whether private
>         - `allow_share`: Whether sharing is allowed
>         - `allow_comment`: Whether commenting is allowed
>       - Other fields:
>         - `share_url`: Video external share link
>         - `user_digged`: Whether the user has liked (0=No, 1=Yes)
>
> - `cursor`: Cursor for next page
> - `has_more`: Whether more data is available (1=Yes, 0=No)

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `sort_type`:string, `publish_time`:string, `filter_duration`:string, `content_type`:string, `search_id`:string, `backtrace`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 关键词 / Keyword | 猫咪 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| sort_type | string | 否 | 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest | 0 | 无 | 无 |
| publish_time | string | 否 | 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last day, 7=Last week, 180=Last half year | 0 | 无 | 无 |
| filter_duration | string | 否 | 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter: 0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes | 0 | 无 | 无 |
| content_type | string | 否 | 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| backtrace | string | 否 | 翻页回溯标识，用于翻页，从上一次请求返回的响应中获取 / Backtrace for pagination, obtained from the last response | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-search-fetch-vision-search"></a>
### `POST /api/u1/v1/douyin/search/fetch_vision_search`

- 摘要：获取图像识别搜索/Fetch vision search (image-based search)
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_vision_search_api_v1_douyin_search_fetch_vision_search_post`

#### 说明

> # [中文]
> ### 用途:
> - 抖音APP图像识别搜索（以图搜图/视觉搜索）。
> - 通过图片进行视觉搜索，返回相似的视频/图文内容。
> - `image_uri` 可从抖音其他接口的返回数据中获取（如视频详情、搜索结果、用户主页等接口的图片uri字段）。
>
> ### 备注:
> - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
> - 翻页时需从上一次响应中获取 `cursor` 和 `search_id` 字段值。
> - `image_uri` 是必填参数，需要先通过抖音图片上传接口获取，或在单一视频接口中获取，其他途径如各类搜索接口返回的图片URI均可使用。
> - `detection` 表示图片中需要识别的区域，格式为 "x1,y1,x2,y2"，默认 "0.1,0.1,0.9,0.9" 表示全图。
>
> ### 参数:
> - image_uri: 图片URI，通过图片上传接口获取，或在单一视频接口中获取，其他途径如各类搜索接口返回的图片URI均可使用。（必填）
> - cursor: 翻页游标（首次请求传 0）
> - search_id: 搜索ID（首次请求传空，翻页时从上次响应获取）
> - search_source: 搜索来源
>     - `graphic_detail`: 图片详情页搜索（默认）
>     - `visual_normal_search`: 带关键词追加搜索（需要传入 user_query）
> - detection: 检测区域坐标，格式为 "x1,y1,x2,y2"
> - detection_index: 检测索引，默认 0
> - user_query: 搜索关键词，仅当 search_source="visual_normal_search" 时使用
> - aweme_id: 原视频ID，仅当 search_source="visual_normal_search" 时使用
>
> ### 请求体示例：
> 基础图片搜索：
> ```json
> payload = {
>     "image_uri": "20251221204239F0C21D7645F172B6085C",
>     "cursor": 0,
>     "search_id": "",
>     "search_source": "graphic_detail",
>     "detection": "0.1,0.1,0.9,0.9",
>     "detection_index": 0
> }
> ```
>
> 带关键词的追加搜索：
> ```json
> payload = {
>     "image_uri": "20251221204239F0C21D7645F172B6085C",
>     "cursor": 0,
>     "search_id": "2025122120452038252994F25A4BAEB043",
>     "search_source": "visual_normal_search",
>     "detection": "0.1,0.1,0.9,0.9",
>     "detection_index": 0,
>     "user_query": "游戏",
>     "aweme_id": "7523532488087817529"
> }
> ```
>
> ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
> - `status_code`: 响应状态码（0为成功）
> - `cursor`: 下一页游标
> - `has_more`: 是否还有更多数据（1=有，0=无）
> - `search_id`: 搜索ID，翻页时使用
> - `data[]`: 搜索结果列表
>   - `type`: 结果类型
>   - `aweme_info`: 视频/图文详细信息
>     - `aweme_id`: 视频ID
>     - `desc`: 视频描述
>     - `author`: 作者信息
>     - `video`: 视频播放信息
>     - `statistics`: 互动统计
>
> # [English]
> ### Purpose:
> - Douyin APP vision search (image-based search / reverse image search).
> - Search for similar videos/images using an image.
> - The `image_uri` can be obtained from other Douyin API responses (such as video details, search results, user profile, etc.), and used directly for vision search.
>
> ### Notes:
> - Set `cursor` to 0 and `search_id` to empty string for the first request.
> - For pagination, obtain `cursor` and `search_id` values from the previous response.
> - `image_uri` is a required parameter. It can be obtained from Douyin API responses that contain image information, such as video details API, general search API, user profile API, etc. These responses typically include image URIs that can be used directly for vision search.
> - `detection` represents the area to be recognized in the image, format "x1,y1,x2,y2", default "0.1,0.1,0.9,0.9" means the whole image.
>
> ### Parameters:
> - image_uri: Image URI obtained from other Douyin API responses (e.g., video details, search results, user profile) (required)
> - cursor: Pagination cursor (0 for the first page)
> - search_id: Search ID (empty for first request, obtained from previous response for pagination)
> - search_source: Search source
>     - `graphic_detail`: Image detail page search (default)
>     - `visual_normal_search`: Search with keyword append (requires user_query)
> - detection: Detection area coordinates, format "x1,y1,x2,y2"
> - detection_index: Detection index, default 0
> - user_query: Search keyword, only used when search_source="visual_normal_search"
> - aweme_id: Original video ID, only used when search_source="visual_normal_search"
>
> ### Request Body Example:
> Basic image search:
> ```json
> payload = {
>     "image_uri": "20251221204239F0C21D7645F172B6085C",
>     "cursor": 0,
>     "search_id": "",
>     "search_source": "graphic_detail",
>     "detection": "0.1,0.1,0.9,0.9",
>     "detection_index": 0
> }
> ```
>
> Search with keyword append:
> ```json
> payload = {
>     "image_uri": "20251221204239F0C21D7645F172B6085C",
>     "cursor": 0,
>     "search_id": "2025122120452038252994F25A4BAEB043",
>     "search_source": "visual_normal_search",
>     "detection": "0.1,0.1,0.9,0.9",
>     "detection_index": 0,
>     "user_query": "game",
>     "aweme_id": "7523532488087817529"
> }
> ```
>
> ### Response (common fields, actual response may contain more fields):
> - `status_code`: Response status code (0 means success)
> - `cursor`: Cursor for next page
> - `has_more`: Whether more data is available (1=Yes, 0=No)
> - `search_id`: Search ID for pagination
> - `data[]`: List of search results
>   - `type`: Result type
>   - `aweme_info`: Video/image post details
>     - `aweme_id`: Video ID
>     - `desc`: Video description
>     - `author`: Author information
>     - `video`: Video playback information
>     - `statistics`: Interaction statistics

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`image_uri*`:string, `cursor`:integer, `search_id`:string, `search_source`:string, `detection`:string, `detection_index`:integer, `user_query`:string, `aweme_id`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| image_uri | string | 是 | 图片URI，从抖音其他接口返回中获取（如视频详情、搜索结果、用户主页等接口的图片uri字段）/ Image URI obtained from other Douyin API responses (e.g., video details, search results, user profile - look for image uri fields) | 无 | 无 | 无 |
| cursor | integer | 否 | 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last response | 0 | 无 | 无 |
| search_id | string | 否 | 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last response | 无 | 无 | 无 |
| search_source | string | 否 | 搜索来源：graphic_detail=图片详情页搜索, visual_normal_search=带关键词追加搜索 / Search source: graphic_detail=Image detail page search, visual_normal_search=Search with keyword append | graphic_detail | 无 | 无 |
| detection | string | 否 | 检测区域坐标，格式为 x1,y1,x2,y2 / Detection area coordinates in format x1,y1,x2,y2 | 0.1,0.1,0.9,0.9 | 无 | 无 |
| detection_index | integer | 否 | 检测索引 / Detection index | 0 | 无 | 无 |
| user_query | string | 否 | 搜索关键词，仅当search_source=visual_normal_search时使用 / Search keyword, only used when search_source=visual_normal_search | 无 | 无 | 无 |
| aweme_id | string | 否 | 原视频ID，仅当search_source=visual_normal_search时使用 / Original video ID, only used when search_source=visual_normal_search | 无 | 无 | 无 |

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
