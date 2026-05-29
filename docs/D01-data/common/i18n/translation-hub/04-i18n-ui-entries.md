# i18n_ui_entries

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-010, R-i18n-011, R-i18n-012 |
| 业务定义 | UI 文案 key 注册表（从代码同步） |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| key_path | text | 是 | 无 | 是 | i18n key 路径 | 如 auth.login，snake_case |
| namespace | text | 是 | 无 | 否 | 业务域 | key 的一级前缀，如 auth/common |
| source_text_zh | text | 是 | 无 | 否 | 中文源文案 | 从 zh.ts 同步 |
| is_deprecated | boolean | 是 | false | 否 | 是否已废弃 | 代码中删除的 key 标记为 true |
| last_synced_at | timestamptz | 是 | now() | 否 | 最后同步时间 | — |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - key_path 从代码 `zh.ts` 资源文件中自动提取（嵌套 key 用 `.` 连接）。
> - namespace 自动从 key_path 的第一级提取。
> - 同步时：代码中新增的 key → 新建记录；代码中删除的 key → is_deprecated=true；中文内容变化 → 更新 source_text_zh 并标记关联翻译为 outdated。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_ui_translations | 1:N | entry_id | CASCADE |
