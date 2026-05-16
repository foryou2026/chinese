<!-- TARGET-PATH: docs/C05-prd/discover-china/app/05-user-journeys.md -->

# 05 · 用户旅程 · discover-china / **app**

## 5.1 主旅程

### J-app-disc-1 · 首次浏览
1. 主导航点"发现中国" → [P-001](06-page-specs/P-app-discover-china-001.md)
2. 12 类目网格展示 → 选 1 类
3. [P-002](06-page-specs/P-app-discover-china-002.md) 该类目文章列表(按发布时间倒序)
4. 选 1 篇 → [P-003](06-page-specs/P-app-discover-china-003.md) 文章详情

### J-app-disc-2 · 逐句精读
1. [P-003](06-page-specs/P-app-discover-china-003.md) → 默认显示"汉字 + 拼音 + 翻译"3 层
2. 点行播放句子 TTS(独立 MP3)
3. 切换显示模式:"仅汉字 / 加拼音 / 加翻译"
4. 切换 UI 语种 → 翻译行热更新

### J-app-disc-3 · 搜索
1. [P-001](06-page-specs/P-app-discover-china-001.md) 顶部搜索
2. 输入(中文 / 拼音 / 5 语标题)→ 实时建议
3. 选项 → 跳详情

### J-app-disc-4 · 找回上次阅读
1. 首页"最近阅读"卡片
2. 点 → [P-003](06-page-specs/P-app-discover-china-003.md) 滚到上次句子序号

## 5.2 异常旅程

| ID | 触发 | 处理 |
|----|------|------|
| J-app-disc-X1 | 文章被 unpublish | "该内容已下架"提示 + 自动返回类目 |
| J-app-disc-X2 | TTS 音频 404 | 行内显示"音频不可用",不阻断阅读 |
| J-app-disc-X3 | 搜索无结果 | 显示"试试其他关键词" + 5 个热门推荐 |
| J-app-disc-X4 | 弱网 | 文章正文优先;音频按需懒加载 |
| J-app-disc-X5 | 订阅过期 | 当日继续读已缓存文章;新文章入口提示订阅 |
