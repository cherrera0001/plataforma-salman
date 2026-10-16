# Plataforma Salman

La raíz Git es esta carpeta. La fuente documental activa está en
[plataforma-salman](plataforma-salman/README.md).

- [Informe vigente de consolidación](plataforma-salman/docs/auditoria/consolidacion-final.md).
- [Constitución propuesta](plataforma-salman/.specify/memory/constitution.md).
- [Cinco features canónicas](plataforma-salman/specs/).
- [Modelos y diagramas](plataforma-salman/docs/arquitectura/README.md).
- [Fuentes originales íntegras](plataforma-salman/docs/originales/).

Desde la raíz Git, con Python 3:

```bash
python plataforma-salman/scripts/validar_todo.py
python plataforma-salman/scripts/auditar_consolidacion.py
```

El primer comando ejecuta cinco suites documentales y de modelos. No ejecuta
PostgreSQL ni realiza una revisión visual. El segundo inventaría los archivos y
examina patrones de secretos en el árbol actual y en blobs alcanzables por Git;
no imprime credenciales. Las líneas base son archivos históricos, no specs activas.

`investigacion-herramientas/rea/` es un checkout externo ignorado, con Git propio;
no forma parte del producto. `.env` permanece local y excluido de Git.
Las cinco features siguen bloqueadas para implementación.
