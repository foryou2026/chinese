# i18n_field_config

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-022, R-i18n-023, R-i18n-050 |
| 业务定义 | 业务表字段的翻译配置（字段级，覆盖表级默认） |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| table_name | text | 是 | 无 | 否 | 所属表名 | 必须存在于 i18n_table_config |
| field_name | text | 是 | 无 | 否 | 字段名 | 实际存在的列名 |
| field_type | text | 是 | 无 | 否 | 字段数据类型 | text/varchar/jsonb 等 |
| needs_translation | boolean | 否 | null | 否 | 是否需要翻译 | null=继承表级，true/false=覆盖 |
| source_locale | text | 否 | null | 否 | 源语言 | null=继承表级，否则为 locale_code |
| needs_audio | boolean | 否 | null | 否 | 是否需要配音 | null=继承表级，true/false=覆盖 |
| is_manually_set | boolean | 是 | false | 否 | 是否手动设置 | 区分手动配置与自动扫描 |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - (table_name, field_name) 联合唯一。
> - needs_translation/source_locale/needs_audio 为 null 时表示继承表级配置（i18n_table_config）。
> - 仅 text/varchar/jsonb 类型的字段允许设置 needs_translation=true。
> - 配置优先级：字段级非 null 值 > 表级默认值。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_table_config | N:1 | table_name | CASCADE |

## 配置优先级合并逻辑（应用层）

```typescript
function resolveFieldConfig(tableConfig: TableConfig, fieldConfig: FieldConfig) {
  return {
    needs_translation: fieldConfig.needs_translation ?? tableConfig.translation_enabled,
    source_locale: fieldConfig.source_locale ?? tableConfig.default_source_locale,
    needs_audio: fieldConfig.needs_audio ?? tableConfig.default_needs_audio,
  };
}
```
