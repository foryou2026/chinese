<!-- TARGET-PATH: docs/B04-design/design-system/01-tokens.md -->

# 01 · 设计 Token

> **阶段**：B04-S  
> **上游**：`B03-ux/05-moodboard.md`、`_input/visual-input.md`  
> **下游**：`system/packages/ui-kit/src/tokens/{tokens.css, tokens.ts, theme.css}`、所有 C 阶段产物  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- **唯一彩色 = 红**；亮模式 `#FF2442` / 暗模式 `#FF3B5C`（小红书红）。
- **5 套 token 矩阵**：颜色 / 字体 / 间距 / 圆角 / 阴影 / 毛玻璃 / 动效。
- 命名采用 CSS 变量优先，配合 `data-theme="light|dark"` 实时切换；TS 端用 `getToken('color.brand')` 读取。
- 所有页面 / 组件**禁止硬编码颜色 / 字号 / 圆角**；新增 token 必须先改本文件 + Storybook。

---

## 1. 颜色

### 1.1 中性色

| Token | 亮模式 | 暗模式 | 场景 |
|-------|--------|--------|------|
| `--bg-app` | `#FFFFFF` | `#0A0A0B` | 页面底色（远景层之下）|
| `--bg-app-tint` | `#F6F6F7` | `#111114` | 顶栏后方"远景"渐变底 |
| `--bg-surface` | `rgba(255,255,255,0.62)` | `rgba(18,18,22,0.55)` | **毛玻璃面板主底色** |
| `--bg-surface-strong` | `rgba(255,255,255,0.82)` | `rgba(20,20,24,0.78)` | 强毛玻璃（弹窗 / Drawer）|
| `--bg-overlay` | `rgba(0,0,0,0.32)` | `rgba(0,0,0,0.55)` | 遮罩层 |
| `--bg-hover` | `rgba(0,0,0,0.04)` | `rgba(255,255,255,0.06)` | 列表项 hover |
| `--bg-active` | `rgba(0,0,0,0.08)` | `rgba(255,255,255,0.10)` | 列表项 active / 选中浅底 |
| `--text-primary` | `#0E0E11` | `#F4F4F5` | 标题 / 正文 |
| `--text-secondary` | `#52525B` | `#A1A1AA` | 描述 / 辅助 |
| `--text-tertiary` | `#9A9AA3` | `#6B6B73` | 占位 / 时间戳 |
| `--text-disabled` | `#C7C7CC` | `#4A4A52` | 禁用 |
| `--text-on-brand` | `#FFFFFF` | `#FFFFFF` | 红底上的文字 |
| `--border-subtle` | `rgba(15,15,20,0.08)` | `rgba(255,255,255,0.10)` | 毛玻璃内边框 / 分割线 |
| `--border-strong` | `rgba(15,15,20,0.18)` | `rgba(255,255,255,0.22)` | 输入框边框 |
| `--ring` | `rgba(255,36,66,0.45)` | `rgba(255,59,92,0.55)` | focus ring |

### 1.2 品牌红

| Token | 亮模式 | 暗模式 | 场景 |
|-------|--------|--------|------|
| `--brand` | `#FF2442` | `#FF3B5C` | 主按钮 / 链接 / 选中态 / Logo |
| `--brand-hover` | `#E61E3B` | `#FF5470` | 主按钮 hover |
| `--brand-active` | `#CC1A34` | `#E62945` | 主按钮 active |
| `--brand-soft` | `rgba(255,36,66,0.10)` | `rgba(255,59,92,0.14)` | 选中行浅底 / Tag 底 |
| `--brand-soft-strong` | `rgba(255,36,66,0.18)` | `rgba(255,59,92,0.22)` | hover 浅底 |
| `--brand-on` | `#FFFFFF` | `#FFFFFF` | 红底上文字 |

> 用户可在「设置 → 显示 → 主题色」覆盖全套品牌色变量；详见 [06-responsive-dark §5](./06-responsive-dark.md)。

### 1.3 语义色（不破坏黑白红基调）

| Token | 亮模式 | 暗模式 | 用途 |
|-------|--------|--------|------|
| `--success` | `#16A34A` | `#22C55E` | 成功文字 / 图标（**不**用大面积底色）|
| `--success-soft` | `rgba(22,163,74,0.10)` | `rgba(34,197,94,0.16)` | 成功 Tag 底 |
| `--warning` | `#D97706` | `#F59E0B` | 警告文字 / 图标 |
| `--warning-soft` | `rgba(217,119,6,0.10)` | `rgba(245,158,11,0.16)` | 警告 Tag 底 |
| `--danger` | `var(--brand)` | `var(--brand)` | **复用品牌红**：错误 / 删除 / 拒绝 |
| `--danger-soft` | `var(--brand-soft)` | `var(--brand-soft)` | 错误 Tag 底 |
| `--info` | `var(--text-secondary)` | `var(--text-secondary)` | 一般信息（不引入蓝色）|

---

## 2. 字体

### 2.1 字体栈

```css
--font-sans: "Inter", "Be Vietnam Pro", "Noto Sans Thai Looped",
             "Noto Sans SC", system-ui, -apple-system, "Segoe UI",
             Roboto, "Helvetica Neue", Arial, sans-serif;
--font-serif: "Noto Serif SC", "Source Han Serif SC", Georgia, serif;
--font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

字体托管详见 [`B01-architecture/07-i18n-responsive.md`](../../B01-architecture/07-i18n-responsive.md)。

### 2.2 文本规模

| Token | 字号 | 字重 | 行高 | 用途 |
|-------|------|------|------|------|
| `text-display` | 36px | 700 | 1.2 | 营销页超大标题 |
| `text-h1` | 28px | 700 | 1.25 | 页面标题 |
| `text-h2` | 22px | 600 | 1.3 | 卡片 / 区域标题 |
| `text-h3` | 18px | 600 | 1.35 | 子标题 / 抽屉标题 |
| `text-body` | 14px | 400 | 1.6 | 正文（移动 ≥ 14px）|
| `text-body-lg` | 16px | 400 | 1.6 | 长阅读（小说 / 课程详文）|
| `text-caption` | 12px | 400 | 1.5 | 辅助 / 时间戳 |
| `text-table` | 14px | 400 | 1.5 | 表格内容 |
| `text-button` | 14px | 500 | 1 | 按钮文字 |
| `text-tag` | 12px | 500 | 1 | 状态 / 标签 |

> 中文教学场景（汉字卡片 / 释义页）使用 `--font-serif`；其余 UI 一律 `--font-sans`。

---

## 3. 间距、圆角、阴影

### 3.1 间距（4px grid）

| Token | 值 | 适用 |
|-------|---|------|
| `space-1` | 4px | 紧凑相邻 |
| `space-2` | 8px | 控件内 / icon-text |
| `space-3` | 12px | 表单字段间隔 |
| `space-4` | 16px | 卡片内边距 / 按钮间距 |
| `space-5` | 24px | 区块间距 |
| `space-6` | 32px | 大区块 / 页面区段 |
| `space-7` | 48px | hero 区 |
| `space-page-x-mobile` | 16px | 移动端页面左右内边距 |
| `space-page-x-desktop` | 32px | 桌面端页面左右内边距 |
| `space-page-y` | 24px | 页顶到导航栏 |

### 3.2 圆角

| Token | 值 | 适用 |
|-------|---|------|
| `radius-sm` | 6px | 按钮 / 输入框 / Tag |
| `radius-md` | 12px | 卡片 / Toast / 下拉 |
| `radius-lg` | 18px | 弹窗 / Drawer / 毛玻璃大面板 |
| `radius-pill` | 9999px | 头像 / Pill 按钮 / 徽标 |

### 3.3 阴影（毛玻璃叠加专用）

| Token | 亮模式 | 暗模式 | 适用 |
|-------|--------|--------|------|
| `shadow-sm` | `0 1px 2px rgba(15,15,20,0.04), 0 1px 1px rgba(15,15,20,0.03)` | `0 1px 2px rgba(0,0,0,0.50)` | 按钮 / 输入 |
| `shadow-md` | `0 6px 18px rgba(15,15,20,0.08)` | `0 6px 18px rgba(0,0,0,0.55)` | 下拉 / Toast |
| `shadow-lg` | `0 18px 48px rgba(15,15,20,0.14)` | `0 18px 48px rgba(0,0,0,0.65)` | 弹窗 / Drawer |
| `shadow-glass-edge` | `inset 0 1px 0 rgba(255,255,255,0.40)` | `inset 0 1px 0 rgba(255,255,255,0.06)` | **毛玻璃顶部高光（关键质感）** |

---

## 4. 毛玻璃面板 token（核心质感）

> 每个毛玻璃组件由 4 个图层组成：**远景渐变底 → backdrop-filter 模糊 → 半透明面色 → 顶部 1px 高光内边**。
> 灵感来源：B03 moodboard 中"中等玻璃 / 顶部 1px 高光 / 微噪 2.5%"。

### 4.1 变量

| Token | 亮模式 | 暗模式 | 说明 |
|-------|--------|--------|------|
| `--glass-blur-sm` | `blur(10px) saturate(140%)` | 同 | 按钮 / Tag |
| `--glass-blur-md` | `blur(18px) saturate(150%)` | 同 | 卡片 / 导航 / Toast |
| `--glass-blur-lg` | `blur(28px) saturate(160%)` | 同 | 弹窗 / Drawer |
| `--glass-bg` | `var(--bg-surface)` | 同 | 主面板色（含 alpha）|
| `--glass-bg-strong` | `var(--bg-surface-strong)` | 同 | 强毛玻璃 |
| `--glass-border` | `1px solid var(--border-subtle)` | 同 | 内边框 |
| `--glass-edge` | `var(--shadow-glass-edge)` | 同 | 顶部高光 |
| `--glass-noise-opacity` | `0.025` | `0.04` | 微噪强度 |

### 4.2 工具类（Tailwind 4 `@layer components`）

```css
.glass-panel  { background: var(--glass-bg); backdrop-filter: var(--glass-blur-md);
                -webkit-backdrop-filter: var(--glass-blur-md); border: var(--glass-border);
                box-shadow: var(--shadow-md), var(--glass-edge); border-radius: var(--radius-lg); }
.glass-nav    { @apply glass-panel; backdrop-filter: var(--glass-blur-md); border-radius: 0; }
.glass-card   { @apply glass-panel; }
.glass-modal  { @apply glass-panel; background: var(--glass-bg-strong);
                backdrop-filter: var(--glass-blur-lg); box-shadow: var(--shadow-lg), var(--glass-edge); }
.glass-button { @apply glass-panel; backdrop-filter: var(--glass-blur-sm);
                border-radius: var(--radius-sm); box-shadow: var(--shadow-sm), var(--glass-edge); }
.glass-toast  { @apply glass-panel; }
.glass-tab    { @apply glass-panel; border-radius: var(--radius-pill); }
```

### 4.3 强制实施约束

1. **页面背景必须有"远景"**：纯白 / 纯黑会让毛玻璃失效。`<body>` 默认绘制 `--bg-app` + 微噪 + 偏移红色径向光斑（透明度 8%）；见 [02-layout §3](./02-layout.md)。
2. **不允许 `background: white/black` 的卡片**：必须使用 `.glass-*` 系列。
3. **降级**：浏览器不支持 `backdrop-filter` → 落 `--bg-surface-strong` + `shadow-md`。
4. **不嵌套**：毛玻璃面板内禁止再嵌套毛玻璃；如需层次用 `--bg-hover` / `--bg-active`。
5. **性能**：低端设备 / 用户主动选「省电模式」→ 切伪毛玻璃。详见 [06 §4](./06-responsive-dark.md)。

---

## 5. 动效

| Token | 值 | 用途 |
|-------|---|------|
| `--motion-fast` | `120ms cubic-bezier(0.2,0.8,0.2,1)` | hover / focus |
| `--motion-base` | `200ms cubic-bezier(0.2,0.8,0.2,1)` | 主交互 / 按钮 |
| `--motion-slow` | `320ms cubic-bezier(0.16,1,0.3,1)` | 弹窗 / Drawer |
| `--motion-spring` | Framer Motion `{ type:'spring', stiffness:260, damping:28 }` | 拖拽 / 列表插入 |

> 必须尊重 `prefers-reduced-motion: reduce`：所有动效降级为 `0ms` 透明度切换。

---

## 6. Tailwind 4 集成

`system/packages/ui-kit/src/tokens/theme.css`：

```css
@theme {
  --color-brand: var(--brand);
  --color-brand-hover: var(--brand-hover);
  --color-bg-app: var(--bg-app);
  --color-surface: var(--bg-surface);
  --color-text: var(--text-primary);
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --shadow-md: var(--shadow-md);
  --font-sans: var(--font-sans);
}
:root[data-theme="light"] { /* 1.x 亮模式赋值 */ }
:root[data-theme="dark"]  { /* 1.x 暗模式赋值 */ }
```

---

## 99. 待确认问题
（无）
