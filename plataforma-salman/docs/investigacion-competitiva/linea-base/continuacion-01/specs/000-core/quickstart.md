# Revisión documental — Core transversal

1. Leer spec.md y los bloqueos `Q-CORE-01: empresas, roles y autorización entre empresas; Q-CORE-02: tratamiento fiscal y proveedor DTE por contribuyente; Q-CORE-03: responsables de datos, retención, recuperación, presupuesto y autonomía.`.
2. Contrastar requisitos con la copia original indicada y trazabilidad global.
3. Revisar plan.md contra constitución; validar modelo e interfaces con responsables de negocio, seguridad y operación.
4. Revisar acceptance.md: completar datos, resultados esperados y ventanas antes del desarrollo.
5. Ejecutar desde la raíz `python3 scripts/validar_documentacion.py`; guardar informe. Esta comprobación es local y no es `/speckit.analyze`.
6. Cuando exista entorno Spec Kit inicializado, seguir `docs/auditorias/spec-kit.md`. No ejecutar implement ni converge en esta fase.

No hay aplicación, servidor, migraciones ni comandos de arranque de producto. Las pruebas futuras usan sandbox; producción requiere una fase posterior.

## Recorrido de validación competitivo (documental)

Revisar cada US-CORE del spec con sus fuentes y ejecutar en mesa de revisión sus AC propuestos: preparar precondiciones y decisiones cliente → recorrer flujo normal → introducir excepción → verificar estado/evidencia/tenant y quién puede continuar. Usar los ejemplos de acceptance.md; no hay servidor para ejecutar el flujo. Registrar resultado revisado, pendiente o no aplicable, sin marcar una prueba como pasada por leerla.

Comparar con la línea base mediante `git diff --no-index docs/investigacion-competitiva/linea-base/specs/000-core/spec.md specs/000-core/spec.md`. Código de salida 1 indica diferencias, no un error de comparación. Para un paquete revisable completo usar cambios.patch y cambios.json en investigación competitiva.
