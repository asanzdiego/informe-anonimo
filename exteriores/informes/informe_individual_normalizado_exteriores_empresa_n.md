# INFORME DE VALORACIÓN TÉCNICA INDIVIDUAL

- **Contrato:** Servicios de mantenimiento y soporte para proyectos exteriores alojados en la plataforma EducaMadrid (BAC01_2026)
- **Licitador:** empresa_n

## RESUMEN EJECUTIVO

### Objeto del informe

El presente informe tiene por objeto realizar la **valoración técnica de la propuesta presentada por empresa_n** en el procedimiento basado en el **Sistema Dinámico de Adquisición SDA 26/2021**, relativo a los **Servicios de mantenimiento y soporte para proyectos exteriores alojados en la plataforma EducaMadrid (BAC01_2026)**.

El informe determina la puntuación correspondiente a los criterios sujetos a juicio de valor, comprueba el cumplimiento del **umbral mínimo de 15 puntos sobre 30** y formula la propuesta de continuación o exclusión que procede para la oferta.

### Metodología de valoración

La evaluación se ha estructurado en dos niveles complementarios. En primer lugar, se ha realizado un análisis técnico detallado de los proyectos y subproyectos incluidos en el Anexo II del Documento de Invitación, examinando el grado de desarrollo, adecuación y verificabilidad de las soluciones propuestas. En segundo lugar, los resultados de dicho análisis se han trasladado al esquema de valoración previsto en el apartado 7.2 del Documento de Invitación, asignando las puntuaciones correspondientes en función del nivel real de adecuación observado.

Este enfoque garantiza la trazabilidad entre **los requisitos definidos, las evidencias contenidas en la memoria, el análisis técnico efectuado y la puntuación final asignada**.

### Síntesis técnica de la propuesta

La propuesta presenta una cobertura documental amplia y una comprensión general razonable del alcance, pero en numerosos subproyectos sustituye la solución técnica concreta por descripciones funcionales o secuencias genéricas de análisis, revisión y validación. La arquitectura, las herramientas, las métricas, los criterios de aceptación y los mecanismos de implantación aparecen desarrollados de forma desigual. Se reconocen fortalezas puntuales en IFP, determinadas actuaciones de sistemas externos y seguridad, aunque no compensan la baja concreción recurrente ni las omisiones identificadas.

### Principales conclusiones del análisis

La clasificación más frecuente sigue siendo el desarrollo insuficiente o genérico: afecta a 26 subproyectos y, junto con los 2 no incluidos, suma 28 de los 53 códigos. Las carencias se repiten en ELIF, Moodle Misc, Dinámicas, integración, sistemas externos y desarrollo seguro; IFP y otros proyectos concretos alcanzan un desarrollo suficiente. La ausencia de ESIS11 y ESIS14, junto con la limitada planificación del segundo año contractual, constituye una deficiencia relevante y no un hecho aislado.

### Resultado de la valoración

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                    6,65 |
| Planificación del servicio |                 15,00 |                    3,05 |
| **TOTAL**                  |             **30,00** |                **9,70** |

### Conclusión del resumen ejecutivo

La oferta presenta una comprensión general aceptable y una cobertura documental extensa, pero no acredita de forma homogénea cómo se ejecutarán, validarán y controlarán numerosas actuaciones. Las deficiencias de concreción técnica se acumulan con una planificación incompleta para el periodo contractual, por lo que la calidad global resulta insuficiente. La oferta obtiene **9,70 puntos sobre 30** y no alcanza el umbral mínimo de 15 puntos.

## INTRODUCCIÓN

### Alcance del informe

El presente informe evalúa la memoria técnica presentada por **empresa_n** para la prestación de los **Servicios de mantenimiento y soporte para proyectos exteriores alojados en la plataforma EducaMadrid (BAC01_2026)**. El análisis comprende tanto la **solución técnica ofertada** como la **planificación del servicio**, de acuerdo con los criterios sujetos a juicio de valor establecidos en el apartado 7.2 del Documento de Invitación.

La evaluación toma como referencia los proyectos, subproyectos, actuaciones y entregables definidos en el Anexo II, y atiende exclusivamente al contenido efectivamente desarrollado en la documentación presentada.

### Marco normativo

El presente informe se elabora en el marco del procedimiento de adjudicación correspondiente a **Sistema Dinámico de Adquisición SDA 26/2021**. El procedimiento se rige por lo dispuesto en la **Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público** (en adelante, LCSP), por el Pliego de Cláusulas Administrativas Particulares y por las condiciones específicas establecidas en el Documento de Invitación y demás documentación reguladora del expediente.

La valoración técnica se fundamenta en los **criterios de adjudicación sujetos a juicio de valor definidos en el apartado 7.2 del Documento de Invitación**, cuya finalidad es evaluar la calidad de la propuesta desde una perspectiva integral que contemple tanto la **adecuación de la solución técnica ofertada** como la **viabilidad organizativa y temporal de su ejecución**.

De conformidad con el **artículo 145 de la LCSP**, los criterios de adjudicación deben permitir determinar la mejor relación calidad-precio y aplicarse de forma objetiva, transparente y no discriminatoria. La evaluación se realiza, por tanto, con arreglo a los principios de **igualdad de trato, objetividad, transparencia, proporcionalidad y trazabilidad**, aplicando a todas las ofertas un mismo marco metodológico y sin incorporar elementos externos a la documentación presentada por los licitadores.

Asimismo, el **artículo 146.3 de la LCSP** permite establecer umbrales mínimos en los criterios cualitativos sujetos a juicio de valor. Conforme al Documento de Invitación, las ofertas deben alcanzar un **nivel mínimo de calidad técnica equivalente al cincuenta por ciento de la puntuación máxima asignable a estos criterios** para continuar en el procedimiento.

La aplicación de este umbral no constituye una decisión discrecional: una vez constatado su incumplimiento, la oferta afectada no puede continuar en las fases posteriores del procedimiento. La valoración debe permitir **comprobar de forma clara la puntuación obtenida y motivar la correspondiente propuesta de admisión o exclusión**.

La evaluación se ajusta igualmente al **principio de evaluabilidad**, conforme al cual únicamente pueden valorarse los elementos de la oferta que estén suficientemente desarrollados y que permitan su comprobación objetiva. Las declaraciones genéricas, las capacidades presumidas, las referencias no desarrolladas o las soluciones futuras no descritas en la memoria no pueden suplirse mediante inferencias del órgano evaluador.

### Contexto técnico del servicio

Los proyectos exteriores son aplicaciones y servicios que, sin constituir el núcleo principal de EducaMadrid, se alojan en su infraestructura o se integran con componentes corporativos de la plataforma. El alcance reúne tecnologías, arquitecturas, responsables funcionales y niveles de criticidad heterogéneos, e incluye actuaciones sobre:

- páginas web Liferay y su integración con Scribe CMS;

- la plataforma Drupal de Innovación y Formación del Profesorado;

- entornos MoodleMisc y sus integraciones;

- aplicaciones heredadas del entorno Dinámicas y su espacio de transferencia de ficheros;

- aplicaciones, plugins, scripts y adaptaciones front-end para integración con EducaMadrid;

- infraestructura, software base, bases de datos, identidades, aprovisionamiento, monitorización, continuidad y seguridad de sistemas externos;

- seguridad de aplicaciones web, desarrollo seguro y gestión del programa de Bug Bounty.

La ejecución debe coordinarse con los responsables de los proyectos exteriores y con los servicios corporativos de EducaMadrid, manteniendo la compatibilidad, disponibilidad, seguridad, trazabilidad y continuidad del entorno. Por ello, no basta con enumerar actuaciones: la oferta debe definir soluciones concretas, técnicamente viables y adaptadas a las dependencias reales de cada subproyecto.

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

La memoria sigue de forma amplia los bloques del Anexo II y mantiene una línea argumental reconocible, pero la relación entre requisitos, arquitectura, procedimientos, planificación y entregables no se desarrolla de manera uniforme. Existen contenidos duplicados en ESIS y referencias residuales ajenas al texto técnico, además de omisiones concretas que reducen el grado de finalización y revisión del documento.

#### Nivel de desarrollo técnico y grado de concreción

La oferta acredita una comprensión funcional del servicio y cubre formalmente la mayoría de los códigos, pero el desarrollo efectivo permanece con frecuencia en un plano declarativo. La falta de arquitecturas específicas, herramientas, métricas, criterios de aceptación y procedimientos verificables limita la viabilidad demostrada y la satisfacción de los requisitos.

#### Comprensión y adaptación al entorno EducaMadrid

La clasificación más frecuente sigue siendo el desarrollo insuficiente o genérico: afecta a 26 subproyectos y, junto con los 2 no incluidos, suma 28 de los 53 códigos. Las carencias se repiten en ELIF, Moodle Misc, Dinámicas, integración, sistemas externos y desarrollo seguro; IFP y otros proyectos concretos alcanzan un desarrollo suficiente. La ausencia de ESIS11 y ESIS14, junto con la limitada planificación del segundo año contractual, constituye una deficiencia relevante y no un hecho aislado.

#### Arquitectura, integración y requisitos no funcionales

La oferta acredita una comprensión funcional del servicio y cubre formalmente la mayoría de los códigos, pero el desarrollo efectivo permanece con frecuencia en un plano declarativo. La falta de arquitecturas específicas, herramientas, métricas, criterios de aceptación y procedimientos verificables limita la viabilidad demostrada y la satisfacción de los requisitos.

#### Trazabilidad y evaluabilidad

La valoración puede reconstruirse por subproyecto y por criterio, pero la trazabilidad hacia métricas, entregables y criterios de aceptación presenta el grado de madurez descrito en el análisis. La normalización conserva las evidencias y puntuaciones del informe de origen y las ordena conforme a una estructura única.

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

### Consideraciones generales sobre la propuesta

#### Enfoque global de evaluación

La oferta acredita una comprensión funcional del servicio y cubre formalmente la mayoría de los códigos, pero el desarrollo efectivo permanece con frecuencia en un plano declarativo. La falta de arquitecturas específicas, herramientas, métricas, criterios de aceptación y procedimientos verificables limita la viabilidad demostrada y la satisfacción de los requisitos.

#### Cobertura del Anexo II

De los 53 subproyectos del Anexo II, 25 se clasifican con desarrollo suficiente, 26 con desarrollo insuficiente o deficiente y 2 como no incluidos. La clasificación describe la cobertura documental y se interpreta conjuntamente con la calidad, la coherencia, la viabilidad y la verificabilidad de cada solución.

#### Fortalezas y aportaciones de valor añadido

La propuesta presenta una cobertura documental amplia y una comprensión general razonable del alcance, pero en numerosos subproyectos sustituye la solución técnica concreta por descripciones funcionales o secuencias genéricas de análisis, revisión y validación. La arquitectura, las herramientas, las métricas, los criterios de aceptación y los mecanismos de implantación aparecen desarrollados de forma desigual. Se reconocen fortalezas puntuales en IFP, determinadas actuaciones de sistemas externos y seguridad, aunque no compensan la baja concreción recurrente ni las omisiones identificadas.

#### Carencias, errores y riesgos recurrentes

La clasificación más frecuente sigue siendo el desarrollo insuficiente o genérico: afecta a 26 subproyectos y, junto con los 2 no incluidos, suma 28 de los 53 códigos. Las carencias se repiten en ELIF, Moodle Misc, Dinámicas, integración, sistemas externos y desarrollo seguro; IFP y otros proyectos concretos alcanzan un desarrollo suficiente. La ausencia de ESIS11 y ESIS14, junto con la limitada planificación del segundo año contractual, constituye una deficiencia relevante y no un hecho aislado.

### Análisis por bloques funcionales del Anexo II

Todos los bloques utilizan la misma secuencia: requisito y alcance, análisis de la propuesta, fortalezas y valor añadido, carencias u omisiones y valoración cualitativa. La clasificación individual se conserva en el anexo.

### Mantenimiento evolutivo y adaptativo de Proyectos web Liferay (ELIF)

- **Consideración general del bloque**

Este bloque comprende la adaptación y evolución de páginas externas integradas en Liferay y Scribe CMS, los elementos corporativos comunes, la presentación, la usabilidad y la accesibilidad. Deben valorarse la compatibilidad con las personalizaciones existentes, la mantenibilidad, el despliegue controlado, la validación multidispositivo y el cumplimiento de los estándares aplicables.

#### ELIF1 — Adaptaciones de las páginas web Liferay

- **Requisito y alcance**

El subproyecto ELIF1 tiene por objeto la realización de los trabajos necesarios para la revisión, adaptación y evolución de las páginas web basadas en Liferay, incluyendo específicamente la adaptación de vistas públicas, vistas de edición, componentes asociados al gestor Scribe CMS y las páginas externas alojadas en dicho entorno. **Se trata de un requisito que no se limita a la actualización estética de las aplicaciones, sino que implica comprender la estructura de publicación, los mecanismos de gestión contenidos y las personalizaciones existentes sobre la plataforma corporativa.**

**La propuesta presentada por empresa_n cubre formalmente el requisito definido en el Documento de Invitación e identifica adecuadamente el ámbito funcional sobre el que deben realizarse las actuaciones.** La memoria reconoce la necesidad de intervenir sobre páginas web basadas en Liferay, vistas públicas y privadas, componentes asociados a Scribe CMS y distintos elementos integrados en los portales de EducaMadrid. La solución propuesta permite apreciar una comprensión razonable de los objetivos perseguidos por la Administración.

- **Análisis de la propuesta**

La oferta original concreta como mejora la **creación de virtual hosts en Liferay y en la infraestructura web**, la preparación de entornos no productivos con copias y restauración y la realización de **despliegues controlados en producción**, coordinados para minimizar el impacto y mantener la continuidad. Esta evidencia respalda la observación del anexo y del CSV.

**No obstante, la mayor parte de la respuesta se desarrolla en términos funcionales y organizativos, sin aportar un nivel suficiente de detalle técnico respecto a los procedimientos concretos que serían empleados para ejecutar las adaptaciones solicitadas.** La memoria incorpora referencias generales a actividades de actualización, revisión y adaptación de contenidos, pero desarrolla de forma limitada aspectos relacionados con análisis de impacto, arquitectura de componentes, procedimientos de validación funcional, pruebas de regresión, criterios de aceptación o mecanismos de control de cambios.

**La principal limitación observada radica en la insuficiente concreción técnica de la solución propuesta.** Como consecuencia de ello, no quedan suficientemente definidos los procedimientos operativos, métricas de control, entregables o mecanismos verificables que permitan valorar favorablemente la capacidad de ejecución de las actuaciones descritas. Aunque la cobertura funcional puede considerarse adecuada, la calidad técnica de la respuesta permanece por debajo de lo esperable para alcanzar niveles superiores de valoración conforme al apartado 7.2.2 del Documento de Invitación.

- **Fortalezas y valor añadido**

**La propuesta presentada por empresa_n cubre formalmente el requisito definido en el Documento de Invitación e identifica adecuadamente el ámbito funcional sobre el que deben realizarse las actuaciones.** La memoria reconoce la necesidad de intervenir sobre páginas web basadas en Liferay, vistas públicas y privadas, componentes asociados a Scribe CMS y distintos elementos integrados en los portales de EducaMadrid. La solución propuesta permite apreciar una comprensión razonable de los objetivos perseguidos por la Administración.

**La principal limitación observada radica en la insuficiente concreción técnica de la solución propuesta.** Como consecuencia de ello, no quedan suficientemente definidos los procedimientos operativos, métricas de control, entregables o mecanismos verificables que permitan valorar favorablemente la capacidad de ejecución de las actuaciones descritas. Aunque la cobertura funcional puede considerarse adecuada, la calidad técnica de la respuesta permanece por debajo de lo esperable para alcanzar niveles superiores de valoración conforme al apartado 7.2.2 del Documento de Invitación.

- **Carencias, omisiones, errores o riesgos**

El subproyecto ELIF1 tiene por objeto la realización de los trabajos necesarios para la revisión, adaptación y evolución de las páginas web basadas en Liferay, incluyendo específicamente la adaptación de vistas públicas, vistas de edición, componentes asociados al gestor Scribe CMS y las páginas externas alojadas en dicho entorno. **Se trata de un requisito que no se limita a la actualización estética de las aplicaciones, sino que implica comprender la estructura de publicación, los mecanismos de gestión contenidos y las personalizaciones existentes sobre la plataforma corporativa.**

**No obstante, la mayor parte de la respuesta se desarrolla en términos funcionales y organizativos, sin aportar un nivel suficiente de detalle técnico respecto a los procedimientos concretos que serían empleados para ejecutar las adaptaciones solicitadas.** La memoria incorpora referencias generales a actividades de actualización, revisión y adaptación de contenidos, pero desarrolla de forma limitada aspectos relacionados con análisis de impacto, arquitectura de componentes, procedimientos de validación funcional, pruebas de regresión, criterios de aceptación o mecanismos de control de cambios.

- **Valoración cualitativa**

- **BAJA**

#### ELIF2 — Barra de herramientas y pie de EducaMadrid

- **Requisito y alcance**

**El subproyecto ELIF2 contempla la evolución y mantenimiento de la barra corporativa de herramientas y del pie común utilizados en los diferentes servicios integrados dentro de la plataforma EducaMadrid.** Este requisito posee una importancia estratégica superior a la que podría desprenderse de una simple actuación sobre componentes visuales, dado que constituye uno de los principales elementos de homogeneización de la experiencia de usuario y de integración funcional entre aplicaciones heterogéneas.

**La propuesta aborda adecuadamente el objeto del subproyecto e incorpora referencias específicas a mecanismos de integración de componentes corporativos, repositorios compartidos, distribución mediante CDN, reutilización de componentes y principios asociados a un Design System corporativo.** Estos elementos evidencian una comprensión satisfactoria del papel estratégico que desempeñan la barra corporativa y el pie común dentro del ecosistema EducaMadrid.

- **Análisis de la propuesta**

La respuesta presenta un nivel de madurez superior al observado en otros apartados del bloque, al incorporar conceptos arquitectónicos identificables y una cierta orientación hacia modelos de reutilización y gobierno de componentes. **Sin embargo, la memoria continúa presentando limitaciones significativas en relación con los procedimientos concretos de implantación, las estrategias de despliegue, la gestión de compatibilidades, los mecanismos de validación funcional o los procesos de control de versiones y coexistencia con desarrollos ya existentes.**

La propuesta permite apreciar una solución técnica reconocible y razonablemente alineada con los objetivos del contrato. **No obstante, la profundidad técnica alcanzada resulta insuficiente para acreditar plenamente la viabilidad operativa de los mecanismos descritos o justificar una valoración situada en niveles superiores.** Atendiendo al modelo de valoración previsto en el Documento de Invitación, la calidad observada se corresponde con una valoración MEDIA.

- **Fortalezas y valor añadido**

**La propuesta aborda adecuadamente el objeto del subproyecto e incorpora referencias específicas a mecanismos de integración de componentes corporativos, repositorios compartidos, distribución mediante CDN, reutilización de componentes y principios asociados a un Design System corporativo.** Estos elementos evidencian una comprensión satisfactoria del papel estratégico que desempeñan la barra corporativa y el pie común dentro del ecosistema EducaMadrid.

- **Carencias, omisiones, errores o riesgos**

La respuesta presenta un nivel de madurez superior al observado en otros apartados del bloque, al incorporar conceptos arquitectónicos identificables y una cierta orientación hacia modelos de reutilización y gobierno de componentes. **Sin embargo, la memoria continúa presentando limitaciones significativas en relación con los procedimientos concretos de implantación, las estrategias de despliegue, la gestión de compatibilidades, los mecanismos de validación funcional o los procesos de control de versiones y coexistencia con desarrollos ya existentes.**

La propuesta permite apreciar una solución técnica reconocible y razonablemente alineada con los objetivos del contrato. **No obstante, la profundidad técnica alcanzada resulta insuficiente para acreditar plenamente la viabilidad operativa de los mecanismos descritos o justificar una valoración situada en niveles superiores.** Atendiendo al modelo de valoración previsto en el Documento de Invitación, la calidad observada se corresponde con una valoración MEDIA.

- **Valoración cualitativa**

- **MEDIA**

#### ELIF3 — Mejoras de presentación

- **Requisito y alcance**

**El subproyecto ELIF3 se orienta a la mejora de la presentación y apariencia de las aplicaciones basadas en Liferay, incorporando requisitos relacionados con HTML5, JSP, JSTL, accesibilidad, adaptación visual y experiencia de usuario.** A diferencia de otros requisitos centrados en mantenimiento funcional, este subproyecto exige una combinación de capacidades de diseño frontend, accesibilidad, integración tecnológica y modernización visual.

La propuesta cubre de forma satisfactoria los principales elementos contemplados en el requisito, incorporando referencias a tecnologías frontend modernas, criterios de accesibilidad, desarrollo responsive, reutilización de componentes y mejora de la experiencia de usuario. **La memoria evidencia un conocimiento adecuado de las tendencias actuales de diseño y evolución de interfaces web.**

- **Análisis de la propuesta**

La oferta original propone expresamente una **arquitectura de presentación desacoplada y basada en componentes reutilizables**, con separación entre lógica y contenido, librerías vectoriales, un sistema centralizado de estilos y procesos automatizados de validación visual. Esta evidencia respalda la síntesis del anexo y del CSV.

Pese a la amplitud de conceptos incluidos, una parte significativa de las actuaciones se presenta mediante formulaciones genéricas o potenciales, sin delimitar con precisión el alcance efectivo de los compromisos asumidos. **Del mismo modo, la memoria desarrolla de manera limitada los procedimientos concretos de validación, métricas de experiencia de usuario, herramientas de auditoría de accesibilidad o criterios objetivos de aceptación.**

**La propuesta demuestra comprensión del problema planteado y presenta una cobertura funcional adecuada del requisito.** Sin embargo, la insuficiente concreción metodológica y la limitada definición de mecanismos verificables de ejecución condicionan la calidad global de la respuesta. En consecuencia, la valoración se corresponde con el nivel MEDIA previsto en el Documento de Invitación.

- **Fortalezas y valor añadido**

La propuesta cubre de forma satisfactoria los principales elementos contemplados en el requisito, incorporando referencias a tecnologías frontend modernas, criterios de accesibilidad, desarrollo responsive, reutilización de componentes y mejora de la experiencia de usuario. **La memoria evidencia un conocimiento adecuado de las tendencias actuales de diseño y evolución de interfaces web.**

**La propuesta demuestra comprensión del problema planteado y presenta una cobertura funcional adecuada del requisito.** Sin embargo, la insuficiente concreción metodológica y la limitada definición de mecanismos verificables de ejecución condicionan la calidad global de la respuesta. En consecuencia, la valoración se corresponde con el nivel MEDIA previsto en el Documento de Invitación.

- **Carencias, omisiones, errores o riesgos**

Pese a la amplitud de conceptos incluidos, una parte significativa de las actuaciones se presenta mediante formulaciones genéricas o potenciales, sin delimitar con precisión el alcance efectivo de los compromisos asumidos. **Del mismo modo, la memoria desarrolla de manera limitada los procedimientos concretos de validación, métricas de experiencia de usuario, herramientas de auditoría de accesibilidad o criterios objetivos de aceptación.**

**La propuesta demuestra comprensión del problema planteado y presenta una cobertura funcional adecuada del requisito.** Sin embargo, la insuficiente concreción metodológica y la limitada definición de mecanismos verificables de ejecución condicionan la calidad global de la respuesta. En consecuencia, la valoración se corresponde con el nivel MEDIA previsto en el Documento de Invitación.

- **Valoración cualitativa**

- **MEDIA**

#### ELIF4 — Mejoras de usabilidad y accesibilidad

- **Requisito y alcance**

El subproyecto ELIF4 persigue la mejora de la usabilidad, la accesibilidad y determinados elementos relacionados con los sistemas de comunicación y boletines integrados en las soluciones web de EducaMadrid. **Se trata de un requisito que exige una aproximación multidisciplinar combinando experiencia de usuario, accesibilidad web, análisis funcional y validación de resultados.**

**La propuesta identifica correctamente los objetivos generales asociados a la mejora de la usabilidad, la accesibilidad y la experiencia de usuario de los servicios web contemplados en el ámbito de EducaMadrid.** Asimismo, incorpora referencias a actividades de revisión, seguimiento y optimización de determinados elementos funcionales.

- **Análisis de la propuesta**

**Sin perjuicio de lo anterior, la memoria desarrolla de forma limitada los aspectos técnicos que constituyen el núcleo del requisito.** Las referencias a estándares de accesibilidad, herramientas de auditoría, metodologías de evaluación de experiencia de usuario, métricas de cumplimiento o procedimientos de validación aparecen insuficientemente desarrolladas. La solución permanece principalmente en el plano conceptual y organizativo.

La principal debilidad observada reside en la falta de concreción técnica de las medidas propuestas. **Dicha circunstancia dificulta la comprobación objetiva de los resultados esperados y limita la capacidad de valorar favorablemente la calidad de la solución presentada.** Conforme al modelo previsto en el apartado 7.2.2 del Documento de Invitación, la respuesta se ajusta al nivel BAJA.

- **Fortalezas y valor añadido**

Se reconoce la cobertura formal del requisito en los términos descritos en la memoria.

- **Carencias, omisiones, errores o riesgos**

**Sin perjuicio de lo anterior, la memoria desarrolla de forma limitada los aspectos técnicos que constituyen el núcleo del requisito.** Las referencias a estándares de accesibilidad, herramientas de auditoría, metodologías de evaluación de experiencia de usuario, métricas de cumplimiento o procedimientos de validación aparecen insuficientemente desarrolladas. La solución permanece principalmente en el plano conceptual y organizativo.

La principal debilidad observada reside en la falta de concreción técnica de las medidas propuestas. **Dicha circunstancia dificulta la comprobación objetiva de los resultados esperados y limita la capacidad de valorar favorablemente la calidad de la solución presentada.** Conforme al modelo previsto en el apartado 7.2.2 del Documento de Invitación, la respuesta se ajusta al nivel BAJA.

- **Valoración cualitativa**

- **BAJA**

#### Conclusión del bloque ELIF

El bloque presenta 4 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **MEDIA**.

### Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado (IFP)

- **Consideración general del bloque**

El bloque aborda la actualización y evolución de la plataforma de Innovación y Formación del Profesorado basada en Drupal. Deben considerarse la migración de versión, las funcionalidades e integraciones, la continuidad, la seguridad, el rendimiento, el tratamiento de contenidos y la validación de la transición.

#### IFP1 — Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado (IFP)

- **Requisito y alcance**

**El subproyecto IFP1 constituye uno de los entregables técnicamente más complejos incluidos dentro del Anexo II, tanto por la diversidad de actuaciones solicitadas como por el grado de transformación tecnológica requerido sobre una plataforma funcional ya consolidada.** A diferencia de otros requisitos centrados principalmente en actividades de mantenimiento o evolución incremental, este subproyecto incorpora actuaciones de modernización tecnológica, migración de componentes críticos, reorganización funcional, rediseño de integraciones, optimización del rendimiento, adaptación de infraestructuras y mejora de mecanismos de interoperabilidad. Todo ello convierte este requisito en uno de los principales indicadores de la capacidad técnica real del licitador para acometer evoluciones complejas dentro del ecosistema EducaMadrid.

La propuesta presentada por empresa_n aborda de forma expresa la práctica totalidad de los trabajos incluidos en este subproyecto, identificando actuaciones relacionadas con la migración a Drupal 11, la actualización de componentes y dependencias, la integración de aplicaciones actualmente independientes, la reorganización de la gestión de inscripciones, la creación de nuevos espacios de intranet, la publicación de APIs para terceros, la migración de infraestructuras y la evolución de los mecanismos de autenticación. **Desde la perspectiva de cobertura funcional, la respuesta permite apreciar una comprensión adecuada del alcance del requisito y evidencia que la empresa ha realizado una lectura detallada de las actuaciones solicitadas por el Documento de Invitación.**

**Asimismo, la memoria mantiene una cierta lógica común de ejecución basada en fases de análisis, adaptación, validación y puesta en servicio que aporta coherencia global al planteamiento presentado.** Esta aproximación permite identificar una estructura metodológica básica aplicable a los distintos ámbitos de actuación contemplados dentro del proyecto.

- **Análisis de la propuesta**

**Pese a la amplitud de cobertura observada, el nivel de desarrollo técnico de las soluciones propuestas resulta sensiblemente inferior al nivel de complejidad inherente a muchas de las actuaciones descritas en el Documento de Invitación.** La memoria identifica correctamente los objetivos funcionales perseguidos en ámbitos como Drupal 11, integración de aplicaciones, APIs, gestión de identidades o migración de infraestructuras, pero desarrolla de forma limitada los procedimientos técnicos mediante los cuales se materializarían dichas actuaciones.

En relación con la migración Drupal 11, la memoria incorpora referencias generales a la actualización de la plataforma y de sus dependencias, si bien el grado de desarrollo aportado resulta insuficiente para valorar aspectos especialmente relevantes como la gestión de módulos, compatibilidades, estrategias de despliegue, procedimientos de regresión funcional o mecanismos avanzados de control del riesgo asociados a este tipo de migraciones.

Una situación similar puede apreciarse en las actuaciones relativas a la integración de aplicaciones, la eliminación de componentes Vue o la creación de APIs para terceros. **Aunque la propuesta reconoce adecuadamente la necesidad de acometer dichas actuaciones, la descripción permanece principalmente en el plano funcional y organizativo, desarrollando de forma limitada la arquitectura técnica, los mecanismos de interoperabilidad, los protocolos de autenticación, las estrategias de versionado o los procedimientos de validación de las integraciones resultantes.**

Del mismo modo, las actuaciones relacionadas con infraestructura, seguridad, LDAP o nuevos espacios intranet presentan una cobertura funcional razonable, pero continúan adoleciendo de una limitada definición de procedimientos técnicos, métricas de control, objetivos de rendimiento, criterios de aceptación y mecanismos verificables de seguimiento.

**La principal fortaleza de la propuesta reside en su amplia cobertura funcional y en la correcta identificación de los distintos ámbitos tecnológicos afectados por el proyecto.** Sin embargo, la principal debilidad observada vuelve a situarse en la insuficiente concreción técnica de una parte significativa de las soluciones propuestas. Como consecuencia de ello, la memoria no desarrolla con el suficiente nivel de detalle las herramientas, procedimientos, arquitecturas, métricas o mecanismos de validación que permitirían verificar objetivamente la capacidad de ejecución de las actuaciones contempladas.

Atendiendo al modelo de valoración previsto en el apartado 7.2.2 del Documento de Invitación, la propuesta demuestra una comprensión adecuada de los requisitos y una cobertura funcional claramente satisfactoria, pero no alcanza el nivel de especialización técnica y verificabilidad necesario para justificar una valoración superior.

- **Fortalezas y valor añadido**

La propuesta presentada por empresa_n aborda de forma expresa la práctica totalidad de los trabajos incluidos en este subproyecto, identificando actuaciones relacionadas con la migración a Drupal 11, la actualización de componentes y dependencias, la integración de aplicaciones actualmente independientes, la reorganización de la gestión de inscripciones, la creación de nuevos espacios de intranet, la publicación de APIs para terceros, la migración de infraestructuras y la evolución de los mecanismos de autenticación. **Desde la perspectiva de cobertura funcional, la respuesta permite apreciar una comprensión adecuada del alcance del requisito y evidencia que la empresa ha realizado una lectura detallada de las actuaciones solicitadas por el Documento de Invitación.**

**Asimismo, la memoria mantiene una cierta lógica común de ejecución basada en fases de análisis, adaptación, validación y puesta en servicio que aporta coherencia global al planteamiento presentado.** Esta aproximación permite identificar una estructura metodológica básica aplicable a los distintos ámbitos de actuación contemplados dentro del proyecto.

- **Carencias, omisiones, errores o riesgos**

**Pese a la amplitud de cobertura observada, el nivel de desarrollo técnico de las soluciones propuestas resulta sensiblemente inferior al nivel de complejidad inherente a muchas de las actuaciones descritas en el Documento de Invitación.** La memoria identifica correctamente los objetivos funcionales perseguidos en ámbitos como Drupal 11, integración de aplicaciones, APIs, gestión de identidades o migración de infraestructuras, pero desarrolla de forma limitada los procedimientos técnicos mediante los cuales se materializarían dichas actuaciones.

En relación con la migración Drupal 11, la memoria incorpora referencias generales a la actualización de la plataforma y de sus dependencias, si bien el grado de desarrollo aportado resulta insuficiente para valorar aspectos especialmente relevantes como la gestión de módulos, compatibilidades, estrategias de despliegue, procedimientos de regresión funcional o mecanismos avanzados de control del riesgo asociados a este tipo de migraciones.

- **Valoración cualitativa**

- **MEDIA**

#### Conclusión del bloque IFP

El bloque presenta 1 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **MEDIA**.

### Proyectos Moodle Misc (EMOM)

- **Consideración general del bloque**

Este bloque reúne la actualización, adaptación, mantenimiento, seguridad y operación del entorno MoodleMisc. Deben valorarse la compatibilidad entre versiones, plugins e integraciones; el despliegue en los distintos entornos; la escalabilidad; el rendimiento; las copias de seguridad; la automatización; y la resolución de problemas específicos.

#### EMOM1 — Actualización de la plataforma MoodleMisc

- **Requisito y alcance**

El subproyecto EMOM1 tiene por objeto la actualización evolutiva de la plataforma MoodleMisc, incluyendo la actualización de versiones Moodle, componentes PHP, plugins asociados, temas gráficos, mecanismos de seguridad, sistemas auxiliares y diversos elementos técnicos que forman parte del ecosistema de explotación de esta plataforma. **El alcance definido en el Documento de Invitación no se limita a la mera instalación de nuevas versiones de software, sino que implica garantizar la compatibilidad funcional de todos los componentes afectados, preservar la continuidad del servicio y asegurar el correcto funcionamiento de las integraciones existentes tras la actualización.**

**La propuesta identifica adecuadamente los principales elementos incluidos en el proceso de actualización de la plataforma MoodleMisc, incorporando referencias a la actualización del núcleo Moodle, revisión de plugins, adaptación de componentes PHP, revisión del tema gráfico y validación posterior de las modificaciones realizadas.** La respuesta evidencia una comprensión razonable de los objetivos generales perseguidos por el requisito y permite apreciar una cobertura funcional satisfactoria de los principales ámbitos afectados.

- **Análisis de la propuesta**

La oferta original incorpora como mejora un proceso sistemático de **auditoría técnica y funcional apoyado en inventario y diagnóstico automatizados**, perfiles normalizados de despliegue y un modelo **CI/CD** para automatizar parcialmente pruebas, validaciones y despliegues. Esta evidencia respalda la observación de CI/CD y auditoría automatizada del anexo y del CSV.

La memoria describe de forma general las actividades que se llevarán a cabo durante la actualización, pero desarrolla de forma limitada los procedimientos técnicos específicos asociados a la gestión de dependencias, el tratamiento de incompatibilidades, la validación de plugins, la ejecución controlada de las actualizaciones o la mitigación de riesgos derivados del proceso de migración tecnológica.

Si bien se identifican los principales componentes tecnológicos afectados, el grado de detalle aportado respecto a las herramientas, mecanismos de control, procedimientos de regresión funcional o criterios de aceptación resulta reducido para un entorno Moodle de las características contempladas en EducaMadrid.

**La propuesta demuestra una comprensión adecuada del alcance funcional del requisito y cubre satisfactoriamente los principales elementos incluidos en el mismo.** Sin embargo, la limitada definición de procedimientos técnicos verificables, mecanismos específicos de validación y estrategias detalladas de implantación impide considerar la solución particularmente avanzada desde el punto de vista metodológico o tecnológico. Conforme al baremo establecido en el Documento de Invitación, la calidad de la respuesta se ajusta al nivel MEDIA.

- **Fortalezas y valor añadido**

**La propuesta identifica adecuadamente los principales elementos incluidos en el proceso de actualización de la plataforma MoodleMisc, incorporando referencias a la actualización del núcleo Moodle, revisión de plugins, adaptación de componentes PHP, revisión del tema gráfico y validación posterior de las modificaciones realizadas.** La respuesta evidencia una comprensión razonable de los objetivos generales perseguidos por el requisito y permite apreciar una cobertura funcional satisfactoria de los principales ámbitos afectados.

**La propuesta demuestra una comprensión adecuada del alcance funcional del requisito y cubre satisfactoriamente los principales elementos incluidos en el mismo.** Sin embargo, la limitada definición de procedimientos técnicos verificables, mecanismos específicos de validación y estrategias detalladas de implantación impide considerar la solución particularmente avanzada desde el punto de vista metodológico o tecnológico. Conforme al baremo establecido en el Documento de Invitación, la calidad de la respuesta se ajusta al nivel MEDIA.

- **Carencias, omisiones, errores o riesgos**

El subproyecto EMOM1 tiene por objeto la actualización evolutiva de la plataforma MoodleMisc, incluyendo la actualización de versiones Moodle, componentes PHP, plugins asociados, temas gráficos, mecanismos de seguridad, sistemas auxiliares y diversos elementos técnicos que forman parte del ecosistema de explotación de esta plataforma. **El alcance definido en el Documento de Invitación no se limita a la mera instalación de nuevas versiones de software, sino que implica garantizar la compatibilidad funcional de todos los componentes afectados, preservar la continuidad del servicio y asegurar el correcto funcionamiento de las integraciones existentes tras la actualización.**

La memoria describe de forma general las actividades que se llevarán a cabo durante la actualización, pero desarrolla de forma limitada los procedimientos técnicos específicos asociados a la gestión de dependencias, el tratamiento de incompatibilidades, la validación de plugins, la ejecución controlada de las actualizaciones o la mitigación de riesgos derivados del proceso de migración tecnológica.

- **Valoración cualitativa**

- **MEDIA**

#### EMOM2 — Adaptación de la plataforma MoodleMisc

- **Requisito y alcance**

El subproyecto EMOM2 constituye uno de los requisitos técnicamente más exigentes del bloque MoodleMisc, ya que incorpora numerosas adaptaciones funcionales, integraciones con plataformas externas y desarrollos asociados a sistemas concretos que forman parte del ecosistema EducaMadrid. **Entre los elementos expresamente contemplados por el pliego destacan integraciones mediante SAML, NextCloud, WebAuth, BigBlueButton, sistemas de inteligencia artificial, CodeRunner, Kuet, escalado horizontal de la plataforma, adaptaciones PostgreSQL, generación documental y otros desarrollos específicos.**

**La propuesta incorpora referencias a la revisión de integraciones, análisis de conectividad, seguimiento del crecimiento de la plataforma y mantenimiento de servicios conectados.** Estas actuaciones guardan relación con el objeto general del requisito y permiten constatar una comprensión básica del entorno funcional sobre el que debe actuar la empresa.

- **Análisis de la propuesta**

**No obstante, una parte significativa de los elementos técnicos individualizados por el Documento de Invitación aparece sustituida por categorías funcionales de carácter general.** Numerosas integraciones específicas contempladas en el pliego no disponen de una respuesta técnica claramente identificable, quedando englobadas bajo referencias genéricas a conectividad, interoperabilidad o adaptación de servicios. Esta circunstancia dificulta valorar el conocimiento especializado de las tecnologías concretas incluidas en el ecosistema MoodleMisc.

Asimismo, la memoria desarrolla de forma limitada las arquitecturas de integración, mecanismos de autenticación federada, procedimientos de sincronización o estrategias de validación funcional necesarias para valorar favorablemente la complejidad técnica de las actuaciones previstas.

La propuesta proporciona una cobertura parcial del alcance efectivo del requisito y presenta un nivel de desarrollo predominantemente funcional y organizativo. **La limitada concreción técnica observada reduce significativamente la capacidad de verificar los mecanismos concretos de ejecución previstos para las diferentes integraciones especializadas contempladas en el Documento de Invitación.** Conforme al modelo de valoración aplicable, la calidad de la respuesta se ajusta al nivel BAJA.

- **Fortalezas y valor añadido**

El subproyecto EMOM2 constituye uno de los requisitos técnicamente más exigentes del bloque MoodleMisc, ya que incorpora numerosas adaptaciones funcionales, integraciones con plataformas externas y desarrollos asociados a sistemas concretos que forman parte del ecosistema EducaMadrid. **Entre los elementos expresamente contemplados por el pliego destacan integraciones mediante SAML, NextCloud, WebAuth, BigBlueButton, sistemas de inteligencia artificial, CodeRunner, Kuet, escalado horizontal de la plataforma, adaptaciones PostgreSQL, generación documental y otros desarrollos específicos.**

**La propuesta incorpora referencias a la revisión de integraciones, análisis de conectividad, seguimiento del crecimiento de la plataforma y mantenimiento de servicios conectados.** Estas actuaciones guardan relación con el objeto general del requisito y permiten constatar una comprensión básica del entorno funcional sobre el que debe actuar la empresa.

- **Carencias, omisiones, errores o riesgos**

**No obstante, una parte significativa de los elementos técnicos individualizados por el Documento de Invitación aparece sustituida por categorías funcionales de carácter general.** Numerosas integraciones específicas contempladas en el pliego no disponen de una respuesta técnica claramente identificable, quedando englobadas bajo referencias genéricas a conectividad, interoperabilidad o adaptación de servicios. Esta circunstancia dificulta valorar el conocimiento especializado de las tecnologías concretas incluidas en el ecosistema MoodleMisc.

Asimismo, la memoria desarrolla de forma limitada las arquitecturas de integración, mecanismos de autenticación federada, procedimientos de sincronización o estrategias de validación funcional necesarias para valorar favorablemente la complejidad técnica de las actuaciones previstas.

- **Valoración cualitativa**

- **BAJA**

#### EMOM3 — Mantenimiento de la plataforma MoodleMisc

- **Requisito y alcance**

**El mantenimiento evolutivo y correctivo de MoodleMisc constituye uno de los componentes de mayor volumen funcional dentro del bloque EMOM.** El pliego identifica un número elevado de actuaciones concretas relacionadas con plugins educativos, plataformas editoriales, sistemas de videoconferencia, herramientas colaborativas, mecanismos antivirus, sistemas de reserva, integraciones externas, automatización de tareas y numerosos componentes auxiliares que forman parte del entorno Moodle.

**La propuesta presentada por empresa_n aborda el mantenimiento de MoodleMisc mediante la agrupación de los diferentes componentes funcionales en grandes categorías de servicios, incluyendo plugins educativos, herramientas colaborativas, integraciones audiovisuales, mecanismos de seguridad y otros elementos auxiliares del ecosistema Moodle.** Desde una perspectiva funcional, la memoria permite apreciar que la empresa comprende la necesidad de garantizar la continuidad operativa de la plataforma y el mantenimiento de sus componentes asociados.

- **Análisis de la propuesta**

**Sin embargo, el nivel de detalle técnico aportado resulta limitado respecto al alcance específico definido en el Documento de Invitación.** Numerosos componentes individualizados por la Administración dejan de disponer de una respuesta identificable y pasan a formar parte de categorías funcionales genéricas. Esta circunstancia dificulta valorar el grado de conocimiento especializado que posee el licitador sobre cada uno de los elementos concretos que forman parte del entorno MoodleMisc de EducaMadrid.

**Asimismo, la memoria desarrolla de forma limitada procedimientos específicos de mantenimiento, estrategias de actualización diferenciada, mecanismos de monitorización, metodologías de resolución de incidencias o procedimientos de validación funcional adaptados a cada conjunto tecnológico.** La propuesta se mantiene principalmente en un plano descriptivo y organizativo.

**Aunque la propuesta permite apreciar una comprensión adecuada de la finalidad del servicio de mantenimiento y cubre de forma general los ámbitos tecnológicos afectados, la escasa concreción técnica observada limita significativamente la verificabilidad de la solución y su capacidad para acreditar experiencia especializada en los distintos componentes que integran MoodleMisc.** Conforme a la escala de valoración del apartado 7.2.2 del Documento de Invitación, la calidad de la respuesta se corresponde con el nivel BAJA.

- **Fortalezas y valor añadido**

**Aunque la propuesta permite apreciar una comprensión adecuada de la finalidad del servicio de mantenimiento y cubre de forma general los ámbitos tecnológicos afectados, la escasa concreción técnica observada limita significativamente la verificabilidad de la solución y su capacidad para acreditar experiencia especializada en los distintos componentes que integran MoodleMisc.** Conforme a la escala de valoración del apartado 7.2.2 del Documento de Invitación, la calidad de la respuesta se corresponde con el nivel BAJA.

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, el nivel de detalle técnico aportado resulta limitado respecto al alcance específico definido en el Documento de Invitación.** Numerosos componentes individualizados por la Administración dejan de disponer de una respuesta identificable y pasan a formar parte de categorías funcionales genéricas. Esta circunstancia dificulta valorar el grado de conocimiento especializado que posee el licitador sobre cada uno de los elementos concretos que forman parte del entorno MoodleMisc de EducaMadrid.

**Asimismo, la memoria desarrolla de forma limitada procedimientos específicos de mantenimiento, estrategias de actualización diferenciada, mecanismos de monitorización, metodologías de resolución de incidencias o procedimientos de validación funcional adaptados a cada conjunto tecnológico.** La propuesta se mantiene principalmente en un plano descriptivo y organizativo.

- **Valoración cualitativa**

- **BAJA**

#### EMOM4 — Mejora de la Ciberseguridad en Moodle Misc

- **Requisito y alcance**

El objeto de este subproyecto consiste en reforzar las medidas de seguridad existentes en la plataforma MoodleMisc mediante actuaciones relacionadas con endurecimiento de configuraciones, protección de accesos, configuración de cabeceras de seguridad, reducción de exposición de información sensible y mejora general del nivel de protección de la aplicación.

**La propuesta contempla actuaciones relacionadas con configuraciones seguras, revisión de cabeceras de seguridad, control de accesos y análisis de determinados parámetros asociados a la protección de la plataforma.** Estas referencias permiten identificar una comprensión general del ámbito funcional sobre el que debe actuarse y una alineación básica con los objetivos perseguidos por el Documento de Invitación.

- **Análisis de la propuesta**

**No obstante, el desarrollo técnico de las medidas propuestas resulta limitado.** La memoria incorpora referencias genéricas a conceptos de seguridad, pero desarrolla escasamente aspectos relacionados con estándares de configuración, políticas de endurecimiento, controles avanzados de protección web, herramientas específicas de auditoría o mecanismos de validación de las medidas implantadas.

**Tampoco quedan suficientemente definidos los procedimientos de seguimiento, revisión periódica, tratamiento de vulnerabilidades o verificación de la efectividad de las actuaciones previstas.** Como consecuencia de ello, la solución mantiene un carácter predominantemente conceptual.

**La propuesta resulta compatible con el objeto del requisito y demuestra una comprensión básica de las necesidades de seguridad planteadas por la Administración.** Sin embargo, la insuficiente especialización técnica observada y la limitada definición de procedimientos verificables reducen de forma significativa el valor diferencial de la solución. Conforme al baremo previsto en el Documento de Invitación, la respuesta se ajusta al nivel BAJA.

- **Fortalezas y valor añadido**

**La propuesta contempla actuaciones relacionadas con configuraciones seguras, revisión de cabeceras de seguridad, control de accesos y análisis de determinados parámetros asociados a la protección de la plataforma.** Estas referencias permiten identificar una comprensión general del ámbito funcional sobre el que debe actuarse y una alineación básica con los objetivos perseguidos por el Documento de Invitación.

**La propuesta resulta compatible con el objeto del requisito y demuestra una comprensión básica de las necesidades de seguridad planteadas por la Administración.** Sin embargo, la insuficiente especialización técnica observada y la limitada definición de procedimientos verificables reducen de forma significativa el valor diferencial de la solución. Conforme al baremo previsto en el Documento de Invitación, la respuesta se ajusta al nivel BAJA.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el desarrollo técnico de las medidas propuestas resulta limitado.** La memoria incorpora referencias genéricas a conceptos de seguridad, pero desarrolla escasamente aspectos relacionados con estándares de configuración, políticas de endurecimiento, controles avanzados de protección web, herramientas específicas de auditoría o mecanismos de validación de las medidas implantadas.

**La propuesta resulta compatible con el objeto del requisito y demuestra una comprensión básica de las necesidades de seguridad planteadas por la Administración.** Sin embargo, la insuficiente especialización técnica observada y la limitada definición de procedimientos verificables reducen de forma significativa el valor diferencial de la solución. Conforme al baremo previsto en el Documento de Invitación, la respuesta se ajusta al nivel BAJA.

- **Valoración cualitativa**

- **BAJA**

#### EMOM5 — Solución de problemas conocidos en Moodle Misc

- **Requisito y alcance**

El subproyecto EMOM5 se orienta a la resolución de diversos problemas conocidos identificados en la plataforma MoodleMisc, incluyendo incidencias relacionadas con Wiris, LaTeX, H5P, calendarios, competencias y diferentes plugins específicos presentes en el entorno.

La memoria identifica expresamente la mayoría de los problemas conocidos contemplados en el Documento de Invitación e incorpora referencias a actuaciones destinadas a su análisis y resolución. **Esta circunstancia permite apreciar una lectura atenta del pliego y una comprensión adecuada de los principales elementos funcionales que deberán abordarse durante la ejecución del contrato.**

- **Análisis de la propuesta**

**Aunque la propuesta reconoce correctamente los problemas existentes, el desarrollo técnico asociado a su resolución resulta limitado.** La memoria describe qué incidencias serán tratadas, pero desarrolla con escaso nivel de detalle los mecanismos de diagnóstico, los procedimientos de análisis de causa raíz, las herramientas de monitorización, los criterios de priorización o los procesos de validación posteriores a las correcciones realizadas.

Como consecuencia de ello, buena parte del contenido aportado se centra en reproducir el alcance funcional ya identificado en el Documento de Invitación, aportando una limitada diferenciación desde la perspectiva de la calidad técnica de la solución.

**La propuesta cubre adecuadamente el ámbito funcional del requisito y demuestra conocimiento sobre los problemas identificados por la Administración.** No obstante, la limitada profundización en las metodologías de resolución y la ausencia de mecanismos de validación suficientemente desarrollados impiden situar la respuesta en niveles superiores de valoración. Conforme al modelo de puntuación del Documento de Invitación, la calidad observada se ajusta al nivel MEDIA.

- **Fortalezas y valor añadido**

La memoria identifica expresamente la mayoría de los problemas conocidos contemplados en el Documento de Invitación e incorpora referencias a actuaciones destinadas a su análisis y resolución. **Esta circunstancia permite apreciar una lectura atenta del pliego y una comprensión adecuada de los principales elementos funcionales que deberán abordarse durante la ejecución del contrato.**

**La propuesta cubre adecuadamente el ámbito funcional del requisito y demuestra conocimiento sobre los problemas identificados por la Administración.** No obstante, la limitada profundización en las metodologías de resolución y la ausencia de mecanismos de validación suficientemente desarrollados impiden situar la respuesta en niveles superiores de valoración. Conforme al modelo de puntuación del Documento de Invitación, la calidad observada se ajusta al nivel MEDIA.

- **Carencias, omisiones, errores o riesgos**

**Aunque la propuesta reconoce correctamente los problemas existentes, el desarrollo técnico asociado a su resolución resulta limitado.** La memoria describe qué incidencias serán tratadas, pero desarrolla con escaso nivel de detalle los mecanismos de diagnóstico, los procedimientos de análisis de causa raíz, las herramientas de monitorización, los criterios de priorización o los procesos de validación posteriores a las correcciones realizadas.

Como consecuencia de ello, buena parte del contenido aportado se centra en reproducir el alcance funcional ya identificado en el Documento de Invitación, aportando una limitada diferenciación desde la perspectiva de la calidad técnica de la solución.

- **Valoración cualitativa**

- **MEDIA**

#### EMOM6 — Tareas sobre las configuraciones para las conexiones externas

- **Requisito y alcance**

El requisito EMOM6 contempla diversas actuaciones relacionadas con integraciones externas, conectividad con plataformas editoriales, servicios LTI, mecanismos de federación y otras conexiones complementarias necesarias para el funcionamiento de MoodleMisc.

**La propuesta incorpora referencias a diversas integraciones externas contempladas en el Documento de Invitación y reconoce la necesidad de mantener operativas las conexiones existentes entre MoodleMisc y otros servicios externos.** Desde la perspectiva funcional, puede apreciarse una comprensión razonable de la finalidad general perseguida por este requisito.

- **Análisis de la propuesta**

**Sin perjuicio de lo anterior, la memoria desarrolla de forma limitada los mecanismos técnicos asociados a dichas integraciones.** Los procedimientos de autenticación, intercambio de información, validación de conectividad, resolución de incidencias de interoperabilidad o control de dependencias aparecen descritos con un bajo nivel de detalle.

Asimismo, los procesos de seguimiento, monitorización y validación funcional permanecen definidos en términos generales, sin que se identifiquen arquitecturas específicas, herramientas especializadas o metodologías avanzadas que permitan valorar favorablemente la complejidad de la solución planteada.

**La propuesta cubre parcialmente el alcance funcional solicitado, pero la limitada profundidad técnica y la escasa definición de mecanismos verificables de integración condicionan significativamente la valoración global del subproyecto.** Conforme al apartado 7.2.2 del Documento de Invitación, la calidad de la respuesta se corresponde con el nivel BAJA.

- **Fortalezas y valor añadido**

**La propuesta incorpora referencias a diversas integraciones externas contempladas en el Documento de Invitación y reconoce la necesidad de mantener operativas las conexiones existentes entre MoodleMisc y otros servicios externos.** Desde la perspectiva funcional, puede apreciarse una comprensión razonable de la finalidad general perseguida por este requisito.

- **Carencias, omisiones, errores o riesgos**

**Sin perjuicio de lo anterior, la memoria desarrolla de forma limitada los mecanismos técnicos asociados a dichas integraciones.** Los procedimientos de autenticación, intercambio de información, validación de conectividad, resolución de incidencias de interoperabilidad o control de dependencias aparecen descritos con un bajo nivel de detalle.

**La propuesta cubre parcialmente el alcance funcional solicitado, pero la limitada profundidad técnica y la escasa definición de mecanismos verificables de integración condicionan significativamente la valoración global del subproyecto.** Conforme al apartado 7.2.2 del Documento de Invitación, la calidad de la respuesta se corresponde con el nivel BAJA.

- **Valoración cualitativa**

- **BAJA**

#### EMOM7 — Otras tareas específicas para la actualización y procedimiento en Moodle Misc

- **Requisito y alcance**

El último subproyecto del bloque EMOM incorpora actuaciones de automatización, administración de infraestructuras auxiliares, gestión de bases de datos, tratamiento de MoodleData, mantenimiento de scripts y otros procedimientos específicos relacionados con la operación técnica de la plataforma.

**La propuesta contempla actuaciones orientadas a la mejora continua de la plataforma, actualización de configuraciones, revisión de procedimientos y realización de distintas tareas complementarias asociadas a la evolución de MoodleMisc.** La memoria incorpora referencias alineadas con la finalidad general perseguida por el Documento de Invitación.

- **Análisis de la propuesta**

**No obstante, el desarrollo ofrecido para este conjunto de actuaciones resulta principalmente genérico y organizativo.** La memoria no concreta suficientemente los procedimientos operativos aplicables, los criterios técnicos de ejecución, los mecanismos de priorización, las métricas de seguimiento ni los entregables asociados a las distintas actuaciones incluidas dentro del alcance del subproyecto.

Como sucede en otros apartados del bloque, la solución desarrolla adecuadamente los objetivos perseguidos, pero aporta limitada información sobre los medios técnicos concretos mediante los cuales se alcanzarán dichos objetivos.

**La principal debilidad observada vuelve a encontrarse en la insuficiente concreción técnica de la solución.** Aunque el requisito se encuentra cubierto desde una perspectiva funcional general, el nivel de detalle aportado resulta insuficiente para acreditar con claridad los procedimientos y mecanismos de ejecución contemplados. Conforme al modelo de valoración aplicable, la calidad de la respuesta se ajusta al nivel BAJA.

- **Fortalezas y valor añadido**

Como sucede en otros apartados del bloque, la solución desarrolla adecuadamente los objetivos perseguidos, pero aporta limitada información sobre los medios técnicos concretos mediante los cuales se alcanzarán dichos objetivos.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el desarrollo ofrecido para este conjunto de actuaciones resulta principalmente genérico y organizativo.** La memoria no concreta suficientemente los procedimientos operativos aplicables, los criterios técnicos de ejecución, los mecanismos de priorización, las métricas de seguimiento ni los entregables asociados a las distintas actuaciones incluidas dentro del alcance del subproyecto.

Como sucede en otros apartados del bloque, la solución desarrolla adecuadamente los objetivos perseguidos, pero aporta limitada información sobre los medios técnicos concretos mediante los cuales se alcanzarán dichos objetivos.

- **Valoración cualitativa**

- **BAJA**

#### Conclusión del bloque EMOM

El bloque presenta 5 subproyectos con desarrollo suficiente, 2 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **BAJA**.

### Proyectos de Dinámicas (EDIN)

- **Consideración general del bloque**

El entorno Dinámicas agrupa aplicaciones heredadas con arquitecturas, dependencias y estados de mantenimiento heterogéneos. Deben valorarse el inventario, la adaptación de código y componentes, la actualización tecnológica, la segregación, la seguridad, la adecuación al ENS, la continuidad y el control de accesos y ficheros.

#### EDIN1 — Mantenimiento, actualización y adecuación ENS del entorno Dinámicas

- **Requisito y alcance**

El subproyecto EDIN1 tiene como finalidad garantizar el mantenimiento, la actualización tecnológica, la mejora continua y la adecuación al Esquema Nacional de Seguridad del entorno de páginas dinámicas utilizado dentro del ecosistema EducaMadrid. **Aunque el número de requisitos asociados a este subproyecto es reducido en comparación con otros bloques del Anexo II, la relevancia técnica de las actuaciones solicitadas es elevada, dado que afectan simultáneamente a la continuidad operativa, la seguridad y el cumplimiento normativo del servicio.**

La propuesta presentada por empresa_n cubre formalmente el alcance funcional del requisito e identifica correctamente la necesidad de realizar actuaciones de mantenimiento, actualización tecnológica, mejora continua y adecuación al Esquema Nacional de Seguridad del entorno de páginas dinámicas de EducaMadrid. **La memoria evidencia una comprensión adecuada del papel que desempeña este entorno dentro del ecosistema tecnológico corporativo, así como de la necesidad de garantizar simultáneamente su continuidad operativa y el cumplimiento de los requisitos de seguridad aplicables.**

La propuesta incorpora referencias a elementos propios del entorno tales como LDAP, servicios FTP, dominios, bases de datos y otros componentes asociados a la explotación habitual de la plataforma, lo que permite apreciar un conocimiento razonable del contexto tecnológico sobre el que deberán desarrollarse los trabajos.

- **Análisis de la propuesta**

**Sin perjuicio de lo anterior, los aspectos que constituyen el núcleo técnico del requisito aparecen insuficientemente desarrollados.** Aunque la memoria incorpora referencias generales a revisión de accesos, alineamiento normativo, control de configuraciones y seguimiento de la evolución del entorno, el grado de desarrollo aportado resulta limitado para acreditar adecuadamente la adecuación efectiva al Esquema Nacional de Seguridad.

**La propuesta incorpora referencias genéricas a seguridad y cumplimiento, pero desarrolla de forma insuficiente aspectos relacionados con análisis de riesgos, categorización de medidas ENS, controles de seguridad específicos, procedimientos de auditoría, generación de evidencias, bastionado, monitorización especializada o mecanismos avanzados de protección.** Como consecuencia, la capacidad de verificar objetivamente la adecuación normativa y técnica de las actuaciones previstas resulta reducida.

Asimismo, los procedimientos operativos permanecen formulados principalmente mediante actividades de revisión, supervisión o verificación, sin incorporar herramientas concretas, métricas objetivas, criterios de aceptación o mecanismos de validación que permitan acreditar la eficacia de las medidas propuestas.

La propuesta demuestra una comprensión razonable del entorno funcional y cubre formalmente el alcance solicitado. **Sin embargo, la insuficiente concreción técnica observada en materias críticas como adecuación ENS, gestión de riesgos, ciberseguridad y validación de controles limita significativamente la calidad de la solución presentada.**

**La principal debilidad identificada es la escasa definición de procedimientos verificables y mecanismos objetivos de cumplimiento.** De esta circunstancia derivan la limitada trazabilidad de las actuaciones, la ausencia de métricas asociadas y la dificultad para verificar el grado real de adecuación alcanzado.

Conforme a la escala de valoración del apartado 7.2.2 del Documento de Invitación, la calidad de la respuesta se corresponde con el nivel **BAJA**.

- **Fortalezas y valor añadido**

La propuesta presentada por empresa_n cubre formalmente el alcance funcional del requisito e identifica correctamente la necesidad de realizar actuaciones de mantenimiento, actualización tecnológica, mejora continua y adecuación al Esquema Nacional de Seguridad del entorno de páginas dinámicas de EducaMadrid. **La memoria evidencia una comprensión adecuada del papel que desempeña este entorno dentro del ecosistema tecnológico corporativo, así como de la necesidad de garantizar simultáneamente su continuidad operativa y el cumplimiento de los requisitos de seguridad aplicables.**

**Sin perjuicio de lo anterior, los aspectos que constituyen el núcleo técnico del requisito aparecen insuficientemente desarrollados.** Aunque la memoria incorpora referencias generales a revisión de accesos, alineamiento normativo, control de configuraciones y seguimiento de la evolución del entorno, el grado de desarrollo aportado resulta limitado para acreditar adecuadamente la adecuación efectiva al Esquema Nacional de Seguridad.

- **Carencias, omisiones, errores o riesgos**

**Sin perjuicio de lo anterior, los aspectos que constituyen el núcleo técnico del requisito aparecen insuficientemente desarrollados.** Aunque la memoria incorpora referencias generales a revisión de accesos, alineamiento normativo, control de configuraciones y seguimiento de la evolución del entorno, el grado de desarrollo aportado resulta limitado para acreditar adecuadamente la adecuación efectiva al Esquema Nacional de Seguridad.

**La propuesta incorpora referencias genéricas a seguridad y cumplimiento, pero desarrolla de forma insuficiente aspectos relacionados con análisis de riesgos, categorización de medidas ENS, controles de seguridad específicos, procedimientos de auditoría, generación de evidencias, bastionado, monitorización especializada o mecanismos avanzados de protección.** Como consecuencia, la capacidad de verificar objetivamente la adecuación normativa y técnica de las actuaciones previstas resulta reducida.

- **Valoración cualitativa**

- **BAJA**

#### EDIN2 — Mantenimiento, actualización y mejora del espacio FTP

- **Requisito y alcance**

**El subproyecto EDIN2 contempla la evolución y mantenimiento del espacio FTP utilizado dentro de la plataforma EducaMadrid, incluyendo tanto actividades de actualización técnica como actuaciones destinadas a mejorar la seguridad, disponibilidad y adecuación normativa del servicio.** Aunque aparentemente se trata de un componente de menor complejidad funcional, la realidad es que este tipo de infraestructuras suelen constituir puntos críticos desde el punto de vista de la seguridad y la gestión de accesos.

La propuesta presentada por empresa_n cubre formalmente las actuaciones asociadas al mantenimiento y evolución del espacio FTP de EducaMadrid. **La memoria identifica correctamente la necesidad de revisar cuentas, analizar permisos, validar condiciones de uso y supervisar la operación general del servicio, evidenciando una comprensión adecuada de las funciones básicas asociadas a este entorno.**

Asimismo, la propuesta reconoce la importancia de controlar los accesos y mantener actualizados los componentes asociados al servicio, contemplando distintas actividades orientadas a preservar su correcto funcionamiento operativo.

- **Análisis de la propuesta**

**No obstante, la solución presentada permanece principalmente en un plano funcional y organizativo.** Aunque se describen actividades de revisión y control, la memoria desarrolla de forma insuficiente los elementos técnicos asociados a la seguridad, trazabilidad y modernización del servicio.

**En particular, apenas se incorporan referencias a protocolos seguros de transferencia, mecanismos de cifrado, autenticación reforzada, auditoría de accesos, retención de registros, segregación avanzada de permisos o procedimientos específicos de adecuación al Esquema Nacional de Seguridad.** Del mismo modo, no se describen herramientas concretas de supervisión ni mecanismos estructurados de validación de configuraciones.

Las mejoras previstas aparecen formuladas principalmente mediante actividades de control y revisión, sin desarrollar suficientemente actuaciones técnicas de modernización, automatización o incremento efectivo de la seguridad del servicio.

**La propuesta cubre adecuadamente el ámbito funcional solicitado y demuestra comprender las necesidades generales asociadas a la explotación del servicio FTP corporativo.** Sin embargo, la profundidad técnica alcanzada resulta insuficiente en relación con los aspectos de seguridad, cumplimiento normativo y evolución tecnológica que constituyen los elementos de mayor valor dentro del requisito.

La limitada definición de procedimientos técnicos, herramientas especializadas, métricas e indicadores verificables impide considerar acreditado un nivel elevado de especialización en este ámbito.

Atendiendo al modelo de valoración previsto en el apartado 7.2.2 del Documento de Invitación, la calidad de la respuesta se corresponde con el nivel **BAJA**.

- **Fortalezas y valor añadido**

La propuesta presentada por empresa_n cubre formalmente las actuaciones asociadas al mantenimiento y evolución del espacio FTP de EducaMadrid. **La memoria identifica correctamente la necesidad de revisar cuentas, analizar permisos, validar condiciones de uso y supervisar la operación general del servicio, evidenciando una comprensión adecuada de las funciones básicas asociadas a este entorno.**

**La propuesta cubre adecuadamente el ámbito funcional solicitado y demuestra comprender las necesidades generales asociadas a la explotación del servicio FTP corporativo.** Sin embargo, la profundidad técnica alcanzada resulta insuficiente en relación con los aspectos de seguridad, cumplimiento normativo y evolución tecnológica que constituyen los elementos de mayor valor dentro del requisito.

- **Carencias, omisiones, errores o riesgos**

**No obstante, la solución presentada permanece principalmente en un plano funcional y organizativo.** Aunque se describen actividades de revisión y control, la memoria desarrolla de forma insuficiente los elementos técnicos asociados a la seguridad, trazabilidad y modernización del servicio.

**En particular, apenas se incorporan referencias a protocolos seguros de transferencia, mecanismos de cifrado, autenticación reforzada, auditoría de accesos, retención de registros, segregación avanzada de permisos o procedimientos específicos de adecuación al Esquema Nacional de Seguridad.** Del mismo modo, no se describen herramientas concretas de supervisión ni mecanismos estructurados de validación de configuraciones.

- **Valoración cualitativa**

- **BAJA**

#### Conclusión del bloque EDIN

El bloque presenta 0 subproyectos con desarrollo suficiente, 2 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **BAJA**.

### Proyectos de Integración con la Plataforma de EducaMadrid (EIPE)

- **Consideración general del bloque**

Este bloque comprende modificaciones de aplicaciones, plugins, scripts e interfaces necesarias para integrar proyectos exteriores con la plataforma. Deben valorarse el análisis de dependencias, la compatibilidad tecnológica, el ciclo de vida del software, la seguridad, la validación y el control del despliegue.

#### EIPE1 — Modificación de aplicaciones, plugins y scripts de integración

- **Requisito y alcance**

**El subproyecto EIPE1 tiene como finalidad la realización de modificaciones puntuales sobre aplicaciones, plugins, componentes software y scripts cuya misión principal consiste en facilitar o mantener la integración entre aplicaciones externas y los distintos servicios de la plataforma EducaMadrid.** El Documento de Invitación identifica expresamente diversas tecnologías asociadas a estos desarrollos, incluyendo PHP, Python, Ruby, Java y Shell Script, configurando un entorno de integración heterogéneo y de elevada complejidad técnica.

**La propuesta presentada por empresa_n cubre formalmente el alcance funcional del requisito e identifica correctamente la necesidad de realizar modificaciones sobre aplicaciones, plugins, componentes software y scripts destinados a mantener y evolucionar las integraciones existentes entre sistemas externos y la plataforma EducaMadrid.** La memoria demuestra comprender que este subproyecto desempeña un papel esencial para garantizar la interoperabilidad entre aplicaciones heterogéneas dentro del ecosistema tecnológico corporativo.

La propuesta contempla actividades de análisis previo, identificación de necesidades, revisión de dependencias, desarrollo, validación y puesta en servicio de las modificaciones requeridas. **Esta secuencia de trabajo resulta coherente con la naturaleza general de los trabajos solicitados y permite apreciar una comprensión adecuada del ciclo de vida asociado a actuaciones de integración.**

- **Análisis de la propuesta**

**No obstante, la profundidad técnica alcanzada resulta significativamente inferior a la complejidad real del requisito.** Aunque el Documento de Invitación identifica expresamente tecnologías y entornos de integración diversos (PHP, Python, Ruby, Java y Shell Script), la propuesta desarrolla escasamente los mecanismos técnicos asociados a dichas tecnologías y evita profundizar en las arquitecturas de integración necesarias para materializar las actuaciones previstas.

**La memoria incorpora referencias genéricas a desarrollos, modificaciones y adaptaciones, pero desarrolla de forma insuficiente aspectos relacionados con intercambio de información, diseño de servicios, APIs, autenticación federada, sincronización de datos, control de errores, trazabilidad de procesos o gestión de dependencias entre sistemas.** Como consecuencia, la solución permanece principalmente en un plano funcional y organizativo.

Tampoco se concretan para el requisito evaluado arquitecturas de referencia, diagramas funcionales, procedimientos específicos de integración, mecanismos de validación técnica o estrategias de verificación que permitan evaluar objetivamente la robustez de las soluciones propuestas. **Esta circunstancia limita de forma significativa la capacidad de acreditar experiencia especializada en entornos complejos de interoperabilidad.**

**La propuesta demuestra una comprensión adecuada del objetivo perseguido por el requisito y cubre formalmente el alcance funcional solicitado por el Documento de Invitación.** Sin embargo, la principal debilidad observada radica en la insuficiente concreción técnica de la solución planteada.

Como consecuencia de esta insuficiente concreción, no quedan suficientemente definidos los mecanismos de integración, procedimientos operativos, arquitecturas técnicas ni criterios de validación necesarios para acreditar con claridad la capacidad de ejecución de las actuaciones descritas.

Atendiendo a la escala de valoración establecida en el apartado 7.2.2 del Documento de Invitación, la calidad técnica observada se corresponde con el nivel **BAJA**.

- **Fortalezas y valor añadido**

La propuesta contempla actividades de análisis previo, identificación de necesidades, revisión de dependencias, desarrollo, validación y puesta en servicio de las modificaciones requeridas. **Esta secuencia de trabajo resulta coherente con la naturaleza general de los trabajos solicitados y permite apreciar una comprensión adecuada del ciclo de vida asociado a actuaciones de integración.**

**La propuesta demuestra una comprensión adecuada del objetivo perseguido por el requisito y cubre formalmente el alcance funcional solicitado por el Documento de Invitación.** Sin embargo, la principal debilidad observada radica en la insuficiente concreción técnica de la solución planteada.

- **Carencias, omisiones, errores o riesgos**

**No obstante, la profundidad técnica alcanzada resulta significativamente inferior a la complejidad real del requisito.** Aunque el Documento de Invitación identifica expresamente tecnologías y entornos de integración diversos (PHP, Python, Ruby, Java y Shell Script), la propuesta desarrolla escasamente los mecanismos técnicos asociados a dichas tecnologías y evita profundizar en las arquitecturas de integración necesarias para materializar las actuaciones previstas.

**La memoria incorpora referencias genéricas a desarrollos, modificaciones y adaptaciones, pero desarrolla de forma insuficiente aspectos relacionados con intercambio de información, diseño de servicios, APIs, autenticación federada, sincronización de datos, control de errores, trazabilidad de procesos o gestión de dependencias entre sistemas.** Como consecuencia, la solución permanece principalmente en un plano funcional y organizativo.

- **Valoración cualitativa**

- **BAJA**

#### EIPE2 — Modificaciones Front-End (HTML, CSS y JavaScript)

- **Requisito y alcance**

**El subproyecto EIPE2 se orienta a la realización de modificaciones frontend necesarias para garantizar la correcta integración de aplicaciones externas con la experiencia de usuario común de la plataforma EducaMadrid.** Estas actuaciones incluyen adaptaciones HTML, CSS y JavaScript que permitan mantener la coherencia visual, funcional y operativa entre los distintos servicios integrados.

**La propuesta presentada por empresa_n aborda correctamente el ámbito funcional definido para este subproyecto, reconociendo la necesidad de realizar adaptaciones frontend destinadas a mantener la coherencia visual y funcional entre aplicaciones externas y los servicios corporativos de EducaMadrid.** La memoria contempla actuaciones relacionadas con HTML, CSS y JavaScript, así como actividades de revisión, modificación y validación de elementos de interfaz.

La respuesta permite apreciar una comprensión adecuada del papel que desempeñan estas actuaciones dentro de una estrategia de integración orientada a ofrecer una experiencia homogénea a los usuarios de la plataforma.

- **Análisis de la propuesta**

**Sin perjuicio de lo anterior, la solución propuesta desarrolla de forma limitada los elementos técnicos que constituyen el núcleo del requisito.** La memoria incorpora referencias generales a modificaciones de interfaz y comportamiento visual, pero apenas desarrolla aspectos relacionados con frameworks frontend, componentes reutilizables, patrones de diseño, validación visual, accesibilidad, compatibilidad entre navegadores o mecanismos avanzados de control de calidad.

**Asimismo, la propuesta centra gran parte de su contenido en actividades de revisión, seguimiento y documentación, desarrollando en menor medida las soluciones tecnológicas concretas que permitirían alcanzar los objetivos funcionales planteados.** Tampoco se concretan para el requisito evaluado métricas, herramientas de validación, procedimientos de prueba o criterios de aceptación asociados a las actuaciones descritas.

Como consecuencia, la respuesta resulta coherente desde una perspectiva funcional, pero presenta un grado de especialización y desarrollo técnico inferior al esperado para un requisito centrado específicamente en integración y evolución frontend.

La propuesta cubre formalmente el alcance solicitado y demuestra comprender el objetivo general del subproyecto. **Sin embargo, la calidad técnica de la respuesta se ve limitada por la insuficiente definición de procedimientos específicos, herramientas, tecnologías y mecanismos verificables asociados a la ejecución de los trabajos.**

La limitada profundidad técnica observada impide considerar acreditado un nivel elevado de especialización en el ámbito de integración frontend y reduce significativamente la diferenciación de la propuesta respecto a una solución genérica de mantenimiento de interfaces.

Conforme a la escala de valoración prevista en el apartado 7.2.2 del Documento de Invitación, la respuesta se corresponde con el nivel **BAJA**.

- **Fortalezas y valor añadido**

**El subproyecto EIPE2 se orienta a la realización de modificaciones frontend necesarias para garantizar la correcta integración de aplicaciones externas con la experiencia de usuario común de la plataforma EducaMadrid.** Estas actuaciones incluyen adaptaciones HTML, CSS y JavaScript que permitan mantener la coherencia visual, funcional y operativa entre los distintos servicios integrados.

**La propuesta presentada por empresa_n aborda correctamente el ámbito funcional definido para este subproyecto, reconociendo la necesidad de realizar adaptaciones frontend destinadas a mantener la coherencia visual y funcional entre aplicaciones externas y los servicios corporativos de EducaMadrid.** La memoria contempla actuaciones relacionadas con HTML, CSS y JavaScript, así como actividades de revisión, modificación y validación de elementos de interfaz.

- **Carencias, omisiones, errores o riesgos**

**Sin perjuicio de lo anterior, la solución propuesta desarrolla de forma limitada los elementos técnicos que constituyen el núcleo del requisito.** La memoria incorpora referencias generales a modificaciones de interfaz y comportamiento visual, pero apenas desarrolla aspectos relacionados con frameworks frontend, componentes reutilizables, patrones de diseño, validación visual, accesibilidad, compatibilidad entre navegadores o mecanismos avanzados de control de calidad.

La propuesta cubre formalmente el alcance solicitado y demuestra comprender el objetivo general del subproyecto. **Sin embargo, la calidad técnica de la respuesta se ve limitada por la insuficiente definición de procedimientos específicos, herramientas, tecnologías y mecanismos verificables asociados a la ejecución de los trabajos.**

- **Valoración cualitativa**

- **BAJA**

#### Conclusión del bloque EIPE

El bloque presenta 0 subproyectos con desarrollo suficiente, 2 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **BAJA**.

### Proyectos de Sistemas Externos (ESIS)

- **Consideración general del bloque**

El bloque ESIS cubre el ciclo completo de incorporación, operación, mantenimiento, seguridad y evolución de proyectos exteriores: software base y bases de datos, consultoría, identidades, aprovisionamiento, configuración, integraciones corporativas, documentación, riesgos, continuidad, monitorización, ciberseguridad y gestión de infraestructura.

#### ESIS1 — Servicio de actualización del software base

- **Requisito y alcance**

El objeto de este subproyecto consiste en garantizar la actualización controlada del software base que soporta los distintos proyectos externos de EducaMadrid, asegurando la compatibilidad de componentes, la corrección de vulnerabilidades conocidas y la sostenibilidad tecnológica de las plataformas durante el ciclo de vida del contrato.

**La propuesta presentada por empresa_n identifica correctamente la necesidad de mantener actualizados los componentes de software base y reconoce la importancia de realizar dichas actualizaciones de forma controlada para minimizar riesgos operativos.** La memoria contempla actividades de revisión de versiones, análisis de compatibilidades y validaciones previas a la puesta en producción, evidenciando una comprensión adecuada de los objetivos perseguidos por la Administración. Asimismo, se incorpora una secuencia de trabajo identificable que incluye análisis previo, validación y despliegue controlado de los cambios previstos. Esta aproximación permite apreciar una cobertura funcional satisfactoria del requisito y una respuesta más desarrollada que la observada en otros subproyectos del bloque.

- **Análisis de la propuesta**

**La calidad de la propuesta resulta superior a la media del bloque al incorporar mecanismos explícitos de validación previa a la implantación de actualizaciones.** Estos elementos permiten reducir parte del riesgo inherente a las modificaciones sobre plataformas de explotación y aportan un cierto grado de estructuración metodológica. No obstante, la memoria continúa desarrollando de forma limitada aspectos especialmente relevantes como la automatización de despliegues, la gestión formal de cambios, los procedimientos de rollback, la definición de entornos de pruebas o la ejecución de planes de regresión avanzados. Aunque estas limitaciones reducen el alcance técnico de la solución, no impiden identificar una aportación diferencial respecto a los niveles mínimos exigidos por el Documento de Invitación.

**La propuesta ofrece una cobertura funcional adecuada, incorpora procedimientos identificables de validación y aporta un elemento de valor añadido expresamente reconocido en el Anexo II mediante la inclusión de validaciones previas estructuradas dentro del proceso de actualización.** Aunque el desarrollo técnico no alcanza niveles de especialización elevados, la solución se encuentra razonablemente definida y presenta una capacidad de ejecución verificable superior a la observada en la mayoría de los subproyectos del bloque ESIS. Por ello, la calidad global de la respuesta puede considerarse situada en un nivel superior al promedio del bloque.

La valoración propuesta no debe interpretarse como una acreditación de excelencia técnica completa del requisito. **Se reconoce la existencia de limitaciones relevantes en ámbitos como automatización, regresión avanzada, procedimientos de reversión y definición detallada de entornos.** No obstante, dentro del contexto específico del bloque ESIS, la propuesta presenta un nivel de estructuración superior al observado en la mayoría de los subproyectos analizados, incorporando mecanismos verificables de validación previa que permiten diferenciarla del patrón general de respuestas predominantemente descriptivas identificado en la oferta.

- **Fortalezas y valor añadido**

**La propuesta presentada por empresa_n identifica correctamente la necesidad de mantener actualizados los componentes de software base y reconoce la importancia de realizar dichas actualizaciones de forma controlada para minimizar riesgos operativos.** La memoria contempla actividades de revisión de versiones, análisis de compatibilidades y validaciones previas a la puesta en producción, evidenciando una comprensión adecuada de los objetivos perseguidos por la Administración. Asimismo, se incorpora una secuencia de trabajo identificable que incluye análisis previo, validación y despliegue controlado de los cambios previstos. Esta aproximación permite apreciar una cobertura funcional satisfactoria del requisito y una respuesta más desarrollada que la observada en otros subproyectos del bloque.

**La propuesta ofrece una cobertura funcional adecuada, incorpora procedimientos identificables de validación y aporta un elemento de valor añadido expresamente reconocido en el Anexo II mediante la inclusión de validaciones previas estructuradas dentro del proceso de actualización.** Aunque el desarrollo técnico no alcanza niveles de especialización elevados, la solución se encuentra razonablemente definida y presenta una capacidad de ejecución verificable superior a la observada en la mayoría de los subproyectos del bloque ESIS. Por ello, la calidad global de la respuesta puede considerarse situada en un nivel superior al promedio del bloque.

- **Carencias, omisiones, errores o riesgos**

**La calidad de la propuesta resulta superior a la media del bloque al incorporar mecanismos explícitos de validación previa a la implantación de actualizaciones.** Estos elementos permiten reducir parte del riesgo inherente a las modificaciones sobre plataformas de explotación y aportan un cierto grado de estructuración metodológica. No obstante, la memoria continúa desarrollando de forma limitada aspectos especialmente relevantes como la automatización de despliegues, la gestión formal de cambios, los procedimientos de rollback, la definición de entornos de pruebas o la ejecución de planes de regresión avanzados. Aunque estas limitaciones reducen el alcance técnico de la solución, no impiden identificar una aportación diferencial respecto a los niveles mínimos exigidos por el Documento de Invitación.

La valoración propuesta no debe interpretarse como una acreditación de excelencia técnica completa del requisito. **Se reconoce la existencia de limitaciones relevantes en ámbitos como automatización, regresión avanzada, procedimientos de reversión y definición detallada de entornos.** No obstante, dentro del contexto específico del bloque ESIS, la propuesta presenta un nivel de estructuración superior al observado en la mayoría de los subproyectos analizados, incorporando mecanismos verificables de validación previa que permiten diferenciarla del patrón general de respuestas predominantemente descriptivas identificado en la oferta.

- **Valoración cualitativa**

- **ALTA**

#### ESIS2 — Servicio de actualización del bases de datos

- **Requisito y alcance**

El requisito contempla la actualización de los distintos motores de bases de datos utilizados por los proyectos externos de EducaMadrid, garantizando la continuidad de servicio, la integridad de la información y la compatibilidad con las aplicaciones dependientes.

**La memoria presentada por empresa_n cubre adecuadamente el alcance funcional solicitado e identifica correctamente la necesidad de abordar las actualizaciones de los sistemas gestores de bases de datos mediante actuaciones planificadas y controladas.** La propuesta contempla tareas de revisión de compatibilidad, validación posterior a la actualización y seguimiento del comportamiento de los sistemas tras su implantación, demostrando una comprensión razonable de los riesgos asociados a este tipo de actuaciones. La solución mantiene además una orientación continua hacia la optimización de los entornos de persistencia, aspecto que se encuentra reflejado expresamente en la clasificación del Anexo I.

- **Análisis de la propuesta**

La respuesta desarrolla con mayor profundidad que otros apartados determinados aspectos relacionados con el mantenimiento evolutivo de las bases de datos, incorporando una visión continuada de optimización del entorno. **Sin embargo, subsisten limitaciones importantes relacionadas con la falta de detalle sobre procedimientos de migración compleja, estrategias de alta disponibilidad, replicación, recuperación ante errores o mecanismos específicos de minimización de indisponibilidades.** Asimismo, la memoria no desarrolla suficientemente cómo se abordarían las particularidades de los distintos motores de bases de datos presentes en el ecosistema tecnológico de EducaMadrid.

**Pese a las limitaciones señaladas, la propuesta proporciona una respuesta más desarrollada que la observada en la mayoría de los subproyectos clasificados como desarrollo deficiente y aporta además un elemento diferencial identificado en el Anexo II como valor añadido asociado a la optimización continua de los entornos de bases de datos.** La combinación de cobertura funcional adecuada, planteamiento técnico estructurado y aportación diferenciadora permite situar la valoración del requisito en un nivel superior al promedio del bloque.

**La valoración asignada responde a una comparación relativa con el resto de soluciones presentadas para el bloque ESIS y no a una consideración de completitud técnica absoluta.** Aunque la memoria no desarrolla con suficiente profundidad aspectos como la alta disponibilidad, la recuperación avanzada o las particularidades de cada motor de base de datos, sí incorpora una aproximación continuada a la revisión y optimización de los entornos de persistencia que, dentro del contexto general de la oferta, proporciona un grado de desarrollo superior al observado en una parte significativa de los requisitos analizados.

- **Fortalezas y valor añadido**

**La memoria presentada por empresa_n cubre adecuadamente el alcance funcional solicitado e identifica correctamente la necesidad de abordar las actualizaciones de los sistemas gestores de bases de datos mediante actuaciones planificadas y controladas.** La propuesta contempla tareas de revisión de compatibilidad, validación posterior a la actualización y seguimiento del comportamiento de los sistemas tras su implantación, demostrando una comprensión razonable de los riesgos asociados a este tipo de actuaciones. La solución mantiene además una orientación continua hacia la optimización de los entornos de persistencia, aspecto que se encuentra reflejado expresamente en la clasificación del Anexo I.

**Pese a las limitaciones señaladas, la propuesta proporciona una respuesta más desarrollada que la observada en la mayoría de los subproyectos clasificados como desarrollo deficiente y aporta además un elemento diferencial identificado en el Anexo II como valor añadido asociado a la optimización continua de los entornos de bases de datos.** La combinación de cobertura funcional adecuada, planteamiento técnico estructurado y aportación diferenciadora permite situar la valoración del requisito en un nivel superior al promedio del bloque.

- **Carencias, omisiones, errores o riesgos**

La respuesta desarrolla con mayor profundidad que otros apartados determinados aspectos relacionados con el mantenimiento evolutivo de las bases de datos, incorporando una visión continuada de optimización del entorno. **Sin embargo, subsisten limitaciones importantes relacionadas con la falta de detalle sobre procedimientos de migración compleja, estrategias de alta disponibilidad, replicación, recuperación ante errores o mecanismos específicos de minimización de indisponibilidades.** Asimismo, la memoria no desarrolla suficientemente cómo se abordarían las particularidades de los distintos motores de bases de datos presentes en el ecosistema tecnológico de EducaMadrid.

**Pese a las limitaciones señaladas, la propuesta proporciona una respuesta más desarrollada que la observada en la mayoría de los subproyectos clasificados como desarrollo deficiente y aporta además un elemento diferencial identificado en el Anexo II como valor añadido asociado a la optimización continua de los entornos de bases de datos.** La combinación de cobertura funcional adecuada, planteamiento técnico estructurado y aportación diferenciadora permite situar la valoración del requisito en un nivel superior al promedio del bloque.

- **Valoración cualitativa**

- **ALTA**

#### ESIS3 — Consultoría de integración

- **Requisito y alcance**

El objetivo de este subproyecto consiste en proporcionar soporte especializado para facilitar la integración de nuevas aplicaciones dentro del ecosistema tecnológico de EducaMadrid, garantizando la interoperabilidad entre sistemas heterogéneos y la adecuada incorporación de nuevos servicios a la arquitectura corporativa.

La propuesta contempla actividades de análisis, evaluación de necesidades e identificación de dependencias asociadas a procesos de integración tecnológica. La respuesta permite apreciar una comprensión general de la finalidad perseguida por el requisito y reconoce la importancia de garantizar la interoperabilidad entre servicios y aplicaciones externas. **Desde una perspectiva funcional, la cobertura puede considerarse adecuada, ya que la memoria identifica los principales ámbitos de actuación asociados a la consultoría de integración.**

- **Análisis de la propuesta**

**No obstante, el desarrollo técnico aportado resulta claramente insuficiente para un requisito cuya principal aportación de valor reside precisamente en la especialización arquitectónica y metodológica.** La memoria formula la mayor parte de sus planteamientos en términos generales, limitándose a describir actividades de consultoría, análisis y acompañamiento sin desarrollar arquitecturas de referencia, patrones de integración, modelos de interoperabilidad, mecanismos de autenticación, estrategias de sincronización o procedimientos específicos de validación técnica. Tampoco se identifican herramientas concretas ni entregables especializados que permitan valorar favorablemente la calidad de la solución. Además, el Anexo II clasifica expresamente este subproyecto como propuesta técnica incluida con desarrollo deficiente y sin valor añadido asociado.

La propuesta cubre el requisito desde una perspectiva funcional, pero no alcanza el nivel de profundidad técnica exigible para una actividad de consultoría especializada. **La ausencia de arquitecturas detalladas, metodologías específicas y mecanismos verificables limita significativamente la capacidad de acreditar experiencia diferencial en entornos complejos de integración.** Considerando la clasificación recogida en el Anexo II y la limitada concreción observada en la memoria, la calidad global de la respuesta se corresponde con un nivel BAJO.

- **Fortalezas y valor añadido**

El objetivo de este subproyecto consiste en proporcionar soporte especializado para facilitar la integración de nuevas aplicaciones dentro del ecosistema tecnológico de EducaMadrid, garantizando la interoperabilidad entre sistemas heterogéneos y la adecuada incorporación de nuevos servicios a la arquitectura corporativa.

La propuesta contempla actividades de análisis, evaluación de necesidades e identificación de dependencias asociadas a procesos de integración tecnológica. La respuesta permite apreciar una comprensión general de la finalidad perseguida por el requisito y reconoce la importancia de garantizar la interoperabilidad entre servicios y aplicaciones externas. **Desde una perspectiva funcional, la cobertura puede considerarse adecuada, ya que la memoria identifica los principales ámbitos de actuación asociados a la consultoría de integración.**

- **Carencias, omisiones, errores o riesgos**

**No obstante, el desarrollo técnico aportado resulta claramente insuficiente para un requisito cuya principal aportación de valor reside precisamente en la especialización arquitectónica y metodológica.** La memoria formula la mayor parte de sus planteamientos en términos generales, limitándose a describir actividades de consultoría, análisis y acompañamiento sin desarrollar arquitecturas de referencia, patrones de integración, modelos de interoperabilidad, mecanismos de autenticación, estrategias de sincronización o procedimientos específicos de validación técnica. Tampoco se identifican herramientas concretas ni entregables especializados que permitan valorar favorablemente la calidad de la solución. Además, el Anexo II clasifica expresamente este subproyecto como propuesta técnica incluida con desarrollo deficiente y sin valor añadido asociado.

La propuesta cubre el requisito desde una perspectiva funcional, pero no alcanza el nivel de profundidad técnica exigible para una actividad de consultoría especializada. **La ausencia de arquitecturas detalladas, metodologías específicas y mecanismos verificables limita significativamente la capacidad de acreditar experiencia diferencial en entornos complejos de integración.** Considerando la clasificación recogida en el Anexo II y la limitada concreción observada en la memoria, la calidad global de la respuesta se corresponde con un nivel BAJO.

- **Valoración cualitativa**

- **BAJA**

#### ESIS4 — Consultoría de ciberseguridad

- **Requisito y alcance**

El objeto de este subproyecto consiste en proporcionar asesoramiento especializado en materia de ciberseguridad para los proyectos externos que deban integrarse o desplegarse dentro de EducaMadrid, garantizando el cumplimiento de los requisitos de seguridad aplicables y la correcta gestión del riesgo tecnológico.

**La memoria contempla actividades vinculadas a la identificación de riesgos, revisión de configuraciones y análisis general del estado de seguridad de los sistemas afectados.** La propuesta demuestra comprender que la ciberseguridad debe integrarse dentro del ciclo de vida de los proyectos y reconoce la necesidad de incorporar controles preventivos desde las fases iniciales de diseño e implantación. Desde la perspectiva funcional, la cobertura del requisito puede considerarse adecuada.

- **Análisis de la propuesta**

Pese a ello, la solución permanece situada en un plano principalmente conceptual. **Las referencias a análisis de riesgos, revisión de configuraciones o evaluación de seguridad aparecen formuladas mediante términos generales y no se desarrollan metodologías concretas de auditoría, marcos de referencia aplicables, procedimientos técnicos de evaluación, herramientas de análisis o mecanismos verificables de seguimiento.** La propuesta reproduce en gran medida los objetivos perseguidos por el Documento de Invitación sin desarrollar con suficiente detalle los medios técnicos mediante los cuales dichos objetivos serían alcanzados. Esta circunstancia resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

**Aunque la comprensión de la finalidad del servicio resulta adecuada, la escasa profundidad metodológica y la ausencia de planteamientos especializados limitan considerablemente la capacidad de valorar favorablemente el requisito.** La respuesta no aporta elementos diferenciales que permitan acreditar un nivel técnico elevado de consultoría de seguridad y se ajusta claramente a los criterios correspondientes a una valoración BAJA.

- **Fortalezas y valor añadido**

**La memoria contempla actividades vinculadas a la identificación de riesgos, revisión de configuraciones y análisis general del estado de seguridad de los sistemas afectados.** La propuesta demuestra comprender que la ciberseguridad debe integrarse dentro del ciclo de vida de los proyectos y reconoce la necesidad de incorporar controles preventivos desde las fases iniciales de diseño e implantación. Desde la perspectiva funcional, la cobertura del requisito puede considerarse adecuada.

Pese a ello, la solución permanece situada en un plano principalmente conceptual. **Las referencias a análisis de riesgos, revisión de configuraciones o evaluación de seguridad aparecen formuladas mediante términos generales y no se desarrollan metodologías concretas de auditoría, marcos de referencia aplicables, procedimientos técnicos de evaluación, herramientas de análisis o mecanismos verificables de seguimiento.** La propuesta reproduce en gran medida los objetivos perseguidos por el Documento de Invitación sin desarrollar con suficiente detalle los medios técnicos mediante los cuales dichos objetivos serían alcanzados. Esta circunstancia resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

- **Carencias, omisiones, errores o riesgos**

Pese a ello, la solución permanece situada en un plano principalmente conceptual. **Las referencias a análisis de riesgos, revisión de configuraciones o evaluación de seguridad aparecen formuladas mediante términos generales y no se desarrollan metodologías concretas de auditoría, marcos de referencia aplicables, procedimientos técnicos de evaluación, herramientas de análisis o mecanismos verificables de seguimiento.** La propuesta reproduce en gran medida los objetivos perseguidos por el Documento de Invitación sin desarrollar con suficiente detalle los medios técnicos mediante los cuales dichos objetivos serían alcanzados. Esta circunstancia resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

**Aunque la comprensión de la finalidad del servicio resulta adecuada, la escasa profundidad metodológica y la ausencia de planteamientos especializados limitan considerablemente la capacidad de valorar favorablemente el requisito.** La respuesta no aporta elementos diferenciales que permitan acreditar un nivel técnico elevado de consultoría de seguridad y se ajusta claramente a los criterios correspondientes a una valoración BAJA.

- **Valoración cualitativa**

- **BAJA**

#### ESIS5 — Actualización de la autenticación centralizada de usuarios

- **Requisito y alcance**

**Este subproyecto persigue la evolución de los mecanismos corporativos de autenticación con objeto de garantizar su compatibilidad con las necesidades futuras de la plataforma, mantener un nivel adecuado de seguridad y asegurar la integración homogénea de los distintos servicios que forman parte del ecosistema EducaMadrid.** La criticidad de este requisito resulta especialmente elevada al constituir la autenticación uno de los servicios transversales más sensibles para el correcto funcionamiento de los sistemas corporativos.

La propuesta presentada por empresa_n identifica correctamente la relevancia de los sistemas corporativos de identidad y contempla actuaciones orientadas a la actualización de los componentes asociados al acceso de usuarios. **La memoria reconoce la necesidad de preservar la continuidad del servicio durante los procesos de evolución tecnológica y pone de manifiesto una comprensión adecuada de la función estratégica que desempeñan los mecanismos de autenticación dentro de la plataforma.** Asimismo, se describen actividades de revisión, actualización y validación funcional posteriores a la implantación de cambios, manteniendo una cobertura funcional compatible con el alcance establecido en el Documento de Invitación.

- **Análisis de la propuesta**

**A pesar de la cobertura funcional observada, la calidad técnica de la solución resulta limitada.** La memoria desarrolla escasamente aquellos aspectos que constituyen precisamente el núcleo tecnológico del requisito, tales como los procedimientos de migración entre versiones, la gestión de identidades federadas, los mecanismos de interoperabilidad con aplicaciones externas, la gestión avanzada del ciclo de vida de las credenciales o la adaptación de los sistemas de autenticación a nuevos requisitos tecnológicos. La mayor parte del contenido permanece formulada mediante actividades de supervisión, revisión y actualización, sin ofrecer una descripción suficientemente desarrollada de los procedimientos técnicos específicos mediante los cuales se ejecutarían las actuaciones previstas.

**Adicionalmente, el Anexo II clasifica este subproyecto como propuesta técnica incluida con desarrollo deficiente y sin valor añadido identificable.** La memoria tampoco incorpora mejoras diferenciales que permitan considerar que la propuesta supera significativamente los mínimos funcionales del Documento de Invitación.

**La solución acredita una comprensión adecuada del objetivo del requisito y proporciona una cobertura funcional aceptable.** Sin embargo, la ausencia de una definición detallada de los mecanismos de implantación, la limitada especialización técnica observada y la inexistencia de elementos de valor añadido verificables impiden considerar que la calidad de la respuesta alcance niveles superiores. Conforme al modelo de valoración aplicado, la solución se corresponde con un nivel BAJO.

- **Fortalezas y valor añadido**

**Este subproyecto persigue la evolución de los mecanismos corporativos de autenticación con objeto de garantizar su compatibilidad con las necesidades futuras de la plataforma, mantener un nivel adecuado de seguridad y asegurar la integración homogénea de los distintos servicios que forman parte del ecosistema EducaMadrid.** La criticidad de este requisito resulta especialmente elevada al constituir la autenticación uno de los servicios transversales más sensibles para el correcto funcionamiento de los sistemas corporativos.

La propuesta presentada por empresa_n identifica correctamente la relevancia de los sistemas corporativos de identidad y contempla actuaciones orientadas a la actualización de los componentes asociados al acceso de usuarios. **La memoria reconoce la necesidad de preservar la continuidad del servicio durante los procesos de evolución tecnológica y pone de manifiesto una comprensión adecuada de la función estratégica que desempeñan los mecanismos de autenticación dentro de la plataforma.** Asimismo, se describen actividades de revisión, actualización y validación funcional posteriores a la implantación de cambios, manteniendo una cobertura funcional compatible con el alcance establecido en el Documento de Invitación.

- **Carencias, omisiones, errores o riesgos**

**A pesar de la cobertura funcional observada, la calidad técnica de la solución resulta limitada.** La memoria desarrolla escasamente aquellos aspectos que constituyen precisamente el núcleo tecnológico del requisito, tales como los procedimientos de migración entre versiones, la gestión de identidades federadas, los mecanismos de interoperabilidad con aplicaciones externas, la gestión avanzada del ciclo de vida de las credenciales o la adaptación de los sistemas de autenticación a nuevos requisitos tecnológicos. La mayor parte del contenido permanece formulada mediante actividades de supervisión, revisión y actualización, sin ofrecer una descripción suficientemente desarrollada de los procedimientos técnicos específicos mediante los cuales se ejecutarían las actuaciones previstas.

**La solución acredita una comprensión adecuada del objetivo del requisito y proporciona una cobertura funcional aceptable.** Sin embargo, la ausencia de una definición detallada de los mecanismos de implantación, la limitada especialización técnica observada y la inexistencia de elementos de valor añadido verificables impiden considerar que la calidad de la respuesta alcance niveles superiores. Conforme al modelo de valoración aplicado, la solución se corresponde con un nivel BAJO.

- **Valoración cualitativa**

- **BAJA**

#### ESIS6 — Mantenimiento de la autenticación centralizada de usuarios

- **Requisito y alcance**

La finalidad de este subproyecto consiste en garantizar la operación continuada de los sistemas corporativos de autenticación, gestionando incidencias, realizando seguimiento del servicio y preservando la disponibilidad de la infraestructura de identidad utilizada por EducaMadrid.

La propuesta contempla actuaciones de supervisión, mantenimiento correctivo, seguimiento operativo y asistencia técnica asociadas al funcionamiento ordinario de los sistemas de autenticación corporativos. **La memoria reconoce adecuadamente el carácter crítico de estos servicios y la necesidad de mantener elevados niveles de disponibilidad para evitar impactos generalizados sobre el conjunto de aplicaciones integradas.** Desde una perspectiva funcional, la respuesta cubre adecuadamente los objetivos perseguidos por el Documento de Invitación.

- **Análisis de la propuesta**

**No obstante, el contenido desarrollado continúa presentando un elevado grado de generalidad.** Las actividades descritas se formulan principalmente en términos de seguimiento, soporte y mantenimiento, sin desarrollar mecanismos específicos de monitorización avanzada, indicadores de disponibilidad, modelos de escalado operativo, herramientas de diagnóstico o procedimientos estructurados de resolución de incidencias. Tampoco se describen métricas verificables que permitan medir objetivamente el rendimiento del servicio o la eficacia de las actuaciones previstas.

La documentación aportada no incorpora elementos diferenciales que permitan considerar la existencia de una metodología especialmente avanzada para la operación de infraestructuras de identidad, circunstancia que resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

La propuesta cubre formalmente el requisito y evidencia comprender las necesidades operativas asociadas al mantenimiento de los sistemas de autenticación. **Sin embargo, la limitada profundidad técnica y la falta de mecanismos verificables reducen significativamente la capacidad de acreditar una especialización diferencial respecto a una prestación estándar de soporte.** Por ello, la calidad global de la solución se corresponde con una valoración BAJA.

- **Fortalezas y valor añadido**

La propuesta contempla actuaciones de supervisión, mantenimiento correctivo, seguimiento operativo y asistencia técnica asociadas al funcionamiento ordinario de los sistemas de autenticación corporativos. **La memoria reconoce adecuadamente el carácter crítico de estos servicios y la necesidad de mantener elevados niveles de disponibilidad para evitar impactos generalizados sobre el conjunto de aplicaciones integradas.** Desde una perspectiva funcional, la respuesta cubre adecuadamente los objetivos perseguidos por el Documento de Invitación.

La documentación aportada no incorpora elementos diferenciales que permitan considerar la existencia de una metodología especialmente avanzada para la operación de infraestructuras de identidad, circunstancia que resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el contenido desarrollado continúa presentando un elevado grado de generalidad.** Las actividades descritas se formulan principalmente en términos de seguimiento, soporte y mantenimiento, sin desarrollar mecanismos específicos de monitorización avanzada, indicadores de disponibilidad, modelos de escalado operativo, herramientas de diagnóstico o procedimientos estructurados de resolución de incidencias. Tampoco se describen métricas verificables que permitan medir objetivamente el rendimiento del servicio o la eficacia de las actuaciones previstas.

La propuesta cubre formalmente el requisito y evidencia comprender las necesidades operativas asociadas al mantenimiento de los sistemas de autenticación. **Sin embargo, la limitada profundidad técnica y la falta de mecanismos verificables reducen significativamente la capacidad de acreditar una especialización diferencial respecto a una prestación estándar de soporte.** Por ello, la calidad global de la solución se corresponde con una valoración BAJA.

- **Valoración cualitativa**

- **BAJA**

#### ESIS7 — Gestión de servicios para la sincronización de usuarios

- **Requisito y alcance**

Este subproyecto tiene por objeto garantizar la coherencia de identidades entre aplicaciones heterogéneas mediante la correcta sincronización de usuarios, grupos y atributos, preservando la consistencia de la información gestionada por los distintos sistemas integrados dentro de EducaMadrid.

La memoria presentada por empresa_n identifica correctamente la necesidad de asegurar la sincronización de identidades y contempla actividades orientadas a revisar la consistencia de los datos y validar la correcta propagación de cambios entre sistemas. La propuesta demuestra comprender la finalidad general del requisito y reconoce la importancia de mantener la coherencia de la información de acceso en entornos integrados. **Desde una perspectiva funcional, puede considerarse que la cobertura ofrecida resulta suficiente.**

- **Análisis de la propuesta**

**La principal limitación observada reside en la escasa concreción técnica de la solución propuesta.** La memoria describe de forma genérica los objetivos perseguidos, pero no desarrolla con suficiente detalle los procesos de sincronización, los mecanismos de resolución de conflictos, las estrategias de reconciliación de identidades, la gestión de errores ni los procedimientos de auditoría necesarios para garantizar la trazabilidad de las operaciones realizadas.

La respuesta permanece situada en un plano eminentemente conceptual, sin que sea posible identificar arquitecturas, herramientas especializadas o procedimientos operativos que permitan verificar objetivamente la viabilidad de los planteamientos descritos. **Esta circunstancia resulta plenamente coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.**

**La propuesta demuestra comprender la necesidad de mantener la coherencia de identidades, pero no desarrolla suficientemente los mecanismos técnicos necesarios para llevar a cabo dicha tarea en un entorno complejo y altamente integrado como EducaMadrid.** La falta de detalle metodológico y la escasa especialización observada justifican una valoración BAJA.

- **Fortalezas y valor añadido**

Este subproyecto tiene por objeto garantizar la coherencia de identidades entre aplicaciones heterogéneas mediante la correcta sincronización de usuarios, grupos y atributos, preservando la consistencia de la información gestionada por los distintos sistemas integrados dentro de EducaMadrid.

La memoria presentada por empresa_n identifica correctamente la necesidad de asegurar la sincronización de identidades y contempla actividades orientadas a revisar la consistencia de los datos y validar la correcta propagación de cambios entre sistemas. La propuesta demuestra comprender la finalidad general del requisito y reconoce la importancia de mantener la coherencia de la información de acceso en entornos integrados. **Desde una perspectiva funcional, puede considerarse que la cobertura ofrecida resulta suficiente.**

- **Carencias, omisiones, errores o riesgos**

**La principal limitación observada reside en la escasa concreción técnica de la solución propuesta.** La memoria describe de forma genérica los objetivos perseguidos, pero no desarrolla con suficiente detalle los procesos de sincronización, los mecanismos de resolución de conflictos, las estrategias de reconciliación de identidades, la gestión de errores ni los procedimientos de auditoría necesarios para garantizar la trazabilidad de las operaciones realizadas.

**La propuesta demuestra comprender la necesidad de mantener la coherencia de identidades, pero no desarrolla suficientemente los mecanismos técnicos necesarios para llevar a cabo dicha tarea en un entorno complejo y altamente integrado como EducaMadrid.** La falta de detalle metodológico y la escasa especialización observada justifican una valoración BAJA.

- **Valoración cualitativa**

- **BAJA**

#### ESIS8 — Supervisión de usuarios de aplicaciones externas

- **Requisito y alcance**

El objetivo de este subproyecto consiste en supervisar los usuarios gestionados por aplicaciones externas integradas en EducaMadrid, garantizando la adecuada gestión de permisos, roles y mecanismos de acceso asociados a dichos servicios.

**La propuesta contempla actividades relacionadas con la supervisión de cuentas de usuario, revisión de permisos y validación de la información gestionada por aplicaciones externas.** La memoria permite apreciar una comprensión razonable de las necesidades generales asociadas al control de identidades y al mantenimiento de la coherencia de acceso entre sistemas heterogéneos. La cobertura funcional del requisito puede considerarse suficiente.

- **Análisis de la propuesta**

**No obstante, la solución desarrollada permanece en un nivel principalmente operativo y organizativo.** La documentación incorporada describe actividades de revisión y supervisión, pero no desarrolla procedimientos automatizados, modelos de detección de anomalías, mecanismos de correlación de eventos, herramientas de auditoría avanzada ni indicadores objetivos que permitan valorar favorablemente la calidad técnica de la propuesta.

El análisis realizado tampoco permite identificar elementos diferenciales que evidencien un conocimiento especialmente profundo de la problemática asociada a la gestión de usuarios en entornos distribuidos. **La respuesta se limita esencialmente a reproducir las actividades básicas asociadas al requisito, circunstancia que resulta coherente con la clasificación de desarrollo deficiente establecida en el Anexo I.**

**La propuesta proporciona una cobertura funcional razonable del requisito, pero su limitado desarrollo técnico, la ausencia de procedimientos verificables y la inexistencia de elementos de valor añadido reducen significativamente la calidad global de la solución.** En consecuencia, la valoración se corresponde con un nivel BAJO.

- **Fortalezas y valor añadido**

El objetivo de este subproyecto consiste en supervisar los usuarios gestionados por aplicaciones externas integradas en EducaMadrid, garantizando la adecuada gestión de permisos, roles y mecanismos de acceso asociados a dichos servicios.

**La propuesta contempla actividades relacionadas con la supervisión de cuentas de usuario, revisión de permisos y validación de la información gestionada por aplicaciones externas.** La memoria permite apreciar una comprensión razonable de las necesidades generales asociadas al control de identidades y al mantenimiento de la coherencia de acceso entre sistemas heterogéneos. La cobertura funcional del requisito puede considerarse suficiente.

- **Carencias, omisiones, errores o riesgos**

**No obstante, la solución desarrollada permanece en un nivel principalmente operativo y organizativo.** La documentación incorporada describe actividades de revisión y supervisión, pero no desarrolla procedimientos automatizados, modelos de detección de anomalías, mecanismos de correlación de eventos, herramientas de auditoría avanzada ni indicadores objetivos que permitan valorar favorablemente la calidad técnica de la propuesta.

El análisis realizado tampoco permite identificar elementos diferenciales que evidencien un conocimiento especialmente profundo de la problemática asociada a la gestión de usuarios en entornos distribuidos. **La respuesta se limita esencialmente a reproducir las actividades básicas asociadas al requisito, circunstancia que resulta coherente con la clasificación de desarrollo deficiente establecida en el Anexo I.**

- **Valoración cualitativa**

- **BAJA**

#### ESIS9 — Soporte técnico en entornos de preproducción

- **Requisito y alcance**

La finalidad de este subproyecto consiste en proporcionar soporte técnico especializado a los entornos de preproducción utilizados para validar nuevas aplicaciones y nuevas versiones antes de su incorporación a producción, minimizando riesgos y garantizando la calidad de las implantaciones.

La memoria contempla actuaciones de acompañamiento, validación y soporte asociadas al proceso de incorporación de nuevos desarrollos a la plataforma EducaMadrid. **La propuesta reconoce adecuadamente el papel que desempeñan los entornos de preproducción en la reducción del riesgo operativo y en la detección temprana de problemas funcionales y técnicos.** Desde esta perspectiva, la cobertura funcional puede considerarse adecuada.

- **Análisis de la propuesta**

**Sin embargo, la respuesta mantiene el mismo patrón observado en numerosos subproyectos del bloque ESIS.** La memoria describe los objetivos perseguidos por el requisito, pero desarrolla de forma insuficiente los mecanismos concretos mediante los cuales se realizarán las validaciones. No se describen planes de prueba, procedimientos de aceptación, automatización de validaciones, gobernanza de despliegues ni criterios formales de certificación de las aplicaciones analizadas.

La propuesta tampoco incorpora metodologías específicas que permitan acreditar una madurez operativa superior a la requerida para una prestación básica de soporte. **En consecuencia, la calidad técnica de la respuesta continúa siendo limitada y resulta coherente con la clasificación de desarrollo deficiente reflejada en el Anexo I.**

**La propuesta cubre adecuadamente la finalidad funcional del requisito, pero la limitada definición de procedimientos verificables impide valorar favorablemente la capacidad real de ejecución de las actuaciones descritas.** La ausencia de metodologías formales de validación y control justifica una valoración BAJA.

- **Fortalezas y valor añadido**

La memoria contempla actuaciones de acompañamiento, validación y soporte asociadas al proceso de incorporación de nuevos desarrollos a la plataforma EducaMadrid. **La propuesta reconoce adecuadamente el papel que desempeñan los entornos de preproducción en la reducción del riesgo operativo y en la detección temprana de problemas funcionales y técnicos.** Desde esta perspectiva, la cobertura funcional puede considerarse adecuada.

La propuesta tampoco incorpora metodologías específicas que permitan acreditar una madurez operativa superior a la requerida para una prestación básica de soporte. **En consecuencia, la calidad técnica de la respuesta continúa siendo limitada y resulta coherente con la clasificación de desarrollo deficiente reflejada en el Anexo I.**

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, la respuesta mantiene el mismo patrón observado en numerosos subproyectos del bloque ESIS.** La memoria describe los objetivos perseguidos por el requisito, pero desarrolla de forma insuficiente los mecanismos concretos mediante los cuales se realizarán las validaciones. No se describen planes de prueba, procedimientos de aceptación, automatización de validaciones, gobernanza de despliegues ni criterios formales de certificación de las aplicaciones analizadas.

La propuesta tampoco incorpora metodologías específicas que permitan acreditar una madurez operativa superior a la requerida para una prestación básica de soporte. **En consecuencia, la calidad técnica de la respuesta continúa siendo limitada y resulta coherente con la clasificación de desarrollo deficiente reflejada en el Anexo I.**

- **Valoración cualitativa**

- **BAJA**

#### ESIS10 — Despliegue de aplicaciones externas en producción

- **Requisito y alcance**

Este subproyecto contempla las actividades necesarias para implantar nuevas aplicaciones y nuevas versiones de aplicaciones existentes dentro de los entornos de producción de EducaMadrid, garantizando la continuidad de servicio y minimizando el impacto asociado a los cambios.

**La propuesta identifica correctamente la necesidad de coordinar despliegues, validar resultados y supervisar la incorporación de cambios a los entornos productivos.** La memoria evidencia comprender la importancia de preservar la estabilidad de los servicios durante los procesos de implantación y reconoce la necesidad de realizar verificaciones posteriores a la puesta en producción. La cobertura funcional puede considerarse adecuada.

- **Análisis de la propuesta**

**A pesar de dicha cobertura, la profundidad técnica observada resulta limitada.** La documentación presentada apenas desarrolla procedimientos de control de versiones, metodologías de despliegue progresivo, mecanismos de reversión, automatización de implantaciones o modelos avanzados de validación post-despliegue. Las actividades descritas permanecen formuladas en términos generales, reproduciendo en buena medida los objetivos perseguidos por el Documento de Invitación sin desarrollar suficientemente la forma concreta en que dichos objetivos serían alcanzados.

La propuesta tampoco incorpora elementos de mejora o valor añadido identificados en el Anexo II y queda clasificada como una propuesta técnica incluida con desarrollo deficiente.

**Aunque la comprensión funcional del requisito resulta adecuada, la limitada definición metodológica y la ausencia de procedimientos técnicos verificables reducen significativamente la calidad de la respuesta.** La solución no aporta evidencias suficientes para acreditar una capacidad diferencial de gestión de despliegues complejos y, por ello, se corresponde con una valoración BAJA.

- **Fortalezas y valor añadido**

**La propuesta identifica correctamente la necesidad de coordinar despliegues, validar resultados y supervisar la incorporación de cambios a los entornos productivos.** La memoria evidencia comprender la importancia de preservar la estabilidad de los servicios durante los procesos de implantación y reconoce la necesidad de realizar verificaciones posteriores a la puesta en producción. La cobertura funcional puede considerarse adecuada.

**A pesar de dicha cobertura, la profundidad técnica observada resulta limitada.** La documentación presentada apenas desarrolla procedimientos de control de versiones, metodologías de despliegue progresivo, mecanismos de reversión, automatización de implantaciones o modelos avanzados de validación post-despliegue. Las actividades descritas permanecen formuladas en términos generales, reproduciendo en buena medida los objetivos perseguidos por el Documento de Invitación sin desarrollar suficientemente la forma concreta en que dichos objetivos serían alcanzados.

- **Carencias, omisiones, errores o riesgos**

**A pesar de dicha cobertura, la profundidad técnica observada resulta limitada.** La documentación presentada apenas desarrolla procedimientos de control de versiones, metodologías de despliegue progresivo, mecanismos de reversión, automatización de implantaciones o modelos avanzados de validación post-despliegue. Las actividades descritas permanecen formuladas en términos generales, reproduciendo en buena medida los objetivos perseguidos por el Documento de Invitación sin desarrollar suficientemente la forma concreta en que dichos objetivos serían alcanzados.

**Aunque la comprensión funcional del requisito resulta adecuada, la limitada definición metodológica y la ausencia de procedimientos técnicos verificables reducen significativamente la calidad de la respuesta.** La solución no aporta evidencias suficientes para acreditar una capacidad diferencial de gestión de despliegues complejos y, por ello, se corresponde con una valoración BAJA.

- **Valoración cualitativa**

- **BAJA**

#### ESIS11 — Integración en el Gestor de Servidores de Bases de Datos

- **Requisito y alcance**

Este subproyecto tiene por finalidad garantizar la integración de las aplicaciones externas con los servicios corporativos de gestión de bases de datos utilizados por EducaMadrid, asegurando la correcta interoperabilidad entre plataformas y la aplicación homogénea de los criterios de explotación establecidos por la organización.

**El análisis de la memoria técnica no permite identificar una propuesta específica que responda de forma directa al alcance solicitado para este subproyecto.** Aunque en distintos apartados del documento se realizan referencias genéricas a la gestión de bases de datos, dichas referencias aparecen integradas en explicaciones de carácter general sobre operación o mantenimiento y no constituyen una solución técnica diferenciada para la integración con el gestor corporativo requerido. La documentación presentada no desarrolla procesos, arquitectura, mecanismos de conexión ni procedimientos que permitan establecer una trazabilidad clara entre el requisito formulado en el Documento de Invitación y la respuesta ofertada.

- **Análisis de la propuesta**

**La ausencia de una propuesta específica impide analizar aspectos como viabilidad técnica, mecanismos de ejecución, herramientas previstas o procedimientos de implantación.** No resulta posible identificar una respuesta evaluable que permita determinar el nivel de conocimiento del entorno requerido ni valorar la capacidad de ejecución del servicio solicitado. Esta situación coincide con la clasificación recogida en el Anexo I, donde el subproyecto figura expresamente como propuesta técnica no incluida.

Al no existir una solución técnica concreta asociada al requisito, no es posible verificar la existencia de mecanismos de implementación, procedimientos operativos o elementos diferenciales susceptibles de valoración. **La ausencia de respuesta específica limita completamente la capacidad de análisis y sitúa el subproyecto en el nivel más bajo de la escala de valoración.**

- **Fortalezas y valor añadido**

Se reconoce la cobertura formal del requisito en los términos descritos en la memoria.

- **Carencias, omisiones, errores o riesgos**

**La ausencia de una propuesta específica impide analizar aspectos como viabilidad técnica, mecanismos de ejecución, herramientas previstas o procedimientos de implantación.** No resulta posible identificar una respuesta evaluable que permita determinar el nivel de conocimiento del entorno requerido ni valorar la capacidad de ejecución del servicio solicitado. Esta situación coincide con la clasificación recogida en el Anexo I, donde el subproyecto figura expresamente como propuesta técnica no incluida.

Al no existir una solución técnica concreta asociada al requisito, no es posible verificar la existencia de mecanismos de implementación, procedimientos operativos o elementos diferenciales susceptibles de valoración. **La ausencia de respuesta específica limita completamente la capacidad de análisis y sitúa el subproyecto en el nivel más bajo de la escala de valoración.**

- **Valoración cualitativa**

- **MUY BAJA**

#### ESIS12 — Estudio de los recursos solicitados

- **Requisito y alcance**

Este subproyecto contempla el análisis de las necesidades de capacidad de los proyectos externos con objeto de dimensionar adecuadamente los recursos de infraestructura requeridos para su despliegue y explotación dentro del ecosistema EducaMadrid.

**La memoria identifica la necesidad de realizar estudios previos de capacidad y contempla actividades de análisis orientadas a determinar los recursos necesarios para soportar nuevas aplicaciones o ampliaciones de las existentes.** La propuesta demuestra comprender la finalidad general del requisito y reconoce la importancia de anticipar las necesidades de infraestructura antes de la implantación de nuevos servicios.

- **Análisis de la propuesta**

**Pese a ello, el desarrollo técnico aportado resulta claramente limitado.** La documentación no describe metodologías específicas de capacity planning, herramientas de monitorización destinadas a la estimación de carga, modelos predictivos, indicadores de consumo o procedimientos de validación que permitan justificar técnicamente las estimaciones realizadas. La respuesta permanece formulada en términos genéricos y reproduce esencialmente el objetivo perseguido por el propio requisito sin profundizar en los mecanismos necesarios para ejecutarlo de forma efectiva.

Esta falta de concreción resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

**Aunque existe una propuesta identificable y funcionalmente alineada con el requisito, la ausencia de metodología específica y de mecanismos verificables limita significativamente la calidad técnica de la solución.** La respuesta permite acreditar comprensión del objetivo, pero no demuestra un nivel suficiente de especialización en materia de dimensionamiento de infraestructuras.

- **Fortalezas y valor añadido**

Este subproyecto contempla el análisis de las necesidades de capacidad de los proyectos externos con objeto de dimensionar adecuadamente los recursos de infraestructura requeridos para su despliegue y explotación dentro del ecosistema EducaMadrid.

Esta falta de concreción resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

- **Carencias, omisiones, errores o riesgos**

**Pese a ello, el desarrollo técnico aportado resulta claramente limitado.** La documentación no describe metodologías específicas de capacity planning, herramientas de monitorización destinadas a la estimación de carga, modelos predictivos, indicadores de consumo o procedimientos de validación que permitan justificar técnicamente las estimaciones realizadas. La respuesta permanece formulada en términos genéricos y reproduce esencialmente el objetivo perseguido por el propio requisito sin profundizar en los mecanismos necesarios para ejecutarlo de forma efectiva.

Esta falta de concreción resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

- **Valoración cualitativa**

- **BAJA**

#### ESIS13 — Solicitud de los recursos necesarios

- **Requisito y alcance**

La finalidad de este subproyecto consiste en gestionar las peticiones de creación, ampliación, modificación o retirada de recursos de infraestructura asociados a los distintos servicios externos integrados dentro de EducaMadrid.

**La propuesta contempla actividades relacionadas con la recepción, análisis y tramitación de solicitudes de recursos, evidenciando comprender la necesidad de establecer mecanismos ordenados de provisión y seguimiento.** La memoria recoge la existencia de procesos de coordinación y gestión que permiten apreciar una cobertura funcional razonable del alcance solicitado.

- **Análisis de la propuesta**

**Sin embargo, la documentación no define flujos de aprobación, circuitos de gestión, criterios de priorización, procedimientos de validación ni modelos de gobernanza que permitan evaluar de manera objetiva la calidad de la solución planteada.** Las actividades descritas se encuentran formuladas de forma muy genérica y no incorporan elementos metodológicos diferenciales que permitan distinguir la propuesta de una descripción básica de procesos administrativos estándar.

La clasificación establecida en el Anexo II resulta plenamente coherente con esta apreciación al considerar el subproyecto como propuesta técnica incluida con desarrollo deficiente.

**La respuesta cubre funcionalmente el requisito, pero la limitada definición de procedimientos y la ausencia de mecanismos verificables impiden atribuir a la solución un nivel de madurez superior.** La propuesta presenta un desarrollo insuficiente para acreditar una capacidad diferencial de gestión.

- **Fortalezas y valor añadido**

**La propuesta contempla actividades relacionadas con la recepción, análisis y tramitación de solicitudes de recursos, evidenciando comprender la necesidad de establecer mecanismos ordenados de provisión y seguimiento.** La memoria recoge la existencia de procesos de coordinación y gestión que permiten apreciar una cobertura funcional razonable del alcance solicitado.

La clasificación establecida en el Anexo II resulta plenamente coherente con esta apreciación al considerar el subproyecto como propuesta técnica incluida con desarrollo deficiente.

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, la documentación no define flujos de aprobación, circuitos de gestión, criterios de priorización, procedimientos de validación ni modelos de gobernanza que permitan evaluar de manera objetiva la calidad de la solución planteada.** Las actividades descritas se encuentran formuladas de forma muy genérica y no incorporan elementos metodológicos diferenciales que permitan distinguir la propuesta de una descripción básica de procesos administrativos estándar.

**La respuesta cubre funcionalmente el requisito, pero la limitada definición de procedimientos y la ausencia de mecanismos verificables impiden atribuir a la solución un nivel de madurez superior.** La propuesta presenta un desarrollo insuficiente para acreditar una capacidad diferencial de gestión.

- **Valoración cualitativa**

- **BAJA**

#### ESIS14 — Bastionado de los recursos solicitados

- **Requisito y alcance**

El objeto de este subproyecto es garantizar la aplicación de medidas de endurecimiento y configuración segura sobre las plataformas que soportan los proyectos externos, reduciendo la superficie de exposición y minimizando los riesgos de seguridad asociados a los entornos gestionados.

No se ha identificado en la memoria técnica una propuesta específica que permita asociar de manera directa una solución concreta a este requisito. **Aunque el documento incorpora referencias generales a buenas prácticas de seguridad, cumplimiento normativo y protección de la infraestructura, dichas referencias no constituyen un desarrollo específico del servicio de bastionado requerido.**

- **Análisis de la propuesta**

**La inexistencia de una propuesta técnica concreta impide analizar metodologías, estándares de endurecimiento, procedimientos de verificación, herramientas de auditoría o mecanismos de validación de configuraciones seguras.** Tampoco se describen actividades específicas orientadas a la implantación o mantenimiento de políticas de bastionado.

El Anexo II clasifica expresamente este requisito como propuesta técnica no incluida, valoración que resulta plenamente coherente con el contenido de la memoria analizada.

**La ausencia de una respuesta específica imposibilita verificar la comprensión efectiva del requisito y limita completamente la capacidad de valorar la solución.** En consecuencia, el subproyecto debe situarse en el nivel más bajo de la escala de valoración.

- **Fortalezas y valor añadido**

El Anexo II clasifica expresamente este requisito como propuesta técnica no incluida, valoración que resulta plenamente coherente con el contenido de la memoria analizada.

**La ausencia de una respuesta específica imposibilita verificar la comprensión efectiva del requisito y limita completamente la capacidad de valorar la solución.** En consecuencia, el subproyecto debe situarse en el nivel más bajo de la escala de valoración.

- **Carencias, omisiones, errores o riesgos**

No se ha identificado en la memoria técnica una propuesta específica que permita asociar de manera directa una solución concreta a este requisito. **Aunque el documento incorpora referencias generales a buenas prácticas de seguridad, cumplimiento normativo y protección de la infraestructura, dichas referencias no constituyen un desarrollo específico del servicio de bastionado requerido.**

**La ausencia de una respuesta específica imposibilita verificar la comprensión efectiva del requisito y limita completamente la capacidad de valorar la solución.** En consecuencia, el subproyecto debe situarse en el nivel más bajo de la escala de valoración.

- **Valoración cualitativa**

- **MUY BAJA**

#### ESIS15 — Instalación de la paquetería y gestión de dependencias

- **Requisito y alcance**

Este subproyecto persigue garantizar el control de los componentes software utilizados por los distintos proyectos externos, asegurando la adecuada gestión de dependencias, la compatibilidad entre versiones y la reducción de riesgos derivados de vulnerabilidades o incompatibilidades técnicas.

**La propuesta presentada por empresa_n contempla referencias a actividades de actualización y mantenimiento de componentes software, permitiendo apreciar una comprensión general de la importancia que tiene la correcta gestión de dependencias en entornos complejos.** Desde la perspectiva funcional puede considerarse que el requisito se encuentra cubierto.

- **Análisis de la propuesta**

**No obstante, la solución permanece formulada en términos excesivamente generales.** La memoria no desarrolla procedimientos específicos de inventariado de componentes, control de dependencias transitivas, validación de compatibilidades, gestión de vulnerabilidades asociadas a librerías o mecanismos automatizados de seguimiento del ciclo de vida del software utilizado.

**La falta de herramientas concretas y la ausencia de una metodología definida reducen significativamente la capacidad de valorar favorablemente la propuesta.** Esta apreciación resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

**La respuesta acredita una comprensión adecuada del objetivo perseguido por el requisito, pero no desarrolla los mecanismos técnicos necesarios para demostrar una capacidad real de gestión avanzada de dependencias.** La limitada concreción observada justifica una valoración BAJA.

- **Fortalezas y valor añadido**

Este subproyecto persigue garantizar el control de los componentes software utilizados por los distintos proyectos externos, asegurando la adecuada gestión de dependencias, la compatibilidad entre versiones y la reducción de riesgos derivados de vulnerabilidades o incompatibilidades técnicas.

**La propuesta presentada por empresa_n contempla referencias a actividades de actualización y mantenimiento de componentes software, permitiendo apreciar una comprensión general de la importancia que tiene la correcta gestión de dependencias en entornos complejos.** Desde la perspectiva funcional puede considerarse que el requisito se encuentra cubierto.

- **Carencias, omisiones, errores o riesgos**

**No obstante, la solución permanece formulada en términos excesivamente generales.** La memoria no desarrolla procedimientos específicos de inventariado de componentes, control de dependencias transitivas, validación de compatibilidades, gestión de vulnerabilidades asociadas a librerías o mecanismos automatizados de seguimiento del ciclo de vida del software utilizado.

**La falta de herramientas concretas y la ausencia de una metodología definida reducen significativamente la capacidad de valorar favorablemente la propuesta.** Esta apreciación resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

- **Valoración cualitativa**

- **BAJA**

#### ESIS16 — Configuración del entorno

- **Requisito y alcance**

El objetivo de este subproyecto consiste en garantizar la correcta configuración de los entornos necesarios para el despliegue y operación de los distintos proyectos externos integrados en EducaMadrid.

La memoria contempla actuaciones relacionadas con la preparación y configuración de entornos de trabajo, incluyendo referencias generales a tareas de parametrización y soporte a la implantación de nuevas soluciones. **La respuesta demuestra comprender la necesidad de disponer de configuraciones homogéneas y adecuadas para garantizar la estabilidad operativa de los servicios.**

- **Análisis de la propuesta**

**Pese a esta cobertura funcional, la propuesta carece de una descripción suficientemente detallada de los procedimientos de configuración previstos.** No se desarrollan mecanismos de automatización, estrategias de gestión de configuraciones, herramientas de infraestructura como código ni procedimientos de control que permitan evaluar la reproducibilidad o consistencia de los entornos generados.

La documentación mantiene un enfoque principalmente descriptivo, reproduciendo los objetivos perseguidos por el Documento de Invitación sin profundizar en los mecanismos técnicos necesarios para alcanzar dichos objetivos. **Esta circunstancia resulta compatible con la clasificación de desarrollo deficiente recogida en el Anexo I.**

**La propuesta proporciona una cobertura funcional aceptable, pero la escasa profundidad técnica y la ausencia de mecanismos verificables limitan significativamente la calidad de la solución.** La respuesta se sitúa por tanto en el nivel correspondiente a una valoración BAJA.

- **Fortalezas y valor añadido**

La memoria contempla actuaciones relacionadas con la preparación y configuración de entornos de trabajo, incluyendo referencias generales a tareas de parametrización y soporte a la implantación de nuevas soluciones. **La respuesta demuestra comprender la necesidad de disponer de configuraciones homogéneas y adecuadas para garantizar la estabilidad operativa de los servicios.**

**Pese a esta cobertura funcional, la propuesta carece de una descripción suficientemente detallada de los procedimientos de configuración previstos.** No se desarrollan mecanismos de automatización, estrategias de gestión de configuraciones, herramientas de infraestructura como código ni procedimientos de control que permitan evaluar la reproducibilidad o consistencia de los entornos generados.

- **Carencias, omisiones, errores o riesgos**

**Pese a esta cobertura funcional, la propuesta carece de una descripción suficientemente detallada de los procedimientos de configuración previstos.** No se desarrollan mecanismos de automatización, estrategias de gestión de configuraciones, herramientas de infraestructura como código ni procedimientos de control que permitan evaluar la reproducibilidad o consistencia de los entornos generados.

**La propuesta proporciona una cobertura funcional aceptable, pero la escasa profundidad técnica y la ausencia de mecanismos verificables limitan significativamente la calidad de la solución.** La respuesta se sitúa por tanto en el nivel correspondiente a una valoración BAJA.

- **Valoración cualitativa**

- **BAJA**

#### ESIS17 — Soporte para la integración con el LDAP de la plataforma EducaMadrid

- **Requisito y alcance**

Este subproyecto tiene como finalidad garantizar la integración de las aplicaciones externas con los mecanismos corporativos de gestión de identidades utilizados por EducaMadrid, permitiendo la correcta autenticación de usuarios y la sincronización de la información necesaria para la prestación de los distintos servicios.

La memoria técnica incorpora referencias a la integración con servicios de directorio y contempla la necesidad de garantizar la interoperabilidad entre las aplicaciones externas y los sistemas corporativos de autenticación. **La propuesta reconoce adecuadamente la importancia de la gestión centralizada de identidades dentro del ecosistema EducaMadrid y describe de forma general las actividades orientadas a facilitar dicha integración.** Desde una perspectiva funcional, puede considerarse que el requisito se encuentra cubierto.

- **Análisis de la propuesta**

**No obstante, el análisis detallado de la documentación revela importantes carencias en la comprensión del entorno tecnológico real asociado a este requisito.** La memoria realiza referencias al denominado LDAP Plano como si se tratara de un servicio LDAP convencional cuando, según la documentación técnica incluida en el Documento de Invitación, dicho componente corresponde realmente a una base de datos PostgreSQL utilizada como repositorio de información. Esta confusión evidencia una comprensión imperfecta de la arquitectura actual de la plataforma y limita la fiabilidad técnica de la propuesta formulada.

Adicionalmente, la solución se desarrolla mediante planteamientos genéricos sobre integración de identidades sin detallar flujos de sincronización, mecanismos de resolución de incidencias, procedimientos de integración, esquemas de replicación ni procesos de validación asociados a la gestión de identidades. La memoria reproduce en buena medida los objetivos perseguidos por el requisito sin desarrollar suficientemente los mecanismos técnicos necesarios para alcanzarlos. **Esta circunstancia resulta plenamente coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.**

**La propuesta acredita una comprensión básica de la finalidad del servicio, pero las inconsistencias detectadas sobre la arquitectura de identidad existente, unidas a la limitada definición técnica de la solución, impiden considerar que la respuesta alcance niveles adecuados de especialización.** La existencia de errores de interpretación sobre componentes esenciales del entorno reduce considerablemente la confianza en la capacidad de ejecución efectiva del servicio solicitado.

**Debe señalarse que las inconsistencias observadas no implican una ausencia total de comprensión del requisito ni del entorno funcional objeto del contrato.** Sin embargo, constituyen indicios objetivos de un conocimiento parcial o imperfecto de determinados componentes tecnológicos específicos de la plataforma EducaMadrid. Por ello, la valoración realizada distingue entre una comprensión general adecuada de la finalidad del servicio y el conocimiento detallado de determinadas implementaciones concretas actualmente desplegadas.

**Debe señalarse que las inconsistencias observadas no implican una ausencia total de comprensión del requisito ni del entorno funcional objeto del contrato.** Sin embargo, constituyen indicios objetivos de un conocimiento parcial o imperfecto de determinados componentes tecnológicos específicos de la plataforma EducaMadrid. Por ello, la valoración realizada distingue entre una comprensión general adecuada de la finalidad del servicio y el conocimiento detallado de determinadas implementaciones concretas actualmente desplegadas.

- **Fortalezas y valor añadido**

La memoria técnica incorpora referencias a la integración con servicios de directorio y contempla la necesidad de garantizar la interoperabilidad entre las aplicaciones externas y los sistemas corporativos de autenticación. **La propuesta reconoce adecuadamente la importancia de la gestión centralizada de identidades dentro del ecosistema EducaMadrid y describe de forma general las actividades orientadas a facilitar dicha integración.** Desde una perspectiva funcional, puede considerarse que el requisito se encuentra cubierto.

**No obstante, el análisis detallado de la documentación revela importantes carencias en la comprensión del entorno tecnológico real asociado a este requisito.** La memoria realiza referencias al denominado LDAP Plano como si se tratara de un servicio LDAP convencional cuando, según la documentación técnica incluida en el Documento de Invitación, dicho componente corresponde realmente a una base de datos PostgreSQL utilizada como repositorio de información. Esta confusión evidencia una comprensión imperfecta de la arquitectura actual de la plataforma y limita la fiabilidad técnica de la propuesta formulada.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el análisis detallado de la documentación revela importantes carencias en la comprensión del entorno tecnológico real asociado a este requisito.** La memoria realiza referencias al denominado LDAP Plano como si se tratara de un servicio LDAP convencional cuando, según la documentación técnica incluida en el Documento de Invitación, dicho componente corresponde realmente a una base de datos PostgreSQL utilizada como repositorio de información. Esta confusión evidencia una comprensión imperfecta de la arquitectura actual de la plataforma y limita la fiabilidad técnica de la propuesta formulada.

**La propuesta acredita una comprensión básica de la finalidad del servicio, pero las inconsistencias detectadas sobre la arquitectura de identidad existente, unidas a la limitada definición técnica de la solución, impiden considerar que la respuesta alcance niveles adecuados de especialización.** La existencia de errores de interpretación sobre componentes esenciales del entorno reduce considerablemente la confianza en la capacidad de ejecución efectiva del servicio solicitado.

- **Valoración cualitativa**

- **BAJA**

#### ESIS18 — Soporte para la integración con el sistema de correo de la plataforma EducaMadrid

- **Requisito y alcance**

Este subproyecto contempla la integración de los distintos proyectos externos con los servicios corporativos de correo electrónico utilizados por EducaMadrid, garantizando la correcta interoperabilidad entre aplicaciones y plataformas de mensajería.

**La memoria identifica la necesidad de integrar los proyectos externos con los mecanismos corporativos de comunicación y contempla actividades relacionadas con la configuración y utilización de servicios de correo electrónico.** La propuesta demuestra comprender la finalidad del requisito y reconoce el carácter transversal de este tipo de integraciones dentro del ecosistema tecnológico objeto del contrato. La cobertura funcional puede considerarse suficiente.

- **Análisis de la propuesta**

**Sin embargo, la definición técnica aportada resulta escasa.** La documentación no desarrolla procedimientos concretos de integración, configuración segura, monitorización de servicios de correo, mecanismos de trazabilidad de comunicaciones o procedimientos de resolución de incidencias. Tampoco se identifican herramientas, arquitecturas o metodologías específicas que permitan acreditar una aproximación diferencial respecto a los requisitos mínimos exigidos.

**La propuesta se limita esencialmente a describir actividades operativas de carácter general, sin profundizar en los aspectos técnicos que constituyen el núcleo del servicio solicitado.** Esta situación resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

**La respuesta cubre funcionalmente el requisito, pero la limitada profundidad técnica y la ausencia de procedimientos verificables reducen significativamente la calidad global de la solución.** La propuesta se corresponde con una valoración BAJA.

- **Fortalezas y valor añadido**

**La memoria identifica la necesidad de integrar los proyectos externos con los mecanismos corporativos de comunicación y contempla actividades relacionadas con la configuración y utilización de servicios de correo electrónico.** La propuesta demuestra comprender la finalidad del requisito y reconoce el carácter transversal de este tipo de integraciones dentro del ecosistema tecnológico objeto del contrato. La cobertura funcional puede considerarse suficiente.

**La propuesta se limita esencialmente a describir actividades operativas de carácter general, sin profundizar en los aspectos técnicos que constituyen el núcleo del servicio solicitado.** Esta situación resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, la definición técnica aportada resulta escasa.** La documentación no desarrolla procedimientos concretos de integración, configuración segura, monitorización de servicios de correo, mecanismos de trazabilidad de comunicaciones o procedimientos de resolución de incidencias. Tampoco se identifican herramientas, arquitecturas o metodologías específicas que permitan acreditar una aproximación diferencial respecto a los requisitos mínimos exigidos.

**La propuesta se limita esencialmente a describir actividades operativas de carácter general, sin profundizar en los aspectos técnicos que constituyen el núcleo del servicio solicitado.** Esta situación resulta coherente con la clasificación de desarrollo deficiente recogida en el Anexo I.

- **Valoración cualitativa**

- **BAJA**

#### ESIS19 — Soporte para la integración con distintas BBDD de la plataforma EducaMadrid

- **Requisito y alcance**

La finalidad de este subproyecto consiste en facilitar la interoperabilidad de los proyectos externos con las distintas plataformas de gestión de datos utilizadas por EducaMadrid, garantizando la correcta integración, explotación y mantenimiento de la información.

La memoria contempla actuaciones orientadas a facilitar la integración entre aplicaciones y repositorios de información, reconociendo la necesidad de garantizar el intercambio de datos entre servicios heterogéneos. **Desde una perspectiva funcional, la propuesta aborda adecuadamente el objetivo general perseguido por el Documento de Invitación y acredita comprender la importancia de la información corporativa como elemento central del ecosistema EducaMadrid.**

- **Análisis de la propuesta**

**A pesar de ello, la solución propuesta adolece de una importante falta de precisión técnica.** La documentación no desarrolla suficientemente las particularidades asociadas a los distintos motores de bases de datos presentes en la plataforma ni los procedimientos específicos necesarios para garantizar una integración robusta y sostenible.

Adicionalmente, se observa una inconsistencia relevante al describir determinados entornos Drupal sobre PostgreSQL cuando, según la documentación técnica del contrato, dichos sistemas se encuentran soportados sobre MySQL. **Esta circunstancia pone de manifiesto un conocimiento imperfecto de la arquitectura actual y limita la capacidad de valorar favorablemente la especialización técnica demostrada por la oferta.**

La ausencia de arquitecturas de integración claramente definidas, procedimientos de validación específicos o mecanismos detallados de interoperabilidad resulta coherente con la clasificación de desarrollo deficiente reflejada en el Anexo I.

**Aunque la propuesta cubre formalmente el requisito, las inconsistencias detectadas respecto al entorno tecnológico real y la limitada profundidad técnica de la solución reducen significativamente la calidad de la respuesta.** La capacidad de acreditar conocimiento especializado del ecosistema de datos de EducaMadrid resulta insuficiente para justificar una valoración superior.

**Debe señalarse que las inconsistencias observadas no implican una ausencia total de comprensión del requisito ni del entorno funcional objeto del contrato.** Sin embargo, constituyen indicios objetivos de un conocimiento parcial o imperfecto de determinados componentes tecnológicos específicos de la plataforma EducaMadrid. Por ello, la valoración realizada distingue entre una comprensión general adecuada de la finalidad del servicio y el conocimiento detallado de determinadas implementaciones concretas actualmente desplegadas.

- **Fortalezas y valor añadido**

La memoria contempla actuaciones orientadas a facilitar la integración entre aplicaciones y repositorios de información, reconociendo la necesidad de garantizar el intercambio de datos entre servicios heterogéneos. **Desde una perspectiva funcional, la propuesta aborda adecuadamente el objetivo general perseguido por el Documento de Invitación y acredita comprender la importancia de la información corporativa como elemento central del ecosistema EducaMadrid.**

La ausencia de arquitecturas de integración claramente definidas, procedimientos de validación específicos o mecanismos detallados de interoperabilidad resulta coherente con la clasificación de desarrollo deficiente reflejada en el Anexo I.

- **Carencias, omisiones, errores o riesgos**

**A pesar de ello, la solución propuesta adolece de una importante falta de precisión técnica.** La documentación no desarrolla suficientemente las particularidades asociadas a los distintos motores de bases de datos presentes en la plataforma ni los procedimientos específicos necesarios para garantizar una integración robusta y sostenible.

Adicionalmente, se observa una inconsistencia relevante al describir determinados entornos Drupal sobre PostgreSQL cuando, según la documentación técnica del contrato, dichos sistemas se encuentran soportados sobre MySQL. **Esta circunstancia pone de manifiesto un conocimiento imperfecto de la arquitectura actual y limita la capacidad de valorar favorablemente la especialización técnica demostrada por la oferta.**

- **Valoración cualitativa**

- **BAJA**

#### ESIS20 — Soporte para la integración del CMDB de la plataforma EducaMadrid

- **Requisito y alcance**

Este subproyecto tiene por objeto garantizar la correcta integración de los proyectos externos con los sistemas corporativos de inventario y gestión de configuración, preservando la trazabilidad de los elementos gestionados por la organización.

**La propuesta contempla referencias generales a la gestión documental, trazabilidad y control de activos tecnológicos.** La memoria permite identificar una comprensión razonable de la necesidad de mantener actualizada la información asociada a los componentes desplegados dentro de la plataforma y reconoce el papel de los sistemas de inventario en la gestión del servicio.

- **Análisis de la propuesta**

**No obstante, el desarrollo técnico aportado resulta limitado.** No se describen procedimientos específicos de integración con la CMDB, mecanismos de sincronización de información, modelos de actualización automática ni arquitecturas que permitan valorar favorablemente la calidad de la solución. La mayor parte de la respuesta permanece formulada mediante principios generales de gestión y trazabilidad sin desarrollar los mecanismos concretos requeridos para su implantación.

La solución tampoco incorpora mejoras o capacidades diferenciales reconocidas en el Anexo II y mantiene la consideración de propuesta técnica incluida con desarrollo deficiente.

**La respuesta permite apreciar una comprensión adecuada de la finalidad del requisito, pero la ausencia de desarrollo técnico específico limita significativamente su calidad.** La propuesta se ajusta a los parámetros correspondientes a una valoración BAJA.

- **Fortalezas y valor añadido**

**La propuesta contempla referencias generales a la gestión documental, trazabilidad y control de activos tecnológicos.** La memoria permite identificar una comprensión razonable de la necesidad de mantener actualizada la información asociada a los componentes desplegados dentro de la plataforma y reconoce el papel de los sistemas de inventario en la gestión del servicio.

**La respuesta permite apreciar una comprensión adecuada de la finalidad del requisito, pero la ausencia de desarrollo técnico específico limita significativamente su calidad.** La propuesta se ajusta a los parámetros correspondientes a una valoración BAJA.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el desarrollo técnico aportado resulta limitado.** No se describen procedimientos específicos de integración con la CMDB, mecanismos de sincronización de información, modelos de actualización automática ni arquitecturas que permitan valorar favorablemente la calidad de la solución. La mayor parte de la respuesta permanece formulada mediante principios generales de gestión y trazabilidad sin desarrollar los mecanismos concretos requeridos para su implantación.

**La respuesta permite apreciar una comprensión adecuada de la finalidad del requisito, pero la ausencia de desarrollo técnico específico limita significativamente su calidad.** La propuesta se ajusta a los parámetros correspondientes a una valoración BAJA.

- **Valoración cualitativa**

- **BAJA**

#### ESIS21 — Documentación del proyecto externo

- **Requisito y alcance**

La finalidad de este subproyecto consiste en garantizar la adecuada generación, actualización y conservación de la documentación asociada a los distintos servicios y proyectos externos gestionados dentro del ámbito del contrato.

La memoria dedica una atención significativa a los aspectos relacionados con la gestión documental, la transferencia de conocimiento y la trazabilidad de la información generada durante la prestación del servicio. Se identifican procedimientos de documentación, repositorios de conocimiento y mecanismos orientados a garantizar la disponibilidad y actualización de la información técnica asociada a los proyectos gestionados. **La cobertura funcional puede considerarse adecuada.**

- **Análisis de la propuesta**

**A pesar de constituir uno de los apartados mejor desarrollados del bloque ESIS, la documentación continúa presentando ciertas limitaciones respecto al nivel de detalle técnico alcanzado.** Aunque se describen procesos de gestión documental y mecanismos de organización de la información, no se desarrollan en profundidad aspectos relacionados con modelos de gobierno documental, automatización del ciclo de vida de la documentación o procedimientos avanzados de control de versiones y auditoría.

**Estas limitaciones justifican que el Anexo II mantenga la clasificación de desarrollo deficiente.** No obstante, el tratamiento otorgado al requisito resulta sensiblemente más elaborado que el observado en otros subproyectos del bloque.

**La propuesta presenta un mayor grado de desarrollo que la mayoría de los requisitos clasificados como desarrollo deficiente, si bien continúa alejándose del nivel de profundidad deseable para acreditar una metodología documental especialmente madura.** En coherencia con la clasificación recogida en el Anexo I, la valoración final se mantiene en nivel BAJO, aunque situada en la parte alta de dicho intervalo.

- **Fortalezas y valor añadido**

La finalidad de este subproyecto consiste en garantizar la adecuada generación, actualización y conservación de la documentación asociada a los distintos servicios y proyectos externos gestionados dentro del ámbito del contrato.

La memoria dedica una atención significativa a los aspectos relacionados con la gestión documental, la transferencia de conocimiento y la trazabilidad de la información generada durante la prestación del servicio. Se identifican procedimientos de documentación, repositorios de conocimiento y mecanismos orientados a garantizar la disponibilidad y actualización de la información técnica asociada a los proyectos gestionados. **La cobertura funcional puede considerarse adecuada.**

- **Carencias, omisiones, errores o riesgos**

**A pesar de constituir uno de los apartados mejor desarrollados del bloque ESIS, la documentación continúa presentando ciertas limitaciones respecto al nivel de detalle técnico alcanzado.** Aunque se describen procesos de gestión documental y mecanismos de organización de la información, no se desarrollan en profundidad aspectos relacionados con modelos de gobierno documental, automatización del ciclo de vida de la documentación o procedimientos avanzados de control de versiones y auditoría.

**Estas limitaciones justifican que el Anexo II mantenga la clasificación de desarrollo deficiente.** No obstante, el tratamiento otorgado al requisito resulta sensiblemente más elaborado que el observado en otros subproyectos del bloque.

- **Valoración cualitativa**

- **BAJA**

#### ESIS22 — Gestión del riesgo del proyecto externo

- **Requisito y alcance**

Este subproyecto tiene por objeto asegurar la identificación, análisis, tratamiento y seguimiento de los riesgos tecnológicos asociados a los proyectos externos integrados en EducaMadrid, garantizando la adopción de medidas proporcionadas para minimizar el impacto potencial sobre la disponibilidad, integridad y seguridad de los servicios.

**La memoria presentada por empresa_n dedica un apartado específico a la gestión del riesgo y desarrolla una aproximación metodológica basada en la aplicación de MAGERIT, identificando las principales fases asociadas al proceso de análisis, evaluación y tratamiento de riesgos.** La propuesta permite apreciar una comprensión adecuada de la importancia que poseen los mecanismos de gestión del riesgo dentro del marco de gobierno de los sistemas de información de las Administraciones Públicas y mantiene una alineación razonable con las exigencias derivadas del Esquema Nacional de Seguridad. La cobertura funcional del requisito puede considerarse satisfactoria y superior a la observada en una parte significativa de los subproyectos analizados.

- **Análisis de la propuesta**

A diferencia de otros apartados del bloque ESIS, la propuesta incorpora una metodología concreta y reconocible para abordar el requisito. **No obstante, la solución continúa presentando limitaciones relevantes desde el punto de vista de su desarrollo práctico, ya que no se describen herramientas específicas, procesos de integración con la operación real del servicio ni mecanismos detallados para el seguimiento continuo de los riesgos identificados.** La propuesta mejora claramente la cobertura mínima exigida por el Documento de Invitación, pero el grado de detalle alcanzado no permite acreditar una especialización particularmente avanzada.

El Anexo II clasifica este subproyecto como propuesta técnica incluida con desarrollo suficiente e identifica expresamente la utilización de MAGERIT como propuesta de mejora respecto al planteamiento base. **Esta clasificación resulta coherente con el contenido efectivamente desarrollado en la memoria.**

**La existencia de una metodología reconocible, la adecuada cobertura funcional del requisito y la incorporación de una propuesta de mejora identificable permiten situar este subproyecto por encima del nivel predominante dentro del bloque ESIS.** No obstante, las limitaciones observadas en cuanto a profundidad técnica y mecanismos de implantación impiden alcanzar valoraciones superiores.

- **Fortalezas y valor añadido**

**La memoria presentada por empresa_n dedica un apartado específico a la gestión del riesgo y desarrolla una aproximación metodológica basada en la aplicación de MAGERIT, identificando las principales fases asociadas al proceso de análisis, evaluación y tratamiento de riesgos.** La propuesta permite apreciar una comprensión adecuada de la importancia que poseen los mecanismos de gestión del riesgo dentro del marco de gobierno de los sistemas de información de las Administraciones Públicas y mantiene una alineación razonable con las exigencias derivadas del Esquema Nacional de Seguridad. La cobertura funcional del requisito puede considerarse satisfactoria y superior a la observada en una parte significativa de los subproyectos analizados.

A diferencia de otros apartados del bloque ESIS, la propuesta incorpora una metodología concreta y reconocible para abordar el requisito. **No obstante, la solución continúa presentando limitaciones relevantes desde el punto de vista de su desarrollo práctico, ya que no se describen herramientas específicas, procesos de integración con la operación real del servicio ni mecanismos detallados para el seguimiento continuo de los riesgos identificados.** La propuesta mejora claramente la cobertura mínima exigida por el Documento de Invitación, pero el grado de detalle alcanzado no permite acreditar una especialización particularmente avanzada.

- **Carencias, omisiones, errores o riesgos**

A diferencia de otros apartados del bloque ESIS, la propuesta incorpora una metodología concreta y reconocible para abordar el requisito. **No obstante, la solución continúa presentando limitaciones relevantes desde el punto de vista de su desarrollo práctico, ya que no se describen herramientas específicas, procesos de integración con la operación real del servicio ni mecanismos detallados para el seguimiento continuo de los riesgos identificados.** La propuesta mejora claramente la cobertura mínima exigida por el Documento de Invitación, pero el grado de detalle alcanzado no permite acreditar una especialización particularmente avanzada.

**La existencia de una metodología reconocible, la adecuada cobertura funcional del requisito y la incorporación de una propuesta de mejora identificable permiten situar este subproyecto por encima del nivel predominante dentro del bloque ESIS.** No obstante, las limitaciones observadas en cuanto a profundidad técnica y mecanismos de implantación impiden alcanzar valoraciones superiores.

- **Valoración cualitativa**

- **MEDIA**

#### ESIS23 — Implementación de sistemas de Backups y procedimiento de Disaster Recovery

- **Requisito y alcance**

La finalidad de este subproyecto consiste en garantizar la protección de la información gestionada por los proyectos externos mediante la implantación de mecanismos de respaldo, recuperación y continuidad de servicio que permitan minimizar el impacto derivado de incidencias graves o situaciones de desastre.

La memoria desarrolla de forma razonablemente extensa las actividades relacionadas con las copias de seguridad, los procedimientos de recuperación y la continuidad operativa de las plataformas. La propuesta describe mecanismos de respaldo periódico, validación de copias, conservación de información y planificación de actuaciones orientadas a facilitar la recuperación de los servicios en caso de contingencia. **La cobertura funcional del requisito resulta adecuada y se encuentra claramente alineada con las necesidades establecidas en el Documento de Invitación.**

- **Análisis de la propuesta**

**El nivel de desarrollo observado resulta superior al de la mayoría de los subproyectos clasificados como desarrollo deficiente.** La memoria aporta una cierta estructuración metodológica y describe los principales elementos necesarios para garantizar la continuidad de las plataformas. Sin embargo, continúan existiendo limitaciones relevantes asociadas a la ausencia de arquitecturas detalladas de recuperación, definición de RPO y RTO específicos, mecanismos avanzados de validación de restauraciones o procedimientos exhaustivos de recuperación ante desastre.

**Estas limitaciones impiden justificar una valoración ALTA, pero permiten diferenciar claramente el subproyecto respecto del conjunto de respuestas genéricas predominantes en el bloque ESIS.** El Anexo II clasifica este requisito como propuesta técnica incluida con desarrollo suficiente, sin identificar propuestas de mejora ni elementos de valor añadido adicionales.

La propuesta proporciona una respuesta técnicamente más desarrollada que la media del bloque, incorpora mecanismos operativos identificables y permite acreditar una capacidad razonable de ejecución. **No obstante, la ausencia de determinados elementos avanzados de continuidad limita la valoración final al nivel correspondiente a una MEDIA.**

- **Fortalezas y valor añadido**

La memoria desarrolla de forma razonablemente extensa las actividades relacionadas con las copias de seguridad, los procedimientos de recuperación y la continuidad operativa de las plataformas. La propuesta describe mecanismos de respaldo periódico, validación de copias, conservación de información y planificación de actuaciones orientadas a facilitar la recuperación de los servicios en caso de contingencia. **La cobertura funcional del requisito resulta adecuada y se encuentra claramente alineada con las necesidades establecidas en el Documento de Invitación.**

**Estas limitaciones impiden justificar una valoración ALTA, pero permiten diferenciar claramente el subproyecto respecto del conjunto de respuestas genéricas predominantes en el bloque ESIS.** El Anexo II clasifica este requisito como propuesta técnica incluida con desarrollo suficiente, sin identificar propuestas de mejora ni elementos de valor añadido adicionales.

- **Carencias, omisiones, errores o riesgos**

**El nivel de desarrollo observado resulta superior al de la mayoría de los subproyectos clasificados como desarrollo deficiente.** La memoria aporta una cierta estructuración metodológica y describe los principales elementos necesarios para garantizar la continuidad de las plataformas. Sin embargo, continúan existiendo limitaciones relevantes asociadas a la ausencia de arquitecturas detalladas de recuperación, definición de RPO y RTO específicos, mecanismos avanzados de validación de restauraciones o procedimientos exhaustivos de recuperación ante desastre.

**Estas limitaciones impiden justificar una valoración ALTA, pero permiten diferenciar claramente el subproyecto respecto del conjunto de respuestas genéricas predominantes en el bloque ESIS.** El Anexo II clasifica este requisito como propuesta técnica incluida con desarrollo suficiente, sin identificar propuestas de mejora ni elementos de valor añadido adicionales.

- **Valoración cualitativa**

- **MEDIA**

#### ESIS24 — Implementación de monitorización básica

- **Requisito y alcance**

Este subproyecto contempla la supervisión continua de los sistemas externos integrados en EducaMadrid con objeto de detectar incidencias, anticipar problemas de capacidad y garantizar el cumplimiento de los niveles de servicio establecidos.

La memoria describe actividades orientadas a la monitorización de infraestructuras, servicios y aplicaciones, reconociendo la importancia de disponer de mecanismos de supervisión continuada sobre los componentes gestionados. **La propuesta cubre adecuadamente la finalidad funcional perseguida por el Documento de Invitación e identifica los principales ámbitos de actuación asociados al control operativo de los sistemas.**

- **Análisis de la propuesta**

**Sin embargo, la solución se desarrolla de forma eminentemente descriptiva.** No se especifican arquitecturas de monitorización, herramientas concretas, procesos de correlación de eventos, mecanismos de observabilidad avanzada ni indicadores operativos que permitan valorar favorablemente la calidad técnica de la propuesta. Adicionalmente, una parte significativa de las capacidades descritas corresponden a prácticas habituales en cualquier servicio de explotación tecnológica y no constituyen elementos diferenciales respecto a las necesidades ordinarias de operación.

La escasa concreción técnica observada resulta coherente con la clasificación de desarrollo deficiente establecida en el Anexo I.

**La cobertura funcional es adecuada, pero la limitada profundidad metodológica y la ausencia de mecanismos verificables reducen significativamente la calidad global de la solución.** La propuesta no acredita capacidades diferenciales que permitan justificar una valoración superior.

- **Fortalezas y valor añadido**

La memoria describe actividades orientadas a la monitorización de infraestructuras, servicios y aplicaciones, reconociendo la importancia de disponer de mecanismos de supervisión continuada sobre los componentes gestionados. **La propuesta cubre adecuadamente la finalidad funcional perseguida por el Documento de Invitación e identifica los principales ámbitos de actuación asociados al control operativo de los sistemas.**

La escasa concreción técnica observada resulta coherente con la clasificación de desarrollo deficiente establecida en el Anexo I.

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, la solución se desarrolla de forma eminentemente descriptiva.** No se especifican arquitecturas de monitorización, herramientas concretas, procesos de correlación de eventos, mecanismos de observabilidad avanzada ni indicadores operativos que permitan valorar favorablemente la calidad técnica de la propuesta. Adicionalmente, una parte significativa de las capacidades descritas corresponden a prácticas habituales en cualquier servicio de explotación tecnológica y no constituyen elementos diferenciales respecto a las necesidades ordinarias de operación.

**La cobertura funcional es adecuada, pero la limitada profundidad metodológica y la ausencia de mecanismos verificables reducen significativamente la calidad global de la solución.** La propuesta no acredita capacidades diferenciales que permitan justificar una valoración superior.

- **Valoración cualitativa**

- **BAJA**

#### ESIS25 — Implementación de monitorización avanzada

- **Requisito y alcance**

La finalidad de este subproyecto consiste en implantar una supervisión avanzada e independiente de la monitorización básica para detectar anomalías de conectividad, rendimiento, disponibilidad, accesos externos y exposición de los servicios de los proyectos exteriores.

**La oferta dedica un apartado específico a ESIS25 y contempla monitorización avanzada de conectividad, rendimiento, tiempos de respuesta, accesos web externos y anomalías de servicio.** También prevé instalar herramientas específicas, configurar alertas avanzadas y revisar las incidencias detectadas de manera separada de la monitorización básica de infraestructura.

- **Análisis de la propuesta**

**La propuesta concreta OpenNMS para supervisión de red, monitorización distribuida y detección de eventos, y Cacti para gráficas, SNMP y análisis histórico de capacidad y rendimiento.** Añade monitorización de seguridad y SEO, validación de servicios expuestos y la posibilidad de desarrollar scripts personalizados. Estas evidencias corresponden al objeto canónico de ESIS25 y corrigen la asignación anterior de contenido sobre gestión de incidencias.

La identificación de herramientas y ámbitos de supervisión aporta una solución evaluable y una mejora concreta. No obstante, la oferta no define con suficiente precisión la arquitectura final, los umbrales, los cuadros de mando, los indicadores de servicio ni los procedimientos de integración y operación de las herramientas propuestas.

**La cobertura es completa y contiene elementos técnicos diferenciales, aunque su implantación queda parcialmente abierta.** La propuesta se clasifica como desarrollo suficiente con valor añadido y se sitúa en el nivel ALTA.

- **Fortalezas y valor añadido**

**La mención expresa de OpenNMS, Cacti, alertas avanzadas, supervisión de seguridad y SEO y scripts personalizados proporciona una base técnica identificable para ampliar la observabilidad de los proyectos exteriores.**

- **Carencias, omisiones, errores o riesgos**

No se concretan la topología definitiva, la integración con la observabilidad corporativa, los umbrales de alerta, los indicadores ni los criterios de aceptación de la implantación.

- **Valoración cualitativa**

- **ALTA**

#### ESIS26 — Implementación de servicios de ciberseguridad básicos

- **Requisito y alcance**

Este subproyecto tiene por objeto implantar medidas básicas de ciberseguridad alineadas con el Esquema Nacional de Seguridad, incluyendo control de accesos, autenticación robusta, gestión de certificados y corrección de vulnerabilidades y configuraciones inseguras.

**La oferta dedica un apartado específico a ESIS26 y contempla la revisión de usuarios, permisos, accesos remotos y cuentas administrativas, así como la implantación de doble factor para accesos privilegiados.** Incluye además revisión y renovación documentada de certificados, validación de TLS, comprobación de dominios y servicios publicados y corrección de componentes o configuraciones vulnerables.

- **Análisis de la propuesta**

**El contenido contrasta de manera directa con el requisito canónico y corrige la asignación anterior de contenido sobre análisis de causa raíz.** La propuesta cubre los principales controles solicitados y añade revisiones periódicas de accesos, privilegios, certificados, dominios, exposición y endurecimiento.

La respuesta es evaluable y suficientemente estructurada, pero la mayor parte de las actuaciones reproduce controles ordinarios del propio requisito. No se concretan herramientas, calendarios, métricas, procedimientos de auditoría, evidencias de cumplimiento ni un modelo de reporting ENS que permita considerar diferencial la solución.

**La propuesta se clasifica como desarrollo suficiente y su refuerzo periódico se considera una mejora sin valor añadido real.** La cobertura y la concreción alcanzadas corresponden al nivel MEDIA.

- **Fortalezas y valor añadido**

La oferta reúne en una secuencia coherente el control de accesos, el doble factor, la gestión de certificados, la revisión TLS, la detección de vulnerabilidades y el endurecimiento básico.

- **Carencias, omisiones, errores o riesgos**

No se definen herramientas, responsables, periodicidades, indicadores, evidencias de control ni procedimientos de reporting y verificación de cumplimiento.

- **Valoración cualitativa**

- **MEDIA**

#### ESIS27 — Implementación de servicios de ciberseguridad avanzados

- **Requisito y alcance**

El objetivo de este subproyecto consiste en reforzar la seguridad de los sistemas externos mediante la implantación de mecanismos de detección, prevención y seguimiento de eventos de seguridad que permitan incrementar el nivel de protección de los activos gestionados.

**La propuesta identifica adecuadamente la necesidad de reforzar la supervisión de la seguridad y contempla actividades orientadas a la detección y seguimiento de eventos relevantes para la protección de los sistemas.** La cobertura funcional del requisito resulta adecuada y evidencia comprender la importancia estratégica de los mecanismos de monitorización de seguridad dentro de entornos complejos y altamente expuestos.

- **Análisis de la propuesta**

**A diferencia de la mayoría de los requisitos del bloque ESIS, la memoria incorpora una propuesta concreta asociada al uso de soluciones SIEM basadas en tecnologías Open Source para el análisis y correlación de eventos de seguridad.** Este planteamiento aporta un elemento diferenciador claramente identificable y proporciona una línea de actuación verificable que trasciende la mera reformulación de los requisitos establecidos por el Documento de Invitación.

Aunque la propuesta podría haberse desarrollado con un mayor nivel de detalle respecto a la arquitectura, capacidades concretas o procedimientos operativos asociados al sistema SIEM propuesto, la existencia de un mecanismo técnico específico aporta un nivel de concreción superior al observado en la mayoría de los subproyectos del bloque. **Esta circunstancia resulta coherente con la clasificación como valor añadido recogida en el Anexo I.**

**La incorporación de una propuesta técnica concreta, diferenciadora y verificable permite acreditar una aportación de valor superior a la media del bloque ESIS.** Aunque la profundidad técnica podría haber sido mayor, la solución incorpora elementos suficientes para justificar una valoración ALTA.

- **Fortalezas y valor añadido**

**La propuesta identifica adecuadamente la necesidad de reforzar la supervisión de la seguridad y contempla actividades orientadas a la detección y seguimiento de eventos relevantes para la protección de los sistemas.** La cobertura funcional del requisito resulta adecuada y evidencia comprender la importancia estratégica de los mecanismos de monitorización de seguridad dentro de entornos complejos y altamente expuestos.

Aunque la propuesta podría haberse desarrollado con un mayor nivel de detalle respecto a la arquitectura, capacidades concretas o procedimientos operativos asociados al sistema SIEM propuesto, la existencia de un mecanismo técnico específico aporta un nivel de concreción superior al observado en la mayoría de los subproyectos del bloque. **Esta circunstancia resulta coherente con la clasificación como valor añadido recogida en el Anexo I.**

- **Carencias, omisiones, errores o riesgos**

No se acreditan mecanismos adicionales de concreción y verificación más allá de los contenidos analizados.

- **Valoración cualitativa**

- **ALTA**

#### ESIS28 — Actualización de los sistemas operativos

- **Requisito y alcance**

Este subproyecto tiene como finalidad garantizar la actualización controlada de los sistemas operativos que soportan los distintos proyectos externos, asegurando tanto la corrección de vulnerabilidades como la compatibilidad de los componentes software desplegados sobre las infraestructuras gestionadas.

La propuesta presentada por empresa_n aborda de forma expresa la necesidad de mantener actualizados los sistemas operativos y contempla actuaciones relacionadas con la planificación, ejecución y validación de las actualizaciones necesarias para preservar la sostenibilidad tecnológica de los entornos gestionados. **La memoria identifica adecuadamente la importancia que tiene este tipo de actuaciones dentro de la operación ordinaria de las plataformas y demuestra una comprensión correcta de los riesgos asociados al envejecimiento tecnológico de la infraestructura.** La cobertura funcional del requisito puede considerarse adecuada y plenamente alineada con las necesidades descritas en el Documento de Invitación.

- **Análisis de la propuesta**

**La solución propuesta presenta un nivel de desarrollo superior al observado en la mayoría de los subproyectos clasificados como desarrollo deficiente.** La memoria describe actividades concretas de validación y control posteriores a la implantación de nuevas versiones, así como mecanismos orientados a minimizar el impacto operativo derivado de los procesos de actualización. No obstante, el nivel de detalle alcanzado sigue siendo limitado en aspectos tales como la automatización de despliegues, la definición de procedimientos de reversión, la validación exhaustiva de compatibilidades o la gestión estructurada de cambios.

A diferencia de otros requisitos del bloque, el contenido desarrollado permite identificar una propuesta técnicamente coherente y suficientemente estructurada. **Esta circunstancia resulta consistente con la clasificación de desarrollo suficiente recogida en el Anexo I.** No obstante, la documentación no incorpora mejoras diferenciales ni elementos de innovación que permitan considerar que la solución supera significativamente las capacidades esperables dentro de un servicio estándar de administración de sistemas.

**La propuesta ofrece una cobertura adecuada del requisito y desarrolla un conjunto de actividades suficientemente definido para acreditar una capacidad razonable de ejecución.** Sin embargo, la ausencia de elementos diferenciales, junto con la limitada profundidad técnica observada en determinados aspectos operativos, impiden justificar una valoración superior. En consecuencia, la calidad global de la respuesta se corresponde con un nivel MEDIO.

- **Fortalezas y valor añadido**

La propuesta presentada por empresa_n aborda de forma expresa la necesidad de mantener actualizados los sistemas operativos y contempla actuaciones relacionadas con la planificación, ejecución y validación de las actualizaciones necesarias para preservar la sostenibilidad tecnológica de los entornos gestionados. **La memoria identifica adecuadamente la importancia que tiene este tipo de actuaciones dentro de la operación ordinaria de las plataformas y demuestra una comprensión correcta de los riesgos asociados al envejecimiento tecnológico de la infraestructura.** La cobertura funcional del requisito puede considerarse adecuada y plenamente alineada con las necesidades descritas en el Documento de Invitación.

A diferencia de otros requisitos del bloque, el contenido desarrollado permite identificar una propuesta técnicamente coherente y suficientemente estructurada. **Esta circunstancia resulta consistente con la clasificación de desarrollo suficiente recogida en el Anexo I.** No obstante, la documentación no incorpora mejoras diferenciales ni elementos de innovación que permitan considerar que la solución supera significativamente las capacidades esperables dentro de un servicio estándar de administración de sistemas.

- **Carencias, omisiones, errores o riesgos**

**La solución propuesta presenta un nivel de desarrollo superior al observado en la mayoría de los subproyectos clasificados como desarrollo deficiente.** La memoria describe actividades concretas de validación y control posteriores a la implantación de nuevas versiones, así como mecanismos orientados a minimizar el impacto operativo derivado de los procesos de actualización. No obstante, el nivel de detalle alcanzado sigue siendo limitado en aspectos tales como la automatización de despliegues, la definición de procedimientos de reversión, la validación exhaustiva de compatibilidades o la gestión estructurada de cambios.

A diferencia de otros requisitos del bloque, el contenido desarrollado permite identificar una propuesta técnicamente coherente y suficientemente estructurada. **Esta circunstancia resulta consistente con la clasificación de desarrollo suficiente recogida en el Anexo I.** No obstante, la documentación no incorpora mejoras diferenciales ni elementos de innovación que permitan considerar que la solución supera significativamente las capacidades esperables dentro de un servicio estándar de administración de sistemas.

- **Valoración cualitativa**

- **MEDIA**

#### ESIS29 — Gestión y seguimiento del proyecto

- **Requisito y alcance**

La finalidad de este subproyecto consiste en establecer mecanismos de seguimiento, control y coordinación que permitan garantizar una gestión homogénea de los distintos servicios externos integrados en EducaMadrid, proporcionando visibilidad sobre el estado de ejecución de las actuaciones realizadas y facilitando la toma de decisiones por parte de los responsables del servicio.

La memoria contempla actividades orientadas a la supervisión del servicio, la generación de información de seguimiento y la elaboración de mecanismos de coordinación y control. **La propuesta identifica adecuadamente la necesidad de disponer de estructuras de gobernanza que permitan realizar un seguimiento continuo de la evolución de los proyectos y mantener una adecuada comunicación entre los distintos actores implicados.** La cobertura funcional puede considerarse satisfactoria y alineada con los objetivos establecidos en el Documento de Invitación.

- **Análisis de la propuesta**

La documentación incorpora determinados elementos de mejora relacionados con la gobernanza y el seguimiento del servicio que permiten diferenciar la propuesta respecto a una mera reproducción literal de los requisitos. **No obstante, dichas mejoras se centran fundamentalmente en reforzar actividades ya previstas dentro del propio alcance contractual y no introducen capacidades técnicas o metodológicas suficientemente innovadoras como para poder considerarlas valor añadido real.**

**La propuesta aporta una cierta estructuración organizativa y metodológica que justifica una valoración superior a la de los subproyectos clasificados como desarrollo deficiente.** Sin embargo, no desarrolla indicadores avanzados de gobierno, modelos de seguimiento ejecutivo, métricas específicas de rendimiento ni mecanismos de explotación de la información que acrediten un nivel especialmente elevado de madurez. Esta apreciación resulta plenamente coherente con la clasificación de propuesta de mejora sin valor añadido recogida en el Anexo I.

**La propuesta incorpora elementos de mejora identificables y desarrolla adecuadamente los mecanismos generales de gobernanza del servicio.** Sin embargo, el alcance real de dichas mejoras resulta limitado y no permite acreditar una capacidad diferencial especialmente significativa. Por ello, la valoración correspondiente al subproyecto se sitúa en el nivel MEDIO.

- **Fortalezas y valor añadido**

La memoria contempla actividades orientadas a la supervisión del servicio, la generación de información de seguimiento y la elaboración de mecanismos de coordinación y control. **La propuesta identifica adecuadamente la necesidad de disponer de estructuras de gobernanza que permitan realizar un seguimiento continuo de la evolución de los proyectos y mantener una adecuada comunicación entre los distintos actores implicados.** La cobertura funcional puede considerarse satisfactoria y alineada con los objetivos establecidos en el Documento de Invitación.

La documentación incorpora determinados elementos de mejora relacionados con la gobernanza y el seguimiento del servicio que permiten diferenciar la propuesta respecto a una mera reproducción literal de los requisitos. **No obstante, dichas mejoras se centran fundamentalmente en reforzar actividades ya previstas dentro del propio alcance contractual y no introducen capacidades técnicas o metodológicas suficientemente innovadoras como para poder considerarlas valor añadido real.**

- **Carencias, omisiones, errores o riesgos**

La documentación incorpora determinados elementos de mejora relacionados con la gobernanza y el seguimiento del servicio que permiten diferenciar la propuesta respecto a una mera reproducción literal de los requisitos. **No obstante, dichas mejoras se centran fundamentalmente en reforzar actividades ya previstas dentro del propio alcance contractual y no introducen capacidades técnicas o metodológicas suficientemente innovadoras como para poder considerarlas valor añadido real.**

**La propuesta aporta una cierta estructuración organizativa y metodológica que justifica una valoración superior a la de los subproyectos clasificados como desarrollo deficiente.** Sin embargo, no desarrolla indicadores avanzados de gobierno, modelos de seguimiento ejecutivo, métricas específicas de rendimiento ni mecanismos de explotación de la información que acrediten un nivel especialmente elevado de madurez. Esta apreciación resulta plenamente coherente con la clasificación de propuesta de mejora sin valor añadido recogida en el Anexo I.

- **Valoración cualitativa**

- **MEDIA**

#### ESIS30 — Segmentación de la actual red de servidores

- **Requisito y alcance**

Este subproyecto tiene por objeto reforzar los mecanismos de protección de acceso a los sistemas gestionados mediante la incorporación de enfoques avanzados de seguridad basados en principios Zero Trust y en la utilización de mecanismos de autenticación multifactor.

**La propuesta de empresa_n identifica adecuadamente las tendencias actuales en materia de protección de identidades y control de acceso, incorporando referencias explícitas a modelos Zero Trust y a mecanismos de autenticación multifactor.** La memoria reconoce la importancia de reforzar la protección de los sistemas corporativos frente a amenazas derivadas del uso indebido de credenciales y plantea actuaciones orientadas a incrementar el nivel de seguridad asociado a los accesos. La cobertura funcional del requisito puede considerarse adecuada y alineada con los objetivos perseguidos por la Administración.

- **Análisis de la propuesta**

**La incorporación de referencias explícitas a modelos Zero Trust y MFA constituye uno de los pocos elementos claramente diferenciadores identificados dentro del bloque ESIS.** La propuesta introduce capacidades que trascienden la mera reproducción de requisitos y plantea una evolución concreta respecto a mecanismos tradicionales de control de acceso. Además, el Anexo II reconoce expresamente este planteamiento como propuesta con valor añadido.

**No obstante, el grado de desarrollo técnico alcanzado continúa siendo limitado en aspectos tales como la arquitectura de implantación, la integración con los sistemas corporativos existentes, la gestión del ciclo de vida de los factores adicionales de autenticación o los procedimientos necesarios para garantizar una transición segura hacia dicho modelo.** Aunque estas limitaciones impiden considerar la propuesta como excelente, no eliminan el valor diferencial que incorpora respecto al resto de subproyectos del bloque.

La existencia de una propuesta concreta, reconocida expresamente como valor añadido en el Anexo I, junto con la incorporación de capacidades de seguridad diferenciadoras respecto a los requisitos mínimos solicitados, permiten considerar que la solución se sitúa en un nivel claramente superior al predominante dentro del bloque ESIS. **Por ello, la valoración correspondiente se considera ALTA.**

- **Fortalezas y valor añadido**

**La propuesta de empresa_n identifica adecuadamente las tendencias actuales en materia de protección de identidades y control de acceso, incorporando referencias explícitas a modelos Zero Trust y a mecanismos de autenticación multifactor.** La memoria reconoce la importancia de reforzar la protección de los sistemas corporativos frente a amenazas derivadas del uso indebido de credenciales y plantea actuaciones orientadas a incrementar el nivel de seguridad asociado a los accesos. La cobertura funcional del requisito puede considerarse adecuada y alineada con los objetivos perseguidos por la Administración.

**La incorporación de referencias explícitas a modelos Zero Trust y MFA constituye uno de los pocos elementos claramente diferenciadores identificados dentro del bloque ESIS.** La propuesta introduce capacidades que trascienden la mera reproducción de requisitos y plantea una evolución concreta respecto a mecanismos tradicionales de control de acceso. Además, el Anexo II reconoce expresamente este planteamiento como propuesta con valor añadido.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el grado de desarrollo técnico alcanzado continúa siendo limitado en aspectos tales como la arquitectura de implantación, la integración con los sistemas corporativos existentes, la gestión del ciclo de vida de los factores adicionales de autenticación o los procedimientos necesarios para garantizar una transición segura hacia dicho modelo.** Aunque estas limitaciones impiden considerar la propuesta como excelente, no eliminan el valor diferencial que incorpora respecto al resto de subproyectos del bloque.

- **Valoración cualitativa**

- **ALTA**

#### ESIS31 — Optimización de la infraestructura de virtualización del entorno

- **Requisito y alcance**

La finalidad de este subproyecto consiste en optimizar la infraestructura de virtualización que soporta los proyectos exteriores para mejorar su rendimiento, disponibilidad, seguridad, capacidad de crecimiento y estabilidad operativa.

**La oferta dedica un apartado específico a ESIS31 y contempla el análisis de hosts, máquinas virtuales, CPU, memoria, almacenamiento, capacidad, balanceo, redes y recursos asignados.** También prevé revisar pools, crecimiento, alta disponibilidad, snapshots, copias, replicaciones, clústeres, accesos administrativos, segmentación y componentes de virtualización.

- **Análisis de la propuesta**

**Estas evidencias corresponden de forma directa al objeto canónico de ESIS31 y corrigen la asignación anterior de contenido genérico sobre soporte e incidencias.** La propuesta incorpora actuaciones concretas de redistribución de recursos, ajuste de configuraciones, control de sobreasignación, revisión de continuidad y pruebas de carga y rendimiento.

La cobertura es suficiente y evaluable, aunque las medidas de mejora se corresponden en gran parte con la operación ordinaria esperable. La oferta no concreta la plataforma de virtualización objeto de cada actuación, los umbrales de capacidad, las herramientas, las métricas, el plan de ejecución ni los criterios de aceptación.

**La propuesta se clasifica como desarrollo suficiente con una mejora sin valor añadido real.** Su cobertura funcional y técnica corresponde al nivel MEDIA.

- **Fortalezas y valor añadido**

La oferta contempla de forma conjunta capacidad, rendimiento, balanceo, continuidad, seguridad y crecimiento de la infraestructura virtual, y propone verificaciones periódicas y pruebas de carga.

- **Carencias, omisiones, errores o riesgos**

No se definen umbrales, indicadores, herramientas, responsables, calendario de optimización ni criterios verificables de aceptación de los ajustes.

- **Valoración cualitativa**

- **MEDIA**

#### Conclusión del bloque ESIS

El bloque presenta 11 subproyectos con desarrollo suficiente, 18 con desarrollo insuficiente y 2 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **BAJA**.

### Seguridad de aplicaciones WEB (ESEG)

- **Consideración general del bloque**

Este bloque aborda la evaluación continua de la seguridad de las aplicaciones web, la gestión y explotación de sus registros y la supervisión de la superficie de exposición. Deben valorarse el alcance, las metodologías, herramientas, evidencias, priorización, seguimiento y coordinación de la remediación.

#### ESEG1 — Realización de Auditorías/Pentesting Web

- **Requisito y alcance**

Este subproyecto tiene por finalidad la ejecución de auditorías técnicas de seguridad sobre aplicaciones web integradas en el ecosistema EducaMadrid, incluyendo la identificación de vulnerabilidades, la evaluación de configuraciones inseguras, la validación de controles implantados y la elaboración de recomendaciones de mitigación. **Se trata de uno de los requisitos más especializados del contrato, puesto que exige capacidades técnicas avanzadas en materia de análisis ofensivo, evaluación de riesgos y validación de la seguridad de aplicaciones complejas.**

**La propuesta presentada por empresa_n aborda expresamente la realización de auditorías de seguridad sobre aplicaciones web e identifica correctamente la necesidad de detectar vulnerabilidades, analizar configuraciones inseguras y emitir recomendaciones orientadas a la mitigación de riesgos.** La memoria demuestra comprender la finalidad general del requisito y reconoce la importancia de incorporar actividades de validación de seguridad dentro del ciclo de mejora continua de los servicios.

Asimismo, la propuesta contempla la elaboración de informes y la revisión tanto de aspectos funcionales como de configuraciones técnicas, evidenciando una alineación razonable con los objetivos perseguidos por el Documento de Invitación.

- **Análisis de la propuesta**

**No obstante, el desarrollo técnico y metodológico observado resulta limitado para un servicio de la especialización requerida.** La memoria apenas incorpora referencias a metodologías reconocidas de auditoría o pentesting, procedimientos estructurados de ejecución, criterios de clasificación de hallazgos o mecanismos de validación de vulnerabilidades detectadas.

Del mismo modo, la propuesta desarrolla de forma insuficiente elementos especialmente relevantes para este tipo de servicios, como la definición de alcances de prueba, metodologías de explotación controlada, mecanismos de revalidación tras la aplicación de medidas correctoras, criterios de criticidad o procedimientos de seguimiento de remediaciones.

La respuesta transmite conocimiento general del objetivo perseguido, pero no desarrolla suficientemente los mecanismos concretos mediante los cuales se ejecutarán y verificarán las auditorías propuestas.

**La propuesta cubre adecuadamente el alcance funcional solicitado y demuestra comprender la finalidad del servicio.** Sin embargo, la limitada especialización metodológica y la insuficiente concreción técnica reducen significativamente su capacidad para acreditar un enfoque diferencial en un ámbito de elevada complejidad técnica.

Atendiendo al modelo de valoración previsto en el apartado 7.2.2 del Documento de Invitación, la calidad técnica observada se corresponde con el nivel **MEDIA**.

- **Fortalezas y valor añadido**

**La propuesta cubre adecuadamente el alcance funcional solicitado y demuestra comprender la finalidad del servicio.** Sin embargo, la limitada especialización metodológica y la insuficiente concreción técnica reducen significativamente su capacidad para acreditar un enfoque diferencial en un ámbito de elevada complejidad técnica.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el desarrollo técnico y metodológico observado resulta limitado para un servicio de la especialización requerida.** La memoria apenas incorpora referencias a metodologías reconocidas de auditoría o pentesting, procedimientos estructurados de ejecución, criterios de clasificación de hallazgos o mecanismos de validación de vulnerabilidades detectadas.

Del mismo modo, la propuesta desarrolla de forma insuficiente elementos especialmente relevantes para este tipo de servicios, como la definición de alcances de prueba, metodologías de explotación controlada, mecanismos de revalidación tras la aplicación de medidas correctoras, criterios de criticidad o procedimientos de seguimiento de remediaciones.

- **Valoración cualitativa**

- **MEDIA**

#### ESEG2 — Gestión de logs de las aplicaciones Web

- **Requisito y alcance**

**El objetivo de este subproyecto consiste en implantar y mantener mecanismos adecuados de recopilación, tratamiento, correlación y explotación de los registros generados por las aplicaciones web integradas dentro de los servicios de EducaMadrid.** La correcta gestión de logs constituye un elemento esencial para facilitar la detección de incidentes, la investigación de eventos de seguridad y la mejora continua de la operación de los sistemas.

**La propuesta contempla actividades relacionadas con recopilación, tratamiento y supervisión de registros generados por las aplicaciones web gestionadas dentro del contrato.** La memoria demuestra comprender la importancia de los logs tanto para la operación de los sistemas como para la detección e investigación de incidentes de seguridad.

Asimismo, la respuesta incorpora referencias a mecanismos de centralización de información y aprovecha los registros como herramienta de apoyo a la seguridad y a la explotación operativa de los servicios.

- **Análisis de la propuesta**

**No obstante, el nivel de detalle técnico aportado resulta moderado.** La memoria desarrolla escasamente aspectos relacionados con correlación de eventos, normalización de registros, políticas de retención, enriquecimiento de información, explotación analítica o definición de casos de uso específicos para la detección de amenazas.

Del mismo modo, apenas se identifican cuadros de mando, métricas, indicadores de operación o procedimientos de respuesta asociados a la información obtenida mediante los sistemas de registro. **Como consecuencia, la capacidad de verificar objetivamente la eficacia de la solución propuesta resulta limitada.**

La propuesta cubre satisfactoriamente el ámbito funcional requerido y demuestra comprender el valor operativo y de seguridad asociado a la gestión de registros. **Sin embargo, la limitada profundidad técnica observada restringe la valoración alcanzable.**

Conforme al baremo previsto en el Documento de Invitación, la calidad de la respuesta se corresponde con el nivel **MEDIA**.

- **Fortalezas y valor añadido**

**El objetivo de este subproyecto consiste en implantar y mantener mecanismos adecuados de recopilación, tratamiento, correlación y explotación de los registros generados por las aplicaciones web integradas dentro de los servicios de EducaMadrid.** La correcta gestión de logs constituye un elemento esencial para facilitar la detección de incidentes, la investigación de eventos de seguridad y la mejora continua de la operación de los sistemas.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el nivel de detalle técnico aportado resulta moderado.** La memoria desarrolla escasamente aspectos relacionados con correlación de eventos, normalización de registros, políticas de retención, enriquecimiento de información, explotación analítica o definición de casos de uso específicos para la detección de amenazas.

Del mismo modo, apenas se identifican cuadros de mando, métricas, indicadores de operación o procedimientos de respuesta asociados a la información obtenida mediante los sistemas de registro. **Como consecuencia, la capacidad de verificar objetivamente la eficacia de la solución propuesta resulta limitada.**

- **Valoración cualitativa**

- **MEDIA**

#### ESEG3 — Análisis y protección de la superficie de ataque

- **Requisito y alcance**

**Este requisito persigue la identificación continua de los activos expuestos de las aplicaciones web, la evaluación de los riesgos asociados a dicha exposición y la adopción de medidas destinadas a reducir la superficie susceptible de ser explotada por potenciales atacantes.** Se trata de un servicio especialmente relevante en entornos caracterizados por una elevada diversidad tecnológica y múltiples canales de acceso.

**La propuesta identifica correctamente la necesidad de analizar los activos expuestos, evaluar los riesgos asociados a dicha exposición y adoptar medidas orientadas a reducir la superficie susceptible de explotación por terceros.** La memoria demuestra una comprensión adecuada de la finalidad general perseguida por el requisito.

Asimismo, resulta positiva la consideración de la superficie de ataque como un ámbito sujeto a revisión continua y no únicamente a auditorías puntuales, circunstancia alineada con las prácticas actuales de gestión de exposición digital.

- **Análisis de la propuesta**

**Sin perjuicio de lo anterior, la propuesta desarrolla de forma muy limitada los mecanismos concretos necesarios para llevar a cabo dichas actuaciones.** La memoria apenas incorpora referencias a descubrimiento continuo de activos, análisis automatizado de exposición, inventariado dinámico, evaluación de servicios expuestos o mecanismos de priorización basados en riesgo.

Tampoco se concretan para el requisito evaluado tecnologías, herramientas o metodologías específicas que permitan valorar adecuadamente cómo se ejecutarán las tareas de identificación, monitorización y reducción de la superficie de ataque descritas en la propuesta.

**La propuesta cubre formalmente el requisito y demuestra comprender adecuadamente el problema planteado.** Sin embargo, la limitada profundidad técnica observada y la ausencia de mecanismos verificables reducen significativamente el grado de especialización acreditado por la solución.

El documento original asignaba una categoría intermedia (**MEDIA-BAJA**) que conviene eliminar para adaptarse al esquema homogéneo de valoración. Atendiendo al contenido realmente desarrollado, la calidad de la respuesta se corresponde con el nivel **BAJA**.

- **Fortalezas y valor añadido**

**La propuesta identifica correctamente la necesidad de analizar los activos expuestos, evaluar los riesgos asociados a dicha exposición y adoptar medidas orientadas a reducir la superficie susceptible de explotación por terceros.** La memoria demuestra una comprensión adecuada de la finalidad general perseguida por el requisito.

Tampoco se concretan para el requisito evaluado tecnologías, herramientas o metodologías específicas que permitan valorar adecuadamente cómo se ejecutarán las tareas de identificación, monitorización y reducción de la superficie de ataque descritas en la propuesta.

- **Carencias, omisiones, errores o riesgos**

**Sin perjuicio de lo anterior, la propuesta desarrolla de forma muy limitada los mecanismos concretos necesarios para llevar a cabo dichas actuaciones.** La memoria apenas incorpora referencias a descubrimiento continuo de activos, análisis automatizado de exposición, inventariado dinámico, evaluación de servicios expuestos o mecanismos de priorización basados en riesgo.

**La propuesta cubre formalmente el requisito y demuestra comprender adecuadamente el problema planteado.** Sin embargo, la limitada profundidad técnica observada y la ausencia de mecanismos verificables reducen significativamente el grado de especialización acreditado por la solución.

- **Valoración cualitativa**

- **BAJA**

#### Conclusión del bloque ESEG

El bloque presenta 2 subproyectos con desarrollo suficiente, 1 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **MEDIA**.

### Realización de pruebas de desarrollo seguro de aplicaciones WEB (EDSA)

- **Consideración general del bloque**

Este bloque comprende el análisis de seguridad del código y el apoyo a los equipos de desarrollo para prevenir, resolver y verificar vulnerabilidades. Deben valorarse la integración en el ciclo de desarrollo, las técnicas de análisis, las herramientas, la gestión de hallazgos y la transferencia de conocimiento.

#### EDSA1 — Análisis de Código Web

- **Requisito y alcance**

**El subproyecto EDSA1 tiene como finalidad identificar vulnerabilidades e incidencias de seguridad directamente sobre el código fuente de las aplicaciones web gestionadas dentro del ámbito del contrato.** La correcta ejecución de este tipo de análisis permite detectar problemas antes de su explotación en entornos productivos y favorece la incorporación temprana de medidas correctoras.

La propuesta presentada por empresa_n contempla actividades orientadas a la revisión de código fuente y a la identificación de vulnerabilidades de seguridad presentes en aplicaciones web. **La memoria demuestra comprender adecuadamente el papel preventivo que desempeñan estas actuaciones dentro del ciclo de vida del desarrollo software.**

Asimismo, la propuesta incorpora el análisis de código como parte de una estrategia global de mejora continua de la seguridad, circunstancia alineada con los principios de desarrollo seguro perseguidos por el Documento de Invitación.

- **Análisis de la propuesta**

**Sin embargo, la memoria desarrolla de forma limitada las metodologías y procedimientos concretos asociados a este tipo de actividades.** Apenas aparecen referencias a análisis estático, análisis dinámico, revisión manual, clasificación de vulnerabilidades, automatización de controles o integración dentro de ciclos DevSecOps.

Del mismo modo, no se identifican herramientas específicas, procedimientos de revisión estructurados, métricas de seguimiento o mecanismos de validación de hallazgos que permitan acreditar una metodología especialmente desarrollada.

**La propuesta cubre adecuadamente el alcance funcional solicitado y demuestra comprender la finalidad del requisito.** No obstante, la limitada concreción técnica observada impide considerar acreditado un nivel elevado de especialización metodológica.

- **Fortalezas y valor añadido**

La propuesta presentada por empresa_n contempla actividades orientadas a la revisión de código fuente y a la identificación de vulnerabilidades de seguridad presentes en aplicaciones web. **La memoria demuestra comprender adecuadamente el papel preventivo que desempeñan estas actuaciones dentro del ciclo de vida del desarrollo software.**

**La propuesta cubre adecuadamente el alcance funcional solicitado y demuestra comprender la finalidad del requisito.** No obstante, la limitada concreción técnica observada impide considerar acreditado un nivel elevado de especialización metodológica.

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, la memoria desarrolla de forma limitada las metodologías y procedimientos concretos asociados a este tipo de actividades.** Apenas aparecen referencias a análisis estático, análisis dinámico, revisión manual, clasificación de vulnerabilidades, automatización de controles o integración dentro de ciclos DevSecOps.

Del mismo modo, no se identifican herramientas específicas, procedimientos de revisión estructurados, métricas de seguimiento o mecanismos de validación de hallazgos que permitan acreditar una metodología especialmente desarrollada.

- **Valoración cualitativa**

- **MEDIA**

#### EDSA2 — Ayuda al Desarrollo Seguro de Código Web

- **Requisito y alcance**

**El objetivo de este requisito consiste en proporcionar apoyo técnico a los equipos de desarrollo para incorporar buenas prácticas de seguridad durante las distintas fases de construcción y mantenimiento de aplicaciones web.** A diferencia del análisis de código, este subproyecto tiene una orientación principalmente preventiva y de acompañamiento.

La propuesta contempla actividades de asesoramiento, revisión y apoyo a equipos de desarrollo para favorecer la incorporación de buenas prácticas de seguridad durante la construcción y mantenimiento de aplicaciones web. **La memoria demuestra comprender adecuadamente la orientación preventiva del requisito.**

Asimismo, la respuesta evidencia una visión alineada con el objetivo general del Documento de Invitación al considerar que la seguridad debe acompañar todo el ciclo de vida del software y no limitarse exclusivamente a fases finales de validación.

- **Análisis de la propuesta**

**No obstante, el nivel de desarrollo técnico aportado resulta reducido.** La memoria desarrolla de forma insuficiente procedimientos concretos de acompañamiento, modelos de revisión continuada, mecanismos de validación de buenas prácticas, metodologías de formación o indicadores de madurez asociados al desarrollo seguro.

Además, en comparación con otros requisitos, la respuesta aparece especialmente genérica y escasamente diferenciada, dificultando la identificación de una metodología verificable asociada a la asistencia técnica descrita.

Aunque existe cierta cobertura funcional del requisito, la limitada concreción metodológica y la escasa definición de mecanismos operativos reducen significativamente la capacidad de valorar favorablemente la solución.

Por coherencia con el modelo revisado y con las propias observaciones recogidas en el análisis global del documento, esta respuesta debe situarse en **BAJA** y no en MEDIA.

- **Fortalezas y valor añadido**

La propuesta contempla actividades de asesoramiento, revisión y apoyo a equipos de desarrollo para favorecer la incorporación de buenas prácticas de seguridad durante la construcción y mantenimiento de aplicaciones web. **La memoria demuestra comprender adecuadamente la orientación preventiva del requisito.**

Aunque existe cierta cobertura funcional del requisito, la limitada concreción metodológica y la escasa definición de mecanismos operativos reducen significativamente la capacidad de valorar favorablemente la solución.

- **Carencias, omisiones, errores o riesgos**

Asimismo, la respuesta evidencia una visión alineada con el objetivo general del Documento de Invitación al considerar que la seguridad debe acompañar todo el ciclo de vida del software y no limitarse exclusivamente a fases finales de validación.

**No obstante, el nivel de desarrollo técnico aportado resulta reducido.** La memoria desarrolla de forma insuficiente procedimientos concretos de acompañamiento, modelos de revisión continuada, mecanismos de validación de buenas prácticas, metodologías de formación o indicadores de madurez asociados al desarrollo seguro.

- **Valoración cualitativa**

- **BAJA**

#### Conclusión del bloque EDSA

El bloque presenta 2 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **MEDIA**.

### Mantenimiento y gestión del programa de Bug Bounty (EBBO)

- **Consideración general del bloque**

El bloque comprende la revisión y gestión del programa de Bug Bounty, la recepción y tratamiento de informes y la coordinación de la información pública asociada al programa.

#### EBBO1 — Mantenimiento y gestión del programa de Bug Bounty

- **Requisito y alcance**

**El último subproyecto incluido en el Anexo II tiene por finalidad garantizar el mantenimiento operativo y la gestión integral del programa de Bug Bounty asociado a los servicios de EducaMadrid.** Este tipo de iniciativas permiten complementar los mecanismos tradicionales de seguridad mediante la colaboración con investigadores externos encargados de identificar vulnerabilidades de forma controlada y coordinada.

La propuesta presentada por empresa_n cubre formalmente el alcance funcional del requisito e identifica correctamente la finalidad de un programa de Bug Bounty como herramienta complementaria dentro de una estrategia global de ciberseguridad. **La memoria contempla actividades relacionadas con la recepción, análisis, seguimiento y tratamiento de vulnerabilidades reportadas por terceros, evidenciando una comprensión adecuada del funcionamiento general de este tipo de iniciativas.**

Asimismo, la propuesta reconoce la necesidad de integrar la gestión de vulnerabilidades identificadas por investigadores externos dentro de los procedimientos generales de mejora continua de la seguridad de las aplicaciones gestionadas. **Esta aproximación resulta coherente con los objetivos perseguidos por el Documento de Invitación.**

- **Análisis de la propuesta**

**Pese a la adecuada comprensión funcional observada, el desarrollo metodológico de la solución resulta limitado.** La memoria desarrolla escasamente aspectos relacionados con la gobernanza del programa, los procedimientos de clasificación y priorización de hallazgos, la coordinación con los investigadores participantes o los mecanismos de validación técnica de las vulnerabilidades reportadas.

**Tampoco se concretan para el requisito evaluado métricas de gestión, indicadores de rendimiento, objetivos de servicio, modelos de seguimiento de remediaciones o procedimientos específicos para el cierre y verificación de vulnerabilidades corregidas.** Como consecuencia, la propuesta permanece principalmente en un plano conceptual y operativo de alto nivel.

La respuesta demuestra comprender qué actividades deben desarrollarse para gestionar el programa, pero aporta limitada información sobre los mecanismos concretos mediante los cuales dichas actividades serán ejecutadas y controladas.

**La principal fortaleza de la propuesta reside en su correcta comprensión del objetivo funcional perseguido y en la cobertura general del alcance solicitado.** Sin embargo, la limitada definición de procedimientos operativos, métricas, criterios de priorización y mecanismos verificables de gestión reduce significativamente la profundidad técnica de la solución.

Conforme al modelo de valoración establecido en el apartado 7.2.2 del Documento de Invitación, la calidad de la respuesta se corresponde con el nivel **MEDIA**.

- **Fortalezas y valor añadido**

La propuesta presentada por empresa_n cubre formalmente el alcance funcional del requisito e identifica correctamente la finalidad de un programa de Bug Bounty como herramienta complementaria dentro de una estrategia global de ciberseguridad. **La memoria contempla actividades relacionadas con la recepción, análisis, seguimiento y tratamiento de vulnerabilidades reportadas por terceros, evidenciando una comprensión adecuada del funcionamiento general de este tipo de iniciativas.**

Asimismo, la propuesta reconoce la necesidad de integrar la gestión de vulnerabilidades identificadas por investigadores externos dentro de los procedimientos generales de mejora continua de la seguridad de las aplicaciones gestionadas. **Esta aproximación resulta coherente con los objetivos perseguidos por el Documento de Invitación.**

- **Carencias, omisiones, errores o riesgos**

**Pese a la adecuada comprensión funcional observada, el desarrollo metodológico de la solución resulta limitado.** La memoria desarrolla escasamente aspectos relacionados con la gobernanza del programa, los procedimientos de clasificación y priorización de hallazgos, la coordinación con los investigadores participantes o los mecanismos de validación técnica de las vulnerabilidades reportadas.

La respuesta demuestra comprender qué actividades deben desarrollarse para gestionar el programa, pero aporta limitada información sobre los mecanismos concretos mediante los cuales dichas actividades serán ejecutadas y controladas.

- **Valoración cualitativa**

- **MEDIA**

#### Conclusión del bloque EBBO

El bloque presenta 0 subproyectos con desarrollo suficiente, 1 con desarrollo insuficiente y 0 no incluidos. El contraste conjunto de las evidencias, fortalezas y carencias sitúa su valoración cualitativa en **MEDIA**.

### Conclusión del análisis detallado

La oferta acredita una comprensión funcional del servicio y cubre formalmente la mayoría de los códigos, pero el desarrollo efectivo permanece con frecuencia en un plano declarativo. La falta de arquitecturas específicas, herramientas, métricas, criterios de aceptación y procedimientos verificables limita la viabilidad demostrada y la satisfacción de los requisitos. El resultado debe interpretarse conjuntamente con la clasificación individual del anexo y con la evaluación ponderada de los criterios del apartado 7.2.

## EVALUACIÓN DE LA SOLUCIÓN TÉCNICA OFERTADA

### Fundamentación de la valoración

La puntuación se fundamenta en la cobertura y en la calidad efectiva de las soluciones, atendiendo a su concreción, coherencia, adecuación, viabilidad y verificabilidad.

### Arquitectura planteada en los distintos subproyectos — máximo 2 puntos

La arquitectura constituye uno de los criterios fundamentales de evaluación al permitir valorar el grado de estructuración, coherencia y madurez técnica de la solución ofertada. **En un contrato de las características analizadas, la arquitectura no debe limitarse a describir las funcionalidades perseguidas, sino que debe proporcionar una visión técnica suficientemente desarrollada sobre la forma en que los distintos componentes interactuarán entre sí, los mecanismos de integración previstos, las tecnologías utilizadas y los principios de diseño que sustentan la solución.**

**Durante el análisis de la memoria se ha constatado que la propuesta identifica correctamente los principales dominios funcionales del contrato y mantiene una estructura alineada con los bloques definidos en el pliego.** Asimismo, en determinados apartados concretos se observan referencias a conceptos arquitectónicos tales como reutilización de componentes, integración de servicios, desacoplamiento funcional o evolución tecnológica de plataformas existentes.

**No obstante, estos elementos aparecen de forma puntual y aislada.** En la mayor parte de los bloques evaluados la propuesta no desarrolla arquitecturas técnicas completas ni describe con suficiente precisión los mecanismos de interacción entre sistemas, los componentes que intervendrán en las integraciones o las tecnologías concretas que permitirán materializar las soluciones planteadas. Esta circunstancia resulta especialmente evidente en ámbitos como Moodle, integración de aplicaciones externas, sistemas externos o determinados servicios de seguridad, donde las referencias arquitectónicas se sustituyen por descripciones funcionales o por secuencias genéricas de trabajo.

**También se observa una ausencia prácticamente generalizada de diagramas, patrones de integración, modelos de comunicación, estrategias de desacoplamiento, diseño de interfaces o arquitecturas de referencia que permitan evaluar adecuadamente la robustez técnica de las soluciones propuestas.** En numerosos casos, la memoria transmite la intención de realizar determinadas actuaciones, pero no desarrolla la arquitectura necesaria para comprender cómo se ejecutarán realmente.

**Especial relevancia adquiere igualmente la ausencia de arquitecturas específicas en ámbitos donde el propio pliego solicita actuaciones de elevada complejidad técnica, como las integraciones entre aplicaciones, la evolución de plataformas educativas o determinados servicios de sistemas externos.** En estos casos, la falta de detalle técnico dificulta significativamente la valoración del diseño propuesto y reduce la capacidad de verificar su idoneidad para el entorno EducaMadrid.

En consecuencia, aunque la propuesta demuestra comprender el contexto general de los sistemas sobre los que deberá actuar, el contraste con la memoria confirma que el desarrollo arquitectónico es incompleto: faltan arquitecturas específicas, relaciones, diagramas y mecanismos de integración en la mayor parte de los bloques. Estos rasgos corresponden al descriptor BAJA.

**Nivel cualitativo:** BAJA

**Puntuación:** 0,50 sobre 2,00

### Grado de comprensión de los requisitos planteados — máximo 2 puntos

El grado de comprensión de los requisitos tiene como finalidad valorar la capacidad del licitador para interpretar adecuadamente el alcance del contrato, identificar las necesidades reales subyacentes a los distintos requerimientos del pliego y trasladar dicha comprensión a una propuesta técnica coherente y alineada con los objetivos perseguidos por la Administración.

**Desde una perspectiva general, la memoria presentada por empresa_n evidencia que la empresa ha realizado una lectura detallada de la documentación contractual y que comprende el objeto global del servicio.** Esta circunstancia se aprecia en el seguimiento de la estructura general de los distintos bloques funcionales contemplados en el Anexo II y en la identificación de los principales ámbitos de actuación asociados a proyectos web, plataformas educativas, integración de sistemas, infraestructuras, seguridad y operación de servicios.

**Asimismo, puede afirmarse que la propuesta demuestra conocer razonablemente el entorno EducaMadrid y los sistemas sobre los que deberán ejecutarse las actuaciones solicitadas.** La memoria hace referencia a numerosas plataformas y servicios existentes dentro del ecosistema tecnológico objeto del contrato y mantiene una línea argumental consistente respecto a la necesidad de garantizar la continuidad operativa, la evolución tecnológica y la integración de los distintos componentes.

**Sin embargo, el análisis detallado realizado en el capítulo precedente ha puesto de manifiesto una limitación recurrente que condiciona significativamente este criterio.** Aunque la empresa presenta una comprensión global adecuada del alcance funcional de los trabajos, en numerosos apartados sustituye requisitos específicos y técnicamente concretos por descripciones mucho más generales y abstractas. Esta situación resulta especialmente visible en ámbitos como MoodleMisc, integración de aplicaciones, determinados proyectos de sistemas externos o actuaciones relacionadas con desarrollo seguro y seguridad web.

En estos bloques se observa una tendencia reiterada a agrupar múltiples requisitos concretos bajo conceptos genéricos como “integraciones”, “servicios conectados”, “plugins”, “automatización”, “revisiones” o “adaptaciones”, sin desarrollar individualmente los elementos específicos que el pliego solicita de manera expresa. **Como consecuencia, aunque puede concluirse que existe una comprensión general del servicio, resulta más difícil acreditar que se haya realizado un análisis igualmente detallado de todos los requisitos técnicos concretos incluidos en el Documento de Invitación.**

**Especial relevancia adquiere el hecho de que determinados requisitos carecen de una propuesta técnica claramente identificable o presentan una cobertura insuficiente.** El informe de análisis identifica expresamente la ausencia de una propuesta evaluable para ESIS11 y ESIS14, así como una respuesta incompleta en diversos apartados de especial relevancia técnica. EDSA2 sí dispone de una respuesta evaluable de apoyo metodológico al desarrollo seguro. Esta circunstancia evidencia que la comprensión demostrada no alcanza de forma homogénea a la totalidad del alcance funcional solicitado.

**Por otra parte, incluso en aquellos ámbitos donde la cobertura resulta más amplia, la respuesta suele formularse desde una perspectiva funcional u organizativa, sin profundizar suficientemente en las implicaciones técnicas específicas del requisito.** Esta situación se observa con claridad en proyectos como IFP1, donde se responde a la práctica totalidad de los apartados solicitados pero sin desarrollar tecnologías, arquitecturas o mecanismos de implementación concretos vinculados a elementos expresamente exigidos por el pliego.

**En consecuencia, la propuesta demuestra una comprensión aceptable del objeto general del contrato y del entorno sobre el que deberán desarrollarse los trabajos.** No obstante, la agrupación de requisitos, la simplificación de determinadas actuaciones y la ausencia de respuesta evaluable en algunos apartados impiden considerar que exista una comprensión excelente o exhaustiva del conjunto de los requisitos solicitados.

**Nivel cualitativo:** MEDIA

**Puntuación:** 1,00 sobre 2,00

### Viabilidad técnica y operativa del proyecto — máximo 1 punto

La evaluación de la viabilidad tiene por objeto determinar si las soluciones propuestas pueden ejecutarse de manera realista dentro del entorno tecnológico existente y si existen elementos suficientes que permitan considerar alcanzables los objetivos planteados por la oferta.

**Desde esta perspectiva, la propuesta presentada por empresa_n no plantea actuaciones que puedan considerarse técnicamente inviables o incompatibles con las tecnologías y plataformas existentes.** A lo largo de la memoria se identifican secuencias de trabajo lógicas basadas en actividades de análisis, adaptación, validación y puesta en servicio que, en términos generales, resultan compatibles con la naturaleza de los proyectos incluidos en el contrato.

**Asimismo, la empresa evita proponer transformaciones radicales o sustituciones masivas de sistemas que pudieran comportar riesgos desproporcionados.** La mayoría de las actuaciones se orientan hacia la evolución progresiva de los servicios existentes, circunstancia que contribuye positivamente a la percepción de viabilidad global de la propuesta.

**No obstante, la viabilidad de una solución no depende únicamente de que las actuaciones sean conceptualmente posibles, sino también de que la memoria aporte suficiente información para acreditar cómo se llevarán a cabo dichas actuaciones y qué mecanismos permitirán garantizar su correcta ejecución.** En este sentido, las carencias identificadas durante el análisis técnico afectan de forma significativa a la valoración de este criterio.

**La falta de arquitecturas desarrolladas, la ausencia de metodologías verificables, la práctica inexistencia de herramientas concretas asociadas a muchas de las actividades propuestas y la escasez de procedimientos técnicos detallados dificultan la evaluación objetiva de la forma en que se ejecutarán numerosas actuaciones.** Esta situación resulta especialmente relevante en aquellos requisitos que implican integraciones complejas, migraciones tecnológicas, automatización de servicios o actuaciones avanzadas de seguridad e infraestructura.

**A ello se suma la ausencia reiterada de métricas, criterios de aceptación, indicadores de éxito y mecanismos de validación cuantificables, lo que impide comprobar de forma objetiva si los resultados previstos podrán alcanzarse en las condiciones descritas.** Esta circunstancia no invalida la solución, pero sí reduce considerablemente el grado de confianza que puede otorgarse a la propuesta desde una perspectiva estrictamente técnica.

Debe considerarse igualmente que la inexistencia de propuesta técnica evaluable para determinados requisitos del pliego introduce incertidumbre adicional sobre la capacidad de ejecución integral del servicio, ya que no resulta posible verificar la estrategia prevista para abordar dichos trabajos ni su integración dentro de la prestación global.

En consecuencia, aunque la propuesta no presenta elementos que permitan cuestionar su viabilidad básica, la falta de profundidad técnica y el escaso nivel de desarrollo de numerosos apartados limitan significativamente la solidez de este criterio.

**Nivel cualitativo:** MEDIA

**Puntuación:** 0,40 sobre 1,00

### Metodología de trabajo aplicada — máximo 1 punto

La metodología constituye uno de los apartados donde las debilidades de la propuesta resultan más evidentes y recurrentes a lo largo del conjunto de la memoria técnica.

**El análisis realizado permite comprobar que empresa_n utiliza de forma constante una terminología asociada a procesos de revisión, análisis, validación, supervisión, actualización y seguimiento.** Estas referencias reflejan la existencia de una intención metodológica general y permiten identificar una aproximación organizativa a la gestión de los trabajos.

**Sin embargo, cuando se analiza el contenido específico de las actuaciones propuestas, se observa que dichas referencias metodológicas rara vez se traducen en procedimientos técnicos concretos.** La memoria repite de manera sistemática expresiones como “se analizará”, “se revisará”, “se validará”, “se verificará” o “se documentará”, pero en la mayoría de los casos no explica cómo se desarrollarán esas actividades ni qué herramientas, técnicas, procedimientos o recursos serán utilizados para ejecutarlas.

**Esta circunstancia se reproduce de forma transversal en prácticamente todos los bloques analizados.** Tanto en proyectos Liferay como en Moodle, integración de aplicaciones, sistemas externos, seguridad de aplicaciones web, desarrollo seguro o gestión del programa de Bug Bounty, las actividades se describen generalmente mediante acciones genéricas de carácter organizativo, sin llegar a desarrollar una metodología técnica verificable.

**Del mismo modo, no se identifican entregables específicos para la mayoría de las actuaciones, ni criterios objetivos de aceptación, ni procedimientos estructurados de validación que permitan comprobar el cumplimiento de los trabajos realizados.** Tampoco se desarrollan mecanismos de control de calidad asociados a cada actividad ni modelos formales de seguimiento orientados a medir resultados.

Otro aspecto especialmente relevante es la escasa presencia de herramientas concretas. La memoria evita de forma recurrente mencionar plataformas, productos, marcos de trabajo o tecnologías específicas que permitan sustentar técnicamente las metodologías descritas. **Como consecuencia, muchas de las actuaciones terminan presentándose como intenciones de trabajo razonables, pero insuficientemente desarrolladas para acreditar una metodología robusta y repetible.**

En consecuencia, aunque existe una aproximación organizativa básica y una secuencia lógica mínima en numerosos apartados, la propuesta no desarrolla una metodología técnica suficientemente formalizada ni verificable para alcanzar valoraciones elevadas dentro de este criterio.

**Nivel cualitativo:** MEDIA

**Puntuación:** 0,50 sobre 1,00

### Rendimiento previsible de las soluciones — máximo 1 punto

El criterio de rendimiento tiene como finalidad valorar la capacidad de la propuesta para mejorar o mantener los niveles de servicio requeridos mediante soluciones eficientes, escalables y correctamente dimensionadas.

**La memoria de empresa_n incorpora numerosas referencias a conceptos asociados a optimización, mejora continua, modernización tecnológica, evolución de plataformas y revisión del comportamiento de los sistemas.** En términos generales, existe una intención clara de mejorar la operación y la eficiencia de los distintos entornos incluidos en el contrato.

**No obstante, el principal problema observado durante el análisis de este criterio es la práctica ausencia de información objetiva que permita evaluar el rendimiento esperado de las soluciones propuestas.** La memoria no incorpora métricas cuantificables, indicadores de capacidad, tiempos objetivo, umbrales de rendimiento, pruebas de carga, KPIs de operación ni criterios verificables de mejora.

**La ausencia de métricas constituye una de las debilidades más repetidas a lo largo de prácticamente todos los bloques analizados.** Tanto en los proyectos Liferay como en IFP, MoodleMisc, Integración, Sistemas Externos, Seguridad Web, Desarrollo Seguro y Bug Bounty, la propuesta menciona actuaciones de mejora, optimización, revisión o modernización, pero rara vez incorpora indicadores que permitan cuantificar los beneficios esperados o verificar posteriormente su consecución.

**Esta situación resulta especialmente significativa en aquellos ámbitos donde el propio pliego demanda actuaciones con una fuerte componente tecnológica, como la modernización de plataformas, la evolución de bases de datos, la integración de servicios, la implantación de mecanismos de seguridad o la optimización de infraestructuras.** En estos casos sería razonable esperar referencias a objetivos de rendimiento, indicadores de disponibilidad, métricas de carga, tiempos de respuesta, criterios de escalabilidad o parámetros similares que permitieran valorar objetivamente la eficacia de las soluciones propuestas. Sin embargo, dichos elementos apenas aparecen desarrollados en la memoria.

**Asimismo, Tampoco se concretan para el requisito evaluado procedimientos concretos de medición del rendimiento ni herramientas específicas destinadas a monitorizar la evolución de los sistemas tras la implantación de las actuaciones propuestas.** Como consecuencia, la valoración de este criterio debe realizarse fundamentalmente a partir de intenciones generales de mejora y no sobre evidencias técnicas cuantificadas.

**Debe señalarse además que numerosos apartados utilizan formulaciones orientadas al análisis, revisión o supervisión del comportamiento de los sistemas, pero sin concretar mecanismos que permitan traducir dichas actividades en mejoras verificables del rendimiento.** Esta circunstancia dificulta considerablemente la capacidad de valorar el impacto real de las actuaciones ofertadas sobre los servicios objeto del contrato.

En consecuencia, aunque la propuesta incorpora referencias generales compatibles con una voluntad de optimización de los sistemas, la ausencia casi absoluta de métricas, indicadores, objetivos cuantificados y procedimientos de medición impide considerar acreditado un nivel suficiente de desarrollo en materia de rendimiento.

**Nivel cualitativo:** BAJA

**Puntuación:** 0,25 sobre 1,00

### Satisfacción de los requisitos del Anexo II — máximo 8 puntos

El grado de satisfacción de los requisitos constituye el criterio con mayor peso dentro del bloque de solución técnica, puesto que permite valorar de manera integrada el nivel de cobertura real alcanzado respecto al conjunto de obligaciones definidas en el Anexo II del Documento de Invitación.

Desde una perspectiva general, debe reconocerse que la propuesta presentada por empresa_n sigue la estructura global del pliego y proporciona una respuesta para una parte importante de los requisitos solicitados. En numerosos bloques se observa una intención clara de alinearse con las actuaciones requeridas y de dar cobertura a los distintos ámbitos funcionales incluidos en el contrato. **Esta circunstancia resulta especialmente visible en proyectos como IFP1, donde la empresa aborda una parte significativa de los requisitos recogidos en el pliego y demuestra una comprensión razonable del alcance funcional solicitado.**

**Sin embargo, la valoración de este criterio no debe realizarse únicamente sobre la existencia formal de respuestas, sino también sobre la profundidad, calidad y completitud de dichas respuestas.** Desde esta perspectiva, el análisis desarrollado a lo largo del capítulo 2 ha puesto de manifiesto limitaciones relevantes que afectan de forma directa al grado de satisfacción alcanzado.

**Una de las deficiencias más recurrentes consiste en la agrupación de requisitos técnicos concretos bajo conceptos genéricos de carácter funcional.** Este patrón aparece de forma especialmente acusada en el bloque MoodleMisc, donde numerosos elementos específicos solicitados por el pliego desaparecen dentro de categorías amplias como integraciones, plugins, automatización o servicios conectados, sin recibir un tratamiento individualizado. Como consecuencia, aunque formalmente existe una respuesta, resulta difícil verificar el nivel real de cobertura alcanzado respecto a los requisitos concretos solicitados.

Similar situación se observa en ámbitos como Integración con EducaMadrid, Sistemas Externos o determinados servicios de seguridad, donde la memoria describe objetivos generales compatibles con el pliego, pero sin desarrollar suficientemente los mecanismos técnicos necesarios para acreditar la cobertura efectiva de las actuaciones requeridas. **La ausencia de arquitecturas, metodologías, herramientas concretas y procedimientos verificables limita considerablemente la calidad de la respuesta proporcionada.**

A esta circunstancia se añade la existencia de requisitos para los que no ha sido posible identificar una propuesta técnica específica evaluable. El análisis realizado concluye expresamente que no existe una respuesta claramente identificable para ESIS11 y ESIS14, lo que supone una cobertura incompleta del alcance funcional solicitado por el Documento de Invitación. EDSA2 sí contiene una respuesta evaluable y se mantiene en la clasificación del anexo y del CSV. **La omisión de los dos apartados indicados tiene una relevancia significativa dentro de la valoración del presente criterio, ya que impide considerar plenamente satisfechos la totalidad de los requisitos incluidos en el contrato.**

**Asimismo, en otros apartados donde sí existe respuesta, ésta se limita frecuentemente a describir actividades genéricas de revisión, análisis, seguimiento o validación, sin incorporar elementos técnicos que permitan valorar la profundidad real de la solución propuesta.** Esta situación afecta especialmente a proyectos relacionados con ENS, ciberseguridad, monitorización, desarrollo seguro o gestión del programa de Bug Bounty, ámbitos que en la memoria reciben un tratamiento claramente inferior al nivel de detalle técnico que cabría esperar para alcanzar valoraciones elevadas.

En consecuencia, el contraste con la memoria confirma una cobertura parcial significativa, pero también una respuesta frecuentemente genérica, carencias técnicas relevantes y dos requisitos sin solución evaluable. Los 26 desarrollos insuficientes y la ausencia de solución evaluable para ESIS11 y ESIS14 sitúan el subcriterio en el nivel MEDIA.

**Nivel cualitativo:** MEDIA

**Puntuación:** 4,00 sobre 8,00

### Resultado global de la solución técnica

| **Subcriterio**                | **Máximo** | **Nivel** | **Puntuación** |
| ------------------------------ | ---------: | --------- | -------------: |
| Arquitectura                   |       2,00 | BAJA      |           0,50 |
| Comprensión de los requisitos  |       2,00 | MEDIA     |           1,00 |
| Viabilidad                     |       1,00 | MEDIA     |           0,40 |
| Metodología                    |       1,00 | MEDIA     |           0,50 |
| Rendimiento                    |       1,00 | BAJA      |           0,25 |
| Satisfacción de los requisitos |       8,00 | MEDIA     |           4,00 |
| **TOTAL SOLUCIÓN TÉCNICA**     |  **15,00** |           |       **6,65** |

## EVALUACIÓN DE LA PLANIFICACIÓN DEL SERVICIO

### Consideraciones generales sobre la planificación

La planificación se valora como herramienta real de gestión: correspondencia con los proyectos, secuencia y duración de tareas, dependencias, hitos, recursos, entregables y mecanismos de riesgo, contingencia, calidad y trazabilidad.

### Calendario de los trabajos a desarrollar — máximo 11 puntos

La planificación temporal constituye el núcleo principal de este criterio, por cuanto debe permitir verificar la distribución de los trabajos a lo largo del periodo contractual, la adecuada secuenciación de actividades, la compatibilidad entre los recursos asignados y el volumen de trabajo previsto, así como la cobertura continuada de los servicios incluidos en el contrato.

**La propuesta presentada por empresa_n incorpora un cronograma general en el que se reflejan distintas actuaciones distribuidas temporalmente a lo largo de un periodo determinado.** Esta representación permite obtener una visión general de la intención organizativa de la empresa y de las principales líneas de actuación previstas para la ejecución del servicio.

**No obstante, el análisis detallado del cronograma revela una primera limitación de carácter estructural que afecta a su interpretabilidad.** La documentación no incorpora ninguna leyenda que permita determinar el significado de los colores empleados, la naturaleza de las distintas marcas gráficas reflejadas ni la relación existente entre dichas representaciones y los recursos efectivamente asignados. Como consecuencia, no resulta posible establecer con certeza qué perfiles participan en cada actividad ni cuál es la dedicación real prevista para cada una de ellas.

**Esta carencia adquiere especial relevancia en un contrato de elevada complejidad técnica y funcional, donde la correcta asignación de recursos especializados constituye un elemento fundamental para garantizar la viabilidad del servicio.** La ausencia de información que permita relacionar actividades, perfiles y dedicaciones dificulta significativamente la evaluación de la suficiencia de los medios previstos para la ejecución de los trabajos.

**A esta limitación se suma una segunda deficiencia de especial importancia.** El contrato objeto de licitación contempla una duración de dos años, mientras que la planificación aportada únicamente desarrolla actuaciones comprendidas entre junio de 2026 y mayo de 2027, sin incluir una planificación equivalente para el segundo año contractual. Esta circunstancia impide verificar cómo se prestarán los servicios durante aproximadamente la mitad del periodo de ejecución previsto.

La ausencia de planificación correspondiente al segundo año afecta de forma directa a la valoración de este criterio, ya que no sólo limita la visibilidad sobre la continuidad operativa del servicio, sino que también imposibilita analizar la asignación de recursos, la distribución de cargas de trabajo, la evolución de los proyectos y la cobertura efectiva de las actividades recurrentes durante una parte sustancial del contrato.

**Igualmente, relevante resulta la inexistencia de una asociación clara entre determinadas actividades reflejadas en el cronograma y los requisitos específicos analizados en el capítulo anterior.** En aquellos casos donde la propuesta técnica presentaba carencias significativas o no incluía una solución evaluable, Tampoco se concretan para el requisito evaluado actividades de planificación claramente vinculadas que permitan inferir cómo se llevarán a cabo dichos trabajos. Como consecuencia, la trazabilidad entre requisitos, propuesta técnica y planificación resulta limitada.

**Otro aspecto que condiciona negativamente la valoración es la dificultad para justificar determinadas duraciones y niveles de dedicación asignados a trabajos de elevada complejidad técnica.** El cronograma no incorpora un desglose suficiente de actividades, subtareas, entregables asociados ni criterios de validación intermedios que permitan verificar la razonabilidad temporal de algunas de las actuaciones previstas. Ello dificulta considerablemente la evaluación objetiva de la carga de trabajo real contemplada para proyectos de integración, ciberseguridad, automatización o evolución de infraestructuras.

Por todo ello, aunque la propuesta incorpora una planificación básica que permite identificar la existencia de una organización temporal inicial de los trabajos, las carencias detectadas limitan de forma muy significativa su utilidad como instrumento de gestión y seguimiento del servicio.

**Nivel cualitativo:** BAJA

**Puntuación:** 1,80 sobre 11,00

### Análisis de riesgos del proyecto — máximo 1 punto

El análisis de riesgos presentado por empresa_n constituye uno de los apartados que presenta un nivel de desarrollo relativamente superior al observado en otros elementos de la planificación.

La memoria identifica diversos factores susceptibles de afectar a la correcta prestación del servicio, reconociendo la existencia de riesgos asociados a la complejidad tecnológica del entorno, la coexistencia de múltiples plataformas, la evolución de infraestructuras existentes y la necesidad de coordinar actuaciones sobre sistemas altamente interdependientes.

También se aprecia una preocupación por aspectos relacionados con la continuidad del servicio, la gestión de cambios y la necesidad de minimizar impactos sobre los sistemas productivos. **Estas consideraciones reflejan una comprensión razonable de los principales riesgos inherentes a la operación de una plataforma compleja como EducaMadrid.**

**No obstante, el análisis realizado permite identificar igualmente determinadas limitaciones.** La gestión de riesgos se plantea principalmente desde una perspectiva conceptual, sin desarrollar con suficiente detalle metodologías formales de evaluación, criterios de clasificación, matrices de impacto y probabilidad o mecanismos específicos de seguimiento de riesgos durante la ejecución del contrato.

Asimismo, no se observa una vinculación clara entre los riesgos identificados y los distintos bloques funcionales del servicio, lo que dificulta valorar el grado de cobertura alcanzado frente a riesgos específicos asociados a subproyectos particularmente complejos.

El contraste con la memoria confirma que existe un análisis de riesgos identificable y razonablemente alineado con la naturaleza del contrato: se reconocen escenarios de continuidad, seguridad, infraestructura y despliegue y se describen prevención, detección y respuesta. La ausencia de una matriz formal, cuantificación y vinculación completa a los subproyectos impide calificarlo como bueno, pero el desarrollo sí alcanza el descriptor de análisis correcto.

**Nivel cualitativo:** MEDIA

**Puntuación:** 0,50 sobre 1,00

### Plan de gestión de contingencias — máximo 1 punto

La propuesta incorpora igualmente referencias a mecanismos orientados a gestionar situaciones excepcionales, incidencias críticas y escenarios que pudieran comprometer la continuidad de los servicios.

Desde una perspectiva general, la memoria transmite la intención de mantener la operatividad de los sistemas mediante procedimientos de respuesta ante incidencias, coordinación técnica y actuaciones correctivas destinadas a restablecer la normalidad operativa en el menor plazo posible.

**Sin embargo, al igual que sucede en otros bloques de la oferta, estas referencias permanecen fundamentalmente en un plano organizativo y conceptual.** No se desarrollan en detalle los procedimientos técnicos específicos que deberían ejecutarse ante distintos escenarios de contingencia ni se describen planes de actuación diferenciados para las principales categorías de riesgo identificadas.

Tampoco se concretan para el requisito evaluado tiempos objetivo de recuperación, mecanismos formales de escalado, responsabilidades asociadas a los distintos niveles de contingencia ni procedimientos documentados de validación una vez restablecido el servicio. **Esta ausencia de elementos verificables limita la valoración alcanzable en este apartado.**

No obstante, la existencia de un planteamiento específico orientado a la gestión de contingencias permite considerar cubierto el requisito en un nivel básico.

**Nivel cualitativo:** BAJA

**Puntuación:** 0,25 sobre 1,00

### Plan de gestión de la calidad del servicio — máximo 1 punto

El plan de calidad presentado por empresa_n se apoya en principios generales de mejora continua, seguimiento del servicio, control de actividades y revisión periódica de resultados.

**La propuesta transmite una orientación favorable hacia el aseguramiento de la calidad y refleja la intención de incorporar mecanismos de control sobre la ejecución de los trabajos.** Asimismo, aparecen referencias a la generación de documentación, seguimiento de actividades y revisión de la correcta prestación de los servicios.

**Sin embargo, el desarrollo de este apartado vuelve a presentar una importante carencia de indicadores objetivos.** La memoria no establece métricas concretas de calidad, umbrales de cumplimiento, procedimientos formalizados de auditoría interna ni criterios claramente definidos para evaluar los resultados obtenidos en cada uno de los bloques funcionales.

La mayor parte del contenido se formula mediante declaraciones generales relativas a la mejora continua y al seguimiento de la prestación del servicio, sin que lleguen a identificarse herramientas, procedimientos de medición o mecanismos verificables que permitan controlar objetivamente la calidad de las actuaciones ejecutadas.

En consecuencia, aunque existe un planteamiento de calidad presente en la propuesta, su grado de desarrollo resulta limitado.

**Nivel cualitativo:** BAJA

**Puntuación:** 0,25 sobre 1,00

### Trazabilidad del servicio — máximo 1 punto

La trazabilidad constituye uno de los aspectos más afectados por las deficiencias observadas en la planificación general presentada por el licitador.

Como ya se ha indicado anteriormente, la falta de identificación de perfiles, la ausencia de leyenda explicativa en el cronograma y la limitada relación existente entre actividades, recursos y requisitos dificultan considerablemente el seguimiento integral de los trabajos previstos.

**Esta situación se ve agravada por la inexistencia de dependencias entre actividades, hitos de control claramente definidos, caminos críticos o mecanismos que permitan verificar la evolución real de los distintos proyectos a medida que avance la ejecución contractual.** El cronograma constituye esencialmente una distribución temporal de actuaciones, pero no proporciona información suficiente para realizar un seguimiento exhaustivo del progreso de los trabajos.

Asimismo, tampoco se observa una vinculación suficientemente desarrollada entre los requisitos del pliego, las actividades de la planificación y los entregables asociados a cada actuación. **Esta falta de trazabilidad dificulta la comprobación de que todos los requisitos solicitados disponen de una planificación específica y de que dicha planificación resulta compatible con los medios previstos para su ejecución.**

Como consecuencia, la capacidad de control y seguimiento que ofrece la planificación aportada debe considerarse limitada.

**Nivel cualitativo:** BAJA

**Puntuación:** 0,25 sobre 1,00

### Resultado global de la planificación

| **Subcriterio**                     | **Máximo** | **Nivel** | **Puntuación** |
| ----------------------------------- | ---------: | --------- | -------------: |
| Calendario y planificación temporal |      11,00 | BAJA      |           1,80 |
| Análisis de riesgos                 |       1,00 | MEDIA     |           0,50 |
| Plan de contingencias               |       1,00 | BAJA      |           0,25 |
| Plan de calidad                     |       1,00 | BAJA      |           0,25 |
| Trazabilidad                        |       1,00 | BAJA      |           0,25 |
| **TOTAL PLANIFICACIÓN**             |  **15,00** |           |       **3,05** |

## RESULTADO FINAL CONSOLIDADO

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                    6,65 |
| Planificación del servicio |                 15,00 |                    3,05 |
| **PUNTUACIÓN FINAL**       |             **30,00** |                **9,70** |

### Interpretación de la puntuación

La oferta presenta una comprensión general aceptable y una cobertura documental extensa, pero no acredita de forma homogénea cómo se ejecutarán, validarán y controlarán numerosas actuaciones. Las deficiencias de concreción técnica se acumulan con una planificación incompleta para el periodo contractual, por lo que la calidad global resulta insuficiente. La puntuación mantiene la correspondencia con los niveles y resultados parciales consignados en las tablas anteriores.

## CONCLUSIONES FINALES Y PROPUESTA

### Conclusiones globales de la evaluación técnica

La oferta presenta una comprensión general aceptable y una cobertura documental extensa, pero no acredita de forma homogénea cómo se ejecutarán, validarán y controlarán numerosas actuaciones. Las deficiencias de concreción técnica se acumulan con una planificación incompleta para el periodo contractual, por lo que la calidad global resulta insuficiente.

### Conclusiones sobre la solución técnica

La oferta acredita una comprensión funcional del servicio y cubre formalmente la mayoría de los códigos, pero el desarrollo efectivo permanece con frecuencia en un plano declarativo. La falta de arquitecturas específicas, herramientas, métricas, criterios de aceptación y procedimientos verificables limita la viabilidad demostrada y la satisfacción de los requisitos. La solución técnica obtiene **6,65 puntos sobre 15**.

### Conclusiones sobre la planificación del servicio

La planificación obtiene **3,05 puntos sobre 15**. Su resultado refleja el grado de detalle temporal, la relación con los subproyectos y la formalización de riesgos, contingencias, calidad y trazabilidad descritos en el análisis.

### Justificación de la valoración

Las puntuaciones parciales responden a las evidencias identificadas en cada subproyecto y a su traslación a los seis criterios de solución técnica y los cinco de planificación. El resultado es proporcionado a la cobertura efectiva, la profundidad técnica, la viabilidad, las mejoras y las carencias acreditadas.

### Aplicación del umbral mínimo y propuesta final

La propuesta de **empresa_n** obtiene una puntuación de **9,70 puntos sobre 30** en los criterios sujetos a juicio de valor.

El umbral mínimo exigido para continuar en el procedimiento es de **15 puntos sobre 30**. Por tanto, la oferta **NO ALCANZA** el nivel mínimo de calidad técnica establecido.

En consecuencia, procede proponer la **exclusión de la oferta del procedimiento**.

### Garantía de igualdad de trato y objetividad

La valoración aplica los criterios, el nivel de exigencia y las reglas de puntuación de la plantilla común, y se fundamenta exclusivamente en las evidencias contenidas en la oferta y en la documentación reguladora.

## ANEXO. RELACIÓN DE PROYECTOS Y GRADO DE DESARROLLO DE LA PROPUESTA TÉCNICA

### Objeto y criterios de clasificación

El presente anexo resume, de manera sistemática, el grado de desarrollo de la propuesta técnica para cada proyecto o subproyecto del Anexo II. Su finalidad es aportar trazabilidad documental al análisis, sin sustituir la motivación cualitativa del informe ni producir por sí solo una traslación automática a la puntuación final.

- **Propuesta técnica no incluida:** no existe una solución concreta para el proyecto o subproyecto.

- **Propuesta técnica incluida con desarrollo insuficiente o deficiente:** existe contenido, pero es genérico o carece de procesos, arquitectura, herramientas o mecanismos de implementación suficientes.

- **Propuesta técnica incluida con desarrollo suficiente:** existe una solución concreta y evaluable, con un grado adecuado de definición técnica.

De forma separada se indican las propuestas de mejora sin valor añadido real (PM), las propuestas con valor añadido (VA) y los errores técnicos relevantes.

### Tablas de subproyectos

#### Proyectos Web Liferay (ELIF)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                   |
| ------------ | ----------------------- | ------ | --------- | --------------------------------------- |
| ELIF1        | SUFICIENTE              | VA     | NO        | virtual hosts y despliegues controlados |
| ELIF2        | SUFICIENTE              | VA     | NO        | design system corporativo reutilizable  |
| ELIF3        | SUFICIENTE              | VA     | NO        | arquitectura frontend desacoplada       |
| ELIF4        | SUFICIENTE              | PM     | NO        | mejora continua accesibilidad           |

#### Innovación y Formación del Profesorado (IFP)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**         |
| ------------ | ----------------------- | ------ | --------- | ----------------------------- |
| IFP1         | SUFICIENTE              | NO     | NO        | Desarrollo técnico evaluable. |

#### Proyectos MoodleMisc (EMOM)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                               |
| ------------ | ----------------------- | ------ | --------- | --------------------------------------------------- |
| EMOM1        | SUFICIENTE              | VA     | NO        | CI/CD y auditoría automatizada                      |
| EMOM2        | SUFICIENTE              | PM     | NO        | evolucionar el modelo actual                        |
| EMOM3        | SUFICIENTE              | PM     | NO        | evolucionar el modelo descrito                      |
| EMOM4        | SUFICIENTE              | PM     | NO        | reforzar el enfoque descrito                        |
| EMOM5        | SUFICIENTE              | NO     | NO        | Desarrollo técnico evaluable.                       |
| EMOM6        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |
| EMOM7        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |

#### Proyectos de Dinámicas (EDIN)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                               |
| ------------ | ----------------------- | ------ | --------- | --------------------------------------------------- |
| EDIN1        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |
| EDIN2        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |

#### Integración con la plataforma EducaMadrid (EIPE)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                               |
| ------------ | ----------------------- | ------ | --------- | --------------------------------------------------- |
| EIPE1        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |
| EIPE2        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |

#### Proyectos de Sistemas Externos (ESIS)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                                        |
| ------------ | ----------------------- | ------ | --------- | ------------------------------------------------------------ |
| ESIS1        | SUFICIENTE              | VA     | NO        | actualización con validaciones previas                       |
| ESIS2        | SUFICIENTE              | VA     | NO        | optimización continua BBDD                                   |
| ESIS3        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS4        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS5        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS6        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS7        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS8        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS9        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS10       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS11       | NO INCLUIDA             | NO     | NO        | No se incluye una solución técnica concreta.                 |
| ESIS12       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS13       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS14       | NO INCLUIDA             | NO     | NO        | No se incluye una solución técnica concreta.                 |
| ESIS15       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS16       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS17       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS18       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS19       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS20       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS21       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS22       | SUFICIENTE              | PM     | NO        | Metodología Magerit                                          |
| ESIS23       | SUFICIENTE              | NO     | NO        | Desarrollo técnico evaluable.                                |
| ESIS24       | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado.          |
| ESIS25       | SUFICIENTE              | VA     | NO        | OpenNMS, Cacti, alertas avanzadas y scripts personalizados   |
| ESIS26       | SUFICIENTE              | PM     | NO        | 2FA, certificados, TLS y revisión de vulnerabilidades        |
| ESIS27       | SUFICIENTE              | VA     | NO        | SIEM OpenSource                                              |
| ESIS28       | SUFICIENTE              | NO     | NO        | Desarrollo técnico evaluable.                                |
| ESIS29       | SUFICIENTE              | PM     | NO        | gobernanza y seguimiento                                     |
| ESIS30       | SUFICIENTE              | VA     | NO        | Zero Trust y MFA                                             |
| ESIS31       | SUFICIENTE              | PM     | NO        | optimización de capacidad, rendimiento y alta disponibilidad |

#### Seguridad de Aplicaciones Web (ESEG)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                               |
| ------------ | ----------------------- | ------ | --------- | --------------------------------------------------- |
| ESEG1        | SUFICIENTE              | VA     | NO        | pentesting y seguimiento vulnerabilidades           |
| ESEG2        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |
| ESEG3        | SUFICIENTE              | VA     | NO        | supervisión superficie exposición                   |

#### Desarrollo Seguro de Aplicaciones Web (EDSA)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                |
| ------------ | ----------------------- | ------ | --------- | ------------------------------------ |
| EDSA1        | SUFICIENTE              | VA     | NO        | análisis automatizado código         |
| EDSA2        | SUFICIENTE              | PM     | NO        | apoyo metodológico desarrollo seguro |

#### Gestión del programa de Bug Bounty (EBBO)

| **Proyecto** | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                               |
| ------------ | ----------------------- | ------ | --------- | --------------------------------------------------- |
| EBBO1        | INSUFICIENTE            | NO     | NO        | Desarrollo genérico o insuficientemente concretado. |

### Resumen cuantitativo del anexo

#### Grado de desarrollo

| **Clasificación**                    | **Número de proyectos** | **Porcentaje** |
| ------------------------------------ | ----------------------: | -------------: |
| No incluidos                         |                       2 |         3,77 % |
| Desarrollo insuficiente o deficiente |                      26 |        49,06 % |
| Desarrollo suficiente                |                      25 |        47,17 % |
| **TOTAL DE PROYECTOS**               |                  **53** |   **100,00 %** |

#### Indicadores adicionales

Los siguientes indicadores no son excluyentes entre sí ni respecto del grado de desarrollo.

| **Indicador**                                  | **Número de proyectos** | **Porcentaje sobre el total** |
| ---------------------------------------------- | ----------------------: | ----------------------------: |
| Con errores técnicos relevantes                |                       0 |                        0,00 % |
| Con propuesta de mejora sin valor añadido real |                       9 |                       16,98 % |
| Con propuesta de mejora con valor añadido real |                      12 |                       22,64 % |

### Conclusión del anexo

La clasificación más frecuente sigue siendo el desarrollo insuficiente o genérico: afecta a 26 subproyectos y, junto con los 2 no incluidos, suma 28 de los 53 códigos. Las carencias se repiten en ELIF, Moodle Misc, Dinámicas, integración, sistemas externos y desarrollo seguro; IFP y otros proyectos concretos alcanzan un desarrollo suficiente. La ausencia de ESIS11 y ESIS14, junto con la limitada planificación del segundo año contractual, constituye una deficiencia relevante y no un hecho aislado. Esta clasificación aporta trazabilidad, pero la puntuación final deriva de la valoración conjunta de todos los criterios y no de un recuento automático de categorías.
