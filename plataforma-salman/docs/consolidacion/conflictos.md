# Registro de Conflictos y Resolución Fundamentada

Este documento registra las discrepancias, tensiones técnicas y divergencias documentales identificadas durante la auditoría cruzada entre las evaluaciones previas y la inspección física del repositorio.

---

## Conflicto 1: Estado y Disponibilidad de la Herramienta REA

### Posiciones en Conflicto
- **Posición Codex (documental previa):**
  En [`docs/investigacion-competitiva/rea.md`](../investigacion-competitiva/rea.md) e [`informe-final.md`](../investigacion-competitiva/informe-final.md) se consignó que la clonación de REA mediante `gh repo clone` y `git clone` directo había fallado por autenticación y problemas de resolución DNS, concluyendo que no existía checkout local ni archivos disponibles en el sistema.
- **Posición Antigravity (auditoría física):**
  Se ejecutó `git clone https://github.com/morluto/rea.git investigacion-herramientas/rea/`, verificando la clonación completa del repositorio en el espacio de trabajo independiente con 4,108 archivos. Se extrajo el commit exacto `4838f444939677107902549c59b73439e14d3ae9` (HEAD de main) y el tag oficial `rea-agents-6.5.0` (`3b79af28e80785afce9f5998d8f03289402a1847`), versión 6.5.0.

### Evidencia
- Directorio local [`investigacion-herramientas/rea/`](../../../investigacion-herramientas/rea/) íntegro, sin archivos internos modificados.
- Salida del comando `git rev-parse HEAD` y verificación de etiquetas en `investigacion-herramientas/rea/`.
- Diagnóstico de runtime: Al intentar ejecutar `node scripts/rea.mjs --help` con el Node.js del host (`v18.19.1`), se produce la excepción `TypeError [ERR_IMPORT_ASSERTION_TYPE_MISSING]` porque REA declara en su `package.json` el motor `"node": "^22.19.0 || ^24.11.0 || >=26.0.0"`.

### Riesgo e Impacto
- Sostener que no hay clon local es fácticamente falso y contradice la evidencia en disco.
- Afirmar que REA puede ejecutarse de inmediato ocultaría la incompatibilidad de la versión de Node.js instalada en el sistema operativo y violaría la directriz de no efectuar cambios globales sin autorización.

### Resolución Fundamentada
Se adopta canónicamente la posición de **Clonación Exitosa con Inspección Estática**, pero con **Ejecución Dinámica BLOCKED**:
1. REA está efectivamente clonado y auditado a nivel documental en `investigacion-herramientas/rea/`.
2. Las herramientas dinámicas no se ejecutan debido a incompatibilidad de runtime (Node 18 vs Node 22+) y a la política de no instalar paquetes globales sin aprobación explícita del usuario.
3. Se actualizan todos los registros de estado en [`rea.md`](../investigacion-competitiva/rea.md) y [`decisiones-pendientes.md`](../investigacion-competitiva/decisiones-pendientes.md).

---

## Conflicto 2: Recuento de Comprobaciones de Validación Automatizada

### Posiciones en Conflicto
- **Posición Previa Reportada:**
  El informe previo indicaba la existencia de 991 comprobaciones (398 en validación documental local y 593 en investigación competitiva).
- **Posición de Auditoría Antigravity:**
  Al inspeccionar la carpeta `scripts/`, se localizó el script adicional [`validar_continuacion.py`](../../scripts/validar_continuacion.py) (564 comprobaciones) que valida la fase de profundización de hotel, inmobiliaria, constructora y core. Al reproducir la ejecución síncrona en vivo de las tres suites completas, el resultado verificado arrojó:
  - `validar_documentacion.py`: 468 comprobaciones
  - `validar_investigacion.py`: 610 comprobaciones
  - `validar_continuacion.py`: 564 comprobaciones
  **Total real reproducido: 1,642 comprobaciones (0 errores).**

### Evidencia
- Registros de salida de subprocesos en la terminal.
- Archivos generados: [`docs/auditorias/validacion-local.json`](../auditorias/validacion-local.json), [`docs/investigacion-competitiva/validacion.json`](../investigacion-competitiva/validacion.json) y [`docs/investigacion-competitiva/continuacion-01/validacion.json`](../investigacion-competitiva/continuacion-01/validacion.json).

### Riesgo e Impacto
- Quedarse con la cifra histórica de 991 comprobaciones ignoraría las pruebas introducidas en la fase de continuación y degradaría la trazabilidad de los nuevos criterios de aceptación.

### Resolución Fundamentada
Se adopta como cifra canónica el total de **1,642 comprobaciones reproducidas en vivo**, explicando con precisión matemática la composición y el propósito de cada una de las tres suites de prueba.

---

## Conflicto 3: Catálogo Canónico de Requisitos Funcionales (66 FR vs. 77 FR)

### Posiciones en Conflicto
- **Catálogo Inicial:**
  [`docs/auditorias/catalogo-requisitos.json`](../auditorias/catalogo-requisitos.json) contenía 66 FRs y 31 SCs correspondientes a la línea base inicial.
- **Catálogo Enriquecido por Continuación:**
  En la profundización documental se agregaron 11 FRs adicionales:
  - `000-core`: FR-012 (Control de efectos laterales en persistencia).
  - `002-hotel-reservas-concierge`: FR-018 (Edición/cancelación con tarifa versionada), FR-019 (Cargos extras y periodicidad), FR-020 (Acuse durable en recepción OTA).
  - `003-inmobiliaria-comercial`: FR-017 (Agenda estática vs sincronizada), FR-018 (Firma electrónica con validez legal), FR-019 (Control de envío en creación de contacto), FR-020 (Segregación Persona y VínculoUnidad).
  - `004-constructora-obra`: FR-021 (Partes diarios por turnos y deduplicación por origen), FR-022 (Recepción parcial y rechazo por entrega), FR-023 (Trazabilidad presupuestaria: comprometido, devengado, pagado).

### Evidencia
- Archivos canónicos [`specs/*/spec.md`](../../specs/) y especificaciones de aceptación [`specs/*/acceptance.md`](../../specs/).
- Manifiestos de línea base incremental en [`linea-base/continuacion-01/manifest.json`](../investigacion-competitiva/linea-base/continuacion-01/manifest.json).

### Riesgo e Impacto
- Descartar los 11 FRs nuevos provocaría regresión en el diseño de las cuatro verticales, omitiendo los comportamientos refinados a partir de manuales oficiales de Mews, Cloudbeds, Booking, Structurely, PlanOK, Procore e ICONSTRUYE.

### Resolución Fundamentada
Se ratifica e integra el catálogo de **77 Requisitos Funcionales y 31 Criterios de Éxito**, preservando la totalidad de los identificadores originales sin introducir renumeraciones que rompan la trazabilidad.

---

## Conflicto 4: Tratamiento de Funcionalidades Complejas de Competidores (P1/P2 vs. Candidatas P3)

### Discrepancia Potencial
- La investigación de mercado identificó funciones de alta complejidad en plataformas como ALICE Technologies (reprogramación algorítmica de obra), Toast/Revinate (autopricing dinámico hotelero) o Procore (gestión integral de subcontratos complejos).
- Podría surgir la tentación de incorporarlas como requisitos de implementación obligatoria.

### Evaluación y Evidencia
- Las cinco features se encuentran formalmente en estado **BLOCKED para implementación**.
- No existen datos de demanda de clientes, series históricas de tarifas, matrices de restricciones de obra ni políticas comerciales ratificadas para justificar algoritmos autónomos complejos.
- Los principios constitucionales I (Core primero), III (Agentes gobernados) y VI (Simplicidad y YAGNI) exigen no construir mecanismos heterogéneos sin justificación comprobada.

### Resolución Fundamentada
- Se mantiene la estricta exclusión de estas funciones de los requisitos activos.
- Quedan registradas únicamente como propuestas futuras en estado **P3 DRAFT**:
  - `US-HOT-004`: Comparación de tarifas competitivas (OP-07).
  - `US-OBR-005`: Simulación de escenarios de programación de obra (OP-08).
  - `US-OBR-006`: Gestión formal de subcontratos (sujeta a Q-OBR-04).
  - `US-OBR-007`: Consultas técnicas en obra tipo RFI (fuera de alcance actual).
- Ninguna de ellas cuenta con FR activo ni compromete recursos de ingeniería en esta etapa.
