# Inventario inicial — 2026-10-16

Inspección recursiva con `rg --files --hidden`, excluyendo metadatos protegidos. Cuatro entradas; sin código, especificaciones separadas ni configuración Spec Kit previa visible. `.git`, `.agents`, `.codex` y `.aws` son directorios protegidos del entorno; `git status --short` falla: no hay repositorio Git utilizable. No se altera esa configuración. Python 3.12.3 disponible; `specify` y `uv` ausentes en PATH. La red del shell falla por DNS; navegación web sí disponible.

La fecha editorial común es 2026-10-15, no equivale a validación de las afirmaciones. La fecha técnica y el SHA-256 constan en `originales-sha256.json`. Los originales siguen en la raíz y se copiaron byte a byte a `docs/originales/`. El DOCX se extrajo con ZIP/XML estándar, preservando el orden de párrafos y celdas; no se preserva su diseño gráfico en Markdown. El binario conserva la fuente completa.

| ID | Ruta original / copia en docs/originales | Formato | Propósito | Estado y dependencias | Problemas |
|---|---|---|---|---|---|
| INV | Estado del arte IA agéntica en hotel, inmobiliaria y cafetería (oct 2026) (1).docx | .docx | Contexto de mercado e integraciones | Fuente conservada; proveedores externos | Ver auditoría individual y hallazgos |
| CAF | Spec SDD 01 Cafetería (mesas, POS inteligente y control de gastos) (1).md | .md | Mesas, POS, gastos y constitución propuesta | Fuente conservada; core y medios Chile | Ver auditoría individual y hallazgos |
| HOT | Spec SDD 02 Hotel (reservas, operación y concierge agéntico) (1).md | .md | Reservas, operación y concierge | Fuente conservada; core, PMS, OTA y pedidos opcionales | Ver auditoría individual y hallazgos |
| INM | Spec SDD 03 Inmobiliaria y constructora (plataforma comercial y control de obra) (1).md | .md | Comercial inmobiliario y puente a obra | Fuente conservada; core, firma, portales y presupuesto de obra | Ver auditoría individual y hallazgos |
