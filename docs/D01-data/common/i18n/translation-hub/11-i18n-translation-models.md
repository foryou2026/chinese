# i18n_translation_models

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-046, R-i18n-017, R-i18n-029 |
| 业务定义 | 翻译供应商下的模型配置（每供应商支持多模型） |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| provider_id | uuid | 是 | 无 | 否 | 所属供应商 | 引用 i18n_translation_providers(id) |
| model_name | text | 是 | 无 | 否 | 模型可读名称 | 如"Claude Sonnet"，长度≤100 |
| model_id | text | 是 | 无 | 否 | 模型 API 标识 | 如 claude-sonnet-4-20250514 |
| extra_params | jsonb | 否 | null | 否 | 请求参数 | 如 {temperature:0.3, max_tokens:4096} |
| is_default | boolean | 是 | false | 否 | 是否默认模型 | 每供应商仅一个默认 |
| is_active | boolean | 是 | true | 否 | 是否启用 | — |
| sort_order | integer | 是 | 0 | 否 | 显示排序 | — |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - (provider_id, model_id) 联合唯一。
> - is_default=true 时，每个 provider 下仅允许一个默认模型（应用层约束）。
> - 翻译时使用方式：将 provider 的 api_endpoint/api_key + model 的 model_id/extra_params 组合发起请求。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_translation_providers | N:1 | provider_id | CASCADE |
| i18n_table_config | 被引用 | default_translation_model_id | SET NULL |
| i18n_field_config | 被引用 | translation_model_id | SET NULL |
| i18n_ui_translations | 被引用 | translation_model_id | SET NULL |
| i18n_content_translations | 被引用 | translation_model_id | SET NULL |
| i18n_translation_tasks | 被引用 | model_id | SET NULL |
