<!-- TARGET-PATH: docs/C01-requirements/discover-china/category/baseline.md -->

# 需求与权限基线 · category

> **阶段**：C01-RP · 需求分析师 + 权限工程师
> **模块**：`discover-china`
> **功能**：`category`（admin 类目管理）
> **上游依赖**：`_input/draft.md`、`../baseline.md`（模块级参考）、`B01-architecture/08-surfaces.md`
> **冻结状态**：已冻结 · 2026-05-16
> **下游影响**：C02-ia-interaction/discover-china/category/

---

## 0. 摘要

- 给谁：admin 端内容运营管理员（U2）。
- 做什么：展示 12 个固定类目的已发布 / 总文章数统计，支持进入类目内容管理；类目本身永不可删除。
- 最大价值：运营一眼看到各类目内容缺口，优先补充薄弱类目。
- 最大风险：统计数字不实时或不准确，导致运营决策偏差。

---

## 2. 需求清单

| R-ID | 标题 | 涉及角色 | 关联页面 | 验收要点 |
|------|------|---------|---------|---------|
| R-discover-china-008 | 12 类目统计 | ROLE-ADMIN | P-admin-discover-china-001 | 每类目显示"已发布数 / 总数"，实时刷新 |
| R-discover-china-018 | 类目固定不可删 | ROLE-ADMIN | P-admin-discover-china-001 | 12 类目永不可删 |

---

## 4. 业务规则（功能范围）

| 规则 ID | 描述 | 来源 R-ID | 边界值 |
|--------|------|---------|--------|
| BR-1 | 12 类目数量固定，类目永不可删 | R-discover-china-018 | — |

> 角色定义、权限矩阵、NFR 见模块基线 `../baseline.md §5-§8`。

---

## 99. 待确认问题

（无）
