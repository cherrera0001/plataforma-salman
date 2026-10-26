# F02 - Habitaciones, tarifas e inventario vendible
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Consultar disponibilidad y precio con configuración de camas, fechas, bloqueos y políticas vigentes.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A01/A05.
Dependencias de orden propuestas: F01.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| HOT-001 | Catastro de 17 habitaciones | P0 | ACC-HOT-001 |
| HOT-002 | Capacidad por personas y configuración | P0 | ACC-HOT-002 |
| HOT-003 | Inventario por tipo y asignación física | P0 | ACC-HOT-003 |
| HOT-004 | Bloqueos de mantenimiento fechados | P0 | ACC-HOT-004 |
| HOT-005 | Estados comerciales y físicos distintos | P0 | ACC-HOT-005 |
| RES-005 | Planes y precios versionados | P0 | ACC-RES-005 |
| RES-006 | Descuento separado de comisión | P0 | ACC-RES-006 |
| REV-001 | Restricciones de venta y gestión tarifaria | P1 | ACC-REV-001 |

## Trabajo del agente de especificación
Desarrollar historias independientes, reglas, escenarios, campos, permisos, efectos financieros/inventario, errores, privacidad y criterios observables. Conservar el ID maestro y crear FR locales. Adjuntar matrices de relación y referencia a versión/hash del maestro.

Para cada requisito leer la fila completa de `matrices/01_requisitos_base.csv` y las decisiones relacionadas. No tratar esta tabla como la especificación final. Añadir nuevos requisitos detectados sin renumerar ni perder los originales.

## Paquete objetivo
Generar spec.md, plan.md, tasks.md, research.md, data-model.md, contracts/, quickstart.md, checklists/, acceptance.md y traceability.csv conforme al grado de madurez y permisos del modo. Las tareas ejecutables solo se aprueban cuando la arquitectura y dependencias correspondientes se hayan resuelto. En fase futura, declarar plan PRELIMINAR, no simular listo para código.

## Pruebas y condiciones de salida
Las pruebas son OBLIGATORIAS. Desarrollar positivos, negativos, fallas, permisos y concurrencia según riesgo. Relacionar escenarios de matrices/05_escenarios_base.csv y nuevos casos propios. La aceptación exige evidencia real después de construir; ahora solo se especifica.

## Dependencias que requieren refinamiento
Número de relaciones heredadas no representadas como predecesor en el orden candidato: 1. Revisar `matrices/07_acoplamientos_a_resolver.csv`. Clasificar antes de planificar: dato, contrato, implementación, prueba integrada o gate de producción. No borrar para aparentar un grafo limpio.

## Exclusiones y límites
No gastos, credenciales, mensajes reales, datos de producción ni pruebas declaradas como ejecutadas. No presuponer que las funciones opcionales estan habilitadas. No reemplazar un servicio externo autorizado por scraping. No autoaprobar la ficha ni reducir criterios para facilitar implementación.
