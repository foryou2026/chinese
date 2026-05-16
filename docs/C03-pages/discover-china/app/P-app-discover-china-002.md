<!-- TARGET-PATH: docs/C03-pages/discover-china/app/P-app-discover-china-002.md -->

# `P-app-discover-china-002` · 类目下文章列表

> **阶段**:C03-N · **path**:`/china/categories/:code` · **R 覆盖**:R-002, R-007
> **角色可见**:公开(01-03)/ 登录(04-12) · **冻结状态**:已冻结 · 2026-05-16

## 1. 布局
- 顶部面包屑:`发现中国 > {类目名}`;
- 标题区:H1 类目名(中 + 本地)+ 介绍;
- 搜索框(仅展示本类目可见语言)+ 文章列表分页。

## 2. DOM 骨架
```
Breadcrumb
PageHeader { h1, p }
SearchBar { input placeholder="搜索本类目文章" }
ArticleList {
  ArticleRow ×N {
    pinyin(text-caption)
    h2 中文标题
    h3 本地语标题(中文用户隐藏)
    meta { 句子数, 更新时间(本地化) }
  }
}
Pagination
```

## 3. 数据
- `GET china/categories/:code/articles?page&pageSize&q` → `{ items, total }`;
- 仅返回 `status=published`。

## 4. 状态
| 态 | 触发 | 表现 |
|---|------|------|
| idle | 默认 | 列表渲染 |
| loading | 首屏 / 翻页 | 5 行 skeleton |
| empty | items.length=0 + q="" | 空态插画"暂无文章,敬请期待" + 返回类目按钮 |
| empty-search | items.length=0 + q!="" | 空态"没有命中『{q}』" + 清除搜索 |
| error | 5xx | ErrorBoundary |
| forbidden | 04-12 未登录(理论已被 P-001 拦截) | 跳 login |

## 5. 交互
- 行点击 → `/china/articles/{code}`;
- 搜索 debounce 300ms;
- 中文用户搜索框仅匹配中文;非中文用户匹配 中文 + 本地语 两列(R-007)。

## 6. 错误码
- 404 类目不存在 → 整页空态"类目不存在" + 返回 /china;
- 5xx → Retry。

## 7. 移动端
- 行简化:仅标题 + 句子数 meta;
- 上拉加载更多(分页改无限滚动)。

## 8. 无障碍
- 列表 `<ul>` 语义 + 行 `<a>`;
- 搜索框 `<label>` 关联。

## 9. 性能 / 埋点
- 列表 SWR 30s;
- 翻页 `china.article_list_page`,搜索 `china.article_search`。
