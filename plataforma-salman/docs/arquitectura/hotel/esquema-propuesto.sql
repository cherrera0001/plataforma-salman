-- ============================================================================
-- ESQUEMA PROPUESTO: Hotel, Reservas, Cupos y Concierge IA
-- ============================================================================
CREATE SCHEMA IF NOT EXISTS hotel;

CREATE TABLE IF NOT EXISTS hotel.hotel_tipos_habitacion (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
codigo varchar(16) NOT NULL,
nombre varchar(64) NOT NULL,
capacidad_max int NOT NULL,
tarifa_base_clp bigint NOT NULL,
    CONSTRAINT uq_hotel_tipos_habitacion_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE hotel.hotel_tipos_habitacion ENABLE ROW LEVEL SECURITY;
ALTER TABLE hotel.hotel_tipos_habitacion FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_hotel_tipos_habitacion_tenant_isolation ON hotel.hotel_tipos_habitacion;
CREATE POLICY p_hotel_tipos_habitacion_tenant_isolation ON hotel.hotel_tipos_habitacion
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS hotel.hotel_habitaciones (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
tipo_id uuid NOT NULL,
numero varchar(16) NOT NULL,
estado_operativo varchar(24) NOT NULL,
estado_limpieza varchar(24) NOT NULL,
    CONSTRAINT uq_hotel_habitaciones_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE hotel.hotel_habitaciones ENABLE ROW LEVEL SECURITY;
ALTER TABLE hotel.hotel_habitaciones FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_hotel_habitaciones_tenant_isolation ON hotel.hotel_habitaciones;
CREATE POLICY p_hotel_habitaciones_tenant_isolation ON hotel.hotel_habitaciones
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS hotel.hotel_cupos_diarios (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
tipo_id uuid NOT NULL,
fecha date NOT NULL,
cupo_total int NOT NULL,
cupo_reservado int DEFAULT 0,
cupo_bloqueado int DEFAULT 0,
version int DEFAULT 1,
    CONSTRAINT chk_cupo_disponible CHECK (cupo_total >= (cupo_reservado + cupo_bloqueado)),
    CONSTRAINT uq_hotel_cupos_diarios_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE hotel.hotel_cupos_diarios ENABLE ROW LEVEL SECURITY;
ALTER TABLE hotel.hotel_cupos_diarios FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_hotel_cupos_diarios_tenant_isolation ON hotel.hotel_cupos_diarios;
CREATE POLICY p_hotel_cupos_diarios_tenant_isolation ON hotel.hotel_cupos_diarios
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS hotel.hotel_reservas (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
codigo_reserva varchar(32) NOT NULL,
fecha_checkin date NOT NULL,
fecha_checkout date NOT NULL,
total_clp bigint NOT NULL,
estado varchar(24) NOT NULL,
    CONSTRAINT uq_hotel_reservas_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE hotel.hotel_reservas ENABLE ROW LEVEL SECURITY;
ALTER TABLE hotel.hotel_reservas FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_hotel_reservas_tenant_isolation ON hotel.hotel_reservas;
CREATE POLICY p_hotel_reservas_tenant_isolation ON hotel.hotel_reservas
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS hotel.hotel_huespedes (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
pasaporte_rut varchar(32) NOT NULL,
nombre_completo varchar(128) NOT NULL,
email varchar(255) NOT NULL,
telefono varchar(32),
    CONSTRAINT uq_hotel_huespedes_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE hotel.hotel_huespedes ENABLE ROW LEVEL SECURITY;
ALTER TABLE hotel.hotel_huespedes FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_hotel_huespedes_tenant_isolation ON hotel.hotel_huespedes;
CREATE POLICY p_hotel_huespedes_tenant_isolation ON hotel.hotel_huespedes
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS hotel.hotel_estadias (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
reserva_id uuid NOT NULL,
habitacion_id uuid NOT NULL,
checkin_real_at timestamptz,
checkout_real_at timestamptz,
    CONSTRAINT uq_hotel_estadias_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE hotel.hotel_estadias ENABLE ROW LEVEL SECURITY;
ALTER TABLE hotel.hotel_estadias FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_hotel_estadias_tenant_isolation ON hotel.hotel_estadias;
CREATE POLICY p_hotel_estadias_tenant_isolation ON hotel.hotel_estadias
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS hotel.hotel_mensajes_concierge (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
reserva_id uuid NOT NULL,
remitente varchar(24) NOT NULL,
contenido text NOT NULL,
requiere_humano boolean DEFAULT false,
    CONSTRAINT uq_hotel_mensajes_concierge_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE hotel.hotel_mensajes_concierge ENABLE ROW LEVEL SECURITY;
ALTER TABLE hotel.hotel_mensajes_concierge FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_hotel_mensajes_concierge_tenant_isolation ON hotel.hotel_mensajes_concierge;
CREATE POLICY p_hotel_mensajes_concierge_tenant_isolation ON hotel.hotel_mensajes_concierge
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);
