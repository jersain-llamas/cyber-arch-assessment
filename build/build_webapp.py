# -*- coding: utf-8 -*-
"""Genera la app web de autoevaluación (HTML autocontenido, sin red) desde el YAML."""
import json
from pathlib import Path
import loader as L

def build(out_dir):
    APP = {"meta": L.summary(),
           "scale": [{"n": n, "label": lab, "desc": d} for n, lab, d in L.SCALE],
           "pillars": []}
    for pid, (name, core) in L.PILLARS.items():
        p = {"id": pid, "name": name, "core": core, "subs": []}
        for ref in L.ORDER:
            if ref[0] != pid:
                continue
            sub, tier, src = L.SUB[ref]
            p["subs"].append({"ref": ref, "name": sub, "tier": tier,
                              "src": src, "items": L.ITEMS[ref]})
        APP["pillars"].append(p)
    tpl = (Path(__file__).resolve().parent / "webapp_template.html").read_text(encoding="utf-8")
    html = tpl.replace("__DATA__", json.dumps(APP, ensure_ascii=False))
    out = Path(out_dir) / "autoevaluacion_ciberseguridad_ALC.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out

if __name__ == "__main__":
    print("app web ->", build(L.ROOT / "dist"))
