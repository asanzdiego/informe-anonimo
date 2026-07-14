# INFORME DE VALORACIÓN TÉCNICA INDIVIDUAL

- **Contrato:** Desarrollo evolutivo y correctivo de las Aulas Virtuales, la Mediateca, las webs de centro, el correo web, EMPieza y otras aplicaciones de EducaMadrid (BAC07_2026)
- **Licitador:** empresa_s

## RESUMEN EJECUTIVO

### Objeto del informe

El presente informe tiene por objeto realizar la **valoración técnica de la propuesta presentada por empresa_s** en el procedimiento basado en el **Sistema Dinámico de Adquisición SDA 26/2021**, relativo a los servicios de **Desarrollo evolutivo y correctivo de las Aulas Virtuales, la Mediateca, las webs de centro, el correo web, EMPieza y otras aplicaciones de EducaMadrid (BAC07_2026)**.

El informe determina la puntuación correspondiente a los criterios sujetos a juicio de valor, comprueba el cumplimiento del **umbral mínimo de 15 puntos sobre 30** y formula la propuesta de continuación o exclusión que procede para la oferta.

### Metodología de valoración

La evaluación se ha estructurado en dos niveles complementarios. En primer lugar, se ha realizado un análisis técnico detallado de los proyectos y subproyectos incluidos en el Anexo II del Documento de Invitación, examinando el grado de desarrollo, adecuación y verificabilidad de las soluciones propuestas. En segundo lugar, los resultados de dicho análisis se han trasladado al esquema de valoración previsto en el apartado 7.2 del Documento de Invitación, asignando las puntuaciones correspondientes en función del nivel real de adecuación observado.

Este enfoque garantiza la trazabilidad entre **los requisitos definidos, las evidencias contenidas en la memoria, el análisis técnico efectuado y la puntuación final asignada**.

### Síntesis técnica de la propuesta

La propuesta desarrolla de forma completa y mayoritariamente individualizada los proyectos del Anexo II. Define arquitecturas modulares, integraciones mediante APIs y servicios, procesos de despliegue y validación, seguridad desde el diseño, monitorización, pruebas y mecanismos de continuidad. Incluye numerosas mejoras concretas y verificables. La planificación es detallada y coherente, aunque algunos aspectos de dimensionamiento, gestión iterativa y análisis de riesgos podrían concretarse más.

### Principales conclusiones del análisis

La cobertura es completa y homogénea en TRA, AV, MED, COR, CLO, WPM, VID, servicios unitarios y sistemas complementarios. Las soluciones se adaptan al entorno EducaMadrid y mantienen criterios comunes de seguridad, integración y operación. WEK constituye la principal excepción: recibe un tratamiento agregado y menos individualizado, aunque incorpora una mejora global basada en despliegue reproducible, copia de seguridad y rollback.

### Resultado de la valoración

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                  13,60 |
| Planificación del servicio |                 15,00 |                  13,10 |
| **TOTAL** |             **30,00** |              **26,70** |

### Conclusión del resumen ejecutivo

La calidad global es alta y plenamente evaluable. La oferta obtiene 26,70 puntos sobre 30, supera el umbral mínimo de 15 puntos y procede proponer su continuación en el procedimiento.

## INTRODUCCIÓN

### Alcance del informe

El presente informe evalúa la memoria técnica presentada por **empresa_s** para la prestación de los servicios de **DESARROLLO EVOLUTIVO Y CORRECTIVO DE LAS AULAS VIRTUALES, LA MEDIATECA, LAS WEBS DE CENTRO, EL CORREO WEB, EMPIEZA Y OTRAS APLICACIONES DE EDUCAMADRID (BAC07_2026)**. El análisis comprende tanto la **solución técnica ofertada** como la **planificación del servicio**, de acuerdo con los criterios sujetos a juicio de valor establecidos en el apartado 7.2 del Documento de Invitación.

La evaluación toma como referencia los proyectos, subproyectos, actuaciones y entregables definidos en el Anexo II, y atiende exclusivamente al contenido efectivamente desarrollado en la documentación presentada.

### Marco normativo

El presente informe se elabora en el marco del procedimiento de adjudicación correspondiente a **Sistema Dinámico de Adquisición SDA 26/2021**. El procedimiento se rige por lo dispuesto en la **Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público** (en adelante, LCSP), por el Pliego de Cláusulas Administrativas Particulares y por las condiciones específicas establecidas en el Documento de Invitación y demás documentación reguladora del expediente.

La valoración técnica se fundamenta en los **criterios de adjudicación sujetos a juicio de valor definidos en el apartado 7.2 del Documento de Invitación**, cuya finalidad es evaluar la calidad de la propuesta desde una perspectiva integral que contemple tanto la **adecuación de la solución técnica ofertada** como la **viabilidad organizativa y temporal de su ejecución**.

De conformidad con el **artículo 145 de la LCSP**, los criterios de adjudicación deben permitir determinar la mejor relación calidad-precio y aplicarse de forma objetiva, transparente y no discriminatoria. La evaluación se realiza, por tanto, con arreglo a los principios de **igualdad de trato, objetividad, transparencia, proporcionalidad y trazabilidad**, aplicando a todas las ofertas un mismo marco metodológico y sin incorporar elementos externos a la documentación presentada por los licitadores.

Asimismo, el **artículo 146.3 de la LCSP** permite establecer umbrales mínimos en los criterios cualitativos sujetos a juicio de valor. Conforme al Documento de Invitación, las ofertas deben alcanzar un **nivel mínimo de calidad técnica equivalente al cincuenta por ciento de la puntuación máxima asignable a estos criterios** para continuar en el procedimiento.

La aplicación de este umbral no constituye una decisión discrecional: una vez constatado su incumplimiento, la oferta afectada no puede continuar en las fases posteriores del procedimiento. La valoración debe permitir **comprobar de forma clara la puntuación obtenida y motivar la correspondiente propuesta de admisión o exclusión**.

La evaluación se ajusta igualmente al **principio de evaluabilidad**, conforme al cual únicamente pueden valorarse los elementos de la oferta que estén suficientemente desarrollados y que permitan su comprobación objetiva. Las declaraciones genéricas, las capacidades presumidas, las referencias no desarrolladas o las soluciones futuras no descritas en la memoria no pueden suplirse mediante inferencias del órgano evaluador.

### Contexto técnico del servicio

El Anexo II define un conjunto amplio y heterogéneo de actuaciones sobre el ecosistema EducaMadrid. Se trata de un entorno de elevada complejidad técnica y operativa, caracterizado por:

- la coexistencia de múltiples plataformas y tecnologías heterogéneas;

- la existencia de dependencias funcionales y flujos de datos entre sistemas;

- la necesidad de garantizar la disponibilidad y continuidad de servicios críticos;

- la integración de nuevas funcionalidades sin comprometer la estabilidad del entorno existente;

- la atención a requisitos de rendimiento, seguridad, escalabilidad, mantenibilidad y protección de datos;

- y la ejecución coordinada de numerosos proyectos y entregables.

Este contexto exige que las propuestas no se limiten a enumerar actuaciones o reproducir los requisitos, sino que definan soluciones concretas, coherentes, técnicamente viables y adaptadas al entorno real, de forma que pueda verificarse su ejecución en condiciones operativas.

### Naturaleza de la valoración

La valoración de los criterios sometidos a juicio de valor requiere un **análisis técnico cualitativo** que determine el grado de adecuación, desarrollo, madurez y calidad de la solución propuesta. No se limita a una comprobación binaria del cumplimiento, sino que examina, entre otros aspectos:

- la coherencia de las arquitecturas propuestas;

- la comprensión del entorno tecnológico y de los requisitos;

- la viabilidad de las soluciones planteadas;

- la adecuación de la metodología de trabajo;

- el rendimiento previsible;

- el grado de satisfacción de los requisitos;

- la capacidad de ejecución y la profundidad de la planificación;

- la concreción, verificabilidad y eventual valor añadido de la propuesta.

La discrecionalidad técnica propia de esta evaluación no implica arbitrariedad. Las conclusiones deben basarse en los criterios previamente establecidos, estar suficientemente motivadas, mantener coherencia con la documentación analizada y poder reconstruirse a partir de evidencias concretas contenidas en la memoria técnica.

### Principios rectores de la valoración

#### Igualdad de trato

Todas las ofertas se analizan mediante **los mismos criterios, el mismo nivel de exigencia y las mismas reglas de puntuación**, sin introducir requisitos adicionales ni emplear estándares distintos para cada licitador. Fortalezas y debilidades equivalentes deben recibir una ponderación equivalente.

#### Objetividad y evaluabilidad

Las puntuaciones se fundamentan exclusivamente en **evidencias identificables en la documentación presentada**, como arquitecturas, procedimientos, metodologías, herramientas, mecanismos de validación, cronogramas e indicadores efectivamente descritos. No se valoran expectativas, capacidades presumidas ni contenidos ajenos a las ofertas.

#### Proporcionalidad

Las fortalezas y debilidades se ponderan según su **relevancia real para la ejecución del servicio**. Una carencia menor no recibe el mismo peso que una deficiencia estructural que comprometa la viabilidad, y una mejora puntual no compensa automáticamente limitaciones significativas del conjunto de la propuesta.

#### Trazabilidad

Cada valoración debe poder **vincularse con los requisitos del pliego, las evidencias concretas de la memoria técnica y la puntuación asignada**. Esta correspondencia garantiza la transparencia, la motivación de las conclusiones y la posibilidad de revisar posteriormente el proceso de evaluación.

#### Coherencia

La puntuación cuantitativa y el nivel cualitativo asignados deben reflejar de forma equilibrada las fortalezas y debilidades identificadas. **Las conclusiones individuales, su integración en la valoración comparativa y la propuesta final deben ser consistentes entre sí**.

### Umbral mínimo

El Documento de Invitación establece una **puntuación máxima de 30 puntos** para los criterios sujetos a juicio de valor y exige alcanzar, como mínimo, el **50 % de dicha puntuación** para continuar en el procedimiento de adjudicación.

En consecuencia:

- la puntuación mínima exigida es de **15 puntos sobre 30**;

- las ofertas que alcancen o superen dicho umbral podrán continuar en el procedimiento;

- las ofertas que no alcancen el umbral deberán ser excluidas por aplicación directa de la documentación reguladora del procedimiento.

## METODOLOGÍA DE VALORACIÓN

La valoración se realiza conforme al apartado 7.2 del Documento de Invitación mediante un **modelo de análisis estructurado, homogéneo y trazable**. La evaluación atiende exclusivamente al contenido efectivamente desarrollado en la memoria y combina dos marcos complementarios:

- los criterios cualitativos y niveles de cumplimiento definidos en el Documento de Invitación;

- los requisitos funcionales y técnicos incluidos en el Anexo II del Documento de Invitación, que determinan el alcance material del servicio.

La calidad de una respuesta no se determina por la mera existencia formal de una referencia a cada requisito, sino por el **grado de desarrollo, madurez, adecuación, viabilidad y verificabilidad** con que se presenta la solución.

### Estructura general de la valoración

El modelo se articula en **dos bloques de 15 puntos cada uno**: la solución técnica ofertada y la planificación del servicio. Ambos configuran conjuntamente los 30 puntos asignados a los criterios sujetos a juicio de valor.

- **Solución técnica ofertada — 15 puntos**
  - Arquitectura.
  - Comprensión de los requisitos.
  - Viabilidad.
  - Metodología.
  - Rendimiento previsible.
  - Satisfacción de los requisitos.

- **Planificación del servicio — 15 puntos**
  - Calendario.
  - Análisis de riesgos.
  - Plan de contingencias.
  - Plan de calidad.
  - Trazabilidad del servicio.

Los dos bloques se evalúan de forma diferenciada, aunque mantienen una relación directa: una solución técnicamente correcta debe acompañarse de una planificación que permita ejecutarla en condiciones reales, y una buena planificación no subsana las deficiencias que comprometan la calidad o viabilidad de la solución.

### Valoración de la solución técnica ofertada

Este bloque evalúa la calidad técnica real de la propuesta, su adecuación al contexto del contrato y el nivel de satisfacción o mejora de los requisitos. Se distribuye en los siguientes subcriterios:

- Arquitectura planteada en los distintos subproyectos (**2 puntos**),

- Grado de comprensión de los requisitos planteados (**2 puntos**),

- Viabilidad del proyecto en general (**1 punto**),

- Metodología de trabajo aplicada (**1 punto**),

- Rendimiento previsible de las distintas soluciones (**1 punto**),

- Satisfacción de los requisitos (**8 puntos**).

La evaluación debe realizarse para cada proyecto o subproyecto del Anexo II del Documento de Invitación distinguiendo entre una **descripción genérica de objetivos** y una **solución técnica efectivamente definida**. Las propuestas de mejora solo se considerarán positivamente cuando aporten una ventaja técnica u operativa objetiva, sean coherentes con el objeto del contrato y estén suficientemente desarrolladas.

Cada uno de estos subcriterios se evaluará siguiendo el siguiente árbol de puntuación:

- **EXCELENTE**: La solución técnica aportada describe de forma excelente y completa la arquitectura de los distintos subproyectos. La comprensión de los requisitos planteados es excelente. La viabilidad del proyecto no genera ningún atisbo de dudas. La metodología de trabajo elegida es comúnmente utilizada dentro del ámbito tecnológico y concuerda con las tareas del proyecto. Se justifica de forma convincente un excelente rendimiento de las distintas soluciones aportadas. La solución técnica cumple ampliamente los requisitos del pliego aportando mejoras coherentes y sustanciales de los mismos.

- **ALTA**: La solución técnica aportada describe de forma correcta y completa la arquitectura de los distintos subproyectos. La comprensión de los requisitos planteados es buena. La viabilidad del proyecto no genera dudas. La metodología de trabajo elegida es utilizada dentro del ámbito tecnológico y concuerda con las tareas del proyecto. Se justifica de forma convincente un buen rendimiento de las distintas soluciones aportadas. La solución técnica cumple los requisitos del pliego aportando pocas mejoras de los mismos.

- **MEDIA**: La solución técnica aportada describe de forma completa la arquitectura de los distintos subproyectos. La comprensión de los requisitos planteados es normal. La viabilidad del proyecto puede generar dudas. La metodología de trabajo elegida es utilizada dentro del ámbito tecnológico, pero no concuerda con las tareas del proyecto. Se justifica de forma convincente un rendimiento normal de las distintas soluciones aportadas. La solución técnica cumple los requisitos del pliego aportando muy pocas mejoras de los mismos o mejoras que no son coherentes.

- **BAJA**: La solución técnica aportada describe de forma incorrecta o incompleta la arquitectura de los distintos subproyectos. La comprensión de los requisitos planteados es mala. La viabilidad del proyecto genera dudas. La metodología de trabajo elegida no es utilizada dentro del ámbito tecnológico, aunque concuerda con las tareas del proyecto. Se justifica de forma convincente un mal rendimiento de las distintas soluciones aportadas. La solución técnica cumple justo los requisitos del pliego sin aportar mejoras o mejoras nada coherentes.

- **MUY BAJA**: La solución técnica aportada no describe o lo hace de forma muy incorrecta la arquitectura de los distintos subproyectos. La comprensión de los requisitos planteados es muy mala. La viabilidad del proyecto genera muchas dudas. La metodología de trabajo elegida no es utilizada dentro del ámbito tecnológico y no concuerda con las tareas del proyecto. Se justifica de forma convincente un rendimiento muy malo de las distintas soluciones aportadas. La solución técnica no cumple, o cumple muy justo los requisitos del pliego sin aportar mejoras o mejoras nada coherentes.

Para cada criterio/subcriterio los porcentajes de las puntuaciones en referencia al árbol de puntuaciones es el siguiente:

- **EXCELENTE:** del 76 % al 100 % de la puntuación de la sección correspondiente.
- **ALTA:** del 51 % al 75 % de la puntuación de la sección correspondiente.
- **MEDIA:** del 26 % al 50 % de la puntuación de la sección correspondiente.
- **BAJA:** del 1 % al 25 % de la puntuación de la sección correspondiente.
- **MUY BAJA:** 0 % de la puntuación de la sección correspondiente.

### Valoración de la planificación del servicio

Este bloque evalúa la capacidad del licitador para organizar, coordinar, controlar y ejecutar el servicio durante la vigencia del contrato. Se distribuye del siguiente modo:

- Calendario de los trabajos a desarrollar (**11 puntos**),

- Análisis de riesgos del proyecto (**1 punto**),

- Plan de gestión de contingencias (**1 punto**),

- Plan de gestión de la calidad del servicio (**1 punto**),

- Trazabilidad del servicio (**1 punto**).

La planificación del servicio debe constituir una **herramienta real de gestión**, no una representación genérica de fases sin detalle suficiente para verificar la viabilidad temporal y operativa de la propuesta.

Cada uno de estos subcriterios se evaluará siguiendo el siguiente árbol de puntuación:

- **EXCELENTE**: Excelente nivel de detalle en cuanto a la planificación, mediante un diagrama de Gantt o similar adaptado al proyecto, con muy buen detalle en cuanto a la ejecución de las diferentes tareas, con fechas específicas de cuándo se va a hacer cada tarea teniendo en cuenta el calendario escolar. Las tareas tienen una excelente coherencia en cuanto a su duración y su relación entre ellas para lograr la consecución de hitos y objetivos definidos. Se presenta un excelente análisis de riesgos del proyecto, un excelente plan de gestión de contingencias, un excelente plan de gestión de la calidad del servicio, y una excelente descripción de cómo se va a fiscalizar la trazabilidad del servicio.

- **ALTA**: Buen nivel de detalle en cuanto a la planificación, mediante un diagrama de Gantt o similar adaptado al proyecto, con buen detalle en cuanto a la ejecución de las diferentes tareas. Las tareas tienen una buena coherencia en cuanto a su duración y relación entre ellas para lograr la consecución de hitos y objetivos definidos. Se presenta un buen análisis de riesgos del proyecto, un buen plan de gestión de contingencias, un buen plan de gestión de la calidad del servicio, y una buena descripción de cómo se va a fiscalizar la trazabilidad del servicio.

- **MEDIA**: Detalle básico en cuanto a la planificación, mediante un diagrama de Gantt o similar, con poco detalle en cuanto a la ejecución de las diferentes tareas. Las tareas tienen una poca de coherencia en cuanto a su duración y su relación entre ellas para lograr la consecución de hitos y objetivos definidos. Se presenta un análisis de riesgos del proyecto correcto, un plan de gestión de contingencias correcto, un plan de gestión de la calidad del servicio correcto, y una descripción correcta de cómo se va a fiscalizar la trazabilidad del servicio.

- **BAJA**: Planificación muy básica, mediante un diagrama de Gantt o similar, con tareas genéricas y con poco detalle en cuanto a la ejecución de las diferentes tareas. Las tareas tienen una nula coherencia en cuanto a su duración y su relación entre ellas para lograr la consecución de hitos y objetivos definidos. Se presenta un mal análisis de riesgos del proyecto, un mal plan de gestión de contingencias, un mal plan de gestión de la calidad del servicio, y una mala descripción de cómo se va a fiscalizar la trazabilidad del servicio.

- **MUY BAJA**: Mala planificación, mediante un diagrama de Gantt o similar, con muy poco detalle en cuanto a la ejecución de las diferentes tareas. Las tareas tienen incoherencias en cuanto a su duración y su relación entre ellas para lograr la consecución de hitos y objetivos definidos. Se presenta un muy mal análisis de riesgos del proyecto, un muy mal plan de gestión de contingencias, un muy mal plan de gestión de la calidad del servicio, y una mala descripción de cómo se va a fiscalizar la trazabilidad del servicio.

Para cada criterio/subcriterio los porcentajes de las puntuaciones en referencia al árbol de puntuaciones es el siguiente:

- **EXCELENTE:** del 76 % al 100 % de la puntuación de la sección correspondiente.
- **ALTA:** del 51 % al 75 % de la puntuación de la sección correspondiente.
- **MEDIA:** del 26 % al 50 % de la puntuación de la sección correspondiente.
- **BAJA:** del 1 % al 25 % de la puntuación de la sección correspondiente.
- **MUY BAJA:** 0 % de la puntuación de la sección correspondiente.

### Fases del proceso de valoración individual

El proceso se desarrolla en las siguientes fases:

1. **Identificación de requisitos:** determinación de los requisitos y entregables aplicables a cada proyecto o subproyecto del Anexo II.

2. **Localización de evidencias:** examen exhaustivo de la memoria para identificar la cobertura, las fortalezas, las debilidades, las omisiones, las incoherencias y los elementos de valor añadido.

3. **Análisis técnico:** valoración del grado de concreción, coherencia, adecuación, viabilidad y verificabilidad de la solución y de la planificación.

4. **Traslado al baremo:** asignación de niveles y puntuaciones conforme a los subcriterios y al árbol de puntuación del Documento de Invitación.

5. **Comprobación de coherencia:** verificación de la correspondencia entre requisitos, evidencias, análisis, niveles cualitativos, puntuaciones y propuesta final.

Este enfoque permite reconstruir el razonamiento que sustenta cada puntuación y facilita la posterior integración del resultado individual en una valoración comparativa homogénea de todas las ofertas.

### Consideraciones preliminares sobre la propuesta

#### Estructura, coherencia interna y grado de finalización

La memoria está completa, mantiene coherencia entre arquitectura, soluciones, metodología y planificación y permite reconstruir la respuesta a los requisitos. El desarrollo técnico se apoya en componentes, APIs, automatizaciones, pruebas, despliegues controlados y mecanismos de seguimiento. No se han identificado errores conceptuales relevantes ni omisiones estructurales.

#### Nivel de desarrollo técnico y grado de concreción

La memoria está completa, mantiene coherencia entre arquitectura, soluciones, metodología y planificación y permite reconstruir la respuesta a los requisitos. El desarrollo técnico se apoya en componentes, APIs, automatizaciones, pruebas, despliegues controlados y mecanismos de seguimiento. No se han identificado errores conceptuales relevantes ni omisiones estructurales.

#### Comprensión y adaptación al entorno EducaMadrid

La memoria está completa, mantiene coherencia entre arquitectura, soluciones, metodología y planificación y permite reconstruir la respuesta a los requisitos. El desarrollo técnico se apoya en componentes, APIs, automatizaciones, pruebas, despliegues controlados y mecanismos de seguimiento. No se han identificado errores conceptuales relevantes ni omisiones estructurales.

#### Arquitectura, integración y requisitos no funcionales

La memoria está completa, mantiene coherencia entre arquitectura, soluciones, metodología y planificación y permite reconstruir la respuesta a los requisitos. El desarrollo técnico se apoya en componentes, APIs, automatizaciones, pruebas, despliegues controlados y mecanismos de seguimiento. No se han identificado errores conceptuales relevantes ni omisiones estructurales.

#### Trazabilidad y evaluabilidad

La memoria está completa, mantiene coherencia entre arquitectura, soluciones, metodología y planificación y permite reconstruir la respuesta a los requisitos. El desarrollo técnico se apoya en componentes, APIs, automatizaciones, pruebas, despliegues controlados y mecanismos de seguimiento. No se han identificado errores conceptuales relevantes ni omisiones estructurales.

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

### Consideraciones generales sobre la propuesta

#### Enfoque global de evaluación

La propuesta desarrolla de forma completa y mayoritariamente individualizada los proyectos del Anexo II. Define arquitecturas modulares, integraciones mediante APIs y servicios, procesos de despliegue y validación, seguridad desde el diseño, monitorización, pruebas y mecanismos de continuidad. Incluye numerosas mejoras concretas y verificables. La planificación es detallada y coherente, aunque algunos aspectos de dimensionamiento, gestión iterativa y análisis de riesgos podrían concretarse más.

#### Cobertura del Anexo II

De los 85 proyectos, 81 presentan desarrollo suficiente, 4 desarrollo insuficiente y 0 no incluyen una solución concreta. La cobertura nominal es completa: los 85 proyectos están presentes y aportan una solución, aunque la cobertura efectiva individualizada no es uniforme. Las soluciones se adaptan al entorno EducaMadrid y mantienen criterios comunes de seguridad, integración y operación. WEK constituye la principal excepción: sus cuatro proyectos reciben un tratamiento agregado y se clasifican individualmente como insuficientes, aunque el bloque incorpora una mejora global basada en despliegue reproducible, copia de seguridad y rollback.

#### Fortalezas y aportaciones de valor añadido

Destacan la cobertura completa, la arquitectura específica por sistema, la integración transversal, el tratamiento del rendimiento y la seguridad, las pruebas automatizadas y las numerosas mejoras verificables: modos de simulación, cuadros de mando, validaciones previas, automatización de especificaciones, controles de secretos y mecanismos de diagnóstico.

#### Carencias, errores y riesgos recurrentes

Las limitaciones son acotadas: parte del dimensionamiento podría cuantificarse mejor, la planificación tiene menor concreción en la gestión iterativa del desarrollo evolutivo, el análisis de riesgos conserva algún contenido genérico y WEK se trata de forma agregada. Estas carencias no impiden evaluar ni ejecutar el conjunto.

### Análisis por bloques funcionales del Anexo II

La exposición se agrupa por bloques cuando la memoria aplica un enfoque común, manteniendo la clasificación individual de los 85 proyectos en el anexo. Cada bloque distingue requisito, evidencia, fortalezas, carencias y valoración cualitativa.

#### Bloque de servicios transversales (TRA)

**Proyectos incluidos:** TRA1 a TRA8.

- **Consideración general del bloque**

El bloque exige resolver identidad, sincronización, interoperabilidad, seguridad y servicios comunes. Los ocho proyectos están desarrollados y se acreditan mejoras como simulación, OpenAPI, detección de secretos y control de eventos.

##### TRA1 a TRA8 — Servicios transversales

- **Requisito y alcance**

El alcance comprende identidad, sincronización, interoperabilidad, seguridad y servicios comunes, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

- **Análisis de la propuesta**

El contraste individual recogido en el anexo identifica 8 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. Los ocho proyectos están desarrollados y se acreditan mejoras como simulación, OpenAPI, detección de secretos y control de eventos.

- **Fortalezas y valor añadido**

Se acreditan soluciones concretas y coherentes; 5 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

- **Carencias, omisiones, errores o riesgos**

No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

- **Valoración cualitativa**

**EXCELENTE**: El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque TRA

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. Los ocho proyectos están desarrollados y se acreditan mejoras como simulación, OpenAPI, detección de secretos y control de eventos.

#### Bloque de Aulas Virtuales (AV — Moodle)

**Proyectos incluidos:** AV1 a AV21.

- **Consideración general del bloque**

El bloque exige resolver evolución de Moodle, integraciones, rendimiento, seguridad, escalabilidad y continuidad. Los veintiún proyectos disponen de soluciones concretas; destacan informes de salud, perfiles de carga, cuadros de mando, modos dry-run y validaciones previas.

##### AV1 a AV21 — Aulas Virtuales

**Requisito y alcance.** El alcance comprende evolución de Moodle, integraciones, rendimiento, seguridad, escalabilidad y continuidad, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 21 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. Los veintiún proyectos disponen de soluciones concretas; destacan informes de salud, perfiles de carga, cuadros de mando, modos dry-run y validaciones previas.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 17 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**EXCELENTE.** El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Integración, rendimiento, escalabilidad y continuidad del servicio

La propuesta relaciona componentes, integraciones, rendimiento, monitorización, seguridad y continuidad mediante mecanismos concretos y verificables, manteniendo coherencia con el entorno existente.

##### Conclusión del bloque AV

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. Los veintiún proyectos disponen de soluciones concretas; destacan informes de salud, perfiles de carga, cuadros de mando, modos dry-run y validaciones previas.

#### Bloque de Mediateca (MED)

**Proyectos incluidos:** MED1 a MED11.

- **Consideración general del bloque**

El bloque exige resolver procesamiento multimedia, subtitulado, búsqueda, almacenamiento, distribución e integración. Los once proyectos están desarrollados con flujos multimedia, indexación, control de versiones, validación de paquetes y mejoras de transcripción y búsqueda.

##### MED1 a MED11 — Mediateca

**Requisito y alcance.** El alcance comprende procesamiento multimedia, subtitulado, búsqueda, almacenamiento, distribución e integración, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 11 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. Los once proyectos están desarrollados con flujos multimedia, indexación, control de versiones, validación de paquetes y mejoras de transcripción y búsqueda.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 11 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**EXCELENTE.** El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Arquitectura, procesamiento multimedia e integración

La propuesta relaciona componentes, integraciones, rendimiento, monitorización, seguridad y continuidad mediante mecanismos concretos y verificables, manteniendo coherencia con el entorno existente.

##### Conclusión del bloque MED

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. Los once proyectos están desarrollados con flujos multimedia, indexación, control de versiones, validación de paquetes y mejoras de transcripción y búsqueda.

#### Bloque de Correo Web (COR)

**Proyectos incluidos:** COR1 a COR4.

- **Consideración general del bloque**

El bloque exige resolver evolución del correo, funciones de inteligencia artificial, seguridad e integración. COR1 a COR4 se adaptan al servicio real e incorporan diagnóstico, retroalimentación del usuario y controles para preservar tono e información factual.

##### COR1 a COR4 — Correo Web

**Requisito y alcance.** El alcance comprende evolución del correo, funciones de inteligencia artificial, seguridad e integración, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 4 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. COR1 a COR4 se adaptan al servicio real e incorporan diagnóstico, retroalimentación del usuario y controles para preservar tono e información factual.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 4 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**EXCELENTE.** El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque COR

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. COR1 a COR4 se adaptan al servicio real e incorporan diagnóstico, retroalimentación del usuario y controles para preservar tono e información factual.

#### Bloque Cloud (CLO — Nextcloud y Collabora)

**Proyectos incluidos:** CLO1 y CLO2.

- **Consideración general del bloque**

El bloque exige resolver almacenamiento, sincronización, edición colaborativa, seguridad y rendimiento. CLO1 y CLO2 definen soluciones concretas para Nextcloud y Collabora, con arquitectura e integración coherentes, aunque sin mejora adicional diferenciada.

##### CLO1 y CLO2 — Cloud

**Requisito y alcance.** El alcance comprende almacenamiento, sincronización, edición colaborativa, seguridad y rendimiento, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 2 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. CLO1 y CLO2 definen soluciones concretas para Nextcloud y Collabora, con arquitectura e integración coherentes, aunque sin mejora adicional diferenciada.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 0 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**ALTA.** El nivel **ALTA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque CLO

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **ALTA**. CLO1 y CLO2 definen soluciones concretas para Nextcloud y Collabora, con arquitectura e integración coherentes, aunque sin mejora adicional diferenciada.

#### Bloque WordPress Multisite (WPM)

**Proyectos incluidos:** WPM1 a WPM5.

- **Consideración general del bloque**

El bloque exige resolver mantenimiento, licencias, protección perimetral, antiabuso y autenticación. Los cinco proyectos están desarrollados con controles de versiones y licencias, correlación WAF, mejoras de captcha y políticas individualizadas de doble factor.

##### WPM1 a WPM5 — WordPress Multisite

**Requisito y alcance.** El alcance comprende mantenimiento, licencias, protección perimetral, antiabuso y autenticación, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 5 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. Los cinco proyectos están desarrollados con controles de versiones y licencias, correlación WAF, mejoras de captcha y políticas individualizadas de doble factor.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 5 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**EXCELENTE.** El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque WPM

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. Los cinco proyectos están desarrollados con controles de versiones y licencias, correlación WAF, mejoras de captcha y políticas individualizadas de doble factor.

#### Bloque de Vídeo y Videoconferencia (VID)

**Proyectos incluidos:** VID1 a VID4.

- **Consideración general del bloque**

El bloque exige resolver integración educativa, concurrencia, calidad, grabaciones y continuidad. Los cuatro proyectos abordan integración, métricas, admisión progresiva, caducidad de grabaciones y eventos de alta audiencia.

##### VID1 a VID4 — Vídeo y Videoconferencia

**Requisito y alcance.** El alcance comprende integración educativa, concurrencia, calidad, grabaciones y continuidad, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 4 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. Los cuatro proyectos abordan integración, métricas, admisión progresiva, caducidad de grabaciones y eventos de alta audiencia.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 4 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**EXCELENTE.** El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque VID

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. Los cuatro proyectos abordan integración, métricas, admisión progresiva, caducidad de grabaciones y eventos de alta audiencia.

#### Servicios unitarios

**Proyectos incluidos:** EMP1, LDAP, EXE, FOR1, BUS1 y ANI1.

##### Consideración general del conjunto

El bloque exige resolver los requisitos específicos y diferenciados de los seis servicios unitarios. Los seis servicios reciben soluciones específicas y evaluables, con cuadros de mando, controles de credenciales, accesibilidad, salud, búsqueda y deuda técnica.

##### EMP1, LDAP, EXE, FOR1, BUS1 y ANI1 — Servicios unitarios

**Requisito y alcance.** El alcance comprende los requisitos específicos y diferenciados de los seis servicios unitarios, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 6 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. Los seis servicios reciben soluciones específicas y evaluables, con cuadros de mando, controles de credenciales, accesibilidad, salud, búsqueda y deuda técnica.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 6 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**EXCELENTE.** El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión de los servicios unitarios

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. Los seis servicios reciben soluciones específicas y evaluables, con cuadros de mando, controles de credenciales, accesibilidad, salud, búsqueda y deuda técnica.

#### Sistemas y servicios complementarios

**Proyectos incluidos:** SYN, CAU, EDU, BAN, DTIC, SEG, ALB, AVI, FOR, BOL, AYU, POR, WES, IFZ, MAX, GES, USO, MAM, EML y ABI.

##### Consideración general del conjunto

El bloque exige resolver integración, seguridad, operación, accesibilidad, comunicación y analítica de los sistemas complementarios. Los veinte sistemas están desarrollados de forma suficiente y dieciséis incorporan mejoras verificables adaptadas a su función.

##### SYN a ABI — Sistemas y servicios complementarios

**Requisito y alcance.** El alcance comprende integración, seguridad, operación, accesibilidad, comunicación y analítica de los sistemas complementarios, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 20 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. Los veinte sistemas están desarrollados de forma suficiente y dieciséis incorporan mejoras verificables adaptadas a su función.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 16 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**EXCELENTE.** El nivel **EXCELENTE** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión de los sistemas complementarios

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **EXCELENTE**. Los veinte sistemas están desarrollados de forma suficiente y dieciséis incorporan mejoras verificables adaptadas a su función.

#### Bloque Wekan (WEK)

**Proyectos incluidos:** WEK1 a WEK4.

- **Consideración general del bloque**

El bloque exige resolver mantenimiento, actualización, despliegue, respaldo y evolución de Wekan. Los cuatro subproyectos se tratan de forma agregada y con menor detalle individual, pero la solución común aporta despliegue reproducible, backup y rollback probado.

##### WEK1 a WEK4 — Wekan

**Requisito y alcance.** El alcance comprende mantenimiento, actualización, despliegue, respaldo y evolución de Wekan, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 0 proyectos con desarrollo suficiente, 4 con desarrollo insuficiente y 0 sin solución concreta. Los cuatro subproyectos se tratan de forma agregada y con menor detalle individual, pero la solución común aporta despliegue reproducible, backup y rollback probado.

**Fortalezas y valor añadido.** Se acreditan soluciones concretas y coherentes; 4 proyectos incorporan mejoras con valor añadido verificable dentro del bloque.

**Carencias, omisiones, errores o riesgos.** 4 proyectos presentan desarrollo genérico o incompleto. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**MEDIA.** El nivel **MEDIA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque WEK

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **MEDIA**. Los cuatro subproyectos se tratan de forma agregada y con menor detalle individual, pero la solución común aporta despliegue reproducible, backup y rollback probado.

### Conclusión del análisis detallado

La cobertura es completa y homogénea en TRA, AV, MED, COR, CLO, WPM, VID, servicios unitarios y sistemas complementarios. Las soluciones se adaptan al entorno EducaMadrid y mantienen criterios comunes de seguridad, integración y operación. WEK constituye la principal excepción: recibe un tratamiento agregado y menos individualizado, aunque incorpora una mejora global basada en despliegue reproducible, copia de seguridad y rollback. Las limitaciones son acotadas: parte del dimensionamiento podría cuantificarse mejor, la planificación tiene menor concreción en la gestión iterativa del desarrollo evolutivo, el análisis de riesgos conserva algún contenido genérico y WEK se trata de forma agregada. Estas carencias no impiden evaluar ni ejecutar el conjunto.

## EVALUACIÓN DE LA SOLUCIÓN TÉCNICA OFERTADA

### Fundamentación de la valoración

La valoración de la solución técnica se basa en el análisis pormenorizado de los proyectos y subproyectos anteriores. La puntuación no responde a la mera presencia formal de contenidos, sino a su **calidad, concreción, coherencia, adecuación, viabilidad y verificabilidad**, así como al alcance real de las fortalezas y carencias detectadas.

### Arquitectura planteada en los distintos subproyectos — máximo 2 puntos

La arquitectura es modular, coherente y específica para los sistemas, con capas diferenciadas, APIs, seguridad, despliegue controlado y mecanismos de integración verificables.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 1,80 sobre 2,00

### Grado de comprensión de los requisitos planteados — máximo 2 puntos

La propuesta interpreta correctamente el entorno y traduce los requisitos funcionales y no funcionales en soluciones concretas, sin errores conceptuales relevantes.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 1,90 sobre 2,00

### Viabilidad técnica y operativa del proyecto — máximo 1 punto

Los despliegues controlados, validaciones previas, rollback y mecanismos de coordinación acreditan una ejecución viable; solo falta mayor cuantificación en algunos dimensionamientos.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 0,90 sobre 1,00

### Metodología de trabajo aplicada — máximo 1 punto

Métrica v3 se integra con prácticas actuales, ciclo de vida, automatización de pruebas e integración continua de forma aplicable al contrato.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 0,90 sobre 1,00

### Rendimiento previsible de las soluciones — máximo 1 punto

Se definen optimización, caché, procesamiento asíncrono, control de concurrencia, monitorización y pruebas de carga adaptadas a los sistemas.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 0,90 sobre 1,00

### Satisfacción de los requisitos del Anexo II — máximo 8 puntos

Los 85 proyectos están cubiertos; 81 presentan desarrollo suficiente y solo WEK conserva desarrollo agregado insuficiente. Se acreditan 72 aportaciones de valor añadido y no se observan errores técnicos relevantes.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 7,20 sobre 8,00

### Resultado global de la solución técnica

| **Subcriterio**                | **Máximo** | **Nivel** | **Puntuación** |
| ------------------------------ | ---------: | --------- | -------------: |
| Arquitectura | 2,00 | EXCELENTE | 1,80 |
| Comprensión de los requisitos | 2,00 | EXCELENTE | 1,90 |
| Viabilidad | 1,00 | EXCELENTE | 0,90 |
| Metodología | 1,00 | EXCELENTE | 0,90 |
| Rendimiento | 1,00 | EXCELENTE | 0,90 |
| Satisfacción de los requisitos | 8,00 | EXCELENTE | 7,20 |
| **TOTAL SOLUCIÓN TÉCNICA**     |  **15,00** |           |     **13,60** |

## EVALUACIÓN DE LA PLANIFICACIÓN DEL SERVICIO

### Consideraciones generales sobre la planificación

La planificación debe constituir una **herramienta real de gestión del servicio**. Su valoración atiende a la correspondencia con los proyectos y entregables del Anexo II, la secuencia y duración de las tareas, sus dependencias, los hitos, la asignación de recursos, la adaptación al calendario del servicio y la integración de los mecanismos de riesgo, contingencia, calidad y trazabilidad.

### Calendario de los trabajos a desarrollar — máximo 11 puntos

La planificación incluye fases, hitos, dependencias, Gantt con leyenda y adaptación al calendario educativo. La gestión iterativa del desarrollo evolutivo podría concretarse más.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 9,60 sobre 11,00

### Análisis de riesgos del proyecto — máximo 1 punto

Se identifican y clasifican riesgos por impacto y probabilidad con medidas de mitigación, aunque parte del tratamiento mantiene un carácter genérico.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 0,85 sobre 1,00

### Plan de gestión de contingencias — máximo 1 punto

Se definen recuperación ante fallos, despliegues controlados y medidas de continuidad coherentes con servicios críticos.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 0,90 sobre 1,00

### Plan de gestión de la calidad del servicio — máximo 1 punto

El modelo incorpora indicadores, mejora continua, auditorías, control de incidencias y mecanismos de validación durante la ejecución.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 0,90 sobre 1,00

### Trazabilidad del servicio — máximo 1 punto

La propuesta relaciona requisitos, actuaciones y entregables, registra la ejecución y facilita el seguimiento y las auditorías.

**Nivel cualitativo:** EXCELENTE
**Puntuación:** 0,85 sobre 1,00

### Resultado global de la planificación

| **Subcriterio**                     | **Máximo** | **Nivel** | **Puntuación** |
| ----------------------------------- | ---------: | --------- | -------------: |
| Calendario y planificación temporal | 11,00 | EXCELENTE | 9,60 |
| Análisis de riesgos | 1,00 | EXCELENTE | 0,85 |
| Plan de contingencias | 1,00 | EXCELENTE | 0,90 |
| Plan de calidad | 1,00 | EXCELENTE | 0,90 |
| Trazabilidad | 1,00 | EXCELENTE | 0,85 |
| **TOTAL PLANIFICACIÓN**             |  **15,00** |           |     **13,10** |

## RESULTADO FINAL CONSOLIDADO

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                  13,60 |
| Planificación del servicio |                 15,00 |                  13,10 |
| **PUNTUACIÓN FINAL** |             **30,00** |              **26,70** |

### Interpretación de la puntuación

La puntuación consolidada de 26,70 puntos refleja de forma proporcionada la cobertura, profundidad, viabilidad y planificación acreditadas. La calidad global es alta y plenamente evaluable. La oferta obtiene 26,70 puntos sobre 30, supera el umbral mínimo de 15 puntos y procede proponer su continuación en el procedimiento.

## CONCLUSIONES FINALES Y PROPUESTA

### Conclusiones globales de la evaluación técnica

La propuesta desarrolla de forma completa y mayoritariamente individualizada los proyectos del Anexo II. Define arquitecturas modulares, integraciones mediante APIs y servicios, procesos de despliegue y validación, seguridad desde el diseño, monitorización, pruebas y mecanismos de continuidad. Incluye numerosas mejoras concretas y verificables. La planificación es detallada y coherente, aunque algunos aspectos de dimensionamiento, gestión iterativa y análisis de riesgos podrían concretarse más. La calidad global es alta y plenamente evaluable. La oferta obtiene 26,70 puntos sobre 30, supera el umbral mínimo de 15 puntos y procede proponer su continuación en el procedimiento.

### Conclusiones sobre la solución técnica

La cobertura es completa y homogénea en TRA, AV, MED, COR, CLO, WPM, VID, servicios unitarios y sistemas complementarios. Las soluciones se adaptan al entorno EducaMadrid y mantienen criterios comunes de seguridad, integración y operación. WEK constituye la principal excepción: recibe un tratamiento agregado y menos individualizado, aunque incorpora una mejora global basada en despliegue reproducible, copia de seguridad y rollback. Las limitaciones son acotadas: parte del dimensionamiento podría cuantificarse mejor, la planificación tiene menor concreción en la gestión iterativa del desarrollo evolutivo, el análisis de riesgos conserva algún contenido genérico y WEK se trata de forma agregada. Estas carencias no impiden evaluar ni ejecutar el conjunto.

### Conclusiones sobre la planificación del servicio

La planificación incluye fases, hitos, dependencias, Gantt con leyenda y adaptación al calendario educativo. La gestión iterativa del desarrollo evolutivo podría concretarse más. Se identifican y clasifican riesgos por impacto y probabilidad con medidas de mitigación, aunque parte del tratamiento mantiene un carácter genérico. Se definen recuperación ante fallos, despliegues controlados y medidas de continuidad coherentes con servicios críticos. El modelo incorpora indicadores, mejora continua, auditorías, control de incidencias y mecanismos de validación durante la ejecución. La propuesta relaciona requisitos, actuaciones y entregables, registra la ejecución y facilita el seguimiento y las auditorías.

### Justificación de la valoración

Las puntuaciones parciales trasladan el nivel efectivamente acreditado en cada subcriterio, sin compensar omisiones estructurales con fortalezas puntuales. El resultado de 13,60 puntos en solución y 13,10 en planificación es coherente con el análisis y con el total de 26,70 puntos.

### Aplicación del umbral mínimo y propuesta final

La propuesta de **empresa_s** obtiene una puntuación de **26,70 puntos sobre 30** en los criterios sujetos a juicio de valor.

El umbral mínimo exigido para continuar en el procedimiento es de **15 puntos sobre 30**. Por tanto, la oferta **ALCANZA** el nivel mínimo de calidad técnica establecido.

En consecuencia, procede proponer la **continuación de la oferta en el procedimiento de adjudicación**.


### Garantía de igualdad de trato y objetividad

La valoración aplica los mismos criterios, niveles de exigencia y reglas de puntuación utilizados para el resto de licitadores. Las conclusiones se fundamentan exclusivamente en la memoria presentada y en la documentación reguladora, sin incorporar capacidades presumidas ni elementos externos.

## ANEXO. RELACIÓN DE PROYECTOS Y GRADO DE DESARROLLO DE LA PROPUESTA TÉCNICA

### Objeto y criterios de clasificación

El presente anexo resume, de manera sistemática, el grado de desarrollo de la propuesta técnica para cada proyecto o subproyecto del Anexo II. Su finalidad es aportar trazabilidad documental al análisis, sin sustituir la motivación cualitativa del informe ni producir por sí solo una traslación automática a la puntuación final.

Se utilizarán, cuando resulten aplicables, los siguientes grados de desarrollo:

- **Propuesta técnica no incluida:** no existe una solución concreta para el proyecto o subproyecto.

- **Propuesta técnica incluida con desarrollo insuficiente o deficiente:** existe contenido, pero es genérico o carece de procesos, arquitectura, herramientas o mecanismos de implementación suficientes.

- **Propuesta técnica incluida con desarrollo suficiente:** existe una solución concreta y evaluable, con un grado adecuado de definición técnica.

De forma separada, se marcarán los siguientes indicadores, que pueden coexistir con cualquiera de los grados anteriores:

- **Error técnico relevante:** contiene errores conceptuales o tecnológicos que afectan a la adecuación o viabilidad de la solución.

- **Propuesta de mejora sin valor añadido real (PM):** refuerza o reformula actuaciones ya exigidas sin incorporar capacidades diferenciales verificables.

- **Propuesta con valor añadido (VA):** incorpora una mejora real, coherente y suficientemente desarrollada mediante nuevas capacidades, herramientas, automatizaciones, arquitecturas o resultados verificables.

### Tablas de subproyectos

#### Bloque transversal (TRA)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| TRA1 | SUFICIENTE | VA | NO | modo “simulación” |
| TRA2 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| TRA3 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| TRA4 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| TRA5 | SUFICIENTE | VA | NO | mejora de seguridad y soporte |
| TRA6 | SUFICIENTE | VA | NO | generación automática de una especificación OpenAPI |
| TRA7 | SUFICIENTE | VA | NO | verificador automático de secretos expuestos |
| TRA8 | SUFICIENTE | VA | NO | modo identificativo único para eventos de centro o de calendario escolar |

#### Aulas Virtuales (AV)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| AV1 | SUFICIENTE | VA | NO | “informe de salud post-upgrade” por isla |
| AV2 | SUFICIENTE | VA | NO | perfiles para tráfico web y tareas internas |
| AV3 | SUFICIENTE | VA | NO | ficha técnica por plugin con “decisión de ciclo de vida” |
| AV4 | SUFICIENTE | VA | NO | cuadro de mando técnico de salud Moodle |
| AV5 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| AV6 | SUFICIENTE | VA | NO | modo compacto |
| AV7 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| AV8 | SUFICIENTE | VA | NO | calendario técnico de “campaña de inicio de curso” |
| AV9 | SUFICIENTE | VA | NO | modo “dry-run” |
| AV10 | SUFICIENTE | VA | NO | prueba automática de conectividad |
| AV11 | SUFICIENTE | VA | NO | notificación por correo al docente |
| AV12 | SUFICIENTE | VA | NO | opción de generar textos en distintos idiomas con IA |
| AV13 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| AV14 | SUFICIENTE | VA | NO | mostrar NIA enmascarado cuando no sea imprescindible verlo completo |
| AV15 | SUFICIENTE | VA | NO | SSO funcional desde el aplicativo móvil |
| AV16 | SUFICIENTE | VA | NO | prueba de carga específica para Kuet |
| AV17 | SUFICIENTE | VA | NO | modo de previsualización |
| AV18 | SUFICIENTE | VA | NO | simulación previa “validar sin enviar” |
| AV19 | SUFICIENTE | VA | NO | añadir estimación previa de impacto |
| AV20 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| AV21 | SUFICIENTE | VA | NO | añadir scopes de API por tipo de operación |

#### Mediateca (MED)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| MED1 | SUFICIENTE | VA | NO | incorporar todos los subtítulos multiidioma en las búsquedas por Elastic |
| MED2 | SUFICIENTE | VA | NO | “modo explicación” |
| MED3 | SUFICIENTE | VA | NO | limitar la comprobación de sesión activa en ciertos casos |
| MED4 | SUFICIENTE | VA | NO | guardado de versiones anteriores del proyecto |
| MED5 | SUFICIENTE | VA | NO | comprobación previa del ZIP e informe al usuario |
| MED6 | SUFICIENTE | VA | NO | modo “simulación” |
| MED7 | SUFICIENTE | VA | NO | mostrar antes de enviar validación ligera en cliente para extensiones admitidas |
| MED8 | SUFICIENTE | VA | NO | bloque “qué puedo hacer ahora” |
| MED9 | SUFICIENTE | VA | NO | transcripción multiidioma |
| MED10 | SUFICIENTE | VA | NO | indicador interno de confianza |
| MED11 | SUFICIENTE | VA | NO | mapa vivo de deuda técnica |

#### Correo Web (COR)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| COR1 | SUFICIENTE | VA | NO | pantalla de diagnóstico |
| COR2 | SUFICIENTE | VA | NO | botón “el resumen no es correcto” |
| COR3 | SUFICIENTE | VA | NO | opción “mantener tono institucional” |
| COR4 | SUFICIENTE | VA | NO | opción “no cambiar información factual” |

#### Cloud (CLO)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| CLO1 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| CLO2 | SUFICIENTE | NO | NO | Solución concreta y evaluable. |

#### WordPress Multisite (WPM)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| WPM1 | SUFICIENTE | VA | NO | panel técnico interno de versiones por componente |
| WPM2 | SUFICIENTE | VA | NO | aviso de licencias a punto de caducar o pendientes de activar |
| WPM3 | SUFICIENTE | VA | NO | procedimiento de correlación entre eventos del WAF y logs de WordPress |
| WPM4 | SUFICIENTE | VA | NO | mejoras en captcha |
| WPM5 | SUFICIENTE | VA | NO | política individualizada de 2FA |

#### Vídeo y Videoconferencia (VID)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| VID1 | SUFICIENTE | VA | NO | recolector de métricas por emisión |
| VID2 | SUFICIENTE | VA | NO | regla de admisión progresiva para salas de invitados |
| VID3 | SUFICIENTE | VA | NO | aviso de caducidad de grabaciones para responsables de centro |
| VID4 | SUFICIENTE | VA | NO | plantilla de “evento de alta audiencia” |

#### Servicios unitarios

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| EMP1 | SUFICIENTE | VA | NO | dashboard de salud de diferentes componentes |
| LDAP | SUFICIENTE | VA | NO | panel de “contraseñas temporales activas” |
| EXE | SUFICIENTE | VA | NO | plantilla “DUA ligero” y reproductor en la nube Nextcloud de EM |
| FOR1 | SUFICIENTE | VA | NO | informe de salud de Formularios |
| BUS1 | SUFICIENTE | VA | NO | modo de “búsquedas frecuentes sin resultados” |
| ANI1 | SUFICIENTE | VA | NO | crear un “mapa de deuda técnica” |

#### Sistemas y servicios complementarios

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| SYN | SUFICIENTE | VA | NO | evolución hacia API de Raíces |
| CAU | SUFICIENTE | VA | NO | panel de verificación postactualización |
| EDU | SUFICIENTE | VA | NO | Biblioteca interna ligera de seguridad para EducaSAAC, |
| BAN | SUFICIENTE | VA | NO | panel de comprobación previa |
| DTIC | SUFICIENTE | VA | NO | informe previo en HTML y CSV |
| SEG | SUFICIENTE | VA | NO | panel de salud de edición |
| ALB | SUFICIENTE | VA | NO | consola de revisión de respuestas sin datos personales |
| AVI | SUFICIENTE | VA | NO | validación de seguridad previa |
| FOR | SUFICIENTE | VA | NO | autencitación contra SSO |
| BOL | SUFICIENTE | VA | NO | validación previa al envío |
| AYU | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| POR | SUFICIENTE | VA | NO | endpoint de validación previa |
| WES | SUFICIENTE | VA | NO | matriz de páginas críticas |
| IFZ | SUFICIENTE | VA | NO | catálogo vivo de componentes |
| MAX | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| GES | SUFICIENTE | VA | NO | validador previo de ficheros |
| USO | SUFICIENTE | VA | NO | instalación de rybbit contra el SSO y script de generación de entorno para los centros solicitados |
| MAM | SUFICIENTE | VA | NO | orquestador ligero de scripts accesible por VPN |
| EML | SUFICIENTE | NO | NO | Solución concreta y evaluable. |
| ABI | SUFICIENTE | NO | NO | Solución concreta y evaluable. |

#### Wekan (WEK)

| **Proyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| WEK1 | INSUFICIENTE | VA | NO | Tratamiento agregado; Docker Compose con backup y rollback probado. |
| WEK2 | INSUFICIENTE | VA | NO | Tratamiento agregado; Docker Compose con backup y rollback probado. |
| WEK3 | INSUFICIENTE | VA | NO | Tratamiento agregado; Docker Compose con backup y rollback probado. |
| WEK4 | INSUFICIENTE | VA | NO | Tratamiento agregado; Docker Compose con backup y rollback probado. |

### Resumen cuantitativo del anexo

#### Grado de desarrollo

| **Clasificación**                    | **Número de proyectos** | **Porcentaje** |
| ------------------------------------ | ----------------------: | -------------: |
| No incluidos                         |                      0 |         0,00 % |
| Desarrollo insuficiente o deficiente |                      4 |         4,71 % |
| Desarrollo suficiente                |                     81 |        95,29 % |
| **TOTAL DE PROYECTOS**               |               **85** |   **100,00 %** |

#### Indicadores adicionales

Los indicadores adicionales no son excluyentes entre sí ni respecto del grado de desarrollo, por lo que sus porcentajes no tienen que sumar el 100 %.

| **Indicador**                                  | **Número de proyectos** | **Porcentaje sobre el total** |
| ---------------------------------------------- | ----------------------: | ----------------------------: |
| Con errores técnicos relevantes                |                      0 |                         0,00 % |
| Con propuesta de mejora sin valor añadido real |                      0 |                       0,00 % |
| Con propuesta de mejora con valor añadido real |                     72 |                        84,71 % |

### Conclusión del anexo

La clasificación muestra 81 proyectos con desarrollo suficiente, 4 insuficientes y 0 sin solución concreta. Se identifican 0 proyectos con errores relevantes y 72 con valor añadido verificable. La cobertura es completa y homogénea en TRA, AV, MED, COR, CLO, WPM, VID, servicios unitarios y sistemas complementarios. Las soluciones se adaptan al entorno EducaMadrid y mantienen criterios comunes de seguridad, integración y operación. WEK constituye la principal excepción: recibe un tratamiento agregado y menos individualizado, aunque incorpora una mejora global basada en despliegue reproducible, copia de seguridad y rollback. El anexo aporta trazabilidad, mientras que la puntuación deriva de la valoración conjunta de todos los subcriterios.
