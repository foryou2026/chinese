# i18n_languages

| 项 | 值 |
|----|-----|
| 关联 R-ID | R-i18n-001, R-i18n-002, R-i18n-003 |
| 业务定义 | 系统支持的语言注册表 |
| 状态机 | 无 |

## 字段

| 字段 | 类型 | 必填 | 默认值 | 唯一 | 说明(≤10字) | 校验(一句) |
|------|------|------|--------|------|-------------|-----------|
| id | uuid | 是 | gen_random_uuid() | 是 | 主键 | — |
| locale_code | text | 是 | 无 | 是 | 语言代码 | IETF BCP 47，如 zh/en/vi |
| name_zh | text | 是 | 无 | 否 | 中文名称 | 如"英语"，长度≤50 |
| name_native | text | 是 | 无 | 否 | 原生名称 | 如"English"，长度≤50 |
| language_family | text | 是 | 无 | 否 | 语系分组 | 枚举:language_family_enum |
| is_active | boolean | 是 | false | 否 | 是否启用 | — |
| is_system_default | boolean | 是 | false | 否 | 是否系统默认 | 仅 zh 为 true |
| sort_order | integer | 是 | 0 | 否 | 显示排序 | 数值越小越靠前 |
| text_direction | text | 是 | 'ltr' | 否 | 文字方向 | 枚举:text_direction_enum |

> - B01 通用字段 created_at/updated_at 按默认规则携带。
> - 种子数据约 50 条，覆盖全球主流语言。
> - is_system_default=true 的记录 is_active 不可修改为 false（应用层 + CHECK 约束）。

## 关系

| 目标表 | 基数 | 外键字段 | 删除策略 |
|--------|------|----------|----------|
| i18n_ui_translations | 1:N | locale (逻辑) | 无物理外键 |
| i18n_content_translations | 1:N | locale (逻辑) | 无物理外键 |
| i18n_audio_config | 1:N | locale (逻辑) | 无物理外键 |

## 种子数据（部分）

```sql
INSERT INTO i18n_languages (locale_code, name_zh, name_native, language_family, is_active, is_system_default, sort_order, text_direction) VALUES
('zh', '中文', '中文', 'east_asian', true, true, 1, 'ltr'),
('en', '英语', 'English', 'west_european', false, false, 2, 'ltr'),
('vi', '越南语', 'Tiếng Việt', 'southeast_asian', false, false, 3, 'ltr'),
('th', '泰语', 'ไทย', 'southeast_asian', false, false, 4, 'ltr'),
('id', '印尼语', 'Bahasa Indonesia', 'southeast_asian', false, false, 5, 'ltr'),
('ja', '日语', '日本語', 'east_asian', false, false, 6, 'ltr'),
('ko', '韩语', '한국어', 'east_asian', false, false, 7, 'ltr'),
('fr', '法语', 'Français', 'west_european', false, false, 8, 'ltr'),
('de', '德语', 'Deutsch', 'west_european', false, false, 9, 'ltr'),
('es', '西班牙语', 'Español', 'west_european', false, false, 10, 'ltr'),
('pt', '葡萄牙语', 'Português', 'west_european', false, false, 11, 'ltr'),
('ru', '俄语', 'Русский', 'east_european', false, false, 12, 'ltr'),
('ar', '阿拉伯语', 'العربية', 'middle_eastern', false, false, 13, 'rtl'),
('hi', '印地语', 'हिन्दी', 'south_asian', false, false, 14, 'ltr'),
('ms', '马来语', 'Bahasa Melayu', 'southeast_asian', false, false, 15, 'ltr'),
('fil', '菲律宾语', 'Filipino', 'southeast_asian', false, false, 16, 'ltr'),
('my', '缅甸语', 'မြန်မာ', 'southeast_asian', false, false, 17, 'ltr'),
('km', '高棉语', 'ខ្មែរ', 'southeast_asian', false, false, 18, 'ltr'),
('lo', '老挝语', 'ລາວ', 'southeast_asian', false, false, 19, 'ltr'),
('it', '意大利语', 'Italiano', 'west_european', false, false, 20, 'ltr'),
('nl', '荷兰语', 'Nederlands', 'west_european', false, false, 21, 'ltr'),
('sv', '瑞典语', 'Svenska', 'north_european', false, false, 22, 'ltr'),
('da', '丹麦语', 'Dansk', 'north_european', false, false, 23, 'ltr'),
('no', '挪威语', 'Norsk', 'north_european', false, false, 24, 'ltr'),
('fi', '芬兰语', 'Suomi', 'north_european', false, false, 25, 'ltr'),
('pl', '波兰语', 'Polski', 'east_european', false, false, 26, 'ltr'),
('cs', '捷克语', 'Čeština', 'east_european', false, false, 27, 'ltr'),
('ro', '罗马尼亚语', 'Română', 'east_european', false, false, 28, 'ltr'),
('uk', '乌克兰语', 'Українська', 'east_european', false, false, 29, 'ltr'),
('hu', '匈牙利语', 'Magyar', 'east_european', false, false, 30, 'ltr'),
('tr', '土耳其语', 'Türkçe', 'middle_eastern', false, false, 31, 'ltr'),
('he', '希伯来语', 'עברית', 'middle_eastern', false, false, 32, 'rtl'),
('fa', '波斯语', 'فارسی', 'middle_eastern', false, false, 33, 'rtl'),
('bn', '孟加拉语', 'বাংলা', 'south_asian', false, false, 34, 'ltr'),
('ur', '乌尔都语', 'اردو', 'south_asian', false, false, 35, 'rtl'),
('ta', '泰米尔语', 'தமிழ்', 'south_asian', false, false, 36, 'ltr'),
('te', '泰卢固语', 'తెలుగు', 'south_asian', false, false, 37, 'ltr'),
('mr', '马拉地语', 'मराठी', 'south_asian', false, false, 38, 'ltr'),
('sw', '斯瓦希里语', 'Kiswahili', 'african', false, false, 39, 'ltr'),
('el', '希腊语', 'Ελληνικά', 'west_european', false, false, 40, 'ltr'),
('pt-BR', '葡萄牙语(巴西)', 'Português (Brasil)', 'west_european', false, false, 41, 'ltr'),
('es-419', '西班牙语(拉美)', 'Español (Latinoamérica)', 'west_european', false, false, 42, 'ltr');
```
