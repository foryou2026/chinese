<!-- TARGET-PATH: docs/C04-pages/course/app/P-app-course-003.md -->

# P-app-course-003 · KP 详情 / 卡片浏览

> F3 源:`P-app-course-003` · 路由 `/lesson/{code}/kp/{kpId}` · R-005/007

## 1. 进入条件
- 已登录;父节 发布态=true` 且父链全发布;
- 通常作为 P-app-course-002 节学习内的卡片栈渲染;直链访问也支持。

## 2. 初始数据
- `GET /app/kp/{kpId}?lang={ui_lang}` → KP 基础(类型/难度)+ 内容 JSON(按 7 类 KP 模板)+ 翻译 + 媒资 URL + 相关题 4-6;
- 与父节聚合接口共享缓存,避免重复请求。

## 3. 主要交互
- 卡片渲染按 KP 类型差异化(`pinyin / hanzi / word / phrase / grammar / sentence / dialog` 模板);
- 音频按钮 → 调媒资 URL 播放(失败回退本地缓存);
- 例句 / 释义双语切换(`zh ↔ ui_lang`);
- "我懂了" → 继续下一张;"再看一次" → 不增进度。

## 4. 弹窗
- 无独立弹窗,共用 D-14 反馈(从相关题入口)。

## 5. 状态
- 加载:卡片骨架;
- 空:不发生;
- 错误:KP 不存在 → 404;媒资 404 → 静音占位 + 文字解析。

## 6. 响应式
- 卡片宽度 ≤480px;
- 拼音 ruby 在中文上方;母语翻译可折叠。

## 7. 不变量回链
§4 5 语字段必填、多语标题字段 结构、媒资按 hash 引用。
