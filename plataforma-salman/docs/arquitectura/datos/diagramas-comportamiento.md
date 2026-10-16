# Diagramas de Comportamiento Dinámico — Máquinas de Estado y Secuencia

**Concilio Técnico:** Arquitecto de Software · Especialista en Modelado de Dominios · QA · Especialista en IA Agéntica.  
**Sintaxis:** Mermaid `stateDiagram-v2` y `sequenceDiagram`.

---

## 1. Máquinas de Estado por Dominio

### A. Cafetería: Ciclo de Vida de Pedido, Cuenta y División (Split)
```mermaid
stateDiagram-v2
    [*] --> BORRADOR_PEDIDO : Cliente escanea QR o Garzón abre orden
    BORRADOR_PEDIDO --> ENVIADO_COCINA : Confirmar comanda
    BORRADOR_PEDIDO --> ANULADO : Descarte antes de comanda
    
    ENVIADO_COCINA --> EN_PREPARACION : Recepción en KDS
    EN_PREPARACION --> SERVIDO : Entrega en mesa
    
    state "Gestión Financiera de Cuenta (AsignacionCuenta)" as Cuenta {
        [*] --> ABIERTA : Apertura de mesa
        ABIERTA --> EN_PAGO_DIVIDIDA : Solicitar cuenta / Dividir
        EN_PAGO_DIVIDIDA --> EN_PAGO_DIVIDIDA : Pago parcial de comensal
        EN_PAGO_DIVIDIDA --> LIQUIDADA : Saldo pendiente = 0 CLP
        LIQUIDADA --> CERRADA : Emisión DTE y liberación de mesa
    }

    state "Estado de Parte individual (ParteSaldo)" as Parte {
        [*] --> PENDIENTE_PAGO : Generar porción (items o igualitaria)
        PENDIENTE_PAGO --> PAGADA_CONCILIADA : Pago exitoso comprobado
        PENDIENTE_PAGO --> ANULADA : Reorganización antes de pagar
    }
```
*Invariante:* Si una `ParteSaldo` pasa a `PAGADA_CONCILIADA`, no puede ser revertida a `PENDIENTE_PAGO` ni cancelada por una reorganización posterior de la mesa. El estado de cocina (`SERVIDO`) es totalmente ajeno a las divisiones financieras.

---

### B. Hotel: Reserva, Asignación de Habitación y Estadía
```mermaid
stateDiagram-v2
    [*] --> PROPUESTA : Cotización de fechas y categoría
    PROPUESTA --> RETENIDA_TEMPORAL : Retención de cupo (15 min)
    PROPUESTA --> EXPIRADA : Sin pago / Timeout
    RETENIDA_TEMPORAL --> EXPIRADA : Caduca ventana de retención
    RETENIDA_TEMPORAL --> CONFIRMADA : Pago de garantía recibido

    CONFIRMADA --> CHECKED_IN : Huésped llega (habitación lista)
    CONFIRMADA --> CANCELADA : Cancelación autorizada
    
    CHECKED_IN --> CHECKED_OUT : Liquidación de folio y salida
    
    state "Habitación Física" as Habitacion {
        [*] --> LIMPIA : Limpieza e inspección lista
        LIMPIA --> OCUPADA : Check-in asociado
        OCUPADA --> SUCIA : Check-out realizado
        SUCIA --> EN_LIMPIEZA : Personal inicia aseo
        EN_LIMPIEZA --> LIMPIA : Aseo completado
        LIMPIA --> BLOQUEADA_MANTENIMIENTO : Daño técnico reportado
        BLOQUEADA_MANTENIMIENTO --> SUCIA : Reparación terminada
    }
```
*Invariante:* El check-in está estrictamente denegado si la habitación física asignada se encuentra en `BLOQUEADA_MANTENIMIENTO` o `SUCIA`.

---

### C. Inmobiliaria: Progresión de Unidad, Cotización y Promesa
```mermaid
stateDiagram-v2
    state "Unidad Inmobiliaria" as Unidad {
        [*] --> DISPONIBLE : Lanzamiento de proyecto
        DISPONIBLE --> COTIZADA : Emisión de cotización
        COTIZADA --> DISPONIBLE : Vencimiento de cotización
        COTIZADA --> RESERVADA : Abono de reserva pagado
        DISPONIBLE --> RESERVADA : Reserva directa en sala
        RESERVADA --> PROMESADA : Promesa firmada por todas las partes
        RESERVADA --> DISPONIBLE : Desistimiento / Devolución
        PROMESADA --> ESCRITURADA : Firma de escritura en Notaría
        PROMESADA --> DISPONIBLE : Resciliación contractual
    }

    state "Promesa de Compraventa" as Promesa {
        [*] --> BORRADOR_LEGAL : Generación desde reserva
        BORRADOR_LEGAL --> EN_REVISION_LEGAL : Validación de cláusulas
        EN_REVISION_LEGAL --> ENVIADA_FIRMA : Aprobación de texto
        ENVIADA_FIRMA --> FIRMADA_PARCIAL : Firma Comprador
        FIRMADA_PARCIAL --> FIRMADA_COMPLETA : Firma Representante Inmobiliaria
        ENVIADA_FIRMA --> RESCILIADA : Expiración de plazo legal
    }
```
*Invariante:* `FIRMADA_PARCIAL` no autoriza el paso de la unidad a `PROMESADA`. Requiere obligatoriamente `FIRMADA_COMPLETA` con evidencias biométricas/OTP auditadas.

---

### D. Constructora: Avance, Observación y Abastecimiento
```mermaid
stateDiagram-v2
    state "Reporte Diario de Avance" as Reporte {
        [*] --> BORRADOR : Captura en terreno
        BORRADOR --> EXTRAIDO_IA : Transcripción de voz/foto
        EXTRAIDO_IA --> EN_REVISION : Revisión jefe de obra
        EN_REVISION --> APROBADO_ITO : Validación fiscalizador
        EN_REVISION --> RECHAZADO : Inconsistencia técnica
    }

    state "Observación de Calidad (Punch List)" as Observacion {
        [*] --> ABIERTA : Detección en inspección
        ABIERTA --> ASIGNADA : Asignación a contratista
        ASIGNADA --> SOLUCION_PROPUESTA : Contratista repara y sube foto
        SOLUCION_PROPUESTA --> CERRADA_ACEPTADA : ITO aprueba reparación
        SOLUCION_PROPUESTA --> REABIERTA : ITO rechaza calidad de trabajo
        REABIERTA --> ASIGNADA : Reasignación
    }

    state "Cadena de Materiales" as Material {
        [*] --> SOLICITUD_BORRADOR : Cubicador requiere insumo
        SOLICITUD_BORRADOR --> ORDEN_COMPRA_EMITIDA : Aprobación presupuestaria
        ORDEN_COMPRA_EMITIDA --> RECEPCION_PARCIAL : Entrega de camión 1
        RECEPCION_PARCIAL --> RECEPCION_TOTAL : Saldo completado
        RECEPCION_PARCIAL --> DISCREPANCIA_REGISTRADA : Material dañado/rechazado
    }
```
*Invariante:* `SOLUCION_PROPUESTA` jamás cierra la observación. El cierre exige la firma digital de un usuario con rol ITO distinto al solucionador.

---

### E. Core: Máquina de Estados de Pagos y Conciliación
```mermaid
stateDiagram-v2
    [*] --> INICIADO : Petición de cobro
    INICIADO --> ENVIADO : Despacho a pasarela externa
    ENVIADO --> AUTORIZADO : Webhook de éxito recibido
    ENVIADO --> RECHAZADO : Fondos insuficientes / Denegado
    ENVIADO --> DESCONOCIDO : Timeout de red / Caída externa
    
    DESCONOCIDO --> DESCONOCIDO : Reintento de consulta de estado
    DESCONOCIDO --> CONCILIADO : Confirmación diferida por operador
    DESCONOCIDO --> EN_DISPUTA : Doble cargo o reporte de contracargo
    AUTORIZADO --> REVERSADO : Devolución formal autorizada
```
*Invariante:* Si el estado es `DESCONOCIDO`, la reserva del bien o servicio se mantiene en suspenso y está estrictamente prohibido disparar un nuevo cargo financiero automático al usuario sin consultar previamente al proveedor.

---

### F. Core: Gobernanza de Acciones Agénticas
```mermaid
stateDiagram-v2
    [*] --> PROPUESTA_AGENTE : Modelo sugiere acción
    PROPUESTA_AGENTE --> RECHAZO_AUTOMATICO : Falta política o permisos
    PROPUESTA_AGENTE --> EN_APROBACION_HUMANA : Acción sensible o monto mayor a 0 CLP
    
    EN_APROBACION_HUMANA --> RECHAZADA_HUMANO : Operador deniega
    EN_APROBACION_HUMANA --> EXPIRADA : Vence ventana de aprobación
    EN_APROBACION_HUMANA --> APROBADA_HUMANO : Operador firma autorización
    
    APROBADA_HUMANO --> EJECUTADA_DETERMINISTA : Servicio transaccional ejecuta
    EJECUTADA_DETERMINISTA --> FALLO_OPERACIONAL : Error en backend
    FALLO_OPERACIONAL --> COMPENSADA_REVERTIDA : Transacción de compensación
```
*Invariante:* Toda acción con impacto monetario, contractual o tributario pasa obligatoriamente por `EN_APROBACION_HUMANA`. El agente de IA carece de credenciales directas a la base de datos o pasarelas.

---

## 2. Diagramas de Secuencia para Flujos P1 Críticos

### Flujo P1 Cafetería: División de Cuenta y Cobro con Terminal sin Afectar Cocina
```mermaid
sequenceDiagram
    autonumber
    actor C as Comensal / Garzón
    participant POS as Servicio POS Cafetería
    participant Core as Core Transaccional
    participant TBK as Terminal Transbank / Pasarela
    participant KDS as Pantalla Cocina (KDS)

    C->>POS: Solicitar división de mesa (3 partes iguales)
    POS->>POS: Validar saldo pendiente (10.000 CLP)
    POS->>POS: Calcular cuotas: 3.334, 3.333, 3.333 CLP (Residuo 1 CLP explícito)
    POS-->>C: Presentar desglose con residuo de redondeo ratificado
    
    Note over POS,KDS: No se envía ningún mensaje a cocina (KDS permanece intacto)

    C->>POS: Comensal 1 paga su parte (3.334 CLP)
    POS->>Core: Iniciar IntentoPago (Idempotency-Key: pos-split-101-p1)
    Core->>TBK: Solicitar cobro en terminal POS
    alt Pago Autorizado
        TBK-->>Core: Código Autorización: 123456 (HTTP 200)
        Core->>Core: Registrar IntentoPago = AUTORIZADO
        Core-->>POS: Pago Confirmado
        POS->>POS: Marcar Parte 1 = PAGADA_CONCILIADA
        POS->>POS: Actualizar AsignacionCuenta (Saldo Pendiente: 6.666 CLP)
        POS-->>C: Comprobante emitido. Mesa continúa ABIERTA.
    else Timeout de Comunicación
        TBK--xCore: Sin respuesta (Socket Timeout)
        Core->>Core: Marcar IntentoPago = DESCONOCIDO
        Core->>TBK: Consulta de estado por correlation_id
        TBK-->>Core: Transacción no encontrada
        Core->>Core: Marcar IntentoPago = RECHAZADO
        Core-->>POS: Cobro fallido / Reintentable
        POS-->>C: Terminal no respondió. Saldo se mantiene pendiente.
    end
```

---

### Flujo P1 Hotel: Reserva Directa con Retención Temporal y Concurrencia
```mermaid
sequenceDiagram
    autonumber
    actor H as Huésped en Web
    participant Moto as Motor Reservas Hotel
    participant Cupo as Servicio Inventario Cupos
    participant Core as Core Pagos
    participant Pasarela as WebPay Plus

    H->>Moto: Cotizar Habitación Suite (01/11 al 05/11)
    Moto->>Cupo: Verificar y Retener Cupo (Bloqueo Pesimista)
    Cupo->>Cupo: BEGIN TX; SELECT FOR UPDATE cupo_disponible
    alt Cupo Disponible >= 1
        Cupo->>Cupo: Incrementar cupo_retenido_ofertas (+1)
        Cupo->>Cupo: COMMIT TX (Expiración: 15 minutos)
        Cupo-->>Moto: Cupo Retenido (Token: ret-9988)
        Moto-->>H: Oferta confirmada. Proceda al pago en 15 min.
        
        H->>Moto: Confirmar reserva y pagar garantía
        Moto->>Core: Iniciar IntentoPago (Monto: 150.000 CLP)
        Core->>Pasarela: Redirigir a WebPay
        Pasarela-->>Core: Transacción Aprobada (Token retorno)
        Core->>Core: IntentoPago = AUTORIZADO
        Core-->>Moto: Pago verificado
        
        Moto->>Cupo: Consolidar Reserva
        Cupo->>Cupo: Decrementar cupo_retenido (-1), Incrementar cupo_reservado (+1)
        Moto->>Moto: Reserva = CONFIRMADA (Habitación física aún NO asignada)
        Moto-->>H: Voucher emitido con código de reserva único.
    else Sin Cupo (Carrera de concurrencia)
        Cupo->>Cupo: ROLLBACK TX
        Cupo-->>Moto: Cupo Agotado
        Moto-->>H: HTTP 409 Conflict: Habitación ya no está disponible.
    end
```

---

### Flujo P1 Inmobiliaria: Cotización Versionada a Promesa con Firma Electrónica
```mermaid
sequenceDiagram
    autonumber
    actor Comprador as Cliente Comprador
    participant CRM as CRM Inmobiliario
    participant Core as Core Pagos
    participant Firma as Proveedor Firma Digital (Ley 19.799)
    actor RepLegal as Representante Inmobiliaria

    Comprador->>CRM: Aceptar Cotización vigente (Precio: 3.500 UF)
    CRM->>CRM: Bloquear cotización a estado = RESERVADA
    CRM->>Core: Cobro abono de reserva (500.000 CLP)
    Core-->>CRM: Abono confirmado
    CRM->>CRM: Unidad = RESERVADA (Bloqueada para otros prospectos)
    
    CRM->>CRM: Generar Borrador Promesa (Plantilla legal hash inmutable)
    CRM->>Firma: Enviar documento a firma del Comprador
    Comprador->>Firma: Validación biométrica / Clave Única y firma
    Firma-->>CRM: Webhook: Firma Comprador registrada
    CRM->>CRM: Promesa = FIRMADA_PARCIAL
    
    Note over CRM,RepLegal: Aprobación y firma del representante legal requerida
    CRM->>RepLegal: Notificar para firma de cierre
    RepLegal->>Firma: Firma con Token Avanzado
    Firma-->>CRM: Webhook: Documento completado con estampillado de tiempo
    CRM->>CRM: Promesa = FIRMADA_COMPLETA
    CRM->>CRM: Unidad = PROMESADA
    CRM-->>Comprador: Copia autorizada de promesa entregada digitalmente.
```

---

### Flujo P1 Constructora: Captura de Avance Diario y Recepción Parcial de Materiales
```mermaid
sequenceDiagram
    autonumber
    actor Jefe as Jefe de Obra / Bodega
    participant Obra as Sistema Control de Obra
    participant Bodega as Gestión de Almacén
    actor ITO as Inspector Técnico (ITO)

    Note over Jefe,Obra: Captura de Parte Diario por Turno
    Jefe->>Obra: Enviar audio de reporte avance ("Hormigonado muro eje A, 15 m3")
    Obra->>Obra: Extracción asistida a borrador de parte (Turno: Mañana)
    Obra-->>Jefe: Presentar borrador con partida sugerida y 15 m3
    Jefe->>Obra: Confirmar y solicitar aprobación
    Obra->>ITO: Notificar para revisión de avance
    ITO->>Obra: Inspección en terreno y Aprobación ITO
    Obra->>Obra: ValorAvance = APROBADO_ITO (Porcentaje de partida actualizado)

    Note over Bodega,Obra: Recepción Parcial de Materiales
    Bodega->>Obra: Registrar ingreso de Guía de Despacho (10 toneladas de acero pedidas)
    Bodega->>Obra: Reportar recepción física: 6 aceptadas, 1 rechazada por daño, 3 pendientes
    Obra->>Obra: Incrementar Stock Disponible = +6 toneladas
    Obra->>Obra: Registrar Discrepancia = 1 tonelada dañada (fotos adjuntas)
    Obra->>Obra: OrdenCompra = RECEPCION_PARCIAL (3 toneladas pendientes)
    Note over Obra: El avance físico NO cambia con la llegada de material a bodega.
```
