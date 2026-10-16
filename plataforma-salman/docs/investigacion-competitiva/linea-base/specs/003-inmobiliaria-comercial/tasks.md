# Tareas — Inmobiliaria comercial

**Estado: BLOCKED**. Tareas ejecutables de aclaración/diseño; no constituyen backlog de implementación aprobado. Identificadores locales a `003-inmobiliaria-comercial`. Dependencias en orden, sin paralelismo supuesto.

- [x] T001 Inventariar fuente, separar alcance y preservar IDs. Evidencia: spec.md y trazabilidad global.
- [x] T002 Derivar modelo conceptual, amenazas y catálogo de aceptación. Evidencia: data-model.md, plan.md y acceptance.md. Esto no equivale a aprobación.
- [ ] T003 Resolver Q-INM-01: proyectos, CRM y captura autorizada de leads; Q-INM-02: reserva, vigencia y reembolsos; Q-INM-03: revisión legal de promesa y firma; Q-INM-04: garantías y responsables. Responsable: cliente y responsables de operación, con revisor tributario/legal según corresponda. Depende de T002. Salida: respuestas firmadas o registradas con fecha y evidencia.
- [ ] T004 Ratificar alternativas y constitución, actualizar ADR y permisos por empresa. Depende de T003. Salida: decisión y matriz de roles aprobadas.
- [ ] T005 Completar contratos técnicos con ejemplos, errores, idempotencia y compatibilidad. Depende de T004. Salida: contrato revisado por productor y consumidor.
- [ ] T006 Convertir acceptance.md en casos de prueba concretos previos a código, con datos autorizados, carga y fallos. Depende de T005. Salida: escenarios revisados, incluidos ADV-001 a ADV-003.
- [ ] T007 Reejecutar controles documentales y análisis de Spec Kit cuando esté disponible; cerrar hallazgos y generar backlog de desarrollo por historia. Depende de T006. Salida: informe sin bloqueos y aprobación de inicio de siguiente fase.

No se incluye implementar T008 ni tareas de despliegue. Crear tareas de implementación verificables solo tras resolver T003–T007, siguiendo las historias de spec.md.
