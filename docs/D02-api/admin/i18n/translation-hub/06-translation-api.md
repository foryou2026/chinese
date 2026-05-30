# 翻译接口管理（多供应商多模型）

> **说明**：本文件覆盖翻译接口配置相关接口（R-i18n-045~047）。
> 翻译接口支持多供应商多模型架构：供应商列表（P-009）→ 供应商详情（P-012，含模型管理）。
> 不硬编码任何具体平台，完全自定义（Dify 风格）。

---

## 供应商管理

### API-i18n-trans-providers-list 翻译供应商列表

> **R-ID**：R-i18n-045

```
GET /api/v1/admin/i18n/translation-api/providers
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "provider_name": "OpenAI",
      "api_endpoint": "https://api.openai.com/v1/chat/completions",
      "api_key_masked": "****abcd",
      "is_active": true,
      "model_count": 3,
      "sort_order": 1,
      "last_tested_at": "2026-05-29T10:00:00Z",
      "test_status": "success",
      "created_at": "2026-05-20T08:00:00Z"
    }
  ]
}
```

---

### API-i18n-trans-provider-create 新增翻译供应商

> **R-ID**：R-i18n-045

```
POST /api/v1/admin/i18n/translation-api/providers
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_name": "OpenAI",
  "api_endpoint": "https://api.openai.com/v1/chat/completions",
  "api_key": "sk-xxxxx",
  "translation_prompt": "你是一个专业的中文教育内容翻译专家。请将以下内容翻译为{target_language}，保持教育术语的准确性。",
  "is_active": true,
  "sort_order": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_name | string | 是 | 供应商名称 |
| api_endpoint | string | 是 | API 端点 URL |
| api_key | string | 是 | API Key（AES-256 加密存储） |
| translation_prompt | string | 否 | 翻译提示词模板，支持 `{target_language}` 占位符 |
| is_active | boolean | 否 | 是否启用，默认 true |
| sort_order | integer | 否 | 排序 |

### 业务逻辑
1. api_key 加密存储（AES-256）
2. 创建供应商记录

### Response 201

```json
{
  "data": {
    "id": "uuid",
    "provider_name": "OpenAI",
    "api_endpoint": "https://api.openai.com/v1/chat/completions",
    "is_active": true
  }
}
```

---

### API-i18n-trans-provider-get 翻译供应商详情

> **R-ID**：R-i18n-046

```
GET /api/v1/admin/i18n/translation-api/providers/:id
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 返回供应商基础信息（API Key 脱敏）
2. 包含该供应商下的所有模型列表

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "provider_name": "OpenAI",
    "api_endpoint": "https://api.openai.com/v1/chat/completions",
    "api_key_masked": "****abcd",
    "translation_prompt": "你是一个专业的中文教育内容翻译专家...",
    "is_active": true,
    "sort_order": 1,
    "last_tested_at": "2026-05-29T10:00:00Z",
    "test_status": "success",
    "models": [
      {
        "id": "uuid",
        "model_name": "GPT-4o",
        "model_id": "gpt-4o",
        "extra_params": { "temperature": 0.3, "max_tokens": 4096 },
        "is_default": true,
        "is_active": true,
        "sort_order": 1
      },
      {
        "id": "uuid",
        "model_name": "GPT-4o-mini",
        "model_id": "gpt-4o-mini",
        "extra_params": { "temperature": 0.3 },
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

### API-i18n-trans-provider-update 更新翻译供应商

> **R-ID**：R-i18n-046

```
PUT /api/v1/admin/i18n/translation-api/providers/:id
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_name": "OpenAI",
  "api_endpoint": "https://api.openai.com/v1/chat/completions",
  "api_key": "sk-xxxxx",
  "translation_prompt": "...",
  "is_active": true,
  "sort_order": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_name | string | 否 | 供应商名称 |
| api_endpoint | string | 否 | API 端点 |
| api_key | string | 否 | 为空时保留已有值 |
| translation_prompt | string | 否 | 翻译提示词模板 |
| is_active | boolean | 否 | 是否启用 |
| sort_order | integer | 否 | 排序 |

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "provider_name": "OpenAI",
    "api_endpoint": "https://api.openai.com/v1/chat/completions",
    "is_active": true
  }
}
```

---

### API-i18n-trans-provider-delete 删除翻译供应商

> **R-ID**：R-i18n-045

```
DELETE /api/v1/admin/i18n/translation-api/providers/:id
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 检查该供应商下是否有模型正在被 field_config / table_config 引用
2. 有引用 → 返回 40015
3. 无引用 → 级联删除供应商及其所有模型

### Response 200

```json
{
  "data": { "deleted": true }
}
```

### Error 40015

```json
{
  "error": { "code": 40015, "message": "该供应商有模型正在被使用，无法删除" }
}
```

---

## 模型管理

### API-i18n-trans-models-list 翻译模型列表

> **R-ID**：R-i18n-046

```
GET /api/v1/admin/i18n/translation-api/providers/:id/models
Authorization: Bearer {jwt}
```

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "provider_id": "uuid",
      "model_name": "GPT-4o",
      "model_id": "gpt-4o",
      "extra_params": { "temperature": 0.3, "max_tokens": 4096 },
      "is_default": true,
      "is_active": true,
      "sort_order": 1,
      "created_at": "2026-05-20T08:00:00Z"
    }
  ]
}
```

---

### API-i18n-trans-model-create 新增翻译模型

> **R-ID**：R-i18n-046

```
POST /api/v1/admin/i18n/translation-api/providers/:id/models
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "model_name": "GPT-4o",
  "model_id": "gpt-4o",
  "extra_params": { "temperature": 0.3, "max_tokens": 4096 },
  "is_default": false,
  "is_active": true,
  "sort_order": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| model_name | string | 是 | 模型显示名称 |
| model_id | string | 是 | 模型技术标识（如 gpt-4o） |
| extra_params | object | 否 | 模型额外参数 |
| is_default | boolean | 否 | 是否全局默认模型，默认 false |
| is_active | boolean | 否 | 是否启用，默认 true |
| sort_order | integer | 否 | 排序 |

### 业务逻辑
1. (provider_id, model_id) 联合唯一校验
2. 如果 is_default=true，取消其他模型的默认标记

### Response 201

```json
{
  "data": {
    "id": "uuid",
    "model_name": "GPT-4o",
    "model_id": "gpt-4o",
    "is_default": false
  }
}
```

---

### API-i18n-trans-model-update 更新翻译模型

> **R-ID**：R-i18n-046

```
PUT /api/v1/admin/i18n/translation-api/models/:modelId
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "model_name": "GPT-4o",
  "extra_params": { "temperature": 0.5, "max_tokens": 8192 },
  "is_default": true,
  "is_active": true,
  "sort_order": 1
}
```

### 业务逻辑
1. 如果 is_default 从 false 改为 true，取消其他模型的默认标记
2. 不可修改 model_id（技术标识不变更）

### Response 200

```json
{
  "data": {
    "id": "uuid",
    "model_name": "GPT-4o",
    "is_default": true
  }
}
```

---

### API-i18n-trans-model-delete 删除翻译模型

> **R-ID**：R-i18n-046

```
DELETE /api/v1/admin/i18n/translation-api/models/:modelId
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 检查模型是否被 field_config / table_config 引用
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

### API-i18n-trans-test 翻译接口连通测试

> **R-ID**：R-i18n-047

```
POST /api/v1/admin/i18n/translation-api/test
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_id": "uuid",
  "model_id": "uuid",
  "text": "你好世界",
  "target_locale": "en"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_id | uuid | 是 | 指定供应商 |
| model_id | uuid | 否 | 指定模型，为空则使用默认 |
| text | string | 否 | 测试文本，默认"你好世界" |
| target_locale | string | 否 | 目标语言，默认 en |

### 业务逻辑
1. 使用指定供应商配置 + 模型参数发起真实翻译调用
2. 返回翻译结果供预览
3. 更新供应商的 last_tested_at 与 test_status

### Response 200

```json
{
  "data": {
    "success": true,
    "source_text": "你好世界",
    "translated_text": "Hello World",
    "target_locale": "en",
    "model_id": "gpt-4o",
    "latency_ms": 650
  }
}
```

### Error 42201

```json
{
  "error": { "code": 42201, "message": "翻译接口连接测试失败" }
}
```

---

## 全局模型查询

### API-i18n-all-models-list 全局翻译模型列表

> **R-ID**：R-i18n-017

```
GET /api/v1/admin/i18n/translation-api/all-models
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 聚合所有供应商下的已启用模型
2. 用于文案翻译/内容翻译页面的模型选择器下拉

### Response 200

```json
{
  "data": [
    {
      "id": "uuid",
      "model_name": "GPT-4o",
      "model_id": "gpt-4o",
      "provider_id": "uuid",
      "provider_name": "OpenAI",
      "is_default": true,
      "is_active": true
    },
    {
      "id": "uuid",
      "model_name": "Claude 3.5 Sonnet",
      "model_id": "claude-3-5-sonnet-20241022",
      "provider_id": "uuid",
      "provider_name": "Anthropic",
      "is_default": false,
      "is_active": true
    }
  ]
}
```
