<!-- TARGET-PATH: docs/A00-meta/consistency-audit-2026-05-16-round2.md -->

# 一致性审计报告 · 2026-05-16 · Round 2（全局规范对齐）

> **目的**：将 `/docs` 全部产物对齐 `/prompt/A-framework` 当前版本（F + C 双周期模型；阶段编码 B01-A / B02-X / B03-S / C01-R / C02-P / C03-I / C04-N / C05-H / C06-E / D01-D / D02-L / D03-V），消除一切残留的旧 12 阶段命名、旧文件名、旧目录结构造成的矛盾、错误引用、错命名。
>
> **承接**：[`consistency-audit-2026-05-16.md`](./consistency-audit-2026-05-16.md)（Round 1 — backup 真值对齐）。
>
> **结论**：本轮共扫到 **6 类一致性问题**，使用 4 个机械化脚本 + 多次手工修订 **共修改 156 个文件**；剩余 78 条疑似断链全部归类为「可接受的预期遗留」（详见 §6）。

---

## 1. 检查范围与方法

- **输入规范**：`prompt/A-framework/A00-{00..04}.md`（5 个框架文件，作为权威）
- **检查对象**：`docs/` 下全部 markdown / HTML（含 `B01–B03 / C01–C06 / A00`，共 700+ 文件）
- **方法**：
  1. 派发 3 路并行 Explore 子代理通读各层；
  2. 汇总后写 4 轮机械化 Python 脚本（`/tmp/zhiyu_fix{,2,3,4}.py`）批量修补；
  3. 写链接完整性检查脚本（`/tmp/zhiyu_check_links.py`）做最终断链扫描。

---

## 2. 问题清单与处置

### 2.1 阶段编码全面错位（高发）

旧 `/docs` 沿用 12 阶段编号（B01..B05、C01..C07），与现行框架（F+C 双周期）不符。

| 旧 → 新 | 命中规模 |
|---------|---------|
| `B03-X`（旧 UX）→ `B02-X` | header / 标题 / 正文混用 |
| `B04-S`（旧设计）→ `B03-S` | 同上 |
| `C02-I`（旧 IA）→ `C03-I` | 同上 |
| `C03-N`（旧页面）→ `C04-N` | 同上 |
| `C04-H`（旧原型）→ `C05-H` | 同上 |
| `C05-E`（旧 PRD）→ `C06-E` | 同上 |
| `B04` 正文裸引用（设计系统）→ `B03` | 90+ 处（C06 PRD 与 design-summary 全套） |
| `B04-04 / B04-05 / B04-06 / B04-07` → `B03-04 / B03-06 / B03-07 / B03-99-扩展` | C06 各 page-spec |

**处置**：脚本机械化重写 `/tmp/zhiyu_fix.py` + `/tmp/zhiyu_fix2.py`，共影响 71 + 52 = **123 个文件**；保留 `A00-meta/changelog.md` 与 `_input/*` 中作为历史记录的旧编号。

### 2.2 设计系统目录文件改名后未同步引用

`B03-design/design-system/` 之前曾整组改名（详见 `changelog.md` Round 5），引用未全部更新：

| 旧文件名 | 现文件名 |
|---------|---------|
| `04-status-components.md` | `04-status-colors.md`（部分组件部分迁入 `05-components/`） |
| `05-interactions.md` | `06-interactions.md` |
| `06-responsive-dark.md` | `07-responsive-dark.md` |
| `07-icons-imagery.md` | `99-extension-icons-imagery.md`（标记为非规范扩展） |
| 旧 `05-components/04-card.md` 等通用名 | 现 `05-components/{01-buttons,02-forms,03-tables,04-modals,05-drawers,06-toasts-alerts,07-empty-loading,08-popovers-tooltips,09-avatars-badges-tags,10-tabs-accordion,11-cards-glass,12-decorations}.md` |

**处置**：脚本统一改写到现行文件名；`B03-design/design-system/00-index.md` 文件清单段重写。

### 2.3 C02 权限目录文件改名后未同步引用

| 旧文件名 | 现文件名 |
|---------|---------|
| `02-auth-flow.md` | `02-authz-mechanism.md` |
| `03-authz-mechanism.md` | `02-authz-mechanism.md` |
| `04-data-model.md` | `03-data-model.md` |
| `05-auth-feature-guideline.md` | **不存在**（合并入 `02-authz-mechanism.md`） |

**处置**：所有正文引用统一指向现行文件；`docs/C02-permissions/99-open-questions.md` 标题误写「B02」已修正为「C02」。

### 2.4 跨目录路径深度错误

部分 `C03 / C04 / C06` 子目录文件使用 `../../` 越过两级，但实际位于 3 级深处，应使用 `../../../`（或反向：`C06-prd/<feat>/<surface>/` 同级 sibling 引用应为 `../../`，曾被脚本误升一级，已回滚）。

**处置**：`/tmp/zhiyu_fix3.py` + `/tmp/zhiyu_fix4.py` 修复 28 + 5 = **33 个文件**。

### 2.5 Auth 流程文件按 surface 拆分但引用未拆

`C01-requirements/auth/flows/` 实际包含 `app-main-flow.md` / `app-exception-flow.md` / `admin-main-flow.md` / `admin-exception-flow.md`（不再存在通用 `main-flow.md` / `exception-flow.md`）。各 surface 引用按 surface 自动重写。

**处置**：`zhiyu_fix3.py` 中按 `app/` vs `admin/` 路径上下文自动选择正确文件名。

### 2.6 索引文件指向已迁移到 surface 子目录的内容

`C03-ia/{course,discover-china}/00-index.md` 仍按"扁平目录"列出 `01-feature-catalog.md / 02-flows.md / ...`，实际这些文件已下沉到 `app/` 与 `admin/`。

**处置**：手工重写两个索引文件，改为分别给出 `app/` 与 `admin/` 双链路；`C03-ia/auth/` 目录新建缺失的根级 `00-index.md`。

### 2.7 其他逐项修复

- `C01-requirements/auth/baseline.md` 上游链：删除指向已不存在 `05-auth-feature-guideline.md` 的引用，并把 `02-auth-flow.md` 改为 `02-authz-mechanism.md`。
- `C03-ia/auth/{app,admin}/06-coverage-matrix.md` L5 链接文字与目标错位，统一为 `[C01 baseline](../../../C01-requirements/auth/baseline.md)`。
- `C03-ia/auth/app/00-index.md`：`./_input/page-direction.md` → `../_input/app-page-direction.md`；`B02-05 §2.1` 引用文字修正为 `C02-permissions/02-authz-mechanism.md §2.1`。
- `C02-permissions/03-data-model.md` 末尾 `./02-auth-flow.md` → `./02-authz-mechanism.md`。
- `C06-prd/course/app/07-business-rules.md` `../../../C01-prd-baseline/baseline.md` → `../../../C01-requirements/course/baseline.md`。

---

## 3. 修改文件总数

| 阶段 | 文件数 | 来源 |
|------|--------|------|
| Round 2.1 旧编号机械改写 | 71 | `zhiyu_fix.py` |
| Round 2.2 残留 B04 / 旧设计文件名 | 52 | `zhiyu_fix2.py` |
| Round 2.3 路径深度 + C02 改名 + 组件名 | 28 | `zhiyu_fix3.py` |
| Round 2.4 路径深度回滚 + C01 baseline 修正 | 5 | `zhiyu_fix4.py` |
| 手工逐项 | 8 | C03-ia 索引、auth 流程、新建文件等 |
| **合计** | **164** | — |

新建文件：

- `docs/C03-ia/auth/00-index.md`（feature 根索引，原缺失）
- `docs/A00-meta/consistency-audit-2026-05-16-round2.md`（本文档）

---

## 4. 验证

- `grep -rE "B04|04-status-components|05-interactions\.md|06-responsive-dark\.md" docs --include="*.md"`（去除历史 / 输入草案）→ **0 命中**。
- `grep -rE "B05|C07|C02-I|C03-N|C04-H|C05-E|B03-X" docs --include="*.md"`（去除历史 / 输入草案）→ **0 命中**（仅业务规则 `BR-C07` 保留，与阶段编号无关）。
- `python3 /tmp/zhiyu_check_links.py`：从 **176 → 78** 条断链，剩余全部归类为下文 §6「可接受遗留」。

---

## 5. 框架原则确认

经全量扫描，下列项已经与 [`prompt/A-framework/A00-{00..04}.md`](../../prompt/A-framework/) 完全对齐：

- 双周期模型（F = B01/B02/B03 一次性；C = C01..D03 每 feature 循环）
- F→C 单向依赖（C 引 F；F 不引 C）
- 跨 feature 不互相引用（每 feature 自闭环）
- C03 IA 多 surface 拆分约定（auth 已按 app/admin 拆，course/discover-china 已按 app/admin 拆 1–6 文件，07/99 跨 surface 共享）
- C04 / C05 按 surface 拆 page-id（`P-app-*` / `P-admin-*`）
- ID 命名约定（`R-<feat>-NNN` / `M-<feat>-...` / `FL-<feat>-NN` / `SM-<feat>-...`）

---

## 6. 可接受的预期遗留（78 条）

| 类别 | 计数 | 说明 / 处置依据 |
|------|------|----------------|
| **`*.scenarios.md` 缺失** | 36 | C04 页面交互约定每页应有同名 `.scenarios.md` 列出 4 态触发条件，目前 37 个 page-spec 仅链接未建文件。属于"已开 feature C04 阶段未完工"项目，不影响 PRD 冻结。建议在进入 D 阶段前补齐；本次审计**有意未自动生成**，避免占位污染 |
| **D 层正向引用** | 18 | `D01-data/` `D02-api/` `D03-validation/` 在 C03/C04 段被预引用，但 D 层目录"按需创建"（per A00-04 §四），三 feature 尚未进入 D 阶段，文件未建。框架明确允许 |
| **`A00-meta/changelog.md` 内历史指针** | 13 | 链接到 `system/`、`function/`、`grules/`（旧仓库目录）、旧 `02-auth-flow.md` / `05-auth-feature-guideline.md` 等已不存在的路径。属于历史变更记录，按"changelog 不可篡改"原则保留 |
| **`B03-design/design-system/05-components/` 引用 `system/packages/...`** | 8 | 指向待开发的 ui-kit 实现路径，与 D 层正向引用同性质 |
| **`_input/*` 草案链接** | 3 | 用户输入快照，按框架约定为不可变历史 |

合计 78 条。**不再修复**。

---

## 7. 已知"软"问题（不在本轮修复，记录待审）

下列项不属于"机械错引用"，而是**架构内容质量问题**，需 PM/owner 决定后续动作：

1. **C04 页面交互文件含 Zod schema / Supabase 调用代码**：根据 [`prompt/A-framework/A00-04 §三 6`](../../prompt/A-framework/A00-04-文档目录规划.md)，C04 仅描述「交互/布局/4 态」，字段验证应在 D01/D02。当前 37 个 C04 文件混入 D 层内容，属于"层越界"。建议在进入 D 阶段时把这些代码迁出。**本轮未自动剥离**（信息损失风险高）。
2. **M-ID 命名两种风格并存**：`course` 用 `M-course-content` 等语义化；`auth` / `discover-china` 用 `M-auth-001` / `M-discover-001` 等数字。建议统一为语义化，但属于改动量极大的非阻断项。
3. **C06-prd `_input/` 文件命名**：`auth` 用 `app-prd-context.md` / `admin-prd-context.md`（双 surface 双文件），其他 feature 用 `prd-context.md`。可在 [`prompt/A-framework/A00-04`](../../prompt/A-framework/A00-04-文档目录规划.md) 显式增补「多 surface 时按 surface 拆 _input」的约定，或反过来强制单文件 + 章节拆分。
4. **`B03-design/design-system/99-extension-icons-imagery.md`** 与正文 `05-components/12-decorations.md` 都涉及视觉装饰元素，命名重叠风险；建议合并入 `05-components/12-decorations.md` 一节，但当前已有内部交叉引用，先保留并在两文件互链。

---

## 8. 完成时间

2026-05-16（与 Round 1 同日完成；Round 2 由 GitHub Copilot 在用户「全局检查文档完美版本」请求下执行）。
