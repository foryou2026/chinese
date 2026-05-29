# 状态机

## SM-i18n-001 翻译条目状态

> 适用于 UI 文案翻译和数据库内容翻译，按（条目 × 语言）独立计算状态。

```mermaid
stateDiagram-v2
    [*] --> pending : 新增条目 / 新启用语言
    pending --> translated : AI 翻译完成
    pending --> reviewed : 管理员手动填写
    translated --> reviewed : 管理员审核通过 / 手动编辑
    translated --> outdated : 源文变更
    reviewed --> outdated : 源文变更
    outdated --> pending : 管理员确认需重新翻译
    outdated --> translated : AI 重新翻译
    outdated --> reviewed : 管理员手动更新
```

### 状态定义

| 状态 | 含义 | 视觉标记 | 触发条件 |
|------|------|---------|---------|
| `pending` | 待翻译 | 🔴 红色 | 新建条目 / 新启用语言 / 手动重置 |
| `translated` | AI 已翻译 | 🟡 黄色 | AI 翻译任务完成 |
| `reviewed` | 已审核 | 🟢 绿色 | 管理员手动编辑或确认 |
| `outdated` | 已过期 | 🟠 橙色 | 源文内容变更 |

### 约束
- 每个翻译条目的每种目标语言各自维护独立状态
- 状态不可跳过（pending 不能直接到 outdated）
- 删除源记录时，对应翻译条目物理删除

## SM-i18n-002 翻译任务状态

```mermaid
stateDiagram-v2
    [*] --> queued : 创建翻译任务
    queued --> running : 开始执行
    running --> completed : 全部翻译完成
    running --> partial : 部分翻译失败
    running --> cancelled : 管理员取消
    queued --> cancelled : 管理员取消
    partial --> queued : 重试失败部分
```

### 状态定义

| 状态 | 含义 |
|------|------|
| `queued` | 已入队，等待执行 |
| `running` | 正在执行翻译 |
| `completed` | 全部完成 |
| `partial` | 部分完成，部分失败 |
| `cancelled` | 已取消 |
