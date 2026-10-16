# Contratos Lógicos de Integración e Intercambio de Datos

**Concilio Técnico:** Arquitecto de Software · Analista de Requisitos · QA · Especialista AppSec.  
**Estado:** Canónico para Fase de Especificación SDD (Sin contratos ejecutables prematuros).

---

## 1. Estándar de Sobre Común, Idempotencia y Manejo de Errores

Todos los contratos lógicos de comunicación entre los clientes, las verticales y el Core implementan un sobre estandarizado con trazabilidad y mitigación de errores de concurrencia:

### A. Encabezados Obligatorios
- `X-Tenant-ID`: Identificador UUID del tenant autenticado y resuelto por el API Gateway.
- `X-Correlation-ID`: Identificador UUID de correlación para observabilidad distribuida.
- `Idempotency-Key`: Cadena única de hasta 128 caracteres obligatoria en toda mutación (`POST`, `PUT`, `PATCH`).
- `If-Match`: Versión entera de la entidad esperada para control de concurrencia optimista (`version`).

### B. Semántica de Respuesta y Formato de Errores
```json
{
  "exito": false,
  "codigo_error": "CONFLICTO_CONCURRENCIA_CUPO",
  "mensaje": "El cupo de la categoría seleccionada cambió durante la transacción. Revalide disponibilidad.",
  "correlation_id": "c1d2e3f4-a5b6-7890-1234-567890abcdef",
  "timestamp": "2026-10-16T18:40:00Z",
  "detalles": [
    {
      "campo": "cupo_disponible",
      "motivo": "INSUFICIENTE_PARA_FECHAS_SOLICITADAS",
      "fechas_afectadas": ["2026-11-03"]
    }
  ]
}
```

- **HTTP 400 Bad Request:** Payload malformado o violación de tipo de datos.
- **HTTP 401 Unauthorized:** Identidad no provista o token JWT expirado.
- **HTTP 403 Forbidden:** Membresía inactiva o falta de permisos para la acción solicitada.
- **HTTP 404 Not Found:** Recurso inexistente o perteneciente a otro tenant (evita enumeración de recursos).
- **HTTP 409 Conflict:** Incompatibilidad de versión (`version != If-Match`) o cupo agotado por carrera de reserva.
- **HTTP 422 Unprocessable Entity:** Misma `Idempotency-Key` utilizada con un payload o monto diferente.
- **HTTP 502 / 504 Gateway Timeout:** Fallo o timeout al consultar un conector externo (genera estado `DESCONOCIDO`).

---

## 2. Contratos Lógicos por Feature y Dominio

### A. Core Transversal (`specs/000-core/contracts/README.md`)
- **`CORE-CONTRATO-01: IniciarIntentoPago`**
  - *Entrada:* `tenant_id`, `idempotency_key`, `modulo_origen`, `referencia_negocio_id`, `monto_clp`, `moneda`, `proveedor_pago`, `datos_retorno_url`.
  - *Salida:* `intento_pago_id`, `estado` ('INICIADO', 'AUTORIZADO', 'ENVIADO'), `url_redireccion_o_token`, `correlation_id`.
  - *Invariantes:* Moneda debe ser explícita; monto en CLP entero; idempotencia estricta por tenant.
- **`CORE-CONTRATO-02: ConciliarResultadoProveedor`**
  - *Entrada:* `tenant_id`, `proveedor`, `payload_raw_json`, `firma_externa_token`.
  - *Salida:* `intento_pago_id`, `estado_final` ('AUTORIZADO', 'RECHAZADO', 'CONCILIADO', 'EN_DISPUTA'), `motivo_rechazo`.
  - *Invariantes:* Un callback repetido con idéntico payload no ejecuta doble abono; eventos desordenados no retroceden un estado ya `CONCILIADO`.
- **`CORE-CONTRATO-03: EvaluarYRegistrarAprobacionAgente`**
  - *Entrada:* `tenant_id`, `agente_nombre`, `operacion_propuesta`, `parametros_json`, `huella_sha256`.
  - *Salida:* `aprobacion_id`, `estado` ('APROBADA_AUTOMATICA', 'EN_APROBACION_HUMANA', 'RECHAZADA_POR_POLITICA').
  - *Invariantes:* Todo monto $> 0$ CLP exige aprobación humana de un solo uso.

### B. Cafetería y POS (`specs/001-cafeteria-mesas-pos/contracts/README.md`)
- **`CAF-CONTRATO-01: DividirCuentaMesa`**
  - *Entrada:* `tenant_id`, `mesa_id`, `asignacion_cuenta_id`, `tipo_division` ('ITEMS' o 'PARTES_IGUALES'), `numero_partes`, `items_por_parte` (opcional).
  - *Salida:* `partes`: Array de `{ secuencia, monto_subtotal_clp, monto_descuento_clp, monto_propina_clp, monto_residuo_clp, monto_exigible_clp, estado }`.
  - *Invariantes:* Suma de montos exigibles igual al saldo total de la mesa; residuo de redondeo asignado de forma determinista y visible. No se transmiten eventos a cocina.
- **`CAF-CONTRATO-02: LiquidarParteCuenta`**
  - *Entrada:* `tenant_id`, `parte_saldo_id`, `medio_pago`, `intento_pago_id`.
  - *Salida:* `saldo_liquidado_clp`, `saldo_pendiente_mesa_clp`, `estado_mesa`.
  - *Invariantes:* Una parte pagada pasa a `PAGADA_CONCILIADA` e inmutable.

### C. Hotel y Reservas (`specs/002-hotel-reservas-concierge/contracts/README.md`)
- **`HOT-CONTRATO-01: CotizarYRetenerCupo`**
  - *Entrada:* `tenant_id`, `propiedad_id`, `tipo_habitacion_id`, `fecha_checkin`, `fecha_checkout`, `huesped_titular`.
  - *Salida:* `token_retencion`, `expira_at`, `monto_total_clp`, `desglose_por_noche`.
  - *Invariantes:* Disminuye `cupo_disponible` mediante incremento de `cupo_retenido_ofertas`; rechaza con HTTP 409 si no hay cupo seguro en todas las noches.
- **`HOT-CONTRATO-02: ConfirmarReserva`**
  - *Entrada:* `tenant_id`, `token_retencion`, `intento_pago_id`.
  - *Salida:* `codigo_reserva`, `estado_reserva` = 'CONFIRMADA'.
  - *Invariantes:* Transforma cupo retenido en reservado; no exige habitación física asignada.
- **`HOT-CONTRATO-03: ProcesarEventoCanalOTA`**
  - *Entrada:* `tenant_id`, `canal_ota`, `external_notification_id`, `payload_json`.
  - *Salida:* `ack_status`: 'ACK_RECIBIDO_DURABLE', `codigo_reserva_local`.
  - *Invariantes:* Acuse de recibo se devuelve únicamente tras almacenamiento durable en base de datos.

### D. Inmobiliaria Comercial (`specs/003-inmobiliaria-comercial/contracts/README.md`)
- **`INM-CONTRATO-01: EmitirCotizacionVersionada`**
  - *Entrada:* `tenant_id`, `unidad_id`, `contacto_id`, `descuento_solicitado_pct`, `pie_propuesto_pct`.
  - *Salida:* `codigo_cotizacion`, `precio_uf`, `pie_clp_referencial`, `vigente_hasta`.
  - *Invariantes:* Inmuta el precio ofertado hasta su vencimiento; la unidad permanece disponible para otras cotizaciones.
- **`INM-CONTRATO-02: FormalizarReservaUnidad`**
  - *Entrada:* `tenant_id`, `codigo_cotizacion`, `intento_pago_id`.
  - *Salida:* `reserva_id`, `estado_unidad` = 'RESERVADA'.
  - *Invariantes:* Solo puede existir una reserva confirmada activa por unidad.
- **`INM-CONTRATO-03: EnviarPromesaFirma`**
  - *Entrada:* `tenant_id`, `reserva_id`, `plantilla_legal_id`, `firmantes_array`.
  - *Salida:* `promesa_id`, `estado` = 'ENVIADA_FIRMA', `enlaces_firma_seguros`.
  - *Invariantes:* Requiere reserva confirmada y pagada; el documento lleva hash SHA-256 de plantilla legal.

### E. Constructora y Obra (`specs/004-constructora-obra/contracts/README.md`)
- **`OBR-CONTRATO-01: RegistrarParteAvanceDiario`**
  - *Entrada:* `tenant_id`, `obra_id`, `partida_id`, `fecha_hecho`, `turno`, `cantidad_avance`, `origen_registro`, `adjuntos_evidencia`.
  - *Salida:* `parte_trabajo_id`, `estado_revision` = 'BORRADOR' o 'EXTRAIDO_IA'.
  - *Invariantes:* Admite múltiples turnos en el mismo día; deduplica por combinación (partida, fecha, turno, origen).
- **`OBR-CONTRATO-02: ValidarCierreObservacion`**
  - *Entrada:* `tenant_id`, `observacion_id`, `inspector_ito_id`, `decision` ('ACEPTAR_CIERRE', 'RECHAZAR_REABRIR'), `comentario`.
  - *Salida:* `estado_observacion` = 'CERRADA_ACEPTADA' o 'REABIERTA'.
  - *Invariantes:* Denegado si `inspector_ito_id` coincide con el contratista solucionador asignado.
- **`OBR-CONTRATO-03: RecepcionarMaterialBodega`**
  - *Entrada:* `tenant_id`, `orden_compra_id`, `guia_despacho_numero`, `lineas`: Array de `{ material_id, cantidad_aceptada, cantidad_rechazada, cantidad_devuelta }`.
  - *Salida:* `entrega_id`, `estado_oc` ('RECEPCION_PARCIAL' o 'RECEPCION_TOTAL'), `discrepancias_registradas`.
  - *Invariantes:* Actualiza inventario de bodega; no computa avance financiero ni físico de la obra.
