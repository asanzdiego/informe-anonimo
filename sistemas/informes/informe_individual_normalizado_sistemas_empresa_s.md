# INFORME DE VALORACIÓN TÉCNICA INDIVIDUAL

- **Contrato:** DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)
- **Licitador:** empresa_s

## RESUMEN EJECUTIVO

### Objeto del informe

El presente informe tiene por objeto realizar la **valoración técnica de la propuesta presentada por empresa_s** en el procedimiento basado en el **Sistema Dinámico de Adquisición SDA 26/2021**, relativo a los servicios de **DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)**.

El informe determina la puntuación correspondiente a los criterios sujetos a juicio de valor, comprueba el cumplimiento del **umbral mínimo de 15 puntos sobre 30** y formula la propuesta de continuación o exclusión que procede para la oferta.

### Metodología de valoración

La evaluación se ha estructurado en dos niveles complementarios. En primer lugar, se ha realizado un análisis técnico detallado de los proyectos y subproyectos incluidos en el Anexo II del Documento de Invitación, examinando el grado de desarrollo, adecuación y verificabilidad de las soluciones propuestas. En segundo lugar, los resultados de dicho análisis se han trasladado al esquema de valoración previsto en el apartado 7.2 del Documento de Invitación, asignando las puntuaciones correspondientes en función del nivel real de adecuación observado.

Este enfoque garantiza la trazabilidad entre **los requisitos definidos, las evidencias contenidas en la memoria, el análisis técnico efectuado y la puntuación final asignada**.

### Síntesis técnica de la propuesta

La propuesta presenta una cobertura amplia y una base técnica sólida, con arquitecturas, procedimientos y herramientas concretas en bases de datos, monitorización, observabilidad, automatización y seguridad. El uso de Ansible, Prometheus, Grafana, JMeter, Docker, Keycloak y GitLab refuerza su viabilidad. El desarrollo cubre también de forma específica MAX y los módulos de inyección de correo; persiste, no obstante, una cuantificación incompleta de métricas, umbrales y criterios de aceptación en distintos subproyectos.

### Principales conclusiones del análisis

La propuesta desarrolla de forma específica los trece bloques del Anexo II, incluidos MAX, la inyección directa de correo y la migración entre CPD. La principal limitación transversal es la falta de indicadores cuantificados, valores objetivo y criterios de aceptación completamente formalizados.

### Resultado de la valoración

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                   11,05 |
| Planificación del servicio |                 15,00 |                    9,80 |
| **TOTAL**                  |             **30,00** |               **20,85** |

### Conclusión del resumen ejecutivo

La propuesta obtiene 20,85 puntos sobre 30 y alcanza el umbral mínimo de 15 puntos. Procede proponer su continuación en coherencia con las fortalezas y carencias desarrolladas en el informe.

## INTRODUCCIÓN

### Alcance del informe

El presente informe evalúa la memoria técnica presentada por **empresa_s** para la prestación de los servicios de **DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)**. El análisis comprende tanto la **solución técnica ofertada** como la **planificación del servicio**, de acuerdo con los criterios sujetos a juicio de valor establecidos en el apartado 7.2 del Documento de Invitación.

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

La memoria mantiene una estructura coherente entre arquitectura, operación, automatización y planificación, e identifica herramientas y procedimientos aplicables al entorno. Su nivel de concreción es alto en los bloques más maduros y aporta procedimientos específicos también para MAX, aunque persisten diferencias de profundidad entre subproyectos. La trazabilidad y la evaluabilidad son suficientes, pero no siempre se apoyan en métricas, umbrales y criterios de aceptación cuantificados.

#### Nivel de desarrollo técnico y grado de concreción

La memoria mantiene una estructura coherente entre arquitectura, operación, automatización y planificación, e identifica herramientas y procedimientos aplicables al entorno. Su nivel de concreción es alto en los bloques más maduros y aporta procedimientos específicos también para MAX, aunque persisten diferencias de profundidad entre subproyectos. La trazabilidad y la evaluabilidad son suficientes, pero no siempre se apoyan en métricas, umbrales y criterios de aceptación cuantificados.

#### Comprensión y adaptación al entorno EducaMadrid

La memoria mantiene una estructura coherente entre arquitectura, operación, automatización y planificación, e identifica herramientas y procedimientos aplicables al entorno. Su nivel de concreción es alto en los bloques más maduros y aporta procedimientos específicos también para MAX, aunque persisten diferencias de profundidad entre subproyectos. La trazabilidad y la evaluabilidad son suficientes, pero no siempre se apoyan en métricas, umbrales y criterios de aceptación cuantificados.

#### Arquitectura, integración y requisitos no funcionales

La memoria mantiene una estructura coherente entre arquitectura, operación, automatización y planificación, e identifica herramientas y procedimientos aplicables al entorno. Su nivel de concreción es alto en los bloques más maduros y aporta procedimientos específicos también para MAX, aunque persisten diferencias de profundidad entre subproyectos. La trazabilidad y la evaluabilidad son suficientes, pero no siempre se apoyan en métricas, umbrales y criterios de aceptación cuantificados.

#### Trazabilidad y evaluabilidad

La memoria mantiene una estructura coherente entre arquitectura, operación, automatización y planificación, e identifica herramientas y procedimientos aplicables al entorno. Su nivel de concreción es alto en los bloques más maduros y aporta procedimientos específicos también para MAX, aunque persisten diferencias de profundidad entre subproyectos. La trazabilidad y la evaluabilidad son suficientes, pero no siempre se apoyan en métricas, umbrales y criterios de aceptación cuantificados.

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

### Consideraciones generales sobre la propuesta

#### Enfoque global de evaluación

La propuesta presenta una cobertura amplia y una base técnica sólida, con arquitecturas, procedimientos y herramientas concretas en bases de datos, monitorización, observabilidad, automatización y seguridad. El uso de Ansible, Prometheus, Grafana, JMeter, Docker, Keycloak y GitLab refuerza su viabilidad. El desarrollo cubre también de forma específica MAX y los módulos de inyección de correo; persiste, no obstante, una cuantificación incompleta de métricas, umbrales y criterios de aceptación en distintos subproyectos.

#### Cobertura del Anexo II

La propuesta desarrolla de forma específica los trece bloques del Anexo II, incluidos MAX, la inyección directa de correo y la migración entre CPD. La principal limitación transversal es la falta de indicadores cuantificados, valores objetivo y criterios de aceptación completamente formalizados.

#### Fortalezas y aportaciones de valor añadido

Se reconocen arquitecturas, herramientas y automatizaciones concretas, especialmente en bases de datos, monitorización, observabilidad, seguridad y DevOps. Estas aportaciones sustentan una valoración alta, sin extender automáticamente esa conclusión a los bloques menos desarrollados.

#### Carencias, errores y riesgos recurrentes

Se repiten la falta de métricas cuantificadas, umbrales operativos y criterios de aceptación, aun cuando la oferta sí desarrolla soluciones específicas para MAX, correo, cloud, LDAP y los servicios auxiliares. Estas limitaciones explican la distancia respecto del nivel excelente.

### Análisis por bloques funcionales del Anexo II

El análisis utiliza la misma estructura para los 89 subproyectos: requisito, contraste de la propuesta, fortalezas, carencias y nivel cualitativo. La clasificación individual se conserva en el anexo.

#### Bloque BD — Mantenimiento y mejora de entornos de Bases de Datos (BD)

- **Consideración general del bloque**

El bloque comprende la operación a gran escala de MariaDB, PostgreSQL, MongoDB y ProxySQL; clústeres, replicación, balanceo, optimización, CMDB, sincronización, seguridad, observabilidad y persistencia en microservicios.

El contraste identifica 6 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 6 incorporan valor añadido según la clasificación del anexo.

##### BD1 — Mantenimiento y mejora de entornos de Bases de Datos MariaDB y Proxy SQL avanzado

- **Requisito y alcance**

**El subproyecto BD1 define un conjunto de requisitos técnicos claramente orientados a la operación avanzada de entornos MariaDB en configuración clusterizada, incluyendo la optimización de nodos, la gestión de ProxySQL como elemento de balanceo y la monitorización del sistema mediante herramientas específicas.** Este tipo de entornos exige la definición de arquitecturas distribuidas, control de replicación, gestión de tráfico de lectura y escritura y mecanismos automatizados de alta disponibilidad.

- **Análisis de la propuesta**

La propuesta presentada por empresa_s desarrolla este subproyecto con un nivel significativo de concreción técnica, incorporando aspectos como la monitorización de clusters MariaDB, la supervisión de la replicación, el control de latencias y concurrencia, así como la optimización de consultas SQL mediante ajustes específicos de parámetros como InnoDB. **Asimismo, se incluye la gestión avanzada de ProxySQL, contemplando el balanceo de carga y la gestión de failover, lo que evidencia una comprensión adecuada del funcionamiento de este tipo de arquitecturas.**

**Adicionalmente, la propuesta incorpora elementos de automatización y observabilidad, así como el uso de herramientas específicas como ClusterControl, lo que aporta un nivel adicional de credibilidad técnica a la solución.** Este enfoque refleja una orientación hacia la operación real en entornos críticos, integrando capacidades de monitorización, automatización y mejora continua.

En términos generales, la propuesta responde de forma sólida al requisito, desarrollando una solución técnicamente coherente, aunque con un margen de mejora en la definición de indicadores cuantificables y procedimientos detallados.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: operación predictiva y alta disponibilidad.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el análisis técnico permite identificar ciertas carencias.** En particular, no se definen de forma explícita métricas concretas, umbrales de funcionamiento ni objetivos de rendimiento asociados a los sistemas, lo que limita parcialmente la verificabilidad de la solución. Asimismo, la descripción de las arquitecturas de replicación y de los procedimientos de failover no alcanza un nivel de detalle completamente operativo.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD2 — Mantenimiento y optimización proactiva de las bases de datos de toda la plataforma

- **Requisito y alcance**

**El subproyecto BD2 se centra en la optimización continua de un entorno compuesto por miles de bases de datos, incluyendo la mejora de consultas, la seguridad de conexiones, el mantenimiento preventivo y la planificación de actuaciones en períodos no lectivos.** Este requisito implica necesariamente la utilización de métricas, herramientas de análisis de rendimiento y estrategias de automatización adaptadas a gran escala.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este subproyecto mediante un planteamiento que incorpora automatización, optimización y control del rendimiento.** En particular, se describen mecanismos de supervisión automatizada, optimización de consultas SQL, gestión de índices y reorganización de datos, así como la redistribución de carga entre sistemas. Asimismo, se incluye la automatización de copias de seguridad y la validación de restauraciones, junto con la auditoría de accesos y el endurecimiento de configuraciones de seguridad.

**Uno de los aspectos más relevantes de la propuesta es su adaptación explícita a un entorno de miles de bases de datos, lo que demuestra una comprensión adecuada de la escala del sistema.** El enfoque planteado introduce un componente significativo de automatización, lo que resulta coherente con la necesidad de operar en un entorno de alta complejidad.

En conjunto, la propuesta presenta una cobertura amplia y técnicamente consistente, demostrando una capacidad adecuada para abordar la optimización proactiva del entorno.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: optimización masiva y automatización.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, se detectan ciertas limitaciones en la identificación de herramientas específicas utilizadas para estas tareas, así como en la definición de ventanas de mantenimiento claramente estructuradas en periodos no lectivos, aspecto que es relevante en el contexto del servicio educativo.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD3 — Mantenimiento de las diferentes Bases de Datos de gestión de la configuración de EducaMadrid

- **Requisito y alcance**

**Este subproyecto exige el desarrollo de una CMDB avanzada, incluyendo la incorporación de relaciones físicas y lógicas, el modelado de dependencias, la automatización de la carga de información y el uso de herramientas de software libre.** Se trata de un requisito clave para la gestión integral de la infraestructura.

- **Análisis de la propuesta**

**La propuesta de empresa_s plantea una evolución de la CMDB orientada a la integración de activos físicos y lógicos, incorporando procesos ETL para la carga de datos y promoviendo la automatización mediante herramientas como Ansible.** Asimismo, se incluyen mecanismos de sincronización continua entre sistemas y controles orientados a garantizar la calidad del dato, incluyendo validación de información y detección de inconsistencias.

**Este enfoque refleja una comprensión adecuada del papel de la CMDB como elemento central en la gestión de la infraestructura, incorporando además una visión transversal que integra distintos componentes del ecosistema.** La apuesta por la automatización y la sincronización continua constituye un elemento positivo que favorece la mantenibilidad del sistema.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: CMDB automatizada y sincronizada.

- **Carencias, omisiones, errores o riesgos**

**No obstante, se observa que la propuesta no desarrolla en profundidad la herramienta concreta indicada en el pliego, lo que limita en cierta medida la alineación completa con los requisitos específicos.** Asimismo, no se identifican métricas cuantificables de calidad del dato que permitan evaluar objetivamente el estado de la CMDB.

En conjunto, la solución es coherente y demuestra un nivel adecuado de madurez técnica, aunque con ciertas carencias en la especificación de herramientas y métricas.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD4 — Mantenimiento de las bases de datos de las Aulas Virtuales

- **Requisito y alcance**

El Documento de Invitación establece que este subproyecto debe abordar la gestión de un entorno de alta complejidad, con miles de bases de datos distribuidas en múltiples servidores, incluyendo el análisis de carga, la redistribución de información y la adaptación arquitectónica.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este requisito con un planteamiento diferenciado respecto a otros sistemas de bases de datos, incorporando herramientas y mecanismos específicos de PostgreSQL.** En este sentido, se describen actuaciones orientadas a la redistribución dinámica de carga, el ajuste fino del rendimiento mediante técnicas de tuning, la optimización de entornos clusterizados y la automatización de copias de seguridad, incluyendo la validación de restauraciones.

**Un aspecto especialmente destacable es que la propuesta no reutiliza enfoques genéricos, sino que adapta el diseño técnico a la tecnología concreta, lo que demuestra un nivel alto de comprensión del entorno.** Asimismo, se introducen elementos de escalabilidad como plantillas estandarizadas y modelos de análisis histórico.

En términos globales, la cobertura del requisito es amplia y técnicamente consistente.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: redistribución dinámica de carga.

- **Carencias, omisiones, errores o riesgos**

Las carencias detectadas se centran en la falta de identificación de herramientas concretas asociadas a PostgreSQL y en la ausencia de criterios objetivos que determinen los procesos de redistribución de carga.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD5 — Mantenimiento de disparadores y Foreign Data Wrappers en los entornos “Portal” y “LDAP Plano”

- **Requisito y alcance**

Este subproyecto requiere la implementación de mecanismos de sincronización entre sistemas, incluyendo el mantenimiento de disparadores, la gestión de FDW y el análisis de consistencia de la información entre Portal y LDAP.

- **Análisis de la propuesta**

La propuesta de empresa_s responde de forma específica a este requisito, desarrollando aspectos como la optimización de disparadores y funciones, la gestión de FDW y la implementación de scripts de sincronización entre sistemas. **Asimismo, se incorporan mecanismos de monitorización de integridad y alertas de desincronización, lo que permite identificar desviaciones en el comportamiento del sistema.**

**La adecuación de la propuesta al requisito es elevada, destacando especialmente la orientación a la trazabilidad mediante el uso de logs y mecanismos de validación.** Este enfoque contribuye a garantizar la coherencia de los datos en un entorno distribuido.

En conjunto, la solución es adecuada y demuestra una comprensión clara del requisito, aunque con margen de mejora en la definición técnica detallada.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: sincronización avanzada Portal-LDAP.

- **Carencias, omisiones, errores o riesgos**

No obstante, la propuesta presenta un nivel limitado de detalle en lo relativo a las estrategias concretas de uso de FDW y los mecanismos de control de consistencia, lo que reduce parcialmente la profundidad técnica del planteamiento.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### BD6 — Implementación y Mantenimiento de las Bases de Datos necesarias en entornos de Microservicios

- **Requisito y alcance**

El subproyecto BD6 introduce un contexto tecnológico basado en arquitecturas de microservicios, incluyendo la adopción de entornos DevOps, la gestión del ciclo de vida de los servicios y la adaptación de las bases de datos a arquitecturas distribuidas.

- **Análisis de la propuesta**

**La propuesta de empresa_s incorpora de forma explícita tecnologías como Docker, así como la utilización de pipelines de integración continua, archivos de definición de despliegue y mecanismos de automatización asociados al ciclo de vida de los servicios.** Asimismo, se contemplan aspectos como la persistencia de datos, la alta disponibilidad y la validación en entornos de preproducción.

**Este enfoque demuestra una orientación clara hacia arquitecturas modernas y una comprensión adecuada de los principios DevOps.** La inclusión de mecanismos de automatización y validación previa a producción constituye un elemento positivo que favorece la calidad del servicio.

En términos globales, la solución es consistente y alineada con el requisito, aunque con margen de mejora en la definición arquitectónica.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: migración DevOps contenerizada.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, se detecta la ausencia de herramientas específicas de orquestación de contenedores, así como una definición limitada de la arquitectura objetivo, especialmente en lo relativo a la gestión del estado y la persistencia en entornos distribuidos.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque BD

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 6 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 6 aportaciones de valor añadido.

#### Bloque MON — Monitorización, testeo y pruebas de rendimiento (MON)

- **Consideración general del bloque**

El bloque comprende la gestión de capacidad y almacenamiento NFS, las pruebas de carga y estrés, las métricas y umbrales, la observabilidad, el alertado proactivo y la monitorización específica de servicios de IA.

El contraste identifica 4 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 4 incorporan valor añadido según la clasificación del anexo.

##### MON1 — Mantenimiento periódico del almacenamiento de los centros

- **Requisito y alcance**

**El subproyecto MON1 establece como requisito la redistribución periódica de la ocupación entre distintos sistemas de almacenamiento NFS, el análisis de la ocupación real, la reorganización del almacenamiento y la ejecución de estas tareas en periodos no lectivos.** Se trata de un requisito claramente orientado a la gestión activa de capacidad y a la optimización del uso del almacenamiento en un entorno distribuido.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este subproyecto mediante la definición de un modelo de monitorización continua de la capacidad y el análisis de ocupación, incorporando mecanismos de redistribución dinámica de datos y balanceo entre nodos.** Se describen, además, procedimientos de migración controlada, validación de integridad de los datos tras el movimiento y automatización de determinadas actuaciones, todo ello orientado a optimizar el uso del almacenamiento disponible.

**Se aprecia una orientación clara hacia la gestión activa de la capacidad, incorporando elementos como el capacity planning y el uso de modelos predictivos que permiten anticipar necesidades futuras de almacenamiento.** Este enfoque se alinea con los requisitos del pliego y aporta un componente de madurez técnica relevante en entornos de gran escala.

En conjunto, la propuesta responde adecuadamente al requisito, desarrollando un modelo operativo coherente orientado a la automatización y la optimización de capacidad.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: redistribución predictiva almacenamiento.

- **Carencias, omisiones, errores o riesgos**

**No obstante, la propuesta presenta una limitación en la definición de herramientas concretas asociadas a la gestión de almacenamiento NFS, así como en la ausencia de umbrales cuantificados que determinen cuándo deben ejecutarse las redistribuciones.** Esta falta de métricas limita parcialmente la capacidad de evaluar objetivamente el comportamiento del sistema.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MON2 — Realización periódica de pruebas de estrés en diferentes entornos de la plataforma

- **Requisito y alcance**

**El subproyecto MON2 requiere la ejecución de pruebas de carga y estrés orientadas a la medición del rendimiento, el análisis de resultados, la identificación de anomalías y la determinación de sus causas, así como la propuesta de soluciones.** Este requisito implica la definición de metodologías de ingeniería de rendimiento y el uso de herramientas específicas.

- **Análisis de la propuesta**

La propuesta de empresa_s desarrolla este subproyecto con un alto grado de concreción técnica, incorporando herramientas reconocidas como Apache JMeter, Gatling y Apache Benchmark, que permiten la simulación de cargas concurrentes y la evaluación del comportamiento de los sistemas bajo diferentes condiciones.

**Asimismo, se define una metodología que incluye el diseño de escenarios de prueba, la ejecución de las mismas, la monitorización de los recursos durante la carga, el análisis de los resultados y la identificación de cuellos de botella.** Este enfoque estructurado aporta un elevado nivel de operatividad y permite evaluar la solución en condiciones próximas a la realidad.

Se valora especialmente la integración de estas pruebas dentro de un modelo continuo de operación que incorpora elementos de DevOps y observabilidad, lo que permite analizar la evolución del rendimiento a lo largo del tiempo.

En términos globales, la propuesta presenta un nivel técnico elevado y una adecuada capacidad de ejecución de pruebas de rendimiento en entornos complejos.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: pruebas integradas en DevOps.

- **Carencias, omisiones, errores o riesgos**

Como limitación, se observa la ausencia de definición explícita de objetivos de rendimiento y umbrales de aceptación asociados a los resultados de las pruebas, así como la falta de escenarios específicos vinculados a aplicaciones concretas de la plataforma.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MON3 — Mantener actualizado el sistema de monitorización y estadísticas de uso

- **Requisito y alcance**

**El subproyecto MON3 exige la actualización continua del sistema de monitorización, la incorporación de nuevos servicios, el uso de herramientas open source y la redefinición de alertas tanto reactivas como proactivas.** Este requisito implica la definición de una arquitectura de monitorización, métricas concretas y una estrategia de alertado.

- **Análisis de la propuesta**

**La propuesta de empresa_s presenta un desarrollo sólido de este requisito, incorporando una arquitectura de monitorización basada en herramientas ampliamente utilizadas como Prometheus, Grafana, Zabbix y Metabase.** La combinación de estas herramientas permite abordar la recolección de métricas, la visualización de información y la generación de cuadros de mando adaptados a diferentes niveles de análisis.

El enfoque planteado incluye la integración de diferentes fuentes de información mediante exporters específicos, la centralización de métricas y la implementación de mecanismos de alertado que permiten detectar anomalías en el comportamiento de los sistemas. **Asimismo, se introduce el concepto de capacity planning, orientado a anticipar la evolución de la carga y dimensionar adecuadamente la infraestructura.**

Se aprecia una alineación directa con los requisitos del pliego, especialmente en lo relativo al uso de herramientas open source y a la evolución continua del sistema de monitorización.

En términos generales, la solución es consistente, bien estructurada y técnicamente adecuada para entornos de gran escala.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: observabilidad avanzada completa.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, la propuesta presenta una cierta falta de definición en lo relativo a los umbrales concretos de alertado y a la clasificación de eventos, lo que introduce un elemento de incertidumbre en la operatividad diaria del sistema.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MON4 — Mantener actualizado el sistema de monitorización y estadísticas de servicios basados en IA

- **Requisito y alcance**

**El subproyecto MON4 introduce la monitorización específica de servicios basados en inteligencia artificial, incluyendo modelos de lenguaje, endpoints de inferencia, estadísticas de consumo y alertas específicas.** Este requisito tiene un carácter especializado y requiere la definición de métricas y herramientas adaptadas a plataformas de IA.

- **Análisis de la propuesta**

La propuesta de empresa_s aborda este requisito integrando la monitorización de servicios de IA dentro de la arquitectura general de observabilidad, incorporando indicadores relacionados con el rendimiento, el consumo y el comportamiento de los modelos. **Asimismo, se definen mecanismos de evaluación continua, incluyendo la medición de precisión, errores y sesgos en las respuestas generadas.**

Este enfoque representa un avance respecto a planteamientos genéricos, al incorporar elementos específicos de control y supervisión de sistemas de inteligencia artificial, incluyendo aspectos de gobernanza como el control de prompts, la trazabilidad de consultas y la auditoría de resultados.

En conjunto, la propuesta cubre el requisito de manera adecuada, incorporando elementos diferenciales propios de la operación de sistemas de IA, aunque con margen de mejora en la definición detallada de indicadores y herramientas.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: modelo LLMOps y control IA.

- **Carencias, omisiones, errores o riesgos**

No obstante, se detecta una menor profundidad en la definición de herramientas específicas para este tipo de monitorización, así como una ausencia de métricas cuantificadas que permitan evaluar el rendimiento de los modelos de forma objetiva.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque MON

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 4 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 4 aportaciones de valor añadido.

#### Bloque UPD — Actualización de servicios existentes (UPD)

- **Consideración general del bloque**

El bloque comprende arquitecturas y procedimientos para videoconferencia, grabación, colaboración, gestión de proyectos, encuestas, calidad de código, streaming, bibliotecas, configuración, contenedores y decomisionado.

El contraste identifica 15 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 15 incorporan valor añadido según la clasificación del anexo.

##### UPD1 — Mantenimiento y mejora de los sistemas de videoconferencias de EducaMadrid

- **Requisito y alcance**

**El subproyecto UPD1 exige la actualización periódica de plataformas de videoconferencia, incluyendo migraciones de versión, adaptación de componentes, optimización del rendimiento y compatibilidad con navegadores.** Se trata de un entorno complejo que requiere gestión de arquitecturas distribuidas y control de concurrencia.

- **Análisis de la propuesta**

La propuesta de empresa_s aborda este requisito mediante la definición de una arquitectura especializada que integra tecnologías como Jitsi y BigBlueButton, incorporando nodos dedicados para la gestión de media, mecanismos de balanceo y monitorización de indicadores de calidad como latencia, jitter y pérdida de paquetes.

**El enfoque planteado refleja una comprensión adecuada de las particularidades de los sistemas de videoconferencia, especialmente en lo relativo a la gestión de sesiones concurrentes y al control de la calidad del servicio.** La incorporación de métricas específicas aporta un elemento diferencial relevante frente a propuestas más genéricas.

En términos generales, la solución es técnicamente adecuada y bien orientada, aunque con margen de mejora en la definición operativa.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: optimización videoconferencia escalable.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, la propuesta no desarrolla en profundidad los mecanismos de escalabilidad ante picos de carga ni los procedimientos detallados de actualización de versiones en entornos distribuidos.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD2 — Mantenimiento y mejora del sistema secundario de Videoconferencias con opción de grabación

- **Requisito y alcance**

Este subproyecto introduce funcionalidades específicas de grabación y procesamiento de sesiones, lo que implica la gestión de almacenamiento, procesamiento y escalabilidad.

- **Análisis de la propuesta**

La propuesta de empresa_s contempla la existencia de nodos diferenciados para la grabación en el caso de BigBlueButton, lo que permite aislar este proceso del resto de la infraestructura y mejorar el rendimiento global del sistema.

Asimismo, se incluye la integración de estos sistemas con el resto de la plataforma, lo que facilita la gestión de contenidos y su posterior uso en entornos educativos.

En conjunto, la solución cubre el requisito, aunque con un desarrollo técnico menos profundo que el observado en otros apartados.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: mejora grabación y estabilidad BBB.

- **Carencias, omisiones, errores o riesgos**

No obstante, la propuesta presenta un nivel de desarrollo limitado en lo relativo a los procesos de almacenamiento, indexación y procesamiento de grabaciones, así como en la definición de políticas de retención y gestión de espacio.

- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD3 — Mantenimiento y mejora de la herramienta Mattermost

- **Requisito y alcance**

El subproyecto exige la gestión de una plataforma de comunicación interna con dependencias en bases de datos, sistemas de indexación y mecanismos de alta disponibilidad.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye la gestión de herramientas colaborativas dentro de una arquitectura segmentada que integra servicios como Mattermost, LDAP y sistemas internos, con capacidad de despliegue en entornos contenerizados y control de accesos mediante SSO.

Este enfoque demuestra una comprensión adecuada del contexto en el que se integra la herramienta, así como de la necesidad de garantizar su disponibilidad y seguridad.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: actualización automatizada sin impacto.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, la propuesta no desarrolla de forma detallada los componentes internos de la plataforma ni los mecanismos específicos de alta disponibilidad o escalabilidad asociados a Mattermost.

En términos generales, la solución es correcta y coherente, aunque con un nivel de detalle técnico limitado.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD4 — Mantenimiento y mejora de la solución Kanban

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y mejora de la solución Kanban**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta identifica Wekan y define actualización sobre versiones estables, migraciones controladas de datos y configuración, validación en preproducción y reversión. Añade despliegue contenerizado, plantillas de flujo e integración de notificaciones.

La evidencia se encuentra en el apartado específico **UPD4** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Mantenimiento de Wekan con migración, preproducción, reversión y despliegue contenerizado.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### UPD5 — Mantenimiento y mejora de la solución GitLab

- **Requisito y alcance**

El subproyecto UPD5 exige la gestión de una plataforma compleja de desarrollo colaborativo, incluyendo pipelines, repositorios y herramientas de integración continua.

- **Análisis de la propuesta**

La propuesta de empresa_s integra GitLab dentro de su modelo DevOps, incluyendo pipelines CI/CD, automatización de despliegues y control de versiones, lo que refleja una comprensión adecuada del papel de esta herramienta en el ciclo de vida del desarrollo.

En términos generales, la solución es coherente y alineada con el requisito, aunque con margen de mejora en la concreción técnica.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: gestión avanzada actualizaciones.

- **Carencias, omisiones, errores o riesgos**

No obstante, el nivel de detalle sobre la configuración específica de pipelines, la gestión de runners o la definición de entornos de despliegue resulta limitado.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD6 — Mantenimiento y mejora de la solución LimeSurvey

- **Requisito y alcance**

**El subproyecto UPD6 establece como requisito la actualización de la herramienta LimeSurvey, la mejora de su arquitectura, la optimización del rendimiento y la evolución funcional del sistema.** Se trata de un entorno que requiere una comprensión clara de su arquitectura, de la gestión de bases de datos subyacentes y de la experiencia de usuario.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este subproyecto dentro de su arquitectura general multinivel, en la que se definen componentes diferenciados para aplicación, datos y almacenamiento, integrados mediante mecanismos de seguridad y operación.** Este planteamiento muestra una comprensión básica del funcionamiento de la herramienta y su ubicación dentro del ecosistema EducaMadrid.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **UPD6** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD7 — Mantenimiento y mejora de SonarQube

- **Requisito y alcance**

El subproyecto UPD7 exige el mantenimiento y mejora de la plataforma SonarQube, incluyendo la gestión de calidad de código, reglas de análisis, perfiles de calidad y control de calidad de proyectos.

- **Análisis de la propuesta**

La propuesta de empresa_s integra SonarQube dentro de su modelo DevOps, donde se contempla el análisis de código dentro de pipelines CI/CD y la automatización de procesos de validación. **Este planteamiento es coherente con el uso habitual de la herramienta en entornos de desarrollo moderno y refleja una comprensión adecuada de su papel dentro del ciclo de vida de software.**

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: integración continua y validación.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el grado de desarrollo técnico específico resulta limitado en lo relativo a la configuración de la herramienta.** No se describen elementos fundamentales como la definición de Quality Gates, la gestión de perfiles de calidad, el uso de reglas específicas o la integración detallada con repositorios. Esta ausencia de detalle reduce la capacidad de evaluar el nivel real de madurez del planteamiento.

En conjunto, la solución cubre el ámbito funcional requerido, aunque con una concreción técnica limitada.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD8 — Mantenimiento y mejora de Redmine

- **Requisito y alcance**

El subproyecto UPD8 plantea la gestión de la herramienta Redmine, incluyendo automatización, mantenimiento evolutivo y mejora funcional.

- **Análisis de la propuesta**

**La propuesta de empresa_s incluye la integración de herramientas de gestión dentro de su modelo operativo, planteando la utilización de APIs, automatización mediante scripts y mecanismos de autenticación centralizada mediante SSO.** Este enfoque facilita la integración de Redmine dentro del ecosistema, especialmente en lo relativo a la trazabilidad del servicio.

Se aprecia una alineación adecuada con el uso de Redmine en entornos de gestión de incidencias y proyectos, incorporando además elementos de automatización que mejoran la eficiencia operativa.

En términos generales, la solución es coherente y funcional, aunque con un desarrollo técnico moderado.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: mejora compatibilidad y rendimiento.

- **Carencias, omisiones, errores o riesgos**

No obstante, la propuesta no profundiza en aspectos como la configuración de flujos de trabajo, la gestión avanzada de proyectos ni la integración detallada con otras herramientas del sistema como GitLab o sistemas de monitorización.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD9 — Mantenimiento y configuración de Wowza Streaming Engine.

- **Requisito y alcance**

El subproyecto UPD9 requiere la gestión de una plataforma de streaming basada en tecnologías como Wowza, incluyendo protocolos de transmisión, codificación de vídeo y distribución de contenidos.

- **Análisis de la propuesta**

**La propuesta de empresa_s contempla la retransmisión en vivo mediante una arquitectura orientada a streaming, incluyendo el uso de Wowza, servicios de transcodificación escalables y distribución mediante CDN.** Este planteamiento demuestra una comprensión clara del funcionamiento de sistemas de streaming y de sus componentes principales.

La inclusión de elementos de procesamiento asíncrono y control de acceso permite abordar de forma adecuada los requisitos de rendimiento y seguridad asociados a la transmisión de contenidos.

En conjunto, la solución presenta un nivel técnico adecuado y una alineación correcta con el requisito, aunque con margen de mejora en la definición operativa.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **UPD9** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD10 — Mantenimiento y gestión de contenidos AbiesWeb

- **Requisito y alcance**

El subproyecto UPD10 está orientado a la gestión de contenidos bibliográficos mediante AbiesWeb, incluyendo la carga masiva de datos, la sincronización con sistemas externos y la gestión de catálogos.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este subproyecto de forma indirecta dentro de su modelo de gestión de aplicaciones, sin desarrollar específicamente las particularidades de AbiesWeb.** Se describen actividades generales de mantenimiento, gestión de contenidos e integración con otros servicios, lo que proporciona una cobertura básica del requisito.

En conjunto, la cobertura del requisito es parcial y se mantiene en un nivel descriptivo general.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **UPD10** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD11 — Actualización, Mantenimiento y gestión de contenidos de Abies+

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Actualización, Mantenimiento y gestión de contenidos de Abies+**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta trata Abies+ como una implantación diferenciada: dimensiona desarrollo, preproducción y producción, optimiza la base de datos, contempla alta disponibilidad, copias consistentes e integración con Keycloak o LDAP, y automatiza las actualizaciones.

La evidencia se encuentra en el apartado específico **UPD11** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Arquitectura, alta disponibilidad y actualización automatizada de Abies+.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### UPD12 — Implementación, mantenimiento y mejora de Empieza

- **Requisito y alcance**

El subproyecto UPD12 presenta un alto nivel de exigencia técnica, incluyendo la necesidad de escalado horizontal y vertical, alta disponibilidad, balanceo de carga y optimización del rendimiento.

- **Análisis de la propuesta**

La propuesta de empresa_s define Empieza como un microservicio central que actúa como elemento de integración entre plataformas mediante APIs y motor de reglas, lo que refleja claramente su papel dentro del ecosistema EducaMadrid.

El planteamiento incluye una arquitectura multinivel con balanceo, integración con sistemas corporativos y mecanismos de seguridad y trazabilidad, lo que aporta coherencia y alineación con el requisito.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **UPD12** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD13 — mantenimiento y mejora del sistema de gestión de la configuración

- **Requisito y alcance**

El subproyecto UPD13 exige el uso de herramientas específicas como CMDBuild y Ansible, así como la automatización de procesos y la correlación de datos.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye la automatización mediante Ansible y la integración de sistemas dentro de una CMDB centralizada, lo que aporta un enfoque coherente con el requisito.

En consecuencia, la cobertura del requisito es parcial, con un enfoque generalista que no alcanza el nivel de detalle requerido.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **UPD13** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD14 — Mantenimiento, Actualización y mejora de la solución de contenedores

- **Requisito y alcance**

Este subproyecto requiere la gestión de entornos de contenedores, incluyendo tecnologías específicas como Docker, Kubernetes o Podman, así como la automatización de despliegues y la gestión de infraestructuras.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye la utilización de Docker y la integración en pipelines CI/CD, lo que demuestra una orientación clara hacia la contenerización.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **UPD14** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### UPD15 — Mantenimiento de gestión y decomisionado de servidores

- **Requisito y alcance**

El subproyecto UPD15 exige la gestión completa del ciclo de vida de servidores, incluyendo su retirada, gestión de DNS, direcciones IP, almacenamiento y eliminación de dependencias.

- **Análisis de la propuesta**

La propuesta de empresa_s aborda este aspecto de forma general dentro de su modelo de operación, incluyendo actividades de actualización de inventario y gestión de sistemas.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **UPD15** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque UPD

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 15 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 15 aportaciones de valor añadido.

#### Bloque CLO — Cloud (CLO)

- **Consideración general del bloque**

El bloque comprende disponibilidad, escalabilidad, almacenamiento temporal, edición en línea, integración, seguridad, rendimiento, actualización y continuidad de los servicios cloud de EducaMadrid.

El contraste identifica 3 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 3 incorporan valor añadido según la clasificación del anexo.

##### CLO1 — Mantenimiento del servicio de la nube de EducaMadrid

- **Requisito y alcance**

**El subproyecto CLO1 requiere la mejora y evolución de la infraestructura cloud, incluyendo la distribución de carga para un entorno de aproximadamente dos millones de usuarios, la redistribución del almacenamiento, la planificación de capacidad a medio y largo plazo y la gestión de cuotas.** Se trata de un requisito claramente orientado a entornos de alta escalabilidad y gestión avanzada de infraestructura.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este subproyecto mediante la definición de una arquitectura cloud basada en soluciones como NextCloud y Collabora, integradas en un entorno multinivel con mecanismos de balanceo, almacenamiento compartido y control de sesión mediante sistemas como Redis.** Este planteamiento permite identificar una base técnica coherente para la prestación del servicio, especialmente en lo relativo a la integración de componentes y a la gestión de sesiones concurrentes.

**Asimismo, se incorporan elementos de seguridad, control de cuotas y gestión de almacenamiento, lo que demuestra una comprensión de las necesidades básicas del sistema cloud en un entorno educativo.** La propuesta plantea además la posibilidad de evolucionar hacia arquitecturas más avanzadas como el uso de object storage en el futuro, lo que indica una orientación hacia la mejora continua.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: arquitectura distribuida escalable.

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, el análisis técnico evidencia que la propuesta no desarrolla en profundidad aspectos críticos como la planificación de capacidad a medio y largo plazo, la definición de mecanismos concretos de redistribución de carga o la gestión operativa de un entorno que puede alcanzar millones de usuarios.** La ausencia de métricas cuantificadas y de procedimientos detallados limita la capacidad de evaluar la viabilidad real de la solución en condiciones de alta demanda.

En consecuencia, la propuesta presenta una base técnica adecuada pero con un desarrollo insuficiente en términos de operación a gran escala.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CLO2 — Mantenimiento y adaptación del sistema de almacenamiento temporal de datos de la nube

- **Requisito y alcance**

**Este subproyecto exige el mantenimiento del sistema de almacenamiento temporal, su interoperabilidad con el entorno cloud y su adaptación a necesidades de escalabilidad y carga.** Se trata de un componente crítico en el funcionamiento de la plataforma.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este subproyecto dentro de su arquitectura general de almacenamiento, contemplando el uso de sistemas NFS y la posible evolución hacia soluciones más avanzadas.** Se incluyen mecanismos de control de almacenamiento temporal, caducidad de datos y trazabilidad de accesos, lo que proporciona una base funcional coherente.

El enfoque planteado permite identificar una comprensión adecuada del papel de este tipo de almacenamiento dentro de la plataforma, especialmente en lo relativo a la gestión del ciclo de vida de los datos temporales y su integración con servicios asociados.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: optimización almacenamiento cloud.

- **Carencias, omisiones, errores o riesgos**

**No obstante, la propuesta presenta carencias significativas en la definición de mecanismos de escalabilidad, distribución de carga y alta disponibilidad.** No se describen procedimientos específicos orientados a garantizar la interoperabilidad con otros sistemas ni se identifican herramientas concretas para la gestión del almacenamiento temporal en entornos de alta concurrencia.

En consecuencia, la solución resulta funcional desde un punto de vista conceptual, pero presenta un desarrollo técnico limitado para abordar escenarios exigentes.

- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CLO3 — Mantenimiento del sistema de edición en línea de EducaMadrid

- **Requisito y alcance**

El subproyecto CLO3 establece la necesidad de mantener y evolucionar el sistema de edición en línea, incluyendo la mejora de infraestructura, la integración con la nube y la capacidad de adaptación a múltiples usuarios.

- **Análisis de la propuesta**

La propuesta de empresa_s plantea una integración entre NextCloud y herramientas de edición colaborativa como Collabora, con separación de componentes y control de sesiones mediante Redis, lo que permite una gestión estructurada del servicio. **Este enfoque refleja una comprensión adecuada de las necesidades de edición colaborativa en entornos educativos, incluyendo la gestión simultánea de múltiples usuarios y la integración con sistemas de almacenamiento.**

En consecuencia, la propuesta presenta una cobertura funcional adecuada, pero con un nivel de desarrollo técnico incompleto.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **CLO3** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque CLO

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 3 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 3 aportaciones de valor añadido.

#### Bloque OTR — Otros desarrollos (OTR)

- **Consideración general del bloque**

El bloque comprende SSO y 2FA, automatización, Elastic, flujos de trabajo, Portal CAU e inteligencia artificial, con especial atención a integraciones, seguridad, trazabilidad, herramientas y operativa real.

El contraste identifica 7 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 7 incorporan valor añadido según la clasificación del anexo.

##### OTR1 — Mantenimiento y mejora del sistema de autentificación centralizada Single Sign On (SSO)

- **Requisito y alcance**

El subproyecto OTR1 requiere la gestión del sistema de autenticación centralizada, incluyendo la integración SSO entre aplicaciones, la sincronización con LDAP, la implantación de alta disponibilidad y la incorporación de mecanismos de autenticación reforzada.

- **Análisis de la propuesta**

**La propuesta de empresa_s desarrolla este subproyecto mediante la adopción de una arquitectura basada en Keycloak, integrada con LDAP y con mecanismos de control de sesiones, lo que refleja una alineación directa con el requisito.** Se contempla la autenticación centralizada como un elemento transversal de la arquitectura, lo que permite su integración con el resto de servicios de la plataforma.

Asimismo, se incorporan aspectos de seguridad como el control de accesos y la protección frente a vulnerabilidades comunes, lo que contribuye a reforzar la fiabilidad del sistema.

En términos generales, la solución es adecuada y demuestra una comprensión del requisito, aunque con margen de mejora en la definición técnica.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: SSO unificado y seguro.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, la propuesta no desarrolla en profundidad aspectos como la federación de identidades, la gestión avanzada de sesiones o la definición detallada de arquitecturas de alta disponibilidad, lo que limita la capacidad de evaluar su comportamiento en escenarios críticos.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR2 — Mantenimiento, configuración y gestión 2FA en el servicio de Single Sign On (SSO)

- **Requisito y alcance**

El subproyecto OTR2 se centra en la gestión de la autenticación multifactor, incluyendo la integración con sistemas existentes, la correlación con directorios LDAP y la configuración de métodos de verificación.

- **Análisis de la propuesta**

**La propuesta de empresa_s incluye el uso de mecanismos de autenticación multifactor basados en OTP y aplicaciones móviles, lo que demuestra una comprensión adecuada de las tecnologías implicadas.** Asimismo, se plantea su integración con el sistema SSO, lo que permite reforzar la seguridad de acceso a la plataforma.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: autenticación multifactor optimizada.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el nivel de detalle técnico es limitado en lo relativo a la gestión de identidades, la sincronización con directorios y la definición de procedimientos de implantación.** Tampoco se describen mecanismos de gestión operativa del sistema ni políticas detalladas de seguridad.

En consecuencia, la solución resulta adecuada desde un punto de vista conceptual, pero carece de desarrollo técnico suficiente.

- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR3 — Mantenimiento y mejora de herramientas de automatización de tareas

- **Requisito y alcance**

Este subproyecto exige la gestión de herramientas de automatización en un entorno complejo, incluyendo la ejecución de tareas repetitivas, la integración entre sistemas y la optimización de procesos.

- **Análisis de la propuesta**

La propuesta de empresa_s incorpora la automatización como uno de los pilares de su modelo operativo, incluyendo el uso de herramientas como Ansible y pipelines CI/CD, lo que aporta coherencia con el enfoque general de la solución.

Este planteamiento introduce un nivel significativo de automatización en la operación del servicio, lo que favorece la eficiencia y la reducción de errores humanos.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: automatización procesos operativos.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, no se identifican arquitecturas específicas de orquestación ni sistemas centralizados de gestión de automatizaciones, lo que limita el desarrollo técnico del subproyecto.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR4 — Mantenimiento y mejora de un sistema de gestión y análisis de datos mediante el stack de Elastic

- **Requisito y alcance**

El subproyecto OTR4 requiere la gestión de sistemas de análisis de datos basados en el stack Elastic, incluyendo la ingestión, procesamiento y análisis de logs.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye la utilización de herramientas de observabilidad y análisis de datos, integradas dentro de su modelo de monitorización, lo que proporciona una base funcional adecuada.

En consecuencia, la cobertura del requisito es parcial.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: analítica avanzada con ELK.

- **Carencias, omisiones, errores o riesgos**

No obstante, el nivel de desarrollo técnico específico es limitado, ya que no se describen arquitecturas detalladas del stack Elastic ni procesos de ingestión, almacenamiento o visualización de datos.

- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR5 — Mantenimiento y mejora de la herramienta de flujos de trabajo

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y mejora de la herramienta de flujos de trabajo**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta desarrolla una plataforma de flujos con actualización controlada, base de datos dedicada, automatización y trazabilidad. La integra expresamente con GitLab, CMDB, monitorización y SSO, y prevé métricas y cuadros de mando.

La evidencia se encuentra en el apartado específico **OTR5** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Flujos automatizados e integrados con GitLab, CMDB, monitorización y SSO.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### OTR6 — Mantenimiento y mejora del Portal CAU

- **Requisito y alcance**

El subproyecto OTR6 requiere la gestión del portal de atención al usuario, incluyendo su evolución funcional, integración y mejora de usabilidad.

- **Análisis de la propuesta**

La propuesta de empresa_s aborda este ámbito de forma general, integrando la gestión de incidencias dentro de su modelo operativo, pero sin desarrollar específicamente las funcionalidades del portal CAU.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: integración herramientas internas.

- **Carencias, omisiones, errores o riesgos**

La falta de detalle técnico limita la valoración del subproyecto.

- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### OTR7 — Mantenimiento y evolución de servicios de Inteligencia Artificial para la plataforma EducaMadrid

- **Requisito y alcance**

Este subproyecto requiere la evolución de servicios de inteligencia artificial dentro de la plataforma, incluyendo el entrenamiento, despliegue y gestión de modelos.

- **Análisis de la propuesta**

La propuesta de empresa_s incorpora la inteligencia artificial de forma transversal, integrándola en diferentes componentes como analítica, automatización y soporte docente, así como en procesos de evaluación continua y control de calidad de resultados.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: IA aplicada a procesos internos.

- **Carencias, omisiones, errores o riesgos**

Se aprecia un enfoque innovador y alineado con las tendencias actuales, aunque la definición técnica de arquitecturas, pipelines de entrenamiento y despliegue de modelos resulta limitada.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque OTR

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 7 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 7 aportaciones de valor añadido.

#### Bloque COR — Correo electrónico (COR)

- **Consideración general del bloque**

El bloque comprende control de envíos, listas, cuotas, spam, buzones, seguridad, infraestructura, escalado de Mailbox Server e inyección directa, incluyendo colas, spool, rendimiento, resiliencia y coexistencia.

El contraste identifica 10 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 10 incorporan valor añadido según la clasificación del anexo.

##### COR1 — Mantenimiento y mejora de los sistemas de control de envíos de correo

- **Requisito y alcance**

**El subproyecto COR1 exige la implantación y evolución de mecanismos de control de envío de correo, incluyendo limitaciones según proveedores, control de flujos y regulación del tráfico saliente.** Se trata de un ámbito que requiere una definición clara de políticas de envío, gestión de colas y control de reputación.

- **Análisis de la propuesta**

La propuesta de empresa_s integra el sistema de correo dentro de una arquitectura distribuida basada en componentes como RoundCube para acceso web y QMail para transporte, incorporando elementos de seguridad como SPF, DKIM y DMARC, así como mecanismos antispam y antimalware. **Este planteamiento demuestra una comprensión adecuada de los componentes técnicos implicados en la infraestructura de correo.**

En consecuencia, la cobertura del requisito resulta parcial, al centrarse en la infraestructura básica y omitir aspectos clave de control operativo.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **COR1** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR2 — Mantenimiento automatizado de listas de distribución de EducaMadrid

- **Requisito y alcance**

Este subproyecto requiere la automatización del mantenimiento de listas de distribución, incluyendo su actualización periódica, sincronización con sistemas corporativos y gestión de altas y bajas masivas.

- **Análisis de la propuesta**

La propuesta de empresa_s aborda este ámbito dentro de su enfoque general de automatización e integración con sistemas corporativos, especialmente mediante su modelo basado en LDAP, SSO y herramientas de automatización como Ansible. **Este planteamiento permite inferir una base funcional para la sincronización de usuarios y la gestión de identidades, lo que constituye un elemento positivo.**

Se aprecia una alineación conceptual con el requisito, en tanto que la propuesta plantea una arquitectura integrada en la que los sistemas de identidad y correo se encuentran interconectados, lo que facilita la automatización de procesos de actualización de usuarios.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **COR2** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR3 — Mantenimiento y mejora del sistema de activación y gestión de cuotas de correo

- **Requisito y alcance**

El subproyecto COR3 implica la definición de políticas de cuotas por usuario y su gestión automatizada, incluyendo la activación de límites y el control del uso del sistema.

- **Análisis de la propuesta**

**La propuesta de empresa_s contempla la gestión del almacenamiento de buzones dentro de una arquitectura distribuida con replicación y alta disponibilidad, incluyendo mecanismos de backup y control de capacidad.** Este enfoque proporciona una base sólida desde el punto de vista de infraestructura.

En consecuencia, la cobertura del requisito resulta parcial, al centrarse en la infraestructura base sin abordar los mecanismos funcionales asociados a la gestión de cuotas.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **COR3** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR4 — Mantenimiento y mejora de las herramientas relacionadas con el control del spam

- **Requisito y alcance**

El subproyecto COR4 exige la gestión avanzada de sistemas antispam, incluyendo la realización de campañas de phishing controladas y la mejora de los mecanismos de detección.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye la integración de sistemas antispam dentro de la arquitectura de correo, junto con mecanismos de seguridad como SPF, DKIM y DMARC, lo que constituye una base adecuada para la protección del sistema frente a amenazas externas.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **COR4** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR5 — Mantenimiento de buzones de correo

- **Requisito y alcance**

Este subproyecto requiere la gestión masiva de buzones, incluyendo su creación, eliminación, redistribución y mantenimiento operativo.

- **Análisis de la propuesta**

La propuesta de empresa_s plantea una arquitectura con almacenamiento distribuido, replicación de buzones y mecanismos de backup y recuperación, lo que aporta un nivel adecuado de robustez desde el punto de vista de infraestructura.

Se aprecia un enfoque orientado a garantizar la continuidad del servicio, con mecanismos de alta disponibilidad y recuperación ante fallos.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **COR5** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR6 — Mantenimiento y mejora continua de la seguridad del sistema de correo

- **Requisito y alcance**

El subproyecto COR6 establece la necesidad de garantizar la seguridad del sistema de correo, incluyendo la gestión de certificados, cifrado y mecanismos de protección.

- **Análisis de la propuesta**

La propuesta de empresa_s integra la seguridad como un elemento transversal, incorporando mecanismos de protección frente a amenazas, control de accesos y monitorización de eventos. **Este enfoque resulta coherente con los requisitos del pliego.**

- **Fortalezas y valor añadido**

La memoria original desarrolla para **COR6** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR7 — Actualización y mejora continua de la infraestructura en la que se basa el sistema de correo

- **Requisito y alcance**

Este subproyecto exige la evolución de la infraestructura de correo, diferenciando componentes y mejorando su rendimiento y escalabilidad.

- **Análisis de la propuesta**

La propuesta de empresa_s integra el sistema de correo dentro de una arquitectura global distribuida basada en RoundCube, QMail y almacenamiento en alta disponibilidad, incorporando mecanismos de replicación, backup y monitorización de parámetros operativos como colas, volumen o latencia. **Este enfoque aporta una base técnica adecuada desde el punto de vista estructural.**

Asimismo, el modelo planteado por empresa_s, basado en automatización y operación continua, sugiere una orientación hacia la mejora progresiva de los sistemas, lo cual resulta coherente con el requisito del pliego.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: alta disponibilidad distribuida.

- **Carencias, omisiones, errores o riesgos**

**No obstante, el desarrollo específico del subproyecto resulta limitado.** No se detallan planes concretos de actualización tecnológica de los componentes de correo ni estrategias de evolución de la arquitectura. Tampoco se describen procedimientos operativos para la realización de actualizaciones en entornos críticos, ni mecanismos de validación previa que garanticen la estabilidad del sistema tras los cambios.

La ausencia de herramientas específicas asociadas a la gestión del ciclo de vida de la infraestructura, así como la falta de métricas cuantificadas que permitan evaluar la mejora continua del servicio, limita la verificabilidad de la solución.

En consecuencia, la propuesta presenta una base técnica adecuada, pero con un desarrollo insuficiente en lo relativo a la evolución estructurada del sistema.

- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR8 — Ampliación del número de servidores Mailbox Server

- **Requisito y alcance**

El subproyecto COR8 implica la ampliación de infraestructura en función de la carga, lo que requiere la definición de métricas y criterios de escalado.

- **Análisis de la propuesta**

La propuesta de empresa_s contempla una arquitectura de almacenamiento distribuido con buzones en alta disponibilidad, basada en replicación y mecanismos de continuidad del servicio. **Este planteamiento permite inferir una base adecuada para soportar el crecimiento del número de servidores.**

Adicionalmente, la propuesta incluye un enfoque general de escalabilidad transversal en la plataforma, apoyado en balanceo y distribución de servicios, lo que constituye un elemento positivo en términos de capacidad de crecimiento.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: optimización rendimiento envíos.

- **Carencias, omisiones, errores o riesgos**

**Sin embargo, el subproyecto no se desarrolla de forma específica desde el punto de vista operativo.** No se describen criterios de dimensionamiento de nuevos servidores, ni políticas de distribución de carga entre buzones, ni procedimientos detallados de ampliación en entornos productivos. Tampoco se identifican herramientas concretas para la gestión del escalado ni métricas que permitan anticipar necesidades de crecimiento.

La falta de planificación de capacidad a medio y largo plazo introduce incertidumbre sobre la capacidad real de adaptación del sistema a incrementos de carga.

En consecuencia, la solución resulta adecuada a nivel conceptual, pero con un desarrollo técnico limitado para su aplicación operativa.

- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### COR9 — Implementación y mejora de un módulo receptor de inyección directa para la infraestructura de transporte de correo

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Implementación y mejora de un módulo receptor de inyección directa para la infraestructura de transporte de correo**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta propone un módulo de ingestión directa mediante QMQP y qmqpd, con escritura atómica en el spool, coexistencia no intrusiva con SMTP, persistencia, escalado en paralelo y despliegue reversible.

La evidencia se encuentra en el apartado específico **COR9** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Inyección QMQP en spool, no intrusiva, persistente, escalable y reversible.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### COR10 — Mantenimiento y soporte del módulo de inyección directa de correo

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y soporte del módulo de inyección directa de correo**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta concreta el soporte de qmqpd: supervisión del socket y los procesos, control de escritura e integridad, parámetros de back-pressure y concurrencia, pruebas funcionales, de carga, resiliencia y coexistencia, rollback, documentación y transferencia.

La evidencia se encuentra en el apartado específico **COR10** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Soporte qmqpd con pruebas, observabilidad, back-pressure, rollback y documentación.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### Conclusión del bloque COR

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 10 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 10 aportaciones de valor añadido.

#### Bloque MAX — Sistema Operativo MAX (MAX)

- **Consideración general del bloque**

El bloque comprende soporte presencial y remoto, servidores de construcción y repositorios, mantenimiento de aplicaciones y distribuciones, integraciones, eventos, dispositivos y gestión centralizada de equipos y maquetas.

El contraste identifica 14 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 14 incorporan valor añadido según la clasificación del anexo.

##### MAX1 — Mantenimiento y actualización de MAX de forma presencial en centros de forma regular

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y actualización de MAX de forma presencial en centros de forma regular**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta define intervenciones presenciales planificadas por criticidad, versión y hardware; incluye actualización, parcheado, compatibilidad de periféricos, imágenes certificadas, diagnóstico remoto previo y automatización de configuraciones.

La evidencia se encuentra en el apartado específico **MAX1** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Intervención presencial planificada, imágenes certificadas y diagnóstico remoto previo.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX2 — Mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta separa los entornos de construcción legacy y actual, gestiona dependencias y propone un pipeline CI/CD, builds reproducibles en contenedores, versionado y trazabilidad de distribuciones y repositorios propios.

La evidencia se encuentra en el apartado específico **MAX2** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Construcción CI/CD reproducible, versionada y trazable de distribuciones MAX.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX3 — Mantenimiento de aplicaciones basadas en MAX

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento de aplicaciones basadas en MAX**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta desarrolla el ciclo de vida de aplicaciones MAX: control de código y versiones, compilación, dependencias, parcheado y validación. Añade preproducción, certificación de aplicaciones, seguimiento de vulnerabilidades y catálogo controlado.

La evidencia se encuentra en el apartado específico **MAX3** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Validación, certificación y control de vulnerabilidades de aplicaciones MAX.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX4 — Lanzamiento de distribuciones de MAX “Full Equip” anualmente

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Lanzamiento de distribuciones de MAX “Full Equip” anualmente**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta estructura el lanzamiento Full Equip en definición, construcción y validación, con pruebas funcionales y de compatibilidad. Añade pipeline de generación, testing, trazabilidad de builds y actualizaciones incrementales.

La evidencia se encuentra en el apartado específico **MAX4** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Lanzamiento Full Equip mediante pipeline, testing y trazabilidad de versiones.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX5 — Lanzamiento de distribuciones de “MAX lite” y/o “max gestión” anualmente

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Lanzamiento de distribuciones de “MAX lite” y/o “max gestión” anualmente**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta diferencia MAX Lite y MAX Gestión, adapta cada distribución a su perfil de uso y hardware, y propone modularidad, optimización de rendimiento e integración de herramientas de gestión.

La evidencia se encuentra en el apartado específico **MAX5** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Distribuciones Lite y Gestión diferenciadas, modulares y optimizadas.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX6 — Integración de aplicaciones externas a los repositorios oficiales

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Integración de aplicaciones externas a los repositorios oficiales**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta define análisis funcional, compatibilidad y seguridad de aplicaciones externas, adaptación y empaquetado, gestión de dependencias e incorporación controlada a repositorios. Añade catálogo, entorno de pruebas, seguimiento de CVE y empaquetado automatizado.

La evidencia se encuentra en el apartado específico **MAX6** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Integración controlada con catálogo, pruebas, seguimiento de CVE y empaquetado automatizado.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX7 — Mantenimiento y mejora del servidor de gestión accesos remotos

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y mejora del servidor de gestión accesos remotos**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta configura una plataforma central de acceso remoto con roles, registro de sesiones e integración en la infraestructura. Añade cifrado, control unificado, monitorización y trazabilidad de conexiones.

La evidencia se encuentra en el apartado específico **MAX7** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Acceso remoto centralizado, cifrado, monitorizado y trazable.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX8 — Soporte de asistencia telefónica y remota para incidencias de entornos MAX

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Soporte de asistencia telefónica y remota para incidencias de entornos MAX**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta combina soporte telefónico y remoto, registro y clasificación de incidencias, diagnóstico y validación posterior. Añade base de conocimiento, priorización y métricas de resolución.

La evidencia se encuentra en el apartado específico **MAX8** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Soporte remoto trazable con priorización, base de conocimiento y métricas.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX9 — Asistencia presencial en los diferentes eventos MAX

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Asistencia presencial en los diferentes eventos MAX**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta planifica la asistencia a eventos, coordina recursos y presta soporte presencial sobre equipos y aplicaciones. Añade preparación previa, procedimientos estandarizados e incorporación de incidencias a la base de conocimiento.

La evidencia se encuentra en el apartado específico **MAX9** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Soporte de eventos planificado, estandarizado y reutilizable como conocimiento.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX10 — Soporte presencial en eventos especiales (MAX Install Party)

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Soporte presencial en eventos especiales (MAX Install Party)**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta prepara las Install Party con imágenes, scripts y repositorios locales, ejecuta instalaciones y configuraciones masivas y recoge resultados. Añade automatización, homogeneidad y transferencia de conocimiento.

La evidencia se encuentra en el apartado específico **MAX10** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Install Party con imágenes, scripts, repositorios locales y despliegue automatizado.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX11 — Gestión, mantenimiento y actualización de equipos MAX en remoto

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Gestión, mantenimiento y actualización de equipos MAX en remoto**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta inventaría los equipos gestionados y ejecuta actualizaciones, parches y validaciones remotas. Añade plataforma central, automatización de despliegues y monitorización continua del parque.

La evidencia se encuentra en el apartado específico **MAX11** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Gestión remota centralizada con inventario, actualizaciones y monitorización.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX12 — Instalación y configuración de dispositivos solicitadas por los centros educativos

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Instalación y configuración de dispositivos solicitadas por los centros educativos**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta valida compatibilidad Linux/MAX, instala controladores, configura y prueba periféricos. Añade catálogo de dispositivos, procedimientos homogéneos, scripts de drivers y base de conocimiento.

La evidencia se encuentra en el apartado específico **MAX12** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Integración de periféricos con catálogo de compatibilidad y scripts de instalación.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX13 — Mantenimiento y soporte del servidor de repositorio individual para centros educativos

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y soporte del servidor de repositorio individual para centros educativos**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta mantiene el repositorio individual mediante una plataforma de software libre orientada a Migasfree, con inventario, paquetes, versiones y control del parque. Añade gestión multicentro, políticas automatizadas y auditoría.

La evidencia se encuentra en el apartado específico **MAX13** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Repositorio Migasfree multicentro con inventario, políticas y auditoría.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### MAX14 — Herramienta de gestión centralizada de maquetas de MAX

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Herramienta de gestión centralizada de maquetas de MAX**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta evoluciona Migasfree como plataforma de maquetas versionadas, agentes, políticas y control de cumplimiento. Añade gobierno del software, despliegues automatizados y detección de equipos fuera de estándar.

La evidencia se encuentra en el apartado específico **MAX14** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Maquetas versionadas y gobernadas mediante Migasfree y políticas automatizadas.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### Conclusión del bloque MAX

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 14 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 14 aportaciones de valor añadido.

#### Bloque AV — Aulas Virtuales (AV)

- **Consideración general del bloque**

El bloque comprende actualización y estabilidad de bases de datos y FrontEnd, despliegue de nuevos grupos, redistribución de NFS, automatización, balanceo y adaptación a picos de carga.

El contraste identifica 4 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 4 incorporan valor añadido según la clasificación del anexo.

##### AV1 — Actualización y comprobación periódicas de servidores físicos y virtuales de BBDD de los entornos de aulas virtuales

- **Requisito y alcance**

El subproyecto AV1 requiere la actualización y comprobación de servidores físicos y virtuales que soportan las bases de datos de aulas virtuales, lo que implica tareas de revisión técnica, control de estado y validación de funcionamiento en entornos de alta carga.

- **Análisis de la propuesta**

**La propuesta de empresa_s aborda este subproyecto de forma indirecta a través de su planteamiento general sobre bases de datos y monitorización, incorporando mecanismos de revisión periódica, optimización y validación del estado de los sistemas.** Se aprecia una coherencia general con lo descrito en el bloque de bases de datos, especialmente en lo relativo a PostgreSQL y entornos de alta carga.

En consecuencia, la cobertura puede considerarse parcial, basada en extrapolaciones de otros apartados de la propuesta.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **AV1** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### AV2 — Mantenimiento de los servidores virtuales FrontEnd de los entornos de aulas virtuales

- **Requisito y alcance**

Este subproyecto exige el mantenimiento de los servidores de front-end, incluyendo la gestión de accesos, la disponibilidad del servicio y la optimización del rendimiento.

- **Análisis de la propuesta**

**La propuesta de empresa_s contempla arquitecturas de aplicaciones distribuidas con balanceo de carga y control de sesiones, lo que permite inferir una base técnica válida para la gestión de servidores frontend.** El enfoque multinivel planteado es coherente con este tipo de sistemas y permite garantizar una cierta escalabilidad del servicio.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **AV2** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### AV3 — Despliegue periódico de nuevos grupos de aulas virtuales y ampliación de los actuales

- **Requisito y alcance**

El subproyecto AV3 requiere el despliegue periódico de nuevos entornos de aulas virtuales, incluyendo la ampliación de infraestructuras existentes.

- **Análisis de la propuesta**

La propuesta de empresa_s incorpora conceptos de automatización y despliegue mediante pipelines CI/CD y herramientas de configuración, lo que permite inferir una capacidad potencial para el despliegue automatizado de servicios.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **AV3** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### AV4 — Redistribución periódica de los NFS de datos de las aulas virtuales

- **Requisito y alcance**

Este subproyecto establece la redistribución periódica de almacenamiento NFS en el entorno de aulas virtuales.

- **Análisis de la propuesta**

**La propuesta de empresa_s incluye en su modelo de operación mecanismos de redistribución de almacenamiento y gestión de capacidad, lo que permite abordar este requisito de forma indirecta.** Se contemplan procesos de análisis de ocupación y traslado de datos entre nodos, así como validaciones posteriores a la migración.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: escalabilidad horizontal LMS.

- **Carencias, omisiones, errores o riesgos**

No obstante, no se desarrollan estrategias específicas para el entorno de aulas virtuales ni se definen criterios concretos de redistribución, como umbrales de ocupación o indicadores de rendimiento.

En consecuencia, la solución es técnicamente coherente pero insuficientemente desarrollada.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque AV

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 4 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 4 aportaciones de valor añadido.

#### Bloque POR — Servicio de LDAP y Portal Educativo (POR)

- **Consideración general del bloque**

El bloque comprende escalado de esclavos LDAP, replicación, disponibilidad y rendimiento, así como planificación, reversibilidad, integridad y validación de la migración del LDAP máster.

El contraste identifica 2 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 2 incorporan valor añadido según la clasificación del anexo.

##### POR1 — Ampliación periódica del sistema de esclavos LDAP de EducaMadrid

- **Requisito y alcance**

**El subproyecto POR1 establece la ampliación del sistema LDAP mediante la incorporación de nuevos nodos esclavos, lo que implica la gestión de replicación del directorio, la sincronización continua de datos y la garantía de consistencia entre nodos en un entorno distribuido.** Se trata de una operación que requiere definir claramente la arquitectura LDAP, los mecanismos de replicación y los procedimientos de validación de integridad del sistema.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye LDAP como uno de los pilares de su arquitectura, integrándolo con sistemas de identidad y control de acceso. **Este enfoque refleja una comprensión adecuada del papel de LDAP dentro del ecosistema EducaMadrid.**

En consecuencia, la cobertura del requisito resulta parcial.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **POR1** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### POR2 — Migración del sistema LDAP máster de EducaMadrid

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Migración del sistema LDAP máster de EducaMadrid**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta define un nuevo LDAP Master virtualizado y endurecido, comunicaciones LDAPS/TLS, exportación e importación controladas, reconfiguración de la replicación y validación funcional. Añade alta disponibilidad, preproducción y copias flexibles.

La evidencia se encuentra en el apartado específico **POR2** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Migración LDAP con LDAPS, replicación, alta disponibilidad, preproducción y copias.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### Conclusión del bloque POR

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 2 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 2 aportaciones de valor añadido.

#### Bloque SEG — Seguridad (SEG)

- **Consideración general del bloque**

El bloque comprende control de cambios y dominios DNS, segregación de identidades privilegiadas, certificados, vulnerabilidades, detección de intrusiones, auditoría continua, centralización de logs, claves RSA y respuesta ante incidentes.

El contraste identifica 11 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 11 incorporan valor añadido según la clasificación del anexo.

##### SEG1 — Mantenimiento y mejora del sistema de control de cambios en DNS

- **Requisito y alcance**

El subproyecto SEG1 exige la implantación de mecanismos de control de cambios en DNS que permitan auditar modificaciones, mantener trazabilidad y garantizar la estabilidad de la configuración en el tiempo.

- **Análisis de la propuesta**

**La propuesta de empresa_s integra la gestión de la infraestructura dentro de un modelo global que incorpora trazabilidad, control de accesos y registro de operaciones.** En particular, se hace referencia a la utilización de mecanismos de auditoría y control dentro de su arquitectura transversal, así como a la existencia de una CMDB y sistemas de automatización que permiten registrar cambios en el entorno.

Este enfoque resulta conceptualmente adecuado y permite inferir que los cambios en sistemas como DNS podrían quedar registrados dentro del modelo general de operación.

En consecuencia, la propuesta cubre el requisito desde una perspectiva general de control del sistema, pero no alcanza el grado de detalle necesario en el ámbito específico de DNS.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG1** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG2 — Mantenimiento y mejora de un LDAP Máster independiente para usuarios privilegiados

- **Requisito y alcance**

Este subproyecto establece la necesidad de separar los usuarios privilegiados en un entorno LDAP independiente, con el objetivo de reforzar la seguridad y el control de accesos.

- **Análisis de la propuesta**

La propuesta de empresa_s plantea una arquitectura de identidad centralizada basada en LDAP y SSO mediante Keycloak, integrando mecanismos de autenticación, control de accesos y gestión de sesiones dentro de un modelo transversal aplicable a toda la plataforma.

Este planteamiento evidencia una comprensión adecuada del modelo de gestión de identidades y del papel del LDAP como elemento central en la arquitectura de seguridad.

En consecuencia, la propuesta presenta un buen enfoque general de identidad, pero no alcanza el nivel de especialización requerido.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG2** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG3 — Gestión, mantenimiento e implantación anual de los certificados de EducaMadrid

- **Requisito y alcance**

El subproyecto SEG3 requiere la gestión completa del ciclo de vida de certificados, incluyendo su generación, distribución, renovación y revocación.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye la seguridad como elemento transversal, contemplando el uso de certificados dentro de su arquitectura general, especialmente en relación con comunicaciones seguras y autenticación entre componentes.

Se aprecia que el modelo de operación incorpora la actualización de componentes y la gestión continua de la seguridad, lo que permite inferir la existencia de procesos asociados a la renovación de certificados.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG3** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG4 — Gestión y mantenimiento periódico de dominios DNS

- **Requisito y alcance**

Este subproyecto implica la administración de dominios DNS, incluyendo su mantenimiento, actualización y control de consistencia.

- **Análisis de la propuesta**

La propuesta de empresa_s integra los sistemas de la plataforma dentro de un entorno gestionado y monitorizado, lo que permite inferir una base de gestión sobre servicios como DNS. **Se incorpora además un modelo de operación basado en automatización y control de cambios que resulta coherente con este tipo de tareas.**

En consecuencia, la cobertura del requisito se mantiene en un nivel general, sin un desarrollo técnico específico.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG4** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG5 — Análisis y corrección de vulnerabilidades

- **Requisito y alcance**

El subproyecto SEG5 exige la identificación y mitigación de vulnerabilidades mediante el uso de herramientas y metodologías específicas.

- **Análisis de la propuesta**

La propuesta de empresa_s contempla la seguridad como un elemento integrado, incluyendo la monitorización continua de amenazas, la identificación de vulnerabilidades y la resolución de incidencias en plazos definidos, como por ejemplo la corrección de vulnerabilidades críticas en periodos inferiores a 24 horas.

Este enfoque representa un aspecto positivo, ya que introduce un componente de operación continua alineado con las buenas prácticas de seguridad.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG5** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG6 — Gestión, mantenimiento y ajuste de la herramienta para la detección de intrusiones, monitorización de la integridad, análisis de logs y respuesta ante incidentes.

- **Requisito y alcance**

Este subproyecto requiere la implantación de mecanismos de detección de intrusiones basados en el análisis de logs y la correlación de eventos.

- **Análisis de la propuesta**

**La propuesta de empresa_s incorpora la monitorización continua y la centralización de logs dentro de su modelo de observabilidad, integrando la recogida de métricas, eventos y trazas en una arquitectura transversal.** Asimismo, se contempla la detección temprana de incidentes y la supervisión constante del sistema, lo que evidencia una orientación hacia la seguridad operativa continua.

Este enfoque resulta alineado con los principios básicos del subproyecto y aporta una base funcional adecuada para la identificación de anomalías y eventos de seguridad.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG6** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG7 — Realización de auditorías internas de aplicaciones

- **Requisito y alcance**

El subproyecto SEG7 exige la realización de auditorías de seguridad en aplicaciones siguiendo metodologías estructuradas.

- **Análisis de la propuesta**

La propuesta de empresa_s integra prácticas de seguridad dentro del ciclo de vida del desarrollo, apoyándose en un modelo DevOps con automatización y validación continua. **Este enfoque permite incorporar controles de calidad en fases tempranas del desarrollo y constituye una base adecuada para la realización de auditorías.**

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG7** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG8 — Realización de auditorías internas continuas de los sistemas

- **Requisito y alcance**

Este subproyecto amplía el anterior al conjunto de sistemas, requiriendo un enfoque continuo de auditoría.

- **Análisis de la propuesta**

La propuesta de empresa_s incorpora elementos de monitorización continua, trazabilidad y control de actividad dentro de su arquitectura global, lo que permite inferir una cierta capacidad para la supervisión continuada del entorno.

En consecuencia, la propuesta presenta un enfoque coherente desde la perspectiva de monitorización continua, pero no alcanza el nivel de formalización requerido para auditorías continuas estructuradas.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG8** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG9 — Mantenimiento y uso de logs centralizados

- **Requisito y alcance**

El subproyecto SEG9 exige la centralización de logs para su análisis y gestión.

- **Análisis de la propuesta**

**La propuesta de empresa_s contempla explícitamente la centralización de logs dentro de su modelo de observabilidad, integrando la recogida de información procedente de múltiples sistemas y su análisis conjunto.** Este enfoque constituye uno de los puntos más sólidos del bloque, ya que permite habilitar capacidades de monitorización avanzada y trazabilidad completa del sistema.

Se valora positivamente la integración de logs, métricas y trazas dentro de una estrategia unificada, lo que facilita la detección de anomalías y el análisis de comportamiento del sistema.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG9** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG10 — Implementación y mantenimiento de claves RSA unificadas

- **Requisito y alcance**

Este subproyecto implica la gestión de claves criptográficas, incluyendo su creación, distribución y renovación.

- **Análisis de la propuesta**

La propuesta de empresa_s incorpora la seguridad y el cifrado como elementos transversales dentro de su arquitectura, incluyendo la protección de comunicaciones y el control de accesos.

En consecuencia, la cobertura del subproyecto resulta parcial.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG10** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### SEG11 — Asistencia y soporte presencial en los diferentes eventos de Ciberseguridad de EducaMadrid

- **Requisito y alcance**

Este subproyecto contempla la participación en eventos y el soporte técnico asociado.

- **Análisis de la propuesta**

La propuesta de empresa_s incluye un modelo de servicio con capacidades de soporte y operación sobre la plataforma, así como un equipo técnico con competencias en seguridad y sistemas, lo que permite inferir la capacidad de prestar este tipo de servicios dentro del marco general del contrato.

En consecuencia, la propuesta cubre el requisito de forma genérica, pero sin un desarrollo específico suficiente.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **SEG11** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque SEG

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 11 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 11 aportaciones de valor añadido.

#### Bloque CON — Automatización y contenedores (CON)

- **Consideración general del bloque**

El bloque comprende orquestación, ciclo de vida de contenedores, infraestructura como código, scripts, herramientas auxiliares, control de versiones, pruebas y observabilidad.

El contraste identifica 3 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 3 incorporan valor añadido según la clasificación del anexo.

##### CON1 — Mantenimiento y mejora del sistema de gestión de contenedores

- **Requisito y alcance**

El subproyecto CON1 requiere la gestión de plataformas de contenedores, incluyendo su mantenimiento, actualización y evolución mediante herramientas específicas.

- **Análisis de la propuesta**

La propuesta de empresa_s aborda este subproyecto mediante la inclusión de contenedores como parte de su estrategia tecnológica, incorporando el uso de Docker y la integración con pipelines de integración continua. **Este enfoque demuestra una orientación adecuada hacia modelos modernos de despliegue y operación de servicios, alineándose con los principios DevOps.**

Asimismo, el propio planteamiento indica en algunos casos que el uso de determinadas tecnologías se encuentra en fase de análisis o evaluación, lo que introduce un grado de incertidumbre sobre su aplicación real en el servicio.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **CON1** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CON2 — Mantenimiento y mejora de los scripts y sistemas de automatización de tareas

- **Requisito y alcance**

Este subproyecto exige la automatización de tareas mediante scripts en un entorno complejo.

- **Análisis de la propuesta**

**La propuesta de empresa_s incorpora la automatización como uno de los pilares fundamentales de su modelo operativo, incluyendo el uso de herramientas como Ansible y la integración de pipelines CI/CD para la gestión de despliegues y configuraciones.** Este enfoque se encuentra alineado con las buenas prácticas actuales y aporta un nivel significativo de eficiencia en la operación del servicio.

La automatización propuesta permite reducir la intervención manual, mejorar la trazabilidad de las actuaciones y minimizar errores operativos, lo que constituye un elemento positivo en un entorno de alta complejidad.

A pesar de esta limitación, el subproyecto presenta una cobertura adecuada y consistente con el planteamiento general de la propuesta.

- **Fortalezas y valor añadido**

La memoria identifica una aportación de valor añadido: infraestructura como código.

- **Carencias, omisiones, errores o riesgos**

Sin embargo, no se identifican sistemas centralizados de orquestación ni plataformas específicas para la gestión global de automatizaciones, lo que limita la capacidad de escalar este enfoque de forma estructurada a todos los sistemas de la plataforma.

- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### CON3 — Mantenimiento y mejora del sistema auxiliar de automatización

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Mantenimiento y mejora del sistema auxiliar de automatización**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta desarrolla CON3 como plataforma de APIs REST versionadas, con supervisión de endpoints, reintentos, registro de eventos y trazabilidad. Añade integración con Ansible y GitLab CI/CD, preproducción y refuerzo de seguridad.

La evidencia se encuentra en el apartado específico **CON3** de la oferta original y permite evaluar el subproyecto de forma separada, sin inferir contenido de otras tareas.

- **Fortalezas y valor añadido**

Automatización por APIs REST con observabilidad, CI/CD, reintentos y auditoría.

- **Carencias, omisiones, errores o riesgos**

Pese al desarrollo técnico acreditado, la oferta no cuantifica de forma completa valores objetivo, umbrales operativos o criterios de aceptación para todos los resultados descritos. Esta limitación impide asignar el nivel EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta, evaluable y adaptada al requisito, con mejoras coherentes; las limitaciones de cuantificación justifican mantenerla en la banda del 51 % al 75 %.

##### Conclusión del bloque CON

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 3 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 3 aportaciones de valor añadido.

#### Bloque MIG — Gestión de la migración de servidores entre CPDs (MIG)

- **Consideración general del bloque**

El bloque comprende coordinación, inventario, dependencias, fases preparatorias, documentación, criterios de aceptación, pruebas, reversibilidad, verificación y soporte posterior a la migración.

El contraste identifica 5 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 5 incorporan valor añadido según la clasificación del anexo.

##### MIG1 — Coordinación y planificación de la revisión de los entornos migrados

- **Requisito y alcance**

**El subproyecto MIG1 establece la necesidad de coordinar y planificar la revisión de los entornos tras los procesos de migración, lo que implica la verificación del estado de los sistemas, la comprobación de los servicios afectados y la coordinación entre los distintos equipos técnicos implicados.** Este tipo de tareas requiere una metodología estructurada que permita validar la correcta transición de los sistemas entre entornos.

- **Análisis de la propuesta**

**La propuesta de empresa_s incorpora un modelo de operación basado en la trazabilidad, monitorización continua y control del servicio, lo que permite inferir una base adecuada para la supervisión de entornos migrados.** En particular, la existencia de monitorización integral, registros de actividad y control de la operación facilita la detección de posibles desviaciones tras la migración.

Asimismo, el modelo de gobierno multinivel (estratégico, táctico y operativo) descrito en la propuesta permite entender que existiría una estructura organizativa capaz de coordinar este tipo de actividades, lo que representa un alineamiento conceptual con el requisito.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **MIG1** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**MEDIA**: El nivel **MEDIA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MIG2 — Fases preparatorias y planificación técnica de la migración

- **Requisito y alcance**

Este subproyecto exige la definición de las fases previas a la migración, incluyendo la planificación técnica, el análisis de dependencias y la preparación de los sistemas, lo que requiere una estructuración clara del proceso.

- **Análisis de la propuesta**

**La propuesta de empresa_s incorpora un enfoque metodológico que incluye planificación, análisis de riesgos y gestión de contingencias, lo que constituye un elemento positivo alineado con este tipo de procesos.** En particular, la inclusión de un plan de riesgos y de un plan de contingencia sugiere una aproximación estructurada a la gestión de cambios complejos.

Asimismo, el modelo DevOps planteado, junto con la validación en entornos de preproducción y el control de despliegues, aporta una base conceptual adecuada para abordar migraciones de sistemas de forma controlada.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **MIG2** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### MIG3 — Preparación de servidores y documentación de sistemas

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **Preparación de servidores y documentación de sistemas**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta recopila CPU, memoria, almacenamiento, sistema operativo, servicios, aplicaciones, puertos y dependencias en fichas técnicas por servidor. Define procedimientos de parada y arranque, validaciones y checklists antes, durante y después de la migración, y añade extracción automatizada y trazabilidad de las comprobaciones.

- **Fortalezas y valor añadido**

Fichas normalizadas, procedimientos reutilizables, recopilación automatizada y checklists operativos.

- **Carencias, omisiones, errores o riesgos**

La oferta desarrolla el procedimiento, pero no fija valores objetivo ni criterios de aceptación cuantificados para todas las verificaciones, por lo que no procede elevar la valoración a EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta y evaluable, con mejoras coherentes y una limitación residual de cuantificación.

##### MIG4 — verificación de la migración

- **Requisito y alcance**

El subproyecto exige una solución concreta y evaluable para **verificación de la migración**, conforme al alcance definido en el Anexo II.

- **Análisis de la propuesta**

La oferta ejecuta scripts de diagnóstico antes, durante y después del traslado, compara estados, supervisa servicios y aplicaciones, registra incidencias y verifica integridad de datos, configuraciones y sistemas de ficheros. Añade informes comparativos, panel de seguimiento y validación por capas.

- **Fortalezas y valor añadido**

Diagnóstico automatizado, comparación pre/post, seguimiento en tiempo real y validación por capas.

- **Carencias, omisiones, errores o riesgos**

La oferta desarrolla el procedimiento, pero no fija valores objetivo ni criterios de aceptación cuantificados para todas las verificaciones, por lo que no procede elevar la valoración a EXCELENTE.

- **Valoración cualitativa**

**ALTA**: existe una solución concreta y evaluable, con mejoras coherentes y una limitación residual de cuantificación.

##### MIG5 — Mantenimiento y soporte tras la migración

- **Requisito y alcance**

El subproyecto MIG5 establece la necesidad de proporcionar soporte posterior a la migración, incluyendo la resolución de incidencias y la estabilización del sistema.

- **Análisis de la propuesta**

**La propuesta de empresa_s contempla un modelo de operación continua basado en monitorización, gestión de incidencias y soporte 24/7 para entornos críticos, lo que constituye un elemento claramente alineado con este requisito.** Asimismo, el enfoque de trazabilidad completa y control del servicio facilita el seguimiento de incidencias y actuaciones.

Se valora positivamente la integración de estos mecanismos dentro del modelo general de operación, ya que permiten una supervisión continua del sistema tras cambios significativos como una migración.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **MIG5** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque MIG

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 5 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 5 aportaciones de valor añadido.

#### Bloque IA — Inteligencia Artificial (IA)

- **Consideración general del bloque**

El bloque comprende evaluación de modelos, ingeniería de prompts, guardarraíles, integración en aplicaciones, capacidad, límites por usuario, métricas, seguridad, trazabilidad y operación de los servicios de IA.

El contraste identifica 5 subproyectos con desarrollo suficiente, 0 con desarrollo insuficiente y 0 no incluidos; 5 incorporan valor añadido según la clasificación del anexo.

##### IA1 — EVALUAR el rendimiento de los modelos seleccionados

- **Requisito y alcance**

El subproyecto IA1 comprende evaluación del rendimiento de los modelos seleccionados, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

- **Análisis de la propuesta**

La propuesta de empresa_s incorpora la inteligencia artificial como un elemento transversal dentro de la arquitectura, integrando su uso en diferentes ámbitos como analítica, automatización y servicios educativos. **En particular, se plantea la evaluación continua del comportamiento de los modelos mediante indicadores como precisión, errores y sesgos, lo que evidencia una comprensión adecuada de la necesidad de medir el rendimiento de estos sistemas.**

Asimismo, se describe el uso de mecanismos de monitorización asociados a los servicios de IA, incluyendo parámetros de funcionamiento y calidad de respuesta, lo que aporta un enfoque coherente con la necesidad de supervisión continua.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **IA1** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA2 — Ingeniería de Prompts adaptados para cada servicio

- **Requisito y alcance**

El subproyecto IA2 comprende ingeniería de prompts adaptados para cada servicio, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

- **Análisis de la propuesta**

La propuesta de empresa_s incorpora explícitamente el concepto de “gobierno de prompts”, incluyendo aspectos como el versionado, la aprobación y la trazabilidad de los mismos. **Este elemento constituye uno de los puntos más destacados del bloque, ya que introduce un enfoque estructurado en la gestión de la interacción con modelos de lenguaje.**

Asimismo, se contempla la integración de la IA en distintos servicios, lo que implica la adaptación de prompts a diferentes casos de uso, mostrando una comprensión adecuada del requisito.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **IA2** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA3 — Testeo de los guardarraíles para el entorno educativo

- **Requisito y alcance**

El subproyecto IA3 comprende testeo de los guardarraíles para el entorno educativo, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

- **Análisis de la propuesta**

**La propuesta de empresa_s incorpora mecanismos de control y supervisión asociados al uso de la IA, incluyendo auditoría de consultas, registro de resultados, control de acceso a datos y validación de respuestas en usos críticos.** Asimismo, se contempla la supervisión humana como elemento de control, lo que constituye un aspecto relevante en entornos sensibles como el educativo.

Este enfoque demuestra una comprensión adecuada de la necesidad de establecer límites operativos en sistemas basados en IA.

En consecuencia, la propuesta aborda adecuadamente el concepto de control de IA, pero sin desarrollar en profundidad los mecanismos técnicos asociados a su implantación.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **IA3** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA4 — Evaluar Posibilidades de Integración en Distintos Aplicativos

- **Requisito y alcance**

El subproyecto IA4 comprende evaluación de posibilidades de integración en distintos aplicativos, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

- **Análisis de la propuesta**

**La propuesta de empresa_s incorpora la IA como un elemento transversal, integrándola en diferentes áreas como analítica, automatización, generación de contenido y mejora de la experiencia de usuario.** Asimismo, se plantean casos de uso concretos como generación de preguntas, análisis de contenido o automatización de procesos, lo que evidencia una visión amplia de integración.

Este planteamiento resulta coherente con el requisito y demuestra una comprensión adecuada de las posibilidades de incorporación de IA en la plataforma.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **IA4** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### IA5 — Evaluación de Capacidades de Respuesta y Límites por Usuario

- **Requisito y alcance**

El subproyecto IA5 comprende evaluación de capacidades de respuesta y límites por usuario, con los procedimientos, integraciones, controles, entregables y mecanismos de validación necesarios para su ejecución en el entorno de EducaMadrid.

- **Análisis de la propuesta**

**La propuesta de empresa_s contempla el análisis de la capacidad de respuesta de los sistemas de IA, incluyendo aspectos relacionados con el rendimiento, el consumo de recursos y el comportamiento de los modelos.** Asimismo, se menciona la evaluación de límites de uso y la necesidad de controlar la interacción de los usuarios con los sistemas de IA.

Este enfoque resulta coherente con el requisito y evidencia una comprensión de la necesidad de regular el uso de estos sistemas.

- **Fortalezas y valor añadido**

La memoria original desarrolla para **IA5** una propuesta de mejora específica en el apartado propio del subproyecto; se conserva como **VA** sin trasladar aportaciones de otros ID.
- **Carencias, omisiones, errores o riesgos**

Aunque existe una solución concreta y evaluable, la oferta no fija en todos los casos valores objetivo para las métricas, los umbrales operativos y los criterios de aceptación; esta limitación impide elevar automáticamente la valoración a EXCELENTE.
- **Valoración cualitativa**

**ALTA**: El nivel **ALTA** mantiene la correspondencia entre el contenido efectivamente desarrollado, su clasificación en el anexo y las fortalezas y carencias anteriores.

##### Conclusión del bloque IA

La valoración conjunta del bloque es **ALTA**. La clasificación individual muestra 5 desarrollos suficientes, 0 insuficientes y 0 no incluidos, con 5 aportaciones de valor añadido.

### Conclusión del análisis detallado

La propuesta desarrolla de forma específica los trece bloques del Anexo II, incluidos MAX, la inyección directa de correo y la migración entre CPD. La principal limitación transversal es la falta de indicadores cuantificados, valores objetivo y criterios de aceptación completamente formalizados. La propuesta presenta una cobertura amplia y una base técnica sólida, con arquitecturas, procedimientos y herramientas concretas en bases de datos, monitorización, observabilidad, automatización y seguridad. El uso de Ansible, Prometheus, Grafana, JMeter, Docker, Keycloak y GitLab refuerza su viabilidad. El desarrollo cubre también de forma específica MAX y los módulos de inyección de correo; persiste, no obstante, una cuantificación incompleta de métricas, umbrales y criterios de aceptación en distintos subproyectos.

## EVALUACIÓN DE LA SOLUCIÓN TÉCNICA OFERTADA

### Fundamentación de la valoración

La valoración se basa en el análisis pormenorizado anterior y atiende a la calidad, concreción, coherencia, adecuación, viabilidad y verificabilidad del contenido, no a su mera presencia formal.

### Arquitectura planteada en los distintos subproyectos — máximo 2,00 puntos

**La propuesta presentada por empresa_s incorpora una arquitectura técnica global claramente definida, estructurada mediante un enfoque multinivel orientado a la integración de servicios, automatización de procesos y operación de infraestructuras complejas.** La memoria describe de forma consistente distintos componentes transversales como LDAP, SSO, monitorización, automatización CI/CD, bases de datos, cloud, servicios colaborativos e inteligencia artificial, estableciendo relaciones funcionales entre ellos y configurando un modelo arquitectónico homogéneo para el conjunto de la plataforma.

**La propuesta destaca especialmente en ámbitos como bases de datos, monitorización, automatización y observabilidad, donde se identifican arquitecturas diferenciadas por tecnología, incluyendo entornos MariaDB, PostgreSQL, ProxySQL, Prometheus, Grafana, JMeter, Docker y sistemas de integración continua.** Este planteamiento aporta un nivel relevante de coherencia técnica y permite comprender cómo se articula la prestación efectiva de los servicios.

Asimismo, se aprecia una adaptación razonable a las particularidades de los distintos bloques incluidos en el Anexo II, evitando en numerosos casos enfoques genéricos y desarrollando soluciones específicas según la naturaleza de cada sistema. **Este aspecto resulta especialmente visible en los bloques de bases de datos, monitorización, streaming, videoconferencia y observabilidad.**

**No obstante, la propuesta presenta limitaciones relevantes en determinados ámbitos.** En particular, algunos bloques muestran un desarrollo arquitectónico claramente inferior al observado en las áreas principales, en la cuantificación de métricas, umbrales y criterios de aceptación de determinados servicios, pese a que la oferta sí aporta arquitecturas y procedimientos específicos para correo, cloud, LDAP, contenedores y MAX.

Asimismo, en algunos subproyectos se identifican referencias a futuras evoluciones o tecnologías pendientes de definición, lo que introduce un cierto nivel de incertidumbre sobre la arquitectura final de determinados componentes.

En consecuencia, la propuesta presenta una arquitectura técnicamente sólida, bien estructurada y con un elevado grado de coherencia, aunque sin alcanzar un nivel plenamente excelente debido a la heterogeneidad observada en determinados bloques del alcance.

**Nivel cualitativo:** ALTA
**Puntuación:** 1,50 sobre 2,00

### Grado de comprensión de los requisitos planteados — máximo 2,00 puntos

**La memoria técnica evidencia una comprensión amplia y detallada del alcance funcional y tecnológico del contrato.** A lo largo de la propuesta se identifican correctamente los distintos ámbitos de actuación definidos en el Anexo II, así como las relaciones existentes entre los múltiples sistemas que componen la plataforma EducaMadrid.

Esta comprensión se manifiesta especialmente en la capacidad de diferenciar tecnologías, necesidades operativas y mecanismos de gestión según la naturaleza de cada servicio. **La propuesta no se limita a reproducir los requisitos del pliego, sino que desarrolla soluciones específicas para bases de datos, monitorización, sistemas colaborativos, videoconferencia, automatización, gestión de identidades y entornos cloud.**

Asimismo, se aprecia una adecuada comprensión de los principales retos asociados a la operación de una plataforma de elevada complejidad, incluyendo aspectos como la escalabilidad, la automatización, la observabilidad, la continuidad del servicio y la gestión de grandes volúmenes de usuarios y sistemas.

**No obstante, el análisis detallado permite observar que esta comprensión no se traduce con la misma intensidad en todos los bloques funcionales.** Existen ámbitos donde el nivel de desarrollo técnico resulta claramente inferior, principalmente por la distinta cuantificación y profundidad operativa de determinados subproyectos, aunque todos los bloques cuentan con desarrollo específico. Estas limitaciones impiden considerar la cobertura de requisitos como completamente homogénea.

En conjunto, la propuesta demuestra un elevado conocimiento del entorno objeto del contrato y una comprensión significativamente superior a la observada en otras propuestas evaluadas, aunque sin alcanzar un nivel excelente debido a las carencias detectadas en determinados ámbitos concretos.

**Nivel cualitativo:** ALTA
**Puntuación:** 1,50 sobre 2,00

### Viabilidad técnica y operativa del proyecto — máximo 1,00 puntos

**Desde una perspectiva global, la propuesta presenta un nivel adecuado de viabilidad técnica y organizativa.** La existencia de arquitecturas definidas, procedimientos operativos, automatización, herramientas concretas y una visión coherente de los distintos sistemas permite considerar que existe una base razonable para la ejecución efectiva del servicio.

La utilización de tecnologías ampliamente implantadas en el sector, tales como Ansible, Prometheus, Grafana, Docker, Keycloak, JMeter o GitLab, contribuye a reforzar la credibilidad técnica del planteamiento y favorece su implementación en condiciones reales de explotación.

Adicionalmente, la propuesta incorpora mecanismos de automatización y observabilidad que permiten mejorar la eficiencia operativa y reducir riesgos asociados a la gestión manual de infraestructuras complejas.

**Sin embargo, la viabilidad global se ve parcialmente condicionada por determinadas carencias detectadas en algunos bloques específicos.** La cuantificación incompleta de resultados en determinados ámbitos de correo electrónico, LDAP, cloud, contenedores y MAX introduce una limitación de verificabilidad, sin negar el desarrollo específico acreditado en la oferta.

Asimismo, la falta recurrente de indicadores cuantificables, métricas operativas y objetivos medibles limita en algunos casos la posibilidad de verificar objetivamente el comportamiento esperado de las soluciones propuestas.

En conjunto, el proyecto puede considerarse viable, aunque con determinados elementos susceptibles de mejora.

**Nivel cualitativo:** ALTA
**Puntuación:** 0,65 sobre 1,00

### Metodología de trabajo aplicada — máximo 1,00 puntos

**La propuesta incorpora una metodología de trabajo alineada con prácticas ampliamente reconocidas dentro del ámbito tecnológico actual.** La memoria refleja una orientación clara hacia modelos DevOps, automatización continua, integración continua, gestión basada en servicios y mejora continua.

**Se describen mecanismos de automatización mediante Ansible, pipelines de integración continua, validaciones previas a producción, monitorización continua y modelos operativos basados en observabilidad.** Estos elementos aportan consistencia metodológica y favorecen una ejecución estructurada del servicio.

Asimismo, la metodología propuesta mantiene una adecuada coherencia con la naturaleza del contrato y con las necesidades operativas de EducaMadrid, especialmente en los ámbitos de sistemas, monitorización y mantenimiento evolutivo.

**No obstante, la metodología presenta una aplicación desigual entre los distintos bloques analizados.** Mientras que en algunas áreas se desarrolla con un elevado nivel de detalle, en otras se mantiene en un plano más conceptual sin llegar a definir procedimientos específicos de ejecución, control o validación.

Estas limitaciones impiden alcanzar un nivel excelente de valoración.

**Nivel cualitativo:** ALTA
**Puntuación:** 0,65 sobre 1,00

### Rendimiento previsible de las soluciones — máximo 1,00 puntos

**Uno de los aspectos más positivos de la propuesta se encuentra en la atención prestada al rendimiento, monitorización y observabilidad de los sistemas.** La memoria desarrolla diversos mecanismos orientados a garantizar el comportamiento adecuado de la plataforma mediante pruebas de carga, análisis de capacidad, monitorización continua y optimización del rendimiento.

Resulta especialmente relevante la definición de soluciones apoyadas en herramientas como Prometheus, Grafana, JMeter, Gatling y otras tecnologías específicamente orientadas al análisis del comportamiento de infraestructuras complejas.

Asimismo, la propuesta incluye actuaciones dirigidas al capacity planning, redistribución de cargas, optimización de bases de datos, pruebas de estrés y análisis de tendencias, lo que permite inferir una capacidad razonable para garantizar niveles adecuados de rendimiento en explotación.

No obstante, el análisis realizado evidencia una carencia recurrente de objetivos cuantificables, indicadores concretos y umbrales operativos, lo que limita la capacidad de verificar objetivamente los niveles de rendimiento esperados.

En consecuencia, el rendimiento previsto puede considerarse adecuadamente justificado, aunque sin alcanzar un nivel plenamente excelente.

**Nivel cualitativo:** ALTA
**Puntuación:** 0,75 sobre 1,00

### Satisfacción de los requisitos del Anexo II — máximo 8,00 puntos

La satisfacción de requisitos constituye el principal elemento de valoración de la solución técnica y representa más del cincuenta por ciento de la puntuación total asignada a este bloque.

**El análisis detallado desarrollado sobre los distintos bloques funcionales del Anexo II permite concluir que la propuesta de empresa_s presenta una cobertura amplia y técnicamente consistente de una parte muy significativa del alcance contractual.** La memoria desarrolla de forma detallada múltiples ámbitos críticos del servicio, incorporando herramientas concretas, procedimientos operativos, automatización, monitorización, integración continua y mecanismos de mejora continua.

Especialmente destacables resultan los bloques relacionados con bases de datos, monitorización, observabilidad, automatización y determinadas infraestructuras críticas, donde la propuesta alcanza niveles elevados de madurez técnica y demuestra una clara orientación hacia la operación real del servicio.

**Sin embargo, la evaluación también ha identificado una importante heterogeneidad en el nivel de desarrollo de los distintos subproyectos.** Existen ámbitos donde el grado de detalle disminuye significativamente o donde la cobertura resulta parcial. Las diferencias se concentran en la cuantificación y formalización de métricas, umbrales y criterios de aceptación entre subproyectos.

Asimismo, aunque se presentan mejoras y mecanismos de evolución tecnológica, en numerosos casos se echan en falta métricas cuantitativas, criterios objetivos o procedimientos completamente definidos que permitan maximizar la verificabilidad de las soluciones propuestas.

En consecuencia, la propuesta satisface los requisitos del pliego de forma claramente superior a la media y demuestra una capacidad técnica suficiente para la prestación del servicio, aunque sin llegar a un nivel excelente debido a las carencias señaladas.

**Nivel cualitativo:** ALTA
**Puntuación:** 6,00 sobre 8,00

### Resultado global de la solución técnica

| **Subcriterio**                | **Máximo** | **Nivel** | **Puntuación** |
| ------------------------------ | ---------: | --------- | -------------: |
| Arquitectura                   |       2,00 | ALTA      |           1,50 |
| Comprensión de los requisitos  |       2,00 | ALTA      |           1,50 |
| Viabilidad                     |       1,00 | ALTA      |           0,65 |
| Metodología                    |       1,00 | ALTA      |           0,65 |
| Rendimiento                    |       1,00 | ALTA      |           0,75 |
| Satisfacción de los requisitos |       8,00 | ALTA      |           6,00 |
| **TOTAL SOLUCIÓN TÉCNICA**     |  **15,00** |           |      **11,05** |

## EVALUACIÓN DE LA PLANIFICACIÓN DEL SERVICIO

### Consideraciones generales sobre la planificación

La planificación se valora como herramienta real de gestión: correspondencia con los subproyectos y entregables, secuencia, duración, dependencias, hitos, recursos y mecanismos de riesgo, contingencia, calidad y trazabilidad.

### Calendario de los trabajos a desarrollar — máximo 11,00 puntos

**La propuesta incorpora una planificación temporal estructurada y adaptada a la naturaleza de los servicios contemplados en el contrato.** El cronograma presentado permite identificar las principales líneas de trabajo, las actuaciones recurrentes y las actividades asociadas a la operación, evolución y mantenimiento de los distintos sistemas integrados en EducaMadrid.

**La planificación mantiene una adecuada coherencia con la estructura general de la propuesta técnica y refleja una organización razonable de las actividades a lo largo de la duración del contrato.** Asimismo, se aprecia una relación lógica entre las diferentes líneas de actuación, particularmente en aquellos ámbitos relacionados con automatización, observabilidad, despliegues evolutivos, monitorización y mantenimiento continuo de infraestructuras.

Otro aspecto positivo es la alineación general de la planificación con los principios operativos descritos en la memoria, incluyendo la realización de actuaciones de mantenimiento preventivo, revisiones periódicas, optimización continua y ejecución de determinadas actividades durante ventanas de menor impacto operativo.

**No obstante, el análisis detallado evidencia que el cronograma no alcanza el nivel de profundidad exigible para una valoración excelente.** En particular, se observa una limitada definición de hitos intermedios, entregables verificables y dependencias explícitas entre actividades. Tampoco se desarrolla con suficiente detalle la planificación específica de numerosos subproyectos incluidos en el Anexo II, lo que dificulta establecer una trazabilidad completa entre el cronograma y la totalidad del alcance contractual.

Asimismo, aunque la propuesta refleja una planificación razonablemente sólida, no se identifican mecanismos avanzados de planificación asociados a escenarios alternativos, redistribución de cargas o replanificación ante contingencias complejas, elementos especialmente relevantes en contratos con una elevada complejidad tecnológica y operativa.

En consecuencia, la planificación presentada puede considerarse superior a la media y claramente utilizable como instrumento de gestión, aunque presenta margen de mejora para alcanzar niveles de excelencia.

**Nivel cualitativo:** ALTA
**Puntuación:** 7,50 sobre 11,00

### Análisis de riesgos del proyecto — máximo 1,00 puntos

**La propuesta incorpora una identificación razonable de riesgos asociados a la operación de infraestructuras complejas, mantenimiento de servicios críticos, disponibilidad de sistemas, evolución tecnológica y continuidad de la prestación del servicio.** El enfoque planteado se encuentra alineado con la naturaleza del contrato y evidencia la conciencia del licitador respecto a los principales factores que pueden afectar a la ejecución del proyecto.

Asimismo, la memoria refleja una orientación preventiva basada en monitorización continua, automatización, observabilidad y gestión proactiva de incidencias, lo que contribuye a reducir parcialmente la exposición a determinados riesgos operativos.

**Sin embargo, el nivel de formalización del análisis resulta limitado.** No se desarrolla una matriz completa de riesgos que contemple probabilidad, impacto, criticidad, responsable, mecanismos de mitigación y procedimientos de seguimiento para cada escenario identificado. Tampoco se incorporan indicadores objetivos que permitan monitorizar su evolución durante la ejecución del contrato.

Esta circunstancia limita la madurez del análisis y reduce su utilidad como herramienta formal de gobierno del servicio.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,50 sobre 1,00

### Plan de gestión de contingencias — máximo 1,00 puntos

**La propuesta contempla medidas orientadas a garantizar la continuidad del servicio mediante mecanismos de redundancia, automatización, replicación, alta disponibilidad, recuperación ante fallos y procedimientos de actuación sobre sistemas críticos.** Estos elementos aportan una base razonablemente sólida para afrontar situaciones de incidencia o degradación del servicio.

Se aprecia además una orientación hacia la resiliencia operativa derivada del uso de arquitecturas distribuidas, monitorización continua y automatización de procesos recurrentes, aspectos que contribuyen positivamente a la gestión de contingencias.

**No obstante, el plan presentado mantiene un carácter principalmente integrado dentro de la solución técnica general y no se desarrolla como un procedimiento independiente y estructurado de gestión de contingencias.** En particular, no se identifican escenarios específicos de fallo, secuencias detalladas de actuación, tiempos objetivos de recuperación, matrices de escalado ni responsables designados para las distintas situaciones contempladas.

La consecuencia es un modelo razonablemente coherente desde el punto de vista conceptual, aunque insuficientemente formalizado desde la perspectiva operativa.

**Nivel cualitativo:** MEDIA
**Puntuación:** 0,50 sobre 1,00

### Plan de gestión de la calidad del servicio — máximo 1,00 puntos

**La propuesta evidencia una orientación clara hacia la calidad del servicio mediante la incorporación de automatización, validaciones previas al despliegue, monitorización continua, observabilidad, análisis de rendimiento y mejora continua.** Estos elementos configuran un modelo operativamente alineado con las buenas prácticas habituales en la gestión de servicios tecnológicos complejos.

Particularmente relevante resulta la integración de herramientas de monitorización y pruebas de rendimiento, así como la utilización de mecanismos DevOps que permiten introducir controles de calidad durante diferentes fases del ciclo de vida de los sistemas.

**Sin embargo, el plan de calidad presenta igualmente ciertas limitaciones.** No se identifican de forma suficientemente detallada los indicadores concretos de calidad, los cuadros de mando asociados, las métricas objetivo ni los procedimientos formales de revisión periódica del cumplimiento de los niveles de servicio.

Esta falta de definición cuantitativa impide disponer de un sistema completamente verificable de gestión de la calidad, aunque el enfoque general de la propuesta puede considerarse adecuado.

**Nivel cualitativo:** ALTA
**Puntuación:** 0,65 sobre 1,00

### Trazabilidad del servicio — máximo 1,00 puntos

La propuesta incorpora diversos mecanismos que favorecen la trazabilidad de las actuaciones realizadas sobre la plataforma. **Entre ellos destacan la utilización de herramientas de gestión, la integración de sistemas de monitorización, la centralización de información operativa, el uso de mecanismos de automatización y la existencia de procesos orientados al control de cambios y a la gestión de configuraciones.**

Asimismo, la presencia de elementos como CMDB, observabilidad, registros operativos y automatización contribuye positivamente a la capacidad de seguimiento de las actuaciones desarrolladas durante la ejecución del servicio.

No obstante, el análisis realizado pone de manifiesto que la memoria no desarrolla completamente un modelo formal de trazabilidad extremo a extremo que permita relacionar de forma directa requisitos, tareas, entregables, incidencias, cambios y resultados medibles asociados a cada uno de los subproyectos incluidos en el Anexo II.

Del mismo modo, la propuesta no define una metodología detallada de gobierno de la información que permita reconstruir de forma sistemática la ejecución completa del servicio a lo largo de todo el ciclo de vida contractual.

En consecuencia, la trazabilidad presentada puede considerarse adecuada, aunque mejorable desde un punto de vista metodológico y de control.

**Nivel cualitativo:** ALTA
**Puntuación:** 0,65 sobre 1,00

### Resultado global de la planificación

| **Subcriterio**                     | **Máximo** | **Nivel** | **Puntuación** |
| ----------------------------------- | ---------: | --------- | -------------: |
| Calendario y planificación temporal |      11,00 | ALTA      |           7,50 |
| Análisis de riesgos                 |       1,00 | MEDIA     |           0,50 |
| Plan de contingencias               |       1,00 | MEDIA     |           0,50 |
| Plan de calidad                     |       1,00 | ALTA      |           0,65 |
| Trazabilidad                        |       1,00 | ALTA      |           0,65 |
| **TOTAL PLANIFICACIÓN**             |  **15,00** |           |       **9,80** |

## RESULTADO FINAL CONSOLIDADO

| **Bloque**                 | **Puntuación máxima** | **Puntuación obtenida** |
| -------------------------- | --------------------: | ----------------------: |
| Solución técnica ofertada  |                 15,00 |                   11,05 |
| Planificación del servicio |                 15,00 |                    9,80 |
| **PUNTUACIÓN FINAL**       |             **30,00** |               **20,85** |

### Interpretación de la puntuación

La puntuación refleja una oferta técnicamente adecuada y viable, con fortalezas claras en arquitectura, automatización, observabilidad y operación. La heterogeneidad entre bloques y la falta de métricas y procedimientos plenamente formalizados impiden alcanzar el nivel excelente.

## CONCLUSIONES FINALES Y PROPUESTA

### Conclusiones globales de la evaluación técnica

La propuesta presenta una cobertura amplia y una base técnica sólida, con arquitecturas, procedimientos y herramientas concretas en bases de datos, monitorización, observabilidad, automatización y seguridad. El uso de Ansible, Prometheus, Grafana, JMeter, Docker, Keycloak y GitLab refuerza su viabilidad. El desarrollo cubre también de forma específica MAX y los módulos de inyección de correo; persiste, no obstante, una cuantificación incompleta de métricas, umbrales y criterios de aceptación en distintos subproyectos.

### Conclusiones sobre la solución técnica

La propuesta desarrolla de forma específica los trece bloques del Anexo II, incluidos MAX, la inyección directa de correo y la migración entre CPD. La principal limitación transversal es la falta de indicadores cuantificados, valores objetivo y criterios de aceptación completamente formalizados.

### Conclusiones sobre la planificación del servicio

El cronograma es coherente y utilizable, aunque no detalla de forma completa hitos, entregables y dependencias. Los planes de riesgos y contingencias requieren mayor formalización; calidad y trazabilidad son adecuados, pero mejorables mediante indicadores cuantificados.

### Justificación de la valoración

La solución técnica obtiene 11,05 puntos y la planificación 9,80 puntos. La suma de 20,85 puntos mantiene la correspondencia con los niveles cualitativos asignados y con las fortalezas, carencias y evidencias desarrolladas en el informe.

### Aplicación del umbral mínimo y propuesta final

La propuesta obtiene una puntuación de **20,85 puntos sobre 30** en los criterios sujetos a juicio de valor.

El umbral mínimo exigido es de **15 puntos sobre 30**. Por tanto, la oferta **ALCANZA** el nivel mínimo de calidad técnica establecido.

En consecuencia, procede proponer la **continuación de la oferta en el procedimiento de adjudicación**.

### Garantía de igualdad de trato y objetividad

La evaluación aplica los mismos criterios, niveles de exigencia y reglas de puntuación a ambos licitadores, y se fundamenta exclusivamente en el contenido de cada oferta y en la documentación reguladora del procedimiento.

## ANEXO. RELACIÓN DE PROYECTOS Y GRADO DE DESARROLLO DE LA PROPUESTA TÉCNICA

### Objeto y criterios de clasificación

El presente anexo resume, de manera sistemática, el grado de desarrollo de la propuesta técnica para cada proyecto o subproyecto del Anexo II. Su finalidad es aportar trazabilidad documental al análisis, sin sustituir la motivación cualitativa del informe ni producir por sí solo una traslación automática a la puntuación final.

Se aplican tres grados de desarrollo: **NO INCLUIDA**, cuando no existe una solución concreta; **INSUFICIENTE**, cuando el contenido es genérico o carece de arquitectura, procesos, herramientas o mecanismos de implementación suficientes; y **SUFICIENTE**, cuando existe una solución concreta y evaluable.

De forma separada se indican los errores técnicos relevantes, las propuestas de mejora sin valor añadido real (**PM**) y las propuestas con valor añadido verificable (**VA**).

El **grado de desarrollo** y el **nivel cualitativo** son dimensiones relacionadas pero no equivalentes: el primero comprueba si existe una solución concreta y evaluable; el segundo pondera su calidad, completitud y mejoras. Por ello, un desarrollo puede ser **SUFICIENTE** y recibir nivel **BAJA** si apenas alcanza el requisito. El valor numérico del CSV se deriva únicamente del nivel cualitativo mediante la escala **MUY BAJA=0, BAJA=2, MEDIA=5, ALTA=8 y EXCELENTE=10**.

### Tablas de subproyectos

#### BD — Mantenimiento y mejora de entornos de Bases de Datos (BD)

| **Subproyecto**                                                                                 | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                       |
| ----------------------------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ------------------------------------------- |
| BD1 — Mantenimiento y mejora de entornos de Bases de Datos MariaDB y Proxy SQL avanzado | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para BD1. |
| BD2 — Mantenimiento y optimización proactiva de las bases de datos de toda la plataforma | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para BD2. |
| BD3 — Mantenimiento de las diferentes Bases de Datos de gestión de la configuración de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para BD3. |
| BD4 — Mantenimiento de las bases de datos de las Aulas Virtuales | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para BD4. |
| BD5 — Mantenimiento de disparadores y Foreign Data Wrappers en los entornos “Portal” y “LDAP Plano” | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para BD5. |
| BD6 — Implementación y Mantenimiento de las Bases de Datos necesarias en entornos de Microservicios | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para BD6. |

#### MON — Monitorización, testeo y pruebas de rendimiento (MON)

| **Subproyecto**                                                                           | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                     |
| ----------------------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ----------------------------------------- |
| MON1 — Mantenimiento periódico del almacenamiento de los centros | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para MON1. |
| MON2 — Realización periódica de pruebas de estrés en diferentes entornos de la plataforma | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para MON2. |
| MON3 — Mantener actualizado el sistema de monitorización y estadísticas de uso | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para MON3. |
| MON4 — Mantener actualizado el sistema de monitorización y estadísticas de servicios basados en IA | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para MON4. |

#### UPD — Actualización de servicios existentes (UPD)

| **Subproyecto**                                                                                   | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                    |
| ------------------------------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ---------------------------------------- |
| UPD1 — Mantenimiento y mejora de los sistemas de videoconferencias de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD1. |
| UPD2 — Mantenimiento y mejora del sistema secundario de Videoconferencias con opción de grabación | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD2. |
| UPD3 — Mantenimiento y mejora de la herramienta Mattermost | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD3. |
| UPD4 — Mantenimiento y mejora de la solución Kanban | SUFICIENTE              | VA                         | NO                          | Wekan con migración, preproducción, reversión y contenedores. |
| UPD5 — Mantenimiento y mejora de la solución GitLab | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD5. |
| UPD6 — Mantenimiento y mejora de la solución LimeSurvey | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD6. |
| UPD7 — Mantenimiento y mejora de SonarQube | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD7. |
| UPD8 — Mantenimiento y mejora de Redmine | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD8. |
| UPD9 — Mantenimiento y configuración de Wowza Streaming Engine. | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD9. |
| UPD10 — Mantenimiento y gestión de contenidos AbiesWeb | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD10. |
| UPD11 — Actualización, Mantenimiento y gestión de contenidos de Abies+ | SUFICIENTE              | VA                         | NO                          | Arquitectura, alta disponibilidad y actualización automatizada de Abies+. |
| UPD12 — Implementación, mantenimiento y mejora de Empieza | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD12. |
| UPD13 — mantenimiento y mejora del sistema de gestión de la configuración | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD13. |
| UPD14 — Mantenimiento, Actualización y mejora de la solución de contenedores | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD14. |
| UPD15 — Mantenimiento de gestión y decomisionado de servidores | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para UPD15. |

#### CLO — Cloud (CLO)

| **Subproyecto**                                                                              | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**               |
| -------------------------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ----------------------------------- |
| CLO1 — Mantenimiento del servicio de la nube de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para CLO1. |
| CLO2 — Mantenimiento y adaptación del sistema de almacenamiento temporal de datos de la nube | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para CLO2. |
| CLO3 — Mantenimiento del sistema de edición en línea de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para CLO3. |

#### OTR — Otros desarrollos (OTR)

| **Subproyecto**                                                                              | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                 |
| -------------------------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ------------------------------------- |
| OTR1 — Mantenimiento y mejora del sistema de autentificación centralizada Single Sign On (SSO) | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para OTR1. |
| OTR2 — Mantenimiento, configuración y gestión 2FA en el servicio de Single Sign On (SSO) | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para OTR2. |
| OTR3 — Mantenimiento y mejora de herramientas de automatización de tareas | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para OTR3. |
| OTR4 — Mantenimiento y mejora de un sistema de gestión y análisis de datos mediante el stack de Elastic | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para OTR4. |
| OTR5 — Mantenimiento y mejora de la herramienta de flujos de trabajo | SUFICIENTE              | VA                         | NO                          | Flujos integrados con GitLab, CMDB, monitorización y SSO. |
| OTR6 — Mantenimiento y mejora del Portal CAU | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para OTR6. |
| OTR7 — Mantenimiento y evolución de servicios de Inteligencia Artificial para la plataforma EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para OTR7. |

#### COR — Correo electrónico (COR)

| **Subproyecto**                                                                       | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**            |
| ------------------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | -------------------------------- |
| COR1 — Mantenimiento y mejora de los sistemas de control de envíos de correo | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR1. |
| COR2 — Mantenimiento automatizado de listas de distribución de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR2. |
| COR3 — Mantenimiento y mejora del sistema de activación y gestión de cuotas de correo | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR3. |
| COR4 — Mantenimiento y mejora de las herramientas relacionadas con el control del spam | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR4. |
| COR5 — Mantenimiento de buzones de correo | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR5. |
| COR6 — Mantenimiento y mejora continua de la seguridad del sistema de correo | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR6. |
| COR7 — Actualización y mejora continua de la infraestructura en la que se basa el sistema de correo | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR7. |
| COR8 — Ampliación del número de servidores Mailbox Server | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para COR8. |
| COR9 — Implementación y mejora de un módulo receptor de inyección directa para la infraestructura de transporte de correo | SUFICIENTE              | VA                         | NO                          | Inyección QMQP en spool, no intrusiva, persistente y reversible. |
| COR10 — Mantenimiento y soporte del módulo de inyección directa de correo | SUFICIENTE              | VA                         | NO                          | Soporte qmqpd con pruebas, observabilidad, rollback y documentación. |

#### MAX — Sistema Operativo MAX (MAX)

| **Subproyecto**                                                                                | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**                  |
| ---------------------------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | -------------------------------------- |
| MAX1 — Mantenimiento y actualización de MAX de forma presencial en centros de forma regular | SUFICIENTE              | VA                         | NO                          | Intervención planificada, imágenes certificadas y diagnóstico remoto. |
| MAX2 — Mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones | SUFICIENTE              | VA                         | NO                          | Construcción CI/CD reproducible y trazable. |
| MAX3 — Mantenimiento de aplicaciones basadas en MAX | SUFICIENTE              | VA                         | NO                          | Certificación y control de vulnerabilidades de aplicaciones. |
| MAX4 — Lanzamiento de distribuciones de MAX “Full Equip” anualmente | SUFICIENTE              | VA                         | NO                          | Pipeline, testing y trazabilidad de versiones Full Equip. |
| MAX5 — Lanzamiento de distribuciones de “MAX lite” y/o “max gestión” anualmente | SUFICIENTE              | VA                         | NO                          | Distribuciones Lite y Gestión diferenciadas y optimizadas. |
| MAX6 — Integración de aplicaciones externas a los repositorios oficiales | SUFICIENTE              | VA                         | NO                          | Catálogo, pruebas, seguimiento de CVE y empaquetado. |
| MAX7 — Mantenimiento y mejora del servidor de gestión accesos remotos | SUFICIENTE              | VA                         | NO                          | Acceso remoto centralizado, cifrado y trazable. |
| MAX8 — Soporte de asistencia telefónica y remota para incidencias de entornos MAX | SUFICIENTE              | VA                         | NO                          | Soporte priorizado con base de conocimiento y métricas. |
| MAX9 — Asistencia presencial en los diferentes eventos MAX | SUFICIENTE              | VA                         | NO                          | Soporte de eventos planificado y reutilizable. |
| MAX10 — Soporte presencial en eventos especiales (MAX Install Party) | SUFICIENTE              | VA                         | NO                          | Install Party con imágenes, scripts y despliegue automatizado. |
| MAX11 — Gestión, mantenimiento y actualización de equipos MAX en remoto | SUFICIENTE              | VA                         | NO                          | Inventario, actualizaciones y monitorización remota. |
| MAX12 — Instalación y configuración de dispositivos solicitadas por los centros educativos | SUFICIENTE              | VA                         | NO                          | Catálogo de compatibilidad y scripts de instalación. |
| MAX13 — Mantenimiento y soporte del servidor de repositorio individual para centros educativos | SUFICIENTE              | VA                         | NO                          | Repositorio Migasfree multicentro con políticas y auditoría. |
| MAX14 — Herramienta de gestión centralizada de maquetas de MAX | SUFICIENTE              | VA                         | NO                          | Maquetas versionadas y gobernadas mediante Migasfree. |

#### AV — Aulas Virtuales (AV)

| **Subproyecto**                                                                                  | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**          |
| ------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------- | --------------------------- | ------------------------------ |
| AV1 — Actualización y comprobación periódicas de servidores físicos y virtuales de BBDD de los entornos de aulas virtuales | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para AV1. |
| AV2 — Mantenimiento de los servidores virtuales FrontEnd de los entornos de aulas virtuales | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para AV2. |
| AV3 — Despliegue periódico de nuevos grupos de aulas virtuales y ampliación de los actuales | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para AV3. |
| AV4 — Redistribución periódica de los NFS de datos de las aulas virtuales | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para AV4. |

#### POR — Servicio de LDAP y Portal Educativo (POR)

| **Subproyecto**                                                         | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**          |
| ----------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ------------------------------ |
| POR1 — Ampliación periódica del sistema de esclavos LDAP de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para POR1. |
| POR2 — Migración del sistema LDAP máster de EducaMadrid | SUFICIENTE              | VA                         | NO                          | LDAP con LDAPS, replicación, HA, preproducción y copias. |

#### SEG — Seguridad (SEG)

| **Subproyecto**                                                        | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**               |
| ---------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ----------------------------------- |
| SEG1 — Mantenimiento y mejora del sistema de control de cambios en DNS | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG1. |
| SEG2 — Mantenimiento y mejora de un LDAP Máster independiente para usuarios privilegiados | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG2. |
| SEG3 — Gestión, mantenimiento e implantación anual de los certificados de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG3. |
| SEG4 — Gestión y mantenimiento periódico de dominios DNS | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG4. |
| SEG5 — Análisis y corrección de vulnerabilidades | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG5. |
| SEG6 — Gestión, mantenimiento y ajuste de la herramienta para la detección de intrusiones, monitorización de la integridad, análisis de logs y respuesta ante incidentes. | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG6. |
| SEG7 — Realización de auditorías internas de aplicaciones | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG7. |
| SEG8 — Realización de auditorías internas continuas de los sistemas | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG8. |
| SEG9 — Mantenimiento y uso de logs centralizados | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG9. |
| SEG10 — Implementación y mantenimiento de claves RSA unificadas | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG10. |
| SEG11 — Asistencia y soporte presencial en los diferentes eventos de Ciberseguridad de EducaMadrid | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para SEG11. |

#### CON — Automatización y contenedores (CON)

| **Subproyecto**                                                      | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**             |
| -------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | --------------------------------- |
| CON1 — Mantenimiento y mejora del sistema de gestión de contenedores | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para CON1. |
| CON2 — Mantenimiento y mejora de los scripts y sistemas de automatización de tareas | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para CON2. |
| CON3 — Mantenimiento y mejora del sistema auxiliar de automatización | SUFICIENTE              | VA                         | NO                          | APIs REST con observabilidad, CI/CD, reintentos y auditoría. |

#### MIG — Gestión de la migración de servidores entre CPDs (MIG)

| **Subproyecto**                                                             | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**            |
| --------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | -------------------------------- |
| MIG1 — Coordinación y planificación de la revisión de los entornos migrados | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para MIG1. |
| MIG2 — Fases preparatorias y planificación técnica de la migración | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para MIG2. |
| MIG3 — Preparación de servidores y documentación de sistemas | SUFICIENTE              | VA                         | NO                          | Fichas, procedimientos, recopilación automatizada y checklists. |
| MIG4 — verificación de la migración | SUFICIENTE              | VA                         | NO                          | Comparación pre/post, seguimiento y validación por capas. |
| MIG5 — Mantenimiento y soporte tras la migración | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para MIG5. |

#### IA — Inteligencia Artificial (IA)

| **Subproyecto**                                                           | **Grado de desarrollo** | **VA** | **Error** | **Observación breve**         |
| ------------------------------------------------------------------------- | ----------------------- | -------------------------- | --------------------------- | ----------------------------- |
| IA1 — EVALUAR el rendimiento de los modelos seleccionados | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para IA1. |
| IA2 — Ingeniería de Prompts adaptados para cada servicio | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para IA2. |
| IA3 — Testeo de los guardarraíles para el entorno educativo | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para IA3. |
| IA4 — Evaluar Posibilidades de Integración en Distintos Aplicativos | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para IA4. |
| IA5 — Evaluación de Capacidades de Respuesta y Límites por Usuario | SUFICIENTE              | VA                         | NO                          | Mejora específica trazada en la oferta para IA5. |

### Resumen cuantitativo del anexo

#### Grado de desarrollo

| **Clasificación**                    | **Número de proyectos** | **Porcentaje** |
| ------------------------------------ | ----------------------: | -------------: |
| No incluidos                         |                       0 |         0,00 % |
| Desarrollo insuficiente o deficiente |                       0 |         0,00 % |
| Desarrollo suficiente                |                      89 |       100,00 % |
| **TOTAL DE PROYECTOS**               |                  **89** |   **100,00 %** |

#### Indicadores adicionales

Los indicadores no son excluyentes entre sí ni respecto del grado de desarrollo.

| **Indicador**                                  | **Número de proyectos** | **Porcentaje sobre el total** |
| ---------------------------------------------- | ----------------------: | ----------------------------: |
| Con errores técnicos relevantes                |                       0 |                        0,00 % |
| Con propuesta de mejora sin valor añadido real |                       0 |                        0,00 % |
| Con propuesta de mejora con valor añadido real |                      89 |                      100,00 % |

### Conclusión del anexo

La propuesta desarrolla de forma específica los trece bloques del Anexo II, incluidos MAX, la inyección directa de correo y la migración entre CPD. La principal limitación transversal es la falta de indicadores cuantificados, valores objetivo y criterios de aceptación completamente formalizados.
