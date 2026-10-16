# Evaluación matemática y económica

**No hay métricas medidas ni proyecciones numéricas aprobadas.** Los SC heredados son objetivos propuestos. Todas las fórmulas esperan observaciones, cotizaciones y volumen; no se rellenan con cifras de proveedores. Moneda de reporte CLP por mes, conservando moneda original, fecha y fuente de tipo de cambio; incluir impuestos y evitar mezclar ingresos con ahorro.

## Variables y fórmulas comunes por vertical

| KPI | Fórmula y unidad | Datos/fuente requerida |
|---|---|---|
| Tiempo neto ahorrado | `T = Σ(t_manual_base_i - t_humano_nuevo_i) / 60`, horas/mes; incluir revisión y corrección | Cronometraje de muestras equivalentes, tareas humanas y reintentos |
| Valor del tiempo | `Vt = T × tarifa_hora_cargada`, CLP/mes | Costo laboral real; distinguir capacidad liberada de ahorro monetario efectivo |
| Costo de inferencia | `Cllm = Σ(tokens_in×precio_in + tokens_out×precio_out + cache + otros_cargos)`, CLP/mes, normalizando unidad por millón cuando aplique | Uso por versión/modelo, tarifa vigente, moneda y cambio |
| Costo herramientas y canal | `Ctool = Σ(llamadas_j×tarifa_j) + canal + OCR + voz + firma + fees`, CLP/mes | Contrato, facturas y telemetría; no asumir WhatsApp gratis |
| Infraestructura | `Cinfra = cómputo + base + almacenamiento + colas + tráfico + backup + observabilidad`, CLP/mes | Cotización por entorno/región y uso; distribuir core sin doble conteo |
| Costo total operativo | `Ctotal = Cllm + Ctool + Cinfra + soporte + revisión_humana + licencias`, CLP/mes | Contabilidad y dedicación atribuible, excluyendo partidas ya contadas |
| Costo por operación | `Cop = Ctotal_atribuido / N_operaciones_completadas`, CLP/operación | Conteo de transacciones únicas, incluyendo costo de intentos fallidos |
| Costo por conversación resuelta | `Cconv = costo_conversacional_total / N_resueltas_correctamente`, CLP/conversación | Resolución validada y sin reapertura en ventana acordada; no contar silencio como éxito |
| Automatización real | `A = N_completadas_correctamente_sin_humano / N_elegibles ×100`, % | Definir elegibilidad antes del piloto, impedir excluir fallos después |
| Error | `E = N_resultados_incorrectos / N_evaluados ×100`, % | Revisión independiente y definición por tarea; errores críticos separados |
| Escalamiento humano | `H = N_casos_escalados / N_casos_iniciados ×100`, % | Eventos auditados; contar intervención espontánea y por fallo |
| Latencia | Percentiles de `resultado_confirmado - recepción`, segundos | Timestamps y clock consistente; registrar timeout, no excluirlo silenciosamente |
| ROI mensual | `(beneficio_incremental_atribuible - Ctotal) / (Ctotal + inversión_inicial_amortizada) ×100`, % | Elegir horizonte y amortización; si denominador cero, no definido; metodología propuesta a ratificar |
| Recuperación inversión | `inversión_inicial / flujo_neto_mensual_positivo`, meses | No calcular con flujo cero/negativo ni sustituir facturación por margen |
| Volumen mínimo SaaS | `Nmin = ceil(costo_fijo_mensual / (precio_unitario_neto - costo_variable_unitario))`, operaciones o conversaciones/mes | Solo si contribución positiva; precio comercial no decidido |
| Volumen mínimo interno | `Nmin = ceil(costo_fijo / (ahorro_real_unitario + margen_incremental_unitario - costo_variable_unitario))` | Evitar doble contar ahorro humano ya incluido en costo; si contribución no positiva no hay umbral finito |

Cada proporción registra numerador, denominador, ventana y cobertura. Si N=0, resultado no definido. Informar incertidumbre y sesgo de selección; no extrapolar 50 conversaciones al mes completo sin representatividad. Para estimar latencia/costo de agentes, reportar distribución y versión, no solo promedio.

## Aplicación por vertical

| Vertical | Unidad de operación / KPI de negocio | Fórmulas específicas y fuentes faltantes |
|---|---|---|
| Cafetería | Pedido liquidado, cuenta cerrada, factura revisada, propuesta reposición | Reducción cierre `(t_base-t_nuevo)/t_base`; error margen `abs(margen_sistema-margen_manual)/abs(margen_manual)` con tratamiento especial si margen manual cero; stock `abs(proyectado-físico)/físico` por insumo, no definido si físico cero. Faltan tickets Eleventa, conteos, recetas, mermas y tiempos; SC-004 debe ratificar si 2 % es relativo o puntos de margen. |
| Hotel | Reserva confirmada sin conflicto, check-in, conversación correctamente resuelta | Directas/total reservas confirmadas en ventana; conflictos/confirmaciones; upsells pagados/no anulados dividido por ofertas elegibles. Descontar cancelaciones y costos OTA reales. Faltan PMS, comisiones, ocupación, tarifas, estacionalidad y tiempos de recepción. SC-008 8 % es objetivo, no medición de Duve transferible. |
| Inmobiliaria | Lead calificado verificable, visita, cotización, reserva, promesa válida y caso postventa | Conversión visitas/leads elegibles; reducción lead→promesa por cohortes equivalentes; morosidad monto vencido/total exigible (o cuotas: elegir y no mezclar). Atribución de venta exige control por precio/campaña. Faltan CRM, cartera, tiempos, garantías y política de firma. |
| Constructora | Reporte aprobado, partida validada, inspección cerrada, compra revisada | Avance físico `cantidad_ejecutada_aceptada/cantidad_total_aprobada×100`; desvío en puntos `avance_real-avance_programado` frente a desvío relativo `(real-programado)/programado×100`. Si programado=0, relativo no definido. Avance ponderado requiere pesos presupuestarios aprobados. Faltan presupuesto versionado, cantidades, programación, reportes y costo de revisión; Q-OBR-02 elige el umbral. |

000 es centro de costo compartido, no vertical con ROI independiente: repartir costo por drivers declarados (tenants activos, pagos, documentos o consumo), registrar regla y evitar cargar el mismo costo completo cuatro veces. La venta de SaaS, el ahorro interno y los ingresos incrementales son modelos económicos distintos que el cliente debe elegir.

## Protocolo de medición propuesto

Registrar línea base antes del piloto durante una ventana representativa que acuerde el negocio; controlar día/turno, temporada y canal. Cada operación tiene ID único, tenant, inicio/fin, minutos humanos, inferencia/herramientas, costo y resultado validado. Separar ambientes de prueba de datos productivos. Comparar cohortes equivalentes y revisar semanalmente errores/costos; ningún beneficio se declara antes de contar con evidencia y revisión humana. Mantener objetivos SC originales y renegociar solo con justificación trazable.

## Granularidad adicional de medición

Los flujos de hotel, inmobiliaria y obra ahora tienen unidades/denominadores por cambio, evento, extra, cita, documento, vínculo, caso, parte, recepción y partida. Ver docs/investigacion-competitiva/continuacion-01/medicion-por-flujo.md. No se agregaron beneficios medidos ni presupuestos ficticios; los ejemplos aritméticos son casos de aceptación. Compromiso, devengo y pago pueden representar etapas de la misma obligación y no se suman indiscriminadamente como gasto nuevo.
