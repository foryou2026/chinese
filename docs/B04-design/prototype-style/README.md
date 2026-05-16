<!-- TARGET-PATH: docs/B04-design/prototype-style/README.md -->

# B04 · 原型样式 prototype-style（占位）

> **冻结状态**：占位 · 待 C04 第一次原型时填充 · 2026-04-28

---

## 0. 用途

本目录存放**所有 C04 HTML 原型共享**的 CSS / JS 资产，从 [`B04-design/design-system`](../design-system/) 翻译成可直接 `<link>` 与 `<script>` 引入的静态文件，目的是：

- 让 C04 单页 HTML 原型可以**离线打开**（双击 `index.html` 即看效果）；
- 让 AI 在 C04 阶段生成原型时，**不需要重新发明 CSS**，直接 `<link href="./_shared/tokens.css">` 即可拿到设计系统；
- 让原型与最终产品视觉**一致**——本目录的 CSS 与 `system/packages/ui-kit/src/tokens/` 是同一份内容的两种载体（一个是 React、一个是纯 HTML）。

---

## 1. 文件清单（待 C04 首次产物时填充）

| 文件 | 职责 | 来源 |
|------|------|------|
| [`tokens.css`](./tokens.css) | CSS 变量：颜色 / 字体 / 间距 / 圆角 / 阴影 / 毛玻璃 / 动效 | 翻译自 [`design-system/01-tokens.md`](../design-system/01-tokens.md) |
| [`themes.css`](./themes.css) | `[data-theme="light"]` / `[data-theme="dark"]` 主题切换 | 翻译自 [`design-system/06-responsive-dark.md`](../design-system/06-responsive-dark.md) |
| [`app.css`](./app.css) | 组件类（`.glass-panel` / `.glass-nav` / `.btn-primary` / `.input` 等）+ 布局类（`.page` / `.page-header` 等）| 翻译自 [`design-system/02-layout.md`](../design-system/02-layout.md) / [`04-status-components.md`](../design-system/04-status-components.md) |
| [`app.js`](./app.js) | 主题切换脚本 + 全局快捷键 + 简单的交互模拟（按钮 loading / Toast 出现 / Modal 打开）| 翻译自 [`design-system/05-interactions.md`](../design-system/05-interactions.md) |

---

## 2. C04 使用约定

C04 阶段产物（HTML 原型）必须在 `<head>` 内按顺序引入：

```html
<link rel="stylesheet" href="../../../B04-design/prototype-style/tokens.css">
<link rel="stylesheet" href="../../../B04-design/prototype-style/themes.css">
<link rel="stylesheet" href="../../../B04-design/prototype-style/app.css">
<script defer src="../../../B04-design/prototype-style/app.js"></script>
```

并在 `<body>` 加 `<body data-theme="light">`（首屏 FOUC 由 `app.js` 内联脚本接管）。

---

## 3. 当前状态

- ✋ **占位**：本目录文件**尚未填充**；将在 C04 第一次产出 HTML 原型时由该次 C04 任务一并落地。
- ✋ 占位文件已建立空骨架，详见 [tokens.css](./tokens.css) / [themes.css](./themes.css) / [app.css](./app.css) / [app.js](./app.js) 顶部注释。
- ✋ 此约定与框架 `prompt/A-framework/A00-04-文档目录规划.md`「设计系统先冻结、原型样式随首个 C04 落地」一致。

---

## 4. 变更约束

- 一旦 C04 首次填充本目录后，所有后续 C04 / 业务原型必须**只**使用本目录提供的 class / variable；不允许在单个原型 HTML 内重新定义 token / 自创组件 class。
- 本目录与 `system/packages/ui-kit/src/tokens/` 必须**保持一致**；任一侧修改必须在 PR 中同步另一侧，并更新 [`docs/A00-meta/changelog.md`](../../A00-meta/changelog.md)。
