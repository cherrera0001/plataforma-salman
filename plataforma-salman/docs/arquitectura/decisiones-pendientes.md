# Decisiones Pendientes y Preguntas de Negocio Abiertas

A continuación se consolidan las definiciones críticas que requieren ratificación comercial o de producto antes de levantar el estado `BLOCKED para implementación`:

| Código | Dominio | Asunto | Descripción | Impacto Técnico / Datos |
| :--- | :--- | :--- | :--- | :--- |
| `Q-COMP-01` | Cafetería | Prorrateo de Propinas | Determinar si la propina sugerida (10%) se fracciona automáticamente entre las cuotas de la división de cuenta o si se abona íntegra a la primera cuota. | Define si `monto_propina_clp` reside en `cuentas` o en `pagos_cuenta`. |
| `Q-COMP-02` | Hotel | Tolerancia de Overbooking OTA | Fijar si el Channel Manager permite sobreventa técnica (buffer del 2%) o cupo cero estricto en temporada alta. | Restricción CHECK en `hotel_cupos_diarios`. |
| `Q-COMP-03` | Inmobiliaria | Caducidad de Reservas | Plazo de gracia (en horas) para pago de garantía de reserva antes de que el motor agéntico libere la unidad al inventario público. | Job programado y estado en `inmobiliaria_unidades`. |
| `Q-COMP-04` | Constructora | Sobregiro de Partidas | Regla de autorización cuando una Orden de Compra supera el saldo disponible de una partida presupuestaria (bloqueo duro vs workflow de aprobación de gerencia). | Constraint CHECK o trigger condicional en `ordenes_compra`. |
| `Q-REA-01` | Plataforma | Runtime Dinámico REA | Solicitar aprobación de actualización del entorno Node.js a v22+ para ejecutar dinámicamente el agente REA (`morluto/rea`). | Bloqueado por directriz de congelamiento global. |
