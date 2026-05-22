# 设计 Token

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：app（用户学习系统专属）
> **系统**：app
> **上游依赖**：05-moodboard.md
> **冻结状态**：未冻结

---

> 以下 CSS 变量与 `prototype-style/tokens.css` 逐字一致。
> 运行时覆盖见 `prototype-style/themes.css`。

## 一、命名约定

```
--color-{role}-{step}        颜色（role: brand|neutral|success|warning|danger|info；step: 50~900）
--text-{name}                字号
--lh-{name}                  行高（与字号 pair）
--space-{n}                  间距
--radius-{name}              圆角
--shadow-{level}             阴影
--shadow-btn                 按钮底部 3D 阴影（游戏化专属）
--motion-{name}              动效
--easing-{name}              缓动曲线
--z-{layer}                  z-index 分层
--font-{role}                字体栈
--glass-*                    毛玻璃专用
--page-bg / --mesh-*         页面渐变背景
--color-xp                   经验值色（琥珀）
--color-streak               连续天数色（橙）
--color-locked               锁定节点色（冷灰）
```

---

## 二、字体

```css
:root {
  --font-sans:    'Inter', 'Noto Sans SC', system-ui, -apple-system, sans-serif;
  --font-display: 'Inter', 'Noto Sans SC', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', 'SF Mono', monospace;
  --font-hanzi:   'Noto Serif SC', 'Source Han Serif SC', serif;
  --font-brush:   'LXGW WenKai', 'Ma Shan Zheng', cursive;
}
```

> `--font-brush` 仅限品牌 Logo。`--font-hanzi` 仅用于学习内容中的汉字展示。正文/表单全部使用 `--font-sans`。

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

> 西文+数字默认 `font-variant-numeric: tabular-nums; font-feature-settings: "tnum" 1, "lnum" 1;`

---

## 四、字重

```css
:root {
  --weight-regular:  400;
  --weight-medium:   500;
  --weight-semibold: 600;
  --weight-bold:     700;
  --weight-extrabold: 800;
}
```

> `--weight-extrabold` 用于游戏化标题、XP 数值、关卡编号等需要超粗视觉冲击的场景。

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
  --radius-sm:   8px;
  --radius-md:  12px;   /* 按钮/输入/Tag 默认 */
  --radius-lg:  16px;   /* 卡片 */
  --radius-xl:  20px;   /* 强卡片/模态（Duolingo 风格大圆角） */
  --radius-2xl: 24px;   /* 抽屉/Hero 容器 */
  --radius-pill: 9999px; /* 胶囊形——游戏化主 CTA 按钮默认 */
}
```

> Duolingo 风格的主 CTA 按钮统一使用 `--radius-pill` 胶囊圆角。卡片与模态使用 `--radius-xl`（20px）或 `--radius-2xl`（24px）。

---

## 七、颜色 · 中性（冷灰阶，accent 无关）

```css
:root {
  --color-neutral-0:   #FFFFFF;
  --color-neutral-50:  #F8FAFC;
  --color-neutral-100: #F1F5F9;
  --color-neutral-200: #E2E8F0;
  --color-neutral-300: #CBD5E1;
  --color-neutral-400: #94A3B8;
  --color-neutral-500: #64748B;
  --color-neutral-600: #475569;
  --color-neutral-700: #334155;
  --color-neutral-800: #1E293B;
  --color-neutral-900: #0F172A;
  --color-neutral-950: #020617;
}
```

---

## 八、颜色 · Brand（Google 四色主题）

> 默认 `data-accent="red"`。运行时切换 `<html data-accent="yellow|blue|green">` 即整体换色。
> 采用 Google 品牌四原色（红黄蓝绿），高饱和度，视觉冲击力强。
> 所有按钮/链接/焦点环/激活下划线/Tag 默认色必须使用 `--color-brand-*`，**禁止**直接引用具体色族。

### 8.1 red · Google 红（默认）

```css
:root {
  --color-brand-50:  #FFEBEE;  --color-brand-100: #FFCDD2;
  --color-brand-200: #EF9A9A;  --color-brand-300: #E57373;
  --color-brand-400: #EF5350;  --color-brand-500: #EA4335;
  --color-brand-600: #E53935;  --color-brand-700: #D32F2F;
  --color-brand-800: #C62828;  --color-brand-900: #B71C1C;
  --color-brand-default: var(--color-brand-500);
  --color-brand-hover:   var(--color-brand-400);
  --color-brand-active:  var(--color-brand-600);
  --color-brand-on:      #FFFFFF;
  --color-brand-ring:    rgba(234, 67, 53, 0.30);
}
```

### 8.2 yellow · Google 黄

锚定 brand-500 #FBBC04。`--color-brand-on` 为深色文字 `#202124`。详见 `themes.css`。

### 8.3 blue · Google 蓝

锚定 brand-500 #4285F4。详见 `themes.css`。

### 8.4 green · Google 绿

锚定 brand-500 #34A853。详见 `themes.css`。

---

## 九、颜色 · 状态（accent 无关）

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

## 十、颜色 · 游戏化专属

```css
:root {
  /* XP 经验值 — 琥珀金 */
  --color-xp:       #F59E0B;
  /* Streak 连续天数 — 火焰橙 */
  --color-streak:   #F97316;
  /* 锁定节点 — 冷灰 */
  --color-locked:   #94A3B8;
}
```

> 这三个颜色不随 `data-accent` 变化，是游戏化 UI 的固定语义色。

---

## 十一、背景 · 极光渐变与毛玻璃

> 极光 Mesh Gradient 的颜色会跟随当前 `data-accent` 主题色动态变化，形成与主色呼应的背景点缀。
> 暗色模式下使用极低透明度的主色变体作微光点缀，保持纯黑底的高级感。

```css
:root {
  /* 页面基底 */
  --page-bg: #FFFAFA;

  /* 极光渐变 Blob 颜色（默认跟随 red 主题） */
  --mesh-color-1: #FFCDD2;   /* 红色调 red-100 */
  --mesh-color-2: #FFE0B2;   /* 暖橙调 */
  --mesh-color-3: #F8BBD0;   /* 粉红调 */
  --mesh-opacity-1: 0.55;
  --mesh-opacity-2: 0.40;
  --mesh-opacity-3: 0.45;

  /* 毛玻璃表面 */
  --glass-bg:          rgba(255, 255, 255, 0.60);
  --glass-bg-card:     rgba(255, 255, 255, 0.65);
  --glass-bg-elevated: rgba(255, 255, 255, 0.75);
  --glass-border:      rgba(255, 255, 255, 0.70);
  --glass-inset:       rgba(255, 255, 255, 0.90);
  --glass-shadow:      rgba(0, 0, 30, 0.06);
  --glass-shadow-elevated: rgba(0, 0, 30, 0.10);
  --glass-blur:        blur(24px) saturate(1.8);
  --glass-blur-lg:     blur(36px) saturate(2.0);
  --glass-blur-sm:     blur(16px) saturate(1.5);
}
```

---

## 十二、阴影

```css
:root {
  --shadow-sm: 0 2px 8px rgba(0, 0, 30, 0.06);
  --shadow-md: 0 6px 18px rgba(0, 0, 30, 0.08);
  --shadow-lg: 0 14px 38px rgba(0, 0, 30, 0.12);

  /* 游戏化 3D 按钮底部阴影 — Duolingo 风格 */
  --shadow-btn: 0 4px 0 0 var(--color-brand-700);
}
```

> `--shadow-btn` 为 Duolingo 风格 3D 按钮专属。按下时阴影减小至 `0 2px 0 0`，同时按钮向下位移 2px，模拟物理按压感。
> 不同变体的 `--shadow-btn` 颜色跟随按钮色系（如 destructive 用 `--color-danger-700`，success 用 `--color-success-700`）。

---

## 十三、焦点环 / 描边

```css
:root {
  --focus-ring: 0 0 0 4px var(--color-brand-ring);
  --border-color: rgba(200, 210, 225, 0.60);
}
```

---

## 十四、动效

```css
:root {
  --motion-fast: 150ms cubic-bezier(.16,1,.3,1);
  --motion-base: 250ms cubic-bezier(.16,1,.3,1);
  --motion-slow: 350ms cubic-bezier(.16,1,.3,1);
  --easing-out:  cubic-bezier(.16,1,.3,1);
  --easing-in-out: cubic-bezier(.4,0,.2,1);
  --easing-spring: cubic-bezier(.34,1.56,.64,1);
  --transition-all: all 200ms cubic-bezier(.16,1,.3,1);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
```

> `--easing-spring` 为弹簧过冲缓动，专用于游戏化按钮按压回弹、正确答案弹跳、XP 数值飞出等需要"弹性"手感的场景。

---

## 十五、z-index

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

## 十六、断点

```css
--bp-sm:   480px;
--bp-md:   768px;
--bp-lg:  1024px;
--bp-xl:  1280px;
--bp-2xl: 1536px;
```

---

## 十七、密度切换

```css
[data-density="default"] { /* 默认值，所有 token 不变 */ }
[data-density="compact"] {
  --text-base: 14px; --text-md: 15px;
  --space-3: 8px; --space-4: 12px; --space-5: 16px; --space-6: 22px;
}
[data-density="elder"] {
  --text-base: 19px; --text-md: 21px; --text-lg: 24px;
  --space-3: 16px; --space-4: 22px; --space-5: 28px; --space-6: 36px;
}
```

---

## 十八、Token 契约

1. 任何业务 CSS / 组件 / 原型只能引用 `--color-brand-*` `--color-neutral-*` `--color-{success|warning|danger|info}-*` `--color-xp` `--color-streak` `--color-locked` `--space-*` `--radius-*` `--shadow-*` `--shadow-btn` `--motion-*` `--easing-*` `--text-*` `--font-*` `--z-*` `--glass-*`。
2. **禁止**引用具体色族（如 `--color-red-700`）；后者为 token 内部实现，因主题切换而易主。
3. 状态色 / 中性色 / 玻璃 / 间距 / 字体 / 游戏化色 不随 `data-accent` 改变。
4. 仅 brand 色 + mesh 极光点缀色 随 `data-accent` 切换；brand / 中性 / 玻璃 / 背景 随 `data-mode` 切换。
5. `--shadow-btn` 的颜色值随按钮变体动态指定，但始终使用 `0 4px 0 0` 的尺寸规格。

---

## 99. 待确认问题

无
