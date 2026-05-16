<!-- TARGET-PATH: docs/C05-prd/discover-china/PRD.md -->

# PRD · discover-china · v1.0

> **阶段**:C05-E · **feature**:`discover-china` · **冻结状态**:已冻结 · 2026-05-16
> **上游**:[C01](../../C01-requirements/discover-china/baseline.md) · [C02](../../C02-ia/discover-china/00-index.md) · [C03](../../C03-pages/discover-china/) · [C04](../../C04-prototype/discover-china/)
> **下游**:D01 数据模型 / D02 接口 / D03 校验

---

## 1. 产品概述

"发现中国"是知语应用首批上线的内容浏览型一级 Tab,以 12 个固定中国文化类目为入口,为东南亚学习者提供"拼音 + 中文 + 本地语言"三层对照的文章 + 逐句 TTS 体验。管理端由 super_admin 独立维护,内容必须 5 语并齐发布。

## 2. 术语表

| 术语 | 说明 |
|------|------|
| 类目(Category)| 12 个固定文化主题,编码 `01..12` |
| 文章(Article)| 类目下的文本,12 位编码 `{类目 2}{自增 10}` |
| 句子(Sentence)| 文章内可单独编辑 / 朗读的最小单元,带 4 位 seq_no |
| 5 语 | 简体中文 / 英 / 越南 / 泰 / 印尼 |
| TTS | 中文文本转语音,全局缓存,键 `{article_code}-{seq_no}` |
| super_admin | 管理端唯一角色 |

## 3. 角色 / 用户故事

- **访客 / 应用用户**:浏览类目 → 选文章 → 逐句阅读 + 朗读 + 记忆进度;
- **super_admin**:管理类目下文章 / 句子 / 多语版本 + 发布状态 + 全局搜索。

详见 [`C01/baseline.md §3`](../../C01-requirements/discover-china/baseline.md)。

## 4. 模块清单

承自 [`C02/01-feature-catalog.md`](../../C02-ia/discover-china/01-feature-catalog.md):**5 个 M-ID**。

## 5. 用户旅程

主旅程 6 + 异常旅程 7,详 [`C01/flows/`](../../C01-requirements/discover-china/flows/) 与 [`C02/02-flows.md`](../../C02-ia/discover-china/02-flows.md)。

## 6. 页面清单与原型

| page-id | 路由 | 规格 | 原型 |
|---------|------|------|------|
| P-app-discover-china-001 | `/china` | [规格](../../C03-pages/discover-china/P-app-discover-china-001.md) | [原型](../../C04-prototype/discover-china/pages/P-app-discover-china-001.html) |
| P-app-discover-china-002 | `/china/categories/:code` | [规格](../../C03-pages/discover-china/P-app-discover-china-002.md) | [原型](../../C04-prototype/discover-china/pages/P-app-discover-china-002.html) |
| P-app-discover-china-003 | `/china/articles/:code` | [规格](../../C03-pages/discover-china/P-app-discover-china-003.md) | [原型](../../C04-prototype/discover-china/pages/P-app-discover-china-003.html) |
| P-admin-discover-china-001 | `/admin/china` | [规格](../../C03-pages/discover-china/P-admin-discover-china-001.md) | [原型](../../C04-prototype/discover-china/pages/P-admin-discover-china-001.html) |
| P-admin-discover-china-002 | `/admin/china/categories/:code` | [规格](../../C03-pages/discover-china/P-admin-discover-china-002.md) | [原型](../../C04-prototype/discover-china/pages/P-admin-discover-china-002.html) |
| P-admin-discover-china-003 | `/admin/china/articles/:id` | [规格](../../C03-pages/discover-china/P-admin-discover-china-003.md) | [原型](../../C04-prototype/discover-china/pages/P-admin-discover-china-003.html) |
| P-admin-discover-china-004 | `/admin/china/search` | [规格](../../C03-pages/discover-china/P-admin-discover-china-004.md) | [原型](../../C04-prototype/discover-china/pages/P-admin-discover-china-004.html) |

弹窗 D-1..D-8 详 [`C02/07-error-pages.md §6`](../../C02-ia/discover-china/07-error-pages.md)。

## 7. 业务规则(全量,标 BR-ID)

| BR-ID | 规则 | 关联 R |
|-------|------|--------|
| BR-01 | 12 类目编码固定 `01..12`,UI 不可新建 / 删除 / 重命名 | R-008, R-018 |
| BR-02 | 类目 04-12 卡片点击 → 未登录弹 D-8;01-03 始终公开 | R-001, R-020 |
| BR-03 | 文章发布需 5 语标题 + 5 语全部句子内容均非空;否则发布拒绝 | R-013 |
| BR-04 | 下架文章自动清空所有用户该文章的阅读进度 | R-013 |
| BR-05 | 句子 seq_no 4 位,删除/重排自动重写;TTS 缓存键随之失效 | R-012 |
| BR-06 | 文章 12 位编码格式 `{cat 2}{seq 10}`,seq 由后端类目内自增,不可手编 | R-009 |
| BR-07 | TTS 缓存键 `{article_code}-{sentence_seq_no}`,全局共享 | R-004 |
| BR-08 | 多管理员并发编辑采用后写覆盖,前端弹被覆盖 Toast | R-017 |
| BR-09 | 应用端进度记录:登录用户存远端 `user_id × article_id`,访客存 `localStorage` | R-006 |
| BR-10 | 句子内容 / 类目 / 文章软删 30 天,过期物理清理由后台 cron | R-019 |
| BR-11 | 应用端搜索范围 = 本类目;管理端搜索可切 `全局 / 本类目 / 本文章` | R-007, R-016 |
| BR-12 | 中文用户应用端隐藏本地语行,仅显示拼音 + 中文 | R-003 |

## 8. 角色权限

| 操作 | 访客 | 应用用户 | super_admin |
|------|:--:|:--:|:--:|
| 浏览 01-03 类目 | ✓ | ✓ | ✓ |
| 浏览 04-12 类目 | × | ✓ | ✓ |
| 阅读 / TTS | ✓(01-03) / ✓(04-12 登录后) | ✓ | ✓ |
| 进度同步(远端) | × | ✓ | ✓ |
| 进入 `/admin/china*` | × | × | ✓ |
| 文章 / 句子 CRUD | × | × | ✓ |
| 全局搜索 | × | × | ✓ |

## 9. 设计 / 原型摘要

- 沿用 [`B04-design`](../../B04-design/) 玻璃拟态 + 中国红主色;
- 12 类目卡片 + 三层对照阅读 + 中央 TTS 播放器为 UI 核心;
- 管理端文章编辑器 sticky 顶栏 + 5 语 Tab + 句子卡片列表;
- 详见 [C04 原型 index](../../C04-prototype/discover-china/index.html)。

## 10. 已知问题 / 风险

- TTS 提供方 SLA 未定,影响 R-004 P95 体验;短期采用首次失败后台 retry 兜底;
- 12 类目封面图素材到位前用占位渐变。

## 11. 路线图

- v1.0(本):核心 CRUD + 5 语 + 阅读 + TTS + 进度;
- v1.1:句子级翻译比对反馈 / 用户收藏文章;
- v1.2:文章历史版本(undo);
- v2.0:开放部分 PGC 投稿 + 审核流水线。

## 12. Changelog

| 版本 | 日期 | 备注 |
|------|------|------|
| v1.0 | 2026-05-16 | 反向回写期产出首版,冻结 |

## 13. 待确认问题

详 [`99-open-questions.md`](./99-open-questions.md) — 已清空。
