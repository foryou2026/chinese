# 枚举定义

## translation_status_enum

> 翻译条目状态（UI 文案 + 数据库内容共用）。仅两种状态，无审核和过期概念。

| 值 | 含义 |
|----|------|
| `pending` | 待翻译 |
| `translated` | 已翻译（AI 翻译完成或管理员手动编辑） |

## translation_task_type_enum

> 翻译任务类型

| 值 | 含义 |
|----|------|
| `ui` | UI 文案翻译 |
| `content` | 数据库内容翻译 |

## task_status_enum

> 任务执行状态（翻译任务和配音任务共用）

| 值 | 含义 |
|----|------|
| `queued` | 已入队 |
| `running` | 执行中 |
| `completed` | 已完成 |
| `partial` | 部分完成 |
| `cancelled` | 已取消 |

## language_family_enum

> 语系分组

| 值 | 含义 |
|----|------|
| `east_asian` | 东亚 |
| `southeast_asian` | 东南亚 |
| `south_asian` | 南亚 |
| `west_european` | 西欧 |
| `north_european` | 北欧 |
| `east_european` | 东欧 |
| `middle_eastern` | 中东 |
| `african` | 非洲 |

## text_direction_enum

> 文字方向

| 值 | 含义 |
|----|------|
| `ltr` | 从左到右 |
| `rtl` | 从右到左 |

## audio_status_enum

> 配音文件状态

| 值 | 含义 |
|----|------|
| `pending` | 待生成 |
| `generating` | 生成中 |
| `completed` | 已完成 |
| `failed` | 生成失败 |

## provider_test_status_enum

> 供应商连接测试状态

| 值 | 含义 |
|----|------|
| `untested` | 未测试 |
| `success` | 测试成功 |
| `failed` | 测试失败 |
