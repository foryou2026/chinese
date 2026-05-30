# 语言管理与总览接口

> **说明**：本文件覆盖语言管理（R-i18n-001~003）、翻译总览（R-i18n-040）、配音总览（R-i18n-063）相关接口。

---

## API-i18n-dashboard 翻译总览

```
GET /api/v1/admin/i18n/dashboard
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": {
    "active_languages": 3,
    "ui_stats": {
      "total": 120,
      "by_status": {
        "pending": 15,
        "translated": 105
      }
    },
    "content_stats": {
      "total_fields": 8,
      "total_records": 500,
      "by_status": {
        "pending": 100,
        "translated": 400
      }
    },
    "by_language": [
      {
        "locale": "en",
        "name_zh": "英语",
        "is_pivot_language": true,
        "ui_coverage": 0.87,
        "content_coverage": 0.78,
        "pending_count": 20
      }
    ]
  }
}
```

---

## API-i18n-dubbing-dashboard 配音总览

```
GET /api/v1/admin/i18n/dubbing/dashboard
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 聚合所有已启用配音字段的音频覆盖率
2. 按语言维度统计配音完成度
3. 统计近期配音任务状态

### Response 200

```json
{
  "data": {
    "audio_enabled_fields": 5,
    "total_audio_items": 200,
    "by_status": {
      "pending": 30,
      "generated": 150,
      "failed": 5,
      "manual": 15
    },
    "by_language": [
      {
        "locale": "en",
        "name_zh": "英语",
        "total_items": 80,
        "generated_count": 65,
        "coverage": 0.81
      }
    ],
    "recent_tasks": [
      {
        "id": "uuid",
        "scope_description": "课程表 · title",
        "status": "completed",
        "completed_at": "2026-05-29T10:02:30Z"
      }
    ]
  }
}
```

---

## API-i18n-languages-list 语言列表

```
GET /api/v1/admin/i18n/languages
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| active_only | boolean | 否 | 仅返回已启用语言 |

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "locale_code": "zh",
      "name_zh": "中文",
      "name_native": "中文",
      "language_family": "east_asian",
      "is_active": true,
      "is_system_default": true,
      "is_pivot_language": false,
      "sort_order": 1,
      "text_direction": "ltr",
      "ui_coverage": 1.0,
      "content_coverage": 1.0
    },
    {
      "id": "uuid",
      "locale_code": "en",
      "name_zh": "英语",
      "name_native": "English",
      "language_family": "west_european",
      "is_active": true,
      "is_system_default": false,
      "is_pivot_language": true,
      "sort_order": 2,
      "text_direction": "ltr",
      "ui_coverage": 0.87,
      "content_coverage": 0.78
    }
  ]
}
```

---

## API-i18n-languages-update 更新语言配置

```
PATCH /api/v1/admin/i18n/languages/:id
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "is_active": true
}
```

### 业务逻辑
1. 校验受保护语言不可停用：
   - is_system_default=true（中文）→ 返回 40010
   - is_pivot_language=true（英文）→ 返回 40010
2. 启用语言时：为所有文案和已配置的翻译字段创建 pending 状态的翻译记录
3. 停用语言时：保留翻译记录，仅标记为不活跃

### Response 200

```json
{
  "data": { "id": "uuid", "locale_code": "vi", "is_active": true }
}
```

### Error 40010

```json
{
  "error": { "code": 40010, "message": "该语言为受保护语言（系统默认/枢纽语言），不可停用" }
}
```

---

## API-i18n-languages-reorder 排序语言

```
PUT /api/v1/admin/i18n/languages/order
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "order": ["uuid-zh", "uuid-en", "uuid-vi"]
}
```

### Response 200

```json
{
  "data": { "updated": 3 }
}
```
