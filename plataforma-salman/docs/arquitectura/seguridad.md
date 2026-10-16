# Seguridad, privacidad y gobernanza agéntica

Estado: controles propuestos, sin prueba de producto. Modelo de amenazas considera web, QR, WhatsApp, OCR, audio, adjuntos, sistemas externos, MCP, servicios internos, colas, datos y operador humano. Toda entrada externa puede contener instrucciones maliciosas; no puede alterar políticas, identidad ni permisos. Revisión de Ley 19.628 y transición 21.719 en E-06; el rol responsable/encargado, finalidad, retención, transferencias y acceso de proveedores LLM requieren Q-CORE-03.

## Controles compartidos verificables

- Identidad humana autenticada y membresía por tenant; agentes con identidad de servicio limitada y contexto de delegación verificable. No obtener empresa/rol del texto del mensaje ni equiparar número WhatsApp a aprobación suficiente.
- Autorización por recurso en todos los caminos: API, consulta semántica, adjuntos, caché, colas, informes y restauraciones. Apoyarse en filtros explícitos y, si se selecciona base compatible, defensa adicional; no depender solo de prompts.
- Herramientas permitidas por lista explícita, inicialmente solo lectura sobre campos mínimos. Borradores no producen compromisos externos. Escritura MCP deshabilitada por defecto; cambios requieren permiso de servicio, política, revisión y evidencia.
- Aprobación crítica ligada a tenant, acción, monto/moneda, versión, destinatario y huella, con autenticación reforzada según riesgo, caducidad y uso único. Un agente no puede aprobar su propuesta. Sin datos o conexión, quedar pendiente y escalar.
- Claves y certificados fuera del modelo, cifrado y rotación según proveedor, cuentas distintas por ambiente/empresa. No almacenar PAN/CVV ni documentos completos en logs; usar pasarela alojada para tarjetas y revisar alcance PCI con proveedor antes de producción.
- Registro con actor, tenant, herramienta/versión, regla, parámetros minimizados, hash/referencia de evidencia, aprobación y resultado. Integridad verificable, acceso restringido y retención legal; no grabar secretos ni prometer ledger eternamente inmutable.
- Recuperación por reconciliación con fuente de verdad, reintentos limitados, alarma y revisión de operaciones desconocidas. Pago, devolución y documento tributario requieren compensaciones auditadas; no borrar historia para simular reversión.

## Matriz de agentes

Esta tabla define políticas separadas; no obliga a desplegar siete procesos ni siete modelos. Todos los límites monetarios autónomos son **0 CLP para compromiso de fondos** hasta política aprobada. Preparar una propuesta con costo no permite enviarla ni comprar.

| Agente / objetivo | Herramientas candidatas y datos mínimos | Permitido inicialmente | Prohibido y aprobación humana | Riesgo específico y recuperación | Pruebas y métricas |
|---|---|---|---|---|---|
| CAF reposición: sugerir insumos | Leer stock/recetas/ventas agregadas; crear borrador interno | Calcular propuesta con evidencia de demanda | Prohibido emitir compra, negociar precio, acceder a tarjetas; humano aprueba toda compra y sus cambios | Factura/CSV inyecta instrucciones o costo falso; validar datos, caducar propuesta 48 h según fuente; conservar versiones | Inyectar orden de comprar en factura; impedir ejecución y medir error de cantidades, cobertura de stock, costo/latencia e intervención |
| CAF anomalías/OCR: alertar y extraer | Leer anulaciones/mermas limitadas; OCR de factura aislado | Extraer líneas pendientes y alertar sin sancionar | Prohibido anular ventas, acusar empleados o aprobar gastos; humano valida gasto y acción | Documento contiene secretos o instrucción de exfiltrar; escanear, restringir salida, descartar extracción y revisar | Factura alterada y usuario de otra sucursal; precisión/recall por campo y alerta, falsos positivos y costo por factura |
| HOT concierge: atender estadía | Leer disponibilidad segura, políticas y reserva de huésped autenticado; borrador de cambio | Informar tarifa comprobada y proponer upsell/link mediante flujo controlado | Prohibido cobrar/cancelar/cambiar tarifa; toda mutación de reserva requiere aprobación inicial, hasta ratificar autonomía | Suplantación y tarifas inventadas; revalidar inventario, aprobación y versión; reversión según política hotelera, nunca prometer devolución | Solicitud ajena y prompt para ignorar penalidad; éxito correcto, reserva errónea, costo/conversación, p95 y tasa humana |
| HOT distribución MCP: exponer oferta | Lectura de proyección pública mínima de disponibilidad/tarifa | Informar oferta sin huéspedes ni IDs internos | Prohibido reservar, alterar cupos o exponer cuentas; humano autoriza publicación y campos | Enumeración/extracción y oferta obsoleta; cuota de consulta, minimizar datos, invalidar proyección y suspender si está vencida | Consultas de tenant ajeno y herramienta oculta; frescura, latencia, costo y fugas detectadas |
| INM calificación: preparar visita | Leer oferta pública y lead autorizado; borrador de calificación/agenda | Preguntar datos mínimos y proponer horario | Prohibido scoring discriminatorio, promesa, precio no vigente, reserva o envío contractual; ejecutivo valida cotización y legal aprueba promesa | Mensaje manipula precio o mezcla dos personas; no fusión ciega, revalidar precio y separar borradores | Lead suplantado e instrucción de descuento; exactitud por campo, agenda correcta, sesgo revisado, costo/lead y escalamiento |
| INM cobranza: asistir seguimiento | Leer cuotas de cliente autenticado, estado de pago y política; borrador recordatorio | Preparar recordatorio con monto comprobado | Prohibido ejecutar cargos, conciliar por texto, condonar, amenazar o divulgar deuda; humano aprueba envío inicial, ajustes y devolución | Número equivocado, link adulterado o pago falso; detener envío y conciliar con proveedor, revocar link según capacidad | Imagen de transferencia falsa, deuda ajena; precisión de monto/destino, costo por gestión, incidentes y revisión humana |
| INM postventa: clasificar provisionalmente | Leer solicitud/evidencias autorizadas y catálogo de política; borrador asignación | Clasificar y sugerir responsable/plazo no vinculante | Prohibido rechazar garantía, cerrar caso o prometer cobertura; responsable decide y comunica | Foto con instrucciones y caso urgente mal clasificado; escalar urgencia a persona y conservar evidencia | Fallo grave disfrazado e instrucción para rechazo; recall de urgentes, precisión, p95 y tasa humana |
| OBR asistente: estructurar avance y compras | Leer presupuesto/partidas permitidos; transcripción aislada; borradores | Estructurar reporte y propuesta sin ejecución | Prohibido certificar seguridad, avance, recepción, comprar o alterar presupuesto; jefe/inspector/admin aprueban según función | Foto/voz falsa, retroceso y ubicación sensible; preservar originales, bloquear consolidación y corregir mediante nueva versión | Orden de compra inyectada y evidencia contradictoria; exactitud por partida, error de avance, costo/reporte, latencia y revisión |

La lectura de datos personales también exige permiso y finalidad. El contexto de cada agente solo incluye la información mínima; ninguna herramienta de consulta permite SQL libre, URLs arbitrarias o acceso a archivos/secretos. Los nombres son capacidades conceptuales, no herramientas MCP ya instaladas.

## Matriz de riesgos

| Riesgo | Impacto / severidad | Control y evidencia de prueba futura | Responsable propuesto | Estado |
|---|---|---|---|---|
| R-01 Escape entre empresas | Exposición financiera/identidad, crítica | Prueba de lectura/escritura/búsqueda/adjunto/worker de A contra B; denegación y auditoría | Seguridad | Diseño propuesto |
| R-02 Duplicación financiera/tributaria | Cobro o documento duplicado, crítica | Repetir/desordenar retornos, caída entre efectos, reconciliación y una única imputación | Finanzas + backend | Bloquea política fiscal |
| R-03 Prompt injection | Compra, fuga o cambio no autorizado, crítica | Texto/voz/OCR/MCP con instrucciones de escalamiento; herramientas deniegan fuera de política | Seguridad agéntica | Suite por diseñar con datos |
| R-04 Suplantación aprobador | Contrato o gasto indebido, crítica | Reusar aprobación, cambiar monto/destino o empresa; exigir nueva autorización | Seguridad + negocio | Identidades pendientes |
| R-05 Sobreventa/reserva doble | Pérdida económica, alta | Carreras local/OTA, expiración y desconexión; no confirmar inventario incierto | Hotel/comercial | Bloquea integraciones |
| R-06 Datos LLM/logs/adjuntos | Incidente de privacidad, alta | Canary de datos entre usuarios, revisión de minimización, salida y retención | Privacidad | Bases legales pendientes |
| R-07 Pérdida de estado offline | Venta perdida o duplicada, alta | Desconexión, reinicio, cola y reconciliación con caja existente | Cafetería | Procedimiento pendiente |
| R-08 Restauración o secretos | Pérdida de operación, alta | Restaurar copia aislada, rotar credencial, comprobar tenant y acceso | Operación | RPO/RTO pendientes |
| R-09 Error agéntico o sesgo | Garantía mal denegada, lead discriminado, alta | Casos estratificados, revisión humana ciega y análisis de errores | Negocio + evaluador | Línea base pendiente |
| R-10 Evidencia de obra falsa | Decisión técnica/seguridad indebida, crítica | Evidencia contradictoria, preservar original y exigir firma humana de inspección | Jefatura de obra | Alcance pendiente |

## Evaluación y gate de autonomía

Por agente y versión registrar dataset, procedencia, autorización, partición de prueba reservada, políticas/herramientas y evaluación humana. Medir exactitud de resolución correcta, costo inferencia/herramientas/canal, latencia p50/p95, errores, intervención y acciones denegadas. Casos críticos exigen cero acciones fuera de política en la suite acordada; no equivale a probabilidad cero en producción. Aprobar tamaño de muestra y umbrales de precisión/costo por negocio; si faltan, no habilitar escritura. Comparar contra proceso manual con igual población y ventana, registrar fallos y reintentos, y detener piloto ante incidente crítico. Ver economia.md.

## Riesgos precisados por investigación adicional

- R-11: cancelación confundida con devolución o cargo con cobro/entrega. Control propuesto: estados separados y aprobación por efecto, pruebas RF-HOT-01/02.
- R-12: acuse de canal antes de recepción durable, pérdida tras acuse o deduplicación por ID reserva que descarta cambios. Control: correspondencia de cuenta, recepción/aplicación separadas y recuperación RF-HOT-03; no se presupone firma webhook disponible, debe verificarse el mecanismo real del proveedor.
- R-13: guardar contacto produce envío implícito. Control: perfil por operación/flag y destinatario, denegar efectos no autorizados incluso si una herramienta se declara readOnly; RF-CORE-01.
- R-14: editar Persona modifica vínculos o una sesión vieja expone la unidad tras reasignación. Control: Persona/VínculoUnidad separados, permiso corriente revalidado y política para documentos históricos; RF-INM-03.
- R-15: porcentaje acumulado sumado a otro, recepción rechazada tratada como stock o compromiso/devengo/pago descontados varias veces. Control: unidades, estados, denominador y regla aprobada, RF-OBR-01/02/03.

Responsables propuestos: negocio/finanzas para R-11; integración/seguridad para R-12/13; privacidad/comercial para R-14; control obra/bodega/contabilidad para R-15. Todos en diseño, sin pruebas de producto ejecutadas. La matriz y los perfiles de continuación identifican intervención, evidencia y recuperación por capacidad.
