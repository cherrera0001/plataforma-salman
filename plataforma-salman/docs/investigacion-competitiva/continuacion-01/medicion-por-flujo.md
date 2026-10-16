# Medición propuesta por flujo

No se obtuvieron resultados de cliente ni se ejecutaron integraciones. La fórmula económica compartida se mantiene; aquí se precisan unidades y denominadores para evitar llamar resolución a una respuesta o mezclar magnitudes.

| Vertical / flujo | Unidad de observación | Fórmula/métrica y fuente requerida | Cautela |
|---|---|---|---|
| Hotel cambio/cancelación | Solicitud única con propuesta/versionado | `cambios_aplicados_con_aceptación/cambios_aplicados`; p95 `resuelto_en - solicitado_en`; costo completo/solicitudes correctamente cerradas | Cancelado, devolución solicitada y devuelta se cuentan separados; medir errores/reintentos |
| Hotel canales | Evento identificado por proveedor/cuenta y objeto/versión | recibidos, durables, acusados, aplicados, en revisión; p95 de `aplicado_en - ocurrido_en` solo si fecha fuente confiable; si no, usar desde recepción | Reenvío no aumenta denominador de hechos; eventos distintos de la misma reserva sí cuentan |
| Hotel extras | Servicio aceptado según regla de cantidad | `cargos_correctos/servicios_aceptados`; `tareas_cumplidas/tareas_exigibles`; costo por servicio correctamente gestionado | Pago, documento y entrega son resultados distintos; persona/noche/estadía explícitos |
| Inmobiliaria visitas | Solicitud/cita única por referencia y cambio | confirmadas/solicitadas, colisiones/confirmadas; p95 de confirmación; costo por cita válida | No medir asistencia desde invitaciones enviadas; segmentar modo de agenda |
| Inmobiliaria firma | Documento y versión con participantes requeridos | válidos completados/enviados; fallidos por causa; tiempo aprobación→última evidencia válida; costo por documento válido | No contar firma parcial ni pago reserva como promesa completa; revisión jurídica requerida |
| Inmobiliaria portal/postventa | Vínculo/unidad/recurso y caso con visita/trabajo/aceptación | accesos indebidamente permitidos/intentos adversariales; reaperturas/cierres; p95 caso→responsable y trabajo→aceptación | Nunca usar corrección de datos personales como evento de transferencia de propiedad |
| Obra partes/avance | Reporte por origen/autor/turno/partida y unidad | campos correctos/campos revisados; duplicados aceptados/reportes; error avance contra cantidades/base autorizadas; costo/parte aprobado | No sumar porcentajes acumulados; no mezclar m³, kg, unidades ni costos como cantidades homogéneas |
| Obra recepción | Línea/entrega/tramo, material/unidad | entregado, aceptado, rechazado, devuelto, pendiente por política; diferencias por orden y días hasta conciliación | Rechazo y devolución no suman stock; comparar cantidades en unidad normalizada y autorizada |
| Obra presupuesto | Partida/versión/obligación de costo | `disponible = presupuesto_vigente - compromisos_aprobados_vigentes - devengos_sin_compromiso`, solo si esos conjuntos no se solapan y política lo aprueba | Pagos/devengos incluidos en compromiso no se restan otra vez. No equivale a flujo de caja. No hay regla contable universal seleccionada |

Costo por operación: inferencia + herramientas + canal + infraestructura atribuida + revisión/corrección/soporte, incluyendo fallos. Registrar modelo/política/versión, tiempo humano y resultado. Sin denominador positivo o datos fiables, informar no evaluable. Los ejemplos 100/50/20/10 de presupuesto son aritmética en una misma unidad monetaria, no proyección financiera real.

Muestras, ventanas, precisión, RPO/RTO y costos máximos siguen abiertos. Para demostrar valor, comparar proceso manual y asistido en cohortes equivalentes con revisión independiente; no se asignan porcentajes de ahorro desde publicaciones de proveedores.
