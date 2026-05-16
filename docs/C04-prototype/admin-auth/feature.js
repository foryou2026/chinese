/* TARGET-PATH placeholder, see vendor/proto-style/app.js for global API. */
(function () {
  'use strict';
  // 仅本 feature 的页面级 mock 调度。
  window.feature = {
    goto: function (pageId, state) {
      state = state || 'default';
      var prefix = state === 'default' ? 'pages/' : 'states/';
      var suffix = state === 'default' ? '' : ('.' + state);
      location.href = '../' + prefix + pageId + suffix + '.html';
    },
    mockApi: function (opId, params) {
      var m = (window.MOCK || {})[opId];
      return m ? m(params) : { ok: false, error: 'MOCK_NOT_FOUND', opId: opId };
    }
  };
})();
