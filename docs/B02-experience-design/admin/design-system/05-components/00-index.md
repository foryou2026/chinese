# 组件清单 · 索引（管理后台）

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：admin（管理后台专属）
> **系统**：admin
> **上游依赖**：../01-tokens.md
> **冻结状态**：未冻结

---

| 序号 | 文件 | 组件 |
|------|------|------|
| 01 | buttons | Button（primary/secondary/ghost/destructive/success/icon-only/link） |
| 02 | inputs | Input / Textarea / Select / Combobox / DatePicker |
| 03 | selection | Checkbox / Radio / Switch |
| 04 | table | Table（排序、筛选、分页、空态，紧凑 40px 行高） |
| 05 | form | Form（标准/内联/分步） |
| 06 | overlays | Modal / Drawer / Popover / Tooltip / Dropdown |
| 07 | tabs-accordion | Tabs / Accordion / Stepper |
| 08 | feedback | Toast / Alert / Banner |
| 09 | loading | Empty / Skeleton / Spinner / ProgressBar |
| 10 | identity | Avatar / Badge / Tag |
| 11 | pagination | Pagination / Breadcrumb |
| 12 | file-upload | FileUpload |

## 通用规则

- 所有组件定义 6 态：默认 / hover / focus / active / disabled / loading
- 异常态按组件需要定义：empty / error / readonly
- 底座：shadcn/ui + Tailwind CSS v4
- Token 对应：`../01-tokens.md`
  - 颜色用 `--color-neutral-*` / `--btn-{primary|secondary}-*` / `--color-accent` / `--color-{success|warning|danger|info}-*`
  - **禁止**引用 app 的 `--color-brand-*`、`--glass-*`
- 表面材质：纯实色背景 + 1px `var(--border-color)` 边框，**不使用**毛玻璃/透明度/backdrop-filter
- 焦点环：`:focus-visible` -> `box-shadow: var(--focus-ring)` = `0 0 0 3px rgba(59,130,246,0.30)`
- 触控目标：最小 44px（移动端）
- 字体：所有元素统一使用 `--font-sans`，代码/ID 用 `--font-mono`
- hover 效果：仅背景色变化，不使用 translateY 浮起或 scale 缩放
- 动效：`--motion-fast`（100ms ease）/ `--motion-base`（200ms ease-out），不使用弹簧缓动

---

## 99. 待确认问题

无
