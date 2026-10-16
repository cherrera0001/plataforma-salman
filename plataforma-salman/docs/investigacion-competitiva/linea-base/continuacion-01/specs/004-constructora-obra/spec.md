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

Las obligaciones fiscales y de recuperación se aplican solo a los efectos pertinentes del dominio; no se atribuyen reservas OTA ni latencias SII al control de obra.

Ver `acceptance.md` para pruebas por requisito; `../../docs/auditorias/trazabilidad.md` para origen y equivalencias. La investigación transversal está en `../../docs/investigacion/estado-del-arte.md`.


## Refinamiento competitivo de historias — 2026-10-16

Estado **PROPUESTO**, sin ratificación del cliente. Las siguientes definiciones amplían las historias originales con alias US, sin eliminarlas. Ante un caso específico se aplica la regla más explícita de esta sección; ninguna cambia los bloqueos comerciales. Evidencia por ID en `../../docs/investigacion-competitiva/matriz-evidencias.md`.

### Historia US-OBR-003 — enriquecimiento de H3 (P1)

Como jefe de obra y administrador de compras, quiero convertir reportes y necesidades en borradores revisables por partida, para hacer visibles desvíos y solicitudes sin inventar avance ni comprar automáticamente.

**Identidad y estado:** alias de `004-constructora-obra/H3`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Convertir reportes y necesidades en borradores revisables por partida. Responde a hacer visibles desvíos y solicitudes sin inventar avance ni comprar automáticamente; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** O03, O05, O07, O08 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-010,FR-011,FR-012,FR-015,FR-020 y NFR-001/002/003/006.

**Disparador:** el jefe envía reporte de avance o necesidad de materiales por texto, voz, foto o entrada manual.

**Precondiciones:** presupuesto/programación versionados, partidas/unidades y aprobadores; catálogo proveedor vigente si existe.

**Flujo principal:** Capturar texto/foto/voz → conservar fuente → extraer partida/cantidad/unidad → marcar inciertos → revisar → consolidar reporte aprobado → calcular desvío → preparar solicitud con precio/convenio como evidencia.

**Flujos alternativos y casos borde:** IA no disponible o deshabilitada: entrada manual equivalente. Unidad/proveedor ambiguo: revisión; convenio vencido no autoriza precio. Retroceso exige rectificación conservada.

**Reglas de negocio y validaciones:** Extracción no aprobación; imagen no certificación. Compra autorizada se vincula a versión de líneas; cualquier cambio requiere nueva revisión. Umbral relativo/puntos sigue Q-OBR-02.

**Datos y estados involucrados:** Reporte, evidencia/fecha/ubicación sugerida, campoExtraído/confianza, partida/versión, cantidad/unidad, referenciaPrecio y aprobación. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](../../docs/investigacion-competitiva/agentes.md) y [seguridad compartida](../../docs/arquitectura/seguridad.md). Fallar cerrado si faltan evidencia, permiso o conectividad.

**Dependencias:** 000, presupuesto/programación/roles según Q-OBR-01/02/03; correspondencia con proyecto comercial opcional. No exige un módulo previo no entregado.

**Riesgos:** Error de transcripción, evidencia falsificada, orden indebida y ubicación sensible.

**Criterios de aceptación Given/When/Then:**

- AC-US-OBR-003-01: Dada nota que dice comprar e incluye instrucciones, cuando se procesa, entonces solo crea borrador con campos pendientes y no envía orden.
- AC-US-OBR-003-02: Dada IA desactivada, cuando se informa avance manualmente, entonces el reporte sigue disponible y conserva autor/evidencia con mismas validaciones.

**Métricas de éxito:** Campos correctos/campos revisados; reportes aprobados; minutos de revisión; costo/reporte y compras no autorizadas. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-OBR-004 — enriquecimiento de H4 (P2)

Como inspector y encargado de materiales, quiero registrar observaciones y recepciones contra evidencia y permisos, para cerrar fallas verificadas y conciliar materiales sin confundirlos con avance.

**Identidad y estado:** alias de `004-constructora-obra/H4`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Registrar observaciones y recepciones contra evidencia y permisos. Responde a cerrar fallas verificadas y conciliar materiales sin confundirlos con avance; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** O01, O02, O06, O09 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-015,FR-016,FR-017,FR-018,FR-019,FR-020 y NFR-001/002/003/006.

**Disparador:** un inspector registra ítem fallido, se propone su solución o bodega recibe material contra una orden.

**Precondiciones:** plantilla/partidas vigentes, unidades, roles de inspector/solucionador y política de recepción.

**Flujo principal:** Registrar inspección → detectar falla → abrir observación vinculada → asignar responsable/plazo → adjuntar solución → validar cierre; por separado registrar recepción parcial → comparar con compra aprobada → conciliar diferencia.

**Flujos alternativos y casos borde:** Solucionador sin permiso de cierre propone resuelto; inspector valida o reabre. Material sobrante/dañado queda en discrepancia; reintento de recepción no duplica.

**Reglas de negocio y validaciones:** Estado resuelto propuesto no equivale a cerrado aceptado. Recibir no consume; consumo no certifica avance. Sensor y reporte manual tienen procedencias distintas.

**Datos y estados involucrados:** Inspección/ítem, Observación, vínculo/origen, asignado, evidenciaSolución, revisor, recepción/línea, orden y discrepancia. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](../../docs/investigacion-competitiva/agentes.md) y [seguridad compartida](../../docs/arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000, presupuesto/programación/roles según Q-OBR-01/02/03; correspondencia con proyecto comercial opcional. No exige un módulo previo no entregado.

**Riesgos:** Cierre sin validación, cantidades duplicadas, unidad incompatible y falsa seguridad estructural.

**Criterios de aceptación Given/When/Then:**

- AC-US-OBR-004-01: Dado ítem de inspección fallido, cuando se crea observación, entonces conserva vínculo, responsable y estado; el reportante sin permiso no puede cerrarla.
- AC-US-OBR-004-02: Dada orden de 10 unidades y recepción de 6, cuando se confirma, entonces quedan 4 pendientes; repetir mismo evento no recibe 12.

**Métricas de éxito:** Observaciones con evidencia/cerradas; reaperturas; recepción conciliada/recibida; discrepancias abiertas por antigüedad. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


## Requisitos derivados de investigación competitiva

Son propuestas de comportamiento propio, sin atribuirlo como implementación observada del competidor.

| ID | El sistema DEBE | Historia |
|---|---|---|
| FR-019 | Vincular observación con ítem/evidencia de inspección, responsable y plazo; separar solución propuesta de cierre autorizado y conservar reaperturas | H4 |
| FR-020 | Mantener solicitudes y recepciones por línea, cantidad/unidad, referencia de precio/convenio y versión aprobada; admitir recepción parcial y discrepancias sin duplicar movimientos ni ejecutar compra desde extracción | H3/H4 |

- NFR-006: toda oferta, extracción o decisión derivada declara procedencia, vigencia e incertidumbre; si no hay evidencia suficiente, no genera compromiso automático ni se informa como éxito. La captura manual conserva permisos, trazabilidad e idempotencia equivalentes.
