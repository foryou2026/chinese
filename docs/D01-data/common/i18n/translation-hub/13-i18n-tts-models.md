# i18n_tts_models

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-056, R-i18n-057, R-i18n-066 |
| 业务定义 | TTS 供应商下的音色模型配置（每供应商支持多音色模型，替代原 i18n_audio_config） |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| provider_id | uuid | 是 | 无 | 否 | 所属供应商 | 引用 i18n_tts_providers(id) |
| model_name | text | 是 | 无 | 否 | 音色可读名称 | 如"Xiaoxiao（活泼女声）" |
| voice_id | text | 是 | 无 | 否 | 音色 API 标识 | TTS 供应商的 voice ID |
| locale | text | 否 | null | 否 | 绑定语言 | 已启用的 locale_code，null=通用 |
| extra_params | jsonb | 否 | null | 否 | 音色参数 | 如 {speed:1.0, pitch:0} |
| output_format | text | 是 | 'mp3' | 否 | 输出格式 | mp3/wav/ogg |
| is_default | boolean | 是 | false | 否 | 是否默认音色 | 每供应商仅一个默认 |
| is_active | boolean | 是 | true | 否 | 是否启用 | — |
| sort_order | integer | 是 | 0 | 否 | 显示排序 | — |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - (provider_id, voice_id) 联合唯一。
> - locale 可为 null，表示通用音色（不限语言）；非 null 时绑定特定语言。
> - 配音时使用方式：将 provider 的 api_endpoint/api_key + model 的 voice_id/extra_params 组合发起 TTS 请求。
> - 本表替代原 i18n_audio_config 表（1.1.8 重构）。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_tts_providers | N:1 | provider_id | CASCADE |
| i18n_table_config | 被引用 | default_tts_model_id | SET NULL |
| i18n_field_config | 被引用 | tts_model_id | SET NULL |
| i18n_audio_files | 被引用 | tts_model_id | SET NULL |
| i18n_audio_tasks | 被引用 | model_id | SET NULL |
