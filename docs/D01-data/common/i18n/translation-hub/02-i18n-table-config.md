# i18n_table_config

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-020, R-i18n-021 |
| 业务定义 | 业务表的翻译配置（表级默认） |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| table_name | text | 是 | 无 | 是 | 业务表名 | public 域下的表名 |
| table_description | text | 否 | null | 否 | 表中文说明 | 长度≤200 |
| translation_enabled | boolean | 是 | false | 否 | 是否启用翻译 | — |
| default_source_locale | text | 是 | 'zh' | 否 | 默认源语言 | 必须是已注册的 locale_code |
| default_translation_model_id | uuid | 否 | null | 否 | 默认翻译模型 | 引用 i18n_translation_models(id) |
| default_needs_audio | boolean | 是 | false | 否 | 默认是否配音 | 表级默认配音开关 |
| default_tts_model_id | uuid | 否 | null | 否 | 默认音色模型 | 引用 i18n_tts_models(id) |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - table_name 仅允许 public 域下的业务表（排除 i18n_* 和系统表）。
> - 当管理员首次进入数据表列表页时，系统自动扫描 public 域下的表并创建配置记录。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_field_config | 1:N | table_name | CASCADE |
| i18n_translation_models | N:1 | default_translation_model_id | SET NULL |
| i18n_tts_models | N:1 | default_tts_model_id | SET NULL |
