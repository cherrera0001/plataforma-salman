# F11 - Conciliación y auxiliares financieros
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Relacionar reservas, cargos, documentos, cobros, liquidaciones y bancos con diferencias visibles.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A02/A05.
Dependencias de orden propuestas: F04.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| FIN-001 | Ingreso devengado versus cobro | P0 | ACC-FIN-001 |
| FIN-002 | Cuentas por cobrar y antiguedad | P0 | ACC-FIN-002 |
| FIN-003 | Importacion bancaria con vista previa | P0 | ACC-FIN-003 |
| FIN-004 | Conciliación muchos-a-muchos | P0 | ACC-FIN-004 |
| FIN-005 | Liquidaciones y comisiones de canales | P0 | ACC-FIN-005 |
| FIN-006 | Bandeja de diferencias | P0 | ACC-FIN-006 |
| FIN-009 | Operación entre unidades y sociedades | P0 | ACC-FIN-009 |
| FIN-011 | Frontera e intercambio contable | P0 | ACC-FIN-011 |

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
