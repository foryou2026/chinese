# R-ID 覆盖矩阵

| R-ID | 描述 | M-ID | page-id | FL-ID | SM-ID |
|------|------|------|---------|-------|-------|
| R-auth-001 | 邮箱密码注册 | M-auth-001 | P-app-auth-002 | FL-auth-002 | SM-auth-001 |
| R-auth-002 | 邮箱密码登录 | M-auth-001 | P-app-auth-001 | FL-auth-001 | SM-auth-001 |
| R-auth-003 | Google 快捷登录 | M-auth-001 | P-app-auth-001, P-app-auth-002 | FL-auth-003 | SM-auth-001 |
| R-auth-004 | 登录失败限流 | M-auth-001 | P-app-auth-001 | FL-auth-001 | SM-auth-001 |
| R-auth-005 | 忘记密码 | M-auth-001 | P-app-auth-003 | FL-auth-004 | 无 |
| R-auth-006 | 重置密码 | M-auth-001 | P-app-auth-004 | FL-auth-005 | SM-auth-001 |
| R-auth-007 | 修改密码 | M-auth-001 | P-app-auth-005 | FL-auth-006 | 无 |
| R-auth-008 | 退出登录 | M-auth-001 | P-app-auth-006 | 无 | SM-auth-001 |
| R-auth-009 | Token 过期 | M-auth-001 | P-app-auth-006 | 无 | SM-auth-001 |
| R-auth-010 | 密码强度 | M-auth-001 | P-app-auth-002, 004, 005 | FL-auth-002, 005, 006 | 无 |
| R-auth-011 | 邮箱格式 | M-auth-001 | P-app-auth-001, 002, 003 | FL-auth-001, 002, 004 | 无 |
| R-auth-012 | Google 自动注册 | M-auth-001 | P-app-auth-001, 002 | FL-auth-003 | SM-auth-001 |
| R-auth-013 | 登录/注册切换 | M-auth-001 | P-app-auth-001, 002 | 无 | 无 |
| R-auth-014 | Google 用户密码管理 | M-auth-001 | P-app-auth-005 | FL-auth-006 | 无 |
| R-auth-015 | 注册邮箱验证码 | M-auth-001 | P-app-auth-002 | FL-auth-002 | 无 |
| R-auth-016 | 多设备登录限制 | M-auth-001 | P-app-auth-001 | 无 | SM-auth-001 |
| R-auth-017 | 多语言切换 | M-auth-001 | P-app-auth-001~004, 006 | 无 | 无 |
| R-auth-018 | 所有 UI 文案国际化 | M-auth-001 | P-app-auth-001~006 | 无 | 无 |

## 未覆盖检查
- [x] 所有 R-ID 落点（含新增 R-auth-017, R-auth-018）
- [x] 所有 M-ID 承接 ≥1 个 R-ID
- [x] 所有 page-id 有 ≥1 条场景验证
