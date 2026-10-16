# Registro de Decisiones de Consolidación SDD

Este documento formaliza las decisiones arquitectónicas, metodológicas y de gobernanza adoptadas por el equipo de consolidación para establecer la **Fuente Única de Verdad** de `plataforma-salman`.

---

## 1. Constitución Compartida como Marco Rector Inmutable

- **Decisión:** Mantener la versión **1.1.0** de la Constitución ([`.specify/memory/constitution.md`](../../.specify/memory/constitution.md)) como la **única** constitución del repositorio.
- **Fundamento:** La constitución contiene 6 principios sólidos (Core primero; Chile operativo; Autonomía gobernada; Seguridad y privacidad; Criterios verificables; Simplicidad y observabilidad) que cubren exhaustivamente las exigencias de arquitectura multi-tenant y gobernanza agéntica.
- **Regla:** Ninguna feature ni documento de investigación puede redefinir, duplicar o flexibilizar los mandatos de la constitución. La ratificación formal de las ampliaciones sigue sujeta al proceso de gobernanza definido con Cristóbal Herrera (Q-GOV-01).

---

## 2. Unificación Canónica de GitHub Spec Kit

- **Decisión:** El catálogo oficial del proyecto se consolida en **77 Requisitos Funcionales (FR)**, **31 Criterios de Éxito Cuantitativos (SC)**, **13 Historias de Usuario activas (US-XXX)** y **65 Criterios de Aceptación (AC)** específicos en formato Given/When/Then.
- **Estructura Canónica:** Cada una de las cinco carpetas de feature bajo [`specs/`](../../specs/) contiene su ciclo completo de 9 artefactos:
  1. `spec.md`: Requisitos de negocio, alcance, historias de usuario, reglas e invariantes.
  2. `research.md`: Alternativas evaluadas, restricciones regulatorias y justificación técnica.
  3. `plan.md`: Propuesta de arquitectura lógica y fases de entrega sin soluciones prematuras.
  4. `data-model.md`: Entidades, atributos, relaciones, máquinas de estado y límites multi-tenant.
  5. `contracts/README.md`: Contratos lógicos de interfaces y esquemas de datos verificables.
  6. `quickstart.md`: Escenarios de verificación funcional y recorridos paso a paso.
  7. `tasks.md`: Lista estructurada de tareas ordenadas por dependencia técnica.
  8. `acceptance.md`: Criterios de aceptación verificables Given/When/Then vinculados a cada FR.
  9. `checklists/requirements.md`: Verificaciones de completitud, seguridad, concurrencia y recuperación.
- **Cero Documentos Paralelos:** Los artefactos canónicos residen exclusivamente en `specs/`. Los documentos en `docs/investigacion-competitiva/` son registros de evidencia de respaldo y auditoría, no especificaciones sustitutivas.

---

## 3. Estado Operativo de REA y Política de Entorno

- **Decisión:** Registrar formalmente la clonación e inspección estática de REA en [`investigacion-herramientas/rea/`](../../../investigacion-herramientas/rea/) (commit `4838f444939677107902549c59b73439e14d3ae9`, tag `rea-agents-6.5.0` en `3b79af28e80785afce9f5998d8f03289402a1847`), pero mantener la ejecución dinámica como **BLOCKED**.
- **Fundamento:** 
  1. El host ejecuta Node.js `v18.19.1`, incompatible con el motor exigido por REA (`node: ^22.19.0 || ^24.11.0 || >=26.0.0`).
  2. Las plataformas investigadas son SaaS comerciales de terceros que no cuentan con sandbox autorizado para instrumentación dinámica invasiva.
  3. La política de gobernanza prohíbe la modificación global de paquetes del sistema operativo o del agente sin autorización previa del usuario.
- **Acción Pendiente:** Solicitar confirmación al usuario antes de planificar cualquier actualización global de Node.js a versión 22+ y configuración de MCP (Q-REA-01 y Q-REA-03).

---

## 4. Política de Gobernanza de Inteligencia Artificial Agéntica

- **Decisión:** Mantener una postura de denegación por defecto con **límite financiero autónomo inicial de 0 CLP**.
- **Reglas Deterministas de Autonomía:**
  1. Los agentes de IA (concierge hotelero, asistente comercial inmobiliario, clasificador de postventa, extractor de notas de obra) operan exclusivamente como **asistentes y redactores de borradores**.
  2. Ningún agente puede confirmar compras, aprobar presupuestos, modificar tarifas hoteleras, alterar estados contables, validar promesas de compraventa ni cerrar observaciones de obra de forma autónoma.
  3. Toda operación con impacto contractual, legal, tributario o financiero debe pasar por un servicio de negocio determinista con validación previa de precondiciones y aprobación humana verificable y de uso único.
  4. Durante la atención humana en conversaciones (handoff en hotel o inmobiliaria), las respuestas automáticas de la IA quedan suspendidas automáticamente.

---

## 5. Control de Alcance: Exclusión de Funcionalidades Complejas (P3)

- **Decisión:** Rechazar la inclusión automática de capacidades complejas observadas en competidores cuando no responden a una necesidad prioritaria fundamentada.
- **Funcionalidades Mantenidas en P3 DRAFT (Fuera de Specs Activos):**
  - `US-HOT-004` (Autopricing y optimización de tarifas): Requiere series de demanda y validación de margen que el cliente no ha entregado.
  - `US-OBR-005` (Optimización paramétrica de cronogramas tipo ALICE): Excede el alcance de la versión 1 y carece de restricciones de obra entregadas.
  - `US-OBR-006` y `US-OBR-007` (Módulo integral de subcontratos enterprise y motor RFI de ingeniería): Condicionados a la definición comercial de la vertical de construcción (Q-OBR-04).

---

## 6. Estado de Bloqueo para Implementación

- **Decisión:** Ratificar el estado **BLOCKED para implementación** en las cinco features.
- **Fundamento:** El objetivo de la fase SDD actual es elevar la calidad de la definición y las pruebas de aceptación, garantizando que el diseño esté completamente blindado antes de programar. No debe escribirse código de producto ni comenzar implementación hasta que las siguientes decisiones comerciales sean resueltas por los responsables del cliente:
  - *Q-COMP-01 (Cafetería):* Regla de asignación del residuo de redondeo en CLP (primer vs último pagador) y modalidad de emisión tributaria SII con boleta electrónica / voucher.
  - *Q-COMP-02 (Hotel):* Política de retención y vencimiento de ofertas de reserva directa y tolerancia a desfases de sincronización en channel managers.
  - *Q-COMP-03 (Inmobiliaria):* Requisitos formales de firma electrónica para promesas de compraventa según Ley 19.799 y política de gestión de agenda de visitas.
  - *Q-COMP-04 (Constructora):* Definición de roles autorizados para el cierre definitivo de observaciones de obra (punch list) y umbrales de alerta de desviación presupuestaria.
