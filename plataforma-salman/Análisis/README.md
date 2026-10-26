# Análisis – Importación de fuentes Hotel Herencia (Paso 1)

Carpeta de trabajo para analizar, en un mismo tablero, las especificaciones de Hotel Herencia y del núcleo del Grupo Salman. Este documento registra **solo el Paso 1: importación y verificación de los datos**. No se ha analizado todavía el contenido de negocio ni se ha integrado Kimi.

Fecha de la importación: 2026-10-26.

## 1. Fuentes importadas

Origen: `C:\Users\herre\Downloads` (vista WSL: `/mnt/c/Users/herre/Downloads`). Los originales **no se modificaron**; se copiaron a `00_originales_copia/`.

| # | Archivo original | Bytes | SHA-256 | Contenido verificado |
|---|---|---|---|---|
| 1 | `Herencia_SDD_V03.zip` | 268 422 | `cde603e561e9613c576feda148232a2aedd2e711ba11186344dea0111aab8cc7` | Paquete "Prompt Maestro SDD v0.3" (24 oct. 2026), 88 archivos |
| 2 | `Herencia_Especificaciones_V1.zip` | 916 484 | `5d9abec78f83e11a5a2a42283449b6057aafb936c14f0e7f50915d37854447b6` | Especificaciones V1.0 (25 oct. 2026), 372 archivos |
| 3 | `Herencia_Especificaciones_V1 28 p.docx` | 72 287 | `2cc11036b5dd0e994820c949dc3fbca8eb54d582ca15b89c5f92a1666dc7a115` | Documento Maestro V1.0 en Word |

Orden cronológico de la cadena: **SDD V0.3 → Especificaciones V1.0 (zip) → Documento Maestro Word**.

## 2. Estructura de esta carpeta

```
Análisis/
├── README.md                      Este índice y el estado del Paso 1
├── 00_originales_copia/           Copias byte a byte de las 3 fuentes (verificadas por SHA-256)
├── 01_extraccion/                 Contenido descomprimido de los zip (no ejecutado)
│   ├── Herencia_SDD_V03/
│   └── Herencia_Especificaciones_V1/
├── 02_texto/                      Texto plano del Word + PDF de verificación de páginas
├── 03_inventario/                 CSV con ruta, bytes, SHA-256 y extensión de cada archivo
└── scripts/                       Utilidades de importación (fuera de las carpetas descomprimidas)
```

## 3. Verificaciones realizadas

| Verificación | Resultado | Etiqueta |
|---|---|---|
| SHA-256 de las copias = SHA-256 de los originales en Descargas (3/3) | Coincide | HECHO DOCUMENTADO (verificado) |
| Hashes de `MANIFEST.json` del paquete V1 contra archivos extraídos | 371 de 371 coinciden; el MANIFEST no incluye a sí mismo | HECHO DOCUMENTADO (verificado) |
| Hashes de `MANIFEST.json` del paquete SDD V0.3 contra archivos extraídos | 86 de 86 coinciden; excluye `MANIFEST.json` y `informes/VALIDACION_FINAL.json` según su propia regla | HECHO DOCUMENTADO (verificado) |
| `fuentes/procedencia_hash.json` del zip V1 declara como origen el SHA-256 de `Herencia_SDD_V03.zip` | Coincide exacto con el archivo real | HECHO DOCUMENTADO (verificado) |
| Baseline de requisitos (`requisitos_baseline_V0_3.csv`) | Hash declarado = hash real del archivo dentro del V1 | HECHO DOCUMENTADO (verificado) |
| Rutas citadas en `00_ENTREGA.md` del V1 (`sdd/`, `specs/`, `registros/`, `ux/`, `seguridad/`, `reglas/`) | Todas existen | HECHO DOCUMENTADO (verificado) |
| Texto del Word suelto vs. `Documento_Maestro_Herencia_V1_0.docx` dentro del zip | **Texto idéntico** (453 líneas, 0 diferencias). Los bytes del archivo difieren | HECHO DOCUMENTADO (verificado) |

## 4. Hallazgos y puntos a aclarar

Estas observaciones son de importación, no de negocio.

1. **CONTRADICCIÓN MENOR – número de páginas.** El nombre del Word dice "28 p." y sus metadatos (`app.xml`) declaran 28. Al renderizarlo con LibreOffice salen **33 páginas** (PDF en `02_texto/pdf_verificacion/Word_suelto_copia.pdf`). Puede deberse al motor de render o a las fuentes. Hay que confirmar la paginación en Word antes de citar "28 p.".
2. **INFORMACIÓN – dos versiones "iguales" del Word.** El texto es idéntico, pero el Word suelto fue guardado por un procesador (metadatos de Word, 28 p.), mientras que el interno fue generado por script (`app.xml` declara 1 página). PROPUESTA: usar el Word suelto como versión de referencia del Documento Maestro y el interno como respaldo del mismo contenido.
3. **INFORMACIÓN – paquetes con código.** Ambos zip incluyen archivos `.py` (2 en SDD V0.3, 1 en V1) y 1 `.yaml`. **No se han ejecutado.** Quedan marcados para revisión antes de cualquier uso.
4. **INFORMACIÓN – cifras declaradas, no verificadas aún.** El documento y el paquete afirman 153 requisitos, 505 tareas, 306 casos, 48 escenarios, 109 entidades, 53 pantallas y 45 decisiones. Este Paso 1 **no ha recontado** esas cifras; queda como **INFORMACIÓN NO VERIFICADA** hasta el análisis de contenido.
5. **DECISIÓN PENDIENTE (heredada del propio paquete).** El V1 indica que stack, proveedores, precios, políticas y datos reales **no están aprobados**. Esto se mantiene como estado documentado, no como decisión de esta carpeta.

## 5. Qué NO se ha hecho en este paso

- No se ha modificado ningún archivo de `Descargas` ni de la carpeta padre.
- No se ha ejecutado código de los paquetes.
- No se ha seleccionado una feature activa ni generado archivos de Spec Kit (`implement` y `converge` quedan fuera de esta entrega, según `AGENTS.md`).
- No se ha conectado Kimi ni creado el tablero compartido.

## 6. Próximos pasos propuestos (Paso 2 en adelante)

Cada paso se hará tras tu confirmación, para avanzar de forma verificable:

1. **Paso 2 – Mapa de contenido.** Índice de los 24 capítulos del maestro (`maestro/M01…M24`) y de las 23 fichas SDD, con referencias a los requisitos originales.
2. **Paso 3 – Recuento de cifras.** Contrastar las cifras declaradas (153 / 505 / 306 / 48 / 109 / 53 / 45) con los CSV de `fuentes/`, `modelos/`, `pruebas/` y `registros/`.
3. **Paso 4 – Tablero compartido para Claude y Kimi.** Definir cómo se comparte el material (formato, convención de etiquetas y lista de preguntas), una vez confirmado el formato con el usuario.

Fuentes de trabajo para el Paso 2: `02_texto/Documento_Word_Especificaciones_V1.txt` e `03_inventario/inventario_Especificaciones_V1.csv`.
