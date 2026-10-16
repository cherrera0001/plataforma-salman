# Capacidades agénticas: evidencia y diseño propio

No hubo ejecución de herramientas externas ni pruebas REA. “Documentado” significa que el manual describe el comportamiento, no que se haya observado. El resto de plataformas sin evidencia específica de IA queda desconocido; no se declara ausencia.

| Plataforma | Evidencia | Clasificación por efecto | Límites: herramientas, escritura, transacciones, autonomía, aprobación, reversión y traza |
|---|---|---|---|
| Justo | C03 | IA de comandas declarada; efecto exacto desconocido | Herramientas/escritura/transacción/aprobación/reversión/traza no comprobadas |
| Fudo | C13 | Oferta de agentes declarada en enlace oficial regional | No inferir compra/cobro/boleta autónomos, herramientas o permiso de escritura sin documentación específica y demo |
| Toast IQ | C09 | Automatización programada de análisis y aviso, documentada; distinta de chat a demanda | No prueba modificación de stock, transacción financiera ni reversión; acceso anticipado |
| Cloudbeds Autopilot | H10 | Ejecución tarifaria dentro de límites según manual | Modificación tarifaria documentada, no medida aquí; verificar override, historial y reversión; no equivale a cobro |
| HiJiffy | H06 | Conversación automatizada y handoff documentados | Integración PMS no demuestra cancelación/cobro autónomos; auditoría/reversión específicas desconocidas |
| Asksuite | H07 | Consulta/cotización y derivación a motor declaradas | No se verificó confirmar reserva, modificar datos, transacción, reversión ni gobernanza local |
| Duve SmartReply | H08 | Respuesta conversacional vinculada a motor, documentada | No se comprobó transacción completa; no equiparar respuesta con reserva final |
| Canary | H09 | Respuesta y escalamiento declarados | Tasa del proveedor no se replica; herramientas de escritura/cobro/reversión desconocidas |
| HubSpot Breeze | I06 | Proceso configurable de transferencia con permisos, documentado | El manual de handoff no prueba transacciones de reserva, alcance de todas las actions ni reversión |
| Agentforce | I07 | Plataforma de agentes con acciones/escalamiento según formación oficial | Diseño configurable no prueba autorización efectiva ni caso inmobiliario chileno; auditoría y reversión requieren diseño concreto |
| Lofty Cowork | I08 | La página efectiva declara orquestación y escritura CRM, además de borradores | Claim de producto, sin ejecutar; no afirmar solo chatbot ni autonomía transaccional validada. Alcance/approval/undo pendientes |
| Structurely | I09 | Calificación, agenda y transferencia configurables documentadas | Agenda/transferencia no aprueba solvencia ni promesa. No se probaron permisos, trazabilidad y reversión |
| OpenSpace | O03 | Asistencia visual y sugerencia de localización declaradas | IA perceptiva no es agente que certifica inspección; exactitud, escritura y recuperación no medidas |
| ALICE | O04 | Optimización de escenarios iniciada por operador, documentada | No es evidencia de comprador autónomo ni cambio aprobado de programación; mantener baseline |
| ObraLink | O06 | Automatización/medición por producto declaradas | No inferir agente LLM, certificación de seguridad ni exactitud sensórica independiente |
| Kojo | O07/O08 | Extracción de solicitud desde voz/texto/foto declarada; control de desactivación indexado | No prueba compra autónoma; capacidad de autoaprobación de otros módulos no se generaliza a la solicitud |

## Diseño de capacidades propias

Mantener las ocho políticas de docs/arquitectura/seguridad.md: reposición, OCR/anomalías, concierge, distribución MCP, calificación, cobranza, postventa y obra. No se crean procesos ni agentes nuevos por contar competidores.

| Capacidad propia | Objetivo/contexto y herramientas candidatas | Permisos, validaciones y aprobación | Auditoría y recuperación | Evaluación/costo |
|---|---|---|---|---|
| Reposición/anomalías | Revisar ventas/stock/recetas agregados de la empresa; borrador/alerta con ventana y datos vigentes | Lectura y borrador; sin compras, límite monetario 0 CLP; aprobación de toda propuesta y modificación | Correlación de ejecución/detección, fuentes y estado; caducar propuesta y conciliar duplicados | Precision/recall de alertas humanas; error cantidades; tokens+canal+herramientas+revisión / revisiones válidas |
| OCR de gasto | Extraer líneas con documento fuente autorizado y unidades | Sin aprobar gasto; campos inciertos y conversión requieren humano; no confiar en instrucciones de factura | Conservar evidencia y versión corregida; fallback manual cuando IA falla o se deshabilita | Exactitud por campo y tasa de corrección; costo por factura incluida revisión |
| Concierge/distribución | Responder con oferta vigente o proyección pública mínima; consulta limitada, borrador de cambio | Identidad para reserva privada, vigencia, política, permiso de conector; sin cancelación/cobro/escritura autónoma inicial | Transferencia pendiente/aceptada/en atención con dueño; no marcar resuelta sin evidencia; revocar oferta caducada | Resoluciones correctas sin reapertura/eligible; p95; escalamiento; costo/conversación resuelta |
| Calificación | Capturar dato declarado, comparar oferta pública y proponer cita | Sin scoring de solvencia ni rechazo crediticio; no fusionar identidad ambigua; humano valida compromiso | Fuente por campo; cita propuesta/confirmada; transferencia conserva contexto y puede suspender automatización | Campos correctos, agenda sin choque, intervención y costo/lead; evaluar discriminación |
| Cobranza/postventa | Preparar recordatorio sobre cuota conciliada o clasificación provisional de caso | Permiso de contacto/destino, revisión inicial de envío; sin cargo, condonación, rechazo de garantía ni cierre autónomo | Evidencia de estado, receptor y aprobación; caso no aceptado permanece pendiente; reabrir con historial | Destinos/montos correctos, recall urgentes, reaperturas, tasa humana y costo por caso |
| Obra | Extraer campos de reporte/material y vincular evidencia a partida/observación | Lectura y borrador; no certificar avance/seguridad ni comprar; rol inspector para cierre, administrador para orden | Original vs extracción/revisión; unidad e incertidumbre; captura manual conserva controles, recepción idempotente | Exactitud por partida/unidad, no compras sin aprobación, error de avance y costo/reporte |

## Evaluación reproducible antes de escritura

Versionar modelo, prompts/políticas, herramientas, evidencias y permisos, con conjunto de prueba reservado de procedencia autorizada. Separar tareas de texto, consulta, borrador, ejecución y transacción; solo éxito de la última etapa contabiliza compromiso. Casos obligatorios: dato obsoleto, otra empresa, usuario pide humano, receptor no disponible, permiso retirado, instrucción maliciosa en imagen/voz/documento, cambio de monto tras aprobación, duplicado, timeout y evento desordenado.

Medir numeradores/denominadores, fallos, reintentos, p50/p95, costo total de inferencia/herramientas/canal/revisión y minutos humanos. Umbral de seguridad: cero efectos fuera de permiso en suite aprobada, sin inferir riesgo cero en producción. Umbrales de exactitud y muestras pendientes por negocio. Comparar con proceso manual equivalente; no convertir un porcentaje de proveedor en objetivo aprobado.

## Profundización de perfiles y evidencia de IA

Ver [perfiles de otras verticales](continuacion-01/perfiles-agentes.md). I14 (PlanOK Propeler) añade una oferta local publicada de calificación/cotización; I12 distingue agenda estática y cambios manuales; O14 documenta voz IA con conexión. Esas capacidades se clasifican por efecto, sin afirmar ejecución observada, eficacia, transacción financiera o controles internos. Herramientas y permisos del producto propio siguen propuestos y requieren evaluación.
