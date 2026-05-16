<!-- TARGET-PATH: docs/C05-prd/course/admin/05-user-journeys.md -->

# 05 · 用户旅程 · course / **admin**

> 详细流程图见 [`../../../C02-ia/course/admin/02-flows.md`](../../../C02-ia/course/admin/02-flows.md)。

## 5.1 主旅程

### J-admin-course-1 · 新章上架闭环
1. `content_admin` 登录(2FA) → 选所属主题
2. [P-001](06-page-specs/P-admin-course-001.md) → 进入主题 → [P-002](06-page-specs/P-admin-course-002.md) 选阶段
3. [P-003](06-page-specs/P-admin-course-003.md) 拖拽排序章 → [P-004](06-page-specs/P-admin-course-004.md) 配置节 + KP 绑定
4. [P-005](06-page-specs/P-admin-course-005.md) 批量导入题目(JSON)→ 抽检 ≥ 10 题 / 节
5. [P-007](06-page-specs/P-admin-course-007.md) 关联媒资 → 5 语字段补齐
6. 点击"发布" → 进入 staging → super 审批 → 上架

### J-admin-course-2 · 举报处理闭环(7 天 SLA)
1. [P-006](06-page-specs/P-admin-course-006.md) → 待处理列表
2. 查看上下文(自动跳转关联题目)→ 判定(有效 / 无效 / 重复)
3. 有效 → 同步修订题目 → 学员侧 SRS 队列自动剔除该题
4. 无效 → 关闭 + 留言
5. 超 7 天未处理 → super 看板告警

### J-admin-course-3 · 长期撤回(>30 天)
1. `content_admin` 发起撤回 → 系统提示"超 30 天需 super 审批"
2. super 在 [P-009](06-page-specs/P-admin-course-009.md) 待审池中确认
3. 通过后撤回生效 → 学员侧节失效 + 自动跳转

### J-admin-course-4 · 全局搜索 / 统计
1. [P-009](06-page-specs/P-admin-course-009.md) 全局搜索(题 / KP / 节 / 媒资)
2. 统计:本主题学员数、节通过率、热门错题(scope 限制)

## 5.2 异常旅程

| ID | 触发 | 处理 |
|----|------|------|
| J-admin-course-X1 | scope 越权 | UI 隐藏 + 服务端 403 + 审计日志 |
| J-admin-course-X2 | 导入文件格式错 | 全文件拒绝 + 显示前 10 条错误行;不部分接受 |
| J-admin-course-X3 | 5 语字段缺 | 发布按钮禁用 + 高亮缺失语种 |
| J-admin-course-X4 | 媒资被引用时尝试删除 | 拒绝 + 列出引用方 |
| J-admin-course-X5 | 高危操作不做二次确认 | 阻断 + 重新弹确认框 |
