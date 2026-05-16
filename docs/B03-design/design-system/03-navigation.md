<!-- TARGET-PATH: docs/B03-design/design-system/03-navigation.md -->

# 03 · 导航菜单

> **阶段**：B03-S  
> **上游**：`02-layout.md`、`C02-permissions/01-roles.md`  
> **下游**：`system/packages/shared-config/src/menus.ts`、`<TopNav />` 组件、所有 C03 N 顶栏部分  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 应用端 5 个一级菜单；未登录可见全部菜单，但仅"发现中国"前 3 主题可浏览，其他点击即跳登录。
- 管理端 4 个一级菜单（用户管理 / 发现中国 / 系统课程 / 小说专区）；v1 不暴露其他后台功能。
- 头像下拉应用端 6 项 + 退出；管理端简化（账号信息 / 切换到应用端 / 退出）。
- 单一数据源 = `shared-config/src/menus.ts`；名称全走 i18n。

---

## 1. 应用端（`web-app`）

| 菜单 | 路由 | 图标（lucide）| 可见角色 | 备注 |
|------|------|--------------|---------|------|
| 发现中国 | `/discover` | `compass` | 所有（含未登录）| 未登录仅可浏览**前 3 主题**；第 4 个起点击即跳登录 |
| 系统课程 | `/courses` | `graduation-cap` | 登录用户 | 未登录点击菜单项直接跳登录页 |
| 游戏专区 | `/games` | `gamepad-2` | 登录用户 | 同上（v1 未实现，菜单先占位）|
| 小说专区 | `/novels` | `book-open` | 登录用户 | 同上（v1 未实现）|
| 个人中心 | `/me` | `user-circle` | 登录用户 | 未登录显示"登录 / 注册"入口 |

### 1.1 头像下拉（登录后，右上角）

```
我的资料        → /me
我的钱包        → /me/wallet
订单与会员      → /me/orders
邀请好友        → /me/referral
设置（语言/主题）→ /settings
─────────────────
退出登录
```

### 1.2 未登录态

- 一级菜单**全部可见**（保证品牌呈现 + 发现路径完整）；
- 仅「发现中国」可部分浏览；其他菜单点击 → `/auth/login?redirect=...`；不弹提示，减少打断；
- 「发现中国」未登录仅渲染前 3 主题卡片：
  - 首页 / 发现页第 4 个及以后卡片点击跳登录；
  - 主题详情内的快闪 / 游戏跳转 / 评论 / 点赞均跳登录；
- 右上角头像位替换为「登录 / 注册」两个文字按钮（`text-button`，红色文字）；
- **路由守卫实现**：`_authed/` 路由组未登录访问 → 重定向；「发现中国」route loader 检测未登录时在请求加 `?guest=1&limit=3`，后端仅返回前 3 主题。

---

## 2. 管理端（`web-admin`，前缀 `/admin`）

| 菜单 | 路由 | 图标 | 可见角色 | 备注 |
|------|------|------|---------|------|
| 用户管理 | `/admin/users` | `users` | `super_admin` | 列表只列 `role='user'`；详见 [B02 §3](../../C02-permissions/01-roles.md) |
| 发现中国 | `/admin/discover` | `compass` | `super_admin` | 内容审核 / 上下架 |
| 系统课程 | `/admin/courses` | `graduation-cap` | `super_admin` | 课程管理 / 上下架 |
| 小说专区 | `/admin/novels` | `book-open` | `super_admin` | 小说审核 / 章节管理 |

> **当前管理端不暴露**：游戏配置、经济、邀请、客服、安全、内容工厂、i18n 校对、支付配置。
> PM 决策（[C02-permissions `_input/roles-input.md`](../../C02-permissions/_input/roles-input.md)）：本期一律视为超管兼任。

### 2.1 管理端头像下拉

```
账号信息       → /admin/me
切换到应用端    → /
─────────────
退出登录
```

### 2.2 角色守卫

- 路由 `/admin/*` 由 `_admin` 路由组守卫：
  - 未登录 → `/admin/auth/login?redirect=...`；
  - 已登录但非 `super_admin` → `/admin/auth/login?reason=not_admin`（不进 `/403`，避免泄露管理端路径）；
- 顶栏菜单按当前角色过滤；不匹配的菜单项**不渲染**（不灰显），减少诱导。

---

## 3. 单一数据源

`system/packages/shared-config/src/menus.ts`：

```ts
type MenuItem = {
  key: string;
  i18nKey: string;          // 'nav.discover'
  path: string;
  icon: LucideIconName;
  requireAuth?: boolean;
  requireRole?: 'super_admin';
  children?: MenuItem[];
};

export const appMenu: MenuItem[] = [/* ... */];
export const adminMenu: MenuItem[] = [/* ... */];
```

- 名称必须走 i18n（`packages/shared-i18n/<locale>/nav.json`）；禁止硬编码任何语言；
- 新增菜单：**先**改 `menus.ts` + 5 语言 + 路由 + 本文件，再合入业务代码。

---

## 4. 视觉规范

- 选中态：参考 [02-layout §2.1](./02-layout.md)（桌面底部红色短线 / 移动 Drawer 左侧红色竖线）；
- 图标：`lucide-react`，**18px**，颜色继承文字色；选中态图标变 `--brand`；
- 徽标（未读消息）：`radius-pill` `--brand` 底白字，最小 16×16，最大显示 `99+`；
- hover：颜色变化 `--motion-fast`。

---

## 99. 待确认问题
（无）
