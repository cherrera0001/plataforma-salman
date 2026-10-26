# Aclaraciones que debe cerrar el Documento Maestro

## Primero, definir el alcance que se esta aceptando
El objetivo es administrar integralmente el hotel y preparar el núcleo del grupo. No equivale a desarrollar desde el primer día una contabilidad legal completa, un motor de remuneraciones certificado, un banco, una red social ni un channel manager mundial. Cuando se utilice un servicio especializado, documentar contrato, costo, dependencia, exportacion y alternativa.

La interfaz con sistemas contables/remuneracionales no puede ocultar falta de control propio: el hotel debe registrar las obligaciones, autorizaciones, documentos y conciliaciones que le corresponden. Decidir con el responsable si un cálculo legal se realiza dentro o fuera y probar el intercambio.

## Cruces heredados que no deben convertirse en bloqueos circulares
El registro inicial preserva dependencias que necesitan refinamiento. Ejemplos: restricciones locales de tarifa frente a distribución Booking; privacidad comun frente a consentimiento comercial; costo del desayuno frente a receta y stock; orden de mantenimiento frente a bloqueo comercial; asistente comercial frente al motor de reservas y pago.

Antes de planificar ejecución, clasificar cada relación como datos, contrato, infraestructura, implementación, prueba integrada o liberación. Separar capacidades básicas de sus adaptadores. Conservar padres, crear hijos y documentar por que cambia el orden. No borrar una dependencia para hacer pasar un validador.

## Primer recorrido de valor
La primera demostración integrada debe mostrar oferta -> reserva -> pago de prueba verificado -> recepción -> tarea -> desayuno -> saldo/salida -> conciliación de prueba. Puede montarse por incrementos, pero no llamarse completo hasta verificar todos sus eslabones. Luego agregar Booking/mensajería real bajo autorización; los enlaces sociales pueden existir antes de automatizar conversaciones.

## No funcionales desde el inicio
Identidad/roles, aislamiento de datos, secretos, historiales, precisión de importes, manejo de fallas y mecanismos de respaldo se disenan desde F00/F01. F21 consolida pruebas y preparación de salida; no posterga seguridad hasta el final.

## Requisitos que surjan durante el maestro
Añadir IDs sin renumerar los 153 de origen. Registrar motivacion, relación con padres, criterios, fase y aprobación. El número inicial no es un techo. No declarar completo el hotel por cubrir solo las filas originales si el análisis descubre una obligación operativa relevante.
