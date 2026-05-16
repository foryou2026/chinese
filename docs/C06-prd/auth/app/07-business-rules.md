<!-- TARGET-PATH: docs/C06-prd/auth/app/07-business-rules.md -->

# 07 · 业务规则 · auth / **app**

| R-ID | 规则 |
|------|------|
| R-A01 | 注册限流 5/h(IP + email-hash) |
| R-A02 | 登录失败 5/15min 锁;15 分自动解 |
| R-A03 | 找回密码 3/h |
| R-A04 | 邮箱未验证可登录,功能受限(标记 banner) |
| R-A05 | 重发验证邮件 60s 冷却 |
| R-A06 | 密码强度:长度 ≥ 8,含字母+数字 |
| R-A07 | 全局登出触发 broadcast,所有端 30s 内被踢 |
| R-A08 | session 15 分,refresh 30 天;闲置 7 天自动登出 |
| R-A09 | Edge 之间 cookie 通过短 nonce 交换,nonce 1 次性 |
