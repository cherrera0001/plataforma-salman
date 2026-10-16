-- ============================================================================
-- ESQUEMA PROPUESTO: Cafetería, Mesas, KDS y POS
-- ============================================================================
CREATE SCHEMA IF NOT EXISTS cafeteria;

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_mesas (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
codigo varchar(16) NOT NULL,
sector varchar(32) NOT NULL,
capacidad int NOT NULL,
estado varchar(24) NOT NULL,
    CONSTRAINT uq_cafeteria_mesas_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_mesas ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_mesas FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_mesas_tenant_isolation ON cafeteria.cafeteria_mesas;
CREATE POLICY p_cafeteria_mesas_tenant_isolation ON cafeteria.cafeteria_mesas
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_sesiones_mesa (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
mesa_id uuid NOT NULL,
estado varchar(24) NOT NULL,
aperturada_at timestamptz DEFAULT clock_timestamp(),
comensales_count int DEFAULT 1,
    CONSTRAINT uq_cafeteria_sesiones_mesa_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_sesiones_mesa ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_sesiones_mesa FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_sesiones_mesa_tenant_isolation ON cafeteria.cafeteria_sesiones_mesa;
CREATE POLICY p_cafeteria_sesiones_mesa_tenant_isolation ON cafeteria.cafeteria_sesiones_mesa
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_pedidos (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
sesion_mesa_id uuid NOT NULL,
numero_orden varchar(32) NOT NULL,
total_bruto_clp bigint NOT NULL,
estado varchar(24) NOT NULL,
    CONSTRAINT uq_cafeteria_pedidos_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_pedidos ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_pedidos FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_pedidos_tenant_isolation ON cafeteria.cafeteria_pedidos;
CREATE POLICY p_cafeteria_pedidos_tenant_isolation ON cafeteria.cafeteria_pedidos
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_detalles_pedido (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
pedido_id uuid NOT NULL,
producto_id uuid NOT NULL,
cantidad int NOT NULL,
precio_unitario_clp bigint NOT NULL,
estado_kds varchar(24) NOT NULL,
    CONSTRAINT uq_cafeteria_detalles_pedido_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_detalles_pedido ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_detalles_pedido FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_detalles_pedido_tenant_isolation ON cafeteria.cafeteria_detalles_pedido;
CREATE POLICY p_cafeteria_detalles_pedido_tenant_isolation ON cafeteria.cafeteria_detalles_pedido
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_cuentas (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
sesion_mesa_id uuid NOT NULL,
total_cuenta_clp bigint NOT NULL,
saldo_pendiente_clp bigint NOT NULL,
estado varchar(24) NOT NULL,
version int DEFAULT 1,
    CONSTRAINT chk_total_cuenta CHECK (total_cuenta_clp >= 0 AND saldo_pendiente_clp >= 0),
    CONSTRAINT uq_cafeteria_cuentas_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_cuentas ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_cuentas FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_cuentas_tenant_isolation ON cafeteria.cafeteria_cuentas;
CREATE POLICY p_cafeteria_cuentas_tenant_isolation ON cafeteria.cafeteria_cuentas
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_divisiones_cuenta (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
cuenta_id uuid NOT NULL,
numero_parte int NOT NULL,
monto_asignado_clp bigint NOT NULL,
estado varchar(24) NOT NULL,
    CONSTRAINT uq_cafeteria_divisiones_cuenta_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_divisiones_cuenta ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_divisiones_cuenta FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_divisiones_cuenta_tenant_isolation ON cafeteria.cafeteria_divisiones_cuenta;
CREATE POLICY p_cafeteria_divisiones_cuenta_tenant_isolation ON cafeteria.cafeteria_divisiones_cuenta
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_pagos_cuenta (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
division_cuenta_id uuid NOT NULL,
monto_clp bigint NOT NULL,
medio_pago varchar(32) NOT NULL,
estado_pago varchar(24) NOT NULL,
    CONSTRAINT uq_cafeteria_pagos_cuenta_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_pagos_cuenta ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_pagos_cuenta FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_pagos_cuenta_tenant_isolation ON cafeteria.cafeteria_pagos_cuenta;
CREATE POLICY p_cafeteria_pagos_cuenta_tenant_isolation ON cafeteria.cafeteria_pagos_cuenta
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_insumos (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
codigo varchar(32) NOT NULL,
nombre varchar(128) NOT NULL,
stock_actual numeric(12,3) NOT NULL,
stock_minimo numeric(12,3) NOT NULL,
    CONSTRAINT uq_cafeteria_insumos_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_insumos ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_insumos FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_insumos_tenant_isolation ON cafeteria.cafeteria_insumos;
CREATE POLICY p_cafeteria_insumos_tenant_isolation ON cafeteria.cafeteria_insumos
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);

CREATE TABLE IF NOT EXISTS cafeteria.cafeteria_movimientos_inventario (
id uuid PRIMARY KEY,
tenant_id uuid NOT NULL,
insumo_id uuid NOT NULL,
tipo_movimiento varchar(24) NOT NULL,
cantidad numeric(12,3) NOT NULL,
motivo varchar(64) NOT NULL,
    CONSTRAINT uq_cafeteria_movimientos_inventario_tenant_id UNIQUE (tenant_id, id)
);

ALTER TABLE cafeteria.cafeteria_movimientos_inventario ENABLE ROW LEVEL SECURITY;
ALTER TABLE cafeteria.cafeteria_movimientos_inventario FORCE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS p_cafeteria_movimientos_inventario_tenant_isolation ON cafeteria.cafeteria_movimientos_inventario;
CREATE POLICY p_cafeteria_movimientos_inventario_tenant_isolation ON cafeteria.cafeteria_movimientos_inventario
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::uuid);
