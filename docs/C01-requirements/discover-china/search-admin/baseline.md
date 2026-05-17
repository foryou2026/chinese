<!-- TARGET-PATH: docs/C01-requirements/discover-china/search-admin/baseline.md -->

# 需求与权限基线 · search-admin

> **阶段**：C01-RP · 需求分析师 + 权限工程师
> **模块**：`discover-china`
> **功能**：`search-admin`（admin 全文搜索）
> **上游依赖**：`_input/draft.md`、`../baseline.md`（模块级参考）、`B01-architecture/08-surfaces.md`
> **冻结状态**：已冻结 · 2026-05-16
> **下游影响**：C02-ia-interaction/discover-china/search-admin/

---

## 0. 摘要

- 给谁：admin 端内容运营管理员（U2）。
- 做什么：三级搜索（类目层全局 / 文章层本类目 / 句子层本文），聚合呈现命中结果并支持跳转编辑。
- 最大价值：运营快速定位需要修改的文章或句子，无需逐层级手动翻找。
- 最大风险：跨类目 / 文章层级的聚合搜索结果分页或高亮逻辑错误导致定位失准。

---

## 2. 需求清单

| R-ID | 标题 | 涉及角色 | 关联页面 | 验收要点 |
|------|------|---------|---------|---------|
| R-discover-china-016 | 三级搜索 | ROLE-ADMIN | P-admin-discover-china-004 | 类目层全局 / 文章层本类目 / 句子层本文；聚合呈现 |

---

## 4. 业务规则（功能范围）

（无额外规则；搜索结果遵循管理端全局可见范围，含草稿，见模块基线 §6.2。）

> 角色定义、权限矩阵、NFR 见模块基线 `../baseline.md §5-§8`。

---

## 99. 待确认问题

- [ ] Q1：搜索是否对草稿态文章 / 句子也可见？（影响：C02 查询范围 + D01 索引范围）
