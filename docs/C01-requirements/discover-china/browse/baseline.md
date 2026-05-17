<!-- TARGET-PATH: docs/C01-requirements/discover-china/browse/baseline.md -->

# 需求与权限基线 · browse

> **阶段**：C01-RP · 需求分析师 + 权限工程师
> **模块**：`discover-china`
> **功能**：`browse`（app 端文化浏览）
> **上游依赖**：`_input/draft.md`、`../baseline.md`（模块级参考）、`B01-architecture/08-surfaces.md`
> **冻结状态**：已冻结 · 2026-05-16
> **下游影响**：C02-ia-interaction/discover-china/browse/

---

## 0. 摘要

- 给谁：app 端访客 / 已登录学习者（U1）。
- 做什么：12 类目卡片入口（01-03 免登录）、类目下文章列表、逐句双语详情阅读 + 句子级 TTS 播放 + 全文朗读 + 阅读进度记忆。
- 最大价值：让东南亚学员在未注册前就能"看见 + 听见"中国文化，降低首次体验门槛。
- 最大风险：TTS 缓存未命中导致首次播放延迟；访客进度本地兜底无法跨设备同步。

---

## 2. 需求清单

| R-ID | 标题 | 涉及角色 | 关联页面 | 验收要点 |
|------|------|---------|---------|---------|
| R-discover-china-001 | 12 类目卡片浏览 | ROLE-USER / 访客 | P-app-discover-china-001 | 立即看到 12 张卡片；名称 + 简介按当前语言显示；01-03 直接进，04-12 未登录拦截 |
| R-discover-china-002 | 类目下已发布文章列表 | ROLE-USER / 访客 | P-app-discover-china-002 | 仅显示已发布文章；空时显示"暂无文章" |
| R-discover-china-003 | 文章逐句详情阅读 | ROLE-USER / 访客 | P-app-discover-china-003 | 首句卡片显示拼音 / 中文 / 当前语言三层；中文用户仅拼音 + 中文 |
| R-discover-china-004 | 单句中文 TTS 播放 | ROLE-USER / 访客 | P-app-discover-china-003 | 命中缓存即时播放；未命中先合成后缓存 |
| R-discover-china-005 | 全文朗读按句循环 | ROLE-USER / 访客 | P-app-discover-china-003 | 从当前句开始按顺序逐句播放；可暂停 / 跳下一句 |
| R-discover-china-006 | 阅读进度记忆 | ROLE-USER | P-app-discover-china-003 | 登录用户跨设备同步；访客本地兜底 |
| R-discover-china-007 | 应用端搜索 | ROLE-USER / 访客 | P-app-discover-china-004 | 命中"中文 + 当前语言"两列，模糊匹配 |

---

## 4. 业务规则（功能范围）

| 规则 ID | 描述 | 来源 R-ID | 边界值 |
|--------|------|---------|--------|
| BR-1 | 12 类目数量固定，类目永不可删 | R-discover-china-001 / 018 | — |
| BR-2 | 01-03 类目访客可直接进；04-12 必须登录 | R-discover-china-001 / 020 | — |
| BR-6 | TTS 缓存键随句子序号变化失效；重排后旧键回收 | R-discover-china-004 / 012 | — |
| BR-7 | 阅读进度：登录用户跨设备同步；访客本地兜底 | R-discover-china-006 | — |
| BR-11 | TTS 失败不阻塞 UI；后台自动重试并提示 | R-discover-china-004 | — |

> 角色定义、权限矩阵、NFR 见模块基线 `../baseline.md §5-§8`。

---

## 99. 待确认问题

（无）
