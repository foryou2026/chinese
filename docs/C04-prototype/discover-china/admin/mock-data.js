window.MOCK = {
  'OP-cat-click':     function (p) { return { ok: true, data: { 类目编码: p && p.code } }; },
  'OP-search':        function (p) { return { ok: true, data: { 命中数: 0, 关键词: p && p.q } }; },
  'OP-tts-play':      function () { return { ok: true, data: { 音频: '已缓存', 时长秒: 4.2 } }; },
  'OP-fulltext-play': function () { return { ok: true, data: { 起始句号: 3, 总句数: 24 } }; },
  'OP-new':           function () { return { ok: true, data: { 文章编码: '020000000123' } }; }
};
