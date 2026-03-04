# Capability Routing Matrix

> 目的：该矩阵是 TikOmni skill 的**能力路由唯一入口清单**。先匹配固定能力，再进入通用兜底。
>
> 边界：这里定义的是 **Agent 路由策略（policy）**，不是对底层脚本执行细节的逐行说明；脚本行为以仓库内实际实现为准。

| capability | status | trigger intents | route chain (entry script/playbook) | output expectation | notes |
|---|---|---|---|---|---|
| douyin.single_video | active | 抖音单视频解析、单条作品结构化提取、按视频链接抓取字段 | `scripts/cli/run_tikomni_extract.py` -> `scripts/platform/douyin/run_douyin_single_video.py` | 输出单视频 `raw + normalized + markdown`；包含 `missing_fields`、`fallback_trace`、`request_id`（可用时） | 明确走 availability-first；`one_video app` 主路，`one_video web` 兜底 |
| xiaohongshu.single_note | active | 小红书单笔记解析、按笔记链接抓取内容与互动字段 | `scripts/platform/xiaohongshu/run_xiaohongshu_extract.py` | 输出单笔记 `raw + normalized + markdown`；包含 `missing_fields`、`fallback_trace`、`request_id`（可用时） | 固定单笔记能力，优先按已定义字段集交付 |
| douyin.homepage_extract | active | 抖音作者主页抓取、主页样本提取、主页分析前置采样 | `references/playbooks/douyin-home-extract.md` | 产出主页样本与可追溯字段，为后续分析/写卡提供输入 | 固定 playbook 路由；命中即直达，不进入通用意图分流 |
| xiaohongshu.homepage_extract | active | 小红书作者主页抓取、主页样本提取、主页分析前置采样 | `references/playbooks/xiaohongshu-home-extract.md` | 产出主页样本与可追溯字段，为后续分析/写卡提供输入 | 固定 playbook 路由；命中即直达，不进入通用意图分流 |
| author.sample_writer | active | 将作者主页样本写入标准卡片、产出作者样本沉淀文档 | `scripts/writers/write_author_homepage_samples.py` | 产出可复用的作者样本写入结果，字段保持可追溯 | 用于样本沉淀与后续内容分析协同 |
| universal.intent_fallback | fallback | 未命中上述固定能力的通用研究/抓取/分析请求 | `references/routing-rules.md` -> `references/api-catalog/index.md` -> `references/normalize-rules.md` -> `references/output-markdown.md` | 输出满足意图的结构化结果/报告，并显式给出 `missing_fields` 与 `fallback_trace` | 仅在矩阵固定能力未命中后触发 |

## Routing Rule (Hard)
1. 先按本矩阵做 capability 精确匹配（active 优先）。
2. 只有当固定能力未命中时，才允许进入 `universal.intent_fallback`。
3. 不得把 playbook 策略描述误写成“保证某脚本已执行”；执行事实以运行结果与 trace 为准。
