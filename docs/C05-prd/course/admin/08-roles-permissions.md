<!-- TARGET-PATH: docs/C05-prd/course/admin/08-roles-permissions.md -->

# 08 · 角色与权限 · course / **admin**

| 角色 | tracks_scope | 可见 P-ID | 可写 |
|------|-------------|-----------|------|
| readonly | 任意 | P-001..009(只读)| ✗ |
| content_admin | 受限于 scope | scope 内 P-001..008 | scope 内全写;不可发布 30 天以上资源 |
| super | 全部 | P-001..009 全 | 全写 + 跨 scope 转移 + 30 天+ unpublish |

> RLS 跳过;过滤由 handler `WHERE track_code = ANY($scope)`;违反返 `COURSE_SCOPE_FORBIDDEN`。
