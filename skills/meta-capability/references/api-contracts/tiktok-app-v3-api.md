# TikTok-App-V3-API Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/tiktok-app-v3-api.md`](../api-tags/tiktok-app-v3-api.md)
- Current contract file: `api-contracts/tiktok-app-v3-api.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `75`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(TikTok-App-V3-API数据接口（当前最新版本）/TikTok-App-V3-API (Current latest version))**

## Route Contracts

<a id="post-api-u1-v1-tiktok-app-v3-ttencrypt-algorithm"></a>
### `POST /api/u1/v1/tiktok/app/v3/TTencrypt_algorithm`

- Summary: TikTok APP加密算法/TikTok APP encryption algorithm
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `TTencrypt_algorithm_api_v1_tiktok_app_v3_TTencrypt_algorithm_post`

#### Notes

> # [中文]
> ### 用途:
> - TikTok APP加密算法，用于生成请求头中的加密参数。
> - 生成的加密参数列表：
>     - `x-ladon`
>     - `x-khronos`
>     - `x-argus`
>     - `x-gorgon` （8404）
>
> ### 参数:
> - url: 需要加密的完整URL
> - data: 如果接口是POST请求，请填写POST请求的数据参与加密计算，GET请求时传入空字符串即可。
> - device_info: 设备信息，可选参数，如果不填写则使用默认设备信息，设备信息会修改传入的URL中的参数。
>
> ### 返回:
> - 加密参数列表
>
> # [English]
> ### Purpose:
> - TikTok APP encryption algorithm, used to generate encrypted parameters in the request header.
> - The generated encrypted parameter list:
>     - `x-ladon`
>     - `x-khronos`
>     - `x-argus`
>     - `x-gorgon` (8404)
>
> ### Parameters:
> - url: Full URL to be encrypted
> - data: If the interface is a POST request, please fill in the data of the POST request to participate in the encryption calculation. For GET requests, pass an empty string.
> - device_info: Device information, optional parameter, if not filled in, the default device information will be used, and the device information will modify the parameters in the URL passed in.
>
> ### Return:
> - Encrypted parameter list

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `url`:string, `data`:string, `device_info`{...}

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| url | string | No | 需要加密的URL/URL to be encrypted | https://api16-normal-useast5.tiktokv.us/tiktok/v1/upvote/item/list?user_id=6726… | None | None |
| data | string | No | 如果有POST请求，请填写POST请求的数据参与加密计算/If there is a POST request, please fill in the data of the POST request to participate in the encryption calculation | None | None | None |
| device_info | object | No | 设备信息，可选参数，如果不填写则使用默认设备信息/Device information, optional parameter, if not filled in, the default device information is used | {"aid": "1233", "cdid": "b820f79c-c74a-47b0-912f-ee3002ce60dc", "channel": "goo… | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-add-video-play-count"></a>
### `GET /api/u1/v1/tiktok/app/v3/add_video_play_count`

- Summary: 根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `add_video_play_count_api_v1_tiktok_app_v3_add_video_play_count_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据视频ID来增加作品的播放数
> ### 参数:
> - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
> - item_id: 作品id，别名为aweme_id
> - invite_code: 邀请码，此接口需要邀请码才能使用。
> ### 返回:
> - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。
>
> # [English]
> ### Purpose:
> - Increase the number of plays of the work according to the video ID
> ### Parameters:
> - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data interface.
> - item_id: Video id, alias aweme_id
> - invite_code: Invite code, this interface requires an invite code to use.
> ### Return:
> - The current timestamp and status code. When the status code is 200, it means success, otherwise it is a failure. You can try to change another work id and call it again, or wait for a period of time and call it again.
>
> # [示例/Example]
> aweme_type = 0
> item_id = "7419966340443819295"
> cookie = None

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_type | query | integer | Yes | 作品类型/Video type | None | 0 | None |
| item_id | query | string | Yes | 作品id/Video id | None | 7419966340443819295 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-check-live-room-online"></a>
### `GET /api/u1/v1/tiktok/app/v3/check_live_room_online`

- Summary: 检测直播间是否在线/Check if live room is online
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `check_live_room_online_api_v1_tiktok_app_v3_check_live_room_online_get`

#### Notes

> # [中文]
> ### 用途:
> - 检测直播间是否在线
> - 直播间的Room ID可以通过直播间链接从`/api/v1/tiktok/web/get_live_room_id`接口获取
> ### 参数:
> - room_id: 直播间id
> ### 返回:
> - 是否在线
>
> # [English]
> ### Purpose:
> - Check if live room is online
> - The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id` interface through the live room link
> ### Parameters:
> - room_id: Live room id
> ### Return:
> - Whether online
>
> # [示例/Example]
> room_id = "7358603858249009962"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id | None | 7358603858249009962 | None |

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

<a id="post-api-u1-v1-tiktok-app-v3-check-live-room-online-batch"></a>
### `POST /api/u1/v1/tiktok/app/v3/check_live_room_online_batch`

- Summary: 批量检测直播间是否在线/Batch check if live rooms are online
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `check_live_room_online_batch_api_v1_tiktok_app_v3_check_live_room_online_batch_post`

#### Notes

> # [中文]
> ### 用途:
> - 批量检测多个 TikTok 直播间是否在线，最大支持50个直播间ID
> - Room ID 可以通过 `/api/v1/tiktok/web/get_live_room_id` 获取
> ### 参数:
> - room_ids: 多个直播间 ID 的数组
> ### 返回:
> - 每个直播间的在线状态
>
> # [English]
> ### Purpose:
> - Batch check TikTok live rooms' online status, supports up to 50 room IDs
> - Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id`
> ### Parameters:
> - room_ids: List of TikTok live room IDs
> ### Return:
> - Online status per room
>
> # [示例/Example]
> ```
> payload = {
>     "room_ids": [
>         "7494491933781003054",
>         "7494514925034113835"
>     ]
> }
> ```

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `room_ids`[string]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| room_ids | array<string> | No | 多个直播间ID组成的数组 / List of TikTok live room IDs | ["7494491933781003054", "7494514925034113835", "7494520590523517739"] | None | None |

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

<a id="post-api-u1-v1-tiktok-app-v3-encrypt-decrypt-login-request"></a>
### `POST /api/u1/v1/tiktok/app/v3/encrypt_decrypt_login_request`

- Summary: 加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `encrypt_decrypt_login_request_api_v1_tiktok_app_v3_encrypt_decrypt_login_request_post`

#### Notes

> # [中文]
> ### 用途:
> - 加密/解密 TikTok APP 登录请求体，用于登录接口的请求体加密和解密。
> ### 参数:
> - username: 用户名，可以是密文或明文。
> - password: 密码，可以是密文或明文。
> - mode: 模式
>     - `encrypt`: 加密
>     - `decrypt`: 解密
> ### 返回:
> - 加密/解密后的请求体
>
> # [English]
> ### Purpose:
> - Encrypt/decrypt the TikTok APP login request body, used for encrypting and decrypting the request body of the login interface.
> ### Parameters:
> - username: Username, can be ciphertext or plaintext.
> - password: Password, can be ciphertext or plaintext.
> - mode: Mode
>     - `encrypt`: Encrypt
>     - `decrypt`: Decrypt
> ### Return:
> - Encrypted/decrypted request body
>
> # [示例/Example]
> ```json
> {
>     "username": "example_username",
>     "password": "example_password",
>     "mode": "encrypt"
> }
> ```

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `username`:string, `password`:string, `mode`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| username | string | No | Plaintext or encrypted username | example_username | None | None |
| password | string | No | Plaintext or encrypted password | example_password | None | None |
| mode | string enum[encrypt, decrypt] | No | Encrypt or decrypt the input string | encrypt | None | enum[encrypt, decrypt] |

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

<a id="post-api-u1-v1-tiktok-app-v3-fetch-content-translate"></a>
### `POST /api/u1/v1/tiktok/app/v3/fetch_content_translate`

- Summary: 获取内容翻译数据/Get content translation data
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_content_translate_api_v1_tiktok_app_v3_fetch_content_translate_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取内容翻译数据
> ### 参数:
> - trg_lang: 目标语言
>     - zh-Hans: 简体中文
>     - zh-Hant: 繁体中文
>     - en: 英语
>     - ja: 日语
>     - ko: 韩语
>     - fr: 法语
>     - de: 德语
>     - ru: 俄语
>     - es: 西班牙语
>     - pt: 葡萄牙语
>     - vi: 越南语
>     - th: 泰语
>     - id: 印尼语
>     - ar: 阿拉伯语
>     - it: 意大利语
>     - tr: 土耳其语
>     - he: 希伯来语
>     - pl: 波兰语
>     - nl: 荷兰语
>     - sv: 瑞典语
>     - da: 丹麦语
>     - fi: 芬兰语
>     - no: 挪威语
>     - cs: 捷克语
>     - hu: 匈牙利语
> - src_content: 源内容，也就是需要翻译的内容，长度不超过5000个字符，如果超过5000个字符，只会翻译前5000个字符。
> ### 返回:
> - 内容翻译数据
>
> # [English]
> ### Purpose:
> - Get content translation data
> ### Parameters:
> - trg_lang: Target language
>     - zh-Hans: Simplified Chinese
>     - zh-Hant: Traditional Chinese
>     - en: English
>     - ja: Japanese
>     - ko: Korean
>     - fr: French
>     - de: German
>     - ru: Russian
>     - es: Spanish
>     - pt: Portuguese
>     - vi: Vietnamese
>     - th: Thai
>     - id: Indonesian
>     - ar: Arabic
>     - it: Italian
>     - tr: Turkish
>     - he: Hebrew
>     - pl: Polish
>     - nl: Dutch
>     - sv: Swedish
>     - da: Danish
>     - fi: Finnish
>     - no: Norwegian
>     - cs: Czech
>     - hu: Hungarian
> - src_content: Source content, that is, the content that needs to be translated, the length does not exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be translated.
> ### Return:
> - Content translation data
>
> # [示例/Example]
> trg_lang = "zh-Hans"
> src_content = "Hello, welcome to TikHub!"

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `trg_lang`:string, `src_content`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| trg_lang | string | No | 目标语言ISO639-1代码，例如：zh-Hans/ Target language ISO639-1 code, e.g. zh-Hans | zh-Hans | None | None |
| src_content | string | No | 源语言内容，也就是需要翻译的内容/ Source language content, i.e. the content to be translated | Hello, welcome to TikHub! | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-creator-info"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_info`

- Summary: 获取带货创作者信息/Get shopping creator information
- Capabilities: creators
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_info_api_v1_tiktok_app_v3_fetch_creator_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者信息，包括创作者的基本信息、粉丝数、橱窗商品数量、带货直播间等信息。
> ### 参数:
> - creator_uid: 创作者uid
> ### 返回:
> - 创作者信息
>
> # [English]
> ### Purpose:
> - Get creator information, including the creator's basic information, number of fans, number of storefront products, shop live room and other information.
> ### Parameters:
> - creator_uid: Creator uid
> ### Return:
> - Creator information
>
> # [示例/Example]
> creator_uid = "6555451606845243393"
>
> # [示例响应/Example Response]
> response = {
>     "code": 200,
>     "request_id": "d5575d80-a8cc-44ab-a46a-b62c2e967829",
>     "router": "/api/v1/tiktok/app/v3/fetch_creator_info",
>     "params": {
>         "creator_uid": "6555451606845243393"
>     },
>     "data": {
>         "code": 0,
>         "data": {
>             "creator_info": {
>                 "creator_id": "6555451606845243393",
>                 "creator_name": "louissescarlettFamily's showcase",
>                 "avatar": {
>                     "uri": "720x720/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248",
>                     "url_list": [
>                         "https://p19-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.webp?dr=9640&refresh_token=fd81a69e&x-expires=1756022400&x-signature=neQwNv%2BxfA4YPnLFb51270Zi8Ps%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5",
>                         "https://p16-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.webp?dr=9640&refresh_token=723df957&x-expires=1756022400&x-signature=9q4A2SUIO%2B42lqTsrVkkpks54dI%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5",
>                         "https://p19-common-sign-sg.tiktokcdn-us.com/tos-alisg-avt-0068/28257cac3d733b5e4bc12655685fc248~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=d63d422b&x-expires=1756022400&x-signature=sycMEH0640dpjl%2BK0nDy1ZPbtxs%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=85ba3243&idc=useast5"
>                     ]
>                 },
>                 "followers_info": {
>                     "count": "18017938",
>                     "count_info": "18.0M followers",
>                     "value": 18017938,
>                     "count_format": "18.0M"
>                 },
>                 "sold_count_info": {
>                     "count": "0",
>                     "value": 0
>                 },
>                 "bg_pic": {
>                     "uri": "tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg",
>                     "url_list": [
>                         "https://p19-oec-general.ttcdn-us.com/tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg~tplv-fhlh96nyum-resize-jpeg:1600:1600.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398",
>                         "https://p16-oec-general.ttcdn-us.com/tos-alisg-i-aphluv4xwc-sg/72edb551d7c77636678a5518cdddfd1c.jpg~tplv-fhlh96nyum-resize-jpeg:1600:1600.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398"
>                     ]
>                 },
>                 "is_banned": false,
>                 "sec_user_id": "MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux",
>                 "follow_status_extended": 0,
>                 "show_follow_button": false,
>                 "can_share": false,
>                 "show_commission_paid": "Creator earns commission",
>                 "product_count_info": {
>                     "count": "713",
>                     "count_info": "713 products",
>                     "value": 713,
>                     "count_format": "713"
>                 },
>                 "dark_bg_pic_new": {
>                     "uri": "tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png",
>                     "url_list": [
>                         "https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398",
>                         "https://p19-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_dark.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398"
>                     ]
>                 },
>                 "light_bg_pic_new": {
>                     "uri": "tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png",
>                     "url_list": [
>                         "https://p16-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398",
>                         "https://p19-oec-general.ttcdn-us.com/tos-maliva-i-acgf4d7es9-us/showcase_header_v2_light.png~tplv-fhlh96nyum-resize-jpeg:1170:699.jpeg?dr=12186&t=555f072d&ps=933b5bde&shp=4ee6669e&shcp=9b759fb9&idc=useast5&from=1323722398"
>                     ]
>                 },
>                 "is_new_header": true,
>                 "dynamic_header": {
>                     "is_dynamic": false,
>                     "delay_time": 0
>                 },
>                 "extra_val": {
>                     "showcase_no_product_show_less_screen": "0",
>                     "us_uk_show_voucher_info": "0"
>                 }
>             },
>             "live_info": {
>                 "room_id": "7541231942331566853",
>                 "upcoming_event_time": "1756141200"
>             },
>             "diversion_module": 0
>         },
>         "message": "success"
>     }
> }

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| creator_uid | query | string | Yes | 创作者uid/Creator uid | None | 6555451606845243393 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights`

- Summary: 创作者搜索洞察/Creator Search Insights
- Capabilities: search / creators / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_api_v1_tiktok_app_v3_fetch_creator_search_insights_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者搜索洞察数据，用于了解热门搜索趋势和创作灵感
> ### 参数:
> - offset: 分页偏移量，默认0
> - limit: 每页数量，默认20
> - tab: 标签页类型，可选值:
>     - all: 全部
>     - content_gap: 内容差距
>     - follower_searched: 粉丝常搜
>     - life_style: 生活方式
>     - topics: 话题
>     - challenges: 挑战
>     - sounds: 声音
>     - hashtags: 标签
> - language_filters: 语言过滤器，多个用逗号分隔，可选值: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko
> - category_filters: 分类过滤器，多个用逗号分隔，可选值: Gaming, Fashion, Tourism, Science, Food, Sports
> - creator_source: 创作者来源，默认 "general_search"
> - force_refresh: 是否强制刷新，默认 False
> ### 返回:
> - 创作者搜索洞察数据
>
> # [English]
> ### Purpose:
> - Get creator search insights data, used to understand trending search topics and creative inspiration
> ### Parameters:
> - offset: Pagination offset, default 0
> - limit: Number per page, default 20
> - tab: Tab type, options:
>     - all: All
>     - content_gap: Content gap
>     - follower_searched: Follower searched
>     - life_style: Life style
>     - topics: Topics
>     - challenges: Challenges
>     - sounds: Sounds
>     - hashtags: Hashtags
> - language_filters: Language filters, separated by comma, options: id, de, en, es, fr, pt, vi, tr, ar, th, ja, ko
> - category_filters: Category filters, separated by comma, options: Gaming, Fashion, Tourism, Science, Food, Sports
> - creator_source: Creator source, default "general_search"
> - force_refresh: Force refresh, default False
> ### Return:
> - Creator search insights data
>
> # [示例/Example]
> offset = 0
> limit = 20
> tab = "all"
> language_filters = "en"
> category_filters = "Gaming"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| offset | query | integer | No | 分页偏移量/Pagination offset | 0 | 0 | None |
| limit | query | integer | No | 每页数量/Number per page | 20 | 20 | None |
| tab | query | string | No | 标签页类型/Tab type (all/content_gap/follower_searched/life_style/topics/challenges/sounds/hashtags) | all | all | None |
| language_filters | query | string | No | 语言过滤器，多个用逗号分隔/Language filters (id/de/en/es/fr/pt/vi/tr/ar/th/ja/ko) | en | en | None |
| category_filters | query | string | No | 分类过滤器，多个用逗号分隔/Category filters (Gaming/Fashion/Tourism/Science/Food/Sports) | None | None | None |
| creator_source | query | string | No | 创作者来源/Creator source | general_search | general_search | None |
| force_refresh | query | boolean | No | 是否强制刷新/Force refresh | false | false | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-detail"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_detail`

- Summary: 创作者搜索洞察详情/Creator Search Insights Detail
- Capabilities: search / creators / details / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_detail_api_v1_tiktok_app_v3_fetch_creator_search_insights_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者搜索洞察详情数据，用于查询特定搜索词条的搜索统计数据
> ### 参数:
> - query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口返回的数据中获取
> - time_range: 时间范围，可选值:
>     - past_7_days: 过去7天
>     - past_30_days: 过去30天（默认）
>     - past_60_days: 过去60天
>     - past_6_months: 过去6个月
>     - custom: 自定义时间（需配合 start_date 和 end_date 使用，不能超过6个月）
> - start_date: 开始时间戳（秒），仅当 time_range=custom 时生效
> - end_date: 结束时间戳（秒），仅当 time_range=custom 时生效
> - dimension_list: 维度列表，多个用逗号分隔，可选值: gender（性别）, age（年龄）, country（国家）
> ### 返回:
> - 搜索洞察详情数据，包含搜索趋势、用户画像等
>
> # [English]
> ### Purpose:
> - Get creator search insights detail data, used to query search statistics for specific query
> ### Parameters:
> - query_id_str: Query ID, obtained from fetch_creator_search_insights response
> - time_range: Time range, options:
>     - past_7_days: Past 7 days
>     - past_30_days: Past 30 days (default)
>     - past_60_days: Past 60 days
>     - past_6_months: Past 6 months
>     - custom: Custom range (requires start_date and end_date, cannot exceed 6 months)
> - start_date: Start timestamp (seconds), only for custom range
> - end_date: End timestamp (seconds), only for custom range
> - dimension_list: Dimension list, separated by comma, options: gender, age, country
> ### Return:
> - Search insights detail data, including search trends, user demographics, etc.
>
> # [示例/Example]
> query_id_str = "122991006"
> time_range = "past_30_days"
> dimension_list = "gender,age,country"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query_id_str | query | string | Yes | 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights | None | 122991006 | None |
| time_range | query | string | No | 时间范围/Time range (past_7_days/past_30_days/past_60_days/past_6_months/custom) | past_30_days | past_30_days | None |
| start_date | query | integer | No | 开始时间戳（秒），仅当 time_range=custom 时生效/Start timestamp (seconds), only for custom range | None | None | None |
| end_date | query | integer | No | 结束时间戳（秒），仅当 time_range=custom 时生效/End timestamp (seconds), only for custom range | None | None | None |
| dimension_list | query | string | No | 维度列表，多个用逗号分隔/Dimension list (gender/age/country) | gender,age,country | gender,age,country | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-trend"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_trend`

- Summary: 创作者搜索洞察趋势/Creator Search Insights Trend
- Capabilities: search / trends / rankings / creators / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_trend_api_v1_tiktok_app_v3_fetch_creator_search_insights_trend_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者搜索洞察趋势数据，包含地区和时间维度的搜索热度
> ### 参数:
> - query_id_str: 搜索词条ID，从 fetch_creator_search_insights 接口返回的数据中获取
> - from_tab_path: 来源标签路径，默认 "TRENDING,TOPICS"
> - query_analysis_required: 是否需要查询分析，默认 True
> ### 返回:
> - 搜索趋势数据，包含地区热度、时间趋势等
>
> # [English]
> ### Purpose:
> - Get creator search insights trend data, including search popularity by region and time
> ### Parameters:
> - query_id_str: Query ID, obtained from fetch_creator_search_insights response
> - from_tab_path: From tab path, default "TRENDING,TOPICS"
> - query_analysis_required: Whether query analysis is required, default True
> ### Return:
> - Search trend data, including regional popularity, time trends, etc.
>
> # [示例/Example]
> query_id_str = "7555720035176562699"
> from_tab_path = "TRENDING,TOPICS"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| query_id_str | query | string | Yes | 搜索词条ID，从 fetch_creator_search_insights 接口获取/Query ID from fetch_creator_search_insights | None | 7555720035176562699 | None |
| from_tab_path | query | string | No | 来源标签路径/From tab path | TRENDING,TOPICS | TRENDING,TOPICS | None |
| query_analysis_required | query | boolean | No | 是否需要查询分析/Whether query analysis is required | true | true | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-creator-search-insights-videos"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_search_insights_videos`

- Summary: 创作者搜索洞察相关视频/Creator Search Insights Videos
- Capabilities: search / creators / content details / analytics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_search_insights_videos_api_v1_tiktok_app_v3_fetch_creator_search_insights_videos_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者搜索洞察相关视频，查询该搜索词条下比较火的相关视频
> ### 参数:
> - keyword: 搜索关键词，从 fetch_creator_search_insights 或 fetch_creator_search_insights_trend 接口获取
> - offset: 分页偏移量，默认0
> - count: 每页数量，默认20
> ### 返回:
> - 相关热门视频列表
>
> # [English]
> ### Purpose:
> - Get creator search insights related videos, query popular related videos for the search term
> ### Parameters:
> - keyword: Search keyword, obtained from fetch_creator_search_insights or fetch_creator_search_insights_trend
> - offset: Pagination offset, default 0
> - count: Number per page, default 20
> ### Return:
> - Related popular videos list
>
> # [示例/Example]
> keyword = "headshots 2 2 3"
> offset = 0
> count = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | headshots 2 2 3 | None |
| offset | query | integer | No | 分页偏移量/Pagination offset | 0 | 0 | None |
| count | query | integer | No | 每页数量/Number per page | 20 | 20 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-creator-showcase-product-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_creator_showcase_product_list`

- Summary: 获取创作者橱窗商品列表/Get creator showcase product list
- Capabilities: creators / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_creator_showcase_product_list_api_v1_tiktok_app_v3_fetch_creator_showcase_product_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取创作者橱窗商品列表
> ### 参数:
> - kol_id: 创作者的sec_user_id
> - count: 数量
> - next_scroll_param: 翻页参数，第一页为空字符串，后续请求使用上一次请求返回的next_scroll_param值。
> ### 返回:
> - 创作者橱窗商品列表
>
> # [English]
> ### Purpose:
> - Get creator showcase product list
> ### Parameters:
> - kol_id: Creator's sec_user_id
> - count: Number
> - next_scroll_param: Page parameter, empty string for the first page, use the next_scroll_param value returned by the last request for subsequent requests.
> ### Return:
> - Creator showcase product list
>
> # [示例/Example]
> kol_id = "MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux"
> count = 20
> next_scroll_param = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kol_id | query | string | Yes | 创作者的sec_user_id/Creator's sec_user_id | None | MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux | None |
| count | query | integer | No | 数量/Number | 20 | None | None |
| next_scroll_param | query | string | No | 翻页参数/Page parameter | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-general-search-result"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_general_search_result`

- Summary: 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_general_search_result_api_v1_tiktok_app_v3_fetch_general_search_result_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定关键词的综合搜索结果
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> - sort_type: 0-相关度，1-最多点赞
> - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年
> ### 返回:
> - 综合搜索结果
>
> # [English]
> ### Purpose:
> - Get comprehensive search results of specified keywords
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> - sort_type: 0-Relatedness, 1-Most likes
> - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year
> ### Return:
> - Comprehensive search results
>
> # [示例/Example]
> keyword = "中华娘"
> offset = 0
> count = 20
> sort_type = 0
> publish_time = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | 中华娘 | None |
| offset | query | integer | No | 偏移量/Offset | 0 | 0 | None |
| count | query | integer | No | 数量/Number | 20 | 20 | None |
| sort_type | query | integer | No | 排序类型/Sort type | 0 | 0 | None |
| publish_time | query | integer | No | 发布时间/Publish time | 0 | 0 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-hashtag-detail"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_detail`

- Summary: 获取指定话题的详情数据/Get details of specified hashtag
- Capabilities: details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_detail_api_v1_tiktok_app_v3_fetch_hashtag_detail_get`

#### Notes

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
> ch_id = "7551"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_id | query | string | Yes | 话题id/Hashtag id | None | 7551 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-hashtag-search-result"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_search_result`

- Summary: 获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords
- Capabilities: search / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_search_result_api_v1_tiktok_app_v3_fetch_hashtag_search_result_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定关键词的话题搜索结果
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> ### 返回:
> - 话题搜索结果
>
> # [English]
> ### Purpose:
> - Get hashtag search results of specified keywords
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> ### Return:
> - Hashtag search results
>
> # [示例/Example]
> keyword = "Cat"
> offset = 0
> count = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | Cat | None |
| offset | query | integer | No | 偏移量/Offset | 0 | None | None |
| count | query | integer | No | 数量/Number | 20 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-hashtag-video-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_hashtag_video_list`

- Summary: 获取指定话题的作品数据/Get video list of specified hashtag
- Capabilities: content details / topics
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_hashtag_video_list_api_v1_tiktok_app_v3_fetch_hashtag_video_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定话题的作品数据
> ### 参数:
> - ch_id: 话题id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量
> ### 返回:
> - 话题作品数据
>
> # [English]
> ### Purpose:
> - Get video list of specified hashtag
> ### Parameters:
> - ch_id: Hashtag id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number
> ### Return:
> - Hashtag video list data
>
> # [示例/Example]
> ch_id = "7551"
> cursor = 0
> sort_type = 0
> count = 10

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ch_id | query | string | Yes | 话题id/Hashtag id | None | 7551 | None |
| cursor | query | integer | No | 游标/Cursor | 0 | None | None |
| count | query | integer | No | 数量/Number | 10 | None | None |

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

<a id="post-api-u1-v1-tiktok-app-v3-fetch-home-feed"></a>
### `POST /api/u1/v1/tiktok/app/v3/fetch_home_feed`

- Summary: 获取主页视频推荐数据/Get home feed(recommend) video data
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_home_feed_api_v1_tiktok_app_v3_fetch_home_feed_post`

#### Notes

> # [中文]
> ### 用途:
> - 获取主页视频推荐数据
> ### 参数:
> - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。
> ### 返回:
> - 视频推荐数据
>
> # [English]
> ### Purpose:
> - Get home feed(recommend) video data
> ### Parameters:
> - cookie: User's own cookie, optional parameter, used for personalized recommendation of interface returned data.
> ### Return:
> - Video recommend data

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: `cookie`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-live-daily-rank"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_live_daily_rank`

- Summary: 获取直播每日榜单数据/Get live daily rank data
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_daily_rank_api_v1_tiktok_app_v3_fetch_live_daily_rank_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取直播每日榜单数据
> ### 参数:
> - anchor_id: 主播id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的主播id。
> - room_id: 直播间id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的id。
> - rank_type: 榜单类型，参数值如下表：
>
>     | type | rankName | 分组类型 | 说明 |
>     |------|----------|----------|------|
>     | 0 | `hourly_rank` | GIFT_RANK | 小时榜 |
>     | 1 | `weekly_rank` | GIFT_RANK | 周榜 |
>     | 5 | `rookie_star_rank` | GIFT_RANK | 新星榜 |
>     | 6 | `sale_rank` | E_COMMERCE | 带货榜 |
>     | 8 | `daily_rank` | GIFT_RANK | 日榜 |
>     | 10 | `weekly_game_rank` | GAME_RANK | 周游戏榜 |
>     | 11 | `daily_game_rank` | GAME_RANK | 日游戏榜 |
>     | 12 | `hall_of_fame_rank` | GIFT_RANK | 名人堂 |
>     | 13 | `champion_tournament` | GIFT_RANK | 冠军赛（含phase_one/two/three） |
>     | 14 | `daily_rookie_star_rank` | GIFT_RANK | 日新星榜 |
>     | 15 | `fans_team_rank` | GIFT_RANK | 粉丝团榜 |
>     | 16 | `ranking_league` | GIFT_RANK | 排位联赛（App内显示: D5段位榜） |
>     | 20 | `pubg` | GAME_RANK | PUBG游戏榜 |
>     | 21 | `mlbb` | GAME_RANK | MLBB游戏榜（Mobile Legends: Bang Bang） |
>     | 22 | `free_fire` | GAME_RANK | Free Fire游戏榜 |
>     | 23 | `sub_weekly_game_rank1` | GAME_RANK | 子周游戏榜1 |
>     | 24 | `sub_weekly_game_rank2` | GAME_RANK | 子周游戏榜2 |
>     | 25 | `sub_weekly_game_rank3` | GAME_RANK | 子周游戏榜3 |
>     | 26 | `collectibles` | E_COMMERCE | 收藏品榜 |
>     | 27 | `beauty` | E_COMMERCE | 美妆榜 |
>     | 28 | `women_wear` | E_COMMERCE | 女装榜 |
>     | 29 | `sale_rank_daily` | E_COMMERCE | 日带货榜 |
>     | 1001 | `league_campaign_rank` | GIFT_RANK | 联赛活动榜 |
>     | -1 | `unknown` | DEFAULT | 未知 |
>
> - region_type: 地区类型，使用默认值即可，具体含义不明。
> - gap_interval: 时间间隔，使用默认值代表当天，使用-1代表排名记录。
> - cookie: 用户自己的cookie，可选参数，用于接口不可用时使用。
> ### 返回:
> - 直播每日榜单数据
>
> # [English]
> ### Purpose:
> - Get live daily rank data
> ### Parameters:
> - anchor_id: Anchor id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different anchor ids of different live rooms.
> - room_id: Live room id, which can be obtained from the live room information interface, use the default value, this parameter will affect the returned data, you can try different room ids of different live rooms.
> - rank_type: Rank type, parameter values are as follows:
>
>     | type | rankName | Group Type | Description |
>     |------|----------|------------|-------------|
>     | 0 | `hourly_rank` | GIFT_RANK | Hourly Rank |
>     | 1 | `weekly_rank` | GIFT_RANK | Weekly Rank |
>     | 5 | `rookie_star_rank` | GIFT_RANK | Rookie Star Rank |
>     | 6 | `sale_rank` | E_COMMERCE | Sale Rank |
>     | 8 | `daily_rank` | GIFT_RANK | Daily Rank |
>     | 10 | `weekly_game_rank` | GAME_RANK | Weekly Game Rank |
>     | 11 | `daily_game_rank` | GAME_RANK | Daily Game Rank |
>     | 12 | `hall_of_fame_rank` | GIFT_RANK | Hall of Fame Rank |
>     | 13 | `champion_tournament` | GIFT_RANK | Champion Tournament (includes phase_one/two/three) |
>     | 14 | `daily_rookie_star_rank` | GIFT_RANK | Daily Rookie Star Rank |
>     | 15 | `fans_team_rank` | GIFT_RANK | Fans Team Rank |
>     | 16 | `ranking_league` | GIFT_RANK | Ranking League (App display: D5 Level Rank) |
>     | 20 | `pubg` | GAME_RANK | PUBG Rank |
>     | 21 | `mlbb` | GAME_RANK | MLBB Rank (Mobile Legends: Bang Bang) |
>     | 22 | `free_fire` | GAME_RANK | Free Fire Rank |
>     | 23 | `sub_weekly_game_rank1` | GAME_RANK | Sub Weekly Game Rank 1 |
>     | 24 | `sub_weekly_game_rank2` | GAME_RANK | Sub Weekly Game Rank 2 |
>     | 25 | `sub_weekly_game_rank3` | GAME_RANK | Sub Weekly Game Rank 3 |
>     | 26 | `collectibles` | E_COMMERCE | Collectibles Rank |
>     | 27 | `beauty` | E_COMMERCE | Beauty Rank |
>     | 28 | `women_wear` | E_COMMERCE | Women Wear Rank |
>     | 29 | `sale_rank_daily` | E_COMMERCE | Daily Sale Rank |
>     | 1001 | `league_campaign_rank` | GIFT_RANK | League Campaign Rank |
>     | -1 | `unknown` | DEFAULT | Unknown |
>
> - region_type: Region type, use the default value, the specific meaning is unknown.
> - gap_interval: Time interval, use the default value to represent the current day, use -1 to represent the ranking record.
> - cookie: User's own cookie, optional parameter, used when the interface is not available.
> ### Return:
> - Live daily rank data

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anchor_id | query | string | No | 主播id/Anchor id | 6952422426752205830 | None | None |
| room_id | query | string | No | 直播间id/Live room id | 7380221319910312750 | None | None |
| rank_type | query | integer | No | 榜单类型/Rank type | 8 | None | None |
| region_type | query | integer | No | 地区类型/Region type | 1 | None | None |
| gap_interval | query | integer | No | 时间间隔/Time interval | 0 | None | None |
| cookie | query | string | No | 用户自己的cookie/User's own cookie | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-live-ranking-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_live_ranking_list`

- Summary: 获取直播间排行榜数据/Get live room ranking list
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_ranking_list_api_v1_tiktok_app_v3_fetch_live_ranking_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取直播间内观众的排行榜数据
> ### 参数:
> - room_id: 直播间id
> - anchor_id: 主播id
> ### 返回:
> - 排行榜数据
>
> # [English]
> ### Purpose:
> - Get ranking list of audience in live room
> ### Parameters:
> - room_id: Live room id
> - anchor_id: Anchor id
> ### Return:
> - Ranking list data
>
> # [示例/Example]
> room_id = "7358603858249009962"
> anchor_id = "7222941468722758702"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id | None | 7358603858249009962 | None |
| anchor_id | query | string | Yes | 主播id/Anchor id | None | 7222941468722758702 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-live-room-info"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_info`

- Summary: 获取指定直播间的数据/Get data of specified live room
- Capabilities: livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_room_info_api_v1_tiktok_app_v3_fetch_live_room_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定直播间的数据
> ### 参数:
> - room_id: 直播间id
> ### 返回:
> - 直播间数据
>
> # [English]
> ### Purpose:
> - Get data of specified live room
> ### Parameters:
> - room_id: Live room id
> ### Return:
> - Live room data
>
> # [示例/Example]
> room_id = "7385461256746060575"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id | None | 7358603858249009962 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list`

- Summary: 获取直播间商品列表数据/Get live room product list data
- Capabilities: commerce / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_room_product_list_api_v1_tiktok_app_v3_fetch_live_room_product_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取直播间商品列表数据
> ### 参数:
> - room_id: 直播间id，必填参数。
> - author_id: 主播id，必填参数。
> - page_size: 每页数量，可选参数，默认为15。
> - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。
> - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。
> - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。
> ### 参数获取:
> - 第一步：使用接口`f"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id"`接口获取直播间id（room_id）。
> - 第二步：使用接口`f"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info"`接口获取直播间信息。
> - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。
> ### 返回:
> - 直播间商品列表数据
>
> # [English]
> ### Purpose:
> - Get live room product list data
> ### Parameters:
> - room_id: Live room id, required parameter.
> - author_id: Anchor id, required parameter.
> - page_size: Number per page, optional parameter, default is 15.
> - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time.
> - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`, please bring your own Cookie, otherwise you will not be able to get data.
> - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`.
> ### Get Parameters:
> - Step 1: Use the interface `f"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id"` to get the live room id (room_id).
> - Step 2: Use the interface `f"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info"` to get the live room information.
> - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the field `$.data.data.owner.id_str` as the anchor id (author_id).
> ### Return:
> - Live room product list data
>
> # [示例/Example]
> room_id = "7420741353250507562"
> author_id = "7408859677050274859"
> page_size = 15
> offset = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id | None | 7420741353250507562 | None |
| author_id | query | string | Yes | 主播id/Anchor id | None | 7408859677050274859 | None |
| page_size | query | integer | No | 数量/Number | 15 | None | None |
| offset | query | integer | No | 数量/Number | 0 | None | None |
| region | query | string | No | 地区/Region | US | None | None |
| cookie | query | string | No | 用户自己的cookie/User's own cookie | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-live-room-product-list-v2"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_live_room_product_list_v2`

- Summary: 获取直播间商品列表数据 V2 /Get live room product list data V2
- Capabilities: commerce / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_room_product_list_v2_api_v1_tiktok_app_v3_fetch_live_room_product_list_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取直播间商品列表数据 V2
> ### 参数:
> - room_id: 直播间id，必填参数。
> - author_id: 主播id，必填参数。
> - page_size: 每页数量，可选参数，默认为15。
> - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。
> - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。
> - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。
> ### 参数获取:
> - 第一步：使用接口`f"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id"`接口获取直播间id（room_id）。
> - 第二步：使用接口`f"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info"`接口获取直播间信息。
> - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。
> ### 返回:
> - 直播间商品列表数据
>
> # [English]
> ### Purpose:
> - Get live room product list data V2
> ### Parameters:
> - room_id: Live room id, required parameter.
> - author_id: Anchor id, required parameter.
> - page_size: Number per page, optional parameter, default is 15.
> - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time.
> - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`, please bring your own Cookie, otherwise you will not be able to get data.
> - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`.
> ### Get Parameters:
> - Step 1: Use the interface `f"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id"` to get the live room id (room_id).
> - Step 2: Use the interface `f"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info"` to get the live room information.
> - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the field `$.data.data.owner.id_str` as the anchor id (author_id).
> ### Return:
> - Live room product list data
>
> # [示例/Example]
> room_id = "7420741353250507562"
> author_id = "7408859677050274859"
> page_size = 15
> offset = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| room_id | query | string | Yes | 直播间id/Live room id | None | 7420741353250507562 | None |
| author_id | query | string | Yes | 主播id/Anchor id | None | 7408859677050274859 | None |
| page_size | query | integer | No | 数量/Number | 15 | None | None |
| offset | query | integer | No | 数量/Number | 0 | None | None |
| region | query | string | No | 地区/Region | US | None | None |
| cookie | query | string | No | 用户自己的cookie/User's own cookie | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-live-search-result"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_live_search_result`

- Summary: 获取指定关键词的直播搜索结果/Get live search results of specified keywords
- Capabilities: search / livestream
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_live_search_result_api_v1_tiktok_app_v3_fetch_live_search_result_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定关键词的直播搜索结果
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量，从0开始，第二页从响应中获取cursor的值作为offset继续请求。
> - count: 数量，不要超过20
> - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。
> ### 返回:
> - 直播搜索结果
>
> # [English]
> ### Purpose:
> - Get live search results of specified keywords
> ### Parameters:
> - keyword: Keyword
> - offset: Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request.
> - count: Number, do not exceed 20
> - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes.
> ### Return:
> - Live search results
>
> # [示例/Example]
> keyword = "Cat"
> offset = 0
> count = 20
> region = "US"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | Cat | None |
| offset | query | integer | No | 偏移量/Offset | 0 | 0 | None |
| count | query | integer | No | 数量/Number | 20 | 20 | None |
| region | query | string | No | 地区/Region | US | US | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-location-search"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_location_search`

- Summary: 获取地点搜索结果/Get location search results
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_location_search_api_v1_tiktok_app_v3_fetch_location_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取地点搜索结果
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> ### 返回:
> - 地点搜索结果
>
> # [English]
> ### Purpose:
> - Get location search results
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> ### Return:
> - Location search results
>
> # [示例/Example]
> keyword = "Shanghai"
> offset = 0
> count = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | Shanghai | None |
| offset | query | integer | No | 偏移量/Offset | 0 | None | None |
| count | query | integer | No | 数量/Number | 20 | None | None |

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

<a id="post-api-u1-v1-tiktok-app-v3-fetch-multi-video"></a>
### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video`

- Summary: 批量获取视频信息/Batch Get Video Information
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_api_v1_tiktok_app_v3_fetch_multi_video_post`

#### Notes

> # [中文]
> ### 用途:
> - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。
> - 如果本接口报错，请使用 fetch_multi_video_v3 接口。
> ### 参数:
> - aweme_ids: 作品id列表，最多支持10个作品id。
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface charges a fixed price of 0.001$ * 10 = 0.01$ each time.
> - If this interface reports an error, please use the fetch_multi_video_v3 interface.
> ### Parameters:
> - aweme_ids: List of video ids, up to 10 video ids are supported.
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_ids = [
>         "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570",
>         "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570",
>     ]

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | Yes | 作品id列表/Video id list | None | None | None |

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

<a id="post-api-u1-v1-tiktok-app-v3-fetch-multi-video-v2"></a>
### `POST /api/u1/v1/tiktok/app/v3/fetch_multi_video_v2`

- Summary: 批量获取视频信息 V2/Batch Get Video Information V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_multi_video_v2_api_v1_tiktok_app_v3_fetch_multi_video_v2_post`

#### Notes

> # [中文]
> ### 用途:
> - 批量获取视频信息，支持图文、视频等，一次性最多支持25个视频，此接口收费固定价格为0.001$ * 25 = 0.025$一次。
> - 注意：此接口为V2版本，支持更多功能和更高效的数据获取，一秒可以获取25个视频数据。
> - 如果本接口报错，请使用 fetch_multi_video_v3 接口。
> ### 参数:
> - aweme_ids: 作品id列表，最多支持25个作品id。
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Batch Get Video Information, support photo, video, etc., up to 25 videos at a time, this interface charges a fixed price of 0.001$ * 25 = 0.025$ each time.
> - Note: This interface is the V2 version, which supports more features and more efficient data retrieval, can retrieve 25 video data per second.
> - If this interface reports an error, please use the fetch_multi_video_v3 interface.
> ### Parameters:
> - aweme_ids: List of video ids, up to 25 video ids are supported.
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_ids = [
>         "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570",
>         "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570", "7339393672959757570",
>     ]

#### Parameters

None

#### Request Body

- required: Yes

##### `application/json`

- Schema summary: [string]

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| [] | array<string> | Yes | 作品id列表/Video id list | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-music-chart-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_music_chart_list`

- Summary: 音乐排行榜/Music Chart List
- Capabilities: music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_chart_list_api_v1_tiktok_app_v3_fetch_music_chart_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取TikTok音乐排行榜数据
> ### 参数:
> - scene: 排行榜类型
>     - 0: Top 50 (热门前50)
>     - 1: Viral 50 (病毒式传播前50)
> - cursor: 分页游标，默认0
> - count: 每页数量，默认50，最大50
> ### 返回:
> - 音乐排行榜数据，包含歌曲信息、排名变化等
>
> # [English]
> ### Purpose:
> - Get TikTok music chart list data
> ### Parameters:
> - scene: Chart type
>     - 0: Top 50 (Popular top 50)
>     - 1: Viral 50 (Viral top 50)
> - cursor: Pagination cursor, default 0
> - count: Number per page, default 50, max 50
> ### Return:
> - Music chart data, including song info, ranking changes, etc.
>
> # [示例/Example]
> scene = 0  # Top 50
> cursor = 0
> count = 50

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| scene | query | integer | No | 排行榜类型/Chart type (0: Top 50, 1: Viral 50) | 0 | 0 | None |
| cursor | query | integer | No | 分页游标/Pagination cursor | 0 | 0 | None |
| count | query | integer | No | 每页数量/Number per page (max 50) | 50 | 50 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-music-detail"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_music_detail`

- Summary: 获取指定音乐的详情数据/Get details of specified music
- Capabilities: details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_detail_api_v1_tiktok_app_v3_fetch_music_detail_get`

#### Notes

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
> music_id = "6943027371519772674"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| music_id | query | string | Yes | 音乐id/Music id | None | 6943027371519772674 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-music-search-result"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_music_search_result`

- Summary: 获取指定关键词的音乐搜索结果/Get music search results of specified keywords
- Capabilities: search / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_search_result_api_v1_tiktok_app_v3_fetch_music_search_result_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定关键词的音乐搜索结果
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量，从0开始，第二页从响应中获取cursor的值作为offset继续请求。
> - count: 数量，不要超过20
> - filter_by: 过滤类型，0-全部，1-标题，2-作者，默认为0-全部
> - sort_type: 排序类型，0-相关度，1-最多使用，2-最新，3-时长最短，4-时长最长，默认为0-相关度
> - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。
> ### 返回:
> - 音乐搜索结果
>
> # [English]
> ### Purpose:
> - Get music search results of specified keywords
> ### Parameters:
> - keyword: Keyword
> - offset: Offset, starting from 0, the second page gets the cursor value from the response as the offset to continue the request.
> - count: Number, do not exceed 20
> - filter_by: Filter type, 0-All, 1-Title, 2-Author, default is 0-All
> - sort_type: Sort type, 0-Relatedness, 1-Most used, 2-Latest, 3-Shortest duration, 4-Longest duration, default is 0-Relatedness
> - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes.
> ### Return:
> - Music search results
>
> # [示例/Example]
> keyword = "Cat"
> offset = 0
> count = 20
> filter_by = 0
> sort_type = 0
> region = "US"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | Cat | None |
| offset | query | integer | No | 偏移量/Offset | 0 | 0 | None |
| count | query | integer | No | 数量/Number | 20 | 20 | None |
| filter_by | query | integer | No | 过滤类型/Filter type | 0 | 0 | None |
| sort_type | query | integer | No | 排序类型/Sort type | 0 | 0 | None |
| region | query | string | No | 地区/Region | US | US | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-music-video-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_music_video_list`

- Summary: 获取指定音乐的视频列表数据/Get video list of specified music
- Capabilities: content details / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_music_video_list_api_v1_tiktok_app_v3_fetch_music_video_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定音乐的视频列表数据
> ### 参数:
> - music_id: 音乐id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量
> ### 返回:
> - 音乐视频列表数据
>
> # [English]
> ### Purpose:
> - Get video list of specified music
> ### Parameters:
> - music_id: Music id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number
> ### Return:
> - Music video list data
>
> # [示例/Example]
> music_id = "6943027371519772674"
> cursor = 0
> count = 10

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| music_id | query | string | Yes | 音乐id/Music id | None | 6943027371519772674 | None |
| cursor | query | integer | No | 游标/Cursor | 0 | None | None |
| count | query | integer | No | 数量/Number | 10 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-one-video"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video`

- Summary: 获取单个作品数据/Get single video data
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_api_v1_tiktok_app_v3_fetch_one_video_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品数据
> ### 参数:
> - aweme_id: 作品id
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data
> ### Parameters:
> - aweme_id: Video id
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_id = "7350810998023949599"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id | None | 7350810998023949599 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url`

- Summary: 根据分享链接获取单个作品数据/Get single video data by sharing link
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_by_share_url_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据分享链接获取单个作品数据
> ### 参数:
> - share_url: 分享链接
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data by sharing link
> ### Parameters:
> - share_url: Share link
> ### Return:
> - Video data
>
> # [示例/Example]
> share_url = "https://www.tiktok.com/t/ZTFNEj8Hk/"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_url | query | string | Yes | 分享链接/Share link | None | https://www.tiktok.com/t/ZTFNEj8Hk/ | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-one-video-by-share-url-v2"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2`

- Summary: 根据分享链接获取单个作品数据/Get single video data by sharing link
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_by_share_url_v2_api_v1_tiktok_app_v3_fetch_one_video_by_share_url_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 根据分享链接获取单个作品数据 V2，数据结构会有些不一样，会返回region字段。
> ### 参数:
> - share_url: 分享链接
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data by sharing link V2, the data structure will be a bit different, and the region field will be returned.
> ### Parameters:
> - share_url: Share link
> ### Return:
> - Video data
>
> # [示例/Example]
> share_url = "https://www.tiktok.com/t/ZTFNEj8Hk/"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_url | query | string | Yes | 分享链接/Share link | None | https://www.tiktok.com/t/ZTFNEj8Hk/ | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-one-video-v2"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v2`

- Summary: 获取单个作品数据 V2/Get single video data V2
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v2_api_v1_tiktok_app_v3_fetch_one_video_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品数据 V2
> ### 参数:
> - aweme_id: 作品id
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data V2
> ### Parameters:
> - aweme_id: Video id
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_id = "7350810998023949599"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id | None | 7350810998023949599 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-one-video-v3"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_one_video_v3`

- Summary: 获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter)
- Capabilities: content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_one_video_v3_api_v1_tiktok_app_v3_fetch_one_video_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个作品数据 V3
> ### 参数:
> - aweme_id: 作品id
> - region: 国家代码，默认US，支持ISO 3166-1 alpha-2国家代码，例如：US、GB、FR、DE、IN、JP等。
> - 备注：某些视频可能在特定国家/地区不可用，设置region参数可以尝试获取该国家/地区的视频数据。
> ### 返回:
> - 作品数据
>
> # [English]
> ### Purpose:
> - Get single video data V3
> ### Parameters:
> - aweme_id: Video id
> - region: Country code, default is US, supports ISO 3166-1 alpha-2 country codes, such as: US, GB, FR, DE, IN, JP, etc.
> - Note: Some videos may not be available in certain countries/regions, setting the region parameter can try to get the video data for that country/region.
> ### Return:
> - Video data
>
> # [示例/Example]
> aweme_id = "7350810998023949599"
> region = "US"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id | None | 7350810998023949599 | None |
| region | query | string | No | 国家代码/Country code | US | US | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-product-detail"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail`

- Summary: 获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead)
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_api_v1_tiktok_app_v3_fetch_product_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品详情数据
> - 即将弃用，使用 fetch_product_detail_v2 代替
> ### 参数:
> - product_id: 商品id，有时候需要从product_id_str字段中获取。
> ### 返回:
> - 商品详情数据
>
> # [English]
> ### Purpose:
> - Get product detail data
> - Will be deprecated, use fetch_product_detail_v2 instead
> ### Parameters:
> - product_id: Product id, sometimes need to get from the product_id_str field.
> ### Return:
> - Product detail data
>
> # [示例/Example]
> product_id = "1729385239712731370"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id/Product id | None | 1729385239712731370 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v2"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v2`

- Summary: 获取商品详情数据V2/Get product detail data V2
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v2_api_v1_tiktok_app_v3_fetch_product_detail_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品详情数据V2
> ### 参数:
> - product_id: 商品id，有时候需要从product_id_str字段中获取。
> ### 返回:
> - 商品详情数据V2
>
> # [English]
> ### Purpose:
> - Get product detail data V2
> ### Parameters:
> - product_id: Product id, sometimes need to get from the product_id_str field.
> ### Return:
> - Product detail data V2
>
> # [示例/Example]
> product_id = "1729385239712731370"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id/Product id | None | 1729385239712731370 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v3"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v3`

- Summary: 获取商品详情数据V3 / Get product detail data V3
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v3_api_v1_tiktok_app_v3_fetch_product_detail_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品详情数据V3。如果商品详情数据V2无法获取，可以尝试使用此接口。
>
> ### 参数:
> - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。
> - region: 商品的国家/地区代码，默认值为 "US"。
>
> ### 支持的国家/地区代码（按区域分组）：
> - 东南亚 Southeast Asia:
>   ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国）
> - 北美 North America:
>   US（美国）, MX（墨西哥）
> - 欧洲 Europe:
>   IE（爱尔兰）, GB（英国）, ES（西班牙）
> - 越南 Vietnam:
>   VN（越南）
>
> ### 返回:
> - 商品详情数据V3
>
> # [English]
> ### Purpose:
> - Get product detail data V3. If product detail data V2 cannot be retrieved, try this version.
>
> ### Parameters:
> - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be obtained from the product share link.
> - region: Country code of the product, default is "US".
>
> ### Supported region codes (grouped by area):
> - Southeast Asia:
>   ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand)
> - North America:
>   US (United States), MX (Mexico)
> - Europe:
>   IE (Ireland), GB (United Kingdom), ES (Spain)
> - Vietnam:
>   VN (Vietnam)
>
> ### Return:
> - Product detail data V3
>
> # [示例 / Example]
> product_id = "1729385239712731370"
> region = "US"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id / Product ID | None | 1729385239712731370 | None |
| region | query | string | No | 商品的国家/地区代码/ Country/region code of the product | US | US | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-product-detail-v4"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_product_detail_v4`

- Summary: 获取商品详情数据V4 / Get product detail data V4
- Capabilities: details / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_detail_v4_api_v1_tiktok_app_v3_fetch_product_detail_v4_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品详情数据V4。如果商品详情数据V3无法获取，可以尝试使用此接口。
>
> ### 参数:
> - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。
> - region: 商品的国家/地区代码，默认值为 "US"。
>
> ### 支持的国家/地区代码（按区域分组）：
> - 东南亚 Southeast Asia:
>   ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国）
> - 北美 North America:
>   US（美国）, MX（墨西哥）
> - 欧洲 Europe:
>   IE（爱尔兰）, GB（英国）, ES（西班牙）
> - 越南 Vietnam:
>   VN（越南）
>
> ### 返回:
> - 商品详情数据V4
>
> # [English]
> ### Purpose:
> - Get product detail data V4. If product detail data V3 cannot be retrieved, try this version.
>
> ### Parameters:
> - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be obtained from the product share link.
> - region: Country code of the product, default is "US".
>
> ### Supported region codes (grouped by area):
> - Southeast Asia:
>   ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand)
> - North America:
>   US (United States), MX (Mexico)
> - Europe:
>   IE (Ireland), GB (United Kingdom), ES (Spain)
> - Vietnam:
>   VN (Vietnam)
>
> ### Return:
> - Product detail data V4
>
> # [示例 / Example]
> seller_id = "8646929864612614278"
> product_id = "1729385239712731370"
> region = "US"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id / Product ID | None | 1729385239712731370 | None |
| region | query | string | No | 商品的国家/地区代码/ Country/region code of the product | US | US | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-product-id-by-share-link"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_product_id_by_share_link`

- Summary: 通过分享链接获取商品ID/Get Product ID by Share Link
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_id_by_share_link_api_v1_tiktok_app_v3_fetch_product_id_by_share_link_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接获取商品ID
> ### 参数:
> - share_link: 分享链接
> ### 返回:
> - 商品ID
>
> # [English]
> ### Purpose:
> - Get Product ID by Share Link
> ### Parameters:
> - share_link: Share link
> ### Return:
> - Product ID
>
> # [示例/Example]
> share_link = "https://www.tiktok.com/t/ZT2A9N1kw/"
> share_link2 = "https://affiliate-us.tiktok.com/api/v1/share/AJ4hS3OdXmSg"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_link | query | string | Yes | 分享链接/Share link | None | https://www.tiktok.com/t/ZT2A9N1kw/ | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-product-review"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_product_review`

- Summary: 获取商品评价数据/Get product review data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_review_api_v1_tiktok_app_v3_fetch_product_review_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品评价数据
> ### 参数:
> - product_id: 商品id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - size: 数量
> - filter_id: 筛选条件
>     - 0: 全部评价
>     - 1: 1星评价
>     - 2: 2星评价
>     - 3: 3星评价
>     - 4: 4星评价
>     - 5: 5星评价
>     - 102: 有图评价
>     - 104: 已购买的评价
> - sort_type: 排序条件
>     - 1: 相关度
>     - 2: 从新到旧
> ### 返回:
> - 商品评价数据
>
> # [English]
> ### Purpose:
> - Get product review data
> ### Parameters:
> - product_id: Product id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - size: Count number
> - filter_id: Filter condition
>     - 0: All reviews
>     - 1: 1-star review
>     - 2: 2-star review
>     - 3: 3-star review
>     - 4: 4-star review
>     - 5: 5-star review
>     - 102: Reviews with pictures
>     - 104: Reviews of purchased products
> - sort_type: Sorting conditions
>     - 1: Relevance
>     - 2: New to old
> ### Return:
> - Product review data
>
> # [示例/Example]
> product_id = "1729448812983194615"
> cursor = 0
> size = 10
> filter_id = 0
> sort_type = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | Yes | 商品id/Product id | None | 1729448812983194615 | None |
| cursor | query | integer | No | 游标/Cursor | 0 | None | None |
| size | query | integer | No | 数量/Number | 10 | None | None |
| filter_id | query | integer | No | 筛选条件/Filter condition | 0 | None | None |
| sort_type | query | integer | No | 排序条件/Sorting conditions | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-product-search"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_product_search`

- Summary: 获取商品搜索结果/Get product search results
- Capabilities: search / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_product_search_api_v1_tiktok_app_v3_fetch_product_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商品搜索结果
> ### 参数:
> - keyword: 关键词
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量
> - sort_type: 商品排序条件
>     - 1: 综合排序
>     - 2: 销量排序
>     - 3: 价格从高到低
>     - 4: 价格从低到高
>     - 5: 最新发布
> - customer_review_four_star: 四星以上评价
> - have_discount: 有优惠
> - min_price: 最低价格
> - max_price: 最高价格
> ### 返回:
> - 商品搜索结果
>
> # [English]
> ### Purpose:
> - Get product search results
> ### Parameters:
> - keyword: Keyword
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number
> - sort_type: Product sorting conditions
>     - 1: Comprehensive sorting
>     - 2: Sales volume sorting
>     - 3: Price high to low
>     - 4: Price low to high
>     - 5: Latest release
> - customer_review_four_star: Four-star or more reviews
> - have_discount: Having discount
> - min_price: Minimum price
> - max_price: Maximum price
> ### Return:
> - Product search results
>
> # [示例/Example]
> keyword = "Cat Toy"
> cursor = 0
> count = 12
> sort_type = 1
> customer_review_four_star = False
> have_discount = False
> min_price = "10"
> max_price = "25"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | Cat Toy | None |
| cursor | query | integer | No | 游标/Cursor | 0 | None | None |
| count | query | integer | No | 数量/Number | 12 | None | None |
| sort_type | query | integer | No | 商品排序条件/Product sorting conditions | 1 | None | None |
| customer_review_four_star | query | boolean | No | 四星以上评价/Four-star or more reviews | false | None | None |
| have_discount | query | boolean | No | 有优惠/Having discount | false | None | None |
| min_price | query | string | No | 最低价格/Minimum price | None | None | None |
| max_price | query | string | No | 最高价格/Maximum price | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-share-qr-code"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_share_qr_code`

- Summary: 获取分享二维码/Get share QR code
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_share_qr_code_api_v1_tiktok_app_v3_fetch_share_qr_code_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取分享二维码
> ### 参数:
> - object_id: 对象id，当前支持个人主页接口响应中的uid作为参数。
> ### 返回:
> - 二维码图片
>
> # [English]
> ### Purpose:
> - Get share QR code
> ### Parameters:
> - object_id: Object id, currently supports the uid in the response of the personal homepage interface as a parameter.
> ### Return:
> - QR code image
>
> # [示例/Example]
> url = "6762244951259661318"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| object_id | query | string | Yes | 对象id/Object id | None | 6762244951259661318 | None |
| schema_type | query | integer | No | 模式类型/Schema type | 4 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-share-short-link"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_share_short_link`

- Summary: 获取分享短链接/Get share short link
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_share_short_link_api_v1_tiktok_app_v3_fetch_share_short_link_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取分享短链接
> ### 参数:
> - url: 长链接或想要转换的链接
> ### 返回:
> - 短链接
>
> # [English]
> ### Purpose:
> - Get share short link
> ### Parameters:
> - url: Long link or link to convert
> ### Return:
> - Short link
>
> # [示例/Example]
> url = "https://www.tiktok.com/passport/web/logout/"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| url | query | string | Yes | 分享链接/Share link | None | https://www.tiktok.com/passport/web/logout/ | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-home"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home`

- Summary: 获取商家主页数据/Get shop home page data
- Capabilities: profiles / accounts / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_home_api_v1_tiktok_app_v3_fetch_shop_home_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商家主页的商品数据
> ### 参数:
> - page_id: 爬取的商家主页Page id，可以从`fetch_shop_home_page_list`这个接口获取
> - seller_id: 商家id,店铺id
> ### 返回:
> - 商家主页数据
>
> # [English]
> ### Purpose:
> - Get product data of the shop home page
> ### Parameters:
> - page_id: Page id of the crawled shop home page, which can be obtained from the interface `fetch_shop_home_page_list`
> - seller_id: Seller id, shop id
> ### Return:
> - Shop home page data
>
> # [示例/Example]
> page_id = "7314705727611930410"
> seller_id = "8646929864612614278"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| page_id | query | string | Yes | 爬取的商家主页Page id/Page id of the crawled shop home page | None | 7314705727611930410 | None |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id | None | 8646929864612614278 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-home-page-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_home_page_list`

- Summary: 获取商家主页Page列表数据/Get shop home page list data
- Capabilities: profiles / accounts / commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_home_page_list_api_v1_tiktok_app_v3_fetch_shop_home_page_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商家主页Page列表数据, 用于商家主页展示，以及爬取商家主页的商品数据
> ### 参数:
> - seller_id: 商家id,店铺id
> ### 返回:
> - 商家主页Page列表数据
>
> # [English]
> ### Purpose:
> - Get shop home page list data, used for shop home page display, and crawling shop home page product data
> ### Parameters:
> - seller_id: Seller id, shop id
> ### Return:
> - Shop home page list data
>
> # [示例/Example]
> seller_id = "8646929864612614278"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id | None | 8646929864612614278 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-id-by-share-link"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_id_by_share_link`

- Summary: 通过分享链接获取店铺ID/Get Shop ID by Share Link
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_id_by_share_link_api_v1_tiktok_app_v3_fetch_shop_id_by_share_link_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过分享链接获取店铺ID
> ### 参数:
> - share_link: 分享链接
> ### 返回:
> - 店铺ID
>
> # [English]
> ### Purpose:
> - Get Shop ID by Share Link
> ### Parameters:
> - share_link: Share link
> ### Return:
> - Shop ID
>
> # [示例/Example]
> share_link = "https://vt.tiktok.com/ZT2AHoGsE/"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| share_link | query | string | Yes | 分享链接/Share link | None | https://vt.tiktok.com/ZT2AHoGsE/ | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-info"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_info`

- Summary: 获取商家信息数据/Get shop information data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_info_api_v1_tiktok_app_v3_fetch_shop_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商家信息数据
> ### 参数:
> - shop_id: 商家id,店铺id
> ### 返回:
> - 商家信息数据
>
> # [English]
> ### Purpose:
> - Get shop information data
> ### Parameters:
> - shop_id: Seller id, shop id
> ### Return:
> - Shop information data
>
> # [示例/Example]
> shop_id = "8646942781241463007"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shop_id | query | string | Yes | 商家id,店铺id/Seller id, shop id | None | 8646942781241463007 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-product-category"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_category`

- Summary: 获取商家产品分类数据/Get shop product category data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_category_api_v1_tiktok_app_v3_fetch_shop_product_category_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商家产品分类数据
> ### 参数:
> - seller_id: 商家id,店铺id
> ### 返回:
> - 商家产品分类数据
>
> # [English]
> ### Purpose:
> - Get shop product category data
> ### Parameters:
> - seller_id: Seller id, shop id
> ### Return:
> - Shop product category data
>
> # [示例/Example]
> seller_id = "7495294980909468039"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id | None | 7495294980909468039 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list`

- Summary: 获取商家商品列表数据/Get shop product list data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_list_api_v1_tiktok_app_v3_fetch_shop_product_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商家商品列表数据
> ### 参数:
> - seller_id: 商家id,店铺id
> - scroll_params: 滚动参数，用于加载更多商品数据
> - page_size: 每页数量
> - sort_field: 排序字段
>     - 1: 综合排序
>     - 3: 最新发布
>     - 4: 销量最好
>     - 5: 价格排序
> - sort_order: 排序方式
>     - 0: 默认价格排序
>     - 1: 价格从高到低
>     - 2: 价格从低到高
> ### 返回:
> - 商家商品列表数据
>
> # [English]
> ### Purpose:
> - Get shop product list data
> ### Parameters:
> - seller_id: Seller id, shop id
> - scroll_params: Scroll parameter, used to load more product data
> - page_size: Number per page
> - sort_field: Sorting field
>     - 1: Comprehensive sorting
>     - 3: Latest release
>     - 4: Best sales
>     - 5: Price sorting
> - sort_order: Sorting method
>     - 0: Default price sorting
>     - 1: Price high to low
>     - 2: Price low to high
> ### Return:
> - Shop product list data
>
> # [示例/Example]
> seller_id = "8646929864612614278"
> scroll_params = ""
> page_size = 10
> sort_field = 1
> sort_order = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id | None | 8646929864612614278 | None |
| scroll_params | query | string | No | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data | None | None | None |
| page_size | query | integer | No | 每页数量/Number per page | 10 | None | None |
| sort_field | query | integer | No | 排序字段/Sorting field | 1 | None | None |
| sort_order | query | integer | No | 排序方式/Sorting method | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-product-list-v2"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_list_v2`

- Summary: 获取商家商品列表数据 V2/Get shop product list data V2
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_list_v2_api_v1_tiktok_app_v3_fetch_shop_product_list_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商家商品列表数据
> ### 参数:
> - seller_id: 商家id,店铺id
> - scroll_params: 滚动参数，用于加载更多商品数据
> - page_size: 每页数量
> - sort_field: 排序字段
>     - 1: 综合排序
>     - 3: 最新发布
>     - 4: 销量最好
>     - 5: 价格排序
> - sort_order: 排序方式
>     - 0: 默认价格排序
>     - 1: 价格从高到低
>     - 2: 价格从低到高
> ### 返回:
> - 商家商品列表数据
>
> # [English]
> ### Purpose:
> - Get shop product list data
> ### Parameters:
> - seller_id: Seller id, shop id
> - scroll_params: Scroll parameter, used to load more product data
> - page_size: Number per page
> - sort_field: Sorting field
>     - 1: Comprehensive sorting
>     - 3: Latest release
>     - 4: Best sales
>     - 5: Price sorting
> - sort_order: Sorting method
>     - 0: Default price sorting
>     - 1: Price high to low
>     - 2: Price low to high
> ### Return:
> - Shop product list data
>
> # [示例/Example]
> seller_id = "8646929864612614278"
> scroll_params = ""
> page_size = 10
> sort_field = 1
> sort_order = 0

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id | None | 8646929864612614278 | None |
| scroll_params | query | string | No | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data | None | None | None |
| page_size | query | integer | No | 每页数量/Number per page | 10 | None | None |
| sort_field | query | integer | No | 排序字段/Sorting field | 1 | None | None |
| sort_order | query | integer | No | 排序方式/Sorting method | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-shop-product-recommend"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_shop_product_recommend`

- Summary: 获取商家商品推荐数据/Get shop product recommend data
- Capabilities: commerce
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_shop_product_recommend_api_v1_tiktok_app_v3_fetch_shop_product_recommend_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取商家商品推荐数据
> ### 参数:
> - seller_id: 商家id,店铺id
> - scroll_param: 滚动参数，用于加载更多商品数据
> - page_size: 每页数量
> ### 返回:
> - 商家商品推荐数据
>
> # [English]
> ### Purpose:
> - Get shop product recommend data
> ### Parameters:
> - seller_id: Seller id, shop id
> - scroll_param: Scroll parameter, used to load more product data
> - page_size: Number per page
> ### Return:
> - Shop product recommend data
>
> # [示例/Example]
> seller_id = "8646929864612614278"
> scroll_param = ""
> page_size = 10

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| seller_id | query | string | Yes | 商家id,店铺id/Seller id, shop id | None | 8646929864612614278 | None |
| scroll_param | query | string | No | 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more product data | None | None | None |
| page_size | query | integer | No | 每页数量/Number per page | 10 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-similar-user-recommendations"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_similar_user_recommendations`

- Summary: 获取类似用户推荐/Similar User Recommendations
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_similar_user_recommendations_api_v1_tiktok_app_v3_fetch_similar_user_recommendations_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取类似用户推荐
> ### 参数:
> - sec_uid: 用户sec_uid
> - page_token: 分页标记，第一次请求时不需要传递，后续请求时传递上一次响应中的next_page_token值。
> ### 返回:
> - 类似用户推荐
>
> # [English]
> ### Purpose:
> - Similar User Recommendations
> ### Parameters:
> - sec_uid: User sec_uid
> - page_token: Page token, not required for the first request, for subsequent requests, pass the next_page_token value from the previous response.
> ### Return:
> - Similar User Recommendations
>
> # [示例/Example]
> sec_uid = "MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b"
> page_token = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_uid/User sec_uid | None | MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b | None |
| page_token | query | string | No | 分页标记/Page token | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-country-by-username"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_country_by_username`

- Summary: 通过用户名获取用户账号国家地区/Get user account country by username
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_country_by_username_api_v1_tiktok_app_v3_fetch_user_country_by_username_get`

#### Notes

> # [中文]
> ### 用途:
> - 通过用户名获取用户账号国家地区
> ### 参数:
> - username: 用户名，可以从用户主页链接中获取，例如：https://www.tiktok.com/@tiktok，用户名即为tiktok。
> ### 返回:
> - 用户账号国家地区
>
> # [English]
> ### Purpose:
> - Get user account country by username
> ### Parameters:
> - username: Username, which can be obtained from the user's homepage link, for example: https://www.tiktok.com/@tiktok, the username is tiktok.
> ### Return:
> - User account country
>
> # [示例/Example]
> username = "tiktok"
>
> # 响应示例/Response Example
> ```json
> {'username': 'tiktok', 'username_modify_time': 1760985494, 'user_id': '107955', 'sec_user_id': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM', 'country': 'US', 'api_version': 'v1'}
> ```

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | tiktok | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-follower-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_follower_list`

- Summary: 获取指定用户的粉丝列表数据/Get follower list of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_follower_list_api_v1_tiktok_app_v3_fetch_user_follower_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的粉丝列表数据
> ### 参数:
> - user_id: 用户ID，这是一个纯数字版本的用户ID (与sec_user_id二选一/One of user_id and sec_user_id)
> - sec_user_id: 用户sec_user_id，这是一个混合字母和数字的版本ID (与user_id二选一/One of user_id and sec_user_id)
> - count: 数量，不要超过20，保持固定。
> - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。
> - page_token: 翻页token，第一次请求使用默认值""，后续请求使用上一次请求返回的page_token值。
> ### 返回:
> - 粉丝列表数据
>
> # [English]
> ### Purpose:
> - Get follower list of specified user
> ### Parameters:
> - user_id: User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id)
> - sec_user_id: User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id)
> - count: Number, do not exceed 20, keep it fixed.
> - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests.
> - page_token: Page token, use default value "" for the first request, and use the page_token value returned by the last request for subsequent requests.
> ### Return:
> - Follower list data
>
> # [示例/Example]
> user_id = "7486586574684881927"
> sec_user_id = "MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP"
> count = 20
> min_time = 0
> page_token = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id) | None | 7486586574684881927 | None |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id) | None | MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP | None |
| count | query | integer | No | 数量/Number | 20 | 20 | None |
| min_time | query | integer | No | 最小时间，用于翻页/Minimum time for paging | 0 | 0 | None |
| page_token | query | string | No | 翻页token/Page token | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-following-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_following_list`

- Summary: 获取指定用户的关注列表数据/Get following list of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_following_list_api_v1_tiktok_app_v3_fetch_user_following_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的关注列表数据
> ### 参数:
> - user_id: 用户ID，这是一个纯数字版本的用户ID (与sec_user_id二选一/One of user_id and sec_user_id)
> - sec_user_id: 用户sec_user_id，这是一个混合字母和数字的版本ID (与user_id二选一/One of user_id and sec_user_id)
> - count: 数量，不要超过20，保持固定。
> - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。
> - page_token: 翻页token，第一次请求使用默认值""，后续请求使用上一次请求返回的page_token值。
> ### 返回:
> - 关注列表数据
>
> # [English]
> ### Purpose:
> - Get following list of specified user
> ### Parameters:
> - user_id: User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id)
> - sec_user_id: User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id)
> - count: Number, do not exceed 20, keep it fixed.
> - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests.
> - page_token: Page token, use default value "" for the first request, and use the page_token value returned by the last request for subsequent requests.
> ### Return:
> - Following list data
>
> # [示例/Example]
> user_id = "7486586574684881927"
> sec_user_id = "MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP"
> count = 20
> min_time = 0
> page_token = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户ID/User ID (与sec_user_id二选一/One of user_id and sec_user_id) | None | 7486586574684881927 | None |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id (与user_id二选一/One of user_id and sec_user_id) | None | MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP | None |
| count | query | integer | No | 数量/Number | 20 | 20 | None |
| min_time | query | integer | No | 最小时间，用于翻页/Minimum time for paging | 0 | 0 | None |
| page_token | query | string | No | 翻页token/Page token | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-like-videos"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_like_videos`

- Summary: 获取用户喜欢作品数据/Get user like video data
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_like_videos_api_v1_tiktok_app_v3_fetch_user_like_videos_get`

#### Notes

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
> sec_user_id = "MS4wLjABAAAA-RkTGCGXLuLKRM5Xcuuwm7Mclg51I2ECO1RqOA7mJHuXFz99nztdi077Z2XmYHZV"
> max_cursor = 0
> counts = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | Yes | 用户sec_user_id/User sec_user_id | None | MS4wLjABAAAA-RkTGCGXLuLKRM5Xcuuwm7Mclg51I2ECO1RqOA7mJHuXFz99nztdi077Z2XmYHZV | None |
| max_cursor | query | integer | No | 最大游标/Maximum cursor | 0 | None | None |
| counts | query | integer | No | 每页数量/Number per page | 20 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-music-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_music_list`

- Summary: 获取用户音乐列表数据/Get user music list data
- Capabilities: profiles / accounts / music / audio
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_music_list_api_v1_tiktok_app_v3_fetch_user_music_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户音乐列表数据
> ### 参数:
> - sec_uid: 用户sec_uid
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量
> ### 返回:
> - 用户音乐列表数据
>
> # [English]
> ### Purpose:
> - Get user music list data
> ### Parameters:
> - sec_uid: User sec_uid
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number
>
> # [示例/Example]
> sec_uid = "MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6"
> cursor = 0
> count = 10

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_uid | query | string | Yes | 用户sec_uid/User sec_uid | None | MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6 | None |
| cursor | query | integer | No | 游标/Cursor | 0 | None | None |
| count | query | integer | No | 数量/Number | 10 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos`

- Summary: 获取用户主页作品数据 V1/Get user homepage video data V1
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户主页作品数据
> ### 参数:
> - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。
> - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
> - count: 最大数量，建议保持默认值20。
> - sort_type: 排序类型，0-最新，1-热门
> - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。
> - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user homepage video data
> ### Parameters:
> - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data.
> - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.
> - count: Maximum count number
> - sort_type: Sort type, 0-Latest, 1-Hot
> - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username.
> - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data.
> ### Return:
> - User video data
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS"
> max_cursor = 0
> counts = 20
> sort_type = 0
> unique_id = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| unique_id | query | string | No | 用户unique_id/User unique_id | None | None | None |
| max_cursor | query | integer | No | 最大游标/Maximum cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| sort_type | query | integer | No | 排序类型/Sort type | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v2"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v2`

- Summary: 获取用户主页作品数据 V2/Get user homepage video data V2
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_videos_api_v1_tiktok_app_v3_fetch_user_post_videos_v2_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户主页作品数据
> ### 参数:
> - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。
> - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
> - count: 最大数量，建议保持默认值20。
> - sort_type: 排序类型，0-最新，1-热门
> - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。
> - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user homepage video data
> ### Parameters:
> - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data.
> - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.
> - count: Maximum count number
> - sort_type: Sort type, 0-Latest, 1-Hot
> - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username.
> - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data.
> ### Return:
> - User video data
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS"
> max_cursor = 0
> counts = 20
> sort_type = 0
> unique_id = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| unique_id | query | string | No | 用户unique_id/User unique_id | None | None | None |
| max_cursor | query | integer | No | 最大游标/Maximum cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| sort_type | query | integer | No | 排序类型/Sort type | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-post-videos-v3"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_post_videos_v3`

- Summary: 获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster)
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_post_videos_v3_api_v1_tiktok_app_v3_fetch_user_post_videos_v3_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户主页作品数据
> ### 参数:
> - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。
> - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
> - count: 最大数量，建议保持默认值20。
> - sort_type: 排序类型，0-最新，1-热门
> - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。
> - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。
> ### 返回:
> - 用户作品数据
>
> # [English]
> ### Purpose:
> - Get user homepage video data
> ### Parameters:
> - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is empty, use unique_id to get user video data.
> - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the max_cursor value in the first response.
> - count: Maximum count number
> - sort_type: Sort type, 0-Latest, 1-Hot
> - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user video data, unique_id is also the user's username.
> - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority, the faster the speed, and it is recommended to use only sec_user_id to get user data.
> ### Return:
> - User video data
>
> # [示例/Example]
> sec_user_id = "MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS"
> max_cursor = 0
> counts = 20
> sort_type = 0
> unique_id = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| unique_id | query | string | No | 用户unique_id/User unique_id | None | None | None |
| max_cursor | query | integer | No | 最大游标/Maximum cursor | 0 | None | None |
| count | query | integer | No | 每页数量/Number per page | 20 | None | None |
| sort_type | query | integer | No | 排序类型/Sort type | 0 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-repost-videos"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_repost_videos`

- Summary: 获取用户转发的作品数据/Get user repost video data
- Capabilities: profiles / accounts / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_repost_videos_api_v1_tiktok_app_v3_fetch_user_repost_videos_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取用户转发的作品数据
> ### 参数:
> - user_id: 用户id，可以通过 handler_user_profile 端点获取，响应中的关键字为uid。
> - offset: 偏移量
> - count: 数量
> ### 返回:
> - 用户转发作品数据
>
> # [English]
> ### Purpose:
> - Get user repost video data
> ### Parameters:
> - user_id: User id, which can be obtained through the handler_user_profile endpoint, with the keyword uid in the response.
> - offset: Offset
> - count: Number
> ### Return:
> - User repost video data
>
> # [示例/Example]
> user_id = 107955
> offset = 0
> count = 21

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | integer | Yes | 用户id/User id | None | 107955 | None |
| offset | query | integer | No | 偏移量/Offset | 0 | None | None |
| count | query | integer | No | 数量/Number | 21 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-user-search-result"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_user_search_result`

- Summary: 获取指定关键词的用户搜索结果/Get user search results of specified keywords
- Capabilities: search / profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_user_search_result_api_v1_tiktok_app_v3_fetch_user_search_result_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定关键词的用户搜索结果
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> - user_search_follower_count（根据粉丝数排序）:
>     - 空-不限制，
>     - ZERO_TO_ONE_K = 0-1K，
>     - ONE_K_TO_TEN_K-1K = 1K-10K，
>     - TEN_K_TO_ONE_H_K = 10K-100K，
>     - ONE_H_K_PLUS = 100K以上
> - user_search_profile_type（根据账号类型排序）:
>     - 空-不限制，
>     - VERIFIED = 认证用户
> - user_search_other_pref（根据其他偏好排序）:
>     - USERNAME = 根据用户名相关性
> ### 返回:
> - 用户搜索结果
>
> # [English]
> ### Purpose:
> - Get user search results of specified keywords
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> - user_search_follower_count（Sort by number of followers）:
>     - Empty-Unlimited,
>     - ZERO_TO_ONE_K = 0-1K,
>     - ONE_K_TO_TEN_K-1K = 1K-10K,
>     - TEN_K_TO_ONE_H_K = 10K-100K,
>     - ONE_H_K_PLUS = 100K and above
> - user_search_profile_type（Sort by account type）:
>     - Empty-Unlimited,
>     - VERIFIED = Verified user
> - user_search_other_pref（Sort by other preferences）:
>     - USERNAME = Sort by username relevance
> ### Return:
> - User search results
>
> # [示例/Example]
> keyword = "Cat"
> offset = 0
> count = 20
> user_search_follower_count = ""
> user_search_profile_type = ""
> user_search_other_pref = ""

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | Cat | None |
| offset | query | integer | No | 偏移量/Offset | 0 | 0 | None |
| count | query | integer | No | 数量/Number | 20 | 20 | None |
| user_search_follower_count | query | string | No | 根据粉丝数排序/Sort by number of followers | None | None | None |
| user_search_profile_type | query | string | No | 根据账号类型排序/Sort by account type | None | None | None |
| user_search_other_pref | query | string | No | 根据其他偏好排序/Sort by other preferences | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-video-comment-replies"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comment_replies`

- Summary: 获取指定视频的评论回复数据/Get comment replies data of specified video
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comments_reply_api_v1_tiktok_app_v3_fetch_video_comment_replies_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定视频的评论回复数据
> ### 参数:
> - item_id: 作品id
> - comment_id: 评论id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
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
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number
> ### Return:
> - Comment replies data
>
> # [示例/Example]
> aweme_id = "7326156045968067873"
> comment_id = "7327061675382260482"
> cursor = 0
> count = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| item_id | query | string | Yes | 作品id/Video id | None | 7326156045968067873 | None |
| comment_id | query | string | Yes | 评论id/Comment id | None | 7327061675382260482 | None |
| cursor | query | integer | No | 游标/Cursor | 0 | None | None |
| count | query | integer | No | 数量/Number | 20 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-video-comments"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_video_comments`

- Summary: 获取单个视频评论数据/Get single video comments data
- Capabilities: comments / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_comments_api_v1_tiktok_app_v3_fetch_video_comments_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取单个视频评论数据
> ### 参数:
> - aweme_id: 作品id
> - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
> - count: 数量
> ### 返回:
> - 评论数据
>
> # [English]
> ### Purpose:
> - Get single video comments data
> ### Parameters:
> - aweme_id: Video id
> - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.
> - count: Number
> ### Return:
> - Comments data
>
> # [示例/Example]
> aweme_id = "7326156045968067873"
> cursor = 0
> count = 20

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id | None | 7326156045968067873 | None |
| cursor | query | integer | No | 游标/Cursor | 0 | None | None |
| count | query | integer | No | 数量/Number | 20 | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-video-search-result"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_video_search_result`

- Summary: 获取指定关键词的视频搜索结果/Get video search results of specified keywords
- Capabilities: search / content details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_video_search_result_api_v1_tiktok_app_v3_fetch_video_search_result_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定关键词的视频搜索结果
> ### 参数:
> - keyword: 关键词
> - offset: 偏移量
> - count: 数量
> - sort_type: 0-相关度，1-最多点赞
> - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年
> - region: 地区，默认为US-美国，可选值请参考TikTok地区代码或ISO 3166-1 alpha-2国家代码。
> ### 返回:
> - 视频搜索结果
>
> # [English]
> ### Purpose:
> - Get video search results of specified keywords
> ### Parameters:
> - keyword: Keyword
> - offset: Offset
> - count: Number
> - sort_type: 0-Relatedness, 1-Most likes
> - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last half year
> - region: Region, default is US-America, for optional values please refer to TikTok region codes or ISO 3166-1 alpha-2 country codes.
> ### Return:
> - Video search results
>
> # [示例/Example]
> keyword = "中华娘"
> offset = 0
> count = 20
> sort_type = 0
> publish_time = 0
> region = "US"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | 中华娘 | None |
| offset | query | integer | No | 偏移量/Offset | 0 | 0 | None |
| count | query | integer | No | 数量/Number | 20 | 20 | None |
| sort_type | query | integer | No | 排序类型/Sort type | 0 | 0 | None |
| publish_time | query | integer | No | 发布时间/Publish time | 0 | 0 | None |
| region | query | string | No | 地区/Region | US | US | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-fetch-webcast-user-info"></a>
### `GET /api/u1/v1/tiktok/app/v3/fetch_webcast_user_info`

- Summary: 获取指定 Webcast 用户的信息/Get information of specified Webcast user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `fetch_webcast_user_info_api_v1_tiktok_app_v3_fetch_webcast_user_info_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的信息
> ### 参数:
> - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户信息。
> - user_id: 用户uid，可选参数，纯数字，如果使用请保持sec_user_id以及unique_id为空。
> - 以上参数必须至少填写一个，优先级为sec_user_id > user_id，优先级越高速度越快。
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get information of specified user
> ### Parameters:
> - sec_user_id: User sec_user_id
> - user_id: User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty.
> - At least one of the above parameters must be filled in, the priority is sec_user_id > user_id, the higher the priority, the faster the speed.
> ### Return:
> - User information
>
> # [示例/Example]
> user_id = "107955"
> sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户uid （可选，纯数字）/User uid (optional, pure number) | None | None | None |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-get-user-id-and-sec-user-id-by-username"></a>
### `GET /api/u1/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username`

- Summary: 使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_user_id_and_sec_user_id_by_username_api_v1_tiktok_app_v3_get_user_id_and_sec_user_id_by_username_get`

#### Notes

> # [中文]
> ### 用途:
> - 使用用户名获取用户 user_id 和 sec_user_id
> ### 参数:
> - username: 用户名
> ### 返回:
> - 用户 user_id 和 sec_user_id
>
> # [English]
> ### Purpose:
> - Get user_id and sec_user_id by Username
> ### Parameters:
> - username: Username
> ### Return:
> - User user_id and sec_user_id
>
> # [示例/Example]
> username = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| username | query | string | Yes | 用户名/Username | None | tiktok | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-handler-user-profile"></a>
### `GET /api/u1/v1/tiktok/app/v3/handler_user_profile`

- Summary: 获取指定用户的信息/Get information of specified user
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `handler_user_profile_api_v1_tiktok_app_v3_handler_user_profile_get`

#### Notes

> # [中文]
> ### 用途:
> - 获取指定用户的信息
> ### 参数:
> - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户信息。
> - user_id: 用户uid，可选参数，纯数字，如果使用请保持sec_user_id以及unique_id为空。
> - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户信息，unique_id也是用户的用户名，如果使用请保持sec_user_id以及user_id为空。
> - 以上参数必须至少填写一个，优先级为sec_user_id > user_id > unique_id，优先级越高速度越快。
> ### 返回:
> - 用户信息
>
> # [English]
> ### Purpose:
> - Get information of specified user
> ### Parameters:
> - sec_user_id: User sec_user_id
> - user_id: User uid, optional parameter, pure number, if used, please keep sec_user_id and unique_id empty.
> - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user information, unique_id is also the user's username, if used, please keep sec_user_id and user_id empty.
> - At least one of the above parameters must be filled in, the priority is sec_user_id > user_id > unique_id, the higher the priority, the faster the speed.
> ### Return:
> - User information
>
> # [示例/Example]
> user_id = "107955"
> sec_user_id = "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
> unique_id = "tiktok"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | No | 用户uid （可选，纯数字）/User uid (optional, pure number) | None | None | None |
| sec_user_id | query | string | No | 用户sec_user_id/User sec_user_id | None | MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM | None |
| unique_id | query | string | No | 用户unique_id （用户名）/User unique_id (username) | None | None | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-keyword-search"></a>
### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search`

- Summary: 生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_keyword_search_api_v1_tiktok_app_v3_open_tiktok_app_to_keyword_search_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果。
>
> ### 参数:
> - keyword: 关键词
> - 注意: 如果未能跳转，请确保APP已经在后台运行。
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result
>
> ### Parameters:
> - keyword: Keyword
> - Note: If you cannot jump, please make sure that the APP is running in the background
>
> ### Return:
> - Share link
>
> # [示例/Example]
> keyword = "Evil0ctal"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | Yes | 关键词/Keyword | None | Evil0ctal | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-send-private-message"></a>
### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message`

- Summary: 生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_send_private_message_api_v1_tiktok_app_v3_open_tiktok_app_to_send_private_message_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信。
>
> ### 参数:
> - uid: 用户id，从用户主页接口中获取。
> - 注意: 如果未能跳转，请确保APP已经在后台运行。
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate TikTok share link, call TikTok APP, and send private messages to specified users
>
> ### Parameters:
> - uid: User id, obtained from the user profile interface.
> - Note: If you cannot jump, please make sure that the APP is running in the background.
>
> ### Return:
> - Share link
>
> # [示例/Example]
> uid = "7059867056504407087"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id | None | 7059867056504407087 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-user-profile"></a>
### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_user_profile`

- Summary: 生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile
- Capabilities: profiles / accounts
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_user_profile_api_v1_tiktok_app_v3_open_tiktok_app_to_user_profile_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页。
>
> ### 参数:
> - uid: 用户id，从用户主页接口中获取。
> - 注意: 如果未能跳转，请确保APP已经在后台运行。
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate TikTok share link, call TikTok APP, and jump to the specified user profile
>
> ### Parameters:
> - uid: User id, obtained from the user profile interface.
> - Note: If you cannot jump, please make sure that the APP is running in the background.
>
> ### Return:
> - Share link
>
> # [示例/Example]
> uid = "7059867056504407087"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| uid | query | string | Yes | 用户id/User id | None | 7059867056504407087 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-open-tiktok-app-to-video-detail"></a>
### `GET /api/u1/v1/tiktok/app/v3/open_tiktok_app_to_video_detail`

- Summary: 生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page
- Capabilities: content details / details
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `open_tiktok_app_to_video_detail_api_v1_tiktok_app_v3_open_tiktok_app_to_video_detail_get`

#### Notes

> # [中文]
> ### 用途:
> - 生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页。
>
> ### 参数:
> - aweme_id: 作品id
> - 注意: 如果未能跳转，请确保APP已经在后台运行。
>
> ### 返回:
> - 分享链接
>
> # [English]
> ### Purpose:
> - Generate TikTok share link, call TikTok APP, and jump to the specified video
>
> ### Parameters:
> - aweme_id: Video id
> - Note: If you cannot jump, please make sure that the APP is running in the background
>
> ### Return:
> - Share link
>
> # [示例/Example]
> aweme_id = "7440436579409153311"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aweme_id | query | string | Yes | 作品id/Video id | None | 7440436579409153311 | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-search-follower-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/search_follower_list`

- Summary: 搜索粉丝列表/Search follower list
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_follower_list_api_v1_tiktok_app_v3_search_follower_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索指定用户的粉丝列表，可以用于查找某个用户的粉丝中是否有特定昵称的用户。
> ### 参数:
> - user_id: 用户ID，这是一个纯数字版本的用户ID，可以先通过获取用户信息接口获取。
> - keyword: 搜索关键词，用户的昵称中包含该关键词即可匹配
> ### 返回:
> - 搜索结果列表
>
> # [English]
> ### Purpose:
> - Search follower list of specified user, can be used to find whether there is a user with a specific nickname in the followers of a certain user.
> ### Parameters:
> - user_id: User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API.
> - keyword: Search keyword, the user's nickname contains the keyword to match.
> ### Return:
> - Search result list
>
> # [示例/Example]
> user_id = "7540849481009988663"
> keyword = "a"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 7540849481009988663 | None |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | a | None |

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

<a id="get-api-u1-v1-tiktok-app-v3-search-following-list"></a>
### `GET /api/u1/v1/tiktok/app/v3/search_following_list`

- Summary: 搜索关注列表/Search following list
- Capabilities: search
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `search_following_list_api_v1_tiktok_app_v3_search_following_list_get`

#### Notes

> # [中文]
> ### 用途:
> - 搜索指定用户的关注列表，可以用于查找某个用户的关注中是否有特定昵称的用户。
> ### 参数:
> - user_id: 用户ID，这是一个纯数字版本的用户ID，可以先通过获取用户信息接口获取。
> - keyword: 搜索关键词，用户的昵称中包含该关键词即可匹配。
> ### 返回:
> - 搜索结果列表
>
> # [English]
> ### Purpose:
> - Search following list of specified user, can be used to find whether there is a user with a specific nickname in the following of a certain user.
> ### Parameters:
> - user_id: User ID, this is a pure numeric version of the user ID, which can be obtained through the get user info API.
> - keyword: Search keyword, the user's nickname contains the keyword to match.
> ### Return:
> - Search result list
>
> # [示例/Example]
> user_id = "7540849481009988663"
> keyword = "a"

#### Parameters

| Field | In | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| user_id | query | string | Yes | 用户ID/User ID | None | 7540849481009988663 | None |
| keyword | query | string | Yes | 搜索关键词/Search keyword | None | a | None |

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
