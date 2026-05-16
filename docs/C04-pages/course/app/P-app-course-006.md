<!-- TARGET-PATH: docs/C04-pages/course/app/P-app-course-006.md -->

# P-app-course-006 · 考试中心入口 + 列表

> F3 源:`P-app-course-006` · R-011

## 1. 进入条件
- 已登录;
- 节末小测随节末入口入,本页主要展示章测 / 阶段考 / HSK 模考。

## 2. 初始数据
- → 列出可考列表:
  - `chapter_test`(已学章解锁)、`stage_exam`(完成阶段所有节解锁)、`hsk_mock`(HSK 主题独享);
  - 每项包含 `pass_score / time_limit / question_count / my_best_attempt`。

## 3. 主要交互
- 卡片点击 → 详情页(规则说明 + 历史成绩 + [开始考试]);
- [开始考试] → 写考试记录 返 `attempt_id` → 跳 P-app-course-007;
- 阶段考已通过显示"已通过 ✓"灰色按钮 + Tooltip "阶段考通过后不可重考"(FX-course-05)。

## 4. 弹窗
- D-1 开始考试二次确认("将开始倒计时,中途退出 = 零分,确定?");

## 5. 状态
- 加载:列表骨架;
- 空:暂无可考(新用户)→ 提示先去学习。

## 6. 响应式
- 卡片网格自适应。

## 7. 不变量回链
R-027 阶段考解锁、R-025 题目动态均分、决策 H5 阶段考不可重考。
