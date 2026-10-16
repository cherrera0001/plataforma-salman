# Modelo conceptual — Constructora y control de obra

Estado: **DRAFT** dentro de feature BLOCKED. No es esquema SQL ni migración.

## Entidades y relaciones

ProyectoObra → PresupuestoVersionado → Partida → Programación; ReporteAvance → Evidencia → Inspección; Material → Movimiento; SolicitudCompra → Aprobación; Subcontrato es candidato pendiente de alcance.

Toda entidad privada incorpora identidad estable, tenant propietario, estado, versión, autor y fechas con zona UTC; presentación Chile según configuración. Relaciones internas exigen misma pertenencia. Las relaciones entre empresas requieren convenio, finalidad y permiso explícitos; pertenecer al mismo grupo no autoriza acceso. No compartir datos personales en catálogos públicos.

## Invariantes

Cada reporte conserva versión previa y autor; retrocesos se registran como rectificación aprobada. Porcentaje entre 0 y 100 con denominador definido. Avance físico, gasto y pago son distintos. Ninguna compra ni certificación técnica se ejecuta desde una transcripción sin revisión.

## Ciclos de vida y concurrencia

Reporte: recibido → extraído → revisión → aprobado/rechazado; solicitud: propuesta → aprobada/rechazada/expirada. Un cambio presupuestario no reescribe la línea base histórica.

Las transiciones críticas comprueban versión y autorización en el límite del servicio. Un resultado financiero desconocido mantiene la reserva de idempotencia mientras se consulta al proveedor. La integración debe tolerar mensajes duplicados y desordenados; verificar estado vigente antes de aplicar.

## Evidencia, privacidad y pendientes

Adjuntos separados del modelo conversacional, con tipo/tamaño permitido y acceso temporal autorizado. Bitácora con integridad verificable y datos personales minimizados; no prometer inmutabilidad absoluta ni conservación infinita. Retención y borrado legal se aplican a datos y evidencias sin destruir conciliación exigible. RPO/RTO y plazos: Q-CORE-03.

Q-OBR-01: obras propias o terceros, presupuesto y módulo previo no entregado; Q-OBR-02: unidad del avance, calendario y umbral; Q-OBR-03: aprobadores, compras, seguridad e inspecciones.
