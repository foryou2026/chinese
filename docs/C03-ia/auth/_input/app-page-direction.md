<!-- TARGET-PATH: docs/C03-ia/auth/app/_input/page-direction.md -->

# `auth` · I01 页面方向

> 确认 by PM · 2026-05-16

---

## 1. 路由布局

- 公共认证页统一前缀 `/auth/*`，**不需要**登录，**不**强制读 layout；
- 个人中心统一前缀 `/me/*`，必须登录；
- `/auth/callback` 为 OAuth + magic link 通用回调；
- 全部页面**复用顶部 GlassNav**（未登录顶栏右上角显「登录 / 注册」文字按钮）；
- 全部页面**禁止侧边栏**（B03 §02 红线）；
- 内容居中区按"卡片 + 表单"模式：单卡片宽度 桌面 480px / 移动 100% - 32px。

## 2. 表单一致性

- 标签上方；
- 字段间距 `space-4`；
- 主按钮在右下，宽度 = 100% 在移动；
- 副按钮（如「Google 继续」/「忘记密码」）放在表单顶部 + 底部，移动端折叠到顶部；
- 错误内联在字段下方，4xx 不弹 Toast；5xx 才弹 Toast（按 [B03 §05](../../B03-design/design-system/05-interactions.md)）。

## 3. 4 态约定

每个页面必须明确：
- `idle`：默认渲染态；
- `submitting`：按钮 loading + disabled，表单字段 readonly；
- `error`：内联（4xx）或 Toast（5xx）；
- 特殊态：每页根据流程列出（如登录页 `kicked-back`、`sent`、`token-invalid` 等）。

## 4. 顶栏在认证页的呈现

- 未登录：右上角「登录」「注册」两个文字按钮；
- 已登录但在 `/auth/*` 页：右上角变回头像下拉，菜单项「我的资料 / 退出登录」（即使错误访问到登录页也允许直接退出）；
- 主题切换 / 语言切换在认证页**仍可用**。

## 5. 状态机重点

- 登录 / 注册按钮"防重复提交"由 `useAsyncAction` 统一封装；
- 验证邮件「重新发送」按钮带 60s 倒计时（节流双层：前端 + 后端）；
- 忘记密码「发送链接」同样 60s 倒计时；
- 修改密码成功后**保留当前会话**，弹 Toast 后跳回 `/me`；
- 全部设备登出 → 跳 `/auth/login`。

## 6. 错误页

- `/401`、`/403`、`/404` 见 [B03 §02](../../B03-design/design-system/02-layout.md)，本 feature 不重新设计；
- `/auth/link-expired` **不**独立成路由，而是作为 `/auth/callback` 与 `/auth/reset-password` 的子状态展示。
