# Plan propuesto — Cafetería

Feature `001-cafeteria-mesas-pos` · 2026-10-16 · **BLOCKED**. Entrada: [spec.md](spec.md).

## Resumen y contexto técnico

Carta digital existente, exportaciones Eleventa, Webpay, SII y WhatsApp; muestras y credenciales no entregadas.

La base Python 3.12/FastAPI, Next.js, PostgreSQL 16 y Redis figura como propuesta en CAF §6, HOT §6 e INM §6; no hay benchmark, repositorio previo, presupuesto ni decisión aprobada. No fijar versiones ni desplegar antes de ADR-003. Claude Agent SDK también es candidato, no dependencia seleccionada. Se propone web responsive y adaptadores por proveedor; hosting, residencia, modelo LLM, colas y almacenamiento quedan pendientes. Las escalas de las fuentes son supuestos, no dimensionamiento validado.

## Constitution Check

| Principio | Resultado documental | Gate de implementación |
|---|---|---|
| Core primero | Responsabilidades separadas, ADR-001 | Validar contratos y límites |
| Chile operativo | Política tributaria y vigencia legal identificadas | Q-CORE-02 pendiente |
| Autonomía gobernada | Política de denegación y aprobación definida | Límites comerciales pendientes |
| Seguridad y privacidad | Amenazas y pruebas propuestas | Retención, roles y revisión legal pendientes |
| Pruebas verificables | acceptance.md trazable a cada FR | No se ejecutaron pruebas de producto |
| Simplicidad y medición | Sin microservicios ni stack impuestos | Costos y línea base pendientes |

No se declara cumplido un gate por haber escrito una tabla. Las ampliaciones de constitución esperan ratificación según su gobernanza.

## Diseño, dependencias y amenazas

Mesa → Pedido → Ítem; Producto → Receta → Insumo; Compra → MovimientoStock; Gasto → Evidencia. Pedido referencia pagos del core, no replica el estado bancario.

Pedido: borrador → enviado → preparado → servido; anulación exige rol y evidencia. Compra: pendiente → aprobada/rechazada. El cierre de mesa exige saldo cero y conciliación; la emisión tributaria tiene estado independiente.

Amenazas específicas: QR adulterado, acceso a otra mesa, doble imputación, OCR malicioso y fraude en anulaciones. Controles: autorización fuera del LLM, evidencia no confiable como datos, claves por tenant, acceso mínimo, deduplicación y revisión humana. Recuperación: reconciliar fuente de verdad, conservar intentos fallidos y aplicar compensación aprobada; una devolución o rectificación no es un borrado.

Consultar `../../docs/arquitectura/dependencias.md`, `seguridad.md` y ADR-001 a ADR-004. No se necesitan bases de datos compartidas entre verticales.

## Fases y estructura

Fase 0: resolver `Q-CAF-01: momento de pago y propina; Q-CAF-02: convivencia Eleventa y alcance offline; Q-CAF-03: carta, exportaciones, responsables de compras y sesión de cliente.` y registrar decisiones. Fase 1: ratificar data-model.md y contratos lógicos con ejemplos válidos/erróneos. Fase 2: concretar tareas de desarrollo, pruebas previas e integración de sandbox. Esta entrega se detiene antes de implementar.

Código futuro en `verticales/cafeteria/`; hoy solo README de alcance. Artefactos presentes: spec, research, plan, data-model, quickstart, tasks, acceptance, contracts y checklists.

## Complexity Tracking

Se reduce el core original (catálogo, gastos y analítica quedan en dominios). Se elimina la dependencia obligatoria hotel→cafetería y obra→comercial mediante interfaces opcionales. No se justifica un proceso worker, Redis ni cuatro agentes separados como necesidad comprobada; evaluar aislamiento y costo antes de introducirlos.
