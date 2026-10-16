# Modelo Físico PostgreSQL, Concurrencia y Seguridad de Datos

**Concilio Técnico:** Arquitecto de Datos · DBA PostgreSQL · Ingeniero de Software · Especialista AppSec.  
**Estado:** DDL e Infraestructura de Datos Propuesta (Documento revisable; **no ejecutar como migración**).

---

## 1. Estrategia de Esquemas y Row Level Security (RLS)

Para garantizar aislamiento multi-tenant estricto por diseño (Constitución Principio IV), la base de datos se estructura en esquemas por dominio y aplica **Row Level Security (RLS)** obligatorio sobre toda tabla con datos de clientes.

```sql
-- Configuración de sesión por transacción en el pool de conexiones:
-- SET LOCAL app.current_tenant_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890';
-- SET LOCAL app.current_user_id   = 'b2c3d4e5-f6a7-8901-bcde-f12345678901';

-- Ejemplo de política RLS estándar aplicada en todas las tablas de negocio:
ALTER TABLE core.intentos_pago ENABLE ROW LEVEL SECURITY;
ALTER TABLE core.intentos_pago FORCE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_intentos_pago ON core.intentos_pago
    FOR ALL
    TO app_user
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);
```

---

## 2. Índices Estratégicos de Rendimiento y Unicidad

### A. Índices Parciales y Compuestos para Operación Diaria
```sql
-- 1. Consultas rápidas de saldo pendiente en mesas activas
CREATE INDEX idx_cafeteria_asignaciones_abiertas
    ON cafeteria.asignaciones_cuenta (tenant_id, mesa_id)
    WHERE estado IN ('ABIERTA', 'EN_PAGO');

-- 2. Prevención de reservas dobles de la misma unidad inmobiliaria
CREATE UNIQUE INDEX uq_inmobiliaria_unidad_bloqueada
    ON inmobiliaria.unidades (tenant_id, id)
    WHERE estado IN ('RESERVADA', 'PROMESADA', 'ESCRITURADA');

-- 3. Búsqueda de cupos hoteleros por rango de fechas (Hot-path de reservas)
CREATE INDEX idx_hotel_cupos_busqueda
    ON hotel.cupos_fecha_tipo (tenant_id, tipo_habitacion_id, fecha, cupo_disponible)
    WHERE cupo_disponible > 0;

-- 4. Monitoreo de pagos pendientes de conciliación en el Core
CREATE INDEX idx_core_pagos_pendientes_conciliacion
    ON core.intentos_pago (tenant_id, proveedor_pago, created_at)
    WHERE estado IN ('ENVIADO', 'DESCONOCIDO');

-- 5. Control de observaciones críticas abiertas en obra
CREATE INDEX idx_constructora_observaciones_criticas
    ON constructora.observaciones_calidad (tenant_id, partida_id, severidad)
    WHERE estado IN ('ABIERTA', 'ASIGNADA', 'REABIERTA');
```

### B. Índices GIN para Metadatos y Búsqueda JSON
```sql
-- Búsqueda eficiente sobre eventos externos y payloads de auditoría
CREATE INDEX idx_core_acciones_parametros_gin
    ON core.acciones_auditadas USING GIN (parametros_minimizados jsonb_path_ops);

CREATE INDEX idx_hotel_eventos_ota_payload_gin
    ON hotel.recepciones_evento_canal USING GIN (payload_json jsonb_path_ops);
```

---

## 3. Concurrencia, Aislamiento y Prevención de Carreras

### A. Niveles de Aislamiento Transaccional
- **READ COMMITTED (Por defecto):** Utilizado para operaciones OLTP estándar (registro de comanda, consulta de catálogo, carga de partes diarios).
- **REPEATABLE READ:** Exigido para:
  1. Liquidación y split de cuentas en cafetería (`cafeteria.asignaciones_cuenta`).
  2. Conciliación y cierre de lote en pasarelas de pago (`core.intentos_pago`).
- **SERIALIZABLE:** Utilizado exclusivamente en la confirmación de reservas de última habitación hotelera en alta temporada o adjudicación de promesas inmobiliarias concurrentes sobre una misma unidad.

### B. Patrón de Bloqueo Pesimista con Timeout (Pessimistic Locking)
Para prevenir sobreventas de cupo hotelero o carreras en pedidos de cafetería, se utiliza `SELECT ... FOR UPDATE` acotado temporalmente:

```sql
-- Bloqueo pesimista con timeout defensivo para reserva de inventario hotelero
BEGIN;
SET LOCAL statement_timeout = '3000ms';
SET LOCAL lock_timeout = '1500ms';

-- Bloquea las filas de cupo para las fechas de la estadía
SELECT id, cupo_disponible, cupo_total_inventario
FROM hotel.cupos_fecha_tipo
WHERE tenant_id = '...'
  AND tipo_habitacion_id = '...'
  AND fecha BETWEEN '2026-11-01' AND '2026-11-05'
FOR UPDATE;

-- Si cupo_disponible < 1 para cualquier fecha: ROLLBACK y error HTTP 409 Conflict.
-- Si hay cupo suficiente:
UPDATE hotel.cupos_fecha_tipo
SET cupo_retenido_ofertas = cupo_retenido_ofertas + 1,
    version = version + 1
WHERE tenant_id = '...'
  AND tipo_habitacion_id = '...'
  AND fecha BETWEEN '2026-11-01' AND '2026-11-05';

COMMIT;
```

---

## 4. Idempotencia y Procesamiento de Eventos Externos

Para evitar duplicaciones por reintentos de red o caídas de webhook, se implementa una tabla de control de idempotencia basada en hash de solicitud:

```sql
CREATE TABLE core.registro_idempotencia (
    tenant_id UUID NOT NULL REFERENCES core.tenants(id),
    idempotency_key VARCHAR(128) NOT NULL,
    operacion VARCHAR(100) NOT NULL,
    request_hash_sha256 VARCHAR(64) NOT NULL,
    response_status SMALLINT NOT NULL,
    response_body_json JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    PRIMARY KEY (tenant_id, idempotency_key)
);

-- Regla: Si llega la misma clave con el MISMO request_hash, se retorna la respuesta ya calculada.
-- Si llega la misma clave con DISTINTO request_hash, se rechaza inmediatamente con HTTP 422 Unprocessable Entity.
```

---

## 5. Privilegios de Acceso y Roles de Base de Datos (Least Privilege)

```sql
-- Creación de roles de base de datos segregados
CREATE ROLE app_user WITH LOGIN PASSWORD '...';             -- Conexión de pool de microservicios
CREATE ROLE app_reporting WITH LOGIN PASSWORD '...';        -- Réplica de solo lectura / BI
CREATE ROLE app_migrator WITH LOGIN PASSWORD '...';         -- Solo para pipeline CI/CD de DDL

-- Concesión de privilegios mínimos
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA core, cafeteria, hotel, inmobiliaria, constructora TO app_user, app_reporting;

-- app_user tiene permisos de DML sobre tablas de negocio
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA core, cafeteria, hotel, inmobiliaria, constructora TO app_user;
-- Excepción: Tabla de auditoría es estrictamente APPEND-ONLY
REVOKE UPDATE, DELETE ON core.acciones_auditadas FROM app_user;

-- app_reporting tiene acceso estrictamente SELECT
GRANT SELECT ON ALL TABLES IN SCHEMA core, cafeteria, hotel, inmobiliaria, constructora TO app_reporting;
```

---

## 6. Seguridad de Datos, Cifrado y Cumplimiento Legal (Ley 19.628 / 21.719)

1. **Datos Sensibles (PII):**
   - Nombres, correos, teléfonos y RUTs de clientes (`core.usuarios_identidad`, `inmobiliaria.contactos_persona`, `hotel.reservas`) deben residir en volúmenes cifrados en reposo mediante **LUKS / AWS KMS** (AES-256).
   - En backups lógicos y logs de depuración, el RUT y el teléfono se anonimizan (`12.345.***-*` y `+569****1234`).
2. **Cifrado de Secretos de Integración:**
   - Credenciales de API de proveedores (Transbank, SII, WhatsApp API) **nunca** se almacenan en texto plano en `core.perfiles_conector`.
   - Se almacenan cifradas con clave asimétrica o mediante un gestor de secretos externo (AWS Secrets Manager / Vault), registrando en base de datos únicamente el identificador opaco (`secret_arn`).
3. **Políticas de Retención y Purga:**
   - Documentos tributarios (DTE) y transacciones financieras: Retención obligatoria de **6 años** por normativa tributaria chilena (SII).
   - Eventos de auditoría operativa y webhooks OTA procesados: Retención de **1 año**, con compactación mensual hacia almacenamiento en frío (Cold Storage).
   - Registros de prospectos inmobiliarios descalificados: Purga o anonimización a los **24 meses** de inactividad conforme a la Ley 21.719.

---

## 7. Estrategia de Migración y Recuperación ante Fallos

- **Objetivos de Recuperación (RPO / RTO):**
  - **RPO (Recovery Point Objective):** $\le 1$ minuto (habilitado mediante streaming replication síncrona y archiving continuo de WALs a S3/GCS).
  - **RTO (Recovery Time Objective):** $\le 15$ minutos (failover automático mediante Patroni / PgBouncer).
- **Estrategia Zero-Downtime:**
  - Toda migración DDL futura debe seguir el patrón *Expand and Contract*.
  - Añadir columnas como `NULLABLE` primero, poblar con backfill en segundo plano y aplicar restricción `NOT NULL` mediante `VALIDATE CONSTRAINT` sin bloqueos de tabla.
