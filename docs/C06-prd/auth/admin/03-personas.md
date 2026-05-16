<!-- TARGET-PATH: docs/C06-prd/auth/admin/03-personas.md -->

# C06 · 03 角色画像 · `auth`

##  · 超级管理员 (admin)

- 数量 首版:1~3 名
- 设备:Mac/Windows 笔记本 + 偶尔手机查看;主用浏览器 Chrome/Edge
- 关注:登录稳定 / 密码可改 / 被踢能感知 / 误操作有提示
- 不关注:头像 / 个性化

##  · 运维 (DevOps,非产品用户)

- 通过 SSH / 容器命令调 `seed-super-admin.sh` 创建新超管
- 通过 SQL 把异常超管 启用态=false`
- 不登录管理后台,但所有变更进 审计记录.actor_role='system'`

## P3 · 攻击者 (假想)

- 暴力猜密 → 节流 5 次/15min + IP 1h ≤ 5 → 锁定
- 钓鱼拿到旧密 → 改密后 revoke 全部 refresh 立即生效
- 拿到 access token (中间人) → HttpOnly Cookie + Secure + SameSite=Lax + CSRF Double-Submit 共同防护
- user 角色越权访问 admin → 双重守卫 (路由 loader + 后端 requireRole)
