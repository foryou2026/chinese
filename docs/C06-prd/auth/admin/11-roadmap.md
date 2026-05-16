<!-- TARGET-PATH: docs/C06-prd/auth/admin/11-roadmap.md -->

# C05 · 11 演进 · `auth`

## v1 (本期)

- 4 页 + 10 R-ID + 邀请制 (SQL seed)

## v1.1 (Q3)

- TOTP 二次验证
- IP 白名单 (按管理员可配)
- "我的设备" 列表页 + 单设备踢

## v2 (Q4)

- 自助邀请 UI:超管能邀请新超管 (需先升级 B02-01 引入 `admin_inviter` 子角色或经审批流)
- 修改邮箱 (绿/红 Workspace 类流程)
- 审计仪表盘 (登录失败次数 / 设备地图 / 异常行为)

## v3+

- SSO (Google Workspace / SAML)
- WebAuthn / Passkey
- 委派子管理员 (多角色矩阵)
