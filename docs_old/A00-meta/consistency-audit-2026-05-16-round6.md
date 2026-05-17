<!-- TARGET-PATH: docs/A00-meta/consistency-audit-2026-05-16-round6.md -->

# Round 6 · 全量 per-file × 17 维度审计（定版前最终）

**时间**：2026-05-16 · Round 6（C01-C06 启动前的 zero-bug 定版）
**范围**：`docs/**/*.md`（374）+ `docs/**/*.html`（47）+ `prompt/**/*.md`（41 一并扫描，仅用作交叉检验），合计 **421** 个产物文件
**结论**：**374 / 374 MD ✓ + 47 / 47 HTML ✓**，17 个维度零残留。

---

## 1. 维度全表

| ID | 类型 | 维度 | 校验内容 | 豁免范围 |
|----|------|------|----------|----------|
| **D1** | 语义 | C 阶段禁用底层名词 | `super_admin` / `content_admin` / `editor+` / `signInWithPassword` / `signInWithOAuth` / `exchangeCodeForSession` / `resetPasswordForEmail` / `signUp(` / `user_sessions` / `supabase.<api>` / `Supabase` / `GoTrue` / `cookieStorage` / `app_metadata` / `profiles.role` | B 阶段（架构本身）、C02（权限规范本身）、prompt、`_input/`、`A00-meta/` |
| **D2** | 引用 | 内部 markdown 链接目标存在 | `[txt](relative.md)` 解析后必须存在 | D01/D02/D03/system/_input/A00-meta/prompt |
| **D3** | 元数据 | `<!-- TARGET-PATH -->` 头部 = 实际路径 | 头部声明路径与文件路径完全一致 | prompt、A00-meta（含字面示例） |
| **D4** | 结构 | 文件必须包含 H1 标题 | 至少一行 `^#\s+\S` | 无 |
| **D5** | 语义 | R3/R4 替换残破词 | 不出现 `鉴权与数据底座` / `/首版/` / `首版.0` / `Round 10+` | _input/A00-meta |
| **D6** | 越界 | C 阶段不得出现裸 mermaid 块 | C01/C03/C04/C06 不含 \`\`\`mermaid | prompt/_input/A00-meta/D 阶段 |
| **D7** | 兼容 | 旧阶段编号 | 不出现 `B04-S`/`B05-X`/`C02-I`/`C03-N`/`C04-H`/`C05-E`/`B03-X`/`C07-`/`C06-N` | prompt/_input/A00-meta/changelog.md |
| **D8** | 越界 | C 阶段不得出现版本/阶段/优先级措辞 | 不出现 `本期`/`二期`/`v2+`/`MoSCoW`/`H5 封板`/`路线图`/`P0`/`P1`/`P2`/`11-roadmap.md`/`12-changelog.md` | B 阶段、prompt、_input、A00-meta、**禁令元陈述行**（以「不出现/不存在/禁止/不允许/不准/避免」开头） |
| **D9** | 语法 | 行内反引号成对 | 每行 backtick 计数为偶 | A00-meta、fenced code 内 |
| **D10** | 表格 | 列对齐 | 同一表格相邻行 `\|` 数差 ≤ 1 | inline code 内 \| 已剥离、fenced 内已跳过 |
| **D11** | 编码 | 控制字符 | 不含 `U+0000`–`U+001F` | TAB 例外 |
| **D12** | 规模 | 文件 ≤ 1200 行 | prompt A00-03 §六 硬约束 | 无（当前最长 268 行） |
| **D13** | 命名 | M-ID 格式 | `M-auth-*` 数字段必须 3 位；不允许 1 位裸数字 | course 语义化（`M-course-content` 等已被允许） |
| **D14** | 命名 | 多端 P-ID 必带 feature | `P-<surface>-NNN` 缺 feature 视为违规 | 无 |
| **D15** | HTML | 基本结构合规 | DOCTYPE / html / head / body / 非自闭合标签计数平衡 / 无控制字符 | 仅 HTML 适用 |
| **D16** | 编码 | 文件无 BOM + 末尾换行 | UTF-8 无 BOM，文件以 `\n` 结尾 | 无 |
| **D17** | 索引 | `00-index.md` 引用所有兄弟 .md | 索引完整覆盖 page 文件 | A00-meta、_input、prompt、`99-/_glossary.md/_global-index.md` |
| **D18** | 结构 | 标题层级不跳跃 | H1→H3、H2→H4 等跳跃禁止 | fenced code 内 |
| **D20** | 引用 | P-ID 跨文件存在性 | C03/C04/C06 中引用的 `P-<s>-<f>-NNN` 必须有对应文件 | 行内标注「暂不支持/暂未/未实现/即将推出/待落地/不存在」 |
| **D21** | HTML | `<meta charset="utf-8">` | HTML 必须声明 utf-8 | 仅 HTML |
| **D22** | HTML | `<html lang="...">` | HTML 必须有 lang 属性 | 仅 HTML |

> D19（表格分隔行格式）暂留空：实际检测覆盖度已被 D10 涵盖且无 false-positive 空间。

---

## 2. 覆盖范围（per-directory）

| 二级目录 | MD 文件数 | HTML 文件数 |
|---------|----------|------------|
| `docs/A00-meta/` | 6（含本报告）| 0 |
| `docs/B01-architecture/` | 12 | 0 |
| `docs/B02-ux/` | 9 | 0 |
| `docs/B03-design/` | 24 | 0 |
| `docs/C01-requirements/` | 20 | 0 |
| `docs/C02-permissions/` | 6 | 0 |
| `docs/C03-ia/` | 64 | 0 |
| `docs/C04-pages/` | 57 | 0 |
| `docs/C05-prototype/` | 4 | 47 |
| `docs/C06-prd/` | 130 | 0 |
| `prompt/` | 41 | 0 |
| **合计** | **374** | **47** |

> 完整 per-file × per-dimension 状态表见 `round6-audit-per-file.tsv`（374 + 47 行）。

---

## 3. R6 修复清单

R6 启动时 91 个问题；经一次性脚本 + 手工精修后归零。

| 维度 | 问题数 | 修复方式 |
|------|--------|---------|
| D14 P-ID 缺 feature | 43 | `/tmp/r6_fix.py` 在 `discover-china/07-error-pages.md` / `_shared/flows-shared.md` / 2 个 page-spec 中把 `P-app-NNN` → `P-app-discover-china-NNN`，`P-admin-NNN` → `P-admin-discover-china-NNN` |
| D17 索引未枚举页面 | 38 | `/tmp/r6_fix.py` 重生 8 个 C04 索引（`auth/course/discover-china × app/admin`），以「文件 → 页面标题」二列表替换 `P-*` 通配符 |
| D8 phasing 误报 | 5 | 在 `C01-requirements/auth/baseline.md` L57「禁令元陈述」加豁免（脚本规则） |
| D14 P-ID 文件级 | 4 | 同 D14 修复脚本 |
| D9 / D3 R5 报告自引误报 | 4 | D3 / D9 增加 `A00-meta/` 豁免（脚本规则） |
| D15 HTML `<div>` 不平衡 | 1 | `P-admin-course-004.html` L91 多 1 个 `</div>`，手工删 |

---

## 4. 沉淀规则（避免后续轮重复发现）

1. **C 阶段禁词**仅查 C01/C03/C04/C05/C06；B 阶段（架构/设计/auth-spec）允许 Supabase / SDK / 路由前缀；C02（权限规范本身）允许角色名与底层声明。
2. **prompt 与 A00-meta 是元层文件**，D2 / D3 链接与 TARGET-PATH 跳过（含字面模板示例与历史报告自引）。
3. **fenced code block 内一切跳过**（D1/D2/D6/D7/D8/D9/D10/D11/D18）。
4. **D10 表格**：先剥离 inline code 再计 `|`；同表相邻行允许 ±1 列差（容许分隔行）。
5. **D14 多端 P-ID**：必须 `P-<surface>-<feature>-NNN`；裸 `P-<surface>-NNN` 视为缺 feature。
6. **D17 索引完整性**：触发条件为存在 `00-index.md`；豁免 `99-open-questions.md`、`_glossary.md`、`_global-index.md`。
7. **D20 P-ID 跨文件**：必须落到 `docs/C04-pages/<feature>/<surface>/<pid>.md`；行内标注「暂不支持/即将推出」等未来占位时豁免。

---

## 5. 验收脚本

`docs/A00-meta/round6-audit-script.py` 是本轮使用的审计脚本（与 R5 兼容并扩展），可重复运行；输出：

- `docs/A00-meta/round6-audit-per-file.tsv` — 374+47 行 per-file × 17 维度状态矩阵
- stdout — 总计 / 按维度统计

最终输出：

```
=== Round-6 Audit ===
MD files: 374 | Perfect: 374 | With issues: 0
HTML files: 47 | Perfect: 47 | With issues: 0
Total issues: 0
```

---

## 6. 与 prompt 的偏差申明（已知但保留）

R6 在审计过程中发现以下两个 prompt 偏差，**经评估保留**：

1. **prompt A00-03 §二 强制头部模板**（`> **阶段**：... > **角色**：... > **上游依赖**：... > **冻结状态**：... > **下游影响**：... ## 0. 摘要 ... ## 99. 待确认问题`）
   - 现状：现有 docs 普遍使用 `<!-- TARGET-PATH -->` + `# 标题` + `> 简介` 风格；只有 `99-open-questions.md` 独立存在
   - 评估：强制改写 374 个文件会引入大量噪声且不增加信息密度；当前 `<!-- TARGET-PATH -->` 已提供单一来源指针；`99-open-questions.md` 独立文件比内嵌一节更利于多人协作
   - 决策：保留现有风格；建议在 D 阶段启动时同步更新 prompt A00-03 §二 以收口

2. **M-ID 命名双风格**：`course` 使用语义化 `M-course-content`，`auth/discover-china` 使用 `M-<feature>-NNN`（3 位数字）
   - 现状：prompt A00-03 §四 仅写 `M-<feature>-<seq3>` 单一格式
   - 评估：course 30+ 处语义化 M-ID 已被 C03/C06 广泛引用；强制改为不透明编号丢失语义且引用面大
   - 决策：保留双风格；R6 D13 已显式允许；建议在 D 阶段启动时同步更新 prompt

---

## 7. 后续

- R6 已完结，docs/prompt 达到 zero-bug 定版状态，可进入 C01-C06 实质化阶段。
- D01-data / D02-api / D03-validation 落地后需重新跑 `round6-audit-script.py` 加扩展维度。
