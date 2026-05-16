<!-- TARGET-PATH: docs/C03-ia/course/app/02-flows.md -->

# 02 · 关键用户流程 · course / **app**

> Round 5 按端过滤。仅描述 C 端学员发起的主流程;管理员发起的内容编辑 / 审核流程见 [../admin/02-flows.md](../admin/02-flows.md);跨端共享(状态机 / 通知)见 [_shared/](../_shared/)。

## F-app-course-1 · 注册到首次学习(冷启动)

```
landing → P-app-auth-002(注册) → 验证邮件 → P-app-auth-001(登录)
       → P-app-course-001(首页:无轨道)→ 选择轨道(M-onboarding)
       → P-app-course-001(首页:进入轨道地图)
       → P-app-course-002(节)→ P-app-course-003(答题)→ 完成
```

涉及 endpoint:`GET /tracks` · `POST /me/select-track` · `GET /tracks/:t/map` · `GET /lessons/:id` · `POST /answers`。

## F-app-course-2 · 日常学习闭环

```
P-app-course-001(首页)→ "今日待复习" → P-app-course-004(SRS 队列)
                                  → 逐题答题(POST /answers,update_srs=true)
                                  → 队列空 → 推荐 P-app-course-002 新节
```

## F-app-course-3 · 学员举报错题

```
P-app-course-003(答题)→ 长按题目 → D-14(举报浮层)→ POST /questions/:q:report
                    → toast "已提交,人工审核中" → 返回答题
```

> 后续 admin 审核走 [../admin/02-flows.md](../admin/02-flows.md#f-admin-course-report)。

## F-app-course-4 · 参加考试

```
P-app-course-001 → 考试入口 tab → P-app-course-006(考试列表)
               → 点击考试 → P-app-course-007(考试进行)
                          ↳ 60s 心跳 + 自动保存
                          ↳ 提交 → P-app-course-008(报告)
                          ↳ 中途离开 → 30 分钟后自动 abandon
```

## F-app-course-5 · 错题本回顾(独立于 SRS)

```
P-app-course-001 → 我的 → P-app-course-005(错题本)
               → 筛选(知识点/时间)→ 选题 → 重做(不进 SRS,仅 mark resolved)
```

## 跨端联动点

| 触发(本端) | 通过 | 影响(admin 端) |
|------------|------|----------------|
| 学员举报 | `course_reports` insert | M-course-report 审核队列 +1 |
| 题目快速反馈(D-14)| 同上 + `severity=low` | 同上 |
| 答题完成 | `course_answers` insert | M-course-search 索引异步刷新 |
