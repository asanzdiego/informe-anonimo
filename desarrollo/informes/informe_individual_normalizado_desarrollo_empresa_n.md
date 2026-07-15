# INFORME DE VALORACIÓN TÉCNICA INDIVIDUAL

- **Contrato:** Desarrollo evolutivo y correctivo de las Aulas Virtuales, la Mediateca, las webs de centro, el correo web, EMPieza y otras aplicaciones de EducaMadrid (BAC07_2026)
- **Licitador:** empresa_n

## RESUMEN EJECUTIVO

### Objeto del informe

El presente informe tiene por objeto realizar la **valoración técnica de la propuesta presentada por empresa_n** en el procedimiento basado en el **Sistema Dinámico de Adquisición SDA 26/2021**, relativo a los servicios de **Desarrollo evolutivo y correctivo de las Aulas Virtuales, la Mediateca, las webs de centro, el correo web, EMPieza y otras aplicaciones de EducaMadrid (BAC07_2026)**.

El informe determina la puntuación correspondiente a los criterios sujetos a juicio de valor, comprueba el cumplimiento del **umbral mínimo de 15 puntos sobre 30** y formula la propuesta de continuación o exclusión que procede para la oferta.

### Metodología de valoración

La evaluación se ha estructurado en dos niveles complementarios. En primer lugar, se ha realizado un análisis técnico detallado de los proyectos y subproyectos incluidos en el Anexo II del Documento de Invitación, examinando el grado de desarrollo, adecuación y verificabilidad de las soluciones propuestas. En segundo lugar, los resultados de dicho análisis se han trasladado al esquema de valoración previsto en el apartado 7.2 del Documento de Invitación, asignando las puntuaciones correspondientes en función del nivel real de adecuación observado.

Este enfoque garantiza la trazabilidad entre **los requisitos definidos, las evidencias contenidas en la memoria, el análisis técnico efectuado y la puntuación final asignada**.

### Síntesis técnica de la propuesta

La propuesta presenta una estructura formal correcta y una cobertura nominal amplia del ecosistema EducaMadrid, pero el desarrollo efectivo es mayoritariamente descriptivo. Faltan arquitecturas específicas, flujos de integración, métricas, criterios de aceptación y mecanismos de validación suficientes. Se reconocen contenidos evaluables en algunos proyectos y una base metodológica apoyada en Métrica v3, aunque su aplicación práctica es limitada. Los errores de interpretación tecnológica y la baja concreción reducen la viabilidad y la trazabilidad del conjunto.

### Principales conclusiones del análisis

El patrón dominante es la inclusión formal de los proyectos con desarrollo insuficiente. Las carencias se repiten en TRA, AV, MED, COR, WPM, los servicios unitarios, los sistemas complementarios y WEK; CLO y parte de VID presentan un tratamiento relativamente más consistente. Entre los errores acreditados figura la contradicción síncrono/asíncrono de AV11.

### Resultado de la valoración

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                    5,10 |
| Planificación del servicio |                 15,00 |                    5,60 |
| **TOTAL**                  |             **30,00** |               **10,70** |

### Conclusión del resumen ejecutivo

La oferta obtiene 10,70 puntos sobre 30 y no alcanza el umbral mínimo de 15 puntos; procede proponer su exclusión por aplicación aritmética del umbral tras la valoración motivada.

## INTRODUCCIÓN

### Alcance del informe

El presente informe evalúa la memoria técnica presentada por **empresa_n** para la prestación de los servicios de **DESARROLLO EVOLUTIVO Y CORRECTIVO DE LAS AULAS VIRTUALES, LA MEDIATECA, LAS WEBS DE CENTRO, EL CORREO WEB, EMPIEZA Y OTRAS APLICACIONES DE EDUCAMADRID (BAC07_2026)**. El análisis comprende tanto la **solución técnica ofertada** como la **planificación del servicio**, de acuerdo con los criterios sujetos a juicio de valor establecidos en el apartado 7.2 del Documento de Invitación.

La evaluación toma como referencia los proyectos, subproyectos, actuaciones y entregables definidos en el Anexo II, y atiende exclusivamente al contenido efectivamente desarrollado en la documentación presentada.

### Marco normativo

El presente informe se elabora en el marco del procedimiento de adjudicación correspondiente a **Sistema Dinámico de Adquisición SDA 26/2021**. El procedimiento se rige por lo dispuesto en la **Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público** (en adelante, LCSP), por el Pliego de Cláusulas Administrativas Particulares y por las condiciones específicas establecidas en el Documento de Invitación y demás documentación reguladora del expediente.

La valoración técnica se fundamenta en los **criterios de adjudicación sujetos a juicio de valor definidos en el apartado 7.2 del Documento de Invitación**, cuya finalidad es evaluar la calidad de la propuesta desde una perspectiva integral que contemple tanto la **adecuación de la solución técnica ofertada** como la **viabilidad organizativa y temporal de su ejecución**.

De conformidad con el **artículo 145 de la LCSP**, los criterios de adjudicación deben permitir determinar la mejor relación calidad-precio y aplicarse de forma objetiva, transparente y no discriminatoria. La evaluación se realiza, por tanto, con arreglo a los principios de **igualdad de trato, objetividad, transparencia, proporcionalidad y trazabilidad**, aplicando a todas las ofertas un mismo marco metodológico y sin incorporar elementos externos a la documentación presentada por los licitadores.

Asimismo, el **artículo 146.3 de la LCSP** permite establecer umbrales mínimos en los criterios cualitativos sujetos a juicio de valor. Conforme al Documento de Invitación, las ofertas deben alcanzar un **nivel mínimo de calidad técnica equivalente al cincuenta por ciento de la puntuación máxima asignable a estos criterios** para continuar en el procedimiento.

La puntuación se determina mediante juicio técnico motivado. Una vez obtenido el total, la aplicación aritmética del umbral no añade una valoración discrecional adicional. La valoración debe permitir **comprobar de forma clara la puntuación obtenida y motivar la correspondiente propuesta de admisión o exclusión**, sin confundir el resultado con la solvencia del licitador ni con un incumplimiento técnico autónomo.

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

La memoria está formalmente ordenada y cubre el alcance de manera extensa, pero la relación entre requisitos, soluciones, arquitectura y planificación no queda desarrollada con precisión suficiente. Predominan formulaciones generales y se detectan errores conceptuales en sistemas clave. La propuesta no define de forma sistemática componentes, interfaces, métricas, entregables verificables ni criterios de aceptación, lo que limita su evaluabilidad.

#### Nivel de desarrollo técnico y grado de concreción

La memoria está formalmente ordenada y cubre el alcance de manera extensa, pero la relación entre requisitos, soluciones, arquitectura y planificación no queda desarrollada con precisión suficiente. Predominan formulaciones generales y se detectan errores conceptuales en sistemas clave. La propuesta no define de forma sistemática componentes, interfaces, métricas, entregables verificables ni criterios de aceptación, lo que limita su evaluabilidad.

#### Comprensión y adaptación al entorno EducaMadrid

La memoria está formalmente ordenada y cubre el alcance de manera extensa, pero la relación entre requisitos, soluciones, arquitectura y planificación no queda desarrollada con precisión suficiente. Predominan formulaciones generales y se detectan errores conceptuales en sistemas clave. La propuesta no define de forma sistemática componentes, interfaces, métricas, entregables verificables ni criterios de aceptación, lo que limita su evaluabilidad.

#### Arquitectura, integración y requisitos no funcionales

La memoria está formalmente ordenada y cubre el alcance de manera extensa, pero la relación entre requisitos, soluciones, arquitectura y planificación no queda desarrollada con precisión suficiente. Predominan formulaciones generales y se detectan errores conceptuales en sistemas clave. La propuesta no define de forma sistemática componentes, interfaces, métricas, entregables verificables ni criterios de aceptación, lo que limita su evaluabilidad.

#### Trazabilidad y evaluabilidad

La memoria está formalmente ordenada y cubre el alcance de manera extensa, pero la relación entre requisitos, soluciones, arquitectura y planificación no queda desarrollada con precisión suficiente. Predominan formulaciones generales y se detectan errores conceptuales en sistemas clave. La propuesta no define de forma sistemática componentes, interfaces, métricas, entregables verificables ni criterios de aceptación, lo que limita su evaluabilidad.

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

### Consideraciones generales sobre la propuesta

#### Enfoque global de evaluación

La propuesta presenta una estructura formal correcta y una cobertura nominal amplia del ecosistema EducaMadrid, pero el desarrollo efectivo es mayoritariamente descriptivo. Faltan arquitecturas específicas, flujos de integración, métricas, criterios de aceptación y mecanismos de validación suficientes. Se reconocen contenidos evaluables en algunos proyectos y una base metodológica apoyada en Métrica v3, aunque su aplicación práctica es limitada. Los errores de interpretación tecnológica y la baja concreción reducen la viabilidad y la trazabilidad del conjunto.

#### Cobertura del Anexo II

De los 85 proyectos, **12 presentan desarrollo suficiente, 73 desarrollo insuficiente** y 0 no incluyen una solución concreta. La cobertura nominal es completa porque los 85 proyectos están presentes; la cobertura efectiva es reducida porque solo 12 alcanzan un desarrollo suficiente. Las carencias se repiten en Servicios Transversales, Aulas Virtuales, Mediateca, COR, WordPress Multisite, los servicios unitarios, los sistemas complementarios y Wekan; Cloud y parte de Videoconferencia presentan un tratamiento relativamente más consistente. El recuento sirve para localizar el contraste y no determina por sí solo el nivel.

#### Fortalezas y aportaciones de valor añadido

Como elementos positivos se reconocen la cobertura formal del alcance, la identificación de numerosos sistemas, la referencia a Métrica v3 y cierto desarrollo en cloud, videoconferencia, seguridad e infraestructura. Estos elementos permiten una valoración parcial, pero no acreditan por sí solos mejoras verificables sobre los requisitos base.

#### Carencias, errores y riesgos recurrentes

Se repiten la falta de detalle técnico, la ausencia de arquitecturas específicas y de trazabilidad, la escasez de métricas y pruebas, y errores acreditados como la oposición entre la ejecución síncrona propuesta y la generación asíncrona exigida en AV11.

### Análisis por bloques funcionales del Anexo II

La exposición se agrupa por bloques cuando la memoria aplica un enfoque común, manteniendo la clasificación individual de los 85 proyectos en el anexo. Cada bloque distingue requisito, evidencia, fortalezas, carencias y valoración cualitativa.

#### Bloque de servicios transversales (TRA)

**Proyectos incluidos:** TRA1 a TRA8.

- **Consideración general del bloque**

El bloque exige resolver identidad, sincronización, interoperabilidad, seguridad y servicios comunes. TRA3, TRA5 y TRA6 alcanzan desarrollo suficiente; los restantes códigos presentan un desarrollo incompleto.

##### TRA1 a TRA8 — Servicios transversales

- **Requisito y alcance**

El alcance comprende identidad, sincronización, interoperabilidad, seguridad y servicios comunes, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

- **Análisis de la propuesta**

El contraste individual recogido en el anexo identifica 3 proyectos con desarrollo suficiente, 5 con desarrollo insuficiente y 0 sin solución concreta. TRA3, TRA5 y TRA6 aportan contenido evaluable; las carencias de los restantes códigos se refieren a su grado de desarrollo y verificabilidad.

- **Fortalezas y valor añadido**

Se reconoce contenido evaluable en 3 proyectos, que permite asignar valor parcial sin extenderlo a los proyectos no desarrollados.

- **Carencias, omisiones, errores o riesgos**

5 proyectos presentan desarrollo genérico o incompleto; 2 contienen errores técnicos relevantes. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

- **Valoración cualitativa**

**BAJA**: El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque TRA

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. El contenido evaluable de TRA3, TRA5 y TRA6 aporta valor parcial, pero el desarrollo incompleto de cinco códigos impide alcanzar el nivel siguiente. El recuento solo apoya esta conclusión cualitativa.

#### Bloque de Aulas Virtuales (AV — Moodle)

**Proyectos incluidos:** AV1 a AV21.

- **Consideración general del bloque**

El bloque exige resolver evolución de Moodle, integraciones, rendimiento, seguridad, escalabilidad y continuidad. AV1 resulta evaluable, pero AV4 identifica una base de datos incorrecta y AV11 plantea de forma inadecuada procesos de IA síncronos; los demás proyectos son mayoritariamente genéricos.

##### AV1 a AV21 — Aulas Virtuales

**Requisito y alcance.** El alcance comprende evolución de Moodle, integraciones, rendimiento, seguridad, escalabilidad y continuidad, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 1 proyecto con desarrollo suficiente, 20 con desarrollo insuficiente y 0 sin solución concreta. AV1 resulta evaluable, pero AV4 identifica una base de datos incorrecta y AV11 plantea de forma inadecuada procesos de IA síncronos; los demás proyectos son mayoritariamente genéricos.

**Fortalezas y valor añadido.** Se reconoce contenido evaluable en 1 proyecto, que permite asignar valor parcial sin extenderlo a los proyectos no desarrollados.

**Carencias, omisiones, errores o riesgos.** 20 proyectos presentan desarrollo genérico o incompleto; 2 contienen errores técnicos relevantes. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**BAJA.** El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Integración, rendimiento, escalabilidad y continuidad del servicio

Las relaciones entre componentes, el comportamiento bajo carga, la monitorización y la recuperación se describen de forma parcial; las carencias y errores identificados impiden validar de manera uniforme la integración del bloque.

##### Conclusión del bloque AV

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. AV1 resulta evaluable, pero AV4 identifica una base de datos incorrecta y AV11 plantea de forma inadecuada procesos de IA síncronos; los demás proyectos son mayoritariamente genéricos.

#### Bloque de Mediateca (MED)

**Proyectos incluidos:** MED1 a MED11.

- **Consideración general del bloque**

El bloque exige resolver procesamiento multimedia, subtitulado, búsqueda, almacenamiento, distribución e integración. MED1 contiene un error relativo a la base de datos y MED2 omite una funcionalidad crítica; el resto carece de detalle suficiente.

##### MED1 a MED11 — Mediateca

**Requisito y alcance.** El alcance comprende procesamiento multimedia, subtitulado, búsqueda, almacenamiento, distribución e integración, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 0 proyectos con desarrollo suficiente, 11 con desarrollo insuficiente y 0 sin solución concreta. MED1 contiene un error relativo a la base de datos y MED2 omite una funcionalidad crítica; el resto carece de detalle suficiente.

**Fortalezas y valor añadido.** No se acreditan fortalezas técnicas suficientes ni mejoras verificables que excedan las obligaciones de base.

**Carencias, omisiones, errores o riesgos.** 11 proyectos presentan desarrollo genérico o incompleto; 2 contienen errores técnicos relevantes. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**BAJA.** El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Arquitectura, procesamiento multimedia e integración

Las relaciones entre componentes, el comportamiento bajo carga, la monitorización y la recuperación se describen de forma parcial; las carencias y errores identificados impiden validar de manera uniforme la integración del bloque.

##### Conclusión del bloque MED

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. MED1 contiene un error relativo a la base de datos y MED2 omite una funcionalidad crítica; el resto carece de detalle suficiente.

#### Bloque de Correo Web (COR)

**Proyectos incluidos:** COR1 a COR4.

- **Consideración general del bloque**

El bloque exige resolver evolución del correo, funciones de inteligencia artificial, seguridad e integración. COR1 presenta contenido evaluable, mientras COR2 a COR4 no se adaptan correctamente al entorno basado en xAI modificado y proponen desarrollos innecesarios desde cero.

##### COR1 a COR4 — Correo Web

**Requisito y alcance.** El alcance comprende evolución del correo, funciones de inteligencia artificial, seguridad e integración, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 1 proyecto con desarrollo suficiente, 3 con desarrollo insuficiente y 0 sin solución concreta. COR1 presenta contenido evaluable, mientras COR2 a COR4 no se adaptan correctamente al entorno basado en xAI modificado y proponen desarrollos innecesarios desde cero.

**Fortalezas y valor añadido.** Se reconoce contenido evaluable en 1 proyecto, que permite asignar valor parcial sin extenderlo a los proyectos no desarrollados.

**Carencias, omisiones, errores o riesgos.** 3 proyectos presentan desarrollo genérico o incompleto; 3 contienen errores técnicos relevantes. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**BAJA.** El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque COR

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. COR1 presenta contenido evaluable, mientras COR2 a COR4 no se adaptan correctamente al entorno basado en xAI modificado y proponen desarrollos innecesarios desde cero.

#### Bloque Cloud (CLO — Nextcloud y Collabora)

**Proyectos incluidos:** CLO1 y CLO2.

- **Consideración general del bloque**

El bloque exige resolver almacenamiento, sincronización, edición colaborativa, seguridad y rendimiento. CLO1 y CLO2 son los únicos proyectos del bloque considerados suficientemente desarrollados, aunque no acreditan mejoras adicionales.

##### CLO1 y CLO2 — Cloud

**Requisito y alcance.** El alcance comprende almacenamiento, sincronización, edición colaborativa, seguridad y rendimiento, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 2 proyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 sin solución concreta. CLO1 y CLO2 son los únicos proyectos del bloque considerados suficientemente desarrollados, aunque no acreditan mejoras adicionales.

**Fortalezas y valor añadido.** Se reconoce contenido evaluable en 2 proyectos, que permite asignar valor parcial sin extenderlo a los proyectos no desarrollados.

**Carencias, omisiones, errores o riesgos.** No se observan omisiones ni errores relevantes; las limitaciones se circunscriben al grado de detalle de algunos elementos.

**MEDIA.** El nivel **MEDIA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque CLO

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **MEDIA**. CLO1 y CLO2 son los únicos proyectos del bloque considerados suficientemente desarrollados, aunque no acreditan mejoras adicionales.

#### Bloque WordPress Multisite (WPM)

**Proyectos incluidos:** WPM1 a WPM5.

- **Consideración general del bloque**

El bloque exige resolver mantenimiento, licencias, protección perimetral, antiabuso y autenticación. Los cinco proyectos se incluyen, pero sin el detalle necesario sobre operación, licencias, protección, antiabuso y autenticación.

##### WPM1 a WPM5 — WordPress Multisite

**Requisito y alcance.** El alcance comprende mantenimiento, licencias, protección perimetral, antiabuso y autenticación, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 0 proyectos con desarrollo suficiente, 5 con desarrollo insuficiente y 0 sin solución concreta. Los cinco proyectos se incluyen, pero sin el detalle necesario sobre operación, licencias, protección, antiabuso y autenticación.

**Fortalezas y valor añadido.** No se acreditan fortalezas técnicas suficientes ni mejoras verificables que excedan las obligaciones de base.

**Carencias, omisiones, errores o riesgos.** 5 proyectos presentan desarrollo genérico o incompleto. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**BAJA.** El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque WPM

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. Los cinco proyectos se incluyen, pero sin el detalle necesario sobre operación, licencias, protección, antiabuso y autenticación.

#### Bloque de Vídeo y Videoconferencia (VID)

**Proyectos incluidos:** VID1 a VID4.

- **Consideración general del bloque**

El bloque exige resolver integración educativa, concurrencia, calidad, grabaciones y continuidad. VID1 y VID2 contienen una respuesta evaluable; VID3 y VID4 quedan en un tratamiento insuficiente sobre grabaciones y eventos de alta concurrencia.

##### VID1 a VID4 — Vídeo y Videoconferencia

**Requisito y alcance.** El alcance comprende integración educativa, concurrencia, calidad, grabaciones y continuidad, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 2 proyectos con desarrollo suficiente, 2 con desarrollo insuficiente y 0 sin solución concreta. VID1 y VID2 contienen una respuesta evaluable; VID3 y VID4 quedan en un tratamiento insuficiente sobre grabaciones y eventos de alta concurrencia.

**Fortalezas y valor añadido.** Se reconoce contenido evaluable en 2 proyectos, que permite asignar valor parcial sin extenderlo a los proyectos no desarrollados.

**Carencias, omisiones, errores o riesgos.** 2 proyectos presentan desarrollo genérico o incompleto. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**MEDIA.** El nivel **MEDIA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque VID

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **MEDIA**. VID1 y VID2 contienen una respuesta evaluable; VID3 y VID4 quedan en un tratamiento insuficiente sobre grabaciones y eventos de alta concurrencia.

#### Servicios unitarios

**Proyectos incluidos:** EMP1, LDAP, EXE, FOR1, BUS1 y ANI1.

##### Consideración general del conjunto

El bloque exige resolver los requisitos específicos y diferenciados de los seis servicios unitarios. EMP1 y EXE presentan desarrollo suficiente; LDAP reproduce el error de interpretación del directorio y FOR1, BUS1 y ANI1 son genéricos.

##### EMP1, LDAP, EXE, FOR1, BUS1 y ANI1 — Servicios unitarios

**Requisito y alcance.** El alcance comprende los requisitos específicos y diferenciados de los seis servicios unitarios, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 2 proyectos con desarrollo suficiente, 4 con desarrollo insuficiente y 0 sin solución concreta. EMP1 y EXE presentan desarrollo suficiente; LDAP reproduce el error de interpretación del directorio y FOR1, BUS1 y ANI1 son genéricos.

**Fortalezas y valor añadido.** Se reconoce contenido evaluable en 2 proyectos, que permite asignar valor parcial sin extenderlo a los proyectos no desarrollados.

**Carencias, omisiones, errores o riesgos.** 4 proyectos presentan desarrollo genérico o incompleto; 1 contiene errores técnicos relevantes. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**BAJA.** El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión de los servicios unitarios

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. EMP1 y EXE presentan desarrollo suficiente; LDAP reproduce el error de interpretación del directorio y FOR1, BUS1 y ANI1 son genéricos.

#### Sistemas y servicios complementarios

**Proyectos incluidos:** SYN, CAU, EDU, BAN, DTIC, SEG, ALB, AVI, FOR, BOL, AYU, POR, WES, IFZ, MAX, GES, USO, MAM, EML y ABI.

##### Consideración general del conjunto

El bloque exige resolver integración, seguridad, operación, accesibilidad, comunicación y analítica de los sistemas complementarios. Solo IFZ alcanza desarrollo suficiente. SYN, BAN y AVI contienen errores tecnológicos y los restantes sistemas reciben respuestas genéricas.

##### SYN a ABI — Sistemas y servicios complementarios

**Requisito y alcance.** El alcance comprende integración, seguridad, operación, accesibilidad, comunicación y analítica de los sistemas complementarios, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 1 proyecto con desarrollo suficiente, 19 con desarrollo insuficiente y 0 sin solución concreta. Solo IFZ alcanza desarrollo suficiente. SYN, BAN y AVI contienen errores tecnológicos y los restantes sistemas reciben respuestas genéricas.

**Fortalezas y valor añadido.** Se reconoce contenido evaluable en 1 proyecto, que permite asignar valor parcial sin extenderlo a los proyectos no desarrollados.

**Carencias, omisiones, errores o riesgos.** 19 proyectos presentan desarrollo genérico o incompleto; 3 contienen errores técnicos relevantes. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**BAJA.** El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión de los sistemas complementarios

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. Solo IFZ alcanza desarrollo suficiente. SYN, BAN y AVI contienen errores tecnológicos y los restantes sistemas reciben respuestas genéricas.

#### Bloque Wekan (WEK)

**Proyectos incluidos:** WEK1 a WEK4.

- **Consideración general del bloque**

El bloque exige resolver mantenimiento, actualización, despliegue, respaldo y evolución de Wekan. Los cuatro subproyectos se mencionan sin soluciones individualizadas ni mecanismos de implementación verificables.

##### WEK1 a WEK4 — Wekan

**Requisito y alcance.** El alcance comprende mantenimiento, actualización, despliegue, respaldo y evolución de Wekan, con soluciones diferenciadas, integraciones, entregables y mecanismos de validación trazables para cada código.

**Análisis de la propuesta.** El contraste individual recogido en el anexo identifica 0 proyectos con desarrollo suficiente, 4 con desarrollo insuficiente y 0 sin solución concreta. Los cuatro subproyectos se mencionan sin soluciones individualizadas ni mecanismos de implementación verificables.

**Fortalezas y valor añadido.** No se acreditan fortalezas técnicas suficientes ni mejoras verificables que excedan las obligaciones de base.

**Carencias, omisiones, errores o riesgos.** 4 proyectos presentan desarrollo genérico o incompleto. Estas limitaciones reducen la concreción, viabilidad o verificabilidad del bloque.

**BAJA.** El nivel **BAJA** refleja la relación entre la cobertura efectiva, la profundidad técnica, las mejoras y las carencias acreditadas para el bloque.

##### Conclusión del bloque WEK

La clasificación del anexo y las evidencias anteriores sitúan el bloque en un nivel **BAJA**. Los cuatro subproyectos se mencionan sin soluciones individualizadas ni mecanismos de implementación verificables.

### Conclusión del análisis detallado

El patrón dominante es la inclusión formal de los proyectos con desarrollo insuficiente. Las carencias se repiten en TRA, AV, MED, COR, WPM, los servicios unitarios, los sistemas complementarios y WEK; CLO y parte de VID presentan un tratamiento relativamente más consistente. Se identifican errores relevantes en identidad, calendarios, bases de datos, procesamiento asíncrono, correo y varios sistemas complementarios. Por su reiteración, no son incidencias aisladas, sino deficiencias estructurales. Se repiten la falta de detalle técnico, la ausencia de arquitecturas específicas y de trazabilidad, la escasez de métricas y pruebas, y errores como la contradicción de AV11: el Anexo II exige generación asíncrona y el apartado II.1.2.11 de la oferta afirma que se ejecutará de forma síncrona.

## EVALUACIÓN DE LA SOLUCIÓN TÉCNICA OFERTADA

### Fundamentación de la valoración

La valoración de la solución técnica se basa en el análisis pormenorizado de los proyectos y subproyectos anteriores. La puntuación no responde a la mera presencia formal de contenidos, sino a su **calidad, concreción, coherencia, adecuación, viabilidad y verificabilidad**, así como al alcance real de las fortalezas y carencias detectadas.

### Arquitectura planteada en los distintos subproyectos — máximo 2 puntos

La propuesta identifica componentes y sistemas, pero no define de manera completa sus relaciones, flujos, despliegues ni mecanismos de resiliencia. El contraste con la memoria confirma una cobertura arquitectónica incompleta y con errores de adaptación al entorno, rasgos que corresponden al descriptor BAJA.

**Nivel cualitativo:** BAJA
**Puntuación:** 0,50 sobre 2,00

### Grado de comprensión de los requisitos planteados — máximo 2 puntos

La comprensión es parcial: se reconoce el alcance general y existe contenido valorable, pero se mantienen errores acreditados como la contradicción síncrono/asíncrono de AV11 y desarrollos insuficientes en identidad, bases de datos, correo y varios sistemas complementarios. Estos rasgos permiten MEDIA, pero impiden alcanzar ALTA.

**Nivel cualitativo:** MEDIA
**Puntuación:** 1,00 sobre 2,00

### Viabilidad técnica y operativa del proyecto — máximo 1 punto

La ausencia de procedimientos de implantación, dependencias y mecanismos de validación, unida a los errores conceptuales detectados, genera dudas relevantes sobre la ejecución real.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,40 sobre 1,00

### Metodología de trabajo aplicada — máximo 1 punto

Métrica v3 constituye una base teórica adecuada, pero no se concreta su aplicación al contrato mediante roles, herramientas, entregables y validaciones suficientemente definidos.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,40 sobre 1,00

### Rendimiento previsible de las soluciones — máximo 1 punto

El rendimiento se trata de forma genérica y sin métricas cuantificables, escenarios de carga ni criterios de aceptación específicos para los sistemas críticos.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,40 sobre 1,00

### Satisfacción de los requisitos del Anexo II — máximo 8 puntos

La oferta aporta contenido suficientemente desarrollado en 12 proyectos distribuidos entre los bloques TRA, AV, COR, CLO, VID y varios servicios unitarios o complementarios. Esta evidencia positiva permite superar la parte inferior de MEDIA. No alcanza el nivel siguiente porque las carencias acreditadas afectan de forma extensa a integraciones, procesamiento, correo, sistemas complementarios y mecanismos de validación relevantes. El recuento de 12 proyectos suficientes y 73 insuficientes es solo un dato auxiliar y no una fórmula de puntuación.

**Nivel cualitativo:** MEDIA
**Puntuación:** 2,40 sobre 8,00

### Resultado global de la solución técnica

| **Subcriterio**                | **Máximo** | **Nivel** | **Puntuación** |
| ------------------------------ | ---------: | --------- | -------------: |
| Arquitectura                   |       2,00 | BAJA      |           0,50 |
| Comprensión de los requisitos  |       2,00 | MEDIA     |           1,00 |
| Viabilidad                     |       1,00 | MEDIA     |           0,40 |
| Metodología                    |       1,00 | MEDIA     |           0,40 |
| Rendimiento                    |       1,00 | MEDIA     |           0,40 |
| Satisfacción de los requisitos |       8,00 | MEDIA     |           2,40 |
| **TOTAL SOLUCIÓN TÉCNICA**     |  **15,00** |           |       **5,10** |

## EVALUACIÓN DE LA PLANIFICACIÓN DEL SERVICIO

### Consideraciones generales sobre la planificación

La planificación debe constituir una **herramienta real de gestión del servicio**. Su valoración atiende a los rasgos publicados: correspondencia con los proyectos y entregables del Anexo II, secuencia y duración de las tareas, dependencias, hitos, objetivos y adaptación al calendario del servicio, junto con los mecanismos de riesgo, contingencia, calidad y trazabilidad.

### Calendario de los trabajos a desarrollar — máximo 11 puntos

El cronograma permite identificar bloques de tareas y su distribución mensual entre septiembre de 2026 y agosto de 2027; por ello existe una planificación básica evaluable y corresponde el nivel MEDIA. No alcanza ALTA porque la representación no permite reconstruir de forma inequívoca la duración de cada tarea, sus relaciones ni su conexión con hitos y objetivos. Se sitúa en la parte baja de MEDIA por esa combinación de cobertura temporal legible y limitada verificabilidad.

**Nivel cualitativo:** MEDIA
**Puntuación:** 3,75 sobre 11,00

### Análisis de riesgos del proyecto — máximo 1 punto

Existe una base conceptual con identificación de riesgos, pero faltan mayor vinculación a proyectos, responsables, indicadores y seguimiento operativo.

**Nivel cualitativo:** ALTA
**Puntuación:** 0,55 sobre 1,00

### Plan de gestión de contingencias — máximo 1 punto

El planteamiento es reconocible, aunque no concreta de forma suficiente activadores, secuencias, recursos, tiempos objetivo, pruebas y retorno a la normalidad.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,40 sobre 1,00

### Plan de gestión de la calidad del servicio — máximo 1 punto

Se citan estándares y mejora continua, pero faltan métricas, niveles de servicio y una relación verificable con los entregables y criterios de aceptación.

**Nivel cualitativo:** ALTA
**Puntuación:** 0,60 sobre 1,00

### Trazabilidad del servicio — máximo 1 punto

No se establece una matriz operativa completa entre requisitos, tareas, responsables, entregables, evidencias y validaciones.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,30 sobre 1,00

### Resultado global de la planificación

| **Subcriterio**                     | **Máximo** | **Nivel** | **Puntuación** |
| ----------------------------------- | ---------: | --------- | -------------: |
| Calendario y planificación temporal |      11,00 | MEDIA     |           3,75 |
| Análisis de riesgos                 |       1,00 | ALTA      |           0,55 |
| Plan de contingencias               |       1,00 | MEDIA     |           0,40 |
| Plan de calidad                     |       1,00 | ALTA      |           0,60 |
| Trazabilidad                        |       1,00 | MEDIA     |           0,30 |
| **TOTAL PLANIFICACIÓN**             |  **15,00** |           |       **5,60** |

## RESULTADO FINAL CONSOLIDADO

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                    5,10 |
| Planificación del servicio |                 15,00 |                    5,60 |
| **PUNTUACIÓN FINAL**       |             **30,00** |               **10,70** |

### Interpretación de la puntuación

La puntuación consolidada de 10,70 puntos refleja de forma proporcionada la cobertura, profundidad, viabilidad y planificación acreditadas. La oferta obtiene 10,70 puntos sobre 30 y no alcanza el umbral mínimo de 15 puntos; procede proponer su exclusión por aplicación aritmética del umbral tras la valoración motivada.

## CONCLUSIONES FINALES Y PROPUESTA

### Conclusiones globales de la evaluación técnica

La propuesta presenta una estructura formal correcta y una cobertura nominal amplia del ecosistema EducaMadrid, pero el desarrollo efectivo es mayoritariamente descriptivo. Faltan arquitecturas específicas, flujos de integración, métricas, criterios de aceptación y mecanismos de validación suficientes. Se reconocen contenidos evaluables en algunos proyectos y una base metodológica apoyada en Métrica v3, aunque su aplicación práctica es limitada. Los errores acreditados y la baja concreción reducen la viabilidad y la trazabilidad del conjunto. La oferta obtiene 10,70 puntos sobre 30 y no alcanza el umbral mínimo de 15 puntos.

### Conclusiones sobre la solución técnica

El patrón dominante es la inclusión formal de los proyectos con desarrollo insuficiente. Las carencias se repiten en TRA, AV, MED, COR, WPM, los servicios unitarios, los sistemas complementarios y WEK; CLO y parte de VID presentan un tratamiento relativamente más consistente. Se identifican errores relevantes en identidad, calendarios, bases de datos, procesamiento asíncrono, correo y varios sistemas complementarios. Por su reiteración, no son incidencias aisladas, sino deficiencias estructurales. Se repiten la falta de detalle técnico, la ausencia de arquitecturas específicas y de trazabilidad, la escasez de métricas y pruebas, y errores como la contradicción concreta de AV11 entre la generación asíncrona exigida y la ejecución síncrona propuesta.

### Conclusiones sobre la planificación del servicio

El cronograma ofrece una visión mensual básica, pero no permite verificar de forma suficiente las duraciones, relaciones entre tareas e hitos. Existe una base conceptual con identificación de riesgos, pero faltan mayor vinculación a proyectos, responsables, indicadores y seguimiento operativo. El planteamiento de contingencias es reconocible, aunque no concreta de forma suficiente activadores, secuencias, tiempos objetivo, pruebas y retorno a la normalidad. Se citan estándares y mejora continua, pero faltan métricas, niveles de servicio y una relación verificable con los entregables y criterios de aceptación. No se establece una matriz operativa completa entre requisitos, tareas, responsables, entregables, evidencias y validaciones.

### Justificación de la valoración

Las puntuaciones parciales trasladan el nivel efectivamente acreditado en cada subcriterio, sin compensar omisiones estructurales con fortalezas puntuales. El resultado de 5,10 puntos en solución y 5,60 en planificación es coherente con el análisis y con el total de 10,70 puntos.

### Aplicación del umbral mínimo y propuesta final

La propuesta de **empresa_n** obtiene una puntuación de **10,70 puntos sobre 30** en los criterios sujetos a juicio de valor.

El umbral mínimo exigido para continuar en el procedimiento es de **15 puntos sobre 30**. Por tanto, la oferta **NO ALCANZA** el umbral.


En consecuencia, una vez motivada la puntuación mediante juicio técnico, procede proponer la **exclusión de la oferta del procedimiento** por aplicación del umbral. Esta conclusión no constituye una apreciación sobre la solvencia del licitador ni añade un incumplimiento técnico distinto de los expresamente identificados.

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

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| TRA1         | INSUFICIENTE            | NO     | SÍ        | LDAP mal interpretado.            |
| TRA2         | INSUFICIENTE            | NO     | NO        | desarrollo incompleto.            |
| TRA3         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| TRA4         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| TRA5         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| TRA6         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| TRA7         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| TRA8         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

#### Aulas Virtuales (AV)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| AV1          | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| AV2          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV3          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV4          | INSUFICIENTE            | NO     | SÍ        | MySQL vs PostgreSQL               |
| AV5          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV6          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV7          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV8          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV9          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV10         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV11         | INSUFICIENTE            | NO     | SÍ        | procesos IA síncronos incorrectos |
| AV12         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV13         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV14         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV15         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV16         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV17         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV18         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV19         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV20         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AV21         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

#### Mediateca (MED)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| MED1         | INSUFICIENTE            | NO     | SÍ        | error BBDD                        |
| MED2         | INSUFICIENTE            | NO     | SÍ        | omisión funcional crítica         |
| MED3         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED4         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED5         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED6         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED7         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED8         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED9         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED10        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MED11        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

#### Correo Web (COR)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                          |
|--------------|-------------------------|--------|-----------|------------------------------------------------|
| COR1         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.                          |
| COR2         | INSUFICIENTE            | NO     | SÍ        | propuesta de desarrollo desde cero innecesario |
| COR3         | INSUFICIENTE            | NO     | SÍ        | propuesta de desarrollo desde cero innecesario |
| COR4         | INSUFICIENTE            | NO     | SÍ        | propuesta de desarrollo desde cero innecesario |

#### Cloud (CLO)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve** |
| ------------ | ----------------------- | ------ | --------- | --------------------- |
| CLO1         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable. |
| CLO2         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable. |

#### WordPress Multisite (WPM)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| WPM1         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WPM2         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WPM3         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WPM4         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WPM5         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

#### Vídeo y Videoconferencia (VID)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| VID1         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| VID2         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| VID3         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| VID4         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

#### Servicios unitarios

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| EMP1         | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| LDAP         | INSUFICIENTE            | NO     | SÍ        | LDAP plano mal interpretado       |
| EXE          | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| FOR1         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| BUS1         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| ANI1         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

#### Sistemas y servicios complementarios

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| SYN          | INSUFICIENTE            | NO     | SÍ        | modelo de datos incorrecto        |
| CAU          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| EDU          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| BAN          | INSUFICIENTE            | NO     | SÍ        | tecnología Java incorrecta        |
| DTIC         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| SEG          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| ALB          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AVI          | INSUFICIENTE            | NO     | SÍ        | tecnología incorrecta             |
| FOR          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| BOL          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| AYU          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| POR          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WES          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| IFZ          | SUFICIENTE              | NO     | NO        | Desarrollo evaluable.             |
| MAX          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| GES          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| USO          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| MAM          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| EML          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| ABI          | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

#### Wekan (WEK)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| ------------ | ----------------------- | ------ | --------- | --------------------------------- |
| WEK1         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WEK2         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WEK3         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |
| WEK4         | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o incompleto. |

### Resumen cuantitativo del anexo

#### Grado de desarrollo

| **Clasificación**                    | **Número de proyectos** | **Porcentaje** |
| ------------------------------------ | ----------------------: | -------------: |
| No incluidos                         |                       0 |         0,00 % |
| Desarrollo insuficiente o deficiente |                      73 |        85,88 % |
| Desarrollo suficiente                |                      12 |        14,12 % |
| **TOTAL DE PROYECTOS**               |                  **85** |   **100,00 %** |

#### Indicadores adicionales

Los indicadores adicionales no son excluyentes entre sí ni respecto del grado de desarrollo, por lo que sus porcentajes no tienen que sumar el 100 %.

| **Indicador**                                  | **Número de proyectos** | **Porcentaje sobre el total** |
| ---------------------------------------------- | ----------------------: | ----------------------------: |
| Con errores técnicos relevantes                |                      12 |                       14,12 % |
| Con propuesta de mejora sin valor añadido real |                       0 |                        0,00 % |
| Con propuesta de mejora con valor añadido real |                       0 |                        0,00 % |

### Conclusión del anexo

La clasificación muestra 12 proyectos con desarrollo suficiente, 73 insuficientes y 0 sin solución concreta. Se identifican 12 proyectos con errores relevantes y 0 con valor añadido verificable. El patrón dominante es la inclusión formal de los proyectos con desarrollo insuficiente. Las carencias se repiten en TRA, AV, MED, COR, WPM, los servicios unitarios, los sistemas complementarios y WEK; CLO y parte de VID presentan un tratamiento relativamente más consistente. Se identifican errores relevantes en identidad, calendarios, bases de datos, procesamiento asíncrono, correo y varios sistemas complementarios.El anexo aporta trazabilidad, mientras que la puntuación deriva de la valoración cualitativa de la relevancia y profundidad del contenido en todos los subcriterios, no de estos recuentos.
