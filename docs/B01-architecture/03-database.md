<!-- TARGET-PATH: docs/B01-architecture/03-database.md -->

# 03 · 数据库规范

> **阶段**：B01-A 架构  
> **角色**：架构师  
> **feature**：全局  
> **上游依赖**：`01-tech-stack.md`、`02-project-structure.md`  
> **冻结状态**：已冻结 · 2026-04-28  
> **下游影响**：所有 D01 D（建表）、D03 V（校验）；user memory `drizzle-jsonb.md` 已作废

---

## 0. 摘要

- DB：自托管 Supabase Postgres 16，schema `zhiyu`，工具链 = Supabase CLI + Supabase MCP，**不使用 ORM**。
- 主键 `id uuid` + `gen_random_uuid()`；通用字段 `created_at` / `updated_at` / `deleted_at`（仅"用户可生成且可恢复"表）。
- 多语言业务文案统一 jsonb `{zh,en,vi,th,id}`。
- 枚举用 `text + CHECK` 不用 PG enum。
- RLS 必开，每张 C 端表至少正/反例测试。
- 复杂事务封装为 Postgres RPC 函数。
- pgvector 默认不启用；非 AI 业务严禁 vector 列。

---

## 1. 命名规则

| 对象 | 规则 | 示例 |
|------|------|------|
| 表名 | `snake_case` 复数名词 | `users`、`course_lessons`、`game_sessions` |
| 关联表 | `表a_表b`（字典序）| `users_roles` |
| 字段名 | `snake_case` | `created_at`、`display_name` |
| 主键 | `id`（`uuid`，`gen_random_uuid()`）| `id uuid` |
| 外键 | `<引用表单数>_id` | `user_id`、`course_id` |
| 索引 | `idx_<表>_<字段...>` | `idx_users_email` |
| 唯一索引 | `uq_<表>_<字段...>` | `uq_users_email` |
| 外键约束 | `fk_<表>_<字段>` | `fk_orders_user_id` |
| RPC 函数 | `fn_<动词>_<对象>` | `fn_purchase_course`、`fn_calc_user_level` |
| 视图 | `v_<对象>` | `v_user_summary` |
| 触发器 | `tg_<表>_<时机>_<动作>` | `tg_users_before_update_set_updated_at` |
| 枚举值 | `lower_snake` 字符串 | `'pending'`、`'in_progress'` |
| 布尔字段 | `is_xxx` / `has_xxx` / `can_xxx` | `is_active`、`has_paid` |
| 时间戳字段 | `xxx_at`（`timestamptz`）| `published_at` |

---

## 2. 通用字段

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `id` | `uuid` | `gen_random_uuid()` | 主键 |
| `created_at` | `timestamptz` | `now()` | 创建时间 |
| `updated_at` | `timestamptz` | `now()` | 更新时间，由触发器自动维护 |
| `deleted_at` | `timestamptz` | `null` | 软删除标记，仅"用户可生成可恢复"表 |

`updated_at` 触发器统一函数 `set_updated_at()` 定义在 `supabase/migrations/0000_helpers.sql`，每张表迁移末尾绑定。

---

## 3. 软删除策略

- **采用**：`users`、`courses`（用户自建）、`novels`、`comments`、`orders` 等用户可生成可恢复数据。
- **不采用（物理删除）**：系统配置表、缓存表、日志表、临时会话（`game_sessions`）、排行榜快照、消息已读标记。
- **查询默认**：`packages/supabase-client/src/helpers/soft-delete.ts` 提供 `selectActive(table)` 自动拼 `.is('deleted_at', null)`；删除显式调用 `softDelete(table, id)`。
- **唯一索引**：必须 `WHERE deleted_at IS NULL`，避免软删后无法复用同名。

---

## 4. 字段类型选用

| 场景 | 类型 | 说明 |
|------|------|------|
| 标识符 | `uuid` | 全表统一 |
| 短文本 | `text` | 由 Zod 限长 |
| 长文本 / 富文本 | `text` | 应用层校验长度 |
| 金额 | `numeric(18,2)` | 禁用 `float` |
| 计数 | `bigint` | 防 32 位溢出 |
| 标签数组 | `text[]` | ≤ 5 个；多则建关联表 |
| 半结构化数据 | `jsonb` | 写入注意见 §9 |
| 多语言文案 | `jsonb` `{zh,en,vi,th,id}` | 缺省回退 `en` |
| 向量（**仅 AI 场景**）| `vector(1536)` | 用前同迁移内 `create extension if not exists vector`，非 AI 业务严禁使用 |
| 枚举 | `text` + `CHECK` 约束 | 不用 PG enum |

---

## 5. 索引与约束

1. 外键字段**必须**建索引。
2. 列表页排序 / 筛选字段建组合索引（最左前缀）。
3. 全文检索字段：`tsvector` 生成列 + GIN 索引。
4. JSONB 经常查询路径：表达式索引。
5. 外键 `ON DELETE`：
   - 用户级数据 → `CASCADE`
   - 系统 / 字典引用 → `RESTRICT`
   - 弱引用（统计 / 日志）→ `SET NULL`

---

## 6. Schema 与迁移（Supabase CLI）

1. 新建迁移：`pnpm supabase migration new <verb>_<object>` → 在 `supabase/migrations/` 生成空 SQL。
2. 编写纯 SQL；Schema 改动只走此路径。
3. 本地应用：`pnpm supabase db reset`（dev 随时全量重建）。
4. 类型同步：`pnpm supabase gen types typescript --local > packages/supabase-client/src/types/database.ts`，提交。
5. **禁止**手改已合入迁移；改字段必须新增迁移。
6. 数据回填脚本放 `scripts/db/backfill/`，TypeScript + `tsx` 执行；不与 schema 迁移混。
7. 复杂查询 / 事务封装为 **Postgres RPC 函数**，由 `supabase.rpc(...)` 调用。

---

## 7. RLS（Row Level Security）

- **C 端可读写表**：必须开启 RLS，Policy 至少覆盖 `select / insert / update / delete`。
- **后台专用表**：开启 RLS 并仅放行 `service_role`。
- Policy 命名：`<表>_<操作>_<角色>`，如 `orders_select_owner`。
- 测试要求：`supabase/tests/rls/` 每张开启 RLS 的表至少 1 条正例 + 1 条反例（pgTAP 或自定义脚本）。
- 后端 service-role 客户端绕过 RLS：仅 `apps/api-*` 与 Edge Functions 可用；前端禁止接触。

---

## 8. 多语言文案存储

- jsonb 结构：

  ```json
  { "zh": "你好", "en": "Hello", "vi": "Xin chào", "th": "สวัสดี", "id": "Halo" }
  ```

- 读取：按用户当前 locale 取值；缺失依次回退 `en` → `zh`。
- 校验：Zod schema 强制至少包含 `zh`、`en`。

---

## 9. JSONB 使用注意事项

- 通过 **supabase-js / PostgREST** 直接 `.insert({ col: obj })` **安全**（走 JSON body，PostgREST 自动识别 jsonb，不会双重编码）。
- 通过 **RPC** 传 jsonb 参数时：
  - SQL 函数签名必须显式 `arg jsonb`；
  - JS 端调用：`supabase.rpc('fn_x', { payload: obj })`，**禁止**先 `JSON.stringify`，否则被识别为字符串入参（`jsonb_typeof = 'string'`）。
- **历史教训作废**：本项目不使用 Drizzle，user memory `drizzle-jsonb.md` 中的"双重编码"坑不再适用；新规则以本节为准。

---

## 10. 缓存表与滚动窗口

- 滚动窗口缓存表 PK `period_start` 必须为**稳定桶键**（如 `date_trunc('hour', now())`），不得使用 `now() - Δ`，否则 `ON CONFLICT` 永不命中（user memory 教训保留）。

---

## 99. 待确认问题
（无）
