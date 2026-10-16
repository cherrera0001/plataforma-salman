# Cobertura de investigación — inmobiliaria

L1 documental y reconstrucción funcional; **sin runtime observado**. Cada área distingue evidencia suficiente para proponer conducta de integración o decisión todavía no validada. La profundidad no es uniforme por plataforma.

| Área solicitada | Evidencia | Nivel real / conclusión acotada | Historia y requisitos propios | Límite/bloqueo |
|---|---|---|---|---|
| Captación y CRM | I01/I02/I04/I05/I11/I17 | API/manual y producto; identidad/contacto/consulta separados | H1; FR-001,003,019 | API Tokko de inicio es placeholder; no prueba operación de leads |
| Calificación agéntica | I14/I09/I06/I07/I08 | Oferta local explícita y ayudas de plataformas agénticas | H1; FR-002,015,016 | No inferir autonomía transaccional, exactitud ni solvencia desde score |
| Visitas y agenda | I12 | Manual de modo estático sin calendario y límites de cambio | H1; FR-002,017 | Proveedor/calendario/horarios y reprogramación pendientes |
| Stock/unidades/cotización | I01/I04/I14; I19 | Producto/API; UF solo definición oficial indexada | H1; FR-003,004,015 | Precio/unidad/tasa y vigencia deben ratificarse; sin valor UF actual recuperado |
| Reserva y pagos | I03/I15; 000 | Ayuda y oferta histórica, no validación de política contractual | H1; FR-005,015 | Expiración/reembolso/transferencia y fiscalidad siguen abiertas |
| Firma electrónica y promesa | I15/I18 | Oferta histórica y evidencia legal incompleta; diseño propio de versión/firmantes | H1; FR-006,018 | Formalidades y proveedor deben aprobarse con abogado; no validez universal |
| Cobranza y portal | I16 | Producto/FAQ con cuentas/documentos y vínculo de propietario | H2; FR-007,009,020 | Pago no se ejecutó; derechos históricos y aviso de deuda por política |
| Postventa y visitas técnicas | I13/I16 | Producto/FAQ; etapas propias de solicitud/visita/solución/aceptación | H2; FR-008,016 | Garantía, plazos y aprobadores no delegados a IA |
| WhatsApp y seguimiento | I14/I06/I09; 000/FR-012 | Oferta WhatsApp y control explícito de efectos; no API Meta validada | H1/H2; FR-016,019 | Permiso/canal/plantillas/tarifas actuales no confirmados |
| Mercado Chile y colaboración brokers | I14 y sitio PlanOK Chile | Existe declaración comercial local de IA; no exclusividad propia | research; oportunidad construir/adaptar | Colaboración externa no habilita compartir tenant ni se agrega marketplace de brokers |
