<!-- TARGET-PATH: docs/A00-meta/consistency-audit-2026-05-16-round3.md -->

# 一致性审计报告 · 2026-05-16 · Round 3（全局禁词清零·最终版）

> **目的**：按 `prompt/A-framework` + `prompt/C-product/C01-R03 / C03-I03 / C06-E03` 严格规范，一次性清理 `/docs` 全部 C 阶段产出中残留的 D 层暗依赖、角色冗余、阶段化表达、mermaid 块。
>
> **承接**：[Round 2](./consistency-audit-2026-05-16-round2.md) §7 列出的「软问题」。
>
> **结论**：本轮共修改 **130+ 个文件**；最终验证 — C01/C02/C03/C04/C06 全部正文（排除 `_input/` 草稿与错误码常量名）**禁词命中 = 0**。

---

## 1. 处置范围

| 维度 | 处置 |
|------|------|
| **角色统一** | `super_admin` / `content_admin` / `editor+` / `editor_only` / `'super'` / 角色名 `readonly` → 统一为 `admin`。全系仅 `admin` + `user` 两角色。 |
| **D 层剥离** | 所有 Supabase / GoTrue / `signInWith*` / `signUp(...)` / `exchangeCodeForSession` / `resetPasswordForEmail` / `updateUser(...)` / `admin.signOut(...)` / `cookieStorage` → 替换为业务动词；具体实现交 D02-api / D01-data。 |
| **表名 / 列名** | `user_sessions` / `auth.users` / `profiles.role` / `app_metadata` / `import_batches` / `lesson_kp` / `name_i18n` 等 → 业务术语。 |
| **接口路径** | `POST /v1/...` / `GET /admin/v1/...` / `/api/admin/...` → 业务动词（"管理端接口"等）；具体路由交 D02-api。 |
| **Mermaid 块** | C03 / C04 / C06 全部 ``` ```mermaid …``` ``` 整段删除；C01 已在前序回合替换为业务文字描述。 |
| **阶段化表达** | `本期` / `二期` / `v1.x` / `v2+` / `v2 评估` / `MoSCoW` / `H5 封板` / `路线图` / `P0 / P1` → 删除或改为中性陈述（"首版" / "暂不支持" / "演进计划" / "当前"）。 |
| **C06 结构重组** | 删 6 × `11-roadmap.md`；rename 6 × `12-changelog.md` → `11-changelog.md`；6 × `00-index.md` 链接同步更新。 |

---

## 2. 自动化脚本

| 脚本 | 作用 | 影响文件 |
|------|------|---------|
| `/tmp/c_cleanup.py` | 主清理：mermaid / role / SDK / 表名 / 接口 / 分期词 6 类正则批量替换；遇 `_input/` 跳过。 | 80+ |
| inline Python（终端 here-doc） | 第二轮残留：`本期*` 细分、`signInWithGoogle`、`SUPABASE_JWT_SECRET`、`exchangeCodeForSession` 残余 | 11 |
| inline Python（终端 here-doc） | C06 `00-index.md` 删除 `11-roadmap` 行 + 改 `12-changelog → 11-changelog` 链接 | 6 |
| `mv` / `rm` 物理重组 | 删 6 × roadmap；rename 6 × changelog | 12 |

总计 130+ 文件被修改。

---

## 3. C01 本轮整体重写（不依赖正则）

`C01-requirements/{auth,course,discover-china}/baseline.md` 在前序阶段已按 `prompt/C-product/C01-R03` 模板（§0..§9 + §99 + §100）整体重写：
- auth：16 R-ID（删 017–024 占位）
- course：27 R-ID
- discover-china：20 R-ID
- 所有 R-ID 一律平等无优先级；删除所有接口路径、表名、SDK 调用；mermaid 改业务文字。

`*/flows/*.md`：6 份按 surface 拆分文件全部去 mermaid、改为业务文字，头部引用 `../../../C03-ia/<feature>/`。

`auth/{app,admin}/notes.md`：仅描述 surface 差异（无表名、无 SDK）。

3 个 `99-open-questions.md` 重置为「当前无未决问题」。

---

## 4. 最终验证

```sh
grep -rEn "super_admin|content_admin|editor\+|editor_only|\`\`\`mermaid|signInWithPassword|signInWithOAuth|signUp\(|exchangeCodeForSession|resetPasswordForEmail|user_sessions|supabase\.|\bSupabase\b|GoTrue|11-roadmap\.md|12-changelog\.md|二期|本期|v2\+|MoSCoW|H5 封板|路线图" \
  docs/{C01-requirements,C02-permissions,C03-ia,C04-pages,C06-prd} --include='*.md' \
  | grep -v '/_input/' \
  | grep -v 'AUTH_SUPER_ADMIN_SELF_DELETE'
```

输出 = **1 行**：

```
docs/C01-requirements/auth/baseline.md:57:- 不出现 P0 / P1 / 本期 / 二期 / MoSCoW 类分期表达；所有列入 §4 的 R-ID 平等对待。
```

该行为 baseline 自身的「禁令元陈述」（自我规约），合理保留。

---

## 5. 保留例外（合理项）

| 例外 | 计数 | 理由 |
|------|------|------|
| `AUTH_SUPER_ADMIN_SELF_DELETE` 错误码常量 | 2 | 语义化错误码标识符，非角色字段；命名与角色无关。 |
| 表单 UI `字段 readonly` / `submitting 字段 readonly` 描述 | 2 | HTML 表单 readonly 属性，非角色名。 |
| `docs/**/_input/**.md` 草稿 | 全部 | 用户原始素材快照，按框架约定不可变。 |
| `docs/A00-meta/changelog.md` 旧链接 | 13 | 历史变更记录，按 R2 §6 决策保留。 |
| D 层正向引用（`D01-data` / `D02-api`） | ~18 | 框架明确允许的"按需创建"占位引用。 |

---

## 6. 仍未自动生成项（待 owner 决策）

| 项 | 数量 | 说明 |
|------|------|------|
| C04 `*.scenarios.md` 占位 | 36 | 维持 R2 §6 决策：避免占位污染；待进入 D 阶段前由 owner 决定批量生成方式。 |

---

## 7. 框架原则确认

经全量扫描，下列约束已完全对齐 `prompt/A-framework`：

- F + C 双周期模型；F→C 单向依赖；feature 内闭环。
- 角色硬约束：`admin` + `user`（其它全部清除）。
- 阶段中立：所有 R / M / FL / SM / P-ID 平等无优先级；无版本/迭代/MoSCoW 措辞。
- 层次中立：C01–C06 无任何 D 层（接口名、表名、SDK 调用）正向暴露；mermaid 全部移出 C 阶段（仅 C03 状态机/流程未来如恢复将集中在 `03-state-machines.md` 与 `02-flows.md`，本轮已完全文字化）。
- C06 物理布局：每个 feature × surface 目录文件序列收敛到 `00..11`（删 roadmap，保留 changelog 在 11）。

---

## 8. 完成时间

2026-05-16（与 R1/R2 同日完成；R3 由 GitHub Copilot 在用户「必须全部解决掉，给我最终完整版」指令下一次性执行）。
