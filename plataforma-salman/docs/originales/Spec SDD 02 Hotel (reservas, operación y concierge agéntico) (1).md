# Spec SDD 02: Hotel (reservas, operación y concierge agéntico)

Oct 15, 2026 · @Cristóbal Herrera

## 0. Flujo spec-kit aplicado

Este documento es el `spec.md` de la feature `002-hotel-reservas-concierge`, segunda vertical sobre el core compartido. Sigue la ruta completa de [spec-kit](https://github.github.com/spec-kit/quickstart.html) (`constitution` → `specify` → `clarify` → `plan` → `checklist` → `tasks` → `analyze` → `implement` → `converge`) y reutiliza la constitución versión 1.0.0 definida en el Spec SDD 01 (Cafetería); no se redefine aquí. La spec dice qué y por qué; la tecnología va en `plan.md`.

Precondición de esta feature: el core (`000-core`) y el módulo de pedidos de la cafetería (`001`) están en producción, porque el servicio a la habitación los reutiliza.

## 2. Escenarios de usuario y pruebas (obligatorio)

La P1 reemplaza la dispersión actual con un solo punto de verdad para reservas; P2 y P3 construyen la operación y el agente sobre ese dato.

**Historia 1 (P1): Reservar y pagar desde la web del hotel**

Un huésped entra a la web, ve disponibilidad y tarifa real, reserva, paga con Webpay o Mercado Pago y recibe confirmación y boleta SII. El inventario se actualiza en todos los canales (Booking, Airbnb) sin intervención manual.

- Por qué P1: hoy todo está disperso; la reserva directa con inventario único es la base de todo lo demás y reduce comisión OTA.
- Prueba independiente: dos reservas simultáneas de la última habitación no generan sobreventa; el calendario de Booking refleja el cambio en menos de 5 minutos.
- Escenarios de aceptación:
  1. Dadas fechas y número de huéspedes, cuando el visitante consulta, entonces ve solo habitaciones disponibles con tarifa vigente y total con IVA.
  2. Dada una reserva con pago aprobado, cuando Webpay confirma, entonces se emite confirmación por correo y WhatsApp y boleta SII en menos de 60 segundos.
  3. Dada una reserva directa confirmada, cuando el channel manager sincroniza, entonces la disponibilidad baja en todos los canales conectados en menos de 5 minutos.
  4. Dada una reserva de Booking, cuando llega por el canal, entonces aparece en el PMS propio con los mismos datos y bloquea inventario.

**Historia 2 (P2): Operar la estadía: check-in digital, pedidos a la habitación y housekeeping**

El huésped hace check-in desde el celular antes de llegar (datos, documento, pago pendiente), pide servicios a la habitación con el mismo módulo de pedidos de la cafetería y el personal ve tareas de limpieza y mantención por habitación.

- Por qué P2: convierte la reserva en operación; reutiliza el módulo de pedidos ya probado en `001`.
- Prueba independiente: un huésped completa check-in, pide desayuno a la habitación y lo recibe cargado a su cuenta sin pasar por recepción.
- Escenarios de aceptación:
  1. Dado un check-in online completo, cuando el huésped llega, entonces recepción solo entrega la llave y el registro queda firmado.
  2. Dado un pedido a la habitación, cuando se confirma, entonces aparece en cocina con número de habitación y se carga a la cuenta del huésped.
  3. Dado un check-out, cuando la habitación se libera, entonces se crea la tarea de limpieza y la habitación no vuelve a estar disponible hasta que se cierre.
  4. Dado un cargo pendiente al check-out, cuando el huésped paga, entonces se emite boleta o factura por el total de la estadía.

**Historia 3 (P3): Concierge agéntico por WhatsApp con reglas de autonomía**

Un agente atiende por el WhatsApp del hotel: responde, cotiza, reserva, modifica fechas dentro de reglas, vende upsells con link de pago y escala a un humano cuando sale de su límite. Toda acción queda en el ledger.

- Por qué P3: es el diferenciador frente a la industria (sección 2 del estado del arte), pero depende del PMS propio (H1) y la operación (H2).
- Prueba independiente: 50 conversaciones de prueba resueltas sin humano en al menos el 70 % y cero cambios fuera de reglas.
- Escenarios de aceptación:
  1. Dada una consulta de disponibilidad por WhatsApp, cuando el agente responde, entonces cotiza con tarifa real y ofrece link de pago en menos de 30 segundos.
  2. Dado un cambio de fechas dentro de la política (sin penalidad), cuando el huésped lo pide, entonces el agente lo ejecuta en el PMS y confirma.
  3. Dado un cambio con penalidad o cancelación, cuando se solicita, entonces el agente escala a recepción con el contexto completo y no actúa.
  4. Dada una reserva pagada 48 horas antes de llegar, cuando corre el agente, entonces ofrece un upsell (late check-out, desayuno) con link de pago.

**Casos borde**

- Reserva doble por carrera entre canal directo y OTA: gana la primera confirmada; la segunda se relocaliza y se avisa.
- Pago aprobado pero boleta rechazada por SII: la reserva se mantiene, la boleta se reintenta y se alerta.
- Huésped sin documento válido en check-in online: el registro queda incompleto y se exige en recepción.
- Agente que recibe lenguaje ofensivo o solicitud ambigua: cierra con escalamiento, nunca inventa tarifa.
- Caída del channel manager: la web propia sigue vendiendo con inventario local y marca conflicto al reconectar.

## 3. Requisitos (obligatorio)

**Requisitos funcionales**

| ID | El sistema DEBE | Historia |
| --- | --- | --- |
| FR-001 | Mantener un inventario único de habitaciones con tarifas por fecha, ocupación y política de cancelación | H1 |
| FR-002 | Exponer un motor de reservas en la web propia con disponibilidad real y pago en línea | H1 |
| FR-003 | Sincronizar disponibilidad y reservas con al menos Booking y Airbnb en ambos sentidos | H1 |
| FR-004 | Cobrar por Webpay/Transbank o Mercado Pago y emitir boleta o factura SII por cada pago | H1 |
| FR-005 | Impedir sobreventa ante reservas concurrentes del mismo inventario | H1 |
| FR-006 | Permitir check-in online con datos del huésped, documento y firma de registro | H2 |
| FR-007 | Reutilizar el módulo de pedidos del core para servicio a la habitación, con cargo a la cuenta del huésped | H2 |
| FR-008 | Generar y cerrar tareas de housekeeping y mantención por habitación y estado | H2 |
| FR-009 | Consolidar todos los cargos de la estadía en una cuenta y liquidarla al check-out | H2 |
| FR-010 | Atender por WhatsApp Business con un agente que consulta y escribe en el PMS vía API | H3 |
| FR-011 | Aplicar reglas de autonomía configurables: acciones permitidas, montos máximos, casos que escalan | H3 |
| FR-012 | Ofrecer upsells con link de pago en momentos definidos (pre-llegada, estadía, salida) | H3 |
| FR-013 | Registrar cada acción del agente en el ledger inmutable con evidencia de la conversación | H3 |
| FR-014 | Exponer disponibilidad y tarifas por un servidor MCP para agentes externos (modelo SiteMinder) | H3 |
| FR-015 | Operar sobre el core compartido (identidad, catálogo, transacciones, pagos, gastos) sin duplicarlo | Todas |

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
| SC-004 | El 100 % de los pagos tienen boleta o factura SII emitida en menos de 60 segundos |
| SC-005 | El 60 % de los huéspedes completa check-in online antes de llegar |
| SC-006 | El agente resuelve al menos el 70 % de conversaciones de WhatsApp sin intervención humana |
| SC-007 | Cero acciones del agente fuera de sus reglas de autonomía (auditoría mensual del ledger) |
| SC-008 | Los upsells ofrecidos por el agente convierten al menos el 8 % (referencia Duve) |
| SC-009 | Un empleado nuevo opera recepción con el sistema tras 2 horas de capacitación |

## 5. Supuestos, dependencias y clarificaciones

**Supuestos**

- Hotel de menos de 50 habitaciones, un solo edificio, sin PMS actual o con uno que se abandona.
- Los canales OTA relevantes son Booking y Airbnb; otros se agregan después.
- La cocina y el servicio a la habitación comparten operación con la cafetería o replican su módulo.
- Recepción opera con horario; fuera de horario el agente es el primer contacto.

**Dependencias**

- Core (`000-core`) y módulo de pedidos (`001`) en producción.
- Channel manager propio o integrado (evaluar en `research.md`: construir conector vs. contratar uno con API).
- Certificado SII, contrato Webpay Plus, cuenta WhatsApp Business API con plantillas aprobadas.
- Credenciales de partner de Booking y Airbnb (requieren proceso de certificación).

**Clarificaciones pendientes** (para `/speckit.clarify`)

- [ ] &#91;NEEDS CLARIFICATION\] ¿Cuántas habitaciones y tipos tiene el hotel, y hay temporada alta definida? Define tarifas y escala.
- [ ] &#91;NEEDS CLARIFICATION\] ¿Qué canales usan hoy y con qué volumen? Define el alcance de FR-003.
- [ ] &#91;NEEDS CLARIFICATION\] ¿Existe PMS actual con datos a migrar o se parte de cero?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Política de cancelación y de cobro anticipado (total, parcial, garantía)?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Se emite factura a empresas con frecuencia? Define si FR-004 incluye factura desde V1.
- [ ] &#91;NEEDS CLARIFICATION\] ¿Límite monetario del agente para ejecutar sin aprobación (por ejemplo, cambios sin penalidad hasta X pesos)?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Housekeeping con personal propio o externo? Define acceso y notificaciones.

## 6. Plan técnico resumido (vista previa de `plan.md`)

**Contexto técnico**

- Misma base que `001`: Python 3.12 + FastAPI, Next.js, PostgreSQL 16, Redis; se agrega un worker de sincronización de canales con cola y reintentos.
- Agentes: Claude Agent SDK con herramientas MCP sobre el PMS propio (disponibilidad, reservas, cuenta) y servidor MCP público de solo lectura para distribución (FR-014).
- Integraciones: Transbank Webpay Plus, Mercado Pago, SII, WhatsApp Business API, Booking Connectivity API y Airbnb API (o channel manager intermedio según `research.md`).
- Pruebas: pytest + Playwright; pruebas de concurrencia para FR-005; conversaciones de prueba versionadas para H3.
- Rendimiento: consulta de disponibilidad en menos de 1 s; sincronización de canales en menos de 5 min; respuesta del agente en menos de 30 s.
- Escala: 50 habitaciones, 200 reservas al mes, 1.000 conversaciones al mes; multi-propiedad en el modelo de datos.

**Chequeo de constitución**

| Principio | Cumple | Nota |
| --- | --- | --- |
| Core primero | Sí | Habitación, Tarifa, Reserva y Canal son de la vertical; identidad, pagos, pedidos y cuenta vienen del core |
| Chile es requisito | Sí | SII y Webpay en H1; factura según clarificación |
| Agente con reglas | Sí | FR-011 define autonomía; cancelaciones siempre escalan |
| Seguridad desde la spec | Pendiente | Modelo de amenazas: datos de huéspedes (Ley 21.719), credenciales OTA, prompt injection vía WhatsApp |
| Test primero | Sí | Escenarios de §2 y pruebas de concurrencia |
| Simplicidad | Con justificación | El worker de canales es un proceso aparte por aislamiento de fallos; se registra en Complexity Tracking |

**Estructura**

```
plataforma-salman/
  core/
  verticales/hotel/
    api/           # habitaciones, tarifas, reservas, cuenta de estadía, housekeeping
    web/           # motor de reservas, check-in online, recepción, dashboard
    canales/       # worker de sincronización Booking / Airbnb
    agentes/       # concierge WhatsApp, upsell, servidor MCP de distribución
  specs/002-hotel-reservas-concierge/
    spec.md  plan.md  research.md  data-model.md  contracts/  quickstart.md  tasks.md  checklists/
```

## 7. Próximos comandos y entregables por fase

1. `/speckit.specify` con §2 a §5 → `spec.md` + `checklists/requirements.md` (la constitución ya existe).
2. `/speckit.clarify` → responder las siete preguntas de §5; la de canales y la de PMS actual son bloqueantes para el plan.
3. `/speckit.plan` con §6 → `plan.md`; `research.md` decide construir conector vs. channel manager con API; `data-model.md`; `contracts/` (OpenAPI de reservas, cuenta, MCP de distribución); `quickstart.md`.
4. `/speckit.checklist` → lista de calidad para sobreventa, pagos y reglas del agente.
5. `/speckit.tasks` → `tasks.md`: Setup → Fundacional (inventario y tarifas) → H1 → H2 → H3 → Pulido.
6. `/speckit.analyze` → corregir y repetir.
7. `/speckit.implement` por fase; H1 con un canal real antes de sumar el segundo.
8. `/speckit.converge` hasta convergencia; pentest del agente (prompt injection por WhatsApp, fuga de datos de huéspedes) antes del cierre.
