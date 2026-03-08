# TikTok-Shop-Web-API 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/tiktok-shop-web-api.md`](../api-tags/tiktok-shop-web-api.md)
- 当前契约文件：`api-contracts/tiktok-shop-web-api.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`15`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(TikTok电商网页版数据接口/TikTok-Shop-Web-API data endpoints)**

## 路由契约

<a id="get-api-u1-v1-tiktok-shop-web-fetch-hot-selling-products-list"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_hot_selling_products_list`

- 摘要：获取热卖商品列表/Get hot selling products list
- 能力：热点/榜单 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_hot_selling_products_list_api_v1_tiktok_shop_web_fetch_hot_selling_products_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok Shop的热卖商品列表
> - 返回当前最受欢迎的商品
> ### 参数:
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> - count: 返回商品数量，默认100 (可选)
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // 热卖商品列表(最多1000个)
>             {
>                 "product_id": "xxx",
>                 "title": "商品标题",
>                 "image": "商品图片",
>                 "price": {},              // 价格信息
>                 "rating": {},             // 评分信息
>                 "sales": {},              // 销量信息
>                 "rank": 1                 // 热卖排名
>             }
>         ]
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get TikTok Shop hot selling products list
> - Returns currently most popular products
> ### Parameters:
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> - count: Number of products to return, default 100 (optional)
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // Hot selling products (up to 1000)
>             {
>                 "product_id": "xxx",
>                 "title": "Product title",
>                 "image": "Product image",
>                 "price": {},              // Price info
>                 "rating": {},             // Rating info
>                 "sales": {},              // Sales info
>                 "rank": 1                 // Hot selling rank
>             }
>         ]
>     }
> }
> ```
>
> # [示例/Example]
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |
| count | query | integer | 否 | 返回商品数量/Number of products to return | 100 | 100 | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-product-detail"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail`

- 摘要：获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data)
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_api_v1_tiktok_shop_web_fetch_product_detail_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok Shop商品的详细信息
> - 包含商品基本信息、价格、库存、评价、推荐商品等完整数据
> - 某些特殊地区的商品可能无法获取到数据（如：泰国），如果遇到此情况请尝试使用 `fetch_product_detail_v3` 接口
> ### 参数:
> - seller_id: 卖家ID (可传空字符串)
> - product_id: 商品ID (必填)
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "global_fe_config": {},      // 全局前端配置
>         "components_map": [],         // 组件映射列表
>         "global_data": {              // 全局数据
>             "product_info": {},       // 商品信息
>             "seller_info": {},        // 卖家信息
>             "shipping_info": {},      // 物流信息
>             "review_info": {}         // 评价信息
>         }
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get detailed information of TikTok Shop products
> - Contains complete data including basic info, price, stock, reviews, recommendations
> - Some products from specific regions may not be accessible (e.g., Thailand); if so, try using `fetch_product_detail_v3`
> ### Parameters:
> - seller_id: Seller ID (can be empty string)
> - product_id: Product ID (required)
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "global_fe_config": {},      // Global frontend config
>         "components_map": [],         // Component mapping list
>         "global_data": {              // Global data
>             "product_info": {},       // Product information
>             "seller_info": {},        // Seller information
>             "shipping_info": {},      // Shipping information
>             "review_info": {}         // Review information
>         }
>     }
> }
> ```
>
> # [示例/Example]
> seller_id = "7494629757824764402"
> product_id = "1729556436942358002"
> region = "MY"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 1729556436942358002 | 无 |
| seller_id | query | string | 否 | 卖家ID(可选)/Seller ID (optional) | 无 | 7494629757824764402 | 无 |
| region | query | string | 否 | 地区代码/Region code | MY | MY | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v2"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v2`

- 摘要：获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data)
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_v2_api_v1_tiktok_shop_web_fetch_product_detail_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok Shop商品详情(移动端接口)
> - 数据结构更精简，响应速度更快
> - 此接口返回的数据更少，如果需要更完整的数据请使用 `fetch_product_detail` 或 `fetch_product_detail_v3` 接口
> ### 参数:
> - seller_id: 卖家ID (可传空字符串)
> - product_id: 商品ID (必填)
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "productDetailSchema": {},    // 商品详细信息
>         "productCategoryInfoSchema": {}, // 分类信息
>         "pdpRelatedKwSchema": [],     // 相关关键词
>         "productsForComponentListSchema": [] // 推荐商品组件
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get TikTok Shop product details (Mobile API)
> - More streamlined data structure with faster response
> - This API returns less data; for more complete data, use `fetch_product_detail` or `fetch_product_detail_v3`
> ### Parameters:
> - seller_id: Seller ID (can be empty string)
> - product_id: Product ID (required)
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "productDetailSchema": {},    // Product details
>         "productCategoryInfoSchema": {}, // Category info
>         "pdpRelatedKwSchema": [],     // Related keywords
>         "productsForComponentListSchema": [] // Recommended product components
>     }
> }
> ```
>
> # [示例/Example]
> seller_id = "7494629757824764402"
> product_id = "1729556436942358002"
> region = "MY"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 1729556436942358002 | 无 |
| seller_id | query | string | 否 | 卖家ID(可选)/Seller ID (optional) | 无 | 7494629757824764402 | 无 |
| region | query | string | 否 | 地区代码/Region code | MY | MY | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-product-detail-v3"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_product_detail_v3`

- 摘要：获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data)
- 能力：详情 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_detail_v3_api_v1_tiktok_shop_web_fetch_product_detail_v3_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok Shop商品详情
> - 提供最完整的商品信息，包括推荐商品、相关视频、店铺信息等
> - 适用于所有地区的商品
> ### 参数:
> - product_id: 商品ID (必填)
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - **请务必确保 `product_id` 对应的 `region` 是正确的，否则接口将不会返回数据。**
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 200,
>     "data": {
>         "productInfo": {},                           // 商品详细信息
>         "frequentlyBoughtTogether": [],              // 经常一起购买的商品
>         "similarProductsInCategory": [],             // 同类别相似商品
>         "exploreMoreFromShop": [],                   // 店铺更多商品
>         "brandInCategoryRecommendedProducts": [],    // 品牌分类推荐商品
>         "customersAlsoBought": [],                   // 顾客还购买了
>         "moreInThisColorStyle": [],                  // 更多颜色款式
>         "relatedVideos": [],                         // 相关视频
>         "shopPerformance": {},                       // 店铺表现
>         "categoryInfo": {},                          // 分类信息
>         "searchRecommendWords": [],                  // 搜索推荐词
>         "randomSearchWord": "",                      // 随机搜索词
>         "shopInfo": {},                              // 店铺信息
>         "shopHotReviews": []                         // 店铺热门评论
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get TikTok Shop product details
> - Provides the most complete product information including recommendations, videos, shop info, etc.
> - Suitable for products from all regions
> ### Parameters:
> - product_id: Product ID (required)
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - **Please ensure that the `region` matches the actual region of the `product_id`, otherwise the API will not return any data.**
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 200,
>     "data": {
>         "productInfo": {},                           // Product details
>         "frequentlyBoughtTogether": [],              // Frequently bought together
>         "similarProductsInCategory": [],             // Similar products in category
>         "exploreMoreFromShop": [],                   // More from shop
>         "brandInCategoryRecommendedProducts": [],    // Brand category recommendations
>         "customersAlsoBought": [],                   // Customers also bought
>         "moreInThisColorStyle": [],                  // More colors/styles
>         "relatedVideos": [],                         // Related videos
>         "shopPerformance": {},                       // Shop performance
>         "categoryInfo": {},                          // Category info
>         "searchRecommendWords": [],                  // Search recommendation words
>         "randomSearchWord": "",                      // Random search word
>         "shopInfo": {},                              // Shop information
>         "shopHotReviews": []                         // Shop hot reviews
>     }
> }
> ```
>
> # [示例/Example]
> product_id = "1732108663255959373"
> region = "SG"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 1732108663255959373 | 无 |
| region | query | string | 否 | 地区代码/Region code | SG | SG | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v1"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v1`

- 摘要：获取商品评论V1/Get product reviews V1
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_reviews_v1_api_v1_tiktok_shop_web_fetch_product_reviews_v1_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok Shop商品的评论列表（支持所有国家区域的商品，无需指定地区代码）
> - 支持按相关性或时间排序
> - 支持评论筛选和分页加载
> ### 参数:
> - product_id: 商品ID (必填)
> - sort_type: 排序方式
>     - 1: 按相关性排序
>     - 2: 按时间排序(最新)，默认值
> - filter_id: 评论筛选ID (可选)
>     - 可从首次响应的 review_filters 列表中获取
> - offset: 分页偏移量，默认1
>     - 如果响应中 has_more=1，使用 next_cursor 值进行下一页请求
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 200,
>     "data": {
>         "reviews": [                      // 评论列表(每页20条)
>             {
>                 "review_id": "xxx",
>                 "user_info": {},          // 用户信息
>                 "rating": 5,              // 评分(1-5星)
>                 "review_content": "...",  // 评论内容
>                 "images": [],             // 评论图片
>                 "videos": [],             // 评论视频
>                 "create_time": 0,         // 创建时间戳
>                 "is_verified_buyer": true // 是否认证买家
>             }
>         ],
>         "has_more": 1,                    // 是否有更多: 1=有, 0=无
>         "next_cursor": "xxx",             // 下一页游标
>         "review_filters": [               // 可用的筛选器
>             {
>                 "filter_id": "xxx",
>                 "filter_name": "所有评论"
>             }
>         ],
>         "statistics": {                   // 统计信息
>             "total_count": 1000,
>             "average_rating": 4.5,
>             "rating_distribution": {}     // 星级分布
>         }
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get TikTok Shop product reviews list (supports products from all countries/regions without specifying region code)
> - Support sorting by relevance or time
> - Support review filtering and pagination
> ### Parameters:
> - product_id: Product ID (required)
> - sort_type: Sort type
>     - 1: Sort by relevance
>     - 2: Sort by recent (default)
> - filter_id: Review filter ID (optional)
>     - Can be obtained from review_filters list in first response
> - offset: Offset for pagination, default 1
>     - If has_more=1 in response, use next_cursor value for next page
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 200,
>     "data": {
>         "reviews": [                      // Review list (20 per page)
>             {
>                 "review_id": "xxx",
>                 "user_info": {},          // User info
>                 "rating": 5,              // Rating (1-5 stars)
>                 "review_content": "...",  // Review content
>                 "images": [],             // Review images
>                 "videos": [],             // Review videos
>                 "create_time": 0,         // Create timestamp
>                 "is_verified_buyer": true // Is verified buyer
>             }
>         ],
>         "has_more": 1,                    // Has more: 1=yes, 0=no
>         "next_cursor": "xxx",             // Next page cursor
>         "review_filters": [               // Available filters
>             {
>                 "filter_id": "xxx",
>                 "filter_name": "All reviews"
>             }
>         ],
>         "statistics": {                   // Statistics
>             "total_count": 1000,
>             "average_rating": 4.5,
>             "rating_distribution": {}     // Rating distribution
>         }
>     }
> }
> ```
>
> # [示例/Example]
> product_id = "1731677627342753961"
> sort_type = 2

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 1731677627342753961 | 无 |
| sort_type | query | integer | 否 | 排序方式/Sort type: 1=相关性/Relevance, 2=最新/Recent | 2 | 2 | 无 |
| filter_id | query | string | 否 | 筛选ID/Filter ID | 无 | 无 | 无 |
| offset | query | integer | 否 | 分页偏移量/Offset for pagination | 1 | 1 | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-product-reviews-v2"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_product_reviews_v2`

- 摘要：获取商品评论V2/Get product reviews V2
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_product_reviews_v2_api_v1_tiktok_shop_web_fetch_product_reviews_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok Shop商品评论（仅支持美洲，欧洲，地区的商品，东南亚地区商品请使用 `fetch_product_reviews_v1` 接口）
> - 支持多种筛选和排序方式
> - 数据结构更完整，包含更多评论详情
> ### 参数:
> - product_id: 商品ID (必填)
> - page_start: 起始页码，默认1
>     - 当响应中 has_more=1 时，使用当前页码 +1 进行下一页请求
> - sort_rule: 排序规则，默认2
> - filter_type: 筛选类型
>     - 1: 默认不选择任何过滤
>     - 2: 包含图片或视频
>     - 3: 真实购买过滤
> - filter_value: 星级筛选
>     - 6: 所有星级的评论(默认)
>     - 5: 5星评价
>     - 4: 4星评价
>     - 3: 3星评价
>     - 2: 2星评价
>     - 1: 1星评价
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "reviews": [                      // 评论列表(每页20条)
>             {
>                 "review_id": "xxx",
>                 "user": {                 // 用户信息
>                     "user_id": "xxx",
>                     "nickname": "用户昵称",
>                     "avatar": "头像URL"
>                 },
>                 "rating": 5,              // 评分(1-5星)
>                 "content": "评论内容",
>                 "medias": [               // 媒体文件(图片/视频)
>                     {
>                         "type": "image",
>                         "url": "媒体URL"
>                     }
>                 ],
>                 "create_time": 0,         // 创建时间戳
>                 "verified_purchase": true, // 是否认证购买
>                 "product_info": {},       // 商品信息
>                 "likes_count": 10,        // 点赞数
>                 "seller_reply": {}        // 卖家回复
>             }
>         ],
>         "has_more": 1,                    // 是否有更多: 1=有, 0=无
>         "page_start": 1,                  // 当前页码
>         "total_count": 500,               // 总评论数
>         "review_summary": {               // 评论摘要
>             "average_rating": 4.8,
>             "star_distribution": {        // 星级分布
>                 "5": 400,
>                 "4": 80,
>                 "3": 15,
>                 "2": 3,
>                 "1": 2
>             }
>         }
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get TikTok Shop product reviews (only supports products from Americas, Europe; for Southeast Asia products, use `fetch_product_reviews_v1`)
> - Support multiple filtering and sorting options
> - More complete data structure with detailed review information
> ### Parameters:
> - product_id: Product ID (required)
> - page_start: Starting page number, default 1
>     - When has_more=1 in response, use current page +1 for next page
> - sort_rule: Sort rule, default 2
> - filter_type: Filter type
>     - 1: Default, no filter
>     - 2: Contains images or videos
>     - 3: Verified purchase filter
> - filter_value: Star filter
>     - 6: All star ratings (default)
>     - 5: 5-star reviews
>     - 4: 4-star reviews
>     - 3: 3-star reviews
>     - 2: 2-star reviews
>     - 1: 1-star reviews
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "reviews": [                      // Review list (20 per page)
>             {
>                 "review_id": "xxx",
>                 "user": {                 // User info
>                     "user_id": "xxx",
>                     "nickname": "Username",
>                     "avatar": "Avatar URL"
>                 },
>                 "rating": 5,              // Rating (1-5 stars)
>                 "content": "Review content",
>                 "medias": [               // Media files (images/videos)
>                     {
>                         "type": "image",
>                         "url": "Media URL"
>                     }
>                 ],
>                 "create_time": 0,         // Create timestamp
>                 "verified_purchase": true, // Is verified purchase
>                 "product_info": {},       // Product info
>                 "likes_count": 10,        // Likes count
>                 "seller_reply": {}        // Seller reply
>             }
>         ],
>         "has_more": 1,                    // Has more: 1=yes, 0=no
>         "page_start": 1,                  // Current page
>         "total_count": 500,               // Total review count
>         "review_summary": {               // Review summary
>             "average_rating": 4.8,
>             "star_distribution": {        // Star distribution
>                 "5": 400,
>                 "4": 80,
>                 "3": 15,
>                 "2": 3,
>                 "1": 2
>             }
>         }
>     }
> }
> ```
>
> # [示例/Example]
> product_id = "1729556436942358002"
> page_start = 1
> sort_rule = 2
> filter_type = 1
> filter_value = 6
> region = "MY"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| product_id | query | string | 是 | 商品ID/Product ID | 无 | 1729556436942358002 | 无 |
| page_start | query | integer | 否 | 起始页码/Page start | 1 | 1 | 无 |
| sort_rule | query | integer | 否 | 排序规则/Sort rule | 2 | 2 | 无 |
| filter_type | query | integer | 否 | 筛选类型/Filter type: 1=默认, 2=有图片/视频, 3=真实购买 | 1 | 1 | 无 |
| filter_value | query | integer | 否 | 星级筛选/Star filter: 6=全部, 5-1=对应星级 | 6 | 6 | 无 |
| region | query | string | 否 | 地区代码/Region code | MY | MY | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-products-by-category-id"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_products_by_category_id`

- 摘要：根据分类ID获取商品列表/Get products by category ID
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_products_by_category_id_api_v1_tiktok_shop_web_fetch_products_by_category_id_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据商品分类ID获取该分类下的商品列表
> - 可用于构建分类浏览功能
> ### 参数:
> - category_id: 分类ID (必填，从fetch_products_category_list接口获取)
> - offset: 翻页偏移量 (默认0)
>     - 每页默认20个商品，每次请求增加20，当响应中的 `hasMore` 为true时可继续请求下一页，否则已到最后一页。
>     - 例如: 第1页offset=0，第2页offset=20，第3页offset=40，以此类推。
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // 商品列表(最多20个)
>             {
>                 "product_id": "xxx",
>                 "title": "商品标题",
>                 "image": "商品图片",
>                 "price": {},              // 价格信息
>                 "rating": {},             // 评分信息
>                 "sales": {}               // 销量信息
>             }
>         ]
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get product list by category ID
> - Can be used to build category browsing feature
> ### Parameters:
> - category_id: Category ID (required, from fetch_products_category_list API)
> - offset: Offset for pagination (default 0)
>     - Default 20 products per page, increase by 20 for each request. If `hasMore` in response is true, can request next page, otherwise reached last page.
>     - Example: Page 1 offset=0, Page 2 offset=20, Page 3 offset=40, and so on.
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // Product list (up to 20)
>             {
>                 "product_id": "xxx",
>                 "title": "Product title",
>                 "image": "Product image",
>                 "price": {},              // Price info
>                 "rating": {},             // Rating info
>                 "sales": {}               // Sales info
>             }
>         ]
>     }
> }
> ```
>
> # [示例/Example]
> category_id = 963976
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category_id | query | integer | 是 | 分类ID/Category ID | 无 | 963976 | 无 |
| offset | query | integer | 否 | 翻页偏移量/Offset for pagination | 0 | 0 | 无 |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-products-category-list"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_products_category_list`

- 摘要：获取商品分类列表/Get product category list
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_products_category_list_api_v1_tiktok_shop_web_fetch_products_category_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取TikTok Shop的商品分类目录
> - 返回完整的分类树结构
> ### 参数:
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 返回数据结构:
> ```json
> [
>     {
>         "self": {                     // 分类自身信息
>             "category_id": "xxx",
>             "category_level": 1,
>             "is_leaf": false,
>             "parent_category_id": "0",
>             "category_name": "分类名称",
>             "category_name_en": "Category Name",
>             "image_url": "分类图片URL"
>         },
>         "children": [                 // 子分类列表
>             {
>                 "self": {...},
>                 "children": [...]
>             }
>         ]
>     }
> ]
> ```
> - 总共约28个主分类
>
> # [English]
> ### Purpose:
> - Get TikTok Shop product category directory
> - Returns complete category tree structure
> ### Parameters:
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Response Structure:
> ```json
> [
>     {
>         "self": {                     // Category info
>             "category_id": "xxx",
>             "category_level": 1,
>             "is_leaf": false,
>             "parent_category_id": "0",
>             "category_name": "Category Name",
>             "category_name_en": "Category Name",
>             "image_url": "Category image URL"
>         },
>         "children": [                 // Sub-categories
>             {
>                 "self": {...},
>                 "children": [...]
>             }
>         ]
>     }
> ]
> ```
> - Total about 28 main categories
>
> # [示例/Example]
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-search-products-list"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list`

- 摘要：搜索商品列表V1/Search products list V1
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_products_list_api_v1_tiktok_shop_web_fetch_search_products_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 根据关键词搜索商品
> - 支持分页加载更多结果
> ### 参数:
> - search_word: 搜索关键词 (必填)
> - offset: 偏移量，用于分页 (默认0)
> - page_token: 分页标记，用于获取下一页
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // 商品列表(每页30个)
>             {
>                 "product_id": "xxx",
>                 "title": "商品标题",
>                 "image": "商品图片URL",
>                 "product_price_info": {},  // 价格信息
>                 "rate_info": {},           // 评分信息
>                 "sold_info": {},           // 销量信息
>                 "seller_info": {},         // 卖家信息
>                 "seo_url": "商品SEO链接",
>                 "product_marketing_info": {} // 营销信息
>             }
>         ],
>         "has_more": true,             // 是否有更多
>         "load_more_params": {         // 分页参数
>             "offset": 30,
>             "page_token": "xxx",
>             "api_source": 2
>         }
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Search products by keyword
> - Support pagination to load more results
> ### Parameters:
> - search_word: Search keyword (required)
> - offset: Offset for pagination (default 0)
> - page_token: Page token for next page
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // Product list (30 per page)
>             {
>                 "product_id": "xxx",
>                 "title": "Product title",
>                 "image": "Product image URL",
>                 "product_price_info": {},  // Price info
>                 "rate_info": {},           // Rating info
>                 "sold_info": {},           // Sales info
>                 "seller_info": {},         // Seller info
>                 "seo_url": "Product SEO URL",
>                 "product_marketing_info": {} // Marketing info
>             }
>         ],
>         "has_more": true,             // Has more
>         "load_more_params": {         // Pagination params
>             "offset": 30,
>             "page_token": "xxx",
>             "api_source": 2
>         }
>     }
> }
> ```
>
> # [示例/Example]
> search_word = "labubu"
> offset = 0
> page_token = ""
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword | 无 | labubu | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 0 | 无 |
| page_token | query | string | 否 | 分页标记/Page token | 无 | 无 | 无 |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v2"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v2`

- 摘要：搜索商品列表V2(移动端)/Search products list V2 (Mobile)
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_products_list_v2_api_v1_tiktok_shop_web_fetch_search_products_list_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索商品(移动端接口)
> - 数据结构更精简，响应更快
> ### 参数:
> - search_word: 搜索关键词 (必填)
> - offset: 偏移量 (默认0)
> - page_token: 分页标记
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [...],            // 商品列表
>         "has_more": true,             // 是否有更多
>         "load_more_params": {}        // 加载更多参数
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Search products (Mobile API)
> - More streamlined data, faster response
> ### Parameters:
> - search_word: Search keyword (required)
> - offset: Offset (default 0)
> - page_token: Page token
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [...],            // Product list
>         "has_more": true,             // Has more
>         "load_more_params": {}        // Load more params
>     }
> }
> ```
>
> # [示例/Example]
> search_word = "labubu"
> offset = 0
> page_token = ""
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword | 无 | labubu | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 0 | 无 |
| page_token | query | string | 否 | 分页标记/Page token | 无 | 无 | 无 |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-search-products-list-v3"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_search_products_list_v3`

- 摘要：搜索商品列表V3/Search products list V3
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_products_list_v3_api_v1_tiktok_shop_web_fetch_search_products_list_v3_get`

#### 说明

> # [中文]
> ### 用途:
> - 搜索TikTok Shop商品，支持高级筛选和排序
> - 提供更多的筛选选项和排序方式
> - 适合需要精细化筛选的场景
> ### 参数:
> - keyword: 搜索关键词 (必填)
> - offset: 分页偏移量，默认0
>     - 每页固定返回20个商品
>     - 如果响应中 has_more=1，使用 cursor 值进行下一页请求
> - region: 地区代码，Alpha-2 国家代码 (必填)
> - sort_by: 排序方式，默认 RELEVANCE
>     - RELEVANCE: 按相关性排序（默认）
>     - PRICE_ASC: 价格从低到高
>     - PRICE_DESC: 价格从高到低
>     - BEST_SELLERS: 最畅销
> - filters_data: 筛选数据，JSON数组格式字符串（可选）
>     - 可从首次响应的 filter_groups 字段获取可用筛选器
>     - 格式示例：
>         - 简单筛选按钮: {"type": 2, "value": "true"}
>         - 范围/多选: {"type": 8, "value_list": ["1,1000"]}
>         - 完整示例（价格和4星及以上）: [{"type": 2, "value": "true"},{"type": 8, "value_list": ["1,1000"]}]
> ### 重要提示:
> - 每页固定返回20个商品
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 200,
>     "data": {
>         "products": [                  // 商品列表
>             {
>                 "product_id": "xxx",
>                 "title": "商品标题",
>                 "image": "商品图片URL",
>                 "price": {             // 价格信息
>                     "current_price": 19.99,
>                     "original_price": 29.99,
>                     "discount": "33% OFF"
>                 },
>                 "rating": {            // 评分信息
>                     "average": 4.8,
>                     "count": 1234
>                 },
>                 "sales": 5000,         // 销量
>                 "seller_info": {},     // 卖家信息
>                 "url": "商品链接"
>             }
>         ],
>         "has_more": 1,                 // 是否有更多: 1=有, 0=无
>         "cursor": "xxx",               // 下一页游标
>         "filter_groups": [             // 可用的筛选器组
>             {
>                 "group_name": "价格",
>                 "filters": [
>                     {
>                         "type": 8,
>                         "name": "价格区间",
>                         "options": [...]
>                     }
>                 ]
>             },
>             {
>                 "group_name": "评分",
>                 "filters": [
>                     {
>                         "type": 2,
>                         "name": "4星及以上",
>                         "value": "true"
>                     }
>                 ]
>             }
>         ],
>         "total_count": 10000           // 总商品数
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Search TikTok Shop products with advanced filtering and sorting
> - Provides more filter options and sort methods
> - Suitable for scenarios requiring fine-grained filtering
> ### Parameters:
> - keyword: Search keyword (required)
> - offset: Offset for pagination, default 0
>     - Fixed 20 products per page
>     - If has_more=1 in response, use cursor value for next page
> - region: Region code, Alpha-2 country code (required)
> - sort_by: Sort method, default RELEVANCE
>     - RELEVANCE: Sort by relevance (default)
>     - PRICE_ASC: Price low to high
>     - PRICE_DESC: Price high to low
>     - BEST_SELLERS: Best sellers
> - filters_data: Filter data, JSON array format string (optional)
>     - Available filters can be obtained from filter_groups field in first response
>     - Format examples:
>         - Simple filter button: {"type": 2, "value": "true"}
>         - Range/multiple select: {"type": 8, "value_list": ["1,1000"]}
>         - Complete example (price and 4+ stars): [{"type": 2, "value": "true"},{"type": 8, "value_list": ["1,1000"]}]
> ### Important Notice:
> - Fixed 20 products per page
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 200,
>     "data": {
>         "products": [                  // Product list
>             {
>                 "product_id": "xxx",
>                 "title": "Product title",
>                 "image": "Product image URL",
>                 "price": {             // Price info
>                     "current_price": 19.99,
>                     "original_price": 29.99,
>                     "discount": "33% OFF"
>                 },
>                 "rating": {            // Rating info
>                     "average": 4.8,
>                     "count": 1234
>                 },
>                 "sales": 5000,         // Sales count
>                 "seller_info": {},     // Seller info
>                 "url": "Product URL"
>             }
>         ],
>         "has_more": 1,                 // Has more: 1=yes, 0=no
>         "cursor": "xxx",               // Next page cursor
>         "filter_groups": [             // Available filter groups
>             {
>                 "group_name": "Price",
>                 "filters": [
>                     {
>                         "type": 8,
>                         "name": "Price range",
>                         "options": [...]
>                     }
>                 ]
>             },
>             {
>                 "group_name": "Rating",
>                 "filters": [
>                     {
>                         "type": 2,
>                         "name": "4 Stars & Up",
>                         "value": "true"
>                     }
>                 ]
>             }
>         ],
>         "total_count": 10000           // Total product count
>     }
> }
> ```
>
> # [示例/Example]
> keyword = "baby"
> offset = 0
> region = "US"
> sort_by = "PRICE_ASC"
> filters_data = '[{"type": 2, "value": "true"},{"type": 8, "value_list": ["1,1000"]}]'

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| keyword | query | string | 是 | 搜索关键词/Search keyword | 无 | Labubu | 无 |
| offset | query | integer | 否 | 偏移量/Offset | 0 | 0 | 无 |
| region | query | string | 否 | 地区代码/Region code (Alpha-2) | US | US | 无 |
| sort_by | query | string | 否 | 排序方式/Sort by: RELEVANCE, PRICE_ASC, PRICE_DESC, BEST_SELLERS | RELEVANCE | RELEVANCE | 无 |
| filters_data | query | string | 否 | 筛选数据JSON/Filters data JSON | 无 | 无 | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion`

- 摘要：获取搜索关键词建议V1/Get search keyword suggestions V1
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_word_suggestion_api_v1_tiktok_shop_web_fetch_search_word_suggestion_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取搜索关键词的自动补全建议
> - 用于搜索框的智能提示功能
> ### 参数:
> - search_word: 搜索关键词 (必填)
> - lang: 语言代码 (en/zh等)
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "",
>     "data": [                        // 建议列表(最多50个)
>         "phone case",
>         "phone mount",
>         "phone holder for car",
>         "..."
>     ]
> }
> ```
>
> # [English]
> ### Purpose:
> - Get auto-complete suggestions for search keywords
> - Used for search box smart suggestions
> ### Parameters:
> - search_word: Search keyword (required)
> - lang: Language code (en/zh etc.)
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "",
>     "data": [                        // Suggestion list (up to 50)
>         "phone case",
>         "phone mount",
>         "phone holder for car",
>         "..."
>     ]
> }
> ```
>
> # [示例/Example]
> search_word = "labubu"
> lang = "en"
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword | 无 | labubu | 无 |
| lang | query | string | 否 | 语言/Language | en | en | 无 |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-search-word-suggestion-v2"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_search_word_suggestion_v2`

- 摘要：获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile)
- 能力：搜索 / 电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_search_word_suggestion_v2_api_v1_tiktok_shop_web_fetch_search_word_suggestion_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取搜索关键词建议(移动端接口)
> - 专为电商搜索结果优化
> ### 参数:
> - search_word: 搜索关键词 (必填)
> - lang: 语言代码 (en/zh等)
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "",
>     "data": [                        // 建议列表(最多50个)
>         "关键词1",
>         "关键词2",
>         "..."
>     ]
> }
> ```
>
> # [English]
> ### Purpose:
> - Get search keyword suggestions (Mobile API)
> - Optimized for e-commerce search results
> ### Parameters:
> - search_word: Search keyword (required)
> - lang: Language code (en/zh etc.)
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "",
>     "data": [                        // Suggestion list (up to 50)
>         "keyword1",
>         "keyword2",
>         "..."
>     ]
> }
> ```
>
> # [示例/Example]
> search_word = "labubu"
> lang = "en"
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| search_word | query | string | 是 | 搜索关键词/Search keyword | 无 | labubu | 无 |
| lang | query | string | 否 | 语言/Language | en | en | 无 |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list`

- 摘要：获取商家商品列表V1/Get seller products list V1
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_seller_products_list_api_v1_tiktok_shop_web_fetch_seller_products_list_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取指定商家的商品列表
> - 支持分页加载更多商品
> ### 参数:
> - seller_id: 卖家ID (必填)
> - search_params: 搜索参数，用于分页加载(可选)
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // 商品列表(每页30个)
>             {
>                 "product_id": "xxx",
>                 "title": "商品标题",
>                 "image": "商品图片URL",
>                 "product_price_info": {},  // 价格信息
>                 "rate_info": {},           // 评分信息
>                 "sold_info": {},           // 销量信息
>                 "seller_info": {},         // 卖家信息
>                 "seo_url": "商品SEO链接"
>             }
>         ],
>         "has_more": true,             // 是否有更多商品
>         "load_more_params": {}        // 加载更多参数(用于下一页)
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get product list from specified seller
> - Support pagination to load more products
> ### Parameters:
> - seller_id: Seller ID (required)
> - search_params: Search parameters for pagination (optional)
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [                // Product list (30 per page)
>             {
>                 "product_id": "xxx",
>                 "title": "Product title",
>                 "image": "Product image URL",
>                 "product_price_info": {},  // Price info
>                 "rate_info": {},           // Rating info
>                 "sold_info": {},           // Sales info
>                 "seller_info": {},         // Seller info
>                 "seo_url": "Product SEO URL"
>             }
>         ],
>         "has_more": true,             // Has more products
>         "load_more_params": {}        // Load more params (for next page)
>     }
> }
> ```
>
> # [示例/Example]
> seller_id = "7495150558072178725"
> search_params = ""
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 卖家ID/Seller ID | 无 | 7495150558072178725 | 无 |
| search_params | query | string | 否 | 搜索参数(用于分页)/Search params (for pagination) | 无 | 30_WzQzOSwzOTAwMDAwMCwxNzIzMDU4NTY3NTM5LCIxNzI5NTc3OTc3OTI0Nzg0MTY1Il0= | 无 |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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

<a id="get-api-u1-v1-tiktok-shop-web-fetch-seller-products-list-v2"></a>
### `GET /api/u1/v1/tiktok/shop/web/fetch_seller_products_list_v2`

- 摘要：获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile)
- 能力：电商
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`fetch_seller_products_list_v2_api_v1_tiktok_shop_web_fetch_seller_products_list_v2_get`

#### 说明

> # [中文]
> ### 用途:
> - 获取商家商品列表(移动端接口)
> - 数据结构更精简
> ### 参数:
> - seller_id: 卖家ID (必填)
> - searchParams: 搜索参数(可选)
> - region: 地区代码 (US/GB/SG/MY/PH/TH/VN/ID)
> ### 重要提示:
> - 由于接口风控原因，请务必将请求timeout设置为30秒
> - 如遇到400错误代码，请重试请求3次
> ### 返回数据结构:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [...],            // 商品列表
>         "has_more": true,             // 是否有更多
>         "load_more_params": {}        // 加载更多参数
>     }
> }
> ```
>
> # [English]
> ### Purpose:
> - Get seller product list (Mobile API)
> - More streamlined data structure
> ### Parameters:
> - seller_id: Seller ID (required)
> - searchParams: Search parameters (optional)
> - region: Region code (US/GB/SG/MY/PH/TH/VN/ID)
> ### Important Notice:
> - Due to API rate limiting, please set request timeout to 30 seconds
> - If you encounter error code 400, please retry the request 3 times
> ### Response Structure:
> ```json
> {
>     "code": 0,
>     "message": "success",
>     "data": {
>         "products": [...],            // Product list
>         "has_more": true,             // Has more
>         "load_more_params": {}        // Load more params
>     }
> }
> ```
>
> # [示例/Example]
> seller_id = "7495150558072178725"
> searchParams = ""
> region = "US"

#### 参数

| 字段 | 位置 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| seller_id | query | string | 是 | 卖家ID/Seller ID | 无 | 7495150558072178725 | 无 |
| searchParams | query | string | 否 | 搜索参数/Search params | 无 | 无 | 无 |
| region | query | string | 否 | 地区代码/Region code | US | US | 无 |

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
