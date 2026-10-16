-- Pruebas de Aislamiento Multi-Tenant con Rol app_user
\set ON_ERROR_STOP on

-- Dar permisos a app_user
GRANT USAGE ON SCHEMA core, cafeteria, hotel, inmobiliaria, constructora TO app_user;
GRANT ALL ON ALL TABLES IN SCHEMA core, cafeteria, hotel, inmobiliaria, constructora TO app_user;

-- Insertar datos base como administrador
SET ROLE postgres;
INSERT INTO cafeteria.cafeteria_mesas (id, tenant_id, codigo, sector, capacidad, estado)
VALUES 
  ('11110001-1111-1111-1111-111111111111', '22222222-2222-2222-2222-222222222222', 'M1', 'Terraza', 4, 'LIBRE'),
  ('22220002-2222-2222-2222-222222222222', '33333333-3333-3333-3333-333333333333', 'M10', 'Interior', 2, 'LIBRE')
ON CONFLICT (id) DO NOTHING;

-- Cambiar al rol de aplicacion app_user y fijar Tenant 22222222-2222-2222-2222-222222222222
SET ROLE app_user;
SET app.current_tenant_id = '22222222-2222-2222-2222-222222222222';

-- Comprobar que solo ve la mesa del Tenant 2
DO $$
DECLARE
  v_count INT;
BEGIN
  SELECT COUNT(*) INTO v_count FROM cafeteria.cafeteria_mesas;
  IF v_count != 1 THEN
    RAISE EXCEPTION 'Falla RLS: app_user ve % mesas, esperaba exactamente 1', v_count;
  END IF;
  RAISE NOTICE 'RLS de aislamiento en SELECT validado exitosamente: 1 mesa visible para tenant_id 2';
END $$;

-- Comprobar que app_user no puede insertar para otro tenant
DO $$
BEGIN
  BEGIN
    INSERT INTO cafeteria.cafeteria_mesas (id, tenant_id, codigo, sector, capacidad, estado)
    VALUES ('33330003-3333-3333-3333-333333333333', '33333333-3333-3333-3333-333333333333', 'M99', 'Terraza', 4, 'LIBRE');
    RAISE EXCEPTION 'Falla RLS: app_user pudo insertar para otro tenant_id';
  EXCEPTION WHEN insufficient_privilege THEN
    RAISE NOTICE 'RLS de aislamiento en INSERT validado exitosamente: rechazo de cross-tenant insert';
  END;
END $$;

RESET ROLE;
