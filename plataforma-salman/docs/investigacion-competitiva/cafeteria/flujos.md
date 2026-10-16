# Análisis funcional — cafeteria

Reconstrucción desde documentación pública; ninguna secuencia fue ejecutada en UI/REA. Cada regla propia se propone para el proyecto; no se atribuye al proveedor. Consulte matriz-evidencias para observación documental y límites.

## US-CAF-001 / H1

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | comensal y cajero autorizado |
| Objetivo | pedir y pagar una parte explícita de una cuenta compartida |
| Evento inicial | el cliente escanea el QR y confirma pedido o solicita pagar su parte de la cuenta |
| Precondiciones | mesa activa, pedido versionado, regla de redondeo y de pago ratificadas; saldo no liquidado |
| Pasos | Abrir mesa → confirmar pedido → ver saldo y partes → elegir ítems o reparto igual → mostrar descuentos/propina/documentación → reservar imputación → pagar → actualizar saldo hasta cierre. |
| Datos | AsignaciónCuenta, versión pedido, parte/ítem, descuentos, propina separada, residuo y pago. |
| Reglas | Suma de partes en CLP equivale al total exigible. Mostrar quién recibe residuo según regla aprobada; sin regla no confirmar reparto. Partes liquidadas no se editan ni anulan por deshacer división. |
| Validaciones | Suma de partes en CLP equivale al total exigible. Mostrar quién recibe residuo según regla aprobada; sin regla no confirmar reparto. Partes liquidadas no se editan ni anulan por deshacer división. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Otro cliente paga el mismo saldo: rechazar segunda imputación y refrescar. Pago desconocido: parte pendiente hasta conciliar. Reagrupar antes del pago no reenvía cocina. |
| Resultado esperado | cerrar el saldo correctamente sin repetir la orden de cocina |
| Evidencia documental y límite | C02, C05, C07, C11, C12; manual/producto. No se observaron interacciones cliente-servidor en vivo. |

## US-CAF-002 / H2

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | administrador de cafetería |
| Objetivo | aprobar costos e importar inventario con procedencia verificable |
| Evento inicial | el administrador carga factura/exportación o se registra una venta que consume una receta |
| Precondiciones | recetas/unidades versionadas, muestra Eleventa autorizada, documento de compra y aprobador |
| Pasos | Importar/extraer → detectar campos ausentes o duplicados → revisar cantidades/unidades/costos → aprobar → generar movimientos una vez → calcular margen con cobertura. |
| Datos | LoteImportación, fila/origen, unidad, conversión revisada, receta/versión, línea gasto y evidencia. |
| Reglas | Costo desconocido no es cero; conservar fuente y versión de receta que originó consumo. No prometer exportación de datos que el archivo no contiene. |
| Validaciones | Costo desconocido no es cero; conservar fuente y versión de receta que originó consumo. No prometer exportación de datos que el archivo no contiene. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | OCR ambiguo requiere captura manual. Subreceta sin correspondencia de unidad bloquea cálculo de ese costo; mostrar cobertura incompleta. |
| Resultado esperado | conocer margen sin ocultar errores de receta ni de migración |
| Evidencia documental y límite | C08, C10, C04, C12; manual/producto. No se observaron interacciones cliente-servidor en vivo. |

## US-CAF-003 / H3

| Campo | Reconstrucción propuesta |
|---|---|
| Actor | administrador aprobador |
| Objetivo | recibir propuestas y alertas con fuente y estado de revisión |
| Evento inicial | vence una revisión programada o llega una anulación, descuento o evento de stock que satisface la regla |
| Precondiciones | stock y ventas con cobertura/fecha; regla de mínimos y aprobador definidos |
| Pasos | Programar revisión autorizada → comprobar datos → detectar umbral → generar propuesta/alerta referenciada → notificar vía permitida → aprobar/rechazar/expirar. |
| Datos | EjecuciónRegla, ventana de datos, evento detectado, propuesta y estado revisión. |
| Reglas | Revisión programada no implica compra autónoma. Mantener propuesta separada de orden; 48 h de expiración heredadas sujetas a política cliente. |
| Validaciones | Revisión programada no implica compra autónoma. Mantener propuesta separada de orden; 48 h de expiración heredadas sujetas a política cliente. Identidad/tenant, versión y evidencia exigibles. |
| Estados/transiciones | Ver data-model de la feature y flujo de historia; pendiente/desconocido no es éxito. |
| Excepciones | Sin datos suficientes o fuente vencida: informar revisión incompleta. Si ya existe alerta del mismo evento/ventana, actualizar evidencia sin enviar duplicados ilimitados. |
| Resultado esperado | reducir revisión repetitiva sin automatizar compromisos de compra |
| Evidencia documental y límite | C09, C10, C13; manual/producto. No se observaron interacciones cliente-servidor en vivo. |

## Precisión regional incorporada

C11/C12 verifican Fudo Chile en https://fu.do/es-cl/; C02 solo inspira el caso de redondeo. La declaración de WebPay en tienda online no implica flujo de mesa o split de cobro equivalente. La evidencia mejora la alternativa de adaptar un POS existente, sin demostrar integración ya ejecutada.
