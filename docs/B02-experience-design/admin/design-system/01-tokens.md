# 设计 Token（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：00-index.md
> **冻结状态**：未冻结

---

> admin 的 Token 体系与 app 完全独立。核心差异：克制低饱和毛玻璃（vs app 的高饱和）、无 mesh-gradient、无 brand 色族切换。
> 所有表面使用半透明毛玻璃背景 + `backdrop-filter` + 半透明边框，有 `@supports` 实色回退。

## 一、命名约定

```
--color-neutral-{step}       中性灰阶（0~950）
--color-{status}-{step}      状态色（success|warning|danger|info；50~700）
--btn-{variant}-{property}   按钮变体（primary|secondary）
--color-accent               链接/焦点蓝
--text-{name}                字号
--lh-{name}                  行高（与字号 pair）
--space-{n}                  间距
--radius-{name}              圆角
--shadow-{level}             阴影
--motion-{name}              动效
--z-{layer}                  z-index 分层
--font-{role}                字体栈
--surface-{name}             表面色
--border-color               通用边框色
--text-{role}                文字色（primary|secondary|muted）
--focus-ring                 焦点环
```

---

## 二、字体

```css
:root {
  --font-sans:  'Inter', 'Noto Sans SC', system-ui, -apple-system, sans-serif;
  --font-mono:  'JetBrains Mono', 'Fira Code', 'SF Mono', monospace;
}
```

> admin 不使用 `--font-display`、`--font-hanzi`、`--font-brush`。所有界面元素统一使用 `--font-sans`，代码/ID 类字段使用 `--font-mono`。

---

## 三、字号 / 行高

```css
:root {
  --text-xs:      12px;    --lh-xs:      18px;
  --text-sm:      14px;    --lh-sm:      22px;
  --text-base:    16px;    --lh-base:    26px;
  --text-md:      18px;    --lh-md:      28px;
  --text-lg:      22px;    --lh-lg:      32px;
  --text-xl:      30px;    --lh-xl:      40px;
  --text-2xl:     40px;    --lh-2xl:     52px;
  --text-display: 52px;    --lh-display: 64px;
}
```

> admin 默认正文使用 `--text-sm`（14px），app 默认正文使用 `--text-base`（16px）。
> 西文+数字默认 `font-variant-numeric: tabular-nums; font-feature-settings: "tnum" 1, "lnum" 1;`

---

## 四、字重

```css
:root {
  --weight-regular:  400;
  --weight-medium:   500;
  --weight-semibold: 600;
  --weight-bold:     700;
}
```

---

## 五、间距（4px 基线）

```css
:root {
  --space-0:  0;
  --space-1:  4px;   --space-2:  8px;   --space-3:  12px;
  --space-4:  16px;  --space-5:  20px;  --space-6:  24px;
  --space-7:  32px;  --space-8:  40px;  --space-9:  48px;
  --space-10: 64px;  --space-11: 80px;  --space-12: 96px;
}
```

---

## 六、圆角

```css
:root {
  --radius-none: 0;
  --radius-xs:   4px;
  --radius-sm:   6px;    /* admin 专用，比 app 更小 */
  --radius-md:   8px;    /* 按钮/输入/Tag 默认 */
  --radius-lg:  12px;    /* 卡片 */
  --radius-xl:  16px;    /* 模态/大面板 */
  --radius-pill: 9999px;
}
```

> admin 圆角整体比 app 更小更克制：app 的 sm/md/lg/xl 分别为 8/12/16/24px，admin 为 6/8/12/16px。

---

## 七、颜色 · 中性灰阶

```css
:root {
  --color-neutral-0:   #FFFFFF;
  --color-neutral-50:  #F9FAFB;
  --color-neutral-100: #F3F4F6;
  --color-neutral-200: #E5E7EB;
  --color-neutral-300: #D1D5DB;
  --color-neutral-400: #9CA3AF;
  --color-neutral-500: #6B7280;
  --color-neutral-600: #4B5563;
  --color-neutral-700: #374151;
  --color-neutral-800: #1F2937;
  --color-neutral-900: #111827;
  --color-neutral-950: #030712;
}
```

> admin 使用 Tailwind gray 系列（暖灰），与 app 的 slate 系列（冷灰）不同。

---

## 八、颜色 · 按钮

```css
:root {
  /* 主按钮：纯黑/纯白对比 */
  --btn-primary-bg:       #18181B;
  --btn-primary-bg-hover:  #27272A;
  --btn-primary-bg-active: #09090B;
  --btn-primary-text:     #FAFAFA;

  /* 次要按钮：白底边框 */
  --btn-secondary-bg:       #FFFFFF;
  --btn-secondary-bg-hover:  #F9FAFB;
  --btn-secondary-bg-active: #F3F4F6;
  --btn-secondary-text:     #374151;
  --btn-secondary-border:   #D1D5DB;
}
```

> admin 不使用品牌色渐变按钮。Secondary 按钮使用半透明毛玻璃底。主按钮采用纯黑底白字（light）/纯白底黑字（dark）的高对比方案。

---

## 九、颜色 · 链接与焦点

```css
:root {
  --color-accent:      #3B82F6;   /* blue-500，链接/焦点色 */
  --color-accent-hover: #2563EB;  /* blue-600 */
  --focus-ring: 0 0 0 3px rgba(59, 130, 246, 0.30);
}
```

> admin 的焦点环为 3px（比 app 的 4px 更紧凑），颜色固定为 blue，不随 accent 切换。

---

## 十、颜色 · 状态（与 app 一致）

```css
:root {
  /* success · 翡翠 */
  --color-success-50:  #ECFDF5;  --color-success-100: #D1FAE5;
  --color-success-200: #A7F3D0;  --color-success-500: #10B981;
  --color-success-700: #047857;

  /* warning · 琥珀 */
  --color-warning-50:  #FFFBEB;  --color-warning-100: #FEF3C7;
  --color-warning-200: #FDE68A;  --color-warning-500: #F59E0B;
  --color-warning-700: #B45309;

  /* danger · 红 */
  --color-danger-50:  #FEF2F2;  --color-danger-100: #FEE2E2;
  --color-danger-200: #FECACA;  --color-danger-500: #EF4444;
  --color-danger-700: #B91C1C;

  /* info · 蓝 */
  --color-info-50:  #EFF6FF;  --color-info-100: #DBEAFE;
  --color-info-200: #BFDBFE;  --color-info-500: #3B82F6;
  --color-info-700: #1D4ED8;
}
```

---

## 十一、表面色 / 毛玻璃

```css
:root {
  /* 实色回退 */
  --surface-page:      #F3F4F6;
  --surface-primary:   #F9FAFB;
  --surface-elevated:  #FFFFFF;

  /* 毛玻璃（Frost — 克制、低饱和） */
  --glass-bg:          rgba(255, 255, 255, 0.72);   /* 导航/输入 */
  --glass-bg-card:     rgba(255, 255, 255, 0.78);   /* 卡片/侧边栏 */
  --glass-bg-elevated: rgba(255, 255, 255, 0.88);   /* 弹层/Modal */
  --glass-border:      rgba(229, 231, 235, 0.80);
  --glass-inset:       rgba(255, 255, 255, 0.70);
  --glass-blur:        blur(20px) saturate(1.4);     /* 卡片默认 */
  --glass-blur-lg:     blur(28px) saturate(1.5);     /* 弹层 */
  --glass-blur-sm:     blur(12px) saturate(1.2);     /* 小控件 */
}
```

> admin 的毛玻璃比 app 更克制：饱和度 ≤ 1.5（app 为 1.8），模糊半径 ≤ 28px（app 为 24px base）。页面底色 #F3F4F6 + 微弱径向渐变让毛玻璃层可感知。必须提供 `@supports not (backdrop-filter)` 实色回退。

---

## 十二、边框

```css
:root {
  --border-color: #E5E7EB;   /* neutral-200，通用分隔线/边框 */
}
```

---

## 十三、文字色

```css
:root {
  --text-primary:   #111827;   /* neutral-900，标题/正文 */
  --text-secondary: #6B7280;   /* neutral-500，辅助文字 */
  --text-muted:     #9CA3AF;   /* neutral-400，占位符/禁用 */
}
```

---

## 十四、阴影

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
  --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.10);
}
```

> admin 阴影极度克制，比 app 的阴影更浅更小。日常卡片不使用阴影（依赖 1px 边框定义边界），仅弹出层使用 `--shadow-md` 或 `--shadow-lg`。

---

## 十五、焦点环 / 描边

```css
:root {
  --focus-ring: 0 0 0 3px rgba(59, 130, 246, 0.30);
  --border-color: #E5E7EB;
}
```

---

## 十六、动效

```css
:root {
  --motion-fast: 100ms ease;
  --motion-base: 200ms ease-out;
  --motion-slow: 200ms ease-out;
  --easing-out:  ease-out;
  --easing-in-out: cubic-bezier(.4, 0, .2, 1);
  --transition-all: all 150ms ease;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
```

> admin 动效比 app 更快更简洁：不使用弹簧缓动（cubic-bezier(.16,1,.3,1)），统一使用标准 `ease` / `ease-out`。
> `--motion-slow` 与 `--motion-base` 时长相同（200ms），admin 不需要 350ms 的慢动效。

---

## 十七、z-index

```css
:root {
  --z-base:     0;
  --z-sticky:   100;
  --z-dropdown: 1000;
  --z-popover:  1100;
  --z-modal:    1200;
  --z-toast:    1300;
  --z-tooltip:  1400;
}
```

---

## 十八、断点

```css
--bp-sm:   480px;
--bp-md:   768px;
--bp-lg:  1024px;
--bp-xl:  1280px;
--bp-2xl: 1536px;
```

---

## 十九、密度切换

```css
[data-density="default"] { /* 默认值，所有 token 不变 */ }
[data-density="compact"] {
  --text-base: 14px; --text-md: 15px;
  --space-3: 8px; --space-4: 12px; --space-5: 16px; --space-6: 22px;
}
```

> admin 仅支持 default 和 compact 两档密度，不支持 elder。compact 模式下表格行高从 40px 缩减至 32px。

---

## 二十、Token 契约

1. 任何业务 CSS / 组件只能引用 `--color-neutral-*` `--color-{success|warning|danger|info}-*` `--btn-{primary|secondary}-*` `--color-accent` `--surface-*` `--text-{primary|secondary|muted}` `--border-color` `--space-*` `--radius-*` `--shadow-*` `--motion-*` `--text-*` `--font-*` `--z-*`。
2. **禁止**引用 app 的 `--color-brand-*`、`--mesh-*`、app 的主题色 token。admin 有独立的 `--glass-*` token（与 app 的 `--glass-*` 值不同）。
3. admin 不存在 accent 切换，所有组件使用固定的中性灰+蓝色 accent。
4. 中性灰阶 / 表面色 / 按钮色 / 边框 / 文字色 随 `data-mode` 切换（light/dark）。

---

## 99. 待确认问题

无
