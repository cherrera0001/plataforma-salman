# Especificación — Constructora y control de obra

Feature: `004-constructora-obra`. Fecha: 2026-10-16. Estado: **BLOCKED** para implementación.
Fuente: INM §2 H3, §3 FR-010–012, SC-008 y encargo de separación 004. Todos los FR y SC son **REQUISITOS PROPUESTOS**, pendientes de ratificación. Los resultados numéricos son objetivos; no se han medido.

## Problema, actores y límites

V2; FR-010 a FR-012 y H3 heredados. Inspección, materiales, presupuesto y compras son requisitos propuestos nuevos; el supuesto módulo existente no fue entregado.

Actores: jefe de obra, inspector, encargado de materiales y administrador aprobador. Las responsabilidades de aprobación no se transfieren al modelo.

## Escenarios de usuario y pruebas

### H3 (P1) — Reportar avance y preparar compras

Valor: control verificable de la operación. Prueba independiente: ejecutar el escenario sin otra vertical, con adaptadores de prueba explícitos.

Dado un reporte con retroceso, cuando se recibe, entonces se preservan versiones y se exige revisión; una compra queda como propuesta.

### H4 (P2) — Controlar presupuesto, inspección y materiales

Valor: control verificable de la operación. Prueba independiente: ejecutar el escenario sin otra vertical, con adaptadores de prueba explícitos.

Dada recepción de materiales, cuando el responsable la valida, entonces se actualiza la partida y su evidencia sin alterar el avance físico.

## Requisitos funcionales

| ID | El sistema DEBE | Historia |
|---|---|---|
| FR-010 | Registrar avance por partida desde texto, voz y foto con fecha, ubicación cuando proceda y evidencia | H3 |
| FR-011 | Comparar avance real con programado y presupuesto bajo unidad y umbral aprobados | H3 |
| FR-012 | Preparar solicitudes de compra con cantidad, proveedor y precio de referencia para aprobación humana | H3 |
| FR-015 | Mantener versiones de presupuesto y programación por partida sin confundir costo y avance físico | H4 |
| FR-016 | Registrar inspecciones, observaciones y cierre humano con evidencia | H4 |
| FR-017 | Registrar recepción, consumo y conciliación de materiales por obra | H4 |
| FR-018 | Aplicar permisos de obra, auditoría y acceso a evidencias por empresa | H4 |

## Criterios de éxito

| ID | Objetivo propuesto |
|---|---|
| SC-008 | Avance por partida disponible el día del reporte; objetivo heredado, condicionado a revisión |
| SC-010 | Cero compras ejecutadas sin aprobación válida en pruebas adversariales |
| SC-011 | 100 % de rectificaciones conserva evidencia y autor en la batería de aceptación |

## Supuestos y decisiones pendientes

Q-OBR-01: obras propias o terceros, presupuesto y módulo previo no entregado; Q-OBR-02: unidad del avance, calendario y umbral; Q-OBR-03: aprobadores, compras, seguridad e inspecciones.

## Reglas normativas y de aceptación añadidas

- NFR-001: toda lectura, escritura, trabajo en cola y evidencia queda limitada por empresa y permiso; probar denegación entre empresas y roles.
- NFR-002: ningún agente ejecuta una acción financiera, tributaria o contractual sin control determinista y autorización vigente; escritura MCP deshabilitada inicialmente.
- NFR-003: reintentos conservan un solo efecto; estados desconocidos no se muestran como éxitos.
- NFR-004: retención, restauración y objetivos de recuperación requieren aprobación en Q-CORE-03; ninguna cifra de disponibilidad se asume acordada.
- NFR-005: medir latencia desde recepción hasta resultado confirmado, incluyendo errores, reintentos y desconexión. No declarar cumplimiento en muestras vacías.

Q-OBR-01: obras propias o terceros, presupuesto y módulo previo no entregado; Q-OBR-02: unidad del avance, calendario y umbral; Q-OBR-03: aprobadores, compras, seguridad e inspecciones.

Los escenarios tributarios y SC de emisión en 30/60 segundos se conservan como aspiración de la fuente, sujetos a aplicabilidad fiscal y disponibilidad externa. No constituyen garantía del SII. El aislamiento local no garantiza por sí solo cero sobreventa entre OTA independientes.

Ver `acceptance.md` para pruebas por requisito; `../../docs/auditorias/trazabilidad.md` para origen y equivalencias. La investigación transversal está en `../../docs/investigacion/estado-del-arte.md`.
