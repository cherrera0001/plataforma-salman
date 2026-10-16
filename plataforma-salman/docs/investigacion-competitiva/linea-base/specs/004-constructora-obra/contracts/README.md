# Contratos lógicos propuestos — Constructora y control de obra

No hay OpenAPI ni endpoints inventados. Este documento fija obligaciones derivadas de los FR para elaborar contratos técnicos tras resolver decisiones.

## Sobre común, errores y compatibilidad

Toda operación privada lleva identidad verificada, tenant resuelto, permiso, referencia de negocio, versión de contrato y correlation-id. Una mutación incluye clave de idempotencia y versión esperada. La respuesta diferencia confirmado, pendiente y rechazado; una denegación no revela existencia de otro tenant. Diferente huella con igual clave se rechaza. Errores recuperables se distinguen de rechazo de política. Solo el servicio de negocio ejecuta, nunca el texto del modelo.

No se aceptan tenant ni aprobación autodeclarados por mensaje. La aprobación liga actor autorizado, acción, monto/moneda, huella, vigencia y uso único. Un cambio invalida la aprobación. Reintentos no repiten efectos. Cambios incompatibles requieren nueva versión y prueba de consumidores; no se publica un SLA externo no contratado.

## Operaciones derivadas

- `OBR-FR-010`: Registrar avance por partida desde texto, voz y foto con fecha, ubicación cuando proceda y evidencia. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H3. Esquema exacto pendiente del modelo ratificado.
- `OBR-FR-011`: Comparar avance real con programado y presupuesto bajo unidad y umbral aprobados. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H3. Esquema exacto pendiente del modelo ratificado.
- `OBR-FR-012`: Preparar solicitudes de compra con cantidad, proveedor y precio de referencia para aprobación humana. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H3. Esquema exacto pendiente del modelo ratificado.
- `OBR-FR-015`: Mantener versiones de presupuesto y programación por partida sin confundir costo y avance físico. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H4. Esquema exacto pendiente del modelo ratificado.
- `OBR-FR-016`: Registrar inspecciones, observaciones y cierre humano con evidencia. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H4. Esquema exacto pendiente del modelo ratificado.
- `OBR-FR-017`: Registrar recepción, consumo y conciliación de materiales por obra. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H4. Esquema exacto pendiente del modelo ratificado.
- `OBR-FR-018`: Aplicar permisos de obra, auditoría y acceso a evidencias por empresa. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H4. Esquema exacto pendiente del modelo ratificado.

## Gate para contrato ejecutable

Q-OBR-01: obras propias o terceros, presupuesto y módulo previo no entregado; Q-OBR-02: unidad del avance, calendario y umbral; Q-OBR-03: aprobadores, compras, seguridad e inspecciones. Deben fijarse esquema de datos, dueño, políticas, ejemplos, errores, paginación si aplica, compatibilidad y pruebas de consumidor. No conectar APIs productivas ni emitir documentos reales para validar esta documentación.
