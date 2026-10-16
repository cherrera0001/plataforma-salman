# Especificación — Inmobiliaria comercial

Feature: `003-inmobiliaria-comercial`. Fecha: 2026-10-16. Estado: **BLOCKED** para implementación.
Fuente: INM §2–5; copia conservada en docs/originales. Todos los FR y SC son **REQUISITOS PROPUESTOS**, pendientes de ratificación. Los resultados numéricos son objetivos; no se han medido.

## Problema, actores y límites

Escrituración y crédito hipotecario fuera de V1; solo hitos. H3 y FR-010 a FR-012 de la fuente se trasladan a 004.

Actores: interesado, ejecutivo, responsable legal y jefe de postventa. Las responsabilidades de aprobación no se transfieren al modelo.

## 2. Escenarios de usuario y pruebas (obligatorio)

La P1 ordena el dato fragmentado (Excel, WhatsApp, portales) en un solo flujo de lead a promesa; sin eso ningún agente puede actuar con permisos claros (brecha e del estado del arte).

**Historia 1 (P1): De lead a promesa en un solo flujo**

Un interesado llega por web, portal o WhatsApp; un agente lo califica (presupuesto, plazo, financiamiento), agenda la visita y lo entrega al ejecutivo. El ejecutivo cotiza desde el stock real de unidades, el cliente reserva con pago en línea y firma la promesa electrónicamente.

- Por qué P1: es el ciclo de ingresos; se propone reducir el trabajo manual de calificación y documentación y la cotización y la promesa son manuales.
- Prueba independiente: un lead de prueba recorre calificación, visita, cotización, reserva pagada y promesa firmada sin planilla externa, en menos de 48 horas de tiempo de proceso.
- Escenarios de aceptación:
  1. Dado un mensaje de WhatsApp de un interesado, cuando el agente responde, entonces en menos de 2 minutos tiene presupuesto, plazo y tipo de unidad y propone horario de visita.
  2. Dada una unidad disponible, cuando el ejecutivo genera cotización, entonces el documento sale con precio vigente, pie, financiamiento estimado y vence a una fecha.
  3. Dada una cotización aceptada, cuando el cliente paga la reserva por Webpay, entonces la unidad queda bloqueada y se emite boleta o comprobante.
  4. Dada una reserva pagada, cuando se envía la promesa, entonces el cliente firma electrónicamente y el documento queda archivado con la unidad.

**Historia 2 (P2): Cobranza y postventa con agente**

Tras la promesa, el sistema controla el calendario de pagos del pie, recuerda cuotas por WhatsApp, concilia pagos y, tras la entrega, recibe y gestiona solicitudes de postventa con un agente que clasifica, asigna y hace seguimiento.

- Por qué P2: cobranza y postventa son el dolor crónico de las inmobiliarias chilenas ; la cobertura real de proveedores no se ha verificado.
- Prueba independiente: 20 clientes con cuotas pendientes reciben recordatorios, 10 solicitudes de postventa se clasifican y asignan sin intervención manual.
- Escenarios de aceptación:
  1. Dada una cuota que vence en 5 días, cuando corre el agente, entonces envía recordatorio con monto y link de pago, y registra la gestión.
  2. Dado un pago recibido, cuando se concilia, entonces el estado de la cuota cambia y el cliente recibe comprobante.
  3. Dada una solicitud de postventa por WhatsApp con foto, cuando el agente la recibe, entonces la clasifica (urgente, garantía, no cubierta), la asigna y responde plazo estimado.
  4. Dada una solicitud sin respuesta del responsable en 72 horas, cuando vence, entonces el agente escala al jefe de postventa.

**Casos borde**

- Dos ejecutivos cotizan la misma unidad: la primera reserva pagada bloquea; la otra cotización se invalida y se avisa.
- Lead que contacta por dos canales: se fusiona en un solo registro, sin duplicar seguimiento.
- Pago de reserva aprobado y promesa no firmada en el plazo: la unidad se libera con aviso y el pago se concilia y la liberación/devolución requiere política y autorización humana; no se reembolsa automáticamente.
- Solicitud de postventa fuera de garantía: el agente responde con la política, no la rechaza solo.

## 3. Requisitos (obligatorio)

**Requisitos funcionales**

| ID | El sistema DEBE | Historia |
| --- | --- | --- |
| FR-001 | Capturar leads desde web, portales (Portalinmobiliario, TOCTOC, Yapo) y WhatsApp en un solo registro deduplicado | H1 |
| FR-002 | Calificar leads por WhatsApp con un agente (presupuesto, plazo, financiamiento, tipo de unidad) y agendar visitas en la agenda del ejecutivo | H1 |
| FR-003 | Mantener el stock de unidades por proyecto con precio vigente, estado (disponible, reservada, promesada, escriturada) y bloqueo por reserva | H1 |
| FR-004 | Generar cotizaciones con precio, pie, financiamiento estimado y vencimiento, trazables al lead y a la unidad | H1 |
| FR-005 | Cobrar la reserva por Webpay/Transbank o Mercado Pago y emitir el documento tributario que corresponda | H1 |
| FR-006 | Enviar la promesa de compraventa a firma electrónica (Ley 19.799) y archivarla con la unidad | H1 |
| FR-007 | Administrar el calendario de pagos del pie, enviar recordatorios por WhatsApp con link de pago y conciliar pagos | H2 |
| FR-008 | Recibir solicitudes de postventa por WhatsApp y web, clasificarlas con un agente, asignarlas y seguir plazos con escalamiento | H2 |
| FR-009 | Exponer al cliente un portal con su unidad, pagos, documentos y solicitudes | H2 |
| FR-013 | Registrar toda acción de agente en el registro de auditoría con integridad verificable y retención aprobada con evidencia y aprobador | Todas |
| FR-014 | Operar sobre el core compartido (identidad, autorización, pagos, documentos y auditoría) sin duplicarlo | Todas |

**Entidades clave**

- Proyecto: nombre, ubicación, etapas, unidades, estado comercial y de obra.
- Unidad: tipo, superficie, precio vigente, estado, reserva, promesa, escritura.
- Lead y Cliente: origen, canal, calificación, ejecutivo, historial de contacto.
- Cotización: unidad, precio, pie, financiamiento, vencimiento, estado.
- Reserva y Promesa: pagos, documentos firmados, plazos.
- Calendario de pagos y Cuota: monto, vencimiento, estado, conciliación.
- Solicitud de postventa: unidad, tipo, clasificación, responsable, plazo, estado.
- Acción de agente: conversación, regla, acción, aprobador, resultado.

## 4. Criterios de éxito (obligatorio)

| ID | Resultado medible |
| --- | --- |
| SC-001 | El 100 % de los leads de todos los canales queda en un solo registro en menos de 5 minutos |
| SC-002 | El tiempo de primera respuesta a un lead baja a menos de 2 minutos, 24/7 |
| SC-003 | Al menos el 60 % de los leads calificados agenda visita sin intervención del ejecutivo |
| SC-004 | El tiempo de lead a promesa firmada baja al menos 30 % frente al proceso actual |
| SC-005 | Cero unidades vendidas dos veces (auditoría trimestral) |
| SC-006 | La morosidad de cuotas del pie baja al menos 20 % en 6 meses |
| SC-007 | El 90 % de las solicitudes de postventa recibe clasificación y plazo en menos de 1 hora |
| SC-009 | Cero acciones de agente fuera de reglas (auditoría mensual del ledger) |

## 5. Supuestos, dependencias y clarificaciones

**Supuestos**

- Inmobiliaria y constructora son del mismo grupo; comparten proyectos y unidades, pero tienen usuarios distintos.
- Hay entre 1 y 5 proyectos activos con menos de 200 unidades en total.
- Los ejecutivos comerciales usan WhatsApp como canal principal; los portales inmobiliarios entregan leads por correo o API.
- La escrituración y el crédito hipotecario siguen fuera del sistema en V1 (solo se registran hitos).

**Dependencias**

- Core (`000-core`) en producción.
- Proveedor de firma electrónica avanzada con API (evaluar en `research.md`).
- Credenciales de portales para captura de leads; cuenta WhatsApp Business API; contrato Webpay Plus; certificado SII.
- Para H3: presupuesto por partida en formato digital (Excel estructurado o itemizado) y lo construido en inspección de terreno y control de obra.

**Clarificaciones pendientes** (para `/speckit.clarify`)

- [ ] [NEEDS CLARIFICATION] ¿Cuántos proyectos y unidades activas hoy, y en qué etapa (verde, blanco, entrega)?
- [ ] [NEEDS CLARIFICATION] ¿Qué CRM o planillas usan hoy y qué historial se migra?
- [ ] [NEEDS CLARIFICATION] ¿La reserva es con pago en línea obligatorio o se acepta transferencia? Afecta FR-005 y el bloqueo de unidad.
- [ ] [NEEDS CLARIFICATION] ¿Quién redacta y aprueba la promesa (abogado interno o externo) y cuál es el plazo máximo entre reserva y promesa?
- [ ] [NEEDS CLARIFICATION] ¿Política de postventa: plazos de garantía por tipo de falla y responsables?
- [ ] [NEEDS CLARIFICATION] ¿La constructora ejecuta solo obras propias o también para terceros? Afecta el alcance de `004`.
- [ ] [NEEDS CLARIFICATION] ¿Límite monetario para que el asistente prepare compras sin revisión del administrador?

## Reglas normativas y de aceptación añadidas

- NFR-001: toda lectura, escritura, trabajo en cola y evidencia queda limitada por empresa y permiso; probar denegación entre empresas y roles.
- NFR-002: ningún agente ejecuta una acción financiera, tributaria o contractual sin control determinista y autorización vigente; escritura MCP deshabilitada inicialmente.
- NFR-003: reintentos conservan un solo efecto; estados desconocidos no se muestran como éxitos.
- NFR-004: retención, restauración y objetivos de recuperación requieren aprobación en Q-CORE-03; ninguna cifra de disponibilidad se asume acordada.
- NFR-005: medir latencia desde recepción hasta resultado confirmado, incluyendo errores, reintentos y desconexión. No declarar cumplimiento en muestras vacías.

Q-INM-01: proyectos, CRM y captura autorizada de leads; Q-INM-02: reserva, vigencia y reembolsos; Q-INM-03: revisión legal de promesa y firma; Q-INM-04: garantías y responsables.

Los escenarios tributarios y SC de emisión en 30/60 segundos se conservan como aspiración de la fuente, sujetos a aplicabilidad fiscal y disponibilidad externa. No constituyen garantía del SII. El aislamiento local no garantiza por sí solo cero sobreventa entre OTA independientes.

Ver `acceptance.md` para pruebas por requisito; `../../docs/auditorias/trazabilidad.md` para origen y equivalencias. La investigación transversal está en `../../docs/investigacion/estado-del-arte.md`.
