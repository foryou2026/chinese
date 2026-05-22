# app 原型样式包

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **冻结状态**：未冻结

---

## 风格

**Quest Glass** — 多邻国游戏化闯关感 + 毛玻璃增强品质层次。

## 引入方式

HEAD 区：
```html
<link rel="stylesheet" href="<相对路径>/app/prototype-style/app.css">
```

BODY 末尾（顺序加载，禁 defer）：
```html
<script src="<相对路径>/app/prototype-style/app.js"></script>
<script>proto.bootstrap();</script>
```

页面级微调一律内联 `<style>` / `<script>`。

## 命名空间

- CSS：`--color-* / --space-* / --text-* / --lh-* / --radius-* / --shadow-* / --motion-* / --z-* / --font-* / --glass-* / --page-bg / --mesh-*`
- JS：`window.proto`（bootstrap / switchTheme / switchAccent / switchDensity / toast / modal / drawer / dropdown）

## DOM 三轴标记

| 轴 | 取值 | DOM |
|----|------|-----|
| 模式 | light / dark / auto | `<html data-mode>` |
| 主题色 | indigo / rose / emerald / amber / violet | `<html data-accent>` |
| 密度 | default / compact / elder | `<html data-density>` |

任意组合皆有效，运行时切换。

## 文件清单

| 文件 | 职责 |
|------|------|
| tokens.css | 与 design-system/01-tokens.md 逐字一致的 CSS 变量 |
| themes.css | 5 套 accent 覆盖 + 暗色模式 + auto 跟随系统 |
| parts/01-base.css | reset + 极光 mesh gradient 背景 + 毛玻璃面板 + 游戏化动效 + 排版 + 容器 |
| parts/02-buttons.css | 3D 弹跳按钮 + Glass/Ghost/状态按钮 |
| parts/03-inputs.css | 毛玻璃输入组件 6 态 + 异常态 |
| parts/04-overlays.css | 毛玻璃 Modal / Drawer / Popover / Tooltip / Dropdown |
| parts/05-feedback.css | 毛玻璃 Toast / Alert / Banner |
| parts/06-loading.css | Skeleton / Spinner / ProgressBar / Empty |
| parts/07-theme-switcher.css | 模式 + 主题色 + 密度 切换按钮样式 |
| app.css | @import 汇总 |
| app.js | window.proto，纯 vanilla，零依赖，三轴切换 |

## 红线

1. 严禁重定义 token（只在 tokens.css 和 themes.css 中定义）
2. 严禁写死 hex/px（必须引用 CSS 变量）
3. 严禁直接引用具体色族（如 `--color-indigo-700`）；只用 `--color-brand-*`
4. 严禁正文/表单使用楷体/宋体（`--font-brush` 仅限品牌 Logo）
5. 可聚焦元素必须可见焦点环（:focus-visible → `--focus-ring`）
6. 必须支持 prefers-reduced-motion: reduce
7. Primary 按钮必须有 3D 底部阴影（多邻国风格弹跳按钮）
8. 所有浮起容器必须使用 `backdrop-filter` 毛玻璃
