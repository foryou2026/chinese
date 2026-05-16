import { getServerSupabase } from '@zhiyu/supabase-client';
import type { Env } from '../env.ts';
import type { SupabaseClient } from '@supabase/supabase-js';

// 不缓存：避免 user-context 操作（getUser / setSession）把 JWT 写入共享 client，
// 让后续 service-role 调用降级为 authenticated。
export function sb(env: Env): SupabaseClient {
  return getServerSupabase(env.SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY);
}
