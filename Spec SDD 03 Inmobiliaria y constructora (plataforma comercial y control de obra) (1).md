# Spec SDD 03: Inmobiliaria y constructora (plataforma comercial y control de obra)

Oct 15, 2026 · @Cristóbal Herrera

## 0. Flujo spec-kit aplicado y división en dos features

Este documento es el `spec.md` de la feature `003-inmobiliaria-comercial`; el control de obra se especifica aparte como `004-constructora-obra`, porque son dos negocios con usuarios, datos y ritmo distintos, y spec-kit trabaja una feature a la vez (`.specify/feature.json`). La ruta completa de [spec-kit](https://github.github.com/spec-kit/quickstart.html) aplica igual que en 01 y 02; la constitución versión 1.0.0 del Spec SDD 01 se reutiliza sin cambios.

| Feature | Alcance | Prioridad | Depende de |
| --- | --- | --- | --- |
| `003-inmobiliaria-comercial` (este doc) | Leads, cotización, reserva, promesa, cobranza, postventa | V1 | `000-core` |
| `004-constructora-obra` | Presupuesto, avance, subcontratos, compras, inspección | V2 | `003` (unidades y proyectos) y lo ya construido en inspección de terreno y control de obra |

La historia P3 de este doc (asistente de obra ligero) es el puente mínimo hacia `004`; no pretende reemplazarla.

## 2. Escenarios de usuario y pruebas (obligatorio)

La P1 ordena el dato fragmentado (Excel, WhatsApp, portales) en un solo flujo de lead a promesa; sin eso ningún agente puede actuar con permisos claros (brecha e del estado del arte).

**Historia 1 (P1): De lead a promesa en un solo flujo**

Un interesado llega por web, portal o WhatsApp; un agente lo califica (presupuesto, plazo, financiamiento), agenda la visita y lo entrega al ejecutivo. El ejecutivo cotiza desde el stock real de unidades, el cliente reserva con pago en línea y firma la promesa electrónicamente.

- Por qué P1: es el ciclo de ingresos; hoy no hay agente nativo en ningún CRM chileno y la cotización y la promesa son manuales.
- Prueba independiente: un lead de prueba recorre calificación, visita, cotización, reserva pagada y promesa firmada sin planilla externa, en menos de 48 horas de tiempo de proceso.
- Escenarios de aceptación:
  1. Dado un mensaje de WhatsApp de un interesado, cuando el agente responde, entonces en menos de 2 minutos tiene presupuesto, plazo y tipo de unidad y propone horario de visita.
  2. Dada una unidad disponible, cuando el ejecutivo genera cotización, entonces el documento sale con precio vigente, pie, financiamiento estimado y vence a una fecha.
  3. Dada una cotización aceptada, cuando el cliente paga la reserva por Webpay, entonces la unidad queda bloqueada y se emite boleta o comprobante.
  4. Dada una reserva pagada, cuando se envía la promesa, entonces el cliente firma electrónicamente y el documento queda archivado con la unidad.

**Historia 2 (P2): Cobranza y postventa con agente**

Tras la promesa, el sistema controla el calendario de pagos del pie, recuerda cuotas por WhatsApp, concilia pagos y, tras la entrega, recibe y gestiona solicitudes de postventa con un agente que clasifica, asigna y hace seguimiento.

- Por qué P2: cobranza y postventa son el dolor crónico de las inmobiliarias chilenas y ningún proveedor local tiene IA en postventa.
- Prueba independiente: 20 clientes con cuotas pendientes reciben recordatorios, 10 solicitudes de postventa se clasifican y asignan sin intervención manual.
- Escenarios de aceptación:
  1. Dada una cuota que vence en 5 días, cuando corre el agente, entonces envía recordatorio con monto y link de pago, y registra la gestión.
  2. Dado un pago recibido, cuando se concilia, entonces el estado de la cuota cambia y el cliente recibe comprobante.
  3. Dada una solicitud de postventa por WhatsApp con foto, cuando el agente la recibe, entonces la clasifica (urgente, garantía, no cubierta), la asigna y responde plazo estimado.
  4. Dada una solicitud sin respuesta del responsable en 72 horas, cuando vence, entonces el agente escala al jefe de postventa.

**Historia 3 (P3): Asistente de obra ligero: avance y compras para la constructora mediana**

El jefe de obra reporta avance por WhatsApp (texto, foto, voz); el asistente lo estructura contra el presupuesto por partida, detecta desvíos y prepara solicitudes de compra que el administrador aprueba.

- Por qué P3: Procore y ALICE son enterprise sin precio público; una constructora mediana necesita algo que funcione desde WhatsApp. Es el puente hacia `004`.
- Prueba independiente: 4 semanas de reportes diarios producen una curva de avance por partida con desvío calculado, y 5 solicitudes de compra aprobadas por WhatsApp.
- Escenarios de aceptación:
  1. Dado un reporte por voz del jefe de obra, cuando el asistente lo procesa, entonces registra partida, porcentaje de avance y evidencia fotográfica con fecha y ubicación.
  2. Dado un avance inferior al programado en más de 10 %, cuando se calcula, entonces se alerta al administrador con la partida y el impacto estimado.
  3. Dada una necesidad de material declarada, cuando el asistente prepara la solicitud de compra, entonces incluye cantidad, proveedor habitual y precio de referencia, y espera aprobación.

**Casos borde**

- Dos ejecutivos cotizan la misma unidad: la primera reserva pagada bloquea; la otra cotización se invalida y se avisa.
- Lead que contacta por dos canales: se fusiona en un solo registro, sin duplicar seguimiento.
- Pago de reserva aprobado y promesa no firmada en el plazo: la unidad se libera con aviso y el pago se reembolsa según política.
- Solicitud de postventa fuera de garantía: el agente responde con la política, no la rechaza solo.
- Reporte de obra contradictorio con el anterior (avance que retrocede): se marca para revisión humana, no se sobreescribe.

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
| FR-010 | Registrar avance de obra por partida desde WhatsApp (texto, voz, foto) con fecha, ubicación y evidencia | H3 |
| FR-011 | Comparar avance real contra programado y presupuesto por partida, y alertar desvíos superiores a un umbral configurable | H3 |
| FR-012 | Preparar solicitudes de compra con cantidad, proveedor y precio de referencia, para aprobación humana | H3 |
| FR-013 | Registrar toda acción de agente en el ledger inmutable con evidencia y aprobador | Todas |
| FR-014 | Operar sobre el core compartido (identidad, catálogo, transacciones, pagos, gastos) sin duplicarlo | Todas |

**Entidades clave**

- Proyecto: nombre, ubicación, etapas, unidades, estado comercial y de obra.
- Unidad: tipo, superficie, precio vigente, estado, reserva, promesa, escritura.
- Lead y Cliente: origen, canal, calificación, ejecutivo, historial de contacto.
- Cotización: unidad, precio, pie, financiamiento, vencimiento, estado.
- Reserva y Promesa: pagos, documentos firmados, plazos.
- Calendario de pagos y Cuota: monto, vencimiento, estado, conciliación.
- Solicitud de postventa: unidad, tipo, clasificación, responsable, plazo, estado.
- Partida de obra y Reporte de avance: presupuesto, programado, real, evidencia.
- Solicitud de compra: partida, material, cantidad, proveedor, aprobador.
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
| SC-008 | El avance de obra por partida está disponible sin planilla y con desvío calculado el mismo día del reporte |
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

- [ ] &#91;NEEDS CLARIFICATION\] ¿Cuántos proyectos y unidades activas hoy, y en qué etapa (verde, blanco, entrega)?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Qué CRM o planillas usan hoy y qué historial se migra?
- [ ] &#91;NEEDS CLARIFICATION\] ¿La reserva es con pago en línea obligatorio o se acepta transferencia? Afecta FR-005 y el bloqueo de unidad.
- [ ] &#91;NEEDS CLARIFICATION\] ¿Quién redacta y aprueba la promesa (abogado interno o externo) y cuál es el plazo máximo entre reserva y promesa?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Política de postventa: plazos de garantía por tipo de falla y responsables?
- [ ] &#91;NEEDS CLARIFICATION\] ¿La constructora ejecuta solo obras propias o también para terceros? Afecta el alcance de `004`.
- [ ] &#91;NEEDS CLARIFICATION\] ¿Límite monetario para que el asistente prepare compras sin revisión del administrador?

## 6. Plan técnico resumido (vista previa de `plan.md`)

**Contexto técnico**

- Misma base que `001` y `002`: Python 3.12 + FastAPI, Next.js, PostgreSQL 16, Redis. Se agrega almacenamiento de documentos (promesas, fotos de obra) con cifrado en reposo.
- Agentes: Claude Agent SDK con herramientas MCP sobre leads, unidades, cotizaciones, cuotas y solicitudes; agente de calificación, agente de cobranza, agente de postventa, asistente de obra (voz a texto para reportes).
- Integraciones: WhatsApp Business API, Transbank Webpay Plus, Mercado Pago, SII, firma electrónica avanzada, conectores de portales (correo parseado o API), calendario de ejecutivos.
- Pruebas: pytest + Playwright; conversaciones versionadas para cada agente; pruebas de concurrencia para el bloqueo de unidades.
- Rendimiento: primera respuesta del agente en menos de 2 min; cotización generada en menos de 10 s; portal de cliente en menos de 1 s.
- Escala: 5 proyectos, 200 unidades, 500 leads al mes, 50 solicitudes de postventa al mes.

**Chequeo de constitución**

| Principio | Cumple | Nota |
| --- | --- | --- |
| Core primero | Sí | Proyecto, Unidad, Cotización, Promesa, Partida son de la vertical; identidad, pagos, gastos y ledger del core |
| Chile es requisito | Sí | Webpay, SII y firma electrónica Ley 19.799 en H1 |
| Agente con reglas | Sí | Calificación y recordatorios autónomos; cotización, promesa, compras y rechazo de garantía requieren humano |
| Seguridad desde la spec | Pendiente | Datos financieros y de identidad de compradores (Ley 21.719); documentos firmados; prompt injection por WhatsApp |
| Test primero | Sí | Escenarios de §2 |
| Simplicidad | Con justificación | Cuatro agentes en lugar de uno: cada uno tiene reglas y permisos distintos; se registra en Complexity Tracking |

**Estructura**

```
plataforma-salman/
  core/
  verticales/inmobiliaria/
    api/           # proyectos, unidades, leads, cotizaciones, promesas, cuotas, postventa
    web/           # panel comercial, portal de cliente, dashboard
    agentes/       # calificacion, cobranza, postventa, asistente-obra
  verticales/constructora/   # feature 004, V2
  specs/003-inmobiliaria-comercial/
    spec.md  plan.md  research.md  data-model.md  contracts/  quickstart.md  tasks.md  checklists/
```

## 7. Próximos comandos y entregables por fase

1. `/speckit.specify` con §2 a §5 → `spec.md` + `checklists/requirements.md`.
2. `/speckit.clarify` → responder las siete preguntas de §5; la de proyectos activos y la de reserva con pago son bloqueantes.
3. `/speckit.plan` con §6 → `plan.md`; `research.md` decide proveedor de firma electrónica y método de captura de portales; `data-model.md`; `contracts/` (OpenAPI de leads, unidades, cotizaciones, cuotas, postventa); `quickstart.md`.
4. `/speckit.checklist` → lista de calidad para bloqueo de unidades, promesa y reglas de los cuatro agentes.
5. `/speckit.tasks` → `tasks.md`: Setup → Fundacional (proyectos y unidades) → H1 → H2 → H3 → Pulido.
6. `/speckit.analyze` → corregir y repetir.
7. `/speckit.implement` por fase; H1 con un proyecto real y un ejecutivo piloto.
8. `/speckit.converge` hasta convergencia; pentest de agentes antes del cierre.
9. Abrir `004-constructora-obra` con `/speckit.specify` cuando H3 lleve 4 semanas en operación.
