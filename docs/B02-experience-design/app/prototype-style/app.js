/**
 * app.js — window.proto
 * 纯 vanilla JS，零依赖
 * 支持三轴切换：mode × accent × density
 */
(function () {
  'use strict';

  var STORAGE_KEY_MODE    = 'proto-mode';
  var STORAGE_KEY_ACCENT  = 'proto-accent';
  var STORAGE_KEY_DENSITY = 'proto-density';
  var html = document.documentElement;

  var VALID_MODES    = ['light', 'dark', 'auto'];
  var VALID_ACCENTS  = ['red', 'yellow', 'blue', 'green'];
  var VALID_DENSITIES = ['default', 'compact', 'elder'];

  var proto = {};

  /* ---- bootstrap ---- */
  proto.bootstrap = function () {
    var savedMode    = localStorage.getItem(STORAGE_KEY_MODE)    || 'auto';
    var savedAccent  = localStorage.getItem(STORAGE_KEY_ACCENT)  || 'red';
    var savedDensity = localStorage.getItem(STORAGE_KEY_DENSITY) || 'default';
    html.setAttribute('data-mode', savedMode);
    html.setAttribute('data-accent', savedAccent);
    html.setAttribute('data-density', savedDensity);
  };

  /* ---- switchTheme (mode) ---- */
  proto.switchTheme = function (mode) {
    if (VALID_MODES.indexOf(mode) === -1) return;
    html.setAttribute('data-mode', mode);
    localStorage.setItem(STORAGE_KEY_MODE, mode);
  };

  /* ---- switchAccent ---- */
  proto.switchAccent = function (accent) {
    if (VALID_ACCENTS.indexOf(accent) === -1) return;
    html.setAttribute('data-accent', accent);
    localStorage.setItem(STORAGE_KEY_ACCENT, accent);
  };

  /* ---- switchDensity ---- */
  proto.switchDensity = function (density) {
    if (VALID_DENSITIES.indexOf(density) === -1) return;
    html.setAttribute('data-density', density);
    localStorage.setItem(STORAGE_KEY_DENSITY, density);
  };

  /* ---- toast ---- */
  var toastContainer = null;
  var toastQueue = [];
  var MAX_TOASTS = 3;

  function ensureToastContainer() {
    if (toastContainer) return toastContainer;
    toastContainer = document.createElement('div');
    toastContainer.className = 'proto-toast-container';
    toastContainer.setAttribute('aria-live', 'polite');
    document.body.appendChild(toastContainer);
    return toastContainer;
  }

  proto.toast = function (opts) {
    var type = opts.type || 'info';
    var message = opts.message || '';
    var duration = opts.duration || (type === 'error' || type === 'warning' ? 5000 : 3000);
    var action = opts.action || null;

    var container = ensureToastContainer();
    var el = document.createElement('div');
    el.className = 'proto-toast proto-toast-' + type;
    el.setAttribute('role', type === 'error' || type === 'warning' ? 'alert' : 'status');

    var iconMap = { success: '&#10003;', error: '&#10007;', warning: '&#9888;', info: '&#8505;' };
    var html_content = '<span class="proto-toast-icon">' + (iconMap[type] || '') + '</span>';
    html_content += '<span class="proto-toast-content">' + message;
    if (action) {
      html_content += ' <button class="proto-toast-action">' + action.label + '</button>';
    }
    html_content += '</span>';
    html_content += '<button class="proto-toast-close" aria-label="close">&times;</button>';

    el.innerHTML = html_content;
    container.prepend(el);

    requestAnimationFrame(function () {
      el.setAttribute('data-open', '');
    });

    var closeBtn = el.querySelector('.proto-toast-close');
    closeBtn.addEventListener('click', function () { removeToast(el); });

    if (action) {
      var actionBtn = el.querySelector('.proto-toast-action');
      actionBtn.addEventListener('click', function () {
        action.onClick();
        removeToast(el);
      });
    }

    toastQueue.push(el);
    if (toastQueue.length > MAX_TOASTS) {
      removeToast(toastQueue[toastQueue.length - 1]);
    }

    setTimeout(function () { removeToast(el); }, duration);
  };

  function removeToast(el) {
    if (!el || !el.parentNode) return;
    el.removeAttribute('data-open');
    var idx = toastQueue.indexOf(el);
    if (idx > -1) toastQueue.splice(idx, 1);
    setTimeout(function () {
      if (el.parentNode) el.parentNode.removeChild(el);
    }, 250);
  }

  /* ---- modal ---- */
  proto.modal = function (opts) {
    var size = opts.size || 'md';
    var title = opts.title || '';
    var body = opts.body || '';
    var onConfirm = opts.onConfirm || null;
    var onCancel = opts.onCancel || null;
    var confirmLabel = opts.confirmLabel || '确认';
    var cancelLabel = opts.cancelLabel || '取消';

    var backdrop = document.createElement('div');
    backdrop.className = 'proto-backdrop';

    var modal = document.createElement('div');
    modal.className = 'proto-modal proto-modal-' + size;
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');

    modal.innerHTML =
      '<div class="proto-modal-header">' +
        '<h3>' + title + '</h3>' +
        '<button class="proto-btn-icon proto-btn-sm" aria-label="close">&times;</button>' +
      '</div>' +
      '<div class="proto-modal-body">' + body + '</div>' +
      '<div class="proto-modal-footer">' +
        '<button class="proto-btn-secondary proto-btn-md proto-modal-cancel">' + cancelLabel + '</button>' +
        '<button class="proto-btn-primary proto-btn-md proto-modal-confirm">' + confirmLabel + '</button>' +
      '</div>';

    document.body.appendChild(backdrop);
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';

    requestAnimationFrame(function () {
      backdrop.setAttribute('data-open', '');
      modal.setAttribute('data-open', '');
    });

    function close() {
      backdrop.removeAttribute('data-open');
      modal.removeAttribute('data-open');
      document.body.style.overflow = '';
      setTimeout(function () {
        if (backdrop.parentNode) backdrop.parentNode.removeChild(backdrop);
        if (modal.parentNode) modal.parentNode.removeChild(modal);
      }, 250);
    }

    var closeBtn = modal.querySelector('[aria-label="close"]');
    closeBtn.addEventListener('click', close);
    backdrop.addEventListener('click', close);

    var cancelBtn = modal.querySelector('.proto-modal-cancel');
    cancelBtn.addEventListener('click', function () {
      if (onCancel) onCancel();
      close();
    });

    var confirmBtn = modal.querySelector('.proto-modal-confirm');
    confirmBtn.addEventListener('click', function () {
      if (onConfirm) onConfirm();
      close();
    });

    modal.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });

    confirmBtn.focus();

    return { close: close };
  };

  /* ---- drawer ---- */
  proto.drawer = function (opts) {
    var direction = opts.direction || 'right';
    var body = opts.body || '';

    var backdrop = document.createElement('div');
    backdrop.className = 'proto-backdrop';

    var drawer = document.createElement('div');
    drawer.className = 'proto-drawer proto-drawer-' + direction;
    drawer.setAttribute('role', 'dialog');
    drawer.setAttribute('aria-modal', 'true');

    if (direction === 'bottom') {
      drawer.innerHTML = '<div class="proto-drawer-handle"></div>' + body;
    } else {
      drawer.innerHTML = body;
    }

    document.body.appendChild(backdrop);
    document.body.appendChild(drawer);
    document.body.style.overflow = 'hidden';

    requestAnimationFrame(function () {
      backdrop.setAttribute('data-open', '');
      drawer.setAttribute('data-open', '');
    });

    function close() {
      backdrop.removeAttribute('data-open');
      drawer.removeAttribute('data-open');
      document.body.style.overflow = '';
      setTimeout(function () {
        if (backdrop.parentNode) backdrop.parentNode.removeChild(backdrop);
        if (drawer.parentNode) drawer.parentNode.removeChild(drawer);
      }, 250);
    }

    backdrop.addEventListener('click', close);
    drawer.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });

    return { close: close };
  };

  /* ---- dropdown ---- */
  proto.dropdown = function (trigger, items) {
    var existing = trigger._protoDropdown;
    if (existing) {
      existing.close();
      return;
    }

    var rect = trigger.getBoundingClientRect();
    var dd = document.createElement('div');
    dd.className = 'proto-dropdown';
    dd.setAttribute('role', 'menu');
    dd.style.position = 'fixed';
    dd.style.top = rect.bottom + 4 + 'px';
    dd.style.left = rect.left + 'px';

    items.forEach(function (item) {
      if (item.separator) {
        var sep = document.createElement('div');
        sep.className = 'proto-dropdown-separator';
        dd.appendChild(sep);
        return;
      }
      var el = document.createElement('div');
      el.className = 'proto-dropdown-item' + (item.destructive ? ' proto-dropdown-item-destructive' : '');
      el.setAttribute('role', 'menuitem');
      el.textContent = item.label;
      el.addEventListener('click', function () {
        if (item.onClick) item.onClick();
        close();
      });
      dd.appendChild(el);
    });

    document.body.appendChild(dd);
    requestAnimationFrame(function () {
      dd.setAttribute('data-open', '');
    });

    function close() {
      dd.removeAttribute('data-open');
      trigger._protoDropdown = null;
      setTimeout(function () {
        if (dd.parentNode) dd.parentNode.removeChild(dd);
      }, 150);
    }

    function onClickOutside(e) {
      if (!dd.contains(e.target) && e.target !== trigger) {
        close();
        document.removeEventListener('click', onClickOutside);
      }
    }

    setTimeout(function () {
      document.addEventListener('click', onClickOutside);
    }, 0);

    trigger._protoDropdown = { close: close };
  };

  /* ---- ripple（Ant Design 6 风格涟漪） ---- */
  function initRipple() {
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('.proto-btn, [class*="proto-btn-"]');
      if (!btn || btn.disabled || btn.getAttribute('aria-busy') === 'true') return;
      var rect = btn.getBoundingClientRect();
      var size = Math.max(rect.width, rect.height);
      var ink = document.createElement('span');
      ink.className = 'proto-ripple-ink';
      ink.style.width = ink.style.height = size + 'px';
      ink.style.left = (e.clientX - rect.left) + 'px';
      ink.style.top = (e.clientY - rect.top) + 'px';
      btn.appendChild(ink);
      setTimeout(function () { ink.remove(); }, 450);
    });
  }
  document.addEventListener('DOMContentLoaded', initRipple);

  /* ---- sfx（音效播放） ---- */
  proto.sfxEnabled = false;
  var sfxCache = {};
  var sfxLastTime = {};

  proto.sfx = function (id, volume) {
    if (!proto.sfxEnabled) return;
    var now = Date.now();
    if (sfxLastTime[id] && now - sfxLastTime[id] < 100) return;
    sfxLastTime[id] = now;
    if (!sfxCache[id]) {
      sfxCache[id] = document.getElementById('sfx-' + id);
    }
    var el = sfxCache[id];
    if (!el) return;
    el.volume = volume || 0.5;
    el.currentTime = 0;
    el.play().catch(function () {});
  };

  /* ---- showXP（XP 飘字） ---- */
  proto.showXP = function (text, anchor) {
    var rect = anchor.getBoundingClientRect();
    var el = document.createElement('div');
    el.className = 'proto-xp-float';
    el.textContent = text;
    el.style.left = (rect.left + rect.width / 2 - 30) + 'px';
    el.style.top = (rect.top - 10) + 'px';
    document.body.appendChild(el);
    proto.sfx('xp', 0.4);
    setTimeout(function () { el.remove(); }, 950);
  };

  /* ---- starBurst（星星爆发） ---- */
  proto.starBurst = function (anchor) {
    var rect = anchor.getBoundingClientRect();
    var cx = rect.left + rect.width / 2;
    var cy = rect.top + rect.height / 2;
    var container = document.createElement('div');
    container.className = 'proto-star-burst';
    container.style.left = cx + 'px';
    container.style.top = cy + 'px';
    for (var i = 0; i < 8; i++) {
      var star = document.createElement('div');
      star.className = 'star';
      var angle = (i / 8) * 360;
      var dist = 40 + Math.random() * 30;
      var bx = Math.cos(angle * Math.PI / 180) * dist;
      var by = Math.sin(angle * Math.PI / 180) * dist + 10;
      star.style.setProperty('--burst-x', bx + 'px');
      star.style.setProperty('--burst-y', by + 'px');
      star.style.setProperty('--burst-r', (Math.random() * 360) + 'deg');
      star.style.background = i % 2 === 0 ? 'var(--color-warning-500)' : 'var(--color-brand-default)';
      star.style.borderRadius = '2px';
      container.appendChild(star);
    }
    document.body.appendChild(container);
    setTimeout(function () { container.remove(); }, 700);
  };

  /* ---- confetti（五彩纸屑） ---- */
  proto.confetti = function () {
    var colors = ['#EA4335', '#FBBC04', '#4285F4', '#34A853', '#FF6D01', '#AB47BC'];
    for (var i = 0; i < 40; i++) {
      var piece = document.createElement('div');
      piece.className = 'proto-confetti-piece';
      piece.style.left = (Math.random() * 100) + 'vw';
      piece.style.top = -(Math.random() * 20 + 10) + 'px';
      piece.style.background = colors[Math.floor(Math.random() * colors.length)];
      piece.style.setProperty('--confetti-r', (Math.random() * 720 - 360) + 'deg');
      piece.style.setProperty('--confetti-dur', (800 + Math.random() * 600) + 'ms');
      piece.style.animationDelay = (Math.random() * 200) + 'ms';
      document.body.appendChild(piece);
      (function (p) {
        setTimeout(function () { p.remove(); }, 1600);
      })(piece);
    }
  };

  /* ---- shake（抖动） ---- */
  proto.shake = function (el) {
    el.classList.add('proto-shake');
    el.addEventListener('animationend', function handler() {
      el.classList.remove('proto-shake');
      el.removeEventListener('animationend', handler);
    });
  };

  /* ---- flashCorrect / flashWrong ---- */
  proto.flashCorrect = function (el) {
    el.classList.add('proto-flash-correct');
    setTimeout(function () { el.classList.remove('proto-flash-correct'); }, 450);
  };
  proto.flashWrong = function (el) {
    el.classList.add('proto-flash-wrong');
    setTimeout(function () { el.classList.remove('proto-flash-wrong'); }, 350);
  };

  /* ---- levelComplete（关卡完成） ---- */
  proto.levelComplete = function () {
    var bg = document.createElement('div');
    bg.className = 'proto-level-complete-bg';
    document.body.appendChild(bg);
    proto.sfx('complete', 0.7);
    proto.confetti();
    setTimeout(function () { bg.remove(); }, 900);
  };

  window.proto = proto;
})();
