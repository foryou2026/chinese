# 组件清单 · 索引

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **冻结状态**：未冻结

---

| 序号 | 文件 | 组件 |
|------|------|------|
| 01 | buttons | Button（primary/secondary/ghost/glass/destructive/success）/ IconButton |
| 02 | inputs | Input / Textarea / Select / Combobox / DatePicker |
| 03 | selection | Checkbox / Radio / Switch |
| 04 | table | Table（排序、筛选、分页、空态） |
| 05 | form | Form（校验、错误显示） |
| 06 | overlays | Modal / Drawer / Popover / Tooltip / Dropdown |
| 07 | tabs-accordion | Tabs / Accordion / Stepper |
| 08 | feedback | Toast / Alert / Banner |
| 09 | loading | Empty / Skeleton / Spinner / ProgressBar |
| 10 | identity | Avatar / Badge / Tag / Chip |
| 11 | pagination | Pagination / Breadcrumb |
| 12 | file-upload | FileUpload |

## 通用规则

- 所有组件定义 6 态：默认 / hover / focus / active / disabled / loading
- 异常态按组件需要定义：empty / error / readonly
- 底座：shadcn/ui + Tailwind CSS v4
- Token 对应：`01-tokens.md`（颜色用 `--color-brand-*` / `--color-neutral-*`，禁止直接引用色族如 `--color-ink-*`）
- 表面材质：毛玻璃为唯一表面语言，卡片/面板用 `.glass` / `.glass-strong`
- 焦点环：`:focus-visible` → `box-shadow: var(--focus-ring)`
- 触控目标：最小 44px（移动端）
- 字体：标签/标题用 `--font-display`，正文用 `--font-sans`，`--font-brush` 仅限印鉴/品牌名
