# Investigación de diseño — Core transversal

Estado: propuesta fundamentada parcialmente; no es decisión de compra. Base: [investigación transversal](../../docs/investigacion/estado-del-arte.md), [matriz de evidencia](../../docs/investigacion/matriz-evidencia.md).

## Contexto y alternativas

Webpay/Transbank, SII/proveedor documental y canal de comunicación mediante adaptadores, sin herramientas financieras directas al modelo.

1. Adaptar un sistema de registro existente: reduce migración y exige API, exportación, licencias y garantías de servicio verificables.
2. Construir el dominio: mayor control, pero asume costo operativo, conciliación y mantenimiento. No aprobar sin inventario real y costo total.
3. Comenzar con apoyo de lectura y borradores: menor riesgo, permite línea base; no prometer automatización de escritura hasta demostrar autorización e idempotencia.

Recomendación provisional: inventariar operación y evaluar adaptadores antes de reemplazar sistemas. No se han probado credenciales, APIs de cliente ni proveedores. Precios, ROI y ausencia de competidores de INV son declaraciones no verificadas y no justifican decisiones.

## Evidencia faltante y experimento

Q-CORE-01: empresas, roles y autorización entre empresas; Q-CORE-02: tratamiento fiscal y proveedor DTE por contribuyente; Q-CORE-03: responsables de datos, retención, recuperación, presupuesto y autonomía.

Solicitar muestra minimizada de datos y reglas aprobadas; documentar estructura, cobertura, duplicados y datos ausentes. Comparar dos alternativas con costo mensual completo, esfuerzo, recuperación y portabilidad; ejecutar luego una prueba de sandbox autorizada. Salida: ADR con evidencia, riesgos, responsable y criterios de reversión.

Las métricas y fórmulas están en `../../docs/arquitectura/economia.md`; no hay valores observados. Booking exige proceso de acceso; Airbnb publica partners pero eso no prueba acceso API; Meta no fue accesible en esta revisión. No inferir capacidad de escritura a partir de que un proveedor diga usar MCP.
