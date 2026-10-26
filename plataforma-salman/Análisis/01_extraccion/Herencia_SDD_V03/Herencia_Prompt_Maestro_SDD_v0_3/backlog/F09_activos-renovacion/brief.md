# F09 - Activos, mantenimiento y renovación
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Distinguir inventario, propiedad, desperfectos, compras, instalación y bloqueos de habitaciones.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A12/A01.
Dependencias de orden propuestas: F02;F06.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| MNT-001 | Activos y planes preventivos | P0 | ACC-MNT-001 |
| MNT-002 | Orden correctiva y liberación | P0 | ACC-MNT-002 |
| CAP-002 | Ficha de activo y condición | P0 | ACC-CAP-002 |
| CAP-003 | Plan de renovaciones y presupuesto | P1 | ACC-CAP-003 |
| CAP-004 | Adquisicion e instalación de equipo | P1 | ACC-CAP-004 |
| CAP-005 | Baja, reparacion y trazabilidad contable | P1 | ACC-CAP-005 |
| CAP-006 | Renovación y disponibilidad hotelera | P1 | ACC-CAP-006 |

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
