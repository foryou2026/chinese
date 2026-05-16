<!-- TARGET-PATH: docs/C02-ia/app-auth/app/05-navigation.md -->

# `app-auth` · 导航

> **冻结状态**：已冻结 · 2026-05-16

---

## 1. 顶栏（未登录态）

| 位置 | 元素 | 行为 |
|------|------|------|
| 右上 1 | 主题切换 (`sun`/`moon`) | 切换 light/dark |
| 右上 2 | 语言切换 (`globe`) | 5 语切换 |
| 右上 3 | 「登录」文字按钮 | 跳 `P-app-app-auth-001` 并带 `redirect=<当前URL>` |
| 右上 4 | 「注册」主按钮 | 跳 `P-app-app-auth-002` |

> 移动端：保留主题切换，「登录」「注册」合并到右侧 Drawer 顶部。

## 2. 顶栏（已登录态）

| 位置 | 元素 | 行为 |
|------|------|------|
| 右上 1 | 主题切换 | 同 |
| 右上 2 | 语言切换 | 同 |
| 右上 3 | 通知 (`bell`) | 见 `notifications` feature |
| 右上 4 | 头像下拉 | 见 §3 |

## 3. 头像下拉（B04 §03 应用端 6 项）

| 顺序 | 文案 (i18n) | 跳转 page-id | 归属 feature |
|------|------------|-------------|-------------|
| 1 | 我的资料 | `P-app-app-auth-007` | **app-auth** |
| 2 | 我的钱包 | `P-app-wallet-001` | wallet（v2）|
| 3 | 订单与会员 | `P-app-orders-001` | orders（v2）|
| 4 | 邀请好友 | `P-app-referral-001` | referral（v2）|
| 5 | 设置（语言/主题）| `P-app-settings-001` | settings（v2）|
| - 分割线 - |
| 6 | 退出登录 | 触发 SM-03 `signOut`，跳 `P-app-app-auth-001` | **app-auth** |

> 本 feature **拥有**第 1 项与第 6 项；其它项在对应 feature 落地之前**显示为禁用**（hover 提示「即将推出」）。

## 4. 个人中心二级菜单（`P-007` 内）

| 卡片 | 跳转 page-id |
|------|-------------|
| 资料 | `P-app-app-auth-009` |
| 账号与安全 | `P-app-app-auth-008` |
| 钱包（v2）| `P-app-wallet-001`（禁用展示）|
| 订单与会员（v2）| `P-app-orders-001`（禁用展示）|
| 邀请好友（v2）| `P-app-referral-001`（禁用展示）|
