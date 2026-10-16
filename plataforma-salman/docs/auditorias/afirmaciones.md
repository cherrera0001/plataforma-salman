# Registro de afirmaciones de las fuentes

Cobertura: cada línea no vacía con contenido de los Markdown y cada párrafo/celda extraído del DOCX. Las líneas que contienen varias proposiciones conservan su contexto; las excepciones materiales se detallan en hallazgos. HECHO DOCUMENTADO significa presencia en la fuente, nunca veracidad externa. Las metas SC son propuestas, no resultados medidos.

| Unidad | Clasificación | Evidencia literal |
|---|---|---|
| INV:L001 | SUPUESTO | Estado del arte: IA agéntica en hotel, inmobiliaria y cafetería (oct 2026) |
| INV:L002 | SUPUESTO | Oct 15, 2026 · @Cristóbal Herrera |
| INV:L003 | SUPUESTO | Investigación comercial de base para los tres proyectos proyectados con Ricardo Salman: qué hace hoy la industria con agentes de IA en cada línea de negocio y dónde hay espacio para C4A. |
| INV:L004 | SUPUESTO | 1. Supuestos de partida |
| INV:L005 | SUPUESTO | Se asumen como dadas las preguntas generales; si alguna falla, cambia el alcance, no la investigación. |
| INV:L006 | SUPUESTO | Los tres negocios son del mismo grupo (Ricardo Salman); el core se diseña multi-tenant desde el inicio porque cuesta lo mismo y abre venta a terceros. |
| INV:L007 | SUPUESTO | Eleventa convive en V1 de la cafetería; se migra cuando la plataforma demuestre valor. |
| INV:L008 | SUPUESTO | Inmobiliaria parte por el lado comercial (venta); control de obra queda para V2. |
| INV:L009 | SUPUESTO | Hotel es de escala pequeña o mediana (menos de 50 habitaciones) y hoy usa canales OTA sin channel manager propio. |
| INV:L010 | SUPUESTO | Facturación electrónica SII y pago con Webpay son requisito en todas las verticales desde V1. |
| INV:L011 | SUPUESTO | El canal preferente de atención al cliente final en Chile es WhatsApp. |
| INV:L012 | SUPUESTO | 2. Hotel: la IA ya ejecuta, pero con autonomía acotada |
| INV:L013 | INFORMACIÓN NO VERIFICADA | Más de la mitad de los hoteles usa IA generativa, pero menos del 10 % reporta una baja del trabajo manual superior al 30 % (State of Distribution 2026, 58.000 propiedades). La capa madura es el concierge por WhatsApp; la capa inmadura es el agente que decide tarifas o cobra solo. |
| INV:L014 | INFORMACIÓN NO VERIFICADA | Cómo lo hace la industria hoy |
| INV:L015 | INFORMACIÓN NO VERIFICADA | PMS y motores de reserva: Mews levantó USD 300 M (enero 2026) para «operar hoteles con IA»; lo concreto es un agente de rooming lists en beta. Cloudbeds lanzó un RMS con Autopilot que mueve tarifas dentro de límites. Oracle OPERA Cloud recomienda y redacta, pero no ejecuta. |
| INV:L016 | INFORMACIÓN NO VERIFICADA | Distribución vía agentes: SiteMinder abrió su inventario por MCP para que ChatGPT/Claude coticen y deriven a reserva directa (abril 2026). Expedia y Booking ya tienen apps dentro de ChatGPT. |
| INV:L017 | INFORMACIÓN NO VERIFICADA | Concierge por WhatsApp (lo más maduro): HiJiffy resuelve más del 80 % de consultas y escribe cambios en el PMS; Asksuite (fuerte en LatAm) reporta casos en Paraguay, Colombia y Uruguay recuperando cotizaciones abandonadas; Duve AI responde en modo autónomo y vende upsells con link de pago; Canary suma agentes de voz para recepción y reservas. |
| INV:L018 | INFORMACIÓN NO VERIFICADA | Check-in digital y upselling: Duve y Canary automatizan registro, ID y pago previo; Duve declara +20 % de ingresos por upsell (cifra de proveedor). |
| INV:L019 | HIPÓTESIS | Lo que nadie documenta: cancelaciones ni cobros autónomos. El cobro se delega a links de pago y la reserva final se cierra en el motor del hotel. |
| INV:L020 | INFORMACIÓN NO VERIFICADA | Solución |
| INV:L021 | INFORMACIÓN NO VERIFICADA | Qué hace agénticamente |
| INV:L022 | INFORMACIÓN NO VERIFICADA | Segmento / precio |
| INV:L023 | INFORMACIÓN NO VERIFICADA | Mews |
| INV:L024 | INFORMACIÓN NO VERIFICADA | Agente de rooming lists (beta); visión de agentes revenue/ops/guest |
| INV:L025 | INFORMACIÓN NO VERIFICADA | Mid-upscale; sin precio público |
| INV:L026 | INFORMACIÓN NO VERIFICADA | Cloudbeds Signals + RMS |
| INV:L027 | INFORMACIÓN NO VERIFICADA | Consulta conversacional; Autopilot de tarifas con límites |
| INV:L028 | INFORMACIÓN NO VERIFICADA | Independientes |
| INV:L029 | INFORMACIÓN NO VERIFICADA | SiteMinder / Little Hotelier |
| INV:L030 | INFORMACIÓN NO VERIFICADA | Inventario vivo vía MCP; derivación a reserva directa |
| INV:L031 | INFORMACIÓN NO VERIFICADA | Pequeños y medianos |
| INV:L032 | INFORMACIÓN NO VERIFICADA | HiJiffy (Aplysia) |
| INV:L033 | INFORMACIÓN NO VERIFICADA | Reserva guiada, check-in, upsell, cambios en PMS por WhatsApp/IG |
| INV:L034 | INFORMACIÓN NO VERIFICADA | USD 4-8 por habitación al mes (reseñas) |
| INV:L035 | INFORMACIÓN NO VERIFICADA | Asksuite |
| INV:L036 | INFORMACIÓN NO VERIFICADA | Cotiza y recupera reservas por WhatsApp; modifica en PMS |
| INV:L037 | INFORMACIÓN NO VERIFICADA | Desde USD 349/mes |
| INV:L038 | INFORMACIÓN NO VERIFICADA | Duve AI |
| INV:L039 | INFORMACIÓN NO VERIFICADA | Respuesta autónoma, upsell con link de pago, check-in online |
| INV:L040 | INFORMACIÓN NO VERIFICADA | Hoteles y apart-hotel |
| INV:L041 | INFORMACIÓN NO VERIFICADA | Aurora Inbox |
| INV:L042 | INFORMACIÓN NO VERIFICADA | WhatsApp: disponibilidad, reserva, link de pago, check-in |
| INV:L043 | INFORMACIÓN NO VERIFICADA | USD 130-380/mes (LatAm) |
| INV:L044 | INFORMACIÓN NO VERIFICADA | Climber RMS |
| INV:L045 | INFORMACIÓN NO VERIFICADA | Pricing dinámico automático opcional sobre Cloudbeds |
| INV:L046 | INFORMACIÓN NO VERIFICADA | Boutique e independientes |
| INV:L047 | HIPÓTESIS | Brechas para un hotel chico (oportunidad) |
| INV:L048 | INFORMACIÓN NO VERIFICADA | Sin integración PMS bidireccional el agente solo informa; los PMS baratos tienen APIs limitadas. |
| INV:L049 | HIPÓTESIS | Nadie resuelve cobro agéntico en pesos chilenos (Webpay, Transbank, boleta SII) ni hay bundle local; Newhotel es lo único con presencia en el Congreso de Hoteleros de Chile y solo anuncia un asistente. |
| INV:L050 | INFORMACIÓN NO VERIFICADA | Las reglas de autonomía (límites de tarifa, escalamiento) siguen siendo manuales; el 29 % de los hoteles pequeños aún tiene tarifa estática (SiteMinder). |
| INV:L051 | INFORMACIÓN NO VERIFICADA | La distribución por MCP favorece OTAs y conectores grandes; el independiente depende de su vendor. |
| INV:L056 | INFORMACIÓN NO VERIFICADA | 3. Inmobiliaria y constructora: el agente global cobra por resultado; el proveedor chileno aún no tiene agente |
| INV:L057 | INFORMACIÓN NO VERIFICADA | El salto 2025-2026 fue de chatbot a agente que ejecuta y cobra por outcome: HubSpot Breeze cobra USD 0,50 por conversación resuelta y USD 1 por lead; Salesforce Agentforce USD 2 por conversación. En Chile, los CRM inmobiliarios y las plataformas de preventa a postventa no traen agente nativo; la capa agéntica llega por terceros. |
| INV:L058 | INFORMACIÓN NO VERIFICADA | Cómo lo hace la industria hoy |
| INV:L059 | INFORMACIÓN NO VERIFICADA | CRM y leads (EE. UU.): Structurely, Ylopo, Lofty y BoldTrail operan como ISA virtuales (llaman, textean, agendan, transfieren en vivo) por USD 300-1.000/mes (rework). Follow Up Boss solo redacta. |
| INV:L060 | INFORMACIÓN NO VERIFICADA | CRM y leads (LatAm/Chile): Wasi (USD 30/usuario/mes, 22 países) y TokkoBroker siguen siendo CRM de inventario y portales; el agente se agrega con Dapta (califica y agenda por WhatsApp) o Whippy. En Chile lo visible es Bitrix24: clasificador caliente/tibio/frío, respuesta fuera de horario, recordatorios de visita, transcripción de llamadas. |
| INV:L061 | HIPÓTESIS | Preventa a postventa (Chile): MobySuite (más de 100 inmobiliarias) cubre reserva, cobranza, escrituración y postventa sin IA publicada; PlanOK contrató en 2025 para construir agentes LLM; TOCTOC firma reservas y promesas electrónicamente desde 2020. Ningún agente chileno gestiona postventa de forma autónoma. |
| INV:L062 | INFORMACIÓN NO VERIFICADA | Control de obra: Procore Digital Coworker (julio 2026) vende paquetes de 5/20/25+ agentes que revisan submittals, RFIs, daily logs y contratos con triggers; Autodesk apuesta por asistente + MCP; OpenSpace Field autolocaliza observaciones y llena formularios por voz; ALICE re-secuencia cronogramas (Suffolk ahorró 42 días). En Chile, ObraLink y Foco en Obra no publican agentes. |
| INV:L063 | INFORMACIÓN NO VERIFICADA | Compras: Kojo (600+ contratistas) usa agentes para seguir distribuidores y entregas; iConstruye mostró en julio 2026 cotización y compra con agentes para constructoras chilenas. |
| INV:L064 | INFORMACIÓN NO VERIFICADA | Adopción: el 38 % de contratistas comerciales reporta impacto medible de IA, el doble que en 2025 (ServiceTitan); los brokerages pequeños (10 agentes o menos) son los más rezagados (Real Estate News). |
| INV:L065 | INFORMACIÓN NO VERIFICADA | Solución |
| INV:L066 | INFORMACIÓN NO VERIFICADA | Qué hace agénticamente |
| INV:L067 | INFORMACIÓN NO VERIFICADA | Segmento / precio |
| INV:L068 | INFORMACIÓN NO VERIFICADA | HubSpot Breeze |
| INV:L069 | INFORMACIÓN NO VERIFICADA | Resuelve conversaciones, recomienda leads |
| INV:L070 | INFORMACIÓN NO VERIFICADA | USD 0,50 por resolución, USD 1 por lead |
| INV:L071 | INFORMACIÓN NO VERIFICADA | Salesforce Agentforce |
| INV:L072 | INFORMACIÓN NO VERIFICADA | Califica, agenda visitas, redacta documentos |
| INV:L073 | INFORMACIÓN NO VERIFICADA | Enterprise; USD 2 por conversación |
| INV:L074 | INFORMACIÓN NO VERIFICADA | Structurely / Lofty / Ylopo |
| INV:L075 | INFORMACIÓN NO VERIFICADA | ISA virtual: llama, textea, agenda, transfiere |
| INV:L076 | INFORMACIÓN NO VERIFICADA | Brokerages EE. UU.; USD 300-1.000/mes |
| INV:L077 | INFORMACIÓN NO VERIFICADA | Dapta |
| INV:L078 | INFORMACIÓN NO VERIFICADA | Califica y agenda por WhatsApp; sincroniza CRM |
| INV:L079 | INFORMACIÓN NO VERIFICADA | PyME LatAm |
| INV:L080 | INFORMACIÓN NO VERIFICADA | Wasi |
| INV:L081 | INFORMACIÓN NO VERIFICADA | CRM + portales; sin agente nativo |
| INV:L082 | INFORMACIÓN NO VERIFICADA | USD 30 por usuario al mes |
| INV:L083 | INFORMACIÓN NO VERIFICADA | Bitrix24 (Chile) |
| INV:L084 | INFORMACIÓN NO VERIFICADA | Clasifica leads, recuerda visitas, transcribe |
| INV:L085 | INFORMACIÓN NO VERIFICADA | PyME |
| INV:L086 | INFORMACIÓN NO VERIFICADA | MobySuite / PlanOK |
| INV:L087 | INFORMACIÓN NO VERIFICADA | Preventa a postventa; agentes en desarrollo |
| INV:L088 | INFORMACIÓN NO VERIFICADA | Inmobiliarias Chile y LatAm |
| INV:L089 | INFORMACIÓN NO VERIFICADA | Procore Digital Coworker |
| INV:L090 | INFORMACIÓN NO VERIFICADA | Revisa submittals, RFIs, contratos; triggers |
| INV:L091 | INFORMACIÓN NO VERIFICADA | Mid y enterprise; cotizar |
| INV:L092 | INFORMACIÓN NO VERIFICADA | OpenSpace Field |
| INV:L093 | INFORMACIÓN NO VERIFICADA | Autolocaliza issues; voz a formulario |
| INV:L094 | INFORMACIÓN NO VERIFICADA | Incluido en Core/Enterprise |
| INV:L095 | INFORMACIÓN NO VERIFICADA | ALICE |
| INV:L096 | INFORMACIÓN NO VERIFICADA | Re-secuencia cronogramas |
| INV:L097 | INFORMACIÓN NO VERIFICADA | Enterprise |
| INV:L098 | INFORMACIÓN NO VERIFICADA | iConstruye |
| INV:L099 | INFORMACIÓN NO VERIFICADA | Cotización y compra con agentes (demo 2026) |
| INV:L100 | INFORMACIÓN NO VERIFICADA | Constructoras Chile |
| INV:L101 | HIPÓTESIS | Brechas para una inmobiliaria + constructora chilena mediana (oportunidad) |
| INV:L102 | HIPÓTESIS | Ningún CRM LatAm trae agente nativo de WhatsApp: siempre hay que integrar una capa externa. |
| INV:L103 | INFORMACIÓN NO VERIFICADA | Cotización y promesa siguen siendo manuales; la firma electrónica existe pero no está orquestada por agentes. |
| INV:L104 | INFORMACIÓN NO VERIFICADA | Postventa sin IA en todos los proveedores locales. |
| INV:L105 | INFORMACIÓN NO VERIFICADA | Procore y ALICE están dimensionados para enterprise y sin precio público; la constructora mediana queda fuera. |
| INV:L106 | INFORMACIÓN NO VERIFICADA | Datos fragmentados (Excel, WhatsApp, portales) impiden que un agente actúe con permisos claros: el primer entregable es el modelo de datos, no el agente. |
| INV:L116 | HIPÓTESIS | 4. Cafetería y POS: nadie en Chile cierra el ciclo agéntico completo |
| INV:L117 | INFORMACIÓN NO VERIFICADA | En EE. UU. el POS ya es plataforma de agentes (Toast IQ vende agentes de marketing, reseñas, turnos y voz desde USD 60/mes); en Chile, Toteat tiene la base más completa por API, pero ninguna solución local ejecuta el ciclo pedido → cobro Webpay → boleta SII → cocina → descuento de stock → reorden sugerido. La adopción real sigue baja: solo el 26 % de operadores usa IA y el 6 % en toma de pedidos (NRA). |
| INV:L118 | INFORMACIÓN NO VERIFICADA | Cómo lo hace la industria hoy |
| INV:L119 | INFORMACIÓN NO VERIFICADA | POS global: Toast IQ suma agente de voz para llamadas y «agentes configurables» en acceso anticipado (anulaciones raras, previsión de producción). Square lanzó inventario con recetas, escaneo de facturas, órdenes de compra automáticas y alertas de merma. Lightspeed AI y SpotOn Profit AI son copilotos analíticos (margen por plato) que recomiendan, no ejecutan. |
| INV:L120 | INFORMACIÓN NO VERIFICADA | POS Chile: Toteat (4.500 clientes, 60 % chilenos, ronda de USD 7,4 M para construir IA) cubre QR con pedido y pago, inventario con recetas y márgenes, SII, Transbank, Getnet, Mercado Pago y API pública; aún sin IA propia publicada. Justo lanzó QR por mesa con cuenta individual y pago parcial (diciembre 2025). Bsale (adquirida por Siigo, octubre 2026) tiene API, webhooks e IA de catálogo, sin módulo gastronómico. |
| INV:L121 | INFORMACIÓN NO VERIFICADA | Pedidos por WhatsApp: Fudo tiene un agente de ventas en beta (Argentina, Chile, México, Colombia) que arma el pedido, pero deriva el cobro a un link y no manda a cocina. Terceros como Oversai y Aurora Inbox toman pedidos y reservas sin integración POS ni boleta SII cerrada. |
| INV:L122 | INFORMACIÓN NO VERIFICADA | Regulación que obliga: desde marzo 2026 el SII exige entregar boleta digital (QR, WhatsApp, correo) si no hay impresora (guía); la emisión automática al confirmar pago es requisito, no extra. |
| INV:L123 | INFORMACIÓN NO VERIFICADA | Solución |
| INV:L124 | INFORMACIÓN NO VERIFICADA | Qué hace agénticamente |
| INV:L125 | INFORMACIÓN NO VERIFICADA | Segmento / precio |
| INV:L126 | INFORMACIÓN NO VERIFICADA | Toast IQ |
| INV:L127 | INFORMACIÓN NO VERIFICADA | Agentes de marketing, reseñas, turnos, voz; agentes configurables |
| INV:L128 | INFORMACIÓN NO VERIFICADA | Desde USD 60/mes (Team), USD 699/mes (Grow) |
| INV:L129 | INFORMACIÓN NO VERIFICADA | Square Restaurant Inventory |
| INV:L130 | INFORMACIÓN NO VERIFICADA | Recetas, escaneo de facturas, OC automáticas, merma |
| INV:L131 | INFORMACIÓN NO VERIFICADA | Usuarios Square |
| INV:L132 | INFORMACIÓN NO VERIFICADA | Lightspeed AI |
| INV:L133 | INFORMACIÓN NO VERIFICADA | Copiloto: margen por plato, insights |
| INV:L134 | INFORMACIÓN NO VERIFICADA | Lightspeed Restaurant |
| INV:L135 | INFORMACIÓN NO VERIFICADA | Toteat |
| INV:L136 | INFORMACIÓN NO VERIFICADA | QR pedido y pago, inventario-recetas-margen, SII, Transbank, API |
| INV:L137 | INFORMACIÓN NO VERIFICADA | Planes básico/avanzado/corporativo (precio no público) |
| INV:L138 | INFORMACIÓN NO VERIFICADA | Justo |
| INV:L139 | INFORMACIÓN NO VERIFICADA | QR por mesa con cuenta individual y pago parcial; terminal propio |
| INV:L140 | INFORMACIÓN NO VERIFICADA | Restaurantes Chile |
| INV:L141 | INFORMACIÓN NO VERIFICADA | Fudo |
| INV:L142 | INFORMACIÓN NO VERIFICADA | Agente WhatsApp que arma pedidos (beta); pago por link |
| INV:L143 | INFORMACIÓN NO VERIFICADA | Tienda Online Plus |
| INV:L144 | INFORMACIÓN NO VERIFICADA | Bsale |
| INV:L145 | INFORMACIÓN NO VERIFICADA | API, webhooks, IA de catálogo e inventario |
| INV:L146 | INFORMACIÓN NO VERIFICADA | Suscripción pyme |
| INV:L147 | INFORMACIÓN NO VERIFICADA | Oversai / Aurora Inbox |
| INV:L148 | INFORMACIÓN NO VERIFICADA | Agentes WhatsApp: pedidos, reservas, cobranza por link |
| INV:L149 | INFORMACIÓN NO VERIFICADA | Por volumen de conversaciones |
| INV:L150 | INFORMACIÓN NO VERIFICADA | eleventa |
| INV:L151 | INFORMACIÓN NO VERIFICADA | Sin IA; POS Windows retail, factura CFDI (México) |
| INV:L152 | INFORMACIÓN NO VERIFICADA | USD 81-189 pago único |
| INV:L153 | INFORMACIÓN NO VERIFICADA | Lo que le falta a eleventa |
| INV:L154 | CONTRADICCIÓN | POS de escritorio Windows diseñado para abarrotes mexicanos: factura CFDI, no DTE/SII; sin nube ni API documentada; exporta a Excel solo inventario (Capterra). |
| INV:L155 | INFORMACIÓN NO VERIFICADA | Sin QR por mesa, sin food cost por receta, sin predicción de compra, sin agente alguno; reseñas reportan fallas en multicaja. |
| INV:L156 | CONTRADICCIÓN | Para la migración: el histórico de ventas y stock sale por la exportación a Excel; no hace falta reversing para eso. |
| INV:L157 | HIPÓTESIS | Brechas para una cafetería chilena (oportunidad) |
| INV:L158 | INFORMACIÓN NO VERIFICADA | Ciclo completo agéntico sin dueño: pedido por QR o WhatsApp → cobro Webpay → boleta SII → KDS → stock → reorden. |
| INV:L159 | INFORMACIÓN NO VERIFICADA | Control de gastos y margen por producto automatizado: lo que hace Square en EE. UU. no tiene equivalente local. |
| INV:L160 | INFORMACIÓN NO VERIFICADA | Toteat es la base más completa por API; la capa de agente (voz/WhatsApp, forecasting, food cost) sigue abierta y puede construirse sobre ella o en paralelo. |
| INV:L172 | HIPÓTESIS | 5. Oportunidades que se presentan hoy para C4A |
| INV:L173 | INFORMACIÓN NO VERIFICADA | El patrón se repite en las tres verticales: el proveedor global ya ejecuta pero no entiende Chile (SII, Webpay, WhatsApp, pesos); el proveedor chileno entiende Chile pero sigue en modo chatbot o sin IA. El espacio es la capa agéntica localizada que se sienta sobre los sistemas de registro existentes, más la seguridad de esa capa. |
| INV:L174 | HIPÓTESIS | Oportunidad |
| INV:L175 | INFORMACIÓN NO VERIFICADA | Hotel |
| INV:L176 | INFORMACIÓN NO VERIFICADA | Inmobiliaria / constructora |
| INV:L177 | INFORMACIÓN NO VERIFICADA | Cafetería |
| INV:L178 | HIPÓTESIS | Cierre de ciclo con cobro y boleta SII (nadie lo hace) |
| INV:L179 | INFORMACIÓN NO VERIFICADA | Reserva → Webpay → boleta → PMS |
| INV:L180 | INFORMACIÓN NO VERIFICADA | Cotización → promesa electrónica → pago reserva |
| INV:L181 | INFORMACIÓN NO VERIFICADA | Pedido → Webpay → boleta → cocina → stock |
| INV:L182 | INFORMACIÓN NO VERIFICADA | Agente por WhatsApp que ejecuta, no solo responde |
| INV:L183 | INFORMACIÓN NO VERIFICADA | Concierge con cambios en PMS (modelo HiJiffy, precio local) |
| INV:L184 | INFORMACIÓN NO VERIFICADA | Calificación, agenda de visitas, postventa (sin proveedor chileno) |
| INV:L185 | INFORMACIÓN NO VERIFICADA | Toma de pedidos con envío a cocina (Fudo se queda en el link) |
| INV:L186 | INFORMACIÓN NO VERIFICADA | Inteligencia de datos que el software local no tiene |
| INV:L187 | INFORMACIÓN NO VERIFICADA | Pricing con límites y escalamiento (modelo Cloudbeds Autopilot) |
| INV:L188 | INFORMACIÓN NO VERIFICADA | Control de obra para constructora mediana (Procore es enterprise) |
| INV:L189 | INFORMACIÓN NO VERIFICADA | Food cost por receta, predicción de compra, control de gastos |
| INV:L190 | INFORMACIÓN NO VERIFICADA | Gobernanza y seguridad de agentes |
| INV:L191 | INFORMACIÓN NO VERIFICADA | Reglas de autonomía: límites de tarifa, quién aprueba |
| INV:L192 | INFORMACIÓN NO VERIFICADA | Permisos sobre datos fragmentados; trazabilidad de decisiones |
| INV:L193 | INFORMACIÓN NO VERIFICADA | Anulaciones anómalas, fraude de caja |
| INV:L194 | INFORMACIÓN NO VERIFICADA | Distribución por MCP |
| INV:L195 | INFORMACIÓN NO VERIFICADA | Exponer inventario a ChatGPT/Claude como SiteMinder |
| INV:L196 | INFORMACIÓN NO VERIFICADA | Exponer stock de unidades a agentes compradores |
| INV:L197 | INFORMACIÓN NO VERIFICADA | Carta y disponibilidad vía MCP para agentes de delivery |
| INV:L198 | DECISIÓN PENDIENTE | Tres decisiones que esto deja sobre la mesa para el equipo: |
| INV:L199 | INFORMACIÓN NO VERIFICADA | Construir sobre el sistema de registro existente (Toteat, MobySuite, un PMS) o reemplazarlo: la evidencia dice que el valor está en la capa agéntica, no en reescribir el POS o el CRM. |
| INV:L200 | HIPÓTESIS | Modelo de cobro: HubSpot y Salesforce ya cobran por outcome (USD 0,50-2 por conversación resuelta); ese modelo es replicable en Chile y alinea precio con valor. |
| INV:L201 | HIPÓTESIS | El diferenciador de C4A frente a cualquier software house es la gobernanza y seguridad de la capa agéntica (reglas de autonomía, pentest de los agentes, trazabilidad), que ningún proveedor local ofrece. |
| INV:L202 | INFORMACIÓN NO VERIFICADA | 6. Fuentes consultadas |
| INV:L203 | INFORMACIÓN NO VERIFICADA | Páginas abiertas durante la investigación (15-10-2026). Las cifras de ROI de proveedores (Asksuite, Duve, Toast, Fudo) son declaraciones de vendor, no verificadas por terceros. |
| INV:L204 | INFORMACIÓN NO VERIFICADA | Hotel |
| INV:L205 | INFORMACIÓN NO VERIFICADA | State of Distribution 2026 (NYU/RateGain/HEDNA) |
| INV:L206 | INFORMACIÓN NO VERIFICADA | Canary: Hotel AI Research Report 2026 |
| INV:L207 | INFORMACIÓN NO VERIFICADA | Mews: ronda USD 300 M |
| INV:L208 | INFORMACIÓN NO VERIFICADA | Cloudbeds RMS Autopilot |
| INV:L209 | INFORMACIÓN NO VERIFICADA | Oracle OPERA Cloud AI |
| INV:L210 | INFORMACIÓN NO VERIFICADA | SiteMinder MCP |
| INV:L211 | INFORMACIÓN NO VERIFICADA | SiteMinder: hoteles pequeños |
| INV:L212 | INFORMACIÓN NO VERIFICADA | HiJiffy en Apaleo |
| INV:L213 | INFORMACIÓN NO VERIFICADA | Asksuite: Villa Huapi y Los Lagos |
| INV:L214 | INFORMACIÓN NO VERIFICADA | Duve AI |
| INV:L215 | INFORMACIÓN NO VERIFICADA | Canary AI Voice |
| INV:L216 | INFORMACIÓN NO VERIFICADA | Fini: modificar reservas vía PMS |
| INV:L217 | INFORMACIÓN NO VERIFICADA | MCP y distribución hotelera |
| INV:L218 | INFORMACIÓN NO VERIFICADA | Aurora Inbox hoteles |
| INV:L219 | INFORMACIÓN NO VERIFICADA | Newhotel en Congreso de Hoteleros Chile |
| INV:L220 | INFORMACIÓN NO VERIFICADA | Inmobiliaria y constructora |
| INV:L221 | INFORMACIÓN NO VERIFICADA | Procore Digital Coworker |
| INV:L222 | INFORMACIÓN NO VERIFICADA | ServiceTitan: adopción IA en contratistas |
| INV:L223 | INFORMACIÓN NO VERIFICADA | HubSpot Breeze: precio por outcome |
| INV:L224 | INFORMACIÓN NO VERIFICADA | Agentforce en real estate |
| INV:L225 | INFORMACIÓN NO VERIFICADA | Agentes IA inmobiliarios 2026 |
| INV:L226 | INFORMACIÓN NO VERIFICADA | Dapta: CRM inmobiliario con IA |
| INV:L227 | INFORMACIÓN NO VERIFICADA | Wasi |
| INV:L228 | INFORMACIÓN NO VERIFICADA | Whippy + TokkoBroker |
| INV:L229 | INFORMACIÓN NO VERIFICADA | Automatización en inmobiliarias chilenas |
| INV:L230 | INFORMACIÓN NO VERIFICADA | MobySuite |
| INV:L231 | INFORMACIÓN NO VERIFICADA | PlanOK: vacante agentes LLM |
| INV:L232 | INFORMACIÓN NO VERIFICADA | TOCTOC firma electrónica |
| INV:L233 | INFORMACIÓN NO VERIFICADA | ALICE 2025 review |
| INV:L234 | INFORMACIÓN NO VERIFICADA | OpenSpace Field GA |
| INV:L235 | INFORMACIÓN NO VERIFICADA | Autodesk DevCon 2026: MCP |
| INV:L236 | INFORMACIÓN NO VERIFICADA | Kojo |
| INV:L237 | INFORMACIÓN NO VERIFICADA | iConstruye: compras con IA |
| INV:L238 | INFORMACIÓN NO VERIFICADA | ObraLink |
| INV:L239 | INFORMACIÓN NO VERIFICADA | Brokerages pequeños rezagados |
| INV:L240 | INFORMACIÓN NO VERIFICADA | Cafetería y POS |
| INV:L241 | INFORMACIÓN NO VERIFICADA | Toast IQ agentes |
| INV:L242 | INFORMACIÓN NO VERIFICADA | Toast Spring 26 Release |
| INV:L243 | INFORMACIÓN NO VERIFICADA | Toast: estadísticas IA |
| INV:L244 | INFORMACIÓN NO VERIFICADA | Square + MarketMan |
| INV:L245 | INFORMACIÓN NO VERIFICADA | Lightspeed AI |
| INV:L246 | INFORMACIÓN NO VERIFICADA | SpotOn Profit AI |
| INV:L247 | INFORMACIÓN NO VERIFICADA | NRA: adopción de IA |
| INV:L248 | INFORMACIÓN NO VERIFICADA | Toteat (documentación) |
| INV:L249 | INFORMACIÓN NO VERIFICADA | Toteat: ronda USD 7,4 M |
| INV:L250 | INFORMACIÓN NO VERIFICADA | Justo: cuenta individual |
| INV:L251 | INFORMACIÓN NO VERIFICADA | Justo: terminal propio |
| INV:L252 | INFORMACIÓN NO VERIFICADA | Fudo: agente de ventas IA |
| INV:L253 | INFORMACIÓN NO VERIFICADA | Bsale |
| INV:L254 | INFORMACIÓN NO VERIFICADA | Oversai WhatsApp Chile 2026 |
| INV:L255 | INFORMACIÓN NO VERIFICADA | Aurora Inbox restaurantes |
| INV:L256 | INFORMACIÓN NO VERIFICADA | Boleta digital SII 2026 |
| INV:L257 | INFORMACIÓN NO VERIFICADA | eleventa en ComparaSoftware |
| INV:L258 | INFORMACIÓN NO VERIFICADA | eleventa en Capterra |
| CAF:L001 | HECHO DOCUMENTADO | # Spec SDD 01: Cafetería (mesas, POS inteligente y control de gastos) |
| CAF:L003 | HECHO DOCUMENTADO | Oct 15, 2026 · @Cristóbal Herrera |
| CAF:L005 | HECHO DOCUMENTADO | ## 0. Flujo spec-kit aplicado a este proyecto |
| CAF:L007 | HECHO DOCUMENTADO | Este documento es el `spec.md` de la feature `001-cafeteria-mesas-pos`, escrito según la ruta completa de [spec-kit](https://github.github.com/spec-kit/quickstart.html): `/speckit.constitution` → `/speckit.specify` → `/speckit.clarify` → `/speckit.plan` → `/speckit.checklist` → `/speckit.tasks` → `/speckit.analyze` → `/speckit.implement` → `/speckit.converge`. La spec dice qué y por qué; la tecnología va en `plan.md`. |
| CAF:L009 | HECHO DOCUMENTADO | &#124; Paso &#124; Comando &#124; Produce &#124; Estado hoy &#124; |
| CAF:L011 | HECHO DOCUMENTADO | &#124; 1 &#124; `/speckit.constitution` &#124; `.specify/memory/constitution.md` (una sola para core + 3 verticales) &#124; Borrador en §1 &#124; |
| CAF:L012 | HECHO DOCUMENTADO | &#124; 2 &#124; `/speckit.specify` &#124; `specs/001-cafeteria-mesas-pos/spec.md` + `checklists/requirements.md` &#124; Este doc (§2 a §5) &#124; |
| CAF:L013 | HECHO DOCUMENTADO | &#124; 3 &#124; `/speckit.clarify` &#124; Preguntas sobre áreas subespecificadas, respuestas incorporadas a `spec.md` &#124; Pendientes en §5 &#124; |
| CAF:L014 | HECHO DOCUMENTADO | &#124; 4 &#124; `/speckit.plan` &#124; `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` &#124; Resumen en §6 &#124; |
| CAF:L015 | HECHO DOCUMENTADO | &#124; 5 &#124; `/speckit.checklist` &#124; Listas de calidad de requisitos, marcadas por el revisor &#124; Por generar &#124; |
| CAF:L016 | HECHO DOCUMENTADO | &#124; 6 &#124; `/speckit.tasks` &#124; `tasks.md` ordenado por dependencias, agrupado por historia &#124; Por generar &#124; |
| CAF:L017 | HECHO DOCUMENTADO | &#124; 7 &#124; `/speckit.analyze` &#124; Informe de conflictos entre spec, plan y tasks (solo lectura) &#124; Por correr &#124; |
| CAF:L018 | HECHO DOCUMENTADO | &#124; 8 &#124; `/speckit.implement` &#124; Ejecuta `tasks.md` por fases; lee las checklists como gate &#124; Por correr &#124; |
| CAF:L019 | HECHO DOCUMENTADO | &#124; 9 &#124; `/speckit.converge` &#124; Compara código contra spec, plan y tasks; añade brechas como tareas &#124; Por correr &#124; |
| CAF:L021 | HECHO DOCUMENTADO | Setup: `uv tool install specify-cli`, luego `specify init plataforma-salman --integration claude`. El estado de feature activa vive en `.specify/feature.json`; con la extensión git se crean ramas numeradas (`001-cafeteria-mesas-pos`). |
| CAF:L023 | HECHO DOCUMENTADO | ## 1. Constitución (compartida por el core y las tres verticales) |
| CAF:L025 | HECHO DOCUMENTADO | Una sola constitución para el monorepo `plataforma-salman`; cada `plan.md` debe pasar el «Constitution Check» contra estos principios. Versión 1.0.0 (2026-10-15). |
| CAF:L027 | HECHO DOCUMENTADO | 1. **Core primero, vertical después.** Identidad, catálogo, transacciones, pagos, gastos y analítica viven en `core/`; una vertical solo agrega lo que ninguna otra necesita. Toda duplicación entre verticales se justifica por escrito en `plan.md` (Complexity Tracking). |
| CAF:L028 | HECHO DOCUMENTADO | 2. **Chile es requisito, no localización.** Boleta electrónica SII emitida al confirmar pago, cobro por Webpay/Transbank o Mercado Pago, coma decimal y pesos sin decimales. Ninguna historia se declara completa sin estos tres. |
| CAF:L029 | HECHO DOCUMENTADO | 3. **Agente que ejecuta bajo reglas explícitas.** Todo agente declara qué acciones hace solo, cuáles requieren aprobación humana y cuál es su límite monetario. Cada acción queda en un ledger inmutable (quién, qué, cuándo, con qué evidencia). Sin reglas, el agente solo informa. |
| CAF:L030 | HECHO DOCUMENTADO | 4. **Seguridad desde la spec.** Cada feature incluye modelo de amenazas resumido en `plan.md`, pentest de la capa agéntica antes de `/speckit.converge` final, y los datos personales se tratan según Ley 21.719 (encargado de tratamiento cuando aplique). |
| CAF:L031 | HECHO DOCUMENTADO | 5. **Test primero, dato real.** Las historias se aceptan con escenarios Given/When/Then automatizados; se prohíbe dato sintético en demos a cliente. `tasks.md` ordena pruebas antes de implementación en cada historia. |
| CAF:L032 | HECHO DOCUMENTADO | 6. **Simplicidad y observabilidad.** YAGNI; una aplicación por vertical sobre el core; logs estructurados, métricas de negocio expuestas desde el día 1 (ventas por hora, margen, latencia de agente). |
| CAF:L034 | HECHO DOCUMENTADO | Gobernanza: cambios a la constitución requieren bump de versión semántica, nota de migración y aprobación de Cristóbal Herrera; `/speckit.analyze` reporta como CRITICAL cualquier violación. |
| CAF:L036 | REQUISITO PROPUESTO | ## 2. Escenarios de usuario y pruebas (obligatorio) |
| CAF:L038 | REQUISITO PROPUESTO | Cada historia es independiente, testeable sola y entrega valor por sí misma; la P1 es el MVP demostrable. |
| CAF:L040 | REQUISITO PROPUESTO | **Historia 1 (P1): Pedir y pagar desde la mesa** |
| CAF:L042 | REQUISITO PROPUESTO | Un cliente escanea el QR de su mesa, ve la carta digital ya existente, arma su pedido (individual o compartido), lo envía a cocina y paga su parte con Webpay o Mercado Pago. Recibe boleta SII digital por WhatsApp o correo. |
| CAF:L044 | REQUISITO PROPUESTO | - Por qué P1: es el dolor visible (sin sistema de mesas) y el que genera los datos que alimentan todo lo demás. |
| CAF:L045 | REQUISITO PROPUESTO | - Prueba independiente: una mesa con dos clientes puede pedir, dividir y pagar sin tocar eleventa ni la caja. |
| CAF:L046 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| CAF:L047 | REQUISITO PROPUESTO | 1. Dado un QR de mesa activo, cuando el cliente abre la carta y confirma un pedido, entonces el pedido aparece en cocina con número de mesa y hora en menos de 5 segundos. |
| CAF:L048 | REQUISITO PROPUESTO | 2. Dado un pedido compartido de dos personas, cuando cada una elige «pagar lo mío», entonces cada una paga solo sus ítems y la mesa queda cerrada cuando el saldo es cero. |
| CAF:L049 | REQUISITO PROPUESTO | 3. Dado un pago aprobado, cuando Webpay confirma, entonces se emite la boleta electrónica y se envía al canal elegido antes de 30 segundos. |
| CAF:L050 | REQUISITO PROPUESTO | 4. Dado un pago rechazado, cuando el cliente reintenta, entonces el pedido se mantiene y no se duplica en cocina. |
| CAF:L052 | REQUISITO PROPUESTO | **Historia 2 (P2): Control de gastos e inventario con margen por producto** |
| CAF:L054 | REQUISITO PROPUESTO | El administrador registra compras (foto de factura o carga manual), el sistema descuenta insumos por receta a medida que se venden y muestra margen real por producto y por día. |
| CAF:L056 | REQUISITO PROPUESTO | - Por qué P2: es la «inteligencia de datos» que eleventa no entrega y la base del agente de compras. |
| CAF:L057 | REQUISITO PROPUESTO | - Prueba independiente: cargar 10 facturas y 1 día de ventas devuelve margen por producto con error menor al 2 % contra cálculo manual. |
| CAF:L058 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| CAF:L059 | REQUISITO PROPUESTO | 1. Dada una receta con 4 insumos, cuando se vende una unidad, entonces el stock de cada insumo baja según la receta. |
| CAF:L060 | REQUISITO PROPUESTO | 2. Dada una factura de proveedor fotografiada, cuando se procesa, entonces las líneas quedan registradas como gasto con proveedor, monto y fecha, pendientes de aprobación. |
| CAF:L061 | REQUISITO PROPUESTO | 3. Dado el cierre de día, cuando el administrador abre el dashboard, entonces ve ventas, costo, margen y los 5 productos con peor margen. |
| CAF:L063 | REQUISITO PROPUESTO | **Historia 3 (P3): Agente que sugiere reposición y alerta anomalías** |
| CAF:L065 | REQUISITO PROPUESTO | Un agente revisa stock, ventas y mermas, propone una orden de compra semanal al proveedor habitual y alerta anulaciones o descuentos fuera de patrón. Nunca compra solo: el administrador aprueba por WhatsApp. |
| CAF:L067 | REQUISITO PROPUESTO | - Por qué P3: valor alto pero depende de datos limpios de las historias 1 y 2. |
| CAF:L068 | REQUISITO PROPUESTO | - Prueba independiente: con 4 semanas de datos, la orden sugerida cubre la demanda sin quiebres ni sobre-stock superior al 15 %. |
| CAF:L069 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| CAF:L070 | REQUISITO PROPUESTO | 1. Dado stock bajo mínimo proyectado a 7 días, cuando corre el agente, entonces envía una propuesta de orden con cantidades y costo estimado para aprobar. |
| CAF:L071 | REQUISITO PROPUESTO | 2. Dada una anulación de venta superior a 3 veces el promedio diario, cuando ocurre, entonces el administrador recibe alerta con detalle en menos de 1 minuto. |
| CAF:L072 | REQUISITO PROPUESTO | 3. Dada una propuesta no aprobada en 48 horas, cuando vence, entonces el agente la archiva y lo registra en el ledger. |
| CAF:L074 | REQUISITO PROPUESTO | **Casos borde** |
| CAF:L076 | REQUISITO PROPUESTO | - Caída de internet en el local: el pedido tomado por QR debe quedar en cola y la caja seguir operando en modo degradado. |
| CAF:L077 | REQUISITO PROPUESTO | - Mesa que se junta o se divide a mitad del servicio. |
| CAF:L078 | REQUISITO PROPUESTO | - Cliente que cierra el navegador antes de pagar: el pedido sigue en cocina y pasa a cobro en caja. |
| CAF:L079 | REQUISITO PROPUESTO | - Rechazo de boleta por el SII (folio agotado o certificado vencido): el pago no se revierte; la boleta se reintenta y se alerta. |
| CAF:L080 | REQUISITO PROPUESTO | - Producto de la carta sin receta cargada: se vende, pero el margen se marca como «sin costo» y aparece en el dashboard. |
| CAF:L082 | HECHO DOCUMENTADO | ## 3. Requisitos (obligatorio) |
| CAF:L084 | HECHO DOCUMENTADO | **Requisitos funcionales** |
| CAF:L086 | HECHO DOCUMENTADO | &#124; ID &#124; El sistema DEBE &#124; Historia &#124; |
| CAF:L088 | REQUISITO PROPUESTO | &#124; FR-001 &#124; Generar un QR único por mesa que abra la carta digital existente sin instalar app &#124; H1 &#124; |
| CAF:L089 | REQUISITO PROPUESTO | &#124; FR-002 &#124; Permitir pedidos individuales y compartidos por mesa, con edición hasta el envío a cocina &#124; H1 &#124; |
| CAF:L090 | REQUISITO PROPUESTO | &#124; FR-003 &#124; Mostrar cada pedido en una pantalla de cocina (KDS) con mesa, hora y estado &#124; H1 &#124; |
| CAF:L091 | REQUISITO PROPUESTO | &#124; FR-004 &#124; Cobrar por Webpay/Transbank y Mercado Pago, con división de cuenta por ítem o por partes iguales &#124; H1 &#124; |
| CAF:L092 | REQUISITO PROPUESTO | &#124; FR-005 &#124; Emitir boleta electrónica SII al confirmar cada pago y entregarla por WhatsApp, correo o QR &#124; H1 &#124; |
| CAF:L093 | REQUISITO PROPUESTO | &#124; FR-006 &#124; Mantener operación de caja en modo degradado sin internet y sincronizar al reconectar &#124; H1 &#124; |
| CAF:L094 | REQUISITO PROPUESTO | &#124; FR-007 &#124; Registrar compras y gastos desde foto de factura o carga manual, con estado pendiente/aprobado &#124; H2 &#124; |
| CAF:L095 | REQUISITO PROPUESTO | &#124; FR-008 &#124; Descontar insumos por receta en cada venta y mantener stock proyectado &#124; H2 &#124; |
| CAF:L096 | REQUISITO PROPUESTO | &#124; FR-009 &#124; Calcular margen por producto, por día y por franja horaria, y exponerlo en un dashboard &#124; H2 &#124; |
| CAF:L097 | REQUISITO PROPUESTO | &#124; FR-010 &#124; Importar el histórico de ventas y stock desde la exportación a Excel de eleventa &#124; H2 &#124; |
| CAF:L098 | REQUISITO PROPUESTO | &#124; FR-011 &#124; Proponer órdenes de compra con cantidades y costo estimado, para aprobación humana por WhatsApp &#124; H3 &#124; |
| CAF:L099 | REQUISITO PROPUESTO | &#124; FR-012 &#124; Alertar anulaciones, descuentos o mermas fuera de patrón en menos de 1 minuto &#124; H3 &#124; |
| CAF:L100 | REQUISITO PROPUESTO | &#124; FR-013 &#124; Registrar toda acción de agente en un ledger inmutable con evidencia y aprobador &#124; H3 &#124; |
| CAF:L101 | REQUISITO PROPUESTO | &#124; FR-014 &#124; Operar sobre el core compartido (identidad, catálogo, transacciones, pagos, gastos) sin duplicarlo &#124; Todas &#124; |
| CAF:L103 | HECHO DOCUMENTADO | **Entidades clave** |
| CAF:L105 | HECHO DOCUMENTADO | - Mesa: identificador, QR, estado (libre, ocupada, por cerrar), pedidos asociados. |
| CAF:L106 | HECHO DOCUMENTADO | - Pedido: mesa, comensal, ítems, estado (borrador, enviado, preparado, servido), pagos. |
| CAF:L107 | HECHO DOCUMENTADO | - Producto y Receta: producto de carta, insumos con cantidades, costo calculado. |
| CAF:L108 | HECHO DOCUMENTADO | - Insumo y Movimiento de stock: unidad, stock actual, entradas por compra, salidas por venta o merma. |
| CAF:L109 | HECHO DOCUMENTADO | - Compra y Gasto: proveedor, documento, líneas, estado de aprobación. |
| CAF:L110 | HECHO DOCUMENTADO | - Pago y Documento tributario: medio, monto, estado, folio SII, canal de entrega. |
| CAF:L111 | HECHO DOCUMENTADO | - Acción de agente: tipo, propuesta, aprobador, resultado, evidencia. |
| CAF:L113 | HECHO DOCUMENTADO | ## 4. Criterios de éxito (obligatorio) |
| CAF:L115 | HECHO DOCUMENTADO | Medibles, agnósticos de tecnología, verificables sin leer código. |
| CAF:L117 | HECHO DOCUMENTADO | &#124; ID &#124; Resultado medible &#124; |
| CAF:L119 | REQUISITO PROPUESTO | &#124; SC-001 &#124; El 90 % de los pedidos por QR llegan a cocina en menos de 5 segundos &#124; |
| CAF:L120 | REQUISITO PROPUESTO | &#124; SC-002 &#124; El tiempo de cierre de cuenta por mesa baja al menos 30 % frente a la medición previa con eleventa &#124; |
| CAF:L121 | REQUISITO PROPUESTO | &#124; SC-003 &#124; El 100 % de los pagos aprobados tienen boleta SII emitida en menos de 30 segundos &#124; |
| CAF:L122 | REQUISITO PROPUESTO | &#124; SC-004 &#124; El margen por producto calculado difiere menos del 2 % del cálculo manual mensual &#124; |
| CAF:L123 | REQUISITO PROPUESTO | &#124; SC-005 &#124; El inventario proyectado difiere menos del 5 % del conteo físico semanal &#124; |
| CAF:L124 | REQUISITO PROPUESTO | &#124; SC-006 &#124; Las órdenes sugeridas por el agente evitan quiebres de stock en al menos el 95 % de los insumos críticos &#124; |
| CAF:L125 | REQUISITO PROPUESTO | &#124; SC-007 &#124; Cero acciones de agente sin registro en el ledger (auditoría mensual) &#124; |
| CAF:L126 | REQUISITO PROPUESTO | &#124; SC-008 &#124; El administrador obtiene el dashboard diario sin planilla manual en menos de 1 minuto &#124; |
| CAF:L128 | SUPUESTO | ## 5. Supuestos, dependencias y clarificaciones |
| CAF:L130 | SUPUESTO | **Supuestos** |
| CAF:L132 | SUPUESTO | - La carta digital existente es editable y exportable (JSON o similar); si no, se migra una vez. |
| CAF:L133 | SUPUESTO | - Eleventa convive en V1 solo como caja de respaldo; el histórico sale por su exportación a Excel. |
| CAF:L134 | SUPUESTO | - Un solo local, una cocina, hasta 30 mesas; no hay delivery en V1. |
| CAF:L135 | SUPUESTO | - Hay conexión a internet estable con fallos ocasionales menores a 30 minutos. |
| CAF:L137 | SUPUESTO | **Dependencias** |
| CAF:L139 | SUPUESTO | - Core compartido: identidad, catálogo, transacciones, pagos, gastos (feature `000-core`). |
| CAF:L140 | SUPUESTO | - Certificado digital SII del contribuyente y contrato Webpay Plus o Mercado Pago activos. |
| CAF:L141 | SUPUESTO | - Cuenta WhatsApp Business API para entrega de boleta y aprobaciones del agente. |
| CAF:L143 | SUPUESTO | **Clarificaciones pendientes** (para `/speckit.clarify`) |
| CAF:L145 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿El cliente paga antes de recibir (modelo café) o después (modelo restaurante)? Cambia el flujo de H1. |
| CAF:L146 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Propina incluida en el flujo de pago y con qué porcentaje por defecto? |
| CAF:L147 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Quién aprueba compras: dueño, administrador o ambos según monto? |
| CAF:L148 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Se reemplaza eleventa en V1 o convive? Define si FR-006 es caja propia o puente. |
| CAF:L149 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Cuenta personal del cliente (perfil persistente) o solo pago por sesión de mesa? |
| CAF:L150 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Proveedores con catálogo digital para la orden de compra o solo WhatsApp? |
| CAF:L152 | REQUISITO PROPUESTO | ## 6. Plan técnico resumido (vista previa de `plan.md`) |
| CAF:L154 | REQUISITO PROPUESTO | Lo que sigue es la propuesta para `/speckit.plan`; la decisión final queda en `plan.md` tras `research.md`. |
| CAF:L156 | REQUISITO PROPUESTO | **Contexto técnico** |
| CAF:L158 | REQUISITO PROPUESTO | - Lenguaje y framework: Python 3.12 + FastAPI para el core y la API; Next.js para carta QR, KDS y dashboard; PostgreSQL 16 como almacenamiento; Redis para cola de pedidos y modo degradado. |
| CAF:L159 | REQUISITO PROPUESTO | - Agentes: Claude Agent SDK con herramientas MCP sobre el core (stock, ventas, compras) y servidor MCP propio para Webpay y SII. |
| CAF:L160 | REQUISITO PROPUESTO | - Integraciones: Transbank Webpay Plus, Mercado Pago, SII (boleta electrónica vía proveedor certificado o integración directa), WhatsApp Business API. |
| CAF:L161 | REQUISITO PROPUESTO | - Pruebas: pytest + Playwright; escenarios Given/When/Then de §2 como suite de aceptación. |
| CAF:L162 | REQUISITO PROPUESTO | - Plataforma objetivo: web responsive; tablet en cocina; sin app nativa. |
| CAF:L163 | REQUISITO PROPUESTO | - Rendimiento: pedido a cocina en menos de 5 s; dashboard diario en menos de 1 s para 1 año de datos. |
| CAF:L164 | REQUISITO PROPUESTO | - Escala: 1 local, 30 mesas, 500 pedidos al día; diseño multi-tenant para los siguientes. |
| CAF:L166 | REQUISITO PROPUESTO | **Chequeo de constitución** |
| CAF:L168 | REQUISITO PROPUESTO | &#124; Principio &#124; Cumple &#124; Nota &#124; |
| CAF:L170 | REQUISITO PROPUESTO | &#124; Core primero &#124; Sí &#124; Mesa, Pedido y Receta son de la vertical; todo lo demás es core &#124; |
| CAF:L171 | REQUISITO PROPUESTO | &#124; Chile es requisito &#124; Sí &#124; SII y Webpay en H1 &#124; |
| CAF:L172 | REQUISITO PROPUESTO | &#124; Agente con reglas &#124; Sí &#124; H3 solo propone; aprobación humana por WhatsApp &#124; |
| CAF:L173 | REQUISITO PROPUESTO | &#124; Seguridad desde la spec &#124; Pendiente &#124; Modelo de amenazas de QR y pagos antes de `/speckit.tasks` &#124; |
| CAF:L174 | REQUISITO PROPUESTO | &#124; Test primero &#124; Sí &#124; Escenarios de §2 &#124; |
| CAF:L175 | REQUISITO PROPUESTO | &#124; Simplicidad &#124; Sí &#124; Una app vertical sobre el core; sin microservicios &#124; |
| CAF:L177 | REQUISITO PROPUESTO | **Estructura** |
| CAF:L180 | REQUISITO PROPUESTO | plataforma-salman/ |
| CAF:L181 | REQUISITO PROPUESTO | core/            # identidad, catálogo, transacciones, pagos, gastos, analítica |
| CAF:L182 | REQUISITO PROPUESTO | verticales/cafeteria/ |
| CAF:L183 | REQUISITO PROPUESTO | api/           # mesas, pedidos, recetas, KDS |
| CAF:L184 | REQUISITO PROPUESTO | web/           # carta QR, KDS, dashboard |
| CAF:L185 | REQUISITO PROPUESTO | agentes/       # reposición, anomalías |
| CAF:L186 | REQUISITO PROPUESTO | specs/001-cafeteria-mesas-pos/ |
| CAF:L187 | REQUISITO PROPUESTO | spec.md  plan.md  research.md  data-model.md  contracts/  quickstart.md  tasks.md  checklists/ |
| CAF:L190 | HECHO DOCUMENTADO | ## 7. Próximos comandos y entregables por fase |
| CAF:L192 | HECHO DOCUMENTADO | 1. `/speckit.constitution` con los seis principios de §1 → `.specify/memory/constitution.md` (una vez, compartida). |
| CAF:L193 | HECHO DOCUMENTADO | 2. `/speckit.specify` con §2 a §5 como entrada → `spec.md` + `checklists/requirements.md`. |
| CAF:L194 | HECHO DOCUMENTADO | 3. `/speckit.clarify` → responder las seis preguntas de §5 y actualizar la spec. |
| CAF:L195 | HECHO DOCUMENTADO | 4. `/speckit.plan` con §6 como entrada → `plan.md`, `research.md` (SII, Webpay, WhatsApp API), `data-model.md`, `contracts/` (OpenAPI de mesas, pedidos, pagos), `quickstart.md`. |
| CAF:L196 | HECHO DOCUMENTADO | 5. `/speckit.checklist` → lista de calidad para pagos y SII; el revisor marca. |
| CAF:L197 | HECHO DOCUMENTADO | 6. `/speckit.tasks` → `tasks.md` por historia: Setup → Fundacional → H1 → H2 → H3 → Pulido. |
| CAF:L198 | HECHO DOCUMENTADO | 7. `/speckit.analyze` → corregir conflictos en la fuente y repetir. |
| CAF:L199 | HECHO DOCUMENTADO | 8. `/speckit.implement` por fase (H1 primero, demo en local real). |
| CAF:L200 | HECHO DOCUMENTADO | 9. `/speckit.converge` hasta que no agregue tareas; pentest de la capa agéntica antes del cierre. |
| HOT:L001 | HECHO DOCUMENTADO | # Spec SDD 02: Hotel (reservas, operación y concierge agéntico) |
| HOT:L003 | HECHO DOCUMENTADO | Oct 15, 2026 · @Cristóbal Herrera |
| HOT:L005 | HECHO DOCUMENTADO | ## 0. Flujo spec-kit aplicado |
| HOT:L007 | HECHO DOCUMENTADO | Este documento es el `spec.md` de la feature `002-hotel-reservas-concierge`, segunda vertical sobre el core compartido. Sigue la ruta completa de [spec-kit](https://github.github.com/spec-kit/quickstart.html) (`constitution` → `specify` → `clarify` → `plan` → `checklist` → `tasks` → `analyze` → `implement` → `converge`) y reutiliza la constitución versión 1.0.0 definida en el Spec SDD 01 (Cafetería); no se redefine aquí. La spec dice qué y por qué; la tecnología va en `plan.md`. |
| HOT:L009 | HECHO DOCUMENTADO | Precondición de esta feature: el core (`000-core`) y el módulo de pedidos de la cafetería (`001`) están en producción, porque el servicio a la habitación los reutiliza. |
| HOT:L011 | REQUISITO PROPUESTO | ## 2. Escenarios de usuario y pruebas (obligatorio) |
| HOT:L013 | REQUISITO PROPUESTO | La P1 reemplaza la dispersión actual con un solo punto de verdad para reservas; P2 y P3 construyen la operación y el agente sobre ese dato. |
| HOT:L015 | REQUISITO PROPUESTO | **Historia 1 (P1): Reservar y pagar desde la web del hotel** |
| HOT:L017 | REQUISITO PROPUESTO | Un huésped entra a la web, ve disponibilidad y tarifa real, reserva, paga con Webpay o Mercado Pago y recibe confirmación y boleta SII. El inventario se actualiza en todos los canales (Booking, Airbnb) sin intervención manual. |
| HOT:L019 | REQUISITO PROPUESTO | - Por qué P1: hoy todo está disperso; la reserva directa con inventario único es la base de todo lo demás y reduce comisión OTA. |
| HOT:L020 | REQUISITO PROPUESTO | - Prueba independiente: dos reservas simultáneas de la última habitación no generan sobreventa; el calendario de Booking refleja el cambio en menos de 5 minutos. |
| HOT:L021 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| HOT:L022 | REQUISITO PROPUESTO | 1. Dadas fechas y número de huéspedes, cuando el visitante consulta, entonces ve solo habitaciones disponibles con tarifa vigente y total con IVA. |
| HOT:L023 | REQUISITO PROPUESTO | 2. Dada una reserva con pago aprobado, cuando Webpay confirma, entonces se emite confirmación por correo y WhatsApp y boleta SII en menos de 60 segundos. |
| HOT:L024 | REQUISITO PROPUESTO | 3. Dada una reserva directa confirmada, cuando el channel manager sincroniza, entonces la disponibilidad baja en todos los canales conectados en menos de 5 minutos. |
| HOT:L025 | REQUISITO PROPUESTO | 4. Dada una reserva de Booking, cuando llega por el canal, entonces aparece en el PMS propio con los mismos datos y bloquea inventario. |
| HOT:L027 | REQUISITO PROPUESTO | **Historia 2 (P2): Operar la estadía: check-in digital, pedidos a la habitación y housekeeping** |
| HOT:L029 | REQUISITO PROPUESTO | El huésped hace check-in desde el celular antes de llegar (datos, documento, pago pendiente), pide servicios a la habitación con el mismo módulo de pedidos de la cafetería y el personal ve tareas de limpieza y mantención por habitación. |
| HOT:L031 | REQUISITO PROPUESTO | - Por qué P2: convierte la reserva en operación; reutiliza el módulo de pedidos ya probado en `001`. |
| HOT:L032 | REQUISITO PROPUESTO | - Prueba independiente: un huésped completa check-in, pide desayuno a la habitación y lo recibe cargado a su cuenta sin pasar por recepción. |
| HOT:L033 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| HOT:L034 | REQUISITO PROPUESTO | 1. Dado un check-in online completo, cuando el huésped llega, entonces recepción solo entrega la llave y el registro queda firmado. |
| HOT:L035 | REQUISITO PROPUESTO | 2. Dado un pedido a la habitación, cuando se confirma, entonces aparece en cocina con número de habitación y se carga a la cuenta del huésped. |
| HOT:L036 | REQUISITO PROPUESTO | 3. Dado un check-out, cuando la habitación se libera, entonces se crea la tarea de limpieza y la habitación no vuelve a estar disponible hasta que se cierre. |
| HOT:L037 | REQUISITO PROPUESTO | 4. Dado un cargo pendiente al check-out, cuando el huésped paga, entonces se emite boleta o factura por el total de la estadía. |
| HOT:L039 | REQUISITO PROPUESTO | **Historia 3 (P3): Concierge agéntico por WhatsApp con reglas de autonomía** |
| HOT:L041 | REQUISITO PROPUESTO | Un agente atiende por el WhatsApp del hotel: responde, cotiza, reserva, modifica fechas dentro de reglas, vende upsells con link de pago y escala a un humano cuando sale de su límite. Toda acción queda en el ledger. |
| HOT:L043 | REQUISITO PROPUESTO | - Por qué P3: es el diferenciador frente a la industria (sección 2 del estado del arte), pero depende del PMS propio (H1) y la operación (H2). |
| HOT:L044 | REQUISITO PROPUESTO | - Prueba independiente: 50 conversaciones de prueba resueltas sin humano en al menos el 70 % y cero cambios fuera de reglas. |
| HOT:L045 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| HOT:L046 | REQUISITO PROPUESTO | 1. Dada una consulta de disponibilidad por WhatsApp, cuando el agente responde, entonces cotiza con tarifa real y ofrece link de pago en menos de 30 segundos. |
| HOT:L047 | REQUISITO PROPUESTO | 2. Dado un cambio de fechas dentro de la política (sin penalidad), cuando el huésped lo pide, entonces el agente lo ejecuta en el PMS y confirma. |
| HOT:L048 | REQUISITO PROPUESTO | 3. Dado un cambio con penalidad o cancelación, cuando se solicita, entonces el agente escala a recepción con el contexto completo y no actúa. |
| HOT:L049 | REQUISITO PROPUESTO | 4. Dada una reserva pagada 48 horas antes de llegar, cuando corre el agente, entonces ofrece un upsell (late check-out, desayuno) con link de pago. |
| HOT:L051 | REQUISITO PROPUESTO | **Casos borde** |
| HOT:L053 | REQUISITO PROPUESTO | - Reserva doble por carrera entre canal directo y OTA: gana la primera confirmada; la segunda se relocaliza y se avisa. |
| HOT:L054 | REQUISITO PROPUESTO | - Pago aprobado pero boleta rechazada por SII: la reserva se mantiene, la boleta se reintenta y se alerta. |
| HOT:L055 | REQUISITO PROPUESTO | - Huésped sin documento válido en check-in online: el registro queda incompleto y se exige en recepción. |
| HOT:L056 | REQUISITO PROPUESTO | - Agente que recibe lenguaje ofensivo o solicitud ambigua: cierra con escalamiento, nunca inventa tarifa. |
| HOT:L057 | REQUISITO PROPUESTO | - Caída del channel manager: la web propia sigue vendiendo con inventario local y marca conflicto al reconectar. |
| HOT:L059 | HECHO DOCUMENTADO | ## 3. Requisitos (obligatorio) |
| HOT:L061 | HECHO DOCUMENTADO | **Requisitos funcionales** |
| HOT:L063 | HECHO DOCUMENTADO | &#124; ID &#124; El sistema DEBE &#124; Historia &#124; |
| HOT:L065 | REQUISITO PROPUESTO | &#124; FR-001 &#124; Mantener un inventario único de habitaciones con tarifas por fecha, ocupación y política de cancelación &#124; H1 &#124; |
| HOT:L066 | REQUISITO PROPUESTO | &#124; FR-002 &#124; Exponer un motor de reservas en la web propia con disponibilidad real y pago en línea &#124; H1 &#124; |
| HOT:L067 | REQUISITO PROPUESTO | &#124; FR-003 &#124; Sincronizar disponibilidad y reservas con al menos Booking y Airbnb en ambos sentidos &#124; H1 &#124; |
| HOT:L068 | REQUISITO PROPUESTO | &#124; FR-004 &#124; Cobrar por Webpay/Transbank o Mercado Pago y emitir boleta o factura SII por cada pago &#124; H1 &#124; |
| HOT:L069 | REQUISITO PROPUESTO | &#124; FR-005 &#124; Impedir sobreventa ante reservas concurrentes del mismo inventario &#124; H1 &#124; |
| HOT:L070 | REQUISITO PROPUESTO | &#124; FR-006 &#124; Permitir check-in online con datos del huésped, documento y firma de registro &#124; H2 &#124; |
| HOT:L071 | REQUISITO PROPUESTO | &#124; FR-007 &#124; Reutilizar el módulo de pedidos del core para servicio a la habitación, con cargo a la cuenta del huésped &#124; H2 &#124; |
| HOT:L072 | REQUISITO PROPUESTO | &#124; FR-008 &#124; Generar y cerrar tareas de housekeeping y mantención por habitación y estado &#124; H2 &#124; |
| HOT:L073 | REQUISITO PROPUESTO | &#124; FR-009 &#124; Consolidar todos los cargos de la estadía en una cuenta y liquidarla al check-out &#124; H2 &#124; |
| HOT:L074 | REQUISITO PROPUESTO | &#124; FR-010 &#124; Atender por WhatsApp Business con un agente que consulta y escribe en el PMS vía API &#124; H3 &#124; |
| HOT:L075 | REQUISITO PROPUESTO | &#124; FR-011 &#124; Aplicar reglas de autonomía configurables: acciones permitidas, montos máximos, casos que escalan &#124; H3 &#124; |
| HOT:L076 | REQUISITO PROPUESTO | &#124; FR-012 &#124; Ofrecer upsells con link de pago en momentos definidos (pre-llegada, estadía, salida) &#124; H3 &#124; |
| HOT:L077 | REQUISITO PROPUESTO | &#124; FR-013 &#124; Registrar cada acción del agente en el ledger inmutable con evidencia de la conversación &#124; H3 &#124; |
| HOT:L078 | REQUISITO PROPUESTO | &#124; FR-014 &#124; Exponer disponibilidad y tarifas por un servidor MCP para agentes externos (modelo SiteMinder) &#124; H3 &#124; |
| HOT:L079 | REQUISITO PROPUESTO | &#124; FR-015 &#124; Operar sobre el core compartido (identidad, catálogo, transacciones, pagos, gastos) sin duplicarlo &#124; Todas &#124; |
| HOT:L081 | HECHO DOCUMENTADO | **Entidades clave** |
| HOT:L083 | HECHO DOCUMENTADO | - Habitación y Tipo de habitación: capacidad, servicios, estado operativo (disponible, ocupada, limpieza, bloqueada). |
| HOT:L084 | HECHO DOCUMENTADO | - Tarifa y Plan tarifario: por fecha, ocupación, canal, política de cancelación. |
| HOT:L085 | HECHO DOCUMENTADO | - Reserva: huésped, habitaciones, fechas, canal de origen, estado, pagos, cuenta. |
| HOT:L086 | HECHO DOCUMENTADO | - Huésped: identidad, documento, preferencias, historial. |
| HOT:L087 | HECHO DOCUMENTADO | - Cuenta de estadía: cargos (alojamiento, pedidos, upsells), pagos, documentos tributarios. |
| HOT:L088 | HECHO DOCUMENTADO | - Tarea operativa: tipo (limpieza, mantención), habitación, responsable, estado. |
| HOT:L089 | HECHO DOCUMENTADO | - Canal: conector (directo, Booking, Airbnb), estado de sincronización, conflictos. |
| HOT:L090 | HECHO DOCUMENTADO | - Acción de agente: conversación, regla aplicada, acción, aprobador, resultado. |
| HOT:L092 | HECHO DOCUMENTADO | ## 4. Criterios de éxito (obligatorio) |
| HOT:L094 | HECHO DOCUMENTADO | &#124; ID &#124; Resultado medible &#124; |
| HOT:L096 | REQUISITO PROPUESTO | &#124; SC-001 &#124; Cero sobreventas en 90 días de operación con al menos dos canales activos &#124; |
| HOT:L097 | REQUISITO PROPUESTO | &#124; SC-002 &#124; La disponibilidad se refleja en todos los canales en menos de 5 minutos en el 95 % de los cambios &#124; |
| HOT:L098 | REQUISITO PROPUESTO | &#124; SC-003 &#124; Las reservas directas pasan del nivel actual a al menos 30 % del total en 6 meses &#124; |
| HOT:L099 | REQUISITO PROPUESTO | &#124; SC-004 &#124; El 100 % de los pagos tienen boleta o factura SII emitida en menos de 60 segundos &#124; |
| HOT:L100 | REQUISITO PROPUESTO | &#124; SC-005 &#124; El 60 % de los huéspedes completa check-in online antes de llegar &#124; |
| HOT:L101 | REQUISITO PROPUESTO | &#124; SC-006 &#124; El agente resuelve al menos el 70 % de conversaciones de WhatsApp sin intervención humana &#124; |
| HOT:L102 | REQUISITO PROPUESTO | &#124; SC-007 &#124; Cero acciones del agente fuera de sus reglas de autonomía (auditoría mensual del ledger) &#124; |
| HOT:L103 | REQUISITO PROPUESTO | &#124; SC-008 &#124; Los upsells ofrecidos por el agente convierten al menos el 8 % (referencia Duve) &#124; |
| HOT:L104 | REQUISITO PROPUESTO | &#124; SC-009 &#124; Un empleado nuevo opera recepción con el sistema tras 2 horas de capacitación &#124; |
| HOT:L106 | SUPUESTO | ## 5. Supuestos, dependencias y clarificaciones |
| HOT:L108 | SUPUESTO | **Supuestos** |
| HOT:L110 | SUPUESTO | - Hotel de menos de 50 habitaciones, un solo edificio, sin PMS actual o con uno que se abandona. |
| HOT:L111 | SUPUESTO | - Los canales OTA relevantes son Booking y Airbnb; otros se agregan después. |
| HOT:L112 | SUPUESTO | - La cocina y el servicio a la habitación comparten operación con la cafetería o replican su módulo. |
| HOT:L113 | SUPUESTO | - Recepción opera con horario; fuera de horario el agente es el primer contacto. |
| HOT:L115 | SUPUESTO | **Dependencias** |
| HOT:L117 | SUPUESTO | - Core (`000-core`) y módulo de pedidos (`001`) en producción. |
| HOT:L118 | DECISIÓN PENDIENTE | - Channel manager propio o integrado (evaluar en `research.md`: construir conector vs. contratar uno con API). |
| HOT:L119 | SUPUESTO | - Certificado SII, contrato Webpay Plus, cuenta WhatsApp Business API con plantillas aprobadas. |
| HOT:L120 | SUPUESTO | - Credenciales de partner de Booking y Airbnb (requieren proceso de certificación). |
| HOT:L122 | SUPUESTO | **Clarificaciones pendientes** (para `/speckit.clarify`) |
| HOT:L124 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Cuántas habitaciones y tipos tiene el hotel, y hay temporada alta definida? Define tarifas y escala. |
| HOT:L125 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Qué canales usan hoy y con qué volumen? Define el alcance de FR-003. |
| HOT:L126 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Existe PMS actual con datos a migrar o se parte de cero? |
| HOT:L127 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Política de cancelación y de cobro anticipado (total, parcial, garantía)? |
| HOT:L128 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Se emite factura a empresas con frecuencia? Define si FR-004 incluye factura desde V1. |
| HOT:L129 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Límite monetario del agente para ejecutar sin aprobación (por ejemplo, cambios sin penalidad hasta X pesos)? |
| HOT:L130 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Housekeeping con personal propio o externo? Define acceso y notificaciones. |
| HOT:L132 | REQUISITO PROPUESTO | ## 6. Plan técnico resumido (vista previa de `plan.md`) |
| HOT:L134 | REQUISITO PROPUESTO | **Contexto técnico** |
| HOT:L136 | REQUISITO PROPUESTO | - Misma base que `001`: Python 3.12 + FastAPI, Next.js, PostgreSQL 16, Redis; se agrega un worker de sincronización de canales con cola y reintentos. |
| HOT:L137 | REQUISITO PROPUESTO | - Agentes: Claude Agent SDK con herramientas MCP sobre el PMS propio (disponibilidad, reservas, cuenta) y servidor MCP público de solo lectura para distribución (FR-014). |
| HOT:L138 | REQUISITO PROPUESTO | - Integraciones: Transbank Webpay Plus, Mercado Pago, SII, WhatsApp Business API, Booking Connectivity API y Airbnb API (o channel manager intermedio según `research.md`). |
| HOT:L139 | REQUISITO PROPUESTO | - Pruebas: pytest + Playwright; pruebas de concurrencia para FR-005; conversaciones de prueba versionadas para H3. |
| HOT:L140 | REQUISITO PROPUESTO | - Rendimiento: consulta de disponibilidad en menos de 1 s; sincronización de canales en menos de 5 min; respuesta del agente en menos de 30 s. |
| HOT:L141 | REQUISITO PROPUESTO | - Escala: 50 habitaciones, 200 reservas al mes, 1.000 conversaciones al mes; multi-propiedad en el modelo de datos. |
| HOT:L143 | REQUISITO PROPUESTO | **Chequeo de constitución** |
| HOT:L145 | REQUISITO PROPUESTO | &#124; Principio &#124; Cumple &#124; Nota &#124; |
| HOT:L147 | REQUISITO PROPUESTO | &#124; Core primero &#124; Sí &#124; Habitación, Tarifa, Reserva y Canal son de la vertical; identidad, pagos, pedidos y cuenta vienen del core &#124; |
| HOT:L148 | REQUISITO PROPUESTO | &#124; Chile es requisito &#124; Sí &#124; SII y Webpay en H1; factura según clarificación &#124; |
| HOT:L149 | REQUISITO PROPUESTO | &#124; Agente con reglas &#124; Sí &#124; FR-011 define autonomía; cancelaciones siempre escalan &#124; |
| HOT:L150 | REQUISITO PROPUESTO | &#124; Seguridad desde la spec &#124; Pendiente &#124; Modelo de amenazas: datos de huéspedes (Ley 21.719), credenciales OTA, prompt injection vía WhatsApp &#124; |
| HOT:L151 | REQUISITO PROPUESTO | &#124; Test primero &#124; Sí &#124; Escenarios de §2 y pruebas de concurrencia &#124; |
| HOT:L152 | REQUISITO PROPUESTO | &#124; Simplicidad &#124; Con justificación &#124; El worker de canales es un proceso aparte por aislamiento de fallos; se registra en Complexity Tracking &#124; |
| HOT:L154 | REQUISITO PROPUESTO | **Estructura** |
| HOT:L157 | REQUISITO PROPUESTO | plataforma-salman/ |
| HOT:L158 | REQUISITO PROPUESTO | core/ |
| HOT:L159 | REQUISITO PROPUESTO | verticales/hotel/ |
| HOT:L160 | REQUISITO PROPUESTO | api/           # habitaciones, tarifas, reservas, cuenta de estadía, housekeeping |
| HOT:L161 | REQUISITO PROPUESTO | web/           # motor de reservas, check-in online, recepción, dashboard |
| HOT:L162 | REQUISITO PROPUESTO | canales/       # worker de sincronización Booking / Airbnb |
| HOT:L163 | REQUISITO PROPUESTO | agentes/       # concierge WhatsApp, upsell, servidor MCP de distribución |
| HOT:L164 | REQUISITO PROPUESTO | specs/002-hotel-reservas-concierge/ |
| HOT:L165 | REQUISITO PROPUESTO | spec.md  plan.md  research.md  data-model.md  contracts/  quickstart.md  tasks.md  checklists/ |
| HOT:L168 | HECHO DOCUMENTADO | ## 7. Próximos comandos y entregables por fase |
| HOT:L170 | HECHO DOCUMENTADO | 1. `/speckit.specify` con §2 a §5 → `spec.md` + `checklists/requirements.md` (la constitución ya existe). |
| HOT:L171 | HECHO DOCUMENTADO | 2. `/speckit.clarify` → responder las siete preguntas de §5; la de canales y la de PMS actual son bloqueantes para el plan. |
| HOT:L172 | HECHO DOCUMENTADO | 3. `/speckit.plan` con §6 → `plan.md`; `research.md` decide construir conector vs. channel manager con API; `data-model.md`; `contracts/` (OpenAPI de reservas, cuenta, MCP de distribución); `quickstart.md`. |
| HOT:L173 | HECHO DOCUMENTADO | 4. `/speckit.checklist` → lista de calidad para sobreventa, pagos y reglas del agente. |
| HOT:L174 | HECHO DOCUMENTADO | 5. `/speckit.tasks` → `tasks.md`: Setup → Fundacional (inventario y tarifas) → H1 → H2 → H3 → Pulido. |
| HOT:L175 | HECHO DOCUMENTADO | 6. `/speckit.analyze` → corregir y repetir. |
| HOT:L176 | HECHO DOCUMENTADO | 7. `/speckit.implement` por fase; H1 con un canal real antes de sumar el segundo. |
| HOT:L177 | HECHO DOCUMENTADO | 8. `/speckit.converge` hasta convergencia; pentest del agente (prompt injection por WhatsApp, fuga de datos de huéspedes) antes del cierre. |
| INM:L001 | HECHO DOCUMENTADO | # Spec SDD 03: Inmobiliaria y constructora (plataforma comercial y control de obra) |
| INM:L003 | HECHO DOCUMENTADO | Oct 15, 2026 · @Cristóbal Herrera |
| INM:L005 | HECHO DOCUMENTADO | ## 0. Flujo spec-kit aplicado y división en dos features |
| INM:L007 | HECHO DOCUMENTADO | Este documento es el `spec.md` de la feature `003-inmobiliaria-comercial`; el control de obra se especifica aparte como `004-constructora-obra`, porque son dos negocios con usuarios, datos y ritmo distintos, y spec-kit trabaja una feature a la vez (`.specify/feature.json`). La ruta completa de [spec-kit](https://github.github.com/spec-kit/quickstart.html) aplica igual que en 01 y 02; la constitución versión 1.0.0 del Spec SDD 01 se reutiliza sin cambios. |
| INM:L009 | HECHO DOCUMENTADO | &#124; Feature &#124; Alcance &#124; Prioridad &#124; Depende de &#124; |
| INM:L011 | HECHO DOCUMENTADO | &#124; `003-inmobiliaria-comercial` (este doc) &#124; Leads, cotización, reserva, promesa, cobranza, postventa &#124; V1 &#124; `000-core` &#124; |
| INM:L012 | HECHO DOCUMENTADO | &#124; `004-constructora-obra` &#124; Presupuesto, avance, subcontratos, compras, inspección &#124; V2 &#124; `003` (unidades y proyectos) y lo ya construido en inspección de terreno y control de obra &#124; |
| INM:L014 | HECHO DOCUMENTADO | La historia P3 de este doc (asistente de obra ligero) es el puente mínimo hacia `004`; no pretende reemplazarla. |
| INM:L016 | REQUISITO PROPUESTO | ## 2. Escenarios de usuario y pruebas (obligatorio) |
| INM:L018 | REQUISITO PROPUESTO | La P1 ordena el dato fragmentado (Excel, WhatsApp, portales) en un solo flujo de lead a promesa; sin eso ningún agente puede actuar con permisos claros (brecha e del estado del arte). |
| INM:L020 | REQUISITO PROPUESTO | **Historia 1 (P1): De lead a promesa en un solo flujo** |
| INM:L022 | REQUISITO PROPUESTO | Un interesado llega por web, portal o WhatsApp; un agente lo califica (presupuesto, plazo, financiamiento), agenda la visita y lo entrega al ejecutivo. El ejecutivo cotiza desde el stock real de unidades, el cliente reserva con pago en línea y firma la promesa electrónicamente. |
| INM:L024 | REQUISITO PROPUESTO | - Por qué P1: es el ciclo de ingresos; hoy no hay agente nativo en ningún CRM chileno y la cotización y la promesa son manuales. |
| INM:L025 | REQUISITO PROPUESTO | - Prueba independiente: un lead de prueba recorre calificación, visita, cotización, reserva pagada y promesa firmada sin planilla externa, en menos de 48 horas de tiempo de proceso. |
| INM:L026 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| INM:L027 | REQUISITO PROPUESTO | 1. Dado un mensaje de WhatsApp de un interesado, cuando el agente responde, entonces en menos de 2 minutos tiene presupuesto, plazo y tipo de unidad y propone horario de visita. |
| INM:L028 | REQUISITO PROPUESTO | 2. Dada una unidad disponible, cuando el ejecutivo genera cotización, entonces el documento sale con precio vigente, pie, financiamiento estimado y vence a una fecha. |
| INM:L029 | REQUISITO PROPUESTO | 3. Dada una cotización aceptada, cuando el cliente paga la reserva por Webpay, entonces la unidad queda bloqueada y se emite boleta o comprobante. |
| INM:L030 | REQUISITO PROPUESTO | 4. Dada una reserva pagada, cuando se envía la promesa, entonces el cliente firma electrónicamente y el documento queda archivado con la unidad. |
| INM:L032 | REQUISITO PROPUESTO | **Historia 2 (P2): Cobranza y postventa con agente** |
| INM:L034 | REQUISITO PROPUESTO | Tras la promesa, el sistema controla el calendario de pagos del pie, recuerda cuotas por WhatsApp, concilia pagos y, tras la entrega, recibe y gestiona solicitudes de postventa con un agente que clasifica, asigna y hace seguimiento. |
| INM:L036 | REQUISITO PROPUESTO | - Por qué P2: cobranza y postventa son el dolor crónico de las inmobiliarias chilenas y ningún proveedor local tiene IA en postventa. |
| INM:L037 | REQUISITO PROPUESTO | - Prueba independiente: 20 clientes con cuotas pendientes reciben recordatorios, 10 solicitudes de postventa se clasifican y asignan sin intervención manual. |
| INM:L038 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| INM:L039 | REQUISITO PROPUESTO | 1. Dada una cuota que vence en 5 días, cuando corre el agente, entonces envía recordatorio con monto y link de pago, y registra la gestión. |
| INM:L040 | REQUISITO PROPUESTO | 2. Dado un pago recibido, cuando se concilia, entonces el estado de la cuota cambia y el cliente recibe comprobante. |
| INM:L041 | REQUISITO PROPUESTO | 3. Dada una solicitud de postventa por WhatsApp con foto, cuando el agente la recibe, entonces la clasifica (urgente, garantía, no cubierta), la asigna y responde plazo estimado. |
| INM:L042 | REQUISITO PROPUESTO | 4. Dada una solicitud sin respuesta del responsable en 72 horas, cuando vence, entonces el agente escala al jefe de postventa. |
| INM:L044 | REQUISITO PROPUESTO | **Historia 3 (P3): Asistente de obra ligero: avance y compras para la constructora mediana** |
| INM:L046 | REQUISITO PROPUESTO | El jefe de obra reporta avance por WhatsApp (texto, foto, voz); el asistente lo estructura contra el presupuesto por partida, detecta desvíos y prepara solicitudes de compra que el administrador aprueba. |
| INM:L048 | REQUISITO PROPUESTO | - Por qué P3: Procore y ALICE son enterprise sin precio público; una constructora mediana necesita algo que funcione desde WhatsApp. Es el puente hacia `004`. |
| INM:L049 | REQUISITO PROPUESTO | - Prueba independiente: 4 semanas de reportes diarios producen una curva de avance por partida con desvío calculado, y 5 solicitudes de compra aprobadas por WhatsApp. |
| INM:L050 | REQUISITO PROPUESTO | - Escenarios de aceptación: |
| INM:L051 | REQUISITO PROPUESTO | 1. Dado un reporte por voz del jefe de obra, cuando el asistente lo procesa, entonces registra partida, porcentaje de avance y evidencia fotográfica con fecha y ubicación. |
| INM:L052 | REQUISITO PROPUESTO | 2. Dado un avance inferior al programado en más de 10 %, cuando se calcula, entonces se alerta al administrador con la partida y el impacto estimado. |
| INM:L053 | REQUISITO PROPUESTO | 3. Dada una necesidad de material declarada, cuando el asistente prepara la solicitud de compra, entonces incluye cantidad, proveedor habitual y precio de referencia, y espera aprobación. |
| INM:L055 | REQUISITO PROPUESTO | **Casos borde** |
| INM:L057 | REQUISITO PROPUESTO | - Dos ejecutivos cotizan la misma unidad: la primera reserva pagada bloquea; la otra cotización se invalida y se avisa. |
| INM:L058 | REQUISITO PROPUESTO | - Lead que contacta por dos canales: se fusiona en un solo registro, sin duplicar seguimiento. |
| INM:L059 | REQUISITO PROPUESTO | - Pago de reserva aprobado y promesa no firmada en el plazo: la unidad se libera con aviso y el pago se reembolsa según política. |
| INM:L060 | REQUISITO PROPUESTO | - Solicitud de postventa fuera de garantía: el agente responde con la política, no la rechaza solo. |
| INM:L061 | REQUISITO PROPUESTO | - Reporte de obra contradictorio con el anterior (avance que retrocede): se marca para revisión humana, no se sobreescribe. |
| INM:L063 | HECHO DOCUMENTADO | ## 3. Requisitos (obligatorio) |
| INM:L065 | HECHO DOCUMENTADO | **Requisitos funcionales** |
| INM:L067 | HECHO DOCUMENTADO | &#124; ID &#124; El sistema DEBE &#124; Historia &#124; |
| INM:L069 | REQUISITO PROPUESTO | &#124; FR-001 &#124; Capturar leads desde web, portales (Portalinmobiliario, TOCTOC, Yapo) y WhatsApp en un solo registro deduplicado &#124; H1 &#124; |
| INM:L070 | REQUISITO PROPUESTO | &#124; FR-002 &#124; Calificar leads por WhatsApp con un agente (presupuesto, plazo, financiamiento, tipo de unidad) y agendar visitas en la agenda del ejecutivo &#124; H1 &#124; |
| INM:L071 | REQUISITO PROPUESTO | &#124; FR-003 &#124; Mantener el stock de unidades por proyecto con precio vigente, estado (disponible, reservada, promesada, escriturada) y bloqueo por reserva &#124; H1 &#124; |
| INM:L072 | REQUISITO PROPUESTO | &#124; FR-004 &#124; Generar cotizaciones con precio, pie, financiamiento estimado y vencimiento, trazables al lead y a la unidad &#124; H1 &#124; |
| INM:L073 | REQUISITO PROPUESTO | &#124; FR-005 &#124; Cobrar la reserva por Webpay/Transbank o Mercado Pago y emitir el documento tributario que corresponda &#124; H1 &#124; |
| INM:L074 | REQUISITO PROPUESTO | &#124; FR-006 &#124; Enviar la promesa de compraventa a firma electrónica (Ley 19.799) y archivarla con la unidad &#124; H1 &#124; |
| INM:L075 | REQUISITO PROPUESTO | &#124; FR-007 &#124; Administrar el calendario de pagos del pie, enviar recordatorios por WhatsApp con link de pago y conciliar pagos &#124; H2 &#124; |
| INM:L076 | REQUISITO PROPUESTO | &#124; FR-008 &#124; Recibir solicitudes de postventa por WhatsApp y web, clasificarlas con un agente, asignarlas y seguir plazos con escalamiento &#124; H2 &#124; |
| INM:L077 | REQUISITO PROPUESTO | &#124; FR-009 &#124; Exponer al cliente un portal con su unidad, pagos, documentos y solicitudes &#124; H2 &#124; |
| INM:L078 | REQUISITO PROPUESTO | &#124; FR-010 &#124; Registrar avance de obra por partida desde WhatsApp (texto, voz, foto) con fecha, ubicación y evidencia &#124; H3 &#124; |
| INM:L079 | REQUISITO PROPUESTO | &#124; FR-011 &#124; Comparar avance real contra programado y presupuesto por partida, y alertar desvíos superiores a un umbral configurable &#124; H3 &#124; |
| INM:L080 | REQUISITO PROPUESTO | &#124; FR-012 &#124; Preparar solicitudes de compra con cantidad, proveedor y precio de referencia, para aprobación humana &#124; H3 &#124; |
| INM:L081 | REQUISITO PROPUESTO | &#124; FR-013 &#124; Registrar toda acción de agente en el ledger inmutable con evidencia y aprobador &#124; Todas &#124; |
| INM:L082 | REQUISITO PROPUESTO | &#124; FR-014 &#124; Operar sobre el core compartido (identidad, catálogo, transacciones, pagos, gastos) sin duplicarlo &#124; Todas &#124; |
| INM:L084 | HECHO DOCUMENTADO | **Entidades clave** |
| INM:L086 | HECHO DOCUMENTADO | - Proyecto: nombre, ubicación, etapas, unidades, estado comercial y de obra. |
| INM:L087 | HECHO DOCUMENTADO | - Unidad: tipo, superficie, precio vigente, estado, reserva, promesa, escritura. |
| INM:L088 | HECHO DOCUMENTADO | - Lead y Cliente: origen, canal, calificación, ejecutivo, historial de contacto. |
| INM:L089 | HECHO DOCUMENTADO | - Cotización: unidad, precio, pie, financiamiento, vencimiento, estado. |
| INM:L090 | HECHO DOCUMENTADO | - Reserva y Promesa: pagos, documentos firmados, plazos. |
| INM:L091 | HECHO DOCUMENTADO | - Calendario de pagos y Cuota: monto, vencimiento, estado, conciliación. |
| INM:L092 | HECHO DOCUMENTADO | - Solicitud de postventa: unidad, tipo, clasificación, responsable, plazo, estado. |
| INM:L093 | HECHO DOCUMENTADO | - Partida de obra y Reporte de avance: presupuesto, programado, real, evidencia. |
| INM:L094 | HECHO DOCUMENTADO | - Solicitud de compra: partida, material, cantidad, proveedor, aprobador. |
| INM:L095 | HECHO DOCUMENTADO | - Acción de agente: conversación, regla, acción, aprobador, resultado. |
| INM:L097 | HECHO DOCUMENTADO | ## 4. Criterios de éxito (obligatorio) |
| INM:L099 | HECHO DOCUMENTADO | &#124; ID &#124; Resultado medible &#124; |
| INM:L101 | REQUISITO PROPUESTO | &#124; SC-001 &#124; El 100 % de los leads de todos los canales queda en un solo registro en menos de 5 minutos &#124; |
| INM:L102 | REQUISITO PROPUESTO | &#124; SC-002 &#124; El tiempo de primera respuesta a un lead baja a menos de 2 minutos, 24/7 &#124; |
| INM:L103 | REQUISITO PROPUESTO | &#124; SC-003 &#124; Al menos el 60 % de los leads calificados agenda visita sin intervención del ejecutivo &#124; |
| INM:L104 | REQUISITO PROPUESTO | &#124; SC-004 &#124; El tiempo de lead a promesa firmada baja al menos 30 % frente al proceso actual &#124; |
| INM:L105 | REQUISITO PROPUESTO | &#124; SC-005 &#124; Cero unidades vendidas dos veces (auditoría trimestral) &#124; |
| INM:L106 | REQUISITO PROPUESTO | &#124; SC-006 &#124; La morosidad de cuotas del pie baja al menos 20 % en 6 meses &#124; |
| INM:L107 | REQUISITO PROPUESTO | &#124; SC-007 &#124; El 90 % de las solicitudes de postventa recibe clasificación y plazo en menos de 1 hora &#124; |
| INM:L108 | REQUISITO PROPUESTO | &#124; SC-008 &#124; El avance de obra por partida está disponible sin planilla y con desvío calculado el mismo día del reporte &#124; |
| INM:L109 | REQUISITO PROPUESTO | &#124; SC-009 &#124; Cero acciones de agente fuera de reglas (auditoría mensual del ledger) &#124; |
| INM:L111 | SUPUESTO | ## 5. Supuestos, dependencias y clarificaciones |
| INM:L113 | SUPUESTO | **Supuestos** |
| INM:L115 | SUPUESTO | - Inmobiliaria y constructora son del mismo grupo; comparten proyectos y unidades, pero tienen usuarios distintos. |
| INM:L116 | SUPUESTO | - Hay entre 1 y 5 proyectos activos con menos de 200 unidades en total. |
| INM:L117 | SUPUESTO | - Los ejecutivos comerciales usan WhatsApp como canal principal; los portales inmobiliarios entregan leads por correo o API. |
| INM:L118 | SUPUESTO | - La escrituración y el crédito hipotecario siguen fuera del sistema en V1 (solo se registran hitos). |
| INM:L120 | SUPUESTO | **Dependencias** |
| INM:L122 | SUPUESTO | - Core (`000-core`) en producción. |
| INM:L123 | DECISIÓN PENDIENTE | - Proveedor de firma electrónica avanzada con API (evaluar en `research.md`). |
| INM:L124 | SUPUESTO | - Credenciales de portales para captura de leads; cuenta WhatsApp Business API; contrato Webpay Plus; certificado SII. |
| INM:L125 | SUPUESTO | - Para H3: presupuesto por partida en formato digital (Excel estructurado o itemizado) y lo construido en inspección de terreno y control de obra. |
| INM:L127 | SUPUESTO | **Clarificaciones pendientes** (para `/speckit.clarify`) |
| INM:L129 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Cuántos proyectos y unidades activas hoy, y en qué etapa (verde, blanco, entrega)? |
| INM:L130 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Qué CRM o planillas usan hoy y qué historial se migra? |
| INM:L131 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿La reserva es con pago en línea obligatorio o se acepta transferencia? Afecta FR-005 y el bloqueo de unidad. |
| INM:L132 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Quién redacta y aprueba la promesa (abogado interno o externo) y cuál es el plazo máximo entre reserva y promesa? |
| INM:L133 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Política de postventa: plazos de garantía por tipo de falla y responsables? |
| INM:L134 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿La constructora ejecuta solo obras propias o también para terceros? Afecta el alcance de `004`. |
| INM:L135 | DECISIÓN PENDIENTE | - [ ] &#91;NEEDS CLARIFICATION\] ¿Límite monetario para que el asistente prepare compras sin revisión del administrador? |
| INM:L137 | REQUISITO PROPUESTO | ## 6. Plan técnico resumido (vista previa de `plan.md`) |
| INM:L139 | REQUISITO PROPUESTO | **Contexto técnico** |
| INM:L141 | REQUISITO PROPUESTO | - Misma base que `001` y `002`: Python 3.12 + FastAPI, Next.js, PostgreSQL 16, Redis. Se agrega almacenamiento de documentos (promesas, fotos de obra) con cifrado en reposo. |
| INM:L142 | REQUISITO PROPUESTO | - Agentes: Claude Agent SDK con herramientas MCP sobre leads, unidades, cotizaciones, cuotas y solicitudes; agente de calificación, agente de cobranza, agente de postventa, asistente de obra (voz a texto para reportes). |
| INM:L143 | REQUISITO PROPUESTO | - Integraciones: WhatsApp Business API, Transbank Webpay Plus, Mercado Pago, SII, firma electrónica avanzada, conectores de portales (correo parseado o API), calendario de ejecutivos. |
| INM:L144 | REQUISITO PROPUESTO | - Pruebas: pytest + Playwright; conversaciones versionadas para cada agente; pruebas de concurrencia para el bloqueo de unidades. |
| INM:L145 | REQUISITO PROPUESTO | - Rendimiento: primera respuesta del agente en menos de 2 min; cotización generada en menos de 10 s; portal de cliente en menos de 1 s. |
| INM:L146 | REQUISITO PROPUESTO | - Escala: 5 proyectos, 200 unidades, 500 leads al mes, 50 solicitudes de postventa al mes. |
| INM:L148 | REQUISITO PROPUESTO | **Chequeo de constitución** |
| INM:L150 | REQUISITO PROPUESTO | &#124; Principio &#124; Cumple &#124; Nota &#124; |
| INM:L152 | REQUISITO PROPUESTO | &#124; Core primero &#124; Sí &#124; Proyecto, Unidad, Cotización, Promesa, Partida son de la vertical; identidad, pagos, gastos y ledger del core &#124; |
| INM:L153 | REQUISITO PROPUESTO | &#124; Chile es requisito &#124; Sí &#124; Webpay, SII y firma electrónica Ley 19.799 en H1 &#124; |
| INM:L154 | REQUISITO PROPUESTO | &#124; Agente con reglas &#124; Sí &#124; Calificación y recordatorios autónomos; cotización, promesa, compras y rechazo de garantía requieren humano &#124; |
| INM:L155 | REQUISITO PROPUESTO | &#124; Seguridad desde la spec &#124; Pendiente &#124; Datos financieros y de identidad de compradores (Ley 21.719); documentos firmados; prompt injection por WhatsApp &#124; |
| INM:L156 | REQUISITO PROPUESTO | &#124; Test primero &#124; Sí &#124; Escenarios de §2 &#124; |
| INM:L157 | REQUISITO PROPUESTO | &#124; Simplicidad &#124; Con justificación &#124; Cuatro agentes en lugar de uno: cada uno tiene reglas y permisos distintos; se registra en Complexity Tracking &#124; |
| INM:L159 | REQUISITO PROPUESTO | **Estructura** |
| INM:L162 | REQUISITO PROPUESTO | plataforma-salman/ |
| INM:L163 | REQUISITO PROPUESTO | core/ |
| INM:L164 | REQUISITO PROPUESTO | verticales/inmobiliaria/ |
| INM:L165 | REQUISITO PROPUESTO | api/           # proyectos, unidades, leads, cotizaciones, promesas, cuotas, postventa |
| INM:L166 | REQUISITO PROPUESTO | web/           # panel comercial, portal de cliente, dashboard |
| INM:L167 | REQUISITO PROPUESTO | agentes/       # calificacion, cobranza, postventa, asistente-obra |
| INM:L168 | REQUISITO PROPUESTO | verticales/constructora/   # feature 004, V2 |
| INM:L169 | REQUISITO PROPUESTO | specs/003-inmobiliaria-comercial/ |
| INM:L170 | REQUISITO PROPUESTO | spec.md  plan.md  research.md  data-model.md  contracts/  quickstart.md  tasks.md  checklists/ |
| INM:L173 | HECHO DOCUMENTADO | ## 7. Próximos comandos y entregables por fase |
| INM:L175 | HECHO DOCUMENTADO | 1. `/speckit.specify` con §2 a §5 → `spec.md` + `checklists/requirements.md`. |
| INM:L176 | HECHO DOCUMENTADO | 2. `/speckit.clarify` → responder las siete preguntas de §5; la de proyectos activos y la de reserva con pago son bloqueantes. |
| INM:L177 | HECHO DOCUMENTADO | 3. `/speckit.plan` con §6 → `plan.md`; `research.md` decide proveedor de firma electrónica y método de captura de portales; `data-model.md`; `contracts/` (OpenAPI de leads, unidades, cotizaciones, cuotas, postventa); `quickstart.md`. |
| INM:L178 | HECHO DOCUMENTADO | 4. `/speckit.checklist` → lista de calidad para bloqueo de unidades, promesa y reglas de los cuatro agentes. |
| INM:L179 | HECHO DOCUMENTADO | 5. `/speckit.tasks` → `tasks.md`: Setup → Fundacional (proyectos y unidades) → H1 → H2 → H3 → Pulido. |
| INM:L180 | HECHO DOCUMENTADO | 6. `/speckit.analyze` → corregir y repetir. |
| INM:L181 | HECHO DOCUMENTADO | 7. `/speckit.implement` por fase; H1 con un proyecto real y un ejecutivo piloto. |
| INM:L182 | HECHO DOCUMENTADO | 8. `/speckit.converge` hasta convergencia; pentest de agentes antes del cierre. |
| INM:L183 | HECHO DOCUMENTADO | 9. Abrir `004-constructora-obra` con `/speckit.specify` cuando H3 lleve 4 semanas en operación. |
