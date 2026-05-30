# i18n_translation_providers

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-045, R-i18n-046 |
| 业务定义 | AI 翻译供应商配置（支持多供应商） |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| provider_name | text | 是 | 无 | 否 | 供应商名称 | 如"Claude"，长度≤100 |
| api_endpoint | text | 是 | 无 | 否 | API 端点 | 合法 URL |
| api_key_encrypted | text | 是 | 无 | 否 | 加密的 API Key | AES-256 加密存储 |
| translation_prompt | text | 否 | null | 否 | 翻译提示词模板 | 支持 {source_lang}/{target_lang}/{text}/{context} |
| is_active | boolean | 是 | true | 否 | 是否启用 | — |
| sort_order | integer | 是 | 0 | 否 | 显示排序 | — |
| last_tested_at | timestamptz | 否 | null | 否 | 最后测试时间 | — |
| test_status | text | 是 | 'untested' | 否 | 测试状态 | 枚举:provider_test_status_enum |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - api_key_encrypted 在 API 返回时脱敏（仅显示末 4 位）。
> - 不硬编码任何供应商平台，完全自定义（Dify 风格）。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_translation_models | 1:N | provider_id | CASCADE |
