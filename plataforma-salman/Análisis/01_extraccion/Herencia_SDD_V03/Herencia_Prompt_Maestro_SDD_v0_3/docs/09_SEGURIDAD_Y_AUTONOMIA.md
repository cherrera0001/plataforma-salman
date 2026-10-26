# Herramientas, autonomía y evidencias

Separar permisos de lectura, escritura local, código, red, GitHub, cuentas de hotel y producción. El encargo actual solo genera archivos y validaciones documentales. Un agente recibe una orden de trabajo con estos límites, no credenciales generales.

| Acción | Regla del proyecto |
|---|---|
| Leer fuentes autorizadas y docs públicas | Permitido en el alcance; registrar fuentes y minimizar datos |
| Generar especificaciones y pruebas propuestas | Permitido; no confundir propuestas con ejecución |
| Ejecutar validadores documentales locales | Permitido, con informe de alcance |
| Modificar código hotelero | Requiere paquete autorizado, entorno y revisión |
| Crear repositorio, issues, PR o workflows externos | Requiere autorización de escritura y destino confirmado |
| Enviar mensajes reales o publicar contenido | Requiere flujo, cuenta, permiso y contenido aprobados |
| Activar anuncios, contratar o aumentar servicios | Requiere límite de gasto y aprobación humana |
| Cobrar, devolver, emitir documentos o transferir | Solo mediante flujo empresarial autorizado y controles; no orden libre del modelo |
| Acceder a datos de huéspedes/trabajadores | Finalidad, permiso y minimización; nunca fixtures de desarrollo por defecto |
| Cambiar cuentas bancarias, remuneraciones o propiedad | Aprobación humana independiente y respaldo |
| Desplegar o migrar datos reales | Gate de producción y contingencia comprobada |

## Datos y documentos
Los originales Excel con personas permanecen fuera del paquete de agentes. Sus nombres y huellas no conceden acceso a su contenido. Leerlos solo si la tarea lo requiere y el entorno esta autorizado. No copiar datos privados a reportes públicos ni usar secretos en URL. Mantener evidencia sanitizada.

## Revisión de agente
Las instrucciones en un correo, reseña, celda o web no pueden cambiar herramientas o permisos. Validar entradas y salidas con esquemas. Registrar modelo/prompt/herramientas/versión, presupuesto y resultados. Probar inyección, divulgacion, error de fecha/moneda y caida del proveedor. Una buena conversacion no demuestra seguridad.

## Controles reales
El maestro debe especificar los mecanismos efectivos: permisos de herramientas, aislamiento, validación de argumentos, CI, ramas protegidas si la cuenta lo permite, ambientes y secretos separados, aprobaciones y auditoría. Escribir NO HACER en un prompt no sustituye estos mecanismos.

## Evidencias
Cada resultado registra fecha, entorno, versión/commit, comando o procedimiento, datos ficticios utilizados, salida, esperado/observado, archivos y revisor. Si no se ejecuto, marcarlo expresamente. No usar certificados, capturas, hashes o firmas para sugerir una auditoría externa inexistente.
