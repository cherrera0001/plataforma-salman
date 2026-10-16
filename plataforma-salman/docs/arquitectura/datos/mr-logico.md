# Modelo Relacional Lógico (MR) — PostgreSQL

**Concilio Técnico:** Arquitecto de Datos · DBA PostgreSQL · Ingeniero de Software · Especialista AppSec.  
**Convención:** Esquemas lógicos segregados (`core`, `cafeteria`, `hotel`, `inmobiliaria`, `constructora`).  
**Normalización:** Tercera Forma Normal (3FN), con desnormalización inmutable deliberada en snapshots contractuales.

---

## 1. Convenciones y Principios Transversales de Modelado

1. **Claves Primarias e Identidad:**
   - Toda tabla transaccional utiliza `id UUID DEFAULT gen_random_uuid() PRIMARY KEY`.
   - Para tablas con particionamiento o integridad multi-tenant compuesta, la clave candidata es `UNIQUE (tenant_id, id)`.
2. **Integridad Referencial Multi-Tenant:**
   - Para impedir que una fila de un tenant A referencie datos de un tenant B mediante claves foráneas cruzadas, todas las relaciones internas de negocio implementan **Foreign Keys compuestas**:
     ```sql
     FOREIGN KEY (tenant_id, entidad_padre_id) REFERENCES esquema.tabla_padre (tenant_id, id) ON DELETE RESTRICT
     ```
3. **Tipos de Datos y Precisión Decimal:**
   - **Moneda Local CLP:** `BIGINT` (enteros sin decimales, reflejando la legislación chilena y evitando errores de punto flotante).
   - **Unidad de Fomento (UF):** `NUMERIC(18, 4)` (permite 4 decimales según la publicación oficial diaria del Banco Central de Chile).
   - **Cantidades Físicas / Rendimiento / Costos Unitarios:** `NUMERIC(18, 4)`.
   - **Porcentajes de Avance y Merma:** `NUMERIC(5, 2)` con `CHECK (valor BETWEEN 0.00 AND 100.00)`.
   - **Marcas Temporales:** `TIMESTAMPTZ` en UTC estricto.
   - **Textos y Códigos:** `VARCHAR(n)` para códigos estructurados (RUT, ISO); `TEXT` para campos de longitud variable.
   - **Metadatos y Auditoría Inmutable:** `JSONB` indexado con GIN.
4. **Auditoría Estándar (Columnas en toda tabla mutable):**
   - `created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()`
   - `created_by UUID NOT NULL` (referencia a `core.usuarios_identidad`)
   - `updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()`
   - `updated_by UUID NOT NULL`
   - `version INT NOT NULL DEFAULT 1` (para control de concurrencia optimista)
   - `deleted_at TIMESTAMPTZ NULL` (para soporte de borrado lógico / soft-delete auditado)

---

## 2. Esquema Lógico `core`

### Tabla `core.tenants`
- `id`: `UUID PRIMARY KEY`
- `rut`: `VARCHAR(12) NOT NULL UNIQUE` (Formato chileno: `12345678-9`, validado con módulo 11)
- `razon_social`: `VARCHAR(255) NOT NULL`
- `nombre_fantasia`: `VARCHAR(255) NOT NULL`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('ACTIVO', 'SUSPENDIDO', 'RETIRADO'))`
- `zona_horaria`: `VARCHAR(50) NOT NULL DEFAULT 'America/Santiago'`
- `moneda_principal`: `VARCHAR(3) NOT NULL DEFAULT 'CLP'`
- Columnas de auditoría estándar.

### Tabla `core.usuarios_identidad`
- `id`: `UUID PRIMARY KEY`
- `email`: `VARCHAR(255) NOT NULL UNIQUE`
- `telefono_e164`: `VARCHAR(20) NULL` (Formato `+569XXXXXXXX`)
- `hash_password`: `VARCHAR(255) NOT NULL` (Hash Argon2id)
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('PENDIENTE_ACTIVACION', 'ACTIVO', 'BLOQUEADO'))`
- `mfa_habilitado`: `BOOLEAN NOT NULL DEFAULT FALSE`
- Columnas de auditoría estándar.

### Tabla `core.membresias`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE CASCADE`
- `usuario_id`: `UUID NOT NULL REFERENCES core.usuarios_identidad(id) ON DELETE CASCADE`
- `rol`: `VARCHAR(50) NOT NULL CHECK (rol IN ('ADMIN_TENANT', 'CAJERO', 'RECEPCIONISTA', 'EJECUTIVO_VENTAS', 'JEFE_OBRA', 'INSPECTOR_ITO', 'AUDITOR'))`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('ACTIVO', 'REVOCADO', 'EXPIRADO'))`
- `vigente_desde`: `TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()`
- `vigente_hasta`: `TIMESTAMPTZ NULL`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, usuario_id)`, `UNIQUE (tenant_id, id)`.

### Tabla `core.perfiles_conector`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `proveedor`: `VARCHAR(50) NOT NULL CHECK (proveedor IN ('TRANSBANK', 'SII_DTE', 'BOOKING', 'AIRBNB', 'WHATSAPP_BUSINESS', 'PORTAL_INMOBILIARIO', 'TOC_SIGN'))`
- `referencia_cuenta_opaca`: `VARCHAR(100) NOT NULL`
- `plan_contratado`: `VARCHAR(50) NULL`
- `pais_operacion`: `VARCHAR(2) NOT NULL DEFAULT 'CL'`
- `capacidades_habilitadas`: `JSONB NOT NULL DEFAULT '[]'`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('ACTIVO', 'PAUSADO', 'REVOCADO', 'ERROR_AUTENTICACION'))`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, proveedor, referencia_cuenta_opaca)`, `UNIQUE (tenant_id, id)`.

### Tabla `core.intentos_pago`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `idempotency_key`: `VARCHAR(128) NOT NULL`
- `modulo_origen`: `VARCHAR(30) NOT NULL CHECK (modulo_origen IN ('CAFETERIA', 'HOTEL', 'INMOBILIARIA', 'CONSTRUCTORA'))`
- `referencia_negocio_id`: `UUID NOT NULL`
- `monto_clp`: `BIGINT NOT NULL CHECK (monto_clp > 0)`
- `moneda`: `VARCHAR(3) NOT NULL DEFAULT 'CLP'`
- `proveedor_pago`: `VARCHAR(50) NOT NULL`
- `estado`: `VARCHAR(30) NOT NULL CHECK (estado IN ('INICIADO', 'ENVIADO', 'AUTORIZADO', 'RECHAZADO', 'DESCONOCIDO', 'CONCILIADO', 'EN_DISPUTA', 'REVERSADO'))`
- `codigo_autorizacion`: `VARCHAR(50) NULL`
- `correlation_id`: `UUID NOT NULL DEFAULT gen_random_uuid()`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, idempotency_key)`, `UNIQUE (tenant_id, id)`.

### Tabla `core.documentos_tributarios`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `intento_pago_id`: `UUID NULL REFERENCES core.intentos_pago(id) ON DELETE RESTRICT`
- `tipo_dte`: `SMALLINT NOT NULL CHECK (tipo_dte IN (33, 34, 39, 41, 52, 56, 61))` (39=Boleta Electrónica, 33=Factura)
- `folio`: `BIGINT NOT NULL CHECK (folio > 0)`
- `rut_emisor`: `VARCHAR(12) NOT NULL`
- `rut_receptor`: `VARCHAR(12) NOT NULL DEFAULT '66666666-6'` (Consumidor final por defecto)
- `monto_neto_clp`: `BIGINT NOT NULL CHECK (monto_neto_clp >= 0)`
- `monto_iva_clp`: `BIGINT NOT NULL CHECK (monto_iva_clp >= 0)`
- `monto_total_clp`: `BIGINT NOT NULL CHECK (monto_total_clp = monto_neto_clp + monto_iva_clp)`
- `estado_sii`: `VARCHAR(20) NOT NULL CHECK (estado_sii IN ('EMITIDO_LOCAL', 'ENVIADO_SII', 'ACEPTADO_SII', 'OBSERVADO_SII', 'RECHAZADO_SII', 'ANULADO'))`
- `track_id_sii`: `VARCHAR(50) NULL`
- `xml_firmado_hash_sha256`: `VARCHAR(64) NOT NULL`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, tipo_dte, folio)`, `UNIQUE (tenant_id, id)`.

### Tabla `core.politicas_agente`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `agente_nombre`: `VARCHAR(50) NOT NULL`
- `limite_monetario_autonomo_clp`: `BIGINT NOT NULL DEFAULT 0 CHECK (limite_monetario_autonomo_clp = 0)` (0 CLP por Constitución)
- `herramientas_autorizadas`: `JSONB NOT NULL DEFAULT '[]'`
- `requiere_aprobacion_humana`: `BOOLEAN NOT NULL DEFAULT TRUE`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, agente_nombre)`, `UNIQUE (tenant_id, id)`.

### Tabla `core.aprobaciones_operacion`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `politica_id`: `UUID NOT NULL REFERENCES core.politicas_agente(id) ON DELETE RESTRICT`
- `proponente_agente`: `VARCHAR(50) NOT NULL`
- `aprobador_id`: `UUID NULL REFERENCES core.usuarios_identidad(id) ON DELETE RESTRICT`
- `operacion`: `VARCHAR(100) NOT NULL`
- `huella_parametros_sha256`: `VARCHAR(64) NOT NULL`
- `parametros_json`: `JSONB NOT NULL`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('SOLICITADA', 'APROBADA', 'RECHAZADA', 'EXPIRADA', 'CONSUMIDA'))`
- `expira_at`: `TIMESTAMPTZ NOT NULL`
- `consumida_at`: `TIMESTAMPTZ NULL`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, id)`.

### Tabla `core.acciones_auditadas` (Append-Only / Inmutable)
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `correlation_id`: `UUID NOT NULL`
- `actor_id`: `UUID NOT NULL`
- `tipo_actor`: `VARCHAR(20) NOT NULL CHECK (tipo_actor IN ('HUMANO', 'AGENTE_IA', 'SISTEMA_EXTERNO'))`
- `accion`: `VARCHAR(100) NOT NULL`
- `recurso`: `VARCHAR(100) NOT NULL`
- `resultado`: `VARCHAR(20) NOT NULL CHECK (resultado IN ('EXITO', 'DENEGADO', 'FALLO'))`
- `parametros_minimizados`: `JSONB NOT NULL`
- `hash_sha256`: `VARCHAR(64) NOT NULL`
- `created_at`: `TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()`
*(Sin updated_at ni deleted_at: tabla de solo inserción).*

---

## 3. Esquema Lógico `cafeteria`

### Tabla `cafeteria.mesas`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `codigo`: `VARCHAR(20) NOT NULL` (ej. 'MESA-01')
- `capacidad`: `SMALLINT NOT NULL CHECK (capacidad > 0)`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('DISPONIBLE', 'OCUPADA', 'EN_LIMPIEZA', 'BLOQUEADA'))`
- `qr_token_hash`: `VARCHAR(64) NOT NULL UNIQUE`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, codigo)`, `UNIQUE (tenant_id, id)`.

### Tabla `cafeteria.pedidos`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `mesa_id`: `UUID NOT NULL`
- `numero_diario`: `INT NOT NULL CHECK (numero_diario > 0)`
- `fecha_jornada`: `DATE NOT NULL`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('BORRADOR', 'ENVIADO_COCINA', 'EN_PREPARACION', 'SERVIDO', 'ANULADO'))`
- `anulado_motivo`: `TEXT NULL`
- `anulado_por`: `UUID NULL REFERENCES core.usuarios_identidad(id)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, mesa_id) REFERENCES cafeteria.mesas (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, fecha_jornada, numero_diario)`, `UNIQUE (tenant_id, id)`.

### Tabla `cafeteria.items_pedido`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `pedido_id`: `UUID NOT NULL`
- `producto_id`: `UUID NOT NULL`
- `cantidad`: `INT NOT NULL CHECK (cantidad > 0)`
- `precio_unitario_clp`: `BIGINT NOT NULL CHECK (precio_unitario_clp >= 0)` (Snapshot inmutable)
- `subtotal_clp`: `BIGINT NOT NULL CHECK (subtotal_clp = cantidad * precio_unitario_clp)`
- `modificadores_json`: `JSONB NOT NULL DEFAULT '[]'`
- `estado_cocina`: `VARCHAR(20) NOT NULL CHECK (estado_cocina IN ('PENDIENTE', 'EN_COCCION', 'PREPARADO', 'ENTREGADO', 'CANCELADO'))`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, pedido_id) REFERENCES cafeteria.pedidos (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, id)`.

### Tabla `cafeteria.asignaciones_cuenta`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `mesa_id`: `UUID NOT NULL`
- `saldo_total_clp`: `BIGINT NOT NULL CHECK (saldo_total_clp >= 0)`
- `saldo_liquidado_clp`: `BIGINT NOT NULL DEFAULT 0 CHECK (saldo_liquidado_clp >= 0 AND saldo_liquidado_clp <= saldo_total_clp)`
- `saldo_pendiente_clp`: `BIGINT NOT NULL CHECK (saldo_pendiente_clp = saldo_total_clp - saldo_liquidado_clp)`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('ABIERTA', 'EN_PAGO', 'LIQUIDADA', 'CERRADA'))`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, mesa_id) REFERENCES cafeteria.mesas (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, id)`.

### Tabla `cafeteria.partes_saldo` (Split de Cuenta)
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `asignacion_cuenta_id`: `UUID NOT NULL`
- `secuencia_parte`: `SMALLINT NOT NULL CHECK (secuencia_parte > 0)`
- `tipo_division`: `VARCHAR(20) NOT NULL CHECK (tipo_division IN ('ITEMS_ESPECIFICOS', 'PARTES_IGUALES'))`
- `items_detalle`: `JSONB NOT NULL DEFAULT '[]'`
- `monto_subtotal_clp`: `BIGINT NOT NULL CHECK (monto_subtotal_clp >= 0)`
- `monto_descuento_clp`: `BIGINT NOT NULL DEFAULT 0 CHECK (monto_descuento_clp >= 0)`
- `monto_propina_clp`: `BIGINT NOT NULL DEFAULT 0 CHECK (monto_propina_clp >= 0)`
- `monto_residuo_clp`: `BIGINT NOT NULL DEFAULT 0` (Diferencia de redondeo en partes iguales)
- `monto_exigible_clp`: `BIGINT NOT NULL CHECK (monto_exigible_clp = (monto_subtotal_clp - monto_descuento_clp) + monto_propina_clp + monto_residuo_clp)`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('PENDIENTE', 'PAGADA_CONCILIADA', 'ANULADA'))`
- `intento_pago_id`: `UUID NULL REFERENCES core.intentos_pago(id)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, asignacion_cuenta_id) REFERENCES cafeteria.asignaciones_cuenta (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, asignacion_cuenta_id, secuencia_parte)`, `UNIQUE (tenant_id, id)`.

---

## 4. Esquema Lógico `hotel`

### Tabla `hotel.propiedades`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `codigo`: `VARCHAR(20) NOT NULL`
- `nombre`: `VARCHAR(150) NOT NULL`
- `direccion`: `TEXT NOT NULL`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, codigo)`, `UNIQUE (tenant_id, id)`.

### Tabla `hotel.tipos_habitacion`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `propiedad_id`: `UUID NOT NULL`
- `codigo`: `VARCHAR(20) NOT NULL` (ej. 'STD_KING')
- `nombre`: `VARCHAR(100) NOT NULL`
- `capacidad_maxima`: `SMALLINT NOT NULL CHECK (capacidad_maxima > 0)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, propiedad_id) REFERENCES hotel.propiedades (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, propiedad_id, codigo)`, `UNIQUE (tenant_id, id)`.

### Tabla `hotel.habitaciones_fisicas`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `tipo_habitacion_id`: `UUID NOT NULL`
- `numero`: `VARCHAR(10) NOT NULL` (ej. '204')
- `piso`: `SMALLINT NOT NULL`
- `estado_operativo`: `VARCHAR(30) NOT NULL CHECK (estado_operativo IN ('DISPONIBLE', 'OCUPADA', 'BLOQUEADA_MANTENIMIENTO'))`
- `estado_limpieza`: `VARCHAR(20) NOT NULL CHECK (estado_limpieza IN ('SUCIA', 'EN_LIMPIEZA', 'LIMPIA', 'INSPECCIONADA'))`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, tipo_habitacion_id) REFERENCES hotel.tipos_habitacion (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, numero)`, `UNIQUE (tenant_id, id)`.

### Tabla `hotel.cupos_fecha_tipo` (Inventario Desacoplado)
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `tipo_habitacion_id`: `UUID NOT NULL`
- `fecha`: `DATE NOT NULL`
- `cupo_total_inventario`: `INT NOT NULL CHECK (cupo_total_inventario >= 0)`
- `cupo_bloqueado_tecnico`: `INT NOT NULL DEFAULT 0 CHECK (cupo_bloqueado_tecnico >= 0)`
- `cupo_retenido_ofertas`: `INT NOT NULL DEFAULT 0 CHECK (cupo_retenido_ofertas >= 0)`
- `cupo_reservado_confirmado`: `INT NOT NULL DEFAULT 0 CHECK (cupo_reservado_confirmado >= 0)`
- `cupo_disponible`: `INT NOT NULL CHECK (cupo_disponible = cupo_total_inventario - (cupo_bloqueado_tecnico + cupo_retenido_ofertas + cupo_reservado_confirmado) AND cupo_disponible >= 0)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, tipo_habitacion_id) REFERENCES hotel.tipos_habitacion (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, tipo_habitacion_id, fecha)`, `UNIQUE (tenant_id, id)`.

### Tabla `hotel.reservas`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `propiedad_id`: `UUID NOT NULL`
- `tipo_habitacion_id`: `UUID NOT NULL`
- `habitacion_asignada_id`: `UUID NULL` (Asignación tardía opcional)
- `codigo_reserva`: `VARCHAR(30) NOT NULL`
- `canal_origen`: `VARCHAR(30) NOT NULL CHECK (canal_origen IN ('MOTOR_DIRECTO', 'BOOKING', 'AIRBNB', 'EXPEDIA', 'RECEPCION'))`
- `referencia_externa_canal`: `VARCHAR(100) NULL`
- `huesped_nombre`: `VARCHAR(200) NOT NULL`
- `huesped_email`: `VARCHAR(255) NOT NULL`
- `fecha_checkin`: `DATE NOT NULL`
- `fecha_checkout`: `DATE NOT NULL CHECK (fecha_checkout > fecha_checkin)`
- `noches`: `SMALLINT NOT NULL CHECK (noches = (fecha_checkout - fecha_checkin))`
- `monto_alojamiento_clp`: `BIGINT NOT NULL CHECK (monto_alojamiento_clp >= 0)`
- `estado`: `VARCHAR(30) NOT NULL CHECK (estado IN ('PROPUESTA', 'RETENIDA_TEMPORAL', 'CONFIRMADA', 'CHECKED_IN', 'CHECKED_OUT', 'CANCELADA', 'EXPIRADA'))`
- `expiracion_retencion_at`: `TIMESTAMPTZ NULL`
- Columnas de auditoría estándar.
- Claves foráneas compuestas:
  - `FOREIGN KEY (tenant_id, propiedad_id) REFERENCES hotel.propiedades (tenant_id, id)`
  - `FOREIGN KEY (tenant_id, tipo_habitacion_id) REFERENCES hotel.tipos_habitacion (tenant_id, id)`
- Restricciones: `UNIQUE (tenant_id, codigo_reserva)`, `UNIQUE (tenant_id, id)`.

---

## 5. Esquema Lógico `inmobiliaria`

### Tabla `inmobiliaria.proyectos`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `codigo`: `VARCHAR(20) NOT NULL`
- `nombre`: `VARCHAR(150) NOT NULL`
- `comuna`: `VARCHAR(100) NOT NULL`
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, codigo)`, `UNIQUE (tenant_id, id)`.

### Tabla `inmobiliaria.unidades`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `proyecto_id`: `UUID NOT NULL`
- `numero`: `VARCHAR(20) NOT NULL`
- `tipo`: `VARCHAR(30) NOT NULL CHECK (tipo IN ('DEPARTAMENTO', 'CASA', 'ESTACIONAMIENTO', 'BODEGA'))`
- `superficie_util_m2`: `NUMERIC(8, 2) NOT NULL CHECK (superficie_util_m2 > 0)`
- `precio_lista_uf`: `NUMERIC(18, 4) NOT NULL CHECK (precio_lista_uf > 0)`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('DISPONIBLE', 'COTIZADA', 'RESERVADA', 'PROMESADA', 'ESCRITURADA'))`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, proyecto_id) REFERENCES inmobiliaria.proyectos (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, proyecto_id, numero)`, `UNIQUE (tenant_id, id)`.

### Tabla `inmobiliaria.cotizaciones`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `unidad_id`: `UUID NOT NULL`
- `contacto_id`: `UUID NOT NULL`
- `codigo_cotizacion`: `VARCHAR(30) NOT NULL`
- `precio_cotizado_uf`: `NUMERIC(18, 4) NOT NULL CHECK (precio_cotizado_uf > 0)` (Snapshot inmutable)
- `pie_porcentaje`: `NUMERIC(5, 2) NOT NULL CHECK (pie_porcentaje BETWEEN 0 AND 100)`
- `vigente_hasta`: `TIMESTAMPTZ NOT NULL`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('VIGENTE', 'VENCIDA', 'RESERVADA', 'RECHAZADA'))`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, unidad_id) REFERENCES inmobiliaria.unidades (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, codigo_cotizacion)`, `UNIQUE (tenant_id, id)`.

### Tabla `inmobiliaria.reservas_unidad`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `unidad_id`: `UUID NOT NULL`
- `cotizacion_id`: `UUID NOT NULL`
- `contacto_id`: `UUID NOT NULL`
- `monto_abono_clp`: `BIGINT NOT NULL CHECK (monto_abono_clp > 0)`
- `estado`: `VARCHAR(30) NOT NULL CHECK (estado IN ('EN_PROCESO_PAGO', 'CONFIRMADA_PAGADA', 'VENCIDA', 'DEVOLUCION_TRAMITADA'))`
- `intento_pago_id`: `UUID NULL REFERENCES core.intentos_pago(id)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas:
  - `FOREIGN KEY (tenant_id, unidad_id) REFERENCES inmobiliaria.unidades (tenant_id, id)`
  - `FOREIGN KEY (tenant_id, cotizacion_id) REFERENCES inmobiliaria.cotizaciones (tenant_id, id)`
- Restricciones: `UNIQUE (tenant_id, id)`.

### Tabla `inmobiliaria.promesas_compraventa`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `unidad_id`: `UUID NOT NULL`
- `reserva_id`: `UUID NOT NULL`
- `numero_promesa`: `VARCHAR(30) NOT NULL`
- `precio_final_uf`: `NUMERIC(18, 4) NOT NULL CHECK (precio_final_uf > 0)`
- `plantilla_legal_hash_sha256`: `VARCHAR(64) NOT NULL`
- `estado`: `VARCHAR(30) NOT NULL CHECK (estado IN ('BORRADOR', 'EN_REVISION_LEGAL', 'ENVIADA_FIRMA', 'FIRMADA_PARCIAL', 'FIRMADA_COMPLETA', 'ESCRITURADA', 'RESCILIADA'))`
- Columnas de auditoría estándar.
- Claves foráneas compuestas:
  - `FOREIGN KEY (tenant_id, unidad_id) REFERENCES inmobiliaria.unidades (tenant_id, id)`
  - `FOREIGN KEY (tenant_id, reserva_id) REFERENCES inmobiliaria.reservas_unidad (tenant_id, id)`
- Restricciones: `UNIQUE (tenant_id, numero_promesa)`, `UNIQUE (tenant_id, id)`.

---

## 6. Esquema Lógico `constructora`

### Tabla `constructora.obras`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `codigo`: `VARCHAR(20) NOT NULL`
- `nombre`: `VARCHAR(150) NOT NULL`
- `direccion`: `TEXT NOT NULL`
- `proyecto_inmobiliario_id`: `UUID NULL` (Vínculo de correspondencia opcional)
- Columnas de auditoría estándar.
- Restricciones: `UNIQUE (tenant_id, codigo)`, `UNIQUE (tenant_id, id)`.

### Tabla `constructora.presupuestos`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `obra_id`: `UUID NOT NULL`
- `version`: `INT NOT NULL CHECK (version > 0)`
- `estado`: `VARCHAR(20) NOT NULL CHECK (estado IN ('LINEA_BASE', 'VIGENTE_APROBADO', 'EN_REVISION'))`
- `total_presupuestado_clp`: `BIGINT NOT NULL CHECK (total_presupuestado_clp >= 0)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, obra_id) REFERENCES constructora.obras (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, obra_id, version)`, `UNIQUE (tenant_id, id)`.

### Tabla `constructora.partidas`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `presupuesto_id`: `UUID NOT NULL`
- `itemizado`: `VARCHAR(30) NOT NULL` (ej. '01.02.03')
- `descripcion`: `TEXT NOT NULL`
- `unidad_medida`: `VARCHAR(10) NOT NULL`
- `cantidad_presupuestada`: `NUMERIC(18, 4) NOT NULL CHECK (cantidad_presupuestada >= 0)`
- `precio_unitario_clp`: `BIGINT NOT NULL CHECK (precio_unitario_clp >= 0)`
- `total_partida_clp`: `BIGINT NOT NULL CHECK (total_partida_clp = ROUND(cantidad_presupuestada * precio_unitario_clp))`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, presupuesto_id) REFERENCES constructora.presupuestos (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, presupuesto_id, itemizado)`, `UNIQUE (tenant_id, id)`.

### Tabla `constructora.reportes_avance`
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `partida_id`: `UUID NOT NULL`
- `fecha_hecho`: `DATE NOT NULL`
- `turno`: `VARCHAR(10) NOT NULL CHECK (turno IN ('MANANA', 'TARDE', 'NOCHE'))`
- `cantidad_avance_periodo`: `NUMERIC(18, 4) NOT NULL`
- `porcentaje_acumulado_pct`: `NUMERIC(5, 2) NOT NULL CHECK (porcentaje_acumulado_pct BETWEEN 0.00 AND 100.00)`
- `origen_registro`: `VARCHAR(20) NOT NULL CHECK (origen_registro IN ('ENTRADA_MANUAL', 'EXTRACCION_VOZ_IA', 'FOTOGRAMETRIA'))`
- `estado_revision`: `VARCHAR(20) NOT NULL CHECK (estado_revision IN ('BORRADOR', 'EXTRAIDO_IA', 'APROBADO_ITO', 'RECHAZADO'))`
- `aprobado_por_ito_id`: `UUID NULL REFERENCES core.usuarios_identidad(id)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, partida_id) REFERENCES constructora.partidas (tenant_id, id)`.
- Restricciones: `UNIQUE (tenant_id, partida_id, fecha_hecho, turno, origen_registro)`, `UNIQUE (tenant_id, id)`.

### Tabla `constructora.observaciones_calidad` (Punch List)
- `id`: `UUID PRIMARY KEY`
- `tenant_id`: `UUID NOT NULL REFERENCES core.tenants(id) ON DELETE RESTRICT`
- `partida_id`: `UUID NOT NULL`
- `numero`: `INT NOT NULL CHECK (numero > 0)`
- `severidad`: `VARCHAR(10) NOT NULL CHECK (severidad IN ('LEVE', 'MEDIA', 'CRITICA'))`
- `descripcion_falla`: `TEXT NOT NULL`
- `estado`: `VARCHAR(30) NOT NULL CHECK (estado IN ('ABIERTA', 'ASIGNADA', 'SOLUCION_PROPUESTA', 'CERRADA_ACEPTADA', 'REABIERTA'))`
- `inspector_ito_id`: `UUID NOT NULL REFERENCES core.usuarios_identidad(id)`
- `solucionador_asignado_id`: `UUID NULL REFERENCES core.usuarios_identidad(id)`
- `cerrada_por_ito_id`: `UUID NULL REFERENCES core.usuarios_identidad(id)`
- Columnas de auditoría estándar.
- Claves foráneas compuestas: `FOREIGN KEY (tenant_id, partida_id) REFERENCES constructora.partidas (tenant_id, id)`.
- Restricciones:
  - `UNIQUE (tenant_id, partida_id, numero)`
  - `UNIQUE (tenant_id, id)`
  - `CHECK (cerrada_por_ito_id IS NULL OR cerrada_por_ito_id != solucionador_asignado_id)` (Invariante estricta de segregación de roles).
