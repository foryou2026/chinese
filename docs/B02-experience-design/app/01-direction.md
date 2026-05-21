# 一页纸定调

> **阶段**：B02-XS 体验设计
> **角色**：体验总监 + 设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app（admin 引用本文件）
> **模块**：全局
> **功能**：全局
> **上游依赖**：docs/B01-architecture/01-tech-stack.md, docs/B01-architecture/07-i18n-responsive.md, docs/B01-architecture/08-systems.md
> **冻结状态**：未冻结

---

## 一句话

> **「当极光落在玻璃上，每一个汉字都在发光。」**
>
> 它必须**让人心动**（艺术品级视觉），**让人想留**（沉浸式学习体验），**让人想晒**（社交传播欲）。

---

## 5 条不可逾越

| 编号 | 红线 | 可验证标准 |
|------|------|-----------|
| R1 | 禁止纯白 / 纯黑大面积色块 | 亮色背景必须使用极光渐变网格 `--page-bg` + mesh blob；正文字色使用冷灰 `--text-primary` 而非 `#000` |
| R2 | 禁止"国风装饰"陷阱 | 不出现卷轴杆 / 大幅水墨字背景 / 印章替代 logo / 楷草隶大字铺底；中国元素仅在品牌标志处以极简方式出现 |
| R3 | 禁止正文使用楷体/宋体 | 正文/表单/列表/按钮全部使用 `--font-sans`（Inter + Noto Sans SC）；仅品牌名 Logo 允许 `--font-brush` |
| R4 | 禁止 hex 硬编码 | 所有颜色必须走 CSS 变量；按钮/链接/焦点环必须随 `data-accent` 自动切换 |
| R5 | 禁止动效 > 400ms | 所有过渡 ≤ 400ms；缓动统一 `cubic-bezier(.16,1,.3,1)`（spring-like）；`prefers-reduced-motion: reduce` 时全部关闭 |

> 任何 PR / 设计稿命中以上任一条 → 打回，不讨论。

---

## 5 条主张

| 编号 | 主张 | 可验证维度 | 参考 | 反例 |
|------|------|-----------|------|------|
| A1 | 极光渐变网格底：页面背景为柔和的多彩 mesh gradient + 缓慢飘移动画 | `--page-bg` + 3 个 `.blob` 径向渐变层叠加 | Linear/Arc Browser/Stripe | 纯白/纯灰/黄底背景 |
| A2 | 棱光毛玻璃唯一表面：glass/glass-card/glass-elevated/glass-bar/glass-dark 五级面板 | 所有内容容器使用毛玻璃 + `backdrop-filter: blur + saturate` + 内顶高光 | Apple visionOS / Raycast | 传统实色卡片 |
| A3 | 五色一键换肤：indigo/rose/emerald/amber/violet 5 套 brand 色，`data-accent` 切换 | 切换 accent 后全站按钮/链接/焦点环/进度条同步变色，零孤岛色 | 现代色彩系统 | 写死 hex 的单一配色 |
| A4 | 三密可调：default/compact/elder 三档，字号/间距/按钮高度 token 联动 | `data-density` 切换后布局自适应 | 适老化无障碍设计 | 固定单一密度 |
| A5 | 数字 tabular-nums：表格/统计/金额/时间戳统一启用 | `font-variant-numeric: tabular-nums` 全局生效 | Linear/Stripe 数字对齐 | 数字错位跳动 |

---

## 检验标准

> 拿新设计稿来，1 分钟内判定通过/不通过。

1. 截图缩到 30%，能否一眼识别这是"极光+玻璃+靛蓝"的独特品牌？→ 否则不通过
2. 所有色值是否能在 `tokens.css` 里找到对应变量？→ 否则不通过
3. `prefers-reduced-motion: reduce` 打开，页面是否仍然可用？→ 否则不通过
4. 切换 `data-mode="dark"`，对比度是否 WCAG AA、毛玻璃是否完整？→ 否则不通过
5. 切换 `data-accent="rose"`，主按钮/链接/焦点环是否同步换色？→ 否则不通过
6. 卡片/面板是否使用毛玻璃（backdrop-filter）？→ 否则不通过
7. 是否有人会想截图发给朋友？→ 否则不通过

---

## 99. 待确认问题

无
