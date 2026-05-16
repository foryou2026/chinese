<!-- TARGET-PATH: docs/C05-prd/auth/_shared/glossary.md -->

# auth · `_shared/glossary.md` · auth feature 共享术语

> **作用**：auth feature 跨 surface 公共术语；项目层通用术语见 [`C05-prd/_glossary.md`](../../_glossary.md)。
> **冻结**：2026-05-17

| 术语 | 定义 |
|------|------|
| **session** | 一条 `user_sessions` 记录 = (user_id × surface × device_label) 三元组，颁发 access+refresh 双 cookie |
| **设备名册** | 同一 (user_id, surface) 下最多 3 条未撤销 session；第 4 条登入触发踢最旧 |
| **kicked** | session 被设备名册满 / 全设备退出 / 账号禁用导致的服务端单方面 revoke |
| **AUTH_USE_USER_ENTRY** | admin 端登入但 `profiles.role ≠ 'super_admin'` 时的拒绝码（提示「请去 app 端登录」） |
| **链接一次性** | 邮件验证 / 重置密码链接，15min TTL + 使用即作废，不可重发同一 token |
| **节流双层** | "60s 倒计时 + 1h 内最多 3 次" 同时生效；任一触顶即拒绝 |
| **csrf 双提交** | header `X-CSRF-Token` 与 cookie `csrf` 字节级相等才放行；仅状态变更接口校验 |
| **3 设备硬上限** | `app` 与 `admin` 各自最多 3 设备，跨端不共享名额（不是 6 设备） |
| **profile 子集** | `profiles` 表中由用户可写的列：`display_name` / `avatar_url` / `locale`；`role` / `is_active` 仅 super_admin 后台脚本可改 |
