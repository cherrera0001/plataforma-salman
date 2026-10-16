# Spec Kit: verificación y compatibilidad

Consulta oficial: 2026-10-16. Release disponible **v1.2.0**, publicada 2026-10-13, identificada con API oficial `/repos/github/spec-kit/releases/latest` y [release](https://github.com/github/spec-kit/releases/tag/v1.2.0). [Referencia SDD](https://github.github.io/spec-kit/reference/agentic-sdd.html), [instalación](https://github.github.io/spec-kit/installation.html) y [README](https://github.com/github/spec-kit).

## Estado comprobado del entorno

`command -v specify` y `command -v uv`: sin resultado. Python 3.12.3 disponible. Sin `.specify` ni configuración de integración previa en los archivos iniciales. `git status --short` falla porque la carpeta no es un repo utilizable; no se modifica el `.git` protegido del entorno. No se ejecutó init ni se instalaron paquetes. Una consulta HTTPS mediante Python falló con `Temporary failure in name resolution`; herramientas web sí permitieron consultar fuentes oficiales. No se fabrica una instalación local ni se atribuye validación al CLI ausente.

## Convenciones aplicadas

Una constitución en `.specify/memory/constitution.md`; cinco features numeradas con spec/plan/research/data-model/quickstart/tasks y contratos/checklists. Las plantillas oficiales de spec y plan fueron inspeccionadas en `main` el 2026-10-16; `main` es mutable, no se afirma igualdad byte a byte con las plantillas del tag. No se copiaron archivos de comandos o scripts internos. Los archivos acceptance.md, catálogo, auditoría y scripts/validar_documentacion.py son **extensiones locales**, no salidas oficiales atribuidas a Spec Kit.

Flujo documentado: constitution una vez; specify → plan → tasks por feature, con clarify/checklist/analyze como controles adicionales. implement y converge se omiten deliberadamente porque la fase no autoriza código. La referencia contempla sintaxis `/speckit.*` y skills `speckit-*` según integración; son invocaciones del agente, no terminal. No se creó `.specify/feature.json`: gestionar feature activa solo tras inicializar con la versión y mecanismo reales.

## Continuación operativa pendiente Q-TOOL-01

En un entorno con red y herramientas disponibles, revisar el release y ejecutar la instalación fijada documentada oficialmente:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v1.2.0
```

Revisar ayuda real de `specify init` y guía de proyecto existente antes de inicializar; no ejecutar a ciegas sobre estos archivos. Inicializar primero una carpeta temporal con integración admitida y comparar plantillas/configuración generadas; preservar este contenido y adoptar únicamente archivos necesarios después de revisar diferencias. El ejemplo oficial `specify init my-project --integration copilot` ilustra una integración, no selecciona la del cliente. No se inventa una opción de sobrescritura ni un comando de validación.

Ejecutar los controles y análisis de agente reales en esa instalación, por feature, y anexar salidas. Hasta entonces la compatibilidad es **documental parcial**, no compatibilidad operacional con versión instalada. Las comprobaciones locales de links, cobertura, estructura y hashes no sustituyen `/speckit.analyze` ni aceptación del negocio. Esta limitación se mantiene abierta en validacion.md.
