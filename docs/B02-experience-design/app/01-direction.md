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

> **「像一张温润的宣纸，铺开宋瓷墨青色的信息，再覆一层薄玻璃。」**
>
> 它必须**沉得住气**（不躁），**留得住人**（不冷），**说得清话**（不绕）。

---

## 5 条不可逾越

| 编号 | 红线 | 可验证标准 |
|------|------|-----------|
| R1 | 禁止纯白 / 纯黑大面积色块 | 亮色背景必须使用宣纸米底渐变 token；正文字色必须使用 `--color-neutral-900: #1F1A14` 暖墨而非 `#000` |
| R2 | 禁止"国风装饰"陷阱 | 不出现卷轴杆 / 大幅水墨字背景 / 印章替代 logo / 楷草隶大字铺底 |
| R3 | 禁止正文使用行楷字体 | 仅品牌名、登录 Hero H1、印鉴 `.seal` 三处允许 `--font-brush`；表格/表单/列表必须 `--font-sans` |
| R4 | 禁止 hex 硬编码 | 所有颜色必须走 CSS 变量；按钮/链接/焦点环必须随 `data-accent` 自动切换 |
| R5 | 禁止动效 > 320ms | 所有过渡 ≤ 320ms；缓动统一 `cubic-bezier(.2,.8,.2,1)`；`prefers-reduced-motion: reduce` 时全部关闭 |

> 任何 PR / 设计稿命中以上任一条 → 打回，不讨论。

---

## 5 条主张

| 编号 | 主张 | 可验证维度 | 参考 | 反例 |
|------|------|-----------|------|------|
| A1 | 宣纸渐变底：页面背景为暖米→月白瓷 linear-gradient + radial-gradient 光晕层 + 宣纸纤维纹 | `--bg-page` + `--bg-page-glow` + `--paper-grain-opacity` 三层叠加 | 宋代宣纸+汝窑月白 | 纯白/纯灰背景 |
| A2 | 毛玻璃唯一表面：glass/glass-strong/glass-tint/glass-bar/glass-hoverable/glass-dark 六级面板 | 所有内容容器使用语义化毛玻璃类 + 顶部 1px 高光 | Apple visionOS 玻璃层级 | 传统实色 box-shadow 卡片 |
| A3 | 五色一键换肤：ink/cinnabar/jade/gold/graphite 5 套 brand 色，`data-accent` 切换 | 切换 accent 后全站按钮/链接/焦点环/Tag 同步变色，零孤岛色 | 中国传统五色体系 | 写死 hex 的单一配色 |
| A4 | 三密可调：default/compact/elder 三档，字号/间距/按钮高度 token 联动 | `data-density` 切换后布局自适应 | 适老化无障碍设计 | 固定单一密度 |
| A5 | 数字 tabular-nums：表格/统计/金额/时间戳统一启用 | `font-variant-numeric: tabular-nums` 全局生效 | Linear/Stripe 数字对齐 | 数字错位跳动 |

---

## 检验标准

> 拿新设计稿来，1 分钟内判定通过/不通过。

1. 截图缩到 30%，能否一眼识别这是"宣纸+墨青+玻璃"而非通用 SaaS？→ 否则不通过
2. 所有色值是否能在 `tokens.css` 里找到对应变量？→ 否则不通过
3. `prefers-reduced-motion: reduce` 打开，页面是否仍然可用？→ 否则不通过
4. 切换 `data-mode="dark"`，对比度是否 WCAG AA、毛玻璃是否完整？→ 否则不通过
5. 切换 `data-accent="cinnabar"`，主按钮/链接/焦点环是否同步换色？→ 否则不通过
6. 卡片/面板是否使用毛玻璃（backdrop-filter）？→ 否则不通过

---

## 99. 待确认问题

无
