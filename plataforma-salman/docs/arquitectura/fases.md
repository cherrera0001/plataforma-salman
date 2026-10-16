# Plan de implementación por fases — propuesto, sin ejecución

| Fase | Entrada y dependencia | Trabajo posterior autorizado solo al iniciar desarrollo | Salida verificable / gate |
|---|---|---|---|
| 0 Descubrimiento | Fuentes y aclaraciones | Medir operación, validar exportaciones, políticas y proveedores | Decisiones bloqueantes cerradas, constitución ratificada y herramientas verificadas |
| 1 Core mínimo | Fase 0 | Pruebas de permisos por tenant, idempotencia, auditoría; contratos de pago/documentos | Denegaciones adversariales, duplicados y restauración probados |
| 2 Primer flujo rentable | 000 y reglas del negocio elegido | 001 H1 o 003 H1 con pruebas antes de código | Recorrido acordado end-to-end en sandbox, conciliación y evaluación humana |
| 3 Operación vertical | Flujo estable y datos | 001 H2, 003 H2; 002 H1/H2 tras PMS/canales; 004 según presupuesto V2 | Integraciones autorizadas, concurrencia y fallos probados |
| 4 Agentes acotados | Datos y políticas validados | Lectura/borradores, evaluación offline, sandbox y luego autonomía aprobada | Sin acciones fuera de política en suite, costo/latencia y tasa humana medidos |
| 5 Preparación operativa | Gates anteriores | Revisión legal, pentest, restauración, observabilidad, costos y contratos | Aprobación separada de lanzamiento; no se ejecuta en esta fase |

No se estiman semanas ni costos sin equipo, datos, cotizaciones y volumen. La fase 2 elige una vertical por valor validado; la numeración de carpetas no impone una cascada técnica. El backlog ejecutable actual es de aclaración y diseño, no de producción.
