# F07 - Aseo, inspección y lavanderia
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Asignar trabajo y registrar textiles/insumos sin duplicar costos ni perder piezas.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A01/A05.
Dependencias de orden propuestas: F05;F06.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| OPS-001 | Tareas por salida y permanencia | P0 | ACC-OPS-001 |
| OPS-002 | Asignación y ejecución móvil | P0 | ACC-OPS-002 |
| OPS-003 | Inspección y retrabajo | P0 | ACC-OPS-003 |
| OPS-004 | Consumos por tarea | P0 | ACC-OPS-004 |
| OPS-005 | Areas comunes | P0 | ACC-OPS-005 |
| LIN-001 | Catálogo textil y estados | P0 | ACC-LIN-001 |
| LIN-002 | Lote enviado y recepción | P0 | ACC-LIN-002 |
| LIN-003 | Vinculo habitación y estadía | P0 | ACC-LIN-003 |
| LIN-004 | Costeo de lote | P1 | ACC-LIN-004 |

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
