<!-- TARGET-PATH: docs/C04-pages/course/app/P-app-course-005.md -->

# P-app-course-005 · 错题本

> F3 源:`P-app-course-005` · 路由 `/wrong` · R-010

## 1. 进入条件
- 已登录。

## 2. 初始数据
- `GET /app/wrong?cursor=&limit=30` → 当前用户 `user_answers WHERE is_correct=false` 去重到 question_id,JOIN questions / kp 显示;
- 字段:题干 / 我的答案 / 正确答案 / 所属节 / 错误次数 / 最近错时间。

## 3. 主要交互
- 列表瀑布;
- 点单题 → Drawer 展示完整解析(只读);
- "去复习" → 跳 P-app-course-004 该 KP 优先;
- 筛选:主题 / KP 类型 / 题型 / 时间段。

## 4. 弹窗
- 无新增。

## 5. 状态
- 空:无错题 → 占位 + 鼓励文案;
- 加载:列表骨架。

## 6. 响应式
- ≤640px 单列卡片;>640px 双列。

## 7. 不变量回链
不修改成绩(R-024)、只读视图、引导回 SRS。
