# Hallazgos y correcciones

Fecha 2026-10-16. Severidad: crítica bloquea decisión o integridad financiera; alta compromete diseño/aceptación; media reduce confiabilidad. Se corrigen derivados, nunca originales. No se equipara control propuesto con decisión cliente aprobada.

| ID | Ubicación | Evidencia | Severidad | Impacto | Corrección propuesta/aplicada | Estado |
|---|---|---|---|---|---|---|
| F-001 | CAF §1.1; CAF/HOT/INM FR de core | Catálogo, transacciones, gastos y analítica se declaran core sin límites comunes | Alta | Acoplamiento, mezcla de permisos y crecimiento innecesario | Core reducido y ADR-001; ratificar cambio constitucional | CORREGIDO DOCUMENTALMENTE / aprobación pendiente |
| F-002 | CAF §1.2, FR-005, SC-003; HOT FR-004/SC-004; INM FR-005 | Cada pago implica boleta; puede haber anticipos, saldo y voucher | Crítica | Doble documentación y tratamiento tributario incorrecto | Separar pago/hecho/entrega, Q-CORE-02 y ADR-004 | CONTROL PROPUESTO / BLOQUEADO fiscalidad |
| F-003 | INV §4 Lo que le falta a eleventa; CAF FR-010 | INV dice solo inventario y luego promete histórico de ventas | Alta | Migración ofrecida sin conocer cobertura | E-07/08 prueban exportación genérica de ventas/movimientos; exigir muestra cliente | CONTRADICCIÓN CORREGIDA / muestra pendiente |
| F-004 | HOT §0, §5; FR-007 frente a CAF §3 entidades | Hotel exige 001 en producción y ubica pedidos en core | Alta | Secuencia obligatoria innecesaria y propiedad ambigua | Pedidos en cafetería, interfaz opcional; hotel H1 independiente | CORREGIDO DOCUMENTALMENTE |
| F-005 | HOT H1/H3 y §5–6 frente a INV §5 | PMS propio se presupone antes de evaluar existente | Crítica | Costo y alcance no autorizados | Sistema de registro por seleccionar; ADR-002, Q-HOT-01 | BLOQUEADO |
| F-006 | HOT casos borde y FR-005 | Seguir vendiendo con inventario local durante caída del channel manager contradice impedir sobreventa | Crítica | Sobreventa y costos de relocalización | No confirmar inventario incierto sin cupo seguro; política comercial pendiente | DEFECTO CORREGIDO / política pendiente |
| F-007 | INM §0 H3 §2 FR-010–012 SC-008 | Obra duplicada en 003 y 004; dependencia de módulo previo no entregado | Alta | Trazabilidad y estimaciones falsas | Trasladar H3/FR/SC a 004 y registrar ausencia de módulo | CORREGIDO / alcance 004 bloqueado |
| F-008 | INV §2–5, tablas de precios y §6 | Referencias sin URL; porcentajes de proveedor y afirmaciones de ausencia universal | Alta | ROI y compra basados en marketing | Registro de afirmaciones, E-14; no usar como hecho ni cálculo financiero | CLASIFICADO / VERIFICACIÓN EXTERNA PARCIAL |
| F-009 | HOT FR-003 y §5; INM FR-001/006 | APIs OTA, portales y firma se tratan como accesibles con credenciales | Crítica | Integración inviable por contrato/certificación | Q-HOT-02, Q-INM-01/03; contratos técnicos no fabricados | BLOQUEADO |
| F-010 | CAF §1.4; HOT/INM plan amenazas | Ley 21.719 sin distinguir vigencia diferida | Alta | Plan legal con fecha equivocada | E-06; distinguir régimen vigente y transición al 01-12-2026 | CORREGIDO DOCUMENTALMENTE / revisión legal pendiente |
| F-011 | CAF §1.5 y autonomía en tres fuentes | Datos reales en demos y ledger inmutable sin tratamiento de privacidad/retención | Alta | Exposición de datos y promesa de conservación absoluta | Conservar regla de demos, exigir autorización; pruebas sintéticas permitidas; integridad y retención controladas | AMPLIACIÓN PROPUESTA / ratificación pendiente |
| F-012 | CAF FR-006; §6 Redis | Cola/Redis remoto no demuestra continuidad local sin red | Alta | Pérdida o duplicación de pedidos y caja | No seleccionar solución offline; procedimiento, persistencia local y reconciliación a decidir Q-CAF-02 | BLOQUEADO |
| F-013 | CAF SC-003; HOT SC-004 y §2 casos SII | 100 % de emisión <30/60 s contradice falla externa prevista | Alta | Criterio imposible de garantizar unilateralmente | Conservar objetivo heredado como aspiración; medir incidencias y pendientes; ratificar SLO por dependencia | BLOQUEADO aceptación final |
| F-014 | INM H3 umbral >10 %; FR-011 | No distingue puntos porcentuales de variación relativa ni base presupuestaria | Alta | Alertas equivocadas | Q-OBR-02, fórmulas alternativas en economia.md | BLOQUEADO |
| F-015 | CAF §5 y las seis preguntas; HOT siete; INM siete | Preguntas de negocio sin respuesta; límites monetarios no definidos | Crítica | No hay autorización ni alcance final | Conservar todas y agrupar Q; sin política escritura cero y fail closed | BLOQUEADO |
| F-016 | Fuentes §0 y §7 | Flujo de agente descrito como ejecutable sin instalación previa | Media | Falsa evidencia de SDD o comando inventado | Contrastar referencia v1.2.0; no crear feature.json ni scripts internos inventados | CORREGIDO DOCUMENTALMENTE / Q-TOOL-01 |
| F-017 | Conjunto de cuatro fuentes | NFR sin RPO/RTO, presupuesto, tratamiento de datos, roles detallados ni mediciones base | Alta | No se puede validar operación ni rentabilidad | NFR, matriz de amenazas, formulas y Q-CORE-01/03 | BLOQUEADO |
| F-018 | CAF FR-004 vs H1; INM casos borde | Reparto igual/por ítem y pago de reserva concurrente no precisan compensaciones | Alta | Cobro duplicado o saldo sin dueño | Escenarios de concurrencia; Q-CAF-01 y Q-INM-02 | BLOQUEADO |
| F-019 | INV §4 regulación SII | Regla de entrega no identifica resolución vigente | Alta | Diseño basado en norma reemplazada | E-05 Resolución 53/2025, separar entrega/emisión | CORREGIDO DOCUMENTALMENTE |
| F-020 | INV supuesto core multi-tenant cuesta lo mismo | Costo equivalente asumido sin estimación | Media | Presupuesto subestimado | Clasificar HIPÓTESIS/SUPUESTO; TCO por tenant e incidentes | CLASIFICADO / medición pendiente |

## Hallazgos de investigación adicional

| ID | Ubicación/evidencia | Impacto / severidad | Corrección / estado |
|---|---|---|---|
| F-021 | INV §3/5: ausencia universal de IA local; oferta oficial PlanOK Propeler I14 | Diferenciación y build/buy falsos / alta | Premisa retirada de derivados; evidencia de oferta comercial registrada, sin afirmar autonomía probada |
| F-022 | Página Tokko I17 accesible pero con placeholder | API supuestamente validada / alta | No usar como contrato de leads; acceso y operación siguen pendientes |
| F-023 | Confusión cancelar/devolver, recepción/acuse y cargo/entrega (H11–15) | Pérdida o doble efecto / crítica | FR hotel 018–020 y contratos/AC propuestos; política/proveedor aún bloqueantes |
| F-024 | Persona frente a vínculo propietario/portal, I16 | Exposición de datos / crítica | FR inmobiliaria 020 y pruebas de revocación/corrección, política histórica pendiente |
| F-025 | Porcentaje acumulado, recepción física/aceptada y compromiso/devengo/pago (O11–18) | Avance/stock/saldo falsos / alta | FR obra 021–023 y ejemplos matemáticos propuestos; validación contable/operativa pendiente |
