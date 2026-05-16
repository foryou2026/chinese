<!-- TARGET-PATH: docs/C03-pages/course/P-app-course-007.md -->

# P-app-course-007 · 考试答题 / 倒计时

> F3 源:`P-C-7` · 路由 `/exam/{attemptId}` · R-011

## 1. 进入条件
- `attempt.status=in_progress`;
- 通过 P-app-course-006 [开始考试] 进入,直链访问校验 `user_id`。

## 2. 初始数据
- `GET /app/exam/attempt/{id}` → snapshot 题列表(已按 blueprint 抽好,顺序固定)+ `time_limit_sec` + `time_used_sec`;
- 全屏沉浸进入,隐藏底部 Tab;
- 倒计时 useEffect 启动,每秒减 1,本地 + 服务端同步。

## 3. 主要交互
- 题号导航条(已答 / 未答标记);
- 答题不反馈对错(与 P-app-course-002 学习模式不同);
- 可前后切题 / 标记疑问;
- 中途无返回按钮;关闭浏览器 / 切应用 → 后端 5 分钟无心跳后 `status=failed score=0`;
- "交卷" → D-1 二次确认 → `POST /app/exam/attempt/{id}/submit` 批量判分 → 结算 D-18。

## 4. 弹窗
- D-1 交卷确认 · D-18 阶段考结果(显示满分 100 + 动态均分单题分 + 通过 / 失败 + 错题入 SRS 提示)

## 5. 状态
- 加载:全屏占位;
- 离线:答案先写本地队列,继续答;回网后批量同步;
- 倒计时归零 → 自动提交。

## 6. 响应式
- 题号导航条 ≤640px 折叠为下拉。

## 7. 不变量回链
R-011 倒计时 + 不能中途退出 + 退出 = 零分、R-025 满分 100 动态均分、R-027 阶段考过解锁下一阶段。
