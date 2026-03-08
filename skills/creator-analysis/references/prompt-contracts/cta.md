# Prompt Contract · CTA

## Inputs
- `asr_raw`（主字段）
- `asr_clean`（遗留兼容字段）

## Method (stable)
1. 扫描 CTA 关键词句（评论/关注/私信/收藏/转发/领取/报名/咨询/下单）。
2. 判定 CTA 类型：互动型 / 线索型 / 转化型。
3. 提取关键动作句（默认取最后一个 CTA 句）。
4. 计算 CTA 密度（CTA句数/总句数）。

## Output Format
- `CTA类型`：`互动型、线索型...`
- `关键动作句`：`原句`
- `CTA密度`：`x/y 句`

## Constraints
- 必须给出至少一个动作句或明确说明缺失。
- 不得虚构转化链路。

## Fallback / Data-insufficient
- 字幕/转写文本为空：输出“数据不足”。
- 无 CTA 句：输出“未检测到明确行动号召”，并给最小补全建议。
