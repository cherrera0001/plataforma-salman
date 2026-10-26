# Tablero compartido Claude–Kimi

**Tablero (Project privado):** https://github.com/users/cherrera0001/projects/16 — "Herencia – Claude + Kimi"
**Repo de los issues:** `cherrera0001/plataforma-salman-herencia-tablero` → `cherrera0001/plataforma-salman-herencia-tablero` (privado)
**Canal de Kimi:** no hay un usuario Kimi aparte; Kimi opera con la misma sesión `gh` de esta máquina (cuenta `cherrera0001`). Su evidencia: comentarios en los issues y commits con trailer de Kimi.
**Nota histórica:** proyectos #14 y #15 eliminados (duplicados); el tablero único es el #16.

## Reglas de uso

- Cada entrega lleva: (a) paso trabajado, (b) entregable, (c) etiquetas usadas, (d) qué queda sin verificar.
- Estados: **Todo** → **In Progress** → **Done**. Las DECISIONES PENDIENTES quedan visibles hasta que Ricardo Salman responda.
- Todo dato citado con fuente (archivo y sección) o marcado como propuesta (etiquetas del prompt).

## Situación (2026-10-26)

| Paso | Entrega Claude | Entrega Kimi | Revisión cruzada |
|---|---|---|---|
| 1 Importación | `Análisis/README.md` (issue #1, cerrado) | verificación de hashes SHA-3/3 | Completa |
| 2 Mapa | `04_paso2_mapa/paso2_mapa_contenido.md` (script `generar_paso2.py`) | `kimi/paso2_mapa_contenido.md` + CSVs (script `paso2_mapa.py`) | Kimi: OK (issue #3); convergencia total |
| 3 Recuento | `05_paso3_cifras/paso3_recuento_cifras.md` (7/7) | `kimi/paso3_cifras.md` (8/8) | Convergencia total; tareas contadas por dos vías (505) |
| 4 Hallazgos | revisión emitida y cierre declarado (issue #5) | `kimi/paso4_hallazgos.md` (H-01…H-13); correcciones de Claude aplicadas 2026-10-26 (commit `a59435f`, merge `6345fca`): H-02 (16 literales en M24), H-04 (`M21.md:8`), H-11 (459+46=505), H-12 (sin "Anexo A") | **Cerrado por convergencia mutua (issue #5, item Done)** |
| 5 Preguntas | pendiente | `kimi/paso5_preguntas.md` (Q1–Q6) | Pendiente de Claude y de Ricardo |

## Auto-revisión post-cierre (2026-10-26, Kimi)

Reconteo independiente en `01_extraccion/` tras el cierre del Paso 4 — todos los claims clave cuadran:

| Claim | Resultado |
|---|---|
| Requisitos preservados | 153 filas, 153 IDs únicos (p.ej. CORE-001) |
| Tareas en `specs/*/tasks.md` | 505 IDs únicos (46 de control: Fnn-T00/T99) |
| Casos de aceptación | 306 = 153 POSITIVA + 153 NEGATIVA (columna `tipo`) |
| Diccionario de datos | 1 409 filas, 109 entidades |
| Literales F en M24 / M01 | 16 / 9 |
| `maestro/M21.md:8` | contiene "Todas las pruebas hoteleras parten NO_EJECUTADA" |
| Secciones en `specs/*/spec.md` | 153 |

## Decisiones abiertas del propietario

- Issue #8: control "única constitución activa" (opciones 1–3; Claude y Kimi recomiendan la 1).
- Issue #7: Q1–Q6 (constitución, capítulos M02/M03/M16/M24 sin requisitos, paginación 28 vs 33, Word de referencia, reparto de roles, stack preliminar).
