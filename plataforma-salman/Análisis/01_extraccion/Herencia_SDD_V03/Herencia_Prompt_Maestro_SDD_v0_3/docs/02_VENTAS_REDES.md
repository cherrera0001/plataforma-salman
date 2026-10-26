# Ventas desde redes sociales - especificación de alcance V0.2

Fecha: 24/10/2026. Propuesta de diseño; no hay cuentas conectadas ni prueba de pago real en esta revisión. Fuentes R01-R16 en 07_FUENTES_v0_2.md.

## 1. Resultado empresarial

Convertir una visita o consulta en una reserva válida, visible en recepción, con política aceptada, fondos identificados y trazabilidad comercial. No confundir automatizar publicaciones con vender alojamiento. No obligar al hotel a desarrollar una tienda nativa dentro de una red social.

La cadena objetivo es: contenido/anuncio -> enlace o conversación -> oferta real -> aceptación -> retención de cupo -> pago/garantía según política -> reserva confirmada -> recepción -> estadía -> conciliación y resultado. Una tarifa corporativa puede confirmar con crédito aprobado en vez de prepago; la regla debe quedar identificada.

## 2. Cinco conexiones distintas

| Capacidad | Que hace | Requisito de habilitacion |
|---|---|---|
| Enlace hacia reservas | Lleva al sitio propio desde perfil, historia, anuncio, QR, correo o mensaje | Derecho a publicar el enlace en esa cuenta; motor y dominio propios. No requiere leer mensajes mediante API. |
| Mensajería integrada | Recibe consultas y permite responder desde la plataforma | Cuenta elegible, permisos, API oficial o proveedor, webhooks y reglas del canal. |
| Publicación | Pública contenidos aprobados y registra su estado | API y formato admitidos; permisos separados; no todos los formatos o botones están disponibles para toda cuenta. |
| Publicidad | Gestiona anuncios y presupuesto, si se habilita | Cuenta publicitaria, permisos, pago, límites y aprobación humana. No es necesaria para la primera reserva directa. |
| Medición | Relaciona visitas/campañas y resultados | Definición de eventos, consentimiento/base aplicable, IDs y deduplicación. No garantiza identificar a todo visitante. |

No utilizar una casilla única "conectado a Meta": cada capacidad lleva su propio estado, evidencia, costo y responsable.

## 3. Ruta A - reserva directa desde un enlace

1. Se aprueba una publicación, historia o anuncio con un enlace disponible en esa superficie. No asumir que cualquier enlace escrito en un post será clicable ni que existe un botón nativo "Reservar" para toda cuenta.
2. El enlace abre el sitio del hotel, adaptado a móvil y a navegadores internos, con página de campaña o buscador. Lleva identificadores de origen, no datos personales.
3. El visitante introduce fechas y ocupantes. El servidor consulta el mismo inventario y motor de precios que usa recepción.
4. Se muestran habitaciones disponibles, precio total, servicios, moneda, condiciones y monto exigido ahora. No mostrar descuentos que ya expiraron.
5. Al continuar, se crea una cotización versionada y, cuando corresponda, una retención temporal de inventario. No bloquear habitaciones por cada vista o mensaje; limitar retenciones abusivas.
6. El huésped acepta condiciones, aporta lo necesario y paga en la página segura del proveedor elegido. Una transferencia puede quedar pendiente de verificación; no se confirma por una foto del comprobante.
7. El servidor verifica el estado real del pago mediante el mecanismo del proveedor. No todos usan webhook: algunos requieren confirmación/consulta de transacción. Validar orden, monto y moneda; guardar una sola aplicación aunque se repita la notificación.
8. Si se cumplen condiciones y existe cupo, se confirma una reserva única. Si el pago llega después de expirar el cupo, se abre una excepción con alternativa o devolución autorizada; no se inventa disponibilidad.
9. Recepción ve la reserva, pasajeros previstos, fechas, importe total, anticipo, saldo y origen. El huésped recibe confirmación por un canal permitido.
10. Se pública el cambio de inventario a canales externos mediante conectividad habilitada. La demora externa se controla con alertas, cupos y contingencia, no con promesas de riesgo cero.

## 4. Ruta B - venta asistida por conversación

El cliente pregunta por Instagram, Messenger o WhatsApp. La API autorizada entrega el evento al servidor, que verifica su autenticidad, elimina duplicados y lo registra en una bandeja con responsable.

El asistente se identifica como automatizado. Solicita solamente datos necesarios para cotizar: fechas, número de personas, configuración deseada y necesidades pertinentes. Si "el viernes" es ambiguo, confirma la fecha exacta. Para identidad o datos sensibles, remite a formulario seguro cuando corresponda; no solicita tarjetas o documentos completos en el chat.

La IA no decide precios ni cupos. Invoca herramientas propias con esquemas y permisos, por ejemplo consultar_disponibilidad, cotizar_estadia, crear_retencion_autorizada, generar_enlace_pago, consultar_estado_reserva y derivar_a_recepcion. Estos son nombres LÓGICOS de herramientas a especificar, no endpoints existentes de Meta o de una pasarela.

La cotización lleva ID, fecha de expiración, tipo de habitación, precio y política. El enlace vuelve al mismo recorrido de la ruta A. Si el cliente pasa a WhatsApp, debe iniciar o autorizar ese contacto y la vinculación de identidad necesita evidencia. No identificar personas solo por coincidencia de nombre o foto.

El sistema puede responder automáticamente en producción solo cuando ese flujo y sus permisos hayan sido aprobados. No se exige aprobar cada consulta rutinaria; si hay descuento excepcional, devolución, conflicto de precio, reclamo, urgencia, falta de datos o solicitud humana, se deriva. Cuando una persona toma el caso, se detiene el bot para evitar respuestas contrapuestas.

Una venta asistida no exige que el cliente cambie de canal, excepto el pago/formulario seguro cuando sea necesario. Se conserva hilo, cotización y reserva para no pedir lo mismo repetidamente.

## 5. Restricciones verificadas y decisiones pendientes

Instagram: usar cuenta profesional y elegir la via oficial adecuada. Con Instagram Login no se presume que siempre haga falta una página Facebook vinculada; otra via de integración si utiliza esa vinculación. Permisos, acceso a usuarios reales y revisiones dependen de la ruta y caso. R01 y R08. No prometer mensajes libres a seguidores ni recuperar todo el historial.

WhatsApp: usar Business Platform/Cloud API o proveedor autorizado, no automatización no autorizada del navegador o de una cuenta personal. La política actual exige opt-in para contacto, respetar la baja y usar plantillas aprobadas fuera de la ventana de servicio de 24 horas; exige una via clara de escalamiento. R02-R03 y R15. El modelo de costos se cotiza con condiciones vigentes; no asumir que la mensajería automática es gratuita.

Número actual: comprobar titularidad, WABA, proveedor, posibilidad de migración y coexistencia con la app. Meta documenta coexistencia bajo requisitos; no se garantiza sin validar el caso del hotel. R04. Ensayar sin cortar el canal actual.

Anuncios a mensajes: Meta documenta anuncios que abren Messenger, Instagram o WhatsApp. R05. Es una entrada comercial, no una confirmación de reserva ni un permiso ilimitado de marketing.

Publicación: API, formatos, autorizaciones y fallos separados de mensajería. R06. La publicidad puede seguir inicialmente en las herramientas oficiales de Meta y enviar trafico al motor propio.

Booking: usar proveedor autorizado. El portal oficial declara que no admite conexiones directas de propiedades individuales y actualmente pausa integraciones de nuevos proveedores. No basar el proyecto en que Herencia obtendra una conexión directa en una fecha garantizada. R16.

Pagos: escoger proveedor habilitado para Herencia SpA. La propuesta no depende de pagos nativos dentro de WhatsApp o Instagram ni de una tienda social de habitaciones; utiliza checkout seguro externo. Webpay Plus es solo una referencia técnica de confirmación desde servidor, no proveedor contratado. R14.

Google: un enlace desde el perfil o sitio no es lo mismo que distribuir precios en Google Hotels. La segunda capacidad requiere conectividad y configuración especificas. R11.

## 6. Estados separados

Conversación: nueva -> en atención -> esperando cliente -> derivada -> resuelta; no leída y no respondida son dimensiones diferentes.
Oportunidad: consulta -> datos suficientes -> cotizada -> enlace enviado -> reserva generada / pérdida / vencida.
Reserva: borrador -> retenida / pendiente de garantía -> confirmada -> modificada / cancelada / no-show -> atendida.
Pago: iniciado -> pendiente -> autorizado/confirmado según proveedor -> aplicado -> liquidado -> conciliado; fallido, devolución y contracargo son estados relacionados, no eliminaciones.
Consentimiento: finalidad/canal, evidencia, fecha, versión, vigencia y baja. No deducir permiso de publicidad de una reserva.

El maestro definira transiciones exactas, actores y restricciones; esta enumeracion es una base para especificarlas, no el esquema final aprobado.

## 7. Datos y privacidad comercial

Entidades nuevas: CuentaDigital, CapacidadConector, Campaña, PiezaContenido, EnlaceCampana, Contacto, IdentidadCanal, Consentimiento, Conversación, Mensaje, AsignacionConversacion, Oportunidad, Seguimiento, PlantillaMensaje, EventoConversion, CostoCampana y VinculoReserva.

Canal de venta y origen comercial se guardan separados: canal DIRECTO; fuente Instagram; medio anuncio; campaña definida. Una reserva Booking influida por redes puede no tener atribución deterministica; no inventarla. Identificación cruzada solo con datos y finalidades permitidos.

Pixel y Conversions API requieren eventos con el mismo nombre e ID para deduplicar una misma acción. R07. La aplicación debe definir antes si Purchase significa una reserva confirmada con su valor o un pago; no enviar ambos como dos ventas. Conservar por separado anticipos, devoluciones, cancelaciones e ingreso por servicio. El mecanismo externo de corrección se verifica; no asumir que un evento Purchase negativo elimina el anterior.

No enviar a plataformas publicitarias RUT, pasaporte, número de habitación, tarjetas, contenidos de chats ni restricciones de salud/alimentación. No condicionar una reserva a seguimiento publicitario. Mostrar fuente desconocida cuando corresponda; reportar cobertura de medición.

## 8. Panel de gestión comercial

Visitas medibles, consultas, solicitudes calificadas, ofertas, reservas, cancelaciones, estadías efectivas, tiempo de respuesta, costo de anuncios/mensajería, ventas atribuidas y margen. Definir ventanas temporales, denominadores, moneda e impuestos. ROAS es un indicador de atribución, no una prueba automática de beneficio incremental.

## 9. Fallos y contingencia

Token vencido, permiso revocado, número migrado, plantilla rechazada, límite de API, duplicados, eventos fuera de orden, mensajes sin entregar, pasarela caída, pago tardio y última habitación concurrente deben tener comportamiento especificado. Mostrar fallos reales, alertar a responsable y permitir continuar con recepción o enlace web cuando corresponda.

## 10. Pruebas mínimas de este módulo

- Enlace etiquetado -> oferta -> pago de prueba -> reserva -> recepción -> conciliación: un solo registro de cada hecho.
- Dos ventas concurrentes al último cupo: solo una confirmación interna válida.
- Mensaje o notificación repetidos: no duplicar oportunidad, pago o confirmación.
- Baja de marketing: cancelar envios promocionales pendientes y conservar servicio permitido.
- Mensaje fuera de ventana sin plantilla válida: bloqueo visible y alternativa autorizada.
- Tomar conversación manualmente: el bot deja de responder hasta nueva habilitacion.
- Manipular precio/fechas en enlace: el servidor rechaza o recotiza; no acepta datos del cliente como autoridad.
- Seguimiento rechazado: el usuario puede reservar; no se envian eventos no autorizados.
- API desconectada: el estado comercial no se presenta como sincronizado.
- Cliente paga después de vencer cupo: caso controlado, sin sobreventa silenciosa.

Estas pruebas están definidas, no ejecutadas sobre una plataforma inexistente. Cada integración real requiere evidencia autorizada adicional.


## Adaptacion SDD V0.3

La venta directa se construye a partir de F02-F05; CRM F14, mensajería oficial F15, asistente F16, marketing F17 y medición F12 se conectan al mismo motor. No existe inventario separado dentro de un bot. Los requisitos se preservan y las fuentes R01-R16 son antecedentes por revalidar al habilitar cada capacidad. La disponibilidad de una API pública no acredita permisos del hotel.

En cada paquete local deben repetirse las obligaciones críticas en FR y criterios de aceptación, no solo enlazar este anexo. La conversacion, el seguimiento publicitario, la confirmación determinista y el abono bancario son hechos distintos. No afirmar una cuenta conectada ni ejecutar mensajes reales durante la generacion de especificaciones.
