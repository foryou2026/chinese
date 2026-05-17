<!-- TARGET-PATH: docs/C06-prd/course/app/05-user-journeys.md -->

# 05 · 用户旅程 · course / **app**

> 详细流程图见 [`../../../C03-ia/course/app/02-flows.md`](../../../C03-ia/course/app/02-flows.md);本文件给出 PRD 视角的旅程概览。

## 5.1 主旅程

### J-app-course-1 · 试学 → 订阅 → 持续学习
1. 注册 → 选首选主题(EC/FC/HSK/DL 之一)→ 进入主题首页
2. 第 1 章前 N 节免费 → 完成 ≥ 1 节后引导订阅
3. 订阅成功 → 解锁全主题 → 进入正常"学练复考"闭环

### J-app-course-2 · 日常学习闭环(单次会话 15-30 min)
1. 首页 [P-001](06-page-specs/P-app-course-001.md) → 续学(回到上次节)
2. 节学习 [P-002](06-page-specs/P-app-course-002.md):KP 讲解 → 节内自测
3. 节内出错 → 自动入 SRS;离开时记录游标

### J-app-course-3 · 复习闭环(每日 ≤ 50)
1. 进入 [P-004](06-page-specs/P-app-course-004.md) → 服务端按 SM-2 返回今日队列(上限 50)
2. 逐题答 → 对/错回写盒子 → 错题保留至下一周期
3. 完成 → 引导回主路径

### J-app-course-4 · 错题本独立闭环
1. [P-005](06-page-specs/P-app-course-005.md) → 仅显示当前游标所在主题的错题
2. 连续 3 次正确 → 移出错题本(但仍走 SRS)

### J-app-course-5 · 考试闭环
1. [P-006](06-page-specs/P-app-course-006.md) → 选节测/章测/阶段考
2. 阶段考前出现"题目卡片式试抽"[P-007](06-page-specs/P-app-course-007.md) §试抽段
3. 交卷 → [P-008](06-page-specs/P-app-course-008.md) 报告(分数、错题归档、推荐复习)

### J-app-course-6 · 个人统计
- [P-008](06-page-specs/P-app-course-008.md) 个人统计 Tab:连续天数、累计学习时长、节通过率

## 5.2 异常旅程

| ID | 触发 | 处理 |
|----|------|------|
| J-app-course-X1 | 弱网 / 离线 | 缓存当前节聚合数据,可离线继续 ≤ 5 道题,答题结果重连后补提 |
| J-app-course-X2 | 内容下线(管理员 unpublish) | 当前游标节失效 → 提示"内容已更新"→ 自动跳下一节 |
| J-app-course-X3 | 答题限流 429 | 友好降级"操作过快,休息一下" |
| J-app-course-X4 | 考试中崩溃 / 切后台 ≥ 5 min | 自动暂存,重进后续答 |
| J-app-course-X5 | 订阅过期 | 当日继续,次日入口受限 |
| J-app-course-X6 | 跨设备登录 | session 仅 1 个有效,旧设备被踢 → 提示 |
| J-app-course-X7 | 5 语切换 | UI / 翻译热更新,**不重载学习状态** |
