<!-- TARGET-PATH: docs/C02-ia/course/01-feature-catalog.md -->

# 01 · 功能模块清单(M-ID) · course

| M-ID | 名称 | 涵盖 R-ID | 关联 P-ID |
|------|------|----------|-----------|
| **M-course-content** | 内容骨架与编辑 | R-013, 014, 015, 016, 017, 022, 023 | P-admin-course-001..005 |
| **M-course-learning** | 节内学习与首页 | R-001, 003, 004, 005, 006, 007, 008 | P-app-course-001..003 |
| **M-course-srs** | SRS 复习与错题本 | R-008, 009, 010, 026 | P-app-course-004, 005 |
| **M-course-exam** | 考试中心(4 类)| R-011, 020, 025, 027 | P-app-course-006, 007, 008 · P-admin-course-008 |
| **M-course-onboarding** | 引导 / 定级 / 订阅 | R-002, 028 | P-app-course-001(子流)|
| **M-course-media** | 媒资库与去重 | R-019 | P-admin-course-007 |
| **M-course-report** | 学员举报闭环 | R-018, 024 | P-admin-course-006 · 答题反馈弹窗 D-14 |
| **M-course-search** | 全局搜索 | R-021 | P-admin-course-009 |
| **M-course-profile** | 个人统计 / 设置 | R-001, 012 | P-app-course-008 |
| **M-course-i18n-perm** | 5 语 + 主题访问控制 + 行级权限 | R-028, 029, 030;§4 全部不变量 | 横切所有页面 |
