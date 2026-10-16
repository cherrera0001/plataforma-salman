# Especificación — Core transversal

Feature: `000-core`. Fecha: 2026-10-16. Estado: **BLOCKED** para implementación.
Fuente: requisitos transversales de CAF §1, HOT §3 e INM §3 y encargo del cliente. Todos los FR y SC son **REQUISITOS PROPUESTOS**, pendientes de ratificación. Los resultados numéricos son objetivos; no se han medido.

## Problema, actores y límites

Core mínimo: identidad, permisos, adaptadores de pago/documentos/comunicación y auditoría. Catálogo, gastos, inventario, CRM y analítica de dominio no son core.

Actores: administrador de empresa, operador de pagos, auditor y responsable de privacidad. Las responsabilidades de aprobación no se transfieren al modelo.

## Escenarios de usuario y pruebas

### H1 (P1) — Administrar acceso por empresa

Valor: control verificable de la operación. Prueba independiente: ejecutar el escenario sin otra vertical, con adaptadores de prueba explícitos.

Dada una membresía activa, cuando se solicita un recurso de otra empresa, entonces se deniega y audita.

### H2 (P1) — Confirmar pagos y documentos sin duplicaciones

Valor: control verificable de la operación. Prueba independiente: ejecutar el escenario sin otra vertical, con adaptadores de prueba explícitos.

Dado un retorno repetido, cuando se procesa, entonces solo una imputación es efectiva y el documento se concilia.

### H3 (P2) — Gobernar acciones y contratos

Valor: control verificable de la operación. Prueba independiente: ejecutar el escenario sin otra vertical, con adaptadores de prueba explícitos.

Dada una acción crítica sin aprobación, cuando el agente intenta ejecutarla, entonces se deniega y registra.

## Requisitos funcionales

| ID | El sistema DEBE | Historia |
|---|---|---|
| FR-001 | Resolver identidad y pertenencia activa a una empresa antes de acceder a cualquier recurso | H1 |
| FR-002 | Autorizar por tenant, rol, recurso y acción con denegación por defecto, incluidos procesos asíncronos | H1 |
| FR-003 | Registrar intentos y estados de pago por empresa, moneda, monto y referencia de negocio, sin duplicar efectos al reintentar | H2 |
| FR-004 | Determinar y emitir el documento tributario aplicable mediante política aprobada por contribuyente; conciliar y evitar doble emisión | H2 |
| FR-005 | Registrar acciones críticas y de agentes con actor, tenant, evidencia, política, aprobación y resultado, con integridad verificable | H3 |
| FR-006 | Separar secretos, almacenamiento y comunicaciones por tenant; minimizar datos y aplicar retención aprobada | H1 |
| FR-007 | Denegar ejecuciones agénticas sin política vigente, identidad, evidencia o aprobación exigida | H3 |
| FR-008 | Recuperar fallos de conectividad mediante estados pendientes, reconciliación y alertas sin declarar éxito ficticio | H2 |
| FR-009 | Versionar contratos y registrar compatibilidad de productores y consumidores antes de cambios | H3 |

## Criterios de éxito

| ID | Objetivo propuesto |
|---|---|
| SC-001 | Cero accesos entre tenants en la batería adversarial aprobada |
| SC-002 | Un único efecto financiero ante diez repeticiones del mismo resultado |
| SC-003 | Toda acción crítica tiene actor, tenant, evidencia y resultado auditables |

## Supuestos y decisiones pendientes

Q-CORE-01: empresas, roles y autorización entre empresas; Q-CORE-02: tratamiento fiscal y proveedor DTE por contribuyente; Q-CORE-03: responsables de datos, retención, recuperación, presupuesto y autonomía.

## Reglas normativas y de aceptación añadidas

- NFR-001: toda lectura, escritura, trabajo en cola y evidencia queda limitada por empresa y permiso; probar denegación entre empresas y roles.
- NFR-002: ningún agente ejecuta una acción financiera, tributaria o contractual sin control determinista y autorización vigente; escritura MCP deshabilitada inicialmente.
- NFR-003: reintentos conservan un solo efecto; estados desconocidos no se muestran como éxitos.
- NFR-004: retención, restauración y objetivos de recuperación requieren aprobación en Q-CORE-03; ninguna cifra de disponibilidad se asume acordada.
- NFR-005: medir latencia desde recepción hasta resultado confirmado, incluyendo errores, reintentos y desconexión. No declarar cumplimiento en muestras vacías.

Q-CORE-01: empresas, roles y autorización entre empresas; Q-CORE-02: tratamiento fiscal y proveedor DTE por contribuyente; Q-CORE-03: responsables de datos, retención, recuperación, presupuesto y autonomía.

Los escenarios tributarios y SC de emisión en 30/60 segundos se conservan como aspiración de la fuente, sujetos a aplicabilidad fiscal y disponibilidad externa. No constituyen garantía del SII. El aislamiento local no garantiza por sí solo cero sobreventa entre OTA independientes.

Ver `acceptance.md` para pruebas por requisito; `../../docs/auditorias/trazabilidad.md` para origen y equivalencias. La investigación transversal está en `../../docs/investigacion/estado-del-arte.md`.
