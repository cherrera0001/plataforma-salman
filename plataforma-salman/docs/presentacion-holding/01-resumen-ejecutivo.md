# Resumen Ejecutivo — Evaluación de la Propuesta de Plataforma Salman

**Clasificación:** PROPUESTA DE COMITÉ (evaluación independiente, no requisito ratificado)
**Fecha:** 19-10-2026 · **Audiencia:** dirección del holding Salman
**Extensión:** 3 páginas. El detalle técnico está en `02-presentacion.md` y en el informe completo del comité (fuera de este repo).

---

## 1. El problema en una frase

Hoy el holding opera sus negocios (hotel, cafetería, inmobiliaria, constructora, farmacia) con software desacoplado, y el proyecto actual —aunque bien documentado— reproduce ese desacoplamiento: construiría **cuatro silos nuevos con una pasarela de pagos común**, sin resolver la visión de grupo que motivó el proyecto.

## 2. Qué se evaluó

Un comité independiente de tres perfiles deliberó sobre: (a) el mercado de software de gastronomía y hotelería en LATAM con fuentes y fechas (oct-2026), y (b) el diseño vigente del repositorio (77 FR / 31 SC, 5 features en estado BLOCKED, 6 ADRs y constitución **sin ratificar**, 0 líneas de código).

## 3. El mercado en tres datos (verificables)

| Dato | Fuente | Fecha |
|---|---|---|
| Toast (líder US): 164.000 locales, US$195B procesados en 2025; **sin presencia en LATAM** | Yahoo Finance / earnings Q4-2025 | feb-2026 |
| Competidores directos en Chile: Toteat levantó US$7,4M para IA y expansión; Fudo supera 25.000 clientes | LatamList / Startupeable | sep-2025 / ago-2026 |
| **Ningún player cubre la plataforma multi-vertical de un grupo familiar en LATAM**; ventana estimada 24-48 meses | Verificación directa del comité | oct-2026 |
| Ley 21.719 de protección de datos entra en vigencia plena el **1-dic-2026**, con multas de hasta 4% de ingresos anuales | Anguita Osorio / Prey | 2026 |

## 4. Dictamen del comité: **MODIFICAR** (confianza media-alta)

Ni continuar tal cual (mata la tesis del holding) ni pivotar (la oportunidad existe y no está cubierta). Cinco modificaciones obligatorias:

1. **Cliente transversal por consentimiento:** reemplazar la prohibición absoluta por una capacidad del core *apagada por defecto* y activable con consentimiento del cliente (legal bajo Ley 21.719; hoy la constitución lo prohíbe sin haber evaluado alternativas).
2. **Una vertical primero:** implementar una sola vertical (recomendación: cafetería o hotel) antes de seguir especificando. Así expandieron Toast, Fudo, Cloudbeds y Mews: ninguno especificó 4 verticales antes de implementar una.
3. **Agentes por política, no 0 CLP universal:** tres clases (tareas no monetarias autónomas / compromisos con aprobación humana / operaciones tributarias por regla fija). El líder mundial (Toast) cobra US$699/mes por agentes *con* aprobación humana: la gobernanza es producto, no freno.
4. **Farmacia dentro o fuera, con fecha:** es un negocio real del holding ausente del diseño, y su regulación (receta electrónica nacional, lanzada nov-dic-2025) abre una ventana de ~24-36 meses.
5. **Ratificar constitución y ADRs con fecha límite:** sin eso, todo lo anterior es papel.

## 5. Las 5 decisiones que no pueden esperar

| # | Decisión | Criterio de cierre | Costo de postergar 6 meses |
|---|---|---|---|
| 1 | Ratificar constitución v1.1.0 y los 6 ADRs (o rechazarlos) | Firma con fecha | Ninguna otra decisión es ejecutable |
| 2 | Cliente transversal: consentimiento vs. prohibición | Cláusula de consentimiento validada legalmente | Irreversible en la práctica: unificar identidades después cuesta 10-50x |
| 3 | Elegir stack tecnológico (ADR-003) | Decisión escrita de lenguaje, base de datos y hosting | Bloquea contratación y cualquier línea de código |
| 4 | Vertical #1 y qué pasa con el software actual (Eleventa, ¿hay PMS?) | Preguntas Q-CAF-01 / Q-HOT-03 respondidas con inventario operativo real | Define el producto entero; competidores ganando clientes mientras tanto |
| 5 | Farmacia: dentro o fuera del alcance | Acta firmada; si dentro, hito de integración a 6 meses | La ventana regulatoria no espera |

## 6. Tres verdades incómodas (presentadas como riesgos)

1. **Riesgo de gobernanza:** el activo principal del proyecto aún es una pregunta sin responder — qué software usa hoy cada negocio. Es la pregunta más barata y la más bloqueante.
2. **Riesgo de tesis:** si se implementa el diseño actual tal cual, el holding tendría dentro de 18 meses el mismo problema con software más nuevo.
3. **Riesgo de ventana:** la oportunidad multi-vertical tiene 24-48 meses y corre desde hoy, no desde el día en que se empiece a implementar.

## 7. Criterio de éxito de la sesión de decisión

La sesión (90 min) se considera exitosa solo si al terminar las cinco decisiones tienen estado: **firmada, rechazada con fecha, o diferida con fecha**. Un "lo pensamos" sin fecha equivale a "no" y activa el escenario pesimista del comité.

---

*Elaborado por el comité de revisión independiente (arquitectura multi-tenant, analista de mercado LATAM, evaluador escéptico). Fuentes de mercado citadas con fecha en cada afirmación; los vacíos de información se declaran explícitamente en el informe completo.*
