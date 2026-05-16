<!-- TARGET-PATH: docs/C05-prd/_global-index.md -->

# C05 PRD · 全局 feature 索引 + 状态总表

> 项目全部 PRD 入口。每启动一个 feature 必须在此追加;每个 feature 的状态(进行中 / 已冻结)在此同步。

## 1. Feature 矩阵

| Feature ID | 业务域 | surface(端) | C05 入口 | 状态 | 最近更新 |
|------------|-------|-------------|----------|------|---------|
| `course` | 课程学习 | app + admin | [course/](course/) · [app](course/app/00-index.md) · [admin](course/admin/00-index.md) | 进行中(Round 6) | 2026-05-16 |
| `discover-china` | 发现中国(文章/句子) | app + admin | [discover-china/](discover-china/) · [app](discover-china/app/00-index.md) · [admin](discover-china/admin/00-index.md) | 进行中(Round 6) | 2026-05-16 |
| `app-auth` | C 端鉴权(退化单 surface) | app | [app-auth/app/](app-auth/app/00-index.md) | 进行中(Round 6) | 2026-05-16 |
| `admin-auth` | admin 端鉴权(退化单 surface) | admin | [admin-auth/admin/](admin-auth/admin/00-index.md) | 进行中(Round 6) | 2026-05-16 |

## 2. 业务域映射(数据源)

| feature | 数据源(`/function/`) | PRD 主要参考 |
|---------|---------------------|-------------|
| `course` | [`function/02-course/`](../../function/02-course/) | `prd/00..07-*.md` + `ai/F1..F4-*` |
| `discover-china` | [`function/01-china/`](../../function/01-china/) | `prd/F1..F3-*.md` + `ai/F1..F3-*` |
| `app-auth` / `admin-auth` | 规范派生(无 `/function/` 入口) | [G3-权限与认证规范](../../grules/G3-权限与认证规范/) + [B02-permissions/](../B02-permissions/) |

## 3. 进度速览

| Feature | C01 R | C02 I | C03 N | C04 H | C05 E |
|---------|:-:|:-:|:-:|:-:|:-:|
| course | ✓ | ✓ | ✓ | ✓ | 进行中(Round 6 展开 page-specs) |
| discover-china | ✓ | ✓ | ✓ | ✓ | 进行中 |
| app-auth | ✓ | ✓ | ✓ | ✓ | 进行中 |
| admin-auth | ✓ | ✓ | ✓ | ✓ | 进行中 |

## 4. 跨 feature 依赖

- `course` 的"学员举报"流向 `course/admin/M-report`,无外部 feature 依赖。
- `discover-china/app` 的 `/me/progress` 已废弃,**不** 再调用 `course/srs`。
- `app-auth` / `admin-auth` 是所有其它 feature 的鉴权前置;两者**不共享** session / cookie / Supabase project。

## 5. 全局术语

详见 [_glossary.md](_glossary.md)。
