# Informe de investigación competitiva y enriquecimiento SDD

**Resultado:** cada vertical tiene revisión documental competitiva trazable y cambios concretos en sus especificaciones. Se conservan 13 historias originales, enriquecidas con 26 criterios específicos; se añaden diez FR (66 en total) y NFR-006. **La misión REA dinámica sigue parcial/BLOCKED**: clonación y análisis no ejecutables por red/entorno. No hay implementación, pruebas de producto ni validación comercial de las propuestas.

## Plataformas y evidencia real

Se revisaron fuentes primarias de las 33 candidatas: cafetería (8: Toteat, Fudo, Justo, Bsale, Toast, Square for Restaurants, Lightspeed Restaurant, Eleventa); hotel (9: Mews, Cloudbeds, SiteMinder, Little Hotelier, OPERA Cloud, HiJiffy, Asksuite, Duve, Canary); inmobiliaria (9: MobySuite, PlanOK, TOCTOC, Wasi, TokkoBroker, HubSpot Breeze, Agentforce, Lofty, Structurely); constructora (7: Procore, Autodesk Construction Cloud, OpenSpace, ALICE, iConstruye, ObraLink, Kojo).

Las 42 fichas de evidencia incluyen fuentes complementarias de inventario, agentes, canales y permisos. La profundidad es diferente: manual/API permite reconstruir reglas; página de producto solo acredita declaración. La lectura no verifica cada área funcional de cada candidata. [Inventario](inventario-plataformas.md), [matriz comparativa](matriz-comparativa.md), [evidencias](matriz-evidencias.md) y [URLs efectivas](urls-verificadas.md) detallan alcance y límites por plataforma.

Fudo Chile: referencia efectiva aportada por el usuario https://fu.do/es-cl/, con enlaces de gestión/soporte abiertos. No se usa empresa homónima ni se presume que un manual de otra región habilita una función en Chile. Tokko raíz redirige a `/es-ar/`; no se validó una ruta chilena. Lofty I08 muestra actualmente Cowork; se corrigió la descripción indexada anterior. Fudo C02 histórico y Kojo O08 tienen contenido oficial indexado pero su apertura directa falló; se conservan con esa advertencia.

No accesibles para análisis de aplicación: cuentas privadas de todas las candidatas, por ausencia de credenciales/demo autorizada y navegador REA. No se inició prueba gratis, llamada, envío WhatsApp, reserva, pago ni contrato. No hay capturas/ HAR/contratos inferidos de tráfico ni código propietario descargado.

## Diferencias concretas frente a la línea base

| Flujo | Ambigüedad anterior | Comportamiento añadido y prueba |
|---|---|---|
| Core | Permiso de integración general, eventos desconocidos sin detalle | Perfil por cuenta/tenant/plan/país y revisión; evento antiguo no retrocede resultado conciliado. AT de capacidad no habilitada y duplicado/desorden. |
| Cafetería H1 | Dividir por ítem/igual sin precisar residuos, descuentos o cuenta ya pagada | Partes liquidada/pending separadas; redondeo ratificado visible; ejemplo 10000 CLP/3 conserva total; redistribuir no reenvía cocina. |
| Cafetería H2/H3 | Costo ausente podía mostrarse “sin costo”; alertas sin identidad de detección | Costo desconocido no cuenta como cero; lote/receta y detección con procedencia/ventana, deduplicación y revisión. |
| Hotel H1/H2 | Limpieza podía retirar disponibilidad futura; 001 seguía como dependencia total en §5 | Cupo por fecha/tipo separado de habitación asignada y preparación; habitación sucia hoy no bloquea por sí sola venta futura, mantenimiento sí bloquea check-in. |
| Hotel H3 | Derivar atención podía contarse como cerrar; oferta sin vigencia explícita | Transferencia pendiente/aceptada/en atención, contexto mínimo y responsable; fuente incierta no confirma cupo ni transacción. |
| Inmobiliaria H1 | Fusión multicanal automática y hitos poco separados; datos de cliente exigidos en tiempo de respuesta | Identidad dudosa se revisa; primera respuesta no garantiza que el cliente dé presupuesto; cita propuesta, cotización, reserva y promesa requieren evidencia diferente. |
| Inmobiliaria H2 | Clasificación/asignación y resolución no distinguían recepción humana | Transferencia no aceptada sigue pendiente; sin rechazo autónomo de garantía y sin divulgar deuda a destino no revalidado. |
| Obra H3/H4 | Inspección sin observación/cierre diferenciados; recepción sin parcialidad explícita | Reportar, proponer solución y aceptar cierre son permisos/estados distintos; recibir 6 de 10 deja 4 pendientes y un reintento no recibe 12; IA deshabilitada conserva captura manual. |

Los IDs H/FR/SC previos permanecen. Los alias US-CORE-001–003, US-CAF-001–003, US-HOT-001–003, US-INM-001–002 y US-OBR-003–004 vinculan historias y pruebas. [Historias completas](historias-propuestas.md) incluyen actor, necesidad, disparador, prioridad, precondiciones, flujos, reglas, datos, riesgos, dependencia, aceptación y métricas.

Nuevas historias candidatas: US-HOT-004 (comparar tarifas) y US-OBR-005 (escenarios de programación), ambas P3 para investigar, **fuera de specs/FR activos**. No se construye autopricing, optimizador, contabilidad universal ni plataforma de sensores por aparecer en la competencia.

## Propagación y decisiones

Los nueve artefactos de cada feature se actualizaron: spec, research, plan, data-model, acceptance, contracts/README, quickstart, tasks y checklist. Los contratos siguen lógicos; no se inventaron endpoints propios ni atribuidos a terceros. ADR-005 documenta estados, procedencia y alcance de conectores, sin elegir infraestructura ni proveedor. Core mantiene controles comunes; cada negocio posee sus estados/datos. No se añaden dependencias obligatorias o circulares entre verticales.

Constitución sin cambios, comprobada contra hash de línea base. Sus principios ya cubren evidencia, aislamiento, mínimo privilegio, autonomía, recuperación y pruebas. Las ampliaciones previas aún requieren su ratificación original.

La [priorización](oportunidades.md) usa nueve criterios ponderados y sensibilidad, con frecuencia/impacto comercial desconocidos. No se infieren demanda, ahorro o ROI desde un competidor. [Agentes](agentes.md) distingue respuesta, asistencia, ejecución declarada, transacción y autonomía no probada; conserva ocho políticas propias y compromiso monetario autónomo inicial cero.

## REA y Spec Kit: uso y límites comprobados

Herramientas utilizadas: shell/Python/Git para lectura, baseline, hashes, diffs y controles locales; navegación/búsqueda web para fuentes públicas. **Herramientas REA ejecutadas: ninguna.** `gh repo clone` falló inicialmente por autenticación; después del token indicado por el usuario falló conectividad a api.github.com; Git directo falló por DNS. El token no figura en archivos ni salidas. No hay checkout completo ni cambios globales de MCP/skills.

Versión documental REA revisada: 6.5.0, commit oficial `3b79af28e80785afce9f5998d8f03289402a1847`; no es versión instalada/ejecutada. [Disponibilidad y continuación](rea.md). Node cumple rango general, pero faltan paquete/conexión y navegador; el uso dinámico no se declara completado. Setup global requiere plan exacto revisable y aprobación del usuario antes de aplicarlo, aún no obtenible por red.

Spec Kit sigue ausente. La referencia previa v1.2.0 orienta los artefactos; no se ejecutaron comandos de agente/CLI ni se declara `/speckit.analyze` realizado. Las validaciones siguientes son propias y no sustituyen validación oficial.

## Validaciones reproducibles y estado

Desde la raíz de plataforma-salman:

```bash
python3 scripts/validar_documentacion.py
python3 scripts/validar_investigacion.py
```

Resultados exactos por comprobación: [documentación activa](../auditorias/validacion-local.json) e [investigación](validacion.json). Se comprueban hashes originales/baseline, IDs, alias, evidencias resolubles, AC propagados, alcance de cambios, enlaces locales, única constitución activa, catálogo y grafo propuesto. No prueba interfaz, exactitud del agente, API ni comportamiento de producto.

Revisión en dos ciclos: detección/enriquecimiento; revalidación de URLs, corrección semántica y controles. [Registro antes/después](registro-cambios.md), [diff Git real](cambios.patch), [archivos previos modificados](cambios.json) y [archivos de entrega](archivos-entrega.txt). La línea base preserva los 51 archivos previos; se excluye de las reglas de documentos activos para no confundir copias históricas con constituciones/features nuevas.

Las cinco features permanecen **BLOCKED para implementación**. Q comerciales/fiscales/privacidad/PMS/OTA/firma/presupuesto siguen abiertos; Q-REA-01/02/03 y Q-COMP/Q-URL detallan lo adicional en [decisiones pendientes](decisiones-pendientes.md). Definiciones más precisas permiten revisar mejor esas decisiones; no las reemplazan. Reanudar análisis dinámico y ratificación cuando haya entorno/objetivo autorizado y datos del cliente.
