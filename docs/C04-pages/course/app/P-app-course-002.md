<!-- TARGET-PATH: docs/C04-pages/course/app/P-app-course-002.md -->

# P-app-course-002 · 学习地图 + 节内学习

> F3 源:`P-app-course-002` · 路由 `/learn` (地图) / `/learn/{track}/{stage}/{chapter}/{lesson}` (节内) · R-004..008

## 1. 进入条件
- 已登录 + 已订阅当前主题(否则触发 D-12);
- 节状态须 `unlocked / in_progress / passed`,`locked` 显示锁状 + Toast 提示。

## 2. 初始数据
- 地图视图:`GET /app/learn/map?track={track}` → 阶段→章→节树 + 每节 `status / progress`;
- 节学习:`GET /app/lesson/{code}` 聚合接口 → 节基本信息 + 12 KP 完整内容 + 节末 6 题 + 媒资 URL;触发整节预下载(`KP+题+音频`),失败走 FX-course-06。

## 3. 主要交互
- 地图视图:阶段卡片点击展开章/节列表;节图标 🔒/⚪/🟡/🟢;
- 节内:顶部进度条(`current_idx / 12`),KP 讲解卡 → 滑下一张;每 3-4 个 KP 插入随堂练 2-4 题;
- 答题:点选即提交,反馈 ✅/❌ + 解析卡;`POST /app/answer` 写 `user_answers` + 触发 SRS;
- 退出节学习时 `POST /app/lesson/{code}/checkpoint` 保存 `last_kp_id`;
- 学完 12 KP 弹 D-13(做小测 / 跳过);
- 节末小测:6 题统一提交 `POST /app/lesson/{code}/finish`,展示结算页(得分 + 通过与否 + 错题列表)。

## 4. 弹窗
- D-13 节末小测确认 · D-14 答题反馈 + 🚩举报 · D-1 退出节中弹"是否退出"

## 5. 状态
- 加载:KP 卡骨架;
- 空:不存在,只有 404;
- 错误:答题接口失败 → 进 FX-course-01 弱网本地队列;
- 离线条:断网持续 >5s 顶部红条 + 本地队列计数。

## 6. 响应式
- 全平台单列;
- 大屏 KP 卡居中,左右留白;
- 答题键盘(`type_pinyin` / `type_zh_ime`)弹起时卡片上推。

## 7. 不变量回链
§4 节固定 12 KP / 6 节末题、`is_quiz_required=false` 可跳过、通过线 60%、节 code 格式 `<track>-<stage>-<chapter>-<lesson>`。
