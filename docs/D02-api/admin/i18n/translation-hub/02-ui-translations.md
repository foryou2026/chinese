# 文案翻译接口

> **说明**：本文件覆盖 UI 文案翻译相关接口（R-i18n-010~016）。1.1.6 起"UI 文案翻译"统一简称为"文案翻译"。

## API-i18n-ui-sync 同步文案

```
POST /api/v1/admin/i18n/ui/sync
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 读取代码中 `packages/shared-i18n/src/zh.ts` 资源文件
2. 递归遍历所有 key，拼接为 `namespace.key.subkey` 格式
3. 与 `i18n_ui_entries` 表比对：
   - 新 key → INSERT，状态 pending
   - 已有 key 中文变化 → 更新 source_text_zh，关联翻译标记 outdated
   - 代码中删除的 key → is_deprecated=true
4. 为新 key 的每个已启用语言创建翻译记录（status=pending）

### Response 200

```json
{
  "data": {
    "added": 5,
    "updated": 2,
    "deprecated": 1,
    "total": 120
  }
}
```

---

## API-i18n-ui-list 文案列表

```
GET /api/v1/admin/i18n/ui/entries
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| locale | string | 否 | 目标语言，默认 en |
| namespace | string | 否 | 业务域筛选 |
| status | string | 否 | 翻译状态筛选 |
| search | string | 否 | 按 key 或中文搜索 |
| page | integer | 否 | 页码，默认 1 |
| page_size | integer | 否 | 每页条数，默认 50 |
| include_deprecated | boolean | 否 | 是否包含废弃条目，默认 false |

### Response 200

```json
{
  "data": {
    "items": [
      {
        "entry_id": "uuid",
        "key_path": "auth.login",
        "namespace": "auth",
        "source_text_zh": "登录",
        "translation": {
          "id": "uuid",
          "locale": "en",
          "translated_text": "Sign In",
          "status": "reviewed",
          "translated_by": "ai",
          "last_translated_at": "2026-05-29T10:00:00Z"
        }
      }
    ],
    "pagination": {
      "page": 1,
      "page_size": 50,
      "total": 120
    },
    "stats": {
      "pending": 15,
      "translated": 80,
      "reviewed": 20,
      "outdated": 5
    },
    "namespaces": ["common", "auth", "nav", "course"]
  }
}
```

---

## API-i18n-ui-update 更新 UI 翻译

```
PATCH /api/v1/admin/i18n/ui/translations/:id
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "translated_text": "Sign In"
}
```

### 业务逻辑
1. 更新翻译内容
2. status 变为 reviewed
3. translated_by 设为当前管理员 user_id
4. 记录审计日志

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "translated_text": "Sign In",
    "status": "reviewed"
  }
}
```

---

## API-i18n-ui-translate 触发文案 AI 翻译

```
POST /api/v1/admin/i18n/ui/translate
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "scope": "all",
  "target_locales": ["en", "vi"],
  "namespace": null,
  "status_filter": ["pending", "outdated"]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| scope | string | 是 | `all` / `namespace` / `selected` |
| target_locales | string[] | 否 | 目标语言，空=所有已启用语言 |
| namespace | string | 否 | scope=namespace 时必填 |
| status_filter | string[] | 否 | 仅翻译指定状态，默认 pending+outdated |
| entry_ids | string[] | 否 | scope=selected 时的条目 ID 列表 |

### 业务逻辑
1. 检查是否有同范围的运行中任务（避免重复）
2. 创建 i18n_translation_tasks 记录
3. 异步执行翻译：
   a. 先翻译 zh → en
   b. 再从 en 翻译到其他目标语言
4. 每完成一条更新进度

### Response 202

```json
{
  "data": {
    "task_id": "uuid",
    "total_items": 45,
    "status": "queued"
  }
}
```

---

## API-i18n-ui-publish 发布 UI 翻译

```
POST /api/v1/admin/i18n/ui/publish
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "target_locales": ["en", "vi"]
}
```

### 业务逻辑
1. 从 DB 读取所有 translated/reviewed 状态的翻译
2. 按语言生成对应的 TS 资源文件（如 `en.ts`、`vi.ts`）
3. 写入 `packages/shared-i18n/src/` 目录
4. 返回变更概览

### Response 200

```json
{
  "data": {
    "published_locales": ["en", "vi"],
    "changes": {
      "en": { "added": 5, "updated": 3, "total": 120 },
      "vi": { "added": 45, "updated": 0, "total": 120 }
    }
  }
}
```
