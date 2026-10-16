# Catálogo de aceptación — Hotel

Escenarios propuestos; ninguno ejecutado sobre producto. Cada ID tiene namespace de feature. Para cada FR se prueba resultado autorizado, denegación, duplicación y recuperación; los datos deben ser autorizados y minimizados.

| Prueba | Requisito | Dado / Cuando / Entonces |
|---|---|---|
| AT-001 | FR-001 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Con fechas/ocupación se ofrece tarifa y política vigentes; habitación en mantenimiento o ocupada no se asigna; impuestos según política ratificada. |
| AT-002 | FR-002 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Consulta y pago web producen una única reserva vinculada al resultado confirmado del proveedor; pago fallido no confirma. |
| AT-003 | FR-003 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Una reserva directa y otra OTA actualizan inventario por el conector autorizado en ambos sentidos; medir desfase y detectar conflicto en vez de ocultarlo. |
| AT-004 | FR-004 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Pago de anticipo y saldo se concilian con documentos aplicables sin segunda emisión por el mismo hecho; SII caído queda pendiente y escala. |
| AT-005 | FR-005 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Intentos concurrentes por la última habitación permiten como máximo una confirmación local; eventos OTA tardíos se detectan y no se aceptan automáticamente sobre cupo. |
| AT-006 | FR-006 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Check-in con documento faltante queda incompleto y se deriva a recepción; acceder al documento exige rol autorizado y registro. |
| AT-007 | FR-007 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Pedido aprobado para habitación crea una comanda y un cargo con referencia/idempotencia; sin cafetería habilitada el servicio se declara no disponible sin bloquear reservas. |
| AT-008 | FR-008 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Check-out crea tarea limpieza; cierre autorizado habilita estado operativo; mantenimiento bloqueado impide asignación aunque termine limpieza. |
| AT-009 | FR-009 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Cuenta acumula cargos/anticipos y liquida saldo; reintentar cargo no duplica, ni se vuelve a documentar importe ya cubierto. |
| AT-010 | FR-010 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Huésped autenticado recibe datos de su reserva; consulta ajena se deniega. Sin permisos de mutación, la petición de cambio queda borrador y escala. |
| AT-011 | FR-011 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Acción fuera de política, monto o vigencia se deniega; modificar parámetros invalida aprobación y no produce cambio en PMS. |
| AT-012 | FR-012 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Oferta de desayuno a huésped elegible genera propuesta y link a flujo controlado, con tarifa comprobada; solo pago confirmado se contabiliza conversión. |
| AT-013 | FR-013 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Cada respuesta con herramienta o acción registra fuente, regla, identidad y resultado sin documento completo del huésped en logs. |
| AT-014 | FR-014 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Consulta externa MCP solo obtiene proyección pública vigente sin datos de huésped ni escritura; intento de modificar reserva se deniega. |
| AT-015 | FR-015 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Flujo hotelero usa core para identidad/pagos/documentos/auditoría y posee reserva/cuenta; probar sin catálogo ni gasto universal del core. |
| ADV-001 | NFR-001/002/003 | Cien intentos sobre la última habitación producen como máximo una confirmación local; el conflicto OTA se detecta y escala. |
| ADV-002 | NFR-001/002/003 | Desconectar canal y simular inventario obsoleto: detener confirmación automática sin asignación segura. |
| ADV-003 | NFR-001/002/003 | Anticipo y pago final mantienen trazabilidad fiscal sin emitir dos documentos por el mismo hecho. |

## Criterios de éxito y evidencia

| Criterio | Verificación pendiente |
|---|---|
| SC-001 | Medir «Cero sobreventas en 90 días de operación con al menos dos canales activos». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-002 | Medir «La disponibilidad se refleja en todos los canales en menos de 5 minutos en el 95 % de los cambios». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-003 | Medir «Las reservas directas pasan del nivel actual a al menos 30 % del total en 6 meses». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-004 | Medir «El 100 % de los pagos queda conciliado con su obligación documental aplicable; objetivo de entrega <60 s cuando proceda y haya disponibilidad externa, sujeto a ratificación; fallos quedan pendientes y alertados». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-005 | Medir «El 60 % de los huéspedes completa check-in online antes de llegar». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-006 | Medir «El agente resuelve al menos el 70 % de conversaciones de WhatsApp sin intervención humana». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-007 | Medir «Cero acciones del agente fuera de sus reglas de autonomía (auditoría mensual del ledger)». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-008 | Medir «Los upsells ofrecidos por el agente convierten al menos el 8 % (referencia Duve)». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-009 | Medir «Un empleado nuevo opera recepción con el sistema tras 2 horas de capacitación». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
