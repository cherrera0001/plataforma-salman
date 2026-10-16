# Auditoría individual — CAF

Análisis del documento de entrada antes de integración. Fecha: 2026-10-16. Fuente conservada en inventario. No se presume aprobación del texto original.

| Dimensión | Ubicación | Evaluación y clasificación | Tratamiento |
|---|---|---|---|
| Problema y objetivos | §2 H1–3 | Problema propuesto de mesas/datos; dolor cuantitativo no medido | Ratificar operación y línea base |
| Usuarios y responsabilidades | §2 y §5 | Cliente/cocina/admin identificados; aprobadores abiertos | Q-CAF-03 y Q-CORE-01 |
| Alcance y exclusiones | §5 | Un local/30 mesas/sin delivery son SUPUESTOS; Eleventa ambiguo | Q-CAF-02 |
| Historias y aceptación | §2 | Historias priorizadas y escenarios; división/offline incompletos | AT y ADV concretos, F-018 |
| FR y reglas de negocio | §3 | 14 FR preservados; fiscalidad y core requieren matices | F-001/002 |
| NFR y recuperación | §2/6 | Latencias propuestas; caja degradada sin diseño de persistencia | F-012 y objetivos recuperación pendientes |
| Datos conceptuales | §3 entidades | Modelo inicial útil; saldo, versiones y pertenencia ausentes | data-model.md |
| Integraciones y dependencias | §5/6 | Carta, Eleventa, Webpay, SII y WhatsApp; sin muestras/contratos | Q-CAF-02/03 y E-04/07/08/11 |
| Legal y regulación | §1.2/4 | Boleta por pago y Ley 21.719 sin calendario | F-002/010/019 |
| Seguridad y multi-tenancy | §1.4 y plan | Modelo de amenazas pendiente, aislamiento no operativo | NFR, seguridad y ADV |
| Arquitectura y tecnología | §6 | Stack propuesto antes de investigación; core grande | ADR-001/003 |
| Agentes y autonomía | H3 §2; §1.3 | Solo propone compras, requiere humano; identidad WhatsApp no definida | Política reposición y anomalías |
| KPI y éxito | §4 | Ocho SC propuestos; sin baseline, SII 100 % incompatible con caída | F-013 y economia.md |
| Riesgos, vacíos y supuestos | §5 | Seis preguntas conservadas; migración no demostrada | Registro de aclaraciones |

Las afirmaciones individuales tienen evidencia literal y localización en afirmaciones.md. La severidad, impacto, propuesta y estado de los defectos materiales se registran por separado en hallazgos.md. Documento procesado completamente; validación externa parcial y decisiones pendientes explícitas.
