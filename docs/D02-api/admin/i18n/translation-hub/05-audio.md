# 配音接口

## API-i18n-audio-config-list 配音接口列表

```
GET /api/v1/admin/i18n/audio/config
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
      "api_type": "openai_tts",
      "api_endpoint": "https://api.openai.com/v1/audio/speech",
      "api_key_masked": "sk-****abcd",
      "voice_id": "alloy",
      "extra_params": { "speed": 1.0 }
    }
  ]
}
```

---

## API-i18n-audio-config-upsert 配置配音接口

```
PUT /api/v1/admin/i18n/audio/config/:locale
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "api_type": "openai_tts",
  "api_endpoint": "https://api.openai.com/v1/audio/speech",
  "api_key": "sk-xxxxx",
  "voice_id": "alloy",
  "extra_params": { "speed": 1.0 }
}
```

### 业务逻辑
1. api_key 加密存储
2. 可选：调用 API 进行连通性测试

### Response 200

```json
{
  "data": { "locale": "en", "api_type": "openai_tts", "status": "configured" }
}
```

---

## API-i18n-audio-generate 触发配音生成

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
| target_locales | string[] | 否 | 空=所有已配置 TTS 的语言 |
| only_missing | boolean | 否 | 仅生成缺失的配音，默认 true |

### 前置校验
- 目标语言必须已配置 TTS 接口
- 目标字段必须已标记 needs_audio=true
- 目标记录必须有对应语言的已翻译内容

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

## API-i18n-audio-files-list 配音文件列表

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
        "source_text": "Beginner Chinese Course",
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

## API-i18n-audio-upload 手动上传配音

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
