<!-- TARGET-PATH: docs/C03-ia/course/07-error-pages.md -->

# 07 · 错误 / 边界态 / 弹窗对照 · course

## 1. 通用错误页

| 状态 | 触发场景 | 表现 | 主要 P-ID |
|------|---------|------|----------|
| `empty` | SRS 今日 0 条 / 错题本 0 条 / 节内无 KP | Empty 组件 + 引导按钮 | P-app-course-004/005 · P-admin-course-002 |
| `403-no-subscription` | 访问非订阅主题 | 强制订阅引导页 + 试学 1 章入口 | P-app-course-002 |
| `403-no-track-scope` | admin 访问 scope 外主题 | 友好拦截 + 申请权限链接 | P-admin-course-002..005 |
| `404` | 节 code / KP id / 题 id 不存在 | 404 + 返回上一级 | 所有详情类 |
| `410-unpublished` | 用户端直链访问 发布态=false` 节 | 410 + "内容已下架" + 回首页 | P-app-course-002, 007 |
| `429` | 接口限流(答题接口 ≥ 60 次/分)| Toast + 退避 | P-app-course-002/004/007 |
| `5xx` | 服务端异常 | 通用错误页 + 重试 | 全部 |
| `offline` | navigator.onLine=false 持续 >5s | 顶部红条 + 本地队列计数 | P-app-course-002/004/007 |

## 2. 弹窗对照表(D-1..D-18)

> 与 〔历史素材〕 编号一致。

| D-ID | 名称 | 触发位置 | 性质 |
|------|------|---------|------|
| D-1 | 二次确认 | 删除 KP/题/媒资/节 | 危险确认 |
| D-2 | 未保存离开拦截 | 编辑 Drawer 表单脏 + 路由切换 | 阻断 |
| D-3 | 批量发布 / 下架确认 | P-admin-course-004/005 列表批量动作 | 危险确认 |
| D-4 | 级联发布提示 | P-admin-course-002 章/节发布 | 信息 + 确认 |
| D-5 | 媒资引用拦截 | P-admin-course-007 删除有引用媒资 | 阻断 |
| D-6 | LWW 覆盖提示 | 多管理员并发保存 | Toast 提示 |
| D-7 | 举报详情抽屉 | P-admin-course-006 行点击 | 抽屉 |
| D-8 | 举报处理动作 | D-7 内[采纳][忽略] | 确认 |
| D-9 | 试抽预览抽屉 | P-admin-course-008 配 blueprint | 抽屉(不写 attempt)|
| D-10 | 缺口看板 | P-admin-course-001 / 002 | 信息 |
| D-11 | 主题切换 Sheet | 应用端顶部主题徽章 | 切换 |
| D-12 | 订阅引导 | 用户访问未订阅主题 | 引导 |
| D-13 | 节末小测确认 | 学完 12 KP | 选择(做/跳)|
| D-14 | 答题反馈 / 🚩举报 | 答题判分后反馈页 | 操作 |
| D-15 | 批量导入 | P-admin-course-004/005 上传 CSV/JSON | 多步 |
| D-16 | KP/题 Drawer | P-admin-course-004/005 编辑 | 抽屉 Tab |
| D-17 | 进入引导 | 首次进 App | 多步流(选语言→选主题→自评→定级)|
| D-18 | 阶段考结果 | P-app-course-007 交卷后 | 信息 |
