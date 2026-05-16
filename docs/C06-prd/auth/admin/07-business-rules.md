<!-- TARGET-PATH: docs/C06-prd/auth/admin/07-business-rules.md -->

# 07 · 业务规则 · auth / **admin**

| R-ID | 规则 |
|------|------|
| R-AA01 | 不开放公共注册;仅 super 可邀请 |
| R-AA02 | 登录失败 3/30min 锁;5 次锁需 super 解 |
| R-AA03 | 找回密码 1/h;3 次失败锁 24h |
| R-AA04 | 自助改密需当前密码二次校验;3/h |
| R-AA05 | 新密码不可与最近 5 次重复 |
| R-AA06 | session 15 分,refresh 7 天;闲置 1 天自动登出 |
| R-AA07 | super 触发全局登出立即生效(不等过期) |
| R-AA08 | 2FA 一旦开启不可关闭(super 例外) |
| R-AA09 | 所有写操作写 admin_action_log |
