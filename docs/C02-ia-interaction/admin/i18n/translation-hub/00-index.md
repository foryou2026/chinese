# 信息架构与交互规范 — 索引

> **阶段**：C02
> **系统**：admin
> **模块**：i18n
> **功能**：translation-hub
> **需求来源**：docs/C01-requirements/admin/i18n/translation-hub/baseline.md

## 文件清单

| 文件 | 内容 |
|------|------|
| 01-feature-catalog.md | 功能模块清单 |
| 02-flows.md | 业务流程图 |
| 03-state-machines.md | 状态机 |
| 04-page-supplement.md | 页面补充规范 |
| 05-coverage-matrix.md | R-ID 覆盖矩阵 |
| 06-error-pages.md | 系统兜底页 |
| 99-open-questions.md | 待确认问题 |

## 增量融合 · 第 2 轮 · 功能「translation-hub」

### 本轮新增
| 类型 | ID | 说明 |
|------|-----|------|
| 模块 | M-i18n-001 | 国际化翻译中心模块 |
| 页面 | P-admin-i18n-001 ~ 009 | 翻译总览/语言管理/UI文案/数据表/字段/翻译详情/任务/配音/接口配置 |
| 流程 | FL-i18n-001 ~ 005 | 语言启用/UI翻译/内容翻译/配音生成/文案发布 |
| 状态机 | SM-i18n-001 | 翻译状态 |

### 融合点 / 冲突点
- 依赖 auth/account-entry 提供的管理员登录
- 管理后台侧边栏新增「国际化管理」一级菜单
