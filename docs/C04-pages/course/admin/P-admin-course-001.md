<!-- TARGET-PATH: docs/C04-pages/course/admin/P-admin-course-001.md -->

# P-admin-course-001 · 课程目录总览

> F3 源:`P-admin-course-001` · 路由 `/admin/course` · R-013

## 1. 进入条件
- 已登录 admin(`super / admin / readonly` 任一)。

## 2. 初始数据
- `GET /admin/course/overview` → 5 主题(按 `admin.主题范围 过滤)+ 每主题已发布章节统计 + 缺口数;
- `GET /admin/course/gaps` → 缺口看板(待发布 KP 数 / 待发布题数 / 媒资引用断链 / 节末测未配置)。

## 3. 主要交互
- 5 张主题卡片点击 → 跳 P-admin-course-002 主题树;
- 缺口看板项点击 → 跳对应详情(P-admin-course-002 / 004 / 005 / 007 / 008)带筛选;
- 顶部全局搜索图标 → 跳 P-admin-course-009。

## 4. 弹窗
- D-10 缺口详情(快速预览)。

## 5. 状态
- 加载:卡片骨架;
- 空:主题范围=[]` 时友好拦截 + 申请权限说明;
- 错误:overview 失败 → 错误占位。

## 6. 响应式
- ≥1280px:5 主题卡片 + 缺口看板并排;
- <1280px:垂直堆叠。

## 7. 不变量回链
§4 5 主题码白名单、行级 主题范围 过滤、永远不删除主题。
