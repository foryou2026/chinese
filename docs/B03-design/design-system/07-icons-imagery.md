<!-- TARGET-PATH: docs/B03-design/design-system/99-extension-icons-imagery.md -->

# 07 · 图标 / 插画 / 图片 / 头像

> **阶段**：B04-S  
> **上游**：`B02-ux/05-moodboard.md`、`_input/visual-input.md`  
> **下游**：所有 C04 H 原型、所有 C03 N 视觉资产规范  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 图标：`lucide-react` 唯一图标库；标准 18px，stroke 2px，颜色继承 `currentColor`。
- 插画：自绘线条风格 + 单色 `--text-tertiary` + 红色辅助高光；不用拟物 / 3D / Lottie 跳舞 mascot。
- 图片：圆角 `radius-md`；暗模式叠 1px `--border-subtle` 防边缘融化。
- 头像：圆形 `radius-pill`；首字符兜底色块（红底白字）。
- 全部 SVG 嵌入（不用 IconFont）；图片走 `<Image>` 二次封装（懒加载 + 占位）。

---

## 1. 图标

### 1.1 库与版本

- **唯一图标库**：`lucide-react`（线条风格、统一 stroke）；
- 引入按需 tree-shake：`import { Compass, GraduationCap } from 'lucide-react'`；
- **禁止**引入 ant icons / heroicons / iconify 等其他图标库（除非 PM 单点放行某一个）。

### 1.2 标准尺寸

| 场景 | 尺寸 | stroke | 颜色 |
|------|------|--------|------|
| 顶栏菜单 | 18px | 2 | 继承文字色 |
| 按钮内 | 16px | 2 | 继承文字色 |
| 表格操作列 | 16px | 1.75 | 继承文字色 |
| Toast 前缀 | 16px | 2 | 状态语义色 |
| Modal 标题前缀（危险）| 20px | 2 | `--danger` |
| 空状态插图（如用图标兜底）| 96px | 1.5 | `--text-tertiary` |

### 1.3 命名映射（核心）

| 含义 | lucide |
|------|--------|
| 发现 / 探索 | `compass` |
| 课程 / 学位 | `graduation-cap` |
| 游戏 | `gamepad-2` |
| 小说 / 书 | `book-open` |
| 个人中心 | `user-circle` |
| 用户管理 | `users` |
| 设置 | `settings` |
| 主题切换 | `sun` / `moon` |
| 通知 | `bell` |
| 语言 | `globe` |
| 搜索 | `search` |
| 筛选 | `sliders` |
| 排序 | `chevrons-up-down` / `chevron-up` / `chevron-down` |
| 关闭 | `x` |
| 成功 | `check-circle` |
| 错误 | `x-circle` |
| 警告 | `alert-triangle` |
| 信息 | `info` |
| 复制 | `copy` |
| 下载 | `download` |
| 上传 | `upload` |
| 删除 | `trash-2` |
| 编辑 | `pencil` |
| 添加 | `plus` |
| 返回 | `arrow-left` |
| 外链 | `external-link` |

> 新增图标需追加到 `system/packages/ui-kit/src/icons/index.ts` 的 export map，便于 PR review。

---

## 2. 插画

### 2.1 风格

- **线条 + 单色 + 红色高光**：主线条 1.5–2px stroke，颜色 `--text-tertiary`；点缀红色辅助高光（`--brand`，面积 < 15%）；
- **不用**：填色卡通 / 3D 渲染 / 真人插画 / 写实风；
- **形态**：抽象几何 + 学习场景元素（笔、本子、汉字部首、卷轴、罗盘…）；
- **暗模式**：使用 `currentColor`，颜色随主题切换；不要"亮 / 暗"两套硬编码颜色。

### 2.2 使用场景

| 场景 | 尺寸 | 备注 |
|------|------|------|
| 空状态（列表 / 搜索 / 错误页）| 96×96 / 128×128 | 居中，文字下方 |
| 404 / 403 / 500 错误页 | 160×160 | 居中，独占一块 |
| Onboarding（首次登录）| 240×240 | 配宣传文案 |
| 营销 / 落地页 | 自由 | 但仍守 §2.1 风格 |

### 2.3 来源

- 优先自绘（SVG inline），存放 `system/packages/ui-kit/src/illustrations/`；
- 第三方素材必须商业可用 + 改色为单色 + 添加红色高光 + 经设计 review；
- 严禁直接使用 unDraw / Storyset 默认彩色版本（违反唯一品牌色原则）。

---

## 3. 图片

### 3.1 通用

- 容器圆角 `radius-md`；
- 加载占位：骨架屏（同色块）+ 渐显（透明度 0→1，`--motion-base`）；
- 失败兜底：灰底（`--bg-active`）+ 16×16 `image-off` 图标居中；
- 暗模式：叠 `1px solid var(--border-subtle)` 防边缘融化；
- 懒加载：`<img loading="lazy">` 默认；首屏 hero 用 `eager`。

### 3.2 业务图片

| 场景 | 比例 | 尺寸 | 备注 |
|------|------|------|------|
| 课程封面 | 16:9 | min 640×360 | webp 优先 |
| 主题卡片 | 4:3 | min 480×360 | 同 |
| 小说封面 | 3:4 | min 240×320 | 同 |
| 用户上传（评论 / 反馈）| 任意 | max 5MB | 客户端转 webp + 压缩 |

### 3.3 二次封装组件

`<Image src={...} alt={...} aspect="16/9" loading="lazy" />`：
- 自动包圆角 + 占位骨架 + 失败兜底；
- 支持 `priority` prop 强制 `eager`；
- 禁止业务直接用 `<img>`（除非 review 单点放行）。

---

## 4. 头像

| 属性 | 值 |
|------|---|
| 形状 | 圆形 `radius-pill` |
| 默认尺寸 | 32px（顶栏）/ 24px（评论）/ 48px（个人中心）/ 96px（资料页）|
| 边框 | `1px solid var(--border-subtle)`，仅暗模式 |
| 兜底（无图）| `--brand` 底 + `--text-on-brand` 白字 + 首字符（取 display_name 首字 / 首字母）|
| 角标 | 在线状态（绿点 `--success` 6×6，右下，外圈 1px 白）|

实现：`<Avatar src={...} name={...} size="md" online={true} />`。

---

## 5. Logo

- **v1 形态**：文字 + 色块（`知语 · Zhiyu`，前缀 24×24 红色方块含"语"字简化图形）；
- 图形版 Logo 待定（[99-open-questions.md](./99-open-questions.md) Q1）；
- Logo 文件存放：`system/packages/ui-kit/src/brand/logo.tsx`（仅一个；亮 / 暗自动适配 `currentColor`）。

---

## 99. 待确认问题

| ID | 问题 | 影响 |
|----|------|------|
| Q1 | 图形版 Logo 是否在 v1 必需？目前 PM 决策为否（仅文字 + 色块），v2 设计师介入 | 落地页 / 营销物料 / favicon 视觉一致性 |
