# Análisis funcional — inmobiliaria

Reconstrucción desde documentación pública; ninguna secuencia fue ejecutada en UI/REA. Cada regla propia se propone para el proyecto; no se atribuye al proveedor. Consulte matriz-evidencias para observación documental y límites.

## US-INM-001 / H1

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | interesado y ejecutivo comercial |
| Objetivo | pasar de un contacto autorizado a una promesa mediante hitos comprobables |
| Evento inicial | ingresa una consulta desde un canal autorizado o el ejecutivo avanza un hito de la oportunidad |
| Precondiciones | canales autorizados y alcance de conector; identidad de contacto revisada; precios, políticas de reserva y promesa aprobados |
| Pasos | Capturar contacto con origen → distinguir persona y consulta → calificar con dato declarado → proponer visita → confirmar agenda → emitir cotización versionada → revalidar unidad → reserva/pago conciliados → revisión legal/firma. |
| Datos | Contacto, consulta/origen, consentimiento/preferencia, declaraciónCalificación, cita/estado, cotización/versión, reserva y evidenciaFirma. |
| Reglas | Presupuesto declarado no es solvencia verificada. Cotización no reserva; cita propuesta no confirmada; reserva pagada no promesa firmada. Renuncia de contacto suspende automatización permitida según política. |
| Validaciones | Presupuesto declarado no es solvencia verificada. Cotización no reserva; cita propuesta no confirmada; reserva pagada no promesa firmada. Renuncia de contacto suspende automatización permitida según política. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Identidad ambigua queda para revisión, no fusión automática. Plan sin webhook usa solo vía autorizada acordada, no scraping. Precio cambió: nueva cotización. Firma fallida no equivale a promesa vigente. |
| Resultado esperado | reservar la unidad correcta y firmar la versión legal aceptada |
| Evidencia documental y límite | I01, I03, I04, I05, I09, I10; manual/producto. No se observaron interacciones cliente-servidor en vivo. |

## US-INM-002 / H2

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | cliente y responsable de postventa/cobranza |
| Objetivo | seguir cuotas y casos con responsable, evidencia y escalamiento |
| Evento inicial | vence una cuota próxima, ingresa una solicitud de postventa o expira su plazo de respuesta |
| Precondiciones | cliente autorizado; cuotas reconciliadas; políticas garantía/plazo; destinatario de transferencia |
| Pasos | Consultar cuota/caso → preparar recordatorio o clasificación provisional → validar destinatario → asignar responsable y plazo según catálogo → registrar atención → resolver con evidencia → validar cierre humano. |
| Datos | Cuota, comunicación autorizada, CasoPostventa, estado, responsable, vencimiento, resolución, evidenciaCierre y reapertura. |
| Reglas | Clasificar no decide cobertura; prometer fecha requiere política. Transferencia no cuenta como resolución. Cobranza no modifica monto ni concilia una imagen de transferencia. |
| Validaciones | Clasificar no decide cobertura; prometer fecha requiere política. Transferencia no cuenta como resolución. Cobranza no modifica monto ni concilia una imagen de transferencia. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Solicitud urgente requiere intervención; receptor ausente queda en cola visible con escalamiento. Caso reabierto conserva historial. Cambio contacto obliga a revalidar destino antes de exponer deuda. |
| Resultado esperado | evitar cobros indebidos y solicitudes perdidas o cerradas sin validación |
| Evidencia documental y límite | I02, I06; manual/producto. No se observaron interacciones cliente-servidor en vivo. |


## Profundización posterior

Ver [revisión funcional profunda](revision-profunda.md): RF-INM-01, RF-INM-02, RF-INM-03, RF-INM-04. Los nuevos criterios se incorporan también a spec/acceptance y no son solo notas de investigación.
