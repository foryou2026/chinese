<!-- TARGET-PATH: docs/C06-prd/course/admin/08-roles-permissions.md -->

# 08 · 角色与权限 · course / **admin**

> 遵从 [docs/C02-permissions/01-roles.md](../../../C02-permissions/01-roles.md) 的 2 角色硬约束。

| 角色 | 可见 P-ID | 可写 |
|------|-----------|------|
| `super_admin` | P-001..009 全 | 全写 + 发布 / 撤回 / 媒资上传 / 举报处置 |
| `user` | —（不出现在 admin 路由，访问返 403）| — |

> 服务端：中间件在 `/api/admin/course/*` 统一校验 `role === 'super_admin'`；RLS 以 `auth.uid()` 设备隔离。不再存在 `tracks_scope` 过滤与 `COURSE_SCOPE_FORBIDDEN`。
