# Especificación — Cafetería

Feature: `001-cafeteria-mesas-pos`. Fecha: 2026-10-16. Estado: **BLOCKED** para implementación.
Fuente: CAF §2–5; copia conservada en docs/originales. Todos los FR y SC son **REQUISITOS PROPUESTOS**, pendientes de ratificación. Los resultados numéricos son objetivos; no se han medido.

## Problema, actores y límites

Un local y sin delivery son supuestos por validar. No se implementa caja offline ni migración hasta definir el sistema de registro.

Actores: cliente, comensal, cocina, caja y administrador. Las responsabilidades de aprobación no se transfieren al modelo.

## 2. Escenarios de usuario y pruebas (obligatorio)

Cada historia es independiente, testeable sola y entrega valor por sí misma; la P1 es el MVP demostrable.

**Historia 1 (P1): Pedir y pagar desde la mesa**

Un cliente escanea el QR de su mesa, ve la carta digital ya existente, arma su pedido (individual o compartido), lo envía a cocina y paga su parte con Webpay o Mercado Pago. Recibe la representación del documento tributario aplicable por el canal elegido, según política aprobada.

- Por qué P1: es el dolor visible (sin sistema de mesas) y el que genera los datos que alimentan todo lo demás.
- Prueba independiente: una mesa con dos clientes puede pedir, dividir y pagar sin tocar eleventa ni la caja.
- Escenarios de aceptación:
  1. Dado un QR de mesa activo, cuando el cliente abre la carta y confirma un pedido, entonces el pedido aparece en cocina con número de mesa y hora en menos de 5 segundos.
  2. Dado un pedido compartido de dos personas, cuando cada una elige «pagar lo mío», entonces cada una paga solo sus ítems y la mesa queda cerrada cuando el saldo es cero.
  3. Dado un pago aprobado, cuando Webpay confirma, entonces se procesa el documento tributario aplicable sin duplicarlo y se entrega al canal elegido; objetivo de 30 segundos sujeto a política fiscal y disponibilidad externa, con pendiente/alerta ante fallo.
  4. Dado un pago rechazado, cuando el cliente reintenta, entonces el pedido se mantiene y no se duplica en cocina.

**Historia 2 (P2): Control de gastos e inventario con margen por producto**

El administrador registra compras (foto de factura o carga manual), el sistema descuenta insumos por receta a medida que se venden y muestra margen real por producto y por día.

- Por qué P2: es el análisis de recetas y margen requerido por la propuesta, cuya cobertura en el sistema actual debe contrastarse y la base del agente de compras.
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
| FR-005 | Emitir el documento SII aplicable según política fiscal aprobada, evitando duplicar voucher y boleta al confirmar pagos y entregarla por WhatsApp, correo o QR | H1 |
| FR-006 | Mantener operación de caja en modo degradado sin internet y sincronizar al reconectar | H1 |
| FR-007 | Registrar compras y gastos desde foto de factura o carga manual, con estado pendiente/aprobado | H2 |
| FR-008 | Descontar insumos por receta en cada venta y mantener stock proyectado | H2 |
| FR-009 | Calcular margen por producto, por día y por franja horaria, y exponerlo en un dashboard | H2 |
| FR-010 | Importar ventas y stock que la exportación de la versión Eleventa del cliente permita recuperar, con cobertura y reconciliación documentadas | H2 |
| FR-011 | Proponer órdenes de compra con cantidades y costo estimado, para aprobación humana por WhatsApp | H3 |
| FR-012 | Alertar anulaciones, descuentos o mermas fuera de patrón en menos de 1 minuto | H3 |
| FR-013 | Registrar toda acción de agente en un registro de auditoría con integridad verificable y retención aprobada con evidencia y aprobador | H3 |
| FR-014 | Operar sobre el core compartido (identidad, autorización, pagos, documentos y auditoría) sin duplicarlo | Todas |

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
| SC-003 | El 100 % de los pagos aprobados queda conciliado con su obligación documental aplicable; objetivo de entrega <30 s cuando proceda y haya disponibilidad externa, sujeto a ratificación; fallos quedan pendientes y alertados |
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

- [ ] [NEEDS CLARIFICATION] ¿El cliente paga antes de recibir (modelo café) o después (modelo restaurante)? Cambia el flujo de H1.
- [ ] [NEEDS CLARIFICATION] ¿Propina incluida en el flujo de pago y con qué porcentaje por defecto?
- [ ] [NEEDS CLARIFICATION] ¿Quién aprueba compras: dueño, administrador o ambos según monto?
- [ ] [NEEDS CLARIFICATION] ¿Se reemplaza eleventa en V1 o convive? Define si FR-006 es caja propia o puente.
- [ ] [NEEDS CLARIFICATION] ¿Cuenta personal del cliente (perfil persistente) o solo pago por sesión de mesa?
- [ ] [NEEDS CLARIFICATION] ¿Proveedores con catálogo digital para la orden de compra o solo WhatsApp?

## Reglas normativas y de aceptación añadidas

- NFR-001: toda lectura, escritura, trabajo en cola y evidencia queda limitada por empresa y permiso; probar denegación entre empresas y roles.
- NFR-002: ningún agente ejecuta una acción financiera, tributaria o contractual sin control determinista y autorización vigente; escritura MCP deshabilitada inicialmente.
- NFR-003: reintentos conservan un solo efecto; estados desconocidos no se muestran como éxitos.
- NFR-004: retención, restauración y objetivos de recuperación requieren aprobación en Q-CORE-03; ninguna cifra de disponibilidad se asume acordada.
- NFR-005: medir latencia desde recepción hasta resultado confirmado, incluyendo errores, reintentos y desconexión. No declarar cumplimiento en muestras vacías.

Q-CAF-01: momento de pago y propina; Q-CAF-02: convivencia Eleventa y alcance offline; Q-CAF-03: carta, exportaciones, responsables de compras y sesión de cliente.

Los escenarios tributarios y SC de emisión en 30/60 segundos se conservan como aspiración de la fuente, sujetos a aplicabilidad fiscal y disponibilidad externa. No constituyen garantía del SII. El aislamiento local no garantiza por sí solo cero sobreventa entre OTA independientes.

Ver `acceptance.md` para pruebas por requisito; `../../docs/auditorias/trazabilidad.md` para origen y equivalencias. La investigación transversal está en `../../docs/investigacion/estado-del-arte.md`.
