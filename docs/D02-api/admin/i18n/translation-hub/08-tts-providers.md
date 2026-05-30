# TTS 配音接口管理（多供应商多模型）

> **说明**：本文件覆盖 TTS 配音接口配置相关接口（R-i18n-065~067）。
> TTS 接口支持多供应商架构：供应商列表（P-011）→ 供应商详情（P-017，含音色模型管理）。
> 不硬编码任何具体平台，完全自定义。

---

## 供应商管理

### API-i18n-tts-providers-list TTS 供应商列表

> **R-ID**：R-i18n-065

```
GET /api/v1/admin/i18n/tts-api/providers
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "provider_name": "OpenAI TTS",
      "api_endpoint": "https://api.openai.com/v1/audio/speech",
      "api_key_masked": "****abcd",
      "is_active": true,
      "model_count": 6,
      "sort_order": 1,
      "last_tested_at": "2026-05-29T10:00:00Z",
      "test_status": "success",
      "created_at": "2026-05-20T08:00:00Z"
    }
  ]
}
```

---

### API-i18n-tts-provider-create 新增 TTS 供应商

> **R-ID**：R-i18n-065

```
POST /api/v1/admin/i18n/tts-api/providers
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_name": "OpenAI TTS",
  "api_endpoint": "https://api.openai.com/v1/audio/speech",
  "api_key": "sk-xxxxx",
  "request_template": {
    "response_format": "mp3"
  },
  "is_active": true,
  "sort_order": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_name | string | 是 | 供应商名称 |
| api_endpoint | string | 是 | TTS API 端点 URL |
| api_key | string | 是 | API Key（AES-256 加密存储） |
| request_template | object | 否 | 请求参数模板（JSON），按供应商自定义 |
| is_active | boolean | 否 | 是否启用，默认 true |
| sort_order | integer | 否 | 排序 |

### Response 201

```json
{
  "data": {
    "id": "uuid",
    "provider_name": "OpenAI TTS",
    "api_endpoint": "https://api.openai.com/v1/audio/speech",
    "is_active": true
  }
}
```

---

### API-i18n-tts-provider-get TTS 供应商详情

> **R-ID**：R-i18n-066

```
GET /api/v1/admin/i18n/tts-api/providers/:id
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 返回供应商基础信息（API Key 脱敏）
2. 包含该供应商下的所有音色模型列表

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "provider_name": "OpenAI TTS",
    "api_endpoint": "https://api.openai.com/v1/audio/speech",
    "api_key_masked": "****abcd",
    "request_template": { "response_format": "mp3" },
    "is_active": true,
    "sort_order": 1,
    "last_tested_at": "2026-05-29T10:00:00Z",
    "test_status": "success",
    "models": [
      {
        "id": "uuid",
        "model_name": "Alloy（自然女声）",
        "voice_id": "alloy",
        "locale": null,
        "extra_params": { "speed": 1.0 },
        "output_format": "mp3",
        "is_default": true,
        "is_active": true,
        "sort_order": 1
      },
      {
        "id": "uuid",
        "model_name": "Nova（温暖女声）",
        "voice_id": "nova",
        "locale": null,
        "extra_params": { "speed": 1.0 },
        "output_format": "mp3",
        "is_default": false,
        "is_active": true,
        "sort_order": 2
      }
    ],
    "created_at": "2026-05-20T08:00:00Z",
    "updated_at": "2026-05-29T10:00:00Z"
  }
}
```

---

### API-i18n-tts-provider-update 更新 TTS 供应商

> **R-ID**：R-i18n-066

```
PUT /api/v1/admin/i18n/tts-api/providers/:id
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_name": "OpenAI TTS",
  "api_endpoint": "https://api.openai.com/v1/audio/speech",
  "api_key": "sk-xxxxx",
  "request_template": { "response_format": "mp3" },
  "is_active": true,
  "sort_order": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_name | string | 否 | 供应商名称 |
| api_endpoint | string | 否 | API 端点 |
| api_key | string | 否 | 为空时保留已有值 |
| request_template | object | 否 | 请求参数模板 |
| is_active | boolean | 否 | 是否启用 |
| sort_order | integer | 否 | 排序 |

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "provider_name": "OpenAI TTS",
    "is_active": true
  }
}
```

---

### API-i18n-tts-provider-delete 删除 TTS 供应商

> **R-ID**：R-i18n-065

```
DELETE /api/v1/admin/i18n/tts-api/providers/:id
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 检查供应商下是否有音色被 field_config / table_config 引用
2. 有引用 → 返回 40015
3. 无引用 → 级联删除供应商及其所有音色模型

### Response 200

```json
{
  "data": { "deleted": true }
}
```

### Error 40015

```json
{
  "error": { "code": 40015, "message": "该供应商有音色正在被使用，无法删除" }
}
```

---

## 音色模型管理（供应商详情页内）

### API-i18n-tts-models-list TTS 音色模型列表

> **R-ID**：R-i18n-066

```
GET /api/v1/admin/i18n/tts-api/providers/:id/models
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "provider_id": "uuid",
      "model_name": "Alloy（自然女声）",
      "voice_id": "alloy",
      "locale": null,
      "extra_params": { "speed": 1.0 },
      "output_format": "mp3",
      "is_default": true,
      "is_active": true,
      "sort_order": 1,
      "created_at": "2026-05-20T08:00:00Z"
    }
  ]
}
```

---

### API-i18n-tts-model-create 新增 TTS 音色模型

> **R-ID**：R-i18n-066

```
POST /api/v1/admin/i18n/tts-api/providers/:id/models
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "model_name": "Alloy（自然女声）",
  "voice_id": "alloy",
  "locale": null,
  "extra_params": { "speed": 1.0 },
  "output_format": "mp3",
  "is_default": false,
  "is_active": true,
  "sort_order": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| model_name | string | 是 | 音色显示名称 |
| voice_id | string | 是 | 供应商的音色技术标识 |
| locale | string | 否 | 适用语言，为空=通用音色 |
| extra_params | object | 否 | 额外参数 |
| output_format | string | 否 | 输出格式，默认 mp3 |
| is_default | boolean | 否 | 是否全局默认 |
| is_active | boolean | 否 | 是否启用，默认 true |
| sort_order | integer | 否 | 排序 |

### 业务逻辑
1. (provider_id, voice_id) 联合唯一校验
2. 如果 is_default=true，取消其他音色模型的默认标记

### Response 201

```json
{
  "data": {
    "id": "uuid",
    "model_name": "Alloy（自然女声）",
    "voice_id": "alloy"
  }
}
```

---

### API-i18n-tts-model-update 更新 TTS 音色模型

> **R-ID**：R-i18n-066

```
PUT /api/v1/admin/i18n/tts-api/models/:modelId
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "model_name": "Alloy（自然女声）",
  "locale": "en",
  "extra_params": { "speed": 1.2 },
  "output_format": "mp3",
  "is_default": true,
  "is_active": true,
  "sort_order": 1
}
```

### 业务逻辑
1. 不可修改 voice_id
2. 如果 is_default 从 false 改为 true，取消其他音色的默认标记

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "model_name": "Alloy（自然女声）",
    "is_default": true
  }
}
```

---

### API-i18n-tts-model-delete 删除 TTS 音色模型

> **R-ID**：R-i18n-066

```
DELETE /api/v1/admin/i18n/tts-api/models/:modelId
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 检查音色是否被引用
2. 有引用 → 返回 40015
3. 无引用 → 删除

### Response 200

```json
{
  "data": { "deleted": true }
}
```

---

## 接口测试

### API-i18n-tts-test TTS 接口连通测试

> **R-ID**：R-i18n-067

```
POST /api/v1/admin/i18n/tts-api/test
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_id": "uuid",
  "voice_id": "alloy",
  "text": "你好世界",
  "extra_params": { "speed": 1.0 }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_id | uuid | 是 | 指定 TTS 供应商 |
| voice_id | string | 是 | 指定音色 ID |
| text | string | 否 | 测试文本，默认"你好世界" |
| extra_params | object | 否 | 附加参数 |

### 业务逻辑
1. 使用指定供应商配置 + 音色参数发起真实 TTS 调用
2. 返回生成的音频 URL 供试听
3. 更新供应商的 last_tested_at 与 test_status

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

## 全局音色查询

### API-i18n-all-tts-models-list 全局音色模型列表

> **R-ID**：R-i18n-055

```
GET /api/v1/admin/i18n/tts-api/all-models
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 聚合所有 TTS 供应商下的已启用音色模型
2. 用于配音管理页面的音色选择器下拉

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "model_name": "Alloy（自然女声）",
      "voice_id": "alloy",
      "locale": null,
      "provider_id": "uuid",
      "provider_name": "OpenAI TTS",
      "is_default": true,
      "is_active": true
    }
  ]
}
```
