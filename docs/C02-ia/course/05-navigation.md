<!-- TARGET-PATH: docs/C02-ia/course/05-navigation.md -->

# 05 · 导航 · course

## 应用端

- 底部 5 Tab(固定顺序):`首页 / 学习 / 复习 / 考试 / 我的` → 分别 `P-app-course-001/002/004/006/008`;
- 主题切换:顶部当前主题徽章 → 点开主题选择 Sheet(只展示已订阅主题);
- 节学习内置面包屑:`主题 › 阶段 › 章 › 节 › KP n/12`;
- 考试中心进考:全屏沉浸,顶部 only 倒计时 + 题号,无返回键(中途退出 = 零分);
- 错题本入口:P-app-course-005 由 P-app-course-008(我的)或 P-app-course-004(复习)二级跳转。

## 管理端

- 顶部水平 Tabs(主菜单)与 P-A-1..9 一一映射;
- 二级导航在 P-admin-course-002 内置主题选择器(行级 `tracks_scope` 过滤);
- 全部页面共享面包屑组件:`课程 › <主题> › <阶段> › <章> › <节>`;
- 编辑 Drawer 内 Tab:基础 / 内容 / 翻译 / 媒资 / 题目(KP)/ 选项 / 解析(Question);
- 全局搜索 `Ctrl/Cmd + K` 触发 → 飞入 P-admin-course-009。

## 与权限联动

| 角色 | 可见页面 |
|------|---------|
| `super` | 全部 9 个 P-admin |
| `content_admin` | 全部 9 个,但只能编辑 `tracks_scope` 内主题 |
| `readonly` | 可见全部,所有写入按钮置灰 |
