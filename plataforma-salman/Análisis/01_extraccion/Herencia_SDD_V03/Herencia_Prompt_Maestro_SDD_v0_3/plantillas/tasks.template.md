# Tasks: {{FEATURE}}
**Input**: {{SPEC_PLAN_CONTRATOS_BASELINE}}
**Status**: PROPUESTA_NO_AUTORIZACION
**Tests**: OBLIGATORIAS. Incluir tareas para escribir y ejecutar pruebas; no son opcionales.

## Format and Traceability
Usar el formato nativo verificado: `- [ ] T001 [P] [US1] Descripcion con ruta de archivo`.
Cada ID es único dentro del paquete; clave global {{FEATURE}}/T001. `[P]` solo si no existen dependencias, conflictos de archivos ni estado compartido. Tareas administrativas pueden no tener historia, pero deben explicar su relación con el alcance.
Enlazar FR/AC y maestro en descripcion o tabla lateral. Indicar resultado, evidencia y dependencias. No marcar `[x]` por proponer la tarea.

## Phase 1: Setup
Preparar contexto, permisos, contrato de trabajo, rama/worktree, validadores y ambiente según plan. No incluir instalación/gasto fuera de la autorización.

## Phase 2: Foundational
Implementar prerequisites compartidos y migraciones con pruebas. Identificar que bloquea y que puede correr en paralelo.

## Phase 3: User Story 1
### Tests - MANDATORY
- [ ] T001 [US1] {{ESCRIBIR_PRUEBA_REGLA_CRITICA_Y_RUTA;FR;AC}}
- [ ] T002 [US1] {{EJECUTAR_PRUEBA_Y_REGISTRAR_RESULTADO_REAL}}
### Implementation
- [ ] T003 [US1] {{CAMBIO_CONCRETO_ARCHIVO;DEPENDE_T001;FR}}
- [ ] T004 [US1] {{PRUEBA_INTEGRACION_PERSISTENCIA_Y_NEGATIVOS}}
No conservar estos ejemplos literalmente al producir tasks reales.

## Phase N: Cross-Cutting Validation
Contratos, permisos, importe/fechas, concurrencia, seguridad, accesibilidad, recuperación, observabilidad, documentación y revisión independiente según el paquete. Adjuntar evidencia sin datos privados.

## Dependencies and Parallel Opportunities
Grafo de tareas, archivos exclusivos, puntos de integración y condiciones de bloqueo. No crear tareas de gran alcance como "programar plataforma".

## Implementation / Convergence Protocol
Después de implementación autorizada, converge revisa intención local. Nuevas tareas correctivas se agregan sin borrar/renumerar anteriores. Cambio de alcance vuelve a spec/plan por control de cambios, no se oculta como corrección. Límite de ciclos y gasto; escalar sin progreso.
