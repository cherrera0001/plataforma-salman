# F21 - Verificación transversal y continuidad
Estado: SEMILLA_NO_ESPECIFICACION_APROBADA. Versión 0.3.

## Resultado empresarial a especificar
Aplicar controles desde el inicio y ensayar recuperación e integración de cada capacidad activada; no esperar al final para probar.

## Contexto y alcance
Entrega candidata: TRANSVERSAL. Responsable propuesto: A08/A07/A09.
Dependencias de orden propuestas: F00.
El detalle definitivo surge del maestro, fuentes y decisiones. No crear código desde esta ficha sin especificación, plan, pruebas y autorización. Las restricciones transversales siguen aplicando aun cuando su requisito primario este en otro paquete.

## Requisitos primarios heredados
| ID maestro | Requisito | Criticidad | Prueba base |
|---|---|---|---|
| SEC-004 | Respaldos y restauración | P0 | ACC-SEC-004 |
| SEC-005 | Contingencia sin conexión | P0 | ACC-SEC-005 |
| AI-006 | Software opera sin IA | P0 | ACC-AI-006 |
| SEC-009 | Verificación independiente de seguridad | P0 | ACC-SEC-009 |
| SEC-010 | Cadena de suministro y cambios seguros | P0 | ACC-SEC-010 |
| QA-001 | Prueba comercial de extremo a extremo | P0 | ACC-QA-001 |
| QA-002 | Concurrencia, fraude y abuso | P0 | ACC-QA-002 |
| QA-003 | Revisión de especificación independiente | P0 | ACC-QA-003 |

## Trabajo del agente de especificación
Desarrollar historias independientes, reglas, escenarios, campos, permisos, efectos financieros/inventario, errores, privacidad y criterios observables. Conservar el ID maestro y crear FR locales. Adjuntar matrices de relación y referencia a versión/hash del maestro.

Para cada requisito leer la fila completa de `matrices/01_requisitos_base.csv` y las decisiones relacionadas. No tratar esta tabla como la especificación final. Añadir nuevos requisitos detectados sin renumerar ni perder los originales.

## Paquete objetivo
Generar spec.md, plan.md, tasks.md, research.md, data-model.md, contracts/, quickstart.md, checklists/, acceptance.md y traceability.csv conforme al grado de madurez y permisos del modo. Las tareas ejecutables solo se aprueban cuando la arquitectura y dependencias correspondientes se hayan resuelto. En fase futura, declarar plan PRELIMINAR, no simular listo para código.

## Pruebas y condiciones de salida
Las pruebas son OBLIGATORIAS. Desarrollar positivos, negativos, fallas, permisos y concurrencia según riesgo. Relacionar escenarios de matrices/05_escenarios_base.csv y nuevos casos propios. La aceptación exige evidencia real después de construir; ahora solo se especifica.

## Dependencias que requieren refinamiento
Número de relaciones heredadas no representadas como predecesor en el orden candidato: 10. Revisar `matrices/07_acoplamientos_a_resolver.csv`. Clasificar antes de planificar: dato, contrato, implementación, prueba integrada o gate de producción. No borrar para aparentar un grafo limpio.

## Exclusiones y límites
No gastos, credenciales, mensajes reales, datos de producción ni pruebas declaradas como ejecutadas. No presuponer que las funciones opcionales estan habilitadas. No reemplazar un servicio externo autorizado por scraping. No autoaprobar la ficha ni reducir criterios para facilitar implementación.
