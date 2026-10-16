# Trazabilidad fuente → requisito → prueba

Namespace estable: `<feature>/<ID>`. FR y SC repetidos entre documentos no se fusionan. Tests propuestos en cada acceptance.md, no ejecutados. CAF/HOT/INM remiten a inventario; ENCARGO es la instrucción de auditoría del cliente.

| Feature | Requisito | Fuente | Historia | Prueba propuesta |
|---|---|---|---|---|
| 000-core | FR-001 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H1 | AT-001 |
| 000-core | FR-002 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H1 | AT-002 |
| 000-core | FR-003 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H2 | AT-003 |
| 000-core | FR-004 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H2 | AT-004 |
| 000-core | FR-005 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H3 | AT-005 |
| 000-core | FR-006 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H1 | AT-006 |
| 000-core | FR-007 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H3 | AT-007 |
| 000-core | FR-008 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H2 | AT-008 |
| 000-core | FR-009 | ENCARGO §4/6/9; CAF §1; HOT/INM §3 | H3 | AT-009 |
| 001-cafeteria-mesas-pos | FR-001 | CAF §3 | H1 | AT-001 |
| 001-cafeteria-mesas-pos | FR-002 | CAF §3 | H1 | AT-002 |
| 001-cafeteria-mesas-pos | FR-003 | CAF §3 | H1 | AT-003 |
| 001-cafeteria-mesas-pos | FR-004 | CAF §3 | H1 | AT-004 |
| 001-cafeteria-mesas-pos | FR-005 | CAF §3 | H1 | AT-005 |
| 001-cafeteria-mesas-pos | FR-006 | CAF §3 | H1 | AT-006 |
| 001-cafeteria-mesas-pos | FR-007 | CAF §3 | H2 | AT-007 |
| 001-cafeteria-mesas-pos | FR-008 | CAF §3 | H2 | AT-008 |
| 001-cafeteria-mesas-pos | FR-009 | CAF §3 | H2 | AT-009 |
| 001-cafeteria-mesas-pos | FR-010 | CAF §3 | H2 | AT-010 |
| 001-cafeteria-mesas-pos | FR-011 | CAF §3 | H3 | AT-011 |
| 001-cafeteria-mesas-pos | FR-012 | CAF §3 | H3 | AT-012 |
| 001-cafeteria-mesas-pos | FR-013 | CAF §3 | H3 | AT-013 |
| 001-cafeteria-mesas-pos | FR-014 | CAF §3 | Todas | AT-014 |
| 002-hotel-reservas-concierge | FR-001 | HOT §3 | H1 | AT-001 |
| 002-hotel-reservas-concierge | FR-002 | HOT §3 | H1 | AT-002 |
| 002-hotel-reservas-concierge | FR-003 | HOT §3 | H1 | AT-003 |
| 002-hotel-reservas-concierge | FR-004 | HOT §3 | H1 | AT-004 |
| 002-hotel-reservas-concierge | FR-005 | HOT §3 | H1 | AT-005 |
| 002-hotel-reservas-concierge | FR-006 | HOT §3 | H2 | AT-006 |
| 002-hotel-reservas-concierge | FR-007 | HOT §3 | H2 | AT-007 |
| 002-hotel-reservas-concierge | FR-008 | HOT §3 | H2 | AT-008 |
| 002-hotel-reservas-concierge | FR-009 | HOT §3 | H2 | AT-009 |
| 002-hotel-reservas-concierge | FR-010 | HOT §3 | H3 | AT-010 |
| 002-hotel-reservas-concierge | FR-011 | HOT §3 | H3 | AT-011 |
| 002-hotel-reservas-concierge | FR-012 | HOT §3 | H3 | AT-012 |
| 002-hotel-reservas-concierge | FR-013 | HOT §3 | H3 | AT-013 |
| 002-hotel-reservas-concierge | FR-014 | HOT §3 | H3 | AT-014 |
| 002-hotel-reservas-concierge | FR-015 | HOT §3 | Todas | AT-015 |
| 003-inmobiliaria-comercial | FR-001 | INM §3 | H1 | AT-001 |
| 003-inmobiliaria-comercial | FR-002 | INM §3 | H1 | AT-002 |
| 003-inmobiliaria-comercial | FR-003 | INM §3 | H1 | AT-003 |
| 003-inmobiliaria-comercial | FR-004 | INM §3 | H1 | AT-004 |
| 003-inmobiliaria-comercial | FR-005 | INM §3 | H1 | AT-005 |
| 003-inmobiliaria-comercial | FR-006 | INM §3 | H1 | AT-006 |
| 003-inmobiliaria-comercial | FR-007 | INM §3 | H2 | AT-007 |
| 003-inmobiliaria-comercial | FR-008 | INM §3 | H2 | AT-008 |
| 003-inmobiliaria-comercial | FR-009 | INM §3 | H2 | AT-009 |
| 003-inmobiliaria-comercial | FR-013 | INM §3 | Todas | AT-010 |
| 003-inmobiliaria-comercial | FR-014 | INM §3 | Todas | AT-011 |
| 004-constructora-obra | FR-010 | INM §3 | H3 | AT-001 |
| 004-constructora-obra | FR-011 | INM §3 | H3 | AT-002 |
| 004-constructora-obra | FR-012 | INM §3 | H3 | AT-003 |
| 004-constructora-obra | FR-015 | ENCARGO §4/9; propuesta nueva | H4 | AT-004 |
| 004-constructora-obra | FR-016 | ENCARGO §4/9; propuesta nueva | H4 | AT-005 |
| 004-constructora-obra | FR-017 | ENCARGO §4/9; propuesta nueva | H4 | AT-006 |
| 004-constructora-obra | FR-018 | ENCARGO §4/9; propuesta nueva | H4 | AT-007 |

## Equivalencias y correcciones

| Fuente | Destino | Cambio |
|---|---|---|
| CAF FR-001–014, SC-001–008, H1–H3 | 001 mismos IDs | Matiz fiscal y core reducido; objetivos sin mediciones |
| HOT FR-001–015, SC-001–009, H1–H3 | 002 mismos IDs | PMS propio pasa a sistema de registro por decidir; room service opcional |
| INM FR-001–009, FR-013–014; SC-001–007,009; H1–H2 | 003 mismos IDs | Se retira obra; firma, fiscalidad y devolución quedan bloqueadas |
| INM H3, FR-010–012, SC-008 | 004 mismos IDs | Traslado único; no duplicación de implementación |
| INM FR-013–014 y SC-009 transversales | 004 FR-018; SC-010–011 nuevos | Ampliación de seguridad según encargo; no se atribuye a fuente original |
| ENCARGO §4 y §9 | 004 H4, FR-015–018 | Requisitos nuevos propuestos de presupuesto, inspección, materiales y permisos |
| CAF §1 y encargo | 000 H1–H3, FR-001–009, SC-001–003 | Core extraído y reducido, no existía spec de core |

Los SC conservados se verifican individualmente en cada acceptance.md. NFR-001 a NFR-005 derivan del encargo §6/9/10 y se cubren con ADV, revisión legal y medición operativa. La independencia de H2/H3 es comprobable con datos/adaptadores; no implica ausencia de dependencias fundacionales.

## Ajustes semánticos conservando identificadores

CAF FR-005/010/013 y SC-003; HOT FR-004/007/013 y SC-004; INM FR-013: se conserva ID pero se corrige interpretación de documento aplicable, exportación con cobertura comprobable, ubicación de pedidos e integridad de auditoría. Los umbrales 30/60 s quedan como objetivos condicionados para ratificar, no garantía universal. Los textos originales exactos son comparables en cambios-*.diff y docs/originales. No son cambios comerciales aprobados.

## Fuente → criterio de éxito → medición propuesta

| Feature | Criterio | Fuente | Evidencia prevista |
|---|---|---|---|
| 000-core | SC-001 | Encargo §6/9; propuesta nueva | 000-core/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 000-core | SC-002 | Encargo §6/9; propuesta nueva | 000-core/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 000-core | SC-003 | Encargo §6/9; propuesta nueva | 000-core/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-001 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-002 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-003 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-004 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-005 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-006 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-007 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 001-cafeteria-mesas-pos | SC-008 | CAF §4 | 001-cafeteria-mesas-pos/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-001 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-002 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-003 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-004 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-005 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-006 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-007 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-008 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 002-hotel-reservas-concierge | SC-009 | HOT §4 | 002-hotel-reservas-concierge/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-001 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-002 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-003 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-004 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-005 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-006 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-007 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 003-inmobiliaria-comercial | SC-009 | INM §4 | 003-inmobiliaria-comercial/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 004-constructora-obra | SC-008 | INM §4 SC-008 + encargo §9/10 | 004-constructora-obra/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 004-constructora-obra | SC-010 | INM §4 SC-008 + encargo §9/10 | 004-constructora-obra/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
| 004-constructora-obra | SC-011 | INM §4 SC-008 + encargo §9/10 | 004-constructora-obra/acceptance.md y docs/arquitectura/economia.md; medición pendiente |
