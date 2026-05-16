/* mock data, keys = OP-ID, business-language fields only (no DB column names) */
window.MOCK = {
  'OP-login':       function () { return { ok: true, data: { 用户: '小语同学', 邮箱: 'demo@example.com' } }; },
  'OP-register':    function () { return { ok: true, data: { 状态: '验证邮件已发送' } }; },
  'OP-google':      function () { return { ok: true, data: { 提供方: 'Google' } }; },
  'OP-forgot':      function () { return { ok: true, data: { 邮件: '已发送' } }; },
  'OP-reset':       function () { return { ok: true, data: { 状态: '已重置' } }; },
  'OP-resend':      function () { return { ok: true, data: { 冷却剩余秒: 60 } }; },
  'OP-change-pw':   function () { return { ok: true, data: { 状态: '已更新' } }; },
  'OP-update-profile': function () { return { ok: true, data: { 状态: '已保存' } }; },
  'OP-submit':      function () { return { ok: true }; },
  'OP-admin-login':     function () { return { ok: true, data: { 角色: 'super_admin' } }; },
  'OP-admin-forgot':    function () { return { ok: true, data: { 邮件: '已发送' } }; },
  'OP-admin-reset':     function () { return { ok: true, data: { 状态: '已重置' } }; },
  'OP-admin-change-pw': function () { return { ok: true, data: { 状态: '已更新' } }; }
};
