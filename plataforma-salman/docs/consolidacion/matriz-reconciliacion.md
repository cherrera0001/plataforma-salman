# Matriz de Reconciliación Semántica — Antigravity (Agy) vs. Codex

Esta matriz consolida las evaluaciones realizadas sobre `plataforma-salman`, clasificando cada hallazgo bajo cuatro categorías rigurosas:
- **CONFIRMADO**: Validación independiente y coincidente entre fuentes primarias y análisis de ambos agentes.
- **COMPLEMENTARIO**: Aporte que profundiza, amplía o refina el alcance sin contradecir la especificación base.
- **CONTRADICTORIO**: Discrepancia en estado, diagnóstico o interpretación, analizada y resuelta con base en evidencia física del repositorio.
- **NO_VERIFICADO**: Declaración comercial de proveedor o hipótesis que carece de comprobación empírica en tiempo de ejecución.

---

## 1. Núcleo Transversal (Core — `specs/000-core`)

| Dimensión | Evaluación Codex | Evaluación Antigravity (Agy) | Categoría | Evidencia Primaria | Decisión y Resolución Canónica |
|---|---|---|---|---|---|
| **Aislamiento Multi-tenant de Conectores** | Propuso desacoplar configuración de conectores por tenant/país (FR-001, FR-002). | Confirmó que credenciales y permisos jamás deben heredarse ni compartirse entre tenants del mismo grupo. | **CONFIRMADO** | Bsale (C04), Tokko (I10), Mews (H13) | Se consolida en `US-CORE-001` y FR-001/FR-002/FR-010. |
| **Máquina de Estados de Conciliación** | Introdujo estados: solicitud enviada $\to$ resultado desconocido $\to$ conciliado/pendiente (FR-003, FR-004). | Confirmó la necesidad de idempotencia estricta ante callbacks repetidos de pasarelas. | **CONFIRMADO** | Square (C06), Mews (H01), Transbank | Se consolida en `US-CORE-002` y FR-003/FR-004/FR-011. |
| **Gobernanza de Herramientas Agénticas** | Estableció límite monetario autónomo inicial de 0 CLP y evaluación fuera de prompt (FR-005). | Ratificó el principio de denegación por defecto y verificación determinista de precondiciones. | **CONFIRMADO** | Salesforce Agentforce (I07), HubSpot (I06) | Se consolida en `US-CORE-003`, FR-005/FR-007 y Constitución Principio III. |
| **Efectos Laterales de Persistencia** | Identificó en continuación que guardar un contacto no debe disparar envíos ni cobros automáticos (FR-012). | Confirmó que la persistencia de datos debe estar segregada del despacho de eventos de mensajería. | **COMPLEMENTARIO** | Wasi API (I11), Tokko API (I17) | Se consolida en FR-012 y regla de efecto colateral en `000-core/spec.md`. |
| **Conversión Monetaria CLP vs. UF** | Registró la definición de UF del Banco Central sin fijar cotización estática (I19). | Confirmó que toda conversión debe registrar fecha, valor oficial de UF y regla de redondeo ratificada. | **CONFIRMADO** | Banco Central de Chile (I19) | Se consolida en FR-003 y NFR-006. |

---

## 2. Cafetería y POS (`specs/001-cafeteria-mesas-pos`)

| Dimensión | Evaluación Codex | Evaluación Antigravity (Agy) | Categoría | Evidencia Primaria | Decisión y Resolución Canónica |
|---|---|---|---|---|---|
| **División de Cuentas (Split) y KDS** | Identificó que dividir cuentas no debe reenviar órdenes a cocina ni anular partes pagadas. | Confirmó el desacoplamiento entre el subsistema financiero del POS y la comanda física en cocina. | **CONFIRMADO** | Toast (C05), Lightspeed (C07), Fudo (C11, C12) | Se consolida en `US-CAF-001`, FR-001..FR-005 y AC-US-CAF-001-01/02. |
| **Residuo de Redondeo en CLP** | Detectó que la división en partes iguales genera residuos en enteros y exige regla visible. | Confirmó que el residuo no puede desaparecer ni cobrarse dos veces; su destino debe ser explícito. | **CONFIRMADO** | Fudo Chile (C11/C12) | Se consolida en FR-015 y decisión pendiente Q-COMP-01. |
| **Procedencia de Costos de Inventario** | Propuso que costo no informado nunca compute como 0 CLP en el cálculo de margen. | Ratificó la obligatoriedad de reportar cobertura de costo desconocida en recetas. | **CONFIRMADO** | Eleventa (C08), Bsale (C04) | Se consolida en `US-CAF-002`, FR-007..FR-010 y AC-US-CAF-002-01/02. |
| **Propuestas de Reposición y Stock** | Propuso generar alertas deduplicadas con expiración de 48 h sin compra automática. | Confirmó que la detección no constituye orden de compra comercial. | **CONFIRMADO** | Documentación de inventario (C09, C10, C13) | Se consolida en `US-CAF-003`, FR-011..FR-013, FR-016. |
| **Claims de IA en Comandas (Justo)** | Mencionó claim comercial de IA para optimizar comandas. | Clasificó el claim como no verificado en runtime; la toma de comanda sigue flujo determinista. | **NO_VERIFICADO** | Justo (C03) | Se mantiene como flujo estándar de comanda; sin adopción de algoritmos opacos. |

---

## 3. Hotel (`specs/002-hotel-reservas-concierge`)

| Dimensión | Evaluación Codex | Evaluación Antigravity (Agy) | Categoría | Evidencia Primaria | Decisión y Resolución Canónica |
|---|---|---|---|---|---|
| **Cupo por Fecha vs. Habitación Asignada** | Separó la disponibilidad de categoría (cupo) de la asignación física de la habitación. | Confirmó que una reserva puede existir sin habitación física asignada previa al check-in. | **CONFIRMADO** | Mews (H01), Cloudbeds (H02, H18) | Se consolida en `US-HOT-001`, FR-001..FR-005, FR-016. |
| **Desacoplamiento de Housekeeping** | Separó estado de limpieza, bloqueo de mantenimiento y ocupación comercial. | Ratificó que habitación sucia hoy no cancela reservas de días posteriores. | **CONFIRMADO** | Oracle OPERA Cloud (H05), Cloudbeds (H16) | Se consolida en `US-HOT-002`, FR-006..FR-009. |
| **Handoff y Concierge Conversacional** | Propuso suspensión de respuestas de compromiso durante atención humana. | Confirmó que la transferencia exige contexto durable, motivo y responsable asignado. | **CONFIRMADO** | HiJiffy (H06), Canary (H09) | Se consolida en `US-HOT-003`, FR-010..FR-014. |
| **Edición/Cancelación con Retención** | Agregó en continuación que cambiar habitación recalcula precio con aceptación versionada. | Confirmó que cancelar reserva no equivale a dinero reembolsado automáticamente. | **COMPLEMENTARIO** | Cloudbeds (H11, H12) | Se consolida en FR-018 y refinamiento P01/P02. |
| **Acuse de Recibo en Canales OTA** | Incorporó acuse de recibo durable antes de confirmar recepción a la OTA. | Confirmó que el acuse técnico previene la pérdida de reservas en caídas transitorias. | **COMPLEMENTARIO** | Booking API (H15), Mews (H13) | Se consolida en FR-020 y refinamiento P04. |
| **Cargos Adicionales y Upsell** | Detalló cargos ligados a estadía vs cargos por persona/noche. | Confirmó que el cargo contable interno no reemplaza la boleta electrónica SII. | **COMPLEMENTARIO** | Mews (H14) | Se consolida en FR-019 y refinamiento P03. |
| **Autopricing Dinámico (US-HOT-004)** | Catalogado como oportunidad OP-07 (P3 DRAFT). | Confirmó que autopricing carece de datos de demanda y se mantiene fuera de los FRs activos. | **CONFIRMADO** | H10 (claim comercial) | Mantenido estrictamente como propuesta futura P3; no implementable. |

---

## 4. Inmobiliaria (`specs/003-inmobiliaria-comercial`)

| Dimensión | Evaluación Codex | Evaluación Antigravity (Agy) | Categoría | Evidencia Primaria | Decisión y Resolución Canónica |
|---|---|---|---|---|---|
| **Progresión de Hitos Comerciales** | Estableció la secuencia: Contacto $\to$ Calificación $\to$ Cotización $\to$ Reserva $\to$ Promesa. | Confirmó que ningún hito posterior puede darse por cumplido sin evidencia verificable previa. | **CONFIRMADO** | MobySuite (I01, I15), PlanOK (I02, I13) | Se consolida en `US-INM-001`, FR-001..FR-006, FR-015. |
| **Calificación Declarada vs. Solvencia** | Separó el presupuesto declarado por el lead de su solvencia financiera real. | Confirmó que la autodeclaración no autoriza promesas de compraventa sin evaluación crediticia. | **CONFIRMADO** | Structurely (I09) | Se consolida en FR-002, FR-004. |
| **Agenda Estática vs. Sincronizada** | Agregó en continuación que una cita sin conexión de calendario queda en estado "por confirmar". | Confirmó que no se debe prometer verificación de colisiones sin integración de calendario. | **COMPLEMENTARIO** | Structurely (I12) | Se consolida en FR-017 y refinamiento P05. |
| **Firma Electrónica de Promesa** | Diferenció la versión contractual aceptada del recibo de pago de la reserva. | Confirmó que la validez jurídica de la promesa en Chile exige ratificación bajo Ley 19.799. | **CONFIRMADO** | MobySuite (I15), BCN Ley 19.799 (I18) | Se consolida en FR-018, decisión pendiente Q-INM-03. |
| **Segregación Persona vs. VínculoUnidad** | Incorporó separación entre los datos personales del cliente y su vínculo de propietario a una unidad. | Confirmó que reasignar o revocar acceso a una unidad no afecta la titularidad de otras unidades. | **COMPLEMENTARIO** | PlanOK iClavis (I16) | Se consolida en FR-020 y refinamiento P07. |
| **Canales Tokko Broker** | Detectó que la documentación pública de Tokko contiene placeholders (`example.com`). | Confirmó que una página web pública no constituye contrato API válido de captura de leads. | **CONFIRMADO** | Tokko Broker API (I17) | Se consolida en conector condicionado y Q-URL-01. |
| **Oferta IA Local (Propeler)** | Identificó la oferta comercial de Propeler (PlanOK) en Chile. | Descartó la premisa de ausencia de IA local en Chile, pero catalogó su autonomía como no probada. | **COMPLEMENTARIO** | PlanOK Propeler (I14) | Se incorpora como referencia competitiva; no se presume autonomía real. |

---

## 5. Constructora (`specs/004-constructora-obra`)

| Dimensión | Evaluación Codex | Evaluación Antigravity (Agy) | Categoría | Evidencia Primaria | Decisión y Resolución Canónica |
|---|---|---|---|---|---|
| **Separación de Roles en Observaciones** | Definió que el rol que propone solución (solucionador) es distinto al que aprueba el cierre (inspector). | Confirmó que una punch list resuelta no equivale a observación cerrada hasta inspección formal. | **CONFIRMADO** | Procore (O01, O10), Autodesk ACC (O02) | Se consolida en `US-OBR-004`, FR-016..FR-019. |
| **Partes Diarios y Turnos Múltiples** | Incorporó en continuación que dos partes del mismo día no deben deduplicarse si son de turnos distintos. | Confirmó que la deduplicación de reportes debe considerar origen, turno y partida, no solo fecha. | **COMPLEMENTARIO** | Procore Daily Log (O11) | Se consolida en FR-021 y refinamiento P08. |
| **Recepción Parcial de Materiales** | Estableció que recibir 6 de 10 deja 4 pendientes y documenta unidades aceptadas vs. rechazadas. | Confirmó que la recepción en bodega no computa como consumo ni como certificación de avance. | **CONFIRMADO** | ICONSTRUYE (O05, O13), Kojo (O07, O15) | Se consolida en FR-020, FR-022 y refinamiento P09. |
| **Trazabilidad Presupuestaria de Compras** | Modeló la separación entre presupuesto total, monto comprometido, devengado y pagado. | Confirmó que un compromiso incluye sus fases derivadas y no debe duplicar la resta presupuestaria. | **COMPLEMENTARIO** | Procore (O16), ICONSTRUYE (O18) | Se consolida en FR-023 y refinamiento P10. |
| **Notas de Voz y Evidencia Visual** | Modeló que notas de voz y fotos extraen campos a borrador revisable; no certifican avance. | Confirmó que la captura visual/acústica exige conectividad y fallback manual obligatorio. | **CONFIRMADO** | OpenSpace (O03, O14, O17), ObraLink (O06) | Se consolida en `US-OBR-003`, FR-010..FR-012, FR-021. |
| **Optimización de Obra (ALICE, US-OBR-005)** | Catalogada como propuesta futura P3 DRAFT fuera de FR activos. | Confirmó que no existen datos ni restricciones suficientes para justificar motor paramétrico. | **CONFIRMADO** | ALICE Technologies (O04) | Se mantiene estrictamente fuera del alcance activo. |

---

## 6. Herramienta REA y Diagnóstico de Entorno

| Dimensión | Evaluación Codex | Evaluación Antigravity (Agy) | Categoría | Evidencia Primaria | Decisión y Resolución Canónica |
|---|---|---|---|---|---|
| **Disponibilidad de Clon de REA** | Reportó que el clon falló por autenticación/DNS en shell sin red; sin checkout local. | Ejecutó `git clone` y clonó íntegramente `morluto/rea` en `investigacion-herramientas/rea/`. | **CONTRADICTORIO** *(Resuelto)* | Repositorio físico en disco, commit `4838f444939677107902549c59b73439e14d3ae9`. | **Resolución:** REA está clonado e inspeccionado estáticamente. La afirmación anterior queda superada por la evidencia física del repositorio. |
| **Compatibilidad con Node.js** | Mencionó Node disponible en general. | Auditó `package.json` de REA (`node: ^22.19.0 || ^24.11.0 || >=26.0.0`) y probó fallo en Node 18 (`ERR_IMPORT_ASSERTION_TYPE_MISSING`). | **COMPLEMENTARIO** | `investigacion-herramientas/rea/package.json#L44-L46` y traza de error en Node v18.19.1. | **Resolución:** REA no es ejecutable en el runtime actual sin actualizar Node a v22+. La ejecución dinámica permanece **BLOCKED**. |
| **Gobernanza de Cambios Globales** | Recomendó evaluar configuración oficial. | Solicitó formalmente aprobación del usuario antes de instalar paquetes globales o alterar Node.js. | **CONFIRMADO** | Instrucciones del usuario y principios de seguridad. | **Resolución:** Prohibición estricta de cambios globales no autorizados. |
