# F04 - Pagos, caja y documentos tributarios
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Verificar y aplicar cobros una vez, distinguir anticipo/garantía, cerrar caja y controlar documentos fiscales.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A02/A05.
Dependencias de orden propuestas: F03.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| PAY-001 | Anticipos y garantías | P0 | ACC-PAY-001 |
| PAY-002 | Pagos parciales y multiples medios | P0 | ACC-PAY-002 |
| PAY-003 | Confirmación pasarela en servidor | P0 | ACC-PAY-003 |
| PAY-004 | Idempotencia de pagos | P0 | ACC-PAY-004 |
| PAY-005 | Devoluciones y contracargos | P0 | ACC-PAY-005 |
| PAY-006 | Arqueo y entrega de turno | P0 | ACC-PAY-006 |
| PAY-007 | Retiros y depositos | P0 | ACC-PAY-007 |
| PAY-008 | Cierre y reapertura | P0 | ACC-PAY-008 |
| TAX-001 | Emisor y proveedor tributario | P0 | ACC-TAX-001 |
| TAX-002 | Reglas de impuestos aprobadas | P0 | ACC-TAX-002 |
| TAX-003 | Notas y correcciones | P0 | ACC-TAX-003 |
| SEC-008 | Enlaces de pago y acceso acotados | P0 | ACC-SEC-008 |

## Trabajo del agente de especificación
Desarrollar historias independientes, reglas, escenarios, campos, permisos, efectos financieros/inventario, errores, privacidad y criterios observables. Conservar el ID maestro y crear FR locales. Adjuntar matrices de relación y referencia a versión/hash del maestro.

Para cada requisito leer la fila completa de `matrices/01_requisitos_base.csv` y las decisiones relacionadas. No tratar esta tabla como la especificación final. Añadir nuevos requisitos detectados sin renumerar ni perder los originales.

## Paquete objetivo
Generar spec.md, plan.md, tasks.md, research.md, data-model.md, contracts/, quickstart.md, checklists/, acceptance.md y traceability.csv conforme al grado de madurez y permisos del modo. Las tareas ejecutables solo se aprueban cuando la arquitectura y dependencias correspondientes se hayan resuelto. En fase futura, declarar plan PRELIMINAR, no simular listo para código.

## Pruebas y condiciones de salida
Las pruebas son OBLIGATORIAS. Desarrollar positivos, negativos, fallas, permisos y concurrencia según riesgo. Relacionar escenarios de matrices/05_escenarios_base.csv y nuevos casos propios. La aceptación exige evidencia real después de construir; ahora solo se especifica.

## Dependencias que requieren refinamiento
Número de relaciones heredadas no representadas como predecesor en el orden candidato: 0. Revisar `matrices/07_acoplamientos_a_resolver.csv`. Clasificar antes de planificar: dato, contrato, implementación, prueba integrada o gate de producción. No borrar para aparentar un grafo limpio.

## Exclusiones y límites
No gastos, credenciales, mensajes reales, datos de producción ni pruebas declaradas como ejecutadas. No presuponer que las funciones opcionales estan habilitadas. No reemplazar un servicio externo autorizado por scraping. No autoaprobar la ficha ni reducir criterios para facilitar implementación.
