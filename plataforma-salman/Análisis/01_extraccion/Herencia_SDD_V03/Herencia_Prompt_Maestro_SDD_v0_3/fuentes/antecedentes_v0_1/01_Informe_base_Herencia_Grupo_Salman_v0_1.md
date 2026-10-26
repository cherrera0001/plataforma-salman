# Plataforma integral del Grupo Salman
## Hotel Herencia: base de diseño y construcción con IA y agentes
**Versión 0.1 | 23 de octubre de 2026 | Inicio operativo objetivo: 1 de enero de 2027**

### Decisión propuesta
Construir una plataforma propia, modular y multiempresa. Comenzar por un sistema hotelero completo en sus procesos esenciales y conectar servicios externos especializados para distribución, pagos y documentos tributarios. La propiedad del código, los datos, las cuentas y el repositorio debe quedar bajo control del grupo. El desarrollo, la documentación y las pruebas se organizarán mediante agentes de IA; las decisiones empresariales y autorizaciones sensibles seguirán siendo humanas.

El resultado buscado no es digitalizar planillas independientes: es registrar una operación una sola vez y hacer que reservas, recepción, habitaciones, personas, limpieza, lavandería, alimentación, compras, personal y finanzas utilicen ese mismo registro. Cada cifra del tablero debe permitir llegar al documento y al evento que la explican.

## 1. Contexto confirmado y fronteras del proyecto
El Hotel Herencia tiene 17 habitaciones, con configuraciones que incluyen dobles y triples, cada una con baño. Existen cocina y baños comunes y una sala de estar utilizable para eventos o trabajo. El alojamiento incluye desayuno; algunas cenas se subcontratan. La recepción funciona las 24 horas. Herencia SpA explota el hotel y Cafetería Fadwa. La administración directa del hotel se retomará el 1 de enero de 2027, después del arriendo iniciado en 2020 a Paulo Huepe. Estos son antecedentes entregados por Ricardo Salman.

La secuencia de ampliación será hotel, cafetería, inmobiliarias, inversiones y matriz. El núcleo compartido se define desde el primer módulo: sociedades, establecimientos, centros de costo, usuarios, proveedores, cuentas, documentos y auditoría. No se deben construir aplicaciones inconexas para intentar unirlas al final.

### Estructura societaria
Distinguir siempre cuatro dimensiones: propiedad jurídica, operación comercial, propiedad de los activos y consolidación de gestión. Un grupo de socios comunes no convierte automáticamente todas las sociedades en filiales de Wembé ni permite mezclar sus cuentas bancarias.

El organigrama de 2018 contiene estos porcentajes históricos, que deben permanecer fechados y pendientes de validación documental para 2027:

| Relación | Participación histórica | Evidencia |
| --- | --- | --- |
| Ricardo / Sandra en Wembé | 50% / 50% | Hoja1, M12:M13 |
| Wembé / Ricardo en Inmobiliaria Salman | 99,5% / 0,5% | Hoja1, M23:M24 |
| Inmobiliaria Salman en Asaí, Azzam, Sirari y Yabal | 99,5% en cada una | Hoja1, K27:K30 y filas 40:41 |
| Inmobiliaria Salman en Valencia y Cía. | 99% | Hoja1, K31 y X40:X41 |
| Ricardo / Sandra en SB Inversiones | 72,66% / 27,34% | Hoja1, T13:T14 |
| Ricardo / Sandra en Constructora Salman y Herencia | 50% / 50% en ambas | Hoja1, Z13:Z14 y AE13:AE14 |

El mismo archivo incluye otras sociedades, como Farmacia Herencia y Autopark San Jorge; su presencia histórica no determina su vigencia ni su incorporación al alcance actual. La plataforma almacenará porcentajes, clases de participación, vigencias, documentos de respaldo y derechos de control separados. La consolidación contable legal no se deducirá solamente del porcentaje.

## 2. Lo que aportan los 15 archivos
Se revisaron las estructuras y datos de 15 libros, con 255 hojas entre formularios, registros y variantes. Los documentos sirven para reconstruir la operación, pero no reemplazan la toma de inventario, las tarifas, los contratos ni las reservas vigentes al traspaso.

| Grupo documental | Hallazgo | Consecuencia para el diseño |
| --- | --- | --- |
| Ocupación: noviembre 2019 y enero-marzo 2020 | Capacidad diaria de 17; distinción directo/Booking; marzo tiene captura parcial | Separar habitaciones-noche, personas-noche, canal y calidad de dato. Ausencia de registro no es ocupación cero. |
| Exportación Booking septiembre | 105 reservas: 79 Stayed, 13 No-Show y 13 Cancelled; comisión 17% en las filas | Importar identificadores externos, estado original y normalizado; conservar importe original, final y comisión. |
| Valores de habitaciones | Tarifas por configuración y ocupantes; pesos/dólares; IVA, canal y promociones mezclados en columnas | Separar precio, ocupación, impuesto, descuento y comisión; todo con fecha de vigencia. |
| Inventarios generales | Entradas, salidas, proveedor, factura, existencia en bodega y en área | Crear movimientos, transferencias y recepciones verificables; no trasladar una hoja por día al sistema. |
| Bebidas y golosinas | Control de existencias y ventas; el libro de bebidas conserva un título de golosinas | Catálogo único de productos con categoría y unidad; importar por contenido, no solamente por nombre de archivo. |
| Lavandería | Sábanas, fundas, cobertores y toallas; saldos y movimientos agregados | Agregar habitación, estadía, responsable, lote, estado, recepción y costo de lavado. |
| Retiros de caja | Resumen mensual de retiros, no un cierre integral de caja | Registrar cobros, salidas, depósitos, responsable y arqueos sin confundir retiros con gastos. |
| Sueldos enero 2019 | Filas con seis cargos de recepcionista y tres de mucama; también plantillas ajenas a hotelería | Son cargos históricos, no una dotación actual. Recuperar conceptos, no tasas ni fórmulas antiguas. |

### Alertas verificables
En la hoja "Lunes 25" de tarifas, el encabezado de I4 habla de 25% para Genius, pero I5 utiliza 10%. La planilla menciona 15% en otro encabezado, mientras el reporte de Booking contiene 17%. No son reglas que deban copiarse literalmente: podrían mezclar descuentos al cliente con comisiones del canal.

Los inventarios de septiembre y octubre presentan #REF! en I66 e I117 de "Inv- PEDIDOS". El libro de sueldos contiene referencias rotas y búsquedas sin resultado. "Nomina Inventarios Junio" identifica JULIO 2019 dentro del libro y contiene una hoja "31-6". Son razones para validar fechas y correspondencias, no para descartar todo el conocimiento operativo.

En ocupación, noviembre 2019 suma 193 habitaciones-noche sobre 510 posibles (37,84%); enero 2020, 294/527 (55,79%); febrero 2020, 330/493 (66,94%). Marzo sólo tiene 17 días con entradas numéricas completas y no constituye una ocupación mensual comparable. Son cálculos sobre estas planillas, no previsiones para 2027.

## 3. Mercado: qué existe y qué conviene construir
Las siguientes son capacidades publicadas por sus proveedores, no resultados de una prueba contratada. No se atribuye a una solución facturación chilena, acceso API irrestricto o cobertura bancaria sin confirmación específica.

| Solución | Referencia útil | Evaluación para Herencia |
| --- | --- | --- |
| Cloudbeds | PMS, motor de reservas, canales y ecosistema de integraciones [S01] | Buena referencia de integración hotelera. Precio por cotización; validar pagos y documentos en Chile. |
| Little Hotelier | Calendario, recepción, venta directa, canales y limpieza [S02] | Referencia de sencillez para un hotel pequeño. La tarifa para 17 habitaciones requiere configuración/cotización. |
| Mews | Operación hotelera, pagos, POS, limpieza y espacios reservables [S04] | Útil para el futuro enlace hotel-cafetería y sala de trabajo. Cotización y alcance local pendientes. |
| Amenitiz | PMS, web, reservas, canales y pagos [S03] | Referencia funcional; su enfoque declarado es europeo. No se presume disponibilidad completa para Chile. |
| LobbyPMS | Reservas, POS, inventarios, compras y API [S05-S06] | Cercano a la integración operativa buscada. La página de precios marca funciones como lavandería/housekeeping en desarrollo; no asumirlas listas. La facturación publicada no acredita SII chileno. |
| SiteMinder | Distribución e integración con PMS [S07-S08] | Candidato para conectividad, sujeto a aceptación, integración, certificación y contrato. No es sustituto de la plataforma del grupo. |
| Channex | API de canales para sistemas propios y proveedores tecnológicos [S09-S10] | Candidato técnico para un sistema propio. Base USD 130/mes + USD 7/hotel: USD 137/mes antes de impuestos y extras. El proveedor advierte que para un solo hotel un channel manager comercial puede resultar más económico. Comparar antes de elegir. |

### La ventaja propia
La oportunidad no consiste en afirmar que ningún PMS hace inventarios o limpieza. Consiste en unir exactamente los procesos de Herencia y del grupo: costo de la habitación y de la estadía, trabajo realizado por persona, ropa utilizada y lavada, desayuno servido, compra de insumos, recepción, deuda a proveedor, cobro y abono bancario. La malla societaria y los resultados por negocio completan esa diferencia.

### Construir / integrar / aplazar
Construir el modelo propio de reservas, operación, inventarios, costos, personal, conciliación y gestión multiempresa. Integrar conectividad de canales, pasarela de pagos y emisión tributaria. Aplazar automatización publicitaria, precios autónomos, biometría, cerraduras inteligentes y una liquidación legal de remuneraciones escrita desde cero.

Booking indica que no acepta conexiones directas de propiedades individuales y recomienda un channel manager [S11]. Construir con IA no elimina requisitos contractuales, certificaciones ni autorizaciones. Se debe validar una prueba de conectividad antes de hacer depender el lanzamiento de ella.

## 4. Arquitectura funcional y de datos
### Una base común, módulos separados
Propuesta inicial: aplicación web adaptable a celular, con un monolito modular y base de datos transaccional. Para esta escala, dividir tempranamente todo en microservicios aumenta los puntos de falla y la coordinación entre agentes. Los módulos tendrán contratos internos claros y adaptadores externos reemplazables.

La base común debe contener Grupo, Sociedad, ParticipaciónSocietaria con vigencia, Establecimiento, UnidadNegocio, CentroCosto, Persona, Contraparte, Usuario, Rol, CuentaBancaria, Documento, EventoAuditoria y ReglaAprobacion. El registro de personas y contrapartes puede compartirse sólo dentro de los permisos y finalidades autorizados; no implica acceso indiscriminado a datos de huéspedes o trabajadores.

El módulo hotelero necesita Habitacion, TipoHabitacion, ConfiguracionCamas, Capacidad, PlanTarifa, PoliticaCancelacion, Canal, Reserva, LineaReserva, AsignacionHabitacion, Huesped, Estadia, Cargo, Anticipo, Pago, AplicacionPago, Devolucion, DocumentoTributario y CierreDiario. Una reserva puede agrupar varias habitaciones y una habitación varios pasajeros. Cambiar de habitación no debe crear otra venta.

El módulo operativo agrega Tarea, AsignacionTarea, Inspeccion, Incidencia, OrdenMantenimiento, ArticuloTextil, LoteLavanderia, Producto, UnidadMedida, Bodega, MovimientoInventario, Receta, ServicioComida, Compra, RecepcionCompra, CuentaPorPagar, Turno, Asistencia, ReglaIncentivo y CostoAsignado.

Finanzas vincula cargo comercial, documento, pago, liquidación del proveedor de pagos y movimiento bancario. Estas entidades no deben fundirse. Una transferencia agrupada puede pagar varias reservas y una reserva puede recibir varios pagos.

### Estados que nunca deben confundirse
Estado comercial de la reserva: cotizada, retenida temporalmente, pendiente de garantía, confirmada, cancelada o no presentada. Estado de estadía: prevista, alojada, terminada. Estado de cuenta: pendiente, parcial, pagada o con saldo a devolver. Estado de limpieza: sucia, asignada, en limpieza, inspección, lista. Estado técnico: operativa o fuera de servicio.

La disponibilidad de venta futura depende del inventario y de las asignaciones por fecha; la entrega inmediata de una habitación depende, además, de su estado físico y de limpieza. Una habitación sucia hoy no necesariamente debe desaparecer de la oferta de todos los meses futuros.

### Reglas estructurales
Cada transacción debe tener sociedad, establecimiento, unidad, responsable, fecha de servicio, fecha de registro, moneda e identificador estable. Las horas se guardarán con zona horaria y presentación America/Santiago; no con un desplazamiento fijo. Los intervalos de noches se modelarán con entrada incluida y salida excluida. Precios y tipos de cambio históricos no se recalcularán con valores posteriores.

Los importes se manejarán con decimales exactos o unidades monetarias enteras según corresponda, nunca con aproximaciones de punto flotante para registrar dinero. Cambios y anulaciones dejarán reversos y evidencia; no se borrarán cobros cerrados para hacer cuadrar la caja.

## 5. Programa del hotel por áreas
### Captación, redes y reservas
Primera versión: enlaces desde Instagram, Facebook, Google y WhatsApp hacia una reserva directa adaptable a celular; identificación de campaña; disponibilidad, precio total, condiciones, pago y confirmación. Un mensaje en redes no será una reserva confirmada. Publicar contenido, gestionar anuncios y responder automáticamente requiere una etapa posterior y permisos específicos.

El calendario debe mostrar 17 habitaciones, tipos, capacidad, bloqueos, entradas, salidas, cambios, grupos, empresas, anticipos y saldo. Las cotizaciones deben expirar; el último cupo necesita protección frente a reservas simultáneas. Las reservas externas no se pueden descartar silenciosamente aunque generen una discrepancia de inventario.

### Recepción y huéspedes
Registrar titular, pasajeros efectivos, empresa pagadora, contactos necesarios, llegada y salida, requisitos del alojamiento y documentación aplicable. Admitir check-in parcial de grupos, extensiones, cambios de habitación, pagos divididos y facturación a empresa. La recepción debe recibir alertas sin acceder a remuneraciones ni a cuentas de otras sociedades.

### Caja, cobros y documentos
Separar anticipo, garantía, ingreso ganado por alojamiento, documento tributario, cobro recibido y abono bancario. Llevar caja por turno y medio de pago, arqueos, gastos autorizados, retiros, diferencias, cierre y reapertura aprobada. El estado de pago online se confirma contra el proveedor en el servidor, no por la imagen de un comprobante ni por el regreso del navegador [S14].

La emisión tributaria debe asociarse al RUT correcto y al proveedor habilitado. La exención hotelera para turistas extranjeros tiene requisitos; no basta la nacionalidad [S17]. El contador debe aprobar reglas de impuestos, anticipos, exportación, documentos y tratamiento de comprobantes de pago antes de producir documentos reales.

### Aseo y mantenimiento
Crear automáticamente tareas por salida, permanencia, limpieza profunda y áreas comunes. Registrar asignación, ejecutor, inicio, término, checklist, insumos, incidencias e inspección. No exigir fotos invasivas de pertenencias de huéspedes. El supervisor libera la habitación; el registro de calidad no debe premiar sólo rapidez.

Mantenimiento contempla equipos, avisos, trabajos preventivos, repuestos, proveedor, costo, garantía y bloqueos de inventario con fecha. Incorporar objetos olvidados, entrega documentada de llaves y bitácora de incidencias como operaciones separadas.

### Ropa de cama y lavandería
Estados: limpia disponible, asignada, usada, enviada a lavado, recibida, rechazada, dañada y dada de baja. Para 17 habitaciones, comenzar con conteos por tipo y lote, no con identificación individual de cada toalla. Registrar piezas efectivamente cambiadas, no presumir que toda noche genera lavado de todas las piezas. Relacionar el lote con habitaciones o estadías cuando exista evidencia; los costos estimados se mostrarán como estimados.

### Desayunos, cenas y sala común
La ocupación prevista genera la previsión de desayunos; el servicio efectivo genera consumo o merma. Llevar recetas, porciones, restricciones alimentarias estrictamente necesarias y proveedores. El desayuno incluido no se vuelve a contabilizar como venta externa. Si lo produce Cafetería Fadwa bajo la misma sociedad, se trata de asignación interna de costo entre unidades; si interviene otro RUT, se aplica un tratamiento distinto validado por contabilidad.

Para cenas subcontratadas: solicitud, confirmación, precio al huésped, costo del proveedor, entrega, cargo y cuenta por pagar. La sala requiere calendario por horas, capacidad, montaje, limpieza, condiciones y reglas de convivencia con el hotel. No se cuenta como habitación número 18.

### Compras e inventarios
Circuito: solicitud, aprobación, orden, recepción parcial/total, documento del proveedor, cuenta por pagar y pago conciliado. El pago no confirma que los productos llegaron. Incluir unidad de compra y de consumo, conversiones, lotes, vencimientos, ubicaciones, mermas, ajustes autorizados y transferencias a pisos o cocina. Alertas de reposición basadas en stock, consumo y ocupación futura.

### Personas, turnos e incentivos
Definir puestos, cobertura, disponibilidad, vacaciones, ausencias, reemplazos, turnos, asistencia, horas aprobadas y tareas verificadas. La jornada ordinaria general pasa a 42 horas desde el 26 de abril de 2026 [S16]; las condiciones específicas, descansos y sistemas aplicables al hotel requieren revisión laboral. Una cobertura de recepción continua exige 168 horas semanales: cuatro jornadas de 42 horas sólo cubren aritméticamente el puesto, sin resolver colaciones, feriados, vacaciones, licencias ni reemplazos.

Los incentivos deben considerar carga y calidad: tipo de tarea, dificultad, retrabajo, verificación y trabajo compartido. La regla, sus topes y vigencia serán aprobados. La IA puede proponer; no modifica remuneraciones ni sanciona. Primera etapa: preliquidación y exportación a un sistema o proceso remuneracional validado, no reutilización de tasas de 2019.

## 6. Conciliación, costos y tablero
### Cuatro comprobaciones distintas
1. Reserva y estadía contra cargos por servicios efectivamente prestados.
2. Cargos y documentos contra anticipos, cobros, devoluciones y cuentas por cobrar.
3. Cobros contra liquidaciones de tarjetas/Booking y comisiones correspondientes.
4. Liquidaciones o transferencias contra movimientos reales del banco.

La conciliación comenzará con cartolas y reportes importados con identificadores, hash de archivo, vista previa y detección de duplicados. Después podrá conectarse un proveedor bancario autorizado. Fintoc publica una oferta de movimientos bancarios para Chile; su cobertura, frecuencia, permisos, seguridad y costo deben verificarse para las cuentas concretas [S13]. No se pedirán claves bancarias en un chat ni se programará scraping de sesiones privadas.

La conciliación debe admitir relaciones uno-a-muchos y muchos-a-uno, comisiones, fechas de abono posteriores, retenciones, diferencias cambiarias y contracargos. Una coincidencia solamente por monto no basta para cerrar automáticamente. Los ingresos no identificados permanecen en una bandeja de excepciones.

### Rentabilidad explicable
Mostrar margen de contribución por reserva, habitación, tipo, canal y empresa cliente: ingreso de servicios sin impuestos recaudados, menos descuentos, comisiones y costos directos atribuibles. Mostrar aparte resultado operativo luego de costos comunes. Mantener diferentes vistas: ingreso devengado, documentos emitidos, recaudación y caja bancaria. Nunca sumarlas como si fueran ventas distintas.

La lavandería propia se puede costear por lote, piezas o kilos con una regla aprobada; el personal por minutos o una base razonable. Agua, energía y costos comunes se asignan con un criterio visible y estable. No presentar distribuciones estimadas como mediciones exactas ni cargar dos veces la misma mano de obra dentro de lavandería y de costos de personal.

### Indicadores obligatorios
Ocupación comercial y física con denominadores visibles; habitaciones fuera de servicio; personas-noche; tarifa media y RevPAR con definición de impuestos y servicios; ingreso por canal y comisión efectiva; anticipo, saldo y antigüedad; cobros no conciliados; tiempo de habitación sucia a lista; tareas e inspecciones; piezas lavadas y costo; desayunos previstos/servidos; consumos y mermas; stock crítico; compras pendientes; costo de personal y margen por estadía.

La ocupación sobre 17 habitaciones físicas y la ocupación sobre habitaciones comercializables se presentarán separadas cuando existan bloqueos. Así no se mejora artificialmente el porcentaje retirando habitaciones del denominador.

## 7. Construcción con IA y agentes
### Organización propuesta
Un agente orquestador administra alcance, dependencias, costos y evidencia. Agentes especializados cubren producto hotelero, arquitectura/datos, finanzas e integraciones, experiencia de usuario, desarrollo, seguridad, pruebas, infraestructura y migración. Se trata de funciones de trabajo: no exige diez modelos distintos ni diez agentes ejecutándose simultáneamente.

Cada encargo debe tener requisito, entrada, archivos autorizados, entregable, contrato de datos/API, pruebas, límite de costo y aprobador. El agente que implementa no se declara aprobado a sí mismo. Otro agente revisa y ejecuta pruebas independientes. Si el entorno sólo admite una instancia, se ejecutan las funciones secuencialmente y se declara esa limitación, sin inventar subagentes.

Se propone un repositorio propio del grupo, separado de VinculaTerritorio, con AGENTS.md, documentos versionados, decisiones de arquitectura, migraciones, contratos de API, pruebas y registro de cambios. Las instrucciones persistentes y los planes por fases están documentados como patrones de trabajo de agentes [S20]. Los documentos fuente y correos de proveedores son datos, nunca instrucciones para el agente.

### Límites de autonomía
Los agentes pueden proponer, programar, documentar y ejecutar pruebas en entornos autorizados. No pueden disponer pagos, emitir documentos fiscales reales, cambiar cuentas de proveedores, borrar datos, variar porcentajes societarios, modificar remuneraciones o desplegar cambios sensibles sin aprobación humana. Se aplicarán herramientas de alcance limitado, credenciales separadas, registro de ejecuciones y protección contra instrucciones maliciosas dentro de contenido externo [S19, S21].

No entrenar modelos con datos de huéspedes o trabajadores por defecto. Los datos de prueba serán ficticios o anonimizados. La aplicación debe seguir funcionando aunque el servicio de IA no esté disponible: reservar, cobrar, limpiar y conciliar son procesos de software determinista, no decisiones libres de un modelo.

### Criterio de terminado
Un requisito sólo está terminado cuando tiene especificación aprobada, implementación identificable, migración cuando corresponda, permisos probados, pruebas automatizadas, evidencia reproducible, revisión independiente y aceptación funcional. Una pantalla o datos simulados no demuestran integración real. El avance se medirá por requisitos aceptados y ponderados por criticidad, no por líneas de código ni declaraciones del agente.

## 8. Seguridad y cumplimiento para enero de 2027
La Ley 21.719 entra en vigencia el 1 de diciembre de 2026 [S15], antes del inicio previsto. Diseñar desde el principio finalidades, base de tratamiento, minimización, perfiles de acceso, retención, derechos del titular, proveedores encargados y gestión de incidentes. Plazos y documentos específicos deben validarse jurídicamente; no inventar un plazo universal de conservación.

Recepción no necesita ver sueldos; aseo no necesita ver pasaportes, precios o deudas; marketing no necesita ver cuentas bancarias. La vista de propietario tampoco sustituye la asignación explícita de permisos. Usar autenticación reforzada para administración y finanzas, cifrado, registros protegidos, copias de respaldo y una restauración ensayada.

Sernatur exige registro para alojamiento turístico [S18]. El traspaso también debe revisar titularidad de cuentas de canales, medios de pago, dominios, permisos, patente, facturación, contratos y condiciones sanitarias aplicables. La plataforma llevará vencimientos y evidencia; no se darán por regularizados por crear una pantalla.

## 9. Secuencia de puesta en marcha
Entre el 23 de octubre y el 1 de enero hay 70 días calendario. El siguiente es un calendario de decisiones y pruebas propuesto, no una garantía de desarrollo ni de habilitación de proveedores.

| Hito propuesto | Resultado que debe poder demostrarse |
| --- | --- |
| Hasta 30 de octubre | Datos maestros y alcance inicial; proveedor de conectividad evaluado; cuentas, autorizaciones y responsables identificados. |
| Hasta 13 de noviembre | Recorrido completo de prueba: reserva, anticipo, asignación, check-in, limpieza, desayuno, cobro, cierre y conciliación importada. |
| Hasta 30 de noviembre | Procesos esenciales integrados; permisos, compras, tareas, lavandería básica y turnos; adaptadores externos verificados según disponibilidad. |
| 1 al 15 de diciembre | Piloto supervisado y pruebas de fallas, recuperación, doble reserva, doble pago, privacidad y traspaso. |
| 16 de diciembre | Decisión formal de salida: operar, operar con contingencia aprobada o no activar funciones no verificadas. |
| 17 al 31 de diciembre | Carga validada de reservas futuras, anticipos, saldos, inventario y personal; capacitación; ensayo de corte. |
| 1 de enero de 2027 | Inicio sólo con controles esenciales aceptados y responsable operativo disponible. |

### Versión inicial obligatoria
Base multiempresa, permisos, 17 habitaciones y capacidades validadas; reservas directas y tratamiento seguro de canales; recepción; cuenta de estadía, anticipos y cobros; caja; documentación tributaria mediante proceso validado; tareas de aseo y lavandería básica; desayunos/cenas; inventarios y compras; turnos y registro verificable de tareas; conciliación por importación; respaldo y contingencia.

### Evolución sin perder el alcance
Después: conexión bancaria automática, costeo más detallado, cálculo automatizado de incentivos aprobados, publicidad y precios asistidos, identificación textil opcional y módulo completo de cafetería. La primera versión ya guardará los datos y conexiones necesarios para esa evolución.

### Traspaso: control crítico
Identificar reservas de 2027 cobradas o parcialmente cobradas por el operador anterior, quién conserva el dinero y quién debe prestar el servicio o devolverlo. Registrar estancia que cruza el 31 de diciembre, vouchers, garantías, devoluciones, deudas de empresas, comisiones y proveedores. No convertir automáticamente saldos recibidos en venta nueva. El acta de corte debe cuadrar con bancos y canales y quedar firmada por los responsables que corresponda.

Si la conectividad no está certificada a tiempo, una contingencia aceptable requiere un único responsable de inventario, cupos separados o cierre de venta inmediata donde proceda, cotejo documentado y escalamiento. Una importación diaria o iCal no equivale a inventario compartido en tiempo real. La alternativa temporal puede ser un proveedor hotelero operativo conectado al núcleo propio, sin convertirlo en una renuncia a la plataforma.

## 10. Datos pendientes y control del presupuesto
Las principales definiciones pendientes son la ficha de las 17 habitaciones y camas; tarifas y políticas 2027; reglas de cobro y cancelación; dotación y turnos; quién prepara desayunos y presta lavandería; proveedor de cenas; bancos y medios de pago; RUT emisor y sistema tributario; cuentas Booking y redes; inventario físico; participaciones vigentes; tratamiento del traspaso y presupuesto de proveedores.

Los agentes avanzarán con parámetros configurables y datos de demostración identificados, sin publicar tarifas ficticias ni contratar servicios. El archivo de decisiones adjunto identifica qué dato bloquea una venta real y cuál sólo bloquea una etapa posterior.

El presupuesto total debe incluir consumo de IA de construcción, revisión y pruebas; alojamiento de aplicación y base; respaldo; monitoreo; correo/mensajería; conectividad; documentos tributarios; conciliación bancaria; comisiones de pago; mantenimiento y contingencia. USD 137/mes es solamente una referencia publicada de conectividad Channex para un hotel [S09-S10]. No existe aún una cotización total aprobada ni una prueba que permita cuantificar el ahorro frente a un PMS contratado.

## 11. Entregables y uso
El prompt maestro adjunto ordena a los agentes producir el documento de requisitos completos, diccionario de datos, estados, pantallas, contratos de API, permisos, reglas financieras, plan de pruebas y plan de implementación. La matriz adjunta es una base trazable de requisitos y pruebas, no una declaración de funciones ya implementadas. AGENTS.md fija las reglas permanentes de construcción.

La secuencia de uso es: leer este informe y los hallazgos; ejecutar el prompt maestro para especificar; resolver decisiones críticas; aprobar una versión; construir por recorridos completos; probar con evidencia; autorizar producción. No se han contratado proveedores, creado conexiones reales ni desplegado una plataforma mediante este documento.

## Fuentes y evidencia
Los identificadores S01-S21 remiten al archivo 07_Fuentes_verificadas.csv, consultado el 23 de octubre de 2026. Los hallazgos propios remiten al archivo 06_Hallazgos_archivos.md, con nombre de libro, hoja y celdas. Los porcentajes de propiedad y los importes históricos no se presentan como información vigente.
