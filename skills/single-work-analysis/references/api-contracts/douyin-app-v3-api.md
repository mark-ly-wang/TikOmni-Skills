# Douyin-App-V3-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/douyin-app-v3-api.md`](../api-tags/douyin-app-v3-api.md)
- 当前契约文件：`api-contracts/douyin-app-v3-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`47`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(抖音-App-V3数据接口（当前最新版本）/Douyin-App-V3-API (Current latest version))**

## 路由契约

<a id="get-api-u1-v1-douyin-app-v3-add-video-play-count"></a>
### `GET /api/u1/v1/douyin/app/v3/add_video_play_count`

- 摘要：根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据视频ID来增加作品的播放数
> - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。
> - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。
> - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。
> - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。
> - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。
> ### 参数:
> - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
> - item_id: 作品id，别名为aweme_id
> - cookie: 可选，默认使用游客Cookie
> ### 返回:
> - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。
>
> # [English]
> ### Purpose:
> - Increase the number of plays of the work according to the video ID
> - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user, please pass it in the parameters.
> - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call.
> - This restriction is for the work, not for the interface. When browsing the work without logging in, using different IP browsers or browsing the work in the APP, the number of plays of the work will not increase.
> - You can carry the Cookie of the Douyin web page to request this interface, but it is not guaranteed to be effective and needs to be tested by yourself.
> - The above restrictions are based on test results, and the specific restrictions may vary, for reference only.
> ### Parameters:
> - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data interface.
> - item_id: Video id, alias aweme_id
> - cookie: Optional, use guest Cookie by default
> ### Return:
> - The current timestamp and status code. When the status code is 200, it means success, otherwise it is a failure. You can try to change another work id and call it again, or wait for a period of time and call it again.
>
> # [示例/Example]
> aweme_type = 0
> item_id = "7197598285882789120"
> cookie = None

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_type | query | integer | 是 | 作品类型/Video type | 无 | 0 | 无 |
| item_id | query | string | 是 | 作品id/Video id | 无 | 7197598285882789120 | 无 |
| cookie | query | string | 否 | 可选，默认使用游客Cookie/Optional, use guest Cookie by default | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-brand-hot-search-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list`

- 摘要：获取抖音品牌热榜分类数据/Get Douyin brand hot search list data
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音品牌热榜分类数据
> ### 返回:
> - 品牌热搜榜分类数据
>
> # [English]
> ### Purpose:
> - Get Douyin brand hot search category data
> ### Return:
> - Hot brand search category data
>
> # [示例/Example]
> pass

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-brand-hot-search-list-detail"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_brand_hot_search_list_detail`

- 摘要：获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data
- 能力：搜索 / 热点/榜单 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音品牌热榜具体分类数据
> ### 参数:
> - category_id: 分类id
> ### 返回:
> - 品牌热搜榜具体分类数据
>
> # [English]
> ### Purpose:
> - Get Douyin brand hot search list detail data
> ### Parameters:
> - category_id: Category id
> ### Return:
> - Hot brand search list detail data
>
> # [示例/Example]
> category_id = 10

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category_id | query | integer | 是 | 分类id/Category id | 无 | 10 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-general-search-result"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_general_search_result`

- 摘要：获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定关键词的综合搜索结果
> - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212773e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量，请保持默认，否则会出现BUG。
> - sort_type: 0:综合排序 1:最多点赞 2:最新发布
> - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年
> - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上
> - content_type: 0:不限 1:视频 2:图片 3:文章
> ### 返回:
> - 综合搜索结果
>
> # [English]
> ### Purpose:
> - Get comprehensive search results of specified keywords
> - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212773e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number Please keep the default, otherwise there will be BUG.
> - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
> - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year
> - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
> - content_type: 0: Unlimited 1: Video 2: Picture 3: Article
> ### Return:
> - Comprehensive search results
>
> # [示例/Example]
> keyword = "中华娘"
> offset = 0
> count = 20
> sort_type = "0"
> publish_time = "0"
> filter_duration = "0"
> content_type = "0"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| sort_type | query | string | 否 | 排序类型/Sort type | 0 | 无 | 无 |
| publish_time | query | string | 否 | 发布时间/Publish time | 0 | 无 | 无 |
| filter_duration | query | string | 否 | 时长/Duration | 0 | 无 | 无 |
| content_type | query | string | 否 | 内容类型/Content type | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-hashtag-detail"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_detail`

- 摘要：获取指定话题的详情数据/Get details of specified hashtag
- 能力：详情 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定话题的详情数据
> ### 参数:
> - ch_id: 话题id
> ### 返回:
> - 话题详情数据
>
> # [English]
> ### Purpose:
> - Get details of specified hashtag
> ### Parameters:
> - ch_id: Hashtag id
> ### Return:
> - Hashtag details data
>
> # [示例/Example]
> ch_id = 1575791821492238

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_id | query | integer | 是 | 话题id/Hashtag id | 无 | 1575791821492238 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-hashtag-search-result"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_search_result`

- 摘要：获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定关键词的话题搜索结果
> - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212794e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 话题搜索结果
>
> # [English]
> ### Purpose:
> - Get hashtag search results of specified keywords
> - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212794e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Hashtag search results
>
> # [示例/Example]
> keyword = "中华娘"
> offset = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-hashtag-video-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_hashtag_video_list`

- 摘要：获取指定话题的作品数据/Get video list of specified hashtag
- 能力：作品详情 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定话题的作品数据
> ### 参数:
> - ch_id: 话题id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - sort_type: 0:综合排序 1:最多点赞 2:最新发布
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 话题作品数据
>
> # [English]
> ### Purpose:
> - Get video list of specified hashtag
> ### Parameters:
> - ch_id: Hashtag id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Hashtag video list data
>
> # [示例/Example]
> ch_id = 1575791821492238
> cursor = 0
> sort_type = 0
> count = 10

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_id | query | string | 是 | 话题id/Hashtag id | 无 | 1575791821492238 | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| sort_type | query | integer | 否 | 排序类型/Sort type | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 10 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-hot-search-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_hot_search_list`

- 摘要：获取抖音热搜榜数据/Get Douyin hot search list data
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音热榜数据，包括：
>     - 热点榜
>     - 种草榜
>     - 娱乐榜
>     - 社会榜
>     - 挑战榜
> ### 参数:
> - board_type:
>     - 0: 热点榜（默认）
>     - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。
> - board_sub_type:
>     - 空字符串: 热点榜（默认）
>     - seeding: 种草榜
>     - 2: 娱乐榜
>     - 4: 社会榜
>     - hotspot_challenge: 挑战榜
> ### 返回:
> - 热搜榜数据
>
> # [English]
> ### Purpose:
> - Get Douyin hot search list data, including:
>     - Hot search list
>     - Seeding list
>     - Entertainment list
>     - Social list
>     - Challenge list
>
> ### Parameters:
> - board_type:
>     - 0: Hot search list (default)
>     - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type parameter.
> - board_sub_type:
>     - Empty string: Hot search list (default)
>     - seeding: Seeding list
>     - 2: Entertainment list
>     - 4: Social list
>     - hotspot_challenge: Challenge list
> ### Return:
> - Hot search list data
>
> # [示例/Example]
> - 获取热点榜数据
>     - board_type = 0
>     - board_sub_type = ""
> - 获取种草榜数据
>     - board_type = 2
>     - board_sub_type = "seeding"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| board_type | query | string | 否 | 榜单类型/Board type | 0 | 无 | 无 |
| board_sub_type | query | string | 否 | 榜单子类型/Board sub type | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-live-hot-search-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_live_hot_search_list`

- 摘要：获取抖音直播热搜榜数据/Get Douyin live hot search list data
- 能力：搜索 / 热点/榜单 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音直播热搜榜数据
> ### 返回:
> - 直播热搜榜数据
>
> # [English]
> ### Purpose:
> - Get Douyin live hot search list data
> ### Return:
> - Live hot search list data
>
> # [示例/Example]
> pass

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-live-search-result"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_live_search_result`

- 摘要：获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- 能力：搜索 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定关键词的直播搜索结果
> - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212789e0
> ### 参数:
> - keyword: 关键词
> - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 直播搜索结果
>
> # [English]
> ### Purpose:
> - Get live search results of specified keywords
> - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212789e0
> ### Parameters:
> - keyword: Keyword
> - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the last request.
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Live search results
>
> # [示例/Example]
> keyword = "小米商城"
> cursor = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 小米商城 | 无 |
| cursor | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-app-v3-fetch-multi-video"></a>
### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video`

- 摘要：批量获取视频信息 V1/Batch Get Video Information V1
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post`

#### 说明

> # [中文]
> ### 用途:
> - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。
> ### 参数:
> - aweme_ids: 作品id列表，最多支持10个作品id。
> ### 返回:
> - 作品数据
> ### 备注:
> - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）
>     - 8：视频不存在或已被删除
>     - 5：该内容被标记为私人内容，没有公开展示权限
>     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见
>     - 更多状态码请提交给我们的客户支持进行补充。
>
> # [English]
> ### Purpose:
> - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface charges a fixed price of 0.001$ * 10 = 0.01$ each time.
> ### Parameters:
> - aweme_ids: List of video ids, up to 10 video ids are supported.
> ### Return:
> - Video data
> ### Note:
> - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)
>     - 8: The video does not exist or has been deleted
>     - 5: This content is marked as private content and does not have public display permissions
>     - 10: This content is marked as partially visible, only visible to some users chosen by the author
>     - For more status codes, please submit them to our customer support for supplementation.
>
> # [示例/Example]
> aweme_ids = ["7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640"]

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：[string]

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | 是 | 无 | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-app-v3-fetch-multi-video-high-quality-play-url"></a>
### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url`

- 摘要：批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_multi_video_high_quality_play_url_post`

#### 说明

> # [中文]
> ### 用途:
> - 此接口目前优惠活动价为$0.25，活动结束后恢复原价$0.5。不足50个视频按50个视频收费。
> - 批量获取视频的最高画质(原始上传画质)播放链接
> - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。
> - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。
> - 此接口非常适合用于批量获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。
> - 使用并发请求，提高批量获取效率。
> - 最多支持50个视频ID。
> ### 参数:
> - aweme_ids: 作品id列表，用逗号分隔，例如: "123,456,789"，最多50个。
> ### 返回:
> - total: 总数
> - success_count: 成功数量
> - failed_count: 失败数量
> - videos: 视频列表，每个视频包含以下字段：
>     - video_id: 作品id
>     - original_video_url: 最高画质(原始上传画质)播放链接
>     - file_size: 文件大小（字节）
>     - file_size_in_mb: 文件大小（MB）
>     - content_type: 内容类型
>     - success: 是否成功
>     - error: 错误信息（如果失败）
> ### 备注:
> - 由于数量较多，处理时间可能会稍长，请增加等待时间。
>
> # [English]
> ### Purpose:
> - This interface is currently on sale for $0.25, and will return to the original price of $0.5 after the event ends. If there are less than 50 videos, they will be charged as 50 videos.
> - Batch get the highest quality (original upload quality) play URL of videos
> - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata.
> - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface.
> - This interface is very suitable for batch obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc.
> - Use concurrent requests to improve batch acquisition efficiency.
> - Support up to 50 video IDs.
> ### Parameters:
> - aweme_ids: Video id list, separated by commas, for example: "123,456,789", up to 50.
> ### Return:
> - total: Total count
> - success_count: Success count
> - failed_count: Failed count
> - videos: Video list, each video contains the following fields:
>     - video_id: Video id
>     - original_video_url: Highest quality (original upload quality) play URL
>     - file_size: File size (bytes)
>     - file_size_in_mb: File size (MB)
>     - content_type: Content type
>     - success: Whether successful
>     - error: Error message (if failed)
> ### Note:
> - Due to the large number, the processing time may be slightly longer, please increase the waiting time.
> # [示例/Example]
> aweme_ids = "7512756548356492544,7448118827402972455,7126745726494821640"

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`aweme_ids`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| aweme_ids | string | 否 | 作品id列表，用逗号分隔，最多50个/Video id list, separated by commas, up to 50 | 7512756548356492544,7448118827402972455,7126745726494821640 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-multi-video-statistics"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_multi_video_statistics`

- 摘要：根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据视频ID获取作品的统计数据，支持多个视频id，一次性最多支持50个视频。
> - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。
> - 价格为：0.025$一次。
> - 可以获取到的统计有：
>     - 点赞数（digg_count）
>     - 下载数（download_count）
>     - 播放数（play_count）
>     - 分享数（share_count）
> ### 参数:
> - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过50个，单个也可以，则无需逗号。
> ### 返回:
> - 作品统计数据
>
> # [English]
> ### Purpose:
> - Get the statistical data of the Post according to the video ID, support multiple video ids, up to 50 videos at a time.
> - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface.
> - Price: 0.025$ each time.
> - List of statistics that can be obtained:
>     - Like count (digg_count)
>     - Download count (download_count)
>     - Play count (play_count)
>     - Share count (share_count)
> ### Parameters:
> - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 50, single is also possible, no need for commas.
> ### Return:
> - Post statistics data
>
> # [示例/Example]
> aweme_ids = "7448118827402972455,7126745726494821640"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_ids | query | string | 是 | 作品id/Video id | 无 | 7448118827402972455,7126745726494821640 | 无 |

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

<a id="post-api-u1-v1-douyin-app-v3-fetch-multi-video-v2"></a>
### `POST /api/u1/v1/douyin/app/v3/fetch_multi_video_v2`

- 摘要：批量获取视频信息 V2/Batch Get Video Information V2
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_v2_api_v1_douyin_app_v3_fetch_multi_video_v2_post`

#### 说明

> # [中文]
> ### 用途:
> - 批量获取视频信息，支持图文、视频等，一次性最多支持50个视频，此接口收费固定价格为0.001$ * 50 = 0.05$一次。
> ### 参数:
> - aweme_ids: 作品id列表，最多支持50个作品id。
> ### 返回:
> - 作品数据
> ### 备注:
> - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）
>     - 8：视频不存在或已被删除
>     - 5：该内容被标记为私人内容，没有公开展示权限
>     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见
>     - 更多状态码请提交给我们的客户支持进行补充。
>
> # [English]
> ### Purpose:
> - Batch Get Video Information, support photo, video, etc., up to 50 videos at a time, this interface charges a fixed price of 0.001$ * 50 = 0.05$ each time.
> ### Parameters:
> - aweme_ids: List of video ids, up to 50 video ids are supported.
> ### Return:
> - Video data
> ### Note:
> - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)
>     - 8: The video does not exist or has been deleted
>     - 5: This content is marked as private content and does not have public display permissions
>     - 10: This content is marked as partially visible, only visible to some users chosen by the author
>     - For more status codes, please submit them to our customer support for supplementation.
>
> # [示例/Example]
> aweme_ids = ["7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640", "7448118827402972455", "7126745726494821640"]

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：[string]

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | 是 | 无 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-music-detail"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_music_detail`

- 摘要：获取指定音乐的详情数据/Get details of specified music
- 能力：详情 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定音乐的详情数据
> ### 参数:
> - music_id: 音乐id
> ### 返回:
> - 音乐详情数据
>
> # [English]
> ### Purpose:
> - Get details of specified music
> ### Parameters:
> - music_id: Music id
> ### Return:
> - Music details data
>
> # [示例/Example]
> music_id = "7136850194742315016"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| music_id | query | string | 是 | 音乐id/Music id | 无 | 7136850194742315016 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-music-hot-search-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_music_hot_search_list`

- 摘要：获取抖音音乐榜数据/Get Douyin music hot search list data
- 能力：搜索 / 热点/榜单 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音音乐热榜数据
> ### 参数:
> - chart_type: 榜单类型，默认值为'hot'，支持下面的值：
>     - 'hot': 热门榜
>     - 'trending': 飙升榜
>     - 'original': 原创榜
> - cursor: 游标，默认值为'0'，用于分页获取数据，每次请求后会返回下一个游标值，并且通过 `has_more` 字段指示是否有更多数据可供获取。
> ### 返回:
> - 音乐热搜榜数据
>
> # [English]
> ### Purpose:
> - Get Douyin music hot search list data
> ### Parameters:
> - chart_type: Chart type, default value is 'hot', supports the following values:
>     - 'hot': Hot chart
>     - 'trending': Trending chart
>     - 'original': Original chart
> - cursor: Cursor, default value is '0', used for paginating data retrieval. After each request, the next cursor value will be returned, and the `has_more` field indicates whether there is more data available.
> ### Return:
> - Music hot search list data
>
> # [示例/Example]
> chart_type = "hot"
> cursor = "0"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| chart_type | query | string | 否 | 榜单类型/Chart type | hot | hot | 无 |
| cursor | query | string | 否 | 游标/Cursor | 0 | 0 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-music-search-result"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_music_search_result`

- 摘要：获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- 能力：搜索 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定关键词的音乐搜索结果
> - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212797e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 音乐搜索结果
>
> # [English]
> ### Purpose:
> - Get music search results of specified keywords
> - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212797e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Music search results
>
> # [示例/Example]
> keyword = "中华娘"
> offset = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-music-video-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_music_video_list`

- 摘要：获取指定音乐的视频列表数据/Get video list of specified music
- 能力：作品详情 / 音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定音乐的视频列表数据
> ### 参数:
> - music_id: 音乐id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 音乐视频列表数据
>
> # [English]
> ### Purpose:
> - Get video list of specified music
> ### Parameters:
> - music_id: Music id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Music video list data
>
> # [示例/Example]
> music_id = "7136850194742315016"
> cursor = 0
> count = 10

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| music_id | query | string | 是 | 音乐id/Music id | 无 | 7136850194742315016 | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 10 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-one-video"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_one_video`

- 摘要：获取单个作品数据/Get single video data
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品数据，支持图文、视频等。
> ### 参数:
> - aweme_id: 作品id
> ### 返回:
> - 作品数据
> ### 备注:
> - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）
>     - 8：视频不存在或已被删除
>     - 5：该内容被标记为私人内容，没有公开展示权限
>     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见
>     - 更多状态码请提交给我们的客户支持进行补充。
>
> # [English]
> ### Purpose:
> - Get single video data, support photo, video, etc.
> ### Parameters:
> - aweme_id: Video id
> ### Return:
> - Video data
> ### Note:
> - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)
>     - 8: The video does not exist or has been deleted
>     - 5: This content is marked as private content and does not have public display permissions
>     - 10: This content is marked as partially visible, only visible to some users chosen by the author
>     - For more status codes, please submit them to our customer support for supplementation.
>
> # [示例/Example]
> aweme_id = "7448118827402972455"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7448118827402972455 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-one-video-by-share-url"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_by_share_url`

- 摘要：根据分享链接获取单个作品数据/Get single video data by sharing link
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据分享链接获取单个作品数据
> ### 参数:
> - share_url: 分享链接
> ### 返回:
> - 作品数据
> ### 备注:
> - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）
>     - 8：视频不存在或已被删除
>     - 5：该内容被标记为私人内容，没有公开展示权限
>     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见
>     - 更多状态码请提交给我们的客户支持进行补充。
>
> # [English]
> ### Purpose:
> - Get single video data by sharing link
> ### Parameters:
> - share_url: Share link
> ### Return:
> - Video data
> ### Note:
> - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)
>     - 8: The video does not exist or has been deleted
>     - 5: This content is marked as private content and does not have public display permissions
>     - 10: This content is marked as partially visible, only visible to some users chosen by the author
>     - For more status codes, please submit them to our customer support for supplementation.
>
> # [示例/Example]
> share_url = "https://v.douyin.com/e3x2fjE/"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_url | query | string | 是 | 分享链接/Share link | 无 | https://v.douyin.com/e3x2fjE/ | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-one-video-v2"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v2`

- 摘要：获取单个作品数据 V2/Get single video data V2
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_v2_api_v1_douyin_app_v3_fetch_one_video_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品数据，支持图文、视频等。
> ### 参数:
> - aweme_id: 作品id
> ### 返回:
> - 作品数据
> ### 备注:
> - 如果接口出现返回空的情况，请使用一样的参数去请求 Web 版本接口，具体响应状态码参考：
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8：该内容因海外版权限制，暂时无法观看（短剧，电影片段等）
>     - 8：视频不存在或已被删除
>     - 5：该内容被标记为私人内容，没有公开展示权限
>     - 10：该内容被标记为部分可见，仅作者选择的部分用户可见
>     - 更多状态码请提交给我们的客户支持进行补充。
>
> # [English]
> ### Purpose:
> - Get single video data, support photo, video, etc.
> ### Parameters:
> - aweme_id: Video id
> ### Return:
> - Video data
> ### Note:
> - If the interface returns empty, please use the same parameters to request the Web version interface. The specific response status code refers to:
>     - JSON PATH: $.data.filter_list[0].reason
>     - 8: This content is temporarily unavailable for viewing due to overseas copyright restrictions (short dramas, movie clips, etc.)
>     - 8: The video does not exist or has been deleted
>     - 5: This content is marked as private content and does not have public display permissions
>     - 10: This content is marked as partially visible, only visible to some users chosen by the author
>     - For more status codes, please submit them to our customer support for supplementation.
>
> # [示例/Example]
> aweme_id = "7448118827402972455"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7448118827402972455 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-one-video-v3"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_one_video_v3`

- 摘要：获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_v3_api_v1_douyin_app_v3_fetch_one_video_v3_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品数据，支持文章、图文、视频等。
> - V3版本的接口，解决了版权限制问题，可以获取更多受限内容，比如 V1，V2版本返回的Reason为8的内容和部分文章或短剧等。
> ### 参数:
> - aweme_id: 作品id
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data, support article, photo, video, etc.
> - V3 version of the interface, which solves the copyright restriction problem and can obtain more restricted content, such as content with Reason 8 returned by V1 and V2 versions and some articles or short dramas.
> ### Parameters:
> - aweme_id: Video id
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_id = "7592116912205630761"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品或文章ID/Video or Article ID | 无 | 7592116912205630761 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-series-detail"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_series_detail`

- 摘要：获取短剧详情信息/Get series detail
- 能力：详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_series_detail_api_v1_douyin_app_v3_fetch_series_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取短剧详情信息
> ### 参数:
> - series_id: 短剧id
> ### 返回:
> - 短剧详情数据
> ### 备注:
> - 该接口返回短剧的详细信息，包括：
>     - 短剧名称、描述、封面
>     - 作者信息
>     - 总集数、更新状态
>     - 播放量、收藏量等统计数据
>     - 付费信息（如有）
>
> # [English]
> ### Purpose:
> - Get series/playlet detail information
> ### Parameters:
> - series_id: Series id
> ### Return:
> - Series detail data
> ### Note:
> - This interface returns detailed information of the series, including:
>     - Series name, description, cover
>     - Author information
>     - Total episodes, update status
>     - Play count, collection count and other statistics
>     - Payment information (if any)
>
> # [示例/Example]
> series_id = "7592054624643713067"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| series_id | query | string | 是 | 短剧id/Series id | 无 | 7592054624643713067 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-series-video-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_series_video_list`

- 摘要：获取短剧视频列表/Get series video list
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_series_video_list_api_v1_douyin_app_v3_fetch_series_video_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取短剧视频列表
> ### 参数:
> - series_id: 短剧id
> - cursor: 游标，用于翻页，第一页为0，第二页通常为count的值（如15）。
> ### 返回:
> - 短剧视频列表数据
> ### 备注:
> - 该接口返回短剧中的所有视频列表
> - 响应中的 aweme_list 包含短剧的各集视频信息
> - has_more 字段表示是否还有更多数据
>
> # [English]
> ### Purpose:
> - Get series/playlet video list
> ### Parameters:
> - series_id: Series id
> - cursor: Cursor, used for paging, the first page is 0, the second page is usually the value of count (e.g., 15).
> ### Return:
> - Series video list data
> ### Note:
> - This interface returns all video list in the series
> - The aweme_list in the response contains video information of each episode
> - The has_more field indicates whether there is more data
>
> # [示例/Example]
> series_id = "7592054624643713067"
> cursor = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| series_id | query | string | 是 | 短剧id/Series id | 无 | 7592054624643713067 | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-share-info-by-share-code"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_share_info_by_share_code`

- 摘要：根据分享口令获取分享信息/Get share info by share code
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_share_info_by_share_code_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据分享口令获取分享信息，比如抖音文章的分享口令提取分享人信息和文章ID等然后再去请求单一作品数据接口获取文章内容。
> ### 参数:
> - share_code: 分享口令
> ### 返回:
> - 分享信息，包含分享人信息和文章ID等
>
> # [English]
> ### Purpose:
> - Get share info by share code, such as extracting sharer information and article ID from Douyin article share code, and then requesting a single video data interface to get the article content.
> ### Parameters:
> - share_code: Share code
> ### Return:
> - Share info, including sharer information and article ID, etc.
>
> # [示例/Example]
> share_code = "8:/ h@O.kP 05/21 【生意场上，装逼就是节省沟通成本】长按复制打开抖音，即可阅读文章 ︽︽2QnCB9aIZZ29︽︽"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_code | query | string | 是 | 分享口令/Share code | 无 | 8:/ h@O.kP 05/21 【生意场上，装逼就是节省沟通成本】长按复制打开抖音，即可阅读文章 ︽︽2QnCB9aIZZ29︽︽ | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-user-fans-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_user_fans_list`

- 摘要：获取用户粉丝列表/Get user fans list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户粉丝列表
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
> - count: 数量，默认为20，建议保持不变。
> ### 返回:
> - 粉丝列表
>
> # [English]
> ### Purpose:
> - Get user fans list
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
> - count: Number, default is 20, it is recommended to keep it unchanged.
> ### Return:
> - Fans list
>
> # [示例/Example]
> sec_user = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"
> max_time = "0"
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id | MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70 | 无 | 无 |
| max_time | query | string | 否 | 最大时间戳/Maximum timestamp | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-user-following-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_user_following_list`

- 摘要：获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户关注列表
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
> - count: 数量，默认为20，建议保持不变。
> ### 返回:
> - 关注列表
>
> # [English]
> ### Purpose:
> - Get user following list
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
> - count: Number, default is 20, it is recommended to keep it unchanged.
> ### Return:
> - Following list
>
> # [示例/Example]
> sec_user = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"
> max_time = "0"
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id | MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70 | 无 | 无 |
| max_time | query | string | 否 | 最大时间戳/Maximum timestamp | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-user-like-videos"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_user_like_videos`

- 摘要：获取用户喜欢作品数据/Get user like video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户喜欢作品数据
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
> - count: 最大数量
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user like video data
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.
> - count: Maximum count number
> ### Return:
> - User video data
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"
> max_cursor = 0
> counts = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 是 | 用户sec_user_id/User sec_user_id | 无 | MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y | 无 |
| max_cursor | query | integer | 否 | 最大游标/Maximum cursor | 0 | 无 | 无 |
| counts | query | integer | 否 | 每页数量/Number per page | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-user-post-videos"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_user_post_videos`

- 摘要：获取用户主页作品数据/Get user homepage video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户主页作品数据
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
> - count: 最大数量，不要超过20，建议保持不变。
> - sort_type: 排序类型，可选值如下：
>     - `0`: 最新排序-默认
>     - `1`: 最热排序
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user homepage video data
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.
> - count: Maximum count number, do not exceed 20, it is recommended to keep it unchanged.
> - sort_type: Sort type, optional values are as follows:
>     - `0`: Latest sorting - default
>     - `1`: Hottest sorting
> ### Return:
> - User video data
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE"
> max_cursor = 0
> counts = 20
> sort_type = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 是 | 用户sec_user_id/User sec_user_id | 无 | MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE | 无 |
| max_cursor | query | integer | 否 | 最大游标/Maximum cursor | 0 | 无 | 无 |
| count | query | integer | 否 | 每页数量/Number per page | 20 | 无 | 无 |
| sort_type | query | integer | 否 | 排序类型/Sort type | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-user-search-result"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_user_search_result`

- 摘要：获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定关键词的用户搜索结果
> - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212785e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量，请保持默认，否则会出现BUG。
> - douyin_user_fans(粉丝数量):
>     - "": 不限
>     - "0_1k": 1000以下
>     - "1k_1w": 1000-1万
>     - "1w_10w": 1w-10w
>     - "10w_100w": 10w-100w
>     - "100w_": 100w以上
> - douyin_user_type(用户类型，请使用英文而不是中文):
>     - "": 不限
>     - "common_user": 普通用户
>     - "enterprise_user": 企业认证
>     - "personal_user": 个人认证
> ### 返回:
> - 用户搜索结果
>
> # [English]
> ### Purpose:
> - Get user search results of specified keywords
> - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212785e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number Please keep the default, otherwise there will be BUG.
> - douyin_user_fans(Fans):
>     - "": Unlimited
>     - "0_1k": Less than 1000
>     - "1k_1w": 1000-10,000
>     - "1w_10w": 10,000-100,000
>     - "10w_100w": 100,000-1,000,000
>     - "100w_": More than 1,000,000
> - douyin_user_type(User type, please use English instead of Chinese):
>     - "": Unlimited
>     - "common_user": Common user
>     - "enterprise_user": Enterprise certification
>     - "personal_user": Personal certification
> ### Return:
> - User search results
>
> # [示例/Example]
> keyword = "动漫"
> offset = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| douyin_user_fans | query | string | 否 | 粉丝数/Fans | 无 | 无 | 无 |
| douyin_user_type | query | string | 否 | 用户类型/User type | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-user-series-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_user_series_list`

- 摘要：获取用户短剧合集列表/Get user series list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_series_list_api_v1_douyin_app_v3_fetch_user_series_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户的短剧合集列表
> ### 参数:
> - user_id: 用户id，与sec_user_id二选一即可
> - sec_user_id: 用户加密id，与user_id二选一即可
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> ### 返回:
> - 用户短剧合集列表数据
> ### 备注:
> - 该接口返回用户发布的所有短剧合集
> - 响应中的 series_id 可用于获取短剧详情和视频列表
>
> # [English]
> ### Purpose:
> - Get user's series/playlet collection list
> ### Parameters:
> - user_id: User id
> - sec_user_id: User encrypted id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> ### Return:
> - User series list data
> ### Note:
> - This interface returns all series collections published by the user
> - The series_id in the response can be used to get series details and video list
>
> # [示例/Example]
> user_id = "3010877781453635"
> sec_user_id = "MS4wLjABAAAAfAU5kMk-W4569G1z2iRsy8t6-kOxO17Eaz6yte4NQokeUeOpeqTGEc480e34O8lK"
> cursor = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 否 | 用户id/User id | 无 | 3010877781453635 | 无 |
| sec_user_id | query | string | 否 | 用户加密id/User sec id | 无 | MS4wLjABAAAAfAU5kMk-W4569G1z2iRsy8t6-kOxO17Eaz6yte4NQokeUeOpeqTGEc480e34O8lK | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-comment-replies"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_comment_replies`

- 摘要：获取指定视频的评论回复数据/Get comment replies data of specified video
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定视频的评论回复数据
> ### 参数:
> - item_id: 作品id
> - comment_id: 评论id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 评论回复数据
>
> # [English]
> ### Purpose:
> - Get comment replies data of specified video
> ### Parameters:
> - item_id: Video id
> - comment_id: Comment id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Comment replies data
>
> # [示例/Example]
> aweme_id = "7354666303006723354"
> comment_id = "7354669356632638218"
> cursor = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id | 无 | 7354666303006723354 | 无 |
| comment_id | query | string | 是 | 评论id/Comment id | 无 | 7354669356632638218 | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-comments"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_comments`

- 摘要：获取单个视频评论数据/Get single video comments data
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个视频评论数据
> ### 参数:
> - aweme_id: 作品id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 评论数据
>
> # [English]
> ### Purpose:
> - Get single video comments data
> ### Parameters:
> - aweme_id: Video id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Comments data
>
> # [示例/Example]
> aweme_id = "7448118827402972455"
> cursor = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7448118827402972455 | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-high-quality-play-url"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_high_quality_play_url`

- 摘要：获取视频的最高画质播放链接/Get the highest quality play URL of the video
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_high_quality_play_url_api_v1_douyin_app_v3_fetch_video_high_quality_play_url_get`

#### 说明

> # [中文]
> ### 用途:
> - 价格：0.005$ 一次。
> - 获取视频的最高画质(原始上传画质)播放链接
> - 该接口会返回最高画质的播放链接，原始上传画质是指用户上传视频时的画质，通常最高画质视频无压缩码率并且文件头包含元数据。
> - 最高画质的视频链接无法从抖音APP或网页版直接获取，需要通过此接口获取。
> - 此接口非常适合用于获取高清无水印视频链接，适用于需要高质量视频的场景，如视频编辑、存档、训练模型等。
> - 一般情况都可以在线播放，如果不行，可以尝试使用IDM或浏览器下载后播放。
> ### 参数:
> - aweme_id: 作品id，优先使用aweme_id，如果没有则使用share_url。
> - share_url: 可选，分享链接，如果提供了作品id，则此参数可以不传。
> ### 返回:
> - video_id： 作品id
> - original_video_url： 最高画质(原始上传画质)播放链接
> - video_data： 视频数据，包含视频的元数据，如时长、大小等。
>
> # [English]
> ### Purpose:
> - Price: 0.005$ each time.
> - Get the highest quality (original upload quality) play URL of the video
> - This interface will return the highest quality play URL, the original upload quality refers to the quality of the video when the user uploads it, usually the highest quality video has an uncompressed bitrate and the file header contains metadata.
> - The highest quality video link cannot be obtained directly from the Douyin APP or web version, and must be obtained through this interface.
> - This interface is very suitable for obtaining high-definition, watermark-free video links, suitable for scenarios that require high-quality videos, such as video editing, archiving, training models, etc.
> - Generally, it can be played online, if not, you can try to download it using IDM or a browser and then play it.
> ### Parameters:
> - aweme_id: Video id, prefer to use aweme_id, if not available, use share_url.
> - share_url: Optional, share link, if the video id is provided, this parameter can be omitted.
> ### Return:
> - video_id: Video id
> - original_video_url: Highest quality (original upload quality) play URL
> - video_data: Video data, including metadata such as duration, size, etc.
> # [示例/Example]
> aweme_id = "7512756548356492544"
> share_url = "https://www.douyin.com/video/7512756548356492544"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 否 | 作品id/Video id | 无 | 7512756548356492544 | 无 |
| share_url | query | string | 否 | 可选，分享链接/Optional, share link | 无 | https://www.douyin.com/video/7512756548356492544 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-mix-detail"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_detail`

- 摘要：获取抖音视频合集详情数据/Get Douyin video mix detail data
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音视频合集详情数据
> ### 参数:
> - mix_id: 合集id
> ### 返回:
> - 视频合集详情数据
>
> # [English]
> ### Purpose:
> - Get Douyin video mix detail data
> ### Parameters:
> - mix_id: Mix id
> ### Return:
> - Video mix detail data
>
> # [示例/Example]
> mix_id = "7302011174286002217"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mix_id | query | string | 是 | 合集id/Mix id | 无 | 7302011174286002217 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-mix-post-list"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_mix_post_list`

- 摘要：获取抖音视频合集作品列表数据/Get Douyin video mix post list data
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音视频合集作品列表数据
> ### 参数:
> - mix_id: 合集id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量，请保持默认，否则会出现BUG。
> ### 返回:
> - 视频合集作品列表数据
>
> # [English]
> ### Purpose:
> - Get Douyin video mix post list data
> ### Parameters:
> - mix_id: Mix id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number Please keep the default, otherwise there will be BUG.
> ### Return:
> - Video mix post list data
>
> # [示例/Example]
> mix_id = "7302011174286002217"
> cursor = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mix_id | query | string | 是 | 合集id/Mix id | 无 | 7302011174286002217 | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-search-result"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result`

- 摘要：获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定关键词的视频搜索结果
> - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量，请保持默认，否则会出现BUG。
> - sort_type: 0:综合排序 1:最多点赞 2:最新发布
> - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年
> - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上
> - content_type: 0:不限 1:视频 2:图文
> ### 返回:
> - 视频搜索结果
>
> # [English]
> ### Purpose:
> - Get video search results of specified keywords
> - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number Please keep the default, otherwise there will be BUG.
> - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
> - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year
> - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
> - content_type: 0: Unlimited 1: Video 2: Graphic and text
> ### Return:
> - Video search results
>
> # [示例/Example]
> keyword = "中华娘"
> offset = 0
> count = 20
> sort_type = "0"
> publish_time = "0"
> filter_duration = "0"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| sort_type | query | string | 否 | 排序类型/Sort type | 0 | 无 | 无 |
| publish_time | query | string | 否 | 发布时间/Publish time | 0 | 无 | 无 |
| filter_duration | query | string | 否 | 时长/Duration | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-search-result-v2"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_search_result_v2`

- 摘要：获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。
> - 收费标准为：0.01$每次请求。
> - 该接口已弃用，替代接口为：https://docs.tikhub.io/370212780e0
> ### 参数:
> - keyword: 关键词
> - sort_type:
>     - 排序类型，可用值如下：
>     - _0 :综合(General)
>     - _1 :最多点赞(More likes)
>     - _2 :最新发布(New)
> - publish_time：
>     - 发布时间，可用值如下：
>     - _0 :不限(No Limit)
>     - _1 :一天之内(last 1 day)
>     - _7 :一周之内(last 1 week)
>     - _180 :半年之内(last half year)
> - filter_duration：
>     - 视频时长，可用值如下：
>     - _0 :不限(No Limit)
>     - _1 :1分钟以下(1 minute and below)
>     - _2 :1-5分钟 (1-5 minutes)
>     - _3 :5分钟以上(5 minutes more)
> - page: 页码
>     - 默认从1开始，然后依次递增加1
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> ### 返回:
> - 视频搜索结果V2
>
> # [English]
> ### Purpose:
> - Get video search results of specified keywords V2, this interface has better stability and higher cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is recommended to use this interface.
> - The charging standard is: $0.01 per request.
> - This interface has been deprecated, and the alternative interface is: https://docs.tikhub.io/370212780e0
> ### Parameters:
> - keyword: Keyword
> - sort_type:
>     - Sort type, available values are as follows:
>     - _0 : General
>     - _1 : More likes
>     - _2 : New
> - publish_time:
>     - Publish time, available values are as follows:
>     - _0 : No Limit
>     - _1 : last 1 day
>     - _7 : last 1 week
>     - _180 : last half year
> - filter_duration:
>     - Duration filter, available values are as follows:
>     - _0 : No Limit
>     - _1 : 1 minute and below
>     - _2 : 1-5 minutes
>     - _3 : 5 minutes more
> - page: Page
>     - Start from 1 by default, then increase by 1 each time
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> ### Return:
> - Video search results V2
>
> # [示例/Example]
> keyword = "中华娘"
> sort_type = "_0"
> publish_time = "_0"
> filter_duration = "_0"
> page = 1
> search_id = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| sort_type | query | string | 否 | 排序类型/Sort type | _0 | 无 | 无 |
| publish_time | query | string | 否 | 发布时间/Publish time | _0 | 无 | 无 |
| filter_duration | query | string | 否 | 视频时长/Duration filter | _0 | 无 | 无 |
| page | query | integer | 否 | 页码/Page | 1 | 无 | 无 |
| search_id | query | string | 否 | 搜索id，翻页时需要提供/Search id, need to provide when paging | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-fetch-video-statistics"></a>
### `GET /api/u1/v1/douyin/app/v3/fetch_video_statistics`

- 摘要：根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据视频ID获取作品的统计数据
> - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。
> - 可以获取到的统计有：
>     - 点赞数（digg_count）
>     - 下载数（download_count）
>     - 播放数（play_count）
>     - 分享数（share_count）
> ### 参数:
> - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。
> ### 返回:
> - 作品统计数据
>
> # [English]
> ### Purpose:
> - Get the statistical data of the Post according to the video ID
> - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be obtained through this interface.
> - List of statistics that can be obtained:
>     - Like count (digg_count)
>     - Download count (download_count)
>     - Play count (play_count)
>     - Share count (share_count)
> ### Parameters:
> - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is also possible, no need for commas.
> ### Return:
> - Post statistics data
>
> # [示例/Example]
> aweme_ids = "7448118827402972455,7126745726494821640"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_ids | query | string | 是 | 作品id/Video id | 无 | 7448118827402972455,7126745726494821640 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-generate-douyin-short-url"></a>
### `GET /api/u1/v1/douyin/app/v3/generate_douyin_short_url`

- 摘要：生成抖音短链接/Generate Douyin short link
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成抖音短链接
> ### 参数:
> - url: 抖音链接
> ### 返回:
> - 短链接数据
>
> # [English]
> ### Purpose:
> - Generate Douyin short link
> ### Parameters:
> - url: Douyin link
> ### Return:
> - Short link data
>
> # [示例/Example]
> url = "https://www.douyin.com/passport/web/logout/"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 抖音链接/Douyin link | 无 | https://www.douyin.com/passport/web/logout/ | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-generate-douyin-video-share-qrcode"></a>
### `GET /api/u1/v1/douyin/app/v3/generate_douyin_video_share_qrcode`

- 摘要：生成抖音视频分享二维码/Generate Douyin video share QR code
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成抖音视频分享二维码
> ### 参数:
> - object_id: 作品id或作者uid
> ### 返回:
> - 二维码数据
>
> # [English]
> ### Purpose:
> - Generate Douyin video share QR code
> ### Parameters:
> - object_id: Video id or author uid
> ### Return:
> - QR code data
>
> # [示例/Example]
> object_id = "7348044435755846962"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| object_id | query | string | 是 | 作品id/Video id | 无 | 7348044435755846962 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-handler-user-profile"></a>
### `GET /api/u1/v1/douyin/app/v3/handler_user_profile`

- 摘要：获取指定用户的信息/Get information of specified user
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的信息
> ### 参数:
> - sec_user_id: 用户sec_user_id
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get information of specified user
> ### Parameters:
> - sec_user_id: User sec_user_id
> ### Return:
> - User information
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 是 | 用户sec_user_id/User sec_user_id | 无 | MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-open-douyin-app-to-keyword-search"></a>
### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_keyword_search`

- 摘要：生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果。
>
> ### 参数:
> - keyword: 关键词
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result
>
> ### Parameters:
> - keyword: Keyword
>
> ### Return:
> - Share link
>
> # [示例/Example]
> keyword = "雷军"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 雷军 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-open-douyin-app-to-send-private-message"></a>
### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_send_private_message`

- 摘要：生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成抖音分享链接，唤起抖音APP，给指定用户发送私信。
>
> ### 参数:
> - uid: 用户id
> - sec_uid: 用户sec_uid
> - 注意: 请确保user_id和sec_uid都有值，否则无法发送私信给指定用户。
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate Douyin share link, call Douyin APP, and send private messages to specified users
>
> ### Parameters:
> - uid: User id
> - sec_uid: User sec_uid
> - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot send private messages to the specified user.
>
> ### Return:
> - Share link
>
> # [示例/Example]
> uid = "96874812426"
> sec_uid = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id | 无 | 96874812426 | 无 |
| sec_uid | query | string | 是 | 用户sec_uid/User sec_uid | 无 | MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-open-douyin-app-to-user-profile"></a>
### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_user_profile`

- 摘要：生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。
>
> ### 参数:
> - uid: 用户id
> - sec_uid: 用户sec_uid
> - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate Douyin share link, call Douyin APP, and jump to the specified user profile
>
> ### Parameters:
> - uid: User id
> - sec_uid: User sec_uid
> - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the specified user profile.
>
> ### Return:
> - Share link
>
> # [示例/Example]
> uid = "96874812426"
> sec_uid = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户id/User id | 无 | 96874812426 | 无 |
| sec_uid | query | string | 是 | 用户sec_uid/User sec_uid | 无 | MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-open-douyin-app-to-video-detail"></a>
### `GET /api/u1/v1/douyin/app/v3/open_douyin_app_to_video_detail`

- 摘要：生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page
- 能力：作品详情 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。
>
> ### 参数:
> - aweme_id: 作品id
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate Douyin share link, call Douyin APP, and jump to the specified video
>
> ### Parameters:
> - aweme_id: Video id
>
> ### Return:
> - Share link
>
> # [示例/Example]
> aweme_id = "7197598285882789120"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7348044435755846962 | 无 |

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

<a id="get-api-u1-v1-douyin-app-v3-register-device"></a>
### `GET /api/u1/v1/douyin/app/v3/register_device`

- 摘要：抖音APP注册设备/Douyin APP register device
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`register_device_api_v1_douyin_app_v3_register_device_get`

#### 说明

> # [中文]
> ### 用途:
> - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。
>
> ### 参数:
> - proxy: 代理，要带http://或https://，仅支持http代理。
>   - 格式: username:password@ip:port
>
> ### 返回:
> - 设备信息以及设备的Cookie信息。
>
> # [English]
> ### Purpose:
> - Register device in Douyin APP, retrieve device information and device cookies.
>
> ### Parameters:
> - proxy: Proxy, with http:// or https://, only supports http proxies.
>   - Format: username:password@ip:port
>
> ### Return:
> - Device information and device cookies.
>
> # [示例/Example]
> proxy = "http://username:password@ip:port"
>
> # [响应/Response]
> ```json
> {
>     "code": 200,
>     "router": "/api/v1/douyin/app/v3/register_device",
>     "params": {
>         "proxy": "username:password@ip:port"
>     },
>     "data": {
>         "iid": "3631064037200330",
>         "device_id": "3631064037196234",
>         "mssdk_token": "",
>         "device_platform": "android",
>         "channel": "xiaomi_64_1775",
>         "version_code": 240900,
>         "version_name": "24.9.0",
>         "manifest_version_code": 240901,
>         "update_version_code": 24909900,
>         "device_type": "V1963A",
>         "device_brand": "vivo",
>         "device_model": "V1963A",
>         "openudid": "5d736335afc17aab",
>         "os_api": 29,
>         "os_version": "10",
>         "resolution": "2400x1080",
>         "dpi": 480,
>         "host_abi": "arm64-v8a",
>         "ua": "com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A; Build/compiler10301842;tt-ok/3.12.13.4-tiktok)",
>         "cookies": {
>             "install_id": "3631064037200330",
>             "odin_tt": "5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841",
>             "d_ticket": "42186c5b0c54ea1a2a9e02d4e62bf6ab",
>             "store-region": "cn-js",
>             "store-region-src": "did",
>             "multi_sids": "462868309327184:38167255076198698951907954929873",
>             "passport_csrf_token": "6f75287240634ad1f51f3b3bdcdb5424",
>             "passport_csrf_token_default": "6f75287240634ad1f51f3b3bdcdb5424",
>             "ttreq": "1$7f616210b41fc044b1f164542ac4e064288b5163"
>         },
>         "lanusk": "",
>         "device_manufacturer": "vivo",
>         "uuid": "357125675341697",
>         "cdid": "f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3",
>         "first_launch_timestamp": 1726970498636,
>         "x_tt_dt": "AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM",
>         "BootTime": 1726980411,
>         "MbTime": 1726780411,
>         "server_time": 1726980500,
>         "mc": "2A:66:7A:2D:8B:29",
>         "rom": "compiler10301842",
>         "rom_version": "PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys"
>     }
> }
> ```

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| proxy | query | string | 否 | 代理/Proxy | 无 | 无 | 无 |

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
