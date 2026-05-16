<!-- TARGET-PATH: docs/C04-pages/auth/app/P-app-auth-007.md -->

# `P-app-auth-007` · 个人中心首页

> **path**：`/me` · **角色可见**：用户（登录守卫）  
> **R 覆盖**：R-008  
> **冻结状态**：已冻结 · 2026-05-16

## 1. 布局

- 全屏宽度 `.page`（B03 §02）；
- `<PageHeader title="个人中心" subtitle={maskedEmail} />`；
- `<PageContent>` 内 12 列 Grid，6 张 `<GlassCard>`（同 [05-navigation §4](../../../C03-ia/auth/app/05-navigation.md)）。

## 2. 卡片清单

| 卡片 | 图标 | 描述 | 跳转 | 状态 |
|------|------|------|------|------|
| 资料 | `user-circle` | 头像 / 显示名 / 偏好语言 | `/me/profile` | 启用 |
| 账号与安全 | `shield` | 修改密码 / 退出登录 | `/me/security` | 启用 |
| 我的钱包 | `wallet` | 充值 / 余额 | `/me/wallet` | **禁用 + 「即将推出」徽标** |
| 订单与会员 | `receipt` | 订单 / 会员等级 | `/me/orders` | 禁用 + 即将推出 |
| 邀请好友 | `gift` | 邀请码 / 奖励 | `/me/referral` | 禁用 + 即将推出 |
| 设置 | `settings` | 语言 / 主题 | `/settings` | 禁用 + 即将推出 |

## 3. 数据

进页加载当前用户资料（字段 `id / email / display_name / avatar_url / locale / role / created_at`；具体接口在 D02-api/auth/app/me 定义），用于：

- 顶部头像与显示名；
- 邮箱脱敏：前 3 字符 + `***@<domain>`（按 [B02-05 §4-7](../../../C02-permissions/02-authz-mechanism.md)）；
- 把数据写入全局 `authStore`（已存在则用本次刷新覆盖）。

## 4. 4 态

| 态 | UI |
|---|----|
| `loading` | 6 个卡片骨架屏 + 顶部头像骨架 |
| `profile-view` | 正常渲染 |
| `error` | 顶部 Toast「无法加载资料，请刷新」+ 卡片显占位「-」|

## 5. 场景

| # | 场景 | 期望 |
|---|------|------|
| S1 | 正常进入 | 6 卡片渲染；前 2 可点 |
| S2 | 禁用卡片 hover | tooltip「即将推出」 |
| S3 | 401 中途失效 | 全局守卫立即跳 /auth/login?reason=expired |
| S4 | 5xx | 骨架消失后 Toast |
