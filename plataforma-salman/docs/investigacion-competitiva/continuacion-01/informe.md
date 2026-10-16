# Continuación: hotel, inmobiliaria, constructora y core

**Resultado documental:** 26 fuentes adicionales, 13 refinamientos de recorridos dentro de ocho historias existentes, once FR nuevos y 39 AC adicionales propagados a las cuatro features pertinentes. Catálogo activo: **77 FR, 31 SC y 65 AC competitivos en las 13 historias heredadas**. Las dos candidatas previas y dos nuevas de obra siguen fuera de specs/FR activos. Sin código de producto ni cambios en los artefactos de cafetería durante esta continuación.

## Resultado por vertical

| Dominio | Diferencias concretas introducidas | Evidencia / revisión |
|---|---|---|
| Hotel | Cambiar/cancelar con tarifa/cupo/consentimiento versionados; separar devolución; extras por regla y cumplimiento; recibir/acusar/aplicar eventos como estados distintos; concierge no ejecuta compromiso por conversar | H11–H18 y H06–09; [revisión profunda](../hotel/revision-profunda.md) y [cobertura](../hotel/cobertura.md) |
| Inmobiliaria | Agenda estática vs calendario y cambio incierto; firma por versión/participante; Persona separada de VínculoUnidad con revocación corriente; postventa desde visita a aceptación/reapertura; efecto lateral de envío controlado | I11–I19; [revisión profunda](../inmobiliaria/revision-profunda.md) y [cobertura](../inmobiliaria/cobertura.md) |
| Constructora | Partes múltiples por día, incrementos/acumulados y extracción; recepción aceptada/rechazada/devuelta por entrega; compromiso/devengo/pago sin doble cómputo; solución y respuesta oficial separadas del cierre | O10–O18; [revisión profunda](../constructora/revision-profunda.md) y [cobertura](../constructora/cobertura.md) |
| Core | Perfil por efecto/flag/destinatario; guardar datos no permite enviar mensajes ni comprometer fondos; recepción no equivale a resultado final | I11/I17/H13/H15; FR-012 y contratos/aceptación 000 |

Los nueve artefactos de cada una de esas cuatro features se actualizaron. Se conservaron todos los FR/SC/H y el contenido anterior mediante línea base de continuación (50 archivos). [Matriz detallada](matriz-detallada.md) y [trazabilidad](trazabilidad.md) relaciona fuente → refinamiento → problema → historia → FR → AC → artefactos. [Cambios incrementales](cambios.patch) son un Git diff real contra esa línea base, separado del diff acumulado de la investigación anterior.

## Calidad y alcance real de la evidencia

42 fichas anteriores más 26 nuevas = **68 evidencias documentales**. Se profundizaron manuales/APIs y oferta primaria relevante a las tres verticales; no se afirma profundidad equivalente de las 33 candidatas. Propeler es oferta adicional de PlanOK localizada en sus páginas oficiales de Chile, no una plataforma homónima. Existencia de oferta IA local retira la hipótesis de ausencia universal, pero no demuestra desempeño o autonomía.

Tokko API REQUEST contiene placeholder: no es contrato de leads validado aunque abra. I18/I19 y O15 conservan limitación de contenido indexado/acceso incompleto. Se verificaron URLs efectivas y tipo/versión de producto; no se atribuye Channels Plus a un conector PMS ni BIM360 antiguo a Build. Manual de agenda estática, voz IA con conexión y consulta offline son capacidades distintas. Las matrices de cobertura identifican las áreas sin datos suficientes.

## Ejemplos de aceptación que reducen ambigüedad

- Reserva cancelada y devolución aún no autorizada: no mostrar dinero devuelto. Tarifa modificada exige nueva aceptación; timeout no duplica cambio.
- Acuse tras recepción durable pero caída antes de aplicar: recuperar del registro. No deduplicar todas las actualizaciones de una reserva por su único ID.
- Agenda sin calendario: horario aceptado sigue por confirmar según política. Dos firmas requeridas y una recibida no completan promesa.
- Cambiar vínculo del portal de U1 no cambia U2 ni otorga acceso por sesión antigua; guardar teléfono no envía documentos implícitamente.
- Reportes acumulados 40 % y 45 % no producen 85 %. Dos turnos del mismo día no son duplicados por coincidir fecha.
- De diez unidades pedidas, seis entregadas con cinco aceptadas y una rechazada a reponer dejan cinco disponibles y cinco pendientes según política del ejemplo.
- Presupuesto 100 y compromiso total 50 que incluye devengo 20/pago10 dejan disponible50, no20. No se mezclan unidades monetarias; caso ilustrativo, sin resultado financiero real.

## Arquitectura, riesgos y prioridades

ADR-006 mantiene core mínimo y estados de cada dominio; no elige stack, colas, proveedor o endpoints. Sin nuevas dependencias obligatorias ni ciclos. Constitución sin modificaciones; ampliación previa sigue sin ratificación. R-11–15 agregan riesgos de efectos implícitos, acuse/pérdida, vínculo de portal y cantidades/costos. [Perfiles agénticos](perfiles-agentes.md) concretan objetivo, herramientas candidatas, contexto, límites, aprobación, auditoría, recuperación y evaluación. [Medición por flujo](medicion-por-flujo.md) prepara fórmulas sin inventar resultados.

Priorización OP-09–13 mantiene pesos, valores de juicio provisional e intervalos por frecuencia/impacto comercial desconocidos. Subcontratos (US-OBR-006) y consultas técnicas (US-OBR-007) se describen como DRAFT fuera de alcance activo, sujetos a Q-OBR-04. No se copian suites enterprise por cantidad de funciones.

## Validación y limitaciones

Ejecutar desde plataforma-salman `python3 scripts/validar_documentacion.py`, `python3 scripts/validar_investigacion.py` y `python3 scripts/validar_continuacion.py`. Sus JSON registran exactamente cada comprobación local. Se verifican integridad de fuentes/baselines, IDs conservados, criterios/evidencias, enlaces, no modificación de cafetería/constitución, catálogo, diff y ausencia de código funcional. No es prueba de producto ni comando oficial de Spec Kit.

REA reintentado con token en subproceso: sin conexión a api.github.com. Ninguna herramienta REA ejecutada, sin clon completo ni capturas dinámicas. No hubo cambios globales ni exposición de credenciales. Spec Kit ausente; no se simula analyze ni aprobación del cliente.

Las cinco features siguen **BLOCKED para implementación** por Q comerciales/fiscales/PMS/canales/agenda/firma/vínculo/presupuesto y validación operativa; la investigación documental de las otras verticales sí avanzó y produjo diferencias verificables. Se detiene este ciclo tras corregir inconsistencias demostrables; las comprobaciones dinámicas requieren conectividad, herramientas y objetivo autorizado, y las reglas finales requieren responsables del cliente.
