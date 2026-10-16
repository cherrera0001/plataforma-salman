Estado del arte: IA agéntica en hotel, inmobiliaria y cafetería (oct 2026)
Oct 15, 2026 · @Cristóbal Herrera
Investigación comercial de base para los tres proyectos proyectados con Ricardo Salman: qué hace hoy la industria con agentes de IA en cada línea de negocio y dónde hay espacio para C4A.
1. Supuestos de partida
Se asumen como dadas las preguntas generales; si alguna falla, cambia el alcance, no la investigación.
Los tres negocios son del mismo grupo (Ricardo Salman); el core se diseña multi-tenant desde el inicio porque cuesta lo mismo y abre venta a terceros.
Eleventa convive en V1 de la cafetería; se migra cuando la plataforma demuestre valor.
Inmobiliaria parte por el lado comercial (venta); control de obra queda para V2.
Hotel es de escala pequeña o mediana (menos de 50 habitaciones) y hoy usa canales OTA sin channel manager propio.
Facturación electrónica SII y pago con Webpay son requisito en todas las verticales desde V1.
El canal preferente de atención al cliente final en Chile es WhatsApp.
2. Hotel: la IA ya ejecuta, pero con autonomía acotada
Más de la mitad de los hoteles usa IA generativa, pero menos del 10 % reporta una baja del trabajo manual superior al 30 % (State of Distribution 2026, 58.000 propiedades). La capa madura es el concierge por WhatsApp; la capa inmadura es el agente que decide tarifas o cobra solo.
Cómo lo hace la industria hoy
PMS y motores de reserva: Mews levantó USD 300 M (enero 2026) para «operar hoteles con IA»; lo concreto es un agente de rooming lists en beta. Cloudbeds lanzó un RMS con Autopilot que mueve tarifas dentro de límites. Oracle OPERA Cloud recomienda y redacta, pero no ejecuta.
Distribución vía agentes: SiteMinder abrió su inventario por MCP para que ChatGPT/Claude coticen y deriven a reserva directa (abril 2026). Expedia y Booking ya tienen apps dentro de ChatGPT.
Concierge por WhatsApp (lo más maduro): HiJiffy resuelve más del 80 % de consultas y escribe cambios en el PMS; Asksuite (fuerte en LatAm) reporta casos en Paraguay, Colombia y Uruguay recuperando cotizaciones abandonadas; Duve AI responde en modo autónomo y vende upsells con link de pago; Canary suma agentes de voz para recepción y reservas.
Check-in digital y upselling: Duve y Canary automatizan registro, ID y pago previo; Duve declara +20 % de ingresos por upsell (cifra de proveedor).
Lo que nadie documenta: cancelaciones ni cobros autónomos. El cobro se delega a links de pago y la reserva final se cierra en el motor del hotel.
Solución
Qué hace agénticamente
Segmento / precio
Mews
Agente de rooming lists (beta); visión de agentes revenue/ops/guest
Mid-upscale; sin precio público
Cloudbeds Signals + RMS
Consulta conversacional; Autopilot de tarifas con límites
Independientes
SiteMinder / Little Hotelier
Inventario vivo vía MCP; derivación a reserva directa
Pequeños y medianos
HiJiffy (Aplysia)
Reserva guiada, check-in, upsell, cambios en PMS por WhatsApp/IG
USD 4-8 por habitación al mes (reseñas)
Asksuite
Cotiza y recupera reservas por WhatsApp; modifica en PMS
Desde USD 349/mes
Duve AI
Respuesta autónoma, upsell con link de pago, check-in online
Hoteles y apart-hotel
Aurora Inbox
WhatsApp: disponibilidad, reserva, link de pago, check-in
USD 130-380/mes (LatAm)
Climber RMS
Pricing dinámico automático opcional sobre Cloudbeds
Boutique e independientes
Brechas para un hotel chico (oportunidad)
Sin integración PMS bidireccional el agente solo informa; los PMS baratos tienen APIs limitadas.
Nadie resuelve cobro agéntico en pesos chilenos (Webpay, Transbank, boleta SII) ni hay bundle local; Newhotel es lo único con presencia en el Congreso de Hoteleros de Chile y solo anuncia un asistente.
Las reglas de autonomía (límites de tarifa, escalamiento) siguen siendo manuales; el 29 % de los hoteles pequeños aún tiene tarifa estática (SiteMinder).
La distribución por MCP favorece OTAs y conectores grandes; el independiente depende de su vendor.




3. Inmobiliaria y constructora: el agente global cobra por resultado; el proveedor chileno aún no tiene agente
El salto 2025-2026 fue de chatbot a agente que ejecuta y cobra por outcome: HubSpot Breeze cobra USD 0,50 por conversación resuelta y USD 1 por lead; Salesforce Agentforce USD 2 por conversación. En Chile, los CRM inmobiliarios y las plataformas de preventa a postventa no traen agente nativo; la capa agéntica llega por terceros.
Cómo lo hace la industria hoy
CRM y leads (EE. UU.): Structurely, Ylopo, Lofty y BoldTrail operan como ISA virtuales (llaman, textean, agendan, transfieren en vivo) por USD 300-1.000/mes (rework). Follow Up Boss solo redacta.
CRM y leads (LatAm/Chile): Wasi (USD 30/usuario/mes, 22 países) y TokkoBroker siguen siendo CRM de inventario y portales; el agente se agrega con Dapta (califica y agenda por WhatsApp) o Whippy. En Chile lo visible es Bitrix24: clasificador caliente/tibio/frío, respuesta fuera de horario, recordatorios de visita, transcripción de llamadas.
Preventa a postventa (Chile): MobySuite (más de 100 inmobiliarias) cubre reserva, cobranza, escrituración y postventa sin IA publicada; PlanOK contrató en 2025 para construir agentes LLM; TOCTOC firma reservas y promesas electrónicamente desde 2020. Ningún agente chileno gestiona postventa de forma autónoma.
Control de obra: Procore Digital Coworker (julio 2026) vende paquetes de 5/20/25+ agentes que revisan submittals, RFIs, daily logs y contratos con triggers; Autodesk apuesta por asistente + MCP; OpenSpace Field autolocaliza observaciones y llena formularios por voz; ALICE re-secuencia cronogramas (Suffolk ahorró 42 días). En Chile, ObraLink y Foco en Obra no publican agentes.
Compras: Kojo (600+ contratistas) usa agentes para seguir distribuidores y entregas; iConstruye mostró en julio 2026 cotización y compra con agentes para constructoras chilenas.
Adopción: el 38 % de contratistas comerciales reporta impacto medible de IA, el doble que en 2025 (ServiceTitan); los brokerages pequeños (10 agentes o menos) son los más rezagados (Real Estate News).
Solución
Qué hace agénticamente
Segmento / precio
HubSpot Breeze
Resuelve conversaciones, recomienda leads
USD 0,50 por resolución, USD 1 por lead
Salesforce Agentforce
Califica, agenda visitas, redacta documentos
Enterprise; USD 2 por conversación
Structurely / Lofty / Ylopo
ISA virtual: llama, textea, agenda, transfiere
Brokerages EE. UU.; USD 300-1.000/mes
Dapta
Califica y agenda por WhatsApp; sincroniza CRM
PyME LatAm
Wasi
CRM + portales; sin agente nativo
USD 30 por usuario al mes
Bitrix24 (Chile)
Clasifica leads, recuerda visitas, transcribe
PyME
MobySuite / PlanOK
Preventa a postventa; agentes en desarrollo
Inmobiliarias Chile y LatAm
Procore Digital Coworker
Revisa submittals, RFIs, contratos; triggers
Mid y enterprise; cotizar
OpenSpace Field
Autolocaliza issues; voz a formulario
Incluido en Core/Enterprise
ALICE
Re-secuencia cronogramas
Enterprise
iConstruye
Cotización y compra con agentes (demo 2026)
Constructoras Chile
Brechas para una inmobiliaria + constructora chilena mediana (oportunidad)
Ningún CRM LatAm trae agente nativo de WhatsApp: siempre hay que integrar una capa externa.
Cotización y promesa siguen siendo manuales; la firma electrónica existe pero no está orquestada por agentes.
Postventa sin IA en todos los proveedores locales.
Procore y ALICE están dimensionados para enterprise y sin precio público; la constructora mediana queda fuera.
Datos fragmentados (Excel, WhatsApp, portales) impiden que un agente actúe con permisos claros: el primer entregable es el modelo de datos, no el agente.









4. Cafetería y POS: nadie en Chile cierra el ciclo agéntico completo
En EE. UU. el POS ya es plataforma de agentes (Toast IQ vende agentes de marketing, reseñas, turnos y voz desde USD 60/mes); en Chile, Toteat tiene la base más completa por API, pero ninguna solución local ejecuta el ciclo pedido → cobro Webpay → boleta SII → cocina → descuento de stock → reorden sugerido. La adopción real sigue baja: solo el 26 % de operadores usa IA y el 6 % en toma de pedidos (NRA).
Cómo lo hace la industria hoy
POS global: Toast IQ suma agente de voz para llamadas y «agentes configurables» en acceso anticipado (anulaciones raras, previsión de producción). Square lanzó inventario con recetas, escaneo de facturas, órdenes de compra automáticas y alertas de merma. Lightspeed AI y SpotOn Profit AI son copilotos analíticos (margen por plato) que recomiendan, no ejecutan.
POS Chile: Toteat (4.500 clientes, 60 % chilenos, ronda de USD 7,4 M para construir IA) cubre QR con pedido y pago, inventario con recetas y márgenes, SII, Transbank, Getnet, Mercado Pago y API pública; aún sin IA propia publicada. Justo lanzó QR por mesa con cuenta individual y pago parcial (diciembre 2025). Bsale (adquirida por Siigo, octubre 2026) tiene API, webhooks e IA de catálogo, sin módulo gastronómico.
Pedidos por WhatsApp: Fudo tiene un agente de ventas en beta (Argentina, Chile, México, Colombia) que arma el pedido, pero deriva el cobro a un link y no manda a cocina. Terceros como Oversai y Aurora Inbox toman pedidos y reservas sin integración POS ni boleta SII cerrada.
Regulación que obliga: desde marzo 2026 el SII exige entregar boleta digital (QR, WhatsApp, correo) si no hay impresora (guía); la emisión automática al confirmar pago es requisito, no extra.
Solución
Qué hace agénticamente
Segmento / precio
Toast IQ
Agentes de marketing, reseñas, turnos, voz; agentes configurables
Desde USD 60/mes (Team), USD 699/mes (Grow)
Square Restaurant Inventory
Recetas, escaneo de facturas, OC automáticas, merma
Usuarios Square
Lightspeed AI
Copiloto: margen por plato, insights
Lightspeed Restaurant
Toteat
QR pedido y pago, inventario-recetas-margen, SII, Transbank, API
Planes básico/avanzado/corporativo (precio no público)
Justo
QR por mesa con cuenta individual y pago parcial; terminal propio
Restaurantes Chile
Fudo
Agente WhatsApp que arma pedidos (beta); pago por link
Tienda Online Plus
Bsale
API, webhooks, IA de catálogo e inventario
Suscripción pyme
Oversai / Aurora Inbox
Agentes WhatsApp: pedidos, reservas, cobranza por link
Por volumen de conversaciones
eleventa
Sin IA; POS Windows retail, factura CFDI (México)
USD 81-189 pago único
Lo que le falta a eleventa
POS de escritorio Windows diseñado para abarrotes mexicanos: factura CFDI, no DTE/SII; sin nube ni API documentada; exporta a Excel solo inventario (Capterra).
Sin QR por mesa, sin food cost por receta, sin predicción de compra, sin agente alguno; reseñas reportan fallas en multicaja.
Para la migración: el histórico de ventas y stock sale por la exportación a Excel; no hace falta reversing para eso.
Brechas para una cafetería chilena (oportunidad)
Ciclo completo agéntico sin dueño: pedido por QR o WhatsApp → cobro Webpay → boleta SII → KDS → stock → reorden.
Control de gastos y margen por producto automatizado: lo que hace Square en EE. UU. no tiene equivalente local.
Toteat es la base más completa por API; la capa de agente (voz/WhatsApp, forecasting, food cost) sigue abierta y puede construirse sobre ella o en paralelo.











5. Oportunidades que se presentan hoy para C4A
El patrón se repite en las tres verticales: el proveedor global ya ejecuta pero no entiende Chile (SII, Webpay, WhatsApp, pesos); el proveedor chileno entiende Chile pero sigue en modo chatbot o sin IA. El espacio es la capa agéntica localizada que se sienta sobre los sistemas de registro existentes, más la seguridad de esa capa.
Oportunidad
Hotel
Inmobiliaria / constructora
Cafetería
Cierre de ciclo con cobro y boleta SII (nadie lo hace)
Reserva → Webpay → boleta → PMS
Cotización → promesa electrónica → pago reserva
Pedido → Webpay → boleta → cocina → stock
Agente por WhatsApp que ejecuta, no solo responde
Concierge con cambios en PMS (modelo HiJiffy, precio local)
Calificación, agenda de visitas, postventa (sin proveedor chileno)
Toma de pedidos con envío a cocina (Fudo se queda en el link)
Inteligencia de datos que el software local no tiene
Pricing con límites y escalamiento (modelo Cloudbeds Autopilot)
Control de obra para constructora mediana (Procore es enterprise)
Food cost por receta, predicción de compra, control de gastos
Gobernanza y seguridad de agentes
Reglas de autonomía: límites de tarifa, quién aprueba
Permisos sobre datos fragmentados; trazabilidad de decisiones
Anulaciones anómalas, fraude de caja
Distribución por MCP
Exponer inventario a ChatGPT/Claude como SiteMinder
Exponer stock de unidades a agentes compradores
Carta y disponibilidad vía MCP para agentes de delivery
Tres decisiones que esto deja sobre la mesa para el equipo:
Construir sobre el sistema de registro existente (Toteat, MobySuite, un PMS) o reemplazarlo: la evidencia dice que el valor está en la capa agéntica, no en reescribir el POS o el CRM.
Modelo de cobro: HubSpot y Salesforce ya cobran por outcome (USD 0,50-2 por conversación resuelta); ese modelo es replicable en Chile y alinea precio con valor.
El diferenciador de C4A frente a cualquier software house es la gobernanza y seguridad de la capa agéntica (reglas de autonomía, pentest de los agentes, trazabilidad), que ningún proveedor local ofrece.
6. Fuentes consultadas
Páginas abiertas durante la investigación (15-10-2026). Las cifras de ROI de proveedores (Asksuite, Duve, Toast, Fudo) son declaraciones de vendor, no verificadas por terceros.
Hotel
State of Distribution 2026 (NYU/RateGain/HEDNA)
Canary: Hotel AI Research Report 2026
Mews: ronda USD 300 M
Cloudbeds RMS Autopilot
Oracle OPERA Cloud AI
SiteMinder MCP
SiteMinder: hoteles pequeños
HiJiffy en Apaleo
Asksuite: Villa Huapi y Los Lagos
Duve AI
Canary AI Voice
Fini: modificar reservas vía PMS
MCP y distribución hotelera
Aurora Inbox hoteles
Newhotel en Congreso de Hoteleros Chile
Inmobiliaria y constructora
Procore Digital Coworker
ServiceTitan: adopción IA en contratistas
HubSpot Breeze: precio por outcome
Agentforce en real estate
Agentes IA inmobiliarios 2026
Dapta: CRM inmobiliario con IA
Wasi
Whippy + TokkoBroker
Automatización en inmobiliarias chilenas
MobySuite
PlanOK: vacante agentes LLM
TOCTOC firma electrónica
ALICE 2025 review
OpenSpace Field GA
Autodesk DevCon 2026: MCP
Kojo
iConstruye: compras con IA
ObraLink
Brokerages pequeños rezagados
Cafetería y POS
Toast IQ agentes
Toast Spring 26 Release
Toast: estadísticas IA
Square + MarketMan
Lightspeed AI
SpotOn Profit AI
NRA: adopción de IA
Toteat (documentación)
Toteat: ronda USD 7,4 M
Justo: cuenta individual
Justo: terminal propio
Fudo: agente de ventas IA
Bsale
Oversai WhatsApp Chile 2026
Aurora Inbox restaurantes
Boleta digital SII 2026
eleventa en ComparaSoftware
eleventa en Capterra
