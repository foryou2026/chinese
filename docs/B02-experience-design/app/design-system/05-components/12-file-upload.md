# 组件：FileUpload

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途与禁忌

- 用途：文件/图片上传（头像、作业、admin 素材管理）
- 禁忌：不用于纯文本输入（用 Textarea）

## 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| dropzone | 拖拽区域 + 点击上传 | 批量文件上传 |
| button | 按钮触发文件选择 | 单文件上传 |
| avatar | 圆形头像上传（点击更换） | 用户头像 |

## Dropzone

### Anatomy

```
┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐
│                                   │  ← .glass 毛玻璃面板
│     [upload icon: 40px]           │
│     [拖拽文件到此处或点击上传]      │  ← var(--font-display)
│     [支持 JPG/PNG, 最大 5MB]      │
│                                   │
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘
```

| 属性 | 值 |
|------|-----|
| 边框 | `2px dashed var(--color-neutral-300)` |
| 材质 | `var(--glass-3)` + `backdrop-filter: var(--glass-blur-sm)` |
| 圆角 | `var(--radius-lg)` |
| min-height | 120px |
| 图标 | `var(--color-neutral-400)`, 40px |
| 主文字 | `var(--text-sm)`, `var(--color-neutral-700)`, `var(--font-display)` |
| 辅助文字 | `var(--text-xs)`, `var(--color-neutral-400)` |

### 状态

| 状态 | 表现 |
|------|------|
| 默认 | dashed 边框，毛玻璃背景 |
| hover | 边框色 `var(--color-brand-400)`，背景 `var(--color-brand-50)` |
| focus | `var(--focus-ring)` |
| drag-over | 边框色 `var(--color-brand-default)`，背景 `var(--color-brand-50)`，图标动画上移 4px |
| disabled | `opacity: 0.45`, `pointer-events: none` |

## 文件列表项

### Anatomy

```
┌──────────────────────────────────┐
│ [type-icon] [filename] [size]  [X] │  ← var(--glass-3) 背景
│             [progress bar]         │
└──────────────────────────────────┘
```

### 状态

| 状态 | 表现 |
|------|------|
| 排队中 | 灰色进度条，"等待上传" |
| 上传中 | brand 色渐变进度条 + 百分比（`tabular-nums`） |
| 成功 | `var(--color-success-500)` emerald 图标，文件名可点击预览 |
| 失败 | `var(--color-danger-500)` red 图标 + 红色文件名 + "重试"链接 |
| 删除 hover | X 按钮变 `var(--color-danger-500)` |

## Avatar 变体

| 属性 | 值 |
|------|-----|
| 尺寸 | 96px 圆形 |
| 默认 | 显示当前头像或 fallback |
| hover | `var(--glass-3)` 遮罩 + 相机图标 |
| 点击 | 打开文件选择器（仅图片） |
| 上传中 | 圆形 ProgressBar 环绕（brand 渐变） |

## 行为

| 交互 | 行为 |
|------|------|
| 拖拽 | 文件拖入区域高亮，释放开始上传 |
| 点击 | 打开系统文件选择器 |
| 键盘 | Tab 聚焦 + Enter/Space 打开 |
| 文件校验 | 上传前校验类型/大小，不合规时 Toast 提示（danger） |
| 多文件 | 支持多选，逐个上传，显示队列进度 |
| 取消 | 上传中可取消单个文件 |

## a11y

- [ ] dropzone 有 `role="button"` + `aria-label`
- [ ] 文件 input `accept` 属性限制类型
- [ ] 上传进度 `aria-live="polite"` 通报
- [ ] 错误信息 `role="alert"`

---

## 99. 待确认问题

无
