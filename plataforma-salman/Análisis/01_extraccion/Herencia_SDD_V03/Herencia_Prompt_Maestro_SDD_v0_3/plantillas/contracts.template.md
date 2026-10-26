# Contracts: {{FEATURE}}

Por interfaz/evento: ID/versión, proveedor/consumidor, finalidad, autoridad sobre dato, autenticación, permisos, esquema, campos obligatorios, validaciones, errores, idempotencia, orden, reintentos, tiempo de espera, límites, trazabilidad y retención. Incluir ejemplos ficticios y negativos.

Contratos propios pueden expresarse en OpenAPI/JSON Schema/AsyncAPI cuando se apruebe el estilo. Un endpoint propio propuesto no es una API oficial externa. Para terceros documentar URL oficial, capacidad exacta, cuenta/permiso, ambiente y evidencia requerida.

Separar adaptador externo, contrato interno estable y mecanismo de reintento/cola muerta. No depender de consultas directas entre módulos que eludan permisos o reglas.

Definir compatibilidad, deprecacion, consumidor afectado, pruebas de contrato y cambio coordinado. Cada webhook necesita verificación, IDs y protección frente a duplicados. No enviar secretos ni datos de tarjeta en ejemplos.
