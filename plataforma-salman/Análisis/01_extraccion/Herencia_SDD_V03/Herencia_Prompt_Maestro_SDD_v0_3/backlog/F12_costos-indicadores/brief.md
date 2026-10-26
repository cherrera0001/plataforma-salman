# F12 - Costos, presupuestos e indicadores
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Mostrar resultados sin duplicados, separar datos medidos/estimados y explicar cada fórmula.

## Contexto y alcance
Entrega candidata: E1. Responsable propuesto: A02/A11.
Dependencias de orden propuestas: F07;F08;F09;F10;F11.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| FIN-007 | Costo directo de estadía | P0 | ACC-FIN-007 |
| FIN-008 | Distribución de costos comunes | P1 | ACC-FIN-008 |
| KPI-001 | Ocupación y calidad de dato | P0 | ACC-KPI-001 |
| KPI-002 | ADR, RevPAR y margen | P0 | ACC-KPI-002 |
| KPI-003 | Operación diaria accionable | P0 | ACC-KPI-003 |
| SOC-012 | Medición de conversión sin duplicados | P1 | ACC-SOC-012 |
| SOC-018 | Costo comercial y rentabilidad de canal | P1 | ACC-SOC-018 |
| REV-002 | Pronósticos y recomendaciones evaluables | P2 | ACC-REV-002 |
| FIN-010 | Presupuesto operativo, inversión y caja | P1 | ACC-FIN-010 |

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
