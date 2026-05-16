<!-- TARGET-PATH: docs/D01-data/app-auth/00-index.md -->

# D01 · `app-auth` 数据规范

> **阶段**：D01-D · **feature**：`app-auth`  
> **上游**：[`B02-permissions/04-data-model.md`](../../B02-permissions/04-data-model.md)、[`C05-prd/app-auth/07-business-rules.md`](../../C05-prd/app-auth/07-business-rules.md)  
> **下游**：[`D02-api/app-auth/`](../../D02-api/app-auth/00-index.md)  
> **冻结状态**：已冻结 · 2026-05-16

---

## 关键结论

> **本 feature 不新增任何表。**  
> 5 张涉及表 100% 来自 B02-04 数据模型（auth.users / profiles / user_sessions / auth_login_attempts / audit_logs）；本目录只列出"本 feature 如何使用这些表"以及验证规则、索引依赖与种子数据。

---

## 文件清单

| 序号 | 文件 | 职责 |
|------|------|------|
| _input | [_input/data-rules.md](./_input/data-rules.md) | 输入 |
| 00 | 00-index.md（本文）| 索引 + 关键结论 |
| 01 | [01-er-diagram.md](./01-er-diagram.md) | 子 ER 图（5 表中本 feature 涉及的字段）|
| 02 | [02-entities/](./02-entities/) | 5 个实体精简卡片（重定向到 B02-04）|
| 03 | [03-business-rules.md](./03-business-rules.md) | 数据写入约束 |
| 04 | [04-validations.md](./04-validations.md) | zod / DB constraint 校验清单 |
| 05 | [05-calculations.md](./05-calculations.md) | 计算字段：邮箱脱敏 / 强度等级 |
| 06 | [06-indexes.md](./06-indexes.md) | 关键索引（已在 B02-04 创建，本节列依赖）|
| 07 | [07-volume-growth.md](./07-volume-growth.md) | 量级预估 |
| 08 | [08-seed-data.md](./08-seed-data.md) | super_admin 种子数据指引 |
| 99 | [99-open-questions.md](./99-open-questions.md) | 无 |
