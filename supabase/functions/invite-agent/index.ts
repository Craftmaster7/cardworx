// Admin-only: invites a new agent by email. Called from the portal admin tab with the admin's session token.
import { createClient } from "npm:@supabase/supabase-js@2";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, content-type" };
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const auth = req.headers.get("Authorization") ?? "";
  const user = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: auth } } });
  const { data: me } = await user.from("profiles").select("role").eq("id", (await user.auth.getUser()).data.user?.id ?? "").single();
  if (me?.role !== "admin") return new Response(JSON.stringify({ error: "Admins only" }), { status: 403, headers: cors });
  const { email, full_name, role } = await req.json();
  const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { error } = await admin.auth.admin.inviteUserByEmail(email, { data: { full_name, role: role === "admin" ? "admin" : "agent" }, redirectTo: Deno.env.get("PORTAL_URL") });
  return new Response(JSON.stringify({ ok: !error, error: error?.message }), { headers: { ...cors, "Content-Type": "application/json" } });
});
