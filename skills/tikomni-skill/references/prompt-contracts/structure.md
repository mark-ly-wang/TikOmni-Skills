# Prompt Contract · 结构（structure）

## Inputs
- `asr_clean`

## Method (stable)
1. 对每句进行结构标签检测：`钩子/冲突/转折/举证/CTA`。
2. 统计各标签覆盖次数。
3. 根据覆盖度判定模板：
   - 覆盖 >=4：`钩子→冲突→转折→举证→CTA`
   - 否则：`钩子→观点→补充说明`
4. 输出缺失模块，作为改写优先级。

## Output Format
- `结构标签覆盖`：`钩子:a, 冲突:b, 转折:c, 举证:d, CTA:e`
- `模板判定`：`...`
- `缺失模块`：`模块1、模块2`（无则“无”）

## Constraints
- 所有判断必须来自句级关键词命中。
- 不允许跳过缺失项输出。

## Fallback / Data-insufficient
- 无有效分句：输出“数据不足”，并提示“补充ASR后再做结构标注”。
