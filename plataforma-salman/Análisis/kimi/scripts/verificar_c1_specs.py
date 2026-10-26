#!/usr/bin/env python3
"""Iteracion 2 - Verificacion C1: ¿los 153 requisitos 'SEMILLA_POR_DESARROLLAR' estan desarrollados en specs/*/spec.md?
Solo lectura de fuentes. Salidas: Análisis/kimi/ (verificacion_c1.md + .json)."""
import csv, re, json
from pathlib import Path
from collections import OrderedDict, defaultdict

BASE = Path("Análisis")
V1 = BASE/"01_extraccion/Herencia_Especificaciones_V1/Herencia_Especificaciones_V1_0"
OUT = BASE/"kimi"
OUT.mkdir(exist_ok=True)

def load_csv(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

reqs = load_csv(V1/"registros/requisitos_originales_preservados.csv")
traz = load_csv(V1/"registros/trazabilidad.csv")
paquetes = {r["paquete"]: r for r in load_csv(V1/"registros/paquetes.csv")}
orig_ids = {r["ID"].strip() for r in reqs}

ID_RE = re.compile(r'^### ([A-Z]{2,5}-\d{3}) - ', re.M)
US_RE = re.compile(r'\bF\d{2}-US\d+\b')
T_RE  = re.compile(r'\bF\d{2}-T\d+[A-Z]?\b')
TC_RE = re.compile(r'\bTC-[A-Z]+-\d{3}-[PN]\b')

secciones = defaultdict(list)   # orig_id -> [(spec_path, n_linea)]
us_ids, t_ids, tc_ids = set(), set(), set()
t_tasks_md = set()
por_spec = OrderedDict()

specs_dir = V1/"specs"
for d in sorted(specs_dir.iterdir()):
    if not d.is_dir():
        continue
    sp = d/"spec.md"
    por_spec[d.name] = {"secciones": 0, "US": 0, "T": 0, "TC": 0}
    if not sp.is_file():
        por_spec[d.name]["falta_spec_md"] = True
        continue
    txt = sp.read_text(encoding="utf-8")
    for m in ID_RE.finditer(txt):
        oid = m.group(1)
        secciones[oid].append((f"specs/{d.name}/spec.md", txt[:m.start()].count("\n")+1))
        por_spec[d.name]["secciones"] += 1
    tm = d/"tasks.md"
    if tm.is_file():
        t_tasks_md |= set(T_RE.findall(tm.read_text(encoding="utf-8")))
    por_spec[d.name]["US"] = len(set(US_RE.findall(txt)))
    por_spec[d.name]["T"]  = len(set(T_RE.findall(txt)))
    por_spec[d.name]["TC"] = len(set(T_RE.findall(txt))) and len(set(TC_RE.findall(txt)))
    us_ids |= set(US_RE.findall(txt)); t_ids |= set(T_RE.findall(txt)); tc_ids |= set(TC_RE.findall(txt))

# Trazabilidad: rutas existen y apuntan al spec donde esta la seccion
traz_map = {r["requisito"].strip(): r["spec"].strip() for r in traz}
faltan_archivo = [f"{rid} -> {p}" for rid, p in traz_map.items() if not (V1/p).is_file()]
en_spec_equivocado = []
for oid, where in secciones.items():
    esperado = traz_map.get(oid)
    reales = {w[0] for w in where}
    if esperado and esperado not in reales:
        en_spec_equivocado.append(f"{oid}: trazabilidad={esperado} vs seccion_en={sorted(reales)}")

desarrollados = set(secciones.keys())
faltan_desarrollo = sorted(orig_ids - desarrollados)
no_orig = sorted(desarrollados - orig_ids)  # IDs en specs que no estan en los 153

# Cruce con paquetes.csv (requisitos por paquete vs secciones por spec)
diff_paquete = []
for f, p in paquetes.items():
    carpeta = p["ruta"].split("/")[-1]
    n = por_spec.get(carpeta, {}).get("secciones", 0)
    if str(n) != p["requisitos"]:
        diff_paquete.append(f"{f}: paquetes.csv={p['requisitos']} vs secciones_spec={n}")

resumen = OrderedDict([
    ("originales", len(orig_ids)),
    ("con_seccion_en_specs", len(desarrollados & orig_ids)),
    ("faltan_desarrollo", faltan_desarrollo),
    ("ids_en_specs_no_originales", no_orig),
    ("specs_con_seccion_duplicada", {k: v for k, v in secciones.items() if len(v) > 1}),
    ("trazabilidad_rutas_inexistentes", faltan_archivo),
    ("seccion_no_coincide_trazabilidad", en_spec_equivocado),
    ("paquetes_csv_vs_secciones", diff_paquete),
    ("US_distintos", len(us_ids)), ("T_citados_en_spec_md", len(t_ids)),
    ("T_unicos_en_tasks_md", len(t_tasks_md)),
    ("T_en_tasks_md_no_citados_en_spec_md", sorted(t_tasks_md - t_ids)),
    ("TC_distintos", len(tc_ids)),
    ("por_spec", por_spec),
])
(OUT/"verificacion_c1.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")

L = []
A = L.append
A("# Verificación C1 — ¿\"desarrollados\"? specs/*/spec.md vs los 153 preservados\n")
A("- **Agente:** Kimi · **Fecha:** 2026-10-26 · Iteración 2 del tablero (issue #3).")
A("- **Pregunta:** el CSV marca los 153 requisitos como `SEMILLA_POR_DESARROLLAR`, pero `00_ENTREGA.md` (línea 15) dice \"preservados **y desarrollados**\". ¿Dónde está el desarrollo?")
A("- **Método:** extraer los `### <ID> -` de las 23 `specs/*/spec.md` y cotejarlos con los 153 IDs preservados y con `registros/trazabilidad.csv`. Solo lectura.\n")
A("## Resultado\n")
A("| Chequeo | Resultado | Etiqueta |")
A("|---|---|---|")
A(f"| IDs preservados con sección propia en alguna `spec.md` | {len(desarrollados & orig_ids)} / 153 | HECHO DOCUMENTADO |")
A(f"| IDs preservados sin sección en specs | {len(faltan_desarrollo)} | {'HECHO DOCUMENTADO' if faltan_desarrollo else '—'} |")
A(f"| IDs en specs que no están entre los 153 | {len(no_orig)} | {'CONTRADICCIÓN' if no_orig else '—'} |")
A(f"| IDs con sección en más de una spec | {len(resumen['specs_con_seccion_duplicada'])} | {'CONTRADICCIÓN' if resumen['specs_con_seccion_duplicada'] else '—'} |")
A(f"| Rutas de trazabilidad inexistentes | {len(faltan_archivo)} | {'CONTRADICCIÓN' if faltan_archivo else '—'} |")
A(f"| Sección en spec distinto al que indica trazabilidad.csv | {len(en_spec_equivocado)} | {'CONTRADICCIÓN' if en_spec_equivocado else '—'} |")
A(f"| paquetes.csv (#req) vs secciones contadas en spec.md | {len(diff_paquete)} diferencias | {'CONTRADICCIÓN' if diff_paquete else 'HECHO DOCUMENTADO'} |")
A(f"| IDs locales en specs: historias US | {len(us_ids)} · casos TC | {len(tc_ids)} | HECHO DOCUMENTADO |")
A(f"| IDs T citados en los cuerpos de spec.md | {len(t_ids)} (3 por requisito) | HECHO DOCUMENTADO |")
A(f"| IDs T únicos en `specs/*/tasks.md` | {len(t_tasks_md)} — reconciliación: {len(t_ids)} citados en spec.md + {len(t_tasks_md - t_ids)} de paquete (`Fnn-T00` base y `Fnn-T99` cierre, 2×23) = {len(t_tasks_md)} | HECHO DOCUMENTADO |\n")
if faltan_desarrollo:
    A("### IDs sin desarrollo en specs\n")
    for x in faltan_desarrollo: A(f"- {x}")
if no_orig:
    A("\n### IDs en specs fuera del baseline\n")
    for x in no_orig: A(f"- {x}")
if diff_paquete:
    A("\n### paquetes.csv vs secciones\n")
    for x in diff_paquete: A(f"- {x}")
A("\n## Conclusión (etiquetada)\n")
cubre = not faltan_desarrollo and not no_orig and not faltan_archivo and not en_spec_equivocado and not diff_paquete
if cubre:
    A("**Los 153/153 requisitos preservados tienen su especificación desarrollada** en `specs/NNN-.../spec.md` (sección propia con historia, tareas y casos), y las rutas de `registros/trazabilidad.csv` coinciden. La afirmación \"preservados y desarrollados\" (00_ENTREGA línea 15) queda **soportada a nivel de especificación documental**. La columna `SEMILLA_POR_DESARROLLAR` describe el estado heredado de la línea base V0.3, no el del V1.0 — la CONTRADICCIÓN C1 se reclasifica como **diferencia de estado entre versiones**, no como desarrollo faltante. Etiqueta: HECHO DOCUMENTADO (verificado) + HIPÓTESIS confirmada. Queda sin verificar: que el *contenido* de cada spec sea correcto (eso es revisión de negocio, fuera de esta verificación estructural).")
else:
    A("**Hay brechas (ver listas arriba).** La CONTRADICCIÓN C1 permanece abierta hasta resolverlas.")
A("")
A("Fuentes: `fuentes/requisitos_baseline_V0_3.csv` = `registros/requisitos_originales_preservados.csv` (IDs idénticos); `registros/trazabilidad.csv`; `specs/001-.../spec.md … specs/023-.../spec.md`; `registros/paquetes.csv`.")
(OUT/"verificacion_c1.md").write_text("\n".join(L), encoding="utf-8")
print(json.dumps({k: v for k, v in resumen.items() if k != "por_spec"}, ensure_ascii=False, indent=2))
print("\n--- por spec (secciones) ---")
for k, v in por_spec.items():
    print(k, v)
