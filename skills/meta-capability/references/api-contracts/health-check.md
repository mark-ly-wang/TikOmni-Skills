# Health-Check 完整契约

- 回到索引：[`api-capability-index.md`](../api-capability-index.md)
- 回到路由详情：[`api-tags/health-check.md`](../api-tags/health-check.md)
- 当前契约文件：`api-contracts/health-check.md`
- 数据源：`https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- 获取时间：`2026-03-08T04:31:58+00:00`
- 路由数：`1`
- 默认认证：请求头 `Authorization` Bearer
- 使用方式：当需要精确的认证说明、参数描述、默认值、示例或成功响应字段时，再读本文件。
- 标签说明：**(服务器健康检查/Server Health Check)**

## 路由契约

<a id="get-api-u1-v1-health-check"></a>
### `GET /api/u1/v1/health/check`

- 摘要：检查服务器是否正确响应请求 / Check if the server responds to requests correctly
- 能力：通用能力
- 认证：请求头 `Authorization: Bearer {token}`；文档说明还可用 Cookie `Authorization` 兜底（`HTTPBearer`）
- operationId：`health_check_api_v1_health_check_get`

#### 说明

> # [中文]
>
> ### 用途说明:
>
> - 检查服务器是否正确响应请求。
>
> ### 参数说明:
>
> - 无参数。
>
> ### 返回结果:
>
> - `status`: 服务器状态，正常为 `ok`。
>
> # [English]
>
> ### Purpose:
>
> - Check if the server responds to requests correctly.
>
> ### Parameter Description:
>
> - No parameters.
>
> ### Return Result:
>
> - `status`: Server status, normal is `ok`.

#### 参数

无

#### 请求体

无

#### 成功响应

##### `200 application/json`

- Schema 摘要：`status`:string

| 字段 | 类型 | 必填 | 说明 | 默认值 | 示例 | 枚举 |
| --- | --- | --- | --- | --- | --- | --- |
| status | string | 否 | 无 | ok | 无 | 无 |
