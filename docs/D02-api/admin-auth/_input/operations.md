<!-- TARGET-PATH: docs/D02-api/admin-auth/_input/operations.md -->

# L01 · 接口需求 · `admin-auth`

- 全部 admin endpoint 路径前缀 `/admin/v1/auth/*`;handler 在 `system/apps/api-admin/src/routes/auth/*`
- 后端 service 100% 复用 `api-app/src/services/auth/*`;handler 仅做:
  1. `requireRole('super_admin')` 守卫 (cookie/* 与 forgot/login-attempt 等公开接口除外)
  2. surface='admin' 标签透传到 service
- 错误码完全沿用 [`B02-03 §4`](../../B02-permissions/03-authz-mechanism.md#4-错误码) + 新增 `AUTH_USE_USER_ENTRY`
- 不引入新表;不引入新事件类型 (events 加 admin.* 前缀以示区分)
