# 配音管理接口

> **说明**：本文件覆盖配音管理相关接口。配音管理采用层级模式（表→字段→详情），与内容翻译结构一致。
> 配音文件嵌入字段详情页，不单独 Tab。音色管理已独立为 [07-voices.md](./07-voices.md)。配音接口配置见 [08-tts-providers.md](./08-tts-providers.md)。
> - R-i18n-050：配音模块开关
> - R-i18n-051~052：数据表/字段配音配置
> - R-i18n-053~055：配音生成/文件/上传
> - R-i18n-060~062：配音任务

---

## API-i18n-dubbing-switch 配音模块全局开关

```
PATCH /api/v1/admin/i18n/dubbing/switch
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "enabled": true
}
```

### 业务逻辑
1. 控制配音模块的全局启停
2. 关闭后所有配音相关页面入口隐藏，但不删除已有数据
3. 进行中的配音任务会继续执行至结束

### Response 200

```json
{
  "data": { "enabled": true }
}
```

---

## 配音数据表层级（P-008 配音管理 · 数据表列表）

### API-i18n-dubbing-tables-list 配音数据表列表

> **R-ID**：R-i18n-051

```
GET /api/v1/admin/i18n/dubbing/tables
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 查询所有已启用翻译的表
2. 左连接 `i18n_field_config` 获取 needs_audio=true 的字段数
3. 聚合 `i18n_audio_files` 计算配音覆盖率
4. 携带表级默认 TTS 模型信息

### Response 200

```json
{
  "data": [
    {
      "table_name": "courses",
      "table_description": "课程表",
      "translation_enabled": true,
      "audio_field_count": 2,
      "default_tts_model_id": "uuid",
      "default_tts_model_name": "Alloy",
      "total_record_count": 50,
      "audio_coverage": {
        "en": 0.70,
        "vi": 0.30
      }
    }
  ]
}
```

---

### API-i18n-dubbing-table-config 表级配音配置

> **R-ID**：R-i18n-051

```
PATCH /api/v1/admin/i18n/dubbing/tables/:tableName
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "default_tts_model_id": "uuid"
}
```

### 业务逻辑
1. 更新 `i18n_table_config.default_tts_model_id`
2. 仅已启用翻译的表才可配置配音

### Response 200

```json
{
  "data": {
    "table_name": "courses",
    "default_tts_model_id": "uuid"
  }
}
```

---

## 配音字段层级（P-014 配音管理 · 字段列表）

### API-i18n-dubbing-fields-list 配音字段列表

> **R-ID**：R-i18n-052

```
GET /api/v1/admin/i18n/dubbing/tables/:tableName/fields
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 查询该表下所有已启用翻译的字段
2. 返回每个字段的 needs_audio 状态
3. 聚合配音覆盖率
4. 携带字段级 TTS 模型信息

### Response 200

```json
{
  "data": {
    "table_config": {
      "default_tts_model_id": "uuid",
      "default_tts_model_name": "Alloy"
    },
    "fields": [
      {
        "field_name": "title",
        "needs_translation": true,
        "needs_audio": true,
        "tts_model_id": "uuid",
        "tts_model_name": "Alloy",
        "record_count": 50,
        "audio_coverage": { "en": 0.80, "vi": 0.40 }
      },
      {
        "field_name": "description",
        "needs_translation": true,
        "needs_audio": false,
        "tts_model_id": null,
        "tts_model_name": null,
        "record_count": 50,
        "audio_coverage": {}
      }
    ]
  }
}
```

---

### API-i18n-dubbing-field-config 字段级配音配置

> **R-ID**：R-i18n-053

```
PATCH /api/v1/admin/i18n/dubbing/tables/:tableName/fields/:fieldName
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "needs_audio": true,
  "tts_model_id": "uuid",
  "tts_model_overrides": {
    "en": "uuid-en-voice",
    "vi": "uuid-vi-voice"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| needs_audio | boolean | 否 | 是否需要配音 |
| tts_model_id | uuid | 否 | 字段级 TTS 音色模型 |
| tts_model_overrides | object | 否 | 语言级音色覆盖，key=locale，value=tts_model_id |

### 校验
- 字段必须已启用翻译（`needs_translation=true`），否则返回 40012

### 业务逻辑
1. UPSERT `i18n_field_config` 的配音相关字段
2. 启用后不自动触发配音生成，需手动或通过任务触发

### 音色模型优先级解析

配音时音色选择按以下优先级：
1. **语言级**：`tts_model_overrides[locale]` 不为空 → 使用该音色
2. **字段级**：`tts_model_id` 不为空 → 使用该音色
3. **表级**：`i18n_table_config.default_tts_model_id` → 使用表级默认
4. **全局默认**：`i18n_tts_models` 中 `is_default=true` 的音色

### Response 200

```json
{
  "data": {
    "table_name": "courses",
    "field_name": "title",
    "needs_audio": true,
    "tts_model_id": "uuid",
    "tts_model_overrides": { "en": "uuid-en-voice" }
  }
}
```

---

## 配音详情层级（P-015 配音管理 · 配音详情）

### API-i18n-dubbing-field-files 字段配音文件列表

> **R-ID**：R-i18n-054

```
GET /api/v1/admin/i18n/dubbing/tables/:tableName/fields/:fieldName/files
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| locale | string | 否 | 按语言筛选 |
| status | string | 否 | 按状态筛选：pending/generated/failed |
| source | string | 否 | 按来源筛选：ai/manual |
| search | string | 否 | 按原文内容搜索 |
| page | integer | 否 | 页码，默认 1 |
| page_size | integer | 否 | 每页条数，默认 50 |

### 业务逻辑
1. 查询该字段已翻译的所有记录
2. 左连接 `i18n_audio_files` 获取配音文件
3. 界面显示：源文 | 译文 | 配音播放器 | 状态
4. 分页返回

### Response 200

```json
{
  "data": {
    "field_config": {
      "needs_audio": true,
      "tts_model_id": "uuid",
      "tts_model_name": "Alloy",
      "tts_model_overrides": { "en": "uuid-en-voice" }
    },
    "items": [
      {
        "record_id": "uuid",
        "source_text": "入门中文课程",
        "translated_text": "Beginner Chinese Course",
        "locale": "en",
        "audio": {
          "id": "uuid",
          "audio_url": "https://storage.example.com/audio/xxx.mp3",
          "duration_ms": 2500,
          "file_size_bytes": 45000,
          "audio_format": "mp3",
          "source": "ai",
          "tts_model_id": "uuid",
          "status": "generated",
          "created_at": "2026-05-29T10:00:00Z"
        }
      },
      {
        "record_id": "uuid",
        "source_text": "高级中文课程",
        "translated_text": "Advanced Chinese Course",
        "locale": "en",
        "audio": null
      }
    ],
    "pagination": { "page": 1, "page_size": 50, "total": 50 },
    "stats": {
      "total": 50,
      "generated": 35,
      "pending": 10,
      "failed": 3,
      "manual": 2
    }
  }
}
```

---

### API-i18n-dubbing-upload 手动上传配音

> **R-ID**：R-i18n-054

```
POST /api/v1/admin/i18n/dubbing/files/:id/upload
Authorization: Bearer {jwt}
Content-Type: multipart/form-data
```

### Request Body

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| file | File | 是 | mp3/wav/ogg 文件 |

### 业务逻辑
1. 上传到对象存储
2. 更新/创建 `i18n_audio_files` 记录
3. 设置 audio_url、duration_ms、file_size_bytes
4. source 设为 manual，status 设为 generated
5. 手动上传的音频不会被自动生成覆盖

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "audio_url": "https://storage.example.com/audio/xxx.mp3",
    "source": "manual",
    "status": "generated"
  }
}
```

---

## 配音生成

### API-i18n-dubbing-generate 触发配音生成

> **R-ID**：R-i18n-055

```
POST /api/v1/admin/i18n/dubbing/generate
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "scope": "field",
  "table_name": "courses",
  "field_name": "title",
  "target_locales": ["en"],
  "model_id": "uuid",
  "only_missing": true
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| scope | string | 是 | `all` / `table` / `field` |
| table_name | string | 否 | scope=table/field 时必填 |
| field_name | string | 否 | scope=field 时必填 |
| target_locales | string[] | 否 | 空=所有已配置音色的语言 |
| model_id | uuid | 否 | 指定音色模型，为空时按优先级解析 |
| only_missing | boolean | 否 | 仅生成缺失的配音，默认 true |

### 前置校验
- 音色模型解析（按优先级）：请求 model_id > 语言级覆盖 > 字段级 > 表级 > 全局默认
- 解析失败 → 返回 40014
- 目标字段必须已标记 needs_audio=true
- 目标记录必须有对应语言的已翻译内容（status=translated）
- 检查是否有同范围的运行中配音任务（幂等保护）

### 业务逻辑
1. 创建 `i18n_audio_tasks` 记录，状态 queued
2. 异步执行 TTS 调用，逐条生成配音
3. 每完成一条更新任务进度
4. 跳过 source=manual 的记录（手动上传不覆盖）

### Response 202

```json
{
  "data": {
    "task_id": "uuid",
    "total_items": 30,
    "status": "queued",
    "model_id": "uuid"
  }
}
```

### Error 40014

```json
{
  "error": { "code": 40014, "message": "请先配置配音接口和音色模型" }
}
```

---

## 配音任务（P-010 配音任务列表页）

### API-i18n-dubbing-tasks-list 配音任务列表

> **R-ID**：R-i18n-060

```
GET /api/v1/admin/i18n/dubbing/tasks
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| status | string | 否 | 按状态筛选：queued/running/completed/partial/cancelled |
| page | integer | 否 | 页码，默认 1 |
| page_size | integer | 否 | 每页条数，默认 20 |

### Response 200

```json
{
  "data": {
    "items": [
      {
        "id": "uuid",
        "scope_description": "课程表 · title",
        "target_locales": ["en"],
        "model_id": "uuid",
        "model_name": "Alloy",
        "status": "running",
        "total_items": 30,
        "completed_items": 18,
        "failed_items": 0,
        "progress": 0.60,
        "created_by": "uuid",
        "created_at": "2026-05-29T10:00:00Z",
        "started_at": "2026-05-29T10:00:01Z",
        "completed_at": null,
        "duration_seconds": null
      }
    ],
    "pagination": { "page": 1, "page_size": 20, "total": 3 }
  }
}
```

### scope_description 显示规则

| scope 类型 | scope_filter 示例 | scope_description |
|-----------|------------------|-------------------|
| 全局 | `{scope:"all"}` | `全部` |
| 按表 | `{scope:"table", table_name:"courses"}` | `课程表 · 全部字段` |
| 按字段 | `{scope:"field", table_name:"courses", field_name:"title"}` | `课程表 · title` |
| 按语言 | `{scope:"language", locale:"en"}` | `全部 · 英语` |

---

### API-i18n-dubbing-task-detail 配音任务详情

> **R-ID**：R-i18n-061

```
GET /api/v1/admin/i18n/dubbing/tasks/:id
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "scope_description": "课程表 · title",
    "scope_filter": {
      "scope": "field",
      "table_name": "courses",
      "field_name": "title"
    },
    "target_locales": ["en"],
    "model_id": "uuid",
    "model_name": "Alloy",
    "provider_name": "OpenAI TTS",
    "status": "partial",
    "total_items": 30,
    "completed_items": 27,
    "failed_items": 3,
    "error_details": [
      {
        "record_id": "uuid",
        "field_name": "title",
        "locale": "en",
        "error": "TTS API rate limit exceeded"
      }
    ],
    "created_by": "uuid",
    "created_at": "2026-05-29T10:00:00Z",
    "started_at": "2026-05-29T10:00:01Z",
    "completed_at": "2026-05-29T10:03:45Z",
    "duration_seconds": 224
  }
}
```

---

### API-i18n-dubbing-task-cancel 取消配音任务

> **R-ID**：R-i18n-062

```
POST /api/v1/admin/i18n/dubbing/tasks/:id/cancel
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 仅 queued/running 状态可取消
2. 已完成的配音文件保留
3. 状态变为 cancelled

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "status": "cancelled",
    "completed_items": 18,
    "total_items": 30
  }
}
```
