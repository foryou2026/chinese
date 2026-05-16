<!-- TARGET-PATH: docs/C06-prd/auth/admin/02-glossary.md -->

# C06 · 02 术语 · `auth`

| 术语 | 释义 |
|------|------|
| super_admin | 唯一管理端角色;`auth.users.app_metadata.role='super_admin'` + `profiles.role='super_admin'` |
| surface=`admin` | 路径前缀 `/admin/*`;`user_sessions.surface` 字段值;3 设备上限按 surface 独立计数 |
| seed 流程 | 运维通过 `scripts/db/seed-super-admin.sh` 注入新管理员;详见 [`B01-09 §1`](../../../B01-architecture/09-auth-infra.md#1-auth-provider-矩阵) |
| not-admin 态 | 登录页子态;user 角色登录尝试被立即 signOut 后展示 |
| kicked-back 态 | 登录页子态;被其它设备踢后跳回带 `?kicked=1` |
| admin Cookie | `zhiyu-at`/`zhiyu-rt`/`zhiyu-csrf`,与 app 共用;Path=`/`,SameSite=Lax |
| 全局退出 | `supabase.auth.admin.signOut(uid, { scope:'global' })` 撤销该用户**所有 surface** 的全部 refresh |
