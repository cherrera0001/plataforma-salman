# Revisión funcional profunda — hotel

Revisión de fuentes primarias y reconstrucción de comportamiento; no se ejecutó aplicación/REA. El campo actor/flujo/reglas siguiente es propuesta propia y conserva sus límites de evidencia.

### RF-HOT-01 — Modificar o cancelar sin confundir liquidación y devolución

**Historia US-HOT-001** (misma historia/ID, prioridad P1; no es historia nueva).

Como huésped autenticado y recepción autorizada, quiero modificar o cancelar sin confundir liquidación y devolución, para conocer diferencias de precio y resultado financiero antes de comprometer un cambio de reserva.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** H11, H12, H18, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** solicitud de nuevas fechas, categoría, habitación o cancelación.

**Precondiciones:** reserva vigente versionada, identidad validada, política de cambios/cancelación y aprobador definidos.

**Flujo principal:**

1. Recuperar reserva, versión, fuente y condiciones aceptadas.
2. Calcular propuesta con fechas/unidad, cupo, tarifa, penalidad y saldo anterior/nuevo.
3. Mostrar diferencias y obtener aceptación/aprobación ligada a la propuesta.
4. Revalidar versión/cupo y aplicar la transición en el sistema de registro seleccionado.
5. Separar resultado de cambio, actualización de canales y propuesta de devolución; informar estados.

**Flujos alternativos y excepciones:** Tarifa cambia durante revisión: invalidar propuesta. Timeout: desconocido, consultar autoridad antes de repetir. Cancelación OTA requiere proceso del canal, no se convierte en cancelación directa.

**Reglas de negocio/validaciones:** Cancelar no devuelve dinero ni borra historial. No aplicar tarifa por arrastrar una reserva sin revisar diferencia. El agente no aprueba penalidad ni reembolso; una habitación sin asignar no es una reserva inexistente.

**Datos y estados:** PropuestaCambio, versionBase, desglose anterior/nuevo, aceptación, aprobación, ResultadoCambio; SolicitudDevolucion separada de Pago y Reserva.

**Dependencias:** Q-HOT-01/02/03 y Q-CORE-02; pagos/documentos del core con referencias, sin elegir PMS.

**Riesgos:** Cambio no consentido, doble devolución, venta sin cupo y fuga de datos huésped.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-HOT-001-03: Dada reserva pagada y política de ejemplo que permite devolución, cuando recepción cancela, entonces la reserva puede quedar cancelada pero el dinero permanece sin devolver hasta operación financiera autorizada y confirmada.
- AC-US-HOT-001-04: Dada nueva tarifa superior a la aceptada, cuando se previsualiza el cambio, entonces muestra diferencia y no la aplica sin nueva aceptación.
- AC-US-HOT-001-05: Dado timeout tras aplicar un cambio, cuando se reintenta, entonces consulta estado y no crea segunda reserva, cargo ni devolución.

**Métricas:** cambios con desglose y consentimiento/cambios aplicados; devoluciones duplicadas; tiempo p95 de regularización. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-HOT-02 — Vincular extras a estadía y entrega operativa

**Historia US-HOT-002** (misma historia/ID, prioridad P2; no es historia nueva).

Como recepcionista, huésped y responsable del servicio, quiero vincular extras a estadía y entrega operativa, para cargar exactamente el servicio contratado y asignar su cumplimiento.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** H14, H16, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** aceptación de desayuno, mejora o pedido de habitación.

**Precondiciones:** reserva/cuenta válidas, producto/servicio mapeado, periodicidad y responsable aprobados.

**Flujo principal:**

1. Identificar cuenta y producto con precio/periodicidad vigentes.
2. Calcular cantidad según configuración aceptada y revalidar disponibilidad si consume cupo.
3. Registrar cargo único y su referencia al pedido/servicio.
4. Asignar tarea de cumplimiento cuando proceda y seguir su estado.
5. Conciliar cancelación o modificación mediante ajuste autorizado, no borrado.

**Flujos alternativos y excepciones:** Mapeo de producto/categoría ausente deja cargo en revisión. Pedido gastronomía no habilitado se informa sin duplicar cocina. Fallo tras cargo se concilia antes de repetir.

**Reglas de negocio/validaciones:** Una noche, persona o estadía son bases distintas. Cargo, pago, documento tributario y entrega son estados separados. Solo el servicio correspondiente conoce la periodicidad; el core no contiene catálogo hotelero ni gastronómico universal.

**Datos y estados:** ServicioEstadia, ReglaCantidad versionada, Cargo, CuentaReferencia, CategoriaExterna opcional, TareaCumplimiento y relación con PedidoExterno.

**Dependencias:** 000 y política fiscal; interfaz opcional 001 para pedidos, no dependencia de hotel H1.

**Riesgos:** Multiplicar extras por noches indebidamente, cargo a huésped ajeno y servicio pagado no entregado.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-HOT-002-03: Dada configuración de ejemplo de desayuno por persona/noche para dos personas y tres noches y una botella por estadía, cuando se calcula, entonces desayuno tiene seis unidades y botella una, con reglas visibles.
- AC-US-HOT-002-04: Dado cargo registrado pero tarea sin entregar, cuando se consulta la cuenta, entonces distingue cobro/cargo de cumplimiento y no informa servicio entregado.
- AC-US-HOT-002-05: Dado mismo pedido/cargo reintentado, cuando el conector responde dos veces, entonces hay un cargo y una tarea vinculados, sin segunda comanda.

**Métricas:** cargos conciliados/servicios aceptados; tareas vencidas; error de cantidad; costo por extra gestionado. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-HOT-03 — Recepcionar eventos y reconciliar inventario de canales

**Historia US-HOT-001** (misma historia/ID, prioridad P1; no es historia nueva).

Como recepción y operador de integración, quiero recepcionar eventos y reconciliar inventario de canales, para recuperar reservas y cambios sin perderlos ni repetir efectos por notificaciones.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** H13, H15, H17, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** llega un evento o se reanuda una ventana de sincronización tras fallo.

**Precondiciones:** conector autorizado, correspondencia de propiedad/recurso y mecanismo de autenticación/revisión definidos.

**Flujo principal:**

1. Validar origen/cuenta y correspondencia de propiedad.
2. Registrar recepción durable y referencia de notificación.
3. Emitir acuse solo en el punto permitido por el contrato del canal tras recepción durable validada; si el protocolo exige aplicación previa, respetar esa condición sin declarar éxito anticipado.
4. Recuperar el estado autoritativo cuando la notificación no incluye todos los datos.
5. Aplicar una vez la transición válida y conservar conflictos.
6. Reanudar por cursor/ventana y comparar cupos/estados.

**Flujos alternativos y excepciones:** No se puede persistir: no acusar recepción que no existe. Mapeo desconocido: recepción retenida en revisión según protocolo contratado, sin inventario ficticio. Caída tras acuse: recuperar del registro durable.

**Reglas de negocio/validaciones:** El acuse no confirma pago ni reserva local válida. Una notificación puede representar cambios sucesivos. No asumir orden total, entrega única, API directa Booking habilitada ni que Channels Plus sea el conector PMS contratado.

**Datos y estados:** RecepcionEvento, ClaveProveedor/cuenta, referenciaExterna, huella, recibidoEn, ocurrioEn si existe, estadoRecepcion, estadoAplicacion, cursor/ventana y Conflicto.

**Dependencias:** Q-HOT-02 y capacidades/contratos 000; control de cupos permanece hotelero.

**Riesgos:** Evento perdido, replay, overbooking, deduplicación incorrecta y pérdida de actualización concurrente.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-HOT-001-06: Dada falla de almacenamiento antes de recepción durable, cuando llega reserva del canal, entonces no se declara acuse exitoso ni confirmación local.
- AC-US-HOT-001-07: Dada recepción durable y acuse completado pero caída antes de aplicar, cuando se recupera, entonces se reaplica desde evidencia sin perder reserva ni duplicar efectos.
- AC-US-HOT-001-08: Dados cinco eventos con igual ID notificación y una actualización nueva del mismo ID de reserva, cuando se reconcilian, entonces se deduplica notificación pero no se descarta el cambio legítimo por usar solo ID reserva.

**Métricas:** eventos recibidos/aplicados/en revisión por canal; lag p95; conflictos detectados; duración de interrupción. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-HOT-04 — Concierge: separar conversación, propuesta y compromiso

**Historia US-HOT-003** (misma historia/ID, prioridad P3; no es historia nueva).

Como huésped y responsable de recepción, quiero concierge: separar conversación, propuesta y compromiso, para recibir respuestas útiles y atención humana sin acciones de negocio supuestas.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** H06, H07, H08, H09, H11, H13, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** consulta de reserva/extra, cambio con efecto económico o solicitud de humano.

**Precondiciones:** identidad para datos privados, datos vigentes, política de acción y receptor humano definidos.

**Flujo principal:**

1. Clasificar intención sin inferir autoridad.
2. Consultar evidencia mínima vigente.
3. Responder o preparar una propuesta diferenciada de confirmación.
4. Si requiere acción/juicio, transferir con responsable y motivo; suspender cambios automáticos.
5. Registrar aceptación humana, resultado y reapertura, distinguiendo estado del canal y del negocio.

**Flujos alternativos y excepciones:** Sin receptor: pendiente visible, sin prometer hora no aprobada. Cambio automático de reserva no dispara mensajes repetidos en cada notificación. Solicitud ambigua pide precisión sin inventar dato.

**Reglas de negocio/validaciones:** Responder, cotizar, enlazar pago, modificar PMS y cobrar son capacidades diferentes. Mensaje del cliente no autoriza devolución. No se usa un porcentaje comercial del proveedor como medición propia.

**Datos y estados:** Intencion, Respuesta/Propuesta, EvidenciaFuente, Transferencia, responsable y resultadoNegocio separado de estadoConversacion.

**Dependencias:** Q-HOT-03, política canal y perfil herramienta; sin permisos de escritura MCP por defecto.

**Riesgos:** Confundir marketing con autonomía, prompt injection, spam por eventos y falsa resolución.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-HOT-003-03: Dada conversación en la que el huésped pide cancelar y devolver, cuando responde concierge, entonces prepara contexto y escala; no ejecuta ninguna de las dos operaciones.
- AC-US-HOT-003-04: Dada misma modificación notificada tres veces, cuando evalúa comunicaciones, entonces no envía tres confirmaciones ni tres upsells por el mismo hecho.
- AC-US-HOT-003-05: Dada respuesta correcta con link a un motor, cuando se contabiliza éxito, entonces no figura como reserva pagada hasta evidencia de negocio independiente.

**Métricas:** resolución correcta sin reapertura/consultas elegibles; intervención, p95, costo total por resolución y acciones denegadas. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.
