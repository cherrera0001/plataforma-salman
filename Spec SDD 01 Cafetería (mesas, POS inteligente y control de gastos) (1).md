# Spec SDD 01: Cafetería (mesas, POS inteligente y control de gastos)

Oct 15, 2026 · @Cristóbal Herrera

## 0. Flujo spec-kit aplicado a este proyecto

Este documento es el `spec.md` de la feature `001-cafeteria-mesas-pos`, escrito según la ruta completa de [spec-kit](https://github.github.com/spec-kit/quickstart.html): `/speckit.constitution` → `/speckit.specify` → `/speckit.clarify` → `/speckit.plan` → `/speckit.checklist` → `/speckit.tasks` → `/speckit.analyze` → `/speckit.implement` → `/speckit.converge`. La spec dice qué y por qué; la tecnología va en `plan.md`.

| Paso | Comando | Produce | Estado hoy |
| --- | --- | --- | --- |
| 1 | `/speckit.constitution` | `.specify/memory/constitution.md` (una sola para core + 3 verticales) | Borrador en §1 |
| 2 | `/speckit.specify` | `specs/001-cafeteria-mesas-pos/spec.md` + `checklists/requirements.md` | Este doc (§2 a §5) |
| 3 | `/speckit.clarify` | Preguntas sobre áreas subespecificadas, respuestas incorporadas a `spec.md` | Pendientes en §5 |
| 4 | `/speckit.plan` | `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` | Resumen en §6 |
| 5 | `/speckit.checklist` | Listas de calidad de requisitos, marcadas por el revisor | Por generar |
| 6 | `/speckit.tasks` | `tasks.md` ordenado por dependencias, agrupado por historia | Por generar |
| 7 | `/speckit.analyze` | Informe de conflictos entre spec, plan y tasks (solo lectura) | Por correr |
| 8 | `/speckit.implement` | Ejecuta `tasks.md` por fases; lee las checklists como gate | Por correr |
| 9 | `/speckit.converge` | Compara código contra spec, plan y tasks; añade brechas como tareas | Por correr |

Setup: `uv tool install specify-cli`, luego `specify init plataforma-salman --integration claude`. El estado de feature activa vive en `.specify/feature.json`; con la extensión git se crean ramas numeradas (`001-cafeteria-mesas-pos`).

## 1. Constitución (compartida por el core y las tres verticales)

Una sola constitución para el monorepo `plataforma-salman`; cada `plan.md` debe pasar el «Constitution Check» contra estos principios. Versión 1.0.0 (2026-10-15).

1. **Core primero, vertical después.** Identidad, catálogo, transacciones, pagos, gastos y analítica viven en `core/`; una vertical solo agrega lo que ninguna otra necesita. Toda duplicación entre verticales se justifica por escrito en `plan.md` (Complexity Tracking).
2. **Chile es requisito, no localización.** Boleta electrónica SII emitida al confirmar pago, cobro por Webpay/Transbank o Mercado Pago, coma decimal y pesos sin decimales. Ninguna historia se declara completa sin estos tres.
3. **Agente que ejecuta bajo reglas explícitas.** Todo agente declara qué acciones hace solo, cuáles requieren aprobación humana y cuál es su límite monetario. Cada acción queda en un ledger inmutable (quién, qué, cuándo, con qué evidencia). Sin reglas, el agente solo informa.
4. **Seguridad desde la spec.** Cada feature incluye modelo de amenazas resumido en `plan.md`, pentest de la capa agéntica antes de `/speckit.converge` final, y los datos personales se tratan según Ley 21.719 (encargado de tratamiento cuando aplique).
5. **Test primero, dato real.** Las historias se aceptan con escenarios Given/When/Then automatizados; se prohíbe dato sintético en demos a cliente. `tasks.md` ordena pruebas antes de implementación en cada historia.
6. **Simplicidad y observabilidad.** YAGNI; una aplicación por vertical sobre el core; logs estructurados, métricas de negocio expuestas desde el día 1 (ventas por hora, margen, latencia de agente).

Gobernanza: cambios a la constitución requieren bump de versión semántica, nota de migración y aprobación de Cristóbal Herrera; `/speckit.analyze` reporta como CRITICAL cualquier violación.

## 2. Escenarios de usuario y pruebas (obligatorio)

Cada historia es independiente, testeable sola y entrega valor por sí misma; la P1 es el MVP demostrable.

**Historia 1 (P1): Pedir y pagar desde la mesa**

Un cliente escanea el QR de su mesa, ve la carta digital ya existente, arma su pedido (individual o compartido), lo envía a cocina y paga su parte con Webpay o Mercado Pago. Recibe boleta SII digital por WhatsApp o correo.

- Por qué P1: es el dolor visible (sin sistema de mesas) y el que genera los datos que alimentan todo lo demás.
- Prueba independiente: una mesa con dos clientes puede pedir, dividir y pagar sin tocar eleventa ni la caja.
- Escenarios de aceptación:
  1. Dado un QR de mesa activo, cuando el cliente abre la carta y confirma un pedido, entonces el pedido aparece en cocina con número de mesa y hora en menos de 5 segundos.
  2. Dado un pedido compartido de dos personas, cuando cada una elige «pagar lo mío», entonces cada una paga solo sus ítems y la mesa queda cerrada cuando el saldo es cero.
  3. Dado un pago aprobado, cuando Webpay confirma, entonces se emite la boleta electrónica y se envía al canal elegido antes de 30 segundos.
  4. Dado un pago rechazado, cuando el cliente reintenta, entonces el pedido se mantiene y no se duplica en cocina.

**Historia 2 (P2): Control de gastos e inventario con margen por producto**

El administrador registra compras (foto de factura o carga manual), el sistema descuenta insumos por receta a medida que se venden y muestra margen real por producto y por día.

- Por qué P2: es la «inteligencia de datos» que eleventa no entrega y la base del agente de compras.
- Prueba independiente: cargar 10 facturas y 1 día de ventas devuelve margen por producto con error menor al 2 % contra cálculo manual.
- Escenarios de aceptación:
  1. Dada una receta con 4 insumos, cuando se vende una unidad, entonces el stock de cada insumo baja según la receta.
  2. Dada una factura de proveedor fotografiada, cuando se procesa, entonces las líneas quedan registradas como gasto con proveedor, monto y fecha, pendientes de aprobación.
  3. Dado el cierre de día, cuando el administrador abre el dashboard, entonces ve ventas, costo, margen y los 5 productos con peor margen.

**Historia 3 (P3): Agente que sugiere reposición y alerta anomalías**

Un agente revisa stock, ventas y mermas, propone una orden de compra semanal al proveedor habitual y alerta anulaciones o descuentos fuera de patrón. Nunca compra solo: el administrador aprueba por WhatsApp.

- Por qué P3: valor alto pero depende de datos limpios de las historias 1 y 2.
- Prueba independiente: con 4 semanas de datos, la orden sugerida cubre la demanda sin quiebres ni sobre-stock superior al 15 %.
- Escenarios de aceptación:
  1. Dado stock bajo mínimo proyectado a 7 días, cuando corre el agente, entonces envía una propuesta de orden con cantidades y costo estimado para aprobar.
  2. Dada una anulación de venta superior a 3 veces el promedio diario, cuando ocurre, entonces el administrador recibe alerta con detalle en menos de 1 minuto.
  3. Dada una propuesta no aprobada en 48 horas, cuando vence, entonces el agente la archiva y lo registra en el ledger.

**Casos borde**

- Caída de internet en el local: el pedido tomado por QR debe quedar en cola y la caja seguir operando en modo degradado.
- Mesa que se junta o se divide a mitad del servicio.
- Cliente que cierra el navegador antes de pagar: el pedido sigue en cocina y pasa a cobro en caja.
- Rechazo de boleta por el SII (folio agotado o certificado vencido): el pago no se revierte; la boleta se reintenta y se alerta.
- Producto de la carta sin receta cargada: se vende, pero el margen se marca como «sin costo» y aparece en el dashboard.

## 3. Requisitos (obligatorio)

**Requisitos funcionales**

| ID | El sistema DEBE | Historia |
| --- | --- | --- |
| FR-001 | Generar un QR único por mesa que abra la carta digital existente sin instalar app | H1 |
| FR-002 | Permitir pedidos individuales y compartidos por mesa, con edición hasta el envío a cocina | H1 |
| FR-003 | Mostrar cada pedido en una pantalla de cocina (KDS) con mesa, hora y estado | H1 |
| FR-004 | Cobrar por Webpay/Transbank y Mercado Pago, con división de cuenta por ítem o por partes iguales | H1 |
| FR-005 | Emitir boleta electrónica SII al confirmar cada pago y entregarla por WhatsApp, correo o QR | H1 |
| FR-006 | Mantener operación de caja en modo degradado sin internet y sincronizar al reconectar | H1 |
| FR-007 | Registrar compras y gastos desde foto de factura o carga manual, con estado pendiente/aprobado | H2 |
| FR-008 | Descontar insumos por receta en cada venta y mantener stock proyectado | H2 |
| FR-009 | Calcular margen por producto, por día y por franja horaria, y exponerlo en un dashboard | H2 |
| FR-010 | Importar el histórico de ventas y stock desde la exportación a Excel de eleventa | H2 |
| FR-011 | Proponer órdenes de compra con cantidades y costo estimado, para aprobación humana por WhatsApp | H3 |
| FR-012 | Alertar anulaciones, descuentos o mermas fuera de patrón en menos de 1 minuto | H3 |
| FR-013 | Registrar toda acción de agente en un ledger inmutable con evidencia y aprobador | H3 |
| FR-014 | Operar sobre el core compartido (identidad, catálogo, transacciones, pagos, gastos) sin duplicarlo | Todas |

**Entidades clave**

- Mesa: identificador, QR, estado (libre, ocupada, por cerrar), pedidos asociados.
- Pedido: mesa, comensal, ítems, estado (borrador, enviado, preparado, servido), pagos.
- Producto y Receta: producto de carta, insumos con cantidades, costo calculado.
- Insumo y Movimiento de stock: unidad, stock actual, entradas por compra, salidas por venta o merma.
- Compra y Gasto: proveedor, documento, líneas, estado de aprobación.
- Pago y Documento tributario: medio, monto, estado, folio SII, canal de entrega.
- Acción de agente: tipo, propuesta, aprobador, resultado, evidencia.

## 4. Criterios de éxito (obligatorio)

Medibles, agnósticos de tecnología, verificables sin leer código.

| ID | Resultado medible |
| --- | --- |
| SC-001 | El 90 % de los pedidos por QR llegan a cocina en menos de 5 segundos |
| SC-002 | El tiempo de cierre de cuenta por mesa baja al menos 30 % frente a la medición previa con eleventa |
| SC-003 | El 100 % de los pagos aprobados tienen boleta SII emitida en menos de 30 segundos |
| SC-004 | El margen por producto calculado difiere menos del 2 % del cálculo manual mensual |
| SC-005 | El inventario proyectado difiere menos del 5 % del conteo físico semanal |
| SC-006 | Las órdenes sugeridas por el agente evitan quiebres de stock en al menos el 95 % de los insumos críticos |
| SC-007 | Cero acciones de agente sin registro en el ledger (auditoría mensual) |
| SC-008 | El administrador obtiene el dashboard diario sin planilla manual en menos de 1 minuto |

## 5. Supuestos, dependencias y clarificaciones

**Supuestos**

- La carta digital existente es editable y exportable (JSON o similar); si no, se migra una vez.
- Eleventa convive en V1 solo como caja de respaldo; el histórico sale por su exportación a Excel.
- Un solo local, una cocina, hasta 30 mesas; no hay delivery en V1.
- Hay conexión a internet estable con fallos ocasionales menores a 30 minutos.

**Dependencias**

- Core compartido: identidad, catálogo, transacciones, pagos, gastos (feature `000-core`).
- Certificado digital SII del contribuyente y contrato Webpay Plus o Mercado Pago activos.
- Cuenta WhatsApp Business API para entrega de boleta y aprobaciones del agente.

**Clarificaciones pendientes** (para `/speckit.clarify`)

- [ ] &#91;NEEDS CLARIFICATION\] ¿El cliente paga antes de recibir (modelo café) o después (modelo restaurante)? Cambia el flujo de H1.
- [ ] &#91;NEEDS CLARIFICATION\] ¿Propina incluida en el flujo de pago y con qué porcentaje por defecto?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Quién aprueba compras: dueño, administrador o ambos según monto?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Se reemplaza eleventa en V1 o convive? Define si FR-006 es caja propia o puente.
- [ ] &#91;NEEDS CLARIFICATION\] ¿Cuenta personal del cliente (perfil persistente) o solo pago por sesión de mesa?
- [ ] &#91;NEEDS CLARIFICATION\] ¿Proveedores con catálogo digital para la orden de compra o solo WhatsApp?

## 6. Plan técnico resumido (vista previa de `plan.md`)

Lo que sigue es la propuesta para `/speckit.plan`; la decisión final queda en `plan.md` tras `research.md`.

**Contexto técnico**

- Lenguaje y framework: Python 3.12 + FastAPI para el core y la API; Next.js para carta QR, KDS y dashboard; PostgreSQL 16 como almacenamiento; Redis para cola de pedidos y modo degradado.
- Agentes: Claude Agent SDK con herramientas MCP sobre el core (stock, ventas, compras) y servidor MCP propio para Webpay y SII.
- Integraciones: Transbank Webpay Plus, Mercado Pago, SII (boleta electrónica vía proveedor certificado o integración directa), WhatsApp Business API.
- Pruebas: pytest + Playwright; escenarios Given/When/Then de §2 como suite de aceptación.
- Plataforma objetivo: web responsive; tablet en cocina; sin app nativa.
- Rendimiento: pedido a cocina en menos de 5 s; dashboard diario en menos de 1 s para 1 año de datos.
- Escala: 1 local, 30 mesas, 500 pedidos al día; diseño multi-tenant para los siguientes.

**Chequeo de constitución**

| Principio | Cumple | Nota |
| --- | --- | --- |
| Core primero | Sí | Mesa, Pedido y Receta son de la vertical; todo lo demás es core |
| Chile es requisito | Sí | SII y Webpay en H1 |
| Agente con reglas | Sí | H3 solo propone; aprobación humana por WhatsApp |
| Seguridad desde la spec | Pendiente | Modelo de amenazas de QR y pagos antes de `/speckit.tasks` |
| Test primero | Sí | Escenarios de §2 |
| Simplicidad | Sí | Una app vertical sobre el core; sin microservicios |

**Estructura**

```
plataforma-salman/
  core/            # identidad, catálogo, transacciones, pagos, gastos, analítica
  verticales/cafeteria/
    api/           # mesas, pedidos, recetas, KDS
    web/           # carta QR, KDS, dashboard
    agentes/       # reposición, anomalías
  specs/001-cafeteria-mesas-pos/
    spec.md  plan.md  research.md  data-model.md  contracts/  quickstart.md  tasks.md  checklists/
```

## 7. Próximos comandos y entregables por fase

1. `/speckit.constitution` con los seis principios de §1 → `.specify/memory/constitution.md` (una vez, compartida).
2. `/speckit.specify` con §2 a §5 como entrada → `spec.md` + `checklists/requirements.md`.
3. `/speckit.clarify` → responder las seis preguntas de §5 y actualizar la spec.
4. `/speckit.plan` con §6 como entrada → `plan.md`, `research.md` (SII, Webpay, WhatsApp API), `data-model.md`, `contracts/` (OpenAPI de mesas, pedidos, pagos), `quickstart.md`.
5. `/speckit.checklist` → lista de calidad para pagos y SII; el revisor marca.
6. `/speckit.tasks` → `tasks.md` por historia: Setup → Fundacional → H1 → H2 → H3 → Pulido.
7. `/speckit.analyze` → corregir conflictos en la fuente y repetir.
8. `/speckit.implement` por fase (H1 primero, demo en local real).
9. `/speckit.converge` hasta que no agregue tareas; pentest de la capa agéntica antes del cierre.
