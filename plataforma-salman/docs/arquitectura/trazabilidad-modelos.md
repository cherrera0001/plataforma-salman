# Matriz de Trazabilidad: Requisitos a Modelos Físicos y Pruebas

Esta matriz certifica que cada historia de usuario y requisito funcional cuenta con representación inequívoca en entidades, tablas relacionales, restricciones físicas y pruebas verificables.

| Historia | FR | Dominio | Entidad MER | Tabla MR / SQL | Regla / Invariante Clave | Prueba Validada |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `US-001` | `FR-001` | Core | `Organization`, `Tenant` | `core.core_tenants` | Aislamiento estricto multi-tenant por UUID | `test_rls_policies.sql` |
| `US-002` | `FR-002` | Core | `User` | `core.core_users` | Roles con privilegios mínimos (`app_user`, `app_reporting`) | `test_rls_policies.sql` |
| `US-003` | `FR-003` | Cafetería | `Mesa`, `SesionMesa` | `cafeteria.cafeteria_mesas` | Estado operativo de mesa y ocupación | `test_rls_policies.sql` |
| `US-004` | `FR-004` | Cafetería | `Cuenta`, `DivisionCuenta` | `cafeteria.cafeteria_divisiones_cuenta` | División de cuenta no anula ni muta comandas KDS | `test_concurrency_locks.sql` |
| `US-005` | `FR-005` | Hotel | `CupoDiario`, `Reserva` | `hotel.hotel_cupos_diarios` | Prevención de sobreventa con `SELECT FOR UPDATE` | `test_constraints_fks.sql` |
| `US-006` | `FR-006` | Hotel | `MensajeConcierge` | `hotel.hotel_mensajes_concierge` | Escalamiento agéntico Human-in-the-Loop | `03_hotel.sql` |
| `US-007` | `FR-007` | Inmobiliaria | `Unidad`, `ReservaUnidad` | `inmobiliaria.inmobiliaria_unidades` | Unidad reservada bloquea cotizaciones competidoras | `04_inmobiliaria.sql` |
| `US-008` | `FR-008` | Inmobiliaria | `PromesaCompraventa` | `inmobiliaria.inmobiliaria_promesas` | Firma electrónica con hash de documento inmutable | `04_inmobiliaria.sql` |
| `US-009` | `FR-009` | Constructora | `PartidaPresupuesto`, `OrdenCompra` | `constructora.constructora_partidas_presupuesto` | Saldo partida descuenta solo compromiso formal | `test_constraints_fks.sql` |
| `US-010` | `FR-010` | Constructora | `ObservacionPunchList` | `constructora.constructora_punchlist` | Segregación de funciones: ITO no puede ser el contratista | `test_constraints_fks.sql` |
| `US-011` | `FR-011` | Core | `PaymentTransaction` | `core.core_payment_transactions` | Montos financieros no negativos en CLP (`BIGINT`) | `test_constraints_fks.sql` |
| `US-012` | `FR-012` | Core | `AgentExecutionAudit` | `core.core_agent_executions` | Auditoría obligatoria con SHA256 de prompts y resultados | `01_core.sql` |
