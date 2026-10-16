# Historias enriquecidas y propuestas

13 historias originales conservadas con alias US y 26 AC específicos nuevos. El contenido completo de los bloques siguientes se incorpora también a los specs activos para que la investigación no quede aislada. Estado PROPUESTO; no indica aceptación del cliente.

### Historia US-CORE-001 — enriquecimiento de H1 (P1)

Como administrador de empresa, quiero habilitar conectores con alcance y cuenta comprobados, para evitar que un acceso técnico se convierta en acceso a otra empresa.

**Identidad y estado:** alias de `000-core/H1`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Habilitar conectores con alcance y cuenta comprobados. Responde a evitar que un acceso técnico se convierta en acceso a otra empresa; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** C04, I10 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-001,FR-002,FR-006,FR-010 y NFR-001/002/003/006.

**Disparador:** el administrador solicita habilitar o revisar una integración para una empresa.

**Precondiciones:** empresa y membresía verificadas; proveedor y cuenta identificados.

**Flujo principal:** Elegir empresa y proveedor → consultar capacidad documentada/contratada → identificar plan, país y permisos → registrar habilitación revisada → permitir solo operaciones incluidas.

**Flujos alternativos y casos borde:** Cuenta sin acceso o plan incompatible: mostrar no habilitado y vía de revisión, sin simular disponibilidad. Cambio de plan revoca capacidad hasta revalidación.

**Reglas de negocio y validaciones:** Acceso público a documentación no habilita API privada; configuración pertenece a un tenant y no se copia entre empresas.

**Datos y estados involucrados:** PerfilConector, referencia de cuenta, plan/país, operaciones, permisos, revisión y versión. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** Q-CORE-01/02/03; autoridad y permisos del proveedor cuando exista integración. El core no depende de ninguna vertical para funcionar.

**Riesgos:** Credencial cruzada, catálogo de capacidades obsoleto y exposición de cuenta.

**Criterios de aceptación Given/When/Then:**

- AC-US-CORE-001-01: Dado conector habilitado para A, cuando B intenta usar su referencia, entonces se deniega sin revelar secretos.
- AC-US-CORE-001-02: Dado plan sin permiso de leads, cuando se solicita captura, entonces se informa capacidad no habilitada y se registra motivo.

**Métricas de éxito:** N_habilitaciones_con_evidencia/N_habilitaciones; incidentes de acceso cruzado; no hay medición. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-CORE-002 — enriquecimiento de H2 (P1)

Como operador de conciliación, quiero distinguir una solicitud recibida de un efecto confirmado, para regularizar fallos sin duplicar cobros ni perder obligaciones.

**Identidad y estado:** alias de `000-core/H2`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Distinguir una solicitud recibida de un efecto confirmado. Responde a regularizar fallos sin duplicar cobros ni perder obligaciones; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** C06, H01 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-003,FR-004,FR-008,FR-011 y NFR-001/002/003/006.

**Disparador:** llega un resultado externo o el operador abre un intento pendiente para conciliarlo.

**Precondiciones:** referencia única de negocio, cuenta/proveedor y política fiscal aprobada.

**Flujo principal:** Registrar intento → enviar a proveedor autorizado → vincular respuesta a intento/monto → aplicar resultado una vez → conciliar o abrir pendiente con responsable.

**Flujos alternativos y casos borde:** Timeout tras envío: resultado desconocido; consultar estado antes de reintento. Evento anterior al estado vigente: conservar evidencia sin retroceder.

**Reglas de negocio y validaciones:** Recibir HTTP o cerrar pantalla no equivale a autorizar; reabrir caso no borra pago. La compensación necesita política y autorización nueva.

**Datos y estados involucrados:** Intento, resultado externo, secuencia/fecha de evento, correlación, motivo pendiente y revisión. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** Q-CORE-01/02/03; autoridad y permisos del proveedor cuando exista integración. El core no depende de ninguna vertical para funcionar.

**Riesgos:** Desorden de eventos, crédito doble, exposición en errores.

**Criterios de aceptación Given/When/Then:**

- AC-US-CORE-002-01: Dado pago desconocido, cuando llega confirmación repetida diez veces, entonces se aplica un solo efecto y el caso se cierra con evidencia.
- AC-US-CORE-002-02: Dado pago rechazado posterior a operación offline registrada, cuando se concilia, entonces no figura autorizado ni se borra la deuda.

**Métricas de éxito:** Pendientes por antigüedad y motivo; tiempo p95 hasta conciliación; efectos duplicados/operaciones. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-CORE-003 — enriquecimiento de H3 (P2)

Como responsable de seguridad y operación, quiero revisar una acción propuesta con evidencia y alcance exactos, para impedir cambios de negocio autorizados solo por el lenguaje del modelo.

**Identidad y estado:** alias de `000-core/H3`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Revisar una acción propuesta con evidencia y alcance exactos. Responde a impedir cambios de negocio autorizados solo por el lenguaje del modelo; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** I06, I07, H10 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-005,FR-007,FR-009,FR-010 y NFR-001/002/003/006.

**Disparador:** una propuesta de acción crítica solicita aprobación o intenta usar una autorización existente.

**Precondiciones:** política vigente, aprobador distinto al proponente y herramientas limitadas.

**Flujo principal:** Agente propone → servicio valida recurso/permiso/capacidad → humano revisa parámetros/evidencia → aprobar o rechazar → ejecutar solo dentro de alcance → registrar resultado.

**Flujos alternativos y casos borde:** Permiso revocado o fuente desactualizada: bloquear; cambio de monto invalida aprobación; reintento conserva identidad de efecto.

**Reglas de negocio y validaciones:** Capacidad agéntica se clasifica por efecto; una instrucción de prompt no sustituye control de servicio. No existe compra/cobro autónomo inicial.

**Datos y estados involucrados:** Política, versión herramienta, propuesta, huella aprobada, aprobador, vigencia y resultado. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). Fallar cerrado si faltan evidencia, permiso o conectividad.

**Dependencias:** Q-CORE-01/02/03; autoridad y permisos del proveedor cuando exista integración. El core no depende de ninguna vertical para funcionar.

**Riesgos:** Confused deputy, prompt injection, aprobación reutilizada y elevación de privilegios.

**Criterios de aceptación Given/When/Then:**

- AC-US-CORE-003-01: Dada aprobación por 10000 CLP, cuando la propuesta cambia a 11000, entonces no se ejecuta con el permiso anterior.
- AC-US-CORE-003-02: Dado conector de lectura, cuando una respuesta solicita escritura, entonces la capa de autorización deniega y registra.

**Métricas de éxito:** Acciones fuera de política en suite; intervenciones/acciones propuestas; costo y p95 por acción. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-CAF-001 — enriquecimiento de H1 (P1)

Como comensal y cajero autorizado, quiero pedir y pagar una parte explícita de una cuenta compartida, para cerrar el saldo correctamente sin repetir la orden de cocina.

**Identidad y estado:** alias de `001-cafeteria-mesas-pos/H1`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Pedir y pagar una parte explícita de una cuenta compartida. Responde a cerrar el saldo correctamente sin repetir la orden de cocina; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** C02, C05, C07, C11, C12 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-001,FR-002,FR-003,FR-004,FR-005,FR-015 y NFR-001/002/003/006.

**Disparador:** el cliente escanea el QR y confirma pedido o solicita pagar su parte de la cuenta.

**Precondiciones:** mesa activa, pedido versionado, regla de redondeo y de pago ratificadas; saldo no liquidado.

**Flujo principal:** Abrir mesa → confirmar pedido → ver saldo y partes → elegir ítems o reparto igual → mostrar descuentos/propina/documentación → reservar imputación → pagar → actualizar saldo hasta cierre.

**Flujos alternativos y casos borde:** Otro cliente paga el mismo saldo: rechazar segunda imputación y refrescar. Pago desconocido: parte pendiente hasta conciliar. Reagrupar antes del pago no reenvía cocina.

**Reglas de negocio y validaciones:** Suma de partes en CLP equivale al total exigible. Mostrar quién recibe residuo según regla aprobada; sin regla no confirmar reparto. Partes liquidadas no se editan ni anulan por deshacer división.

**Datos y estados involucrados:** AsignaciónCuenta, versión pedido, parte/ítem, descuentos, propina separada, residuo y pago. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000 para identidad/auditoría/pagos aplicables; Q-CAF-01/02/03 y muestra de carta, recetas o exportación según historia. Sin dependencia de hotel.

**Riesgos:** Doble pago, pérdida de descuento, QR ajeno y factura duplicada.

**Criterios de aceptación Given/When/Then:**

- AC-US-CAF-001-01: Dada regla de ejemplo que asigna residuo a última parte y total 10000 CLP, cuando se divide en tres, entonces se muestran 3333,3333,3334 y una sola comanda original.
- AC-US-CAF-001-02: Dada una parte pagada, cuando se modifica el reparto pendiente, entonces aquella conserva monto y evidencia; no se reinicia su cobro.

**Métricas de éxito:** Error de saldo por cuenta; duplicados de cocina; tiempo de cierre comparado con línea base. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-CAF-002 — enriquecimiento de H2 (P2)

Como administrador de cafetería, quiero aprobar costos e importar inventario con procedencia verificable, para conocer margen sin ocultar errores de receta ni de migración.

**Identidad y estado:** alias de `001-cafeteria-mesas-pos/H2`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Aprobar costos e importar inventario con procedencia verificable. Responde a conocer margen sin ocultar errores de receta ni de migración; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** C08, C10, C04, C12 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-007,FR-008,FR-009,FR-010 y NFR-001/002/003/006.

**Disparador:** el administrador carga factura/exportación o se registra una venta que consume una receta.

**Precondiciones:** recetas/unidades versionadas, muestra Eleventa autorizada, documento de compra y aprobador.

**Flujo principal:** Importar/extraer → detectar campos ausentes o duplicados → revisar cantidades/unidades/costos → aprobar → generar movimientos una vez → calcular margen con cobertura.

**Flujos alternativos y casos borde:** OCR ambiguo requiere captura manual. Subreceta sin correspondencia de unidad bloquea cálculo de ese costo; mostrar cobertura incompleta.

**Reglas de negocio y validaciones:** Costo desconocido no es cero; conservar fuente y versión de receta que originó consumo. No prometer exportación de datos que el archivo no contiene.

**Datos y estados involucrados:** LoteImportación, fila/origen, unidad, conversión revisada, receta/versión, línea gasto y evidencia. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000 para identidad/auditoría/pagos aplicables; Q-CAF-01/02/03 y muestra de carta, recetas o exportación según historia. Sin dependencia de hotel.

**Riesgos:** Inventario falso, margen optimista y exposición de facturas.

**Criterios de aceptación Given/When/Then:**

- AC-US-CAF-002-01: Dada receta sin costo de un insumo, cuando se calcula margen, entonces se marca no calculable y no integra un promedio como cero.
- AC-US-CAF-002-02: Dado mismo archivo importado dos veces, cuando se reconcilia, entonces totales y movimientos no se duplican y filas descartadas tienen motivo.

**Métricas de éxito:** Cobertura costos calculables/productos vendidos; error vs cálculo manual; filas conciliadas/filas fuente. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-CAF-003 — enriquecimiento de H3 (P3)

Como administrador aprobador, quiero recibir propuestas y alertas con fuente y estado de revisión, para reducir revisión repetitiva sin automatizar compromisos de compra.

**Identidad y estado:** alias de `001-cafeteria-mesas-pos/H3`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Recibir propuestas y alertas con fuente y estado de revisión. Responde a reducir revisión repetitiva sin automatizar compromisos de compra; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** C09, C10, C13 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-011,FR-012,FR-013,FR-016 y NFR-001/002/003/006.

**Disparador:** vence una revisión programada o llega una anulación, descuento o evento de stock que satisface la regla.

**Precondiciones:** stock y ventas con cobertura/fecha; regla de mínimos y aprobador definidos.

**Flujo principal:** Programar revisión autorizada → comprobar datos → detectar umbral → generar propuesta/alerta referenciada → notificar vía permitida → aprobar/rechazar/expirar.

**Flujos alternativos y casos borde:** Sin datos suficientes o fuente vencida: informar revisión incompleta. Si ya existe alerta del mismo evento/ventana, actualizar evidencia sin enviar duplicados ilimitados.

**Reglas de negocio y validaciones:** Revisión programada no implica compra autónoma. Mantener propuesta separada de orden; 48 h de expiración heredadas sujetas a política cliente.

**Datos y estados involucrados:** EjecuciónRegla, ventana de datos, evento detectado, propuesta y estado revisión. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). Fallar cerrado si faltan evidencia, permiso o conectividad.

**Dependencias:** 000 para identidad/auditoría/pagos aplicables; Q-CAF-01/02/03 y muestra de carta, recetas o exportación según historia. Sin dependencia de hotel.

**Riesgos:** Falsos positivos, omisiones, spam y compra inducida por factura maliciosa.

**Criterios de aceptación Given/When/Then:**

- AC-US-CAF-003-01: Dada alerta ya emitida por una anulación, cuando se reejecuta misma ventana, entonces se identifica la misma alerta y no una nueva compra.
- AC-US-CAF-003-02: Dada propuesta no aprobada y datos vencidos, cuando se intenta usarla, entonces se bloquea y exige revisión.

**Métricas de éxito:** Precisión/recall de alertas revisadas; propuestas aceptadas/propuestas; costo por revisión y tasa humana. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-HOT-001 — enriquecimiento de H1 (P1)

Como huésped y recepcionista, quiero reservar una categoría disponible con cotización y estado de sincronización explícitos, para evitar sobreventa y promesas de disponibilidad basadas en datos inciertos.

**Identidad y estado:** alias de `002-hotel-reservas-concierge/H1`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Reservar una categoría disponible con cotización y estado de sincronización explícitos. Responde a evitar sobreventa y promesas de disponibilidad basadas en datos inciertos; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** H01, H02, H03, H04 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-001,FR-002,FR-003,FR-004,FR-005,FR-016,FR-017 y NFR-001/002/003/006.

**Disparador:** el visitante indica fechas y ocupación y solicita cotización o confirmación de reserva.

**Precondiciones:** sistema de registro y conectores autorizados; política tarifa/cancelación/anticipo; antigüedad máxima ratificada.

**Flujo principal:** Consultar fechas/ocupación → mostrar oferta vigente → revalidar cupo/precio → retener según política → iniciar pago → confirmar una vez → registrar propagación por canal.

**Flujos alternativos y casos borde:** Cotización vence o cambia: mostrar diferencia y requerir nueva aceptación. Canal incierto sin cupo seguro: guardar solicitud pendiente y escalar, sin confirmar.

**Reglas de negocio y validaciones:** Unidad de inventario por fecha/tipo no es habitación física asignada. No habilitar sobreventa por opción de proveedor. No usar respuesta desactualizada para afirmar sincronizado.

**Datos y estados involucrados:** OfertaVersionada, TipoHabitación, cupo por fecha, retención, Reserva, referencia externa y estado por canal. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000, sistema de registro/PMS y canales habilitados según Q-HOT-01/02/03; pedidos de cafetería solo en servicio a habitación opcional.

**Riesgos:** Carrera local/OTA, cobro sin cupo y datos obsoletos.

**Criterios de aceptación Given/When/Then:**

- AC-US-HOT-001-01: Dada última unidad y cien intentos, cuando se confirma, entonces como máximo una reserva local obtiene cupo; conflictos externos se identifican y escalan.
- AC-US-HOT-001-02: Dada habitación sucia hoy pero vendible en fecha futura, cuando se busca esa fecha, entonces limpieza actual no elimina inventario futuro por sí sola.

**Métricas de éxito:** Sobreventas/confimaciones; desfase por canal p95; consultas bloqueadas por fuente obsoleta; latencia oferta. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-HOT-002 — enriquecimiento de H2 (P2)

Como recepcionista y responsable de housekeeping, quiero asignar y preparar la habitación sin mezclar limpieza y reserva, para recibir al huésped en un recurso operativo conservando ocupación futura.

**Identidad y estado:** alias de `002-hotel-reservas-concierge/H2`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Asignar y preparar la habitación sin mezclar limpieza y reserva. Responde a recibir al huésped en un recurso operativo conservando ocupación futura; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** H05, H01 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-006,FR-007,FR-008,FR-009,FR-016 y NFR-001/002/003/006.

**Disparador:** recepción prepara un check-in/check-out o housekeeping informa un cambio de preparación.

**Precondiciones:** reserva válida; roles de limpieza/inspección; integración gastronómica opcional habilitada.

**Flujo principal:** Ver reserva → verificar registro → asignar recurso físico → consultar limpieza/mantenimiento → habilitar entrada solo con condiciones cumplidas → crear cargos autorizados → liquidar y crear tarea de salida.

**Flujos alternativos y casos borde:** Limpieza completa con mantenimiento activo: no habilitar entrada. Inspección solo si política exige; discrepancia con recepción queda pendiente de supervisor.

**Reglas de negocio y validaciones:** Limpia, inspeccionada, asignada, ocupada y bloqueada son dimensiones distintas. Habitación no preparada no anula automáticamente venta futura. Pedido/cargo idempotentes y entre empresas solo mediante permiso.

**Datos y estados involucrados:** Asignación, estadoLimpieza, bloqueoTécnico, tarea/responsable, inspección opcional, cargo y cuenta. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000, sistema de registro/PMS y canales habilitados según Q-HOT-01/02/03; pedidos de cafetería solo en servicio a habitación opcional.

**Riesgos:** Asignación insegura, exposición de nombre huésped y cargo duplicado.

**Criterios de aceptación Given/When/Then:**

- AC-US-HOT-002-01: Dada habitación limpia con mantenimiento abierto, cuando se intenta check-in, entonces se bloquea y se ofrece gestión humana de asignación.
- AC-US-HOT-002-02: Dado checkout completado, cuando housekeeping termina, entonces solo cambia preparación; reservas de otras fechas permanecen intactas.

**Métricas de éxito:** Incidentes de asignación; tiempo checkout→preparada; tareas vencidas; discrepancias revisadas. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-HOT-003 — enriquecimiento de H3 (P3)

Como huésped autenticado y recepción, quiero recibir respuesta basada en datos y transferir la atención con contexto, para resolver consultas sin cambios de reserva no autorizados.

**Identidad y estado:** alias de `002-hotel-reservas-concierge/H3`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Recibir respuesta basada en datos y transferir la atención con contexto. Responde a resolver consultas sin cambios de reserva no autorizados; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** H06, H07, H08, H09, H10 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-010,FR-011,FR-012,FR-013,FR-014,FR-017 y NFR-001/002/003/006.

**Disparador:** llega una consulta WhatsApp, petición de cambio de reserva o solicitud explícita de atención humana.

**Precondiciones:** identidad cuando hay datos privados; fuente vigente, canal permitido y receptor humano configurado.

**Flujo principal:** Recibir consulta → clasificar necesidad → recuperar datos mínimos vigentes → responder o proponer → verificar límites → si hace falta transferir con motivo/contexto → registrar dueño y estado.

**Flujos alternativos y casos borde:** Cliente pide humano, información falta o reserva se modifica: abrir transferencia; sin receptor disponible dejar estado pendiente con canal de contacto aprobado, sin afirmar resuelto.

**Reglas de negocio y validaciones:** Una respuesta de texto, link o propuesta no confirma transacción. Durante atención humana se suspende respuesta automática de compromiso; reanudar solo por evento autorizado. Autopricing no se habilita.

**Datos y estados involucrados:** ConversaciónReferenciada, estadoAtención, responsable, motivo, fuente/fecha, propuesta, aprobación y resultado. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). Fallar cerrado si faltan evidencia, permiso o conectividad.

**Dependencias:** 000, sistema de registro/PMS y canales habilitados según Q-HOT-01/02/03; pedidos de cafetería solo en servicio a habitación opcional.

**Riesgos:** Suplantación, tarifa inventada, pérdida de transferencia y doble atención.

**Criterios de aceptación Given/When/Then:**

- AC-US-HOT-003-01: Dada solicitud de cancelación, cuando se deriva, entonces recepción recibe resumen mínimo y referencia; el agente no cancela ni marca resuelto.
- AC-US-HOT-003-02: Dado estado en atención humana, cuando llega mensaje adicional, entonces no dispara una modificación autónoma ni dos respuestas de compromiso.

**Métricas de éxito:** Resoluciones correctas/elegibles con reapertura controlada; transferencias completadas/iniciadas; costo/conversación p95. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-INM-001 — enriquecimiento de H1 (P1)

Como interesado y ejecutivo comercial, quiero pasar de un contacto autorizado a una promesa mediante hitos comprobables, para reservar la unidad correcta y firmar la versión legal aceptada.

**Identidad y estado:** alias de `003-inmobiliaria-comercial/H1`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Pasar de un contacto autorizado a una promesa mediante hitos comprobables. Responde a reservar la unidad correcta y firmar la versión legal aceptada; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** I01, I03, I04, I05, I09, I10 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-001,FR-002,FR-003,FR-004,FR-005,FR-006,FR-015,FR-016 y NFR-001/002/003/006.

**Disparador:** ingresa una consulta desde un canal autorizado o el ejecutivo avanza un hito de la oportunidad.

**Precondiciones:** canales autorizados y alcance de conector; identidad de contacto revisada; precios, políticas de reserva y promesa aprobados.

**Flujo principal:** Capturar contacto con origen → distinguir persona y consulta → calificar con dato declarado → proponer visita → confirmar agenda → emitir cotización versionada → revalidar unidad → reserva/pago conciliados → revisión legal/firma.

**Flujos alternativos y casos borde:** Identidad ambigua queda para revisión, no fusión automática. Plan sin webhook usa solo vía autorizada acordada, no scraping. Precio cambió: nueva cotización. Firma fallida no equivale a promesa vigente.

**Reglas de negocio y validaciones:** Presupuesto declarado no es solvencia verificada. Cotización no reserva; cita propuesta no confirmada; reserva pagada no promesa firmada. Renuncia de contacto suspende automatización permitida según política.

**Datos y estados involucrados:** Contacto, consulta/origen, consentimiento/preferencia, declaraciónCalificación, cita/estado, cotización/versión, reserva y evidenciaFirma. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000, canales de leads autorizados, agenda y proveedor de firma/política legal según Q-INM-01/02/03/04. Sin dependencia obligatoria de obra.

**Riesgos:** Discriminación, duplicados de persona, doble reserva y contrato sin versión.

**Criterios de aceptación Given/When/Then:**

- AC-US-INM-001-01: Dado lead con presupuesto declarado, cuando se califica, entonces se etiqueta como declaración y no como aprobación de financiamiento.
- AC-US-INM-001-02: Dada reserva pagada y firma fallida, cuando se revisa estado, entonces no aparece promesada ni se libera/reembolsa sin política autorizada.

**Métricas de éxito:** Leads con origen/total; primera respuesta; visitas confirmadas/elegibles; tiempo por hito; reservas duplicadas. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


### Historia US-INM-002 — enriquecimiento de H2 (P2)

Como cliente y responsable de postventa/cobranza, quiero seguir cuotas y casos con responsable, evidencia y escalamiento, para evitar cobros indebidos y solicitudes perdidas o cerradas sin validación.

**Identidad y estado:** alias de `003-inmobiliaria-comercial/H2`; conserva historia y prioridad, **REQUISITO PROPUESTO**. No hay validación del cliente ni observación de runtime.

**Descripción funcional y necesidad de negocio:** Seguir cuotas y casos con responsable, evidencia y escalamiento. Responde a evitar cobros indebidos y solicitudes perdidas o cerradas sin validación; la evidencia competitiva precisa el comportamiento, no demuestra demanda comercial.

**Fuente de inspiración y evidencia:** I02, I06 en matriz-evidencias.md. Lectura documental, reconstrucción propia. Requisitos: FR-007,FR-008,FR-009,FR-016 y NFR-001/002/003/006.

**Disparador:** vence una cuota próxima, ingresa una solicitud de postventa o expira su plazo de respuesta.

**Precondiciones:** cliente autorizado; cuotas reconciliadas; políticas garantía/plazo; destinatario de transferencia.

**Flujo principal:** Consultar cuota/caso → preparar recordatorio o clasificación provisional → validar destinatario → asignar responsable y plazo según catálogo → registrar atención → resolver con evidencia → validar cierre humano.

**Flujos alternativos y casos borde:** Solicitud urgente requiere intervención; receptor ausente queda en cola visible con escalamiento. Caso reabierto conserva historial. Cambio contacto obliga a revalidar destino antes de exponer deuda.

**Reglas de negocio y validaciones:** Clasificar no decide cobertura; prometer fecha requiere política. Transferencia no cuenta como resolución. Cobranza no modifica monto ni concilia una imagen de transferencia.

**Datos y estados involucrados:** Cuota, comunicación autorizada, CasoPostventa, estado, responsable, vencimiento, resolución, evidenciaCierre y reapertura. Transiciones conservan actor, tenant, fecha y versión; el modelo específico detalla los estados.

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000, canales de leads autorizados, agenda y proveedor de firma/política legal según Q-INM-01/02/03/04. Sin dependencia obligatoria de obra.

**Riesgos:** Divulgar deuda, perder urgencia, denegar garantía y duplicar atención.

**Criterios de aceptación Given/When/Then:**

- AC-US-INM-002-01: Dada solicitud fuera de garantía aparente, cuando clasifica el agente, entonces propone revisión humana sin rechazar ni cerrar.
- AC-US-INM-002-02: Dado caso sin aceptación de receptor, cuando se transfiere, entonces permanece pendiente con alerta y no cuenta como resuelto.

**Métricas de éxito:** Recall urgentes; primera clasificación; casos reabiertos/cerrados; tasa de transferencia completada y costo/caso. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


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

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). Fallar cerrado si faltan evidencia, permiso o conectividad.

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

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](agentes.md) y [seguridad compartida](../arquitectura/seguridad.md). No se exige IA para completar este flujo.

**Dependencias:** 000, presupuesto/programación/roles según Q-OBR-01/02/03; correspondencia con proyecto comercial opcional. No exige un módulo previo no entregado.

**Riesgos:** Cierre sin validación, cantidades duplicadas, unidad incompatible y falsa seguridad estructural.

**Criterios de aceptación Given/When/Then:**

- AC-US-OBR-004-01: Dado ítem de inspección fallido, cuando se crea observación, entonces conserva vínculo, responsable y estado; el reportante sin permiso no puede cerrarla.
- AC-US-OBR-004-02: Dada orden de 10 unidades y recepción de 6, cuando se confirma, entonces quedan 4 pendientes; repetir mismo evento no recibe 12.

**Métricas de éxito:** Observaciones con evidencia/cerradas; reaperturas; recepción conciliada/recibida; discrepancias abiertas por antigüedad. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.

## Nuevas historias candidatas fuera del alcance activo

No se añaden a los specs ni a los 66 FR. Son investigación P3 pendiente; no sustituyen ninguna historia heredada ni autorizan implementación.

### Historia US-HOT-004 — Revisar un escenario de tarifas (P3, INVESTIGAR)

Como administrador hotelero, quiero comparar una propuesta de tarifa con sus límites y motivo, para decidir si conviene modificarla sin delegar cobros ni cancelaciones.

Descripción/necesidad: propuesta revisable separada de tarifa vigente. Inspiración H10 (manual Cloudbeds Autopilot); evidencia de patrón, sin demanda cliente validada. Disparador: revisión tarifaria autorizada. Precondiciones: PMS elegido, histórico/tarifas lícitos, política y persona aprobadora. Flujo: recuperar versión vigente → preparar escenario con costos/reglas → comparar → aprobar/rechazar → conservar decisión; esta propuesta no ejecuta cambio. Alternativos/borde: precio protegido, datos obsoletos, base ausente o cambio concurrente dejan bloqueado el escenario. Reglas: no alterar inventario, política ni contrato desde una recomendación; sin autorizar autopricing. Datos: escenario, tarifa base, límites, evidencia, aprobador y versión. Dependencias: Q-HOT-01/03 y medición de necesidad; no implementable ahora. Riesgos: pérdida de margen, sesgo/estacionalidad y compromiso comercial indebido.

- AC-US-HOT-004-01: Dada tarifa protegida y escenario propuesto, cuando se revisa, entonces no se cambia la tarifa vigente y se muestra la restricción.
- AC-US-HOT-004-02: Dado cambio concurrente de tarifa base, cuando se intenta aprobar escenario anterior, entonces se invalida y se solicita revisión nueva.

Métricas propuestas: error de recomendación contra revisión experta, costo/escenario y tiempo de decisión; impacto en ingreso exige experimento controlado, no supuesto. Agente solo lee/propone, sin escritura ni límite monetario positivo; evidencias y recuperación por descarte versionado.

### Historia US-OBR-005 — Comparar alternativas de programación (P3, INVESTIGAR)

Como planificador de obra, quiero comparar un escenario con restricciones contra la línea base, para evaluar una recuperación sin reemplazar el programa aprobado.

Descripción/necesidad: análisis de escenarios independiente del registro diario. Inspiración O04 (manual ALICE), sin copiar optimizador ni inferir ahorro. Disparador: desvío aprobado que requiere planificación. Precondiciones: programa versionado, cantidades/recursos/restricciones verificadas y planificador responsable. Flujo: seleccionar baseline → declarar cambio/restricción → calcular o cargar alternativa → comparar impacto → registrar aceptación/rechazo; no actualizar programa automáticamente. Alternativos/borde: restricción faltante, recursos inviables o programa concurrente invalidan comparación. Reglas: escenario no certifica avance, compra ni seguridad; aprobación de nueva baseline es proceso aparte. Datos: escenario, restricciones, versión base, resultados y evidencia. Dependencias: Q-OBR-01/02 y escala/valor confirmados; complejidad hoy no justificada. Riesgos: falsa precisión y cambios de presupuesto no autorizados.

- AC-US-OBR-005-01: Dadas restricciones incompletas, cuando se compara, entonces se informa no evaluable y no se presenta un calendario como factible.
- AC-US-OBR-005-02: Dada alternativa aceptada para estudio, cuando se consulta baseline, entonces conserva programa original y su historial sin sobrescritura.

Métricas propuestas: alternativas factibles validadas/evaluadas, tiempo experto y costo/escenario; no declarar días ahorrados antes de ejecución real. Asistente de lectura, validación humana y descarte versionado al fallar.

## Profundización de historias existentes — continuación

### RF-CORE-01 — Declarar efectos externos de cada herramienta

**Historia US-CORE-003** (misma historia/ID, prioridad P2; no es historia nueva).

Como responsable de integraciones y aprobador, quiero declarar efectos externos de cada herramienta, para evitar que guardar un contacto o recibir un evento envíe mensajes o ejecute compromisos sin autorización.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** I11, I17, H13, H15, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** se habilita o invoca una operación de conector o se procesa una notificación.

**Precondiciones:** tenant/cuenta verificados, operación soportada y permisos/revisión definidos.

**Flujo principal:**

1. Consultar capacidad y efectos declarados por operación, incluidos flags de envío.
2. Validar intención, destinatario, datos mínimos y permiso para cada efecto.
3. Preparar vista previa o borrador sin envío cuando falte autorización.
4. Ejecutar solo alcance aprobado, registrar resultado y conciliar desconocidos.

**Flujos alternativos y excepciones:** Contrato incompleto o placeholder: operación no habilitada. Evento duplicado no repite envío. No inferir permiso de API desde documentación pública.

**Reglas de negocio/validaciones:** El método HTTP y la etiqueta MCP readOnly no prueban ausencia de efectos. Recepción/acuso, consulta, actualización y envío son resultados distintos; tenant se resuelve por identidad/cuenta autorizada, no texto o payload arbitrario.

**Datos y estados:** PerfilOperacion con efectos/flags; IntencionEnvio/destinatario; EventoExterno y evidencia mínima; estado propuesto/autorizado/intentado/confirmado/desconocido.

**Dependencias:** Q-CORE-01/03 y contrato real por operación; no incluye un motor CRM compartido.

**Riesgos:** Exfiltración, spam, cruce de empresas, firma de aprobación reutilizada y éxito aparente.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-CORE-003-03: Dada herramienta de contacto con flag de envío, cuando solo se autorizó guardar datos, entonces el adaptador no envía correo y registra los efectos excluidos.
- AC-US-CORE-003-04: Dada página de contrato con placeholder o efectos desconocidos, cuando se intenta habilitar la herramienta, entonces queda bloqueada sin llamar al destino.
- AC-US-CORE-003-05: Dada notificación de cuenta A repetida con referencia de B, cuando se procesa, entonces no accede a B ni repite comunicación; registra discrepancia para revisar.

**Métricas:** efectos no autorizados/ejecuciones; duplicados por evento; costo completo y p95 de revisión por acción. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-HOT-003-03: Dada conversación en la que el huésped pide cancelar y devolver, cuando responde concierge, entonces prepara contexto y escala; no ejecuta ninguna de las dos operaciones.
- AC-US-HOT-003-04: Dada misma modificación notificada tres veces, cuando evalúa comunicaciones, entonces no envía tres confirmaciones ni tres upsells por el mismo hecho.
- AC-US-HOT-003-05: Dada respuesta correcta con link a un motor, cuando se contabiliza éxito, entonces no figura como reserva pagada hasta evidencia de negocio independiente.

**Métricas:** resolución correcta sin reapertura/consultas elegibles; intervención, p95, costo total por resolución y acciones denegadas. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-INM-01 — Proponer, confirmar y cambiar visitas con modo de agenda explícito

**Historia US-INM-001** (misma historia/ID, prioridad P1; no es historia nueva).

Como interesado y ejecutivo comercial, quiero proponer, confirmar y cambiar visitas con modo de agenda explícito, para saber si existe una cita confirmada o solo una solicitud de horario.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** I12, I14, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** el lead pide visitar o cambiar/cancelar una visita.

**Precondiciones:** ejecutivo/canal autorizado, zona horaria, duración y modalidad de agenda revisadas.

**Flujo principal:**

1. Consultar preferencias y declarar modo calendario sincronizado o ventana estática.
2. Proponer horarios con zona y duración.
3. Verificar disponibilidad autorizada o pedir confirmación al ejecutivo si no hay calendario.
4. Confirmar cita e identificar referencia y destinatarios válidos.
5. Gestionar cambio/cancelación por vía admitida; conservar estado previo hasta resultado conocido.

**Flujos alternativos y excepciones:** Calendario caído o agenda estática: pendiente de confirmación humana, sin afirmar disponibilidad real. Horario ambiguo por zona/cambio horario: pedir precisión. Choque de citas: ofrecer alternativas sin duplicar.

**Reglas de negocio/validaciones:** Invitación enviada no comprueba disponibilidad en calendarios no conectados. Calificación no es aprobación crediticia. No copiar reglas de zona/horario de un proveedor extranjero.

**Datos y estados:** Cita, modoAgenda, zona/offset y duración, horarioPropuesto, horarioConfirmado, referenciaCalendario, responsable y solicitudCambio.

**Dependencias:** Q-INM-01, calendario o proceso manual ratificado; 000 comunicaciones controladas.

**Riesgos:** Doble cita, fecha interpretada erróneamente, contacto no permitido y falsa confirmación.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-INM-001-03: Dada agenda estática sin consulta al calendario, cuando el interesado acepta horario, entonces se identifica solicitud pendiente y no se afirma confirmación hasta aceptación autorizada.
- AC-US-INM-001-04: Dado horario local ambiguo, cuando se prepara cita, entonces exige zona/offset claro y muestra la misma fecha/hora acordada a ambas partes.
- AC-US-INM-001-05: Dada reprogramación con timeout, cuando se revisa, entonces conserva referencia de cita anterior y nueva propuesta sin crear dos citas confirmadas ni cancelar a ciegas.

**Métricas:** citas confirmadas/solicitadas, conflictos/confirmadas, reprogramaciones resueltas y costo por cita. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-INM-02 — Versionar promesa y evidencias de firma

**Historia US-INM-001** (misma historia/ID, prioridad P1; no es historia nueva).

Como ejecutivo, responsable legal y firmantes autorizados, quiero versionar promesa y evidencias de firma, para distinguir reserva pagada de documento contractual aprobado y firmado.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** I15, I18, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** reserva permite preparar promesa o se modifica el documento antes de completar firma.

**Precondiciones:** plantilla y formalidades revisadas por abogado, proveedor/identificación de firmantes y política de conservación aprobados.

**Flujo principal:**

1. Seleccionar versión legal y datos de unidad/precio aceptados.
2. Generar borrador y revisar representación/firmantes requeridos.
3. Aprobar huella exacta del documento y enviar por canal autorizado.
4. Registrar estado por firmante y evidencia del proveedor.
5. Declarar contrato completado solo cuando condiciones jurídicas y firmas exigidas se verifican.

**Flujos alternativos y excepciones:** Firma parcial/expirada/rechazada mantiene estado no completado. Cambiar el documento tras enviar requiere nueva versión y revisión. Webhook firmado no sustituye revisar identidad/estado del documento.

**Reglas de negocio/validaciones:** Ley o producto de firma no prueba por sí solo formalidad válida de esta promesa. Pago y firma son estados independientes. Conservar originales y no reescribir historia al cambiar precio. Si precio UF se acuerda, conservar unidad y referencia de conversión sin inventar valor vigente.

**Datos y estados:** DocumentoVersionado, huella, versionPlantillaLegal, participantes/representación, SolicitudFirma, EvidenciaFirma, precioAceptado y referenciaReserva.

**Dependencias:** Q-INM-02/03 y Q-CORE-02/03; no se selecciona firma ni se asegura API.

**Riesgos:** Contrato equivocado, firma incompleta, suplantación, filtración y precio no aceptado.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-INM-001-06: Dado ejemplo cuya política requiere dos firmantes y solo uno firmó, cuando se consulta la promesa, entonces muestra pendiente y no unidad promesada por ese hecho.
- AC-US-INM-001-07: Dado cambio del documento tras aprobación, cuando se intenta reutilizar autorización anterior, entonces se invalida y exige revisión de nueva huella.
- AC-US-INM-001-08: Dada firma fallida con reserva pagada, cuando se comunica el estado, entonces no se libera ni devuelve dinero automáticamente y se preserva evidencia de ambos procesos.

**Métricas:** documentos completados válidamente/enviados; fallos por versión/firmante, tiempo por hito y costo por documento válido. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-INM-03 — Mantener persona, vínculo a unidad y permisos del portal

**Historia US-INM-002** (misma historia/ID, prioridad P2; no es historia nueva).

Como administrador autorizado y cliente titular del acceso, quiero mantener persona, vínculo a unidad y permisos del portal, para corregir o reasignar accesos sin modificar otras unidades ni divulgar documentos.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** I11, I16, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** cambio autorizado de contacto/vínculo de portal, corrección de datos o intento de acceso a unidad.

**Precondiciones:** identidad de personas revisada, vínculo actual y política de acceso/historial aprobados.

**Flujo principal:**

1. Identificar si se corrige Persona o se cambia VínculoUnidad.
2. Previsualizar unidades/documentos afectados y validar aprobador.
3. Actualizar solo el objeto previsto y versionar vínculo/acceso.
4. Invalidar permisos previos de consulta corriente según política y habilitar destinatario revisado.
5. Notificar por vía autorizada y conservar historial sin envío implícito.

**Flujos alternativos y excepciones:** Coincidencia de nombre/teléfono o identidad dudosa bloquea reasignación. Archivo compartido o sesión anterior debe revalidar permisos; derechos históricos no se adivinan.

**Reglas de negocio/validaciones:** Editar una persona no transfiere propiedad ni vínculo. Cambiar acceso no ejecuta compraventa/escritura. Opciones de envío de API se validan explícitamente; no enviar deuda/documentos al guardar un contacto.

**Datos y estados:** Persona, ConsultaOrigen, VinculoUnidad con vigencia/versión, PermisoPortal, EvidenciaCambio y autorizaciónComunicacion.

**Dependencias:** Q-CORE-01/03, Q-INM-01/04; propiedad comercial sigue 003, no base compartida con obra.

**Riesgos:** Acceso del titular anterior, cambio global accidental, exposición financiera y transferencia jurídica aparente.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-INM-002-03: Dada persona A vinculada a U1 y U2 y reasignación autorizada solo del acceso corriente a U1 a B, cuando se aplica, entonces U2 no cambia y A no obtiene documentos corrientes de U1 por una sesión antigua.
- AC-US-INM-002-04: Dada corrección del teléfono de A, cuando se guarda, entonces no cambia titular de ninguna unidad ni envía información sin permiso explícito.
- AC-US-INM-002-05: Dado vínculo o identidad ambiguos, cuando se pide reasignar portal, entonces queda revisión humana sin fusionar personas ni conceder acceso.

**Métricas:** accesos indebidos por vínculo; cambios aprobados/cambios; incidentes de envío y tiempo de revisión. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-INM-04 — Coordinar visita, trabajo y aceptación de postventa

**Historia US-INM-002** (misma historia/ID, prioridad P2; no es historia nueva).

Como cliente, coordinador de postventa y técnico asignado, quiero coordinar visita, trabajo y aceptación de postventa, para seguir un caso desde clasificación provisional hasta reparación aceptada, manteniendo urgencias e historial.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** I13, I16, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** solicitud de postventa, fecha de visita, solución propuesta o reapertura del cliente.

**Precondiciones:** cliente/unidad autorizados, catálogo de fallas y reglas de plazo/garantía ratificados.

**Flujo principal:**

1. Recibir caso y evidencia con información mínima.
2. Clasificar provisionalmente, separar urgencia y verificar responsable.
3. Coordinar visita y confirmar acceso/horario.
4. Registrar inspección/trabajo y propuesta de resolución.
5. Revisar cierre por rol autorizado y conservar reapertura o inconformidad.

**Flujos alternativos y excepciones:** Cliente ausente no implica falla solucionada. Receptor técnico no acepta: caso pendiente y escala. Foto o relato contradictorios requieren inspección humana; urgencia no espera clasificación exhaustiva.

**Reglas de negocio/validaciones:** No rechazar garantía desde IA ni convertir visita agendada en solución. Estados de cobro y postventa independientes. Plazo y exclusiones deben venir de política legal/operativa, no del vendor.

**Datos y estados:** CasoPostventa, ClasificacionProvisional, Visita/estado, trabajo, propuestaSolucion, evidencia, revisor, motivosReapertura.

**Dependencias:** Q-INM-04; agenda/canal con permisos; referencia opcional a obra mediante interfaz autorizada, sin acceso automático a trabajadores/presupuesto.

**Riesgos:** Garantía rechazada indebidamente, falsa resolución, acceso a hogar y documentos ajenos.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-INM-002-06: Dada visita agendada y cliente ausente, cuando el técnico registra intento, entonces el caso no se marca reparado ni cerrado y conserva motivo para recoordinar.
- AC-US-INM-002-07: Dada reparación propuesta sin aceptación exigida por política, cuando se consulta, entonces aparece por validar y no resuelta por el solo mensaje del agente.
- AC-US-INM-002-08: Dada reapertura con nueva evidencia, cuando el cliente reclama, entonces preserva intervención previa, responsable y plazos sin borrar historial ni rechazar automáticamente garantía.

**Métricas:** tiempo recepción→responsable y visita→aceptación, reaperturas/cierres, recall urgentes y costo por caso aceptado. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-OBR-01 — Registrar partes y extracción sin perder autoría, unidades o conectividad

**Historia US-OBR-003** (misma historia/ID, prioridad P1; no es historia nueva).

Como jefe de obra, colaborador y revisor de avance, quiero registrar partes y extracción sin perder autoría, unidades o conectividad, para consolidar cantidades aprobadas sin duplicar reportes ni presentar transcripción como avance certificado.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O11, O14, O17, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** se recibe parte manual o evidencia de campo, o se reintenta enviar tras falla.

**Precondiciones:** obra/partida/versión y unidades identificadas; permisos de reporte/revisión y canal soportado.

**Flujo principal:**

1. Conservar original con autor, fecha de hecho/recepción y alcance turno/zona si aplica.
2. Verificar recepción antes de informar enviado; extracción IA solo si disponible.
3. Separar cantidades nuevas, acumuladas y correcciones; marcar ambigüedad.
4. Revisor aprueba o rechaza aportes y relaciona duplicados.
5. Consolidar avance solo desde cantidades aceptadas y denominador vigente.

**Flujos alternativos y excepciones:** Sin conectividad para IA: no afirmar extracción terminada; usar captura manual o envío diferido soportado, sin prometer aplicación offline no definida. Dos reportes del día pueden ser legítimos; porcentaje sin base no se suma.

**Reglas de negocio/validaciones:** La clave del reporte no es solo fecha+obra. Voz es evidencia no confiable; edición no sustituye original. Exportación offline consultable no demuestra captura/sincronización IA sin red.

**Datos y estados:** Parte, claveOrigen, autor, fechaHecho, recibidoEn, turno/zona/partida, tipoCantidad incremental/acumulada/corrección, extracción/revisión y versión base.

**Dependencias:** Q-OBR-01/02/03, canal y procedimiento de contingencia; no crea app móvil ni promete reconocimiento local.

**Riesgos:** Doble avance, falsa precisión, reporte perdido, prompt injection y ubicación personal expuesta.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-003-03: Dados dos partes legítimos de turnos distintos en una obra/día y un reenvío del primero, cuando se reciben, entonces conserva ambos aportes y no duplica el reenvío.
- AC-US-OBR-003-04: Dado porcentaje 40 % acumulado y nuevo reporte 45 % acumulado de la misma partida, cuando se revisa, entonces no produce 85 % por sumarlos y requiere la base/unidad definida.
- AC-US-OBR-003-05: Dada falta de conexión para transcribir, cuando se carga evidencia, entonces no se marca transcrita/aprobada; la vía manual soportada conserva mismos permisos y revisión.

**Métricas:** partes aceptados/recibidos, error por unidad/campo, retraso hecho→validación, duplicados y costo por parte aprobado. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-OBR-02 — Conciliar entrega, aceptación, rechazo y devolución de material

**Historia US-OBR-004** (misma historia/ID, prioridad P2; no es historia nueva).

Como encargado de bodega, comprador y aprobador de recepción, quiero conciliar entrega, aceptación, rechazo y devolución de material, para saber qué material se puede consumir y qué obligación sigue pendiente.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O13, O15, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** llega entrega parcial o se comunica rechazo/devolución.

**Precondiciones:** orden/líneas/versiones autorizadas, unidades revisadas, documento de entrega y responsables.

**Flujo principal:**

1. Identificar orden, tramo/entrega y líneas de material.
2. Registrar cantidad física entregada y separar aceptada/rechazada con motivo/evidencia.
3. Actualizar existencias solo de lo aceptado y calcular pendiente según política de reposición.
4. Registrar devolución como movimiento vinculado, sin borrar recepción.
5. Conciliar con compra/guía/factura por proceso autorizado antes de pago.

**Flujos alternativos y excepciones:** Entrega repetida no es nueva recepción. Conversión de unidad, exceso o versión discrepante van a revisión. Una factura no demuestra que el material llegó ni fue aceptado.

**Reglas de negocio/validaciones:** Pendiente, aceptado, rechazado y devuelto son magnitudes distintas; reposición/cancelación requieren regla del comprador. No usar rechazo como borrado de evidencia ni como pago automático.

**Datos y estados:** EntregaProveedor, TramoOrden, RecepcionLinea, cantidadEntregada/aceptada/rechazada/devuelta, MotivoEvidencia y discrepanciaContable.

**Dependencias:** Q-OBR-03 y Q-CORE-02; contabilidad/facturación se integra si se decide, no se presume módulo existente.

**Riesgos:** Stock inexistente, recepción doble, pago de material rechazado y cambio de unidad oculto.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-004-03: Dada orden de diez unidades y entrega física de seis con cinco aceptadas y una rechazada a reponer por política configurada, cuando se valida, entonces stock aumenta cinco y pendientes de suministro son cinco, con rechazo documentado.
- AC-US-OBR-004-04: Dada misma entrega recibida dos veces por reintento, cuando se registra, entonces no duplica stock; una segunda entrega con identidad distinta sí se evalúa como nueva.
- AC-US-OBR-004-05: Dada devolución de una unidad previamente aceptada, cuando se aprueba, entonces conserva recepción y registra movimiento de devolución; no se infiere abono financiero ni cambio de contrato.

**Métricas:** cantidades aceptadas/entregadas, discrepancias por orden, días pendientes y costo de conciliación por recepción. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-OBR-03 — Controlar línea base y compromiso sin sumar estados del mismo gasto

**Historia US-OBR-004** (misma historia/ID, prioridad P2; no es historia nueva).

Como control de obra y administrador de compras, quiero controlar línea base y compromiso sin sumar estados del mismo gasto, para detectar desviaciones presupuestarias con unidades y obligaciones comparables.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O16, O18, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** nueva propuesta de compra, cambio presupuestario o conciliación de obligación.

**Precondiciones:** presupuesto vigente por partida, reglas de compromiso/devengo/pago y aprobación definidos.

**Flujo principal:**

1. Seleccionar línea base y versión vigente.
2. Clasificar propuesta/compromiso/recepción/devengo/pago de cada obligación.
3. Calcular exposición y disponible con fórmula aprobada, sin doble contar estados de la misma obligación.
4. Alertar desvío o falta de clasificación y solicitar decisión humana.
5. Registrar cambio aprobado de presupuesto como nueva versión manteniendo comparación histórica.

**Flujos alternativos y excepciones:** Sin presupuesto o regla contable se informa no evaluable. Cancelación de compromiso ajusta saldo según política/evidencia; cambio de fecha no altera cantidades físicas.

**Reglas de negocio/validaciones:** Gasto, pago y avance físico no son equivalentes. El compromiso puede contener importes ya devengados/pagados, por lo que no se suman ciegamente. No aprobar excedente ni subcontrato desde IA.

**Datos y estados:** PresupuestoVersionado, Partida, ObligacionCosto y sus estados, compromisosVigentes, ajustes/causa/aprobador y FormulaControl versionada.

**Dependencias:** Q-OBR-01/02/03 y regla contable del cliente; gestión integral de subcontratos queda fuera del alcance activo hasta decisión.

**Riesgos:** Disponible inflado/negativo por doble cuenta, cambio de base invisible y compromiso no autorizado.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-004-06: Dado presupuesto de ejemplo 100 y compromiso total 50 que ya incluye devengo 20 y pago 10, cuando se calcula disponible sin otras obligaciones, entonces es 50 y no 20 al descontar los tres estados otra vez.
- AC-US-OBR-004-07: Dada modificación aprobada de presupuesto, cuando se compara avance/costo histórico, entonces conserva línea base, versión vigente y motivo/aprobador; no reescribe el pasado.
- AC-US-OBR-004-08: Dada partida sin fórmula o clasificación válida, cuando se evalúa compra, entonces indica control no evaluable y requiere revisión, sin aprobar automáticamente.

**Métricas:** partidas con exposición conciliada/partidas, error de disponible vs revisión y tiempo de detectar desvío; no ROI inventado. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-OBR-04 — Aceptar solución y distinguir respuesta técnica oficial

**Historia US-OBR-004** (misma historia/ID, prioridad P2; no es historia nueva).

Como inspector, solucionador y responsable técnico, quiero aceptar solución y distinguir respuesta técnica oficial, para cerrar una falla con autoridad y evidencia, sin confundir comentario de IA con instrucción de obra.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O10, O12, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** se entrega solución, respuesta técnica o revisión de inspección.

**Precondiciones:** observación vinculada a evidencia/partida, responsables y permisos de solución/cierre definidos.

**Flujo principal:**

1. Relacionar solución/respuesta con observación y versión de evidencia.
2. Solucionador declara lista para revisión sin cerrar por sí solo.
3. Revisor autorizado acepta, no acepta o pide información con motivo.
4. Registrar cierre o reapertura y responsable de siguiente acción.
5. Si una respuesta exige cambio contractual/presupuestario, abrir decisión aparte sin ejecutarla.

**Flujos alternativos y excepciones:** Varios comentarios o revisores no equivalen a respuesta oficial. Caso duplicado se vincula sin borrar evidencia. Nueva falla tras cierre reabre o crea caso relacionado según política.

**Reglas de negocio/validaciones:** El sistema no certifica seguridad estructural. Respuesta oficial es declaración del rol habilitado, no texto de modelo. Flujo RFI enterprise no se incorpora por usarlo como comparación.

**Datos y estados:** Observacion, PropuestaSolucion, RespuestaTecnica con emisor/alcance, EvidenciaRevision, estado/revisor/motivo y referenciaDecisionCambio.

**Dependencias:** Q-OBR-03 y política de evidencia; interfaz con comercial/postventa solo por convenio, sin permisos compartidos por grupo.

**Riesgos:** Cerrar trabajo no inspeccionado, ejecutar instrucción técnica no válida y exposición de fotos.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-004-09: Dado solucionador sin permiso de aceptar, cuando informa reparación lista, entonces queda por revisar y no cerrada; el inspector puede no aceptar con motivo.
- AC-US-OBR-004-10: Dado comentario generado por IA que cambia una especificación técnica, cuando se adjunta al caso, entonces no se convierte en respuesta oficial ni modifica presupuesto o programa.
- AC-US-OBR-004-11: Dada observación reabierta por nueva evidencia, cuando se inspecciona historial, entonces conserva cierre previo, responsable, evidencia y motivo de reapertura.

**Métricas:** cierres aceptados/revisados, reaperturas, tiempo listo→aceptado y casos sin responsable. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.

## Candidatas adicionales de constructora — no activas

### Historia US-OBR-006 — Registrar hitos de subcontrato (P3, DRAFT)

Como administrador de obra, quiero distinguir un subcontrato en borrador de uno aprobado y sus cambios, para no tratar una propuesta como compromiso autorizado.

Descripción/necesidad: registro mínimo y trazable de obligaciones, si Q-OBR-04 confirma que forma parte del producto. Inspiración O16 (FAQ Procore), como patrón documental, sin adoptar sus estados literalmente ni afirmar demanda. Disparador: propuesta o cambio de alcance de subcontrato. Precondiciones: cliente acepta el módulo, modelo legal y aprobadores definidos. Flujo: registrar propuesta y alcance → revisión técnica/legal → aprobación o rechazo → conservar versión y referencia a compromiso → controlar modificación con nueva revisión. Alternativos/casos borde: falta firma, cambio posterior, contrato cancelado o información financiera incierta no autorizan pago ni avance. Reglas: aprobar subcontrato no certifica ejecución ni paga; agentes solo preparan borradores. Datos: subcontrato/versión, partes, alcance, monto/moneda, revisión, evidencia legal y estado de compromiso. Dependencias: Q-OBR-04, Q-CORE-02/03 y política legal. Riesgos: obligación no autorizada, exposición de términos y falsa certificación. **Sin FR ni tarea de implementación activos**.

- AC-US-OBR-006-01: Dado borrador sin aprobación exigida, cuando se consulta presupuesto comprometido, entonces no se registra como obligación aprobada por su mera creación.
- AC-US-OBR-006-02: Dado alcance cambiado tras aprobación, cuando se presenta la versión anterior para ejecutar, entonces requiere nueva revisión sin sobrescribir evidencia.

Métricas propuestas: borradores/aprobados con evidencia, cambios sin versión y costo/contrato revisado; no hay medición ni ahorro demostrado.

### Historia US-OBR-007 — Pedir y aceptar aclaración técnica (P3, DRAFT)

Como responsable técnico, quiero diferenciar comentarios de una respuesta oficial a una consulta, para no ejecutar una instrucción sin autoridad ni perder la decisión.

Descripción/necesidad: coordinación mínima de dudas cuando los usuarios validen el problema; no se incorpora el motor RFI enterprise. Inspiración O12 (Autodesk Build). Disparador: falta de información o contradicción documental en una partida/inspección. Precondiciones: Q-OBR-04 cerrado, responsables/versión y canal autorizados. Flujo: registrar consulta con referencia → asignar receptor → incorporar respuestas separadas → responsable selecciona/revisa respuesta oficial → comunicar y cerrar con evidencia. Alternativos/casos borde: múltiples revisores no equivalen a consenso; consulta irrelevante se retira preservando motivo; cambio de plano requiere nueva revisión. Reglas: una respuesta no aprueba por sí sola presupuesto, programa, compra ni seguridad; IA no es aprobador técnico. Datos: consulta, referencia de plano/partida, versión, respuestas, receptor, evidencia y decisión. Dependencias: Q-OBR-04 y política de documentos/roles, sin dependencia obligatoria de inmobiliaria. Riesgos: ejecutar texto no autorizado, perder contexto y exponer información técnica. **Sin FR ni contrato API activos**.

- AC-US-OBR-007-01: Dadas dos respuestas divergentes, cuando se consulta estado, entonces no existe una respuesta oficial hasta decisión del rol autorizado.
- AC-US-OBR-007-02: Dado comentario del asistente que propone cambiar partida, cuando se registra, entonces no cambia presupuesto ni cierra observación automáticamente.

Métricas propuestas: consultas con dueño/abiertas, tiempo hasta decisión oficial, reaperturas y costo/consulta; sin resultados observados.
