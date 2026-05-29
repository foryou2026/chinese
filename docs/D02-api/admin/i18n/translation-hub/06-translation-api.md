# 翻译接口配置

> **说明**：本文件覆盖翻译接口配置相关接口（R-i18n-045~046）。1.1.6 起翻译接口配置（P-009）与配音接口配置（P-011）完全解耦为独立页面。
> 翻译接口采用自定义供应商模式（Dify 风格），不硬编码任何具体平台。

---

## API-i18n-translation-config-get 获取翻译接口配置

> **R-ID**：R-i18n-045

```
GET /api/v1/admin/i18n/translation-api/config
Authorization: Bearer {jwt}
```

### 业务逻辑
1. 返回当前翻译接口的全局配置
2. API Key 脱敏返回（仅显示末 4 位）

### Response 200

```json
{
  "data": {
    "provider_name": "自建翻译服务",
    "api_endpoint": "https://translate.example.com/v1/translate",
    "api_key_masked": "****abcd",
    "request_template": {
      "model": "gpt-4o",
      "temperature": 0.3
    },
    "translation_prompt": "你是一个专业的中文教育内容翻译专家。请将以下中文翻译为{target_language}，保持教育术语的准确性。",
    "is_configured": true,
    "last_tested_at": "2026-05-29T10:00:00Z",
    "test_status": "success"
  }
}
```

---

## API-i18n-translation-config-save 保存翻译接口配置

> **R-ID**：R-i18n-045

```
PUT /api/v1/admin/i18n/translation-api/config
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "provider_name": "自建翻译服务",
  "api_endpoint": "https://translate.example.com/v1/translate",
  "api_key": "sk-xxxxx",
  "request_template": {
    "model": "gpt-4o",
    "temperature": 0.3
  },
  "translation_prompt": "你是一个专业的中文教育内容翻译专家。请将以下中文翻译为{target_language}，保持教育术语的准确性。"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| provider_name | string | 是 | 自定义供应商名称 |
| api_endpoint | string | 是 | 翻译 API 端点 URL |
| api_key | string | 否 | API Key，为空时保留已有值 |
| request_template | object | 否 | 请求参数模板（JSON），按供应商自定义 |
| translation_prompt | string | 否 | 翻译提示词模板，支持 `{target_language}` 占位符 |

### 业务逻辑
1. api_key 加密存储（AES-256）
2. 不硬编码任何供应商平台，完全自定义（Dify 风格）
3. UPSERT 全局配置记录
4. translation_prompt 为可选项，若填写则在 AI 翻译时作为系统提示词

### Response 200

```json
{
  "data": {
    "provider_name": "自建翻译服务",
    "api_endpoint": "https://translate.example.com/v1/translate",
    "is_configured": true
  }
}
```

---

## API-i18n-translation-test 翻译接口连通测试

> **R-ID**：R-i18n-046

```
POST /api/v1/admin/i18n/translation-api/test
Authorization: Bearer {jwt}
Content-Type: application/json
```

### Request Body

```json
{
  "text": "你好世界",
  "target_locale": "en"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| text | string | 否 | 测试文本，默认"你好世界" |
| target_locale | string | 否 | 目标语言，默认 en |

### 业务逻辑
1. 使用已保存的配置（含 translation_prompt）发起真实翻译调用
2. 返回翻译结果供预览
3. 更新 last_tested_at 与 test_status

### Response 200

```json
{
  "data": {
    "success": true,
    "source_text": "你好世界",
    "translated_text": "Hello World",
    "target_locale": "en",
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
