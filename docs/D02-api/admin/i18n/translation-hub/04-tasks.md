# 翻译任务接口

> **说明**：本文件仅覆盖**翻译任务**（R-i18n-030~032）。配音任务为独立模块，详见 [05-audio.md](./05-audio.md)。

---

## API-i18n-tasks-list 翻译任务列表

```
GET /api/v1/admin/i18n/tasks
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| status | string | 否 | 按状态筛选：queued/running/completed/partial/cancelled |
| task_type | string | 否 | ui / content |
| page | integer | 否 | 页码，默认 1 |
| page_size | integer | 否 | 每页条数，默认 20 |

### Response 200

```json
{
  "data": {
    "items": [
      {
        "id": "uuid",
        "task_type": "ui",
        "scope_description": "文案 · auth域",
        "target_locales": ["en", "vi"],
        "model_id": "uuid",
        "model_name": "GPT-4o",
        "status": "running",
        "total_items": 45,
        "completed_items": 30,
        "failed_items": 0,
        "progress": 0.67,
        "created_by": "uuid",
        "created_at": "2026-05-29T10:00:00Z",
        "started_at": "2026-05-29T10:00:01Z",
        "completed_at": null,
        "duration_seconds": null
      }
    ],
    "pagination": { "page": 1, "page_size": 20, "total": 5 }
  }
}
```

### scope_description 显示规则

| scope 类型 | scope_filter 示例 | scope_description |
|-----------|------------------|-------------------|
| UI 文案 · 全局 | `{type:"ui", scope:"all"}` | `文案 · 全部` |
| UI 文案 · 按域 | `{type:"ui", scope:"namespace", namespace:"auth"}` | `文案 · auth域` |
| UI 文案 · 选中项 | `{type:"ui", scope:"selected", count:5}` | `文案 · 选中5条` |
| 内容 · 全局 | `{type:"content", scope:"all"}` | `内容 · 全部` |
| 内容 · 按表 | `{type:"content", scope:"table", table_name:"courses"}` | `课程表 · 全部字段` |
| 内容 · 按字段 | `{type:"content", scope:"field", table_name:"courses", field_name:"title"}` | `课程表 · title` |

---

## API-i18n-task-detail 任务详情

```
GET /api/v1/admin/i18n/tasks/:id
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "task_type": "content",
    "scope_description": "课程表 · title",
    "scope_filter": {
      "type": "content",
      "scope": "field",
      "table_name": "courses",
      "field_name": "title"
    },
    "target_locales": ["en", "vi"],
    "model_id": "uuid",
    "model_name": "GPT-4o",
    "provider_name": "OpenAI",
    "status": "partial",
    "total_items": 50,
    "completed_items": 47,
    "failed_items": 3,
    "error_details": [
      {
        "record_id": "uuid",
        "field_name": "title",
        "locale": "vi",
        "error": "AI API rate limit exceeded"
      }
    ],
    "created_by": "uuid",
    "created_at": "2026-05-29T10:00:00Z",
    "started_at": "2026-05-29T10:00:01Z",
    "completed_at": "2026-05-29T10:02:30Z",
    "duration_seconds": 149
  }
}
```

---

## API-i18n-task-cancel 取消任务

```
POST /api/v1/admin/i18n/tasks/:id/cancel
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 仅 queued/running 状态可取消
2. 已完成的翻译条目保留
3. 状态变为 cancelled

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "status": "cancelled",
    "completed_items": 30,
    "total_items": 45
  }
}
```
