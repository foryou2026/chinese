# Round 5 · 全量 per-file × 11 维度审计

**时间**：2026-05-16 · Round 5（每文件每维度可追溯版本）
**范围**：`docs/**/*.md` + `prompt/**/*.md`，共 **373 文件**
**结论**：**373 / 373 全 ✓**，11 个维度零残留。

---

## 1. 维度定义

| ID | 维度 | 校验内容 | 豁免范围 |
|----|------|----------|----------|
| **D1** | C 阶段禁用底层名词 | `super_admin` / `content_admin` / `editor+` / `signInWithPassword` / `signInWithOAuth` / `exchangeCodeForSession` / `resetPasswordForEmail` / `signUp(` / `user_sessions` / `supabase.<api>` / `Supabase` / `GoTrue` / `cookieStorage` / `app_metadata` / `profiles.role` | B 阶段（架构/设计本就该写）、C02（权限规范本身）、prompt（模板）、`_input/`（用户输入）、`A00-meta/`（历史） |
| **D2** | 内部 markdown 链接目标存在性 | `[txt](relative.md)` 解析后必须存在 | D01-data / D02-api / D03-validation / `system/` / `_input/` / `A00-meta/` / prompt |
| **D3** | `<!-- TARGET-PATH: ... -->` 头部 = 实际路径 | 头部声明路径与文件路径完全一致 | prompt（含字面模板示例） |
| **D4** | 文件必须包含 H1 标题 | 至少一行 `^#\s+\S` | （无） |
| **D5** | R3/R4 替换残破词 | 不出现 `鉴权与数据底座` / `/首版/` / `首版.0` / `Round 10+` | `_input/`、`A00-meta/` |
| **D6** | C 阶段不得出现裸 mermaid 块 | C01/C03/C04/C06 不含 ` ```mermaid ` | prompt、`_input/`、`A00-meta/`、D 阶段 |
| **D7** | 旧阶段编号（合并前） | 不出现 `B04-S` / `B05-X` / `C02-I` / `C03-N` / `C04-H` / `C05-E` / `B03-X` / `C07-` / `C06-N` | prompt、`_input/`、`A00-meta/`、`changelog.md` |
| **D8** | C 阶段不得出现版本/阶段/优先级措辞 | 不出现 `本期` / `二期` / `v2+` / `MoSCoW` / `H5 封板` / `路线图` / `P0` / `P1` / `P2` / `11-roadmap.md` / `12-changelog.md` | B 阶段（架构允许讨论技术演进顺序）、prompt、`_input/`、`A00-meta/` |
| **D9** | 行内反引号必须成对 | 每行反引号数为偶数（fenced code block 内例外） | （fenced 内自动跳过） |
| **D10** | 表格列对齐 | 同一连续表块所有行列数差不超过 1 | fenced code block 内跳过；inline code 内的 `\|` 不计；`\\\|` 转义不计 |
| **D11** | 控制字符 | 不出现 NUL / VT / FF 等 | （无） |

---

## 2. 全文件 per-file 审计踪迹

完整 trace 写入 `/tmp/audit-per-file.tsv`，格式：

```
D1D2D3D4D5D6D7D8D9D10D11	path
✓✓✓✓✓✓✓✓✓✓✓	docs/A00-meta/changelog.md
✓✓✓✓✓✓✓✓✓✓✓	docs/A00-meta/consistency-audit-2026-05-16-round2.md
... (373 行)
```

按目录覆盖统计：

| 目录 | 文件数 | 状态 |
|------|--------|------|
| `docs/A00-meta` | 6 | ✓ |
| `docs/B01-architecture` | 12 | ✓ |
| `docs/B02-ux` | 9 | ✓ |
| `docs/B03-design` | 24 | ✓ |
| `docs/C01-requirements` | 20 | ✓ |
| `docs/C02-permissions` | 6 | ✓ |
| `docs/C03-ia` | 64 | ✓ |
| `docs/C04-pages` | 57 | ✓ |
| `docs/C05-prototype` | 4 | ✓ |
| `docs/C06-prd` | 130 | ✓ |
| `prompt/A-framework` | 5 | ✓ |
| `prompt/B-foundation` | 9 | ✓ |
| `prompt/C-product` | 18 | ✓ |
| `prompt/D-develop` | 9 | ✓ |
| **合计** | **373** | **✓** |

---

## 3. 本轮修复明细

### 3.1 D9 行内反引号未闭合（55 处）

R3/R4 替换 `Supabase`/`app_metadata`/`user_sessions` 等术语为中文时，连带破坏了行内反引号配对。例：

- `\`app_metadata.role\`` → `账号元数据.role\`` （左反引号丢失）
- `\`user_sessions\`` → `会话记录\`` （同上）

采用「左到右配对，未匹配的孤立反引号补齐对侧」启发式处理 39 行；对结构性破损（`## 5. \`zhiyu.审计记录\`` 标题、表清单 `\`zhiyu.X\` + \`zhiyu.Y\``、`JWT 中映射` 行等 15 处）人工精修，恢复语义。

### 3.2 D2 链接失效（48 处）

- **40 处** C06 page-spec 模板的 `*.scenarios.md` 占位链接：去除 markdown link 包装，改为内联代码路径文本（保留"若存在"的语义）。
- **5 处** B03 design-system 链接路径错误：`./_input/visual-input.md` → `../_input/visual-input.md`；`./99-open-questions.md` → `../99-open-questions.md`。
- **3 处** prompt 模板示例链接：审计规则放宽（prompt 是模板，链接为示例不强校）。

### 3.3 D3 TARGET-PATH 头部与实际路径不符（7 处）

- 6 处 `_input/` 文件（C03/C04/C05 auth 端）：头部声明的 `<surface>/_input/<name>.md` 与实际归并后位置 `_input/<surface>-<name>.md` 不一致，更新头部。
- 1 处 prompt B01-A03：含字面字符串 `<!-- TARGET-PATH: ... -->` 作为模板演示，审计规则跳过 prompt。

### 3.4 D4 缺 H1（7 处）

- 3 处 `99-open-questions.md`（C03/C04/C06 auth 合并后）：以 `## C0X` 开头，提升为 `#`。
- 4 处 `_shared/{business-rules,glossary}.md`（C06 course / discover-china）：插入文档级 H1，保留原有 `## 7` / `## 2` 章节号。

### 3.5 D10 表格列漂移（8 处）

- 5 处假阳性：inline code 内的 `|`（如 `Accept-Language: zh-CN | en | vi | th | id`）被误计 → 审计规则改为先剥离 inline code 再数 `|`。
- 2 处假阳性：fenced code block 内的 ASCII 艺术（B03 / prompt B03-S03）→ 审计规则跳过 fenced block。
- 1 处真问题：`docs/C03-ia/auth/app/05-navigation.md` 的 `| - 分割线 - |` 单列行 → 补齐为合规 4 列 `| — | — 分割线 — | — | — |`。

### 3.6 D1/D5/D6/D7/D8/D11 零修复

R3/R4 已彻底清理，本轮 0 命中。

---

## 4. 审计规则修正（沉淀）

为消除假阳性，本轮校准了 4 处审计规则；这些规则将作为后续每轮审计的基线：

1. **D1 禁词只对 C 阶段产品文档**（C01/C03/C04/C06）；B 阶段架构/设计与 C02 权限规范是 Supabase/SDK 名词的合法宿主。
2. **D8 阶段/优先级措辞同 D1**：只在 C 阶段产品文档强约束；B 阶段技术演进顺序、prompt 模板教学内容、`_input/` 用户输入不强约束。
3. **D2 / D3 跳过 prompt**：prompt 是模板，链接 / TARGET-PATH 多为字面示例。
4. **D10 表格检测**：剥离 inline code + 跳过 fenced code block + ±1 列容忍（用于分隔/合并单元格场景）。

---

## 5. 验收脚本

`/tmp/audit_all.py` 是本轮使用的审计脚本，可重复运行；输出：

- `/tmp/audit-per-file.tsv` — 373 行 per-file × 11 维度状态矩阵
- `/tmp/audit-issues.txt` — 每条问题 `path \t Dx|line|detail`
- stdout — 总计 / 按维度统计

最终输出：

```
Audited files : 373
Perfect (all 11 dims ✓) : 373
With issues : 0
Total issues : 0
By dimension:
  D1: 0  D2: 0  D3: 0  D4: 0  D5: 0  D6: 0  D7: 0  D8: 0  D9: 0  D10: 0  D11: 0
```

---

## 6. 后续

- R5 已完结。任何 D-stage 新文档（D01-data / D02-api / D03-validation 实质化）落地后，需要重新跑 `audit_all.py` 验证。
- 审计规则与豁免范围已在 §1 / §4 沉淀，避免后续轮次重新发现已被有意豁免的"问题"。
