# i18n_ui_translations

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-013, R-i18n-014, R-i18n-015, R-i18n-016 |
| 业务定义 | UI 文案的翻译内容（每个 key × 每种语言 = 一条记录） |
| 状态机 | SM-i18n-001 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| entry_id | uuid | 是 | 无 | 否 | 关联 UI 文案 | 引用 i18n_ui_entries(id) |
| locale | text | 是 | 无 | 否 | 目标语言 | 已启用的 locale_code |
| translated_text | text | 否 | null | 否 | 翻译内容 | 翻译后填入 |
| status | text | 是 | 'pending' | 否 | 翻译状态 | 枚举:translation_status_enum |
| translated_by | text | 否 | null | 否 | 翻译来源 | 'ai' 或管理员 user_id |
| last_translated_at | timestamptz | 否 | null | 否 | 最后翻译时间 | — |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - (entry_id, locale) 联合唯一。
> - 启用新语言时，系统为所有 i18n_ui_entries 自动创建该语言的翻译记录（status=pending）。
> - 源文案（中文）变更时，该 entry 的所有翻译记录 status 自动标记为 outdated。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_ui_entries | N:1 | entry_id | CASCADE |
