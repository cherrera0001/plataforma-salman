-- Pruebas de Integridad Referencial y Restricciones CHECK
\set ON_ERROR_STOP on

-- 1. Insertar organizaciones y tenants válidos
INSERT INTO core.core_organizations (id, rut_tax_id, legal_name, is_active)
VALUES ('11111111-1111-1111-1111-111111111111', '76.123.456-7', 'Holding Gastronomico SpA', true)
ON CONFLICT (id) DO NOTHING;

INSERT INTO core.core_tenants (id, organization_id, slug, vertical_type, is_active)
VALUES 
  ('22222222-2222-2222-2222-222222222222', '11111111-1111-1111-1111-111111111111', 'cafe-central', 'cafeteria', true),
  ('33333333-3333-3333-3333-333333333333', '11111111-1111-1111-1111-111111111111', 'hotel-costanera', 'hotel', true)
ON CONFLICT (id) DO NOTHING;

-- 2. Prueba CHECK: Monto negativo debe fallar
DO $$
BEGIN
  BEGIN
    INSERT INTO core.core_payment_transactions (id, tenant_id, account_id, amount_clp, status, reconciliation_status)
    VALUES ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '22222222-2222-2222-2222-222222222222', 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', -5000, 'PENDING', 'UNRECONCILED');
    RAISE EXCEPTION 'CHECK de amount_clp negativo NO falló';
  EXCEPTION WHEN check_violation THEN
    RAISE NOTICE 'CHECK amount_clp >= 0 validado exitosamente';
  END;
END $$;

-- 3. Prueba CHECK: Segregación Punch List (cerrada_por_ito != contratista)
DO $$
BEGIN
  BEGIN
    INSERT INTO constructora.constructora_punchlist (id, tenant_id, obra_id, descripcion_defecto, contratista_id, cerrada_por_ito_id, estado)
    VALUES ('cccccccc-cccc-cccc-cccc-cccccccccccc', '22222222-2222-2222-2222-222222222222', 'dddddddd-dddd-dddd-dddd-dddddddddddd', 'Fisura en muro', '99999999-9999-9999-9999-999999999999', '99999999-9999-9999-9999-999999999999', 'CERRADA');
    RAISE EXCEPTION 'CHECK de segregacion punch list NO falló';
  EXCEPTION WHEN check_violation THEN
    RAISE NOTICE 'CHECK segregación ITO != Contratista validado exitosamente';
  END;
END $$;

-- 4. Prueba CHECK: Cupos de Hotel no pueden superar el total
DO $$
BEGIN
  BEGIN
    INSERT INTO hotel.hotel_cupos_diarios (id, tenant_id, tipo_id, fecha, cupo_total, cupo_reservado, cupo_bloqueado)
    VALUES ('eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee', '33333333-3333-3333-3333-333333333333', 'ffffffff-ffff-ffff-ffff-ffffffffffff', CURRENT_DATE, 10, 8, 5);
    RAISE EXCEPTION 'CHECK de cupo disponible negativo NO falló';
  EXCEPTION WHEN check_violation THEN
    RAISE NOTICE 'CHECK cupo_total >= (reservado + bloqueado) validado exitosamente';
  END;
END $$;
