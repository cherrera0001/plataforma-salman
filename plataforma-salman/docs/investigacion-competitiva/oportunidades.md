# Priorización cuantitativa de mejoras

Puntúa decisiones de definición, no proveedores ni rentabilidad. Se mantienen prioridades originales P1/P2/P3; no se inventa demanda desde la oferta competidora. Los valores conocidos de la tabla son **juicio provisional del investigador**, no mediciones. Impacto comercial y frecuencia quedan desconocidos; se calculan intervalos en lugar de sustituirlos por resultados supuestos.

## Pesos y fórmula

Valor usuario 20 %, impacto comercial 15 %, frecuencia 10 %, criticidad operacional 15 %, complejidad inversa 10 %, riesgo técnico inverso 10 %, dependencias inversas 5 %, calidad de evidencia 10 %, diferenciación 5 %. Priman valor y operación; diferenciación pesa poco porque no justifica alcance sola. La evidencia pesa por precisión del comportamiento, no por notoriedad del proveedor.

Escala 1–5. En factores inversos, 5 es menor esfuerzo/riesgo/dependencia. `S = Σ peso_i × (s_i-1)/4`, rango 0–100. Variables comerciales desconocidas usan extremos 1/5 para cotas; no son proyecciones de venta. Pesos y valores completos en priorizacion.json. Si el cliente cambia pesos se recalcula; los intervalos solapados impiden afirmar orden definitivo.

| ID | Mejora y trazabilidad | Intervalo S | Justificación / decisión |
|---|---|---|---|
| OP-01 | Conciliar pendientes y capacidades por conector — US-CORE-001/002 (C04/C06/H01/I10) | 56.25–81.25 | Previene efectos financieros duplicados; el volumen y costo siguen desconocidos. |
| OP-02 | Reparto de cuenta sin alterar pagos ni cocina — US-CAF-001 (C02/C05/C07/C12) | 60.00–85.00 | Refina el P1 existente; demanda y frecuencia requieren observar el local. |
| OP-03 | Inventario, asignación y preparación independientes — US-HOT-001/002 (H01/H02/H05) | 57.50–82.50 | Corrige una ambigüedad operativa antes de elegir PMS. |
| OP-04 | Identidad, cita y contrato como hitos evidenciados — US-INM-001 (I01/I03/I09/I10) | 55.00–80.00 | Reduce compromisos incorrectos; no demuestra mayor conversión. |
| OP-05 | Observación con cierre autorizado y recepción parcial — US-OBR-003/004 (O01/O02/O05/O09) | 58.75–83.75 | Precisa trazabilidad de obra y compras, condicionado al alcance V2. |
| OP-06 | Transferencia humana con contexto y responsable — US-HOT-003/INM-002 (H06/I06) | 56.25–81.25 | No contar handoff como resolución; no construir helpdesk universal. |
| OP-07 | Autopricing hotelero — US-HOT-004 propuesta futura (H10) | 27.50–52.50 | Mantener en investigación P3: faltan demanda, política, datos y evaluación. |
| OP-08 | Optimización paramétrica de obra — US-OBR-005 propuesta futura (O04) | 30.00–55.00 | No integrar al alcance activo: requiere programación y restricciones que no se han entregado. |

OP-01 a OP-06 enriquecen necesidades ya presentes; no es autorización para implementar más módulos. OP-07 y OP-08 se mantienen propuestas futuras fuera de FR activos. Diferenciación local en pagos/documentos/gobernanza sigue hipótesis: no se afirma exclusividad.

Resultados comprobados: cambios documentales y fuentes identificadas. Beneficios esperados: menos ambigüedad y mejores controles de aceptación; no se afirma reducción medida de tiempo, costo, error o ventas. Para decidir secuencia real: entrevistar usuarios, muestrear frecuencia/errores, estimar esfuerzo con equipo y cotizar proveedores. Ver economía compartida para unidades, denominadores y ROI sin números inventados.

## Prioridades de profundización en las otras verticales

Se mantienen pesos y escala; puntuaciones son juicio provisional, no demanda o ROI observado. Impacto comercial y frecuencia continúan nulos y generan intervalos. No se cambia prioridad original ni se habilita alcance de candidatas.

| ID | Mejora | Intervalo 0–100 | Evidencia / decisión |
|---|---|---|---|
| OP-09 | Cambio/cancelación hotel y recepción de canales | 57.50–82.50 | H11/H12/H13/H15: Prevenir pérdida/doble efecto; frecuencia e impacto económico no medidos. |
| OP-10 | Modo de agenda y versión de firma | 55.00–80.00 | I12/I15/I18: Distinguir compromiso real y recuperación; formalidades pendientes. |
| OP-11 | Vínculo de portal y efectos implícitos | 58.75–83.75 | I11/I16/I17: Confidencialidad y consentimiento; API real por verificar. |
| OP-12 | Partes, recepción y exposición presupuestaria | 56.25–81.25 | O11/O13/O14/O16/O18: Semántica y cálculo antes de automatización; escala del negocio desconocida. |
| OP-13 | Subcontratos y consultas técnicas opcionales | 32.50–57.50 | O12/O16: Mantener DRAFT fuera de alcance hasta validar necesidad y autoridad. |
