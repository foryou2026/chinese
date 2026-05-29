# 语言管理接口

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
        "translated": 80,
        "reviewed": 20,
        "outdated": 5
      }
    },
    "content_stats": {
      "total_fields": 8,
      "total_records": 500,
      "by_status": {
        "pending": 100,
        "translated": 350,
        "reviewed": 40,
        "outdated": 10
      }
    },
    "by_language": [
      {
        "locale": "en",
        "name_zh": "英语",
        "ui_coverage": 0.87,
        "content_coverage": 0.78,
        "pending_count": 20
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
      "sort_order": 1,
      "text_direction": "ltr",
      "ui_coverage": 1.0,
      "content_coverage": 1.0
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
1. 校验 is_system_default=true 的语言不可停用
2. 启用语言时：为所有文案和已配置的翻译字段创建 pending 状态的翻译记录
3. 停用语言时：保留翻译记录，仅标记为不活跃

### Response 200

```json
{
  "data": { "id": "uuid", "locale_code": "en", "is_active": true }
}
```

### Error 40010

```json
{
  "error": { "code": 40010, "message": "中文为系统默认语言，不可停用" }
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
