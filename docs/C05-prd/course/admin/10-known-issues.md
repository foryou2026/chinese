<!-- TARGET-PATH: docs/C05-prd/course/admin/10-known-issues.md -->

# 10 · 已知问题 · course / **admin**

| ID | 一句话 | 影响 | 计划 |
|----|-------|------|------|
| KI-admin-course-001 | 5 语字段录入切 Tab 时,光标位置丢失 | [P-005](06-page-specs/P-admin-course-005.md) | Round 8 修 |
| KI-admin-course-002 | 章节拖拽在 Firefox 偶发跳位 | [P-003](06-page-specs/P-admin-course-003.md) | 改用 react-dnd 统一适配 |
| KI-admin-course-003 | 批量导入 > 5000 行时浏览器卡顿 | [P-005](06-page-specs/P-admin-course-005.md) | 改为分片上传 + 服务端流式校验 |
| KI-admin-course-004 | scope 内统计与全量统计 UI 区分不明显 | [P-009](06-page-specs/P-admin-course-009.md) | 加显眼"scope: EC" 徽标 |
| KI-admin-course-005 | 撤回超 30 天的二次确认弹窗文案不够强 | 全局 | Round 7+ 文案审 |

## 已澄清不修

| ID | 一句话 | 原因 |
|----|-------|------|
| KI-admin-course-006 | 不支持 AI 自动生成题目 | 2025-11 已撤"系统内生成工作台",明确不做 |
| KI-admin-course-007 | 不支持 5 语机器翻译填充 | 必须人工填齐;翻译质量为内容竞争力 |
