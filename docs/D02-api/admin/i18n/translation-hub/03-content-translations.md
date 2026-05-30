# 内容翻译接口

> **说明**：本文件覆盖数据库内容翻译相关接口（R-i18n-020~029）。
> 状态仅 pending / translated 两种。管理员手动编辑已翻译内容时，status 保持 translated 不变。源文变更时 status 回退为 pending。
> 配音管理已完全解耦，详见 [05-audio.md](./05-audio.md)。

---

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
      "default_translation_model_id": "uuid",
      "default_translation_model_name": "GPT-4o",
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
  "default_source_locale": "zh",
  "default_translation_model_id": "uuid"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| table_description | string | 否 | 表描述（中文） |
| translation_enabled | boolean | 否 | 是否启用翻译 |
| default_source_locale | string | 否 | 默认源语言 |
| default_translation_model_id | uuid | 否 | 表级默认翻译模型 |

### 业务逻辑
1. UPSERT `i18n_table_config`
2. 首次配置表时自动扫描字段并创建 `i18n_field_config` 记录

### Response 200

```json
{
  "data": {
    "table_name": "courses",
    "translation_enabled": true,
    "default_translation_model_id": "uuid"
  }
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
      "default_source_locale": "zh",
      "default_translation_model_id": "uuid",
      "default_translation_model_name": "GPT-4o"
    },
    "fields": [
      {
        "field_name": "title",
        "field_type": "text",
        "needs_translation": true,
        "source_locale": "zh",
        "is_manually_set": true,
        "is_translatable_type": true,
        "translation_model_id": "uuid",
        "translation_model_name": "GPT-4o",
        "record_count": 50,
        "coverage": { "en": 0.90, "vi": 0.60 }
      },
      {
        "field_name": "created_at",
        "field_type": "timestamptz",
        "needs_translation": false,
        "source_locale": null,
        "is_manually_set": false,
        "is_translatable_type": false,
        "translation_model_id": null,
        "translation_model_name": null,
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
  "source_locale": "zh",
  "translation_model_id": "uuid",
  "translation_model_overrides": {
    "vi": "uuid-vi-model",
    "th": "uuid-th-model"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| needs_translation | boolean | 否 | 是否需要翻译 |
| source_locale | string | 否 | 源语言 |
| translation_model_id | uuid | 否 | 字段级翻译模型 |
| translation_model_overrides | object | 否 | 语言级模型覆盖，key=locale，value=model_id |

### 校验
- 字段类型必须是 text/varchar/jsonb（否则返回 40011）
- source_locale 必须是已注册的 locale_code
- translation_model_id 必须是有效的翻译模型 ID

### 业务逻辑
1. UPSERT `i18n_field_config`，标记 is_manually_set=true
2. 如果从 false 改为 true：为该字段的所有记录×所有已启用语言创建 pending 翻译记录
3. 如果 source_locale 变更：原翻译记录全部回退为 pending

### 模型优先级解析

翻译时模型选择按以下优先级：
1. **语言级**：`translation_model_overrides[locale]` 不为空 → 使用该模型
2. **字段级**：`translation_model_id` 不为空 → 使用该模型
3. **表级**：`i18n_table_config.default_translation_model_id` → 使用表级默认
4. **全局默认**：`i18n_translation_models` 中 `is_default=true` 的模型

### Response 200

```json
{
  "data": {
    "table_name": "courses",
    "field_name": "title",
    "needs_translation": true,
    "source_locale": "zh",
    "translation_model_id": "uuid",
    "translation_model_overrides": { "vi": "uuid-vi-model" },
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
| status | string | 否 | 状态筛选：pending / translated |
| search | string | 否 | 按原文内容搜索 |
| page | integer | 否 | 页码，默认 1 |
| page_size | integer | 否 | 每页条数，默认 50 |

### 业务逻辑
1. 从业务表读取该字段的原始值（source text）
2. 左连接 `i18n_content_translations` 获取翻译
3. 界面显示为源语言（中文）与目标语言的对照
4. 分页返回

### Response 200

```json
{
  "data": {
    "field_config": {
      "source_locale": "zh",
      "translation_model_id": "uuid",
      "translation_model_name": "GPT-4o",
      "translation_model_overrides": { "vi": "uuid-vi-model" }
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
          "translation_model_id": "uuid",
          "last_translated_at": "2026-05-29T10:00:00Z"
        }
      }
    ],
    "pagination": { "page": 1, "page_size": 50, "total": 50 },
    "stats": { "pending": 5, "translated": 45 }
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

### 业务逻辑
1. 更新翻译内容
2. status 保持 translated（手动编辑不改变状态）
3. translated_by 设为当前管理员 user_id

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "translated_text": "Beginner Chinese Course",
    "status": "translated"
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
  "scope": "field",
  "table_name": "courses",
  "field_name": "title",
  "target_locales": ["en", "vi"],
  "status_filter": ["pending"],
  "model_id": "uuid"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| scope | string | 是 | `all` / `table` / `field` |
| table_name | string | 否 | scope=table/field 时必填 |
| field_name | string | 否 | scope=field 时必填 |
| target_locales | string[] | 否 | 空=所有已启用语言 |
| status_filter | string[] | 否 | 默认 pending |
| model_id | uuid | 否 | 指定翻译模型，为空时按优先级解析 |

### 业务逻辑
1. 模型解析（按优先级）：
   - 请求中指定 model_id → 直接使用
   - 按 field_config 的 translation_model_overrides[locale] → 语言级覆盖
   - 按 field_config 的 translation_model_id → 字段级模型
   - 按 table_config 的 default_translation_model_id → 表级默认
   - 按 i18n_translation_models 的 is_default=true → 全局默认
   - 以上均无 → 返回 40013
2. 检查是否有同范围的运行中任务（避免重复）
3. 创建 i18n_translation_tasks 记录（task_type=content，携带 model_id、scope_filter）
4. 异步执行翻译（枢纽语言链）：
   a. 对于非英文目标语言，先检查英文翻译是否存在
   b. 英文翻译不存在 → 先生成英文翻译
   c. 从英文翻译到目标语言
5. 每完成一条更新任务进度

### Response 202

```json
{
  "data": {
    "task_id": "uuid",
    "total_items": 100,
    "status": "queued",
    "model_id": "uuid"
  }
}
```
