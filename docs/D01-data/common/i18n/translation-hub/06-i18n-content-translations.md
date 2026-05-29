# i18n_content_translations

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-024, R-i18n-025, R-i18n-026, R-i18n-027, R-i18n-028 |
| 业务定义 | 数据库业务内容的翻译（通用翻译表，框架核心） |
| 状态机 | SM-i18n-001 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| table_name | text | 是 | 无 | 否 | 业务表名 | 如 courses |
| record_id | uuid | 是 | 无 | 否 | 原记录 ID | 业务表的主键值 |
| field_name | text | 是 | 无 | 否 | 字段名 | 如 title |
| locale | text | 是 | 无 | 否 | 目标语言 | 已启用的 locale_code |
| source_text_hash | text | 否 | null | 否 | 源文哈希 | MD5，用于检测源文变更 |
| translated_text | text | 否 | null | 否 | 翻译内容 | 翻译后填入 |
| status | text | 是 | 'pending' | 否 | 翻译状态 | 枚举:translation_status_enum |
| translated_by | text | 否 | null | 否 | 翻译来源 | 'ai' 或管理员 user_id |
| last_translated_at | timestamptz | 否 | null | 否 | 最后翻译时间 | — |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - (table_name, record_id, field_name, locale) 联合唯一。
> - 无物理外键关联业务表（通用框架设计，通过 table_name + record_id 逻辑关联）。
> - source_text_hash 用于检测源文变更：业务表记录更新时，应用层比较当前字段值的 hash 与 source_text_hash，不一致则标记 status=outdated。
> - 业务表记录删除时，应用层需清理该记录的所有翻译条目。

## 关系

无物理外键。通过 (table_name, record_id) 逻辑关联任意业务表。

## 源文变更检测方案

**方案：应用层检测（推荐）**

在业务表的 CRUD Service 中，update 操作后检查修改的字段是否在 i18n_field_config 中配置了翻译。如果是，重新计算 hash 并比较：

```typescript
async function afterUpdate(tableName: string, recordId: string, changedFields: Record<string, any>) {
  const fieldConfigs = await getTranslatableFields(tableName);
  for (const field of Object.keys(changedFields)) {
    if (fieldConfigs.has(field)) {
      const newHash = md5(String(changedFields[field]));
      await db.query(`
        UPDATE i18n_content_translations
        SET status = 'outdated', updated_at = now()
        WHERE table_name = $1 AND record_id = $2 AND field_name = $3
          AND source_text_hash != $4
      `, [tableName, recordId, field, newHash]);
    }
  }
}
```

## app 端读取翻译（前端/API）

```typescript
async function getTranslatedContent(
  tableName: string,
  recordId: string,
  fieldName: string,
  locale: string,
  fallbackLocales: string[] = ['en', 'zh']
): Promise<string | null> {
  const locales = [locale, ...fallbackLocales.filter(l => l !== locale)];
  for (const l of locales) {
    const result = await db.query(`
      SELECT translated_text FROM i18n_content_translations
      WHERE table_name = $1 AND record_id = $2 AND field_name = $3
        AND locale = $4 AND status IN ('translated', 'reviewed')
    `, [tableName, recordId, fieldName, l]);
    if (result?.translated_text) return result.translated_text;
  }
  return null;
}
```
