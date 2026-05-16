<!-- TARGET-PATH: docs/D02-api/admin-auth/03-endpoints/POST-admin-auth-password.md -->

# POST /admin/v1/auth/password

## 1. 概述

admin 改密;先校验旧密 → updateUser → revoke 其他 admin refresh → 保留当前 session。

## 2. 入参

```json
{ "old_password": "...", "new_password": "...", "repeat": "..." }
```

zod:
```ts
z.object({
  old_password: z.string().min(1),
  new_password: z.string().min(8).regex(/[a-zA-Z]/).regex(/\d/),
  repeat: z.string()
}).refine(d => d.new_password === d.repeat, { path:['repeat'] })
```

## 3. 出参

```json
{ "data": { "ok": true }, "error": null }
```

错误:`AUTH_INVALID_OLD_PASSWORD` / `AUTH_SAME_AS_OLD_PASSWORD` / `AUTH_WEAK_PASSWORD` / `AUTH_PASSWORD_CHANGE_RATE_LIMITED`

## 4. 逻辑

1. Redis 节流:`throttle:pwd-change:admin:<uid>` 5min ≤ 3 次,否则 `AUTH_PASSWORD_CHANGE_RATE_LIMITED`;
2. `supabase.auth.signInWithPassword({ email, password: old_password })`(临时 client,不动当前 session)→ 失败返 `AUTH_INVALID_OLD_PASSWORD`;
3. 若 new===old → `AUTH_SAME_AS_OLD_PASSWORD`;
4. `supabase.auth.admin.updateUserById(uid, { password: new_password })`;
5. revoke 其他 admin session:`DELETE FROM user_sessions WHERE user_id=${uid} AND surface='admin' AND session_id!=${current}` + `supabase.auth.admin.signOut(uid, { scope:'others' })` (注:Supabase 暂无 others scope,实际通过列出 refresh tokens 后逐个删,详见 service 实现);
6. 审计:`admin.password_changed`。

## 5. 守卫

`requireAuth` + `requireRole('super_admin')` + `csrfGuard`

## 6. 审计

`admin.password_changed` · payload 不含明文 / 不含 hash
