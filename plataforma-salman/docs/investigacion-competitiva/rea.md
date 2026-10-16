# Disponibilidad real de REA

## Identidad y revisión oficial

Repositorio [morluto/rea](https://github.com/morluto/rea). Clonado en directorio independiente: `investigacion-herramientas/rea/`.
- Commit exacto HEAD: `4838f444939677107902549c59b73439e14d3ae9` (fecha: Sat Oct 17 01:49:55 2026 +0800).
- Release oficial fijado: [rea-agents-6.5.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.5.0), tag commit `3b79af28e80785afce9f5998d8f03289402a1847`.
- Paquete: `rea-agents` v6.5.0, MCP name: `io.github.morluto/rea`.
- Código interno de REA: íntegro, sin modificaciones. No contiene credenciales ni secretos.

Lecturas de documentación oficial:
- [README](../../../investigacion-herramientas/rea/README.md)
- [Instalación oficial fijada al commit](https://raw.githubusercontent.com/morluto/rea/3b79af28e80785afce9f5998d8f03289402a1847/docs/installation.md)
- [Observación web fijada](https://raw.githubusercontent.com/morluto/rea/3b79af28e80785afce9f5998d8f03289402a1847/docs/browser-observation.md)
- [Contratos MCP](../../../investigacion-herramientas/rea/docs/mcp-contracts.md)

## Estado de clonación e instalación comprobada

1. **Clonación local:** Completada exitosamente en `investigacion-herramientas/rea/` mediante `git clone https://github.com/morluto/rea.git`. El árbol de archivos está íntegro y sin modificaciones.
2. **Disponibilidad en PATH y sistema:** `rea` no está en PATH. No hay instalación global en el sistema (`npm list -g --depth=0` vacío). No hay configuración de servidor MCP de REA registrada en Codex o Antigravity.
3. **Diagnóstico de ejecución local:**
   - Runtime del sistema: Node.js `v18.19.1` y npm `9.2.0`.
   - Requisito de runtime declarado en `package.json` de REA: `"engines": { "node": "^22.19.0 || ^24.11.0 || >=26.0.0" }`.
   - Comprobación: La ejecución directa de los scripts ESM de REA (`node scripts/rea.mjs --help`) arroja `TypeError [ERR_IMPORT_ASSERTION_TYPE_MISSING]` debido a que Node.js 18 no soporta de forma nativa la sintaxis de import attributes (`with { type: "json" }`) requerida por la versión 6.5.0.

## Capacidades pertinentes y límites

REA documenta capacidades de análisis estático (binarios nativos, Hopper/Ghidra/IDA, JavaScript/Electron ASAR) y observación web mediante CDP (Chrome DevTools Protocol) en puerto loopback para targets explícitamente autorizados.

Operaciones documentadas pertinentes: `list_browser_targets`, `inspect_web_page`, `observe_web_session`, `compare_web_captures`, `capture_web_screenshot`.

**Operaciones dinámicas de REA ejecutadas en esta fase: ninguna.**
Motivos técnicos y de gobernanza:
- No se han efectuado modificaciones globales al entorno (actualización a Node >= 22.19.0 ni `npm install -g rea-agents`) a la espera de aprobación del usuario.
- Los portales comerciales y SaaS investigados son sistemas de terceros protegidos por autenticación y términos de servicio; no se dispone de sandbox o entorno de demo autorizado para instrumentación dinámica intrusiva.
- La investigación se sustenta en fuentes documentales primarias, manuales oficiales, especificaciones de API y análisis funcional estricto de interfaces públicas.

## Configuración oficial y solicitud de aprobación

La guía oficial de REA establece el flujo de configuración:
```bash
npx rea-agents setup
# O para previsualizar sin aplicar cambios:
rea setup --client codex --dry-run --json
```

Este procedimiento registra el servidor MCP de REA y sus instrucciones de flujo de trabajo en la configuración del agente, y puede sugerir la instalación de dependencias nativas (como Hopper o Ghidra).

**Evaluación y política de gobernanza:**
Conforme a las instrucciones recibidas, **no se aplican cambios globales en el entorno sin aprobación previa del usuario**. La ejecución dinámica de REA permanece como **BLOCKED** para salvaguardar la estabilidad del sistema, respetando que cualquier actualización global de Node.js o registro de MCP sea explícitamente autorizada.

## Reintento de continuación

Se volvió a intentar `gh repo clone morluto/rea investigacion-herramientas/rea` con el token del usuario pasado solo al entorno del subproceso. Resultado: error de conexión a api.github.com. No se concluye validez/invalidez del token. Sin checkout, herramientas MCP/CLI ni captura REA nuevos. La investigación de hotel/inmobiliaria/obra continuó documentalmente; no se presentó como observación de runtime.
