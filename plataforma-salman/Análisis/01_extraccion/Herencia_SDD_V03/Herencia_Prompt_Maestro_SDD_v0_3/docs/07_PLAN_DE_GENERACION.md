# Plan para producir las especificaciones

## Producto final buscado
Un maestro de 24 capítulos DESARROLLADOS, fichas completas de todos los requisitos del alcance, modelos/contratos, matrices y paquetes de funcionalidades compatibles con Spec Kit. No volver a entregar el mismo prompt o el índice como si fueran el maestro.

## Lote L0 - Inventario y fundamentos
Validar archivos, leer contexto, registrar decisiones, detectar contradicciones, proponer constitución y preparar estado de trabajo. Inventariar entorno sin instalar ni crear cuentas por defecto. Conservar hashes de fuentes. Analizar los acoplamientos heredados y clasificar dependencias.
Salida: índice definitivo, registro de fuentes/políticas, diccionario comun inicial, mapa de capacidades, dependencias tipadas y plan de lotes.

## Lote L1 - Recorrido comercial y financiero central
Desarrollar M01-M08 y las reglas pertinentes de M14/M16/M17/M19. Especificar páginas públicas, reserva y precio, dinero, estados y recepción como un mismo recorrido; no hacer solo interfaces. Preparar primeros paquetes F00-F05 y sus contratos.
Salida: reglas y escenarios completos para enlace -> reserva -> pago -> recepción, con límites de proveedores y autorizaciones pendientes.

## Lote L2 - Operación y recursos
Desarrollar M09-M14: aseo, lavanderia, alimentos, sala, compras, inventarios, activos, renovación, personal, cuentas y costos. Completar eventos compartidos y resolver dependencias de stock/costos.
Salida: fichas operativas, configuración requerida a administración, modelos y pruebas; paquetes F06-F12.

## Lote L3 - Canales y experiencia
Completar redes, mensajería, asistente, marketing, portal, canales externos, banco y KPI. Aplicar privacidad y control de gasto en cada función. No simplificar redes a enlaces ni hacer obligatoria la publicidad avanzada para reservar.
Salida: F13-F19 y las vistas comerciales/experiencia pendientes; evidencia pública de capacidades, no cuentas ficticiamente habilitadas.

## Lote L4 - Transversales y transicion
Cerrar M15-M24, traspaso F20, controles F21 y contratos futuros F22. Detallar seguridad, experiencia, infraestructura, agentes, pruebas, presupuesto, soporte, migración y planes de contingencia. No esperar a este lote para considerar seguridad; aqui se consolida su revisión transversal.
Salida: maestro coherente, matrices, procedimientos y criterios de salida.

## Lote L5 - Paquetes SDD y auditoría final
Completar todas las especificaciones locales y vinculos. Planes y tareas del primer conjunto listo se desarrollan con stack/contratos ya aprobados. Para entregas posteriores completar el comportamiento y proponer el plan técnico con estado PRELIMINAR; no simular plan ejecutable si falta una decisión bloqueante. Cuando se resuelva, continuar hasta EJECUTABLE_APROBADO sin perder alcance.
Salida: informe de cobertura, brechas, estado por archivo, primeros paquetes listos y decisiones necesarias. Si el usuario encarga todos los planes, continuar por lotes hasta completarlos o reportar exactamente los bloqueados.

## Ubicacion y reanudacion
Sin repositorio: generar bajo `salida_especificaciones/` con `maestro/`, `specs/`, `registros/`, `contratos/`, `evidencias_documentales/` y `estado.json`. Son RUTAS OBJETIVO que se crearán al ejecutar, no archivos presentes ahora.

Con repositorio autorizado: importar a `docs/master/`, `specs/` y rutas efectivas de Spec Kit, preservando referencias y constitución. Revisar antes de sobrescribir. El paquete de entrada permanece inmutable como baseline y los cambios se hacen en archivos de salida versionados.

Cada cierre de sesión entrega: archivos hechos, estado, hashes, decisiones, dependencias, hallazgos, comandos realmente ejecutados y próximo bloque exacto. Usar la instrucción de reanudacion. No depender de conversaciones anteriores ni prometer trabajo posterior automático.

## Gestión del volumen
Los lotes pueden subdividirse, pero no reducirse a resúmenes o esquemas vacios. Registrar que campos o casos faltan. Priorizar profundidad verificable por funcionalidad sobre número de páginas. El objetivo de inicio 2027 no autoriza saltar controles o prometer viabilidad sin plan y pruebas.
