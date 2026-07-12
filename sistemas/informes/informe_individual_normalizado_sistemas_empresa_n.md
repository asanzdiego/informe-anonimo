# INFORME DE VALORACIÓN TÉCNICA INDIVIDUAL

- **Contrato:** DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)
- **Licitador:** empresa_n

## RESUMEN EJECUTIVO

### Objeto del informe

El presente informe tiene por objeto realizar la **valoración técnica de la propuesta presentada por empresa_n** en el procedimiento basado en el **Sistema Dinámico de Adquisición SDA 26/2021**, relativo a los servicios de **DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)**.

El informe determina la puntuación correspondiente a los criterios sujetos a juicio de valor, comprueba el cumplimiento del **umbral mínimo de 15 puntos sobre 30** y formula la propuesta de continuación o exclusión que procede para la oferta.

### Metodología de valoración

La evaluación se ha estructurado en dos niveles complementarios. En primer lugar, se ha realizado un análisis técnico detallado de los proyectos y subproyectos incluidos en el Anexo II del Documento de Invitación, examinando el grado de desarrollo, adecuación y verificabilidad de las soluciones propuestas. En segundo lugar, los resultados de dicho análisis se han trasladado al esquema de valoración previsto en el apartado 7.2 del Documento de Invitación, asignando las puntuaciones correspondientes en función del nivel real de adecuación observado.

Este enfoque garantiza la trazabilidad entre **los requisitos definidos, las evidencias contenidas en la memoria, el análisis técnico efectuado y la puntuación final asignada**.

### Síntesis técnica de la propuesta

La propuesta presenta una cobertura formal amplia y una identificación correcta del entorno de EducaMadrid, pero su desarrollo es mayoritariamente descriptivo. Faltan arquitecturas específicas, procedimientos operativos, herramientas, métricas, criterios de aceptación y mecanismos de validación. La referencia a Métrica V3 y algunos contenidos evaluables en GitLab y Redmine aportan valor parcial, sin compensar la baja concreción ni la ausencia de solución en bloques completos.

### Principales conclusiones del análisis

El patrón dominante es el desarrollo insuficiente: 66 de los 89 subproyectos se clasifican como insuficientes y 21 no incluyen solución concreta. MAX e IA carecen de desarrollo técnico evaluable, mientras las carencias de BD, MON, CLO, COR, CON y MIG son recurrentes. Solo UPD5 y UPD8 alcanzan desarrollo suficiente y el valor añadido real es residual.

### Resultado de la valoración

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                  5,05 |
| Planificación del servicio |                 15,00 |                  6,40 |
| **TOTAL**                  |             **30,00** |              **11,45** |

### Conclusión del resumen ejecutivo

La propuesta obtiene 11,45 puntos sobre 30 y no alcanza el umbral mínimo de 15 puntos. Procede proponer su exclusión en coherencia con las fortalezas y carencias desarrolladas en el informe.

## INTRODUCCIÓN

### Alcance del informe

El presente informe evalúa la memoria técnica presentada por **empresa_n** para la prestación de los servicios de **DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)**. El análisis comprende tanto la **solución técnica ofertada** como la **planificación del servicio**, de acuerdo con los criterios sujetos a juicio de valor establecidos en el apartado 7.2 del Documento de Invitación.

La evaluación toma como referencia los proyectos, subproyectos, actuaciones y entregables definidos en el Anexo II, y atiende exclusivamente al contenido efectivamente desarrollado en la documentación presentada.

### Marco normativo

El presente informe se elabora en el marco del procedimiento de adjudicación correspondiente a **Sistema Dinámico de Adquisición SDA 26/2021**. El procedimiento se rige por lo dispuesto en la **Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público** (en adelante, LCSP), por el Pliego de Cláusulas Administrativas Particulares y por las condiciones específicas establecidas en el Documento de Invitación y demás documentación reguladora del expediente.

La valoración técnica se fundamenta en los **criterios de adjudicación sujetos a juicio de valor definidos en el apartado 7.2 del Documento de Invitación**, cuya finalidad es evaluar la calidad de la propuesta desde una perspectiva integral que contemple tanto la **adecuación de la solución técnica ofertada** como la **viabilidad organizativa y temporal de su ejecución**.

De conformidad con el **artículo 145 de la LCSP**, los criterios de adjudicación deben permitir determinar la mejor relación calidad-precio y aplicarse de forma objetiva, transparente y no discriminatoria. La evaluación se realiza, por tanto, con arreglo a los principios de **igualdad de trato, objetividad, transparencia, proporcionalidad y trazabilidad**, aplicando a todas las ofertas un mismo marco metodológico y sin incorporar elementos externos a la documentación presentada por los licitadores.

Asimismo, el **artículo 146.3 de la LCSP** permite establecer umbrales mínimos en los criterios cualitativos sujetos a juicio de valor. Conforme al Documento de Invitación, las ofertas deben alcanzar un **nivel mínimo de calidad técnica equivalente al cincuenta por ciento de la puntuación máxima asignable a estos criterios** para continuar en el procedimiento.

La aplicación de este umbral no constituye una decisión discrecional: una vez constatado su incumplimiento, la oferta afectada no puede continuar en las fases posteriores del procedimiento. La valoración debe permitir **comprobar de forma clara la puntuación obtenida y motivar la correspondiente propuesta de admisión o exclusión**.

La evaluación se ajusta igualmente al **principio de evaluabilidad**, conforme al cual únicamente pueden valorarse los elementos de la oferta que estén suficientemente desarrollados y que permitan su comprobación objetiva. Las declaraciones genéricas, las capacidades presumidas, las referencias no desarrolladas o las soluciones futuras no descritas en la memoria no pueden suplirse mediante inferencias del órgano evaluador.

### Contexto técnico del servicio

EducaMadrid constituye un entorno tecnológico complejo y de gran escala que integra servicios interdependientes de bases de datos, almacenamiento, monitorización, videoconferencia, colaboración, cloud, correo electrónico, sistema operativo MAX, aulas virtuales, LDAP y portal educativo, seguridad, contenedores, migración entre CPDs e inteligencia artificial.

La infraestructura comprende más de 700 servidores y aproximadamente 3.500 bases de datos. Su operación exige especialización, automatización y mecanismos verificables de disponibilidad, seguridad, rendimiento, escalabilidad, continuidad, integración y trazabilidad.

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

- **EXCELENTE:** hasta el 100 % de la puntuación de la sección correspondiente.
- **ALTA:** hasta el 75 % de la puntuación de la sección correspondiente.
- **MEDIA:** hasta el 50 % de la puntuación de la sección correspondiente.
- **BAJA:** hasta el 25 % de la puntuación de la sección correspondiente.
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

- **EXCELENTE:** hasta el 100 % de la puntuación de la sección correspondiente.
- **ALTA:** hasta el 75 % de la puntuación de la sección correspondiente.
- **MEDIA:** hasta el 50 % de la puntuación de la sección correspondiente.
- **BAJA:** hasta el 25 % de la puntuación de la sección correspondiente.
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

La memoria está formalmente estructurada y reconoce el alcance del contrato, pero no mantiene una relación verificable entre requisitos, arquitectura, soluciones, metodología y planificación. Predominan formulaciones generales; no se definen de forma sistemática componentes, interfaces, métricas, entregables ni criterios de aceptación, y MAX e IA quedan sin contenido técnico evaluable.

#### Nivel de desarrollo técnico y grado de concreción

La memoria está formalmente estructurada y reconoce el alcance del contrato, pero no mantiene una relación verificable entre requisitos, arquitectura, soluciones, metodología y planificación. Predominan formulaciones generales; no se definen de forma sistemática componentes, interfaces, métricas, entregables ni criterios de aceptación, y MAX e IA quedan sin contenido técnico evaluable.

#### Comprensión y adaptación al entorno EducaMadrid

La memoria está formalmente estructurada y reconoce el alcance del contrato, pero no mantiene una relación verificable entre requisitos, arquitectura, soluciones, metodología y planificación. Predominan formulaciones generales; no se definen de forma sistemática componentes, interfaces, métricas, entregables ni criterios de aceptación, y MAX e IA quedan sin contenido técnico evaluable.

#### Arquitectura, integración y requisitos no funcionales

La memoria está formalmente estructurada y reconoce el alcance del contrato, pero no mantiene una relación verificable entre requisitos, arquitectura, soluciones, metodología y planificación. Predominan formulaciones generales; no se definen de forma sistemática componentes, interfaces, métricas, entregables ni criterios de aceptación, y MAX e IA quedan sin contenido técnico evaluable.

#### Trazabilidad y evaluabilidad

La memoria está formalmente estructurada y reconoce el alcance del contrato, pero no mantiene una relación verificable entre requisitos, arquitectura, soluciones, metodología y planificación. Predominan formulaciones generales; no se definen de forma sistemática componentes, interfaces, métricas, entregables ni criterios de aceptación, y MAX e IA quedan sin contenido técnico evaluable.

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

### Consideraciones generales sobre la propuesta

#### Enfoque global de evaluación

La propuesta presenta una cobertura formal amplia y una identificación correcta del entorno de EducaMadrid, pero su desarrollo es mayoritariamente descriptivo. Faltan arquitecturas específicas, procedimientos operativos, herramientas, métricas, criterios de aceptación y mecanismos de validación. La referencia a Métrica V3 y algunos contenidos evaluables en GitLab y Redmine aportan valor parcial, sin compensar la baja concreción ni la ausencia de solución en bloques completos.

#### Cobertura del Anexo II

El patrón dominante es el desarrollo insuficiente: 66 de los 89 subproyectos se clasifican como insuficientes y 21 no incluyen solución concreta. MAX e IA carecen de desarrollo técnico evaluable, mientras las carencias de BD, MON, CLO, COR, CON y MIG son recurrentes. Solo UPD5 y UPD8 alcanzan desarrollo suficiente y el valor añadido real es residual.

#### Fortalezas y aportaciones de valor añadido

Se reconocen la comprensión general del entorno y la cobertura formal del alcance, con contenidos puntualmente evaluables en GitLab y Redmine. Estas fortalezas permiten una valoración parcial, pero el anexo solo identifica valor añadido real en UPD8.

#### Carencias, errores y riesgos recurrentes

Se repiten la falta de arquitecturas específicas, procedimientos, herramientas, métricas y criterios de aceptación; MAX e IA carecen de solución evaluable y las mejoras son mayoritariamente incrementales. El efecto acumulado reduce la viabilidad y la satisfacción de requisitos.

### Análisis por bloques funcionales del Anexo II

El análisis utiliza la misma estructura para los 89 subproyectos: requisito, contraste de la propuesta, fortalezas, carencias y nivel cualitativo. La clasificación individual se conserva en el anexo.

#### Bloque BD — Bases de Datos

##### Consideración general del bloque

El bloque comprende la operación a gran escala de MariaDB, PostgreSQL, MongoDB y ProxySQL; clústeres, replicación, balanceo, optimización, CMDB, sincronización, seguridad, observabilidad y persistencia en microservicios.

El contraste identifica 0 subproyectos con desarrollo suficiente, 6 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### BD1 — Mantenimiento y mejora de entornos de Bases de Datos MariaDB y ProxySQL avanzado

###### Requisito y alcance

**El subproyecto BD1 define un conjunto de requisitos técnicos claramente orientados a la operación avanzada de entornos MariaDB en configuración clusterizada, incluyendo la optimización de nodos, la gestión de ProxySQL como elemento de balanceo y la monitorización del sistema mediante herramientas específicas.** Este tipo de entornos exige la definición de arquitecturas distribuidas, control de replicación, gestión de tráfico de lectura y escritura y mecanismos automatizados de alta disponibilidad.

###### Análisis de la propuesta

En relación con las propuestas de mejora, éstas se limitan a reforzar las actividades ya descritas, como la revisión y seguimiento del estado del sistema, sin introducir elementos técnicos adicionales ni metodologías específicas, lo que impide identificar un valor diferencial respecto a las tareas base.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta presentada por empresa_n aborda este subproyecto mediante una descripción general de tareas de mantenimiento, entre las que se incluyen la comprobación del estado de los servidores, la revisión de configuraciones, la validación del balanceo y la verificación de conectividad. **No obstante, el análisis técnico evidencia que no se desarrolla ningún procedimiento específico asociado a la optimización de entornos clusterizados, ni se describen mecanismos de replicación, ni configuraciones avanzadas de ProxySQL, ni estrategias de balanceo dinámico.** Asimismo, no se identifican herramientas concretas de monitorización, siendo sustituido este elemento por referencias genéricas a soluciones no especificadas.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD2 — Mantenimiento y optimización proactiva de las bases de datos de toda la plataforma

###### Requisito y alcance

**El subproyecto BD2 se centra en la optimización continua de un entorno compuesto por miles de bases de datos, incluyendo la mejora de consultas, la seguridad de conexiones, el mantenimiento preventivo y la planificación de actuaciones en períodos no lectivos.** Este requisito implica necesariamente la utilización de métricas, herramientas de análisis de rendimiento y estrategias de automatización adaptadas a gran escala.

###### Análisis de la propuesta

Las propuestas de mejora identificadas se basan en la ampliación de las tareas de revisión y mantenimiento ya descritas, sin aportar elementos técnicos adicionales ni metodologías diferenciadas, lo que limita su impacto real sobre el rendimiento del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n plantea actividades como la revisión de consultas, la aplicación de ajustes, la ejecución de copias de seguridad y la planificación de intervenciones en horarios de baja actividad. **Sin embargo, el análisis revela la ausencia de métricas de rendimiento, herramientas de análisis de consultas, planes de indexación o mecanismos de análisis estadístico.** Tampoco se define una estrategia específica para la gestión de aproximadamente 3.500 bases de datos ni se detallan mecanismos de seguridad asociados al cifrado de conexiones o la gestión de certificados.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD3 — Mantenimiento de las bases de datos de gestión de la configuración de EducaMadrid

###### Requisito y alcance

**Este subproyecto exige el desarrollo de una CMDB avanzada, incluyendo la incorporación de relaciones físicas y lógicas, el modelado de dependencias, la automatización de la carga de información y el uso de herramientas de software libre.** Se trata de un requisito clave para la gestión integral de la infraestructura.

###### Análisis de la propuesta

**La propuesta de empresa_n se limita a describir actividades como la revisión de elementos registrados, la actualización de información y la importación de datos, sin desarrollar mecanismos de descubrimiento automático, inventariado dinámico ni integración con otras plataformas.** Tampoco se describen modelos de relaciones ni estructuras de dependencias entre sistemas, ni se identifican herramientas concretas de software libre, como exige el Documento de Invitación.

Las propuestas de mejora siguen el mismo patrón observado en el resto del bloque, consistiendo en la ampliación de las tareas de revisión y actualización, sin incorporar automatización ni evolución funcional del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

El desarrollo es genérico o incompleto. La observación del anexo precisa: actualización CMDB sin automatización.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD4 — Mantenimiento de las bases de datos de las Aulas Virtuales

###### Requisito y alcance

El Documento de Invitación establece que este subproyecto debe abordar la gestión de un entorno de alta complejidad, con miles de bases de datos distribuidas en múltiples servidores, incluyendo el análisis de carga, la redistribución de información y la adaptación arquitectónica.

###### Análisis de la propuesta

Las mejoras propuestas consisten en reforzar las labores de seguimiento y control, sin introducir procedimientos técnicos adicionales, lo que no permite identificar una evolución real de la solución.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe actividades como la revisión de carga, el seguimiento de rendimiento y la incorporación o eliminación de servidores, manteniéndose en un nivel descriptivo.** No se identifican herramientas de análisis de rendimiento, ni metodologías de redistribución, ni mecanismos de balanceo o replicación orientados a entornos de gran escala. Tampoco se desarrolla una estrategia específica para gestionar el volumen de bases de datos indicado en el Documento de Invitación.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD5 — Mantenimiento de disparadores y Foreign Data Wrappers en los entornos Portal y LDAP Plano

###### Requisito y alcance

Este subproyecto requiere la implementación de mecanismos de sincronización entre sistemas, incluyendo el mantenimiento de disparadores, la gestión de FDW y el análisis de consistencia de la información entre Portal y LDAP.

###### Análisis de la propuesta

**La propuesta de empresa_n se limita a mencionar la revisión de registros, la comprobación de triggers y la verificación de conectividad, sin desarrollar mecanismos de sincronización, planificación de ejecuciones ni procedimientos de validación de datos.** Tampoco se abordan aspectos como la resolución de conflictos, la consistencia de información o la auditoría de datos entre sistemas.

Las propuestas de mejora se centran en ampliar las tareas de revisión, sin aportar mecanismos técnicos que permitan garantizar la sincronización efectiva de los sistemas implicados.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

El desarrollo es genérico o incompleto. La observación del anexo precisa: verificación sin sincronización avanzada.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD6 — Implementación y mantenimiento de bases de datos en entornos de microservicios

###### Requisito y alcance

El subproyecto BD6 introduce un contexto tecnológico basado en arquitecturas de microservicios, incluyendo la adopción de entornos DevOps, la gestión del ciclo de vida de los servicios y la adaptación de las bases de datos a arquitecturas distribuidas.

###### Análisis de la propuesta

Las propuestas de mejora consisten en la ampliación de tareas de mantenimiento general, sin introducir elementos propios de arquitecturas modernas basadas en microservicios.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n plantea actividades centradas en la instalación de versiones, la verificación de funcionamiento y el mantenimiento correctivo, lo que refleja un enfoque propio de entornos tradicionales.** No se describen mecanismos de orquestación, ni integración con contenedores, ni estrategias de persistencia de datos en entornos distribuidos. Tampoco se abordan aspectos como la automatización de despliegues o la observabilidad del sistema.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque BD

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 6 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque MON — Monitorización, testeo y pruebas de rendimiento

##### Consideración general del bloque

El bloque comprende la gestión de capacidad y almacenamiento NFS, las pruebas de carga y estrés, las métricas y umbrales, la observabilidad, el alertado proactivo y la monitorización específica de servicios de IA.

El contraste identifica 0 subproyectos con desarrollo suficiente, 4 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### MON1 — Mantenimiento periódico del almacenamiento de los centros

###### Requisito y alcance

**El subproyecto MON1 establece como requisito la redistribución periódica de la ocupación entre distintos sistemas de almacenamiento NFS, el análisis de la ocupación real, la reorganización del almacenamiento y la ejecución de estas tareas en periodos no lectivos.** Se trata de un requisito claramente orientado a la gestión activa de capacidad y a la optimización del uso del almacenamiento en un entorno distribuido.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar las tareas de supervisión y reorganización, sin incorporar mecanismos adicionales que permitan determinar cómo se gestionará de forma efectiva la redistribución periódica exigida.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n describe actividades como la revisión de la ocupación, la identificación de posibles desequilibrios, el movimiento de información entre sistemas y la reorganización del almacenamiento. **Sin embargo, el análisis técnico evidencia que no se define ninguna metodología concreta para realizar la redistribución de datos, ni se establecen criterios objetivos de balanceo, ni se identifican métricas de ocupación o crecimiento.** Tampoco se describen procedimientos de migración de datos, automatización de procesos ni análisis de rendimiento específico del sistema NFS.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MON2 — Realización periódica de pruebas de estrés en diferentes entornos de la plataforma

###### Requisito y alcance

**El subproyecto MON2 requiere la ejecución de pruebas de carga y estrés orientadas a la medición del rendimiento, el análisis de resultados, la identificación de anomalías y la determinación de sus causas, así como la propuesta de soluciones.** Este requisito implica la definición de metodologías de ingeniería de rendimiento y el uso de herramientas específicas.

###### Análisis de la propuesta

Las propuestas de mejora se basan en ampliar la ejecución de pruebas y la revisión de resultados, sin introducir metodologías estructuradas ni procesos de análisis profundo, lo que limita significativamente el alcance técnico del planteamiento.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta presentada por empresa_n menciona la realización de pruebas de carga mediante simulación de accesos concurrentes, así como el análisis general de resultados y la revisión del rendimiento.** No obstante, el análisis detallado muestra que no se describen procedimientos concretos para la ejecución de pruebas de carga avanzadas, resistencia o degradación controlada. Tampoco se identifican herramientas de testeo, ni se establecen escenarios de carga, ni se definen modelos de análisis de resultados o correlación con sistemas de monitorización.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MON3 — Mantenimiento del sistema de monitorización y estadísticas de uso

###### Requisito y alcance

**El subproyecto MON3 exige la actualización continua del sistema de monitorización, la incorporación de nuevos servicios, el uso de herramientas open source y la redefinición de alertas tanto reactivas como proactivas.** Este requisito implica la definición de una arquitectura de monitorización, métricas concretas y una estrategia de alertado.

###### Análisis de la propuesta

Las propuestas de mejora se centran en ampliar la monitorización y el seguimiento, manteniéndose en un nivel genérico y sin aportar elementos técnicos que permitan evaluar la evolución del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n incluye la incorporación de nuevos sistemas, la actualización de herramientas, el seguimiento de alertas y la elaboración de informes. **Sin embargo, el análisis técnico pone de manifiesto la ausencia de una arquitectura definida de monitorización, así como la no identificación de herramientas específicas.** No se describen métricas, umbrales, clasificación de alertas ni mecanismos de correlación de eventos.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MON4 — Monitorización y estadísticas de servicios basados en IA

###### Requisito y alcance

**El subproyecto MON4 introduce la monitorización específica de servicios basados en inteligencia artificial, incluyendo modelos de lenguaje, endpoints de inferencia, estadísticas de consumo y alertas específicas.** Este requisito tiene un carácter especializado y requiere la definición de métricas y herramientas adaptadas a plataformas de IA.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a extender los procesos generales de monitorización, sin introducir elementos diferenciales asociados a la naturaleza específica de los sistemas de inteligencia artificial.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n describe actividades como el alta de modelos, la revisión de conectividad, la monitorización general y la generación de informes. **No obstante, no se identifican métricas específicas para modelos de IA, ni mecanismos de observabilidad, ni análisis de consumo, ni sistemas de alertado adaptados a este tipo de servicios.**

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque MON

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 4 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque UPD — Actualización de servicios existentes

##### Consideración general del bloque

El bloque comprende arquitecturas y procedimientos para videoconferencia, grabación, colaboración, gestión de proyectos, encuestas, calidad de código, streaming, bibliotecas, configuración, contenedores y decomisionado.

El contraste identifica 2 subproyectos con desarrollo suficiente, 12 con desarrollo insuficiente y 1 no incluidos; 1 incorporan valor añadido según la clasificación del anexo.

##### UPD1 — Mantenimiento y mejora de los sistemas de videoconferencias de EducaMadrid

###### Requisito y alcance

**El subproyecto UPD1 exige la actualización periódica de plataformas de videoconferencia, incluyendo migraciones de versión, adaptación de componentes, optimización del rendimiento y compatibilidad con navegadores.** Se trata de un entorno complejo que requiere gestión de arquitecturas distribuidas y control de concurrencia.

###### Análisis de la propuesta

Las propuestas de mejora consisten en reforzar las tareas de validación y seguimiento, sin introducir mecanismos técnicos adicionales que permitan evaluar la evolución de la plataforma.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n plantea actividades como la instalación de versiones, la validación de compatibilidad y el mantenimiento correctivo. **Sin embargo, no se desarrollan aspectos técnicos relacionados con la arquitectura del sistema, la escalabilidad, la gestión de sesiones concurrentes ni la optimización del rendimiento en entornos de alta carga.**

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD2 — Mantenimiento y mejora del sistema secundario de videoconferencias con opción de grabación

###### Requisito y alcance

Este subproyecto introduce funcionalidades específicas de grabación y procesamiento de sesiones, lo que implica la gestión de almacenamiento, procesamiento y escalabilidad.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque genérico, sin incorporar elementos diferenciados asociados a la funcionalidad de grabación.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta presentada resulta prácticamente idéntica a la del subproyecto anterior, sin adaptarse a las particularidades del sistema de grabación.** No se mencionan componentes específicos como el procesamiento de grabaciones, la gestión de almacenamiento ni los mecanismos asociados al sistema BigBlueButton.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD3 — Mantenimiento y mejora de Mattermost

###### Requisito y alcance

El subproyecto exige la gestión de una plataforma de comunicación interna con dependencias en bases de datos, sistemas de indexación y mecanismos de alta disponibilidad.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar las tareas existentes sin aportar desarrollo técnico adicional.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe tareas de actualización y mantenimiento, incorporando algunas fases de validación, pero no desarrolla los componentes técnicos de la plataforma.** No se mencionan elementos como bases de datos, integración LDAP, ni arquitecturas de alta disponibilidad.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD4 — Mantenimiento y mejora de la solución Kanban

###### Requisito y alcance

El subproyecto plantea la gestión de una herramienta de tipo Kanban, incluyendo su mantenimiento, actualización y evolución funcional.

###### Análisis de la propuesta

El análisis específico se integra en las fortalezas y carencias que siguen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta presentada por empresa_n se limita a describir actividades genéricas como actualización, validación y gestión de incidencias.** No se identifica la herramienta concreta utilizada, ni se desarrollan funcionalidades específicas relacionadas con la gestión de proyectos o automatización de tareas.

Las propuestas de mejora no incorporan elementos adicionales y mantienen el mismo nivel de generalidad.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD5 — Mantenimiento y mejora de GitLab

###### Requisito y alcance

El subproyecto UPD5 exige la gestión de una plataforma compleja de desarrollo colaborativo, incluyendo pipelines, repositorios y herramientas de integración continua.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque y no aportan elementos técnicos diferenciados.

###### Fortalezas y valor añadido

Se acredita una solución concreta y evaluable, aunque la mejora asociada no constituye por sí sola un valor añadido real.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n aborda este subproyecto como si se tratara de una aplicación convencional, describiendo tareas de actualización y mantenimiento preventivo.** No se desarrollan componentes propios de la plataforma ni se identifican elementos específicos de su arquitectura.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD6 — Mantenimiento y mejora de LimeSurvey

###### Requisito y alcance

**El subproyecto UPD6 establece como requisito la actualización de la herramienta LimeSurvey, la mejora de su arquitectura, la optimización del rendimiento y la evolución funcional del sistema.** Se trata de un entorno que requiere una comprensión clara de su arquitectura, de la gestión de bases de datos subyacentes y de la experiencia de usuario.

###### Análisis de la propuesta

Las propuestas de mejora identificadas mantienen el mismo enfoque descriptivo, centrado en ajustes generales y revisiones, sin introducir elementos técnicos adicionales que permitan evaluar una evolución real del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta presentada por empresa_n describe actuaciones relacionadas con la revisión de la apariencia, la aplicación de ajustes y la validación del rendimiento general. **Sin embargo, no se desarrollan aspectos técnicos relacionados con la arquitectura objetivo, la escalabilidad del sistema ni la optimización de las consultas asociadas.** Tampoco se identifican mecanismos de mejora de experiencia de usuario ni se describen procedimientos de prueba orientados a validar el rendimiento en escenarios reales.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD7 — Mantenimiento y mejora de SonarQube

###### Requisito y alcance

El subproyecto UPD7 exige el mantenimiento y mejora de la plataforma SonarQube, incluyendo la gestión de calidad de código, reglas de análisis, perfiles de calidad y control de calidad de proyectos.

###### Análisis de la propuesta

En la propuesta de empresa_n se detecta una **desviación relevante**, ya que el contenido asociado a este subproyecto no corresponde con SonarQube, sino que hace referencia a Redmine, evidenciando una reutilización de contenido no adaptada al requisito. Como consecuencia, desaparecen elementos fundamentales como los perfiles de calidad, las reglas específicas de análisis de código, los Quality Gates o la gestión de proyectos en SonarQube.

Las propuestas de mejora asociadas a este subproyecto se encuentran igualmente afectadas por esta incongruencia, al basarse en un contenido que no corresponde con la tecnología requerida.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

El desarrollo es genérico o incompleto. La observación del anexo precisa: contenido incorrecto sin valor.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD8 — Mantenimiento y mejora de Redmine

###### Requisito y alcance

El subproyecto UPD8 plantea la gestión de la herramienta Redmine, incluyendo automatización, mantenimiento evolutivo y mejora funcional.

###### Análisis de la propuesta

Las propuestas de mejora se centran en reforzar los elementos ya descritos, sin introducir nuevas líneas de evolución técnica, manteniéndose dentro de un enfoque incremental.

###### Fortalezas y valor añadido

La memoria identifica una aportación de valor añadido: uso API y automatización básica.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n presenta en este caso un mayor grado de alineación con el requisito, identificando elementos como la API REST, la automatización mediante scripts y la incorporación de mecanismos de autenticación adicional. **No obstante, el desarrollo técnico continúa siendo limitado, ya que no se describen arquitecturas, estrategias de despliegue ni integración con otros sistemas como LDAP o SSO.**

###### Valoración cualitativa

**Valoración cualitativa: ALTA**

El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD9 — Mantenimiento y configuración de Wowza Streaming Engine

###### Requisito y alcance

El subproyecto UPD9 requiere la gestión de una plataforma de streaming basada en tecnologías como Wowza, incluyendo protocolos de transmisión, codificación de vídeo y distribución de contenidos.

###### Análisis de la propuesta

Las propuestas de mejora se encuentran afectadas por la misma desviación, al no estar vinculadas al subproyecto requerido.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La propuesta presentada por empresa_n **no responde al requisito**, ya que el contenido asociado a este subproyecto describe nuevamente aspectos relacionados con SonarQube, repitiendo un contenido no aplicable a la tecnología solicitada. Como consecuencia, no se identifican elementos propios de streaming como protocolos RTMP, RTSP, HLS ni componentes de codificación o distribución de vídeo.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD10 — Mantenimiento y gestión de contenidos AbiesWeb

###### Requisito y alcance

El subproyecto UPD10 está orientado a la gestión de contenidos bibliográficos mediante AbiesWeb, incluyendo la carga masiva de datos, la sincronización con sistemas externos y la gestión de catálogos.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar las actividades de gestión ya descritas, sin introducir elementos adicionales que permitan evaluar una mejora significativa del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n presenta una respuesta parcial, centrada en tareas de mantenimiento básico y gestión general de contenidos. **Sin embargo, no se desarrollan procedimientos de carga masiva, ni se describen mecanismos de integración con sistemas externos, ni se abordan aspectos relacionados con la sincronización de información.**

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD11 — Actualización, mantenimiento y gestión de contenidos de Abies+

###### Requisito y alcance

Este subproyecto exige la evolución del sistema Abies+, incluyendo la realización de pruebas, la implementación de mejoras y la gestión de contenidos.

###### Análisis de la propuesta

Las propuestas de mejora se mantienen en el mismo nivel de generalidad, limitándose a ampliar tareas existentes sin introducir mecanismos de evolución estructurada.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n se centra fundamentalmente en tareas de actualización y resolución de incidencias, incluyendo una gestión básica de contenidos. **No obstante, no se desarrollan procedimientos de prueba, ni mecanismos de validación, ni planes de evolución funcional del sistema.** Tampoco se aborda la posible migración desde sistemas previos.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD12 — Implementación, mantenimiento y mejora de Empieza

###### Requisito y alcance

El subproyecto UPD12 presenta un alto nivel de exigencia técnica, incluyendo la necesidad de escalado horizontal y vertical, alta disponibilidad, balanceo de carga y optimización del rendimiento.

###### Análisis de la propuesta

Las propuestas de mejora se centran en reforzar estas ideas, sin concretar los elementos técnicos necesarios para su implementación.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n menciona aspectos como ajustes de alta disponibilidad, configuración de balanceo y revisión de arquitectura. **Sin embargo, no identifica mecanismos concretos ni herramientas específicas asociadas a estos conceptos.** No se describen balanceadores, ni arquitecturas de clustering ni mecanismos de replicación, manteniéndose en un nivel conceptual sin desarrollo técnico.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD13 — Mantenimiento y mejora del sistema de gestión de la configuración

###### Requisito y alcance

El subproyecto UPD13 exige el uso de herramientas específicas como CMDBuild y Ansible, así como la automatización de procesos y la correlación de datos.

###### Análisis de la propuesta

Las propuestas de mejora no introducen las herramientas ni los mecanismos requeridos, manteniéndose en un enfoque generalista.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n incluye referencias a automatización básica y revisión de datos, pero omite las herramientas específicas indicadas en el Documento de Invitación. **No se desarrollan mecanismos de correlación de información ni integración entre sistemas, lo que limita la capacidad del sistema de gestión de configuración.**

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD14 — Mantenimiento, actualización y mejora de la solución de contenedores

###### Requisito y alcance

Este subproyecto requiere la gestión de entornos de contenedores, incluyendo tecnologías específicas como Docker, Kubernetes o Podman, así como la automatización de despliegues y la gestión de infraestructuras.

###### Análisis de la propuesta

Las propuestas de mejora se mantienen en el mismo nivel de generalidad, sin introducir herramientas ni arquitecturas específicas.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe tareas de actualización de plataformas y ejecución de scripts generales, sin identificar las tecnologías concretas ni los mecanismos de orquestación.** No se desarrollan arquitecturas de contenedores ni procesos de despliegue automatizado.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD15 — Mantenimiento, gestión y decomisionado de servidores

###### Requisito y alcance

El subproyecto UPD15 exige la gestión completa del ciclo de vida de servidores, incluyendo su retirada, gestión de DNS, direcciones IP, almacenamiento y eliminación de dependencias.

###### Análisis de la propuesta

Las propuestas de mejora consisten en ampliar las tareas de revisión, sin introducir procedimientos completos de gestión del ciclo de vida.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n se limita a describir la eliminación de servidores y la actualización del inventario, sin desarrollar procedimientos completos de decomisionado.** No se abordan aspectos como la gestión de DNS, la limpieza de almacenamiento ni la retirada de configuraciones asociadas.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque UPD

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 2 desarrollos suficientes, 12 insuficientes y 1 no incluidos, con 1 aportaciones de valor añadido.

#### Bloque CLO — Cloud

##### Consideración general del bloque

El bloque comprende disponibilidad, escalabilidad, almacenamiento temporal, edición en línea, integración, seguridad, rendimiento, actualización y continuidad de los servicios cloud de EducaMadrid.

El contraste identifica 0 subproyectos con desarrollo suficiente, 2 con desarrollo insuficiente y 1 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### CLO1 — Mantenimiento del servicio de la nube de EducaMadrid

###### Requisito y alcance

**El subproyecto CLO1 requiere la mejora y evolución de la infraestructura cloud, incluyendo la distribución de carga para un entorno de aproximadamente dos millones de usuarios, la redistribución del almacenamiento, la planificación de capacidad a medio y largo plazo y la gestión de cuotas.** Se trata de un requisito claramente orientado a entornos de alta escalabilidad y gestión avanzada de infraestructura.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo nivel de generalidad, sin introducir elementos técnicos adicionales ni procedimientos concretos, lo que impide identificar un planteamiento operativo para la evolución del servicio.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La propuesta presentada por empresa_n no desarrolla este subproyecto de forma específica, limitándose a referencias genéricas al mantenimiento del entorno cloud. No se describen procedimientos concretos de distribución de carga ni planificación de capacidad, ni se identifican mecanismos de escalabilidad, ni estrategias de redistribución de almacenamiento o gestión de cuotas. **La falta de desarrollo resulta especialmente significativa considerando el volumen de usuarios indicado en el Documento de Invitación, ya que no se define cómo se abordaría este requisito en términos operativos.**

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CLO2 — Mantenimiento y adaptación del sistema de almacenamiento temporal de datos de la nube

###### Requisito y alcance

**Este subproyecto exige el mantenimiento del sistema de almacenamiento temporal, su interoperabilidad con el entorno cloud y su adaptación a necesidades de escalabilidad y carga.** Se trata de un componente crítico en el funcionamiento de la plataforma.

###### Análisis de la propuesta

Las propuestas de mejora reproducen el mismo enfoque, basándose en ajustes progresivos y supervisión, sin incorporar mecanismos técnicos adicionales que permitan evaluar la adaptación del sistema a escenarios de alta demanda.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n describe actuaciones como la revisión del sistema, la realización de ajustes básicos, la supervisión y la adaptación progresiva de recursos. **Sin embargo, no se definen mecanismos concretos de escalabilidad ni estrategias de distribución de carga, ni se desarrollan aspectos relacionados con la persistencia de datos o la alta disponibilidad.** Tampoco se identifican procedimientos para garantizar la interoperabilidad con el resto de los sistemas de la plataforma.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CLO3 — Mantenimiento del sistema de edición en línea de EducaMadrid

###### Requisito y alcance

El subproyecto CLO3 establece la necesidad de mantener y evolucionar el sistema de edición en línea, incluyendo la mejora de infraestructura, la integración con la nube y la capacidad de adaptación a múltiples usuarios.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar el mantenimiento y la adaptación básica a múltiples usuarios, sin incorporar elementos técnicos que permitan evaluar la evolución del sistema hacia un modelo escalable.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n describe tareas de mantenimiento, actualización y comprobación de accesos, así como la integración básica con el almacenamiento. **Sin embargo, no se desarrollan mecanismos específicos de escalabilidad, ni estrategias de gestión de sesiones concurrentes, ni procedimientos de optimización del rendimiento.** Tampoco se identifican actuaciones orientadas a la mejora arquitectónica del sistema.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque CLO

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 2 insuficientes y 1 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque OTR — Otros desarrollos

##### Consideración general del bloque

El bloque comprende SSO y 2FA, automatización, Elastic, flujos de trabajo, Portal CAU e inteligencia artificial, con especial atención a integraciones, seguridad, trazabilidad, herramientas y operativa real.

El contraste identifica 0 subproyectos con desarrollo suficiente, 7 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### OTR1 — Mantenimiento y mejora del sistema de autenticación centralizada Single Sign-On (SSO)

###### Requisito y alcance

El subproyecto OTR1 requiere la gestión del sistema de autenticación centralizada, incluyendo la integración SSO entre aplicaciones, la sincronización con LDAP, la implantación de alta disponibilidad y la incorporación de mecanismos de autenticación reforzada.

###### Análisis de la propuesta

Las propuestas de mejora se centran en reforzar aspectos ya descritos, como el balanceo o la autenticación adicional, sin aportar mecanismos específicos que permitan evaluar el funcionamiento real del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n identifica correctamente los elementos principales del sistema, mencionando tecnologías como Keycloak, LDAP, mecanismos de alta disponibilidad y autenticación multifactor. **No obstante, el análisis técnico pone de manifiesto la ausencia de desarrollo de mecanismos concretos de federación de identidades, gestión de sesiones, sincronización avanzada o arquitectura detallada de alta disponibilidad.**

###### Valoración cualitativa

**Valoración cualitativa: MEDIA**

El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR2 — Mantenimiento, configuración y gestión de 2FA en el servicio de Single Sign-On

###### Requisito y alcance

El subproyecto OTR2 se centra en la gestión de la autenticación multifactor, incluyendo la integración con sistemas existentes, la correlación con directorios LDAP y la configuración de métodos de verificación.

###### Análisis de la propuesta

Las propuestas de mejora mantienen este enfoque general, sin corregir la inconsistencia identificada ni desarrollar mecanismos concretos de integración y correlación de identidades.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n incluye referencias a OTP, TOTP, Google Authenticator y LDAP, lo que indica un conocimiento general del ámbito. Sin embargo, se detecta una **inconsistencia relevante** al hacer referencia a la sincronización con Directorio Activo, lo que no se corresponde con el entorno descrito en el Documento de Invitación, basado en LDAP/OpenLDAP.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR3 — Mantenimiento y mejora de herramientas de automatización de tareas

###### Requisito y alcance

Este subproyecto exige la gestión de herramientas de automatización en un entorno complejo, incluyendo la ejecución de tareas repetitivas, la integración entre sistemas y la optimización de procesos.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a ampliar las tareas automatizadas existentes, sin introducir herramientas ni metodologías específicas.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe la automatización de tareas mediante scripts y la revisión de procesos, sin identificar herramientas concretas ni desarrollar arquitecturas de automatización.** No se definen sistemas de orquestación ni mecanismos de gestión centralizada de automatizaciones.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR4 — Mantenimiento y mejora del sistema de gestión y análisis de datos mediante Elastic

###### Requisito y alcance

El subproyecto OTR4 requiere la gestión de sistemas de análisis de datos basados en el stack Elastic, incluyendo la ingestión, procesamiento y análisis de logs.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque general, sin aportar elementos técnicos que permitan evaluar la capacidad analítica del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n hace referencia a la gestión de logs y análisis de datos, pero no desarrolla los componentes específicos del stack Elastic, ni describe arquitecturas, ni procesos de ingestión o visualización de datos.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR5 — Mantenimiento y mejora de la herramienta de flujos de trabajo

###### Requisito y alcance

El subproyecto OTR5 establece la gestión de una herramienta de workflow, incluyendo la automatización de procesos y la gestión de flujos de trabajo.

###### Análisis de la propuesta

La propuesta de empresa_n describe tareas de mantenimiento y gestión de incidencias, sin identificar la herramienta concreta ni desarrollar los mecanismos de definición de flujos, automatización o integración con otros sistemas.

Las propuestas de mejora consisten en ampliar las tareas de mantenimiento sin introducir elementos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

El desarrollo es genérico o incompleto. La observación del anexo precisa: workflow sin herramienta identificada.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR6 — Mantenimiento y mejora del Portal CAU

###### Requisito y alcance

El subproyecto OTR6 requiere la gestión del portal de atención al usuario, incluyendo su evolución funcional, integración y mejora de usabilidad.

###### Análisis de la propuesta

La propuesta de empresa_n incluye tareas de mantenimiento y actualización, sin desarrollar aspectos relacionados con la arquitectura del sistema, la integración con herramientas de soporte ni la mejora funcional del portal.

Las propuestas de mejora se limitan a reforzar las tareas descritas, sin aportar mecanismos de evolución del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

El desarrollo es genérico o incompleto. La observación del anexo precisa: portal sin evolución funcional.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR7 — Mantenimiento y evolución de servicios de Inteligencia Artificial

###### Requisito y alcance

Este subproyecto requiere la evolución de servicios de inteligencia artificial dentro de la plataforma, incluyendo el entrenamiento, despliegue y gestión de modelos.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a extender este enfoque conceptual, sin introducir elementos técnicos que permitan evaluar su aplicabilidad.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n aborda este apartado de forma conceptual, sin desarrollar arquitecturas, herramientas ni procedimientos técnicos asociados a la gestión de modelos de IA.** No se identifican pipelines, entornos de entrenamiento ni sistemas de despliegue.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque OTR

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 7 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque COR — Correo electrónico

##### Consideración general del bloque

El bloque comprende control de envíos, listas, cuotas, spam, buzones, seguridad, infraestructura, escalado de Mailbox Server e inyección directa, incluyendo colas, spool, rendimiento, resiliencia y coexistencia.

El contraste identifica 0 subproyectos con desarrollo suficiente, 10 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### COR1 — Mantenimiento y mejora de los sistemas de control de envíos de correo

###### Requisito y alcance

**El subproyecto COR1 exige la implantación y evolución de mecanismos de control de envío de correo, incluyendo limitaciones según proveedores, control de flujos y regulación del tráfico saliente.** Se trata de un ámbito que requiere una definición clara de políticas de envío, gestión de colas y control de reputación.

###### Análisis de la propuesta

Las propuestas de mejora se basan en reforzar la supervisión y el ajuste de parámetros, sin introducir mecanismos técnicos adicionales que permitan evaluar el control efectivo del sistema.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n describe actividades como la supervisión del sistema, el análisis del comportamiento de los envíos y la realización de ajustes progresivos. **Sin embargo, no se desarrollan mecanismos concretos de control del tráfico, ni políticas diferenciadas por dominio o proveedor, ni estrategias de gestión de colas o limitación de envíos.**

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR2 — Mantenimiento automatizado de listas de distribución de EducaMadrid

###### Requisito y alcance

Este subproyecto requiere la automatización del mantenimiento de listas de distribución, incluyendo su actualización periódica, sincronización con sistemas corporativos y gestión de altas y bajas masivas.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque general, centrado en la revisión y actualización manual, sin incorporar mecanismos adicionales de automatización.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe tareas relacionadas con la gestión de listas y la incorporación de usuarios, pero no desarrolla mecanismos de automatización ni procesos de sincronización entre sistemas.** No se identifican procedimientos de actualización masiva ni herramientas específicas orientadas a la gestión automatizada.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR3 — Mantenimiento y mejora del sistema de activación y gestión de cuotas de correo

###### Requisito y alcance

El subproyecto COR3 implica la definición de políticas de cuotas por usuario y su gestión automatizada, incluyendo la activación de límites y el control del uso del sistema.

###### Análisis de la propuesta

Las propuestas de mejora reproducen este enfoque general, sin incorporar sistemas de control más avanzados.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n menciona la revisión del almacenamiento y la aplicación de ajustes generales, pero no define mecanismos de asignación de cuotas ni estrategias de gestión automatizada.** Tampoco se describe la integración con sistemas de gestión de usuarios ni el control del consumo en tiempo real.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR4 — Mantenimiento y mejora de las herramientas de control del spam

###### Requisito y alcance

El subproyecto COR4 exige la gestión avanzada de sistemas antispam, incluyendo la realización de campañas de phishing controladas y la mejora de los mecanismos de detección.

###### Análisis de la propuesta

Las propuestas de mejora se centran en ampliar la supervisión del sistema, sin introducir nuevos mecanismos técnicos de detección o prevención.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n se limita a describir la revisión de filtros y la supervisión del sistema de protección, sin desarrollar campañas de pruebas ni mecanismos específicos de análisis de amenazas.** No se identifican herramientas concretas ni estrategias de concienciación de usuarios.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR5 — Mantenimiento de buzones de correo

###### Requisito y alcance

Este subproyecto requiere la gestión masiva de buzones, incluyendo su creación, eliminación, redistribución y mantenimiento operativo.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque, sin introducir elementos adicionales que permitan gestionar el sistema en volumen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe actividades básicas de administración de buzones, sin desarrollar procesos automatizados ni estrategias de gestión a gran escala.** No se identifican mecanismos de balanceo ni de redistribución de carga entre servidores.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR6 — Mantenimiento y mejora de la seguridad del sistema de correo

###### Requisito y alcance

El subproyecto COR6 establece la necesidad de garantizar la seguridad del sistema de correo, incluyendo la gestión de certificados, cifrado y mecanismos de protección.

###### Análisis de la propuesta

Las propuestas de mejora no introducen elementos adicionales en este ámbito.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n menciona la revisión de certificados y ajustes generales, pero no desarrolla estrategias de seguridad ni procedimientos avanzados de protección.** No se definen mecanismos de cifrado, rotación de claves o control de accesos.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR7 — Actualización y mejora continua de la infraestructura de correo

###### Requisito y alcance

Este subproyecto exige la evolución de la infraestructura de correo, diferenciando componentes y mejorando su rendimiento y escalabilidad.

###### Análisis de la propuesta

Las propuestas de mejora mantienen este mismo enfoque generalista.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta presenta el sistema como un bloque único, sin diferenciar componentes ni desarrollar la arquitectura subyacente.** No se describen mecanismos de mejora de infraestructura ni estrategias de escalabilidad.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR8 — Ampliación del número de servidores Mailbox Server

###### Requisito y alcance

El subproyecto COR8 implica la ampliación de infraestructura en función de la carga, lo que requiere la definición de métricas y criterios de escalado.

###### Análisis de la propuesta

Las propuestas de mejora no aportan mecanismos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n no define umbrales ni criterios de ampliación, ni se identifican mecanismos de análisis de carga que permitan justificar la evolución de la infraestructura.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR9 — Implementación de un módulo receptor de inyección directa de correo

###### Requisito y alcance

Este subproyecto exige la implementación de un sistema de recepción de correo mediante inyección directa, incluyendo su integración con la infraestructura existente.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo nivel de generalidad.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe de forma genérica la recepción de mensajes, sin desarrollar el sistema completo ni su integración.** No se describen mecanismos de persistencia ni gestión de colas.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR10 — Mantenimiento y soporte del módulo de inyección directa de correo

###### Requisito y alcance

El subproyecto COR10 implica el mantenimiento del sistema de inyección directa, incluyendo soporte, monitorización y mejora del rendimiento.

###### Análisis de la propuesta

Las propuestas de mejora no introducen cambios relevantes.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta describe actividades básicas de soporte, sin desarrollar mecanismos de mejora ni sistemas de control del rendimiento.** No se identifican herramientas ni métricas específicas.

En la propuesta de empresa_n referente al bloque COR se detecta una **desviación relevante**, ya que al final del bloque se incluye con una imagen que representa una arquitectura de Active Directory en Cluster activo/pasivo. Esta arquitectura no corresponde con la que tiene EducaMadrid en producción actualmente, evidenciando desconocimiento de la plataforma real de EducaMadrid, y una falta de comprensión de los requisitos planteados en el Anexo II del Documento de Invitación, en donde se especifican las tecnologías usadas por EducaMadrid.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque COR

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 10 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque MAX — Sistema Operativo MAX

##### Consideración general del bloque

El bloque comprende soporte presencial y remoto, servidores de construcción y repositorios, mantenimiento de aplicaciones y distribuciones, integraciones, eventos, dispositivos y gestión centralizada de equipos y maquetas.

El contraste identifica 0 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 14 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### MAX1 — Mantenimiento y actualización de MAX de forma presencial en centros de forma regular

###### Requisito y alcance

El subproyecto MAX1 comprende mantenimiento y actualización de MAX de forma presencial en centros de forma regular, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX2 — Mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones

###### Requisito y alcance

El subproyecto MAX2 comprende mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX3 — Mantenimiento de aplicaciones basadas en MAX

###### Requisito y alcance

El subproyecto MAX3 comprende mantenimiento de aplicaciones basadas en MAX, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX4 — Lanzamiento anual de distribuciones de MAX «Full Equip»

###### Requisito y alcance

El subproyecto MAX4 comprende lanzamiento anual de distribuciones de MAX «Full Equip», con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX5 — Lanzamiento anual de distribuciones «MAX lite» y/o «MAX gestión»

###### Requisito y alcance

El subproyecto MAX5 comprende lanzamiento anual de distribuciones «MAX lite» y/o «MAX gestión», con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX6 — Integración de aplicaciones externas en los repositorios oficiales

###### Requisito y alcance

El subproyecto MAX6 comprende integración de aplicaciones externas en los repositorios oficiales, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX7 — Mantenimiento y mejora del servidor de gestión de accesos remotos

###### Requisito y alcance

El subproyecto MAX7 comprende mantenimiento y mejora del servidor de gestión de accesos remotos, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX8 — Soporte de asistencia telefónica y remota para incidencias de entornos MAX

###### Requisito y alcance

El subproyecto MAX8 comprende soporte de asistencia telefónica y remota para incidencias de entornos MAX, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX9 — Asistencia presencial en los diferentes eventos MAX

###### Requisito y alcance

El subproyecto MAX9 comprende asistencia presencial en los diferentes eventos MAX, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX10 — Soporte presencial en eventos especiales MAX Install Party

###### Requisito y alcance

El subproyecto MAX10 comprende soporte presencial en eventos especiales MAX Install Party, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX11 — Gestión, mantenimiento y actualización de equipos MAX en remoto

###### Requisito y alcance

El subproyecto MAX11 comprende gestión, mantenimiento y actualización de equipos MAX en remoto, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX12 — Instalación y configuración de dispositivos solicitados por los centros educativos

###### Requisito y alcance

El subproyecto MAX12 comprende instalación y configuración de dispositivos solicitados por los centros educativos, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX13 — Mantenimiento y soporte del servidor de repositorio individual para centros educativos

###### Requisito y alcance

El subproyecto MAX13 comprende mantenimiento y soporte del servidor de repositorio individual para centros educativos, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MAX14 — Herramienta de gestión centralizada de maquetas de MAX

###### Requisito y alcance

El subproyecto MAX14 comprende herramienta de gestión centralizada de maquetas de MAX, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata MAX1 a MAX14 de forma agregada, por lo que la valoración de este subproyecto se integra en la conclusión conjunta del bloque y en su clasificación individual del anexo.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque MAX

La valoración conjunta del bloque es **MUY BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 0 insuficientes y 14 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque AV — Aulas Virtuales

##### Consideración general del bloque

El bloque comprende actualización y estabilidad de bases de datos y FrontEnd, despliegue de nuevos grupos, redistribución de NFS, automatización, balanceo y adaptación a picos de carga.

El contraste identifica 0 subproyectos con desarrollo suficiente, 4 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### AV1 — Actualización y comprobación periódicas de servidores de bases de datos de aulas virtuales

###### Requisito y alcance

El subproyecto AV1 requiere la actualización y comprobación de servidores físicos y virtuales que soportan las bases de datos de aulas virtuales, lo que implica tareas de revisión técnica, control de estado y validación de funcionamiento en entornos de alta carga.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar las tareas de revisión y seguimiento sin introducir mecanismos técnicos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n plantea actividades de revisión periódica, comprobación de estado y mantenimiento general, manteniéndose en un nivel descriptivo.** No se identifican procedimientos específicos de validación, ni herramientas de diagnóstico, ni mecanismos de análisis del rendimiento asociados a los servidores de bases de datos. Tampoco se desarrollan estrategias para garantizar la estabilidad en escenarios de alta concurrencia.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### AV2 — Mantenimiento de los servidores FrontEnd de aulas virtuales

###### Requisito y alcance

Este subproyecto exige el mantenimiento de los servidores de front-end, incluyendo la gestión de accesos, la disponibilidad del servicio y la optimización del rendimiento.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque, centrado en la supervisión sin aportar elementos técnicos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta describe tareas generales de mantenimiento y supervisión, sin desarrollar arquitecturas de despliegue ni mecanismos de balanceo o escalabilidad.** No se identifican herramientas de gestión de tráfico ni estrategias para la distribución de carga entre servidores.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### AV3 — Despliegue de nuevos grupos de aulas virtuales

###### Requisito y alcance

El subproyecto AV3 requiere el despliegue periódico de nuevos entornos de aulas virtuales, incluyendo la ampliación de infraestructuras existentes.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar la ampliación de entornos sin definir los mecanismos técnicos asociados.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n menciona la creación de nuevos entornos y la ampliación de los existentes, pero no desarrolla procedimientos de despliegue, ni automatización, ni estrategias de escalado.** No se describen dependencias ni secuencias de despliegue.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### AV4 — Redistribución periódica de NFS de aulas virtuales

###### Requisito y alcance

Este subproyecto establece la redistribución periódica de almacenamiento NFS en el entorno de aulas virtuales.

###### Análisis de la propuesta

Las propuestas de mejora no aportan elementos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta describe la reorganización del almacenamiento y la revisión de ocupación, sin definir criterios de redistribución ni herramientas de análisis.** No se identifican métricas ni procedimientos de migración de datos.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque AV

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 4 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque POR — Servicio de LDAP y Portal Educativo

##### Consideración general del bloque

El bloque comprende escalado de esclavos LDAP, replicación, disponibilidad y rendimiento, así como planificación, reversibilidad, integridad y validación de la migración del LDAP máster.

El contraste identifica 0 subproyectos con desarrollo suficiente, 2 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### POR1 — Ampliación periódica del sistema de esclavos LDAP de EducaMadrid

###### Requisito y alcance

**El subproyecto POR1 establece la ampliación del sistema LDAP mediante la incorporación de nuevos nodos esclavos, lo que implica la gestión de replicación del directorio, la sincronización continua de datos y la garantía de consistencia entre nodos en un entorno distribuido.** Se trata de una operación que requiere definir claramente la arquitectura LDAP, los mecanismos de replicación y los procedimientos de validación de integridad del sistema.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar la ampliación y supervisión del sistema, sin introducir elementos técnicos adicionales que permitan evaluar la gestión efectiva del entorno LDAP distribuido.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta presentada por empresa_n plantea la ampliación del sistema mediante la incorporación de nuevos servidores y la revisión general de su estado, sin desarrollar los mecanismos técnicos asociados a la replicación ni a la sincronización de datos.** No se describen configuraciones específicas, ni procedimientos de control de divergencias, ni mecanismos de validación del estado del directorio entre nodos.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### POR2 — Migración del sistema LDAP máster de EducaMadrid

###### Requisito y alcance

El subproyecto POR2 implica la migración del nodo maestro LDAP, operación crítica que requiere planificación, ejecución controlada y validación de integridad del sistema, así como la minimización del impacto sobre los servicios dependientes.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque, reforzando la revisión del proceso sin incorporar metodologías adicionales que permitan garantizar la correcta ejecución de la migración en un entorno crítico.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n aborda la migración mediante una descripción general del proceso, haciendo referencia a su ejecución y comprobación posterior, sin definir fases concretas ni procedimientos técnicos asociados.** No se describen mecanismos de traslado de datos, validación de consistencia ni herramientas de soporte a la migración.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque POR

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 2 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque SEG — Seguridad

##### Consideración general del bloque

El bloque comprende control de cambios y dominios DNS, segregación de identidades privilegiadas, certificados, vulnerabilidades, detección de intrusiones, auditoría continua, centralización de logs, claves RSA y respuesta ante incidentes.

El contraste identifica 0 subproyectos con desarrollo suficiente, 11 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### SEG1 — Mantenimiento y mejora del sistema de control de cambios en DNS

###### Requisito y alcance

El subproyecto SEG1 exige la implantación de mecanismos de control de cambios en DNS que permitan auditar modificaciones, mantener trazabilidad y garantizar la estabilidad de la configuración en el tiempo.

###### Análisis de la propuesta

Las propuestas de mejora se centran en reforzar la supervisión del sistema sin incorporar mecanismos adicionales que permitan garantizar la trazabilidad de los cambios.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe la revisión y control general del sistema DNS sin desarrollar procedimientos específicos de control de cambios ni definir herramientas de auditoría o versionado.** No se identifican flujos de validación ni mecanismos de aprobación de modificaciones.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG2 — LDAP Máster independiente para usuarios privilegiados

###### Requisito y alcance

Este subproyecto establece la necesidad de separar los usuarios privilegiados en un entorno LDAP independiente, con el objetivo de reforzar la seguridad y el control de accesos.

###### Análisis de la propuesta

Las propuestas de mejora mantienen este enfoque general sin aportar elementos técnicos que permitan evaluar la implantación efectiva de un entorno segregado.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta presentada describe de forma general la gestión del sistema sin desarrollar una arquitectura diferenciada ni mecanismos específicos de control de accesos.** No se identifican políticas de segregación ni procedimientos de gestión de privilegios.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG3 — Gestión, mantenimiento e implantación de certificados

###### Requisito y alcance

El subproyecto SEG3 requiere la gestión completa del ciclo de vida de certificados, incluyendo su generación, distribución, renovación y revocación.

###### Análisis de la propuesta

Las propuestas de mejora se centran en reforzar la revisión del sistema, sin introducir nuevos elementos técnicos.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n se limita a mencionar la gestión y revisión de certificados sin desarrollar procedimientos específicos asociados a su ciclo de vida.** No se describen mecanismos de automatización ni herramientas de gestión centralizada.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG4 — Gestión y mantenimiento de dominios DNS

###### Requisito y alcance

Este subproyecto implica la administración de dominios DNS, incluyendo su mantenimiento, actualización y control de consistencia.

###### Análisis de la propuesta

Las propuestas de mejora reproducen el mismo planteamiento sin aportar elementos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta describe tareas generales de gestión de dominios sin definir procedimientos específicos ni herramientas asociadas. **No se desarrollan mecanismos de automatización ni control de errores.**

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG5 — Análisis y corrección de vulnerabilidades

###### Requisito y alcance

El subproyecto SEG5 exige la identificación y mitigación de vulnerabilidades mediante el uso de herramientas y metodologías específicas.

###### Análisis de la propuesta

Las propuestas de mejora mantienen este enfoque general sin introducir mecanismos técnicos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta plantea la revisión de sistemas y la corrección de vulnerabilidades sin identificar herramientas ni procesos de análisis. **No se definen metodologías de evaluación ni clasificación de riesgos.**

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG6 — Detección de intrusiones y análisis de logs

###### Requisito y alcance

Este subproyecto requiere la implantación de mecanismos de detección de intrusiones basados en el análisis de logs y la correlación de eventos.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar el seguimiento, sin aportar elementos técnicos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta describe la revisión de logs sin definir sistemas SIEM ni arquitecturas de detección avanzada.** No se contemplan procesos de correlación ni respuestas automatizadas.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG7 — Auditorías internas de aplicaciones

###### Requisito y alcance

El subproyecto SEG7 exige la realización de auditorías de seguridad en aplicaciones siguiendo metodologías estructuradas.

###### Análisis de la propuesta

Las propuestas de mejora mantienen este mismo nivel de generalidad.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta menciona la ejecución de auditorías sin definir metodologías ni estándares de referencia.** No se identifican herramientas ni procesos de evaluación detallados.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG8 — Auditorías internas continuas de sistemas

###### Requisito y alcance

Este subproyecto amplía el anterior al conjunto de sistemas, requiriendo un enfoque continuo de auditoría.

###### Análisis de la propuesta

Las propuestas de mejora reproducen el mismo patrón.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta describe revisiones periódicas sin desarrollar mecanismos de monitorización continua ni procesos estructurados.** No se identifican herramientas ni métricas de control.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG9 — Mantenimiento y uso de logs centralizados

###### Requisito y alcance

El subproyecto SEG9 exige la centralización de logs para su análisis y gestión.

###### Análisis de la propuesta

El análisis específico se integra en las fortalezas y carencias que siguen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta menciona la recopilación de logs sin definir arquitectura, almacenamiento ni explotación de información.** No se desarrollan procesos de análisis ni correlación de eventos.

Las propuestas de mejora no incorporan elementos adicionales.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG10 — Implementación y mantenimiento de claves RSA unificadas

###### Requisito y alcance

Este subproyecto implica la gestión de claves criptográficas, incluyendo su creación, distribución y renovación.

###### Análisis de la propuesta

Las propuestas de mejora no aportan contenido adicional.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta se limita a mencionar la gestión de claves sin describir procedimientos técnicos ni herramientas específicas.** No se identifican mecanismos de control ni protección del ciclo de vida.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG11 — Asistencia en eventos de ciberseguridad

###### Requisito y alcance

Este subproyecto contempla la participación en eventos y el soporte técnico asociado.

###### Análisis de la propuesta

Las propuestas de mejora mantienen este enfoque descriptivo.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta describe la asistencia de forma general sin desarrollar la prestación técnica ni definir tareas concretas.** No se identifican procedimientos asociados al soporte.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque SEG

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 11 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque CON — Automatización y contenedores

##### Consideración general del bloque

El bloque comprende orquestación, ciclo de vida de contenedores, infraestructura como código, scripts, herramientas auxiliares, control de versiones, pruebas y observabilidad.

El contraste identifica 0 subproyectos con desarrollo suficiente, 3 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### CON1 — Mantenimiento y mejora del sistema de gestión de contenedores

###### Requisito y alcance

El subproyecto CON1 requiere la gestión de plataformas de contenedores, incluyendo su mantenimiento, actualización y evolución mediante herramientas específicas.

###### Análisis de la propuesta

Las propuestas de mejora se limitan a reforzar las tareas descritas, sin introducir elementos técnicos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe la actualización de sistemas y el uso de scripts generales sin identificar tecnologías concretas ni arquitecturas de contenedores.** No se desarrollan mecanismos de orquestación ni despliegue.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CON2 — Mantenimiento y mejora de scripts y automatización de tareas

###### Requisito y alcance

Este subproyecto exige la automatización de tareas mediante scripts en un entorno complejo.

###### Análisis de la propuesta

Las propuestas de mejora mantienen el mismo enfoque general.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta menciona la automatización sin identificar herramientas ni arquitecturas de gestión centralizada.** No se describen procesos ni control de ejecución.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CON3 — Mantenimiento del sistema auxiliar de automatización

###### Requisito y alcance

El subproyecto requiere la gestión de sistemas auxiliares de automatización de procesos.

###### Análisis de la propuesta

Las propuestas de mejora no aportan elementos adicionales.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta describe el mantenimiento de sistemas sin desarrollar componentes ni procedimientos técnicos.** No se identifican herramientas ni mecanismos de integración.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque CON

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 3 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque MIG — Gestión de la migración de servidores entre CPDs

##### Consideración general del bloque

El bloque comprende coordinación, inventario, dependencias, fases preparatorias, documentación, criterios de aceptación, pruebas, reversibilidad, verificación y soporte posterior a la migración.

El contraste identifica 0 subproyectos con desarrollo suficiente, 5 con desarrollo insuficiente y 0 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### MIG1 — Coordinación y planificación de la revisión de los entornos migrados

###### Requisito y alcance

**El subproyecto MIG1 establece la necesidad de coordinar y planificar la revisión de los entornos tras los procesos de migración, lo que implica la verificación del estado de los sistemas, la comprobación de los servicios afectados y la coordinación entre los distintos equipos técnicos implicados.** Este tipo de tareas requiere una metodología estructurada que permita validar la correcta transición de los sistemas entre entornos.

###### Análisis de la propuesta

El análisis específico se integra en las fortalezas y carencias que siguen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n aborda este subproyecto mediante referencias generales a la coordinación de equipos y a la revisión de los entornos migrados, sin definir un marco metodológico concreto. No se describen procedimientos de validación, ni criterios de aceptación, ni mecanismos de comprobación de dependencias entre sistemas. **Las propuestas de mejora se limitan a reforzar la revisión posterior a la migración sin incorporar herramientas, fases ni controles adicionales que permitan evaluar la ejecución del proceso de forma estructurada.**

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MIG2 — Fases preparatorias y planificación técnica de la migración

###### Requisito y alcance

Este subproyecto exige la definición de las fases previas a la migración, incluyendo la planificación técnica, el análisis de dependencias y la preparación de los sistemas, lo que requiere una estructuración clara del proceso.

###### Análisis de la propuesta

El análisis específico se integra en las fortalezas y carencias que siguen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n menciona la planificación de las migraciones de forma general, sin definir fases ni cronogramas, ni establecer una secuencia de actuaciones.** No se identifican análisis de dependencias ni mecanismos de coordinación entre sistemas. Las propuestas de mejora reproducen este mismo enfoque, sin aportar elementos adicionales que permitan estructurar el proceso de migración en fases claramente definidas.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MIG3 — Preparación de servidores y documentación de sistemas

###### Requisito y alcance

El subproyecto MIG3 implica la preparación de los servidores antes de la migración, incluyendo la revisión de configuraciones, la estandarización de sistemas y la generación de documentación técnica.

###### Análisis de la propuesta

El análisis específico se integra en las fortalezas y carencias que siguen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

**La propuesta de empresa_n describe la preparación de servidores y la elaboración de documentación de forma genérica, sin desarrollar procedimientos concretos ni herramientas de automatización.** No se definen plantillas, criterios de validación ni mecanismos de estandarización. Las propuestas de mejora se centran en reforzar estas tareas sin incorporar mecanismos adicionales que permitan evaluar la preparación de sistemas en un entorno complejo.

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MIG4 — Verificación de la migración

###### Requisito y alcance

Este subproyecto requiere la validación del proceso de migración mediante la comprobación de la integridad de los sistemas, la disponibilidad de los servicios y la correcta transferencia de los datos.

###### Análisis de la propuesta

El análisis específico se integra en las fortalezas y carencias que siguen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n menciona la verificación del proceso tras la migración, sin definir procedimientos específicos ni criterios de validación. No se describen mecanismos de comprobación de integridad ni herramientas de validación de servicios. **Las propuestas de mejora refuerzan la revisión posterior sin incorporar metodologías adicionales que permitan verificar el resultado de la migración de forma objetiva.**

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MIG5 — Mantenimiento y soporte tras la migración

###### Requisito y alcance

El subproyecto MIG5 establece la necesidad de proporcionar soporte posterior a la migración, incluyendo la resolución de incidencias y la estabilización del sistema.

###### Análisis de la propuesta

El análisis específico se integra en las fortalezas y carencias que siguen.

###### Fortalezas y valor añadido

Se reconoce cobertura formal del subproyecto y una propuesta de mejora, pero no se acredita una capacidad diferencial verificable.

###### Carencias, omisiones, errores o riesgos

La propuesta de empresa_n describe el soporte de forma general, haciendo referencia a la resolución de incidencias y seguimiento del sistema, sin definir mecanismos de monitorización ni procedimientos de estabilización. No se identifican métricas ni indicadores de estado. **Las propuestas de mejora se limitan a reforzar el seguimiento sin aportar elementos adicionales que permitan evaluar la fase post-migración.**

###### Valoración cualitativa

**Valoración cualitativa: BAJA**

El nivel **BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque MIG

La valoración conjunta del bloque es **BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 5 insuficientes y 0 no incluidos, con 0 aportaciones de valor añadido.

#### Bloque IA — Inteligencia Artificial

##### Consideración general del bloque

El bloque comprende evaluación de modelos, ingeniería de prompts, guardarraíles, integración en aplicaciones, capacidad, límites por usuario, métricas, seguridad, trazabilidad y operación de los servicios de IA.

El contraste identifica 0 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 5 no incluidos; 0 incorporan valor añadido según la clasificación del anexo.

##### IA1 — Evaluación del rendimiento de los modelos seleccionados

###### Requisito y alcance

El subproyecto IA1 comprende evaluación del rendimiento de los modelos seleccionados, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata IA1 a IA5 de forma agregada y no aporta para este subproyecto una solución técnica diferenciada, herramientas, procedimientos ni mecanismos de validación evaluables.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA2 — Ingeniería de prompts adaptados para cada servicio

###### Requisito y alcance

El subproyecto IA2 comprende ingeniería de prompts adaptados para cada servicio, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata IA1 a IA5 de forma agregada y no aporta para este subproyecto una solución técnica diferenciada, herramientas, procedimientos ni mecanismos de validación evaluables.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA3 — Testeo de los guardarraíles para el entorno educativo

###### Requisito y alcance

El subproyecto IA3 comprende testeo de los guardarraíles para el entorno educativo, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata IA1 a IA5 de forma agregada y no aporta para este subproyecto una solución técnica diferenciada, herramientas, procedimientos ni mecanismos de validación evaluables.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA4 — Evaluación de posibilidades de integración en distintos aplicativos

###### Requisito y alcance

El subproyecto IA4 comprende evaluación de posibilidades de integración en distintos aplicativos, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata IA1 a IA5 de forma agregada y no aporta para este subproyecto una solución técnica diferenciada, herramientas, procedimientos ni mecanismos de validación evaluables.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA5 — Evaluación de capacidades de respuesta y límites por usuario

###### Requisito y alcance

El subproyecto IA5 comprende evaluación de capacidades de respuesta y límites por usuario, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

###### Análisis de la propuesta

La memoria trata IA1 a IA5 de forma agregada y no aporta para este subproyecto una solución técnica diferenciada, herramientas, procedimientos ni mecanismos de validación evaluables.

###### Fortalezas y valor añadido

No se acreditan fortalezas técnicas ni mejoras evaluables para este subproyecto.

###### Carencias, omisiones, errores o riesgos

La ausencia de una solución concreta impide valorar arquitectura, procedimientos, herramientas, rendimiento y viabilidad del subproyecto.

###### Valoración cualitativa

**Valoración cualitativa: MUY BAJA**

El nivel **MUY BAJA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque IA

La valoración conjunta del bloque es **MUY BAJA**. La clasificación individual muestra 0 desarrollos suficientes, 0 insuficientes y 5 no incluidos, con 0 aportaciones de valor añadido.

### Conclusión del análisis detallado

El patrón dominante es el desarrollo insuficiente: 66 de los 89 subproyectos se clasifican como insuficientes y 21 no incluyen solución concreta. MAX e IA carecen de desarrollo técnico evaluable, mientras las carencias de BD, MON, CLO, COR, CON y MIG son recurrentes. Solo UPD5 y UPD8 alcanzan desarrollo suficiente y el valor añadido real es residual. La propuesta presenta una cobertura formal amplia y una identificación correcta del entorno de EducaMadrid, pero su desarrollo es mayoritariamente descriptivo. Faltan arquitecturas específicas, procedimientos operativos, herramientas, métricas, criterios de aceptación y mecanismos de validación. La referencia a Métrica V3 y algunos contenidos evaluables en GitLab y Redmine aportan valor parcial, sin compensar la baja concreción ni la ausencia de solución en bloques completos.

## EVALUACIÓN DE LA SOLUCIÓN TÉCNICA OFERTADA

### Fundamentación de la valoración

La valoración se basa en el análisis pormenorizado anterior y atiende a la calidad, concreción, coherencia, adecuación, viabilidad y verificabilidad del contenido, no a su mera presencia formal.

### Arquitectura planteada en los distintos subproyectos — máximo 2,00 puntos

La propuesta presentada por empresa_n incluye una descripción amplia del ecosistema tecnológico de EducaMadrid, en la que se identifican los principales sistemas, su carácter distribuido y la interrelación entre los diferentes componentes que configuran la plataforma. **Este aspecto evidencia una adecuada comprensión del entorno tecnológico en el que se desarrollará el servicio, así como de su complejidad y criticidad.**

**Sin embargo, desde el punto de vista de los criterios establecidos en el Documento de Invitación, la evaluación de la arquitectura no se limita a la correcta identificación del entorno existente, sino que exige la definición de una arquitectura propia, específica y técnicamente desarrollada que permita verificar cómo se implementará la solución propuesta.** En este sentido, el análisis detallado permite constatar que la propuesta no incorpora una arquitectura técnica definida, sino que se limita en gran medida a describir el estado actual del sistema o a reproducir elementos ya existentes en el entorno.

**Se observa, en particular, la ausencia de diagramas arquitectónicos desarrollados por el licitador que representen la solución propuesta, la falta de definición de relaciones entre componentes y la inexistencia de modelos concretos de distribución de servicios, escalabilidad o alta disponibilidad.** Asimismo, no se identifican arquitecturas específicas por subproyecto ni se definen mecanismos técnicos asociados a elementos críticos como balanceo de carga, replicación, segmentación funcional o resiliencia del sistema.

**Estas carencias adquieren una especial relevancia en bloques tecnológicos que, por su naturaleza, requieren un desarrollo arquitectónico detallado, como son los ámbitos de bases de datos, cloud, inteligencia artificial o el sistema operativo MAX.** En estos casos, la propuesta se mantiene en un plano conceptual o descriptivo, sin aportar diseño técnico alguno que permita evaluar su aplicabilidad real.

**Adicionalmente, se han detectado algunos elementos que no se ajustan adecuadamente al entorno tecnológico de EducaMadrid, como la inclusión de arquitecturas no alineadas con el modelo real del sistema o la reutilización de esquemas no adaptados al contexto específico del contrato.** Este tipo de inconsistencias reduce la credibilidad de la propuesta y añade incertidumbre respecto a su adecuación técnica.

**Como consecuencia de todo lo anterior, no resulta posible evaluar adecuadamente aspectos esenciales exigidos por el Documento de Invitación, tales como la capacidad de escalado del sistema, su comportamiento ante situaciones de alta carga, la distribución eficiente de los servicios o la resiliencia frente a fallos.** En consecuencia, la arquitectura presentada debe considerarse identificada a nivel conceptual, pero no definida ni desarrollada a nivel técnico, lo que limita de forma significativa su verificabilidad.

De acuerdo con la escala de valoración establecida en el Documento de Invitación, esta situación se corresponde con un nivel de evaluación medio, en tanto existe una comprensión general del entorno, pero no una propuesta arquitectónica definida y verificable.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,90 sobre 2,00

### Grado de comprensión de los requisitos planteados — máximo 2,00 puntos

**La memoria técnica presentada por empresa_n incluye un desarrollo extenso de la comprensión de los requisitos del Documento de Invitación, en el que se identifican adecuadamente el objeto del contrato, su carácter evolutivo y correctivo, la criticidad del entorno y la necesidad de garantizar la continuidad del servicio junto con elevados niveles de disponibilidad, rendimiento y seguridad.** Esta exposición evidencia un esfuerzo significativo por parte del licitador en la interpretación global del alcance del contrato.

**Asimismo, se reconoce de forma adecuada la estructura del Documento de Invitación por bloques funcionales y se identifican los distintos ámbitos tecnológicos implicados, lo que permite afirmar que la comprensión conceptual del servicio es correcta desde un punto de vista teórico.** No obstante, el análisis conjunto de la memoria técnica y del desarrollo por subproyectos realizado en el capítulo 2 pone de manifiesto una diferencia significativa entre dicha comprensión declarada y su traducción efectiva en soluciones técnicas concretas.

**En particular, se observa que la identificación de requisitos no se acompaña de una definición de procedimientos específicos que permitan su cumplimiento, ni de la selección de herramientas técnicas que soporten su ejecución.** Del mismo modo, en numerosos subproyectos no se desarrollan mecanismos operativos que permitan materializar las necesidades identificadas, lo que evidencia una limitación en la capacidad de trasladar la comprensión conceptual a una solución técnica efectiva.

**Esta situación resulta especialmente visible en ámbitos como la monitorización, donde se identifica la necesidad de disponer de sistemas avanzados pero no se definen métricas ni herramientas; en el ámbito de bases de datos, donde se reconoce la importancia de la optimización sin desarrollar metodologías concretas; o en el caso de las migraciones, donde no se establecen fases ni procedimientos detallados.** Asimismo, en bloques completos como inteligencia artificial o sistema MAX, la comprensión teórica no se traduce en ningún contenido técnico evaluable.

**A estas limitaciones se añaden determinadas inconsistencias técnicas detectadas en la propuesta, tales como la inclusión de referencias a tecnologías no alineadas con el entorno del Documento de Invitación o la reutilización de contenidos no adaptados a los subproyectos correspondientes.** Estas circunstancian afectan de forma directa a la valoración de la comprensión real del servicio, al evidenciar una falta de ajuste en determinados aspectos técnicos.

**En consecuencia, si bien la comprensión del Documento de Invitación puede considerarse adecuada en términos conceptuales, su aplicación práctica resulta limitada, lo que condiciona su valoración global.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel medio, dado que la comprensión es correcta pero no se materializa de forma suficiente en la solución técnica.

**Nivel cualitativo:** MEDIA
**Puntuación:** 1,00 sobre 2,00

### Viabilidad técnica y operativa del proyecto — máximo 1,00 puntos

**La propuesta presentada por empresa_n plantea una viabilidad general coherente desde un punto de vista estructural, en la medida en que se articula en torno a los distintos bloques funcionales definidos en el Documento de Invitación y recoge, al menos a nivel descriptivo, las principales líneas de actuación requeridas para la prestación del servicio.** Esta aproximación permite identificar una cierta lógica interna en la organización del documento, así como una alineación formal con el alcance del contrato.

**No obstante, el análisis técnico detallado evidencia que la viabilidad real del proyecto se encuentra condicionada por la falta de desarrollo de los elementos necesarios para su ejecución efectiva.** En particular, se constata que la propuesta no define procedimientos operativos concretos que permitan determinar cómo se llevarán a cabo las actuaciones descritas, ni identifica herramientas específicas que sirvan de base tecnológica para la prestación del servicio. Asimismo, no se desarrollan arquitecturas que permitan comprender cómo se integran los distintos componentes del sistema ni cómo se gestionarán aspectos críticos como la disponibilidad, la escalabilidad o la distribución de cargas.

**Estas carencias se refuerzan al analizar determinados bloques en los que la propuesta no presenta contenido técnico evaluable, como ocurre en el caso del sistema operativo MAX o en el ámbito de inteligencia artificial, donde se limita a reproducir los requisitos del Documento de Invitación sin aportar soluciones.** Esta ausencia de desarrollo técnico en ámbitos completos introduce una incertidumbre relevante respecto a la capacidad global de ejecución del servicio.

**Adicionalmente, la presencia de determinadas inconsistencias técnicas, derivadas de la reutilización de contenidos no adaptados o de la inclusión de referencias tecnológicas incorrectas, reduce la confianza en la adecuación real de la propuesta al entorno específico de EducaMadrid.** Estas circunstancias, en conjunto, impiden evaluar con precisión la capacidad operativa del licitador, así como la viabilidad efectiva de la solución planteada.

**En consecuencia, si bien la propuesta presenta coherencia desde un punto de vista formal, la falta de concreción técnica y de elementos verificables limita de forma significativa su viabilidad real.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel de valoración medio, al existir una cobertura general del alcance pero sin acreditación suficiente de la capacidad de ejecución.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,40 sobre 1,00

### Metodología de trabajo aplicada — máximo 1,00 puntos

La propuesta de empresa_n incorpora como marco metodológico la metodología Métrica V3, junto con referencias a estándares reconocidos en el ámbito de la gestión de servicios y del desarrollo de sistemas de información. **Este planteamiento constituye un elemento positivo en la medida en que se apoya en metodologías consolidadas y ampliamente utilizadas en el sector.**

**Sin embargo, el análisis detallado pone de manifiesto que la utilización de estos marcos metodológicos se realiza a un nivel fundamentalmente teórico, reproduciendo en gran medida la estructura de los estándares sin adaptarlos de manera específica al objeto del contrato ni a las particularidades del entorno EducaMadrid.** En este sentido, no se identifican procedimientos concretos de aplicación de la metodología en los distintos subproyectos, ni se definen mecanismos de control, seguimiento o validación asociados a su implantación.

Asimismo, la propuesta no establece una integración clara entre la metodología descrita y la operativa real del servicio, especialmente en ámbitos como la gestión de incidencias, la ejecución de tareas recurrentes o la gestión de cambios. **Tampoco se identifican herramientas que soporten la aplicación efectiva de la metodología, lo que limita su capacidad para ser utilizada como un instrumento operativo dentro del servicio.**

Esta falta de adaptación al contexto específico del contrato implica que la metodología se presenta como un marco conceptual de referencia, pero no como un modelo de trabajo directamente aplicable. **Como consecuencia, su impacto en la calidad y en la ejecución del servicio resulta limitado desde el punto de vista de los criterios del Documento de Invitación.**

De acuerdo con la escala establecida en el Documento de Invitación, esta situación se corresponde con un nivel de valoración medio, al existir una referencia a metodologías reconocidas pero sin un desarrollo operativo concreto que permita su aplicación efectiva.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,50 sobre 1,00

### Rendimiento previsible de las soluciones — máximo 1,00 puntos

La propuesta de empresa_n incluye diversas referencias al rendimiento esperado de la solución, indicando que este se basará en un enfoque de monitorización continua, mantenimiento proactivo y optimización progresiva del sistema. **Estas afirmaciones reflejan una intención de garantizar un adecuado comportamiento de la plataforma desde el punto de vista operativo.**

**No obstante, el análisis técnico evidencia que dichas afirmaciones no se sustentan en elementos verificables que permitan evaluar de forma objetiva el rendimiento propuesto.** En particular, no se definen indicadores de rendimiento que permitan medir la calidad del servicio, tales como tiempos de respuesta, latencias, niveles de disponibilidad o capacidad de procesamiento. Tampoco se establecen umbrales de funcionamiento ni objetivos cuantificables que permitan determinar cuándo el sistema cumple o no con los requisitos de rendimiento establecidos.

Del mismo modo, no se identifican herramientas específicas de monitorización ni sistemas de medición que permitan obtener datos operativos sobre el comportamiento de la plataforma. **La propuesta se limita a mencionar de forma genérica la existencia de mecanismos de supervisión, sin detallar su naturaleza ni su funcionamiento.** Asimismo, no se describen escenarios de prueba que permitan evaluar el comportamiento del sistema ante situaciones de carga elevada o ante condiciones de estrés.

**Estas carencias son especialmente relevantes en un entorno como el de EducaMadrid, caracterizado por un elevado número de usuarios y por la necesidad de garantizar un funcionamiento continuo y estable.** La ausencia de un modelo de evaluación del rendimiento impide verificar la adecuación de la solución propuesta a estos requisitos.

**En consecuencia, el rendimiento planteado presenta un carácter declarativo, basado en afirmaciones generales que no pueden ser contrastadas mediante elementos técnicos objetivos.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel de valoración bajo, al no existir evidencia suficiente que permita evaluar el rendimiento de la solución.

**Nivel cualitativo:** BAJA
**Puntuación:** 0,25 sobre 1,00

### Satisfacción de los requisitos del Anexo II — máximo 8,00 puntos

**El subcriterio de satisfacción de los requisitos constituye el elemento de mayor ponderación dentro de la evaluación de la solución técnica, por lo que su análisis resulta determinante para la valoración global de la propuesta.** Este criterio no se limita a verificar la cobertura formal de los subproyectos incluidos en el Anexo II, sino que exige evaluar el grado en que la solución presentada permite satisfacer de manera efectiva los requisitos técnicos planteados, incluyendo la existencia de procedimientos, herramientas, metodologías y capacidades operativas que garanticen su ejecución.

A efectos de la presente evaluación, se entiende por solución técnica adecuada aquella que incorpore elementos verificables, tales como procedimientos definidos, herramientas identificadas y mecanismos de ejecución contrastables, de conformidad con el criterio de verificabilidad implícito en el apartado 7.2.2 del Documento de Invitación.

El análisis realizado en el capítulo 2 permite concluir que la propuesta de empresa_n presenta una cobertura formal amplia de los subproyectos, en el sentido de que identifica los distintos ámbitos funcionales del servicio y desarrolla descripciones asociadas a cada uno de ellos. **No obstante, esta cobertura formal no se traduce en una satisfacción técnica efectiva de los requisitos, ya que en la mayoría de los casos las propuestas se limitan a describir actividades genéricas de mantenimiento, supervisión o revisión, sin aportar desarrollo técnico suficiente.**

De forma generalizada, las soluciones planteadas no incorporan procedimientos operativos concretos, ni identifican herramientas específicas que permitan su ejecución. **Tampoco se desarrollan arquitecturas, metodologías o mecanismos de automatización que aporten valor añadido al cumplimiento de los requisitos.** Esta situación impide considerar que la propuesta satisface los requisitos desde un punto de vista técnico, al no demostrar cómo se llevarán a cabo las actuaciones en un entorno real.

Asimismo, se identifican bloques completos en los que no existe contenido técnico evaluable, como ocurre en el caso del sistema operativo MAX o en el ámbito de inteligencia artificial. **En estos casos, la propuesta se limita a reproducir los requisitos del Documento de Invitación sin aportar soluciones, lo que supone una deficiencia estructural que afecta de manera directa a la valoración del conjunto.**

**A estas carencias se añaden determinadas inconsistencias, derivadas de la reutilización de contenidos no adaptados o de la inclusión de referencias incorrectas, que reducen la adecuación de la propuesta a los requisitos planteados.** Del mismo modo, las denominadas propuestas de mejora no introducen elementos técnicos adicionales, sino que se limitan a reforzar las tareas ya descritas, sin aportar metodologías ni herramientas que permitan considerarlas como un valor diferencial.

**En consecuencia, la propuesta presenta una cobertura formal de los requisitos, pero una satisfacción técnica limitada, caracterizada por un reducido nivel de desarrollo, una baja verificabilidad y una ausencia de elementos críticos en ámbitos relevantes del servicio.** Conforme a la escala del Documento de Invitación, esta situación se corresponde con un nivel de valoración bajo, al situarse claramente por debajo de los niveles exigidos para considerar la solución como adecuada desde un punto de vista técnico.

**Nivel cualitativo:** BAJA
**Puntuación:** 2,00 sobre 8,00

### Resultado global de la solución técnica

| **Subcriterio** | **Máximo** | **Nivel** | **Puntuación** |
| --- | ---: | --- | ---: |
| Arquitectura | 2,00 | MEDIA | 0,90 |
| Comprensión de los requisitos | 2,00 | MEDIA | 1,00 |
| Viabilidad | 1,00 | MEDIA | 0,40 |
| Metodología | 1,00 | MEDIA | 0,50 |
| Rendimiento | 1,00 | BAJA | 0,25 |
| Satisfacción de los requisitos | 8,00 | BAJA | 2,00 |
| **TOTAL SOLUCIÓN TÉCNICA** | **15,00** |  | **5,05** |

## EVALUACIÓN DE LA PLANIFICACIÓN DEL SERVICIO

### Consideraciones generales sobre la planificación

La planificación se valora como herramienta real de gestión: correspondencia con los subproyectos y entregables, secuencia, duración, dependencias, hitos, recursos y mecanismos de riesgo, contingencia, calidad y trazabilidad.

### Calendario de los trabajos a desarrollar — máximo 11,00 puntos

La propuesta presentada por empresa_n incluye un cronograma estructurado por bloques funcionales y distribuido a lo largo de un periodo anual, en el que se contemplan los distintos ámbitos del servicio definidos en el Documento de Invitación. **Este planteamiento evidencia un cumplimiento formal del requisito exigido, al incorporar un elemento gráfico que pretende reflejar la planificación temporal de las actuaciones.**

No obstante, el análisis técnico detallado del diagrama de Gantt revela que dicho cronograma no responde a un modelo de planificación operativo propiamente dicho, sino que presenta un carácter híbrido que dificulta su interpretación y limita su utilidad como herramienta de gestión del servicio. En particular, el diagrama combina elementos propios de una planificación temporal con matrices de asignación de cargas o prioridades representadas mediante valores numéricos, **sin que se proporcione una leyenda o modelo interpretativo que permita comprender el significado de dichos valores ni la lógica de los colores empleados**.

**Esta falta de definición impide determinar si los valores representados corresponden a niveles de esfuerzo, dedicación de recursos, criticidad o cualquier otro parámetro, lo que convierte el cronograma en un elemento no verificable desde el punto de vista técnico.** La ausencia de un marco interpretativo claro constituye una deficiencia relevante, ya que impide al evaluador analizar la coherencia interna de la planificación y su adecuación al alcance del contrato.

**Adicionalmente, se observa que el cronograma no refleja una secuencia temporal estructurada de las actividades, sino que presenta la activación de tareas en meses aislados sin continuidad ni definición de su duración real.** En numerosos casos, una misma actividad aparece reflejada en un mes concreto y desaparece en los siguientes, sin que se identifique un inicio, un desarrollo y una finalización coherente. Esta circunstancia es especialmente significativa en servicios que, por su naturaleza, deben prestarse de forma continua, como ocurre con el mantenimiento de sistemas, la gestión del correo electrónico o la seguridad de la plataforma.

**La ausencia de continuidad en este tipo de servicios evidencia una desalineación entre la planificación representada en el Gantt y la naturaleza real del contrato, que se basa en la prestación de servicios recurrentes y no en la ejecución de actuaciones puntuales.** Esta circunstancia reduce la credibilidad del cronograma como instrumento de planificación efectiva.

Asimismo, el diagrama no incorpora relaciones de dependencia entre tareas, ni establece secuencias lógicas de ejecución que permitan identificar precedencias técnicas o caminos críticos. En particular, no se observa ninguna vinculación entre actividades que, por su naturaleza, deberían estar relacionadas, como ocurre en los procesos de migración, donde no se diferencian fases preparatorias, ejecuciones y validaciones. **Esta ausencia de dependencias impide evaluar la coherencia temporal del proyecto y limita la capacidad de analizar el impacto de posibles retrasos.**

Otro aspecto relevante es la falta de asignación explícita de recursos a las distintas actividades. **El cronograma no identifica los perfiles técnicos asociados a cada tarea ni el volumen de dedicación requerido, lo que impide evaluar si la planificación es compatible con los medios propuestos por el licitador.** Aunque se incluyen valores numéricos en las celdas, la ausencia de definición de estos impide utilizarlos como referencia válida para el análisis de cargas de trabajo.

Por otra parte, no se observa una vinculación clara entre el cronograma y los subproyectos definidos en el Anexo II del Documento de Invitación. Si bien se incluyen denominaciones similares a las del Documento de Invitación, no se establece una correspondencia trazable que permita verificar qué actuaciones se ejecutan en cada momento para cada requisito. **Esta carencia limita de forma directa la trazabilidad de la planificación y su alineación con el alcance real del contrato.**

El diagrama tampoco incluye hitos o puntos de control que permitan realizar un seguimiento estructurado del servicio, tales como entregables, revisiones o validaciones intermedias. **La ausencia de estos elementos impide definir mecanismos de control del avance del proyecto y dificulta la evaluación de su ejecución a lo largo del tiempo.**

Finalmente, el cronograma no contempla mecanismos de adaptación a riesgos ni incluye márgenes o buffers que permitan absorber desviaciones, lo que evidencia una planificación rígida y poco resiliente.

En conjunto, el diagrama de Gantt presentado cumple con el requisito formal de incluir un cronograma, pero no constituye una planificación operativa completa ni verificable. **De acuerdo con la escala establecida en el Documento de Invitación, estas deficiencias sitúan la valoración de este subcriterio en un nivel medio-bajo, cercano al límite inferior, al no permitir acreditar de forma suficiente la capacidad de planificación del servicio.**

**Nivel cualitativo:** MEDIA
**Puntuación:** 5,00 sobre 11,00

### Análisis de riesgos del proyecto — máximo 1,00 puntos

**La propuesta de empresa_n incluye un apartado dedicado al análisis de riesgos en el que se identifican distintos factores que podrían afectar a la prestación del servicio, tales como incidencias técnicas, problemas operativos o situaciones derivadas de la complejidad del entorno.** Este enfoque permite constatar que el licitador ha considerado la existencia de riesgos asociados al desarrollo del contrato.

**Sin embargo, el análisis presentado se mantiene en un nivel general, sin desarrollar una metodología específica de gestión del riesgo que permita su aplicación efectiva.** En particular, no se observa una cuantificación de los riesgos identificados ni una evaluación de su probabilidad de ocurrencia o de su impacto potencial sobre el servicio. Del mismo modo, no se establece una priorización de los riesgos que permita focalizar la gestión en aquellos con mayor relevancia.

**Asimismo, los riesgos identificados no se vinculan de forma directa con los subproyectos concretos definidos en el Anexo II, lo que limita la capacidad de trasladar este análisis a un contexto operativo real.** Tampoco se definen mecanismos específicos de seguimiento o indicadores que permitan monitorizar la evolución de los riesgos a lo largo del tiempo.

**En consecuencia, el análisis de riesgos presentado puede considerarse adecuado desde un punto de vista conceptual, pero insuficiente desde una perspectiva operativa, al no proporcionar las herramientas necesarias para una gestión efectiva del riesgo.** Conforme a la escala del Documento de Invitación, esta situación se corresponde con un nivel medio.

**Nivel cualitativo:** BAJA
**Puntuación:** 0,25 sobre 1,00

### Plan de gestión de contingencias — máximo 1,00 puntos

**El plan de contingencias presentado por empresa_n incluye referencias a la adopción de medidas generales para garantizar la continuidad del servicio ante posibles incidencias, así como a la existencia de mecanismos de recuperación y de coordinación en situaciones de fallo.** Este planteamiento evidencia la consideración de la necesidad de contar con procedimientos de respuesta ante eventos adversos.

**No obstante, el análisis detallado pone de manifiesto que dichas medidas no se desarrollan con el nivel de concreción necesario para su aplicación efectiva.** En particular, no se definen procedimientos específicos asociados a escenarios concretos de fallo, ni se establecen tiempos de recuperación que permitan evaluar la capacidad de respuesta del sistema ante incidencias relevantes. Tampoco se identifican responsables, recursos asociados o secuencias de actuación que permitan estructurar el plan de contingencias de manera operativa.

**Asimismo, no se establece una relación directa entre el plan de contingencias y los riesgos previamente identificados, lo que limita la coherencia global del modelo de gestión propuesto.** Esta falta de integración reduce la eficacia del plan y dificulta su aplicación en situaciones reales.

**En consecuencia, el plan de contingencias presenta un carácter generalista, basado en principios de actuación comunes, pero sin un desarrollo técnico suficiente que permita su implantación.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel medio-bajo.

**Nivel cualitativo:** BAJA
**Puntuación:** 0,25 sobre 1,00

### Plan de gestión de la calidad del servicio — máximo 1,00 puntos

El plan de calidad presentado por empresa_n incorpora referencias generales a acuerdos de nivel de servicio, clasificación de incidencias y seguimiento del servicio, lo que evidencia una orientación inicial hacia la gestión de la calidad. **No obstante, el análisis detallado pone de manifiesto que este planteamiento se mantiene en un nivel fundamentalmente conceptual, sin el desarrollo operativo necesario para su aplicación efectiva.**

En particular, no se definen indicadores cuantificables que permitan medir el rendimiento del servicio ni se establecen métricas asociadas a los objetivos del contrato. **Esta ausencia impide verificar el cumplimiento de los niveles de servicio y limita la capacidad de control del sistema desde un punto de vista objetivo.**

**Adicionalmente, no se describen herramientas ni sistemas de monitorización del cumplimiento de los ANS, ni se establece un modelo de seguimiento continuo basado en la recogida y análisis de datos.** Esta carencia resulta especialmente relevante a la vista del diagrama de Gantt presentado, en el que tampoco se integran mecanismos que permitan relacionar la planificación temporal con la medición de la calidad del servicio.

Asimismo, no se observa la existencia de procesos estructurados de mejora continua basados en resultados medibles, lo que limita la capacidad evolutiva del modelo propuesto.

En consecuencia, el plan de calidad presenta un carácter generalista, con un nivel de desarrollo insuficiente para su aplicación efectiva, lo que justifica su valoración en un nivel medio-bajo conforme a la escala del Documento de Invitación.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,50 sobre 1,00

### Trazabilidad del servicio — máximo 1,00 puntos

**La propuesta contempla mecanismos generales de seguimiento y registro de las actuaciones realizadas, incluyendo referencias a la documentación de intervenciones y al uso de herramientas de gestión.** Este planteamiento permite identificar una intención inicial de dotar al servicio de trazabilidad.

**Sin embargo, el análisis detallado pone de manifiesto que estos mecanismos no se desarrollan hasta constituir un sistema completo y verificable de trazabilidad.** En particular, no se define un modelo que permita relacionar de forma directa los requisitos del Documento de Invitación con las actividades ejecutadas, ni se establecen vínculos claros entre los subproyectos del Anexo II y la planificación temporal del servicio.

**Esta carencia resulta especialmente evidente al analizar el diagrama de Gantt, en el que no existe una correspondencia estructurada entre las tareas planificadas y los subproyectos definidos en el Documento de Invitación, ni se proporciona una codificación o sistema de referencia que permita realizar dicha vinculación.** Como consecuencia, no es posible determinar con precisión qué actividades se ejecutan para cada requisito ni en qué momento temporal.

Asimismo, no se identifican herramientas concretas ni procedimientos específicos de gestión de la trazabilidad que permitan garantizar el seguimiento de las actuaciones a lo largo del ciclo de vida del servicio.

En consecuencia, la trazabilidad propuesta presenta un nivel de desarrollo insuficiente y un carácter fundamentalmente declarativo, lo que limita su aplicabilidad real y justifica su valoración en un nivel bajo conforme a la escala del Documento de Invitación.

**Nivel cualitativo:** BAJA
**Puntuación:** 0,40 sobre 1,00

### Resultado global de la planificación

| **Subcriterio** | **Máximo** | **Nivel** | **Puntuación** |
| --- | ---: | --- | ---: |
| Calendario y planificación temporal | 11,00 | MEDIA | 5,00 |
| Análisis de riesgos | 1,00 | BAJA | 0,25 |
| Plan de contingencias | 1,00 | BAJA | 0,25 |
| Plan de calidad | 1,00 | MEDIA | 0,50 |
| Trazabilidad | 1,00 | BAJA | 0,40 |
| **TOTAL PLANIFICACIÓN** | **15,00** |  | **6,40** |

## RESULTADO FINAL CONSOLIDADO

| **Bloque** | **Puntuación máxima** | **Puntuación obtenida** |
| --- | ---: | ---: |
| Solución técnica ofertada | 15,00 | 5,05 |
| Planificación del servicio | 15,00 | 6,40 |
| **PUNTUACIÓN FINAL** | **30,00** | **11,45** |

### Interpretación de la puntuación

La puntuación refleja una oferta formalmente estructurada, pero con desarrollo técnico insuficiente y baja verificabilidad. Las carencias de arquitectura, procedimientos, métricas y contenido en bloques completos justifican que el resultado quede por debajo del umbral.

## CONCLUSIONES FINALES Y PROPUESTA

### Conclusiones globales de la evaluación técnica

La propuesta presenta una cobertura formal amplia y una identificación correcta del entorno de EducaMadrid, pero su desarrollo es mayoritariamente descriptivo. Faltan arquitecturas específicas, procedimientos operativos, herramientas, métricas, criterios de aceptación y mecanismos de validación. La referencia a Métrica V3 y algunos contenidos evaluables en GitLab y Redmine aportan valor parcial, sin compensar la baja concreción ni la ausencia de solución en bloques completos.

### Conclusiones sobre la solución técnica

El patrón dominante es el desarrollo insuficiente: 66 de los 89 subproyectos se clasifican como insuficientes y 21 no incluyen solución concreta. MAX e IA carecen de desarrollo técnico evaluable, mientras las carencias de BD, MON, CLO, COR, CON y MIG son recurrentes. Solo UPD5 y UPD8 alcanzan desarrollo suficiente y el valor añadido real es residual.

### Conclusiones sobre la planificación del servicio

El cronograma cumple formalmente, pero su desglose, dependencias, hitos, entregables y adaptación operativa son limitados. Los planes de riesgos, contingencias, calidad y trazabilidad se mantienen en gran medida en un nivel conceptual.

### Justificación de la valoración

La solución técnica obtiene 5,05 puntos y la planificación 6,40 puntos. La suma de 11,45 puntos mantiene la correspondencia con los niveles cualitativos asignados y con las fortalezas, carencias y evidencias desarrolladas en el informe.

### Aplicación del umbral mínimo y propuesta final

La propuesta obtiene una puntuación de **11,45 puntos sobre 30** en los criterios sujetos a juicio de valor.

El umbral mínimo exigido es de **15 puntos sobre 30**. Por tanto, la oferta **NO ALCANZA** el nivel mínimo de calidad técnica establecido.

En consecuencia, procede proponer la **exclusión de la oferta del procedimiento**, por no acreditar el nivel mínimo de calidad técnica exigido.

### Garantía de igualdad de trato y objetividad

La evaluación aplica los mismos criterios, niveles de exigencia y reglas de puntuación a ambos licitadores, y se fundamenta exclusivamente en el contenido de cada oferta y en la documentación reguladora del procedimiento.

## ANEXO. RELACIÓN DE PROYECTOS Y GRADO DE DESARROLLO DE LA PROPUESTA TÉCNICA

### Objeto y criterios de clasificación

El presente anexo resume, de manera sistemática, el grado de desarrollo de la propuesta técnica para cada proyecto o subproyecto del Anexo II. Su finalidad es aportar trazabilidad documental al análisis, sin sustituir la motivación cualitativa del informe ni producir por sí solo una traslación automática a la puntuación final.

Se aplican tres grados de desarrollo: **NO INCLUIDA**, cuando no existe una solución concreta; **INSUFICIENTE**, cuando el contenido es genérico o carece de arquitectura, procesos, herramientas o mecanismos de implementación suficientes; y **SUFICIENTE**, cuando existe una solución concreta y evaluable.

De forma separada se indican los errores técnicos relevantes, las propuestas de mejora sin valor añadido real (**PM**) y las propuestas con valor añadido verificable (**VA**).

### Tablas de subproyectos

#### BD — Bases de Datos

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| BD1 — Mantenimiento y mejora de entornos de Bases de Datos MariaDB y ProxySQL avanzado | INSUFICIENTE | PM | NO | refuerzo de revisiones sin técnicas nuevas. |
| BD2 — Mantenimiento y optimización proactiva de las bases de datos de toda la plataforma | INSUFICIENTE | PM | NO | ampliación mantenimiento sin herramientas. |
| BD3 — Mantenimiento de las bases de datos de gestión de la configuración de EducaMadrid | INSUFICIENTE | PM | NO | actualización CMDB sin automatización. |
| BD4 — Mantenimiento de las bases de datos de las Aulas Virtuales | INSUFICIENTE | PM | NO | seguimiento carga sin metodología. |
| BD5 — Mantenimiento de disparadores y Foreign Data Wrappers en los entornos Portal y LDAP Plano | INSUFICIENTE | PM | NO | verificación sin sincronización avanzada. |
| BD6 — Implementación y mantenimiento de bases de datos en entornos de microservicios | INSUFICIENTE | PM | NO | mantenimiento sin enfoque microservicios. |

#### MON — Monitorización, testeo y pruebas de rendimiento

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| MON1 — Mantenimiento periódico del almacenamiento de los centros | INSUFICIENTE | PM | NO | supervisión ampliada sin criterios técnicos. |
| MON2 — Realización periódica de pruebas de estrés en diferentes entornos de la plataforma | INSUFICIENTE | PM | NO | más pruebas sin metodología definida. |
| MON3 — Mantenimiento del sistema de monitorización y estadísticas de uso | INSUFICIENTE | PM | NO | monitorización ampliada sin métricas. |
| MON4 — Monitorización y estadísticas de servicios basados en IA | INSUFICIENTE | PM | NO | extensión genérica a IA sin especialización. |

#### UPD — Actualización de servicios existentes

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| UPD1 — Mantenimiento y mejora de los sistemas de videoconferencias de EducaMadrid | INSUFICIENTE | PM | NO | validaciones adicionales sin arquitectura. |
| UPD2 — Mantenimiento y mejora del sistema secundario de videoconferencias con opción de grabación | INSUFICIENTE | PM | NO | repetición del modelo anterior. |
| UPD3 — Mantenimiento y mejora de Mattermost | INSUFICIENTE | PM | NO | tareas ampliadas sin integración técnica. |
| UPD4 — Mantenimiento y mejora de la solución Kanban | INSUFICIENTE | PM | NO | gestión genérica sin herramienta definida. |
| UPD5 — Mantenimiento y mejora de GitLab | SUFICIENTE | PM | NO | mantenimiento convencional sin pipelines. |
| UPD6 — Mantenimiento y mejora de LimeSurvey | INSUFICIENTE | PM | NO | ajustes básicos sin optimización técnica. |
| UPD7 — Mantenimiento y mejora de SonarQube | INSUFICIENTE | PM | SÍ | contenido incorrecto sin valor. |
| UPD8 — Mantenimiento y mejora de Redmine | SUFICIENTE | VA | NO | uso API y automatización básica. |
| UPD9 — Mantenimiento y configuración de Wowza Streaming Engine | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| UPD10 — Mantenimiento y gestión de contenidos AbiesWeb | INSUFICIENTE | PM | NO | gestión básica sin integración. |
| UPD11 — Actualización, mantenimiento y gestión de contenidos de Abies+ | INSUFICIENTE | PM | NO | incidencias sin evolución funcional. |
| UPD12 — Implementación, mantenimiento y mejora de Empieza | INSUFICIENTE | PM | NO | HA conceptual sin implementación. |
| UPD13 — Mantenimiento y mejora del sistema de gestión de la configuración | INSUFICIENTE | PM | NO | sin uso herramientas exigidas. |
| UPD14 — Mantenimiento, actualización y mejora de la solución de contenedores | INSUFICIENTE | PM | NO | contenedores sin tecnología definida. |
| UPD15 — Mantenimiento, gestión y decomisionado de servidores | INSUFICIENTE | PM | NO | decomisionado incompleto. |

#### CLO — Cloud

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| CLO1 — Mantenimiento del servicio de la nube de EducaMadrid | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| CLO2 — Mantenimiento y adaptación del sistema de almacenamiento temporal de datos de la nube | INSUFICIENTE | PM | NO | ajustes progresivos sin escalabilidad. |
| CLO3 — Mantenimiento del sistema de edición en línea de EducaMadrid | INSUFICIENTE | PM | NO | uso concurrente sin arquitectura. |

#### OTR — Otros desarrollos

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| OTR1 — Mantenimiento y mejora del sistema de autenticación centralizada Single Sign-On (SSO) | INSUFICIENTE | PM | NO | SSO genérico sin federación técnica. |
| OTR2 — Mantenimiento, configuración y gestión de 2FA en el servicio de Single Sign-On | INSUFICIENTE | PM | NO | 2FA genérico con inconsistencias. |
| OTR3 — Mantenimiento y mejora de herramientas de automatización de tareas | INSUFICIENTE | PM | NO | scripts sin orquestación. |
| OTR4 — Mantenimiento y mejora del sistema de gestión y análisis de datos mediante Elastic | INSUFICIENTE | PM | NO | analítica genérica sin stack definido. |
| OTR5 — Mantenimiento y mejora de la herramienta de flujos de trabajo | INSUFICIENTE | PM | NO | workflow sin herramienta identificada. |
| OTR6 — Mantenimiento y mejora del Portal CAU | INSUFICIENTE | PM | NO | portal sin evolución funcional. |
| OTR7 — Mantenimiento y evolución de servicios de Inteligencia Artificial | INSUFICIENTE | PM | NO | IA conceptual sin implementación. |

#### COR — Correo electrónico

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| COR1 — Mantenimiento y mejora de los sistemas de control de envíos de correo | INSUFICIENTE | PM | NO | supervisión sin control de tráfico. |
| COR2 — Mantenimiento automatizado de listas de distribución de EducaMadrid | INSUFICIENTE | PM | NO | gestión manual sin automatización. |
| COR3 — Mantenimiento y mejora del sistema de activación y gestión de cuotas de correo | INSUFICIENTE | PM | NO | revisión sin política de cuotas. |
| COR4 — Mantenimiento y mejora de las herramientas de control del spam | INSUFICIENTE | PM | NO | control básico sin estrategia antispam. |
| COR5 — Mantenimiento de buzones de correo | INSUFICIENTE | PM | NO | gestión manual de buzones. |
| COR6 — Mantenimiento y mejora de la seguridad del sistema de correo | INSUFICIENTE | PM | NO | seguridad genérica sin técnicas. |
| COR7 — Actualización y mejora continua de la infraestructura de correo | INSUFICIENTE | PM | NO | infraestructura sin modularidad. |
| COR8 — Ampliación del número de servidores Mailbox Server | INSUFICIENTE | PM | NO | sin criterios de escalado. |
| COR9 — Implementación de un módulo receptor de inyección directa de correo | INSUFICIENTE | PM | NO | inyección sin arquitectura definida. |
| COR10 — Mantenimiento y soporte del módulo de inyección directa de correo | INSUFICIENTE | PM | NO | soporte básico sin optimización. |

#### MAX — Sistema Operativo MAX

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| MAX1 — Mantenimiento y actualización de MAX de forma presencial en centros de forma regular | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX2 — Mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX3 — Mantenimiento de aplicaciones basadas en MAX | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX4 — Lanzamiento anual de distribuciones de MAX «Full Equip» | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX5 — Lanzamiento anual de distribuciones «MAX lite» y/o «MAX gestión» | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX6 — Integración de aplicaciones externas en los repositorios oficiales | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX7 — Mantenimiento y mejora del servidor de gestión de accesos remotos | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX8 — Soporte de asistencia telefónica y remota para incidencias de entornos MAX | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX9 — Asistencia presencial en los diferentes eventos MAX | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX10 — Soporte presencial en eventos especiales MAX Install Party | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX11 — Gestión, mantenimiento y actualización de equipos MAX en remoto | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX12 — Instalación y configuración de dispositivos solicitados por los centros educativos | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX13 — Mantenimiento y soporte del servidor de repositorio individual para centros educativos | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| MAX14 — Herramienta de gestión centralizada de maquetas de MAX | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |

#### AV — Aulas Virtuales

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| AV1 — Actualización y comprobación periódicas de servidores de bases de datos de aulas virtuales | INSUFICIENTE | PM | NO | revisión sin herramientas. |
| AV2 — Mantenimiento de los servidores FrontEnd de aulas virtuales | INSUFICIENTE | PM | NO | supervisión sin balanceo. |
| AV3 — Despliegue de nuevos grupos de aulas virtuales | INSUFICIENTE | PM | NO | despliegue sin automatización. |
| AV4 — Redistribución periódica de NFS de aulas virtuales | INSUFICIENTE | PM | NO | redistribución sin criterios. |

#### POR — Servicio de LDAP y Portal Educativo

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| POR1 — Ampliación periódica del sistema de esclavos LDAP de EducaMadrid | INSUFICIENTE | PM | NO | ampliación sin replicación técnica. |
| POR2 — Migración del sistema LDAP máster de EducaMadrid | INSUFICIENTE | PM | NO | migración sin procedimientos. |

#### SEG — Seguridad

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| SEG1 — Mantenimiento y mejora del sistema de control de cambios en DNS | INSUFICIENTE | PM | NO | control básico sin auditoría. |
| SEG2 — LDAP Máster independiente para usuarios privilegiados | INSUFICIENTE | PM | NO | segregación sin arquitectura. |
| SEG3 — Gestión, mantenimiento e implantación de certificados | INSUFICIENTE | PM | NO | gestión sin ciclo de vida. |
| SEG4 — Gestión y mantenimiento de dominios DNS | INSUFICIENTE | PM | NO | gestión DNS sin automatización. |
| SEG5 — Análisis y corrección de vulnerabilidades | INSUFICIENTE | PM | NO | vulnerabilidades sin herramientas. |
| SEG6 — Detección de intrusiones y análisis de logs | INSUFICIENTE | PM | NO | logs sin correlación SIEM. |
| SEG7 — Auditorías internas de aplicaciones | INSUFICIENTE | PM | NO | auditorías sin metodología. |
| SEG8 — Auditorías internas continuas de sistemas | INSUFICIENTE | PM | NO | control continuo sin métricas. |
| SEG9 — Mantenimiento y uso de logs centralizados | INSUFICIENTE | PM | NO | logs sin explotación técnica. |
| SEG10 — Implementación y mantenimiento de claves RSA unificadas | INSUFICIENTE | PM | NO | claves sin gestión avanzada. |
| SEG11 — Asistencia en eventos de ciberseguridad | INSUFICIENTE | PM | NO | soporte sin procedimientos. |

#### CON — Automatización y contenedores

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| CON1 — Mantenimiento y mejora del sistema de gestión de contenedores | INSUFICIENTE | PM | NO | scripts sin orquestación. |
| CON2 — Mantenimiento y mejora de scripts y automatización de tareas | INSUFICIENTE | PM | NO | automatización sin herramientas. |
| CON3 — Mantenimiento del sistema auxiliar de automatización | INSUFICIENTE | PM | NO | sistema auxiliar sin definición. |

#### MIG — Gestión de la migración de servidores entre CPDs

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| MIG1 — Coordinación y planificación de la revisión de los entornos migrados | INSUFICIENTE | PM | NO | coordinación sin metodología. |
| MIG2 — Fases preparatorias y planificación técnica de la migración | INSUFICIENTE | PM | NO | planificación sin fases definidas. |
| MIG3 — Preparación de servidores y documentación de sistemas | INSUFICIENTE | PM | NO | preparación sin automatización. |
| MIG4 — Verificación de la migración | INSUFICIENTE | PM | NO | verificación sin criterios claros. |
| MIG5 — Mantenimiento y soporte tras la migración | INSUFICIENTE | PM | NO | soporte sin indicadores. |

#### IA — Inteligencia Artificial

| **Subproyecto** | **Grado de desarrollo** | **Mejora o valor añadido** | **Error técnico relevante** | **Observación breve** |
| --- | --- | --- | --- | --- |
| IA1 — Evaluación del rendimiento de los modelos seleccionados | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| IA2 — Ingeniería de prompts adaptados para cada servicio | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| IA3 — Testeo de los guardarraíles para el entorno educativo | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| IA4 — Evaluación de posibilidades de integración en distintos aplicativos | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |
| IA5 — Evaluación de capacidades de respuesta y límites por usuario | NO INCLUIDA | NO | NO | No se incluye una solución técnica concreta. |

### Resumen cuantitativo del anexo

#### Grado de desarrollo

| **Clasificación** | **Número de proyectos** | **Porcentaje** |
| --- | ---: | ---: |
| No incluidos | 21 | 23,60 % |
| Desarrollo insuficiente o deficiente | 66 | 74,16 % |
| Desarrollo suficiente | 2 | 2,25 % |
| **TOTAL DE PROYECTOS** | **89** | **100,00 %** |

#### Indicadores adicionales

Los indicadores no son excluyentes entre sí ni respecto del grado de desarrollo.

| **Indicador** | **Número de proyectos** | **Porcentaje sobre el total** |
| --- | ---: | ---: |
| Con errores técnicos relevantes | 1 | 1,12 % |
| Con propuesta de mejora sin valor añadido real | 67 | 75,28 % |
| Con propuesta de mejora con valor añadido real | 1 | 1,12 % |

### Conclusión del anexo

El patrón dominante es el desarrollo insuficiente: 66 de los 89 subproyectos se clasifican como insuficientes y 21 no incluyen solución concreta. MAX e IA carecen de desarrollo técnico evaluable, mientras las carencias de BD, MON, CLO, COR, CON y MIG son recurrentes. Solo UPD5 y UPD8 alcanzan desarrollo suficiente y el valor añadido real es residual.
