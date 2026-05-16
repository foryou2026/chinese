<!-- TARGET-PATH: docs/C01-requirements/discover-china/flows/main-flow.md -->

# C01 · 主流程图 · discover-china

> 6 张主流(应用端 3 + 管理端 3)

## ① 应用端 · 访客首次浏览 01-03 公开类目

```mermaid
flowchart LR
  A[首页/Tab 切到 发现中国] --> B[GET 12 类目]
  B --> C{选择类目 code}
  C -- 01-03 --> D[文章列表]
  C -- 04-12 --> L[弹 登录提示 Modal]
  D --> E{选文章}
  E --> F[文章详情 第 1 句]
  F --> G{点播放}
  G -- 缓存命中 --> H[< 200ms 播放]
  G -- 缓存未命中 --> I[AI 生成 + 落缓存] --> H
```

## ② 应用端 · 用户全文朗读

```mermaid
flowchart LR
  A[文章详情 当前句 N] --> B[点 全文朗读]
  B --> C[播放第 N 句]
  C --> D[onended] --> E{N+1 存在?}
  E -- 是 --> F[滚动 + 高亮 + 播放 N+1] --> D
  E -- 否 --> G[结束 Toast]
```

## ③ 应用端 · 进度记忆

```mermaid
flowchart LR
  A[滚动 / 点句子卡片] --> B[当前句 N 锚定]
  B --> C{已登录?}
  C -- 是 --> D[debounce 1s PUT 进度]
  C -- 否 --> E[localStorage 写]
  F[下次进入文章] --> G[GET / read 进度] --> H[跳到 N]
```

## ④ 管理端 · 新建文章

```mermaid
flowchart LR
  A[/admin/china] --> B[选类目卡片] --> C[文章列表]
  C --> D[点 新建文章] --> E[Modal 填名称 5 语 + 拼音]
  E --> F[提交 → 系统生成 12 位 code] --> G[跳编辑页]
  G --> H[添加首句] --> I[5 语 Tab 填写] --> J[保存]
  J --> K{发布?}
  K -- 是 --> L[发布 → 应用端可见]
  K -- 否 --> M[保留 待发布]
```

## ⑤ 管理端 · 句子编辑 + 任意位置插入

```mermaid
flowchart LR
  A[文章编辑页] --> B[句子分页列表]
  B --> C{操作}
  C -- 编辑 --> D[Drawer 5 Tab + 拼音 + 中文]
  C -- 在当前后插入 --> E[Drawer 新句子] --> F[保存 → seq_no 自动重排]
  C -- 重排 --> G[拖拽 Drawer] --> H[保存 → seq_no 重新分配 + 缓存键跟随]
  D --> I[保存 → 后写覆盖检查] --> J[Toast]
```

## ⑥ 管理端 · 三级搜索

```mermaid
flowchart LR
  A[类目层搜索框] --> B[全局搜 文章标题 + 句子]
  B --> C[聚合页 P-admin-007]
  D[文章层搜索框] --> E[本类目内搜]
  F[句子层搜索框] --> G[本文章句子搜]
```
