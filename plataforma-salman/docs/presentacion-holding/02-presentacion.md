# Presentación de Decisión — Plataforma Salman

**Clasificación:** PROPUESTA DE COMITÉ · **Formato:** 12 láminas, cada diagrama acompañado de su explicación en palabras simples. Los diagramas se renderizan en GitHub (Mermaid).

---

## Lámina 1 — Portada

**Plataforma Salman: de los silos a la plataforma del grupo**
Sesión de decisión · 90 minutos · Paquete de evaluación independiente (oct-2026)

> **En palabras simples:** esta no es una reunión para informar. Es la reunión donde se firman o se rechazan las decisiones que llevan meses pendientes.

---

## Lámina 2 — El problema de hoy

```mermaid
flowchart LR
    subgraph Hoy["Cómo opera el holding hoy"]
        A1["Hotel<br/>reservas por OTA, sin sistema central"]
        A2["Cafetería<br/>caja + planillas"]
        A3["Inmobiliaria<br/>leads en Excel y WhatsApp"]
        A4["Constructora<br/>avance por WhatsApp"]
        A5["Farmacia<br/>fuera de todo sistema del grupo"]
    end
    D1["Ninguna visión de grupo"] 
    A1 & A2 & A3 & A4 & A5 --> D1
```

> **En palabras simples:** cada negocio vive en su isla. Nadie del grupo puede responder "¿cuánto facturamos en conjunto este mes?" sin armar planillas a mano. Ese era el problema que este proyecto debía resolver.

---

## Lámina 3 — Qué existe hoy: mucho documento, cero código

```mermaid
flowchart TD
    S1["77 requisitos funcionales<br/>31 criterios de aceptación"] --> S2["4 verticales especificadas<br/>cafetería · hotel · inmobiliaria · constructora"]
    S2 --> S3["6 decisiones de arquitectura + constitución<br/>PROPUESTAS, sin firma"]
    S3 --> S4["31-37 preguntas de negocio<br/>sin responder"]
    S4 --> S5["Líneas de código: 0<br/>Todo en estado BLOQUEADO"]
    style S5 fill:#ffe0e0
```

> **En palabras simples:** hay un diseño detallado y auditado —como los planos de una casa—, pero nadie ha aprobado los planos y no se ha movido un solo ladrillo. Y hay más de 30 preguntas sobre el negocio que solo el grupo puede responder y siguen abiertas.

---

## Lámina 4 — El mercado en 3 datos

| Dato | Qué significa para el holding |
|---|---|
| Toast: 164.000 locales, US$195B procesados (2025), **sin entrar a LATAM** | El modelo ganador (software + pagos + agentes) no ha llegado; hay tiempo, no mucho |
| Toteat (Chile) levantó US$7,4M (sep-2025); Fudo supera 25.000 clientes | Los locales están creciendo y agregando IA; cada mes de espera es mercado que se asienta |
| **Nadie cubre la plataforma de grupo familiar multi-vertical en LATAM** (verificado oct-2026) | La oportunidad del holding existe y está libre: ventana estimada 24-48 meses |

> **En palabras simples:** los gigantes no han llegado, los locales están acelerando, y el terreno que el holding podría ocupar —ser la plataforma de un grupo de negocios— está vacío. Las ventanas así no se avisan dos veces.

---

## Lámina 5 — La oportunidad: el terreno está libre

```mermaid
flowchart TD
    V["¿Quién da un sistema UNICO<br/>a un grupo con hotel + café + inmuebles + farmacia?"]
    V --> P1["Toast / Square: no, son de un solo rubro<br/>y no están en LATAM"]
    V --> P2["Fudo / Toteat: no, solo restaurantes"]
    V --> P3["Cloudbeds / Mews: no, solo hoteles"]
    V --> P4["Plataforma Salman:<br/>terreno libre (24-48 meses)"]
    style P4 fill:#d0f0d0
```

> **En palabras simples:** cada proveedor fuerte hace una cosa. Ninguno hace "el sistema del grupo". Ese hueco es exactamente lo que el holding necesita para sí mismo — y lo que podría luego vender a otros grupos familiares.

---

## Lámina 6 — El hallazgo central: un candado que nadie decidió poner

```mermaid
flowchart TD
    subgraph OpcionA["Diseño actual (propuesto)"]
        A["Cliente del hotel"] --> A1["Silo hotel"]
        A2["Cliente de la cafetería"] --> A2b["Silo cafetería"]
        A1 -. "jamás se cruzan" .- A2b
    end
    subgraph OpcionB["Lo que propone el comité"]
        B["Persona"] --> B1["Hotel"]
        B --> B2["Cafetería"]
        B --> B3["Inmobiliaria"]
        C["Consentimiento del cliente<br/>(una aceptación al comprar)<br/>apagado por defecto"] -. "activa" .- B
    end
    style OpcionA fill:#ffe0e0
    style OpcionB fill:#d0f0d0
```

> **En palabras simples:** el diseño actual prohíbe que el sistema reconozca al mismo cliente en dos negocios del grupo. La ley chilena nueva (vigente desde dic-2026) **no lo prohíbe**: pide el consentimiento del cliente, como un checkbox. El comité propone guardar esa llave: apagado por defecto, activable por negocio. Si en dos años el dueño pregunta "¿por qué no sabemos quién es nuestro cliente común?", la respuesta no puede ser "un papel sin firmar lo prohibió".

---

## Lámina 7 — Los tres escenarios a 36 meses

```mermaid
flowchart TD
    E{"¿Se firman las decisiones<br/>en los próximos 90 días?"}
    E -- "No" --> R1["PESIMISTA (~40%):<br/>se sigue documentando; Toteat/Fudo ganan;<br/>el grupo compra software suelto; esto queda archivo"]
    E -- "Sí" --> F{"¿La primera vertical<br/>demuestra valor en 6 meses?"}
    F -- "No" --> R2["BASE (~45%):<br/>un producto funcionando en 1-2 locales;<br/>resto congelado; decisión informada después"]
    F -- "Sí" --> R3["OPTIMISTA (~15%):<br/>2 verticales + farmacia (ventana receta electrónica)<br/>+ primer grupo externo como cliente"]
    style R1 fill:#ffe0e0
    style R2 fill:#fff3d0
    style R3 fill:#d0f0d0
```

**Gatillos observables (primeros 90 días):** constitución firmada con fecha · stack elegido · inventario operativo entregado por el grupo · primer commit del núcleo.

> **En palabras simples:** el escenario malo no depende de la tecnología, depende de una firma. Si en 90 días no hay constitución aprobada, ya estamos en el escenario rojo — y se puede saber sin esperar 3 años.

---

## Lámina 8 — Dictamen: MODIFICAR (no seguir tal cual, no abandonar)

| # | Modificación obligatoria | Por qué |
|---|---|---|
| 1 | Cliente transversal **por consentimiento**, apagado por defecto | Mantiene la tesis del holding sin riesgo legal |
| 2 | **Una vertical primero** (cafetería u hotel), las demás congeladas | Así crecieron todos los players que hoy dominan |
| 3 | Agentes **por política**: autónomos en tareas sin dinero, aprobación humana en gastos, regla fija en boletas/facturas | Gobernanza es producto (Toast cobra por ella), no freno |
| 4 | **Farmacia: decisión explícita con fecha** | Su regulación abierta (receta electrónica, nov-2025) da ~24-36 meses de ventana |
| 5 | **Ratificar constitución y 6 ADRs con fecha límite** | Sin firma, todo lo demás es papel |

> **En palabras simples:** el diseño es bueno material, pero tiene una decisión clave al revés, demasiado papel sin ladrillos, y un negocio del grupo (farmacia) que nadie miró. Se corrige, no se tira.

---

## Lámina 9 — Las 5 decisiones de hoy

| # | Decisión | Costo de postergarla 6 meses |
|---|---|---|
| 1 | Ratificar constitución y ADRs | Nada avanza sin esto |
| 2 | Cliente transversal: consentimiento vs prohibición | Unificar identidades después cuesta 10 a 50 veces más |
| 3 | Stack tecnológico (lenguaje, base de datos, hosting) | No se puede contratar ni escribir código |
| 4 | Primera vertical + qué pasa con el software actual | Es la definición del producto; el mercado no espera |
| 5 | Farmacia: dentro o fuera | La ventana regulatoria se cierra sola |

> **En palabras simples:** estas cinco son baratas hoy (son decisiones de una reunión) y caras después (son obras de demolición). Por eso se deciden hoy, una por una: firma, rechazo con fecha, o aplazamiento con fecha.

---

## Lámina 10 — Cómo trabajaría un agente con gobernanza (ejemplo real)

```mermaid
sequenceDiagram
    participant Ag as Agente (software con IA)
    participant Op as Persona a cargo
    participant Sis as Sistemas del negocio
    Note over Ag,Sis: Caso 1: tarea sin dinero (responder reseña, agendar)
    Ag->>Sis: ejecuta directamente
    Note over Ag,Sis: Caso 2: gastar dinero (comprar insumos)
    Ag->>Op: propuesta con monto y proveedor
    Op-->>Ag: aprueba desde el celular
    Ag->>Sis: ejecuta la compra
    Note over Ag,Sis: Caso 3: boleta o factura (obligación con el SII)
    Ag->>Sis: nunca decide: sistema de reglas fijo
```

> **En palabras simples:** el agente es como un encargado con tarjeta limitada. Para tareas sin plata, trabaja solo. Para gastar, pide permiso por teléfono y el permiso sirve una sola vez y por el monto exacto. Para documentos tributarios no decide nada: ahí manda la regla fija, porque un error le cuesta multa al holding. Esto es lo que ya vende Toast en EE.UU. a US$699/mes.

---

## Lámina 11 — Lo que NO se está proponiendo hoy

- ❌ Escribir código mañana (primero se firma el diseño; la fase sigue siendo documental)
- ❌ Compartir datos de clientes sin permiso (la llave del consentimiento está apagada por defecto)
- ❌ Reemplazar de golpe los sistemas actuales (la convivencia con Eleventa y el PMS actual es decisión #4, con datos del grupo)
- ❌ Prometer las 4 verticales (se implementa una; las otras quedan como opciones evaluadas)

> **En palabras simples:** hoy no se gasta dinero de desarrollo. Se cierran decisiones para que el próximo peso invertido vaya en lo correcto.

---

## Lámina 12 — Agenda de la sesión y regla de cierre

```mermaid
flowchart LR
    M0["0-15 min<br/>el problema en una frase"] --> M1["15-35 min<br/>mercado: 3 datos"]
    M1 --> M2["35-85 min<br/>las 5 decisiones,<br/>una por una"]
    M2 --> M3["85-90 min<br/>acta firmada"]
    style M3 fill:#d0f0d0
```

**Regla de cierre:** cada decisión termina en **firmada**, **rechazada con fecha**, o **diferida con fecha**. "Lo pensamos" sin fecha = no, y activa el escenario pesimista.

**Material previo enviado (T-7 días):** resumen ejecutivo + cuestionario de 12 preguntas que solo el grupo puede responder (`03-cuestionario-previo.md`).

---

*Fuentes de mercado con fecha en `01-resumen-ejecutivo.md` y en el informe completo del comité. Lo no verificable se declara como tal.*
