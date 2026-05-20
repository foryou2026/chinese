# 响应式与暗黑模式

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：01-tokens.md, 02-layout.md
> **冻结状态**：未冻结

---

## 断点行为

| 组件/模式 | <480px (mobile) | 480-767px (sm) | 768-1023px (md) | 1024-1279px (lg) | ≥1280px (xl+) |
|----------|----------------|----------------|-----------------|------------------|---------------|
| app 导航 | BottomBar | BottomBar | BottomBar | TopBar | TopBar |
| admin 导航 | 汉堡+抽屉 | 汉堡+抽屉 | 汉堡+抽屉 | SideBar折叠 | SideBar展开 |
| 表格 | 卡片列表 | 卡片列表 | 横向滚动 | 完整表格 | 完整表格 |
| Modal | 全屏 | 全屏 | 居中弹窗(.glass) | 居中弹窗(.glass) | 居中弹窗(.glass) |
| Form | 单列全宽 | 单列全宽 | 双列 | 双列 | 双列 |
| 按钮组 | 纵向堆叠全宽 | 横向排列 | 横向排列 | 横向排列 | 横向排列 |
| 容器内边距 | 24px | 24px | 28px | 36px | 48px~96px |
| 毛玻璃 blur | 16px (减负) | 22px | 22px | 22px | 22px |

---

## DOM 三轴标记

| 轴 | 属性 | 取值 | 默认 |
|----|------|------|------|
| 模式 | `data-mode` | light / dark / auto | auto |
| 主题色 | `data-accent` | ink / cinnabar / jade / gold / graphite | ink |
| 密度 | `data-density` | default / compact / elder | default |

> 三轴均在 `<html>` 元素上设置，JS 初始化时从 localStorage 读取或使用默认值。
> 任意组合皆有效，运行时切换。详见 `prototype-style/app.js` 中 `window.proto`。

---

## 暗黑模式 — 宣纸→墨夜映射

### 页面背景

| 属性 | Light | Dark |
|------|-------|------|
| `--bg-page` | `#F8F2E0 → #F2EBD3 → #E8EFF5` (宣纸→月白瓷) | `#0B1626 → #102040 → #14304F` (墨夜渐变) |
| `--bg-page-glow` | 鎏金+墨青微光 | 同源降透至 40% |
| `--paper-grain-opacity` | 0.06 | 0.03 (暗底减弱纸纹) |

### 中性灰阶反转

| Token | Light | Dark |
|-------|-------|------|
| `--color-neutral-0` | #FFFBF0 (暖白) | #0B1020 (墨底) |
| `--color-neutral-50` | #F8F2E0 | #14243C |
| `--color-neutral-100` | #F0E8D2 | #1B3050 |
| `--color-neutral-200` | #E5DCC7 | #243C60 |
| `--color-neutral-300` | #C5BBA8 | #3A5070 |
| `--color-neutral-400` | #9C9080 | #6A809A |
| `--color-neutral-500` | #6F6452 | #90A0B0 |
| `--color-neutral-600` | #56493A | #B0C0D0 |
| `--color-neutral-700` | #3D3327 | #D0DCE8 |
| `--color-neutral-800` | #2A2218 | #E0E8F0 |
| `--color-neutral-900` | #1F1A14 | #F0F4F8 |
| `--color-neutral-950` | #100D0A | #F8FAFB |

### 品牌色调整

| Token | Light | Dark | 原因 |
|-------|-------|------|------|
| `--color-brand-default` | brand-700 | brand-400 | 暗底提升对比度 |
| `--color-brand-hover` | brand-600 | brand-300 | 同上 |
| `--color-brand-active` | brand-800 | brand-500 | 同上 |
| `--color-brand-on` | neutral-0 | neutral-950 | 反色文字 |
| `--color-brand-ring` | `rgba(46,92,138,.18)` | `rgba(168,192,212,.25)` | 暗底提亮环 |

### 毛玻璃参数

| Token | Light | Dark |
|-------|-------|------|
| `--glass-1` | `rgba(255,251,240, 0.55)` | `rgba(14, 36, 62, 0.55)` |
| `--glass-2` | `rgba(255,251,240, 0.72)` | `rgba(14, 36, 62, 0.72)` |
| `--glass-3` | `rgba(255,251,240, 0.42)` | `rgba(14, 36, 62, 0.42)` |
| `--glass-tint` | `rgba(207,221,232, 0.45)` | `rgba(46, 92, 138, 0.30)` |
| `--glass-dark` | `rgba(20, 48, 79, 0.78)` | `rgba(8, 20, 38, 0.85)` |
| `--glass-border` | `rgba(255,250,235, 0.78)` | `rgba(168,192,212, 0.12)` |
| `--glass-border-strong` | `rgba(255,250,235, 0.92)` | `rgba(168,192,212, 0.22)` |
| `--glass-shadow` | `inset + 0.14 rgba` | 阴影降低至 0.06 + 暗调 inset |

### 状态色

| 状态 | Light 文字 | Dark 文字 | Light 背景 | Dark 背景 |
|------|-----------|-----------|-----------|-----------|
| success 翠玉 | #4A6F5A | #C9DCD2 | #E5EFE9 | `rgba(74,111,90, 0.18)` |
| warning 鎏金 | #B8923A | #E8D5A8 | #F4ECD8 | `rgba(184,146,58, 0.18)` |
| danger 朱砂 | #B14545 | #EAC0B8 | #F5E0DC | `rgba(177,69,69, 0.18)` |
| info 青花 | #2E5C8A | #CFDDE8 | #E8EFF5 | `rgba(46,92,138, 0.18)` |

> 暗色模式下文字用 -100 级（提亮），背景用 18% 透明度半透。

### 阴影策略

| Light | Dark |
|-------|------|
| `box-shadow: var(--shadow-*)` 墨色淡阴影 | 阴影 rgba 降至 0.06；`--glass-shadow` inset 高光改为暗调边光 |

---

## CSS 实现

完整暗色覆盖定义在 `prototype-style/themes.css` 中 `[data-mode="dark"]` 选择器内。

auto 模式实现：

```css
@media (prefers-color-scheme: dark) {
  [data-mode="auto"] {
    /* 复制 [data-mode="dark"] 全部 token 覆盖 */
  }
}
```

---

## 密度切换

| Token | default | compact | elder |
|-------|---------|---------|-------|
| `--space-3` | 12px | 8px | 16px |
| `--space-4` | 16px | 12px | 22px |
| `--space-5` | 20px | 16px | 28px |
| `--space-6` | 24px | 22px | 36px |
| `--text-base` | 17px | 15px | 20px |
| `--text-md` | 19px | 16px | 22px |
| `--text-lg` | 24px | 24px | 26px |
| `--container-pad` | 响应式阶梯 | 16px | 32px |

---

## 五色主题

通过 `[data-accent]` 切换品牌色族：

| accent | 色名 | 主色 -500 | 用途 |
|--------|------|-----------|------|
| ink | 墨青 | #2E5C8A | 默认，稳重知性 |
| cinnabar | 朱砂 | #B14545 | 热烈，节庆 |
| jade | 翠玉 | #4A6F5A | 清新，自然 |
| gold | 鎏金 | #B8923A | 典雅，尊贵 |
| graphite | 水墨 | #4A4A4A | 极简，专注 |

每套 accent 在 `themes.css` 中覆盖 `--color-brand-50`~`--color-brand-900` 全色阶 + 语义别名（default/hover/active/on/ring）。

---

## 99. 待确认问题

无
