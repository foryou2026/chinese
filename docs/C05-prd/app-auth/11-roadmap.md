<!-- TARGET-PATH: docs/C05-prd/app-auth/11-roadmap.md -->

# 11 · 路线图

## v1（当前）

- 邮箱 + 密码 + Google 注册 / 登入
- 找回密码 / 修改密码 / 修改资料
- 多设备硬上限 + 锁定 + 禁用兜底
- 邮件 mock（dev）

## v1.1（小迭代）

- 接 prod SMTP（实邮件）
- 邀请码注册（仅放开邀请，结构已经在 hook 中预留）
- 头像上传（对象存储）

## v2

- 手机号 OTP 登入（如 OTP 服务成本可控）
- 第二 OAuth Provider（Apple / Facebook 视市场而定；Google 已覆盖东南亚主流）
- 2FA TOTP
- "我的设备"页（列出 user_sessions，可主动撤销某台）
- 修改邮箱（带验证）
- 自助删账号 / 数据导出（GDPR-like）

## v3+

- 单一登录 SSO（B2B 学校 / 企业客户）
- 通行密钥 (Passkey / WebAuthn)
