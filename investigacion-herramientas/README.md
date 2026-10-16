# Investigación de REA

Clon solicitado: `git clone https://github.com/morluto/rea.git investigacion-herramientas/rea`.
Estado: **Completado exitosamente**.

- Repositorio: `morluto/rea` (oficial).
- Directorio local: `investigacion-herramientas/rea/` (directorio de investigación independiente, sin tocar código del producto).
- Commit exacto HEAD: `4838f444939677107902549c59b73439e14d3ae9` (fecha: Sat Oct 17 01:49:55 2026 +0800).
- Release tag oficial: `rea-agents-6.5.0` (`3b79af28e80785afce9f5998d8f03289402a1847`).
- Versión de paquete: `6.5.0` (`rea-agents`, MCP: `io.github.morluto/rea`).
- Integridad: No hay archivos internos modificados en REA. No contiene credenciales ni tokens.
- Diagnóstico de entorno local:
  - Runtime actual: Node.js `v18.19.1`, npm `9.2.0`.
  - Requisito de runtime declarado por REA (`package.json`): `"engines": { "node": "^22.19.0 || ^24.11.0 || >=26.0.0" }`.
  - Comprobación de ejecución local de REA: `node scripts/rea.mjs --help` arroja `TypeError [ERR_IMPORT_ASSERTION_TYPE_MISSING]` debido a que Node 18 no soporta la sintaxis de import attributes (`with { type: "json" }`) requerida por la versión 6.5.0 de REA.
  - Disponibilidad en Codex / Antigravity: REA no está instalado globalmente (`npm list -g --depth=0` vacío) ni registrado en la configuración MCP del entorno.
  - Política de cambios globales: Conforme a las instrucciones, la instalación global (`npm install -g rea-agents`) o actualización de Node.js a versión 22+ y configuración de MCP requiere evaluación previa y aprobación explícita del usuario antes de efectuar cambios globales en el sistema.
- Documentación de investigación: Consultar `plataforma-salman/docs/investigacion-competitiva/rea.md` e `informe-final.md`.
