# 组件：Empty / Skeleton / Spinner / ProgressBar

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

## Empty

### 用途

数据为空时的占位展示，引导用户下一步操作。

### 变体

| 变体 | 说明 | 示例语境 |
|------|------|---------|
| default | 图标 + 文字 + 操作按钮 | 列表无数据 |
| search | 搜索无结果 | "未找到匹配结果" |
| error | 加载失败 | "加载失败，点击重试" |

### 材质

| 属性 | 值 |
|------|-----|
| 容器 | `.glass` 毛玻璃面板 + `backdrop-filter: var(--glass-blur-sm)` |
| 圆角 | `var(--radius-lg)` |

### Anatomy

```
      [icon: 48px, var(--color-neutral-300)]
      [title: var(--text-base), var(--weight-semibold), var(--font-display)]
      [description: var(--text-sm), var(--color-neutral-500)]
      [action button: .proto-btn-secondary md]
```

| 属性 | 值 |
|------|-----|
| 图标尺寸 | 48px |
| 图标颜色 | `var(--color-neutral-300)` |
| 标题 | `var(--text-base)`, `var(--weight-semibold)`, `var(--font-display)` |
| 描述 | `var(--text-sm)`, `var(--color-neutral-500)` |
| 按钮 | 可选，`.proto-btn-secondary` |
| 内容居中 | 水平垂直居中 |
| 最小高度 | 200px |

---

## Skeleton

### 用途

内容加载中的占位骨架，模拟最终布局形态。

### 变体

| 变体 | 说明 |
|------|------|
| text | 单行文字占位（高度 16px，圆角 `var(--radius-xs)`） |
| title | 标题占位（高度 24px，宽度 60%） |
| avatar | 圆形占位（40px / 48px） |
| card | 卡片占位（组合 avatar + title + text） |
| table-row | 表格行占位 |
| image | 矩形占位（圆角 `var(--radius-sm)`） |

### 样式

| 属性 | Light | Dark |
|------|-------|------|
| 背景 | `var(--glass-3)` (暖米白半透) | `var(--glass-3)` (墨青半透) |
| shimmer | 左→右暖白渐变扫过 | 左→右冷白渐变扫过 |
| 动画 | 1.5s infinite | 1.5s infinite |
| 圆角 | 跟随目标组件圆角 | — |

### 动画

```css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
```

Light: `linear-gradient(90deg, transparent 0%, rgba(255,251,240,0.5) 50%, transparent 100%)`
Dark: `linear-gradient(90deg, transparent 0%, rgba(168,192,212,0.15) 50%, transparent 100%)`

### 使用原则

- Skeleton 布局必须与真实内容布局一致，避免加载完成后布局跳变
- 列表 Skeleton 显示 3-5 行
- 不用于已有缓存数据的刷新场景（用 Spinner 叠加在内容上方）

---

## Spinner

### 用途

小范围加载指示（按钮内、局部刷新、无限滚动加载更多）。

### 尺寸

| 尺寸 | 直径 | 线宽 | 场景 |
|------|------|------|------|
| sm | 16px | 2px | 按钮内 |
| md | 24px | 3px | 区域加载 |
| lg | 40px | 4px | 页面级加载 |

### 样式

| 属性 | 值 |
|------|-----|
| 颜色 | `var(--color-brand-default)`（默认）/ `var(--color-brand-on)`（在品牌色按钮内） |
| 轨道 | `var(--color-neutral-200)`（可选） |
| 动画 | `rotate 360deg`，0.8s linear infinite |

### a11y

- `role="status"`
- `aria-label="加载中"`

---

## ProgressBar

### 用途

展示确定或不确定进度（文件上传、课程完成度、XP 进度）。

### 变体

| 变体 | 说明 |
|------|------|
| determinate | 已知进度百分比 |
| indeterminate | 未知进度，循环动画 |

### 尺寸

| 尺寸 | 高度 | 圆角 |
|------|------|------|
| sm | 4px | `var(--radius-pill)` |
| md | 8px | `var(--radius-pill)` |
| lg | 12px | `var(--radius-pill)` |

### 样式

| 属性 | 值 |
|------|-----|
| 轨道背景 | `var(--color-neutral-200)` |
| 默认填充 | `linear-gradient(90deg, var(--color-brand-700), var(--color-brand-500))` |
| 成功填充 | `linear-gradient(90deg, var(--color-success-700), var(--color-success-500))` |
| 动画（determinate） | 宽度过渡 `var(--motion-base)` `var(--easing-out)` |
| 动画（indeterminate） | 左右循环滑动，2s infinite |
| 文字标签 | 可选，右侧或上方显示 "60%"，`tabular-nums` |

### 状态

| 状态 | 表现 |
|------|------|
| 0% | 仅轨道，无填充 |
| 1-99% | 填充条宽度对应百分比 |
| 100% | 满条 + 可选变色为 success 翠玉 |
| error | 填充条变为 `var(--color-danger-500)` |

### a11y

- `role="progressbar"`
- `aria-valuenow` / `aria-valuemin` / `aria-valuemax`
- indeterminate 时不设 `aria-valuenow`

---

## 99. 待确认问题

无
