# iOS-Shortcut Route Summary

- Back to index: [`api-capability-index.md`](../api-capability-index.md)
- Current tag file: `api-tags/ios-shortcut.md`
- Full contract: [`api-contracts/ios-shortcut.md`](../api-contracts/ios-shortcut.md)
- Source: `https://app.tikomni.com/openapi/tikomni-openapi.full.with-u2.public.latest.json`
- Fetched at: `2026-03-08T06:54:04+00:00`
- Route count: `1`
- Common capabilities: general
- Default auth: Header `Authorization` Bearer
- Common inputs: None
- Tag description: **(iOS快捷方式接口/iOS-Shortcut endpoints)**

## Routes

### `GET /api/u1/v1/ios_shortcut/shortcut`

- Summary: 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts
- Capabilities: general
- Auth: Header `Authorization: Bearer {token}`; docs also allow Cookie `Authorization` as fallback (`HTTPBearer`)
- operationId: `get_shortcut_api_v1_ios_shortcut_shortcut_get`
- Full contract: [`api-contracts/ios-shortcut.md#get-api-u1-v1-ios-shortcut-shortcut`](../api-contracts/ios-shortcut.md#get-api-u1-v1-ios-shortcut-shortcut)

#### Parameters

None

#### Request Body

None

#### Success Response

##### `200 application/json`

- Schema summary: `version*`:string, `update*`:string, `link*`:string, `link_en*`:string, `note*`:string, `note_en*`:string

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| version | string | Yes | None |
| update | string | Yes | None |
| link | string | Yes | None |
| link_en | string | Yes | None |
| note | string | Yes | None |
| note_en | string | Yes | None |
