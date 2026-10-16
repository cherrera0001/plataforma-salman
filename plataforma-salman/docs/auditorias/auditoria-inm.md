# Auditoría individual — INM

Análisis del documento de entrada antes de integración. Fecha: 2026-10-16. Fuente conservada en inventario. No se presume aprobación del texto original.

| Dimensión | Ubicación | Evaluación y clasificación | Tratamiento |
|---|---|---|---|
| Problema y objetivos | §2 H1/H2 | Dato fragmentado y ciclo comercial propuestos; competencia absoluta no probada | Eliminar claims universales del alcance |
| Usuarios y responsabilidades | §2/5 | Ejecutivo/cliente/postventa/jefe obra; abogado por definir | Q-INM-03/04 |
| Alcance y exclusiones | §0/5 | Comercial V1, obra V2 pero H3 en comercial | F-007 separar 004 |
| Historias y aceptación | §2 | Dos historias comerciales y H3 obra; firma y devolución requieren reglas | AT, equivalencia H3 conservada |
| FR y reglas de negocio | §3 | 14 FR fuente; 010–012 trasladados sin renumerar | Trazabilidad y catálogo |
| NFR y recuperación | §6 | Tiempos/escala propuestos, no retención ni recuperación | NFR y Q-CORE-03 |
| Datos conceptuales | §3 entidades | Unidad/proyecto mezclan estado comercial/obra; duplicados persona abiertos | Correspondencia opcional y no fusión ciega |
| Integraciones y dependencias | §5/6 | Portales, firma, calendario, pagos; acceso no demostrado | Q-INM-01/03 |
| Legal y regulación | §2/5 | Ley 19.799 citada no valida promesa ni tipo de firma automáticamente | Revisión abogado y proveedor |
| Seguridad y multi-tenancy | §5/6 | Datos financieros y compradores, empresas grupo sin reglas de acceso | Aislamiento y finalidad explícitos |
| Arquitectura y tecnología | §6 | Stack candidato; cuatro agentes no justifican cuatro servicios | ADR-003 y Complexity Tracking |
| Agentes y autonomía | §2 H1–3; §6 | Califica/cobra/clasifica; garantía no se rechaza sola y compra se aprueba | Políticas por agente; no enviar automáticamente al inicio |
| KPI y éxito | §4 | Nueve objetivos, SC-008 a obra; plazos/porcentajes sin línea base | Economía y pruebas por SC |
| Riesgos, vacíos y supuestos | §5 | Siete preguntas; módulo de obra previo no entregado | Bloqueos por comercial y obra, sin fingir preexistencia |

Las afirmaciones individuales tienen evidencia literal y localización en afirmaciones.md. La severidad, impacto, propuesta y estado de los defectos materiales se registran por separado en hallazgos.md. Documento procesado completamente; validación externa parcial y decisiones pendientes explícitas.
