# 内容翻译接口

> **说明**：本文件覆盖数据库内容翻译相关接口（R-i18n-020~028）。1.1.6 起"数据库内容翻译"统一简称为"内容翻译"。配音配置已完全解耦，详见 [05-audio.md](./05-audio.md)。

## API-i18n-tables-list 数据表列表

```
GET /api/v1/admin/i18n/content/tables
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 查询 `information_schema.tables` 获取 public 域下所有表
2. 排除 i18n_* 系统表
3. 左连接 `i18n_table_config` 获取翻译配置
4. 聚合 `i18n_field_config` 获取可翻译字段数
5. 聚合 `i18n_content_translations` 计算覆盖率

### Response 200

```json
{
  "data": [
    {
      "table_name": "courses",
      "table_description": "课程表",
      "translation_enabled": true,
      "default_source_locale": "zh",
      "translatable_field_count": 3,
      "total_record_count": 50,
      "coverage": {
        "en": 0.85,
        "vi": 0.60
      }
    }
  ]
}
```

---

## API-i18n-table-config 表级配置

```
PATCH /api/v1/admin/i18n/content/tables/:tableName
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "table_description": "课程表",
  "translation_enabled": true,
  "default_source_locale": "zh"
}
```

### 业务逻辑
1. UPSERT `i18n_table_config`
2. 首次配置表时自动扫描字段并创建 `i18n_field_config` 记录

### Response 200

```json
{
  "data": { "table_name": "courses", "translation_enabled": true }
}
```

---

## API-i18n-fields-list 字段列表

```
GET /api/v1/admin/i18n/content/tables/:tableName/fields
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 查询 `information_schema.columns` 获取表字段
2. 左连接 `i18n_field_config` 获取字段配置
3. 合并表级默认配置（字段级 null 时使用表级值）
4. 聚合翻译覆盖率

### Response 200

```json
{
  "data": {
    "table_config": {
      "translation_enabled": true,
      "default_source_locale": "zh"
    },
    "fields": [
      {
        "field_name": "title",
        "field_type": "text",
        "needs_translation": true,
        "source_locale": "zh",
        "is_manually_set": true,
        "is_translatable_type": true,
        "record_count": 50,
        "coverage": { "en": 0.90, "vi": 0.60 }
      },
      {
        "field_name": "course_code",
        "field_type": "varchar",
        "needs_translation": false,
        "source_locale": "zh",
        "is_manually_set": true,
        "is_translatable_type": true,
        "record_count": 50,
        "coverage": {}
      },
      {
        "field_name": "created_at",
        "field_type": "timestamptz",
        "needs_translation": false,
        "source_locale": null,
        "is_manually_set": false,
        "is_translatable_type": false,
        "record_count": 50,
        "coverage": {}
      }
    ]
  }
}
```

---

## API-i18n-field-config 字段级配置

```
PATCH /api/v1/admin/i18n/content/tables/:tableName/fields/:fieldName
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "needs_translation": true,
  "source_locale": "en"
}
```

### 校验
- 字段类型必须是 text/varchar/jsonb（否则返回 40011）
- source_locale 必须是已注册的 locale_code

### 业务逻辑
1. UPSERT `i18n_field_config`，标记 is_manually_set=true
2. 如果从 false 改为 true：为该字段的所有记录×所有已启用语言创建 pending 翻译记录
3. 如果 source_locale 变更：原翻译记录全部标记为 outdated

### Response 200

```json
{
  "data": {
    "table_name": "courses",
    "field_name": "title",
    "needs_translation": true,
    "source_locale": "en",
    "is_manually_set": true
  }
}
```

---

## API-i18n-field-translations 字段翻译列表

```
GET /api/v1/admin/i18n/content/tables/:tableName/fields/:fieldName/translations
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| locale | string | 否 | 目标语言，默认 en |
| status | string | 否 | 状态筛选 |
| search | string | 否 | 按原文内容搜索 |
| page | integer | 否 | 页码，默认 1 |
| page_size | integer | 否 | 每页条数，默认 50 |

### 业务逻辑
1. 从业务表读取该字段的原始值（source text）
2. 左连接 `i18n_content_translations` 获取翻译
3. 分页返回

### Response 200

```json
{
  "data": {
    "field_config": {
      "source_locale": "zh"
    },
    "items": [
      {
        "record_id": "uuid",
        "source_text": "入门中文课程",
        "translation": {
          "id": "uuid",
          "locale": "en",
          "translated_text": "Beginner Chinese Course",
          "status": "translated",
          "translated_by": "ai",
          "last_translated_at": "2026-05-29T10:00:00Z"
        }
      }
    ],
    "pagination": { "page": 1, "page_size": 50, "total": 50 },
    "stats": { "pending": 5, "translated": 40, "reviewed": 3, "outdated": 2 }
  }
}
```

---

## API-i18n-content-update 更新内容翻译

```
PATCH /api/v1/admin/i18n/content/translations/:id
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "translated_text": "Beginner Chinese Course"
}
```

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "translated_text": "Beginner Chinese Course",
    "status": "reviewed"
  }
}
```

---

## API-i18n-content-translate 触发内容 AI 翻译

```
POST /api/v1/admin/i18n/content/translate
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "scope": "table",
  "table_name": "courses",
  "field_name": null,
  "target_locales": ["en"],
  "status_filter": ["pending", "outdated"]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| scope | string | 是 | `all` / `table` / `field` |
| table_name | string | 否 | scope=table/field 时必填 |
| field_name | string | 否 | scope=field 时必填 |
| target_locales | string[] | 否 | 空=所有已启用语言 |
| status_filter | string[] | 否 | 默认 pending+outdated |

### Response 202

```json
{
  "data": {
    "task_id": "uuid",
    "total_items": 100,
    "status": "queued"
  }
}
```
