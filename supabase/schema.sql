-- Cardworx Agent Portal schema. Applied by the GitHub Action (supabase db push).
create extension if not exists pgcrypto;

-- One row per login. Created automatically when an invited user first signs in.
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null,
  full_name text,
  role text not null default 'agent' check (role in ('agent','admin')),
  created_at timestamptz not null default now()
);

-- Emails listed here become admins automatically when they first sign in. Seeded by the deploy workflow.
create table if not exists public.admin_emails (email text primary key);
alter table public.admin_emails enable row level security;

create or replace function public.handle_new_user() returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, email, full_name, role)
  values (new.id, new.email, coalesce(new.raw_user_meta_data->>'full_name',''),
    case when exists (select 1 from public.admin_emails a where lower(a.email) = lower(new.email)) then 'admin' else coalesce(new.raw_user_meta_data->>'role','agent') end)
  on conflict (id) do nothing;
  return new;
end $$;
drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users for each row execute procedure public.handle_new_user();

create or replace function public.is_admin() returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin');
$$;

-- Pipeline: prospects an agent is working. Stage list is the source of truth for the portal UI.
create table if not exists public.prospects (
  id uuid primary key default gen_random_uuid(),
  agent_id uuid not null references public.profiles(id) on delete cascade,
  business_name text not null,
  contact_name text,
  phone text,
  email text,
  business_type text,
  monthly_volume numeric,
  stage text not null default 'Lead' check (stage in ('Lead','Statement in','Proposal','Signed','Active','Lost')),
  next_step text,
  notes text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists prospects_agent_idx on public.prospects(agent_id, stage);

-- Statement submissions (cost analysis requests). Files live in the private "statements" bucket.
create table if not exists public.submissions (
  id uuid primary key default gen_random_uuid(),
  agent_id uuid not null references public.profiles(id) on delete cascade,
  prospect_id uuid references public.prospects(id) on delete set null,
  business_name text not null,
  contact_name text,
  phone text,
  email text,
  business_type text,
  monthly_volume numeric,
  current_processor text,
  notes text,
  file_paths text[] not null default '{}',
  status text not null default 'Received' check (status in ('Received','In review','Analysis sent','Closed')),
  created_at timestamptz not null default now()
);
create index if not exists submissions_agent_idx on public.submissions(agent_id, created_at desc);

-- Resources shown to every agent. Admins manage rows; files live in the "resources" bucket or at an external url.
create table if not exists public.resources (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  category text not null default 'General',
  description text,
  file_path text,
  url text,
  sort_order int not null default 100,
  created_at timestamptz not null default now()
);

create or replace function public.touch_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;
drop trigger if exists prospects_touch on public.prospects;
create trigger prospects_touch before update on public.prospects for each row execute procedure public.touch_updated_at();

-- Row level security: agents see and edit only their own rows; admins see everything.
alter table public.profiles enable row level security;
alter table public.prospects enable row level security;
alter table public.submissions enable row level security;
alter table public.resources enable row level security;

drop policy if exists "profiles self or admin" on public.profiles;
create policy "profiles self or admin" on public.profiles for select using (id = auth.uid() or public.is_admin());
drop policy if exists "profiles self update" on public.profiles;
create policy "profiles self update" on public.profiles for update using (id = auth.uid()) with check (id = auth.uid() and role = (select role from public.profiles where id = auth.uid()));

drop policy if exists "prospects own or admin" on public.prospects;
create policy "prospects own or admin" on public.prospects for select using (agent_id = auth.uid() or public.is_admin());
drop policy if exists "prospects insert own" on public.prospects;
create policy "prospects insert own" on public.prospects for insert with check (agent_id = auth.uid());
drop policy if exists "prospects update own or admin" on public.prospects;
create policy "prospects update own or admin" on public.prospects for update using (agent_id = auth.uid() or public.is_admin());
drop policy if exists "prospects delete own" on public.prospects;
create policy "prospects delete own" on public.prospects for delete using (agent_id = auth.uid());

drop policy if exists "submissions own or admin" on public.submissions;
create policy "submissions own or admin" on public.submissions for select using (agent_id = auth.uid() or public.is_admin());
drop policy if exists "submissions insert own" on public.submissions;
create policy "submissions insert own" on public.submissions for insert with check (agent_id = auth.uid());
drop policy if exists "submissions admin update" on public.submissions;
create policy "submissions admin update" on public.submissions for update using (public.is_admin());

drop policy if exists "resources read all" on public.resources;
create policy "resources read all" on public.resources for select using (auth.uid() is not null);
drop policy if exists "resources admin write" on public.resources;
create policy "resources admin write" on public.resources for all using (public.is_admin()) with check (public.is_admin());

-- Storage: private buckets. Agents upload under their own folder; only admins can read statements.
insert into storage.buckets (id, name, public) values ('statements','statements',false) on conflict (id) do nothing;
insert into storage.buckets (id, name, public) values ('resources','resources',false) on conflict (id) do nothing;

drop policy if exists "statements upload own folder" on storage.objects;
create policy "statements upload own folder" on storage.objects for insert with check (bucket_id = 'statements' and (storage.foldername(name))[1] = auth.uid()::text);
drop policy if exists "statements read own or admin" on storage.objects;
create policy "statements read own or admin" on storage.objects for select using (bucket_id = 'statements' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin()));
drop policy if exists "resources read signed in" on storage.objects;
create policy "resources read signed in" on storage.objects for select using (bucket_id = 'resources' and auth.uid() is not null);
drop policy if exists "resources admin write" on storage.objects;
create policy "resources admin write" on storage.objects for all using (bucket_id = 'resources' and public.is_admin()) with check (bucket_id = 'resources' and public.is_admin());

-- Email notification: call the notify-submission function on every new submission. :'REF' is passed in by the deploy workflow.
create extension if not exists pg_net;
drop trigger if exists submissions_notify on public.submissions;
create trigger submissions_notify after insert on public.submissions for each row
  execute function supabase_functions.http_request('https://' || :'REF' || '.supabase.co/functions/v1/notify-submission', 'POST', '{"Content-Type":"application/json"}', '{}', '5000');
