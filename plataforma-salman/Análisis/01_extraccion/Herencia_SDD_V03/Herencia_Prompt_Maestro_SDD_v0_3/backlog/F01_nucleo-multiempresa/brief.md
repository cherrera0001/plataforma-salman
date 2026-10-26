# F01 - Sociedades, identidad, permisos y auditoría
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Operar con sociedad y unidad explícitas, permisos comprobables, documentos y cambios trazables.

## Contexto y alcance
Entrega candidata: E0. Responsable propuesto: A03/A07.
Dependencias de orden propuestas: F00.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| CORE-001 | Sociedades y unidades separadas | P0 | ACC-CORE-001 |
| CORE-002 | Participaciones con vigencia | P1 | ACC-CORE-002 |
| CORE-003 | Permisos por acción y alcance | P0 | ACC-CORE-003 |
| CORE-004 | Historial y reversos | P0 | ACC-CORE-004 |
| CORE-005 | Fechas y monedas exactas | P0 | ACC-CORE-005 |
| CORE-006 | Documentos y proveedores comunes | P0 | ACC-CORE-006 |
| SEC-001 | Autenticación reforzada | P0 | ACC-SEC-001 |
| SEC-002 | Privacidad y retención | P0 | ACC-SEC-002 |
| SEC-003 | Secretos y datos sensibles | P0 | ACC-SEC-003 |
| SEC-006 | Instrucciones externas no confiables | P0 | ACC-SEC-006 |

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
