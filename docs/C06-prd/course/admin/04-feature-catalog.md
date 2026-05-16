<!-- TARGET-PATH: docs/C06-prd/course/admin/04-feature-catalog.md -->

# 04 · 功能模块()· course / **admin**

## Must-Have

| M-ID | 名称 | 验收 |
|------|------|------|
| M-course-content | 内容骨架与编辑(轨道→题) | 5 级编辑完整;发布校验通过 |
| M-course-i18n-perm-admin | 5 语校验 + 主题范围 列级 + 审计 | 5 key 缺一拒收;scope 外不可见 |
| M-course-exam-admin | 考试编辑与预览 | 可创建 4 类考试并预览效果 |

## Should-Have

| M-course-media | 媒资库与去重 | sha256 秒传命中率 ≥ 60% |
| M-course-report | 学员举报审核 | 平均处理 < 24h |
| M-course-search | 全局搜索 + 统计 | 关键字 ≤ 500ms |

## Could-Have

- 协同编辑(实时多人光标)
- AI 辅助出题(已有题→变体)

## Won't-Have

- 全文 OCR 题目识别(下季度评估)
