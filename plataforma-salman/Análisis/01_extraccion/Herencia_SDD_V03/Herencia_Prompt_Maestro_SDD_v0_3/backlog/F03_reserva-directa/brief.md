# F03 - Reserva directa desde enlace social
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Convertir una visita en reserva mediante el motor central; parametrizar anticipo y enlazar el pago real en F04.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A01/A04/A06.
Dependencias de orden propuestas: F02.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| RES-001 | Motor de reserva directa móvil | P0 | ACC-RES-001 |
| RES-002 | Origen y campania | P0 | ACC-RES-002 |
| RES-003 | Cotización y retención temporal | P0 | ACC-RES-003 |
| RES-004 | Último cupo concurrente | P0 | ACC-RES-004 |
| RES-007 | Reservas de varias habitaciones | P0 | ACC-RES-007 |
| RES-008 | Empresa pagadora y convenio | P0 | ACC-RES-008 |
| RES-009 | Modificaciones parciales | P0 | ACC-RES-009 |
| RES-010 | Cancelaciones y no-show | P0 | ACC-RES-010 |
| RES-011 | Grupos y reparto de cargos | P1 | ACC-RES-011 |
| INT-005 | Notificaciones al huésped | P0 | ACC-INT-005 |
| SOC-002 | Enlaces de redes y páginas de campaña | P0 | ACC-SOC-002 |
| SOC-003 | Reserva en navegador interno móvil | P0 | ACC-SOC-003 |
| SOC-016 | Cotización compartida y enlace seguro | P0 | ACC-SOC-016 |
| UX-001 | Accesibilidad verificable | P0 | ACC-UX-001 |
| UX-002 | Idiomas, formatos y estados de interfaz | P1 | ACC-UX-002 |

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
