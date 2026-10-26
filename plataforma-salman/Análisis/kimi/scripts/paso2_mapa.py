#!/usr/bin/env python3
"""Paso 2 - Mapa de contenido. Solo lectura sobre fuentes; escribe salidas en Análisis/04_paso2_mapa/."""
import csv, re, json
from pathlib import Path
from collections import defaultdict, OrderedDict

BASE = Path("Análisis")
V1 = BASE/"01_extraccion/Herencia_Especificaciones_V1/Herencia_Especificaciones_V1_0"
SDD = BASE/"01_extraccion/Herencia_SDD_V03/Herencia_Prompt_Maestro_SDD_v0_3"
REG = V1/"registros"
OUT = BASE/"kimi"
OUT.mkdir(exist_ok=True)

def load_csv(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

reqs = load_csv(REG/"requisitos_originales_preservados.csv")
paquetes = {r["paquete"]: r for r in load_csv(REG/"paquetes.csv")}
traz = load_csv(REG/"trazabilidad.csv")

# Inventario V1: ruta -> (bytes, sha)
inv = {}
with open(BASE/"03_inventario/inventario_Especificaciones_V1.csv", encoding="utf-8-sig") as f:
    for row in csv.reader(f):
        if len(row) >= 3 and row[0] != "ruta":
            inv[row[0]] = (row[1], row[2])

master = (BASE/"02_texto/Documento_Word_Especificaciones_V1.txt").read_text(encoding="utf-8")

# Mapa del documento: materia por capitulo
materia = dict(re.findall(r'\| (M\d{2}) \| ([^|]+) \|', master))
# Cuerpo por capitulo
parts = re.split(r'\n# (M\d{2})\. [^\n]*\n', master)
body = {parts[i]: parts[i+1] for i in range(1, len(parts)-1, 2)}
def expand_f(txt):
    """Expande rangos F02-F13 y captura menciones sueltas FNN."""
    out = set()
    for m in re.finditer(r'\bF(\d{2})-F(\d{2})\b', txt):
        a, b = int(m.group(1)), int(m.group(2))
        out.update(f"F{i:02d}" for i in range(a, b + 1))
    tmp = re.sub(r'\bF\d{2}-F\d{2}\b', ' ', txt)
    out.update(re.findall(r'\bF\d{2}\b', tmp))
    return sorted(out)

# Referencias F en el texto de cada capitulo (con rangos expandidos)
f_texto = {m: expand_f(body.get(m, "")) for m in materia}

# Requisitos por capitulo segun CSV
por_cap = defaultdict(list)
anomalias = []
for r in reqs:
    cap = (r.get("Capitulo maestro") or "").strip()
    rid = r["ID"].strip()
    if not cap or not re.fullmatch(r'M\d{2}', cap):
        anomalias.append(f"Capitulo maestro anomalo en {rid}: '{cap}'")
    por_cap[cap].append(rid)

orden = [f"M{i:02d}" for i in range(1, 25)]

# Verificaciones
total = sum(len(v) for v in por_cap.values())
id_dup = len(reqs) - len({r["ID"] for r in reqs})
faltan_hash = [m for m in orden if f"Herencia_Especificaciones_V1_0/maestro/{m}.md" not in inv]
caps_csv = sorted(por_cap.keys())

# Cruce por capitulo
filas = []
for m in orden:
    rs = por_cap.get(m, [])
    f_csv = sorted({ (r.get("Paquete SDD propuesto") or "").strip() for r in reqs if (r.get("Capitulo maestro") or "").strip() == m and (r.get("Paquete SDD propuesto") or "").strip() })
    ft = f_texto.get(m, [])
    cross = sorted(set(ft) - set(f_csv))
    faltan_texto = sorted(set(f_csv) - set(ft))
    dec = []
    for f in f_csv:
        dec += [d for d in (paquetes.get(f, {}).get("decisiones") or "").split(";") if d]
    ruta = f"Herencia_Especificaciones_V1_0/maestro/{m}.md"
    size, sha = inv.get(ruta, ("?", "?"))
    filas.append(OrderedDict([
        ("capitulo", m),
        ("materia", materia.get(m, "?").strip()),
        ("fuente", f"maestro/{m}.md"),
        ("bytes", size),
        ("sha256", sha),
        ("fichas_csv", ";".join(f_csv)),
        ("fichas_texto", ";".join(ft)),
        ("fichas_cruce", "OK" if not cross and not faltan_texto else f"extra_en_texto={','.join(cross) or '-'};solo_en_csv={','.join(faltan_texto) or '-'}"),
        ("n_req", len(rs)),
        ("requisitos", ";".join(rs)),
        ("decisiones", ";".join(sorted(set(dec)))),
    ]))

# Fichas SDD (23)
fichas = []
backlog = sorted(p.name for p in (SDD/"backlog").iterdir() if p.is_dir())
for f in sorted(paquetes):
    p = paquetes[f]
    fichas.append(OrderedDict([
        ("ficha", f),
        ("nombre", p["nombre"]),
        ("ruta_specs_v1", p["ruta"]),
        ("ficha_v03", next((b for b in backlog if b.startswith(f + "_")), "")),
        ("entrega", p["entrega"]),
        ("n_req_paquetes_csv", p["requisitos"]),
        ("decisiones", p["decisiones"]),
        ("estado", p["estado"]),
    ]))

# Trazabilidad vs originales: mismos IDs?
set_traz = {r["requisito"].strip() for r in traz}
set_orig = {r["ID"].strip() for r in reqs}
traz_diff = (set_traz ^ set_orig)

# SDD v0.3: requisitos base
base03 = load_csv(SDD/"matrices/01_requisitos_base.csv")

# Escrituras
with open(OUT/"paso2_mapa_capitulos.csv", "w", encoding="utf-8", newline="") as fo:
    w = csv.DictWriter(fo, fieldnames=list(filas[0].keys()))
    w.writeheader(); w.writerows(filas)
with open(OUT/"paso2_mapa_fichas_sdd.csv", "w", encoding="utf-8", newline="") as fo:
    w = csv.DictWriter(fo, fieldnames=list(fichas[0].keys()))
    w.writeheader(); w.writerows(fichas)

resumen = OrderedDict([
    ("capitulos_en_mapa", len(materia)),
    ("capitulos_csv_distintos", caps_csv),
    ("capitulos_sin_archivo_en_inventario", faltan_hash),
    ("total_requisitos_csv", total),
    ("filas_requisitos_csv", len(reqs)),
    ("ids_duplicados", id_dup),
    ("anomalias", anomalias),
    ("fichas_paquetes_csv", len(paquetes)),
    ("fichas_backlog_v03", len(backlog)),
    ("diferencia_trazabilidad_vs_originales", sorted(traz_diff)),
    ("req_base_v03", len(base03)),
    ("suma_requisitos_paquetes_csv", sum(int(p["requisitos"]) for p in paquetes.values())),
    ("cruce_inconsistente", {f["capitulo"]: f["fichas_cruce"] for f in filas if f["fichas_cruce"] != "OK"}),
])
(OUT/"paso2_verificaciones.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(resumen, ensure_ascii=False, indent=2))
print("\n--- por capitulo ---")
for f in filas:
    print(f["capitulo"], f["n_req"], f["fichas_csv"], "| texto:", f["fichas_texto"])
