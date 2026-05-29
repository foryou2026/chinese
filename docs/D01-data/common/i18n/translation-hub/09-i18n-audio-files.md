# i18n_audio_files

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-052, R-i18n-053 |
| 业务定义 | 配音音频文件记录 |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| table_name | text | 是 | 无 | 否 | 业务表名 | 同 i18n_content_translations |
| record_id | uuid | 是 | 无 | 否 | 原记录 ID | 业务表的主键值 |
| field_name | text | 是 | 无 | 否 | 字段名 | — |
| locale | text | 是 | 无 | 否 | 语言 | 已启用的 locale_code |
| audio_url | text | 否 | null | 否 | 音频文件 URL | 对象存储路径 |
| duration_ms | integer | 否 | null | 否 | 时长(毫秒) | — |
| file_size_bytes | integer | 否 | null | 否 | 文件大小 | — |
| audio_format | text | 是 | 'mp3' | 否 | 音频格式 | mp3/wav/ogg |
| source | text | 是 | 'ai' | 否 | 来源 | 'ai'=TTS生成, 'manual'=手动上传 |
| status | text | 是 | 'pending' | 否 | 状态 | 枚举:audio_status_enum |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - (table_name, record_id, field_name, locale) 联合唯一。
> - audio_url 指向 Supabase Storage 或其他对象存储。
> - 手动上传的音频 source='manual'，不会被重新生成覆盖。

## 关系

无物理外键。通过 (table_name, record_id, field_name) 逻辑关联 i18n_content_translations。
