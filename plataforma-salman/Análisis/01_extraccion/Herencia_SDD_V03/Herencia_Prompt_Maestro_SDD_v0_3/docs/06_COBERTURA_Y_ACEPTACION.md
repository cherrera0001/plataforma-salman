# Cobertura, profundidad y aceptación

## Lo que debe cubrir cada ficha
ID/versión/fuente; objetivo; sociedad y unidad; actores; precondiciones; evento disparador; entradas con validaciones; salidas; flujo normal y alternos; estados y transiciones; cálculos y redondeos; permisos; efectos en dinero/inventario/tareas; interfaces; fallas y compensaciones; privacidad; auditoría; KPI; pruebas; dependencias; fase; aprobadores y evidencia.

Completar campos, no repetir la etiqueta. Cuando no aplica, justificar. Si falta un dato, indicar responsable, decisión y operación bloqueada. No marcar como terminado un requisito que remite vagamente a otro módulo sin contrato.

## Cuatro vistas de cobertura
1. Los 153 requisitos base, hijos nuevos y controles SDD con IDs estables.
2. Actores por etapa del ciclo (captar, cotizar, reservar, cobrar, alojar, servir, limpiar, comprar, liquidar, conciliar, mantener, renovar, cerrar).
3. Excepciones por etapa: datos faltantes, duplicados, concurrencia, permisos, cambios, errores, anulaciones, reversos, diferencias y contingencia.
4. Sociedades, unidades, fechas, monedas y canales que participan en cada proceso.

## Trazabilidad completa
Cadena obligatoria: necesidad -> requisito maestro -> regla -> entidad/campo -> pantalla/servicio -> contrato -> FR/US/AC local -> tarea -> prueba -> evidencia -> aprobación. `matrices/06_trazabilidad_por_desarrollar.csv` es una estructura vacía, no una trazabilidad ya completada.

La matriz de 48 escenarios es un mínimo heredado, no un techo. Desarrollar datos de entrada, precondiciones, resultado numérico/observable, negativos, entornos y responsable. Añadir escenarios SDD de paquete incorrecto, baseline obsoleta, tests omitidos, autoaprobacion, pérdida de contexto y ciclo sin progreso.

## Profundidad técnica
Precisar claves, precisión de moneda, horarios/fechas de negocio, transacciones, restricciones, idempotencia, versionado, contrato API/eventos, paginacion, límites, errores, autenticación, orden de mensajes, reintentos, retención y borrado. Definir autoridad por dato, contabilidad auxiliar y vinculación con sistemas externos. No exigir todas las tecnologias posibles: registrar decisiones y alternativas descartadas.

## No funcionales
Criterios medibles de rendimiento, carga, navegadores, accesibilidad, aislamiento, respaldo, recuperación y soporte. Metas propuestas requieren presupuesto y validación, no declaracion de cumplimiento. Especificar pruebas reproducibles para cada meta activa.

## Calidad de prueba
Una checklist comprueba requisitos; una prueba ejecutada comprueba comportamiento en un entorno. Definir negativos que detecten acceso indebido y duplicaciones. Distinguir proveedor simulado, sandbox y producción controlada. No reutilizar capturas como evidencia de persistencia. Verificar integridad de reportes y consistencia entre caja, deuda y banco.

## Revisión de omisiones
A13 entrega tabla de hallazgos: ID, severidad, fuente, regla ausente/contradictoria, impacto, artefacto a corregir, responsable, prueba de cierre y estado. Un título nuevo no cierra la brecha. Revisar desde propietario, recepción, aseo, cocina, compras, trabajador, contador, huésped y soporte.

## Avance
Mostrar por separado cobertura funcional documentada, paquetes listos, código implementado, pruebas superadas, aceptación y activación. Definir denominador versionado, ponderacion y exclusión justificada. No presentar la validación estructural del ZIP como avance de construcción del hotel.
