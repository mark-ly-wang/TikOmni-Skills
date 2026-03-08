# TikTok-Web-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/tiktok-web-api.md`](../api-tags/tiktok-web-api.md)
- Current contract file: `api-contracts/tiktok-web-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `58`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(TikTok-Web-API数据接口/TikTok-Web-API data endpoints)**

## Route Contracts

<a id="get-api-u1-v1-tiktok-web-decrypt-strdata"></a>
### `GET /api/u1/v1/tiktok/web/decrypt_strData`

- Summary: 解密strData/Decrypt strData
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `decrypt_strData_api_v1_tiktok_web_decrypt_strData_get`

#### Notes

> # [中文]
> ### 用途:
> - 解密strData指纹数据，用于分析msToken请求中的指纹信息
> ### 参数:
> - encrypted_data: 加密后的strData字符串，从浏览器自行抓包获取
> ### 返回:
> - 解密后的原始指纹数据，包含浏览器指纹信息和环境信息等。
>
> # [English]
> ### Purpose:
> - Decrypt strData fingerprint data to analyze fingerprint info in msToken request
> ### Parameters:
> - encrypted_data: Encrypted strData string, obtained from browser packet capture
> ### Return:
> - Decrypted raw fingerprint data, including browser fingerprint info and environment info, etc.

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| encrypted_data | query | string | Yes | 加密后的strData字符串/Encrypted strData string | None | 3BvqYbNXLLOcZehvxZVbjpAu7vq82RoWmFSJHLFwzDwJIZevE0AeilQfP55LridxmdGGjknoksqIsLq… | None |

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

<a id="get-api-u1-v1-tiktok-web-device-register"></a>
### `GET /api/u1/v1/tiktok/web/device_register`

- Summary: 设备注册/Register device for TikTok Web
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `device_register_api_v1_tiktok_web_device_register_get`

#### Notes

> # [中文]
> ### 用途:
> - 设备注册，为TikTok Web生成设备ID和游客Cookie
> ### 参数:
> - 无
> ### 返回:
> - 设备注册信息，包括设备ID和游客Cookie
>
> # [English]
> ### Purpose:
> - Register device to generate device ID and guest Cookie for TikTok Web
> ### Parameters:
> - None
> ### Return:
> - Device registration information, including device ID and guest Cookie
> # [响应/Response]:
> ```json
> {
>     "deviceId": "7556227929396708877",
>     "cookie": "tt_chain_token=wBqjjz5I8m1bt96uxA1s8A==",
>     "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
> }
> ```

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

<a id="get-api-u1-v1-tiktok-web-encrypt-strdata"></a>
### `GET /api/u1/v1/tiktok/web/encrypt_strData`

- Summary: 加密strData/Encrypt strData
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `encrypt_strData_api_v1_tiktok_web_encrypt_strData_get`

#### Notes

> # [中文]
> ### 用途:
> - 加密strData指纹数据，用于生成msToken请求
> ### 参数:
> - data: 原始指纹数据字符串（请先将JSON格式然后转换成字符串进行请求）
> ### 返回:
> - 加密后的strData
>
> # [English]
> ### Purpose:
> - Encrypt strData fingerprint data for msToken request
> ### Parameters:
> - data: Raw fingerprint data string (please convert JSON format to string before requesting)
> ### Return:
> - Encrypted strData

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| data | query | string | Yes | 原始指纹数据字符串（JSON格式或字典字符串）/Raw fingerprint data string (JSON format or dict string) | None | {"behavior":{"beResize":[],"beMotion":[{"ts":1701069187299,"x":null,"y":null,"z… | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-batch-check-live-alive"></a>
### `GET /api/u1/v1/tiktok/web/fetch_batch_check_live_alive`

- Summary: 批量直播间开播状态检测/Batch live room start status check
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_batch_check_live_alive_api_v1_tiktok_web_fetch_batch_check_live_alive_get`

#### Notes

> # [中文]
> ### 用途:
> - 批量直播间开播状态检测
> - 最多支持50个直播间同时查询
> - 如果某个直播间不存在或已下播，则对应位置返回空或null。
> ### 参数:
> - room_ids: 直播间ID列表，用英文逗号分隔，如：7530611486784277278,7530633767468288782
> ### 返回:
> - 批量直播间开播状态列表
> ### 价格:
> - 定价0.025$，请尽量达到50个直播间查询，避免浪费API调用次数。
> ### 说明:
> - 同一个room_id不会重复返回开播状态。
>
> # [English]
> ### Purpose:
> - Batch live room start status check
> - Support up to 50 live rooms query at once
> - If a live room does not exist or has ended, the corresponding position will return empty or null.
> ### Parameters:
> - room_ids: Live room ID list separated by commas, e.g.: 7530611486784277278,7530633767468288782
> ### Return:
> - Batch live room start status list
> ### Price:
> - Charged by the number of live rooms queried, 0.025$ per live room, please try to query 50 live rooms to avoid wasting API call counts.
> ### Note:
> - The same room_id will not return the start status repeatedly.
>
> # [示例/Example]
> room_ids = "7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_ids | query | string | Yes | 直播间ID列表，用英文逗号分隔，最多支持50个/Live room ID list separated by commas, up to 50 IDs | None | 7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142 | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-check-live-alive"></a>
### `GET /api/u1/v1/tiktok/web/fetch_check_live_alive`

- Summary: 直播间开播状态检测/Live room start status check
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_check_live_alive_api_v1_tiktok_web_fetch_check_live_alive_get`

#### Notes

> # [中文]
> ### 用途:
> - 直播间开播状态检测
> - 如果当前直播间不存在或已下播，则返回空。
> ### 参数:
> - room_id: 直播间ID
> ### 返回:
> - 直播间开播状态
>
> # [English]
> ### Purpose:
> - Live room start status check
> - If the current live room does not exist or has ended, it will return empty.
> ### Parameters:
> - room_id: Live room ID
> ### Return:
> - Live room start status
>
> # [示例/Example]
> room_id = "7381444193462078214"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间ID/Live room ID | None | 7381444193462078214 | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-explore-post"></a>
### `GET /api/u1/v1/tiktok/web/fetch_explore_post`

- Summary: 获取探索作品数据/Get explore video data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_explore_post_api_v1_tiktok_web_fetch_explore_post_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取探索作品数据
> ### 参数:
> - categoryType: 作品分类
>     - 100: 动画与漫画
>     - 101: 表演
>     - 102: 美容护理
>     - 103: 游戏
>     - 104: 喜剧
>     - 105: 日常生活
>     - 106: 家庭
>     - 107: 情感关系
>     - 108: 戏剧
>     - 109: 穿搭
>     - 110: 对口型
>     - 111: 美食
>     - 112: 运动
>     - 113: 动物
>     - 114: 社会
>     - 115: 汽车
>     - 116: 教育
>     - 117: 健身和健康
>     - 118: 科技
>     - 119: 唱歌跳舞
>     - 120: 全部
> - count: 每页数量
> ### 返回:
> - 作品数据
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get explore video data
> ### Parameters:
> - categoryType: Video category
>     - 100: Animation and comics
>     - 101: Performance
>     - 102: Beauty care
>     - 103: Game
>     - 104: Comedy
>     - 105: Daily life
>     - 106: Family
>     - 107: Emotional relationship
>     - 108: Drama
>     - 109: Dress up
>     - 110: Dubbing
>     - 111: Food
>     - 112: Sports
>     - 113: Animals
>     - 114: Society
>     - 115: Car
>     - 116: Education
>     - 117: Fitness and health
>     - 118: Technology
>     - 119: Singing and dancing
>     - 120: All
> - count: Number per page
> ### Return:
> - Video data
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> categoryType = "120"
> count = 16

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| categoryType | query | string | No | 作品分类/Video category | 120 | None | None |
| count | query | integer | No | 每页数量/Number per page | 16 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-general-search"></a>
### `GET /api/u1/v1/tiktok/web/fetch_general_search`

- Summary: 获取综合搜索列表/Get general search list
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_general_search_api_v1_tiktok_web_fetch_general_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取综合搜索列表
> ### 参数:
> - keyword: 搜索关键词
> - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
> ### 返回:
> - 综合搜索列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get general search list
> ### Parameters:
> - keyword: Search keyword
> - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor.
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required)
> ### Return:
> - General search list
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> keyword = "TikTok"
> offset = 0
> search_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | TikTok | None |
| offset | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| search_id | query | string | No | 搜索id，翻页时需要提供/Search id, need to provide when paging | None | None | None |
| cookie | query | string | No | 用户cookie(按需提供)/User cookie(if needed) | None | None | None |

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

<a id="post-api-u1-v1-tiktok-web-fetch-gift-name-by-id"></a>
### `POST /api/u1/v1/tiktok/web/fetch_gift_name_by_id`

- Summary: 根据Gift ID查询礼物名称/Get gift name by gift ID
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_gift_name_by_id_api_v1_tiktok_web_fetch_gift_name_by_id_post`

#### Notes

> 根据TikTok的Gift ID查询对应的礼物名称 | Get gift name by TikTok gift ID

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `gift_id*`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| gift_id | string | Yes | 礼物ID \| Gift ID | None | 10001 | None |

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

<a id="post-api-u1-v1-tiktok-web-fetch-gift-names-by-ids"></a>
### `POST /api/u1/v1/tiktok/web/fetch_gift_names_by_ids`

- Summary: 批量查询Gift ID对应的礼物名称($0.025/次,建议50个)/Batch get gift names by gift IDs ($0.025/call, suggest 50)
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_gift_names_by_ids_api_v1_tiktok_web_fetch_gift_names_by_ids_post`

#### Notes

> 批量查询多个TikTok Gift ID对应的礼物名称。计费：$0.025每次调用。建议每次查询50个ID以获得最佳性价比，超过50个时自动处理前50个 | Batch get gift names by multiple TikTok gift IDs. Pricing: $0.025 per call. Recommend querying 50 IDs at once for best value, auto-process first 50 IDs if more than 50

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `gift_ids*`[string]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| gift_ids | array<string> | Yes | 礼物ID列表，建议50个/次获得最佳性价比($0.025)，超过50个时自动处理前50个 \| Gift ID list, recommend 50/call for best value ($0.025), auto-process first 50 if more than 50 | None | ["10001", "10002", "10003"] | None |

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

<a id="post-api-u1-v1-tiktok-web-fetch-home-feed"></a>
### `POST /api/u1/v1/tiktok/web/fetch_home_feed`

- Summary: 首页推荐作品/Home Feed
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post`

#### Notes

> # [中文]
> ### 用途:
> - 首页推荐作品
> ### 参数:
> - count: 每页数量
> - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。
> ### 返回:
> - 首页推荐作品
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Home Feed
> ### Parameters:
> - count: Number per page
> - cookie: User's own cookie, optional parameter, used for personalized recommendations of interface return data.
> ### Return:
> - Home Feed
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> count = 15
> Cookie = "Your_Cookie"

#### Parameters

None

#### Request Body

- required: No

##### `application/json`

- Schema summary: `count`:integer, `cookie`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| count | integer | No | 每页数量/Number per page | 15 | None | None |
| cookie | string | No | 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。/ User's own cookie, optional parameter, used for personalized recommendations of interface return data. | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-live-gift-list"></a>
### `GET /api/u1/v1/tiktok/web/fetch_live_gift_list`

- Summary: 获取直播间礼物列表/Get live room gift list
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_gift_list_api_v1_tiktok_web_fetch_live_gift_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取直播间礼物列表
> - room_id为可选参数，不传则获取通用礼物列表（2025年08月15日统计是256种礼物）
> ### 参数:
> - room_id: 直播间ID（可选）
> ### 返回:
> - 直播间礼物列表数据
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get live room gift list
> - room_id is optional parameter, if not provided, will get general gift list (as of August 15, 2025, there are 256 types of gifts)
> ### Parameters:
> - room_id: Live room ID (optional)
> ### Return:
> - Live room gift list data
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> room_id = "7381444193462078214"  # 可选/Optional

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | No | 直播间ID，可选参数/Live room ID, optional parameter | None | 7381444193462078214 | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-live-im-fetch"></a>
### `GET /api/u1/v1/tiktok/web/fetch_live_im_fetch`

- Summary: TikTok直播间弹幕参数获取/tiktok live room danmaku parameters
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_im_fetch_api_v1_tiktok_web_fetch_live_im_fetch_get`

#### Notes

> # [中文]
> ### 用途:
> - TikTok直播间弹幕参数获取
> ### 参数:
> - room_id: 直播间号
> - user_unique_id: 用户唯一ID
>
> ### 返回:
> - 弹幕参数数据
>
> # [English]
> ### Purpose:
> - TikTok live room danmaku parameters
> ### Parameters:
> - room_id: Live room id
> - user_unique_id: User unique ID
>
> ### Return:
> - Danmaku parameter data

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间号/Live room id | None | 7382517534467115826 | None |
| user_unique_id | query | string | Yes | 用户唯一ID/User unique ID | None | 7382524529011246630 | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-live-recommend"></a>
### `GET /api/u1/v1/tiktok/web/fetch_live_recommend`

- Summary: 获取直播间首页推荐列表/Get live room homepage recommendation list
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_recommend_api_v1_tiktok_web_fetch_live_recommend_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取直播间首页推荐列表
> ### 参数:
> - related_live_tag: 相关直播标签
> ### 返回:
> - 直播间首页推荐列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get live room homepage recommendation list
> ### Parameters:
> - related_live_tag: Related live tag
> ### Return:
> - Live room homepage recommendation list
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> related_live_tag = "VALORANT"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| related_live_tag | query | string | Yes | 相关直播标签/Related live tag | None | VALORANT | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-post-comment"></a>
### `GET /api/u1/v1/tiktok/web/fetch_post_comment`

- Summary: 获取作品的评论列表/Get video comments
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comment_api_v1_tiktok_web_fetch_post_comment_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取作品的评论列表
> ### 参数:
> - aweme_id: 作品id
> - cursor: 翻页游标
> - count: 每页数量
> - current_region: 当前地区，默认为空。
> ### 返回:
> - 作品的评论列表
>
> # [English]
> ### Purpose:
> - Get video comments
> ### Parameters:
> - aweme_id: Video id
> - cursor: Page cursor
> - count: Number per page
> - current_region: Current region, default is empty.
> ### Return:
> - Video comments
>
> # [示例/Eample]
> aweme_id = "7304809083817774382"
> cursor = 0
> count = 20
> current_region = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id | None | 7304809083817774382 | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| current_region | query | string | No | 当前地区/Current region | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-post-comment-reply"></a>
### `GET /api/u1/v1/tiktok/web/fetch_post_comment_reply`

- Summary: 获取作品的评论回复列表/Get video comment replies
- Capabilities: comments / comment replies / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_comment_reply_api_v1_tiktok_web_fetch_post_comment_reply_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取作品的评论回复列表
> ### 参数:
> - item_id: 作品id
> - comment_id: 评论id
> - cursor: 翻页游标
> - count: 每页数量
> - current_region: 当前地区，默认为空。
> ### 返回:
> - 作品的评论回复列表
>
> # [English]
> ### Purpose:
> - Get video comment replies
> ### Parameters:
> - item_id: Video id
> - comment_id: Comment id
> - cursor: Page cursor
> - count: Number per page
> - current_region: Current region, default is empty.
> ### Return:
> - Video comment replies
>
> # [示例/Eample]
> item_id = "7304809083817774382"
> comment_id = "7304877760886588191"
> cursor = 0
> count = 20
> current_region = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id | None | 7304809083817774382 | None |
| comment_id | query | string | Yes | 评论id/Comment id | None | 7304877760886588191 | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| current_region | query | string | No | 当前地区/Current region | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-post-detail"></a>
### `GET /api/u1/v1/tiktok/web/fetch_post_detail`

- Summary: 获取单个作品数据/Get single video data
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_detail_api_v1_tiktok_web_fetch_post_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品数据
> ### 参数:
> - itemId: 作品id
> ### 返回:
> - 作品数据
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get single video data
> ### Parameters:
> - itemId: Video id
> ### Return:
> - Video data
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> itemId = "7339393672959757570"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| itemId | query | string | Yes | 作品id/Video id | None | 7339393672959757570 | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-post-detail-v2"></a>
### `GET /api/u1/v1/tiktok/web/fetch_post_detail_v2`

- Summary: 获取单个作品数据 V2/Get single video data V2
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_post_detail_v2_api_v1_tiktok_web_fetch_post_detail_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品数据
> ### 参数:
> - itemId: 作品id
> ### 返回:
> - 作品数据
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get single video data
> ### Parameters:
> - itemId: Video id
> ### Return:
> - Video data
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> itemId = "7339393672959757570"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| itemId | query | string | Yes | 作品id/Video id | None | 7339393672959757570 | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-search-keyword-suggest"></a>
### `GET /api/u1/v1/tiktok/web/fetch_search_keyword_suggest`

- Summary: 搜索关键字推荐/Search keyword suggest
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_keyword_suggest_api_v1_tiktok_web_fetch_search_keyword_suggest_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索关键字推荐
> ### 参数:
> - keyword: 搜索关键词
> ### 返回:
> - 关键字推荐列表
>
> # [English]
> ### Purpose:
> - Search keyword suggest
> ### Parameters:
> - keyword: Search keyword
> ### Return:
> - Keyword suggest list
>
> # [示例/Example]
> keyword = "TikTok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | TikTok | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-search-live"></a>
### `GET /api/u1/v1/tiktok/web/fetch_search_live`

- Summary: 搜索直播/Search live
- Capabilities: search / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_live_api_v1_tiktok_web_fetch_search_live_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索直播
> ### 参数:
> - keyword: 搜索关键词
> - count: 每页数量
> - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取。
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
> ### 返回:
> - 直播列表
>
> # [English]
> ### Purpose:
> - Search live
> ### Parameters:
> - keyword: Search keyword
> - count: Number per page
> - offset: Page offset, 0 for the first request, need to provide for the second paging.
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required)
> ### Return:
> - Live list
>
> # [示例/Example]
> keyword = "TikTok"
> count = 20
> offset = 0
> search_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | TikTok | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| offset | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| search_id | query | string | No | 搜索id，翻页时需要提供/Search id, need to provide when paging | None | None | None |
| cookie | query | string | No | 用户cookie(按需提供)/User cookie(if needed) | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-search-photo"></a>
### `GET /api/u1/v1/tiktok/web/fetch_search_photo`

- Summary: 搜索照片/Search photo
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_photo_api_v1_tiktok_web_fetch_search_photo_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索照片
> ### 参数:
> - keyword: 搜索关键词
> - count: 每页数量，建议保持默认值20。
> - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
> ### 返回:
> - 视频列表
>
> # [English]
> ### Purpose:
> - Search photo
> ### Parameters:
> - keyword: Search keyword
> - count: Number per page, it is recommended to keep the default value 20.
> - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor.
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - offset: Page cursor
> - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required)
> ### Return:
> - Video list
>
> # [示例/Example]
> keyword = "TikTok"
> count = 20
> offset = 0
> search_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | TikTok | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| offset | query | integer | No | 翻页游标/Page offset | 0 | None | None |
| search_id | query | string | No | 搜索id，翻页时需要提供/Search id, need to provide when paging | None | None | None |
| cookie | query | string | No | 用户cookie(按需提供)/User cookie(if needed) | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-search-user"></a>
### `GET /api/u1/v1/tiktok/web/fetch_search_user`

- Summary: 搜索用户/Search user
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_user_api_v1_tiktok_web_fetch_search_user_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索用户
> ### 参数:
> - keyword: 搜索关键词
> - cursor: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
> ### 返回:
> - 用户列表
> ### 备注:
> - 如果接口响应的 `data` 字段中的 `status_code` 不为0，说明搜索请求未成功，此时请检查响应里的异常，有可能你在搜索 TikTok 不允许的关键词，或者搜索了敏感内容，请更换关键词重试。
>
> # [English]
> ### Purpose:
> - Search user
> ### Parameters:
> - keyword: Search keyword
> - cursor: Page cursor, 0 for the first request, need to provide for the second paging, generally the keyword of this value is offset or cursor.
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required)
> ### Return:
> - User list
> ### Note:
> - If the `status_code` in the `data` field of the interface response is not 0, it means that the search request was not successful. Please check the exceptions in the response. You may be searching for keywords that TikTok does not allow, or searching for sensitive content. Please change the keywords and try again.
>
> # [示例/Example]
> keyword = "TikTok"
> cursor = 0
> search_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | TikTok | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| search_id | query | string | No | 搜索id，翻页时需要提供/Search id, need to provide when paging | None | None | None |
| cookie | query | string | No | 用户cookie(按需提供)/User cookie(if needed) | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-search-video"></a>
### `GET /api/u1/v1/tiktok/web/fetch_search_video`

- Summary: 搜索视频/Search video
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_search_video_api_v1_tiktok_web_fetch_search_video_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索视频
> ### 参数:
> - keyword: 搜索关键词
> - count: 每页数量，建议保持默认值20。
> - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取。
> - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
>     - 例如: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
> ### 返回:
> - 视频列表
>
> # [English]
> ### Purpose:
> - Search video
> ### Parameters:
> - keyword: Search keyword
> - count: Number per page, it is recommended to keep the default value 20.
> - offset: Page offset, 0 for the first request, need to provide for the second paging.
> - search_id: Search id, empty for the first request, need to provide for the second paging, need to get it from the return response of the last request.
>     - For example: search_id = "20240828035554C02011379EBB6A00E00B"
>     - JSON Path-1 : $.data.extra.logid
>     - JSON Path-2 : $.data.log_pb.impr_id
> - cookie: User cookie (If you need to search with your own account, or encounter an interface error, you can provide the cookie yourself, default is not required)
> ### Return:
> - Video list
>
> # [示例/Example]
> keyword = "TikTok"
> count = 20
> offset = 0
> search_id = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | TikTok | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| offset | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| search_id | query | string | No | 搜索id，翻页时需要提供/Search id, need to provide when paging | None | None | None |
| cookie | query | string | No | 用户cookie(按需提供)/User cookie(if needed) | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-sso-login-auth"></a>
### `GET /api/u1/v1/tiktok/web/fetch_sso_login_auth`

- Summary: 认证SSO登录/Authenticate SSO login
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_sso_login_auth_api_v1_tiktok_web_fetch_sso_login_auth_get`

#### Notes

> # [中文]
> ### 用途:
> - 认证SSO登录
> ### 参数:
> - device_id: 设备ID
> - verifyFp: verifyFp
> - region: 地区
> - proxy: 代理
> ### 返回:
> - SSO登录认证信息
> ### 说明:
> - 认证需要保持参数一致，否则会认证失败。
>
> # [English]
> ### Purpose:
> - Authenticate SSO login
> ### Parameters:
> - token: Login token
> - device_id: Device ID
> - verifyFp: verifyFp
> - region: Region
> - proxy: Proxy
> ### Return:
> - SSO login authentication information
> ### Description:
> - Please use the value obtained by the /fetch_sso_login_status interface for input.
> - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.
>
> # [示例/Example]
> device_id = "7481276116461831688"
> verifyFp = "verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL"
> region = "US"
> proxy = "None"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| device_id | query | string | Yes | 设备ID/Device ID | None | 7481276116461831688 | None |
| verifyFp | query | string | Yes | verifyFp | None | verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL | None |
| region | query | string | Yes | 地区/Region | None | US | None |
| proxy | query | string | Yes | 代理/Proxy | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-sso-login-qrcode"></a>
### `GET /api/u1/v1/tiktok/web/fetch_sso_login_qrcode`

- Summary: 获取SSO登录二维码/Get SSO login QR code
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_sso_login_qrcode_api_v1_tiktok_web_fetch_sso_login_qrcode_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取SSO登录二维码
> ### 参数:
> - device_id: 设备ID
> - region: 地区
> - proxy: 代理
> ### 返回:
> - SSO登录二维码
> ### 说明:
> - 该接口返回的二维码需要使用手机扫描登录，登录成功后会返回登录信息。
> - 不传入设备ID将由后端自动生成设备ID。
> - 如果需要使用代理，请传入代理地址，否则传入None。
> - 单次二维码有效期为一分钟。
>
> # [English]
> ### Purpose:
> - Get SSO login QR code
> ### Parameters:
> - device_id: Device ID
> - region: Region
> - proxy: Proxy
> ### Return:
> - SSO login QR code
> ### Description:
> - The QR code returned by this interface needs to be scanned by the mobile phone for login, and the login information will be returned after successful login.
> - If the device ID is not passed in, the device ID will be automatically generated by the backend.
> - If you need to use a proxy, please pass in the proxy address, otherwise pass in None
> - The validity period of a single QR code is one minute.
>
> # [示例/Example]
> device_id = "7481276116461831688"
> region = "US"
> proxy = "None"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| device_id | query | string | Yes | 设备ID/Device ID | None | 7481276116461831688 | None |
| region | query | string | Yes | 地区/Region | None | US | None |
| proxy | query | string | Yes | 代理/Proxy | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-sso-login-status"></a>
### `GET /api/u1/v1/tiktok/web/fetch_sso_login_status`

- Summary: 获取SSO登录状态/Get SSO login status
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_sso_login_status_api_v1_tiktok_web_fetch_sso_login_status_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取SSO登录状态
> ### 参数:
> - token: 登录令牌
> - device_id: 设备ID
> - verifyFp: verifyFp
> - region: 地区
> - proxy: 代理
> ### 返回:
> - SSO登录状态
> ### 说明:
> - 该接口返回的登录状态需要轮询，建议2秒轮询一次。
> - 请使用/fetch_sso_login_qrcode接口获取的值进行传入。
> - 如果需要使用代理，请传入代理地址，否则传入None。
> - 扫码状态：
>     - new: 未扫码
>     - expired: 二维码过期（需要重新请求/fetch_sso_login_qrcode）
>     - scanned: 已扫码
>     - confirmed: 已确认登录（需要请求/fetch_sso_login_auth认证）
>
> # [English]
> ### Purpose:
> - Get SSO login status
> ### Parameters:
> - token: Login token
> - device_id: Device ID
> - verifyFp: verifyFp
> - region: Region
> - proxy: Proxy
> ### Return:
> - SSO login status
> ### Description:
> - The login status returned by this interface needs to be polled, and it is recommended to poll once every 2 seconds.
> - Please use the value obtained by the /fetch_sso_login_qrcode interface for input.
> - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.
> - Scan status:
>     - new: Not scanned
>     - expired: QR code expired (need to request /fetch_sso_login_qrcode again)
>     - scanned: Scanned
>     - confirmed: Confirmed login (need to request /fetch_sso_login_auth for authentication
>
> # [示例/Example]
> token = "jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5"
> device_id = "7481276116461831688"
> verifyFp = "verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL"
> region = "US"
> proxy = "None"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| token | query | string | Yes | 登录令牌/Login token | None | jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5 | None |
| device_id | query | string | Yes | 设备ID/Device ID | None | 7481276116461831688 | None |
| verifyFp | query | string | Yes | verifyFp | None | verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL | None |
| region | query | string | Yes | 地区/Region | None | US | None |
| proxy | query | string | Yes | 代理/Proxy | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-tag-detail"></a>
### `GET /api/u1/v1/tiktok/web/fetch_tag_detail`

- Summary: Tag详情/Tag Detail
- Capabilities: details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_tag_detail_api_v1_tiktok_web_fetch_tag_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - Tag详情
> ### 参数:
> - tag_name: Tag名称
> ### 返回:
> - Tag详情
>
> # [English]
> ### Purpose:
> - Tag Detail
> ### Parameters:
> - tag_name: Tag name
> ### Return:
> - Tag Detail
>
> # [示例/Example]
> tag_name = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tag_name | query | string | Yes | Tag名称/Tag name | None | tiktok | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-tag-post"></a>
### `GET /api/u1/v1/tiktok/web/fetch_tag_post`

- Summary: Tag作品/Tag Post
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_tag_post_api_v1_tiktok_web_fetch_tag_post_get`

#### Notes

> # [中文]
> ### 用途:
> - Tag作品
> ### 参数:
> - challengeID: Tag ID
> - count: 每页数量
> - cursor: 翻页游标
> ### 返回:
> - Tag作品
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Tag Post
> ### Parameters:
> - challengeID: Tag ID
> - count: Number per page
> - cursor: Page cursor
> ### Return:
> - Tag Post
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> challengeID = "7551"
> count = 30
> cursor = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| challengeID | query | string | Yes | Tag ID | None | 7551 | None |
| count | query | integer | No | 每页数量/Number per page | 30 | None | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-tiktok-live-data"></a>
### `GET /api/u1/v1/tiktok/web/fetch_tiktok_live_data`

- Summary: 通过直播链接获取直播间信息/Get live room information via live link
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_tiktok_live_data_api_v1_tiktok_web_fetch_tiktok_live_data_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过直播链接获取直播间信息
> - 此接口可获取离线直播间信息
> ### 参数:
> - live_room_url: 直播间链接
> ### 返回:
> - 直播间信息
>
> # [English]
> ### Purpose:
> - Get live room information via live link
> - This interface can get offline live room information
> ### Parameters:
> - live_room_url: Live room link
> ### Return:
> - Live room information
>
> # [示例/Example]
> live_room_url = "https://www.tiktok.com/@.caseoh_daily/live"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| live_room_url | query | string | Yes | 直播间链接/Live room link | None | https://www.tiktok.com/@.caseoh_daily/live | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-tiktok-web-guest-cookie"></a>
### `GET /api/u1/v1/tiktok/web/fetch_tiktok_web_guest_cookie`

- Summary: 获取游客 Cookie/Get the guest Cookie
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_tiktok_web_guest_cookie_api_v1_tiktok_web_fetch_tiktok_web_guest_cookie_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取 TikTok Web的游客Cookie
> - 可以用于爬取 TikTok Web 的数据，如用户作品、合辑作品等。
> - 可以固定身份避免部分接口重复数据。
> - 请注意：游客Cookie无法爬取所有数据，有一定的限制。
> - 可以配合开源项目使用此接口实现TikTok Web的数据爬取。
> ### 参数:
> - user_agent: 用户浏览器代理
> ### 返回:
> - 游客Cookie
>
> # [English]
> ### Purpose:
> - Get the guest Cookie of TikTok Web
> - Can be used to crawl data of TikTok Web, such as user videos, mix videos, etc.
> - Can fix identity to avoid duplicate data for some interfaces.
> - Please note: Guest Cookie cannot crawl all data, there are certain restrictions.
> - Can be used with open source projects to implement data crawling of TikTok Web using this interface.
> ### Parameters:
> - user_agent: User browser agent
> ### Return:
> - Guest Cookie
>
> # [示例/Example]
> user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
>
> # [响应/Response]:
> ```json
> {
>     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
>     "Cookie": "ttwid=1%7Ck5lqyYxAq2wSmaEculMCk31ur4lkvy3DVwn6Phf45GQ%7C1759321284%7C6bac9a25e1f6b512aecad91a37167ad753b47f2306ffe0d70695001d6b4dd793;tt_csrf_token=tueWm0Fw-jL4Ie3Iu2z755XYPzAphhgJmHDA;tt_chain_token=drrbnMAs2A13tME+L6XbsA==",
>     "Referer": "https://www.tiktok.com/explore"
> }
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_agent | query | string | Yes | 用户浏览器代理/User browser agent | None | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko… | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-trending-post"></a>
### `GET /api/u1/v1/tiktok/web/fetch_trending_post`

- Summary: 获取每日热门内容作品数据/Get daily trending video data
- Capabilities: trends / rankings / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_trending_post_api_v1_tiktok_web_fetch_trending_post_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取每日热门内容作品数据
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get daily trending video data
> ### Return:
> - Video data
>
> # [示例/Example]

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

<a id="get-api-u1-v1-tiktok-web-fetch-trending-searchwords"></a>
### `GET /api/u1/v1/tiktok/web/fetch_trending_searchwords`

- Summary: 获取每日趋势搜索关键词/Get daily trending search words
- Capabilities: search / trends / rankings
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_trending_searchwords_api_v1_tiktok_web_fetch_trending_searchwords_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取每日趋势搜索关键词
> ### 返回:
> - 趋势搜索关键词
>
> # [English]
> ### Purpose:
> - Get daily trending search words
> ### Return:
> - Trending search words
>
> # [示例/Example]

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-collect"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_collect`

- Summary: 获取用户的收藏列表/Get user favorites
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_collect_api_v1_tiktok_web_fetch_user_collect_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的收藏列表
> - 注意: 该接口目前只能获取自己的收藏列表，需要提供自己账号的cookie。
> ### 参数:
> - cookie: 用户cookie
> - secUid: 用户secUid
> - cursor: 翻页游标
> - count: 每页数量
> - coverFormat: 封面格式
> ### 返回:
> - 用户的收藏列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user favorites
> - Note: This interface can currently only get your own favorites list, you need to provide your account cookie.
> ### Parameters:
> - cookie: User cookie
> - secUid: User secUid
> - cursor: Page cursor
> - count: Number per page
> - coverFormat: Cover format
> ### Return:
> - User favorites
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> cookie = "Your_Cookie"
> secUid = "Your_SecUid"
> cursor = 0
> count = 30
> coverFormat = 2

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cookie | query | string | Yes | 用户cookie/User cookie | None | Your_Cookie | None |
| secUid | query | string | Yes | 用户secUid/User secUid | None | Your_SecUid | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 30 | None | None |
| coverFormat | query | integer | No | 封面格式/Cover format | 2 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-fans"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_fans`

- Summary: 获取用户的粉丝列表/Get user followers
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_fans_api_v1_tiktok_web_fetch_user_fans_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的粉丝列表
> ### 参数:
> - secUid: 用户secUid
> - count: 每页数量
> - maxCursor: 最大游标
> - minCursor: 最小游标
> ### 返回:
> - 用户的粉丝列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user followers
> ### Parameters:
> - secUid: User secUid
> - count: Number per page
> - maxCursor: Max cursor
> - minCursor: Min cursor
> ### Return:
> - User followers
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
> count = 30
> maxCursor = 0
> minCursor = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| secUid | query | string | Yes | 用户secUid/User secUid | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| count | query | integer | No | 每页数量/Number per page | 30 | None | None |
| maxCursor | query | integer | No | 最大游标/Max cursor | 0 | None | None |
| minCursor | query | integer | No | 最小游标/Min cursor | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-follow"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_follow`

- Summary: 获取用户的关注列表/Get user followings
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follow_api_v1_tiktok_web_fetch_user_follow_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的关注列表
> ### 参数:
> - secUid: 用户secUid
> - count: 每页数量
> - maxCursor: 最大游标
> - minCursor: 最小游标
> ### 返回:
> - 用户的关注列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user followings
> ### Parameters:
> - secUid: User secUid
> - count: Number per page
> - maxCursor: Max cursor
> - minCursor: Min cursor
> ### Return:
> - User followings
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
> count = 30
> maxCursor = 0
> minCursor = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| secUid | query | string | Yes | 用户secUid/User secUid | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| count | query | integer | No | 每页数量/Number per page | 30 | None | None |
| maxCursor | query | integer | No | 最大游标/Max cursor | 0 | None | None |
| minCursor | query | integer | No | 最小游标/Min cursor | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-like"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_like`

- Summary: 获取用户的点赞列表/Get user likes
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_like_api_v1_tiktok_web_fetch_user_like_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的点赞列表
> - 注意: 该接口需要用户点赞列表为公开状态
> ### 参数:
> - secUid: 用户secUid
> - cursor: 翻页游标
> - count: 每页数量，默认为20，不可变更。
> - coverFormat: 封面格式
> - post_item_list_request_type: 排序方式
>     - 0：默认排序
>     - 1：热门排序
>     - 2：最旧排序
> ### 返回:
> - 用户的点赞列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user likes
> - Note: This interface requires that the user's like list be public
> ### Parameters:
> - secUid: User secUid
> - cursor: Page cursor
> - count: Number per page, default is 20, cannot be changed.
> - coverFormat: Cover format
> - post_item_list_request_type: Sort type
>     - 0: Default sort
>     - 1: Hot sort
>     - 2: Oldest sort
> ### Return:
> - User likes
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> secUid = "MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU"
> cursor = 0
> count = 20
> coverFormat = 2

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| secUid | query | string | Yes | 用户secUid/User secUid | None | MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| coverFormat | query | integer | No | 封面格式/Cover format | 2 | None | None |
| post_item_list_request_type | query | integer | No | 排序方式/Sort type | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-live-detail"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_live_detail`

- Summary: 获取用户的直播详情/Get user live details
- Capabilities: profiles / accounts / details / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_live_detail_api_v1_tiktok_web_fetch_user_live_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的直播详情
> ### 参数:
> - uniqueId: 用户uniqueId
> ### 返回:
> - 用户的直播详情
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user live details
> ### Parameters:
> - uniqueId: User uniqueId
> ### Return:
> - User live details
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> uniqueId = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uniqueId | query | string | Yes | 用户uniqueId/User uniqueId | None | tiktok | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-mix"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_mix`

- Summary: 获取用户的合辑列表/Get user mix list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_mix_api_v1_tiktok_web_fetch_user_mix_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的合辑列表
> ### 参数:
> - mixId: 合辑id
> - cursor: 翻页游标
> - count: 每页数量
> ### 返回:
> - 用户的合辑列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user mix list
> ### Parameters:
> - mixId: Mix id
> - cursor: Page cursor
> - count: Number per page
> ### Return:
> - User mix list
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Eample]
> mixId = "7101538765474106158"
> cursor = 0
> count = 30

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mixId | query | string | Yes | 合辑id/Mix id | None | 7101538765474106158 | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 30 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-play-list"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_play_list`

- Summary: 获取用户的播放列表/Get user play list
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_play_list_api_v1_tiktok_web_fetch_user_play_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的播放列表
> ### 参数:
> - secUid: 用户secUid
> - cursor: 翻页游标
> - count: 每页数量
> ### 返回:
> - 用户的播放列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user play list
> ### Parameters:
> - secUid: User secUid
> - cursor: Page cursor
> - count: Number per page
> ### Return:
> - User play list
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Eample]
> secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
> cursor = 0
> count = 30

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| secUid | query | string | Yes | 用户secUid/User secUid | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 30 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-post"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_post`

- Summary: 获取用户的作品列表/Get user posts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_api_v1_tiktok_web_fetch_user_post_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的作品列表
> ### 参数:
> - secUid: 用户secUid
> - cursor: 翻页游标
> - count: 每页数量，默认为20，不可变更。
> - coverFormat: 封面格式，默认为2，可选值为1或2。
> - post_item_list_request_type: 排序方式
>     - 0：默认排序
>     - 1：热门排序
>     - 2：最旧排序
> ### 返回:
> - 用户的作品列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user posts
> ### Parameters:
> - secUid: User secUid
> - cursor: Page cursor
> - count: Number per page, default is 20, cannot be changed.
> - coverFormat: Cover format, default is 2, optional values are 1 or 2.
> - post_item_list_request_type: Sort type
>     - 0: Default sort
>     - 1: Hot sort
>     - 2: Oldest sort
> ### Return:
> - User posts
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
> cursor = 0
> post_item_list_request_type = 0
> count = 20
> coverFormat = 2

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| secUid | query | string | Yes | 用户secUid/User secUid | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | 0 | None |
| count | query | integer | No | 每页数量/Number per page | 20 | 20 | None |
| coverFormat | query | integer | No | 封面格式/Cover format | 2 | 2 | None |
| post_item_list_request_type | query | integer | No | 排序方式/Sort type | 0 | 0 | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-profile"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_profile`

- Summary: 获取用户的个人信息/Get user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_profile_api_v1_tiktok_web_fetch_user_profile_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的个人信息
> ### 参数:
> - secUid: 用户secUid
> - uniqueId: 用户uniqueId
> - secUid和uniqueId至少提供一个, 优先使用uniqueId, 也就是用户主页的链接中的用户名。
> ### 返回:
> - 用户的个人信息
>
> # [English]
> ### Purpose:
> - Get user profile
> ### Parameters:
> - secUid: User secUid
> - uniqueId: User uniqueId
> - At least one of secUid and uniqueId is provided, and uniqueId is preferred, that is, the username in the user's homepage link.
> ### Return:
> - User profile
>
> # [示例/Example]
> secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
> uniqueId = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uniqueId | query | string | No | 用户uniqueId/User uniqueId | None | tiktok | None |
| secUid | query | string | No | 用户secUid/User secUid | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-fetch-user-repost"></a>
### `GET /api/u1/v1/tiktok/web/fetch_user_repost`

- Summary: 获取用户的转发作品列表/Get user reposts
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_repost_api_v1_tiktok_web_fetch_user_repost_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户的转发作品列表
> ### 参数:
> - secUid: 用户secUid
> - cursor: 翻页游标
> - count: 每页数量，默认为20，不可变更。
> - coverFormat: 封面格式，默认为2，可选值为1或2。
> ### 返回:
> - 用户的转发作品列表
> ### 备注:
> - 此接口返回的所有视频CDN链接均需要携带返回的 `tt_chain_token` 参数才能正常访问，否则会返回HTTP403错误。
> - 在访问视频CDN链接时，请务必在请求头中携带 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 替换为接口返回的 `tt_chain_token` 参数值。
> - **如果访问视频CDN链接时返回HTTP 403错误**:
>   1. 请使用接口响应中以 `https://www.tiktok.com/aweme/v1/play/` 开头的视频链接(通常在响应数据的 `video.playAddr` 或类似字段中)
>   2. 在请求该链接时，务必在请求头中添加 `Cookie: tt_chain_token={tt_chain_token}`，其中 `{tt_chain_token}` 为接口返回的 `tt_chain_token` 参数值
>   3. 示例请求头: `Cookie: tt_chain_token=xxx`
> - 如果需要绕过此限制获取可以直接访问的无水印视频CDN链接，请使用 TikTok APP V3 目录下的接口。
>
> # [English]
> ### Purpose:
> - Get user reposts
> ### Parameters:
> - secUid: User secUid
> - cursor: Page cursor
> - count: Number per page, default is 20, cannot be changed.
> - coverFormat: Cover format, default is 2, optional values are 1 or 2.
> ### Return:
> - User reposts
> ### Note:
> - All video CDN links returned by this interface need to carry the returned `tt_chain_token` parameter to be accessed normally, otherwise HTTP 403 error will be returned.
> - When accessing the video CDN link, be sure to carry `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is replaced with the `tt_chain_token` parameter value returned by the interface.
> - **If you receive HTTP 403 error when accessing video CDN links**:
>   1. Use the video link starting with `https://www.tiktok.com/aweme/v1/play/` from the API response (usually found in `video.playAddr` or similar fields)
>   2. When requesting this link, make sure to add `Cookie: tt_chain_token={tt_chain_token}` in the request header, where `{tt_chain_token}` is the value returned by the API
>   3. Example request header: `Cookie: tt_chain_token=xxx`
> - If you need to bypass this restriction to get a watermark-free video CDN link that can be accessed directly, please use the interface under the TikTok APP V3 directory.
>
> # [示例/Example]
> secUid = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
> cursor = 0
> count = 20
> coverFormat = 2

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| secUid | query | string | Yes | 用户secUid/User secUid | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| cursor | query | integer | No | 翻页游标/Page cursor | 0 | 0 | None |
| count | query | integer | No | 每页数量/Number per page | 20 | 20 | None |
| coverFormat | query | integer | No | 封面格式/Cover format | 2 | 2 | None |

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

<a id="get-api-u1-v1-tiktok-web-generate-fingerprint"></a>
### `GET /api/u1/v1/tiktok/web/generate_fingerprint`

- Summary: 生成浏览器指纹/Generate browser fingerprint
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_fingerprint_api_v1_tiktok_web_generate_fingerprint_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成随机浏览器指纹数据，可用于自定义msToken请求
> ### 参数:
> - browser_type: 指定浏览器类型，可选值:
>     - chrome_windows: Chrome + Windows
>     - chrome_mac: Chrome + macOS
>     - firefox_windows: Firefox + Windows
>     - firefox_mac: Firefox + macOS
>     - 不传则随机选择
> ### 返回:
> - 浏览器指纹数据
>
> # [English]
> ### Purpose:
> - Generate random browser fingerprint data for custom msToken request
> ### Parameters:
> - browser_type: Specify browser type, options:
>     - chrome_windows: Chrome + Windows
>     - chrome_mac: Chrome + macOS
>     - firefox_windows: Firefox + Windows
>     - firefox_mac: Firefox + macOS
>     - Leave empty for random selection
> ### Return:
> - Browser fingerprint data

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| browser_type | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-generate-hashed-id"></a>
### `GET /api/u1/v1/tiktok/web/generate_hashed_id`

- Summary: 生成哈希ID/Generate hashed ID
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_hashed_id_api_v1_tiktok_web_generate_hashed_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成TikTok Web的哈希ID
> ### 参数:
> - email: 邮箱地址
> ### 返回:
> - 生成的哈希ID字符串
>
> # [English]
> ### Purpose:
> - Generate hashed ID for TikTok Web
> ### Parameters:
> - email: Email address
> ### Return:
> - Generated hashed ID string
>
> # [示例/Example]
> email = "test@example.com"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| email | query | string | Yes | 邮箱地址/Email address | None | test@example.com | None |

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

<a id="get-api-u1-v1-tiktok-web-generate-real-mstoken"></a>
### `GET /api/u1/v1/tiktok/web/generate_real_msToken`

- Summary: 生成真实msToken/Generate real msToken
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_real_msToken_api_v1_tiktok_web_generate_real_msToken_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成真实msToken
> ### 参数:
> - random_strData: 是否使用随机化的浏览器指纹数据（推荐开启以提高反爬虫能力）
> - browser_type: 指定浏览器类型，可选值:
>     - chrome_windows: Chrome + Windows
>     - chrome_mac: Chrome + macOS
>     - firefox_windows: Firefox + Windows
>     - firefox_mac: Firefox + macOS
>     - 不传则随机选择
> ### 返回:
> - 真实msToken
>
> # [English]
> ### Purpose:
> - Generate real msToken
> ### Parameters:
> - random_strData: Whether to use randomized browser fingerprint data (recommended for better anti-bot)
> - browser_type: Specify browser type, options:
>     - chrome_windows: Chrome + Windows
>     - chrome_mac: Chrome + macOS
>     - firefox_windows: Firefox + Windows
>     - firefox_mac: Firefox + macOS
>     - Leave empty for random selection
> ### Return:
> - Real msToken

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| random_strData | query | boolean | No | None | false | None | None |
| browser_type | query | string | No | None | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-generate-ttwid"></a>
### `GET /api/u1/v1/tiktok/web/generate_ttwid`

- Summary: 生成ttwid/Generate ttwid
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_ttwid_api_v1_tiktok_web_generate_ttwid_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成ttwid
> ### 参数:
> - 无
> ### 返回:
> - ttwid
>
> # [English]
> ### Purpose:
> - Generate ttwid
> ### Parameters:
> - None
> ### Return:
> - ttwid

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_agent | query | string | No | None | Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0 | None | None |

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

<a id="get-api-u1-v1-tiktok-web-generate-webid"></a>
### `GET /api/u1/v1/tiktok/web/generate_webid`

- Summary: 生成web_id/Generate web_id
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_webid_api_v1_tiktok_web_generate_webid_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成 TikTok web_id （Web接口请求参数中的device_id）
> ### 参数:
> - cookie: 自定义 cookie（需包含 odin_tt），如不传则使用随机生成的游客Cookie值
> - user_agent: 用户代理字符串
> - url: 请求来源 URL
> - referer: 来源页面
> - user_unique_id: 用户唯一 ID（可选）
> - app_id: 应用 ID，默认 1988，代表 TikTok Web 应用
> ### 返回:
> - web_id: 生成的 web_id
> - e: 错误码 (0 表示成功)
> - ssid: 会话 ID
>
> # [English]
> ### Purpose:
> - Generate TikTok web_id (device_id in Web API request parameters)
> ### Parameters:
> - cookie: Custom cookie (must contain odin_tt), uses default if not provided
> - user_agent: User agent string
> - url: Request source URL
> - referer: Referrer page
> - user_unique_id: User unique ID (optional)
> - app_id: Application ID, default 1988, represents TikTok Web app
> ### Return:
> - web_id: Generated web_id
> - e: Error code (0 means success)
> - ssid: Session ID

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cookie | query | string | No | None | None | None | None |
| user_agent | query | string | No | None | Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/… | None | None |
| url | query | string | No | None | https://www.tiktok.com/explore | None | None |
| referer | query | string | No | None | None | None | None |
| user_unique_id | query | string | No | None | None | None | None |
| app_id | query | integer | No | None | 1988 | None | None |

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

<a id="post-api-u1-v1-tiktok-web-generate-xbogus"></a>
### `POST /api/u1/v1/tiktok/web/generate_xbogus`

- Summary: 生成 XBogus/Generate XBogus
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_xbogus_api_v1_tiktok_web_generate_xbogus_post`

#### Notes

> # [中文]
> ### 用途:
> - 生成xbogus
> ### 参数:
> - url: 未签名的API URL
> - user_agent: 用户浏览器User-Agent
> ### 返回:
> - xbogus
>
> # [English]
> ### Purpose:
> - Generate xbogus
> ### Parameters:
> - url: Unsigned API URL
> - user_agent: User browser User-Agent
> ### Return:
> - xbogus
>
> # [示例/Example]
>
> ```json
> {
>     "url": "https://www.tiktok.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&downlink=10&effective_type=4g&round_trip_time=100",
>     "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
> }

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `url*`:string, `user_agent*`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| url | string | Yes | 请求的API URL，不需要进行编码 \| The requested API URL, no need to encode | None | https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&… | None |
| user_agent | string | Yes | 请求API时的User-Agent \| User-Agent when requesting the API | None | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko… | None |

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

<a id="post-api-u1-v1-tiktok-web-generate-xgnarly"></a>
### `POST /api/u1/v1/tiktok/web/generate_xgnarly`

- Summary: 生成 XGnarly /Generate XGnarly
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_xgnarly_api_v1_tiktok_web_generate_xgnarly_post`

#### Notes

> # [中文]
> ### 用途:
> - 生成 XGnarly 加密，用于 TikTok Web API 请求
> ### 参数:
> - url (str): 不携带签名（X-Bogus 或 X-Gnarly）的 原始 URL 字符串 或 查询参数字符串，不需要进行URL编码
> - user_agent (str): 用户浏览器User-Agent，参与加密，请确保与请求时的User-Agent一致
> - body (str): 请求的API参数，适用于POST请求，如果是GET请求则不需要提供
> ### 返回:
> - X-Gnarly 加密字符串
>
> # [English]
> ### Purpose:
> - Generate XGnarly encryption, used for TikTok Web API requests
> ### Parameters:
> - url (str): The original URL string or query parameter string without signature (X-Bogus or X-Gnarly), no need to URL encode
> - user_agent (str): User browser User-Agent, involved in encryption, please ensure it is consistent with the User-Agent when requesting
> - body (str): The API parameters of the request, applicable for POST requests, not required for
> ### Return:
> - X-Gnarly encryption string
>
> # [示例/Example]
>
> ```json
> {
>     "url": "https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1756087650&aid=1988&app_language=zh-Hans&app_name=tiktok_web&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7542339104672111234&device_platform=web_pc&focus_state=true&from_page=search&history_len=3&is_fullscreen=true&is_page_visible=true&keyword=musk&odinId=7542338997269211234&os=mac&priority_region&referer&region=US&screen_height=967&screen_width=1496&search_id&tz_name=America%2FLos_Angeles&user_is_login=false&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=zh-Hans",
>     "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
>     "body": ""
> }

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `url*`:string, `user_agent*`:string, `body`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| url | string | Yes | 请求的API URL，不需要进行URL编码 \| The requested API URL, no need to URL encode | None | None | None |
| user_agent | string | Yes | 请求API时的User-Agent \| User-Agent when requesting the API | None | None | None |
| body | string | No | 请求的API参数，适用于POST请求 \| The API parameters of the request, applicable for POST requests | None | None | None |

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

<a id="post-api-u1-v1-tiktok-web-generate-xgnarly-and-xbogus"></a>
### `POST /api/u1/v1/tiktok/web/generate_xgnarly_and_xbogus`

- Summary: 生成 XGnarly 和 XBogus /Generate XGnarly and XBogus
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `generate_xgnarly_and_xbogus_api_v1_tiktok_web_generate_xgnarly_and_xbogus_post`

#### Notes

> # [中文]
> ### 用途:
> - 生成 XGnarly 加密，用于 TikTok Web API 请求
> - 用这个接口可以生成最新版本的加密参数 X-Bogus 和 X-Gnarly，不可自定义 User-Agent，会自动生成一个常见浏览器的User-Agent
> - 此接口为完美还原算法，无视除验证码外的一切风控，可以用于爬取商品，价格：0.005 美金/次
> - 本接口生成的 X-Bogus 和 X-Gnarly 均为最新版本（2026年1月）
> ### 参数:
> - url (str): 不携带签名（X-Bogus 或 X-Gnarly）并且包含域名的请求URL，不需要进行URL编码
> - body (str): 请求的API参数，适用于POST请求，如果是GET请求则不需要提供
> ### 返回:
> - 最新版本的 X-Gnarly 加密 + 最新版本的 X-Bogus 加密 + 随机浏览器的 User-Agent
>
> # [English]
> ### Purpose:
> - Generate XGnarly encryption, used for TikTok Web API requests
> - This interface can generate the latest version of encryption parameters X-Bogus and X-Gnarly, User-Agent cannot be customized, a common browser User-Agent will be automatically generated
> - This interface perfectly restores the algorithm, ignores all risk controls except for verification codes, and can be used to crawl products, price: $0.005/time
> - The X-Bogus and X-Gnarly generated by this interface are the latest versions (January 2026)
> ### Parameters:
> - url (str): The requested API URL without signature (X-Bogus or X-Gnarly) and including the domain name, no need to URL encode
> - body (str): The API parameters of the request, applicable for POST requests, not required for
> ### Return:
> - The latest version of X-Gnarly encryption + the latest version of X-Bogus encryption + User-Agent of a random browser
>
> # [示例/Example]
>
> ```json
> {
>     "url": "https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1756087650&aid=1988&app_language=zh-Hans&app_name=tiktok_web&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7542339104672111234&device_platform=web_pc&focus_state=true&from_page=search&history_len=3&is_fullscreen=true&is_page_visible=true&keyword=musk&odinId=7542338997269211234&os=mac&priority_region&referer&region=US&screen_height=967&screen_width=1496&search_id&tz_name=America%2FLos_Angeles&user_is_login=false&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=zh-Hans",
>     "body": ""
> }

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `url*`:string, `body`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| url | string | Yes | 包含域名和参数的请求的API URL，不需要进行URL编码 \| The requested API URL, no need to URL encode | None | None | None |
| body | string | No | 请求的API参数，适用于POST请求 \| The API parameters of the request, applicable for POST requests | None | None | None |

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

<a id="post-api-u1-v1-tiktok-web-get-all-aweme-id"></a>
### `POST /api/u1/v1/tiktok/web/get_all_aweme_id`

- Summary: 提取列表作品id/Extract list video id
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_all_aweme_id_api_v1_tiktok_web_get_all_aweme_id_post`

#### Notes

> # [中文]
> ### 用途:
> - 提取列表作品id
> ### 参数:
> - url: 作品链接 (最多支持20个链接)
> ### 返回:
> - 作品id
>
> # [English]
> ### Purpose:
> - Extract list video id
> ### Parameters:
> - url: Video link (Support up to 20 links)
> ### Return:
> - Video id
>
> # [示例/Example]
> url = ["https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"]

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | Yes | 作品链接/Video link | None | None | None |

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

<a id="post-api-u1-v1-tiktok-web-get-all-sec-user-id"></a>
### `POST /api/u1/v1/tiktok/web/get_all_sec_user_id`

- Summary: 提取列表用户sec_user_id/Extract list user sec_user_id
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_all_sec_user_id_api_v1_tiktok_web_get_all_sec_user_id_post`

#### Notes

> # [中文]
> ### 用途:
> - 提取列表用户id
> ### 参数:
> - url: 用户主页链接（最多支持10个链接）、
> ### 返回:
> - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。
>
> # [English]
> ### Purpose:
> - Extract list user id
> ### Parameters:
> - url: User homepage link (Support up to 10 links)
> ### Return:
> - If the sec_user_id is successfully obtained, the sec_user_id is returned, otherwise the original input link is returned, and the reason why the sec_user_id cannot be obtained can be manually verified later.
>
> # [示例/Example]
> url = ["https://www.tiktok.com/@tiktok"]

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | Yes | 用户主页链接/User homepage link | None | None | None |

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

<a id="post-api-u1-v1-tiktok-web-get-all-unique-id"></a>
### `POST /api/u1/v1/tiktok/web/get_all_unique_id`

- Summary: 获取列表unique_id/Get list unique_id
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_all_unique_id_api_v1_tiktok_web_get_all_unique_id_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取列表unique_id
> ### 参数:
> - url: 用户主页链接 (最多支持20个链接)
> ### 返回:
> - unique_id
>
> # [English]
> ### Purpose:
> - Get list unique_id
> ### Parameters:
> - url: User homepage link (Support up to 20 links)
> ### Return:
> - unique_id
>
> # [示例/Example]
> url = ["https://www.tiktok.com/@tiktok"]

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | Yes | 用户主页链接/User homepage link | None | None | None |

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

<a id="get-api-u1-v1-tiktok-web-get-aweme-id"></a>
### `GET /api/u1/v1/tiktok/web/get_aweme_id`

- Summary: 提取单个作品id/Extract single video id
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_aweme_id_api_v1_tiktok_web_get_aweme_id_get`

#### Notes

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
> url = "https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 作品链接/Video link | None | https://www.tiktok.com/@owlcitymusic/video/7218694761253735723 | None |

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

<a id="get-api-u1-v1-tiktok-web-get-live-room-id"></a>
### `GET /api/u1/v1/tiktok/web/get_live_room_id`

- Summary: 根据直播间链接提取直播间ID/Extract live room ID from live room link
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_live_room_id_api_v1_tiktok_web_get_live_room_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据直播间链接提取直播间Room ID
> - 支持短链接，如：https://vt.tiktok.com/ZSjuyJnWQ/
> - 支持长链接，如：https://www.tiktok.com/@maksukaracun/live
> ### 参数:
> - live_room_url: 直播间链接
> ### 返回:
> - 直播间Room ID
>
> # [English]
> ### Purpose:
> - Extract live room Room ID from live room link
> - Support short links, such as: https://vt.tiktok.com/ZSjuyJnWQ/
> - Support long links, such as: https://www.tiktok.com/@maksukaracun/live
> ### Parameters:
> - live_room_url: Live room link
> ### Return:
> - Live room Room ID
>
> # [示例/Example]
> live_room_url = "https://www.tiktok.com/@maksukaracun/live"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| live_room_url | query | string | Yes | 直播间链接/Live room link | None | https://www.tiktok.com/@maksukaracun/live | None |

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

<a id="get-api-u1-v1-tiktok-web-get-sec-user-id"></a>
### `GET /api/u1/v1/tiktok/web/get_sec_user_id`

- Summary: 提取用户sec_user_id/Extract user sec_user_id
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_sec_user_id_api_v1_tiktok_web_get_sec_user_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 提取列表用户id
> ### 参数:
> - url: 用户主页链接
> ### 返回:
> - 用户id
>
> # [English]
> ### Purpose:
> - Extract list user id
> ### Parameters:
> - url: User homepage link
> ### Return:
> - User id
>
> # [示例/Example]
> url = "https://www.tiktok.com/@tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 用户主页链接/User homepage link | None | https://www.tiktok.com/@tiktok | None |

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

<a id="get-api-u1-v1-tiktok-web-get-unique-id"></a>
### `GET /api/u1/v1/tiktok/web/get_unique_id`

- Summary: 获取用户unique_id/Get user unique_id
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_unique_id_api_v1_tiktok_web_get_unique_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户unique_id
> ### 参数:
> - url: 用户主页链接
> ### 返回:
> - unique_id
>
> # [English]
> ### Purpose:
> - Get user unique_id
> ### Parameters:
> - url: User homepage link
> ### Return:
> - unique_id
>
> # [示例/Example]
> url = "https://www.tiktok.com/@tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 用户主页链接/User homepage link | None | https://www.tiktok.com/@tiktok | None |

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

<a id="get-api-u1-v1-tiktok-web-get-user-id"></a>
### `GET /api/u1/v1/tiktok/web/get_user_id`

- Summary: 提取用户user_id/Extract user user_id
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_id_api_v1_tiktok_web_get_user_id_get`

#### Notes

> # [中文]
> ### 用途:
> - 提取用户user_id
> ### 参数:
> - url: 用户主页链接
> ### 返回:
> - 用户id
>
> # [English]
> ### Purpose:
> - Extract list user id
> ### Parameters:
> - url: User homepage link
> ### Return:
> - User id
>
> # [示例/Example]
> url = "https://www.tiktok.com/@tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 用户主页链接/User homepage link | None | https://www.tiktok.com/@tiktok | None |

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

<a id="get-api-u1-v1-tiktok-web-tiktok-live-room"></a>
### `GET /api/u1/v1/tiktok/web/tiktok_live_room`

- Summary: 提取直播间弹幕/Extract live room danmaku
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `tiktok_live_room_api_v1_tiktok_web_tiktok_live_room_get`

#### Notes

> # [中文]
> ### 用途:
> - 提取直播间弹幕
> - 该接口已不再提供线上服务，需要自行购买源代码后在本地部署使用，购买源代码请在Discord服务器联系管理员，Discord邀请链接：https://discord.gg/aMEAS8Xsvz
> #### 价格:
> - 每10条数据消耗0.001$，支持阶梯式计费折扣。
> ### 参数:
> - live_room_url: 直播间链接
> - danmaku_type: 消息类型
>     - WebcastChatMessage: 聊天消息
>     - WebcastMemberMessage: 成员消息
>     - WebcastRoomUserSeqMessage: 用户序列消息
>     - WebcastGiftMessage: 礼物消息
>     - WebcastSocialMessage: 社交消息
>     - WebcastLikeMessage: 点赞消息
>     - WebcastLinkMicFanTicketMethod: 连麦粉丝票方法
>     - WebcastLinkMicMethod: 连麦方法
> ### 返回:
> - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。
>
> # [English]
> ### Purpose:
> - Extract live room danmaku
> - This interface is no longer available online, you need to purchase the source code and deploy it locally for use. To purchase the source code, please contact the administrator in the Discord server. Discord invite link: https://discord.gg/aMEAS8Xsvz
> #### Price:
> - 0.001$ per 10 data, support tiered billing discount.
> ### Parameters:
> - live_room_url: Live room link
> - danmaku_type: Message type
>     - WebcastChatMessage: Chat message
>     - WebcastMemberMessage: Member message
>     - WebcastRoomUserSeqMessage: User sequence message
>     - WebcastGiftMessage: Gift message
>     - WebcastSocialMessage: Social message
>     - WebcastLikeMessage: Like message
>     - WebcastLinkMicFanTicketMethod: Link Mic Fan Ticket Method
>     - WebcastLinkMicMethod: Link Mic Method
> ### Return:
> - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get the danmaku data, this interface does not return the danmaku data.

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| live_room_url | query | string | Yes | 直播间链接/Live room link | None | https://www.tiktok.com/@mpl.id.official/live | None |
| danmaku_type | query | string | Yes | 消息类型/Message type | None | WebcastChatMessage | None |

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
