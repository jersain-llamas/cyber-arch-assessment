# -*- coding: utf-8 -*-
"""Carga framework.yaml (fuente de verdad) y expone las estructuras que usan
los generadores del Excel, la app web y el navegador."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
_y = yaml.safe_load((ROOT / "framework.yaml").read_text(encoding="utf-8"))

META  = _y["meta"]
SCALE = [(s["nivel"], s["etiqueta"], s["descripcion"]) for s in META["escala"]]

PILLARS, SUB, ITEMS, ORDER = {}, {}, {}, []
for p in _y["pilares"]:
    PILLARS[p["id"]] = (p["nombre"], p["nucleo"])
    for s in p["subpilares"]:
        SUB[s["ref"]]   = (s["nombre"], s["tier"], s["referencia_comparada"])
        ITEMS[s["ref"]] = list(s["items"])
        ORDER.append(s["ref"])

def summary():
    return {"pilares": len(PILLARS), "subpilares": len(SUB),
            "items": sum(len(v) for v in ITEMS.values())}
