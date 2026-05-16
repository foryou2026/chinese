<!-- TARGET-PATH: docs/B04-design/design-system/04-status-colors.md -->

# 04 · 状态色与基础组件

> **阶段**：B04-S  
> **上游**：`01-tokens.md`、`B03-ux/04-voice-tone.md`、`B03-ux/06-experience-principles.md`、`grules/G2-视觉与交互风格/04-状态与组件.md`  
> **下游**：`system/packages/ui-kit/src/components/`、所有 C03 4 态文案承载  
> **冻结状态**：已冻结 · 2026-04-28

---

## 0. 摘要

- 状态色严格遵守"黑白红 + 中性语义"：错误 / 拒绝 / 取消统一复用品牌红。
- 组件：StatusTag / Button / Table / Form / Modal / Drawer / Toast / Confirm；全部毛玻璃化。
- 业务页面**禁止**直接用 shadcn/ui 原始组件，必须经 `ui-kit` 二次封装。

---

## 1. 状态标签 `<StatusTag />`

> 通用枚举；禁止手写颜色。

| 状态语义 | 背景 | 文字 | 适用枚举 |
|---------|------|------|---------|
| 初始 / 草稿 | `--bg-active` | `--text-secondary` | `draft / pending` |
| 进行中 | `--bg-active` + 1px `--border-strong` 虚线 | `--text-primary` | `active / processing / in_progress` |
| 成功 / 完成 | `--success-soft` | `--success` | `done / completed / success / paid` |
| 警告 | `--warning-soft` | `--warning` | `warning / pending_review / overdue` |
| 失败 / 拒绝 / 取消 | `--danger-soft` | `--danger`（= `--brand`）| `failed / rejected / cancelled / refunded` |
| 已归档 / 已关闭 | `--bg-active` | `--text-tertiary` | `archived / closed` |

- 形状：`radius-pill`，高度 22px，内边距左右 8px，字号 `text-tag`；
- 图标可选（文字左 4px，尺寸 12px）。

---

## 2. 按钮 `<Button />`

| 类型 | 场景 | 背景 | 文字 | 边框 | 高度 (sm/md/lg) | 圆角 | 备注 |
|------|------|------|------|------|----|------|------|
| `primary` | 创建 / 提交 | `--brand` | `--text-on-brand` | 无 | 28/32/36 | `radius-sm` | hover→`--brand-hover`；active→`--brand-active` |
| `secondary` | 筛选 / 导出 | `.glass-button` | `--text-primary` | `--border-subtle` | 28/32/36 | `radius-sm` | hover 加 `--bg-hover` |
| `danger` | 删除 / 重置 | `--danger-soft` | `--danger` | `--danger` 1px | 28/32/36 | `radius-sm` | hover 变实色 `--brand` + 白字 |
| `ghost` | 表格内操作 | 透明 | `--text-primary` | 无 | 28 | `radius-sm` | hover 加 `--bg-hover` |
| `link` | 表单内跳转 | 透明 | `--brand` | 无 | 行内 | — | hover 下划线 |
| 禁用 | — | `--bg-active` | `--text-disabled` | `--border-subtle` | 同 | 同 | `cursor: not-allowed`；禁止 hover 变化 |
| Loading | — | 同原态 + 左侧 14px Spinner | 文字保持 | — | 同 | — | 自动禁用点击；见 [05 §1](./05-interactions.md) |

- 默认 `md`；移动端默认 `lg`（更易触控）；
- **每个区段 / 弹窗只允许 1 个 primary**（B03 克制原则）；
- 图标按钮（icon-only）36×36 / 32×32 正方形，必须 `aria-label`。

---

## 3. 表格 `<Table />`

| 属性 | 值 |
|------|---|
| 容器 | `<GlassCard>`，圆角 `radius-md` |
| 表头背景 | 透明（毛玻璃透出）；文字 `text-caption` / 字重 600 / `--text-secondary` |
| 行高 | 桌面 48 / 移动 56 |
| 斑马纹 | **不开**（叠毛玻璃易脏）|
| hover 行 | `--bg-hover` |
| 选中行 | `--brand-soft` + `--text-primary` |
| 边框 | 行间 1px `--border-subtle`；外层卡片自带边框 |
| 操作列 | **固定右侧**；按钮间距 8px；文字按钮（ghost）|
| 排序 | `chevrons-up-down` 12px；激活后 `chevron-up/down` + `--brand` |

### 3.1 空状态

行内插画 48×48 + "暂无数据"（`--text-secondary`）+ 可选 `New` 主按钮，居中，纵向 `space-6` 留白。

### 3.2 加载

骨架屏行数 = 当前 `pageSize`；每行 4 个矩形条占位（按列宽分布）。

### 3.3 大数据量

行数 > 100 必须 TanStack Virtual 虚拟滚动；表头 sticky。

---

## 4. 表单 `<Form />`

| 属性 | 值 |
|------|---|
| 标签位置 | 桌面 / 移动**均在上方**（不要左右布局）|
| 标签字号 / 字重 | `text-caption` / 500 |
| 字段间距 | `space-4` |
| 输入框高度 | 36（默认）/ 32（紧凑）/ 44（移动）|
| 输入框背景 | `.glass-button`（半透明 + `--glass-blur-sm`）|
| 输入框边框 | `--border-strong` 1px；focus → 2px `--ring` |
| 必填标记 | 标签后 4px，红色 `*` |
| 错误提示颜色 | `--danger` |
| 错误提示字号 / 位置 | `text-caption`；字段下方 4px，与标签同列对齐 |
| 字数限制 | 字段右下角，`text-caption text-tertiary`；超限变 `--danger` |
| 帮助文案 | 字段下方 4px，`text-caption text-tertiary`，**与错误提示互斥** |

- Select / Combobox / DatePicker 弹层一律 `.glass-panel`；
- 表单按钮区：**右下角，取消左 + 主按钮右**（与弹窗一致；B03 红线）。

---

## 5. 弹窗 Modal `<Modal />`

| 属性 | 值 |
|------|---|
| 默认宽度 | 480px |
| 大弹窗 | 720px |
| 全屏断点 | `< 640px` 宽 = `100vw - 16px`，高 = `90vh`，从底部弹起 |
| 遮罩 | `--bg-overlay` |
| 容器 | `.glass-modal`（高强度毛玻璃 + `radius-lg`）|
| 标题 | `text-h3` / 600 |
| 内容内边距 | 24px |
| 底部按钮 | **右对齐 + 取消左 / 确认右** |
| 关闭 | 右上 X + ESC + 点遮罩（**危险弹窗禁用点遮罩**）|
| 进入动效 | 透明度 0→1 + 缩放 0.96→1，`--motion-slow` |

---

## 6. 抽屉 Drawer `<Drawer />`

| 属性 | 值 |
|------|---|
| 默认宽度 | 桌面 480 / 移动 100% |
| 滑出方向 | **右侧** |
| 容器 | `.glass-modal` 风格 |
| 遮罩 | `--bg-overlay` |
| 关闭 | 右上 X + ESC + 点遮罩 |
| 顶部 | 标题（`text-h3`）+ X 按钮；下方 1px `--border-subtle` |
| 底部 | 操作区固定底部：取消左 / 主按钮右；含 `safe-area-inset-bottom` |

> 移动端导航 Drawer 同遵守。

---

## 7. 消息提示 Toast `<Toast />`

| 属性 | 值 |
|------|---|
| 位置 | **顶部居中**，距顶栏底部 16px |
| 容器 | `.glass-toast`（毛玻璃 + `radius-md` + `shadow-md`）|
| 进入 | 自顶向下 16px → 0，`--motion-base` |
| 自动消失 | 成功 3s / 错误 5s / 警告 4s |
| 同时上限 | 3 条；超出时最旧的提前消失 |
| 成功 | 左 16px `check-circle` `--success` + 文字 `--text-primary` |
| 错误 | 左 `x-circle` `--danger` + 文字 `--text-primary` |
| 警告 | 左 `alert-triangle` `--warning` + 文字 `--text-primary` |
| 信息 | 左 `info` `--text-secondary` + 文字 `--text-primary` |
| 关闭 | 右侧 X 图标（hover 时显示）|

> Toast **只用于"不可恢复错误（5xx / 网络）/ 信息确认"**；表单字段错误一律内联（[05 §8](./05-interactions.md)）。

---

## 8. 确认弹窗 `<Confirm />`（危险操作）

| 属性 | 值 |
|------|---|
| 触发 | 删除 / 重置 / 不可撤销操作 |
| 容器 | Modal 480px，`.glass-modal` |
| 标题 | "确认删除 / 确认重置 / 确认 XX" |
| 内容 | "确定要 XX「{name}」吗？此操作不可撤销。" |
| 标题图标 | `alert-triangle` 20px `--danger` |
| 取消按钮 | `secondary` |
| 确认按钮 | **`danger`**（红色危险按钮）|
| 关闭 | X + ESC（**禁用点遮罩**）|
| 二次确认（高危）| 输入对象名匹配后才能点确认（适用于"删除用户 / 删除课程"等不可恢复）|

---

## 9. 组件目录约定

- 全部毛玻璃组件来自 `system/packages/ui-kit/src/components/`：
  - `GlassNav`、`GlassCard`、`GlassButton`、`GlassModal`、`GlassDrawer`、`GlassTabs`、`GlassToast`、`StatusTag`、`Skeleton`、`PageHeader`、`PageContent`、`EmptyState`、`Confirm`；
- 业务页面**禁止**直接使用 shadcn/ui 原始组件（`<Card>` / `<Dialog>` 等）；必须经 `ui-kit` 二次封装以保证毛玻璃主题统一。
- Storybook 必须给每个组件提供 4 态（idle / hover / active / disabled）+ 亮 / 暗双主题。

---

## 99. 待确认问题
（无）
