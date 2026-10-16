# Auditoría individual — HOT

Análisis del documento de entrada antes de integración. Fecha: 2026-10-16. Fuente conservada en inventario. No se presume aprobación del texto original.

| Dimensión | Ubicación | Evaluación y clasificación | Tratamiento |
|---|---|---|---|
| Problema y objetivos | §2 H1 | Centralizar reserva es propuesta, no diagnóstico levantado | Q-HOT-01 |
| Usuarios y responsabilidades | §2/5 | Huésped/recepción/housekeeping; propio o externo pendiente | Q-HOT-03 |
| Alcance y exclusiones | §0/5 | Menos de 50 habitaciones, PMS abandonado y cafetería son supuestos | Eliminar dependencia total, evaluar PMS |
| Historias y aceptación | §2 | Escenarios buenos; sobreventa global requiere control externo | ADV y F-006 |
| FR y reglas de negocio | §3 | 15 FR, fiscalidad y room service mal ubicado | F-002/004 |
| NFR y recuperación | §2/6 | SLO sincronización y agente; falla permite seguir vendiendo | F-006/013, cupos seguros |
| Datos conceptuales | §3 entidades | Reservas, cuenta y tarifas; falta separación ocupación/limpieza | data-model.md |
| Integraciones y dependencias | §5/6 | Booking/Airbnb directos o channel manager sin acceso | E-09/10; Q-HOT-02 |
| Legal y regulación | §1/5 | Datos de identidad, anticipo, factura y cancelación no definidos | Q-HOT-03 y fiscalidad |
| Seguridad y multi-tenancy | §6 amenazas | Pendiente; MCP público puede exponer disponibilidad/datos | Seguridad concierge/distribución |
| Arquitectura y tecnología | §6 | PMS propio asumido y worker justificado sin alternativa comparada | ADR-002/003 |
| Agentes y autonomía | §2 H3 / FR-010–014 | Cambios sin penalidad propuestos, monto y autenticación ausentes | Política inicial lectura; aprobación posterior |
| KPI y éxito | §4 | Nueve SC sin medición, 8 % upsell atribuido a vendor | Objetivo propuesto, no forecast |
| Riesgos, vacíos y supuestos | §5 | Siete preguntas y supuestos no validados | Feature BLOCKED |

Las afirmaciones individuales tienen evidencia literal y localización en afirmaciones.md. La severidad, impacto, propuesta y estado de los defectos materiales se registran por separado en hallazgos.md. Documento procesado completamente; validación externa parcial y decisiones pendientes explícitas.
