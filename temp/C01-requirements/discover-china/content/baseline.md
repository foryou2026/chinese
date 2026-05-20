<!-- TARGET-PATH: docs/C01-requirements/discover-china/content/baseline.md -->

# 需求与权限基线 · content

> **阶段**：C01-RP · 需求分析师 + 权限工程师
> **模块**：`discover-china`
> **功能**：`content`（admin 文章编辑管理）
> **上游依赖**：`_input/draft.md`、`../baseline.md`（模块级参考）、`B01-architecture/08-surfaces.md`
> **冻结状态**：已冻结 · 2026-05-16
> **下游影响**：C02-ia-interaction/discover-china/content/

---

## 0. 摘要

- 给谁：admin 端内容运营管理员（U2）。
- 做什么：文章列表 CRUD + 发布状态切换、文章 5 语 Tab 编辑（每句 5 语 + 拼音 + 中文校对）、句子任意位置插入 / 拖拽重排、危险操作二次确认、未保存离开拦截、多人编辑后写覆盖。
- 最大价值：批量录入 + 句子级精编，保证高质量双语对照内容安全发布。
- 最大风险：多管理员并发编辑后写覆盖导致他人改动丢失；句子重排后 TTS 缓存键失效需及时清理。

---

## 2. 需求清单

| R-ID | 标题 | 涉及角色 | 关联页面 | 验收要点 |
|------|------|---------|---------|---------|
| R-discover-china-009 | 文章列表 CRUD | ROLE-ADMIN | P-admin-discover-china-002 | 分页 / 搜索 / 新建 / 编辑 / 删除 / 发布 / 下架 |
| R-discover-china-010 | 文章 5 语 Tab 编辑 | ROLE-ADMIN | P-admin-discover-china-003 | 基本信息 + 句子分页；每句 5 语 Tab + 拼音 + 中文校对 |
| R-discover-china-011 | 句子任意位置插入 | ROLE-ADMIN | P-admin-discover-china-003 | "开头 / 结尾 / 当前后插入"三按钮；插入后句子顺序自动重排 |
| R-discover-china-012 | 句子重排 | ROLE-ADMIN | P-admin-discover-china-003 | 拖拽排序；保存后句子序号重分配；缓存键随之更新 |
| R-discover-china-013 | 文章发布状态切换 | ROLE-ADMIN | P-admin-discover-china-002 | 待发布 ↔ 已发布；下架后清空所有用户该文章进度 |
| R-discover-china-014 | 危险操作二次确认 | ROLE-ADMIN | P-admin-discover-china-002 / 003 | 删除 / 下架 / 大批量修改前弹层确认 |
| R-discover-china-015 | 未保存离开拦截 | ROLE-ADMIN | P-admin-discover-china-003 | 表单脏 + 路由切换 / 关页 → 拦截弹层 |
| R-discover-china-017 | 多人编辑后写覆盖 + 提示 | ROLE-ADMIN | P-admin-discover-china-003 | 保存时若已被他人更新则覆盖并提示被谁覆盖 |
| R-discover-china-019 | 软删后物理清理 | 系统 | — | 软删 30 天后物理清理（类目除外） |
| R-discover-china-020 | 文章下架后清空阅读进度 | 系统 | — | 下架后清空所有用户该文章进度 |

---

## 4. 业务规则（功能范围）

| 规则 ID | 描述 | 来源 R-ID | 边界值 |
|--------|------|---------|--------|
| BR-3 | 文章发布前必须 5 语齐备（草稿允许缺） | R-discover-china-010 | — |
| BR-4 | 句子序号在所属文章内连续递增，重排后自动重写 | R-discover-china-011 / 012 | — |
| BR-5 | 文章编码 = 类目编码（2 位）+ 文章序号（10 位，左补零） | R-discover-china-010 | — |
| BR-6 | TTS 缓存键随句子序号变化失效；重排后旧键回收 | R-discover-china-012 | — |
| BR-8 | 多人编辑使用"后写覆盖 + 提示"语义，不做强锁 | R-discover-china-017 | — |
| BR-9 | 文章下架后立即清空所有用户对该文章的阅读进度 | R-discover-china-013 | — |
| BR-10 | 软删 30 天后物理清理 | R-discover-china-019 | — |

> 角色定义、权限矩阵、NFR 见模块基线 `../baseline.md §5-§8`。

---

## 99. 待确认问题

（无）
