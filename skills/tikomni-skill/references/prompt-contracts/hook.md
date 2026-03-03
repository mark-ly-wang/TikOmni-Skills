# Prompt Contract · Hook

## Inputs
- `title`
- `asr_clean`

## Method (stable)
1. 提取开头钩子：ASR 首句（无则用标题）。
2. 提取中段钩子：ASR 中位句。
3. 提取结尾钩子：最后一句含 CTA/召回词的句子。
4. 开头钩子类型判定：疑问式 / 反常识式 / 场景代入式 / 陈述式。

## Output Format
- `开头钩子（类型）`：`原句`
- `中段钩子`：`原句`
- `结尾钩子`：`原句`

## Constraints
- 必须优先输出原话，不做大幅改写。
- 结尾若无动作句要明确标注“未检测到明确结尾钩子”。

## Fallback / Data-insufficient
- 标题与 ASR 均缺失：三项输出“数据不足”。
- 中段不足：输出“数据不足（中段文本不足）”。
