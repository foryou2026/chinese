<!-- TARGET-PATH: docs/C02-ia-interaction/discover-china/content/00-index.md -->

# IA 与交互规范 · content

> **阶段**：C02-IN · 信息架构师 + 交互设计师
> **模块**：`discover-china`
> **功能**：`content`
> **上游依赖**：`C01-requirements/discover-china/content/baseline.md`
> **冻结状态**：已冻结 · 2026-05-16

---

## 功能范围

admin 端**文章与句子编辑发布**：文章 CRUD（标题 / 正文 / 分类 / 封面 / 5 语）、句子切分与标注、TTS 生成 / 重新生成 / 失败重试、文章发布 / 撤回。

---

## 拥有的 ID

| 类别 | ID 清单 |
|------|---------|
| 功能模块 M-ID | `M-discover-content`、`M-discover-tts-admin` |
| 页面 P-ID | P-admin-discover-china-002, P-admin-discover-china-003 |
| 覆盖 R-ID | R-discover-china-009~015, R-discover-china-017, R-discover-china-019, R-discover-china-020 |

---

## 文件一览

| 文件 | 内容 |
|------|------|
| [04-pages.md](./04-pages.md) | 功能专属页面清单（P-admin-discover-china-002~003）|

> 流程图、状态机、导航结构、覆盖矩阵、错误页详见模块级文件 `../`。
