# Arquitectura de Datos y Modelos Visuales — Plataforma Salman

Este directorio contiene los artefactos formales, editables y técnicamente verificables que rigen la arquitectura de datos, el aislamiento multi-tenant y los flujos de comportamiento de Plataforma Salman.

## Estructura de Entregables
- [trazabilidad-modelos.md](trazabilidad-modelos.md): Matriz integral Historia → Requisito → Regla → Entidad → Restricción → Prueba.
- [validacion-global.md](validacion-global.md): Informe de ejecución de suites de comprobación estructural, semántica y PostgreSQL.
- [decisiones-pendientes.md](decisiones-pendientes.md): Registro de decisiones arquitectónicas y preguntas abiertas de negocio.

### Dominios
- [core/](core/): Multi-tenant, Organizaciones, Usuarios, Pagos, Idempotencia y Auditoría Agéntica.
- [cafeteria/](cafeteria/): Mesas, KDS, División de Cuentas, POS e Inventario.
- [hotel/](hotel/): Tipos de Habitación, Cupos Diarios, Reservas, Check-in y Concierge.
- [inmobiliaria/](inmobiliaria/): Proyectos, Unidades, Leads, Cotizaciones y Promesas de Compraventa.
- [constructora/](constructora/): Obras, Presupuesto, Órdenes de Compra y Punch List.
- [transversal/](transversal/): MER integrado, DBML global, diagramas C4 y mapa de dependencias.
- [pruebas/](pruebas/): DDL ejecutable, tests de RLS, restricciones de integridad y concurrencia.
