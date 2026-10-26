# Feature Specification: {{ID_Y_NOMBRE}}
**Feature Directory**: {{RUTA_REAL}}
**Created**: {{FECHA}}
**Status**: {{BORRADOR_EN_REVISION_APROBADO}}
**Input**: {{OBJETIVO_Y_FUENTE}}
**Master Baseline**: {{VERSION_Y_HASH}}
**Master Requirement IDs**: {{IDS_ESTABLES}}
**Owner / Reviewer**: {{ROL_AUTOR_Y_REVISOR}}

## Context and Scope
Objetivo empresarial, sociedad/unidad, capacidad, usuarios, origen de demanda y alcance de esta entrega. Definir exclusiones y dependencias sin eliminar el alcance futuro del maestro.

## User Scenarios & Testing (mandatory)
### User Story 1 - {{TÍTULO}} (Priority: {{P1_P2_P3}})
Como {{ACTOR}}, necesito {{ACCIÓN}} para {{RESULTADO}}.
**Business Criticality**: {{P0_P1_P2_MAESTRO}}
**Why this priority**: {{JUSTIFICACION}}
**Independent Test**: {{RESULTADO_OBSERVABLE}}
**Acceptance Scenarios**:
1. **Given** {{ESTADO_Y_DATOS}}, **When** {{ACCIÓN}}, **Then** {{RESULTADO_Y_EFECTOS}}.
2. Caso negativo/falla/permisos/duplicacion según riesgo.
Cada historia incluye cuentas, stock, tareas, privacidad y auditoría afectados; indicar cuando no aplica.

## Requirements (mandatory)
### Functional Requirements
- **FR-001**: {{DEBE_HACER_ALGO_COMPROBABLE}}. Fuente maestro: {{ID}}. Regla: {{ID_REGLA}}.
Por FR: precondiciones, disparador, entradas/validaciones, salida, estados, fórmulas, autorizaciones, errores, compensación, historial y evidencia requerida. No dejar fórmulas implícitas.
### Business Rules and State Transitions
Tabla estado/evento/permiso/precondición/nuevo_estado/efectos/error. Incluir condiciones de expiración, reintentos, cancelación y cambios cuando proceda.
### Key Entities
Entidades conceptuales, identificadores y relaciones; detalles técnicos en data-model.md. No introducir un segundo inventario o saldo independiente por conveniencia de un canal.
### Edge Cases
Concurrencia, duplicados, mensajes tardios, parámetros invalidos, faltantes, permisos, cambios, pérdida de conexión y conciliación según riesgo.
### Cross-Cutting Constraints
Materializar las obligaciones relevantes de constitución, dinero, multiempresa, privacidad, accesibilidad y continuidad. No remitir todo a un capítulo distante.

## Testing Requirements - OBLIGATORIAS
Se requieren pruebas de esta funcionalidad; NO son opcionales. Definir unitarias, integración, contrato y flujos completos apropiados; incluir casos negativos/seguridad/concurrencia/recuperación según riesgo. No afirmar resultados ahora. Cada prueba se convertira en tarea y evidencia tras implementar.

## Success Criteria (mandatory)
- **SC-001**: {{METRICA_DE_SOFTWARE_OBSERVABLE_CON_UMBRAL_Y_ENTORNO}}.
Separar indicadores comerciales posteriores de criterios para aceptar software. No prometer ocupación o ventas por construir un módulo.

## Clarifications and Decisions
{{ID_DECISION;ESTADO;RESPONSABLE;ALTERNATIVA;GATE_BLOQUEADO}}
Resolver preguntas respondidas en fuentes antes de preguntar. Parametrizar pendientes seguros; no simular aprobaciones.

## Traceability and Review
Maestro -> FR/US/AC -> contrato/datos -> prueba propuesta. Registrar revisión, hallazgos y aprobación real. Un spec aprobado no significa código ni producción autorizados.
