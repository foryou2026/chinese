<!-- TARGET-PATH: docs/B04-design/prototype-style/README.md -->

# B04 · 原型样式 prototype-style

> **冻结状态**:**v1.0 已填充** · 2026-05-16(随批次 3/4 C04 补登)

---

## 0. 用途

存放所有 C04 HTML 原型共享的 CSS / JS 资产,从 [`B04-design/design-system`](../design-system/) 翻译成可直接 `<link>` / `<script>` 的静态文件。

---

## 1. 文件清单

| 文件 | 职责 | 来源 |
|------|------|------|
| [`tokens.css`](./tokens.css) | CSS 变量(颜色 / 字体 / 间距 / 圆角 / 阴影 / 毛玻璃 / 动效)| [`design-system/01-tokens.md`](../design-system/01-tokens.md) |
| [`themes.css`](./themes.css) | `[data-theme="dark"]` 覆盖 + `prefers-reduced-motion` | [`design-system/06-responsive-dark.md`](../design-system/06-responsive-dark.md) |
| [`app.css`](./app.css) | 全局 reset + `.glass-*` / `.btn-*` / `.input` / `.toast` / `.skeleton` / `.proto-switcher` / `.env-badge` 等组件类 | [`design-system/02-layout.md`](../design-system/02-layout.md) + [`04-status-components.md`](../design-system/04-status-components.md) |
| [`app.js`](./app.js) | `window.proto.*` 全局 API:`bootstrap` / `setTheme` / `toggleTheme` / `toast` / `cooldown` / `devtools.mountStateSwitcher` | [`design-system/05-interactions.md`](../design-system/05-interactions.md) |

---

## 2. C04 使用约定

C04 阶段产物每个 feature 目录下必须有 `vendor/proto-style/`,**字节级**全量拷自本目录:

```bash
cp -R docs/B04-design/prototype-style/{tokens.css,themes.css,app.css,app.js} \
      docs/C04-prototype/<feature-id>/vendor/proto-style/
```

页面以相对路径引入:

```html
<link rel="stylesheet" href="../vendor/proto-style/tokens.css">
<link rel="stylesheet" href="../vendor/proto-style/themes.css">
<link rel="stylesheet" href="../vendor/proto-style/app.css">
<link rel="stylesheet" href="../feature.css">
<script defer src="../vendor/proto-style/app.js"></script>
<script defer src="../mock-data.js"></script>
<script defer src="../feature.js"></script>
```

并在 `<body>` 末尾:`<script>proto.bootstrap();</script>`

---

## 3. `proto.*` 公共 API

| API | 说明 |
|-----|------|
| `proto.bootstrap()` | 一次性挂载:环境徽标 / 主题按钮绑定 / 滚动阴影 / 快捷键 / 表单 mock / 状态切换浮窗 |
| `proto.setTheme('light'\|'dark')` | 切换主题并写入 localStorage |
| `proto.toggleTheme()` | 反转当前主题 |
| `proto.toast({ type, msg, duration })` | type ∈ success/error/warning/info;栈上限 3 |
| `proto.cooldown(btnEl, seconds, '{s} 秒后可重试')` | 倒计时禁用按钮;`{s}` ≥ 60 自动 mm:ss 格式 |
| `proto.devtools.mountStateSwitcher()` | 读取页面 `<meta name="proto:page-id">` / `proto:state` / `proto:states` 渲染右上角状态切换胶囊 |
| `proto.on('theme-change', fn)` | 监听主题变化 |

---

## 4. 变更约束

- 一旦填充后,所有 C04 / 业务原型必须**只**使用本目录提供的 class / variable;不允许在单个原型 HTML 内重新定义 token / 自创组件 class。
- 本目录与 `system/packages/ui-kit/src/tokens/` 必须**保持一致**;任一侧修改必须同步另一侧并更新 [`docs/A00-meta/changelog.md`](../../A00-meta/changelog.md)。
- 各 feature 的 `vendor/proto-style/` 内文件**禁止**编辑;只能从本目录重拷。
