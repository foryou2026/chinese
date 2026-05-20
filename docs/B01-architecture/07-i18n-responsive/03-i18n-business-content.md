# 业务内容多语言规范

> **阶段**：B01-A 技术架构
> **冻结状态**：已冻结

---

## 适用范围

文章标题、分类名称、课程名称、题干、知识点标题等来自数据库或 API 的内容型数据。

## 与 UI 文案的区分

| 类型 | 存储 | 读取方式 | 生命周期 |
|------|------|---------|---------|
| UI 文案（按钮、导航、提示） | `shared-i18n` TS 文件 | `t('key')` | 随代码发布 |
| 业务内容（文章标题、分类名） | 数据库 `*_i18n` JSONB 字段 | `pickI18n(map, lang)` | 随数据/内容更新 |

> 两类不可混用。UI 文案不进数据库，业务内容不进 i18n 包。

## 数据库字段规范

`*_i18n` 字段类型为 JSONB，结构：

```typescript
type I18nMap = Partial<Record<Locale, string>>;

// 示例
// title_i18n: { zh: '入门课程', en: 'Beginner Course', vi: 'Khóa học cơ bản', ... }
```

## 前端读取方式

```typescript
function pickI18n(
  map: I18nMap | undefined,
  lang: Locale,
  fallbacks: Locale[] = ['en', 'zh']
): string {
  if (!map) return '';
  const ordered = [lang, ...fallbacks.filter(l => l !== lang)];
  for (const l of ordered) {
    const v = map[l];
    if (typeof v === 'string' && v.trim()) return v;
  }
  // 任意非空值
  const any = Object.values(map).find(v => typeof v === 'string' && v.trim());
  return any ?? '';
}
```

**Fallback 优先级**：当前语言 → `en` → `zh` → 任意非空值 → 空字符串

## 使用示例

```tsx
import { pickI18n } from '../../lib/china-types';

const title = pickI18n(article.title_i18n, currentLang);
```

---

## 99. 待确认问题

无
