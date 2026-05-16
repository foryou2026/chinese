<!-- TARGET-PATH: docs/C05-prd/course/app/02-glossary.md -->

# 02 · 术语(app 端局部)

> 项目级术语见 [`../../_glossary.md`](../../_glossary.md);feature 跨端术语见 [`../_shared/glossary.md`](../_shared/glossary.md);本文件仅列 **app 端独有 / 易混淆** 的术语。

| 术语 | app 端定义 |
|------|-----------|
| **节(lesson)** | 学员视角的最小学习单位,对应一次连续 15-30 分钟学习活动 |
| **节卡片** | [P-002](06-page-specs/P-app-course-002.md) 主区域显示的 KP 切换式卡片堆 |
| **静默题型** | app 端唯一可见题型集合(12 种):无麦克风、无手写 |
| **SRS 复习队列** | `/api/app/v1/srs/today` 返回的当日待复习 KP 集合,上限 50 |
| **错题本** | 答错过且尚未 3 次连续答对的题目集合,不进 SRS |
| **考试(exam)** | 包含节测 / 章测 / 阶段考三类;**学员端不可见**"系统内生成工作台"(2025-11 已撤) |
| **试抽(trial draw)** | 阶段考开始前的题目卡片预览(2025-11 新增) |
| **当前进度** | 学员当前所处的 `track/stage/chapter/lesson` 四级游标,登录态本地缓存 + 服务端同步 |
