# Revisión funcional profunda — inmobiliaria

Revisión de fuentes primarias y reconstrucción de comportamiento; no se ejecutó aplicación/REA. El campo actor/flujo/reglas siguiente es propuesta propia y conserva sus límites de evidencia.

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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

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

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-INM-002-06: Dada visita agendada y cliente ausente, cuando el técnico registra intento, entonces el caso no se marca reparado ni cerrado y conserva motivo para recoordinar.
- AC-US-INM-002-07: Dada reparación propuesta sin aceptación exigida por política, cuando se consulta, entonces aparece por validar y no resuelta por el solo mensaje del agente.
- AC-US-INM-002-08: Dada reapertura con nueva evidencia, cuando el cliente reclama, entonces preserva intervención previa, responsable y plazos sin borrar historial ni rechazar automáticamente garantía.

**Métricas:** tiempo recepción→responsable y visita→aceptación, reaperturas/cierres, recall urgentes y costo por caso aceptado. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.
