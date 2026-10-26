# Uso posterior con Spec Kit

## Ahora: producir especificaciones
Extraer el ZIP, conservar la carpeta completa y entregar su contenido al agente. Ejecutar `02_INICIAR_ESPECIFICACIONES.txt`. No pegar solo el archivo de instrucciones de inicio sin los archivos que menciona. Si el agente no ve el sistema de archivos, adjuntar el ZIP y exigir que lo inspeccione.

No hace falta instalar Spec Kit para redactar el maestro, pero entonces la salida se declara compatible documentalmente y no probada en runtime. Para preparar planes concretos se inspeccionara el entorno autorizado cuando exista.

## Después: inicializacion controlada
Aprobados el agente, versión, repositorio y permisos, consultar SDD02/SDD04 en el registro de fuentes. Los siguientes son PATRONES oficiales, no comandos ejecutados aqui ni una recomendacion de versión concreta:

```text
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
specify version
specify init <directorio-nuevo> --integration <clave-verificada> --script <sh|ps|py>
```

Sustituir todos los marcadores antes de usar; consultar la ayuda de la versión elegida. No ejecutar `init` sobre un repositorio existente sin el procedimiento de adopción/backup. No usar `--force`, omitir verificaciones o aceptar ejecución de extensiones por comodidad. Windows, shell y disponibilidad de herramientas deben comprobarse, no asumirse.

## Instalar nuestras reglas
Comparar el AGENTS existente, adoptar la constitución propuesta ratificada y cargar las reglas del proyecto. Mantener la estructura oficial y registrar ubicaciones reales. Si se aplican overrides, revisar el mecanismo de la versión fijada; no copiar plantillas a rutas no verificadas.

Los archivos de `plantillas/` son plantillas originales del proyecto para asegurar contenido. Se utilizan como guía o se adaptan al template nativo. No se distribuyen componentes de Spec Kit ni se incluye un plugin instalable en este ZIP.

## Preparar un paquete
Seleccionar una ficha `backlog/`, confirmar que sus dependencias y baseline estan listas, y ejecutar specify/clarify/plan/checklist/tasks/analyze en el agente con la sintaxis instalada. Alimentar solo la funcionalidad activa y las reglas compartidas necesarias. Comprobar resultado después de cada paso.

Antes de construir, revisar alcance, versión, prueba obligatoria, plan, tasks, gates y autorización. Solo entonces ejecutar implement. Probar, converger y revisar con los límites acordados. Aprobar y liberar son actos posteriores.

## Actualizaciones y cambio de agente
Registrar versión previa, evaluar diferencias de templates/comandos y hacer un piloto con datos ficticios. Revalidar constitución, ruta activa, sintaxis e integraciones. Conservar archivos de negocio y evidencias; no reiniciar el proyecto desde cero al cambiar de modelo. No declarar compatibilidad nativa hasta comprobarla con la combinacion concreta.
