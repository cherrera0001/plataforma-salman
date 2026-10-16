# Visión general

**plataforma-salman** es un monorepo documental para un SaaS de negocios separados. No existe aplicación funcional. Tenants representan empresas con permisos y responsabilidades propios; propiedad común no implica visibilidad común. Una propiedad o local es ámbito operativo dentro de la empresa, no un tenant universal decidido de antemano. Q-CORE-01 debe confirmar la jerarquía.

Core mínimo: identidad/autorización, aislamiento, adaptadores financieros/documentales, mensajería como mecanismo y auditoría. No contiene catálogo universal, recetas, gastos de obra y cafetería mezclados, ni analítica comercial genérica. La política de cada operación y su fuente de verdad pertenecen al dominio; el core aplica controles y adaptadores sin decidir garantías o tarifas.

Cafetería posee mesas, pedidos, recetas, cocina y stock; hotel posee inventario por fecha, reservas, cuentas y tareas operativas o integra un PMS; inmobiliaria posee proyectos comerciales, unidades, leads y promesas; constructora posee obra, partidas, avances, materiales e inspecciones. Los proyectos comerciales y de obra pueden corresponder sin ser la misma entidad ni compartir todos sus atributos.

Se recomienda evaluar límites modulares antes de decidir procesos separados o microservicios. Python/FastAPI, Next.js, PostgreSQL, Redis y SDK agéntico son candidatos de las fuentes; no existe ADR de selección. No se impone cloud, región, topología, licencia ni proveedor. Los README de core y verticales expresan responsabilidades futuras, sin carpetas vacías de implementación.

Estados en esta entrega: cinco features BLOCKED para implementación; artefactos de investigación y preparación disponibles. Decisiones y responsables en aclaraciones.md; evidencia en matriz-evidencia.md y validacion.md.
