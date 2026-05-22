# 组件：FileUpload（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md, ../04-status-colors.md
> **冻结状态**：未冻结

---

## 用途

文件/图片上传，支持拖拽和点击选择。

## 变体

| 变体 | 说明 | 适用 |
|------|------|------|
| dropzone | 大型拖拽区 | 批量文件上传 |
| button | 按钮式触发 | 单文件选择 |
| avatar | 圆形头像上传 | 用户头像 |

## Dropzone 样式

| 属性 | 值 |
|------|-----|
| 背景 | `var(--surface-primary)` |
| 边框 | 2px dashed `var(--border-color)` |
| 圆角 | `var(--radius-lg)` |
| 最小高度 | 160px |
| 图标尺寸 | 40px |
| 图标色 | `var(--color-neutral-300)` |
| 主文案 | `var(--text-sm)` `var(--text-primary)` |
| 副文案 | `var(--text-xs)` `var(--text-muted)` |

### 状态

| 状态 | 边框 | 背景 |
|------|------|------|
| 默认 | dashed `var(--border-color)` | `var(--surface-primary)` |
| hover | dashed `var(--border-hover)` | `var(--surface-hover)` |
| dragover | dashed `var(--color-accent)` | `var(--color-accent-50)` |
| error | dashed `var(--color-danger-500)` | `var(--color-danger-50)` |

## 文件列表项

| 属性 | 值 |
|------|-----|
| 高度 | 48px |
| 背景 | `var(--surface-primary)` |
| 边框 | 1px solid `var(--border-color)` |
| 圆角 | `var(--radius-md)` |
| 文件名 | `var(--text-sm)` 截断 |
| 文件大小 | `var(--text-xs)` `var(--text-muted)` |
| 进度条 | 内嵌 4px ProgressBar |
| 操作 | 删除按钮（icon-only） |

### 文件列表状态

| 状态 | 表现 |
|------|------|
| uploading | 进度条 + 百分比 |
| success | 绿色 ✓ 图标 |
| error | 红色 ✗ + 重试按钮 |

## 反例

- 不使用毛玻璃上传区
- 不使用动画弹跳上传成功效果

## a11y 验收点

- [ ] `<input type="file">` 隐藏但保持可聚焦
- [ ] dropzone `role="button"` + `tabindex="0"`
- [ ] 上传状态通过 `aria-live="polite"` 播报
- [ ] 删除按钮 `aria-label="删除 xxx"`

---

## 99. 待确认问题

无
