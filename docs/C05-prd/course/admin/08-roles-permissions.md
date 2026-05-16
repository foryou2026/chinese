<!-- TARGET-PATH: docs/C05-prd/course/admin/08-roles-permissions.md -->

> **本文件为 surface=`admin` 视角的 PRD 章节(Round 2 从 PRD.md 第 8 章拆出初版,后续按端过滤实质内容)。** 跨端通用术语见 [_shared/glossary.md](../_shared/glossary.md),跨端业务规则见 [_shared/business-rules.md](../_shared/business-rules.md)。

## 8. 角色权限矩阵

| 操作 | 学员 | content_admin (scope ⊃ track) | super | readonly |
|------|:--:|:--:|:--:|:--:|
| 浏览应用端 5 Tab | ✓ | × | × | × |
| 节学习 / SRS / 错题本 | ✓ | × | × | × |
| 考试(节/章/阶段/HSK)| ✓ | × | × | × |
| 进 `/admin/course/*` | × | ✓ | ✓ | ✓(只读)|
| 内容 CRUD(节 / KP / 题)| × | ✓(scope 内)| ✓ | ✗ |
| 媒资 CRUD | × | ✓ | ✓ | ✗ |
| 学员举报处理 | × | ✓ | ✓ | ✗ |
| 考试中心配置 / 发布 | × | ✓(scope 内)| ✓ | ✗ |
| 全局搜索 | × | ✓(scope 过滤)| ✓ | ✓(只读跳转)|
| 管理员账号 / `tracks_scope` 配置 | × | × | ✓ | × |
