<!-- TARGET-PATH: docs/A00-meta/changelog.md -->

# A00 · changelog · 跨阶段变更与冻结记录

> 本文件按时间倒序记录所有阶段产物的「冻结 / 变更 / 解冻」事件，以及全局一致性审计。

---

## 2026-05-16 · 一致性审计与 zero-bug 定版

| 日期 | 范围 | 操作 | 说明 |
|------|------|------|------|
| 2026-05-16 R6 | `docs/**/*.md` (374) + `docs/**/*.html` (47) | 定版 | per-file × 17 维度审计；374/374 MD + 47/47 HTML 全 ✓；C01-C06 启动前的最终基线。详见 [consistency-audit-2026-05-16-round6.md](./consistency-audit-2026-05-16-round6.md) |
| 2026-05-16 R5 | `docs/**/*.md` + `prompt/**/*.md` (373) | 审计 | per-file × 11 维度全量审计，373/373 ✓。详见 [consistency-audit-2026-05-16-round5.md](./consistency-audit-2026-05-16-round5.md) |
| 2026-05-16 R4 | C02 系列 | 反向恢复 | R3 过度抽象的「Supabase/v1/SDK」名词在 C02-permissions 内有限恢复（C02 是权限规范层，需点明实现底座）；修破损片段 `鉴权与数据底座-js` `/首版/` `首版.0` 等。未生成独立报告，规则沉淀进 R6 §1 D5 维度。 |
| 2026-05-16 R3 | C01/C03/C04/C06 全部 | 全局禁词清零 | 角色统一为 admin/user 两角色；删 mermaid、Supabase API、表名、`/v1/*` 路径、版本/阶段措辞；C06 重组（删 11-roadmap，rename 12-changelog→11-changelog）。详见 [consistency-audit-2026-05-16-round3.md](./consistency-audit-2026-05-16-round3.md) |
| 2026-05-16 R2 | 全局 | 框架对齐 | 12 阶段 → F+C 双周期模型；阶段编码 B04-S→B03-S、C02-I→C03-I、C03-N→C04-N、C04-H→C05-H、C05-E→C06-E；C02 文件合并；C04/C05/C06 引入 surface 拆分；reduce broken links 176→78。详见 [consistency-audit-2026-05-16-round2.md](./consistency-audit-2026-05-16-round2.md) |
| 2026-05-16 R1 | docs vs backup | 真值对齐 | 与 `/backup` 系统对齐：保留 Paddle 支付、DB 字段 `is_active`、5 主题、Edge Functions 仅 B01 保留。详见 [consistency-audit-2026-05-16.md](./consistency-audit-2026-05-16.md) |
| 2026-05-16 | 全 `docs/` 当前内容 | 初始化 | 以本日仓库内容作为基线，正式启用本 changelog；此前的所有迭代过程不再追溯记录。 |

---

## 变更约定

- 任何已冻结文件需修改前：在文件头把 `冻结状态` 改为 `变更中`，新开对话让 AI 先出 diff 报告，再改。
- F 层变更广播：B01~B03 任一文件变更，须在本文件追加一行「受影响 feature 列表」，并触发它们的 D03 V 重跑。
- 解冻 / 重冻 都要在本文件追加一行（YYYY-MM-DD · 文件 · 操作 · 签字）。
- 全局审计：每次完成 cross-feature 大规模审计，在本表追加一行 + 独立报告写入 `docs/A00-meta/consistency-audit-<YYYY-MM-DD>-round<N>.md`。
