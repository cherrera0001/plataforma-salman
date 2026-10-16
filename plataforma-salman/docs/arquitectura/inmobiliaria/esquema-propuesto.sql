-- ============================================================================
-- ESQUEMA PROPUESTO: Inmobiliaria Comercial, Leads, Promesas y Unidades
-- ============================================================================
CREATE SCHEMA IF NOT EXISTS inmobiliaria;

CREATE TABLE IF NOT EXISTS inmobiliaria.inmobiliaria_proyectos (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
codigo varchar(16) NOT NULL,
nombre varchar(128) NOT NULL,
comuna varchar(64) NOT NULL,
estado varchar(24) NOT NULL,
    CONSTRAINT uq_inmobiliaria_proyectos_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE inmobiliaria.inmobiliaria_proyectos ENABLE ROW LEVEL SECURITY;
ALTER TABLE inmobiliaria.inmobiliaria_proyectos FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_inmobiliaria_proyectos_tenant_isolation ON inmobiliaria.inmobiliaria_proyectos;
CREATE POLICY p_inmobiliaria_proyectos_tenant_isolation ON inmobiliaria.inmobiliaria_proyectos
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS inmobiliaria.inmobiliaria_etapas (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
proyecto_id uuid NOT NULL,
nombre varchar(64) NOT NULL,
fecha_entrega_estimada date NOT NULL,
    CONSTRAINT uq_inmobiliaria_etapas_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE inmobiliaria.inmobiliaria_etapas ENABLE ROW LEVEL SECURITY;
ALTER TABLE inmobiliaria.inmobiliaria_etapas FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_inmobiliaria_etapas_tenant_isolation ON inmobiliaria.inmobiliaria_etapas;
CREATE POLICY p_inmobiliaria_etapas_tenant_isolation ON inmobiliaria.inmobiliaria_etapas
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS inmobiliaria.inmobiliaria_unidades (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
etapa_id uuid NOT NULL,
numero varchar(16) NOT NULL,
precio_lista_uf numeric(12,4) NOT NULL,
estado_comercial varchar(24) NOT NULL,
version int DEFAULT 1,
    CONSTRAINT chk_precio_uf CHECK (precio_lista_uf > 0),
    CONSTRAINT uq_inmobiliaria_unidades_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE inmobiliaria.inmobiliaria_unidades ENABLE ROW LEVEL SECURITY;
ALTER TABLE inmobiliaria.inmobiliaria_unidades FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_inmobiliaria_unidades_tenant_isolation ON inmobiliaria.inmobiliaria_unidades;
CREATE POLICY p_inmobiliaria_unidades_tenant_isolation ON inmobiliaria.inmobiliaria_unidades
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS inmobiliaria.inmobiliaria_leads (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
rut_o_pasaporte varchar(32) NOT NULL,
nombre varchar(128) NOT NULL,
email varchar(255) NOT NULL,
canal_captacion varchar(32) NOT NULL,
    CONSTRAINT uq_inmobiliaria_leads_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE inmobiliaria.inmobiliaria_leads ENABLE ROW LEVEL SECURITY;
ALTER TABLE inmobiliaria.inmobiliaria_leads FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_inmobiliaria_leads_tenant_isolation ON inmobiliaria.inmobiliaria_leads;
CREATE POLICY p_inmobiliaria_leads_tenant_isolation ON inmobiliaria.inmobiliaria_leads
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS inmobiliaria.inmobiliaria_cotizaciones (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
lead_id uuid NOT NULL,
unidad_id uuid NOT NULL,
precio_ofrecido_uf numeric(12,4) NOT NULL,
vigencia_dias int DEFAULT 1,
    CONSTRAINT uq_inmobiliaria_cotizaciones_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE inmobiliaria.inmobiliaria_cotizaciones ENABLE ROW LEVEL SECURITY;
ALTER TABLE inmobiliaria.inmobiliaria_cotizaciones FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_inmobiliaria_cotizaciones_tenant_isolation ON inmobiliaria.inmobiliaria_cotizaciones;
CREATE POLICY p_inmobiliaria_cotizaciones_tenant_isolation ON inmobiliaria.inmobiliaria_cotizaciones
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS inmobiliaria.inmobiliaria_reservas_unidad (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
unidad_id uuid NOT NULL,
lead_id uuid NOT NULL,
monto_reserva_clp bigint NOT NULL,
estado varchar(24) NOT NULL,
    CONSTRAINT uq_inmobiliaria_reservas_unidad_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE inmobiliaria.inmobiliaria_reservas_unidad ENABLE ROW LEVEL SECURITY;
ALTER TABLE inmobiliaria.inmobiliaria_reservas_unidad FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_inmobiliaria_reservas_unidad_tenant_isolation ON inmobiliaria.inmobiliaria_reservas_unidad;
CREATE POLICY p_inmobiliaria_reservas_unidad_tenant_isolation ON inmobiliaria.inmobiliaria_reservas_unidad
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS inmobiliaria.inmobiliaria_promesas (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
unidad_id uuid NOT NULL,
lead_id uuid NOT NULL,
precio_pactado_uf numeric(12,4) NOT NULL,
estado_firma varchar(24) NOT NULL,
    CONSTRAINT uq_inmobiliaria_promesas_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE inmobiliaria.inmobiliaria_promesas ENABLE ROW LEVEL SECURITY;
ALTER TABLE inmobiliaria.inmobiliaria_promesas FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_inmobiliaria_promesas_tenant_isolation ON inmobiliaria.inmobiliaria_promesas;
CREATE POLICY p_inmobiliaria_promesas_tenant_isolation ON inmobiliaria.inmobiliaria_promesas
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);
