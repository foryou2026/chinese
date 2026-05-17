<!-- TARGET-PATH: docs/C06-prd/auth/_input/admin-prd-context.md -->

# E01 · PRD 背景 · `auth`

- 内部产品 · 仅供运营/超管使用
- 目标:让超管能登录、改密、退出;边界外的所有自助功能 (邀请/删除/改邮箱) 均走运维 SQL
- 商业模式:无 (内部工具)
- 关键风险:超管账号被盗 → 全平台失守;依赖运维侧严控 seed 密码 + 锁定 + 审计
- v2 路线:自助邀请 UI · TOTP · IP 白名单 · SSO
