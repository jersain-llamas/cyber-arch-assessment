# -*- coding: utf-8 -*-
"""Regenera los tres artefactos desde framework.yaml:
  · dist/  -> Excel + app web (autoevaluación)
  · docs/  -> navegador (GitHub Pages) + copias descargables de la app y el Excel
Uso:  python build/generate_all.py
"""
import runpy, shutil
from pathlib import Path
import loader as L
import build_webapp, build_navigator

ROOT = L.ROOT
DIST = ROOT / "dist"
DOCS = ROOT / "docs"

def main():
    m = L.summary()
    print(f"Fuente: framework.yaml  ·  {m['pilares']} pilares / {m['subpilares']} subpilares / {m['items']} ítems\n")

    runpy.run_path(str(ROOT / "build" / "build_workbook.py"), run_name="__main__")
    print("  [ok] dist/autoevaluacion_ciberseguridad_ALC.xlsx")

    app = build_webapp.build(DIST)
    print(f"  [ok] {app.relative_to(ROOT)}")

    nav = build_navigator.build(DOCS)
    print(f"  [ok] {nav.relative_to(ROOT)}")

    DOCS.mkdir(parents=True, exist_ok=True)
    for f in ["autoevaluacion_ciberseguridad_ALC.html", "autoevaluacion_ciberseguridad_ALC.xlsx"]:
        shutil.copy(DIST / f, DOCS / f)
    print("  [ok] docs/ (navegador + app + Excel descargables)\n")
    print("Listo. Publica el sitio en GitHub Pages sirviendo la carpeta /docs.")

if __name__ == "__main__":
    main()
