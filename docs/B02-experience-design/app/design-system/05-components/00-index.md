# 组件清单 · 索引

> **阶段**：B02-XS 体验设计
> **角色**：设计系统工程师
> **归属**：按系统（app + admin 共享）
> **系统**：app
> **冻结状态**：未冻结

---

| 序号 | 文件 | 组件 |
|------|------|------|
| 01 | buttons | Button / IconButton |
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
- 底座：shadcn/ui，token 对应 `01-tokens.md`
- 触控目标：最小 44px（移动端）
