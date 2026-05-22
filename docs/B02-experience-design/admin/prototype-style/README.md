# admin 原型样式包

admin 管理后台的专属原型样式包。风格：**Minimal Ink + Frost** — 飞书/Notion 极简专业 + 克制毛玻璃。

## 引入方式

```html
<link rel="stylesheet" href="path/to/admin/prototype-style/app.css">
<script src="path/to/admin/prototype-style/app.js"></script>
<script>if(typeof proto !== 'undefined') proto.bootstrap();</script>
```

## DOM 标记

```html
<html lang="zh-CN" data-mode="light" data-density="default">
```

| 轴 | 属性 | 取值 | 默认 |
|----|------|------|------|
| 模式 | `data-mode` | light / dark / auto | light |
| 密度 | `data-density` | default / compact | default |

> admin 无 `data-accent` 轴（无主题色切换）。

## 文件清单

| 文件 | 职责 |
|------|------|
| tokens.css | 颜色/字体/间距/圆角/阴影/动效/毛玻璃 CSS 变量 |
| themes.css | 暗色模式覆盖（含 glass token dark 覆盖）+ auto 跟随系统 |
| app.css | 汇总入口（7 个 @import） |
| app.js | 主题切换 + toast/modal/drawer/dropdown |
| parts/01-base.css | reset + 毛玻璃卡片 + 排版 + 容器 + 页面渐变底色 |
| parts/02-buttons.css | Primary(黑/白) + Secondary(毛玻璃) + Ghost + 状态按钮 |
| parts/03-inputs.css | 输入框/下拉/文本域（毛玻璃边框风格） |
| parts/04-overlays.css | Modal + Drawer + Dropdown + Tooltip（毛玻璃弹层） |
| parts/05-feedback.css | Toast(毛玻璃) + Alert(毛玻璃) + Banner |
| parts/06-loading.css | Skeleton(毛玻璃) + ProgressBar + Empty(毛玻璃) |
| parts/07-theme-switcher.css | 模式/密度切换器（毛玻璃） |

## 毛玻璃策略

admin 的毛玻璃是**克制、低饱和**的，与 app 的高饱和/高模糊做明确区分：

| 层级 | Token | 典型用途 |
|------|-------|---------|
| 基础 | `--glass-blur-sm` blur(12px) saturate(1.2) | 输入框、按钮、小控件 |
| 标准 | `--glass-blur` blur(20px) saturate(1.4) | 卡片、侧边栏、顶栏 |
| 提升 | `--glass-blur-lg` blur(28px) saturate(1.5) | Modal、Drawer、Toast |

页面底色使用 `#F3F4F6` + 微弱径向渐变（`.admin-page-bg`），让毛玻璃层可感知。

## 红线规则

1. Primary 按钮亮色必须为纯黑 #18181B，暗色必须为纯白 #FAFAFA
2. 所有颜色必须走 CSS 变量
3. 动效不超过 200ms
4. 无装饰性动画（无 float、无 drift、无 mesh-gradient）
5. 毛玻璃饱和度 ≤ 1.5（区别于 app 的 1.8）
6. 必须提供 `@supports not (backdrop-filter)` 回退
