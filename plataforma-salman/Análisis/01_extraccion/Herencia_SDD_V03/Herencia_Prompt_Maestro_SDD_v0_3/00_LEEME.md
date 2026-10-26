# Hotel Herencia / Grupo Salman
## Prompt Maestro SDD - Versión 0.3
**Fecha:** 24 de octubre de 2026. **Finalidad:** producir las especificaciones completas y prepararlas para construir con IA y agentes bajo GitHub Spec Kit.

## Empezar aqui
El archivo principal es [01_PROMPT_MAESTRO_SDD_v0_3.txt](01_PROMPT_MAESTRO_SDD_v0_3.txt). Su copia Markdown tiene el mismo contenido. Para iniciar, entregar al agente **la carpeta completa o este ZIP**, no solo el texto del prompt, y utilizar [02_INICIAR_ESPECIFICACIONES.txt](02_INICIAR_ESPECIFICACIONES.txt).

Este paquete sustituye la V0.2 como instrucción activa. Los antecedentes se conservan para trazabilidad, no para ejecutarlos de nuevo. No se necesita buscar decisiones en conversaciones anteriores.

## Que contiene
| Componente | Contenido y utilidad |
|---|---|
| Prompt consolidado | Todas las reglas funcionales anteriores y la capa SDD: alcance, fuentes, roles, modelos, controles, entregables y gates |
| 24 capítulos | Índice detallado del maestro que se debe desarrollar, no un maestro ya terminado |
| 153 requisitos de base | IDs y campos originales conservados, con asignación candidata a paquetes |
| 23 fichas de funcionalidad | Punto de partida para descomponer trabajo; no son specs aprobadas |
| 18 controles SDD | Reglas del proceso de construcción, separadas de las funciones del hotel |
| 48 escenarios de prueba | Casos críticos preservados; deben desarrollarse y ejecutarse después de construir |
| 44 decisiones | 36 pendientes anteriores más ocho sobre ejecución, permisos, versión y revisión |
| Plantillas de especificación | Spec, plan, tasks, research, datos, contratos, quickstart, checklists, aceptación, cambios, ADR y orden de trabajo |
| Validación documental | Scripts locales, resultados, manifiesto de integridad y límites expresos |

## Los archivos más importantes
- [Prompt maestro](01_PROMPT_MAESTRO_SDD_v0_3.md) y [orden para iniciar](02_INICIAR_ESPECIFICACIONES.txt).
- [Índice de 24 capítulos](docs/01_INDICE_MAESTRO.md) y [ventas desde redes](docs/02_VENTAS_REDES.md).
- [Contrato SDD](docs/03_CONTRATO_SDD.md), [constitución propuesta](docs/04_CONSTITUCION_PROPUESTA.md) y [AGENTS.md](AGENTS.md).
- [Plan de generacion](docs/07_PLAN_DE_GENERACION.md), [uso posterior con Spec Kit](docs/08_INSTALACION_Y_USO_POSTERIOR.md) y [registro de paquetes](config/paquetes_sdd.json).
- [Registro de requisitos](matrices/01_requisitos_base.csv), [decisiones](matrices/02_decisiones.csv) y [escenarios](matrices/05_escenarios_base.csv).

## Que producira al ejecutarlo
Un Documento Maestro desarrollado, modelos y contratos, matrices, fichas de requisitos, auditoría de omisiones y paquetes compatibles con Spec Kit. Las especificaciones funcionales cubren todo el alcance; los planes ejecutables y tareas se afinan por paquete cuando las decisiones técnicas y empresariales correspondientes esten resueltas. Los planes futuros no se presentan falsamente como aprobados para código.

El trabajo se realiza por lotes. Si una ejecución no alcanza para todo, debe entregar archivos completos de ese lote, estado y próximo bloque, sin diluir el contenido en un resumen ni prometer trabajo en segundo plano. Para continuar: [03_REANUDAR_ESPECIFICACIONES.txt](03_REANUDAR_ESPECIFICACIONES.txt).

## Que NO contiene ni autoriza
No es el Documento Maestro ya desarrollado, una aplicación de hotel, un repositorio creado, una extension oficial de Spec Kit ni una instalación probada. No conecta Booking, redes, pasarelas o bancos. No autoriza gastos, mensajes, operaciones reales ni despliegues. El método SDD esta acordado; las políticas y decisiones aun pendientes siguen pendientes.

El archivo [04_PREPARAR_CONSTRUCCION_POSTERIOR.txt](04_PREPARAR_CONSTRUCCION_POSTERIOR.txt) es para una autorización futura, no una instrucción de ejecución automática al abrir el ZIP.

## Venta desde redes: alcance conservado
Cinco capacidades diferentes: enlace de reserva, mensajería, contenido/publicación, publicidad y medición. El motor del hotel es la autoridad sobre cupo, precio y confirmación. Un asistente no mantiene inventario aparte ni inventa tarifas. Conversacion, cotización, anticipo, reserva, estadía y banco son hechos distintos. Las APIs y permisos se validan por capacidad/cuenta antes de activar.

## Dependencias que el maestro debe precisar
Hay **22 relaciones heredadas** que no encajan directamente como predecesores en el orden candidato de paquetes. Estan registradas en [matrices/07_acoplamientos_a_resolver.csv](matrices/07_acoplamientos_a_resolver.csv). No se eliminaron ni ocultaron: el agente debe distinguir dependencia de datos, contrato, implementación, prueba o salida y descomponer capacidades antes de autorizar el plan ejecutable. El orden propuesto no es todavia un grafo definitivo de construcción.

## Validación y sus límites
El validador comprueba archivos, IDs, referencias, preservacion de requisitos/decisiones, capítulos, escenarios, fichas, estructura JSON/CSV y hashes cuando existe manifiesto. Los tests del validador comprueban que detecte cambios y faltantes. **No son pruebas del hotel ni certificacion de compatibilidad nativa con Spec Kit.**

```text
python scripts/validar_paquete.py
python scripts/probar_validador.py
```

Requieren Python 3.10 o posterior por la sintaxis del script; no requieren paquetes de terceros ni conexión a internet. No instalan ni modifican servicios. El primer comando es de solo lectura salvo `--output`; el segundo usa copias temporales. No son comandos de GitHub Spec Kit.

Los informes se encuentran en `informes/`. `MANIFEST.json` contiene huellas SHA-256 de los archivos de entrega; no acredita aprobación empresarial ni autoria externa. Una modificacion deliberada de archivos requiere nueva versión/manifiesto; el resultado no debe interpretarse como corrupcion del negocio.

## Privacidad y datos originales
No se vuelven a empaquetar las planillas con datos de huéspedes o trabajadores. Se conservan hallazgos sanitizados e inventario de nombres/huellas. Los datos reales se consultan solo cuando resulten necesarios y con acceso autorizado; las pruebas usan datos ficticios.

## Formatos
Markdown y TXT para lectura y agentes; CSV UTF-8 para matrices, con delimitador coma y nombres de columna; JSON para configuración/schema; Python para validación. CSV no significa que las decisiones esten aprobadas. Las plantillas tienen marcadores deliberados, no datos reales. Los archivos de antecedentes mantienen sus bytes originales.

**Siguiente acción:** ejecutar la instrucción de inicio con todo el paquete disponible para producir las especificaciones, sin comenzar aun la programación del hotel.
