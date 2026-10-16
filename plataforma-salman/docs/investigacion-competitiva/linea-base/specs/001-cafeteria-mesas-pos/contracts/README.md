# Contratos lógicos propuestos — Cafetería

No hay OpenAPI ni endpoints inventados. Este documento fija obligaciones derivadas de los FR para elaborar contratos técnicos tras resolver decisiones.

## Sobre común, errores y compatibilidad

Toda operación privada lleva identidad verificada, tenant resuelto, permiso, referencia de negocio, versión de contrato y correlation-id. Una mutación incluye clave de idempotencia y versión esperada. La respuesta diferencia confirmado, pendiente y rechazado; una denegación no revela existencia de otro tenant. Diferente huella con igual clave se rechaza. Errores recuperables se distinguen de rechazo de política. Solo el servicio de negocio ejecuta, nunca el texto del modelo.

No se aceptan tenant ni aprobación autodeclarados por mensaje. La aprobación liga actor autorizado, acción, monto/moneda, huella, vigencia y uso único. Un cambio invalida la aprobación. Reintentos no repiten efectos. Cambios incompatibles requieren nueva versión y prueba de consumidores; no se publica un SLA externo no contratado.

## Operaciones derivadas

- `CAF-FR-001`: Generar un QR único por mesa que abra la carta digital existente sin instalar app. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H1. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-002`: Permitir pedidos individuales y compartidos por mesa, con edición hasta el envío a cocina. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H1. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-003`: Mostrar cada pedido en una pantalla de cocina (KDS) con mesa, hora y estado. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H1. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-004`: Cobrar por Webpay/Transbank y Mercado Pago, con división de cuenta por ítem o por partes iguales. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H1. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-005`: Emitir el documento SII aplicable según política fiscal aprobada, evitando duplicar voucher y boleta al confirmar pagos y entregarla por WhatsApp, correo o QR. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H1. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-006`: Mantener operación de caja en modo degradado sin internet y sincronizar al reconectar. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H1. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-007`: Registrar compras y gastos desde foto de factura o carga manual, con estado pendiente/aprobado. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H2. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-008`: Descontar insumos por receta en cada venta y mantener stock proyectado. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H2. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-009`: Calcular margen por producto, por día y por franja horaria, y exponerlo en un dashboard. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H2. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-010`: Importar ventas y stock que la exportación de la versión Eleventa del cliente permita recuperar, con cobertura y reconciliación documentadas. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H2. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-011`: Proponer órdenes de compra con cantidades y costo estimado, para aprobación humana por WhatsApp. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H3. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-012`: Alertar anulaciones, descuentos o mermas fuera de patrón en menos de 1 minuto. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H3. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-013`: Registrar toda acción de agente en un registro de auditoría con integridad verificable y retención aprobada con evidencia y aprobador. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia H3. Esquema exacto pendiente del modelo ratificado.
- `CAF-FR-014`: Operar sobre el core compartido (identidad, autorización, pagos, documentos y auditoría) sin duplicarlo. Entrada mínima: referencia del recurso y datos de negocio validados; salida: estado y evidencia; autorización según rol de la historia Todas. Esquema exacto pendiente del modelo ratificado.

## Gate para contrato ejecutable

Q-CAF-01: momento de pago y propina; Q-CAF-02: convivencia Eleventa y alcance offline; Q-CAF-03: carta, exportaciones, responsables de compras y sesión de cliente. Deben fijarse esquema de datos, dueño, políticas, ejemplos, errores, paginación si aplica, compatibilidad y pruebas de consumidor. No conectar APIs productivas ni emitir documentos reales para validar esta documentación.
