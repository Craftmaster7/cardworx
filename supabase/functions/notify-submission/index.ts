// Emails the Cardworx team when an agent submits a statement. Triggered by a database webhook on public.submissions insert.
import { createClient } from "npm:@supabase/supabase-js@2";
Deno.serve(async (req) => {
  const { record } = await req.json();
  const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const { data: agent } = await sb.from("profiles").select("email,full_name").eq("id", record.agent_id).single();
  const links: string[] = [];
  for (const p of record.file_paths ?? []) {
    const { data } = await sb.storage.from("statements").createSignedUrl(p, 60 * 60 * 24 * 7);
    if (data?.signedUrl) links.push(`<li><a href="${data.signedUrl}">${p.split("/").pop()}</a></li>`);
  }
  const html = `<h2>New statement submission</h2>
<p><b>Agent:</b> ${agent?.full_name ?? ""} (${agent?.email ?? ""})</p>
<p><b>Business:</b> ${record.business_name}<br><b>Contact:</b> ${record.contact_name ?? ""} ${record.phone ?? ""} ${record.email ?? ""}<br>
<b>Type:</b> ${record.business_type ?? ""}<br><b>Monthly volume:</b> ${record.monthly_volume ?? ""}<br><b>Current processor:</b> ${record.current_processor ?? ""}</p>
<p><b>Notes:</b> ${record.notes ?? ""}</p><p><b>Files (links valid 7 days):</b></p><ul>${links.join("")}</ul>`;
  const r = await fetch("https://api.resend.com/emails", { method: "POST",
    headers: { Authorization: `Bearer ${Deno.env.get("RESEND_API_KEY")}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from: Deno.env.get("NOTIFY_FROM") ?? "Cardworx Portal <onboarding@resend.dev>", to: [Deno.env.get("NOTIFY_TO")!], subject: `Statement submission: ${record.business_name}`, html }) });
  return new Response(JSON.stringify({ ok: r.ok }), { headers: { "Content-Type": "application/json" } });
});
