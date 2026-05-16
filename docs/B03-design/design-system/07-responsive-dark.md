<!-- TARGET-PATH: docs/B03-design/design-system/07-responsive-dark.md -->

# 06 · 响应式与暗黑模式

> **阶段**：B04-S  
> **上游**：`01-tokens.md`、`B01-architecture/07-i18n-responsive.md`  
> **下游**：所有 C03 N 移动 / 桌面差异、`<ThemeProvider />`  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 6 断点 xs / sm / md / lg / xl / 2xl；应用端 mobile-first，管理端 desktop-first。
- 全屏宽度（不在中间居中），`2xl` 下仍占满视口。
- 暗黑：用户优先 → 系统偏好 → 默认亮。无 FOUC（内联脚本提前设 `data-theme` + `--brand`）。
- 毛玻璃降级：浏览器不支持 / 用户选省电模式 / 运行时低 FPS → 切伪毛玻璃。
- 主题色自定义：6 预设 + HEX 自定义；仅覆盖 brand 系列 token；不做节日皮肤。

---

## 1. 断点矩阵

| 名称 | min-width | 设备 | 内容区内边距 | 顶栏高度 | 一级菜单 |
|------|-----------|------|------------|----------|---------|
| `xs` | 0 | 小屏手机 | 16px | 56px | 右侧 Drawer |
| `sm` | 640px | 大屏手机 / 小平板 | 16px | 56px | 右侧 Drawer |
| `md` | 768px | 平板 | 24px | 64px | 横向 |
| `lg` | 1024px | 笔记本 | 32px | 64px | 横向 |
| `xl` | 1280px | 桌面 | 32px | 64px | 横向 |
| `2xl` | 1536px | 大屏 | 48px | 64px | 横向 |

- 设计基线：移动 360×780 / 桌面 1440×900；
- 应用端：mobile-first，`xs` 必须完整可用；
- 管理端：desktop-first，`< md` 仅保证只读查看，关键编辑提示"建议使用更大屏幕"；
- 全屏宽度：所有页面在 `2xl` 仍占满视口，不在中间居中。

---

## 2. 移动端细则

1. 触控热区 ≥ **44×44 CSS 像素**；按钮默认 `lg`（高 44）；
2. 关键底部操作按钮固定底部安全区：`padding-bottom: env(safe-area-inset-bottom)`；
3. 禁止页面缩放：`<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">`；
4. 长列表必须虚拟滚动（TanStack Virtual）；
5. 横竖屏切换：游戏页（PixiJS）监听 `resize` + `devicePixelRatio`；横竖屏切换提示见游戏模块 PRD。

---

## 3. 暗黑模式

### 3.1 切换逻辑

- 优先级：用户显式选择（Supabase user metadata + `localStorage.theme`）→ `prefers-color-scheme` → **默认 `light`**；
- 顶栏右侧主题切换 `sun` / `moon` 图标按钮，循环 `light ↔ dark`，自动持久化；
- `index.html` 内联脚本（< 1KB）首屏执行，避免 FOUC：

```html
<script>
  (function () {
    var t = localStorage.getItem('theme');
    if (!t) t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', t);
    var c = localStorage.getItem('brand-color');
    if (c) document.documentElement.style.setProperty('--brand', c);
  })();
</script>
```

### 3.2 设计准则

- 亮模式：白底 + 黑字 + 红强调；远景层带极低饱和红色径向光斑；
- 暗模式：**真黑 `#0A0A0B`**（避免纯 `#000` 与红色对比过冲）+ 白字 + 红强调；同样有红色径向光斑（透明度略高）；
- 红色：亮 `#FF2442` / 暗 `#FF3B5C`；
- 所有插画 / 图标必须提供"亮 / 暗"两套或使用 `currentColor`；
- 截图 / 图片缩略图暗模式下叠 `1px solid var(--border-subtle)` 防边缘融化。

### 3.3 测试

- Storybook 双主题快照；
- CI 关键页面 `axe-core` 跑对比度；
- **禁止**任何 `bg-white` / `text-black` 等硬编码颜色 class。

---

## 4. 毛玻璃在低端设备的降级

> 策略：偏向**宽松**——默认毛玻璃启用；仅在浏览器明确不支持或运行时实际揉帧时才降级，不再仅凭静态阈值推断。

| 条件 | 行为 |
|------|------|
| `CSS.supports('backdrop-filter: blur(1px)')` 为 `false` | 「伪毛玻璃」：`--bg-surface-strong` + 噪点 + `shadow-md` |
| 运行时滚动连续 1s FPS < 40 | 「动态降级」：仅顶栏 + 当前能见区卡片保留毛玻璃；连续 5s 低 → 表层切伪毛玻璃 |
| `navigator.deviceMemory <= 1` **且** `hardwareConcurrency <= 2` | 启动即「伪毛玻璃」；设置内可手动开回 |
| 用户在「设置 → 显示」选「省电模式」 | 全局「伪毛玻璃」 |
| 滚动中（`is-scrolling` class）| 顶栏保留模糊；列表卡片可短暂禁用模糊以稳定 60fps（仅滚动 200ms 内）|

---

## 5. 主题色自定义（皮肤系统）

> 本期**仅提供主题色自定义**；节日皮肤（圣诞 / 春节等）本期不上。

### 5.1 能力范围

- 用户在「设置 → 显示 → 主题色」可选：
  - **6 个预设**：小红书红 `#FF2442` / Reddit 橙红 `#FF4500` / 珊瑚 `#FF6B6B` / 薰衣草 `#A855F7` / 深海蓝 `#3B82F6` / 森林绿 `#22C55E`；
  - **自定义 HEX**：`react-colorful` 调色盘，仅 6 位 HEX，不允许 alpha；
- 选定后预览顶栏 / 主按钮 / Tag 实时变色；
- 仅覆盖下列 token，黑白中性色不变：
  - `--brand` = 用户选色；
  - `--brand-hover` = HSL `L × 0.92`；
  - `--brand-active` = HSL `L × 0.84`；
  - `--brand-soft` = alpha 0.10 / 0.14；
  - `--brand-soft-strong` = alpha 0.18 / 0.22；
  - `--ring` = alpha 0.45 / 0.55；
  - `--brand-on` = WCAG AA 自动反推黑 / 白字（`relative-luminance > 0.5` → 黑字）。

### 5.2 存储与同步

- 本地：`localStorage.brand-color`（仅 HEX 7 字节，防注入）；
- 帐号：同步 Supabase user metadata `display.brand_color`，多端一致；
- FOUC：首屏内联脚本（§3.1）同时读取并设置。

### 5.3 约束

- 主题色变化后**重新计算** `--brand-on` 保证 WCAG AA；不达标时调色盘提示"对比度偏低"但不阻止保存；
- 状态色（`--success / --warning`）**不**跟随主题色；
- `--danger` 始终复用 `--brand`（保持语义一致）；
- Storybook 提供「主题色预览」装饰器。

---

## 6. 字体响应式

- 桌面 base = 14px；移动 base = 14px；
- 标题在 `< md` 降一级：`text-h1` 28→24 / `text-h2` 22→20；
- 中文教学卡片字号按"卡片宽度 / 7 字"自适应（`clamp()`），保证一行不溢出。

---

## 7. 可访问性

- 颜色对比度 ≥ WCAG AA（正文 4.5:1 / 大字 3:1）；
- 键盘焦点 ring 在毛玻璃面板上仍清晰可见（`--ring` 红色半透明 2px）；
- `prefers-reduced-motion: reduce` 时所有 `--motion-*` 退化为 `0ms`；毛玻璃保留（视觉非动效）。

---

## 99. 待确认问题
（无）
