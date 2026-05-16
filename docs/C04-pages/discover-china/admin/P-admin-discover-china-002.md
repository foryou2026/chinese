<!-- TARGET-PATH: docs/C04-pages/discover-china/admin/P-admin-discover-china-002.md -->

# `P-admin-discover-china-002` · 类目下文章管理列表

> **path**:`/admin/china/categories/:code` · **R 覆盖**:R-009, R-013, R-014, R-016, R-019
> **冻结状态**:已冻结 · 2026-05-16

## 1. 布局
- 面包屑 `发现中国 > {类目名}`;
- 顶栏:`+ 新建文章` · `搜索框(本类目)` · `状态筛选(全部 / 待发布 / 已发布)`;
- 表格列出文章(分页);
- 行操作:`编辑 / 发布或下架 / 删除`。

## 2. DOM 骨架
```
Breadcrumb
Toolbar { Btn 新建 (data-op="OP-new"), SearchBox, StatusFilter, TotalBadge "共 N 篇" }
Table {
  Header[ 编码 / 拼音 / 中文标题 / 状态 / 句子数 / 更新时间 / 操作 ]
  Row ×N {
    code, pinyin, title_zh, StatusTag(draft|published), sentence_count, updated_at,
    Actions[ 编辑(→P-admin-003) / 发布或下架(R-013) / 删除(D-5 确认) ]
  }
}
Pagination
```

## 3. 数据
- `GET admin/china/categories/:code/articles?page&pageSize&q&status` → `{ items, total }`;
- `POST admin/china/articles`(D-1 Modal 提交);
- `PATCH admin/china/articles/:id { status }`;
- `DELETE admin/china/articles/:id`(软删)。

## 4. 状态
| 态 | 表现 |
|---|------|
| idle | 表格 |
| loading | 5 行 skeleton |
| empty | 空态"该类目下还没有文章" + `+ 新建`大按钮 |
| publishing | 行高亮 + spinner |
| deleting | 行半透明 + spinner |
| error | Retry |

## 5. 交互
- **新建文章**:点 → D-1 Modal,字段 `拼音 / 5 语标题`;提交后跳 P-admin-003 编辑;
- **发布**:`PATCH status=published` → 行刷新 → Toast 成功;
- **下架**:同上;**且后端清空所有用户该文章进度(R-013)**;UI 弹 D-5 确认"下架将清空所有用户阅读进度,确认?";
- **删除**:D-5 确认 → 软删 → 行消失;
- **搜索**:debounce 300ms,本类目范围;
- **状态切换 Tab**:`全部 / 待发布 / 已发布`。

## 6. 错误码
- 422 名称 5 语未齐 → Modal 内联字段错误;
- 409 拼音冲突 → Toast"该拼音已存在"。

## 7-10. 略,沿用管理端通用约定。
