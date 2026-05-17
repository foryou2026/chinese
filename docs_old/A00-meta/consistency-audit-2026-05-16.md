<!-- TARGET-PATH: docs/A00-meta/consistency-audit-2026-05-16.md -->

# 一致性审计报告 · 2026-05-16

> **目的**：核对 `/docs`（AI 反推规范）与 `/backup`（已开发系统 + 既有规则 + 既有 PRD）的事实一致性，并把 `/docs` 修订到与 **`backup/system` 已运行代码** 完全一致，避免后续 C01–C05 与"既成事实"冲突。
>
> **结论**：本次审计共发现 9 类不一致，已按用户决策全部处理。`/docs` 当前与 `backup/system/supabase/migrations/*.sql` + `backup/function/02-course/prd/*` + `backup/env.md` 一致。

---

## 1. 处理原则（用户决策）

| 决策点 | 用户选择 |
|--------|---------|
| 支付方案冲突（backup 配了微信支付凭证 vs docs 写 Paddle）| **保留 Paddle 不变**（env.md 微信凭证作为基础设施备份，本期支付走 Paddle mock）|
| DB 字段冲突（grules 规范 `is_disabled` vs migrations 已用 `is_active`）| **以已运行 migrations 为准**，docs 全部对齐 |
| 课程主题数（5 vs 4）| **5 主题**（`share/ec/fc/hsk/dl`），统一所有 roadmap |
| Edge Functions（实际未启用 vs docs 多处引用）| 已确认 v1 仅 `auth / discover-china / course` 三 feature；Edge Functions 仅在 `B01` 保留为基础设施能力，**未被任何 feature 引用** |

---

## 2. 已修订冲突清单

### 2.1 DB schema 命名

- **事实**：`backup/system/supabase/migrations/*` 全部使用 `zhiyu.<table>` schema。
- **修订**：`docs/C02-permissions/04-data-model.md` 中所有 `public.profiles / user_sessions / audit_logs / auth_login_attempts` → `zhiyu.<table>`。

### 2.2 `profiles` 表字段

- **事实**（`0002_profiles_sessions_audits.sql`）：

  ```
  id, email, role, display_name, avatar_url, locale,
  is_active boolean default true,
  email_verified_at timestamptz,
  created_at, updated_at
  ```

  **没有** `is_disabled` / `disabled_reason` / `disabled_at` / `disabled_by` 字段；状态用 `is_active` 取反表达。
- **修订**：
  - `04-data-model.md` 重写 `profiles` 表定义；
  - `02-auth-flow.md`：禁用判定 `is_disabled=true` → `is_active=false`，删 `disabled_reason/by/at` 相关 SQL；
  - `03-authz-mechanism.md`：缓存检查列 → `is_active`；
  - `00-index.md`：表述同步；
  - `B02-ux/04-voice-tone.md`：错误文案不再含 `{reason}`；
  - `C01-requirements/auth/flows/*.md`：Mermaid 节点 `is_disabled=true` → `is_active=false`。
- **保留**：错误码 `AUTH_ACCOUNT_DISABLED`（语义合理，前端文案沿用"账号已被停用"）。

### 2.3 `user_sessions` 表字段

- **事实**：
  ```
  id, user_id, device_id text, device_name text, user_agent, ip text,
  refresh_jti text, last_seen_at, created_at
  UNIQUE(user_id, device_id)
  ```
- **docs 原写**：`refresh_token_hash` + `device` 枚举 `'web'|'mobile-web'`。
- **修订**：
  - `04-data-model.md` 重写表定义；
  - `02-auth-flow.md`：会话注册插入字段更新；
  - `C06-prd/auth/app/02-glossary.md`：术语 `refresh_token_hash` → `refresh_jti`；`device_info` → `device_id/device_name`。
- **业务语义对齐**：同一用户同一 `device_id` 唯一；多设备硬上限 3 仍生效（用 `user_id` count 判定）。

### 2.4 `auth_login_attempts` 表字段

- **事实**：`email/ip/user_agent/success/reason/created_at`（**没有** `succeeded`/`attempted_at`）。
- **修订**：`04-data-model.md` 字段对齐；锁定判定 SQL 改用 `success=false`。

### 2.5 `audit_logs` 表字段

- **事实**：`actor_id/actor_role/event/target_type/target_id/meta jsonb/ip text/created_at`（**没有** `action`/`actor_user_id`/`target_user_id`/`payload`/`user_agent`/`surface`）。
- **修订**：`04-data-model.md` 字段对齐；事件列表用 `event` 列，例：`event='auth.signin_success'`、`event='user.disable'`。

### 2.6 `ip` 字段类型

- **事实**：全表使用 `ip text`（**不是** `inet`）。
- **修订**：`04-data-model.md` 全部改 `text`。

### 2.7 UUID 默认生成函数

- **事实**：`profiles.id` 用 `auth.users(id)` 引用（不自带默认）；`user_sessions.id` 用 `uuid_generate_v4()`；`china_*` 用 `gen_random_uuid()`。
- **修订**：`04-data-model.md` 与实际函数一致；`B01-architecture/03-database.md` 通用规则 `gen_random_uuid()` 不变（适用于新建业务表）。
- **遗留约定**：B02-04 摘要原写"所有 id UUID v7" → 改为"所有 id UUID v4（`gen_random_uuid()` 或 `uuid_generate_v4()`）"。

### 2.8 课程主题数（5 vs 4）

- **事实**：`backup/function/02-course/prd/01-课程目录骨架.md` + `docs/C01-requirements/course/baseline.md` = **5 主题**（`share` 为共享预备主题，外加 `ec/fc/hsk/dl`）。
- **修订**：
  - `C06-prd/course/app/11-roadmap.md` "4 主题骨架" / "4 主题全量发布" → "5 主题"；
  - `C06-prd/course/admin/11-roadmap.md` 同步。

### 2.9 `profiles.role` CHECK 约束顺序

- **事实**：`check (role in ('super_admin','user'))`。
- **docs 写**：`check (role in ('user', 'super_admin'))`。
- **修订**：对齐到 migration 顺序（无功能差异，纯字面一致）。

---

## 3. 已确认一致项（无需修订）

| 维度 | 状态 |
|------|------|
| Monorepo 结构（apps × 4 + packages × 7）| ✅ |
| 端口（3100/4100/8100/9100/6379）| ✅ |
| 自托管 Supabase + Docker only | ✅ |
| 2 角色（`user` / `super_admin`）+ 超管自保规则 | ✅ |
| 5 语 i18n（`zh/en/vi/th/id`）| ✅ |
| 反爬虫硬约束（禁止 SSR / 数据预注入）| ✅ |
| `china` 模块 12 类目 + 多语 jsonb | ✅ |
| `discover-china` / `course` / `auth` 三 feature 范围 | ✅ |
| 微信支付凭证（`backup/env.md`）| ⚠️ 仅作基础设施备份，业务支付层仍按 docs `Paddle mock` 推进；本期不涉及实际支付路径 |
| 腾讯云短信凭证（`backup/env.md`）| ⚠️ 同上，本期 v1 不接短信登录；保持 docs `Adapter console mock` |
| Dify / NocoBase / OpenClaw | ✅ 已停用，docs 不引用，一致 |
| Edge Functions | ⚠️ 实际 `backup/system/supabase/` 下无 `functions/` 目录；docs 仅作为"未来基础设施"描述，未被任何 v1 feature 引用 |

---

## 4. 后续建议（非阻塞）

1. **如需启用禁用原因审计**：增补 migration `0008_profiles_disabled_extras.sql` 加 `disabled_reason/disabled_at/disabled_by` 列后，再回填 docs 文案 `{reason}` 插值。
2. **支付落地时**：若决定改用微信支付（已有凭证），再启动一轮 B01→C01 修订，把 Paddle 全部替换为 wechat-pay。
3. **`user_sessions.device_id` 生成规则**：建议落地一份 `docs/C02-permissions/05-auth-feature-guideline.md` 章节，明确 device_id 由前端 fingerprint（`navigator.userAgent + screen` hash）生成，避免不同浏览器重复占用 3 槽。

---

## 5. 修订执行清单（git 跟踪）

| 文件 | 改动类型 |
|------|---------|
| `docs/C02-permissions/04-data-model.md` | 全表重写（schema + 字段） |
| `docs/C02-permissions/02-auth-flow.md` | 字段名 / SQL 改写 |
| `docs/C02-permissions/03-authz-mechanism.md` | 字段名 / SQL 改写 |
| `docs/C02-permissions/00-index.md` | 摘要表述同步 |
| `docs/B02-ux/04-voice-tone.md` | 错误文案去 `{reason}` |
| `docs/C01-requirements/auth/flows/app-exception-flow.md` | Mermaid 节点 |
| `docs/C01-requirements/auth/flows/app-main-flow.md` | Mermaid 节点 |
| `docs/C01-requirements/auth/flows/admin-exception-flow.md` | Mermaid 节点 |
| `docs/C06-prd/auth/app/02-glossary.md` | 术语 |
| `docs/C06-prd/course/app/11-roadmap.md` | 4 → 5 主题 |
| `docs/C06-prd/course/admin/11-roadmap.md` | 4 → 5 主题 |
| `docs/A00-meta/consistency-audit-2026-05-16.md` | 本文档（新增）|

> 完成时间：2026-05-16
