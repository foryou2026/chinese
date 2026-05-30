# 音色管理接口

> **说明**：本文件覆盖音色管理相关接口（R-i18n-056~058）。
> 音色管理为独立顶级菜单页（P-016），不嵌套在配音管理内。
> 音色数据来源于 `i18n_tts_models` 表。

---

## API-i18n-voice-list 音色列表

> **R-ID**：R-i18n-056

```
GET /api/v1/admin/i18n/voices
Authorization: Bearer {jwt}
```

### Query Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_id | uuid | 否 | 按供应商筛选 |
| locale | string | 否 | 按语言筛选 |
| is_active | boolean | 否 | 按启用状态筛选 |

### 业务逻辑
1. 聚合所有 TTS 供应商下的音色模型
2. 用于配音管理页面的音色选择器和独立音色管理页

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "provider_id": "uuid",
      "provider_name": "OpenAI TTS",
      "model_name": "Alloy（自然女声）",
      "voice_id": "alloy",
      "locale": "en",
      "locale_name_zh": "英语",
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

## API-i18n-voice-create 新增音色

> **R-ID**：R-i18n-057

```
POST /api/v1/admin/i18n/voices
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_id": "uuid",
  "model_name": "Alloy（自然女声）",
  "voice_id": "alloy",
  "locale": "en",
  "extra_params": { "speed": 1.0 },
  "output_format": "mp3",
  "is_default": false,
  "is_active": true,
  "sort_order": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_id | uuid | 是 | 所属 TTS 供应商 |
| model_name | string | 是 | 音色显示名称 |
| voice_id | string | 是 | 供应商的音色技术标识 |
| locale | string | 否 | 适用语言，为空=通用音色 |
| extra_params | object | 否 | 额外参数（速率、音调等） |
| output_format | string | 否 | 输出格式，默认 mp3 |
| is_default | boolean | 否 | 是否全局默认 |
| is_active | boolean | 否 | 是否启用，默认 true |
| sort_order | integer | 否 | 排序 |

### 业务逻辑
1. (provider_id, voice_id) 联合唯一校验
2. 如果 is_default=true，取消其他音色的默认标记
3. locale 为空表示通用音色，适用于所有语言

### Response 201

```json
{
  "data": {
    "id": "uuid",
    "model_name": "Alloy（自然女声）",
    "voice_id": "alloy",
    "provider_name": "OpenAI TTS"
  }
}
```

---

## API-i18n-voice-update 更新音色

> **R-ID**：R-i18n-057

```
PUT /api/v1/admin/i18n/voices/:id
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "model_name": "Alloy（自然女声）",
  "extra_params": { "speed": 1.2 },
  "output_format": "mp3",
  "is_default": true,
  "is_active": true,
  "sort_order": 1
}
```

### 业务逻辑
1. 不可修改 voice_id 和 provider_id
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

## API-i18n-voice-delete 删除音色

> **R-ID**：R-i18n-057

```
DELETE /api/v1/admin/i18n/voices/:id
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 检查音色是否被 field_config / table_config 引用
2. 有引用 → 返回 40015
3. 无引用 → 删除

### Response 200

```json
{
  "data": { "deleted": true }
}
```

### Error 40015

```json
{
  "error": { "code": 40015, "message": "该音色正在被使用，无法删除" }
}
```

---

## API-i18n-voice-test 音色试听测试

> **R-ID**：R-i18n-058

```
POST /api/v1/admin/i18n/voices/test
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_id": "uuid",
  "voice_id": "alloy",
  "text": "Hello, this is a voice test.",
  "extra_params": { "speed": 1.0 }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_id | uuid | 是 | 指定 TTS 供应商 |
| voice_id | string | 是 | 要测试的音色 ID |
| text | string | 是 | 试听文本 |
| extra_params | object | 否 | 附加参数 |

### 业务逻辑
1. 使用指定供应商配置 + 音色参数发起真实 TTS 调用
2. 返回生成的音频 URL 供试听

### Response 200

```json
{
  "data": {
    "audio_url": "https://storage.example.com/audio/voice-test-xxx.mp3",
    "duration_ms": 2000,
    "latency_ms": 820
  }
}
```
