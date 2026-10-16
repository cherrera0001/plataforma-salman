# Análisis funcional — hotel

Reconstrucción desde documentación pública; ninguna secuencia fue ejecutada en UI/REA. Cada regla propia se propone para el proyecto; no se atribuye al proveedor. Consulte matriz-evidencias para observación documental y límites.

## US-HOT-001 / H1

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | huésped y recepcionista |
| Objetivo | reservar una categoría disponible con cotización y estado de sincronización explícitos |
| Evento inicial | el visitante indica fechas y ocupación y solicita cotización o confirmación de reserva |
| Precondiciones | sistema de registro y conectores autorizados; política tarifa/cancelación/anticipo; antigüedad máxima ratificada |
| Pasos | Consultar fechas/ocupación → mostrar oferta vigente → revalidar cupo/precio → retener según política → iniciar pago → confirmar una vez → registrar propagación por canal. |
| Datos | OfertaVersionada, TipoHabitación, cupo por fecha, retención, Reserva, referencia externa y estado por canal. |
| Reglas | Unidad de inventario por fecha/tipo no es habitación física asignada. No habilitar sobreventa por opción de proveedor. No usar respuesta desactualizada para afirmar sincronizado. |
| Validaciones | Unidad de inventario por fecha/tipo no es habitación física asignada. No habilitar sobreventa por opción de proveedor. No usar respuesta desactualizada para afirmar sincronizado. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Cotización vence o cambia: mostrar diferencia y requerir nueva aceptación. Canal incierto sin cupo seguro: guardar solicitud pendiente y escalar, sin confirmar. |
| Resultado esperado | evitar sobreventa y promesas de disponibilidad basadas en datos inciertos |
| Evidencia documental y límite | H01, H02, H03, H04; manual/producto. No se observaron interacciones cliente-servidor en vivo. |

## US-HOT-002 / H2

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | recepcionista y responsable de housekeeping |
| Objetivo | asignar y preparar la habitación sin mezclar limpieza y reserva |
| Evento inicial | recepción prepara un check-in/check-out o housekeeping informa un cambio de preparación |
| Precondiciones | reserva válida; roles de limpieza/inspección; integración gastronómica opcional habilitada |
| Pasos | Ver reserva → verificar registro → asignar recurso físico → consultar limpieza/mantenimiento → habilitar entrada solo con condiciones cumplidas → crear cargos autorizados → liquidar y crear tarea de salida. |
| Datos | Asignación, estadoLimpieza, bloqueoTécnico, tarea/responsable, inspección opcional, cargo y cuenta. |
| Reglas | Limpia, inspeccionada, asignada, ocupada y bloqueada son dimensiones distintas. Habitación no preparada no anula automáticamente venta futura. Pedido/cargo idempotentes y entre empresas solo mediante permiso. |
| Validaciones | Limpia, inspeccionada, asignada, ocupada y bloqueada son dimensiones distintas. Habitación no preparada no anula automáticamente venta futura. Pedido/cargo idempotentes y entre empresas solo mediante permiso. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Limpieza completa con mantenimiento activo: no habilitar entrada. Inspección solo si política exige; discrepancia con recepción queda pendiente de supervisor. |
| Resultado esperado | recibir al huésped en un recurso operativo conservando ocupación futura |
| Evidencia documental y límite | H05, H01; manual/producto. No se observaron interacciones cliente-servidor en vivo. |

## US-HOT-003 / H3

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | huésped autenticado y recepción |
| Objetivo | recibir respuesta basada en datos y transferir la atención con contexto |
| Evento inicial | llega una consulta WhatsApp, petición de cambio de reserva o solicitud explícita de atención humana |
| Precondiciones | identidad cuando hay datos privados; fuente vigente, canal permitido y receptor humano configurado |
| Pasos | Recibir consulta → clasificar necesidad → recuperar datos mínimos vigentes → responder o proponer → verificar límites → si hace falta transferir con motivo/contexto → registrar dueño y estado. |
| Datos | ConversaciónReferenciada, estadoAtención, responsable, motivo, fuente/fecha, propuesta, aprobación y resultado. |
| Reglas | Una respuesta de texto, link o propuesta no confirma transacción. Durante atención humana se suspende respuesta automática de compromiso; reanudar solo por evento autorizado. Autopricing no se habilita. |
| Validaciones | Una respuesta de texto, link o propuesta no confirma transacción. Durante atención humana se suspende respuesta automática de compromiso; reanudar solo por evento autorizado. Autopricing no se habilita. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Cliente pide humano, información falta o reserva se modifica: abrir transferencia; sin receptor disponible dejar estado pendiente con canal de contacto aprobado, sin afirmar resuelto. |
| Resultado esperado | resolver consultas sin cambios de reserva no autorizados |
| Evidencia documental y límite | H06, H07, H08, H09, H10; manual/producto. No se observaron interacciones cliente-servidor en vivo. |


## Profundización posterior

Ver [revisión funcional profunda](revision-profunda.md): RF-HOT-01, RF-HOT-02, RF-HOT-03, RF-HOT-04. Los nuevos criterios se incorporan también a spec/acceptance y no son solo notas de investigación.
