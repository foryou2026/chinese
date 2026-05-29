# i18n_audio_config

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-051 |
| 业务定义 | 各语言的 TTS 配音接口配置 |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| locale | text | 是 | 无 | 是 | 语言代码 | 已启用的 locale_code |
| api_type | text | 是 | 无 | 否 | TTS API 类型 | 枚举:tts_api_type_enum |
| api_endpoint | text | 是 | 无 | 否 | API 地址 | 合法 URL |
| api_key_encrypted | text | 是 | 无 | 否 | 加密的 API Key | 存储加密后的值 |
| voice_id | text | 否 | null | 否 | 语音 ID | TTS 服务的语音标识 |
| extra_params | jsonb | 否 | null | 否 | 附加参数 | 如语速、音调等 |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - api_key_encrypted 在数据库中加密存储，API 返回时脱敏。

## 关系

无物理外键。通过 locale 逻辑关联 i18n_languages。
