<!-- TARGET-PATH: docs/C03-pages/course/P-app-course-001.md -->

# P-app-course-001 · 首页 / 主题切换 / 引导入口

> F3 源:`P-C-1` · 路由 `/` 或 `/home` · R-001/002/003

## 1. 进入条件
- 已登录(未登录 → 跳 `/auth/login`);
- 用户已选 `current_track`(否则触发 D-17 引导多步流)。

## 2. 初始数据(1 次请求)
- `GET /app/home/summary?track={current_track}` → 返回:
  - `user`(头像 / 昵称 / 母语 / UI 语言);
  - `continue_lesson`(节 code + 进度 % + last_kp_id);
  - `srs_due_count`(今日到期 KP 数);
  - `next_unlock`(即将解锁的节);
  - `recommend`(推荐节列表);
  - `streak_days`(连续打卡天数)。

## 3. 主要交互
- 顶部主题徽章 → 点开 D-11 主题 Sheet(只列已订阅主题)→ 切换写 `users.current_track` 并刷新 summary;
- "继续学习"卡片 → 跳 P-app-course-002(节学习)`/learn/{lesson_code}` 续传 `last_kp_id`;
- "今日复习 N"卡片 → 跳 P-app-course-004;
- "推荐"卡片 → 跳 P-app-course-002 该节;
- 底部 Tab 切换 → 不刷新 summary(本地缓存 10 分钟)。

## 4. 弹窗
- D-11 主题切换 Sheet · D-12 订阅引导(无订阅时触发)· D-17 引导(新用户首登)

## 5. 状态
- 加载态:5 区域骨架屏;
- 空态:新用户尚无 `continue_lesson` → "去学习"按钮跳学习地图;
- 错误:summary 失败 → 整页错误占位 + 重试。

## 6. 响应式
- ≤640px:5 区垂直堆叠;
- >640px:`continue_lesson` 与 `srs_due_count` 横向并列。

## 7. 不变量回链
R-028 订阅控制、R-029 永不读未发布、R-030 服务端为准 · §4 5 主题码白名单。
