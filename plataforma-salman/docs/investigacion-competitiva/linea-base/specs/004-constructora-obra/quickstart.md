# Revisión documental — Constructora y control de obra

1. Leer spec.md y los bloqueos `Q-OBR-01: obras propias o terceros, presupuesto y módulo previo no entregado; Q-OBR-02: unidad del avance, calendario y umbral; Q-OBR-03: aprobadores, compras, seguridad e inspecciones.`.
2. Contrastar requisitos con la copia original indicada y trazabilidad global.
3. Revisar plan.md contra constitución; validar modelo e interfaces con responsables de negocio, seguridad y operación.
4. Revisar acceptance.md: completar datos, resultados esperados y ventanas antes del desarrollo.
5. Ejecutar desde la raíz `python3 scripts/validar_documentacion.py`; guardar informe. Esta comprobación es local y no es `/speckit.analyze`.
6. Cuando exista entorno Spec Kit inicializado, seguir `docs/auditorias/spec-kit.md`. No ejecutar implement ni converge en esta fase.

No hay aplicación, servidor, migraciones ni comandos de arranque de producto. Las pruebas futuras usan sandbox; producción requiere una fase posterior.
