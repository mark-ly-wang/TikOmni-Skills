# Prompt Contract · ASR_CLEAN

## Inputs
- `raw_content`
- `asr_clean`（若上游已提供，作为优先输入）

## Method (stable)
1. 选择输入基底：优先 `asr_clean`，否则 `raw_content`。
2. 去噪清洗：移除明显口头禅、重复叠词、异常空白。
3. 语义断句：按 `。！？；\n` 断句，并补齐句末中文标点。
4. 分段规则：每句单独一行，每段 2~4 句，段间空一行。
5. 保真约束：不新增事实、不改写核心结论、不输出提示词文本。

## Output Format
- 纯文本多段落：
  - 每句一行
  - 段间空行

## Constraints
- 不把清洗提示词写入正文。
- 不生成“总结式改写”，仅做可读性清洗。
- 不得凭空补充数据、观点和案例。

## Fallback / Data-insufficient
- 两个输入均为空：输出空字符串。
- 断句失败：保留原文并补单句句号。
- 超长段落：强制按 3 句一段切分。
