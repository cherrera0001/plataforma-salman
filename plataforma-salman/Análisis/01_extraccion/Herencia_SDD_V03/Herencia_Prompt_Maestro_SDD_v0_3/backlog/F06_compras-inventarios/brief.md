# F06 - Compras, existencias y precios unitarios
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Comparar compras, recibir cantidades reales, registrar deuda y mantener inventario por ubicacion/lote.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A12/A02.
Dependencias de orden propuestas: F01.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| INV-001 | Catálogo y unidades | P0 | ACC-INV-001 |
| INV-002 | Movimientos y ubicaciones | P0 | ACC-INV-002 |
| INV-003 | Lotes y vencimientos | P0 | ACC-INV-003 |
| INV-004 | Inventario físico y ajustes | P0 | ACC-INV-004 |
| INV-005 | Reposición y alertas | P1 | ACC-INV-005 |
| PUR-001 | Solicitud y aprobación | P0 | ACC-PUR-001 |
| PUR-002 | Recepción parcial | P0 | ACC-PUR-002 |
| PUR-003 | Control orden-recepción-documento | P0 | ACC-PUR-003 |
| PUR-004 | Cuenta por pagar y programación | P0 | ACC-PUR-004 |
| CAP-001 | Precios unitarios comparables | P0 | ACC-CAP-001 |

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
