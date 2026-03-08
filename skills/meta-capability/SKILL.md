---
name: meta-capability
description: Use this skill for TikOmni platform capability discovery, full API route lookup, input-field requirements, and route-selection across Douyin, Xiaohongshu, TikTok, YouTube, X, WeChat Channels, Official Accounts, and other supported platforms. 当用户问“支持哪些平台/接口”“能抓什么”“该调哪个接口”“要传哪些字段”“怎么获取作品/评论/主页/搜索/榜单/创作者数据”时触发；单作品深度分析和创作者聚合分析继续走专用 skill。
---

# Meta Capability

## 何时使用

- 用户先要确认 TikOmni 当前支持哪些平台、对象和 API 能力。
- 用户要知道“该调哪个 route”“要传哪些字段”“是否有评论/搜索/榜单/主页接口”。
- 需要在真正进入分析前，先完成平台能力盘点、路由选择和字段可得性判断。
- 面对陌生平台或陌生对象时，需要从全量 OpenAPI 中筛出最小可行调用链。

## 核心职责

- 提供完整 API 路由目录，让 agent 先知道“有哪些接口”。
- 告诉 agent 每条 route 的典型能力类型、入参位置和请求体字段。
- 给出当前仓库已验证的优先路由链，避免 agent 在全量目录里盲选。
- 在进入专用 skill 之前，先完成能力发现、接口选择、字段盘点和可行性判断。

## 不要做

- 不要把浏览器观察、猜测或人工补写内容伪装成接口结果。
- 不要承诺当前平台或当前接口链路拿不到的字段。
- 不要把单作品深度分析或作者级聚合分析直接塞进本 skill 本体。
- 不要只写“能力描述”而不给 route、入参和字段要求。

## 工作流程

1. 先读 `references/api-capability-index.md`，确认平台标签、能力类型和对应 tag 文件。
2. 再按需读 `references/api-tags/*.md`，确认 route 摘要、认证方式、关键入参和关键成功响应。
3. 如果需要精确字段说明、默认值、示例或完整响应结构，再读 `references/api-contracts/*.md`。
4. 再读 `references/implemented-route-map.md`，优先走当前仓库已经验证过的路由链。
5. 读取 `references/execution-guidelines.md`，确认对象类型、目标字段、输出形式和降级策略。
6. 如果任务涉及 ASR 超时、公网 URL 不可读或 U3 媒体中转，读取 `references/service-guides/asr-u2-u3-fallback.md`。
7. 如果任务是单作品深度分析或创作者聚合分析，再转交给专用 skill，但保留已经确认的 route 和字段事实。

## References

- API 能力索引：`references/api-capability-index.md`
- 按 tag 路由详情：`references/api-tags/`
- 按 tag 完整契约：`references/api-contracts/`
- 当前已验证路由链：`references/implemented-route-map.md`
- 通用执行规则：`references/execution-guidelines.md`
- U2/U3 ASR fallback：`references/service-guides/asr-u2-u3-fallback.md`
