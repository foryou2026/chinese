#!/usr/bin/env python3
"""Split choice.html into individual L3 files in choice/ directory."""
import os

SRC = '/opt/projects/zhiyu/survey/exam/choice.html'
OUT = '/opt/projects/zhiyu/survey/exam/choice'

SECTIONS = [
    # (id, l2_cn, l3_cn, l3_num, start, end)
    ('py-char2py',     '拼音',   '汉字选拼音',   1, 61, 198),
    ('py-listen2py',   '拼音',   '听音选拼音',   2, 201, 329),
    ('py-listen2tone', '拼音',   '听音辨调',     3, 332, 475),
    ('ch-py2char',     '汉字',   '拼音选汉字',   4, 493, 627),
    ('ch-def2char',    '汉字',   '释义选汉字',   5, 630, 727),
    ('ch-listen2char', '汉字',   '听音选汉字',   6, 730, 825),
    ('ch-pic2char',    '汉字',   '图片选汉字',   7, 828, 916),
    ('ch-radical2char','汉字',   '部首选汉字',   8, 919, 1024),
    ('wd-context',     '词语',   '语境选词',     9, 1042, 1140),
    ('wd-meaning',     '词语',   '词义选择',    10, 1143, 1215),
    ('wd-def2word',    '词语',   '释义选词',    11, 1218, 1294),
    ('wd-synonym',     '词语',   '同义词辨析',  12, 1297, 1389),
    ('wd-listen',      '词语',   '听音选词',    13, 1392, 1472),
    ('gr-correct',     '语法',   '选正确句',    14, 1488, 1623),
    ('gr-fill',        '语法',   '语法词填选',  15, 1626, 1700),
    ('gr-error',       '语法',   '错句辨别',    16, 1703, 1793),
    ('id-meaning',     '成语',   '成语选义',    17, 1809, 1896),
    ('id-choose',      '成语',   '含义选成语',  18, 1899, 1966),
    ('id-context',     '成语',   '语境选成语',  19, 1969, 2042),
    ('ls-word',        '听力理解','听词选义',    20, 2058, 2136),
    ('ls-sentence',    '听力理解','听句选义',    21, 2139, 2229),
    ('ls-dialog',      '听力理解','听对话答题',  22, 2232, 2323),
]

# L2 groups for index
L2_GROUPS = [
    ('拼音', [s for s in SECTIONS if s[1]=='拼音']),
    ('汉字', [s for s in SECTIONS if s[1]=='汉字']),
    ('词语', [s for s in SECTIONS if s[1]=='词语']),
    ('语法', [s for s in SECTIONS if s[1]=='语法']),
    ('成语', [s for s in SECTIONS if s[1]=='成语']),
    ('听力理解', [s for s in SECTIONS if s[1]=='听力理解']),
]

with open(SRC, 'r', encoding='utf-8') as f:
    lines = f.readlines()

STYLE = """\
<style>
.shared-tpl { background:#f6ffed; border:1px solid #b7eb8f; border-radius:6px; padding:6px 10px; font-size:11px; color:#389e0d; margin:8px 0; display:inline-flex; align-items:center; gap:4px; }
.shared-tpl::before { content:'\\267b'; }
.field-map { font-size:11px; color:rgba(0,0,0,.45); margin-top:4px; }
.field-map strong { color:var(--primary); font-weight:500; }
</style>"""

# Generate each L3 file
for sid, l2, l3, num, start, end in SECTIONS:
    # Extract inner content (skip the <div data-l3> open and </div> close)
    inner = lines[start:end-1]  # 0-indexed: start is the line AFTER <div data-l3>, end-1 skips </div>
    # Remove 4 spaces of indentation from each line
    cleaned = []
    for line in inner:
        if line.startswith('    '):
            cleaned.append(line[4:])
        else:
            cleaned.append(line)
    content = ''.join(cleaned)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>选择题 · {l2} · {l3}</title>
<link rel="stylesheet" href="../../styles.css">
{STYLE}
</head>
<body>

<div class="page-header">
  <a href="index.html" class="back-link">← 选择题 · 全部变体</a>
  <h1>#{num} {l3}</h1>
  <span class="badge solid-green">零AI</span>
  <span class="subtitle">选择题 × {l2} × {l3}</span>
</div>

<div class="content">
{content}
</div>

</body>
</html>
"""
    path = os.path.join(OUT, f'{sid}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  ✓ {sid}.html ({end-start} lines)')

# Generate index.html
index_cards = []
for l2_name, items in L2_GROUPS:
    cards = []
    for sid, l2, l3, num, start, end in items:
        cards.append(f'''    <a class="index-card" href="{sid}.html">
      <div class="title">#{num} {l3}</div>
      <div class="desc">选择题 × {l2} × {l3}</div>
    </a>''')
    index_cards.append(f'''  <h2 style="font-size:16px;margin:24px 0 12px">{l2_name} <span style="font-size:12px;color:rgba(0,0,0,.45)">({len(items)}种)</span></h2>
  <div class="index-grid">
{chr(10).join(cards)}
  </div>''')

index_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>选择题 · 6种知识类型 · 22种变体</title>
<link rel="stylesheet" href="../../styles.css">
</head>
<body>

<div class="page-header">
  <a href="../index.html" class="back-link">← 返回题型列表</a>
  <h1>选择题 (Multiple Choice)</h1>
  <span class="badge solid-green">零AI</span>
  <span class="badge blue">6种知识类型 · 22种变体</span>
</div>

<div class="content">
  <div class="callout info" style="margin-bottom:24px">
    <span class="icon">💡</span>
    <div>选择题按6种知识类型(拼音/汉字/词语/语法/成语/听力理解)细分出22种L3题目变体。点击进入查看每种变体的<strong>应用端原型</strong>和<strong>管理端配置表单</strong>。</div>
  </div>

{chr(10).join(index_cards)}
</div>

</body>
</html>
"""

with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
print(f'  ✓ index.html')
print(f'Done: {len(SECTIONS)} L3 files + index.html')
