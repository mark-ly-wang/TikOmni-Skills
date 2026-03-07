---
name: meta-capability
description: 在需要先探索平台能力、定位可用接口、设计最小可行执行路径，或处理陌生平台而尚未命中固定业务模块时使用。适用于先完成接口发现、资源定位、字段盘点、执行编排，再决定是否转交 $single-work-analysis 或 $creator-analysis 的任务。
---

# Meta Capability

## 何时使用

- 用户目标还不够具体，先要判断应该走哪条能力链路。
- 平台较陌生，先要确认有哪些接口、字段、媒体资源和执行约束。
- 需要为“其他平台”设计最小可行接入路径，但还没有专用适配脚本。

## 不要做

- 不要定义作品卡或作者卡字段语义。
- 不要输出 `single-work-analysis` 或 `creator-analysis` 的正式分析结论。
- 不要把浏览器/manual observation 伪装成平台 API 结果。

## 工作流程

1. 先明确目标：平台、对象、数量、需要的字段、预期输出。
2. 读取 `references/dispatch.md`，判断应转交 `$single-work-analysis`、`$creator-analysis`，还是先继续做通用探索。
3. 如果进入通用探索，读取 `references/execution-guidelines.md`，优先确定：
   - 可用接口
   - 媒体/文本资源入口
   - 必须字段是否可取
   - 是否需要下载媒体或调用外部 ASR
4. 一旦业务边界清晰，转交到对应能力模块，不继续持有业务语义。

## References

- 路由与转交：`references/dispatch.md`
- 通用执行规则：`references/execution-guidelines.md`
