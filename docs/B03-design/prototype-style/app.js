/* TARGET-PATH: docs/B03-design/prototype-style/app.js
 * 翻译自 docs/B03-design/design-system/05-interactions.md
 * 全局 proto.* API：bootstrap / theme / toast / modal / cooldown / devtools
 */
(function () {
  'use strict';

  // ----- FOUC theme bootstrap (runs ASAP) -----
  try {
    var savedTheme = localStorage.getItem('proto.theme');
    var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    var theme = savedTheme || (prefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
    var brand = localStorage.getItem('proto.brand');
    if (brand) document.documentElement.style.setProperty('--brand', brand);
  } catch (_) {}

  var listeners = { 'theme-change': [] };
  function emit(evt, payload) { (listeners[evt] || []).forEach(function (fn) { try { fn(payload); } catch (_) {} }); }

  var proto = {
    version: '1.0.0',

    bootstrap: function () {
      proto.mountEnvBadge();
      proto.bindThemeButtons();
      proto.bindScrollShadow();
      proto.bindShortcuts();
      proto.bindFormDemo();
      proto.devtools.mountStateSwitcher();
    },

    mountEnvBadge: function () {
      if (document.querySelector('.env-badge')) return;
      var b = document.createElement('div');
      b.className = 'env-badge';
      b.textContent = 'PROTOTYPE';
      document.body.appendChild(b);
    },

    setTheme: function (t) {
      document.documentElement.setAttribute('data-theme', t);
      try { localStorage.setItem('proto.theme', t); } catch (_) {}
      emit('theme-change', t);
    },
    toggleTheme: function () {
      var cur = document.documentElement.getAttribute('data-theme') || 'light';
      proto.setTheme(cur === 'dark' ? 'light' : 'dark');
    },
    on: function (evt, fn) { (listeners[evt] = listeners[evt] || []).push(fn); },

    bindThemeButtons: function () {
      document.querySelectorAll('[data-action="toggle-theme"]').forEach(function (el) {
        el.addEventListener('click', function (e) { e.preventDefault(); proto.toggleTheme(); });
      });
    },

    bindScrollShadow: function () {
      var nav = document.querySelector('.topnav');
      if (!nav) return;
      var sync = function () { nav.classList.toggle('is-scrolled', window.scrollY > 4); };
      window.addEventListener('scroll', sync, { passive: true });
      sync();
    },

    bindShortcuts: function () {
      document.addEventListener('keydown', function (e) {
        if (e.target.matches && e.target.matches('input,textarea,select,[contenteditable]')) return;
        if (e.key === '?') { proto.toast({ type: 'info', msg: '快捷键：?=帮助 · g h=首页 · / =搜索 · ESC=关闭' }); }
      });
    },

    bindFormDemo: function () {
      // any <form data-mock-op="OP-X"> intercepts submit and shows loading toast
      document.querySelectorAll('form[data-mock-op]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
          e.preventDefault();
          var btn = form.querySelector('button[type="submit"]');
          if (btn) btn.classList.add('is-loading');
          setTimeout(function () {
            if (btn) btn.classList.remove('is-loading');
            proto.toast({ type: 'success', msg: '原型演示：提交完成（已 mock）' });
          }, 1200);
        });
      });
    },

    toast: function (opts) {
      opts = opts || {};
      var stack = document.querySelector('.toast-stack');
      if (!stack) {
        stack = document.createElement('div');
        stack.className = 'toast-stack';
        document.body.appendChild(stack);
      }
      while (stack.children.length >= 3) stack.removeChild(stack.firstChild);
      var t = document.createElement('div');
      t.className = 'toast glass-toast toast-' + (opts.type || 'info');
      t.setAttribute('role', 'status');
      t.innerHTML = '<span class="toast-icon"></span><span class="toast-msg"></span>';
      t.querySelector('.toast-msg').textContent = opts.msg || '';
      stack.appendChild(t);
      var d = opts.duration || 3200;
      setTimeout(function () { t.style.opacity = '0'; setTimeout(function () { t.remove(); }, 200); }, d);
      return t;
    },

    cooldown: function (btn, seconds, labelTpl) {
      labelTpl = labelTpl || '{s} 秒后可重试';
      var original = btn.textContent;
      var originalCls = btn.className;
      btn.disabled = true;
      btn.classList.add('btn-cooldown');
      var remain = seconds;
      var tick = function () {
        if (remain <= 0) {
          btn.disabled = false;
          btn.className = originalCls;
          btn.textContent = original;
          return;
        }
        var m = Math.floor(remain / 60), s = remain % 60;
        var label = seconds >= 60
          ? labelTpl.replace('{s}', (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s))
          : labelTpl.replace('{s}', remain);
        btn.textContent = label;
        remain -= 1;
        setTimeout(tick, 1000);
      };
      tick();
    },

    devtools: {
      mountStateSwitcher: function () {
        // Inspect <meta name="proto:states"> for the page's available states list
        var meta = document.querySelector('meta[name="proto:states"]');
        if (!meta) return;
        var current = (document.querySelector('meta[name="proto:state"]') || {}).content || 'default';
        var pageId = (document.querySelector('meta[name="proto:page-id"]') || {}).content || '';
        var states = meta.content.split(',').map(function (s) { return s.trim(); });
        if (!states.length) return;
        var wrap = document.createElement('nav');
        wrap.className = 'proto-switcher';
        wrap.setAttribute('aria-label', '状态切换');
        states.forEach(function (s) {
          var a = document.createElement('a');
          var href;
          if (s === 'default') href = '../pages/' + pageId + '.html';
          else href = '../states/' + pageId + '.' + s + '.html';
          a.href = href;
          a.textContent = s;
          if (s === current) a.classList.add('is-current');
          wrap.appendChild(a);
        });
        document.body.appendChild(wrap);
      }
    }
  };

  window.proto = proto;
})();
