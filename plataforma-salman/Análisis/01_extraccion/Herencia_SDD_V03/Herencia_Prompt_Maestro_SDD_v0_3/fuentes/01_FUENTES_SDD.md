# Fuentes oficiales consultadas para V0.3

Consulta: 2026-10-24. Solo documentación pública. No se instalaron herramientas ni se accedio a cuentas del hotel. Las páginas `main` son mutables: escoger y fijar release/commit antes de ejecución nativa. Las fuentes sustentan características del marco, no garantizan compatibilidad ejecutada.

## SDD01 - GitHub Spec Kit - Quickstart

https://github.github.com/spec-kit/quickstart.html

Uso: Flujo completo, directorio activo, checklist y pasos del agente.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD02 - GitHub Spec Kit - Integration CLI

https://github.github.com/spec-kit/integrations/cli.html

Uso: Sintaxis según agente; integraciones y seguridad de instalación.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD03 - GitHub Spec Kit - Agentic SDD

https://github.github.com/spec-kit/reference/agentic-sdd.html

Uso: Comandos, artefactos y taskstoissues deprecado.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD04 - GitHub Spec Kit - Installation

https://github.github.com/spec-kit/installation.html

Uso: Fijacion de versión y prerequisitos; no instalación realizada.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD05 - GitHub Spec Kit - tasks template

https://raw.githubusercontent.com/github/spec-kit/main/templates/tasks-template.md

Uso: Tests opcionales salvo solicitud expresa: el proyecto los exige siempre.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD06 - GitHub Spec Kit - converge command

https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/converge.md

Uso: Inventario de intención local; tareas correctivas; no modifica spec/plan/código.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD07 - GitHub Spec Kit - constitution command

https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/constitution.md

Uso: Ruta .specify/memory/constitution.md, límites y versionado.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD08 - GitHub Spec Kit - common Python helpers

https://raw.githubusercontent.com/github/spec-kit/main/scripts/python/common.py

Uso: Resolución de feature dir y opcion no-persist cuando soportada.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## SDD09 - GitHub Spec Kit - plan template

https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md

Uso: Modelo de artefactos, contratos y comprobación constitucional.
Estado: consultada en esta revisión; revalidar contra la versión instalada.

## Evidencia heredada

Los archivos de fuentes V0.1/V0.2 se incluyen como antecedentes, con sus fechas y limitaciones originales. No se afirma haber vuelto a verificar todos sus precios, permisos ni reglas legales en esta entrega. Al producir el maestro, revalidar normas, servicios y contratos pertinentes para el alcance y fecha de operación. No copiar como vigente una tasa, precio o API por figurar en el historial.

## Discrepancias controladas

Algunas referencias de converge abrevian la ruta constitucional como `/memory/constitution.md`; constitution describe `.specify/memory/constitution.md`. Se exige verificar la ruta efectiva y que todos los comandos lean la misma versión. Un resultado indexado antiguo que asocia feature exclusivamente a rama no prevalece sobre el comportamiento de la versión comprobada. No se distribuye código oficial de Spec Kit dentro de este paquete.
