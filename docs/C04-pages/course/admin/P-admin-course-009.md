<!-- TARGET-PATH: docs/C04-pages/course/admin/P-admin-course-009.md -->

# P-admin-course-009 · 全局搜索

> F3 源:`P-admin-course-009` · 快捷键 `Ctrl/Cmd + K` · R-021

## 1. 进入条件
- admin。

## 2. 初始数据
- 顶部搜索框 + 3 段命中(`Lesson / KP / Question`)分别 `LIMIT 20`;
- 默认按 主题范围 过滤。

## 3. 主要交互
- 输入 → 300ms 防抖触发;
- 每段命中卡片显示:`code / 标题 / 主题 / 高亮片段`;
- 点击 → 跳目标编辑:
  - Lesson → P-admin-course-003;
  - KP → P-admin-course-004 + 自动打开 Drawer;
  - Question → P-admin-course-005 + 自动选中并打开预览;
- 顶部筛选 chips:主题 / KP 类型 / 题型 / 状态。

## 4. 弹窗
- 无新增。

## 5. 状态
- 加载:三段骨架;
- 空:无命中 → "尝试更换关键词"提示;
- 错误:接口失败 → 局部错误条。

## 6. 响应式
- 三段命中区:≥1024px 横排;<1024px 纵排折叠。

## 7. 不变量回链
R-021 三段聚合 + 高亮、行级 主题范围 过滤、跳目标编辑保持 LWW。
