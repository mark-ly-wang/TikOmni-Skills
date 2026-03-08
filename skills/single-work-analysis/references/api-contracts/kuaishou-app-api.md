# Kuaishou-App-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/kuaishou-app-api.md`](../api-tags/kuaishou-app-api.md)
- 当前契约文件：`api-contracts/kuaishou-app-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`20`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(快手App数据接口/Kuaishou-App-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-kuaishou-app-fetch-brand-top-list"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_brand_top_list`

- 摘要：快手品牌榜单/Kuaishou brand top list
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 快手品牌榜单
> ### 参数:
> 获取快手品牌榜单，支持多个子榜单，具体参数如下：
>
> - 品牌榜单热门美妆榜对应参数：
>     - subTabId = 0
>     - subTabName = None
> - 品牌榜单热门服饰榜对应参数：
>     - subTabId = 131
>     - subTabName = "服饰"
> - 品牌榜单热门汽车榜对应参数：
>     - subTabId = 1
>     - subTabName = "汽车"
> - 品牌榜单热门游戏榜对应参数：
>     - subTabId = 25
>     - subTabName = "游戏"
> - 品牌榜单热门医疗健康榜对应参数：
>     - subTabId = 24
>     - subTabName = "医疗健康"
> - 品牌榜单热门3C数码榜对应参数：
>     - subTabId = 130
>     - subTabName = "3C数码"
> - 品牌榜单热门手机榜对应参数：
>     - subTabId = 128
>     - subTabName = "手机"
> - 品牌榜单热门家电榜对应参数：
>     - subTabId = 11
>     - subTabName = "家电"
> - 品牌榜单热门母婴榜对应参数：
>     - subTabId = 4
>     - subTabName = "母婴"
> - 品牌榜单热门食品饮料榜对应参数：
>     - subTabId = 2
>     - subTabName = "食品饮料"
>
> ### 返回:
> - 榜单数据
>
> # [English]
> ### Purpose:
> - Kuaishou brand top list
> ### Parameters:
> Get the Kuaishou brand top list, support multiple sub-top lists, specific parameters are as follows:
>
> - Corresponding parameters for the brand hot beauty list:
>     - subTabId = 0
>     - subTabName = None
> - Corresponding parameters for the brand hot clothing list:
>     - subTabId = 131
>     - subTabName = "Clothing"
> - Corresponding parameters for the brand hot car list:
>     - subTabId = 1
>     - subTabName = "Car"
> - Corresponding parameters for the brand hot game list:
>     - subTabId = 25
>     - subTabName = "Game"
> - Corresponding parameters for the brand hot medical health list:
>     - subTabId = 24
>     - subTabName = "Medical Health"
> - Corresponding parameters for the brand hot 3C digital list:
>     - subTabId = 130
>     - subTabName = "3C Digital"
> - Corresponding parameters for the brand hot mobile phone list:
>     - subTabId = 128
>     - subTabName = "Mobile Phone"
> - Corresponding parameters for the brand hot home appliance list:
>     - subTabId = 11
>     - subTabName = "Home Appliance"
> - Corresponding parameters for the brand hot maternal and child list:
>     - subTabId = 4
>     - subTabName = "Maternal and Child"
> - Corresponding parameters for the brand hot food and beverage list:
>     - subTabId = 2
>     - subTabName = "Food and Beverage"
>
>
> ### Returns:
> - List data
>
> # [示例/Example]
> subTabId = 0
> subTabName = None

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subTabId | query | integer | 否 | 无 | 0 | 无 | 无 |
| subTabName | query | string | 否 | 无 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-hot-board-categories"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_hot_board_categories`

- 摘要：快手热榜分类/Kuaishou hot categories
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get`

#### 说明

> # [中文]
> ### 用途:
> - 快手热榜分类
> ### 返回:
> - 分类数据
>
> # [English]
> ### Purpose:
> - Kuaishou hot categories
> ### Returns:
> - Categories data

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

<a id="get-api-u1-v1-kuaishou-app-fetch-hot-board-detail"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_hot_board_detail`

- 摘要：快手热榜详情/Kuaishou hot board detail
- 能力：热点/榜单 / 详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 快手热榜详情
> ### 参数:
> - boardType: 榜单类型
> - boardId: 榜单ID
> - boardType 和 boardId 可以从热榜分类接口中获取。
> ### 返回:
> - 详情数据
>
> # [English]
> ### Purpose:
> - Kuaishou hot board detail
> ### Parameters:
> - boardType: Board type
> - boardId: Board ID
> - boardType and boardId can be obtained from the hot board categories interface.
> ### Returns:
> - Detail data
>
> # [示例/Example]
> boardType = 1
> boardId = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| boardType | query | integer | 否 | 无 | 1 | 无 | 无 |
| boardId | query | integer | 否 | 无 | 1 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-hot-search-person"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_hot_search_person`

- 摘要：快手热搜人物榜单/Kuaishou hot search person board
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get`

#### 说明

> # [中文]
> ### 用途:
> - 快手热搜人物榜单
> ### 返回:
> - 榜单数据
>
> # [English]
> ### Purpose:
> - Kuaishou hot search person board
> ### Returns:
> - Board data

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

<a id="get-api-u1-v1-kuaishou-app-fetch-live-top-list"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_live_top_list`

- 摘要：快手直播榜单/Kuaishou live top list
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 快手直播榜单
> ### 参数:
> 获取快手直播榜单，支持多个子榜单，具体参数如下：
>
> - 直播总榜对应参数：
>     - subTabId = 0
>     - subTabName = None
> - 直播音乐榜对应参数：
>     - subTabId = 102
>     - subTabName = "音乐"
> - 直播舞蹈榜对应参数：
>     - subTabId = 107
>     - subTabName = "舞蹈"
> - 直播颜值榜对应参数：
>     - subTabId = 101
>     - subTabName = "颜值"
> - 直播国艺榜对应参数：
>     - subTabId = 105
>     - subTabName = "国艺"
> - 直播相亲榜对应参数：
>     - subTabId = 111
>     - subTabName = "相亲"
> - 直播游戏榜对应参数：
>     - subTabId = 106
>     - subTabName = "游戏"
> - 直播二次元榜对应参数：
>     - subTabId = 110
>     - subTabName = "二次元"
> - 直播故事榜对应参数：
>     - subTabId = 104
>     - subTabName = "故事"
> - 直播团播榜对应参数：
>     - subTabId = 113
>     - subTabName = "团播"
> - 直播九宫格榜对应参数：
>     - subTabId = 114
>     - subTabName = "九宫格"
>
> ### 返回:
> - 榜单数据
>
> # [English]
> ### Purpose:
> - Kuaishou live top list
> ### Parameters:
> Get the Kuaishou live top list, support multiple sub-top lists, specific parameters are as follows:
>
> - Corresponding parameters for the live total list:
>     - subTabId = 0
>     - subTabName = None
> - Corresponding parameters for the live music list:
>     - subTabId = 102
>     - subTabName = "Music"
> - Corresponding parameters for the live dance list:
>     - subTabId = 107
>     - subTabName = "Dance"
> - Corresponding parameters for the live beauty list:
>     - subTabId = 101
>     - subTabName = "Beauty"
> - Corresponding parameters for the live national art list:
>     - subTabId = 105
>     - subTabName = "National Art"
> - Corresponding parameters for the live blind date list:
>     - subTabId = 111
>     - subTabName = "Blind Date"
> - Corresponding parameters for the live game list:
>     - subTabId = 106
>     - subTabName = "Game"
> - Corresponding parameters for the live second element list:
>     - subTabId = 110
>     - subTabName = "Second Element"
> - Corresponding parameters for the live story list:
>     - subTabId = 104
>     - subTabName = "Story"
> - Corresponding parameters for the live group broadcast list:
>     - subTabId = 113
>     - subTabName = "Group Broadcast"
> - Corresponding parameters for the live nine-grid list:
>     - subTabId = 114
>     - subTabName = "Nine Grid"
>
> ### Returns:
> - List data
>
> # [示例/Example]
> subTabId = 0
> subTabName = None

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subTabId | query | integer | 否 | 无 | 0 | 无 | 无 |
| subTabName | query | string | 否 | 无 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-magic-face-hot"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_magic_face_hot`

- 摘要：获取魔法表情热门视频/Fetch magic face hot videos
- 能力：热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取快手魔法表情热门视频列表（H5接口）
> ### 参数:
> - magic_face_id: 魔法表情ID
> - pcursor: 分页游标，首页为"0"，后续使用响应中返回的pcursor值
> - count: 每页数量，默认18
> ### 返回:
> - 魔法表情热门视频列表
>
> # [English]
> ### Purpose:
> - Fetch Kuaishou magic face hot videos list (H5 API)
> ### Parameters:
> - magic_face_id: Magic face ID
> - pcursor: Pagination cursor, "0" for first page, use pcursor from response for subsequent pages
> - count: Count per page, default 18
> ### Returns:
> - Magic face hot videos list
>
> # [示例/Example]
> magic_face_id = "11541661"
> pcursor = "0"
> count = 18

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| magic_face_id | query | string | 是 | 无 | 无 | 11541661 | 无 |
| pcursor | query | string | 否 | 无 | 0 | 0 | 无 |
| count | query | integer | 否 | 无 | 18 | 18 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-magic-face-usage"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_magic_face_usage`

- 摘要：获取魔法表情使用人数/Fetch magic face usage count
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取快手魔法表情使用人数（H5接口）
> ### 参数:
> - magic_face_id: 魔法表情ID
> ### 返回:
> - 魔法表情使用人数
>
> # [English]
> ### Purpose:
> - Fetch Kuaishou magic face usage count (H5 API)
> ### Parameters:
> - magic_face_id: Magic face ID
> ### Returns:
> - Magic face usage count
>
> # [示例/Example]
> magic_face_id = "11541661"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| magic_face_id | query | string | 是 | 无 | 无 | 11541661 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-user-v2"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_user_v2`

- 摘要：获取单个用户数据V2/Get single user data V2
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个用户数据 V2
> - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
> ### 参数:
> - user_id: 支持`eid`或`userId`，eid是用户主页链接中的一部分，user_id则可以从不同的接口中获取。
> - 两种用户ID都可以使用，下面是两种用户ID的示例，这两个ID都指向同一个用户：
>     - eid = "3xz63mn6fngqtiq"
>     - userId = "228905802"
> ### 返回:
> - 用户数据
>
> # [English]
> ### Purpose:
> - Fetch single user data V2
> - This API is more expensive, but more stable, please check the price list in the user background for specific prices.
> ### Parameters:
> - user_id: Supports `eid` or `userId`, `eid` is part of the user profile link, and `user_id` can be obtained from different interfaces.
> - Both user IDs can be used, here are examples of the two user IDs, both of which point to the same user:
>     - eid = "3xz63mn6fngqtiq"
>     - userId = "228905802"
> ### Returns:
> - User data
>
> # [示例/Example]
> user_id = "3xz63mn6fngqtiq"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 无 | 无 | 3xz63mn6fngqtiq | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-video"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_video`

- 摘要：视频详情V1/Video detailsV1
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品数据接口 V1。
> ### 参数:
> - photo_id: 作品ID，作品ID可以从分享链接中提取
>     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。
> ### 返回:
> - 视频数据
>
> # [English]
> ### Purpose:
> - Fetch single video data API V1.
> ### Parameters:
> - photo_id: Photo ID, the photo ID can be extracted from the share link
>     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed.
> ### Returns:
> - Video data
>
> # [示例/Example]
> photo_id = "3xhpk3xcf6e4iac"
> photo_id = "5246975215478907538"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| photo_id | query | string | 是 | 无 | 无 | 3xhpk3xcf6e4iac | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-video-by-url"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_video_by_url`

- 摘要：根据链接获取单个作品数据/Fetch single video by URL
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据链接获取单个作品数据，此接口默认使用价格更便宜的V1接口进行请求。
> ### 参数:
> - share_text: 作品链接或分享文本
> ### 返回:
> - 视频数据
>
> # [English]
> ### Purpose:
> - Fetch single video by URL, this API defaults to using the cheaper V1 API for requests.
> ### Parameters:
> - share_text: Photo URL or share text
> ### Returns:
> - Video data
>
> # [示例/Example]
> share_text = "https://v.kuaishou.com/cNYP0Z"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | 是 | 无 | 无 | https://v.kuaishou.com/cNYP0Z | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-video-comment"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_video_comment`

- 摘要：获取单个作品评论数据/Get single video comment data
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品评论数据
> ### 参数:
> - photo_id: 作品ID
>     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。
> - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
> ### 返回:
> - 评论数据
>
> # [English]
> ### Purpose:
> - Fetch single video comment data
> ### Parameters:
> - photo_id: Photo ID
>     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed.
> - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests.
> ### Returns:
> - Comments data
>
> # [示例/Example]
> photo_id = "3x7gxp2zhgjv832"
> pcursor = None

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| photo_id | query | string | 是 | 无 | 无 | 3x7gxp2zhgjv832 | 无 |
| pcursor | query | string | 否 | 无 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-shopping-top-list"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_shopping_top_list`

- 摘要：快手购物榜单/Kuaishou shopping top list
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 快手购物榜单
> ### 参数:
> 获取快手购物榜单，支持多个子榜单，具体参数如下：
>
> - 购物榜单热门主播榜对应参数：
>     - subTabId = 0
>     - subTabName = None
> - 购物榜单热销商品榜对应参数：
>     - subTabId = 102
>     - subTabName = "热销商品"
>
> ### 返回:
> - 榜单数据
>
> # [English]
> ### Purpose:
> - Kuaishou shopping top list
> ### Parameters:
> Get the Kuaishou shopping top list, support multiple sub-top lists, specific parameters are as follows:
>
> - Corresponding parameters for the shopping hot anchor list:
>     - subTabId = 0
>     - subTabName = None
> - Corresponding parameters for the shopping hot selling product list:
>     - subTabId = 102
>     - subTabName = "Hot Selling Product"
>
> ### Returns:
> - List data
>
> # [示例/Example]
> subTabId = 0
> subTabName = None

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subTabId | query | integer | 否 | 无 | 0 | 无 | 无 |
| subTabName | query | string | 否 | 无 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-user-hot-post"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_user_hot_post`

- 摘要：获取用户热门作品数据/Get user hot post data
- 能力：热点/榜单 / 主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户热门作品数据
> ### 参数:
> - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。
> - user_id 可以从获取单个用户数据接口中获取。
> - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get user hot post data
> ### Parameters:
> - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID.
> - user_id can be obtained from the get single user data interface.
> - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests.
> ### Returns:
> - Post data
>
> # [示例/Example]
> user_id = "228905802"
> pcursor = None

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 无 | 无 | 228905802 | 无 |
| pcursor | query | string | 否 | 无 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-user-live-info"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_user_live_info`

- 摘要：获取用户直播信息/Get user live info
- 能力：主页/账号 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户直播信息
> ### 参数:
> - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。
> - user_id 可以从获取单个用户数据接口中获取。
> ### 返回:
> - 直播信息
>
> # [English]
> ### Purpose:
> - Get user live info
> ### Parameters:
> - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID.
> - user_id can be obtained from the get single user data interface.
> ### Returns:
> - Live info
>
> # [示例/Example]
> user_id = "1377082950"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 无 | 无 | 1377082950 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-user-post-v2"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_user_post_v2`

- 摘要：用户视频列表V2/User video list V2
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 用户视频列表 V2
> - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
> ### 参数:
> - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。
> - user_id 可以从获取单个用户数据接口中获取。
> - pcursor: 视频游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
> ### 返回:
> - 视频数据
>
> # [English]
> ### Purpose:
> - User video list V2
> - This API is more expensive, but more stable, please check the price list in the user background for specific prices.
> ### Parameters:
> - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure digital ID.
> - user_id can be obtained from the get single user data interface.
> - pcursor: Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests.
> ### Returns:
> - Videos data
>
> # [示例/Example]
> user_id = "903511772"
> pcursor = None

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | 是 | 无 | 无 | 903511772 | 无 |
| pcursor | query | string | 否 | 无 | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-videos-batch"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_videos_batch`

- 摘要：快手批量视频查询接口/Kuaishou batch video query API
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get`

#### 说明

> # [中文]
> ### 用途:
> - 批量获取多个作品数据，单次请求最多支持40个视频ID。
> - 如果此接口连续请求失败，可以尝试使用价格更昂贵的V2接口进行冗余请求。
> - 此接口收费标准默认为：40 * 0.001 = 0.04 美元/次。
> ### 参数:
> - photo_ids: 作品ID列表，多个ID用英文逗号分隔，单次最多40个
>     - 格式备注：支持纯数字版本的ID，也支持短字符串版本（eID）的ID，两种ID可以混合使用。
> ### 返回:
> - 视频数据列表
>
> # [English]
> ### Purpose:
> - Batch fetch multiple video data, supports up to 40 video IDs per request.
> - If this API continuously fails, you can try to use the more expensive V2 API for redundant requests.
> - The default charging standard for this API is: 40 * 0.001 = 0.04 USD/time.
> ### Parameters:
> - photo_ids: Photo ID list, multiple IDs separated by commas, max 40 per request
>     - Format note: Supports both pure digital version IDs and short string version (eID) IDs, both types can be mixed.
> ### Returns:
> - Video data list
>
> # [示例/Example]
> photo_ids = "5228960823332207296,5196309727975443273,5222486898325987583"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| photo_ids | query | string | 是 | 多个作品ID用逗号分隔，单次最多40个/Multiple photo IDs separated by commas, max 40 per request | 无 | 5228960823332207296,5196309727975443273,5222486898325987583 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-generate-kuaishou-share-link"></a>
### `GET /api/u1/v1/kuaishou/app/generate_kuaishou_share_link`

- 摘要：生成快手分享链接/Generate Kuaishou share link
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成快手分享链接
> ### 参数:
> - shareObjectId: 作品ID
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate Kuaishou share link
> ### Parameters:
> - photo_id: Photo ID
> ### Returns:
> - Share link
>
> # [示例/Example]
> shareObjectId = "3xg5wjqdtekbb3u"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shareObjectId | query | string | 是 | 无 | 无 | 3xg5wjqdtekbb3u | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-search-comprehensive"></a>
### `GET /api/u1/v1/kuaishou/app/search_comprehensive`

- 摘要：综合搜索/Comprehensive search
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get`

#### 说明

> # [中文]
> ### 用途:
> - 快手综合搜索接口，支持搜索视频、用户等内容，并提供多维度筛选功能。
> ### 参数:
> - keyword: 搜索关键词（必填）
> - pcursor: 分页游标，首次请求为空，后续使用响应中的pcursor值
> - sort_type: 排序方式
>     - all: 综合排序（默认）
>     - newest: 最新发布
>     - most_likes: 最多点赞
> - publish_time: 发布时间筛选
>     - all: 全部时间（默认）
>     - one_day: 近一日
>     - one_week: 近一周
>     - one_month: 近一月
> - duration: 作品时长筛选
>     - all: 全部时长（默认）
>     - under_1_min: 1分钟以内
>     - 1_to_5_min: 1-5分钟
>     - over_5_min: 5分钟以上
> - search_scope: 搜索范围
>     - all: 全部（默认）
> ### 返回:
> - 搜索结果数据
>
> # [English]
> ### Purpose:
> - Kuaishou comprehensive search API, supports searching videos, users, etc., and provides multi-dimensional filtering.
> ### Parameters:
> - keyword: Search keyword (required)
> - pcursor: Pagination cursor, empty for first request, use pcursor from response for subsequent pages
> - sort_type: Sort type
>     - all: Comprehensive sort (default)
>     - newest: Latest release
>     - most_likes: Most likes
> - publish_time: Publish time filter
>     - all: All time (default)
>     - one_day: Last day
>     - one_week: Last week
>     - one_month: Last month
> - duration: Duration filter
>     - all: All duration (default)
>     - under_1_min: Under 1 minute
>     - 1_to_5_min: 1-5 minutes
>     - over_5_min: Over 5 minutes
> - search_scope: Search scope
>     - all: All (default)
> ### Returns:
> - Search result data
>
> # [示例/Example]
> keyword = "汽车之家"
> sort_type = "most_likes"
> publish_time = "one_week"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 无 | 无 | 汽车之家 | 无 |
| pcursor | query | string | 否 | 无 | 无 | 无 | 无 |
| sort_type | query | string | 否 | 可选值: all(综合排序), newest(最新发布), most_likes(最多点赞) | all | 无 | 无 |
| publish_time | query | string | 否 | 可选值: all(全部), one_day(近一日), one_week(近一周), one_month(近一月) | all | 无 | 无 |
| duration | query | string | 否 | 可选值: all(全部), under_1_min(1分钟以内), 1_to_5_min(1-5分钟), over_5_min(5分钟以上) | all | 无 | 无 |
| search_scope | query | string | 否 | 可选值: all(全部) | all | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-search-user-v2"></a>
### `GET /api/u1/v1/kuaishou/app/search_user_v2`

- 摘要：搜索用户V2/Search user V2
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_user_v2_api_v1_kuaishou_app_search_user_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索用户 V2
> - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
> ### 参数:
> - keyword: 搜索关键词
> - page: 用户页数，从1开始
> ### 返回:
> - 用户数据
>
> # [English]
> ### Purpose:
> - Search user V2
> - This API is more expensive, but more stable, please check the price list in the user background for specific prices.
> ### Parameters:
> - keyword: Search keyword
> - page: User page number, starting from 1
> ### Returns:
> - User data
>
> # [示例/Example]
> keyword = "人工智能"
> page = "1"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 无 | 无 | 人工智能 | 无 |
| page | query | string | 否 | 无 | 1 | 无 | 无 |

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

<a id="get-api-u1-v1-kuaishou-app-search-video-v2"></a>
### `GET /api/u1/v1/kuaishou/app/search_video_v2`

- 摘要：搜索视频V2/Search video V2
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`search_video_v2_api_v1_kuaishou_app_search_video_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索视频 V2
> - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
> ### 参数:
> - keyword: 搜索关键词
> - page: 视频页数，从1开始
> ### 返回:
> - 视频数据
>
> # [English]
> ### Purpose:
> - Search video V2
> - This API is more expensive, but more stable, please check the price list in the user background for specific prices.
> ### Parameters:
> - keyword: Search keyword
> - page: Page number, starting from 1
> ### Returns:
> - Videos data
>
> # [示例/Example]
> keyword = "人工智能"
> page = "1"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 无 | 无 | 人工智能 | 无 |
| page | query | string | 否 | 无 | 1 | 无 | 无 |

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
