# Kuaishou-App-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/kuaishou-app-api.md`](../api-tags/kuaishou-app-api.md)
- Current contract file: `api-contracts/kuaishou-app-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `20`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(快手App数据接口/Kuaishou-App-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-kuaishou-app-fetch-brand-top-list"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_brand_top_list`

- Summary: 快手品牌榜单/Kuaishou brand top list
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_brand_top_list_api_v1_kuaishou_app_fetch_brand_top_list_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subTabId | query | integer | No | None | 0 | None | None |
| subTabName | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-hot-board-categories"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_hot_board_categories`

- Summary: 快手热榜分类/Kuaishou hot categories
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_board_categories_api_v1_kuaishou_app_fetch_hot_board_categories_get`

#### Notes

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

<a id="get-api-u1-v1-kuaishou-app-fetch-hot-board-detail"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_hot_board_detail`

- Summary: 快手热榜详情/Kuaishou hot board detail
- Capabilities: trends / rankings / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_board_detail_api_v1_kuaishou_app_fetch_hot_board_detail_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| boardType | query | integer | No | None | 1 | None | None |
| boardId | query | integer | No | None | 1 | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-hot-search-person"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_hot_search_person`

- Summary: 快手热搜人物榜单/Kuaishou hot search person board
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hot_search_person_api_v1_kuaishou_app_fetch_hot_search_person_get`

#### Notes

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

<a id="get-api-u1-v1-kuaishou-app-fetch-live-top-list"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_live_top_list`

- Summary: 快手直播榜单/Kuaishou live top list
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_top_list_api_v1_kuaishou_app_fetch_live_top_list_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subTabId | query | integer | No | None | 0 | None | None |
| subTabName | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-magic-face-hot"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_magic_face_hot`

- Summary: 获取魔法表情热门视频/Fetch magic face hot videos
- Capabilities: trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_magic_face_hot_api_v1_kuaishou_app_fetch_magic_face_hot_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| magic_face_id | query | string | Yes | None | None | 11541661 | None |
| pcursor | query | string | No | None | 0 | 0 | None |
| count | query | integer | No | None | 18 | 18 | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-magic-face-usage"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_magic_face_usage`

- Summary: 获取魔法表情使用人数/Fetch magic face usage count
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_magic_face_usage_api_v1_kuaishou_app_fetch_magic_face_usage_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| magic_face_id | query | string | Yes | None | None | 11541661 | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-user-v2"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_user_v2`

- Summary: 获取单个用户数据V2/Get single user data V2
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_user_v2_api_v1_kuaishou_app_fetch_one_user_v2_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | None | None | 3xz63mn6fngqtiq | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-video"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_video`

- Summary: 视频详情V1/Video detailsV1
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v1_api_v1_kuaishou_app_fetch_one_video_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| photo_id | query | string | Yes | None | None | 3xhpk3xcf6e4iac | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-video-by-url"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_video_by_url`

- Summary: 根据链接获取单个作品数据/Fetch single video by URL
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_by_share_text_api_v1_kuaishou_app_fetch_one_video_by_url_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_text | query | string | Yes | None | None | https://v.kuaishou.com/cNYP0Z | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-one-video-comment"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_one_video_comment`

- Summary: 获取单个作品评论数据/Get single video comment data
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comment_api_v1_kuaishou_app_fetch_one_video_comment_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| photo_id | query | string | Yes | None | None | 3x7gxp2zhgjv832 | None |
| pcursor | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-shopping-top-list"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_shopping_top_list`

- Summary: 快手购物榜单/Kuaishou shopping top list
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shopping_top_list_api_v1_kuaishou_app_fetch_shopping_top_list_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| subTabId | query | integer | No | None | 0 | None | None |
| subTabName | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-user-hot-post"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_user_hot_post`

- Summary: 获取用户热门作品数据/Get user hot post data
- Capabilities: trends / rankings / profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_hot_post_api_v1_kuaishou_app_fetch_user_hot_post_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | None | None | 228905802 | None |
| pcursor | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-user-live-info"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_user_live_info`

- Summary: 获取用户直播信息/Get user live info
- Capabilities: profiles / accounts / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_live_info_api_v1_kuaishou_app_fetch_user_live_info_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | None | None | 1377082950 | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-user-post-v2"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_user_post_v2`

- Summary: 用户视频列表V2/User video list V2
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_v2_api_v1_kuaishou_app_fetch_user_post_v2_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | None | None | 903511772 | None |
| pcursor | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-fetch-videos-batch"></a>
### `GET /api/u1/v1/kuaishou/app/fetch_videos_batch`

- Summary: 快手批量视频查询接口/Kuaishou batch video query API
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_videos_batch_api_v1_kuaishou_app_fetch_videos_batch_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| photo_ids | query | string | Yes | 多个作品ID用逗号分隔，单次最多40个/Multiple photo IDs separated by commas, max 40 per request | None | 5228960823332207296,5196309727975443273,5222486898325987583 | None |

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

<a id="get-api-u1-v1-kuaishou-app-generate-kuaishou-share-link"></a>
### `GET /api/u1/v1/kuaishou/app/generate_kuaishou_share_link`

- Summary: 生成快手分享链接/Generate Kuaishou share link
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_kuaishou_share_link_api_v1_kuaishou_app_generate_kuaishou_share_link_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shareObjectId | query | string | Yes | None | None | 3xg5wjqdtekbb3u | None |

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

<a id="get-api-u1-v1-kuaishou-app-search-comprehensive"></a>
### `GET /api/u1/v1/kuaishou/app/search_comprehensive`

- Summary: 综合搜索/Comprehensive search
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_comprehensive_api_v1_kuaishou_app_search_comprehensive_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | None | None | 汽车之家 | None |
| pcursor | query | string | No | None | None | None | None |
| sort_type | query | string | No | 可选值: all(综合排序), newest(最新发布), most_likes(最多点赞) | all | None | None |
| publish_time | query | string | No | 可选值: all(全部), one_day(近一日), one_week(近一周), one_month(近一月) | all | None | None |
| duration | query | string | No | 可选值: all(全部), under_1_min(1分钟以内), 1_to_5_min(1-5分钟), over_5_min(5分钟以上) | all | None | None |
| search_scope | query | string | No | 可选值: all(全部) | all | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-search-user-v2"></a>
### `GET /api/u1/v1/kuaishou/app/search_user_v2`

- Summary: 搜索用户V2/Search user V2
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_user_v2_api_v1_kuaishou_app_search_user_v2_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | None | None | 人工智能 | None |
| page | query | string | No | None | 1 | None | None |

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

<a id="get-api-u1-v1-kuaishou-app-search-video-v2"></a>
### `GET /api/u1/v1/kuaishou/app/search_video_v2`

- Summary: 搜索视频V2/Search video V2
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_video_v2_api_v1_kuaishou_app_search_video_v2_get`

#### Notes

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

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | None | None | 人工智能 | None |
| page | query | string | No | None | 1 | None | None |

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
