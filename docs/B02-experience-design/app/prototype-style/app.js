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
  var VALID_ACCENTS  = ['ink', 'cinnabar', 'jade', 'gold', 'graphite'];
  var VALID_DENSITIES = ['default', 'compact', 'elder'];

  var proto = {};

  /* ---- bootstrap ---- */
  proto.bootstrap = function () {
    var savedMode    = localStorage.getItem(STORAGE_KEY_MODE)    || 'auto';
    var savedAccent  = localStorage.getItem(STORAGE_KEY_ACCENT)  || 'ink';
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
    }, 200);
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
      }, 200);
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
      }, 200);
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

  window.proto = proto;
})();
