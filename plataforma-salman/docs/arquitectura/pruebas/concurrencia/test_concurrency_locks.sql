-- Pruebas de Concurrencia, SELECT FOR UPDATE y Control Optimista
\set ON_ERROR_STOP on

-- Preparar cuenta con version 1
INSERT INTO cafeteria.cafeteria_cuentas (id, tenant_id, sesion_mesa_id, total_cuenta_clp, saldo_pendiente_clp, estado, version)
VALUES ('44440001-4444-4444-4444-444444444444', '22222222-2222-2222-2222-222222222222', '55550001-5555-5555-5555-555555555555', 50000, 50000, 'ABIERTA', 1)
ON CONFLICT (id) DO NOTHING;

-- Simular lectura con bloqueo pesimista
BEGIN;
SET LOCAL lock_timeout = '2000ms';
SELECT id, saldo_pendiente_clp, version 
FROM cafeteria.cafeteria_cuentas 
WHERE id = '44440001-4444-4444-4444-444444444444'
FOR UPDATE;

-- Actualizacion con control optimista incrementando version
UPDATE cafeteria.cafeteria_cuentas
SET saldo_pendiente_clp = saldo_pendiente_clp - 20000,
    version = version + 1
WHERE id = '44440001-4444-4444-4444-444444444444' AND version = 1;

COMMIT;

-- Verificar saldo y version actualizados
DO $$
DECLARE
  v_rec RECORD;
BEGIN
  SELECT saldo_pendiente_clp, version INTO v_rec 
  FROM cafeteria.cafeteria_cuentas 
  WHERE id = '44440001-4444-4444-4444-444444444444';
  IF v_rec.saldo_pendiente_clp != 30000 OR v_rec.version != 2 THEN
    RAISE EXCEPTION 'Falla concurrencia: valores inesperados saldo=%, version=%', v_rec.saldo_pendiente_clp, v_rec.version;
  END IF;
  RAISE NOTICE 'Control de concurrencia y version optimista validado exitosamente';
END $$;
