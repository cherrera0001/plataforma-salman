# Implementation Plan: {{FEATURE}}
**Date**: {{FECHA}} | **Spec**: {{RUTA_SPEC}} | **Master Baseline**: {{VERSION_HASH}}
**Status**: {{PRELIMINAR_REVISADO_EJECUTABLE_APROBADO}}

## Summary
Solución propuesta y por que satisface la especificación sin ampliar alcance.

## Technical Context
Lenguaje/versión; dependencias y licencias; framework; persistencia; pruebas; plataforma; carga; objetivos; límites; código existente inspeccionado; decisiones pendientes. No fijar versiones inventadas. En ausencia de decisión aprobada, proponer un stack coherente con ADR y declarar estado preliminar.

## Constitution Check
Principio -> control concreto -> prueba -> estado. Verificar ruta y versión de constitución. Pruebas OBLIGATORIAS. Aplicar privacidad, dinero y aislamiento; no aceptar comprobaciones omitidas por archivo faltante.

## Project Structure
Árbol real o propuesto identificado; rutas exactas de componentes, migraciones, tests y contratos. Eliminar opciones descartadas. Conservar un solo plan coherente. No atribuir rutas propuestas a un repositorio que no fue inspeccionado.

## Research and Decisions
Enlazar research.md, ADR, fuentes oficiales, alternativas y bloqueos. Servicios externos con capacidad/cuenta/permiso y estados demo/sandbox/producción separados.

## Data, Contracts and Transactions
Modelo, restricciones, eventos, autoridad de datos, transacciones, idempotencia, concurrencia, orden/reintentos, errores, compatibilidad y versionado. Precisar cambios de esquema, migración, integridad y recuperación.

## Implementation Strategy
Incrementos verticales con historias, dependencias tipadas, componentes compartidos, archivos permitidos, contratos consumidos/producidos y criterios para paralelizar. No ocultar ciclos como tareas pendientes indefinidas.

## Testing and Evidence
Datos ficticios, comandos reales a usar una vez conocidos, esperado/observado, entornos, casos positivos/negativos, seguridad, carga, fallas y restauración. Tests OBLIGATORIOS y revisión de calidad de tests.

## Delivery and Operations
Observabilidad, soporte, despliegue, migraciones, feature flags, rollback o compensaciones, costo y autorizaciones. Un release no se habilita por terminar el plan.

## Complexity Tracking
Complejidad adicional -> necesidad -> alternativa simple rechazada -> costo/riesgo. No imponer microservicios por moda.

## Readiness
Decisiones bloqueantes, resultados de analyze/checklists, aprobador y versión. Tasks se genera después del plan, no se declara ya implementado por listar acciones.
