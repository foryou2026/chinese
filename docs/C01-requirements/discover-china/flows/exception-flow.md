<!-- TARGET-PATH: docs/C01-requirements/discover-china/flows/exception-flow.md -->

# C01 · 异常流程图 · discover-china

> 7 个异常流

## E1 · 应用端 04-12 类目未登录

```mermaid
flowchart LR
  A[点 04-12 类目卡片] --> B[弹 登录提示 Modal]
  B --> C{选择}
  C -- 主按钮 登录 --> D[/auth/login?redirect=/china/categories/04]
  C -- 取消 --> E[关闭 Modal 留在类目卡片页]
```

## E2 · TTS 调用失败

```mermaid
flowchart LR
  A[点播放] --> B[POST tts/synthesize] --> C{结果}
  C -- 200 --> D[播放 + 缓存]
  C -- 5xx / timeout --> E[Toast 朗读失败 稍后重试]
  E --> F[后台异步 retry n 次] --> G[成功后 invalidate cache]
```

## E3 · 文章下架时正在阅读

```mermaid
flowchart LR
  A[用户阅读中] --> B[管理员下架]
  B --> C[用户下次拉文章 / 句子] --> D[404]
  D --> E[空态页 文章已下架] --> F[返回类目]
```

## E4 · 管理端保存被覆盖

```mermaid
flowchart LR
  A[编辑器 A 用户加载 t0] --> B[B 用户在 t1 保存]
  C[A 用户在 t2 保存] --> D{服务端 updated_at > t0?}
  D -- 是 --> E[允许覆盖] --> F[Toast 该内容被 B 修改过 已覆盖]
  D -- 否 --> G[正常保存]
```

## E5 · 未保存离开拦截

```mermaid
flowchart LR
  A[表单脏] --> B[路由切换 / 关闭页 / 刷新]
  B --> C[拦截 Modal]
  C --> D{选择}
  D -- 离开 --> E[丢弃 + 跳走]
  D -- 取消 --> F[留在页面]
  D -- 保存后离开 --> G[执行保存 → 跳走]
```

## E6 · 删除类目尝试

```mermaid
flowchart LR
  A[管理员尝试 DELETE 类目 API] --> B[后端拒绝 405]
  B --> C[前端禁用按钮 + tooltip 类目固定不可删]
```

## E7 · 5 语未填全发布

```mermaid
flowchart LR
  A[文章状态 待发布] --> B[点 发布]
  B --> C{所有句子 5 语齐?}
  C -- 否 --> D[弹错误 Modal 列出缺失列表] --> E[跳到首个缺失句子]
  C -- 是 --> F[发布成功]
```
