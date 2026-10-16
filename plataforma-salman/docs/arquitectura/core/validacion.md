# Informe de Validación Técnica y Normalización: Core Multi-tenant y Gobernanza Agéntica

## 1. Alcance y Entidades de Dominio
- **Identificador de Feature**: `000-core`
- **Esquema PostgreSQL**: `core`
- **Entidades Definidas**: 7 entidades
- **Relaciones Modeladas**: 6 relaciones directas

## 2. Análisis de Formas Normales (1FN a 3FN)
1. **Primera Forma Normal (1FN)**:
   - Todos los atributos contienen valores atómicos indivisibles.
   - Las colecciones o matrices se extraen a tablas de asociación independientes (ej. `detalles_pedido`, `detalles_oc`, `divisiones_cuenta`).
2. **Segunda Forma Normal (2FN)**:
   - Toda columna no clave depende funcionalmente de la totalidad de la clave primaria `id` (o la clave candidata compuesta `(tenant_id, id)`).
3. **Tercera Forma Normal (3FN)**:
   - Se eliminan las dependencias transitivas. Los totales acumulativos (como `total_cuenta_clp` o `costo_comprometido_clp`) se mantienen como proyecciones materializadas transaccionales con control de concurrencia optimista (`version INT`) para evitar bloqueos masivos por agregaciones en lectura caliente.

## 3. Integridad Multi-Tenant y Aislamiento
- Cada tabla contiene la columna discriminadora `tenant_id UUID NOT NULL`.
- Restricción compuesta `UNIQUE (tenant_id, id)` en todas las entidades base.
- Políticas `FORCE ROW LEVEL SECURITY` con validación estricta de contexto `app.current_tenant_id`.
- Bloqueo preventivo de cross-tenant referencing en inserciones y consultas.

## 4. Estado de Validación Ejecutable
- Esquema DDL validado en PostgreSQL 18: **PASS**.
- Verificación estructural de draw.io XML: **PASS**.
- Coherencia con modelo DBML: **PASS**.
