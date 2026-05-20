# 时区、货币与日期格式化

> **阶段**：B01-A 技术架构
> **冻结状态**：已冻结

---

## 时区策略

| 项目 | 决定 |
|------|------|
| 存储 | 数据库统一 UTC (`timestamptz`) |
| 传输 | API 统一 ISO 8601 UTC |
| 展示 | 前端按用户浏览器时区转换 |

## 货币与数字本地化

| 项目 | 决定 |
|------|------|
| 货币 | 使用 `Intl.NumberFormat` 按 locale 格式化 |
| 数字 | 使用 `Intl.NumberFormat` |
| 具体货币类型 | 由 Paddle 支付系统决定，前端按 Paddle 返回展示 |

## 日期格式

| 项目 | 决定 |
|------|------|
| 格式化库 | `Intl.DateTimeFormat`（原生，零依赖） |
| 相对时间 | `Intl.RelativeTimeFormat` |
| 显示格式 | 按用户 locale 自动适配 |

---

## 99. 待确认问题

无
