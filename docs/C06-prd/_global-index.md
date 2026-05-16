<!-- TARGET-PATH: docs/C06-prd/_global-index.md -->

# C05 PRD · 全局 feature 索引 + 状态总表

> 项目全部 PRD 入口。每启动一个 feature 必须在此追加;每个 feature 的状态(进行中 / 已冻结)在此同步。

## 1. Feature 矩阵

| Feature ID | 业务域 | surface(端) | C05 入口 | 状态 | 最近更新 |
|------------|-------|-------------|----------|------|---------|
| `course` | 课程学习 | app + admin | [course/](course/) · [app](course/app/00-index.md) · [admin](course/admin/00-index.md) | 进行中(Round 6) | 2026-05-16 |
| `discover-china` | 发现中国(文章/句子) | app + admin | [discover-china/](discover-china/) · [app](discover-china/app/00-index.md) · [admin](discover-china/admin/00-index.md) | 进行中(Round 6) | 2026-05-16 |
| `auth` | 鉴权(单 feature 多端 = app + admin) | app + admin | [auth/](auth/) · [app](auth/app/00-index.md) · [admin](auth/admin/00-index.md) | 进行中(Round 7;双 feature 合并 2026-05-17) | 2026-05-17 |

## 2. 业务域映射

| feature | 来源 | PRD 主要参考 |
|---------|------|-------------|
| `course` | 0→1 PRD | C06-prd/course/{app,admin}/ |
| `discover-china` | 0→1 PRD | C06-prd/discover-china/{app,admin}/ |
| `auth` | 规范派生 | [C02-permissions/](../C02-permissions/) |

## 3. 进度速览

| Feature | C01 R | C02 I | C03 N | C04 H | C05 E |
|---------|:-:|:-:|:-:|:-:|:-:|
| course | ✓ | ✓ | ✓ | ✓ | 进行中(Round 6 展开 page-specs) |
| discover-china | ✓ | ✓ | ✓ | ✓ | 进行中 |
| auth | ✓ | ✓ | ✓ | ✓ | 进行中(已并 app+admin 为单 feature 多端) |

## 4. 跨 feature 依赖

- `course` 的"学员举报"流向 `course/admin/M-report`,无外部 feature 依赖。
- `discover-china/app` 的 `/me/progress` 已废弃,**不** 再调用 `course/srs`。
- `auth` 是所有其它 feature 的鉴权前置;app + admin 共享一份 鉴权后端,但 `会话记录` 上独立计数,3-设备硬上限按端隔离。

## 5. 全局术语

详见 [_glossary.md](_glossary.md)。
