# Catálogo de aceptación — Core transversal

Escenarios propuestos; ninguno ejecutado sobre producto. Cada ID tiene namespace de feature. Para cada FR se prueba resultado autorizado, denegación, duplicación y recuperación; los datos deben ser autorizados y minimizados.

| Prueba | Requisito | Dado / Cuando / Entonces |
|---|---|---|
| AT-001 | FR-001 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Una identidad con membresía vencida solicita datos: se deniega; la membresía vigente solo habilita su empresa. |
| AT-002 | FR-002 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Usuario, worker y agente de A usan identificador de B: se deniega sin revelar existencia y se registra el intento. |
| AT-003 | FR-003 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Diez retornos repetidos y desordenados de una orden producen una única imputación; monto u orden incoherentes pasan a revisión sin saldo acreditado. |
| AT-004 | FR-004 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Una operación cubierta por voucher o anticipo ya documentado no genera duplicado; una observación documental conserva pago y alerta para regularización según política. |
| AT-005 | FR-005 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Una acción crítica produce evidencia con actor, tenant, política, aprobación y resultado; alteración del registro es detectable por el mecanismo seleccionado. |
| AT-006 | FR-006 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Un operador sin permiso intenta leer certificado o adjunto ajeno: se deniega; vence el plazo de retención aprobado y se aplica disposición registrada. |
| AT-007 | FR-007 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Un agente cambia el monto después de la aprobación: autorización inválida, operación denegada y nueva aprobación requerida. |
| AT-008 | FR-008 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: El proveedor cae tras enviar confirmación: el estado queda desconocido/pendiente; al consultar y reconciliar se aplica un solo resultado. |
| AT-009 | FR-009 | Dadas precondiciones del requisito y actor/tenant autorizados, cuando se ejecuta el flujo: Un consumidor de versión anterior recibe cambio incompatible: se mantiene versión compatible o se impide publicación hasta completar prueba y migración. |
| ADV-001 | NFR-001/002/003 | Un usuario, worker y agente del tenant A intentan leer/escribir un recurso de B: todos reciben denegación sin revelar existencia. |
| ADV-002 | NFR-001/002/003 | Repetir confirmación bancaria diez veces mantiene un único efecto y permite auditoría. |
| ADV-003 | NFR-001/002/003 | Cambiar monto tras aprobación invalida autorización; proveedor desconectado queda pendiente y bloquea ejecución. |

## Criterios de éxito y evidencia

| Criterio | Verificación pendiente |
|---|---|
| SC-001 | Medir «Cero accesos entre tenants en la batería adversarial aprobada». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-002 | Medir «Un único efecto financiero ante diez repeticiones del mismo resultado». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
| SC-003 | Medir «Toda acción crítica tiene actor, tenant, evidencia y resultado auditables». Registrar muestra, ventana temporal, denominador, errores y línea base; conservar conteos y evidencia. No hay medición actual. |
