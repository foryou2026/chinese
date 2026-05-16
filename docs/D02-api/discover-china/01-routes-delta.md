<!-- TARGET-PATH: docs/D02-api/discover-china/01-routes-delta.md -->

# 01 · 路由变更清单

## 新增(本期)

### 应用端 `/api/v1/china/*`

| Method | Path | OP-ID |
|--------|------|-------|
| GET | `/api/v1/china/categories` | OP-C1 |
| GET | `/api/v1/china/categories/:code/articles` | OP-C2 |
| GET | `/api/v1/china/articles/:code` | OP-C3 |
| POST | `/api/v1/china/sentences/:id/audio` | OP-C4 |
| GET | `/api/v1/china/sentences/:id/audio` | OP-AUX |
| GET | `/api/v1/china/articles/:code/audio-playlist` | OP-C5 |
| GET | `/api/v1/china/health` | OP-I2 |

### 管理端 `/admin/v1/china/*`

| Method | Path | OP-ID |
|--------|------|-------|
| GET | `/admin/v1/china/categories` | OP-A1 |
| GET | `/admin/v1/china/categories/:code/articles` | OP-A2 |
| GET | `/admin/v1/china/articles/:id` | OP-A3 |
| POST | `/admin/v1/china/articles` | OP-A4 |
| PATCH | `/admin/v1/china/articles/:id` | OP-A5 |
| POST | `/admin/v1/china/articles/:id/publish` | OP-A6 |
| POST | `/admin/v1/china/articles/:id/unpublish` | OP-A7 |
| DELETE | `/admin/v1/china/articles/:id` | OP-A8 |
| GET | `/admin/v1/china/articles/:id/sentences` | OP-A9 |
| GET | `/admin/v1/china/sentences/:id` | OP-A10 |
| POST | `/admin/v1/china/articles/:id/sentences` | OP-A11 |
| PATCH | `/admin/v1/china/sentences/:id` | OP-A12 |
| DELETE | `/admin/v1/china/sentences/:id` | OP-A13 |
| POST | `/admin/v1/china/articles/:id/sentences:reorder` | OP-A14 |
| GET | `/admin/v1/china/search` | OP-A15 |

### 内部 `/internal/v1/china/*`

| Method | Path | OP-ID |
|--------|------|-------|
| POST | `/internal/v1/china/tts/callback` | OP-I1(仅 dev / mock) |

## 下线

| Method | Path | OP-ID | 备注 |
|--------|------|-------|------|
| PUT | `/api/v1/china/articles/:code/progress` | OP-C6 | 2026-04 产品评审取消;路由不再挂载,文件保留 |
| GET | `/api/v1/china/articles/:code/progress` | OP-C7 | 同上 |

## 无变更
无。
