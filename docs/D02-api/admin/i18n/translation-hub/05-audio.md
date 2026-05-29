# 配音管理接口

> **说明**：本文件覆盖配音（TTS/dubbing）全部接口，包含配音接口配置（R-i18n-060~062）、配音数据表/字段配置（R-i18n-051~052）、音色管理（R-i18n-054~055）、配音生成（R-i18n-053）、配音任务（R-i18n-056~058）。
> 1.1.6 起配音与翻译完全解耦：翻译接口配置见 `06-translation-api.md`（P-009），配音接口配置独立页面（P-011）。

---

## API-i18n-audio-switch 配音模块全局开关

```
PATCH /api/v1/admin/i18n/audio/switch
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

## 配音接口配置（P-011 配音接口配置页）

### API-i18n-audio-config-get 获取配音接口配置

> **R-ID**：R-i18n-060

```
GET /api/v1/admin/i18n/audio/api/config
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 返回当前配音 TTS 接口的全局配置
2. API Key 脱敏返回（仅显示末 4 位）

### Response 200

```json
{
  "data": {
    "provider_name": "自建 TTS 服务",
    "api_endpoint": "https://tts.example.com/v1/speech",
    "api_key_masked": "****abcd",
    "request_template": {
      "model": "tts-1",
      "response_format": "mp3"
    },
    "is_configured": true,
    "last_tested_at": "2026-05-29T10:00:00Z",
    "test_status": "success"
  }
}
```

---

### API-i18n-audio-config-save 保存配音接口配置

> **R-ID**：R-i18n-060

```
PUT /api/v1/admin/i18n/audio/api/config
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_name": "自建 TTS 服务",
  "api_endpoint": "https://tts.example.com/v1/speech",
  "api_key": "sk-xxxxx",
  "request_template": {
    "model": "tts-1",
    "response_format": "mp3"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_name | string | 是 | 自定义供应商名称（如"自建 TTS 服务"） |
| api_endpoint | string | 是 | TTS API 端点 URL |
| api_key | string | 否 | API Key，为空时保留已有值 |
| request_template | object | 否 | 请求参数模板（JSON），按供应商自定义 |

### 业务逻辑
1. api_key 加密存储（AES-256）
2. 不硬编码任何供应商平台，完全自定义（Dify 风格）
3. UPSERT 全局配置记录

### Response 200

```json
{
  "data": {
    "provider_name": "自建 TTS 服务",
    "api_endpoint": "https://tts.example.com/v1/speech",
    "is_configured": true
  }
}
```

---

### API-i18n-audio-config-test 配音接口连通测试

> **R-ID**：R-i18n-062

```
POST /api/v1/admin/i18n/audio/api/test
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "text": "你好世界",
  "voice_id": "alloy"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| text | string | 否 | 测试文本，默认"你好世界" |
| voice_id | string | 否 | 指定音色 ID，不传则使用默认 |

### 业务逻辑
1. 使用已保存的配置发起真实 TTS 调用
2. 返回生成的音频 URL 供试听
3. 更新 last_tested_at 与 test_status

### Response 200

```json
{
  "data": {
    "success": true,
    "audio_url": "https://storage.example.com/audio/test-xxx.mp3",
    "duration_ms": 1500,
    "latency_ms": 820
  }
}
```

### Error 42202

```json
{
  "error": { "code": 42202, "message": "配音接口连接测试失败" }
}
```

---

## 音色管理

### API-i18n-voice-list 音色列表

> **R-ID**：R-i18n-054

```
GET /api/v1/admin/i18n/audio/voices
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "locale": "en",
      "locale_name_zh": "英语",
      "voice_id": "alloy",
      "voice_name": "Alloy（自然女声）",
      "extra_params": { "speed": 1.0 },
      "created_at": "2026-05-29T10:00:00Z"
    }
  ]
}
```

---

### API-i18n-voice-upsert 配置语言音色

> **R-ID**：R-i18n-054

```
PUT /api/v1/admin/i18n/audio/voices/:locale
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "voice_id": "alloy",
  "voice_name": "Alloy（自然女声）",
  "extra_params": { "speed": 1.0 }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| voice_id | string | 是 | TTS 供应商的音色标识 |
| voice_name | string | 否 | 可读名称，用于管理界面展示 |
| extra_params | object | 否 | 该语言的音色附加参数 |

### 业务逻辑
1. UPSERT 按 locale 维度的音色配置
2. 校验 locale 必须是已注册的 locale_code

### Response 200

```json
{
  "data": { "locale": "en", "voice_id": "alloy", "voice_name": "Alloy（自然女声）" }
}
```

---

### API-i18n-voice-delete 删除语言音色

> **R-ID**：R-i18n-054

```
DELETE /api/v1/admin/i18n/audio/voices/:locale
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 删除指定语言的音色配置
2. 已生成的配音文件不受影响

### Response 200

```json
{
  "data": { "deleted": true, "locale": "en" }
}
```

---

### API-i18n-voice-test 音色试听测试

> **R-ID**：R-i18n-054

```
POST /api/v1/admin/i18n/audio/voices/test
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "text": "Hello, this is a voice test.",
  "voice_id": "alloy",
  "extra_params": { "speed": 1.0 }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| text | string | 是 | 试听文本 |
| voice_id | string | 是 | 要测试的音色 ID |
| extra_params | object | 否 | 附加参数 |

### Response 200

```json
{
  "data": {
    "audio_url": "https://storage.example.com/audio/voice-test-xxx.mp3",
    "duration_ms": 2000
  }
}
```

---

## 配音数据表/字段配置（R-i18n-051~052）

> **说明**：配音的数据表/字段配置独立于翻译配置。管理员可单独指定哪些表/字段需要配音。

### API-i18n-audio-tables-list 配音数据表列表

> **R-ID**：R-i18n-051

```
GET /api/v1/admin/i18n/audio/tables
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 查询所有已启用翻译的表
2. 左连接配音配置，返回各表的配音启用状态
3. 聚合配音覆盖率

### Response 200

```json
{
  "data": [
    {
      "table_name": "courses",
      "table_description": "课程表",
      "audio_enabled": true,
      "audio_field_count": 2,
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

### API-i18n-audio-table-config 表级配音配置

> **R-ID**：R-i18n-051

```
PATCH /api/v1/admin/i18n/audio/tables/:tableName
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "audio_enabled": true
}
```

### 业务逻辑
1. UPSERT 配音表级配置
2. 仅已启用翻译的表才可启用配音
3. 启用时不自动为所有字段开启配音（需逐字段配置）

### Response 200

```json
{
  "data": { "table_name": "courses", "audio_enabled": true }
}
```

---

### API-i18n-audio-field-config 字段级配音配置

> **R-ID**：R-i18n-052

```
PATCH /api/v1/admin/i18n/audio/tables/:tableName/fields/:fieldName
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "needs_audio": true
}
```

### 校验
- 字段必须已启用翻译（`needs_translation=true`）
- 表级配音必须已启用

### 业务逻辑
1. UPSERT 配音字段级配置
2. 启用后不自动触发配音生成，需手动或通过任务触发

### Response 200

```json
{
  "data": {
    "table_name": "courses",
    "field_name": "title",
    "needs_audio": true
  }
}
```

---

## 配音生成与文件管理

### API-i18n-audio-generate 触发配音生成

> **R-ID**：R-i18n-053

```
POST /api/v1/admin/i18n/audio/generate
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
  "only_missing": true
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| scope | string | 是 | `all` / `table` / `field` |
| table_name | string | 否 | scope=table/field 时必填 |
| field_name | string | 否 | scope=field 时必填 |
| target_locales | string[] | 否 | 空=所有已配置音色的语言 |
| only_missing | boolean | 否 | 仅生成缺失的配音，默认 true |

### 前置校验
- 配音接口必须已配置且测试通过
- 目标语言必须已配置音色
- 目标字段必须已标记 needs_audio=true
- 目标记录必须有对应语言的已翻译内容
- 检查是否有同范围的运行中配音任务（幂等保护）

### 业务逻辑
1. 创建配音任务记录（i18n_audio_tasks），状态 queued
2. 异步执行 TTS 调用，逐条生成配音
3. 每完成一条更新任务进度
4. 任务可在配音任务列表页（P-010）查看

### Response 202

```json
{
  "data": {
    "task_id": "uuid",
    "total_items": 30,
    "status": "queued"
  }
}
```

---

### API-i18n-audio-files-list 配音文件列表

> **R-ID**：R-i18n-053

```
GET /api/v1/admin/i18n/audio/files
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| table_name | string | 否 | 按表筛选 |
| field_name | string | 否 | 按字段筛选 |
| locale | string | 否 | 按语言筛选 |
| status | string | 否 | 按状态筛选 |
| search | string | 否 | 按中文原文搜索 |
| page | integer | 否 | 页码 |
| page_size | integer | 否 | 每页条数 |

### Response 200

```json
{
  "data": {
    "items": [
      {
        "id": "uuid",
        "table_name": "courses",
        "record_id": "uuid",
        "field_name": "title",
        "locale": "en",
        "source_text_zh": "入门中文课程",
        "translated_text": "Beginner Chinese Course",
        "audio_url": "https://storage.example.com/audio/xxx.mp3",
        "duration_ms": 2500,
        "file_size_bytes": 45000,
        "audio_format": "mp3",
        "source": "ai",
        "status": "completed"
      }
    ],
    "pagination": { "page": 1, "page_size": 50, "total": 30 }
  }
}
```

---

### API-i18n-audio-upload 手动上传配音

> **R-ID**：R-i18n-055

```
POST /api/v1/admin/i18n/audio/files/:id/upload
Authorization: Bearer {jwt}
Content-Type: multipart/form-data
```

### Request Body

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| file | File | 是 | mp3/wav/ogg 文件 |

### 业务逻辑
1. 上传到对象存储
2. 更新 audio_url、duration_ms、file_size_bytes
3. source 设为 manual
4. status 设为 completed

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "audio_url": "https://storage.example.com/audio/xxx.mp3",
    "source": "manual",
    "status": "completed"
  }
}
```

---

## 配音任务（P-010 配音任务列表页）

### API-i18n-audio-tasks-list 配音任务列表

> **R-ID**：R-i18n-056

```
GET /api/v1/admin/i18n/audio/tasks
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
        "scope_description": "courses 表 → en",
        "target_locales": ["en"],
        "status": "running",
        "total_items": 30,
        "completed_items": 18,
        "failed_items": 0,
        "progress": 0.60,
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

---

### API-i18n-audio-task-detail 配音任务详情

> **R-ID**：R-i18n-057

```
GET /api/v1/admin/i18n/audio/tasks/:id
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "scope_description": "courses 表 → en",
    "scope_filter": { "table_name": "courses" },
    "target_locales": ["en"],
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
    "created_at": "2026-05-29T10:00:00Z",
    "started_at": "2026-05-29T10:00:01Z",
    "completed_at": "2026-05-29T10:03:45Z",
    "duration_seconds": 224
  }
}
```

---

### API-i18n-audio-task-cancel 取消配音任务

> **R-ID**：R-i18n-058

```
POST /api/v1/admin/i18n/audio/tasks/:id/cancel
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
