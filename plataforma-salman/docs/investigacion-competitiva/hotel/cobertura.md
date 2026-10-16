# Cobertura de investigación — hotel

L1 documental y reconstrucción funcional; **sin runtime observado**. Cada área distingue evidencia suficiente para proponer conducta de integración o decisión todavía no validada. La profundidad no es uniforme por plataforma.

| Área solicitada | Evidencia | Nivel real / conclusión acotada | Historia y requisitos propios | Límite/bloqueo |
|---|---|---|---|---|
| Disponibilidad y habitaciones | H01/H02/H05/H18 | Manual/API; inventario, asignación y preparación diferenciados | H1/H2; FR-001,005,016 | PMS/inventario real y correspondencia de recursos pendientes |
| Reserva directa y modificación | H11/H12 | Manual; precio/cancelación/devolución separados | H1; FR-002,018 | Política y conector para aplicar cambios no seleccionados |
| OTA y sincronización | H13/H15/H17; H03 | Manual/API de evento/acuse; oferta de distribución | H1/H3; FR-003,017,020 | No hay credenciales ni prueba de integración; Channels Plus no demuestra PMS connector |
| Check-in y check-out | H16/H05 | Guía de integración y manual operativo | H2; FR-006,008,009,016 | Registro/firma/identidad y política Chile requieren validación |
| Housekeeping y mantenimiento | H05/H16/H18 | Manual: limpieza/inspección, asignación y ocupación | H2; FR-008,016 | Roles/plazos y disponibilidad operativa del cliente no ratificados |
| Servicio a habitación y extras | H14 | API/caso de cargo y tarea; periodicidad propuesta propia | H2/H3; FR-007,009,019 | Interfaz gastronómica opcional, regla de facturación entre empresas pendiente |
| Cobros/conciliación | H11/H14; 000 | Manual: cancelación/cargo no implica devolución/pago | H1/H2; FR-004,018,019 | Webpay/SII y política fiscal conservan Q-CORE-02 |
| Tarifas y autonomía | H10/H12 | Manual de límites y recalculación; sin habilitar pricing | H1/H3; FR-011,018; US-HOT-004 candidata | No se adopta tarifa dinámica ni objetivos de ingreso de proveedor |
| Concierge y reserva conversacional | H06/H07/H08/H09; RF-HOT-04 | Ayuda/oferta: respuesta, motor y transferencia; efectos delimitados | H3; FR-010–014,017,018 | Escritura/cobro/reversión y tasas reales no probadas |
| Comparación PMS pequeño vs enterprise | H04/H05/H01/H02 | Oferta de Little Hotelier y documentación PMS | ADR-002/006; research | No se concluye mejor proveedor sin TCO/plan/API/operación real |
