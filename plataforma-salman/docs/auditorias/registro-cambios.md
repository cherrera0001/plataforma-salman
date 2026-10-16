# Registro de modificaciones y ciclo controlado

Fecha 2026-10-16. Todas las ediciones se limitan a plataforma-salman; ninguna fuente se elimina o modifica. No se realiza commit ni inicialización Git: el .git del entorno no es utilizable/protegido. La reversibilidad documental se sustenta en originales byte a byte, manifiesto SHA-256 y diffs reproducibles.

| Ciclo | Analizar y detectar | Corrección concreta | Validación y resultado |
|---|---|---|---|
| 0 Inspección | Cuatro entradas, sin artefactos ni CLI disponible; Git falla | Lectura completa Markdown/DOCX, inventario y copias hash | Cuatro fuentes preservadas, evidencia de versión oficial |
| 1 Auditoría individual | Problemas por 14 dimensiones y afirmaciones por unidad; F-001–020 | Separar core/verticales, trasladar H3 de obra, políticas, gates y aclaraciones | Primera corrida local: 232 comprobaciones, 0 errores; 56 FR y 31 SC |
| 2 Coherencia semántica | Búsqueda de frases heredadas detectó boleta por pago, ledger absoluto y PMS/relocación asumidos aún en escenarios | Corregir escenarios/SC manteniendo IDs; matizar exportación; cambiar ejecución autónoma a gate; reemplazar AT genéricos por resultados de negocio concretos | Segunda corrida final en validacion-local.json; revisar fuentes y diff para cada cambio |

## Cambios por fuente y justificación

INV: extracción íntegra y síntesis auditada; clasificar marketing, cifras, supuestos y contradicción Eleventa, sin inventar bibliografía. CAF: separar constitución única, conservar H1–H3/14 FR/8 SC, corregir fiscalidad y límites core. HOT: conservar H1–H3/15 FR/9 SC, sistema de registro por decidir, disponibilidad segura en desconexión, room service opcional. INM: conservar H1–H2/11 FR/8 SC en 003; trasladar H3/FR-010–012/SC-008 a 004 y ampliar requisitos de obra como propuestas identificadas. Core: nueve FR nuevos trazados al encargo y reglas transversales.

Comparación exacta fuente→spec derivada en cambios-cafeteria.diff, cambios-hotel.diff y cambios-inmobiliaria.diff. Son reestructuraciones documentales amplias; los diffs no implican aprobación comercial. Equivalencias de traslado y nuevos FR en trazabilidad.md.

## Regla de parada aplicada

No hay nuevos defectos estructurales detectados por el control local; permanecen decisiones y verificaciones externas que no puede resolver una iteración de redacción. Se detiene antes de implementación, aprobación comercial o simulación de controles oficiales. El siguiente ciclo depende de respuestas Q, revisión experta y entorno Spec Kit real.

## Investigación competitiva posterior

Se guardó línea base de 51 archivos y se enriquecieron 13 historias, 10 FR nuevos y NFR-006; catálogo actual de 66 FR y 31 SC. Se precisaron URLs efectivas y alcance regional, sin modificar originales ni constitución. Ver docs/investigacion-competitiva/registro-cambios.md, cambios.patch y validacion.json para evidencia y detalle. Ninguna prueba de producto, operación externa o análisis REA fue ejecutado.
