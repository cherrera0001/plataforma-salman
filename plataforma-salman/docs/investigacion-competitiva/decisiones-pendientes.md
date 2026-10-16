# Decisiones pendientes tras investigación

Los Q anteriores permanecen abiertos. Evidencia de competidor no aprueba políticas del cliente ni levanta estado BLOCKED.

| ID nuevo / vínculo previo | Decisión | Alternativas y recomendación | Evidencia faltante / cierre |
|---|---|---|---|
| Q-REA-01 / Q-TOOL-01 | Entorno de ejecución y runtime REA | Clon completado en `investigacion-herramientas/rea/` (commit `4838f444939677107902549c59b73439e14d3ae9`, tag `rea-agents-6.5.0`). Runtime actual Node 18.19.1 no cumple motor requerido (Node >= 22.19.0). Actualizar Node requiere aprobación. | Evaluación de actualización global a Node 22+ y autorización del usuario. |
| Q-REA-02 | Objetivo permitido y navegador | Demo autorizada o componente propio, CDP local y perfil separado; no cuenta ajena | Autorización del target, navegador y caso sin efectos reales |
| Q-REA-03 | Registro global MCP/skill | Evaluar plan oficial `npx rea-agents setup`; solicitar aprobación del usuario antes de efectuar cambios globales en el sistema. | Aprobación explícita del usuario previa a modificación global de MCP/skills. |
| Q-COMP-01 / Q-CAF-01 | Reparto/redondeo, descuentos, propina y partes pagadas | Regla visible y consistente; destino de residuo configurable y ratificado; nunca alterar pagos previos | Ejemplos negocio y política tributaria |
| Q-COMP-02 / Q-HOT-01/02 | Cupo por fecha/tipo vs asignación y fuente vigente | Mantener dimensiones separadas; detener compromiso sin evidencia suficiente | Inventario real, SLA/plan de conector, criterio de frescura y asignación |
| Q-COMP-03 / Q-INM-01/02/03 | Identidad/calificación/hitos/transferencia | No fusionar identidad ambigua ni equiparar reserva a promesa; handoff con aceptación | Políticas de canal, consentimiento, agenda y firma |
| Q-COMP-04 / Q-OBR-02/03 | Observación, cierre y recepción parcial | Roles distintos para solucionar/aceptar; cantidades y evidencia por línea; fallback manual | Roles y ejemplos de órdenes/inspecciones reales |
| Q-COMP-05 / Q-CORE-03 | Medición y priorización | Usar intervalos por frecuencia e impacto desconocidos; contrastar usuarios | Datos de demanda, tiempo, errores, costo y disposición a pagar |
| Q-URL-01 | Aplicabilidad territorial y por plan | URL efectiva Fudo Chile y validación identidad para cada candidata; no adivinar rutas regionales | Confirmar funciones por cuenta/canal; Tokko Chile no validado, manuales US/L-Series solo patrones |

Constitución revisada: no se modifica ni cambia versión. Nuevos comportamientos son desarrollos de principios existentes, ratificación anterior Q-GOV-01 permanece pendiente. ADR-005 tampoco es decisión aprobada.

## Aclaraciones adicionales de otras verticales

| ID | Regla por ratificar | Responsable / evidencia de cierre |
|---|---|---|
| Q-HOT-04 | Cambios de fecha/categoría/tarifa, penalidad, saldo y devolución; fuente de verdad y aceptación | Hotel + finanzas/tributario; ejemplos y transición aprobada |
| Q-HOT-05 | Extras por persona/noche/estadía, destino del cargo, cumplimiento y relación entre empresas | Hotel/cafetería/contabilidad; matriz servicio-regla-cuenta-contribuyente |
| Q-HOT-06 | Acuse por canal, mapeos, persistencia/recuperación y manejo de conflicto | Responsable de integración/proveedor; contrato real de operación y casos sandbox |
| Q-INM-05 | Modo de agenda, duración/zona, conflicto, cambio y cancelación | Comercial; flujo confirmado con calendario o confirmación humana |
| Q-INM-06 | Participantes, plantilla/huella, formalidades y evidencia por firma; moneda/UF si aplica | Legal/finanzas; modelo ratificado y ejemplos sin suponer valor UF actual |
| Q-INM-07 | Corrección Persona vs VínculoUnidad/acceso; revocación corriente y acceso histórico | Comercial/postventa + privacidad; matriz de permisos y procedimiento |
| Q-OBR-04 | Alcance de subcontratos y consultas técnicas/RFI | Jefatura/cliente/legal; incluir/excluir y riesgos, sin activar módulos por investigar |
| Q-OBR-05 | Partes por turno/autor, unidades, incrementos/acumulados, corte y revisión | Control obra; ejemplos de cómputo y rectificación |
| Q-OBR-06 | Recepción/rechazo/devolución/reposición; compromiso/devengo/pago y regla presupuestaria | Bodega/compras/contabilidad; cantidades y fórmulas aprobadas |
| Q-CORE-04 | Efectos laterales por herramienta/parámetro; quién autoriza mensajes/cargos y cómo se deduplican | Seguridad + integración + negocio; perfil de operación real y prueba negativa |

Estos Q amplían los existentes; no sustituyen Q-CORE-01/02/03 ni el inventario operativo pendiente. El cambio de acceso de portal no autoriza transferencia jurídica de inmueble. Hallazgos de proveedores no fijan política tributaria, plazos de garantía ni datos obligatorios del cliente.
