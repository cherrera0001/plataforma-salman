> Informe inicial conservado. La investigación competitiva posterior actualiza el catálogo a 77 FR; estado y validaciones vigentes en docs/investigacion-competitiva/informe-final.md y sus JSON. Los conteos iniciales siguientes describen la entrega anterior.

# Informe de validación y consistencia — 2026-10-16

**Resultado: base documental construida; cinco features BLOCKED para implementación.** No existe producto ni integración ejecutada. La versión oficial consultada de Spec Kit es v1.2.0, pero no está instalada. La compatibilidad operacional solicitada permanece abierta; se alcanzó el punto de parada por decisiones humanas y entorno indicado en el encargo.

## Cobertura comprobada

Cuatro documentos procesados, originales y copias con SHA-256 verificables. El registro de afirmaciones cubre cada línea significativa de los Markdown y cada párrafo/celda de texto extraído del DOCX, con clasificación contextual y evidencia literal; no constituye verificación externa de todos los claims. Cuatro auditorías individuales evalúan 14 dimensiones antes de su consolidación. Veinte hallazgos materiales tienen ubicación, evidencia, impacto, severidad, corrección y estado.

Cinco features con nueve artefactos cada una, 56 FR y 31 SC con namespace y trazabilidad; H3 y FR-010–012/SC-008 de obra se trasladaron sin duplicar alcance comercial. Una sola constitución, cuatro ADR con estado propuesto/pendiente, grafo sin ciclos, diez riesgos y ocho políticas de capacidades agénticas. Fórmulas económicas preparadas sin beneficios inventados.

## Comprobación reproducible

Comando ejecutado: `python3 plataforma-salman/scripts/validar_documentacion.py` desde la carpeta de trabajo; alternativamente desde la raíz del proyecto usar `python3 scripts/validar_documentacion.py`. Código y resultado de cada comprobación en scripts/validar_documentacion.py y validacion-local.json. El número final de comprobaciones es el del JSON, que incluye enlaces agregados al README final. Ver arbol.txt para archivos reales y cambios-*.diff para transformaciones.

Se verifica existencia y contenido no trivial, hash de ocho archivos (cuatro originales y cuatro copias), una constitución, IDs exactos por feature, pruebas propuestas por FR, medición propuesta por SC, origen por FR y enlaces Markdown locales. El grafo interno comprobado es una representación local explícita del propuesto en dependencias.md, no un análisis de código o de conexiones reales. Sin código funcional en core/verticales; solo un script local de auditoría.

## Revisión semántica y límites

Se revisaron manualmente consistencia de fuente/derivado, separación spec/plan, core mínimo, dependencias opcionales, fiscalidad, continuidad, datos y autonomía. La segunda revisión corrigió frases heredadas en escenarios y criterios. Las pruebas de aceptación son propuestas, no pruebas de producto ejecutadas; los contratos carecen deliberadamente de endpoints hasta conocer datos/reglas. Los modelos son conceptuales, no SQL. Las tareas no prometen implementación antes de cerrar gates.

Los umbrales originales de 30/60 segundos de entrega documental se mantienen como objetivos condicionados por confirmar, sin garantía universal. Otros objetivos como cero sobreventa, porcentajes de margen y resolución necesitan definición de muestra, denominador, tolerancia y operación real; figuran como objetivos propuestos. No hay métricas medidas ni ROI calculado.

## Estado por feature

| Feature | Estado | Condiciones de salida |
|---|---|---|
| 000-core | BLOCKED | Q-CORE-01/02/03, Q-GOV-01 y Q-TOOL-01 |
| 001-cafeteria-mesas-pos | BLOCKED | Gates core y Q-CAF-01/02/03 |
| 002-hotel-reservas-concierge | BLOCKED | Gates core y Q-HOT-01/02/03; no exige 001 para H1 |
| 003-inmobiliaria-comercial | BLOCKED | Gates core y Q-INM-01/02/03/04 |
| 004-constructora-obra | BLOCKED | Gates core y Q-OBR-01/02/03, alcance V2 |

## No verificado y seguimiento

No se ejecutaron comandos oficiales de agente ni CLI Spec Kit, pruebas API, certificaciones SII/OTA, sandbox de pagos, revisión jurídica de promesa, pentest ni pruebas de restauración. Las fuentes externas se verificaron con alcance acotado en matriz-evidencia.md; Meta falló y la mayoría de claims de mercado de INV sigue sin verificación independiente. No afirmar preparación READY ni legalidad/viabilidad de integración hasta resolverlo.

Parada: los defectos corregibles documentales detectados fueron tratados o convertidos en controles propuestos con gate explícito. Las contradicciones dependientes de decisión cliente no se declaran resueltas; están en hallazgos y aclaraciones. Reanudar con las respuestas y evidencia; primero ratificar decisiones y completar contratos/pruebas, después revisar readiness por feature.
