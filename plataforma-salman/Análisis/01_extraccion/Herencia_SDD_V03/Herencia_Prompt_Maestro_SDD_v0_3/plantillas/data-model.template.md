# Data Model: {{FEATURE}}
Baseline, versión de contratos, alcance y decisiones.

## Entities
Por entidad: propósito, sociedad/unidad, propietario del dato, PK, campos, tipo, precisión, null/default, validaciones, FK, indices, restricciones, fuente, clasificación, permisos, historial y retención. Identidad externa incluye proveedor/cuenta/propiedad, no solo un número.

## Relationships and State Machines
Cardinalidades, integridad referencial, estados y eventos. Transacciones que cambian varias entidades. Separar conceptos de reserva/estadía/pago/cargo/documento/banco.

## Money and Time
Precisión y redondeos aprobados, moneda, tipo de cambio, fecha de servicio/documento/registro/pago/abono; timezone. No float binario para saldos monetarios.

## Concurrency and Idempotency
Claves, expiración, detección de repetidos, conflictos, versionado y compensación. Inventario no negativo salvo excepción controlada especificada.

## Privacy and Lifecycle
Finalidad, acceso, minimización, cifrado, borrado/anonimización, trazabilidad y respaldo. Datos sintéticos para ejemplos.

## Migrations
Origen/destino, transformación, validaciones, rechazos, controles de totales, orden, rollback/compensación y prueba. No ejecutar cambios reales durante especificación.
