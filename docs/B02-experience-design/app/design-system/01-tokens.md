# 设计 Token

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
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
--motion-{name}              动效
--z-{layer}                  z-index 分层
--font-{role}                字体栈
--glass-{name}               毛玻璃专用
--bg-page / --bg-page-glow   页面渐变背景
```

---

## 二、字体

```css
:root {
  --font-brush:   'Ma Shan Zheng', 'STKaiti', cursive;
  --font-display: 'ZCOOL XiaoWei', 'Source Han Serif SC', 'Noto Serif SC', serif;
  --font-sans:    'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'SF Mono', Consolas, monospace;
}
```

> `--font-brush` 仅限品牌名 / Hero H1 / 印鉴 `.seal`，正文/表单禁用。

---

## 三、字号 / 行高

```css
:root {
  --text-xs:      12px;    --lh-xs:      18px;
  --text-sm:      14px;    --lh-sm:      22px;
  --text-base:    17px;    --lh-base:    28px;
  --text-md:      19px;    --lh-md:      30px;
  --text-lg:      24px;    --lh-lg:      34px;
  --text-xl:      32px;    --lh-xl:      42px;
  --text-2xl:     42px;    --lh-2xl:     54px;
  --text-display: 54px;    --lh-display: 66px;
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
  --radius-sm:   8px;
  --radius-md:  12px;   /* 按钮/输入/Tag 默认 */
  --radius-lg:  18px;   /* 卡片 */
  --radius-xl:  26px;   /* 强卡片/模态 */
  --radius-2xl: 34px;   /* 抽屉/Hero 容器 */
  --radius-pill: 999px;
}
```

---

## 七、颜色 · 中性（暖墨灰阶，accent 无关）

```css
:root {
  --color-neutral-0:   #FFFBF0;   /* 暖白纸 */
  --color-neutral-50:  #F8F2E0;
  --color-neutral-100: #F0E8D2;
  --color-neutral-200: #E5DCC7;
  --color-neutral-300: #C5BBA8;
  --color-neutral-400: #9C9080;
  --color-neutral-500: #6F6452;   /* 茶灰·辅助文字 */
  --color-neutral-600: #56493A;
  --color-neutral-700: #3D3327;   /* 副文 */
  --color-neutral-800: #2A2218;
  --color-neutral-900: #1F1A14;   /* 暖墨·正文 */
  --color-neutral-950: #100D0A;
}
```

---

## 八、颜色 · Brand（5 主题色族）

> 默认 `data-accent="ink"`。运行时切换 `<html data-accent="cinnabar|jade|gold|graphite">` 即整体换色。
> 所有按钮/链接/焦点环/激活下划线/Tag 默认色必须使用 `--color-brand-*`，**禁止**直接引用具体色族。

### 8.1 ink · 宋瓷墨青（默认）

```css
:root {
  --color-brand-50:  #E8EFF5;  --color-brand-100: #CFDDE8;
  --color-brand-200: #A8C0D4;  --color-brand-300: #7EA0BF;
  --color-brand-400: #5481A8;  --color-brand-500: #2E5C8A;
  --color-brand-600: #244A72;  --color-brand-700: #1B3A5C;   /* 主锚定 */
  --color-brand-800: #142A44;  --color-brand-900: #0E1F38;
  --color-brand-default: var(--color-brand-700);
  --color-brand-hover:   var(--color-brand-600);
  --color-brand-active:  var(--color-brand-800);
  --color-brand-on:      #FFFBF0;
  --color-brand-ring:    rgba(46, 92, 138, 0.18);
}
```

### 8.2 cinnabar · 朱砂

锚定 brand-500。详见 `themes.css`。

### 8.3 jade · 翠玉

锚定 brand-600。详见 `themes.css`。

### 8.4 gold · 鎏金

锚定 brand-700。详见 `themes.css`。

### 8.5 graphite · 古墨

锚定 brand-600。详见 `themes.css`。

---

## 九、颜色 · 状态（accent 无关）

```css
:root {
  /* success · 翠玉 */
  --color-success-50:  #E5EFE9;  --color-success-100: #C9DCD2;
  --color-success-200: #97BAA7;  --color-success-500: #4A6F5A;
  --color-success-700: #2F5640;
  /* warning · 鎏金 */
  --color-warning-50:  #F4ECD8;  --color-warning-100: #E8D5A8;
  --color-warning-200: #D4B870;  --color-warning-500: #B8923A;
  --color-warning-700: #8C6E2A;
  /* danger · 朱砂 */
  --color-danger-50:  #F5E0DC;  --color-danger-100: #EAC0B8;
  --color-danger-200: #D89488;  --color-danger-500: #B14545;
  --color-danger-700: #8A2F2F;
  /* info · 青花 */
  --color-info-50:  #E8EFF5;  --color-info-100: #CFDDE8;
  --color-info-500: #2E5C8A;  --color-info-700: #1B3A5C;
}
```

---

## 十、背景 · 渐变与毛玻璃

```css
:root {
  /* 页面渐变（宣纸→月白瓷） */
  --bg-page: linear-gradient(180deg, #F8F2E0 0%, #F2EBD3 38%, #E8EFF5 100%);
  --bg-page-glow:
    radial-gradient(60% 50% at 75% 12%, rgba(184,146,58,0.10), transparent 60%),
    radial-gradient(45% 40% at 18% 92%, rgba(46,92,138,0.08), transparent 55%);
  --paper-grain-opacity: 0.06;

  /* 毛玻璃表面 */
  --glass-1: rgba(255, 251, 240, 0.55);   /* 默认 */
  --glass-2: rgba(255, 251, 240, 0.72);   /* 强卡 */
  --glass-3: rgba(255, 251, 240, 0.42);   /* 极薄 */
  --glass-tint:  rgba(207, 221, 232, 0.45); /* 月白瓷蓝 */
  --glass-dark:  rgba(20, 48, 79, 0.78);   /* 反白·hero / TopBar */
  --glass-blur:    saturate(170%) blur(22px);
  --glass-blur-lg: saturate(170%) blur(34px);
  --glass-blur-sm: saturate(170%) blur(16px);
  --glass-border:        1px solid rgba(255, 250, 235, 0.78);
  --glass-border-strong: 1px solid rgba(255, 250, 235, 0.92);
  --glass-shadow:
    0 6px 24px rgba(14, 31, 56, 0.14),
    inset 0 1px 0 rgba(255, 250, 235, 0.65);
  --glass-shadow-lg:
    0 14px 38px rgba(14, 31, 56, 0.18),
    inset 0 1px 0 rgba(255, 250, 235, 0.65);
}
```

---

## 十一、阴影

```css
:root {
  --shadow-sm: 0 2px 8px rgba(14, 31, 56, 0.08);
  --shadow-md: 0 6px 18px rgba(14, 31, 56, 0.12);
  --shadow-lg: 0 14px 38px rgba(14, 31, 56, 0.18);
}
```

---

## 十二、焦点环 / 描边

```css
:root {
  --focus-ring: 0 0 0 4px var(--color-brand-ring);
  --border-strong: 1px solid var(--color-neutral-300);
  --border-subtle: 1px solid var(--color-neutral-200);
}
```

---

## 十三、动效

```css
:root {
  --motion-fast: 120ms cubic-bezier(.2,.8,.2,1);
  --motion-base: 200ms cubic-bezier(.2,.8,.2,1);
  --motion-slow: 320ms cubic-bezier(.2,.8,.2,1);
  --easing-out:  cubic-bezier(.2,.8,.2,1);
  --easing-in-out: cubic-bezier(.4,0,.2,1);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
```

---

## 十四、z-index

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

## 十五、断点

```css
--bp-sm:   480px;
--bp-md:   768px;
--bp-lg:  1024px;
--bp-xl:  1280px;
--bp-2xl: 1536px;
```

---

## 十六、密度切换

```css
[data-density="default"] { /* 默认值，所有 token 不变 */ }
[data-density="compact"] {
  --text-base: 15px; --text-md: 16px;
  --space-3: 8px; --space-4: 12px; --space-5: 16px; --space-6: 22px;
}
[data-density="elder"] {
  --text-base: 20px; --text-md: 22px; --text-lg: 26px;
  --space-3: 16px; --space-4: 22px; --space-5: 28px; --space-6: 36px;
}
```

---

## 十七、Token 契约

1. 任何业务 CSS / 组件 / 原型只能引用 `--color-brand-*` `--color-neutral-*` `--color-{success|warning|danger|info}-*` `--space-*` `--radius-*` `--shadow-*` `--motion-*` `--text-*` `--font-*` `--z-*` `--glass-*`。
2. **禁止**引用具体色族（如 `--color-ink-700`）；后者为 token 内部实现，因主题切换而易主。
3. 状态色 / 中性色 / 玻璃 / 间距 / 字体 不随 `data-accent` 改变。
4. 仅 brand 色随 `data-accent` 切换；brand / 中性 / 玻璃 / 背景 随 `data-mode` 切换。

---

## 99. 待确认问题

无
