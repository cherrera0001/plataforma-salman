# Estados, aprobaciones y cambios

## Estado real de esta entrega
El método SDD fue aceptado. El paquete contiene el prompt y sus apoyos. No existe aqui ratificación del maestro, código hotelero, cuenta conectada, repositorio creado ni instalación de Spec Kit. El validador de paquete no prueba nada de eso.

## Dimensiones independientes
| Dimension | Estados de referencia |
|---|---|
| Especificación | SEMILLA, BORRADOR, EN_REVISION, BLOQUEADA, APROBADA, SUSTITUIDA |
| Plan | NO_PLANIFICADO, PRELIMINAR, REVISADO, EJECUTABLE_APROBADO |
| Código | NO_IMPLEMENTADO, EN_CONSTRUCCION, IMPLEMENTADO |
| Prueba | NO_EJECUTADA, FALLIDA, PARCIAL, SUPERADA_CON_EVIDENCIA |
| Aceptación | PENDIENTE, RECHAZADA, ACEPTADA |
| Activación | FUTURA, DESACTIVADA, PILOTO, PRODUCCION_AUTORIZADA |
| Integración | DOCUMENTADA, CUENTA_VERIFICADA, PERMISO_VALIDADO, PRUEBA_CONTROLADA, PRODUCCION_VERIFICADA, BLOQUEADA, NO_DISPONIBLE |

No deducir una columna a partir de otra. El estado de integración es por capacidad y por cuenta, no por marca del proveedor. Un permiso vencido revoca la condición operativa aunque haya prueba histórica.

## Autoridades
Ricardo decide objetivos, presupuesto, políticas comerciales y fases. Deben designarse administración, contabilidad/tesoreria, responsable laboral, seguridad/infraestructura y autorizador de salida. Las personas no identificadas se anotan como rol pendiente; no inventar nombres ni exigir programadores humanos para escribir código.

A00 coordina y propone; A13 audita especificaciones; A08 prueba; A07 revisa seguridad. Son responsabilidades que pueden ejecutar agentes; la independencia real debe declararse. El usuario puede aprobar un conjunto de tareas de bajo riesgo; no exigir una confirmación por cada linea de código autorizada.

## Gates
- G0: fuentes, modo, alcance y permisos identificados.
- G1: base de negocio y constitución revisadas; pendientes con punto de bloqueo.
- G2: funcionalidad especificada con pruebas obligatorias y trazabilidad.
- G3: plan, tareas, contratos y dependencias consistentes; autorizar CONSTRUIR_PAQUETE.
- G4: código y pruebas con evidencia; revisión independiente.
- G5: aceptación funcional y financiera cuando corresponde.
- G6: producción autorizada, integraciones reales, respaldo/restauración, personas capacitadas y corte conciliado.

Cada gate registra versión, evidencia y aprobador. Si falta evidencia, no marcarlo aprobado. Un gate documental no comprueba software.

## Control de cambios
Clasificar: corrección de documento, nueva política, nueva funcionalidad, corrección de defecto, cambio de proveedor/stack/modelo, o incidente urgente. En todos los casos identificar alcance, riesgo, requisitos, contratos, datos, pantallas, tareas y pruebas afectados.

El modelo global de negocio vive en el maestro; cada `spec.md` es su refinamiento local. Un cambio global requiere análisis de impacto y actualización de los paquetes afectados. Un cambio local que altere comportamiento empresarial vuelve al maestro y requiere aprobación. No mantener copias divergentes; conservar matriz de versiones y bloquear construcción con baseline obsoleta.

La corrección de un bug puede utilizar un flujo de reparacion compatible si se autoriza. Aun así debe enlazar requisito, causa, prueba de regresion y resultado. Una reparacion no autoriza funcionalidades nuevas.

## Gestión de alcance futuro
E0, E1, E2 y E3 son entregas candidatas, no promesas. P0 es criticidad del alcance activado, no una fecha. Una capacidad futura conserva detalle funcional y requisitos previos; plan y tareas se actualizan al acercarse su implementación. No omitir controles de seguridad, privacidad o dinero de funciones que ya operan.
