# Hallazgos documentales y reglas de migración
**Fecha: 23/10/2026.** Análisis de 15 libros y 255 hojas. Los archivos originales no fueron modificados. Este inventario registra procedencia; no certifica vigencia jurídica, tributaria ni operativa.

## 1. Inventario de fuentes
| Archivo | Hojas | SHA-256 |
| --- | ---: | --- |
| % de ocupacion habitaciones hotel(1).xlsx | 3 | 02594846f8dfc81eec0ed083634f12190ae1733fb185f718189dbe71e777c649 |
| % de ocupacion habitaciones hotel.xlsx | 1 | 3ab881dbd81765084047290c744e4e63453e9f510eb32b9ccd89240b84de1e06 |
| INVENTARIO BEBIDAS.xlsx | 32 | 92a55c9b87a2c2ed96283e216c325cae4fa99e2697a6e6fb112dc98e4f040e96 |
| INVENTARIO GOLOSINAS.xlsx | 32 | 7622181b976d03ae3918cb7cb7c8763a145148a8eaf0fb349fd8fe9441d066c1 |
| Lavanderia ropa cama-toallas.xlsx | 31 | e6f599fc77a35341290c3f2072e367c2dc79bebbe72ef2b19fe4bdcc1aafe3ec |
| Nomina Inventarios  Junio Hotel.xlsx | 33 | 69545773d94316ba211dc630d3b5073fc953c38f7685a168c3b484d59a69cdfe |
| Nomina Inventarios Hotel Agosto.xlsx | 33 | caa4fe01ce70d8285f497bd670d66e248a6d08d3f63443d61791205602606552 |
| Nomina Inventarios Hotel Octubre.xlsx | 33 | 72e6d67b4177693e470c3ded0ecbf17068a26bab8fbc7ee05d4f8d403a9f02a5 |
| Nomina Inventarios Hotel SEPTIEMBRE.xlsx | 33 | 4e5abb8a7a2ca5a713c4657b79145451a774686e2388dfa6366520d7d3a81144 |
| RETIRO CAJA HERENCIA HOTEL.xlsx | 1 | 53cb9eecc8a56b0aa8540094bc2d5baab7850ca08afafb4bc6c641c02a14e687 |
| Resumen Valorizado Bebidas y Golosinas.xlsx | 1 | 7767c6dd6203c151f45142efdd392ce4004156369513aacef444b5641735c261 |
| Sueldos_HERENCIA HOTEL_ENERO 2019.xlsx | 9 | 4ab12e2defd32b6795c11e45a25b0d37dabd331d1fc909759fe838867b2f82ac |
| VALORES DE LAS HABITACIONES.xlsx | 8 | 53854e3f138ad26ea93b052007eb32a2e3e7ba2d6cb0ed1aedcb6b664892ab1a |
| Organigrama Holding Salman 2018.xls | 4 | 0eeab557dea9ecff3196c38b21b983960c9a4b1ac458e259c3ba5e0d49f60d54 |
| booking septiembre.xls | 1 | f055157a8f40b631793ccb9f56158ba8d7d04b96479bf72f6b1c4a7c078e783a |

## 2. Malla societaria
Fuente: Organigrama Holding Salman 2018.xls, Hoja1. M12:M13: Wembé 50/50 Ricardo/Sandra. M23:M24: Inmobiliaria Salman 99,5% Wembé y 0,5% Ricardo. T13:T14: SB 72,66% Ricardo y 27,34% Sandra. Z13:Z14 y AE13:AE14: Constructora y Herencia 50/50. K27:K31 y filas 40:41: filiales inmobiliarias. Se recuperó texto tanto de celdas como de cuadros de texto; las cifras relevantes también están explícitas en celdas.

Interpretación: registrar antecedentes históricos. No convertir el encabezado informal "empresas no relacionadas" en una calificación tributaria/legal. No afirmar que todas las sociedades son filiales de Wembé. Validar vigencias antes de activar una malla actual.

## 3. Ocupación
% de ocupacion habitaciones hotel.xlsx, Hoja1, B8:I37: noviembre 2019. Suma C8:C37 = 193 habitaciones-noche; D8:D37 = 510; F = 100 directas; H = 93 Booking. Ocupación calculada: 37,84%.

% de ocupacion habitaciones hotel(1).xlsx, Enero 2020, B8:I38: 294 habitaciones-noche sobre 527; 148 directas y 146 Booking; 55,79%. Febrero 2020, B8:I36: 330/493; 169 directas y 161 Booking; 66,94%. Marzo 2020 tiene 17 filas con fecha y todos los conteos numéricos requeridos; 92 habitaciones-noche en esas filas. Las filas incompletas no se convierten en ceros.

Los dos archivos no son duplicados binarios ni representan el mismo periodo. Las columnas G e I dividen las habitaciones por canal por el total de habitaciones, no por las habitaciones ocupadas: no confundirlas con participación del canal dentro de las ventas. Los libros no demuestran por sí solos cuántas habitaciones estaban fuera de servicio.

## 4. Booking septiembre
booking septiembre.xls, Sheet1, A1:L106: doce columnas para identificador, fecha de reserva, quien reserva, huésped, habitaciones, personas, noches, porcentaje de comisión, importe original, final, comisión y estado. Existen 105 filas de reservas: 79 Stayed, 13 No-Show y 13 Cancelled. H2:H106 indica 17%. El total de comisiones almacenado figura en K108.

No se utiliza la fecha Booked on como fecha de llegada ni se presume una moneda que el encabezado no identifica. Para conciliación actual se requieren fechas de servicio, moneda, liquidaciones, documentos y movimientos de banco. Los nombres y datos personales de huéspedes no se reproducen en este anexo ni en las pruebas sintéticas.

## 5. Tarifas
VALORES DE LAS HABITACIONES.xlsx contiene ocho hojas con tarifas, pilotos y acuse de informativo. En "Lunes 25", B4:J5 distingue configuración, valor de canal, dólar y tarifas con/sin IVA. I4 menciona 25% y I5 calcula 10%; C4 menciona 15%, diferente del 17% del reporte Booking. Las hojas contienen referencias temporales antiguas: no son un tarifario 2027.

"hoja de registro de informativo", A1:D2, contempla fecha, nombre, habitación y firma. Diseñar acuse digital del reglamento o informativo con versión del documento y fecha, sin presumir que equivale a consentimiento para publicidad.

## 6. Inventarios generales
Nomina Inventarios Junio: 33 hojas; "Inv- PEDIDOS" F2:G2 indica JULIO 2019, y existe una hoja denominada "31-6". Agosto, septiembre y octubre contienen plantillas diarias y resumen. En septiembre "01-9", B6:L6: producto, unidad, stock inicial, entrada, proveedor, factura, salida, stock final, stock en área y precio.

Septiembre y octubre, "Inv- PEDIDOS", I66 e I117: valores de error #REF!. No se deben copiar fórmulas rotas. Normalizar producto, unidad, ubicación, documento y movimiento; reconciliar bodega frente a área sin duplicar stock. Distinguir alimentos, limpieza, insumos, elementos reutilizables y activos.

## 7. Bebidas, golosinas y ventas complementarias
INVENTARIO BEBIDAS.xlsx y INVENTARIO GOLOSINAS.xlsx: 32 hojas cada uno; resumen AGOSTO y hojas diarias. B5:I5 contiene producto, stock anterior, fechas y cantidades de compra/venta, saldo y recibido por. El libro de bebidas conserva en B2 un título de golosinas aunque B6 y siguientes contienen bebidas.

Resumen Valorizado Bebidas y Golosinas.xlsx, Hoja1: ventas con producto, cantidad, número de boleta, monto y fecha. Vincular venta a salida real de stock y, cuando corresponda, a cuenta de estadía, sin duplicar cobro en recepción y punto de venta.

## 8. Lavandería
Lavanderia ropa cama-toallas.xlsx: 31 hojas, RESUMEN y días de septiembre. B4:F20 contempla ropa de cama con saldo anterior, entrada bodega, salida lavandería y saldo; B26:F29 contiene toallas. No se observa en esos encabezados identificación de habitación, estadía, ejecutor o lote individual.

Conservar el catálogo, mejorar nomenclatura y agregar estados, procedencia, lote, recepción parcial, faltantes, calidad y costo. El lavado es un servicio sobre un elemento reutilizable, no una baja de inventario por cada uso.

## 9. Caja
RETIRO CAJA HERENCIA HOTEL.xlsx, Retiros Hotel, B3:D: mes e importes CLP/USD; no contiene por sí solo el circuito de arqueo, documento y depósito. Convertir el control mensual de retiros en registro de movimientos con fecha, moneda, responsable, destino, evidencia y conciliación.

## 10. Personal y remuneraciones
Sueldos_HERENCIA HOTEL_ENERO 2019.xlsx: nueve hojas. MES F9:F17 registra seis cargos de RECEPCIONISTA y tres de MUCAMA. Esto no demuestra dotación actual ni simultaneidad de contratos. MES, fila 8, contiene conceptos de sueldo, horas, descuentos, aportes y pagos; otras hojas incluyen bonos y transferencia.

Se detectaron 82 celdas con valor almacenado #REF! y 74 con #N/A en el libro; los valores almacenados no son una recalculación independiente. Hay referencias rotas y búsquedas no resueltas que requieren revisión. Recuperar campos y necesidades de control, no importar las tasas legales, salarios, contratos ni fórmulas como vigentes. No reproducir datos personales de los trabajadores en el paquete de desarrollo.

## 11. Regla transversal
Archivo histórico no equivale a dato inicial de producción. Antes de migrar: preservar original, validar hoja/fecha, normalizar unidades, separar datos personales, registrar transformaciones, detectar duplicados y obtener aprobación del responsable. Pruebas y demostraciones usan datos ficticios.
