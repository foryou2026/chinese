# 原型样式包

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **冻结状态**：未冻结

---

## 引入方式

HEAD 区：
```html
<link rel="stylesheet" href="<相对路径>/prototype-style/app.css">
```

BODY 末尾（顺序加载，禁 defer）：
```html
<script src="<相对路径>/prototype-style/app.js"></script>
<script>proto.bootstrap();</script>
```

页面级微调一律内联 `<style>` / `<script>`。

## 命名空间

- CSS：`--color-* / --space-* / --text-* / --radius-* / --shadow-* / --motion-* / --z-* / --font-* / --ease-*`
- JS：`window.proto`（bootstrap / switchTheme / toast / modal / drawer / dropdown）

## DOM 三轴标记

| 轴 | 取值 | DOM |
|----|------|-----|
| 模式 | light / dark / auto | `<html data-mode>` |
| 主题色 | accent-1 | `<html data-accent>` |
| 密度 | default / compact | `<html data-density>` |

## 文件清单

| 文件 | 职责 |
|------|------|
| tokens.css | 与 design-system/01-tokens.md 逐字一致的 CSS 变量 |
| themes.css | 暗黑/密度覆写 |
| parts/01-base.css | reset + 排版 + 基础元素 |
| parts/02-buttons.css | 按钮 6 态 + 异常态 |
| parts/03-inputs.css | 输入组件 6 态 + 异常态 |
| parts/04-overlays.css | Modal/Drawer/Popover/Tooltip/Dropdown |
| parts/05-feedback.css | Toast/Alert/Banner |
| parts/06-loading.css | Skeleton/Spinner/ProgressBar/Empty |
| parts/07-theme-switcher.css | 主题切换按钮样式 |
| app.css | @import 汇总 |
| app.js | window.proto，纯 vanilla，零依赖 |

## 红线

1. 严禁重定义 token（只在 tokens.css 和 themes.css 中定义）
2. 严禁写死 hex/px（必须引用 CSS 变量）
3. 可聚焦元素必须可见焦点环（:focus-visible）
4. 必须支持 prefers-reduced-motion: reduce
