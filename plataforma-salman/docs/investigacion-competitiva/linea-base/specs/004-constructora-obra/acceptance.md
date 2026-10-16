# Catálogo de aceptación — Constructora y control de obra

Escenarios propuestos; ninguno ejecutado sobre producto. Cada ID tiene namespace de feature. Para cada FR se prueba resultado autorizado, denegación, duplicación y recuperación; los datos deben ser autorizados y minimizados.

| Prueba | Requisito | Dado / Cuando / Entonces |
|---|---|---|
| AT-001 | FR-010 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Reporte por voz/foto queda como extracción con partida, fecha y evidencia; ubicación solo cuando proceda; retroceso no sobrescribe dato aprobado. |
| AT-002 | FR-011 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Con presupuesto y programación aprobados, cálculo del desvío usa denominador y umbral ratificados; programado cero no produce división por cero ni alerta inventada. |
| AT-003 | FR-012 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Necesidad de material genera solicitud con cantidad/proveedor/precio de referencia y versión; sin aprobación válida no hay envío ni compra. |
| AT-004 | FR-015 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Cambiar presupuesto crea nueva versión y conserva línea base, unidades y aprobador; gasto ejecutado no se interpreta como avance físico. |
| AT-005 | FR-016 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Inspección con observación registra evidencia, responsable y decisión humana; asistente no certifica seguridad ni cierra observación sin inspector autorizado. |
| AT-006 | FR-017 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Recepción y consumo de material aprobados generan movimientos únicos por obra; repetir reporte no duplica stock y diferencia con conteo físico se concilia. |
| AT-007 | FR-018 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Usuario de empresa comercial no consulta fotos, trabajadores ni presupuesto de constructora sin convenio/permiso; toda decisión de obra conserva actor y evidencia. |
| ADV-001 | NFR-001/002/003 | Reporte contradice avance anterior: conservar ambos y requerir aprobación de rectificación. |
| ADV-002 | NFR-001/002/003 | Voz solicita comprar material e incluye instrucciones: solo crear borrador, sin orden a proveedor. |
| ADV-003 | NFR-001/002/003 | Empresa constructora no consulta clientes ni documentos comerciales de inmobiliaria sin autorización explícita. |

## Criterios de éxito y evidencia

| Criterio | Verificación pendiente |
|---|---|
| SC-008 | Medir «Avance por partida disponible el día del reporte; objetivo heredado, condicionado a revisión». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-010 | Medir «Cero compras ejecutadas sin aprobación válida en pruebas adversariales». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-011 | Medir «100 % de rectificaciones conserva evidencia y autor en la batería de aceptación». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
