# Revisión funcional profunda — constructora

Revisión de fuentes primarias y reconstrucción de comportamiento; no se ejecutó aplicación/REA. El campo actor/flujo/reglas siguiente es propuesta propia y conserva sus límites de evidencia.

### RF-OBR-01 — Registrar partes y extracción sin perder autoría, unidades o conectividad

**Historia US-OBR-003** (misma historia/ID, prioridad P1; no es historia nueva).

Como jefe de obra, colaborador y revisor de avance, quiero registrar partes y extracción sin perder autoría, unidades o conectividad, para consolidar cantidades aprobadas sin duplicar reportes ni presentar transcripción como avance certificado.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O11, O14, O17, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** se recibe parte manual o evidencia de campo, o se reintenta enviar tras falla.

**Precondiciones:** obra/partida/versión y unidades identificadas; permisos de reporte/revisión y canal soportado.

**Flujo principal:**

1. Conservar original con autor, fecha de hecho/recepción y alcance turno/zona si aplica.
2. Verificar recepción antes de informar enviado; extracción IA solo si disponible.
3. Separar cantidades nuevas, acumuladas y correcciones; marcar ambigüedad.
4. Revisor aprueba o rechaza aportes y relaciona duplicados.
5. Consolidar avance solo desde cantidades aceptadas y denominador vigente.

**Flujos alternativos y excepciones:** Sin conectividad para IA: no afirmar extracción terminada; usar captura manual o envío diferido soportado, sin prometer aplicación offline no definida. Dos reportes del día pueden ser legítimos; porcentaje sin base no se suma.

**Reglas de negocio/validaciones:** La clave del reporte no es solo fecha+obra. Voz es evidencia no confiable; edición no sustituye original. Exportación offline consultable no demuestra captura/sincronización IA sin red.

**Datos y estados:** Parte, claveOrigen, autor, fechaHecho, recibidoEn, turno/zona/partida, tipoCantidad incremental/acumulada/corrección, extracción/revisión y versión base.

**Dependencias:** Q-OBR-01/02/03, canal y procedimiento de contingencia; no crea app móvil ni promete reconocimiento local.

**Riesgos:** Doble avance, falsa precisión, reporte perdido, prompt injection y ubicación personal expuesta.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-003-03: Dados dos partes legítimos de turnos distintos en una obra/día y un reenvío del primero, cuando se reciben, entonces conserva ambos aportes y no duplica el reenvío.
- AC-US-OBR-003-04: Dado porcentaje 40 % acumulado y nuevo reporte 45 % acumulado de la misma partida, cuando se revisa, entonces no produce 85 % por sumarlos y requiere la base/unidad definida.
- AC-US-OBR-003-05: Dada falta de conexión para transcribir, cuando se carga evidencia, entonces no se marca transcrita/aprobada; la vía manual soportada conserva mismos permisos y revisión.

**Métricas:** partes aceptados/recibidos, error por unidad/campo, retraso hecho→validación, duplicados y costo por parte aprobado. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-OBR-02 — Conciliar entrega, aceptación, rechazo y devolución de material

**Historia US-OBR-004** (misma historia/ID, prioridad P2; no es historia nueva).

Como encargado de bodega, comprador y aprobador de recepción, quiero conciliar entrega, aceptación, rechazo y devolución de material, para saber qué material se puede consumir y qué obligación sigue pendiente.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O13, O15, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** llega entrega parcial o se comunica rechazo/devolución.

**Precondiciones:** orden/líneas/versiones autorizadas, unidades revisadas, documento de entrega y responsables.

**Flujo principal:**

1. Identificar orden, tramo/entrega y líneas de material.
2. Registrar cantidad física entregada y separar aceptada/rechazada con motivo/evidencia.
3. Actualizar existencias solo de lo aceptado y calcular pendiente según política de reposición.
4. Registrar devolución como movimiento vinculado, sin borrar recepción.
5. Conciliar con compra/guía/factura por proceso autorizado antes de pago.

**Flujos alternativos y excepciones:** Entrega repetida no es nueva recepción. Conversión de unidad, exceso o versión discrepante van a revisión. Una factura no demuestra que el material llegó ni fue aceptado.

**Reglas de negocio/validaciones:** Pendiente, aceptado, rechazado y devuelto son magnitudes distintas; reposición/cancelación requieren regla del comprador. No usar rechazo como borrado de evidencia ni como pago automático.

**Datos y estados:** EntregaProveedor, TramoOrden, RecepcionLinea, cantidadEntregada/aceptada/rechazada/devuelta, MotivoEvidencia y discrepanciaContable.

**Dependencias:** Q-OBR-03 y Q-CORE-02; contabilidad/facturación se integra si se decide, no se presume módulo existente.

**Riesgos:** Stock inexistente, recepción doble, pago de material rechazado y cambio de unidad oculto.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-004-03: Dada orden de diez unidades y entrega física de seis con cinco aceptadas y una rechazada a reponer por política configurada, cuando se valida, entonces stock aumenta cinco y pendientes de suministro son cinco, con rechazo documentado.
- AC-US-OBR-004-04: Dada misma entrega recibida dos veces por reintento, cuando se registra, entonces no duplica stock; una segunda entrega con identidad distinta sí se evalúa como nueva.
- AC-US-OBR-004-05: Dada devolución de una unidad previamente aceptada, cuando se aprueba, entonces conserva recepción y registra movimiento de devolución; no se infiere abono financiero ni cambio de contrato.

**Métricas:** cantidades aceptadas/entregadas, discrepancias por orden, días pendientes y costo de conciliación por recepción. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-OBR-03 — Controlar línea base y compromiso sin sumar estados del mismo gasto

**Historia US-OBR-004** (misma historia/ID, prioridad P2; no es historia nueva).

Como control de obra y administrador de compras, quiero controlar línea base y compromiso sin sumar estados del mismo gasto, para detectar desviaciones presupuestarias con unidades y obligaciones comparables.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O16, O18, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** nueva propuesta de compra, cambio presupuestario o conciliación de obligación.

**Precondiciones:** presupuesto vigente por partida, reglas de compromiso/devengo/pago y aprobación definidos.

**Flujo principal:**

1. Seleccionar línea base y versión vigente.
2. Clasificar propuesta/compromiso/recepción/devengo/pago de cada obligación.
3. Calcular exposición y disponible con fórmula aprobada, sin doble contar estados de la misma obligación.
4. Alertar desvío o falta de clasificación y solicitar decisión humana.
5. Registrar cambio aprobado de presupuesto como nueva versión manteniendo comparación histórica.

**Flujos alternativos y excepciones:** Sin presupuesto o regla contable se informa no evaluable. Cancelación de compromiso ajusta saldo según política/evidencia; cambio de fecha no altera cantidades físicas.

**Reglas de negocio/validaciones:** Gasto, pago y avance físico no son equivalentes. El compromiso puede contener importes ya devengados/pagados, por lo que no se suman ciegamente. No aprobar excedente ni subcontrato desde IA.

**Datos y estados:** PresupuestoVersionado, Partida, ObligacionCosto y sus estados, compromisosVigentes, ajustes/causa/aprobador y FormulaControl versionada.

**Dependencias:** Q-OBR-01/02/03 y regla contable del cliente; gestión integral de subcontratos queda fuera del alcance activo hasta decisión.

**Riesgos:** Disponible inflado/negativo por doble cuenta, cambio de base invisible y compromiso no autorizado.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-004-06: Dado presupuesto de ejemplo 100 y compromiso total 50 que ya incluye devengo 20 y pago 10, cuando se calcula disponible sin otras obligaciones, entonces es 50 y no 20 al descontar los tres estados otra vez.
- AC-US-OBR-004-07: Dada modificación aprobada de presupuesto, cuando se compara avance/costo histórico, entonces conserva línea base, versión vigente y motivo/aprobador; no reescribe el pasado.
- AC-US-OBR-004-08: Dada partida sin fórmula o clasificación válida, cuando se evalúa compra, entonces indica control no evaluable y requiere revisión, sin aprobar automáticamente.

**Métricas:** partidas con exposición conciliada/partidas, error de disponible vs revisión y tiempo de detectar desvío; no ROI inventado. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.


### RF-OBR-04 — Aceptar solución y distinguir respuesta técnica oficial

**Historia US-OBR-004** (misma historia/ID, prioridad P2; no es historia nueva).

Como inspector, solucionador y responsable técnico, quiero aceptar solución y distinguir respuesta técnica oficial, para cerrar una falla con autoridad y evidencia, sin confundir comentario de IA con instrucción de obra.

**Descripción y necesidad:** refinamiento funcional de la necesidad anterior. La propuesta precisa responsabilidad, recuperación y significado del éxito; no presupone demanda ni beneficio medido.

**Inspiración y evidencia:** O10, O12, con URLs y límites en matriz-evidencias.md. Reconstrucción documental e **INFERENCIA PROPIA** para el diseño; no comportamiento ejecutado ni arquitectura observada.

**Disparador:** se entrega solución, respuesta técnica o revisión de inspección.

**Precondiciones:** observación vinculada a evidencia/partida, responsables y permisos de solución/cierre definidos.

**Flujo principal:**

1. Relacionar solución/respuesta con observación y versión de evidencia.
2. Solucionador declara lista para revisión sin cerrar por sí solo.
3. Revisor autorizado acepta, no acepta o pide información con motivo.
4. Registrar cierre o reapertura y responsable de siguiente acción.
5. Si una respuesta exige cambio contractual/presupuestario, abrir decisión aparte sin ejecutarla.

**Flujos alternativos y excepciones:** Varios comentarios o revisores no equivalen a respuesta oficial. Caso duplicado se vincula sin borrar evidencia. Nueva falla tras cierre reabre o crea caso relacionado según política.

**Reglas de negocio/validaciones:** El sistema no certifica seguridad estructural. Respuesta oficial es declaración del rol habilitado, no texto de modelo. Flujo RFI enterprise no se incorpora por usarlo como comparación.

**Datos y estados:** Observacion, PropuestaSolucion, RespuestaTecnica con emisor/alcance, EvidenciaRevision, estado/revisor/motivo y referenciaDecisionCambio.

**Dependencias:** Q-OBR-03 y política de evidencia; interfaz con comercial/postventa solo por convenio, sin permisos compartidos por grupo.

**Riesgos:** Cerrar trabajo no inspeccionado, ejecutar instrucción técnica no válida y exposición de fotos.

**Humano y agente:** consulta/borrador dentro de permiso; compromiso financiero/tributario/contractual o cierre técnico requiere control determinista y aprobación humana. Ningún MCP recibe escritura por defecto. Evidencia original, versión, aprobación y resultado se auditan; resultado desconocido se reconcilia, no se presenta confirmado. La capacidad concreta se delimita en [perfiles de agentes](../continuacion-01/perfiles-agentes.md).

**Aceptación Given/When/Then propuesta (no ejecutada):**

- AC-US-OBR-004-09: Dado solucionador sin permiso de aceptar, cuando informa reparación lista, entonces queda por revisar y no cerrada; el inspector puede no aceptar con motivo.
- AC-US-OBR-004-10: Dado comentario generado por IA que cambia una especificación técnica, cuando se adjunta al caso, entonces no se convierte en respuesta oficial ni modifica presupuesto o programa.
- AC-US-OBR-004-11: Dada observación reabierta por nueva evidencia, cuando se inspecciona historial, entonces conserva cierre previo, responsable, evidencia y motivo de reapertura.

**Métricas:** cierres aceptados/revisados, reaperturas, tiempo listo→aceptado y casos sin responsable. Informar unidad, numerador/denominador y ventana; sin muestra no se informa porcentaje. Objetivos y políticas siguen pendientes de ratificación.
