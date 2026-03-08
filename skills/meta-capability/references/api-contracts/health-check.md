# Health-Check Full Contract

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Back to route summary: [`api-tags/health-check.md`](../api-tags/health-check.md)
- Current contract file: `api-contracts/health-check.md`
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `1`
- Default auth: Header `Authorization` Bearer
- Read this file only when you need precise auth notes, parameter descriptions, defaults, examples, or success-response fields.
- Tag description: **(服务器健康检查/Server Health Check)**

## Route Contracts

<a id="get-api-u1-v1-health-check"></a>
### `GET /api/u1/v1/health/check`

- Summary: 检查服务器是否正确响应请求 / Check if the server responds to requests correctly
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `health_check_api_v1_health_check_get`

#### Notes

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

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `status`:string

| Field | Type | Required | Description | Default | Example | Enum |
| --- | --- | --- | --- | --- | --- | --- |
| status | string | No | None | ok | None | None |
