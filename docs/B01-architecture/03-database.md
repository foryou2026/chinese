# 数据库规范

> **阶段**：B01-A 技术架构
> **角色**：架构师
> **归属**：共享
> **系统**：全局
> **模块**：全局
> **功能**：全局
> **上游依赖**：01-tech-stack
> **冻结状态**：✅ 已冻结

---

## 命名规则

| 对象 | 规则 | 示例 |
|------|------|------|
| 表名 | snake_case 复数 | `user_profiles`, `order_items` |
| 字段名 | snake_case | `display_name`, `created_at` |
| 主键 | `id` | `id` |
| 外键 | `<被引用表单数>_id` | `user_id`, `category_id` |
| 索引 | `idx_<表名>_<字段>` | `idx_user_profiles_email` |
| 唯一索引 | `uniq_<表名>_<字段>` | `uniq_user_profiles_email` |
| 枚举值 | snake_case | `draft`, `published`, `in_progress` |
| 布尔字段 | `is_` / `has_` / `can_` 前缀 | `is_active`, `has_verified` |
| 时间字段 | `_at` 后缀 | `created_at`, `published_at` |
| i18n 字段 | `_i18n` 后缀，JSONB 类型 | `title_i18n`, `name_i18n` |

## 通用字段

> 后续根据页面确定具体业务字段。以下为每张表推荐携带的基础字段。

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | uuid | 主键，默认 `gen_random_uuid()` |
| created_at | timestamptz | 创建时间，默认 `now()` |
| updated_at | timestamptz | 更新时间，默认 `now()`，触发器自动更新 |
| created_by | uuid | 创建者，引用 `auth.users(id)`，可空 |
| updated_by | uuid | 最后修改者，可空 |

## 主键策略

AI 推荐：**UUID v7**

| 项目 | 决定 |
|------|------|
| 类型 | uuid |
| 生成方式 | 数据库端 `gen_random_uuid()`（PG 内置），应用层使用 uuid v7 库 |
| 理由 | 有序（时间排序友好）、分布式安全、无自增暴露 |

> PostgreSQL 17 原生支持 UUIDv7 `uuidv7()`。若 PG 版本 < 17，使用扩展 `pg_uuidv7` 或应用层生成。

## 软删除策略

AI 推荐：**deleted_at 时间戳**

| 项目 | 决定 |
|------|------|
| 字段 | `deleted_at timestamptz DEFAULT NULL` |
| 查询约定 | 默认查询追加 `WHERE deleted_at IS NULL` |
| Drizzle 层 | 使用 `.$defaultFn()` 或查询 helper 统一过滤 |
| 硬删除 | 仅在数据保留期过期后由定时任务执行 |
| 适用范围 | 业务数据表；日志/审计表不做软删除 |

## 迁移策略

| 项目 | 决定 |
|------|------|
| 工具 | Drizzle Kit (`drizzle-kit`) |
| 迁移目录 | `system/apps/api-server/src/db/migrations/` |
| Git 留痕 | `system/supabase/migrations/` 同步存放带时间戳 SQL |
| 执行方式 | 开发环境通过 `drizzle-kit push` 或 `drizzle-kit migrate` |
| 回滚 | 编写对应 down 迁移，禁止手动修改已执行迁移 |

## 索引策略

| 规则 | 说明 |
|------|------|
| 外键字段 | 自动创建索引 |
| 高频查询字段 | 按实际查询模式添加 |
| 复合索引 | 遵循最左前缀原则 |
| JSONB 字段 | 按需使用 GIN 索引 |
| 软删除 | `WHERE deleted_at IS NULL` 部分索引 |

## 字符集与排序

| 项目 | 决定 |
|------|------|
| 字符集 | UTF-8 |
| 排序规则 | `en_US.utf8`（Supabase 默认） |
| i18n 文本 | JSONB 存储，应用层按语言取值 |

## RLS 铁律

| 规则 | 说明 |
|------|------|
| 新表第一条语句 | `ALTER TABLE <table> ENABLE ROW LEVEL SECURITY;` |
| 默认策略 | `auth.uid() = user_id` 行级隔离 |
| 公开表 | 必须显式确认后方可开放 anon 访问 |
| admin 表 | 使用 `auth.jwt() ->> 'role' = 'admin'` 限制 |

---

## 99. 待确认问题

无
