"""Digest the algebra-redteam-research workflow output into compact markdown."""
import json, os, re
from collections import Counter

SRC = r"C:\Users\18084\AppData\Local\Temp\claude\C--Users-18084-algebra\2b35cea8-4076-4d4b-ba2b-ca521af8730a\tasks\w0mejk87g.output"
OUT = r"C:\Users\18084\algebra\research-output"
os.makedirs(OUT, exist_ok=True)

d = json.loads(open(SRC, encoding="utf-8").read())
r = d.get("result", d)
units = r.get("units", []) or []
cc = r.get("crossCutting", []) or []
srl = r.get("safeReferenceList", []) or []
counts = r.get("counts", {})

SEV = {"critical": 0, "major": 1, "minor": 2, "enhancement": 3}
sevkey = lambda s: SEV.get((s or "").lower(), 9)
norm = lambda s: re.sub(r"\s+", " ", (s or "").strip().lower())

def codetok(s):
    s = s or ""
    m = re.search(r"\d+\.\d+(?:\.\w+)?", s)
    if m:
        return m.group(0)
    m = re.search(r"[Ll]esson\s+\d+\.\d+", s)
    return norm(m.group(0)) if m else None

matched = unmatched = rejected_total = 0
sev_counts = Counter(); cat_counts = Counter()
overview_rows = []
fmd = ["# Confirmed red-team findings (adjudicated by adversarial verify)\n"]

for u in units:
    uid, title = u.get("id"), u.get("title")
    rt, vf = (u.get("redteam") or {}), (u.get("verify") or {})
    findings = rt.get("findings", []) or []
    verdicts = vf.get("verdicts", []) or []
    missed = vf.get("missed_findings", []) or []
    vmap, vtok = {}, {}
    for v in verdicts:
        vmap[norm(v.get("locator"))] = v
        t = codetok(v.get("locator"))
        if t:
            vtok.setdefault(t, v)
    kept, rejected = [], []
    for f in findings:
        v = vmap.get(norm(f.get("locator"))) or vtok.get(codetok(f.get("locator")))
        verdict = (v or {}).get("verdict", "unverified")
        if verdict == "rejected":
            rejected.append((f, v)); continue
        kept.append((f, v))
        if v is not None: matched += 1
        else: unmatched += 1
    rejected_total += len(rejected)
    overview_rows.append((uid, title, rt.get("overall_quality", "?"), len(kept), len(missed), len(rejected)))
    fmd.append(f"\n## {uid} — {title}  (quality: {rt.get('overall_quality','?')})")
    if rt.get("summary"):
        fmd.append(f"\n_{rt.get('summary')}_\n")
    rows = [(f, v, False) for f, v in kept] + [(m, {"verdict": "confirmed"}, True) for m in missed]
    rows.sort(key=lambda x: sevkey(x[0].get("severity")))
    for f, v, ismiss in rows:
        sev, cat = (f.get("severity") or "?"), (f.get("category") or "?")
        sev_counts[sev] += 1; cat_counts[cat] += 1
        rec = f.get("recommendation", "")
        if (v or {}).get("verdict") == "revise" and (v or {}).get("revised_recommendation"):
            rec = v["revised_recommendation"] + "  [REVISED by verifier]"
        tag = "MISSED+ " if ismiss else ""
        fmd.append(f"- **[{sev}/{cat}] {tag}{f.get('locator','?')}** — {f.get('description','')}")
        fmd.append(f"    -> {rec}")
        if f.get("citation"):
            fmd.append(f"    - cite: {f.get('citation')}")
        vd = (v or {}).get("verdict", "unverified")
        if vd not in ("confirmed", "unverified") and not ismiss:
            fmd.append(f"    - verdict: {vd}")
    if rejected:
        fmd.append(f"\n  REJECTED ({len(rejected)}):")
        for f, v in rejected:
            fmd.append(f"    - ~~[{f.get('severity','?')}/{f.get('category','?')}] {f.get('locator','?')}~~ — {(v or {}).get('reasoning','')[:200]}")

open(os.path.join(OUT, "01-findings-confirmed.md"), "w", encoding="utf-8").write("\n".join(fmd))

ov = ["# Overview\n", f"counts: {counts}\n", "| unit | quality | kept | missed+ | rejected |", "|---|---|---|---|---|"]
for uid, title, q, k, m, rj in overview_rows:
    ov.append(f"| {uid} | {q} | {k} | {m} | {rj} |")
ov += [f"\n**confirmed by severity:** {dict(sev_counts)}",
       f"\n**by category:** {dict(cat_counts)}",
       f"\n**verdict-match:** matched={matched} unmatched(no-verdict)={unmatched} rejected={rejected_total}"]
open(os.path.join(OUT, "00-overview.md"), "w", encoding="utf-8").write("\n".join(ov))

ccmd = ["# Cross-cutting research\n"]
for c in cc:
    ccmd.append(f"\n## {c.get('topic','?')}")
    for kf in (c.get("key_findings") or []):
        ccmd.append(f"- ({kf.get('confidence','?')}) {kf.get('claim','')}" + (f"  [cite: {kf.get('citation')}]" if kf.get('citation') else ""))
    if c.get("recommendations"):
        ccmd.append("  **recommendations:**")
        ccmd += [f"    - {x}" for x in c["recommendations"]]
    if c.get("sources"):
        ccmd.append("  **sources:**")
        ccmd += [f"    - {s.get('title','?')} — {s.get('url','')}" + (f" ({s.get('license_note')})" if s.get('license_note') else "") for s in c["sources"][:14]]
open(os.path.join(OUT, "02-crosscutting.md"), "w", encoding="utf-8").write("\n".join(ccmd))

order = {"gold": 0, "strong": 1, "acceptable": 2, "reject": 3}
smd = ["# Vetted safe reference list\n", f"total={len(srl)}; authority={dict(Counter((s.get('authority') or '?') for s in srl))}\n"]
cur = None
for s in sorted(srl, key=lambda s: order.get((s.get("authority") or "").lower(), 9)):
    a = (s.get("authority") or "?").lower()
    if a == "reject":
        continue
    if a != cur:
        cur = a; smd.append(f"\n## authority: {a}")
    smd.append(f"- **{s.get('title','?')}** — {s.get('publisher','')} — {s.get('url','')}")
    smd.append(f"    - covers: {', '.join((s.get('concepts_covered') or [])[:8])} | license: {s.get('license','?')} | accessible: {s.get('accessible','?')}")
open(os.path.join(OUT, "03-sources.md"), "w", encoding="utf-8").write("\n".join(smd))

print("UNITS", len(units), "CC", len(cc), "SOURCES", len(srl))
print("counts:", counts)
print("sev:", dict(sev_counts))
print("cat:", dict(cat_counts))
print("match: matched", matched, "no-verdict", unmatched, "rejected", rejected_total)
for fn in ["00-overview.md", "01-findings-confirmed.md", "02-crosscutting.md", "03-sources.md"]:
    print(fn, os.path.getsize(os.path.join(OUT, fn)), "bytes")
