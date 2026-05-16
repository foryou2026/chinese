<!-- TARGET-PATH: docs/C05-prd/admin-auth/07-business-rules.md -->

# C05 · 07 业务规则 · `admin-auth`

| BR-ID | 规则 | 落地 |
|-------|------|------|
| BR-1 | 仅 `app_metadata.role==='super_admin'` 可登录 admin;其它角色登录成功后立即 signOut | C03/P-001 + D02 session-register 守卫 |
| BR-2 | 5 次错密 / 15min → 锁定该邮箱 (内存 + auth_login_attempts 双查) | D01-03 D-BR-04 (复用) |
| BR-3 | `profiles.is_disabled=true` → 立即拒登 (30s LRU 缓存) | D01-03 D-BR-05 (复用) |
| BR-4 | 同一超管 admin surface 上限 3 设备活跃会话;第 4 登录踢最早 | D02-03 POST session-register (surface 维度) |
| BR-5 | 重置链接 15min 一次性;exchange 成功后 token 标记已用 | Supabase 内置 |
| BR-6 | 改密成功后立即 revoke 该用户**全部 surface** 的非当前 refresh | D02 POST password |
| BR-7 | 全局退出 = `supabase.auth.admin.signOut(uid, scope:'global')` | D02 POST logout-global |
| BR-8 | 任何 admin 写操作必须落 `audit_logs`,actor_role='super_admin' | D02-06 events |
| BR-9 | admin 端登录页**不展示** "切换到用户端" 链接;入口物理隔离 | C03/P-001 |
| BR-10 | 严禁 admin 端任何 UI 提供"创建新管理员"功能 | B02-05 §5 |
