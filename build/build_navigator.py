# -*- coding: utf-8 -*-
"""Genera el navegador público (GitHub Pages): referencia de los 10 pilares,
59 subpilares y 177 ítems, con escala y referencias comparadas. Solo lectura."""
import html as H
from pathlib import Path
import loader as L

NCOL = ["#c9ccd1", "#d98c5f", "#e6c14b", "#7bb36b", "#2f8f57"]

SHORT = {"A": "Gobernanza y coordinación", "B": "Capacidades operativas",
         "C": "Gestión de riesgos", "D": "Infraestructuras esenciales",
         "E": "Reportes de incidentes", "F": "Productos y certificación",
         "G": "Cooperación internacional", "H": "Compras públicas y fomento",
         "I": "Transparencia y sostenibilidad", "J": "Responsabilidades y sanciones"}

LAYERS = [("Fundamento institucional", ["A", "B"]),
          ("Gestión del riesgo", ["C", "D"]),
          ("Incidentes y mercado", ["E", "F"]),
          ("Entorno, fomento y ejecución", ["G", "H", "I", "J"])]

def _wrap(s, n=20):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= n:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines[:2]

def arch_svg():
    W, x0, top = 920, 168, 70
    cardH, rowGap, cols, gap, padR = 56, 14, 4, 12, 16
    colW = (W - x0 - padR - (cols - 1) * gap) / cols
    H = top + 4 * cardH + 3 * rowGap + 16
    s = [f'<svg viewBox="0 0 {W} {int(H)}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Arquitectura de los 10 pilares">']
    s.append(f'<rect x="0" y="0" width="{W}" height="46" rx="9" fill="#152844"/>')
    s.append(f'<rect x="0" y="42" width="{W}" height="4" fill="#C8A24B"/>')
    s.append(f'<text x="20" y="29" fill="#fff" font-family="system-ui,Arial" font-size="15" font-weight="800">10 pilares · ciberseguridad ex ante</text>')
    s.append(f'<text x="{W-20}" y="29" fill="#c3d0df" font-family="system-ui,Arial" font-size="12.5" font-weight="600" text-anchor="end">arquitectura jurídica coherente</text>')
    for r, (lname, refs) in enumerate(LAYERS):
        y = top + r * (cardH + rowGap)
        cy = y + cardH / 2
        s.append(f'<rect x="0" y="{y}" width="5" height="{cardH}" rx="2" fill="#C8A24B"/>')
        ll = _wrap(lname, 18)
        ty = cy - (len(ll) - 1) * 8 + 4
        for li, t in enumerate(ll):
            s.append(f'<text x="16" y="{ty + li*15:.0f}" fill="#46586a" font-family="system-ui,Arial" font-size="12.5" font-weight="700">{t}</text>')
        for c, ref in enumerate(refs):
            x = x0 + c * (colW + gap)
            s.append(f'<rect x="{x:.0f}" y="{y}" width="{colW:.0f}" height="{cardH}" rx="9" fill="#fff" stroke="#dbe2ea"/>')
            s.append(f'<rect x="{x+9:.0f}" y="{y+(cardH-26)/2:.0f}" width="26" height="26" rx="6" fill="#152844"/>')
            s.append(f'<text x="{x+22:.0f}" y="{y+cardH/2+5:.0f}" fill="#fff" font-family="system-ui,Arial" font-size="14" font-weight="800" text-anchor="middle">{ref}</text>')
            nm = _wrap(SHORT[ref], 18)
            nty = cy - (len(nm) - 1) * 7 + 4
            for li, t in enumerate(nm):
                s.append(f'<text x="{x+44:.0f}" y="{nty + li*13:.0f}" fill="#1b2530" font-family="system-ui,Arial" font-size="11.5" font-weight="600">{t}</text>')
    s.append("</svg>")
    return '<div class="diagram">' + "".join(s) + '<div class="cap">Los 10 pilares en cuatro capas — del fundamento institucional a la ejecución. Cada pilar agrupa subpilares e ítems verificables.</div></div>'

def build(out_dir):
    m = L.summary()
    parts = []
    a = parts.append

    a(f"""<!DOCTYPE html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Arquetipo legislativo de ciberseguridad · ALC — Navegador</title>
<style>
:root{{--navy:#152844;--navy2:#1F3A5F;--gold:#C8A24B;--ink:#1b2530;--slate:#5a6b7b;--line:#dbe2ea;--bg:#eef2f6;--card:#fff;--soft:#f6f8fb}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);font-size:15px;line-height:1.5}}
h1,h2,h3{{margin:0;font-weight:700;letter-spacing:-.01em}}
a{{color:var(--navy2)}}
header{{background:var(--navy);color:#fff;border-bottom:3px solid var(--gold)}}
.top{{max-width:1140px;margin:0 auto;padding:26px 22px}}
.eyebrow{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:700}}
.top h1{{font-size:26px;margin:6px 0 4px}}
.top p{{color:#c3d0df;font-size:14px;max-width:760px;margin:0}}
.cta{{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}}
.cta a{{text-decoration:none;font-weight:600;font-size:13.5px;border-radius:8px;padding:9px 14px;border:1px solid #3a4f6c;color:#dce5ef}}
.cta a.gold{{background:var(--gold);color:#2a2410;border-color:var(--gold)}}
.cta a:hover{{filter:brightness(1.07)}}
.shell{{max-width:1140px;margin:0 auto;padding:24px 22px 70px;display:grid;grid-template-columns:200px 1fr;gap:28px}}
.idx{{position:sticky;top:14px;align-self:start}}
.idx h3{{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--slate);margin-bottom:8px}}
.idx a{{display:flex;gap:9px;align-items:center;text-decoration:none;color:var(--ink);padding:6px 7px;border-radius:8px;border-left:3px solid transparent}}
.idx a:hover{{background:#e6ecf3;border-left-color:var(--gold)}}
.idx .d{{width:22px;height:22px;border-radius:6px;background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:800;font-size:12px;flex:0 0 auto}}
.idx .n{{font-size:12.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.intro{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin-bottom:22px}}
.intro p{{margin:0 0 10px}}
.intro .lead{{font-size:15.5px}}
.diagram{{margin:16px 0 6px}}
.diagram svg{{width:100%;height:auto;display:block}}
.diagram .cap{{font-size:11.5px;color:var(--slate);text-align:center;margin-top:4px}}
.docs{{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px}}
.docs a{{font-size:13px;font-weight:600;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:7px 12px;color:var(--navy2);background:var(--soft)}}
.docs a:hover{{background:#e9eff6}}
.about{{font-size:14px;margin-top:6px}}
.legend{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;margin-top:6px}}
.legend .row{{display:flex;gap:9px;align-items:flex-start;font-size:12.5px}}
.legend .lv{{flex:0 0 24px;height:22px;border-radius:5px;display:grid;place-items:center;font-weight:800;color:#fff;font-size:12px}}
.pillar{{margin-bottom:30px;scroll-margin-top:14px}}
.ph{{display:flex;align-items:center;gap:13px;margin-bottom:4px}}
.ph .big{{width:40px;height:40px;border-radius:9px;background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:800;font-size:20px}}
.ph h2{{font-size:19px}}
.core{{color:var(--slate);font-size:13px;margin:0 0 14px 53px}}
.sub{{background:var(--card);border:1px solid var(--line);border-radius:12px;margin-bottom:12px;overflow:hidden}}
.sh{{display:flex;align-items:center;gap:11px;padding:11px 15px;background:var(--soft);border-bottom:1px solid var(--line)}}
.sh .ref{{font-weight:800;color:var(--navy);font-size:13px;background:#e7eef6;border-radius:6px;padding:3px 8px}}
.sh .nm{{font-weight:700;font-size:14.5px;flex:1}}
.tier{{font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px;text-transform:uppercase;letter-spacing:.03em}}
.tier.Núcleo{{background:#fbe3d2;color:#9a4a1c}}.tier.Intermedio{{background:#e2ebf6;color:#2c4d7a}}.tier.Avanzado{{background:#ececec;color:#555}}
.sub ul{{margin:0;padding:12px 18px 6px 34px}}
.sub li{{margin-bottom:7px;font-size:14px}}
.src{{padding:8px 15px 12px;font-size:12px;color:var(--slate)}}
.src b{{color:#46586a}}
footer{{border-top:1px solid var(--line);background:#fff}}
.foot{{max-width:1140px;margin:0 auto;padding:22px;font-size:12.5px;color:var(--slate);line-height:1.7}}
.foot b{{color:#46586a}}
@media (max-width:820px){{.shell{{grid-template-columns:1fr}}.idx{{position:static}}.idx a{{display:inline-flex;margin:2px}}}}
:focus-visible{{outline:2px solid var(--gold);outline-offset:2px}}
</style></head><body>
<header><div class="top">
 <div class="eyebrow">América Latina y el Caribe</div>
 <h1>Arquetipo legislativo de ciberseguridad</h1>
 <p>Marco común de referencia: {m['pilares']} pilares, {m['subpilares']} subpilares y {m['items']} ítems verificables para evaluar la arquitectura legal de una ley de ciberseguridad. La tesis: el reto regional es de <b>arquitectura jurídica coherente</b>, no de mera ausencia de normas.</p>
 <div class="cta">
  <a class="gold" href="autoevaluacion_ciberseguridad_ALC.html">Abrir autoevaluación interactiva</a>
  <a href="autoevaluacion_ciberseguridad_ALC.xlsx">Descargar versión Excel</a>
  <a href="https://www.eucybernet.eu/wp-content/uploads/2026/01/ciberseguridad-en-america-latina-y-el-caribe.pdf">Documento (ES)</a>
  <a href="https://www.eucybernet.eu/wp-content/uploads/2026/01/ciberseguridad-en-america-latina-y-el-caribe-eng.pdf">Document (EN)</a>
  <a href="https://github.com/jersain-llamas/cyber-arch-assessment">Repositorio</a>
 </div>
</div></header>
<div class="shell">
 <nav class="idx"><h3>Pilares</h3>""")

    for pid, (name, core) in L.PILLARS.items():
        a(f'<a href="#p{pid}"><span class="d">{pid}</span><span class="n">{H.escape(name)}</span></a>')
    a("</nav><main>")

    # intro + escala
    a('<div class="intro">')
    a('<p class="lead">Un marco común de referencia para diagnosticar y construir leyes de ciberseguridad en la región. Cada subpilar es un componente que una ley especial debería establecer; se evalúa con la escala de madurez 0–4 (el nivel del subpilar es el promedio de sus ítems).</p>')
    a(arch_svg())
    a('<p class="about"><b>¿De qué se trata?</b> La región ha avanzado en tipificar el cibercrimen y proteger datos, pero esos bloques no bastan para una gobernanza preventiva basada en riesgo. El problema es de <b>arquitectura jurídica coherente</b>, no de mera ausencia de normas. Este marco descompone esa arquitectura en 10 pilares, 59 subpilares y 177 ítems verificables, y ofrece tres herramientas para usarlos: este navegador de referencia, una autoevaluación interactiva y una versión en Excel.</p>')
    a('<div class="docs"><a href="https://www.eucybernet.eu/wp-content/uploads/2026/01/ciberseguridad-en-america-latina-y-el-caribe.pdf">📄 Documento fuente (ES)</a><a href="https://www.eucybernet.eu/wp-content/uploads/2026/01/ciberseguridad-en-america-latina-y-el-caribe-eng.pdf">📄 Source document (EN)</a></div>')
    a('<p><b>Ciberseguridad (ex ante)</b> — gestión de riesgo, continuidad y resiliencia — frente a <b>ciberdelito (ex post)</b> — persecución y sanción penal: este marco evalúa la primera, no la segunda.</p>')
    a('<div class="legend">')
    for n, lab, desc in L.SCALE:
        a(f'<div class="row"><span class="lv" style="background:{NCOL[n]}">{n}</span><div><b>{H.escape(lab)}.</b> {H.escape(desc)}</div></div>')
    a('</div>')
    a('<p style="font-size:12.5px;color:var(--slate);margin-top:12px"><b>Lectura:</b> nivel ≥ 3 = ya está en una ley especial (cobertura legal); nivel 4 = además verificable (madurez operativa).</p>')
    a('</div>')

    for pid, (name, core) in L.PILLARS.items():
        a(f'<section class="pillar" id="p{pid}"><div class="ph"><div class="big">{pid}</div><h2>{H.escape(name)}</h2></div>')
        a(f'<p class="core">{H.escape(core)}</p>')
        for ref in L.ORDER:
            if ref[0] != pid:
                continue
            sub, tier, src = L.SUB[ref]
            a(f'<div class="sub"><div class="sh"><span class="ref">{ref}</span><span class="nm">{H.escape(sub)}</span><span class="tier {tier}">{tier}</span></div>')
            a("<ul>")
            for it in L.ITEMS[ref]:
                a(f"<li>{H.escape(it)}</li>")
            a("</ul>")
            a(f'<div class="src"><b>Referencia comparada:</b> {H.escape(src)}</div></div>')
        a("</section>")
    a("</main></div>")

    a("""<footer><div class="foot">
 <p><b>Alcance.</b> Los niveles 0–3 miden la arquitectura legal; el nivel 4 añade la capa operativa verificable, como extensión.</p>
 <p><b>Tier.</b> Núcleo / Intermedio / Avanzado es una secuencia de adopción propuesta y editable, no asignada en el documento de origen.</p>
 <p><b>Referencias.</b> NIS2, DORA, CRA, CER, Cyber Solidarity Act, Convenio de Budapest, Chile (Ley 21.663) y otras se citan como anclas de redacción, no de copia literal.</p>
 <p><b>Fuente.</b> Llamas Covarrubias &amp; Moliné Rodríguez, «Ciberseguridad en América Latina y el Caribe: hacia una arquitectura legal y un marco común».</p>
 <p>Generado automáticamente desde <code>framework.yaml</code>.</p>
</div></footer></body></html>""")

    out = Path(out_dir) / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(parts), encoding="utf-8")
    return out

if __name__ == "__main__":
    print("navegador ->", build(L.ROOT / "docs"))
