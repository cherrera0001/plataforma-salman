# Consolidación definitiva — estado verificable

Fecha: 16-10-2026. Estado: consolidación local realizada; publicación bloqueada.
Este es el único informe vigente de esta misión. Los informes competitivos son
evidencia de fases diferentes; el informe anterior de consolidación es un enlace histórico.

## Git y publicación

- Raíz: `F:/Code/RSalman`; rama: `docs/consolidacion-definitiva`.
- Base preservada: `707b586` (arquitectura visual). El árbol tenía un cambio previo
  en `docs/auditorias/arbol.txt`; su inventario fue actualizado, sin descartar fuentes.
- HEAD final: consultar `git rev-parse HEAD` en la raíz; el hash del commit que
  contiene este informe no puede incrustarse en su propio contenido.
- GitHub: no hay remoto configurado, URL real disponible ni rama publicada.
- PR: no creado. No se usó force push ni se reescribió el historial.
- Evidencia de bloqueo: `gh api user` devolvió error de socket no permitido al
  conectar a `api.github.com:443`. La solicitud de ejecución con red ampliada fue
  rechazada por revisión automática por falta de autorización explícita reconocida
  para leer el token de `.env` y publicar. No se reintentó por otra vía.
- Repositorio anidado: únicamente el checkout externo ignorado de REA. No se alteró.

## Autoridad y estructura

La raíz Git contiene el README de navegación y configuración de exclusiones.
Dentro de `plataforma-salman/`: `.specify/` conserva la constitución propuesta y
su estructura real; `specs/` contiene cinco features activas; `docs/investigacion/`
y `docs/investigacion-competitiva/` conservan evidencia primaria y contextual;
`docs/arquitectura/` contiene modelos; `scripts/` contiene verificadores;
`core/` y `verticales/` reservan implementación futura.

Se conservan `docs/arquitectura/decisiones/` y `docs/auditorias/` para no romper
enlaces y automatizaciones existentes. `docs/auditoria/` contiene la evidencia de
esta misión. No se crean copias de ADR ni se mueve la estructura de Spec Kit.

Los requisitos, historias y criterios vigentes pertenecen a `specs/*/spec.md` y
`acceptance.md`; el catálogo de `docs/auditorias/catalogo-requisitos.json` comprueba
sus IDs por namespace. Los `research.md` son la síntesis por feature. Las fuentes
originales y las líneas base no son especificaciones activas.

## Inventario y preservación

El primer inventario examinó 325 archivos propios; excluyó `.git`, cachés y el
checkout externo REA. El inventario actualizado registra cada ruta, clasificación,
motivo y SHA-256, excepto secretos locales cuyo hash también se omite:
[inventario](inventario-consolidacion.json).

Se eliminaron cuatro copias de originales en la raíz. Se comprobó igualdad
binaria con `docs/originales/`, hash del manifiesto y blob recuperable en el commit
base antes de borrar. Requisitos, citas, metadatos y binarios quedan íntegros.
[Matriz de equivalencias y recuperación](equivalencias-eliminados.json).
No se eliminó ninguna fuente primaria única ni línea base.

Los 19 grupos iniciales de igualdad exacta comprendían cuatro copias eliminadas,
archivos de baseline y cinco SQL derivados. Las baselines permanecen porque los
validadores comprueban su integridad. Los cinco SQL de `pruebas/sql/` son copias
generadas de los DDL por dominio usadas por el arnés histórico; no son modelos
independientes. Las diferencias semánticas entre niveles conceptual y físico
requieren revisión humana antes de implementar; igualdad de hash no demuestra
equivalencia de modelos distintos.

## Modelos canónicos y regeneración

`docs/arquitectura/datos/` contiene la propuesta conceptual y lógica transversal.
En cada dominio de `docs/arquitectura/`, `mer.mmd` representa el MER,
`modelo-relacional.dbml` el modelo relacional propuesto y `esquema-propuesto.sql`
el DDL propuesto. `*.drawio` representa vistas de datos, estados y secuencias;
`transversal/` contiene C4 y vistas integradas.

El generador `scripts/generar_y_validar_arquitectura.py` contiene las definiciones
`DOMAINS` y produce estas representaciones y las copias SQL de pruebas. Su ejecución
también escribe documentación y puede ejecutar Docker: no se ejecutó para esta
limpieza. Cambios en sus definiciones requieren regeneración controlada y revisión
de diff. No editar una copia SQL de pruebas como un segundo modelo independiente.
No se afirma equivalencia semántica total ni cierre de hallazgos de datos con una
simple validación estructural. El desarrollo sigue bloqueado.

## Cobertura y validaciones

Se resuelve 77 frente a 91: core 12 FR, cafetería 16, hotel 20, inmobiliaria 17 y
constructora 12: total 77 FR y 31 SC. El desglose 20 inmobiliaria y 23 constructora
del informe anterior era incorrecto. No se renumeraron IDs. Se conservan 13 historias
y 65 AC competitivos, además de las pruebas propuestas AT por requisito.

El [resultado consolidado](validacion-consolidada.json) distingue cinco suites:
documentación, semántica de investigación, semántica de continuación, modelos de
datos y estructura XML/evidencia histórica. Todas se ejecutan mediante
`python scripts/validar_todo.py` desde `plataforma-salman/`.

La ejecución final obtuvo 553 + 610 + 564 + 29 + 209 = 1.965 comprobaciones,
sin errores. La cifra documental varía con enlaces añadidos y hashes de copias
eliminadas; los JSON generados registran el resultado actual. La suite documental
comprueba enlaces relativos y cobertura FR/SC/AT.

PostgreSQL actual: NO EJECUTADO. Revisión visual actual: NO EJECUTADA.
La suite que lee logs PostgreSQL comprueba evidencia histórica, no ejecuta SQL.
No se presentan estas comprobaciones como análisis oficial de Spec Kit ni pruebas
funcionales de producto.

## Seguridad y pendientes

El primer examen recorrió 308 blobs históricos alcanzables, además del árbol actual:
cero coincidencias detectadas y cero `.env` versionados. Se compararon valores
sensibles locales en memoria y patrones de GitHub, AWS y claves privadas, sin
imprimirlos. [Resultado actualizado y límites](seguridad-consolidacion.json).
Es un detector acotado; no acredita ausencia universal de secretos. No se verificó
validez, propietario ni permisos del token por el bloqueo de red y aprobación.
`.env.example` está permitido con valores ficticios; no se creó sin necesidad.

Pendientes: autorización explícita reconocida para usar el token y publicar;
verificar cuenta/permisos, reutilizar remoto o crear repositorio privado,
publicar esta rama y abrir PR a `main`. Antes de desarrollo: ratificación de la
constitución, resolución de preguntas comerciales, reconciliación semántica de
modelos, PostgreSQL aislado y revisión visual. No se declara completa la misión
de publicación ni la validación semántica integral de modelos.
