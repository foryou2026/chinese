<!-- TARGET-PATH: docs/C05-prd/course/app/04-feature-catalog.md -->

# 04 · 功能模块(MoSCoW)· course / **app**

> Round 5 按端过滤。完整全端清单见 [_shared/](../_shared/);admin 端见 [../admin/04-feature-catalog.md](../admin/04-feature-catalog.md)。

## Must-Have

| M-ID | 名称 | 价值 | 验收 |
|------|------|------|------|
| M-course-learning | 节内学习与首页 | C 端核心;无此模块产品不可用 | 8 页核心路径全可达;答题写库成功 |
| M-course-srs | SRS 复习与错题本 | 学习留存关键 | 队列拉取 < 300ms;错题本可回看 |
| M-course-exam | 考试中心 | 学员目标驱动 | 4 类考试可完整完成 + 报告 |
| M-course-i18n-perm-app | 5 语 + 主题切换 + RLS | 多语市场 + 数据隔离 | 5 语切换正常;RLS 不漏权 |

## Should-Have

| M-ID | 名称 | 价值 |
|------|------|------|
| M-course-onboarding | 引导 / 定级 / 订阅 | 提高完成率 |
| M-course-profile | 个人统计 / 设置 | 学员留存 |

## Could-Have

| M-ID | 名称 |
|------|------|
| M-course-report-app | 学员举报入口浮层(D-14) |

## Won't-Have (this release)

- 离线模式 / pwa
- 社交 / 评论
- 自定义题目
