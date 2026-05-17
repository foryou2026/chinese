<!-- TARGET-PATH: docs/C02-ia-interaction/auth/05-navigation.md -->

# 导航结构

> **阶段**：C02-IN · **功能**：`auth`
> **冻结状态**：已冻结 · 2026-05-16

---

## app 端

### 1. 顶栏（未登录态）

| 位置 | 元素 | 行为 |
|------|------|------|
| 右上 1 | 主题切换（sun / moon）| 切换 light / dark |
| 右上 2 | 语言切换（globe）| 5 语切换 |
| 右上 3 | 「登录」文字按钮 | 跳 P-app-auth-001 并带 `redirect=<当前URL>` |
| 右上 4 | 「注册」主按钮 | 跳 P-app-auth-002 |

> 移动端：保留主题切换，「登录」「注册」合并到右侧 Drawer 顶部。

### 2. 顶栏（已登录态）

| 位置 | 元素 | 行为 |
|------|------|------|
| 右上 1 | 主题切换 | 同上 |
| 右上 2 | 语言切换 | 同上 |
| 右上 3 | 通知（bell）| 见 `notifications` feature |
| 右上 4 | 头像下拉 | 见 §3 |

### 3. 头像下拉（6 项）

| 顺序 | 文案（i18n）| 跳转 page-id | 归属 feature |
|------|------------|-------------|-------------|
| 1 | 我的资料 | P-app-auth-007 | **auth** |
| 2 | 我的钱包 | P-app-wallet-001 | wallet（暂不支持，禁用展示）|
| 3 | 订单与会员 | P-app-orders-001 | orders（暂不支持，禁用展示）|
| 4 | 邀请好友 | P-app-referral-001 | referral（暂不支持，禁用展示）|
| 5 | 设置（语言 / 主题）| P-app-settings-001 | settings（暂不支持，禁用展示）|
| — | — 分割线 — | — | — |
| 6 | 退出登录 | 触发 SM-auth-app-03 `signOut`，跳 P-app-auth-001 | **auth** |

### 4. 个人中心二级菜单（P-app-auth-007 内）

| 卡片 | 跳转 page-id |
|------|-------------|
| 资料 | P-app-auth-009 |
| 账号与安全 | P-app-auth-008 |
| 钱包（暂不支持）| P-app-wallet-001（禁用展示）|
| 订单与会员（暂不支持）| P-app-orders-001（禁用展示）|
| 邀请好友（暂不支持）| P-app-referral-001（禁用展示）|

---

## admin 端

### 1. 顶栏（admin 主框架右上）

| 元素 | 行为 |
|------|------|
| Logo「知语·后台」| 点击 → `/admin`（Dashboard）|
| 语言切换 | 5 语，不要求登录态 |
| 头像（initial）| 点击展开下拉 |

### 2. 头像下拉（2 项）

| 序 | 项 | 跳转 |
|---|----|------|
| 1 | 账号与安全 | `/admin/me`（P-admin-auth-004）|
| 2 | 退出登录 | 调管理端接口后跳 `/admin/auth/login` |

### 3. 路由树

```
/admin/auth/login           公开
/admin/auth/forgot          公开
/admin/auth/reset-password  公开
/admin/me                   admin
/admin/*                    admin（其它业务路径）
```
