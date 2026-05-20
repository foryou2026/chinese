# R-ID 覆盖矩阵

| R-ID | 描述 | M-ID | page-id | FL-ID | SM-ID | 增量标记 |
|------|------|------|---------|-------|-------|---------|
| R-auth-001 | 邮箱密码登录 | M-auth-001 | P-admin-auth-001 | FL-auth-001 | SM-auth-001 | [本轮新增] |
| R-auth-002 | 登录失败限流 | M-auth-001 | P-admin-auth-001 | FL-auth-001 | SM-auth-001 | [本轮新增] |
| R-auth-003 | 忘记密码 | M-auth-001 | P-admin-auth-002 | FL-auth-002 | 无 | [本轮新增] |
| R-auth-004 | 重置密码 | M-auth-001 | P-admin-auth-003 | FL-auth-003 | SM-auth-001 | [本轮新增] |
| R-auth-005 | 登录态修改密码 | M-auth-001 | P-admin-auth-004 | FL-auth-004 | 无 | [本轮新增] |
| R-auth-006 | 退出登录 | M-auth-001 | P-admin-auth-004 | 无 | SM-auth-001 | [本轮新增] |
| R-auth-007 | Token 过期处理 | M-auth-001 | P-admin-auth-004 | 无 | SM-auth-001 | [本轮新增] |
| R-auth-008 | 角色校验拦截 | M-auth-001 | P-admin-auth-001 | FL-auth-001 | SM-auth-001 | [本轮新增] |
| R-auth-009 | 密码强度校验 | M-auth-001 | P-admin-auth-003, P-admin-auth-004 | FL-auth-003, FL-auth-004 | 无 | [本轮新增] |
| R-auth-010 | 邮箱格式校验 | M-auth-001 | P-admin-auth-001, P-admin-auth-002 | FL-auth-001, FL-auth-002 | 无 | [本轮新增] |

## 未覆盖检查
- [x] 所有 R-ID 落点
- [x] 所有 M-ID 承接 ≥1 个 R-ID
- [x] 所有 page-id 有 ≥1 条场景验证
