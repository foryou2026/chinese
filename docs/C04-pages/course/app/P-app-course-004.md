<!-- TARGET-PATH: docs/C04-pages/course/app/P-app-course-004.md -->

# P-app-course-004 · SRS 今日复习

> F3 源:`P-app-course-004` · 路由 `/review` · R-009/026

## 1. 进入条件
- 已登录;
- 无订阅也可复习(已学内容)。

## 2. 初始数据
- `GET /app/srs/today?limit=50` → 按 `box ASC, due_at ASC` 拉到期 KP;
- 每 KP 抽一道关联题(`questions WHERE kp_id IN (...) ORDER BY RANDOM()`),题型随机轮换避免背答案;
- 一组 10 题。

## 3. 主要交互
- 顶部统计:今日到期总数 / 已完成数 / 剩余;
- 逐题答题(交互与 P-app-course-002 一致),`context_type=srs_review`;
- 答对:复习队列.box +1, due_at += `间隔表`(1/3/7/14/30 天);
- 答错:`box=1, due_at=明天`;
- 完成一组 → 结算页 + "再来一组" / "稍后";到期清空 → 完成态 + 推荐学习新节。

## 4. 弹窗
- D-14 反馈 / 举报 · 中途退出 D-1 二次确认("中断不算练习,确定?")

## 5. 状态
- 加载:题卡骨架;
- 空:今日 0 到期 → 庆祝态 + "去学新节"按钮;
- 离线:走 FX-course-01 本地队列。

## 6. 响应式
- 同 P-app-course-002 答题区域。

## 7. 不变量回链
SRS Leitner 5 盒间隔表、R-026 答题副作用、R-029 永不读未发布(关联题须 发布态=`true`)。
