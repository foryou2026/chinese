# i18n_translation_tasks

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-030, R-i18n-031, R-i18n-032 |
| 业务定义 | AI 翻译批次任务 |
| 状态机 | SM-i18n-002 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| task_type | text | 是 | 无 | 否 | 任务类型 | 枚举:translation_task_type_enum |
| scope_description | text | 是 | 无 | 否 | 范围描述 | 如"全局"、"auth 域"、"courses 表" |
| target_locales | text[] | 是 | 无 | 否 | 目标语言列表 | locale_code 数组 |
| scope_filter | jsonb | 否 | null | 否 | 范围过滤条件 | 如 {namespace:"auth"} 或 {table_name:"courses"} |
| status | text | 是 | 'queued' | 否 | 任务状态 | 枚举:translation_task_status_enum |
| total_items | integer | 是 | 0 | 否 | 总条目数 | — |
| completed_items | integer | 是 | 0 | 否 | 已完成数 | — |
| failed_items | integer | 是 | 0 | 否 | 失败条目数 | — |
| error_details | jsonb | 否 | null | 否 | 失败详情 | [{item_id, error_msg}] |
| started_at | timestamptz | 否 | null | 否 | 开始执行时间 | — |
| completed_at | timestamptz | 否 | null | 否 | 完成时间 | — |
| created_by | uuid | 是 | 无 | 否 | 创建人 | 管理员 user_id |

> - B01 通用字段 created_at/updated_at 按默认规则携带。

## 关系

无物理外键。
