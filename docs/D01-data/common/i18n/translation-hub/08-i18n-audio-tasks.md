# i18n_audio_tasks

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-060, R-i18n-061, R-i18n-062 |
| 业务定义 | TTS 配音批次任务（独立于翻译任务） |
| 状态机 | SM-i18n-003 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| scope_description | text | 是 | 无 | 否 | 范围描述 | 如"课程表 · title" |
| target_locales | text[] | 是 | 无 | 否 | 目标语言列表 | locale_code 数组 |
| scope_filter | jsonb | 否 | null | 否 | 范围过滤条件 | 如 {scope:"field", table_name:"courses", field_name:"title"} |
| model_id | uuid | 否 | null | 否 | 使用的音色模型 | 引用 i18n_tts_models(id) |
| status | text | 是 | 'queued' | 否 | 任务状态 | 枚举:task_status_enum |
| total_items | integer | 是 | 0 | 否 | 总条目数 | — |
| completed_items | integer | 是 | 0 | 否 | 已完成数 | — |
| failed_items | integer | 是 | 0 | 否 | 失败条目数 | — |
| error_details | jsonb | 否 | null | 否 | 失败详情 | [{item_id, error_msg}] |
| started_at | timestamptz | 否 | null | 否 | 开始执行时间 | — |
| completed_at | timestamptz | 否 | null | 否 | 完成时间 | — |
| created_by | uuid | 是 | 无 | 否 | 创建人 | 管理员 user_id |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - 与翻译任务完全独立的表，遵循配音模块解耦原则。

### scope_description 生成规则

| scope 类型 | scope_filter | 生成文案 |
|-----------|-------------|---------|
| 全局 | `{scope:"all"}` | `全部` |
| 按表 | `{scope:"table", table_name:"courses"}` | `课程表 · 全部字段` |
| 按字段 | `{scope:"field", table_name:"courses", field_name:"title"}` | `课程表 · title` |
| 按语言 | `{scope:"language", locale:"en"}` | `全部 · 英语` |

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_tts_models | N:1 | model_id | SET NULL |
