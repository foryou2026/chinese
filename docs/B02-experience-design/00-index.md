<!-- TARGET-PATH: docs/B02-experience-design/00-index.md -->

# B02 · 体验定调与设计系统（索引）

> **阶段**：B02-XS 体验与设计系统
> **角色**：体验总监 + 设计系统工程师
> **功能**：全局
> **上游依赖**：`B01-architecture/07-i18n-responsive.md`、`_input/style-input.md`、`_input/visual-input.md`
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- **一句话定调**："给东南亚成年学习者的、像高级社交产品一样使用的汉语学习应用。"
- 风格 = **现代 / 克制 / 质感 / 趣味 / 沉浸**（5 个可验证形容词，任何设计决策命中 ≥ 3）。
- 视觉锚 = 黑白 + 红 + 全局毛玻璃；体验锚 = 不打断 / 不打扰 / 不模糊 / 不让等。
- 参照：小红书 + Stitch + Notion；反例：Duolingo + HelloChinese + 传统 ToB 后台。
- 唯一品牌色 = 红；全局毛玻璃；无侧边栏；全屏宽度；暗模式真黑。

---

## 1. 文件清单

### 1.1 体验定调

| 序号 | 文件 | 职责 |
|------|------|------|
| 01 | [01-direction.md](./01-direction.md) | 一句话定调 + 5 形容词 + 评分卡 |
| 02 | [02-references.md](./02-references.md) | ≥ 3 参照，说明借什么 / 不借什么 |
| 03 | [03-anti-examples.md](./03-anti-examples.md) | ≥ 3 反例，说明如何防止走偏 |
| 04 | [04-voice-tone.md](./04-voice-tone.md) | 文案口吻、错误提示、5 语本地化 |
| 05 | [05-moodboard.md](./05-moodboard.md) | 情绪 / 色感 / 材质 / 节奏关键词 |
| 06 | [06-experience-principles.md](./06-experience-principles.md) | 4 不原则 / 5 互动公约 / 加载/反馈/错误/空状态口径 |

### 1.2 设计系统（Markdown 规范）

| 序号 | 文件 | 职责 |
|------|------|------|
| DS-00 | [design-system/00-index.md](./design-system/00-index.md) | 设计系统索引 + 边界约定 |
| DS-01 | [design-system/01-tokens.md](./design-system/01-tokens.md) | 颜色 / 字体 / 间距 / 圆角 / 阴影 / 毛玻璃 / 动效 token |
| DS-02 | [design-system/02-layout.md](./design-system/02-layout.md) | 顶栏、远景层、内容区、空状态、加载策略 |
| DS-03 | [design-system/03-navigation.md](./design-system/03-navigation.md) | 应用端 / 管理端菜单 + 角色守卫 |
| DS-04 | [design-system/04-status-colors.md](./design-system/04-status-colors.md) | 状态色映射 |
| DS-05 | [design-system/05-components/](./design-system/05-components/) | 组件规范（12 份） |
| DS-06 | [design-system/06-interactions.md](./design-system/06-interactions.md) | 防重提交 / 搜索 / 列表 / 表单离开 / 键盘 / 动效 |
| DS-07 | [design-system/07-responsive-dark.md](./design-system/07-responsive-dark.md) | 断点 / 移动端 / 暗黑模式 / 毛玻璃降级 |
| DS-99 | [design-system/99-extension-icons-imagery.md](./design-system/99-extension-icons-imagery.md) | 图标 / 插画 / 图片（扩展） |

### 1.3 设计系统（可运行资产）

| 文件 | 职责 |
|------|------|
| [prototype-style/tokens.css](./prototype-style/tokens.css) | CSS 变量（与 DS-01 同源） |
| [prototype-style/themes.css](./prototype-style/themes.css) | 暗黑主题覆盖 + prefers-reduced-motion |
| [prototype-style/app.css](./prototype-style/app.css) | 全局 reset + glass-* / btn-* / input / toast 等组件类 |
| [prototype-style/app.js](./prototype-style/app.js) | `window.proto.*` 公共 API |
| [prototype-style/course/](./prototype-style/course/) | course feature 专属样式 |

### 1.4 其他

| 文件 | 职责 |
|------|------|
| [99-open-questions.md](./99-open-questions.md) | 待确认问题 |

---

## 2. 体验定调评分卡（用于评审任何原型 / 页面）

> 任何 C 阶段产物上线前打分，任何维度 ≤ 2 直接打回。

| 维度 | 1 分 | 3 分 | 5 分 |
|------|------|------|------|
| 现代感 | 像 2015 教辅 | 像主流 SaaS | 像 Stitch / 小红书 2024+ |
| 克制度 | 颜色 / 控件 / emoji 满天飞 | 主从有别 | 黑白红 + 毛玻璃 + 1 个主操作 |
| 质感 | 平面 + 实色卡片 | 阴影 + 圆角 | 毛玻璃 + 高光内边 + 微噪 |
| 趣味 | 无激励 / 反馈 | 偶有微互动 | 有进度 / 连胜 / 微动效但**不打断**学习 |
| 沉浸 | 中心固定列宽 + 边缘苍白 | 自适应宽度 | 全屏宽度 + 远景光晕 + 真黑暗模式 |

总分 ≥ 18 / 25 即可上线。

---

## 3. 边界

- **体验定调（01-06）**：只描述"感觉"，不定义 token / hex / px。
- **设计系统（design-system/）**：把感觉转成可工程化的 token / 组件 / 交互规则；唯一真相。
- **原型资产（prototype-style/）**：直接被 C03-H HTML 原型引用，与 token 同源。
- 所有 C 阶段产物的 4 态文案口吻与反馈节奏必须援引本目录。

---

## 99. 待确认问题

（无，见 [99-open-questions.md](./99-open-questions.md)）
