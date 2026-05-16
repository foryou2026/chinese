<!-- TARGET-PATH: docs/B04-design/design-system/02-layout.md -->

# 02 · 全局布局

> **阶段**：B04-S  
> **上游**：`01-tokens.md`、`B03-ux/05-moodboard.md`、`B03-ux/06-experience-principles.md`  
> **下游**：所有 C04 H 原型、所有 C03 N 页面骨架  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- **顶部导航 + 远景层 + 全屏内容区**三层结构；**无侧边栏**；**无中心固定列宽**；**无 Footer**（业务页）。
- 顶栏 64 桌面 / 56 移动；远景层固定在 body::before 提供红色径向光晕。
- 内容区 `.page` 左右 padding 桌面 32 / 移动 16，顶部 24。

---

## 1. 布局总览

```
┌──── 顶部导航 GlassNav (h: 64/56, sticky top:0, z:50) ────┐
│  Logo+产品名 ┊ 菜单（横向）         ┊ Locale│Theme│Bell│Avatar▾  │
└──────────────────────────────────────────────────────────────┘
┌──── 远景层（body::before, 红色径向光晕 + 微噪, 全局固定） ────┐
│   ┌──── 内容区 .page (max-w:none, 全屏自适应) ────┐         │
│   │  PageHeader → PageContent → GlassCard / 表格 / 表单     │
│   └────────────────────────────────────────────────┘         │
└──────────────────────────────────────────────────────────────┘
                  无 Footer（落地 / 营销页除外）
```

- **B03 锚点**："沉浸"= 全屏 + 远景光晕；"现代"= 顶栏 sticky + 滚动后阴影渐变。

---

## 2. 顶部导航 GlassNav

| 属性 | 桌面 | 移动 |
|------|------|------|
| 高度 | 64px | 56px |
| 内边距 | 左右 32px | 左右 16px |
| 背景 | `.glass-nav`（`--glass-blur-md`，无圆角，底部 1px `--border-subtle`）| 同左 |
| z-index | 50 | 50 |
| 阴影 | 滚动 > 4px 加 `shadow-md`（监听 `window.scrollY` 加 class `is-scrolled`）| 同 |
| 安全区 | `padding-top: env(safe-area-inset-top)` | 同 |

### 2.1 桌面（≥ md）

```
[Logo+产品名]   [菜单项 间距24]                [Locale][Theme][Bell][Avatar▾]
```

- 选中态：底部 2px `--brand` 短线（长度 = 文字宽度）+ 文字 `--brand`；
- hover：文字 `--brand`，无下划线；
- 字号 `text-button`。

### 2.2 移动（< md）

```
[Logo]                              [Theme][Avatar▾][Hamburger ☰]
```

- 菜单收纳到右侧 Drawer（自右向左滑入，`.glass-modal` 风格）；
- Drawer 内菜单项纵向排列，行高 48px，选中态左侧 2px `--brand` 竖线 + 浅底；
- Drawer 顶部含语言切换 + 通知入口；
- 关闭：点遮罩 / ESC / 点 X。

### 2.3 Logo

- 文字版：`知语 · Zhiyu`，`text-h2`，前缀色块 24×24（`--brand` `radius-sm`，内含白色"语"字简化图形）；
- 点击 Logo 总返回各端首页（应用端 `/`，管理端 `/admin`）；
- v1 暂用文字 + 色块，图形 Logo 待定（见 [99](./99-open-questions.md) Q1）。

---

## 3. 远景层（body::before）

```css
body::before {
  content: "";
  position: fixed; inset: 0; z-index: -1;
  background:
    radial-gradient(60% 50% at 15% 10%, rgba(255,36,66,0.10), transparent 60%),
    radial-gradient(45% 40% at 85% 90%, rgba(255,36,66,0.08), transparent 65%),
    var(--bg-app-tint);
}
body::after { /* 1px 微噪 PNG 平铺, opacity: var(--glass-noise-opacity) */ }
```

- 暗模式：`--bg-app-tint = #111114`，红色径向光斑透明度提至 `0.14 / 0.10`；
- 禁止承载业务内容；仅做"光感"。

---

## 4. 内容区 `.page`

| 属性 | 桌面 ≥ md | 移动 < md |
|------|----------|----------|
| 宽度 | `width: 100%; max-width: none` | 同 |
| 左右内边距 | 32px | 16px |
| 顶部内边距 | 24px | 16px |
| 栅格 | 12 列, `gap: 24px`（CSS Grid 推荐）| 1 列 |
| 阅读型长文 | `<article class="prose max-w-[72ch] mx-auto">` 内部限宽 | 移动不限宽 |

### 4.1 通用骨架

```tsx
<Page>
  <PageHeader title="..." subtitle="..." actions={<Button>新建</Button>} />
  <PageContent>
    <GlassCard>...</GlassCard>
  </PageContent>
</Page>
```

- `PageHeader`：`text-h1` 标题 + `text-caption` 副标题 + 右侧操作槽；下方 `space-5` 间距；
- `PageContent`：仅承载业务；**禁止**直接 `bg-white` / 实色背景；
- 卡片型展示统一走 `<GlassCard>`（`.glass-card`）。

---

## 5. 空状态 & 加载

### 5.1 空状态（来自 [B03 §不让用户等](../../B03-ux/06-experience-principles.md)）

| 元素 | 规格 |
|------|------|
| 容器 | `<GlassCard class="text-center py-12">` |
| 插图 | 96×96 SVG（线条 + 单色 `--text-tertiary` + 红色辅助高光）|
| 标题 | `text-h3 text-primary` |
| 描述 | `text-body text-secondary` |
| 操作 | 主按钮（如适用），居中 |

### 5.2 加载

- 默认：骨架屏（`<Skeleton>`），毛玻璃风格，行 / 卡片轮廓与最终一致；
- < 200ms 请求**不展示**骨架（避免闪烁）；
- 全屏路由切换：顶部 2px `--brand` 进度条（fork TanStack Router progress）。

---

## 6. 禁用布局

1. **侧边栏**：v1 全禁（PM 单点放行除外）；
2. **固定中心列宽**：`max-w-7xl mx-auto` 等中心容器禁用于普通页（仅长文段落允许）；
3. **不透明卡片**：禁 `bg-white` / `bg-zinc-900` 当卡片底；必须毛玻璃；
4. **第二种品牌色**；
5. **业务页面 Footer**：仅营销 / 落地页有 Footer，登录后业务页一律无 Footer。

---

## 99. 待确认问题
（无 · 图形 Logo 在 [99-open-questions.md](./99-open-questions.md) Q1）
