# Douyin-Web-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/douyin-web-api.md`](../api-tags/douyin-web-api.md)
- 当前契约文件：`api-contracts/douyin-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`76`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(抖音Web数据接口/Douyin-Web-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-douyin-web-douyin-live-room"></a>
### `GET /api/u1/v1/douyin/web/douyin_live_room`

- 摘要：提取直播间弹幕/Extract live room danmaku
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`douyin_live_room_api_v1_douyin_web_douyin_live_room_get`

#### 说明

> # [中文]
> ### 用途:
> - 提取直播间弹幕
> - 该接口已不再提供线上服务，需要自行购买源代码后在本地部署使用，购买源代码请在Discord服务器联系管理员，Discord邀请链接：https://discord.gg/aMEAS8Xsvz
> #### 价格:
> - 每10条数据消耗0.001$，支持阶梯式计费折扣。
> ### 参数:
> - live_room_url: 直播间链接
> - danmaku_type: 消息类型
>     - WebcastRoomMessage：直播间消息
>     - WebcastLikeMessage：点赞消息
>     - WebcastMemberMessage：成员消息
>     - WebcastChatMessage：聊天消息
>     - WebcastGiftMessage：礼物消息
>     - WebcastSocialMessage：社交消息
>     - WebcastRoomUserSeqMessage：用户序列消息
>     - WebcastUpdateFanTicketMessage：更新粉丝消息
>     - WebcastCommonTextMessage：常规文本消息
>     - WebcastMatchAgainstScoreMessage：比赛得分消息
>     - WebcastFansclubMessage：粉丝俱乐部消息
>     - WebcastRanklistHourEntranceMessage：排行榜小时入口消息
>     - WebcastRoomStatsMessage：直播间统计消息
>     - WebcastLiveShoppingMessage: 直播购物消息
>     - WebcastLiveEcomGeneralMessage: 直播电商通用消息
>     - WebcastProductChangeMessage: 直播商品变更消息
>     - WebcastRoomStreamAdaptationMessage: 直播间流适配消息
>     - WebcastNotifyEffectMessage: 通知效果消息
>     - WebcastLightGiftMessage: 亮礼物消息
>     - WebcastProfitInteractionScoreMessage: 收益互动分消息
>     - WebcastRoomRankMessage: 直播间排行消息
> ### 返回:
> - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。
>
> # [English]
> ### Purpose:
> - Extract live room danmaku
> - This interface is no longer available online, you need to purchase the source code and deploy it locally for use. To purchase the source code, please contact the administrator in the Discord server. Discord invite link: https://discord.gg/aMEAS8Xsvz
> #### Price:
> - 0.001$ per 10 data, support tiered billing discounts.
> ### Parameters:
> - live_room_url: Live room link
> - danmaku_type: Message type
>     - WebcastRoomMessage: Live room message
>     - WebcastLikeMessage: Like message
>     - WebcastMemberMessage: Member message
>     - WebcastChatMessage: Chat message
>     - WebcastGiftMessage: Gift message
>     - WebcastSocialMessage: Social message
>     - WebcastRoomUserSeqMessage: User sequence message
>     - WebcastUpdateFanTicketMessage: Update fan message
>     - WebcastCommonTextMessage: Common text message
>     - WebcastMatchAgainstScoreMessage: Match score message
>     - WebcastFansclubMessage: Fans club message
>     - WebcastRanklistHourEntranceMessage: Ranking list hour entrance message
>     - WebcastRoomStatsMessage: Live room statistics message
>     - WebcastLiveShoppingMessage: Live shopping message
>     - WebcastLiveEcomGeneralMessage: Live e-commerce general message
>     - WebcastProductChangeMessage: Live product change message
>     - WebcastRoomStreamAdaptationMessage: Live room stream adaptation message
>     - WebcastNotifyEffectMessage: Notification effect message
>     - WebcastLightGiftMessage: Light gift message
>     - WebcastProfitInteractionScoreMessage: Profit interaction score message
>     - WebcastRoomRankMessage: Live room ranking message
> ### Return:
> - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get the danmaku data, this interface does not return the danmaku data.

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| live_room_url | query | string | 是 | 直播间链接/Live room link | 无 | https://live.douyin.com/834624950943 | 无 |
| danmaku_type | query | string | 是 | 消息类型/Message type | 无 | WebcastRoomMessage | 无 |

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

<a id="get-api-u1-v1-douyin-web-encrypt-uid-to-sec-user-id"></a>
### `GET /api/u1/v1/douyin/web/encrypt_uid_to_sec_user_id`

- 摘要：加密用户uid到sec_user_id/Encrypt user uid to sec_user_id
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`encrypt_uid_to_sec_user_id_api_v1_douyin_web_encrypt_uid_to_sec_user_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 加密用户uid到sec_user_id
> ### 参数:
> - uid: 用户uid，也就是抖音号的short_id
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Encrypt user uid to sec_user_id
> ### Parameters:
> - uid: User uid, which is the short_id of the Douyin number
> ### Return:
> - User information
>
> # [示例/Example]
> uid = "1673937488185292"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户uid(short_id)/User uid(short_id) | 无 | 1673937488185292 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-batch-user-profile-v1"></a>
### `GET /api/u1/v1/douyin/web/fetch_batch_user_profile_v1`

- 摘要：获取批量用户信息(最多10个)/Get batch user profile (up to 10)
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_batch_user_profile_v1_api_v1_douyin_web_fetch_batch_user_profile_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取批量用户信息，最多支持10个用户
> ### 参数:
> - sec_user_ids: 用户sec_user_id列表，用逗号分隔，最多10个
> ### 返回:
> - 批量用户信息
>
> # [English]
> ### Purpose:
> - Get batch user profile, up to 10 users
> ### Parameters:
> - sec_user_ids: User sec_user_id list, separated by commas, up to 10
> ### Return:
> - Batch user profile
>
> # [示例/Example]
> sec_user_ids = "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_ids | query | string | 是 | 用户sec_user_id列表，用逗号分隔/User sec_user_id list, separated by commas | 无 | MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQ… | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-batch-user-profile-v2"></a>
### `GET /api/u1/v1/douyin/web/fetch_batch_user_profile_v2`

- 摘要：获取批量用户信息(最多50个)/Get batch user profile (up to 50)
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_batch_user_profile_v2_api_v1_douyin_web_fetch_batch_user_profile_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取批量用户信息，最多支持50个用户
> ### 参数:
> - sec_user_ids: 用户sec_user_id列表，用逗号分隔，最多50个
> ### 返回:
> - 批量用户信息
>
> # [English]
> ### Purpose:
> - Get batch user profile, up to 50 users
> ### Parameters:
> - sec_user_ids: User sec_user_id list, separated by commas, up to 50
> ### Return:
> - Batch user profile
>
> # [示例/Example]
> sec_user_ids = "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_ids | query | string | 是 | 用户sec_user_id列表，用逗号分隔/User sec_user_id list, separated by commas | 无 | MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE,MS4wLjABAAAAW9FWcqS7RdQ… | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-cartoon-aweme"></a>
### `GET /api/u1/v1/douyin/web/fetch_cartoon_aweme`

- 摘要：二次元作品推荐/Anime Video
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_cartoon_aweme_api_v1_douyin_web_fetch_cartoon_aweme_get`

#### 说明

> # [中文]
> ### 用途:
> - 二次元作品
> ### 参数:
> - count: 每页数量，默认为16
> - refresh_index: 翻页索引，默认为1
> - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
> - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### 返回:
> - 二次元作品数据
>
> # [English]
> ### Purpose:
> - Cartoon Video
> ### Parameters:
> - count: Number per page, default is 16
> - refresh_index: Paging index, default is 1
> - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging
> - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### Return:
> - Cartoon Video data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| count | query | integer | 是 | 每页数量/Number per page | 无 | 16 | 无 |
| refresh_index | query | integer | 否 | 翻页索引/Paging index | 1 | 无 | 无 |
| cookie | query | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-web-fetch-challenge-posts"></a>
### `POST /api/u1/v1/douyin/web/fetch_challenge_posts`

- 摘要：话题作品/Challenge Posts
- 能力：作品详情 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_challenge_posts_api_v1_douyin_web_fetch_challenge_posts_post`

#### 说明

> # [中文]
> ### 用途:
> - 话题作品
> ### 参数:
> - challenge_id: 话题id
> - sort_type: 排序类型
>     - 0:综合排序 1:最热排序 2:最新排序
> - cursor: 游标
> - count: 数量
> - cookie: 用户自行提供的Cookie，用于获取更多数据。
> ### 返回:
> - 话题作品
>
> # [English]
> ### Purpose:
> - Challenge Posts
> ### Parameters:
> - challenge_id: Challenge id
> - sort_type: Sort type
>     - 0: Comprehensive sorting 1: Hottest sorting 2: Latest sorting
> - cursor: Cursor
> - count: Number
> - cookie: User provided Cookie, used to get more data
> ### Return:
> - Challenge Posts
>
> # [示例/Example]
> challenge_id = "1750525814851611"
> sort_type = 0
> offset = 0
> cursor = 0
> count = 20

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`challenge_id`:string, `sort_type`:integer, `cursor`:integer, `count`:integer, `cookie`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| challenge_id | string | 否 | 话题ID/Challenge ID | 1608846127610893 | 无 | 无 |
| sort_type | integer | 否 | 排序类型/Sort type | 0 | 无 | 无 |
| cursor | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| count | integer | 否 | 数量/Count | 20 | 无 | 无 |
| cookie | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-douyin-web-guest-cookie"></a>
### `GET /api/u1/v1/douyin/web/fetch_douyin_web_guest_cookie`

- 摘要：获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_douyin_web_guest_cookie_api_v1_douyin_web_fetch_douyin_web_guest_cookie_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音Web的游客Cookie
> - 可以用于爬取抖音Web的数据，如用户作品、合辑作品等。
> - 可以固定身份避免部分接口重复数据。
> - 请注意：游客Cookie无法爬取所有数据，有一定的限制。
> - 可以配合开源项目使用此接口实现抖音Web的数据爬取。
> ### 参数:
> - user_agent: 用户浏览器代理
> ### 返回:
> - 游客Cookie
>
> # [English]
> ### Purpose:
> - Get the guest Cookie of Douyin Web
> - Can be used to crawl data of Douyin Web, such as user videos, mix videos, etc.
> - Can fix identity to avoid duplicate data for some interfaces.
> - Please note: Guest Cookie cannot crawl all data, there are certain restrictions.
> - Can be used with open source projects to implement data crawling of Douyin Web using this interface.
> ### Parameters:
> - user_agent: User browser agent
> ### Return:
> - Guest Cookie
>
> # [示例/Example]
> user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_agent | query | string | 是 | 用户浏览器代理/User browser agent | 无 | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko… | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-food-aweme"></a>
### `GET /api/u1/v1/douyin/web/fetch_food_aweme`

- 摘要：美食作品推荐/Food Video
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_cartoon_aweme_api_v1_douyin_web_fetch_food_aweme_get`

#### 说明

> # [中文]
> ### 用途:
> - 美食作品
> ### 参数:
> - count: 每页数量，默认为16
> - refresh_index: 翻页索引，默认为1
> - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
> - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### 返回:
> - 美食作品数据
>
> # [English]
> ### Purpose:
> - Food Video
> ### Parameters:
> - count: Number per page, default is 16
> - refresh_index: Paging index, default is 1
> - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging
> - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### Return:
> - Food Video data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| count | query | integer | 是 | 每页数量/Number per page | 无 | 16 | 无 |
| refresh_index | query | integer | 否 | 翻页索引/Paging index | 1 | 无 | 无 |
| cookie | query | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-game-aweme"></a>
### `GET /api/u1/v1/douyin/web/fetch_game_aweme`

- 摘要：游戏作品推荐/Game Video
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_game_aweme_api_v1_douyin_web_fetch_game_aweme_get`

#### 说明

> # [中文]
> ### 用途:
> - 知识作品
> ### 参数:
> - count: 每页数量，默认为16
> - refresh_index: 翻页索引，默认为1
> - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
> - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### 返回:
> - 游戏作品数据
>
> # [English]
> ### Purpose:
> - Knowledge Video
> ### Parameters:
> - count: Number per page, default is 16
> - refresh_index: Paging index, default is 1
> - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging
> - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### Return:
> - Game Video data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| count | query | integer | 是 | 每页数量/Number per page | 无 | 16 | 无 |
| refresh_index | query | integer | 否 | 翻页索引/Paging index | 1 | 无 | 无 |
| cookie | query | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-general-search-result"></a>
### `GET /api/u1/v1/douyin/web/fetch_general_search_result`

- 摘要：[已弃用/Deprecated] 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords
- 能力：搜索
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_general_search_result_api_v1_douyin_web_fetch_general_search_result_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212773e0
> ### 用途:
> - 获取指定关键词的综合搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次。
> - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212773e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> - sort_type: 0:综合排序 1:最多点赞 2:最新发布
> - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年
> - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上
> -search_range: 0:不限 1:最近看过 2:还未看过 3:关注的人
> -content_type: 0:不限 1:视频 2:图集
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> ### 返回:
> - 综合搜索结果
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212773e0
> ### Purpose:
> - Get comprehensive search results of specified keywords, this interface may fail, if it fails, please use the same parameters to request 1-3 times again.
> - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212773e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
> - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year
> - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
> - search_range: 0: Unlimited 1: Recently viewed 2: Not yet viewed 3: Followed
> - content_type: 0: Unlimited 1: Video 2: Album
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
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

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| sort_type | query | string | 否 | 排序类型/Sort type | 0 | 无 | 无 |
| publish_time | query | string | 否 | 发布时间/Publish time | 0 | 无 | 无 |
| filter_duration | query | string | 否 | 视频时长/Duration filter | 0 | 无 | 无 |
| search_range | query | string | 否 | 搜索范围/Search range | 0 | 无 | 无 |
| content_type | query | string | 否 | 内容类型/Content type | 0 | 无 | 无 |
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

<a id="get-api-u1-v1-douyin-web-fetch-home-feed"></a>
### `GET /api/u1/v1/douyin/web/fetch_home_feed`

- 摘要：获取首页推荐数据/Get home feed data
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_home_feed_api_v1_douyin_web_fetch_home_feed_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取首页推荐数据
> ### 参数:
> - count: 数量，默认为10，建议保持不变。
> - refresh_index: 翻页索引，默认为0，然后每次增加1用于翻页。
> ### 返回:
> - Feed数据
>
> # [English]
> ### Purpose:
> - Get home feed data
> ### Parameters:
> - count: Number, default is 10, it is recommended to keep it unchanged.
> - refresh_index: Paging index, default is 0, then increase by 1 each time for paging.
> ### Return:
> - Feed data
>
> # [示例/Example]
> count = 10
> refresh_index = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| count | query | integer | 否 | 数量/Number | 10 | 无 | 无 |
| refresh_index | query | integer | 否 | 翻页索引/Paging index | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-hot-search-result"></a>
### `GET /api/u1/v1/douyin/web/fetch_hot_search_result`

- 摘要：获取抖音热榜数据/Get Douyin hot search results
- 能力：搜索 / 热点/榜单
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_search_result_api_v1_douyin_web_fetch_hot_search_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取抖音热榜数据
> ### 返回:
> - 热榜数据
>
> # [English]
> ### Purpose:
> - Get Douyin hot search results
> ### Return:
> - Hot search results

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

<a id="get-api-u1-v1-douyin-web-fetch-knowledge-aweme"></a>
### `GET /api/u1/v1/douyin/web/fetch_knowledge_aweme`

- 摘要：知识作品推荐/Knowledge Video
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_knowledge_aweme_api_v1_douyin_web_fetch_knowledge_aweme_get`

#### 说明

> # [中文]
> ### 用途:
> - 知识作品
> ### 参数:
> - count: 每页数量，默认为16
> - refresh_index: 翻页索引，默认为1
> - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
> - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### 返回:
> - 知识作品数据
>
> # [English]
> ### Purpose:
> - Knowledge Video
> ### Parameters:
> - count: Number per page, default is 16
> - refresh_index: Paging index, default is 1
> - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging
> - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### Return:
> - Knowledge Video data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| count | query | integer | 是 | 每页数量/Number per page | 无 | 16 | 无 |
| refresh_index | query | integer | 否 | 翻页索引/Paging index | 1 | 无 | 无 |
| cookie | query | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-live-gift-ranking"></a>
### `GET /api/u1/v1/douyin/web/fetch_live_gift_ranking`

- 摘要：获取直播间送礼用户排行榜/Get live room gift user ranking
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_gift_ranking_api_v1_douyin_web_fetch_live_gift_ranking_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取直播间送礼用户排行榜
> ### 参数:
> - room_id: 直播间room_id
> - rank_type: 排行类型，默认为30不用修改。
> ### 返回:
> - 排行榜数据
>
> # [English]
> ### Purpose:
> - Get live room gift user ranking
> ### Parameters:
> - room_id: Room room_id
> - rank_type: Leaderboard type, default is 30, no need to modify.
> ### Return:
> - Leaderboard data
>
> # [示例/Example]
> room_id = "7356585666190461731"
> rank_type = 30

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间room_id/Room room_id | 无 | 7356585666190461731 | 无 |
| rank_type | query | integer | 否 | 排行类型/Leaderboard type | 30 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-live-im-fetch"></a>
### `GET /api/u1/v1/douyin/web/fetch_live_im_fetch`

- 摘要：抖音直播间弹幕参数获取/Douyin live room danmaku parameters
- 能力：直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_im_fetch_api_v1_douyin_web_fetch_live_im_fetch_get`

#### 说明

> # [中文]
> ### 用途:
> - 抖音直播间弹幕参数获取
> ### 参数:
> - room_id: 直播间号
> - user_unique_id: 用户唯一ID
>
> ### 返回:
> - 弹幕参数数据
>
> # [English]
> ### Purpose:
> - Douyin live room danmaku parameters
> ### Parameters:
> - room_id: Live room id
> - user_unique_id: User unique ID
>
> ### Return:
> - Danmaku parameter data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间号/Live room id | 无 | 7382517534467115826 | 无 |
| user_unique_id | query | string | 是 | 用户唯一ID/User unique ID | 无 | 7382524529011246630 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-live-room-product-result"></a>
### `GET /api/u1/v1/douyin/web/fetch_live_room_product_result`

- 摘要：抖音直播间商品信息/Douyin live room product information
- 能力：电商 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_room_product_result_api_v1_douyin_web_fetch_live_room_product_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 抖音直播间商品信息
> ### 参数:
> - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie，如获取失败请手动过一次验证码)
> - room_id: 直播间room_id
> - author_id: 作者id
> - offset: 偏移量
> - limit: 数量
> ### 返回:
> - 商品信息
> ### 备注:
> author_id的获取方法：
>     1. 通过用户的sec_user_id获取用户信息接口获取uid字段即为author_id。
>     2. 通过直播间room_id获取直播间信息接口获取author_id字段。
> roon_id不是固定不变的，每次开播都会变化。
>
> # [English]
> ### Purpose:
> - Douyin live room product information
> ### Parameters:
> - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie, if the acquisition fails, please manually pass the captcha code once)
> - room_id: Room room_id
> - author_id: Author id
> - offset: Offset
> - limit: Number
> ### Return:
> - Product information
> ### Note:
> The method to obtain author_id:
>     1. Obtain the uid field as author_id through the user information interface by sec_user_id.
>     2. Obtain the author_id field through the live room information interface by room_id.
> The roon_id is not fixed, it changes every time the live broadcast starts.
>
> # [示例/Example]
> cookie = "YOUR_COOKIE"
> room_id = "7356742011975715619"
> author_id = "2207432981615527"
> offset = 0
> limit = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间room_id/Room room_id | 无 | 7360830184578091776 | 无 |
| author_id | query | string | 是 | 作者id/Author id | 无 | 1714858898241277 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| limit | query | integer | 否 | 数量/Number | 20 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-live-search-result"></a>
### `GET /api/u1/v1/douyin/web/fetch_live_search_result`

- 摘要：[已弃用/Deprecated] 获取指定关键词的直播搜索结果/Get live search results of specified keywords
- 能力：搜索 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_live_search_result_api_v1_douyin_web_fetch_live_search_result_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212789e0
> ### 用途:
> - 获取指定关键词的直播搜索结果
> - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212789e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> ### 返回:
> - 直播搜索结果
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212789e0
> ### Purpose:
> - Get live search results of specified keywords
> - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212789e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> ### Return:
> - Live search results
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

<a id="post-api-u1-v1-douyin-web-fetch-multi-video"></a>
### `POST /api/u1/v1/douyin/web/fetch_multi_video`

- 摘要：批量获取视频信息/Batch Get Video Information
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_api_v1_douyin_web_fetch_multi_video_post`

#### 说明

> # [中文]
> ### 用途:
> - 批量获取视频信息，支持图文、视频等，一次性最多支持50个视频，此接口收费固定价格为0.001$ * 50 = 0.05$一次。
> - 若此接口失效，请使用APP接口替代。
> ### 参数:
> - aweme_ids: 作品id列表，最多支持50个作品id。
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Batch Get Video Information, support photo, video, etc., up to 50 videos at a time, this interface charges a fixed price of 0.001$ * 50 = 0.05$ each time.
> - If this interface fails, please use the APP interface instead.
> ### Parameters:
> - aweme_ids: List of video ids, up to 50 video ids are supported.
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_ids = ["7372484719365098803", "7126745726494821640", "7372484719365098803", "7126745726494821640", "7372484719365098803", "7126745726494821640", "7372484719365098803", "7126745726494821640", "7372484719365098803", "7126745726494821640"]

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

<a id="post-api-u1-v1-douyin-web-fetch-multi-video-high-quality-play-url"></a>
### `POST /api/u1/v1/douyin/web/fetch_multi_video_high_quality_play_url`

- 摘要：批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_multi_video_high_quality_play_url_api_v1_douyin_web_fetch_multi_video_high_quality_play_url_post`

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

<a id="get-api-u1-v1-douyin-web-fetch-music-aweme"></a>
### `GET /api/u1/v1/douyin/web/fetch_music_aweme`

- 摘要：音乐作品推荐/Music Video
- 能力：音乐/音频
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_cartoon_aweme_api_v1_douyin_web_fetch_music_aweme_get`

#### 说明

> # [中文]
> ### 用途:
> - 音乐作品
> ### 参数:
> - count: 每页数量，默认为16
> - refresh_index: 翻页索引，默认为1
> - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
> - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### 返回:
> - 音乐作品数据
>
> # [English]
> ### Purpose:
> - Music Video
> ### Parameters:
> - count: Number per page, default is 16
> - refresh_index: Paging index, default is 1
> - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging
> - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### Return:
> - Music Video data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| count | query | integer | 是 | 每页数量/Number per page | 无 | 16 | 无 |
| refresh_index | query | integer | 否 | 翻页索引/Paging index | 1 | 无 | 无 |
| cookie | query | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-one-video"></a>
### `GET /api/u1/v1/douyin/web/fetch_one_video`

- 摘要：获取单个作品数据/Get single video data
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_api_v1_douyin_web_fetch_one_video_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品数据 V1，若此接口失效，请使用 `/fetch_one_video_v2` 接口，或使用APP接口。
> ### 参数:
> - aweme_id: 作品id
> - need_anchor_info: 是否需要锚点信息，默认为False，开启后会看到一些有关视频的锚点信息，如地理位置，商户信息，商品橱窗等，可能会增加接口响应时间。
> - 如果不需要锚点信息，建议保持默认值False，如果接口报错，可以尝试关闭此参数。
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data V1, if this interface fails, please use the `/fetch_one_video_v2` interface, or use the APP interface.
> ### Parameters:
> - aweme_id: Video id
> - need_anchor_info: Whether anchor information is needed, default is False, enabling it will show some anchor information about the video, such as location, merchant information, product showcase, etc., which may increase the interface response time.
> - If anchor information is not needed, it is recommended to keep the default value False, if the interface reports an error, you can try to turn off this parameter.
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_id = "7372484719365098803"
> need_anchor_info = False

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7372484719365098803 | 无 |
| need_anchor_info | query | boolean | 否 | 是否需要锚点信息/Whether anchor information is needed | false | false | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-one-video-by-share-url"></a>
### `GET /api/u1/v1/douyin/web/fetch_one_video_by_share_url`

- 摘要：根据分享链接获取单个作品数据/Get single video data by sharing link
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_by_share_url_api_v1_douyin_web_fetch_one_video_by_share_url_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据分享链接获取单个作品数据 （本质上基于 `/fetch_one_video` 接口实现，建议有能力自行获取视频ID以提升接口响应速度）
> - 返回的视频画质比APP接口高一些，但是响应字段没有APP接口多。
> ### 参数:
> - share_url: 分享链接
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data by sharing link (Essentially implemented based on the `/fetch_one_video` interface, it is recommended to obtain the video ID by yourself to improve the interface response speed)
> - The returned video quality is higher than the APP interface, but the response fields are not as many as the APP interface.
> ### Parameters:
> - share_url: Share link
> ### Return:
> - Video data
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

<a id="get-api-u1-v1-douyin-web-fetch-one-video-danmaku"></a>
### `GET /api/u1/v1/douyin/web/fetch_one_video_danmaku`

- 摘要：获取单个作品视频弹幕数据/Get single video danmaku data
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_danmaku_api_v1_douyin_web_fetch_one_video_danmaku_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品视频弹幕数据
> ### 参数:
> - item_id: 作品id
> - duration: 视频总时长
> - end_time: 结束时间
> - start_time: 开始时间
> ### 返回:
> - 视频弹幕数据
>
> # [English]
> ### Purpose:
> - Get single video danmaku data
> ### Parameters:
> - item_id: Video id
> - duration: Video total duration
> - end_time: End time
> - start_time: Start time
> ### Return:
> - Video danmaku data
>
> # [示例/Example]
> item_id = "7355433624046472498"
> duration = 15134
> end_time = 15133
> start_time = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | 是 | 作品id/Video id | 无 | 7355433624046472498 | 无 |
| duration | query | integer | 是 | 视频总时长/Video total duration | 无 | 15134 | 无 |
| end_time | query | integer | 是 | 结束时间/End time | 无 | 15133 | 无 |
| start_time | query | integer | 是 | 开始时间/Start time | 无 | 0 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-one-video-v2"></a>
### `GET /api/u1/v1/douyin/web/fetch_one_video_v2`

- 摘要：获取单个作品数据 V2/Get single video data V2
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_one_video_api_v1_douyin_web_fetch_one_video_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个作品数据 V2，若此接口失效，请使用 `/fetch_one_video` 接口，或使用APP接口。
> ### 参数:
> - aweme_id: 作品id
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data V2, if this interface fails, please use the `/fetch_one_video` interface, or use the APP interface.
> ### Parameters:
> - aweme_id: Video id
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_id = "7372484719365098803"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7372484719365098803 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-product-coupon"></a>
### `GET /api/u1/v1/douyin/web/fetch_product_coupon`

- 摘要：获取商品优惠券信息/Get product coupon information
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_coupon_api_v1_douyin_web_fetch_product_coupon_get`

#### 说明

> # [中文]
>
> 获取商品优惠券相关信息
>
> # [English]
>
> Get product coupon information
>
> # [示例/Example]
>
> product_id = "3770337983790711029"
> shop_id = "129508461"
> price = "1490"
> author_id = "3109048548866375"
> sec_user_id = "MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 3770337983790711029 | 无 |
| shop_id | query | string | 是 | 店铺ID/Shop ID | 无 | 129508461 | 无 |
| price | query | string | 是 | 价格/Price | 无 | 1490 | 无 |
| author_id | query | string | 是 | 作者ID/Author ID | 无 | 3109048548866375 | 无 |
| sec_user_id | query | string | 是 | 作者ID/Secure Author ID | 无 | MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-product-detail"></a>
### `GET /api/u1/v1/douyin/web/fetch_product_detail`

- 摘要：获取商品详情/Get product detail
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_api_v1_douyin_web_fetch_product_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取商品详情信息
> ### 参数:
> - product_id: 商品ID（必填）
> - aweme_id: 作品ID（可选，如果商品来自某个视频）
> - room_id: 直播间ID（可选，如果商品来自直播间）
> - sec_user_id: 用户sec_user_id（可选，商品所属用户）
> ### 返回:
> - 商品详细信息
>
> # [English]
> ### Purpose:
> - Get product detail information
> ### Parameters:
> - product_id: Product ID (required)
> - aweme_id: Video ID (optional, if product is from a video)
> - room_id: Room ID (optional, if product is from live room)
> - sec_user_id: User sec_user_id (optional, product owner)
> ### Return:
> - Product detail information
>
> # [示例/Example]
> product_id = "3654018325143066950"
> aweme_id = "7546956331878501673"  # 可选
> room_id = ""  # 可选
> sec_user_id = "MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy"  # 可选

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 3654018325143066950 | 无 |
| aweme_id | query | string | 否 | 作品ID（可选）/Video ID (optional) | 7546956331878501673 | 无 | 无 |
| room_id | query | string | 否 | 直播间ID（可选）/Room ID (optional) | 无 | 无 | 无 |
| sec_user_id | query | string | 否 | 用户sec_user_id（可选）/User sec_user_id (optional) | MS4wLjABAAAALoWx-cZWuQVWWvvlE-HiKgm9jel_nmwMcjAMIaEAwFq25sskN1Zgqy_T3x4D0Goy | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-product-review-list"></a>
### `GET /api/u1/v1/douyin/web/fetch_product_review_list`

- 摘要：获取商品评价列表/Get product review list
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_review_list_api_v1_douyin_web_fetch_product_review_list_get`

#### 说明

> # [中文]
>
> 获取商品评价列表
>
> # [English]
>
> Get product review list
>
> # [示例/Example]
>
> product_id = "3770337983790711029"
> shop_id = "129508461"
> cursor = 0
> count = 20
> sort_type = 0  # 0: 默认排序, 1: 最新排序

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 3770337983790711029 | 无 |
| shop_id | query | string | 是 | 店铺ID/Shop ID | 无 | 129508461 | 无 |
| cursor | query | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Count | 20 | 无 | 无 |
| sort_type | query | integer | 否 | 排序类型 (0: 默认排序, 1: 最新排序)/Sort Type (0: Default, 1: Latest) | 0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-product-review-score"></a>
### `GET /api/u1/v1/douyin/web/fetch_product_review_score`

- 摘要：获取商品评价评分/Get product review score
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_review_score_api_v1_douyin_web_fetch_product_review_score_get`

#### 说明

> # [中文]
>
> 获取商品评价评分
>
> # [English]
>
> Get product review score
>
> # [示例/Example]
>
> product_id = "3770337983790711029"
> shop_id = "129508461"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 3770337983790711029 | 无 |
| shop_id | query | string | 是 | 店铺ID/Shop ID | 无 | 129508461 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-product-sku-list"></a>
### `GET /api/u1/v1/douyin/web/fetch_product_sku_list`

- 摘要：获取商品SKU列表/Get product SKU list
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_sku_list_api_v1_douyin_web_fetch_product_sku_list_get`

#### 说明

> # [中文]
>
> 获取商品SKU列表
>
> # [English]
>
> Get product SKU list
>
> # [示例/Example]
>
> product_id = "3770337983790711029"
> author_id = "3109048548866375"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 3770337983790711029 | 无 |
| author_id | query | string | 是 | 作者ID/Author ID | 无 | 3109048548866375 | 无 |

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

<a id="post-api-u1-v1-douyin-web-fetch-query-user"></a>
### `POST /api/u1/v1/douyin/web/fetch_query_user`

- 摘要：查询抖音用户基本信息/Query Douyin user basic information
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_query_user_api_v1_douyin_web_fetch_query_user_post`

#### 说明

> # [中文]
> ### 用途:
> - 查询抖音用户基本信息
> ### 参数:
> - cookie: 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。
> ### 返回:
> - 用户基本信息
>
> # [English]
> ### Purpose:
> - Query Douyin user basic information
> ### Parameters:
> - cookie: User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get.
> ### Return:
> - User basic information
>
> # [示例/Example]
> cookie = "ttwid=xxx;"

#### 参数

无

#### 请求体

- required：否

##### `application/json`

- Schema 摘要：string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| value | string | 是 | 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。/User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get. | ttwid=1%7CNBG4pKnnBr32xpXszWA57PAooMT-02MTYJCyYl0fayI%7C1746172842%7Ce2aa988d35… | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-related-posts"></a>
### `GET /api/u1/v1/douyin/web/fetch_related_posts`

- 摘要：获取相关作品推荐数据/Get related posts recommendation data
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_related_posts_api_v1_douyin_web_fetch_related_posts_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取相关作品推荐数据
> ### 参数:
> - aweme_id: 作品id
> - refresh_index: 翻页索引，默认为1，然后每次增加1用于翻页。
> - count: 数量，默认为20，建议保持不变。
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get related posts recommendation data
> ### Parameters:
> - aweme_id: Video id
> - refresh_index: Paging index, default is 1, then increase by 1 each time for paging.
> - count: Number, default is 20, it is recommended to keep it unchanged.
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_id = "7393365489105358132"
> refresh_index = 1
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7393365489105358132 | 无 |
| refresh_index | query | integer | 否 | 翻页索引/Paging index | 1 | 无 | 无 |
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

<a id="post-api-u1-v1-douyin-web-fetch-search-challenge"></a>
### `POST /api/u1/v1/douyin/web/fetch_search_challenge`

- 摘要：[已弃用/Deprecated] 搜索话题/Search Challenge
- 能力：搜索 / 话题
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_challenge_api_v1_douyin_web_fetch_search_challenge_post`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212773e0
> ### 用途:
> - 搜索话题，此接口不带Cookie请求时只能获取到前30条数据，建议自行提供Cookie获取更多数据。
> - Cookie获取方式：打开网页抖音，登录后，按F12打开开发者工具，点击Network，刷新页面，找到第一个请求，复制Cookie。
> ### 参数:
> - keyword: 关键词
> - cursor: 偏移量
> - count: 数量
> - cookie: 用户自行提供的Cookie，用于获取更多数据。
> ### 返回:
> - 话题搜索结果
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212773e0
> ### Purpose:
> - Search Challenge, when this interface is requested without Cookie, only the first 30 data can be obtained, it is recommended to provide Cookie to get more data.
> - Cookie acquisition method: Open the Douyin webpage, log in, press F12 to open the developer tool, click Network, refresh the page, find the first request, copy the Cookie.
> ### Parameters:
> - keyword: Keyword
> - cursor: Offset
> - count: Number
> - cookie: User provided Cookie, used to get more data.
> ### Return:
> - Challenge search results
>
> # [示例/Example]
> keyword = "动漫"
> cursor = 0
> count = 20

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`keyword`:string, `cursor`:integer, `count`:integer, `cookie`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| keyword | string | 否 | 搜索关键词/Search keyword | 游戏 | 无 | 无 |
| cursor | integer | 否 | 游标/Cursor | 0 | 无 | 无 |
| count | integer | 否 | 数量/Count | 30 | 无 | 无 |
| cookie | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-series-aweme"></a>
### `GET /api/u1/v1/douyin/web/fetch_series_aweme`

- 摘要：短剧作品/Series Video
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_series_aweme_api_v1_douyin_web_fetch_series_aweme_get`

#### 说明

> # [中文]
> ### 用途:
> - 短剧作品
> ### 参数:
> - offset: 页码，默认为0
> - count: 每页数量，默认为16
> - content_type: 子类型，默认为0
>     - 0: 热榜
>     - 101: 甜宠
>     - 102: 搞笑
>     - 104: 正能量
>     - 105: 成长
>     - 106: 悬疑
>     - 109: 家庭
>     - 110: 都市
>     - 112: 奇幻
>     - 113: 玄幻
>     - 114: 职场
>     - 115: 青春
>     - 116: 古装
>     - 117: 动作
>     - 119: 逆袭
>     - 124: 其他
> - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
> - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
> ### 返回:
> - 短剧作品数据
>
> # [English]
> ### Purpose:
> - Series Video
> ### Parameters:
> - offset: Page number, default is 0
> - count: Number per page, default is 16
> - content_type: Subtype, default is 0
>     - 0: Hot list
>     - 101: Sweet pet
>     - 102: Funny
>     - 104: Positive energy
>     - 105: Growth
>     - 106: Suspense
>     - 109: Family
>     - 110: Urban
>     - 112: Fantasy
>     - 113: Fantasy
>     - 114: Workplace
>     - 115: Youth
>     - 116: Ancient costume
>     - 117: Action
>     - 119: Counterattack
>     - 124: Other
> - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may be a problem of data duplication when paging
> - Guest cookie acquisition interface: https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
>
> ### Return:
> - Series Video data

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| offset | query | integer | 是 | 页码/Page number | 无 | 0 | 无 |
| count | query | integer | 是 | 每页数量/Number per page | 无 | 16 | 无 |
| content_type | query | integer | 是 | 短剧类型/Subtype | 无 | 0 | 无 |
| cookie | query | string | 否 | 用户自行提供的Cookie/User provided Cookie | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-web-fetch-user-collection-videos"></a>
### `POST /api/u1/v1/douyin/web/fetch_user_collection_videos`

- 摘要：获取用户收藏作品数据/Get user collection video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户收藏作品数据
> ### 参数:
> - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie)
> - max_cursor: 最大游标
> - count: 最大数量
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user collection video data
> ### Parameters:
> - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie)
> - max_cursor: Maximum cursor
> - count: Maximum number
> ### Return:
> - User video data
>
> # [示例/Example]
> cookie = "YOUR_COOKIE"
> max_cursor = 0
> counts = 20

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`cookie*`:string, `max_cursor`:integer, `counts`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| cookie | string | 是 | 用户网页版抖音Cookie/Your web version of Douyin Cookie | 无 | 无 | 无 |
| max_cursor | integer | 否 | 最大游标/Maximum cursor | 0 | 无 | 无 |
| counts | integer | 否 | 每页数量/Number per page | 20 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-web-fetch-user-collects"></a>
### `POST /api/u1/v1/douyin/web/fetch_user_collects`

- 摘要：获取用户收藏夹/Get user collection
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户收藏夹
> ### 参数:
> - max_cursor: 最大游标
> - count: 最大数量
> - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie)
> ### 返回:
> - 用户收藏夹数据
>
> # [English]
> ### Purpose:
> - Get user collection
> ### Parameters:
> - max_cursor: Maximum cursor
> - count: Maximum number
> - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie)
> ### Return:
> - User collection data
>
> # [示例/Example]
> cookie = "YOUR_COOKIE"
> max_cursor = 0
> counts = 20

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`max_cursor`:integer, `counts`:integer, `cookie*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| max_cursor | integer | 否 | 最大游标/Maximum cursor | 0 | 无 | 无 |
| counts | integer | 否 | 每页数量/Number per page | 20 | 无 | 无 |
| cookie | string | 是 | 用户网页版抖音Cookie/Your web version of Douyin Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-collects-videos"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_collects_videos`

- 摘要：获取用户收藏夹数据/Get user collection data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_collects_videos_api_v1_douyin_web_fetch_user_collects_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户收藏夹数据
> ### 参数:
> - collects_id: 收藏夹id
> - max_cursor: 最大游标
> - count: 最大数量
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user collection data
> ### Parameters:
> - collects_id: Collection id
> - max_cursor: Maximum cursor
> - count: Maximum number
> ### Return:
> - User video data
>
> # [示例/Example]
> collects_id = ""
> max_cursor = 0
> counts = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collects_id | query | string | 是 | 收藏夹id/Collection id | 无 | 无 | 无 |
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

<a id="get-api-u1-v1-douyin-web-fetch-user-fans-list"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_fans_list`

- 摘要：获取用户粉丝列表/Get user fans list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_fans_list_api_v1_douyin_web_fetch_user_fans_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户粉丝列表
> - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，source_type传`1`，即可获取到粉丝列表。
> - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。
>
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
> - count: 数量，默认为20，建议保持不变。
> - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。
> ### 返回:
> - 粉丝列表
>
> # [English]
> ### Purpose:
> - Get user fans list
> - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty fans list will be returned, which contains max_time, then pass the max_time returned by the previous request for paging each time, pass `1` for source_type, you can get the fans list.
> - If you do not request according to the above method, it may cause the returned data to contain duplicate data.
>
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
> - count: Number, default is 20, it is recommended to keep it unchanged.
> - source_type: Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request.
> ### Return:
> - Fans list
>
> # [示例/Example]
> sec_user = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"
> max_time = "0"
> count = 20
> source_type = 2

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id | MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70 | 无 | 无 |
| max_time | query | string | 否 | 最大时间戳/Maximum timestamp | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| source_type | query | integer | 否 | 来源类型/Source type | 1 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-following-list"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_following_list`

- 摘要：获取用户关注列表/Get user following list
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_following_list_api_v1_douyin_web_fetch_user_following_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户关注列表
> - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，source_type传`1`，即可获取到粉丝列表。
> - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
> - count: 数量，默认为20，建议保持不变。
> - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。
> ### 返回:
> - 关注列表
>
> # [English]
> ### Purpose:
> - Get user following list
> - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty fans list will be returned, which contains max_time, then pass the max_time returned by the previous request for paging each time, pass `1` for source_type, you can get the fans list.
> - If you do not request according to the above method, it may cause the returned data to contain duplicate data.
>
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
> - count: Number, default is 20, it is recommended to keep it unchanged.
> - source_type: Source type, default is `1`, use `2` as the source type for the first request, and then use `1` as the source type for the subsequent request.
> ### Return:
> - Following list
>
> # [示例/Example]
> sec_user = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70"
> max_time = "0"
> count = 20
> source_type = 2

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 否 | 用户sec_user_id/User sec_user_id | MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70 | 无 | 无 |
| max_time | query | string | 否 | 最大时间戳/Maximum timestamp | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| source_type | query | integer | 否 | 来源类型/Source type | 1 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-web-fetch-user-like-videos"></a>
### `POST /api/u1/v1/douyin/web/fetch_user_like_videos`

- 摘要：获取用户喜欢作品数据/Get user like video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户喜欢作品数据
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_cursor: 最大游标
> - count: 最大数量
> - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie)
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user like video data
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_cursor: Maximum cursor
> - count: Maximum count number
> - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own Cookie)
> ### Return:
> - User video data
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAAW9FWcqS7RdQAWPd2AA5fL_ilmqsIFUCQ_Iym6Yh9_cUa6ZRqVLjVQSUjlHrfXY1Y"
> max_cursor = 0
> counts = 20

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`sec_user_id*`:string, `max_cursor`:integer, `counts`:integer, `cookie`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | string | 是 | 用户sec_user_id/User sec_user_id | 无 | 无 | 无 |
| max_cursor | integer | 否 | 最大游标/Maximum cursor | 0 | 无 | 无 |
| counts | integer | 否 | 每页数量/Number per page | 20 | 无 | 无 |
| cookie | string | 否 | 用户网页版抖音Cookie/Your web version of Douyin Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-live-info-by-uid"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_live_info_by_uid`

- 摘要：使用UID获取用户开播信息/Get user live information by UID
- 能力：主页/账号 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_live_info_by_uid_api_v1_douyin_web_fetch_user_live_info_by_uid_get`

#### 说明

> # [中文]
> ### 用途:
> - 使用UID获取用户开播信息
> ### 参数:
> - uid: 用户UID
> ### 返回:
> - 用户开播信息，包含room_id与live_status
>
> # [English]
> ### Purpose:
> - Get user live information by UID
> ### Parameters:
> - uid: User UID
> ### Return:
> - User live information, including room_id and live_status
>
> # [示例/Example]
> uid = "3081254195702747"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户UID/User UID | 无 | 3081254195702747 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-live-videos"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_live_videos`

- 摘要：获取用户直播流数据/Get user live video data
- 能力：主页/账号 / 作品详情 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_live_videos_api_v1_douyin_web_fetch_user_live_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户直播流数据
> ### 参数:
> - webcast_id: 直播间 webcast_id
> - 获取方法：
>     - 假设你的直播间链接为：https://www.douyin.com/root/live/376034101029
>     - 那么直播间webcast_id为：376034101029
>     - webcast_id为直播间链接的最后一段数字，与room_id不同。
> ### 返回:
> - 直播流数据
>
> # [English]
> ### Purpose:
> - Get user live video data
> ### Parameters:
> - webcast_id: Room webcast_id
> - Acquisition method:
>     - Assuming your live room link is: https://www.douyin.com/root/live/376034101029
>     - Then the live room webcast_id is: 376034101029
>     - The webcast_id is the last number of the live room link, which is different from the room_id.
> ### Return:
> - Live stream data
>
> # [示例/Example]
> webcast_id = "376034101029"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| webcast_id | query | string | 是 | 直播间webcast_id/Room webcast_id | 无 | 376034101029 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-live-videos-by-room-id"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id`

- 摘要：通过room_id获取指定用户的直播流数据 V1/Get live video data of specified user by room_id V1
- 能力：主页/账号 / 作品详情 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_live_videos_by_room_id_api_v1_douyin_web_fetch_user_live_videos_by_room_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的直播流数据
> ### 参数:
> - room_id: 直播间room_id
> ### 返回:
> - 直播流数据
>
> # [English]
> ### Purpose:
> - Get live video data of specified user
> ### Parameters:
> - room_id: Room room_id
> ### Return:
> - Live stream data
>
> # [示例/Example]
> room_id = "7318296342189919011"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间room_id/Room room_id | 无 | 7318296342189919011 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-live-videos-by-room-id-v2"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_room_id_v2`

- 摘要：通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2
- 能力：主页/账号 / 作品详情 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_live_videos_by_room_id_v2_api_v1_douyin_web_fetch_user_live_videos_by_room_id_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的直播流数据V2
> ### 参数:
> - room_id: 直播间room_id
> ### 返回:
> - 直播流数据
> ### 备注:
> modify_time字段是直播间的最后更新时间，也就相当于开播时间，如果下播也不会重置回0，而是一直保持最后的更新时间。
>
> # [English]
> ### Purpose:
> - Gets the live stream data of the specified user V2
> ### Parameters:
> - room_id: Room room_id
> ### Return:
> - Live stream data
> ### Note:
> The modify_time field is the last update time of the live room, which is equivalent to the start time. If the live stream is offline, it will not be reset to 0, but will always maintain the last update time.
>
> # [示例/Example]
> room_id = "7462723839303093032"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | 是 | 直播间room_id/Room room_id | 无 | 7462723839303093032 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-live-videos-by-sec-uid"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_live_videos_by_sec_uid`

- 摘要：通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid
- 能力：主页/账号 / 作品详情 / 直播
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_live_videos_by_sec_uid_api_v1_douyin_web_fetch_user_live_videos_by_sec_uid_get`

#### 说明

> # [中文]
> ### 用途:
> - 通过sec_uid获取指定用户的直播流数据
> ### 参数:
> - sec_uid: 用户sec_uid，也叫 sec_user_id，可以在用户主页链接中找到。
> ### 返回:
> - 直播流数据
>
> # [English]
> ### Purpose
> - Get live video data of specified user by sec_uid
> ### Parameters
> - sec_uid: User sec_uid, also called sec_user_id, can be found in the user's homepage link.
> ### Return
> - Live stream data
>
> # [示例/Example]
> sec_uid = "MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | 是 | 用户sec_uid/User sec_uid | 无 | MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-mix-videos"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_mix_videos`

- 摘要：获取用户合辑作品数据/Get user mix video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_mix_videos_api_v1_douyin_web_fetch_user_mix_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户合辑作品数据
> ### 参数:
> - mix_id: 合辑id
> - max_cursor: 最大游标
> - count: 最大数量
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user mix video data
> ### Parameters:
> - mix_id: Mix id
> - max_cursor: Maximum cursor
> - count: Maximum number
> ### Return:
> - User video data
>
> # [示例/Example]
> url = https://www.douyin.com/collection/7348687990509553679
> mix_id = "7348687990509553679"
> max_cursor = 0
> counts = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mix_id | query | string | 是 | 合辑id/Mix id | 无 | 7348687990509553679 | 无 |
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

<a id="get-api-u1-v1-douyin-web-fetch-user-post-videos"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_post_videos`

- 摘要：获取用户主页作品数据/Get user homepage video data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_post_videos_api_v1_douyin_web_fetch_user_post_videos_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取用户主页作品数据
> - 注意：请尽量使用APP的接口而不是WEB的接口，因为WEB的接口可能会被不稳定。
> ### 参数:
> - sec_user_id: 用户sec_user_id
> - max_cursor: 翻页游标，第一次请求传0，然后每次请求传上一次请求返回的max_cursor进行翻页。
> - count: 最大数量，建议不要超过20
> - filter_type: 过滤类型，可选参数如下：
>     - 0: 默认排序
>     - 3: 热度排序
> - cookie: 用户网页版抖音Cookie(此接口可以接受用户提供自己的Cookie)
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user homepage video data
> - Note: Please try to use the APP interface instead of the WEB API, because the WEB API may be unstable.
> ### Parameters:
> - sec_user_id: User sec_user_id
> - max_cursor: Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by the previous request for paging each time.
> - count: Maximum count number, it is recommended not to exceed 20
> - filter_type: Filter type, optional parameters are as follows:
>     - 0: Default sorting
>     - 3: Sort by popularity
> - cookie: User's web version of Douyin Cookie (This interface can accept users to provide their own Cookie)
> ### Return:
> - User video data
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE"
> max_cursor = "0"
> counts = 20
> filter_type = "0"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | 是 | 用户sec_user_id/User sec_user_id | 无 | MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE | 无 |
| max_cursor | query | string | 否 | 最大游标/Maximum cursor | 0 | 无 | 无 |
| count | query | integer | 否 | 每页数量/Number per page | 20 | 无 | 无 |
| filter_type | query | string | 否 | 过滤类型/Filter type | 0 | 无 | 无 |
| cookie | query | string | 否 | 用户网页版抖音Cookie/Your web version of Douyin Cookie | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-profile-by-short-id"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_profile_by_short_id`

- 摘要：使用Short ID获取用户信息/Get user information by Short ID
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_profile_by_short_id_api_v1_douyin_web_fetch_user_profile_by_short_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 使用Short ID获取用户信息
> ### 参数:
> - short_id: 用户Short ID
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get user information by Short ID
> ### Parameters:
> - short_id: User Short ID
> ### Return:
> - User information
>
> # [示例/Example]
> short_id = "114131058"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| short_id | query | string | 是 | 用户Short ID/User Short ID | 无 | 114131058 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-profile-by-uid"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_profile_by_uid`

- 摘要：使用UID获取用户信息/Get user information by UID
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_profile_by_uid_api_v1_douyin_web_fetch_user_profile_by_uid_get`

#### 说明

> # [中文]
> ### 用途:
> - 使用UID获取用户信息
> ### 参数:
> - uid: 用户UID
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get user information by UID
> ### Parameters:
> - uid: User UID
> ### Return:
> - User information
>
> # [示例/Example]
> uid = "68141954464"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户UID/User UID | 无 | 68141954464 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-user-search-result"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_search_result`

- 摘要：获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please refer to the following document for replacement interface)
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_result_api_v1_douyin_web_fetch_user_search_result_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0
> ### 用途:
> - 获取指定关键词的用户搜索结果
> - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> - douyin_user_fans: 留空:不限, "0_1k": 1000以下, "1k_1w": 1000-1万, "1w_10w": 1w-10w, "10w_100w": 10w-100w，"100w_": 100w以上
> - douyin_user_type: 留空:不限, "common_user": 普通用户, "enterprise_user": 企业认证, "personal_user": 个人认证
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> ### 返回:
> - 用户搜索结果
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0
> ### Purpose:
> - Get user search results of specified keywords
> - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> - douyin_user_fans: Leave blank: Unlimited, "0_1k": Below 1000, "1k_1w": 1000-10,000, "1w_10w": 10,000-100,000, "10w_100w": 100,000-1 million, "100w_": More than 1 million
> - douyin_user_type: Leave blank: Unlimited, "common_user": Ordinary user, "enterprise_user": Enterprise certification, "personal_user": Personal certification
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> ### Return:
> - User search results
>
> # [示例/Example]
> keyword = "动漫"
> offset = 0
> count = 20
> douyin_user_fans = ""
> douyin_user_type = ""
> search_id = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| douyin_user_fans | query | string | 否 | 粉丝数/Fans | 无 | 无 | 无 |
| douyin_user_type | query | string | 否 | 用户类型/User type | 无 | 无 | 无 |
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

<a id="get-api-u1-v1-douyin-web-fetch-user-search-result-v2"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_search_result_v2`

- 摘要：获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated, please refer to the following document for replacement interface)
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_result_v2_api_v1_douyin_web_fetch_user_search_result_v2_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0
> ### 用途:
> - 获取指定关键词的用户搜索结果V2
> - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0
> ### 参数:
> - keyword: 关键词
> - cursor: 游标，第一次请求时为0，后续从返回数据中获取，用于翻页。
> ### 返回:
> - 用户搜索结果V2
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0
> ### Purpose:
> - Get user search results of specified keywords V2
> - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0
> ### Parameters:
> - keyword: Keyword
> - cursor: Cursor, 0 for the first request, get from the returned data later, used for paging.
> ### Return:
> - User search results V2
>
> # [示例/Example]
> keyword = "中华娘"
> cursor = 0

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
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

<a id="get-api-u1-v1-douyin-web-fetch-user-search-result-v3"></a>
### `GET /api/u1/v1/douyin/web/fetch_user_search_result_v3`

- 摘要：获取指定关键词的用户搜索结果 V3 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V3 (deprecated, please refer to the following document for replacement interface)
- 能力：搜索 / 主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_user_search_result_v3_api_v1_douyin_web_fetch_user_search_result_v3_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212785e0
> ### 用途:
> - 获取指定关键词的用户搜索结果 V3
> - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212785e0
> ### 参数:
> - keyword: 关键词
> - cursor: 偏移量
> - douyin_user_fans: 留空:不限, "0_1k": 1000以下, "1k_1w": 1000-1万, "1w_10w": 1w-10w, "10w_100w": 10w-100w，"100w_": 100w以上
> - douyin_user_type: 留空:不限, "common_user": 普通用户, "enterprise_user": 企业认证, "personal_user": 个人认证
> ### 返回:
> - 用户搜索结果
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212785e0
> ### Purpose:
> - Get user search results of specified keywords V3
> - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212785e0
> ### Parameters:
> - keyword: Keyword
> - cursor: Offset
> - douyin_user_fans: Leave blank: Unlimited, "0_1k": Below 1000, "1k_1w": 1000-10,000, "1w_10w": 10,000-100,000, "10w_100w": 100,000-1 million, "100w_": More than 1 million
> - douyin_user_type: Leave blank: Unlimited, "common_user": Ordinary user, "enterprise_user": Enterprise certification, "personal_user": Personal certification
> ### Return:
> - User search results
>
> # [示例/Example]
> keyword = "中华娘"
> cursor = "0"
> douyin_user_fans = ""
> douyin_user_type = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 中华娘 | 无 |
| cursor | query | string | 否 | 游标/Cursor | 0 | 无 | 无 |
| douyin_user_type | query | string | 否 | 用户类型/User type | 无 | 无 | 无 |
| douyin_user_fans | query | string | 否 | 粉丝数/Fans | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-video-channel-result"></a>
### `GET /api/u1/v1/douyin/web/fetch_video_channel_result`

- 摘要：抖音视频频道数据/Douyin video channel data
- 能力：主页/账号 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_channel_result_api_v1_douyin_web_fetch_video_channel_result_get`

#### 说明

> # [中文]
> ### 用途:
> - 抖音视频频道数据
> - https://www.douyin.com/channel/300205
> ### 参数:
> - tag_id: 标签id，从URL中获取
> - count: 数量
> - refresh_index: 刷新索引
> ### 返回:
> - 视频频道数据
>
> # [English]
> ### Purpose:
> - Douyin video channel data
> - https://www.douyin.com/channel/300205
> ### Parameters:
> - tag_id: Tag id, get from the URL
> - count: Number
> - refresh_index: Refresh index
> ### Return:
> - Video channel data
>
> # [示例/Example]
> tag_id = 300203
> count = 10
> refresh_index = 1

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tag_id | query | integer | 是 | 标签id/Tag id | 无 | 300203 | 无 |
| count | query | integer | 否 | 数量/Number | 10 | 无 | 无 |
| refresh_index | query | integer | 否 | 刷新索引/Refresh index | 1 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-fetch-video-comment-replies"></a>
### `GET /api/u1/v1/douyin/web/fetch_video_comment_replies`

- 摘要：获取指定视频的评论回复数据/Get comment replies data of specified video
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_comments_reply_api_v1_douyin_web_fetch_video_comment_replies_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定视频的评论回复数据
> ### 参数:
> - item_id: 作品id
> - comment_id: 评论id
> - cursor: 游标
> - count: 数量
> ### 返回:
> - 评论回复数据
>
> # [English]
> ### Purpose:
> - Get comment replies data of specified video
> ### Parameters:
> - item_id: Video id
> - comment_id: Comment id
> - cursor: Cursor
> - count: Number
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

<a id="get-api-u1-v1-douyin-web-fetch-video-comments"></a>
### `GET /api/u1/v1/douyin/web/fetch_video_comments`

- 摘要：获取单个视频评论数据/Get single video comments data
- 能力：评论 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_comments_api_v1_douyin_web_fetch_video_comments_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取单个视频评论数据
> ### 参数:
> - aweme_id: 作品id
> - cursor: 游标
> - count: 数量
> ### 返回:
> - 评论数据
>
> # [English]
> ### Purpose:
> - Get single video comments data
> ### Parameters:
> - aweme_id: Video id
> - cursor: Cursor
> - count: Number
> ### Return:
> - Comments data
>
> # [示例/Example]
> aweme_id = "7372484719365098803"
> cursor = 0
> count = 20

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | 是 | 作品id/Video id | 无 | 7372484719365098803 | 无 |
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

<a id="get-api-u1-v1-douyin-web-fetch-video-high-quality-play-url"></a>
### `GET /api/u1/v1/douyin/web/fetch_video_high_quality_play_url`

- 摘要：获取视频的最高画质播放链接/Get the highest quality play URL of the video
- 能力：作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_high_quality_play_url_api_v1_douyin_web_fetch_video_high_quality_play_url_get`

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

<a id="get-api-u1-v1-douyin-web-fetch-video-search-result"></a>
### `GET /api/u1/v1/douyin/web/fetch_video_search_result`

- 摘要：[已弃用/Deprecated] 获取指定关键词的视频搜索结果/Get video search results of specified keywords
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_result_api_v1_douyin_web_fetch_video_search_result_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212780e0
> ### 用途:
> - 获取指定关键词的视频搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次，目前的失败率在5%以下。
> - 此接口收费相较于其他搜索接口便宜，但是稳定性差，需要配合重试机制使用。
> - 请求价格：0.001$ / 次
> - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212780e0
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量，第一次请求时为0，后续从返回数据中获取，用于翻页。
>     - 例如: offset = 10
>     - JSON Path-1 : $.data.cursor
> - count: 数量，默认为10，建议保持不变。
> - sort_type:
>     - 0:综合排序
>     - 1:最多点赞
>     - 2:最新发布
> - publish_time:
>     - 0:不限
>     - 1:最近一天
>     - 7:最近一周
>     - 180:最近半年
> - filter_duration:
>     - 0:不限 0-1:1分钟以内
>     - 1-5:1-5分钟
>     - 5-10000:5分钟以上
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> ### 返回:
> - 视频搜索结果
>
> # [English]
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212780e0
> ### Purpose:
> - Get video search results of specified keywords, this interface may fail, if it fails, please use the same parameters to request 1-3 times again, the current failure rate is below 5%.
> - This interface is cheaper than other search interfaces, but the stability is poor and needs to be used with a retry mechanism.
> - Request price: 0.001$ / time
> - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212780e0
> ### Parameters:
> - keyword: Keyword
> - offset: Offset, 0 for the first request, get from the returned data later, used for paging.
>     - For example: offset = 10
>     - JSON Path-1 : $.data.cursor
> - count: Number, default is 10, it is recommended to keep it unchanged.
> - sort_type:
>     - 0: Comprehensive sorting
>     - 1: Most likes
>     - 2: Latest release
> - publish_time:
>     - 0: Unlimited
>     - 1: Last day
>     - 7: Last week
>     - 180: Last half year
> - filter_duration:
>     - 0: Unlimited
>     - 0-1: Within 1 minute
>     - 1-5: 1-5 minutes
>     - 5-10000: More than 5 minutes
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "2024083107320448E367ECDCCC6B71F7F3"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> ### Return:
> - Video search results
>
> # [示例/Example]
> keyword = "游戏"
> offset = 0
> count = 10
> sort_type = "0"
> publish_time = "0"
> filter_duration = "0"
> search_id = ""

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 关键词/Keyword | 无 | 游戏 | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 无 | 无 |
| count | query | integer | 否 | 数量/Number | 20 | 无 | 无 |
| sort_type | query | string | 否 | 排序类型/Sort type | 0 | 无 | 无 |
| publish_time | query | string | 否 | 发布时间/Publish time | 0 | 无 | 无 |
| filter_duration | query | string | 否 | 视频时长/Duration filter | 0 | 无 | 无 |
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

<a id="get-api-u1-v1-douyin-web-fetch-video-search-result-v2"></a>
### `GET /api/u1/v1/douyin/web/fetch_video_search_result_v2`

- 摘要：获取指定关键词的视频搜索结果 V2 （废弃，替代接口请参考下方文档）/Get video search results of specified keywords V2 (Deprecated, please refer to the following document for replacement interface)
- 能力：搜索 / 作品详情
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_video_search_result_v2_api_v1_douyin_web_fetch_video_search_result_v2_get`

#### 说明

> # [中文]
> ## ⚠️ 此接口已弃用，不再维护，可能无法正常使用。请使用抖音搜索系列接口替代：https://docs.tikhub.io/370212780e0
> ### 用途:
> - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。
> - 收费标准为：0.01$每次请求。
> - 推荐默认使用专门的搜索接口，稳定性更好：https://docs.tikhub.io/370212780e0
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
> ## ⚠️ This endpoint is deprecated, no longer maintained, and may not work properly. Please use the Douyin Search API instead: https://docs.tikhub.io/370212780e0
> ### Purpose:
> - Get video search results of specified keywords V2, this interface has better stability and higher cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is recommended to use this interface.
> - The charging standard is: $0.01 per request.
> - It is recommended to use the dedicated search interface by default, which is more stable: https://docs.tikhub.io/370212780e0
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

<a id="post-api-u1-v1-douyin-web-generate-a-bogus"></a>
### `POST /api/u1/v1/douyin/web/generate_a_bogus`

- 摘要：使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_a_bogus_api_v1_douyin_web_generate_a_bogus_post`

#### 说明

> # [中文]
> ### 用途:
> - 使用接口网址生成A-Bogus参数，提交的URL不能带有a_bogus参数，同时a_bogus参数与请求头中的User-Agent有关，需要一起提交和请求。
> ### 参数:
> - url: API链接，请去除url中的原本的a_boogus参数(如有)。
> - data: 请求载荷，只有在POST请求中才需要提交，GET请求中使用空字符串即可。
> - user_agent: user-agent，需要提交你请求头中的User-Agent，该值参与a_bogus参数的计算。
> - index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改。
> - index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改。
> - index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改。
> ### 返回:
> - A-Bogus参数
>
> # [English]
> ### Purpose:
> - Generate A-Bogus parameter using API URL, the submitted URL cannot contain the original a_boogus parameter, and the a_bogus parameter is related to the User-Agent in the request header, which needs to be submitted and requested together.
> ### Parameters:
> - url: API link, please remove the original a_boogus parameter from the url (if any).
> - data: Request payload, only need to submit in POST request, use an empty string in GET request.
> - user_agent: user-agent, you need to submit the User-Agent in your request header, which is involved in the calculation of the a_bogus parameter.
> - index_0: The first value of the encrypted plaintext list, no special requirements, the default is 0, do not modify it at will.
> - index_1: The second value of the encrypted plaintext list, no special requirements, the default is 1, do not modify it at will.
> - index_2: The third value of the encrypted plaintext list, no special requirements, the default is 14, do not modify it at will.
> ### Return:
> - A-Bogus parameter
>
> # [示例/Example]
> ```json
> {
> "url": "https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5%A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=7346905902554844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_version=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D",
> "data": "",
> "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
> "index_0": 0,
> "index_1": 1,
> "index_2": 14
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`url*`:string, `data*`:string, `user_agent*`:string, `index_0`:integer, `index_1`:integer, `index_2`:integer

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| url | string | 是 | 请求的API URL，需要使用urlencode(url, safe='*')进行编码 \| The requested API URL, needs to be encoded using urlencode(url, safe='*') | 无 | https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=weba… | 无 |
| data | string | 是 | POST请求API时的载荷数据，需要使用urlencode(data, safe='*')进行编码 \| The payload data when requesting the API with POST, needs to be encoded using urlencode(data, safe='*') | 无 | 无 | 无 |
| user_agent | string | 是 | 请求API时的User-Agent \| User-Agent when requesting the API | 无 | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko… | 无 |
| index_0 | integer | 否 | 加密明文列表的第一个值，无特殊要求，默认为0 | 0 | 无 | 无 |
| index_1 | integer | 否 | 加密明文列表的第一个值，无特殊要求，默认为1 | 1 | 无 | 无 |
| index_2 | integer | 否 | 加密明文列表的第一个值，无特殊要求，默认为14 | 14 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-generate-real-mstoken"></a>
### `GET /api/u1/v1/douyin/web/generate_real_msToken`

- 摘要：生成真实msToken/Generate real msToken
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_real_msToken_api_v1_douyin_web_generate_real_msToken_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成真实msToken
> ### 返回:
> - msToken
>
> # [English]
> ### Purpose:
> - Generate real msToken
> ### Return:
> - msToken

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

<a id="get-api-u1-v1-douyin-web-generate-s-v-web-id"></a>
### `GET /api/u1/v1/douyin/web/generate_s_v_web_id`

- 摘要：生成s_v_web_id/Generate s_v_web_id
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_s_v_web_id_api_v1_douyin_web_generate_s_v_web_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成s_v_web_id
> ### 返回:
> - s_v_web_id
>
> # [English]
> ### Purpose:
> - Generate s_v_web_id
> ### Return:
> - s_v_web_id

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

<a id="get-api-u1-v1-douyin-web-generate-ttwid"></a>
### `GET /api/u1/v1/douyin/web/generate_ttwid`

- 摘要：生成ttwid/Generate ttwid
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_ttwid_api_v1_douyin_web_generate_ttwid_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成ttwid
> ### 返回:
> - ttwid
>
> # [English]
> ### Purpose:
> - Generate ttwid
> ### Return:
> - ttwid

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_agent | query | string | 否 | 无 | Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-generate-verify-fp"></a>
### `GET /api/u1/v1/douyin/web/generate_verify_fp`

- 摘要：生成verify_fp/Generate verify_fp
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_verify_fp_api_v1_douyin_web_generate_verify_fp_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成verify_fp
> ### 返回:
> - verify_fp
>
> # [English]
> ### Purpose:
> - Generate verify_fp
> ### Return:
> - verify_fp

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

<a id="get-api-u1-v1-douyin-web-generate-wss-xb-signature"></a>
### `GET /api/u1/v1/douyin/web/generate_wss_xb_signature`

- 摘要：生成弹幕xb签名/Generate barrage xb signature
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_wss_xb_signature_api_v1_douyin_web_generate_wss_xb_signature_get`

#### 说明

> # [中文]
> ### 用途:
> - 生成弹幕xb签名
> ### 参数:
> - user_agent: 用户浏览器代理
> - room_id: 房间号
> - user_unique_id: 用户唯一ID
> ### 返回:
> - 弹幕xb签名
>
> # [English]
> ### Purpose:
> - Generate danmu xb signature
> ### Parameters:
> - user_agent: User browser agent
> - room_id: Room ID
> - user_unique_id: User unique ID
> ### Return:
> - Danmu xb signature
>
> # [示例/Example]
> user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
> room_id = "7382517534467115826"
> user_unique_id = "7382524529011246630"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_agent | query | string | 是 | 用户浏览器代理/User browser agent | 无 | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko… | 无 |
| room_id | query | string | 是 | 房间号/Room ID | 无 | 7382517534467115826 | 无 |
| user_unique_id | query | string | 是 | 用户唯一ID/User unique ID | 无 | 7382524529011246630 | 无 |

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

<a id="post-api-u1-v1-douyin-web-generate-x-bogus"></a>
### `POST /api/u1/v1/douyin/web/generate_x_bogus`

- 摘要：使用接口网址生成X-Bogus参数/Generate X-Bogus parameter using API URL
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`generate_x_bogus_api_v1_douyin_web_generate_x_bogus_post`

#### 说明

> # [中文]
> ### 用途:
> - 使用接口网址生成X-Bogus参数
> ### 参数:
> - url: 接口网址
>
> # [English]
> ### Purpose:
> - Generate X-Bogus parameter using API URL
> ### Parameters:
> - url: API URL
>
> # [示例/Example]
>
> ```json
> {
> "url": "https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&downlink=10&effective_type=4g&round_trip_time=100",
> "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：`url*`:string, `user_agent*`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| url | string | 是 | 请求的API URL，不需要进行编码 \| The requested API URL, no need to encode | 无 | https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&… | 无 |
| user_agent | string | 是 | 请求API时的User-Agent \| User-Agent when requesting the API | 无 | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko… | 无 |

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

<a id="post-api-u1-v1-douyin-web-get-all-aweme-id"></a>
### `POST /api/u1/v1/douyin/web/get_all_aweme_id`

- 摘要：提取列表作品id/Extract list video id
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_all_aweme_id_api_v1_douyin_web_get_all_aweme_id_post`

#### 说明

> # [中文]
>  ### 用途:
>  - 提取列表作品id（最多支持20个链接）
>  ### 参数:
>  - url: 作品链接列表
>  ### 返回:
>  - 作品id列表
>
>  # [English]
>  ### Purpose:
>  - Extract list video id (supports up to 20 links)
>  ### Parameters:
>  - url: Video link list
>  ### Return:
>  - Video id list
>
>  # [示例/Example]
>  ```json
>  {
> "urls":[
>     "0.53 02/26 I@v.sE Fus:/ 你别太帅了郑润泽# 现场版live # 音乐节 # 郑润泽  https://v.douyin.com/iRNBho6u/ 复制此链接，打开Dou音搜索，直接观看视频!",
>     "https://v.douyin.com/iRNBho6u/",
>     "https://www.iesdouyin.com/share/video/7298145681699622182/?region=CN&mid=7298145762238565171&u_code=l1j9bkbd&did=MS4wLjABAAAAtqpCx0hpOERbdSzQdjRZw-wFPxaqdbAzsKDmbJMUI3KWlMGQHC-n6dXAqa-dM2EP&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=05kGlqGmR4_IwCX.ZGk6xuL0osNA..5ur7b0jbOx6cc-&share_version=170400&ts=1699262937&from_aid=6383&from_ssr=1&from=web_code_link",
>     "https://www.douyin.com/video/7298145681699622182?previous_page=web_code_link",
>     "https://www.douyin.com/video/7298145681699622182",
>  ]
>  }
>  ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：[string]

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | 是 | 作品链接列表/Video link list | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-web-get-all-sec-user-id"></a>
### `POST /api/u1/v1/douyin/web/get_all_sec_user_id`

- 摘要：提取列表用户id/Extract list user id
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_all_sec_user_id_api_v1_douyin_web_get_all_sec_user_id_post`

#### 说明

> # [中文]
>  ### 用途:
>  - 提取列表用户id
>  ### 参数:
>  - url: 用户主页链接列表（最多支持10个链接）
>  ### 返回:
>  - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。
>
>  # [English]
>  ### Purpose:
>  - Extract list user id
>  ### Parameters:
>  - url: User homepage link list (supports up to 10 links)
>  ### Return:
>  - If the sec_user_id is successfully obtained from the link, the sec_user_id is returned, otherwise the original input link is returned, and the reason why the sec_user_id cannot be obtained can be manually verified later.
>
>  # [示例/Example]
>  ```json
>  {
> "urls":[
>    "https://www.douyin.com/user/MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE?vid=7285950278132616463",
>    "https://www.douyin.com/user/MS4wLjABAAAAVsneOf144eGDFf8Xp9QNb1VW6ovXnNT5SqJBhJfe8KQBKWKDTWK5Hh-_i9mJzb8C",
>    "长按复制此条消息，打开抖音搜索，查看TA的更多作品。 https://v.douyin.com/idFqvUms/",
>    "https://v.douyin.com/idFqvUms/"
>     ]
>  }
>  ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：[string]

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | 是 | 用户主页链接列表/User homepage link list | 无 | 无 | 无 |

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

<a id="post-api-u1-v1-douyin-web-get-all-webcast-id"></a>
### `POST /api/u1/v1/douyin/web/get_all_webcast_id`

- 摘要：提取列表直播间号/Extract list webcast id
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_all_webcast_id_api_v1_douyin_web_get_all_webcast_id_post`

#### 说明

> # [中文]
> ### 用途:
> - 提取列表直播间号
> ### 参数:
> - url: 直播间链接列表（最多支持20个链接）
> ### 返回:
> - 直播间号列表
>
> # [English]
> ### Purpose:
> - Extract list webcast id
> ### Parameters:
> - url: Room link list (supports up to 20 links)
> ### Return:
> - Room id list
>
> # [示例/Example]
> ```json
> {
>   "urls": [
>         "https://live.douyin.com/775841227732",
>         "https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_share_link&enter_method=web_share_link&previous_page=app_code_link",
>         'https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSjlIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={"from_request_id":"20231230162057EC005772A8EAA0199906","im_channel_invite_id":"0"}&user_id=3644207898042206&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919011&activity_info={}',
>         "6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播",
>         "https://v.douyin.com/i8tBR7hX/",
>         ]
> }
> ```

#### 参数

无

#### 请求体

- required：是

##### `application/json`

- Schema 摘要：[string]

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | 是 | 直播间链接列表/Room link list | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-douyin-web-get-aweme-id"></a>
### `GET /api/u1/v1/douyin/web/get_aweme_id`

- 摘要：提取单个作品id/Extract single video id
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_aweme_id_api_v1_douyin_web_get_aweme_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 提取单个作品id
> ### 参数:
> - url: 作品链接
> ### 返回:
> - 作品id
>
> # [English]
> ### Purpose:
> - Extract single video id
> ### Parameters:
> - url: Video link
> ### Return:
> - Video id
>
> # [示例/Example]
> url = "https://www.douyin.com/video/7298145681699622182"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 无 | 无 | https://www.douyin.com/video/7298145681699622182 | 无 |

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

<a id="get-api-u1-v1-douyin-web-get-sec-user-id"></a>
### `GET /api/u1/v1/douyin/web/get_sec_user_id`

- 摘要：提取单个用户id/Extract single user id
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_sec_user_id_api_v1_douyin_web_get_sec_user_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 提取单个用户id
> ### 参数:
> - url: 用户主页链接
> ### 返回:
> - 用户sec_user_id
>
> # [English]
> ### Purpose:
> - Extract single user id
> ### Parameters:
> - url: User homepage link
> ### Return:
> - User sec_user_id
>
> # [示例/Example]
> url = "https://www.douyin.com/user/MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 无 | 无 | https://www.douyin.com/user/MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s0… | 无 |

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

<a id="get-api-u1-v1-douyin-web-get-webcast-id"></a>
### `GET /api/u1/v1/douyin/web/get_webcast_id`

- 摘要：提取直播间号/Extract webcast id
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`get_webcast_id_api_v1_douyin_web_get_webcast_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 提取列表直播间号
> ### 参数:
> - url: 直播间链接
> ### 返回:
> - 直播间号
>
> # [English]
> ### Purpose:
> - Extract list webcast id
> ### Parameters:
> - url: Room link
> ### Return:
> - Room id
>
> # [示例/Example]
> url = "https://live.douyin.com/775841227732"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | 是 | 无 | 无 | https://live.douyin.com/775841227732 | 无 |

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

<a id="get-api-u1-v1-douyin-web-handler-shorten-url"></a>
### `GET /api/u1/v1/douyin/web/handler_shorten_url`

- 摘要：生成短链接
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`handler_shorten_url_api_v1_douyin_web_handler_shorten_url_get`

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| target_url | query | string | 是 | 待转换的短链接/Target URL to be converted | 无 | https://www.douyin.com/video/7575136499386720761 | 无 |

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

<a id="get-api-u1-v1-douyin-web-handler-user-profile"></a>
### `GET /api/u1/v1/douyin/web/handler_user_profile`

- 摘要：使用sec_user_id获取指定用户的信息/Get information of specified user by sec_user_id
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`handler_user_profile_api_v1_douyin_web_handler_user_profile_get`

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

<a id="get-api-u1-v1-douyin-web-handler-user-profile-v2"></a>
### `GET /api/u1/v1/douyin/web/handler_user_profile_v2`

- 摘要：使用unique_id（抖音号）获取指定用户的信息/Get information of specified user by unique_id
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`handler_user_profile_v2_api_v1_douyin_web_handler_user_profile_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据抖音号获取指定用户的信息
> ### 参数:
> - unique_id: 用户unique_id
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get information of specified user by unique_id
> ### Parameters:
> - unique_id: User unique_id
> ### Return:
> - User information
>
> # [示例/Example]
> unique_id = "TheChief"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| unique_id | query | string | 是 | 用户unique_id/User unique_id | 无 | TheChief | 无 |

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

<a id="get-api-u1-v1-douyin-web-handler-user-profile-v3"></a>
### `GET /api/u1/v1/douyin/web/handler_user_profile_v3`

- 摘要：根据抖音uid获取指定用户的信息/Get information of specified user by uid
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`handler_user_profile_v3_api_v1_douyin_web_handler_user_profile_v3_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据抖音uid获取指定用户的信息
> ### 参数:
> - uid: 用户uid，也就是抖音号的short_id
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get information of specified user by unique_id
> ### Parameters:
> - uid: User uid, which is the short_id of the Douyin number
> ### Return:
> - User information
>
> # [示例/Example]
> uid = "1673937488185292"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | 是 | 用户uid(short_id)/User uid(short_id) | 无 | 1673937488185292 | 无 |

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

<a id="get-api-u1-v1-douyin-web-handler-user-profile-v4"></a>
### `GET /api/u1/v1/douyin/web/handler_user_profile_v4`

- 摘要：根据sec_user_id获取指定用户的信息（性别，年龄，直播等级、牌子）/Get information of specified user by sec_user_id (gender, age, live level、brand)
- 能力：主页/账号
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`handler_user_profile_v4_api_v1_douyin_web_handler_user_profile_v4_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定用户的信息
> ### 参数:
> - sec_user_id: 用户sec_user_id
> ### 返回:
> - 用户信息，包含性别，年龄，直播等级，直播间牌子
> ### 说明：
> - 性别：1为男，2为女，0为未知，在live_user字段中。
> - 年龄：在user字段中，-1为未知。
>
> # [English]
> ### Purpose:
> - Get information of specified user
> ### Parameters:
> - sec_user_id: User sec_user_id
> ### Return:
> - User information, including gender, age, live level, live room brand
> ### Description:
> - gender: 1 male, 2 female, 0 unknown, in the live_user field.
> - age: in the user field, -1 unknown.
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

<a id="get-api-u1-v1-douyin-web-webcast-id-2-room-id"></a>
### `GET /api/u1/v1/douyin/web/webcast_id_2_room_id`

- 摘要：直播间号转房间号/Webcast id to room id
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`webcast_id_2_room_id_api_v1_douyin_web_webcast_id_2_room_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 直播间号转房间号
> ### 参数:
> - webcast_id: 直播间号
> ### 返回:
> - 房间号
>
> # [English]
> ### Purpose:
> - Webcast id to room id
> ### Parameters:
> - webcast_id: Webcast id
> ### Return:
> - Room id
>
> # [示例/Example]
> "webcast_id = "775841227732"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| webcast_id | query | string | 是 | 直播间号/Webcast id | 无 | 775841227732 | 无 |

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
