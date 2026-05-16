(function () {
  'use strict';
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
