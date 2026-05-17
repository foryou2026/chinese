<!-- TARGET-PATH: docs/B03-design/prototype-style/README.md -->

# B03 · 原型样式 prototype-style

> **冻结状态**:**v1.0 已填充** · 2026-05-16(随批次 3/4 C04 补登)

---

## 0. 用途

存放所有 C04 HTML 原型共享的 CSS / JS 资产,从 [`B03-design/design-system`](../design-system/) 翻译成可直接 `<link>` / `<script>` 的静态文件。

---

## 1. 文件清单

| 文件 | 职责 | 来源 |
|------|------|------|
| [`tokens.css`](./tokens.css) | CSS 变量(颜色 / 字体 / 间距 / 圆角 / 阴影 / 毛玻璃 / 动效)| [`design-system/01-tokens.md`](../design-system/01-tokens.md) |
| [`themes.css`](./themes.css) | `[data-theme="dark"]` 覆盖 + `prefers-reduced-motion` | [`design-system/07-responsive-dark.md`](../design-system/07-responsive-dark.md) |
| [`app.css`](./app.css) | 全局 reset + `.glass-*` / `.btn-*` / `.input` / `.toast` / `.skeleton` / `.proto-switcher` / `.env-badge` 等组件类 | [`design-system/02-layout.md`](../design-system/02-layout.md) + [`04-status-colors.md`](../design-system/04-status-colors.md) |
| [`app.js`](./app.js) | `window.proto.*` 全局 API:`bootstrap` / `setTheme` / `toggleTheme` / `toast` / `cooldown` / `devtools.mountStateSwitcher` | [`design-system/06-interactions.md`](../design-system/06-interactions.md) |

---

## 2. C04 使用约定

> **铁律**:C04 原型**极简平铺**(一个页面 = 一个默认态 HTML,平铺在 `<surface>/` 根下),且**严禁**在 feature 目录下拷贝本目录任何文件(`vendor/`、`assets/styles.css`、`assets/app.css`、`feature.css`、`feature.js`、`mock-data.js` 等皆禁)。所有 HTML 通过相对路径**直接引用**本目录,保证全仓单一来源、修改即时生效。详见 [/prompt/C-product/C05-H03-AI输出-HTML原型规范.md](../../../prompt/C-product/C05-H03-AI输出-HTML原型规范.md) §0 / §硬约束。

### 2.1 统一深度:`<surface>/index.html` 与 `<surface>/<page-id>.html` 均位于 docs/ 下 3 层

```html
<link rel="stylesheet" href="../../../B03-design/prototype-style/tokens.css">
<link rel="stylesheet" href="../../../B03-design/prototype-style/themes.css">
<link rel="stylesheet" href="../../../B03-design/prototype-style/app.css">
<script defer src="../../../B03-design/prototype-style/app.js"></script>
```

并在 `<body>` 末尾:`<script>proto.bootstrap();</script>`

页面级微调样式 / 微交互一律内联在该 HTML 的 `<style>` / `<script>` 中;页面示例数据直接写在 HTML 静态片段(业务语言),**不**产出 `mock-data.js` / `feature.css` / `feature.js`。

### 2.2 feature 专属样式包(按需)

若 feature 沿用一套已成型的视觉结构(类名 / 主题),允许在 `docs/B03-design/prototype-style/<feature>/` 下放置该 feature 专属的 `styles.css` / `prototype.js`,HTML 引用路径与通用包同样为 `../../../B03-design/prototype-style/<feature>/X`(3 ups)。仍然**只引用、不拷贝**。

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
- C04 feature 目录下**禁止**出现本目录文件的副本(`vendor/`、`assets/styles.css` 等);如需调整全局样式必须直接改本目录,所有 feature 引用立即生效。
