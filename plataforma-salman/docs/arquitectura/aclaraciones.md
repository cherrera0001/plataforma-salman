# Registro de decisiones y aclaraciones pendientes

Sin respuestas se mantiene BLOCKED. Las preguntas originales completas permanecen además en cada spec (CAF/HOT/INM §5). No se descartaron por agruparlas aquí. Responsable comercial general: cliente/Ricardo Salman; autoridad documental y técnica original: Cristóbal Herrera. Los cargos funcionales siguientes requieren designación nominal.

| ID | Información o decisión requerida | Responsable propuesto | Evidencia de cierre | Impacto |
|---|---|---|---|---|
| Q-CORE-01 | Empresas/RUT, locales, jerarquía tenant, roles, soporte y accesos entre empresas | Cliente + seguridad | Matriz empresa/rol/recurso/acción aprobada | Aislamiento, todas |
| Q-CORE-02 | Por contribuyente: comprobantes, anticipos, reservas, IVA aplicable, voucher, factura, proveedor DTE, pasarela y certificados | Responsable tributario + cliente | Política firmada y ejemplos aprobados | Pagos/documentos, todas |
| Q-CORE-03 | Responsable/encargado, finalidades, base legal, retención, residencia, presupuesto, RPO/RTO y límites agénticos | Cliente + privacidad + operación | Registro de tratamiento, objetivos y presupuesto | Seguridad y plan |
| Q-CAF-01 | Pago antes/después, propina voluntaria, división por ítem/igual y anulaciones | Administrador cafetería | Flujo y reglas de cuenta aprobados | H1 |
| Q-CAF-02 | Eleventa convive o se reemplaza; caja offline, doble registro y reconciliación | Cliente + caja | Procedimiento de continuidad y muestra de versión/exportación | FR-006,010 |
| Q-CAF-03 | Carta exportable, perfil persistente o sesión, recetas, proveedores y aprobadores por monto | Administrador cafetería | Muestras y matriz de compras | H1–H3 |
| Q-HOT-01 | PMS actual, datos migrables, habitaciones/tipos, temporadas y fuente de verdad | Administración hotel | Inventario y decisión build/buy/adapt | H1 |
| Q-HOT-02 | Canales, volumen y acceso contractual API/channel manager | Hotel + proveedor | Contrato, permisos, sandbox y capacidades | FR-003,005 |
| Q-HOT-03 | Cancelación, cobro anticipado, factura empresa, documentación check-in, housekeeping propio/externo y límites del agente | Hotel + legal/tributario | Políticas y roles aprobados | H1–H3 |
| Q-INM-01 | Proyectos/unidades/etapas, CRM/planillas, migración y canales/portales autorizados | Jefatura comercial | Inventario y muestras minimizadas | H1 |
| Q-INM-02 | Reserva obligatoria online o transferencia, expiración, bloqueo, pago duplicado y reembolso | Comercial + finanzas | Máquina de estados y política | FR-003,005 |
| Q-INM-03 | Redactor/aprobador legal, plazo a promesa, tipo de firma, formalidades y proveedor API | Abogado + cliente | Modelo aprobado y verificación proveedor | FR-006 |
| Q-INM-04 | Garantías por falla, responsables y plazos; clasificación provisional vs decisión vinculante | Postventa + legal | Catálogo y SLA ratificado | H2 |
| Q-OBR-01 | Obras propias/terceros, presupuesto digital y supuesto módulo existente de inspección | Jefatura de obra | Alcance, presupuesto y entrega del módulo o exclusión explícita | 004 completo |
| Q-OBR-02 | Avance físico/costo, denominador, 10 % relativo vs puntos porcentuales y programación | Control de obra | Regla matemática con ejemplos | FR-011 |
| Q-OBR-03 | Compras, proveedores, responsables, límites, aprobación por WhatsApp autenticada y seguridad de inspecciones | Administrador obra + prevención | Política aprobada y matriz de rol | FR-012,016–018 |
| Q-TOOL-01 | Entorno con red e instalación de Spec Kit v1.2.0, integración y feature activa | Mantenedor técnico | CLI y comandos oficiales verificados | Validación operativa SDD |
| Q-GOV-01 | Ratificar ampliaciones de constitución y seis principios | Cristóbal Herrera | Versión, aprobación y nota de migración | Gate compartido |

Recomendación: resolver primero Q-CORE-01/02, Q-CAF-01/02, Q-HOT-01/02 y Q-INM-02/03. Sin ellos no se puede convertir planes en compromisos de desarrollo. Se puede continuar investigación y revisión documental sin aprobar funcionalidades.

## Extensión por investigación de otras verticales

El [registro competitivo de decisiones](../investigacion-competitiva/decisiones-pendientes.md) agrega Q-HOT-04/05/06 (cambios/extras/canales), Q-INM-05/06/07 (agenda/firma/vínculo), Q-OBR-04/05/06 (subcontratos-consultas/partes/recepción-presupuesto) y Q-CORE-04 (efectos de herramientas). Amplían las preguntas originales; no sustituyen sus responsables ni proporcionan respuestas automáticas. Siguen pendientes de ratificación y evidencia operativa.
