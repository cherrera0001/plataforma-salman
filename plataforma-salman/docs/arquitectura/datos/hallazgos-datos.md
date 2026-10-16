# Informe de Hallazgos Técnicos y Auditoría de Datos

**Concilio Técnico:** Arquitecto de Datos · DBA PostgreSQL · Ingeniero de Software · Especialista AppSec · QA.  
**Criterio de Evaluación:** Severidad AppSec, integridad relacional, consistencia matemática y robustez operacional.

---

## 1. Clasificación de Hallazgos por Severidad

### Severidad Crítica (P0 — Riesgo de Seguridad / Integridad Financiera)

#### H-DAT-01: Vulnerabilidad de Fuga Multi-tenant por Claves Foráneas Simples
- **Descripción:** Si una tabla multi-tenant utiliza claves foráneas simples (`REFERENCES tabla(id)`), un error en la capa de aplicación o una inyección de parámetros podría permitir que una entidad del Tenant A apunte a un registro padre del Tenant B, quebrando el aislamiento estricto exigido por la Constitución (Principio IV).
- **Impacto:** Fuga de datos entre empresas del mismo grupo o competidores alojados en la plataforma.
- **Resolución Aplicada:** Imposición obligatoria de **Foreign Keys compuestas** `(tenant_id, entidad_padre_id) REFERENCES esquema.tabla_padre(tenant_id, id) ON DELETE RESTRICT` y activación forzada de **Row Level Security (RLS)** con `FORCE ROW LEVEL SECURITY` en PostgreSQL.

#### H-DAT-02: Carrera Crítica de Sobreventa en Inventario Hotelero
- **Descripción:** En escenarios de alta concurrencia (ej. último cupo disponible de una categoría en temporada alta), dos transacciones concurrentes bajo el nivel de aislamiento por defecto `READ COMMITTED` pueden leer `cupo_disponible = 1`, emitir ambas el cobro y confirmar dos reservas para una sola habitación física.
- **Impacto:** Sobreventa forzada, penalizaciones con OTAs y daño reputacional.
- **Resolución Aplicada:** Patrón de **bloqueo pesimista defensivo** `SELECT ... FOR UPDATE` sobre la fila de `hotel.cupos_fecha_tipo` con `lock_timeout = '1500ms'`, acompañado de la restricción de integridad `CHECK (cupo_disponible >= 0)`.

#### H-DAT-03: Corrupción de Balanza por Modificación de Pagos Consolidados en Cafetería
- **Descripción:** Al reorganizar mesas o dividir cuentas en múltiples partes, un flujo de usuario mal diseñado podría permitir desasociar o cancelar una parte de la cuenta que ya fue cobrada y conciliada ante la pasarela de pagos.
- **Impacto:** Pérdida de cuadratura de caja, discrepancias contables y emisión tributaria inconsistente ante el SII.
- **Resolución Aplicada:** Inmutabilidad estricta del estado `PAGADA_CONCILIADA` en `cafeteria.partes_saldo`. El total liquidado se deduce formalmente de la balanza y está desacoplado del flujo de comanda en cocina.

---

### Severidad Alta (P1 — Consistencia Operacional y Control de Negocio)

#### H-DAT-04: Doble Resta Presupuestaria de Compras y Recepciones en Obra
- **Descripción:** Si el sistema resta del saldo disponible de la partida presupuestaria tanto la Orden de Compra aprobada como la Guía de Despacho al recepcionar el material en bodega, el monto se computa dos veces como gasto.
- **Impacto:** Distorsión artificial del presupuesto disponible, paralización indebida de adquisiciones y reportes falsos de sobrecosto.
- **Resolución Aplicada:** Modelado matemático riguroso en `constructora.obligaciones_costo`:
  $$\text{saldo\_disponible} = \text{monto\_presupuestado} - \text{monto\_comprometido\_oc}$$
  La recepción física (devengo) y el pago son fases de liquidación de la orden comprometida, no deducciones adicionales al saldo disponible.

#### H-DAT-05: Conflicto de Interés y Autoaprobación en Punch List de Obra
- **Descripción:** Si el modelo permite que el mismo usuario que ejecuta la reparación de una observación de calidad apruebe su cierre, se elimina el control técnico de la Inspección Técnica de Obra (ITO).
- **Impacto:** Certificación de fallas no resueltas y vicios ocultos de construcción.
- **Resolución Aplicada:** Restricción declarada a nivel relacional:
  ```sql
  CHECK (cerrada_por_ito_id IS NULL OR cerrada_por_ito_id != solucionador_asignado_id)
  ```

#### H-DAT-06: Falsa Premisa de Detección de Conflictos en Agenda Estática Inmobiliaria
- **Descripción:** Si el sistema ofrece agendamiento de visitas sin sincronización bidireccional con Google Calendar o Microsoft 365, prometer al usuario "detección automática de colisiones de agenda" es un reclamo falso.
- **Impacto:** Cruces de horario entre ejecutivos de venta y prospectos en salas de ventas.
- **Resolución Aplicada:** Atributo explícito `modo_agenda` ('ESTATICA' vs 'SINCRONIZADA') en `inmobiliaria.citas_visita`. En modo estático, las citas propuestas quedan con estado `POR_CONFIRMAR` hasta validación manual.

---

### Severidad Media (P2 — Precisión Numérica y Reglas de Dominio)

#### H-DAT-07: Discrepancia de Redondeo en División de Cuentas en Pesos Chilenos (CLP)
- **Descripción:** Al dividir una cuenta de $10.000$ CLP entre 3 comensales, el cálculo genera cuotas periódicas de $3.333,333\dots$ CLP.
- **Impacto:** Pérdida o creación artificial de pesos en los balances de caja.
- **Resolución Aplicada:** Introducción del campo `monto_residuo_clp` en `cafeteria.partes_saldo`. El sistema calcula cuotas enteras ($3.334$, $3.333$, $3.333$ CLP) y asigna el residuo de $1$ CLP según una regla visible y ratificada por el negocio (Q-COMP-01).

#### H-DAT-08: Acoplamiento Indebido entre Persona y Titularidad de Unidad
- **Descripción:** Si los datos del lead/comprador se fusionan directamente con la unidad inmobiliaria, corregir un número de teléfono o correo podría alterar históricamente la titularidad de los derechos de garantía de otras unidades del mismo cliente.
- **Impacto:** Problemas de acceso al portal de propietarios y asignación incorrecta de solicitudes de postventa.
- **Resolución Aplicada:** Creación de la entidad asociativa `inmobiliaria.vinculos_unidad` con vigencia temporal (`vigente_desde`, `vigente_hasta`) y rol específico ('PROPIETARIO', 'ARRENDATARIO'), desacoplada de la entidad `core.usuarios_identidad`.

---

### Severidad Baja (P3 — Higiene de Código y Estándares)

#### H-DAT-09: Estandarización de Zonas Horarias y Tipos de Fecha
- **Descripción:** Manejo ambiguo de marcas temporales locales sin indicación de huso horario.
- **Resolución Aplicada:** Adopción mandatoria de `TIMESTAMPTZ` en UTC para eventos transaccionales y `DATE` sin hora para jornadas contables o fechas de ocupación hotelera.

---

## 2. Estado de Bloqueos Críticos y Decisiones de Negocio

La auditoría técnica confirma que los modelos de datos están completamente especificados a nivel lógico y físico, pero las cinco features **permanecen formalmente en estado BLOCKED para implementación**.

No se debe iniciar migración de base de datos ni codificación hasta que Cristóbal Herrera y los responsables comerciales resuelvan los siguientes puntos de decisión:

1. **`Q-COMP-01` (Cafetería):** Ratificación de la política de asignación del residuo de redondeo en CLP (primer vs último pagador de la mesa) y confirmación de emisión tributaria SII con boleta electrónica versus comprobante de pago electrónico Transbank.
2. **`Q-COMP-02` (Hotel):** Ratificación de la ventana de expiración de cotizaciones directas (15 minutos propuesta) y definición del SLA de latencia tolerable en la sincronización con Channel Managers.
3. **`Q-COMP-03` (Inmobiliaria):** Validación legal del tipo de firma electrónica requerida bajo la Ley 19.799 para la promesa de compraventa (Firma Simple vs Firma Avanzada con e-Token).
4. **`Q-COMP-04` (Constructora):** Definición de perfiles de usuario autorizados para aceptar el cierre definitivo de observaciones de calidad y fijación del umbral de alerta presupuestaria por partida (porcentaje relativo vs monto absoluto en UF/CLP).
5. **`Q-REA-01 / Q-REA-03` (Entorno de Ejecución):** Decisión sobre la aprobación de actualización global de Node.js a versión 22+ para habilitar el runtime dinámico de REA.
