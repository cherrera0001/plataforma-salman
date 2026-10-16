# Especificación — Hotel

Feature: `002-hotel-reservas-concierge`. Fecha: 2026-10-16. Estado: **BLOCKED** para implementación.
Fuente: HOT §2–5; copia conservada en docs/originales. Todos los FR y SC son **REQUISITOS PROPUESTOS**, pendientes de ratificación. Los resultados numéricos son objetivos; no se han medido.

## Problema, actores y límites

La sincronización bidireccional está bloqueada por acceso comercial y técnico. El hotel básico no necesita que la cafetería esté en producción.

Actores: huésped, recepción, housekeeping, administrador y concierge. Las responsabilidades de aprobación no se transfieren al modelo.

## 2. Escenarios de usuario y pruebas (obligatorio)

La P1 reemplaza la dispersión actual con un solo punto de verdad para reservas; P2 y P3 construyen la operación y el agente sobre ese dato.

**Historia 1 (P1): Reservar y pagar desde la web del hotel**

Un huésped entra a la web, ve disponibilidad y tarifa real, reserva, paga con Webpay o Mercado Pago y recibe confirmación y el documento tributario que corresponda. El inventario se actualiza en todos los canales (Booking, Airbnb) sin intervención manual.

- Por qué P1: hoy todo está disperso; la reserva directa con inventario único es la base de todo lo demás y reduce comisión OTA.
- Prueba independiente: dos reservas simultáneas de la última habitación no generan sobreventa; el calendario de Booking refleja el cambio en menos de 5 minutos.
- Escenarios de aceptación:
  1. Dadas fechas y número de huéspedes, cuando el visitante consulta, entonces ve solo habitaciones disponibles con tarifa vigente y total con IVA.
  2. Dada una reserva con pago aprobado, cuando Webpay confirma, entonces se envía confirmación y se procesa el documento tributario aplicable sin duplicación; objetivo de 60 segundos sujeto a política fiscal y disponibilidad externa, con pendiente/alerta ante fallo.
  3. Dada una reserva directa confirmada, cuando el channel manager sincroniza, entonces la disponibilidad baja en todos los canales conectados en menos de 5 minutos.
  4. Dada una reserva de Booking, cuando llega por el canal, entonces aparece en el sistema de registro hotelero seleccionado con los mismos datos y bloquea inventario.

**Historia 2 (P2): Operar la estadía: check-in digital, pedidos a la habitación y housekeeping**

El huésped hace check-in desde el celular antes de llegar (datos, documento, pago pendiente), pide servicios a la habitación con el mismo módulo de pedidos de la cafetería y el personal ve tareas de limpieza y mantención por habitación.

- Por qué P2: convierte la reserva en operación; reutiliza el módulo de pedidos ya probado en `001`.
- Prueba independiente: un huésped completa check-in, pide desayuno a la habitación y lo recibe cargado a su cuenta sin pasar por recepción.
- Escenarios de aceptación:
  1. Dado un check-in online completo, cuando el huésped llega, entonces recepción solo entrega la llave y el registro queda firmado.
  2. Dado un pedido a la habitación, cuando se confirma, entonces aparece en cocina con número de habitación y se carga a la cuenta del huésped.
  3. Dado un check-out, cuando la habitación se libera, entonces se crea la tarea de limpieza y la habitación no queda preparada para el siguiente check-in hasta completar la tarea y levantar bloqueos aplicables; el inventario de fechas futuras se calcula por separado.
  4. Dado un cargo pendiente al check-out, cuando el huésped paga, entonces se concilia el saldo y se documenta el hecho aplicable sin repetir anticipos ya cubiertos.

**Historia 3 (P3): Concierge agéntico por WhatsApp con reglas de autonomía**

Un agente atiende por el WhatsApp del hotel: responde, cotiza, reserva, modifica fechas dentro de reglas, vende upsells con link de pago y escala a un humano cuando sale de su límite. Toda acción queda en el ledger.

- Por qué P3: es una hipótesis de valor a validar con el cliente, pero depende del sistema de registro hotelero seleccionado (H1) y la operación (H2).
- Prueba independiente: 50 conversaciones de prueba resueltas sin humano en al menos el 70 % y cero cambios fuera de reglas.
- Escenarios de aceptación:
  1. Dada una consulta de disponibilidad por WhatsApp, cuando el agente responde, entonces cotiza con tarifa real y ofrece link de pago en menos de 30 segundos.
  2. Dado un cambio de fechas dentro de la política (sin penalidad), cuando el huésped lo pide, entonces el sistema verifica identidad, política y autorización; inicialmente el cambio requiere aprobación humana. Solo podrá ejecutarse autónomamente tras ratificar Q-HOT-03 y superar evaluación.
  3. Dado un cambio con penalidad o cancelación, cuando se solicita, entonces el agente escala a recepción con el contexto completo y no actúa.
  4. Dada una reserva pagada 48 horas antes de llegar, cuando corre el agente, entonces ofrece un upsell (late check-out, desayuno) con link de pago.

**Casos borde**

- Reserva doble por carrera entre canal directo y OTA: se previene confirmación local incompatible; si un canal externo ya confirmó, se registra conflicto y escala para resolución humana según política pendiente, sin relocalizar automáticamente.
- Pago aprobado pero boleta rechazada por SII: la reserva se mantiene, la boleta se reintenta y se alerta.
- Huésped sin documento válido en check-in online: el registro queda incompleto y se exige en recepción.
- Agente que recibe lenguaje ofensivo o solicitud ambigua: queda pendiente de atención humana con motivo, nunca inventa tarifa.
- Caída del channel manager: se suspende confirmación automática cuando no exista cupo seguro, se conserva la solicitud y se escala para reconciliar.

## 3. Requisitos (obligatorio)

**Requisitos funcionales**

| ID | El sistema DEBE | Historia |
| --- | --- | --- |
| FR-001 | Mantener un inventario único de habitaciones con tarifas por fecha, ocupación y política de cancelación | H1 |
| FR-002 | Exponer un motor de reservas en la web propia con disponibilidad real y pago en línea | H1 |
| FR-003 | Sincronizar disponibilidad y reservas con al menos Booking y Airbnb en ambos sentidos | H1 |
| FR-004 | Cobrar por Webpay/Transbank o Mercado Pago y emitir el documento SII aplicable, sin duplicar anticipos ni documentos previos | H1 |
| FR-005 | Impedir sobreventa ante reservas concurrentes del mismo inventario | H1 |
| FR-006 | Permitir check-in online con datos del huésped, documento y firma de registro | H2 |
| FR-007 | Consumir una interfaz opcional de pedidos de cafetería para servicio a la habitación, con cargo a la cuenta del huésped | H2 |
| FR-008 | Generar y cerrar tareas de housekeeping y mantención por habitación y estado | H2 |
| FR-009 | Consolidar todos los cargos de la estadía en una cuenta y liquidarla al check-out | H2 |
| FR-010 | Atender por WhatsApp Business con un agente que consulta el sistema de registro seleccionado y propone cambios; escritura solo tras autorización y política aprobadas | H3 |
| FR-011 | Aplicar reglas de autonomía configurables: acciones permitidas, montos máximos, casos que escalan | H3 |
| FR-012 | Ofrecer upsells con link de pago en momentos definidos (pre-llegada, estadía, salida) | H3 |
| FR-013 | Registrar cada acción del agente en el registro de auditoría con integridad verificable y retención aprobada con evidencia de la conversación | H3 |
| FR-014 | Exponer disponibilidad y tarifas por un servidor MCP para agentes externos (modelo SiteMinder) | H3 |
| FR-015 | Operar sobre el core compartido (identidad, autorización, pagos, documentos y auditoría) sin duplicarlo | Todas |

**Entidades clave**

- Habitación y Tipo de habitación: capacidad, servicios, estado operativo (disponible, ocupada, limpieza, bloqueada).
- Tarifa y Plan tarifario: por fecha, ocupación, canal, política de cancelación.
- Reserva: huésped, habitaciones, fechas, canal de origen, estado, pagos, cuenta.
- Huésped: identidad, documento, preferencias, historial.
- Cuenta de estadía: cargos (alojamiento, pedidos, upsells), pagos, documentos tributarios.
- Tarea operativa: tipo (limpieza, mantención), habitación, responsable, estado.
- Canal: conector (directo, Booking, Airbnb), estado de sincronización, conflictos.
- Acción de agente: conversación, regla aplicada, acción, aprobador, resultado.

## 4. Criterios de éxito (obligatorio)

| ID | Resultado medible |
| --- | --- |
| SC-001 | Cero sobreventas en 90 días de operación con al menos dos canales activos |
| SC-002 | La disponibilidad se refleja en todos los canales en menos de 5 minutos en el 95 % de los cambios |
| SC-003 | Las reservas directas pasan del nivel actual a al menos 30 % del total en 6 meses |
| SC-004 | El 100 % de los pagos queda conciliado con su obligación documental aplicable; objetivo de entrega <60 s cuando proceda y haya disponibilidad externa, sujeto a ratificación; fallos quedan pendientes y alertados |
| SC-005 | El 60 % de los huéspedes completa check-in online antes de llegar |
| SC-006 | El agente resuelve al menos el 70 % de conversaciones de WhatsApp sin intervención humana |
| SC-007 | Cero acciones del agente fuera de sus reglas de autonomía (auditoría mensual del ledger) |
| SC-008 | Los upsells ofrecidos por el agente convierten al menos el 8 % (referencia Duve) |
| SC-009 | Un empleado nuevo opera recepción con el sistema tras 2 horas de capacitación |

## 5. Supuestos, dependencias y clarificaciones

**Supuestos**

- Hotel de menos de 50 habitaciones, un solo edificio, PMS actual y continuidad por confirmar en Q-HOT-01; no se decide abandonarlo.
- Los canales OTA relevantes son Booking y Airbnb; otros se agregan después.
- La cocina y el servicio a la habitación podrían compartir operación con la cafetería mediante interfaz opcional; no se replica su módulo por defecto.
- Recepción opera con horario; fuera de horario el agente es el primer contacto.

**Dependencias**

- Core (`000-core`) para H1; interfaz opcional de pedidos (`001` o adaptador autorizado) solo para el servicio a habitación de H2.
- Channel manager propio o integrado (evaluar en `research.md`: construir conector vs. contratar uno con API).
- Certificado SII, contrato Webpay Plus, cuenta WhatsApp Business API con plantillas aprobadas.
- Credenciales de partner de Booking y Airbnb (requieren proceso de certificación).

**Clarificaciones pendientes** (para `/speckit.clarify`)

- [ ] [NEEDS CLARIFICATION] ¿Cuántas habitaciones y tipos tiene el hotel, y hay temporada alta definida? Define tarifas y escala.
- [ ] [NEEDS CLARIFICATION] ¿Qué canales usan hoy y con qué volumen? Define el alcance de FR-003.
- [ ] [NEEDS CLARIFICATION] ¿Existe PMS actual con datos a migrar o se parte de cero?
- [ ] [NEEDS CLARIFICATION] ¿Política de cancelación y de cobro anticipado (total, parcial, garantía)?
- [ ] [NEEDS CLARIFICATION] ¿Se emite factura a empresas con frecuencia? Define si FR-004 incluye factura desde V1.
- [ ] [NEEDS CLARIFICATION] ¿Límite monetario del agente para ejecutar sin aprobación (por ejemplo, cambios sin penalidad hasta X pesos)?
- [ ] [NEEDS CLARIFICATION] ¿Housekeeping con personal propio o externo? Define acceso y notificaciones.

## Reglas normativas y de aceptación añadidas

- NFR-001: toda lectura, escritura, trabajo en cola y evidencia queda limitada por empresa y permiso; probar denegación entre empresas y roles.
- NFR-002: ningún agente ejecuta una acción financiera, tributaria o contractual sin control determinista y autorización vigente; escritura MCP deshabilitada inicialmente.
- NFR-003: reintentos conservan un solo efecto; estados desconocidos no se muestran como éxitos.
- NFR-004: retención, restauración y objetivos de recuperación requieren aprobación en Q-CORE-03; ninguna cifra de disponibilidad se asume acordada.
- NFR-005: medir latencia desde recepción hasta resultado confirmado, incluyendo errores, reintentos y desconexión. No declarar cumplimiento en muestras vacías.

Q-HOT-01: PMS actual y fuente de inventario; Q-HOT-02: acceso OTA/channel manager; Q-HOT-03: habitaciones, cancelación, anticipos, datos de registro y autonomía.

Los escenarios tributarios y SC de emisión en 30/60 segundos se conservan como aspiración de la fuente, sujetos a aplicabilidad fiscal y disponibilidad externa. No constituyen garantía del SII. El aislamiento local no garantiza por sí solo cero sobreventa entre OTA independientes.

Ver `acceptance.md` para pruebas por requisito; `../../docs/auditorias/trazabilidad.md` para origen y equivalencias. La investigación transversal está en `../../docs/investigacion/estado-del-arte.md`.


## Refinamiento competitivo de historias — 2026-10-16

Estado **PROPUESTO**, sin ratificación del cliente. Las siguientes definiciones amplían las historias originales con alias US, sin eliminarlas. Ante un caso específico se aplica la regla más explícita de esta sección; ninguna cambia los bloqueos comerciales. Evidencia por ID en `../../docs/investigacion-competitiva/matriz-evidencias.md`.

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

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](../../docs/investigacion-competitiva/agentes.md) y [seguridad compartida](../../docs/arquitectura/seguridad.md). No se exige IA para completar este flujo.

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

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](../../docs/investigacion-competitiva/agentes.md) y [seguridad compartida](../../docs/arquitectura/seguridad.md). No se exige IA para completar este flujo.

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

**Interacción humana/agéntica:** el humano responde por revisión y aprobación; el agente solo consulta o propone dentro del permiso. Herramientas candidatas, campos mínimos, límites cero para compromiso, evidencia y reversión se detallan en [gobernanza comparada](../../docs/investigacion-competitiva/agentes.md) y [seguridad compartida](../../docs/arquitectura/seguridad.md). Fallar cerrado si faltan evidencia, permiso o conectividad.

**Dependencias:** 000, sistema de registro/PMS y canales habilitados según Q-HOT-01/02/03; pedidos de cafetería solo en servicio a habitación opcional.

**Riesgos:** Suplantación, tarifa inventada, pérdida de transferencia y doble atención.

**Criterios de aceptación Given/When/Then:**

- AC-US-HOT-003-01: Dada solicitud de cancelación, cuando se deriva, entonces recepción recibe resumen mínimo y referencia; el agente no cancela ni marca resuelto.
- AC-US-HOT-003-02: Dado estado en atención humana, cuando llega mensaje adicional, entonces no dispara una modificación autónoma ni dos respuestas de compromiso.

**Métricas de éxito:** Resoluciones correctas/elegibles con reapertura controlada; transferencias completadas/iniciadas; costo/conversación p95. Valores objetivo y ventanas deben ratificarse; no hay resultados medidos ni beneficio financiero calculado.


## Requisitos derivados de investigación competitiva

Son propuestas de comportamiento propio, sin atribuirlo como implementación observada del competidor.

| ID | El sistema DEBE | Historia |
|---|---|---|
| FR-016 | Distinguir inventario vendible por fecha/tipo, asignación física y preparación de habitación; impedir check-in con bloqueo operativo sin eliminar automáticamente inventario futuro | H1/H2 |
| FR-017 | Registrar vigencia y estado de sincronización por canal y procedencia de la oferta; no confirmar disponibilidad incierta y gestionar transferencia humana con estado explícito | H1/H3 |

- NFR-006: toda oferta, extracción o decisión derivada declara procedencia, vigencia e incertidumbre; si no hay evidencia suficiente, no genera compromiso automático ni se informa como éxito. La captura manual conserva permisos, trazabilidad e idempotencia equivalentes.
