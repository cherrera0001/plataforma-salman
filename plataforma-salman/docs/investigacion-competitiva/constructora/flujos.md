# Análisis funcional — constructora

Reconstrucción desde documentación pública; ninguna secuencia fue ejecutada en UI/REA. Cada regla propia se propone para el proyecto; no se atribuye al proveedor. Consulte matriz-evidencias para observación documental y límites.

## US-OBR-003 / H3

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | jefe de obra y administrador de compras |
| Objetivo | convertir reportes y necesidades en borradores revisables por partida |
| Evento inicial | el jefe envía reporte de avance o necesidad de materiales por texto, voz, foto o entrada manual |
| Precondiciones | presupuesto/programación versionados, partidas/unidades y aprobadores; catálogo proveedor vigente si existe |
| Pasos | Capturar texto/foto/voz → conservar fuente → extraer partida/cantidad/unidad → marcar inciertos → revisar → consolidar reporte aprobado → calcular desvío → preparar solicitud con precio/convenio como evidencia. |
| Datos | Reporte, evidencia/fecha/ubicación sugerida, campoExtraído/confianza, partida/versión, cantidad/unidad, referenciaPrecio y aprobación. |
| Reglas | Extracción no aprobación; imagen no certificación. Compra autorizada se vincula a versión de líneas; cualquier cambio requiere nueva revisión. Umbral relativo/puntos sigue Q-OBR-02. |
| Validaciones | Extracción no aprobación; imagen no certificación. Compra autorizada se vincula a versión de líneas; cualquier cambio requiere nueva revisión. Umbral relativo/puntos sigue Q-OBR-02. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | IA no disponible o deshabilitada: entrada manual equivalente. Unidad/proveedor ambiguo: revisión; convenio vencido no autoriza precio. Retroceso exige rectificación conservada. |
| Resultado esperado | hacer visibles desvíos y solicitudes sin inventar avance ni comprar automáticamente |
| Evidencia documental y límite | O03, O05, O07, O08; manual/producto. No se observaron interacciones cliente-servidor en vivo. |

## US-OBR-004 / H4

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | inspector y encargado de materiales |
| Objetivo | registrar observaciones y recepciones contra evidencia y permisos |
| Evento inicial | un inspector registra ítem fallido, se propone su solución o bodega recibe material contra una orden |
| Precondiciones | plantilla/partidas vigentes, unidades, roles de inspector/solucionador y política de recepción |
| Pasos | Registrar inspección → detectar falla → abrir observación vinculada → asignar responsable/plazo → adjuntar solución → validar cierre; por separado registrar recepción parcial → comparar con compra aprobada → conciliar diferencia. |
| Datos | Inspección/ítem, Observación, vínculo/origen, asignado, evidenciaSolución, revisor, recepción/línea, orden y discrepancia. |
| Reglas | Estado resuelto propuesto no equivale a cerrado aceptado. Recibir no consume; consumo no certifica avance. Sensor y reporte manual tienen procedencias distintas. |
| Validaciones | Estado resuelto propuesto no equivale a cerrado aceptado. Recibir no consume; consumo no certifica avance. Sensor y reporte manual tienen procedencias distintas. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Solucionador sin permiso de cierre propone resuelto; inspector valida o reabre. Material sobrante/dañado queda en discrepancia; reintento de recepción no duplica. |
| Resultado esperado | cerrar fallas verificadas y conciliar materiales sin confundirlos con avance |
| Evidencia documental y límite | O01, O02, O06, O09; manual/producto. No se observaron interacciones cliente-servidor en vivo. |


## Profundización posterior

Ver [revisión funcional profunda](revision-profunda.md): RF-OBR-01, RF-OBR-02, RF-OBR-03, RF-OBR-04. Los nuevos criterios se incorporan también a spec/acceptance y no son solo notas de investigación.
