-- ============================================================================
-- ESQUEMA PROPUESTO: Constructora, Obras, Control de Costos y Punch List
-- ============================================================================
CREATE SCHEMA IF NOT EXISTS constructora;

CREATE TABLE IF NOT EXISTS constructora.constructora_obras (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
codigo_obra varchar(16) NOT NULL,
nombre varchar(128) NOT NULL,
estado varchar(24) NOT NULL,
fecha_inicio date NOT NULL,
    CONSTRAINT uq_constructora_obras_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE constructora.constructora_obras ENABLE ROW LEVEL SECURITY;
ALTER TABLE constructora.constructora_obras FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_constructora_obras_tenant_isolation ON constructora.constructora_obras;
CREATE POLICY p_constructora_obras_tenant_isolation ON constructora.constructora_obras
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS constructora.constructora_partidas_presupuesto (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
obra_id uuid NOT NULL,
codigo_item varchar(32) NOT NULL,
costo_presupuestado_clp bigint NOT NULL,
costo_comprometido_clp bigint DEFAULT 0,
    CONSTRAINT uq_constructora_partidas_presupuesto_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE constructora.constructora_partidas_presupuesto ENABLE ROW LEVEL SECURITY;
ALTER TABLE constructora.constructora_partidas_presupuesto FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_constructora_partidas_presupuesto_tenant_isolation ON constructora.constructora_partidas_presupuesto;
CREATE POLICY p_constructora_partidas_presupuesto_tenant_isolation ON constructora.constructora_partidas_presupuesto
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS constructora.constructora_ordenes_compra (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
obra_id uuid NOT NULL,
numero_oc varchar(32) NOT NULL,
total_oc_clp bigint NOT NULL,
estado varchar(24) NOT NULL,
    CONSTRAINT uq_constructora_ordenes_compra_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE constructora.constructora_ordenes_compra ENABLE ROW LEVEL SECURITY;
ALTER TABLE constructora.constructora_ordenes_compra FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_constructora_ordenes_compra_tenant_isolation ON constructora.constructora_ordenes_compra;
CREATE POLICY p_constructora_ordenes_compra_tenant_isolation ON constructora.constructora_ordenes_compra
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS constructora.constructora_detalles_oc (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
orden_compra_id uuid NOT NULL,
partida_id uuid NOT NULL,
cantidad numeric(12,3) NOT NULL,
precio_unitario_clp bigint NOT NULL,
    CONSTRAINT uq_constructora_detalles_oc_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE constructora.constructora_detalles_oc ENABLE ROW LEVEL SECURITY;
ALTER TABLE constructora.constructora_detalles_oc FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_constructora_detalles_oc_tenant_isolation ON constructora.constructora_detalles_oc;
CREATE POLICY p_constructora_detalles_oc_tenant_isolation ON constructora.constructora_detalles_oc
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS constructora.constructora_recepciones (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
orden_compra_id uuid NOT NULL,
guia_despacho_folio varchar(64) NOT NULL,
estado_conforme boolean NOT NULL,
    CONSTRAINT uq_constructora_recepciones_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE constructora.constructora_recepciones ENABLE ROW LEVEL SECURITY;
ALTER TABLE constructora.constructora_recepciones FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_constructora_recepciones_tenant_isolation ON constructora.constructora_recepciones;
CREATE POLICY p_constructora_recepciones_tenant_isolation ON constructora.constructora_recepciones
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS constructora.constructora_punchlist (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
obra_id uuid NOT NULL,
descripcion_defecto text NOT NULL,
contratista_id uuid NOT NULL,
cerrada_por_ito_id uuid,
estado varchar(24) NOT NULL,
    CONSTRAINT chk_punchlist_segregation CHECK (cerrada_por_ito_id IS NULL OR cerrada_por_ito_id != contratista_id),
    CONSTRAINT uq_constructora_punchlist_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE constructora.constructora_punchlist ENABLE ROW LEVEL SECURITY;
ALTER TABLE constructora.constructora_punchlist FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_constructora_punchlist_tenant_isolation ON constructora.constructora_punchlist;
CREATE POLICY p_constructora_punchlist_tenant_isolation ON constructora.constructora_punchlist
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);
