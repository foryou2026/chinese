<!-- TARGET-PATH: docs/C06-prd/auth/app/03-personas.md -->

# 03 · 角色与画像

> 详细角色定义见 [`C02-permissions/01-roles.md`](../../C02-permissions/01-roles.md)，本节只摘录与 `auth` 相关部分。

## 1. 未登录访客（anonymous）

- 入口：落地页、所有 `/auth/*` 路径、所有公开内容（v1 v2 评估）
- 期望：在 1 分钟内完成注册或登入
- 风险：被钓鱼站冒充 → 文案 / 域名要清晰

## 2. 应用端用户（role=`user`）

- 主要角色，本 feature 99% 的用户
- 入口：登入后跳 `/` 或 `?redirect`
- 期望：登一次能用 30 天；改密码 / 改资料快、清晰
- 关心：密码安全、被踢提示要友好、错误英文要少（i18n 覆盖）

## 3. 超级管理员（role=`super_admin`）

- 不应进入应用端登录页；若误入，本 feature 必须把它"礼貌赶走"
- 走 [`auth` feature](../../C06-prd/auth/admin/00-index.md) (批次 4)

## 4. 反例 / 攻击者

| 类型 | 本 feature 的对抗手段 |
|------|---------------------|
| 撞库 | login-attempt-record 节流 + 5/15 锁定 |
| 注册轰炸 | register-throttle 节流（email+IP）|
| OAuth 回调伪造 | exchangeCodeForSession state 校验（Supabase 内置）|
| 被禁账号刷接口 | disabledCache + 401 立返 |
