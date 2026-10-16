# Arquitectura C4 — Contexto y Contenedores Multi-tenant

**Concilio Técnico:** Arquitecto de Software · Arquitecto de Datos · Especialista AppSec.  
**Modelo:** C4 Model (Nivel 1: Contexto de Sistema, Nivel 2: Contenedores).

---

## 1. Nivel 1: Diagrama de Contexto de Sistema

```mermaid
flowchart TD
    subgraph Actores ["Actores del Negocio"]
        Comensal["Comensal (Carta QR / POS)"]
        Huesped["Huésped (Web / Concierge)"]
        Comprador["Comprador Inmobiliario"]
        JefeObra["Jefe de Obra / ITO"]
        AdminTenant["Administrador de Empresa / Gerente"]
    end

    subgraph SistemaSalman ["Plataforma Salman (SaaS B2B Multi-tenant)"]
        Plataforma["Plataforma Salman Core & Verticales"]
    end

    subgraph Externos ["Sistemas Externos de Integración"]
        TBK["Pasarelas de Pago (Transbank WebPay / POS)"]
        SII["Servicio de Impuestos Internos (SII DTE)"]
        OTAs["Canales OTA (Booking / Airbnb API)"]
        Firma["Proveedor Firma Electrónica (Ley 19.799)"]
        WhatsApp["WhatsApp Business Cloud API"]
    end

    Comensal -->|Pide y paga parte| Plataforma
    Huesped -->|Reserva y consulta| Plataforma
    Comprador -->|Cotiza y firma promesa| Plataforma
    JefeObra -->|Reporta avance y fallas| Plataforma
    AdminTenant -->|Gobierna y concilia| Plataforma

    Plataforma -->|Autoriza pagos| TBK
    Plataforma -->|Emite boletas y facturas| SII
    Plataforma <-->|Sincroniza cupos y reservas| OTAs
    Plataforma -->|Valida identidad y firma| Firma
    Plataforma <-->|Mensajería conversacional| WhatsApp
```

---

## 2. Nivel 2: Diagrama de Contenedores y Fronteras de Dominio

```mermaid
flowchart TD
    subgraph Clientes ["Clientes y Puntos de Acceso"]
        WebPortal["Web SPA / Portal Clientes (Next.js)"]
        MobileTerreno["PWA Móvil Terreno / Offline (Jefe Obra / Garzón)"]
    end

    subgraph Ingress ["Frontera de Entrada"]
        APIGateway["API Gateway & Reverse Proxy\n(Resolución Tenant, TLS, Rate Limit, Auth)"]
    end

    subgraph Microservicios ["Servicios de Dominio (Backends)"]
        CoreSvc["Core Platform Service\n(Identidad, Tenancy, Pagos, Auditoría)"]
        CafeteriaSvc["Cafetería & POS Service\n(Mesas, Split Cuentas, KDS, Stock)"]
        HotelSvc["Hotel & Reservas Service\n(Inventario Cupos, PMS, Concierge)"]
        InmobiliariaSvc["Inmobiliaria Commercial Service\n(CRM, Cotizaciones, Promesas)"]
        ConstructoraSvc["Constructora Obra Service\n(Partidas, Avance, Punch List, Compras)"]
        AgenteSidecar["Agente IA Orchestrator (Sidecar)\n(Solo lectura y borradores, Límite 0 CLP)"]
    end

    subgraph Mensajeria ["Capa de Eventos Asíncronos"]
        EventBroker["Message Broker (Eventos de Dominio y Webhooks)"]
    end

    subgraph Persistencia ["Almacenamiento y Persistencia"]
        PostgresDB[("PostgreSQL 16+\n(RLS Habilitado por Tenant\nEsquemas: core, cafeteria, hotel, inm, constr)")]
        ObjectStore[("Object Storage (S3 Compatible)\n(DTEs firmados, PDFs Promesas, Fotos Obra)")]
    end

    Clientes --> APIGateway
    APIGateway --> CoreSvc
    APIGateway --> CafeteriaSvc
    APIGateway --> HotelSvc
    APIGateway --> InmobiliariaSvc
    APIGateway --> ConstructoraSvc

    CafeteriaSvc -.->|Contrato Pago| CoreSvc
    HotelSvc -.->|Contrato Pago / DTE| CoreSvc
    InmobiliariaSvc -.->|Contrato Pago / Auditoría| CoreSvc
    ConstructoraSvc -.->|Auditoría / Aprobaciones| CoreSvc

    HotelSvc -.->|Consulta Menú / Cargo Opcional| CafeteriaSvc
    ConstructoraSvc -.->|Vínculo Proyecto Opcional| InmobiliariaSvc

    AgenteSidecar -->|Propone Borrador con Huella| CoreSvc

    CoreSvc --> EventBroker
    HotelSvc --> EventBroker
    InmobiliariaSvc --> EventBroker
    ConstructoraSvc --> EventBroker

    CoreSvc --> PostgresDB
    CafeteriaSvc --> PostgresDB
    HotelSvc --> PostgresDB
    InmobiliariaSvc --> PostgresDB
    ConstructoraSvc --> PostgresDB

    CoreSvc --> ObjectStore
    InmobiliariaSvc --> ObjectStore
    ConstructoraSvc --> ObjectStore
```

### Aislamiento y Fronteras Clave
1. **Frontera de Ingress:** El `APIGateway` valida el token JWT del usuario, extrae los tenants permitidos y establece el encabezado inmutable `X-Tenant-ID`.
2. **Contexto de Base de Datos:** Todo servicio establece `SET LOCAL app.current_tenant_id = :tenant_id` al tomar una conexión del pool, activando automáticamente las políticas RLS a nivel de motor PostgreSQL.
3. **Frontera Agéntica:** El contenedor `AgenteSidecar` se ejecuta en una red interna aislada sin acceso de escritura a la base de datos ni a los adaptadores de pago. Sus propuestas se envían como eventos firmados que requieren aprobación humana previa a cualquier mutación de estado.
