#!/usr/bin/env python3
"""Genera los entregables Markdown del Paso 2 (mapa) y Paso 3 (recuento) a partir de los CSV ya producidos."""
import csv, json
from pathlib import Path
from collections import OrderedDict

BASE = Path("Análisis")
OUT2 = BASE/"kimi"
OUT3 = BASE/"kimi"
OUT3.mkdir(exist_ok=True)

def load_csv(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

caps = load_csv(OUT2/"paso2_mapa_capitulos.csv")
fichas = load_csv(OUT2/"paso2_mapa_fichas_sdd.csv")
verif = json.loads((OUT2/"paso2_verificaciones.json").read_text(encoding="utf-8"))

L = []
A = L.append
A("# Paso 2 — Mapa de contenido (entrega Kimi)\n")
A("- **Agente:** Kimi · **Fecha:** 2026-10-26")
A("- **Rol:** por instrucción del propietario (\"continuar con el análisis, colaborar con Claude, iterar\"), Kimi produce este Paso 2 y el Paso 3; **queda pendiente la revisión cruzada de Claude** (roles invertidos respecto al guion original; registrado en el tablero).")
A("- **Aclaración del propietario acogida:** no son 4 módulos ni capítulos: son **24 capítulos** y **23 fichas/paquetes SDD**.\n")
A("## Verificación de la aclaración (24, no 4)\n")
A("| Afirmación | Resultado | Fuente | Etiqueta |")
A("|---|---|---|---|")
A('| El maestro declara "24 capitulos y 23 paquetes SDD desarrollados" | Confirmado | `02_texto/Documento_Word_Especificaciones_V1.txt` línea 14 (tabla de cobertura) | HECHO DOCUMENTADO |')
A("| El Mapa del Documento Maestro lista M01–M24 (24 filas) | Confirmado | mismo archivo, líneas 40–66 | HECHO DOCUMENTADO |")
A("| Existen 24 archivos maestro/M01.md…M24.md con SHA-256 | Confirmado | `03_inventario/inventario_Especificaciones_V1.csv` líneas 38–61 | HECHO DOCUMENTADO |")
A('| Se encontró alguna afirmación de "4 capítulos/módulos" en las fuentes | **No** en maestro, inventarios ni registros revisados | búsqueda en fuentes | INFORMACIÓN NO VERIFICADA (no aparece) |')
A("| Posible origen del número 4: las 4 entregas E0–E3 del Anexo A | Plausible | mismo archivo, líneas 354–379 | HIPÓTESIS |\n")
A("## Tabla A — Capítulo → fuente → requisitos asociados (24 capítulos)\n")
A("Fuentes por fila: `maestro/MNN.md` (bytes, SHA-256 según inventario), asignación capítulo↔requisito de `registros/requisitos_originales_preservados.csv` (columna \"Capitulo maestro\"), fichas de `registros/paquetes.csv`. Verificación: 153/153 requisitos tienen capítulo válido M01–M24, sin duplicados ni anomalías.\n")
A("| Cap | Materia | Fuente (maestro) | #Req | Fichas SDD | Requisitos asociados (IDs preservados) | Etiqueta |")
A("|---|---|---|---|---|---|---|")
for r in caps:
    sha = r["sha256"][:12]
    A(f'| {r["capitulo"]} | {r["materia"]} | `{r["fuente"]}` · {r["bytes"]} B · sha {sha} | {r["n_req"]} | {r["fichas_csv"] or "—"} | {r["requisitos"] or "—"} | HECHO DOCUMENTADO |')
A("")
A("## Tabla B — Las 23 fichas/paquetes SDD\n")
A("Fuentes: `registros/paquetes.csv` (V1) y `backlog/` del SDD v0.3 extraído en `01_extraccion/Herencia_SDD_V03/`. Verificación: 23 fichas F00–F22 en ambos paquetes; suma de requisitos por paquete = 153.\n")
A("| Ficha | Nombre | Spec V1 (`specs/`) | Semilla v0.3 (`backlog/`) | Entrega | #Req | Decisiones | Estado | Etiqueta |")
A("|---|---|---|---|---|---|---|---|---|")
for r in fichas:
    A(f'| {r["ficha"]} | {r["nombre"]} | `{r["ruta_specs_v1"]}` | `{r["ficha_v03"]}` | {r["entrega"]} | {r["n_req_paquetes_csv"]} | {r["decisiones"]} | {r["estado"]} | HECHO DOCUMENTADO |')
A("")
A("## Hallazgos del mapa (Paso 2)\n")
A("1. **Cuatro capítulos sin requisitos asignados en el CSV:** M02 (fuentes/decisiones), M03 (procesos/roles), M16 (modelo de datos), M24 (plan de ejecución) tienen 0 requisitos en `registros/requisitos_originales_preservados.csv`. Son capítulos transversales; el texto de M24 referencia los 23 paquetes. Etiqueta: HECHO DOCUMENTADO (el 0 es conteo) + SUPUESTO (se asume cobertura intencional; confirmar con propietario).")
A("2. **Cruce texto del maestro vs CSV de trazabilidad:** las referencias \"F…\" explícitas en el cuerpo de cada capítulo no siempre coinciden con las fichas asignadas en el CSV. Detalle en `paso2_verificaciones.json` (`cruce_inconsistente`). El texto usa rangos (p.ej. \"F14-F17\") y menciones contextuales (p.ej. M12: \"la compra atraviesa F06\"), mientras el CSV asigna por pertenencia. Etiqueta: HECHO DOCUMENTADO; no constituye CONTRADICCIÓN (el CSV es la trazabilidad autoritativa; el texto referencia de forma selectiva).")
A("3. **IDs estables:** los 153 IDs preservados (prefijos AI, CAP, CORE, FIN, FNB, GEX, GOV, HOT, HR, INT, INV, KPI, LIN, MIG, MNT, OPS, PAY, PUR, QA, REC, RES, REV, SEC, SOC, SPA, TAX, UX) coinciden exactamente entre `requisitos_originales_preservados.csv` y `trazabilidad.csv` (diferencia = 0). Etiqueta: HECHO DOCUMENTADO.")
A("4. **Prioridades:** P0=118, P1=29, P2=6 (suma 153). Todas las filas son `REQUISITO_DE_PRODUCTO_O_CONTROL_EXISTENTE`. Etiqueta: HECHO DOCUMENTADO.\n")
A("## Qué queda sin verificar en este paso\n")
A("- Relación padre/hijo entre requisitos (columna \"Padre o relacion\") no analizada.")
A("- Fichas SDD v0.3 como specs: `backlog/` son semillas según su propio AGENTS.md; no specs aprobadas (dato, no instrucción).")
A("- Cifras de paginación del Word (CONTRADICCIÓN MENOR del Paso 1) sin resolver.")
A("- Contenido interno de los 24 archivos maestro/MNN.md (este mapa usa el Word + CSV; los MNN.md son la misma base según el maestro, línea 25).\n")
(OUT2/"paso2_mapa_contenido.md").write_text("\n".join(L), encoding="utf-8")

# ---------- Paso 3 ----------
R = []
B = R.append
B("# Paso 3 — Recuento de cifras declaradas vs contadas (entrega Kimi)\n")
B("- **Agente:** Kimi · **Fecha:** 2026-10-26 · pendiente revisión cruzada de Claude.\n")
B("| Cifra declarada | Contada | Método de conteo | Estado | Etiqueta |")
B("|---|---|---|---|---|")
B("| 153 requisitos | 153 | Filas de `registros/requisitos_originales_preservados.csv` (153); `registros/trazabilidad.csv` (mismos 153 IDs, dif 0); suma de la columna requisitos de `registros/paquetes.csv` (=153); `matrices/01_requisitos_base.csv` del SDD v0.3 (=153) | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 505 tareas | 505 | Filas de `registros/tareas.csv` | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 306 casos | 306 | Filas de `pruebas/casos_aceptacion.csv` (153 POSITIVA + 153 NEGATIVA; exactamente 2 por cada uno de los 153 requisitos; min=max=2) | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 48 escenarios críticos | 48 | Filas de `pruebas/escenarios_criticos.csv` | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 109 entidades | 109 | Valores distintos de la columna `entity` en `modelos/diccionario_datos.csv` (1 409 filas = campos, no entidades) | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 53 pantallas | 53 | Filas de `ux/pantallas.csv` | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 45 decisiones | 45 | Filas de `registros/decisiones.csv`; consistente con el maestro (\"se conserva D01-D44 y se agrega D45\", línea 88) | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 22 acoplamientos clasificados | 22 | Filas de `registros/acoplamientos_resueltos.csv` | Coincide | HECHO DOCUMENTADO (verificado) |")
B("| 1 409 campos (00_ENTREGA.md línea 15) | 1 409 | Filas de `modelos/diccionario_datos.csv` (nivel campo; las 109 entidades son valores distintos de su columna `entity`) | Coincide | HECHO DOCUMENTADO (verificado) |\n")
B("**Resultado: las 8 cifras declaradas en el maestro (líneas 13–18) coinciden con el conteo sobre los CSV extraídos; además, el \"1 409 campos\" declarado en `00_ENTREGA.md` (línea 15) coincide con las filas del diccionario.**\n")
B("## Datos complementarios del recuento\n")
B("- Prioridades: P0=118 · P1=29 · P2=6.")
B("- Niveles de caso: 292 `FUTURA_PRUEBA_DE_ACEPTACION` + 14 `DOCUMENTAL_Y_PIPELINE`.")
B("- Las 8 cifras se verificaron con `tail -n +2` (restar cabecera) y, para entidades, con valores distintos de la columna clave; no se ejecutó código de los paquetes.\n")
B("## Sin verificar todavía (para iteración)\n")
B("- Número de tareas por paquete frente a `specs/NNN-.../tasks.md` (si existe).")
B("- Escenarios críticos por funcionalidad vs el maestro.")
B("- `pruebas/gherkin/` (cantidad de features).")
B("- URLs S01–S18 (Anexo C) — requieren acceso externo; no verificadas.")
B("- Paginación 28 vs 33 del Word (CONTRADICCIÓN MENOR viva).\n")
(OUT3/"paso3_cifras.md").write_text("\n".join(R), encoding="utf-8")
print("OK:", OUT2/"paso2_mapa_contenido.md", "y", OUT3/"paso3_cifras.md")
