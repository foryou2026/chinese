<!-- TARGET-PATH: docs/C06-prd/auth/app/10-known-issues.md -->

# 10 · 已知问题

| # | 描述 | 风险 | 缓解 / 计划 |
|---|------|------|------------|
| K-01 | 邮件 mock 仅写 `.eml` 到磁盘，dev 自测需手动复制链接 | 仅影响开发体验 | v1 接 prod SMTP（按 `B01-architecture/06-deploy-env.md`）|
| K-02 | 没有图床，头像只接受 URL | 体验弱 | v2 接对象存储 + 上传组件 |
| K-03 | 无设备管理页，用户看不到「我的设备」清单 | 透明度弱；安全感差 | v2 评估；当前用 Toast 提示被踢已能满足下限 |
| K-04 | OAuth 用户的初始密码字段为空，若之后想"添加密码登入方式"目前无入口 | 体验弱 | v2 提供「绑定密码」入口 |
| K-05 | 邮箱不能改 | 用户邮箱变更走客服 | v2 评估 |
| K-06 | `auth.refreshSession` 失败 reason 在前端只能粗略归类（kicked/expired），实际原因可能是 GoTrue 自我升级期间临时不可用 | 极偶发 | 后续接 GoTrue 状态页 + 重试 |
