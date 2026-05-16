<!-- TARGET-PATH: docs/C03-pages/discover-china/P-admin-discover-china-004.md -->

# `P-admin-discover-china-004` · 全局搜索结果聚合

> **path**:`/admin/china/search` · **query**:`q, scope=global|category|article, category_code?, article_id?`
> **R 覆盖**:R-016 · **冻结状态**:已冻结 · 2026-05-16

## 1. 布局
- 面包屑 `发现中国 > 搜索结果`;
- 搜索栏:输入 + 范围切换器 + 提交;
- 结果两栏聚合:`命中文章 N` · `命中句子 M`;
- 每条结果带"前往编辑"。

## 2. DOM 骨架
```
Breadcrumb
ScopeSearch { input, scope select, Btn 搜索 }
ResultArea {
  Section "命中文章 N" { ArticleHitRow ×N { 类目, 标题, snippet, →编辑 } }
  Section "命中句子 M" { SentenceHitRow ×M { 类目 / 文章, 中文 snippet, →编辑 } }
}
Pagination(双栏各一)
```

## 3. 数据
- `GET admin/china/search?q&scope&category_code&article_id&page&pageSize` → `{ articles, sentences }`(每段独立分页)。

## 4. 状态
| 态 | 表现 |
|---|------|
| idle | 默认(空 q 不查询) |
| loading | 双栏 skeleton |
| empty | 空态"没有命中『{q}』" + 修改搜索按钮 |
| error | Retry |

## 5. 交互
- 搜索提交 Enter / 点按钮;
- scope 切换实时联动后端;
- 命中行点击 → 跳对应 P-admin-002 或 P-admin-003 + anchor 到句子。

## 6. 错误码
- 422 q 过短(< 2 字)→ 字段内联;
- 5xx → Retry。

## 7-10. 略。
