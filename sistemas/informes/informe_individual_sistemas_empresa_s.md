# INTRODUCCIÓN

## Objeto del informe

**El presente informe tiene por objeto la evaluación técnica de la propuesta presentada por la empresa empresa_s** en el procedimiento relativo al desarrollo evolutivo y correctivo del portal educativo, LDAP, cloud, sistema operativo MAX y otros sistemas de la plataforma EducaMadrid. La evaluación se realiza conforme a los criterios establecidos en el Documento de Invitación, con especial atención a los definidos en el apartado 7.2.2 relativos a criterios sujetos a juicio de valor.

El análisis tiene como finalidad determinar el nivel real de adecuación de la propuesta tanto en términos de calidad técnica como de viabilidad operativa, considerando la capacidad efectiva del licitador para ejecutar el servicio en un entorno de alta complejidad tecnológica y criticidad operativa como el descrito en el pliego.

## Alcance de la evaluación

**La evaluación comprende el análisis integral de la memoria técnica presentada por empresa_s, incluyendo tanto la solución técnica como la planificación del servicio.** Se ha abordado de forma específica el grado de cobertura de los requisitos contenidos en el Anexo II mediante una evaluación detallada de los 89 subproyectos definidos, agrupados en 13 bloques funcionales.

El enfoque adoptado se basa en la verificación de la correspondencia real entre los requisitos del pliego y las soluciones propuestas, identificando el nivel de concreción técnica, la existencia de procedimientos operativos, la definición de herramientas concretas, la incorporación de métricas verificables y la coherencia global de la propuesta.

Asimismo, se ha analizado la consistencia entre el planteamiento teórico descrito en la memoria y su posible aplicación en un entorno real de producción.

## Contexto técnico del servicio

**La plataforma EducaMadrid constituye un ecosistema altamente complejo que integra múltiples servicios interdependientes, entre los que se incluyen portales web, sistemas de aula virtual, servicios cloud, herramientas colaborativas, correo electrónico y soluciones basadas en inteligencia artificial.** Este entorno se caracteriza por la coexistencia de un elevado número de sistemas heterogéneos, con dependencias técnicas cruzadas y requisitos estrictos de disponibilidad, rendimiento y seguridad.

La propia memoria de empresa_s reconoce este contexto al definir su propuesta como un modelo de operación tecnológica avanzada orientado a la continuidad del servicio, la automatización y la escalabilidad, planteando una arquitectura modular multinivel con integración transversal de componentes como SSO, LDAP, monitorización y automatización CI/CD.

La magnitud del entorno, con miles de bases de datos y un volumen elevado de usuarios concurrentes, exige soluciones no solo técnicamente correctas, sino plenamente operativas, verificables y escalables.

## Metodología de evaluación

El análisis se ha realizado mediante la revisión detallada de la memoria técnica, identificando para cada subproyecto el grado de desarrollo técnico de la solución propuesta, su alineación con los requisitos del pliego y su viabilidad en condiciones reales de explotación.

Se ha prestado especial atención a la verificabilidad de la solución, entendida como la capacidad de demostrar objetivamente cómo se ejecutará el servicio mediante procedimientos, herramientas, métricas y mecanismos de control.

Una vez completado el análisis pormenorizado de los subproyectos, se procederá a una evaluación global conforme a los criterios establecidos en el apartado 7.2.2 del Documento de Invitación.

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

### BLOQUE BD — BASES DE DATOS

## BD1 — Mantenimiento y mejora de entornos de Bases de Datos MariaDB y ProxySQL avanzado

**El subproyecto BD1 define un conjunto de requisitos orientados a la operación avanzada de entornos MariaDB en configuración clusterizada, junto con el uso de ProxySQL como elemento de balanceo y gestión del tráfico.** Este tipo de entornos requiere una comprensión profunda de la replicación de bases de datos, la optimización de consultas, la gestión del tráfico de lectura y escritura y la monitorización avanzada del sistema.

La propuesta presentada por empresa_s desarrolla este subproyecto con un nivel significativo de concreción técnica, incorporando aspectos como la monitorización de clusters MariaDB, la supervisión de la replicación, el control de latencias y concurrencia, así como la optimización de consultas SQL mediante ajustes específicos de parámetros como InnoDB. **Asimismo, se incluye la gestión avanzada de ProxySQL, contemplando el balanceo de carga y la gestión de failover, lo que evidencia una comprensión adecuada del funcionamiento de este tipo de arquitecturas.**

**Adicionalmente, la propuesta incorpora elementos de automatización y observabilidad, así como el uso de herramientas específicas como ClusterControl, lo que aporta un nivel adicional de credibilidad técnica a la solución.** Este enfoque refleja una orientación hacia la operación real en entornos críticos, integrando capacidades de monitorización, automatización y mejora continua.

**No obstante, el análisis técnico permite identificar ciertas carencias.** En particular, no se definen de forma explícita métricas concretas, umbrales de funcionamiento ni objetivos de rendimiento asociados a los sistemas, lo que limita parcialmente la verificabilidad de la solución. Asimismo, la descripción de las arquitecturas de replicación y de los procedimientos de failover no alcanza un nivel de detalle completamente operativo.

En términos generales, la propuesta responde de forma sólida al requisito, desarrollando una solución técnicamente coherente, aunque con un margen de mejora en la definición de indicadores cuantificables y procedimientos detallados.

**Valoración cualitativa: Alta**

## BD2 — Mantenimiento y optimización proactiva de las bases de datos de toda la plataforma

**El subproyecto BD2 se centra en la optimización continua de un entorno compuesto por miles de bases de datos, incluyendo la mejora de consultas, la gestión de backups, la seguridad de las conexiones y el mantenimiento preventivo en periodos de baja actividad.** Se trata de un requisito especialmente exigente desde el punto de vista operativo debido a la escala del sistema.

**La propuesta de empresa_s aborda este subproyecto mediante un planteamiento que incorpora automatización, optimización y control del rendimiento.** En particular, se describen mecanismos de supervisión automatizada, optimización de consultas SQL, gestión de índices y reorganización de datos, así como la redistribución de carga entre sistemas. Asimismo, se incluye la automatización de copias de seguridad y la validación de restauraciones, junto con la auditoría de accesos y el endurecimiento de configuraciones de seguridad.

**Uno de los aspectos más relevantes de la propuesta es su adaptación explícita a un entorno de miles de bases de datos, lo que demuestra una comprensión adecuada de la escala del sistema.** El enfoque planteado introduce un componente significativo de automatización, lo que resulta coherente con la necesidad de operar en un entorno de alta complejidad.

Sin embargo, se detectan ciertas limitaciones en la identificación de herramientas específicas utilizadas para estas tareas, así como en la definición de ventanas de mantenimiento claramente estructuradas en periodos no lectivos, aspecto que es relevante en el contexto del servicio educativo.

En conjunto, la propuesta presenta una cobertura amplia y técnicamente consistente, demostrando una capacidad adecuada para abordar la optimización proactiva del entorno.

**Valoración cualitativa: Alta**

## BD3 — Mantenimiento de las bases de datos de gestión de la configuración de EducaMadrid

El subproyecto BD3 exige el desarrollo y evolución de un sistema de gestión de la configuración que permita representar relaciones entre activos, automatizar la carga de información y garantizar la coherencia del sistema.

**La propuesta de empresa_s plantea una evolución de la CMDB orientada a la integración de activos físicos y lógicos, incorporando procesos ETL para la carga de datos y promoviendo la automatización mediante herramientas como Ansible.** Asimismo, se incluyen mecanismos de sincronización continua entre sistemas y controles orientados a garantizar la calidad del dato, incluyendo validación de información y detección de inconsistencias.

**Este enfoque refleja una comprensión adecuada del papel de la CMDB como elemento central en la gestión de la infraestructura, incorporando además una visión transversal que integra distintos componentes del ecosistema.** La apuesta por la automatización y la sincronización continua constituye un elemento positivo que favorece la mantenibilidad del sistema.

**No obstante, se observa que la propuesta no desarrolla en profundidad la herramienta concreta indicada en el pliego, lo que limita en cierta medida la alineación completa con los requisitos específicos.** Asimismo, no se identifican métricas cuantificables de calidad del dato que permitan evaluar objetivamente el estado de la CMDB.

En conjunto, la solución es coherente y demuestra un nivel adecuado de madurez técnica, aunque con ciertas carencias en la especificación de herramientas y métricas.

**Valoración cualitativa: Alta**

## BD4 — Mantenimiento de las bases de datos de las Aulas Virtuales

Este subproyecto implica la gestión de un entorno de alta complejidad basado en miles de bases de datos PostgreSQL, incluyendo el análisis de carga, la redistribución de información y la optimización del sistema.

**La propuesta de empresa_s aborda este requisito con un planteamiento diferenciado respecto a otros sistemas de bases de datos, incorporando herramientas y mecanismos específicos de PostgreSQL.** En este sentido, se describen actuaciones orientadas a la redistribución dinámica de carga, el ajuste fino del rendimiento mediante técnicas de tuning, la optimización de entornos clusterizados y la automatización de copias de seguridad, incluyendo la validación de restauraciones.

**Un aspecto especialmente destacable es que la propuesta no reutiliza enfoques genéricos, sino que adapta el diseño técnico a la tecnología concreta, lo que demuestra un nivel alto de comprensión del entorno.** Asimismo, se introducen elementos de escalabilidad como plantillas estandarizadas y modelos de análisis histórico.

Las carencias detectadas se centran en la falta de identificación de herramientas concretas asociadas a PostgreSQL y en la ausencia de criterios objetivos que determinen los procesos de redistribución de carga.

En términos globales, la cobertura del requisito es amplia y técnicamente consistente.

**Valoración cualitativa: Alta**

## BD5 — Mantenimiento de disparadores y Foreign Data Wrappers

El subproyecto BD5 se centra en la sincronización de información entre sistemas mediante el uso de triggers y Foreign Data Wrappers, lo que implica garantizar la integridad y consistencia de los datos entre diferentes plataformas.

La propuesta de empresa_s responde de forma específica a este requisito, desarrollando aspectos como la optimización de disparadores y funciones, la gestión de FDW y la implementación de scripts de sincronización entre sistemas. **Asimismo, se incorporan mecanismos de monitorización de integridad y alertas de desincronización, lo que permite identificar desviaciones en el comportamiento del sistema.**

**La adecuación de la propuesta al requisito es elevada, destacando especialmente la orientación a la trazabilidad mediante el uso de logs y mecanismos de validación.** Este enfoque contribuye a garantizar la coherencia de los datos en un entorno distribuido.

No obstante, la propuesta presenta un nivel limitado de detalle en lo relativo a las estrategias concretas de uso de FDW y los mecanismos de control de consistencia, lo que reduce parcialmente la profundidad técnica del planteamiento.

En conjunto, la solución es adecuada y demuestra una comprensión clara del requisito, aunque con margen de mejora en la definición técnica detallada.

**Valoración cualitativa: Alta**

## BD6 — Implementación y mantenimiento de bases de datos en entornos de microservicios

El subproyecto BD6 introduce un contexto tecnológico basado en arquitecturas de microservicios y metodologías DevOps, lo que requiere una adaptación de los sistemas de bases de datos a entornos distribuidos y contenerizados.

**La propuesta de empresa_s incorpora de forma explícita tecnologías como Docker, así como la utilización de pipelines de integración continua, archivos de definición de despliegue y mecanismos de automatización asociados al ciclo de vida de los servicios.** Asimismo, se contemplan aspectos como la persistencia de datos, la alta disponibilidad y la validación en entornos de preproducción.

**Este enfoque demuestra una orientación clara hacia arquitecturas modernas y una comprensión adecuada de los principios DevOps.** La inclusión de mecanismos de automatización y validación previa a producción constituye un elemento positivo que favorece la calidad del servicio.

Sin embargo, se detecta la ausencia de herramientas específicas de orquestación de contenedores, así como una definición limitada de la arquitectura objetivo, especialmente en lo relativo a la gestión del estado y la persistencia en entornos distribuidos.

En términos globales, la solución es consistente y alineada con el requisito, aunque con margen de mejora en la definición arquitectónica.

**Valoración cualitativa: Alta**

## Conclusión del bloque BD

El análisis del bloque de bases de datos pone de manifiesto que la propuesta de empresa_s presenta un nivel técnico elevado, con una adaptación real a los requisitos del pliego y una orientación clara hacia la automatización y la operación en entornos de gran escala. **La utilización de tecnologías concretas y la diferenciación por tipología de sistema constituyen elementos especialmente positivos.**

**Las principales limitaciones identificadas se relacionan con la falta de métricas cuantificables, la definición incompleta de ciertos procedimientos y la ausencia de detalle en algunos aspectos arquitectónicos.** No obstante, estas carencias no comprometen la viabilidad global de la solución, que se sitúa en una franja alta de valoración.

### BLOQUE MON — MONITORIZACIÓN, TESTEO Y PRUEBAS DE RENDIMIENTO

## MON1 — Mantenimiento periódico del almacenamiento de los centros

**El subproyecto MON1 establece la necesidad de gestionar activamente el almacenamiento distribuido de la plataforma, incluyendo la redistribución periódica de la ocupación entre sistemas NFS, el análisis de la capacidad y la ejecución de actuaciones en periodos no lectivos.** Se trata de un requisito que implica un enfoque proactivo basado en el análisis continuo de la ocupación y el crecimiento del sistema.

**La propuesta de empresa_s aborda este subproyecto mediante la definición de un modelo de monitorización continua de la capacidad y el análisis de ocupación, incorporando mecanismos de redistribución dinámica de datos y balanceo entre nodos.** Se describen, además, procedimientos de migración controlada, validación de integridad de los datos tras el movimiento y automatización de determinadas actuaciones, todo ello orientado a optimizar el uso del almacenamiento disponible.

**Se aprecia una orientación clara hacia la gestión activa de la capacidad, incorporando elementos como el capacity planning y el uso de modelos predictivos que permiten anticipar necesidades futuras de almacenamiento.** Este enfoque se alinea con los requisitos del pliego y aporta un componente de madurez técnica relevante en entornos de gran escala.

**No obstante, la propuesta presenta una limitación en la definición de herramientas concretas asociadas a la gestión de almacenamiento NFS, así como en la ausencia de umbrales cuantificados que determinen cuándo deben ejecutarse las redistribuciones.** Esta falta de métricas limita parcialmente la capacidad de evaluar objetivamente el comportamiento del sistema.

En conjunto, la propuesta responde adecuadamente al requisito, desarrollando un modelo operativo coherente orientado a la automatización y la optimización de capacidad.

**Valoración cualitativa: Alta**

## MON2 — Realización periódica de pruebas de estrés en diferentes entornos de la plataforma

**El subproyecto MON2 exige la ejecución de pruebas de carga y estrés que permitan evaluar el rendimiento de los sistemas, identificar anomalías y proponer medidas correctivas.** Este tipo de actividades requiere la definición de una metodología estructurada y el uso de herramientas específicas de ingeniería de rendimiento.

La propuesta de empresa_s desarrolla este subproyecto con un alto grado de concreción técnica, incorporando herramientas reconocidas como Apache JMeter, Gatling y Apache Benchmark, que permiten la simulación de cargas concurrentes y la evaluación del comportamiento de los sistemas bajo diferentes condiciones.

**Asimismo, se define una metodología que incluye el diseño de escenarios de prueba, la ejecución de las mismas, la monitorización de los recursos durante la carga, el análisis de los resultados y la identificación de cuellos de botella.** Este enfoque estructurado aporta un elevado nivel de operatividad y permite evaluar la solución en condiciones próximas a la realidad.

Se valora especialmente la integración de estas pruebas dentro de un modelo continuo de operación que incorpora elementos de DevOps y observabilidad, lo que permite analizar la evolución del rendimiento a lo largo del tiempo.

Como limitación, se observa la ausencia de definición explícita de objetivos de rendimiento y umbrales de aceptación asociados a los resultados de las pruebas, así como la falta de escenarios específicos vinculados a aplicaciones concretas de la plataforma.

En términos globales, la propuesta presenta un nivel técnico elevado y una adecuada capacidad de ejecución de pruebas de rendimiento en entornos complejos.

**Valoración cualitativa: Muy alta**

## MON3 — Mantener actualizado el sistema de monitorización y estadísticas de uso

El subproyecto MON3 exige la gestión evolutiva del sistema de monitorización, incluyendo la incorporación de nuevos servicios, la utilización de herramientas open source y la definición de alertas tanto reactivas como proactivas.

**La propuesta de empresa_s presenta un desarrollo sólido de este requisito, incorporando una arquitectura de monitorización basada en herramientas ampliamente utilizadas como Prometheus, Grafana, Zabbix y Metabase.** La combinación de estas herramientas permite abordar la recolección de métricas, la visualización de información y la generación de cuadros de mando adaptados a diferentes niveles de análisis.

El enfoque planteado incluye la integración de diferentes fuentes de información mediante exporters específicos, la centralización de métricas y la implementación de mecanismos de alertado que permiten detectar anomalías en el comportamiento de los sistemas. **Asimismo, se introduce el concepto de capacity planning, orientado a anticipar la evolución de la carga y dimensionar adecuadamente la infraestructura.**

Se aprecia una alineación directa con los requisitos del pliego, especialmente en lo relativo al uso de herramientas open source y a la evolución continua del sistema de monitorización.

Sin embargo, la propuesta presenta una cierta falta de definición en lo relativo a los umbrales concretos de alertado y a la clasificación de eventos, lo que introduce un elemento de incertidumbre en la operatividad diaria del sistema.

En términos generales, la solución es consistente, bien estructurada y técnicamente adecuada para entornos de gran escala.

**Valoración cualitativa: Alta**

## MON4 — Monitorización y estadísticas de servicios basados en IA

El subproyecto MON4 introduce la monitorización específica de servicios basados en inteligencia artificial, lo que implica la definición de métricas adaptadas a este tipo de sistemas, incluyendo consumo de recursos, comportamiento de modelos y calidad de respuesta.

La propuesta de empresa_s aborda este requisito integrando la monitorización de servicios de IA dentro de la arquitectura general de observabilidad, incorporando indicadores relacionados con el rendimiento, el consumo y el comportamiento de los modelos. **Asimismo, se definen mecanismos de evaluación continua, incluyendo la medición de precisión, errores y sesgos en las respuestas generadas.**

Este enfoque representa un avance respecto a planteamientos genéricos, al incorporar elementos específicos de control y supervisión de sistemas de inteligencia artificial, incluyendo aspectos de gobernanza como el control de prompts, la trazabilidad de consultas y la auditoría de resultados.

No obstante, se detecta una menor profundidad en la definición de herramientas específicas para este tipo de monitorización, así como una ausencia de métricas cuantificadas que permitan evaluar el rendimiento de los modelos de forma objetiva.

En conjunto, la propuesta cubre el requisito de manera adecuada, incorporando elementos diferenciales propios de la operación de sistemas de IA, aunque con margen de mejora en la definición detallada de indicadores y herramientas.

**Valoración cualitativa: Alta**

## Conclusión del bloque MON

**El bloque de monitorización y pruebas de rendimiento presenta un nivel técnico elevado, destacando especialmente la definición de herramientas concretas y la adopción de metodologías estructuradas en el ámbito de las pruebas de carga.** La propuesta de empresa_s se caracteriza por una orientación clara hacia la observabilidad, la automatización y el análisis continuo del rendimiento.

**Las principales carencias se centran en la falta de definición de métricas cuantificables y umbrales operativos, lo que limita parcialmente la capacidad de validar de forma objetiva el comportamiento del sistema.** No obstante, la solución es consistente y adecuada para un entorno de alta complejidad.

### BLOQUE UPD — ACTUALIZACIÓN DE SERVICIOS EXISTENTES

## UPD1 — Mantenimiento y mejora de los sistemas de videoconferencias

El subproyecto UPD1 requiere la gestión y evolución de sistemas de videoconferencia, incluyendo la actualización de componentes, la optimización del rendimiento y la gestión de entornos de alta concurrencia.

La propuesta de empresa_s aborda este requisito mediante la definición de una arquitectura especializada que integra tecnologías como Jitsi y BigBlueButton, incorporando nodos dedicados para la gestión de media, mecanismos de balanceo y monitorización de indicadores de calidad como latencia, jitter y pérdida de paquetes.

**El enfoque planteado refleja una comprensión adecuada de las particularidades de los sistemas de videoconferencia, especialmente en lo relativo a la gestión de sesiones concurrentes y al control de la calidad del servicio.** La incorporación de métricas específicas aporta un elemento diferencial relevante frente a propuestas más genéricas.

Sin embargo, la propuesta no desarrolla en profundidad los mecanismos de escalabilidad ante picos de carga ni los procedimientos detallados de actualización de versiones en entornos distribuidos.

En términos generales, la solución es técnicamente adecuada y bien orientada, aunque con margen de mejora en la definición operativa.

**Valoración cualitativa: Alta**

## UPD2 — Sistema secundario de videoconferencias con grabación

Este subproyecto introduce la funcionalidad de grabación dentro de los sistemas de videoconferencia, lo que implica la gestión de almacenamiento, procesamiento de contenidos y escalabilidad del sistema.

La propuesta de empresa_s contempla la existencia de nodos diferenciados para la grabación en el caso de BigBlueButton, lo que permite aislar este proceso del resto de la infraestructura y mejorar el rendimiento global del sistema.

Asimismo, se incluye la integración de estos sistemas con el resto de la plataforma, lo que facilita la gestión de contenidos y su posterior uso en entornos educativos.

No obstante, la propuesta presenta un nivel de desarrollo limitado en lo relativo a los procesos de almacenamiento, indexación y procesamiento de grabaciones, así como en la definición de políticas de retención y gestión de espacio.

En conjunto, la solución cubre el requisito, aunque con un desarrollo técnico menos profundo que el observado en otros apartados.

**Valoración cualitativa: Media**

## UPD3 — Mantenimiento y mejora de Mattermost

El subproyecto UPD3 exige la gestión de una plataforma de comunicación interna, incluyendo su mantenimiento, actualización e integración con otros sistemas de la plataforma.

La propuesta de empresa_s incluye la gestión de herramientas colaborativas dentro de una arquitectura segmentada que integra servicios como Mattermost, LDAP y sistemas internos, con capacidad de despliegue en entornos contenerizados y control de accesos mediante SSO.

Este enfoque demuestra una comprensión adecuada del contexto en el que se integra la herramienta, así como de la necesidad de garantizar su disponibilidad y seguridad.

Sin embargo, la propuesta no desarrolla de forma detallada los componentes internos de la plataforma ni los mecanismos específicos de alta disponibilidad o escalabilidad asociados a Mattermost.

En términos generales, la solución es correcta y coherente, aunque con un nivel de detalle técnico limitado.

**Valoración cualitativa: Media-Alta**

## UPD4 — Solución Kanban

El subproyecto UPD4 requiere la gestión y evolución de una herramienta de tipo Kanban para la organización del trabajo.

La propuesta de empresa_s aborda este requisito de forma indirecta, integrando herramientas de gestión dentro del ecosistema general, pero sin desarrollar de forma específica una solución concreta ni identificar la herramienta utilizada.

La falta de concreción técnica impide evaluar con detalle la capacidad real de ejecución en este ámbito, así como su integración con otros sistemas como Redmine o GitLab.

En consecuencia, la cobertura del requisito resulta parcialmente insuficiente, al mantenerse en un nivel conceptual sin desarrollo operativo.

**Valoración cualitativa: Media-Baja**

## UPD5 — Mantenimiento y mejora de GitLab

El subproyecto UPD5 exige la gestión de una plataforma de desarrollo colaborativo, incluyendo repositorios, pipelines de integración continua y herramientas de control de calidad.

La propuesta de empresa_s integra GitLab dentro de su modelo DevOps, incluyendo pipelines CI/CD, automatización de despliegues y control de versiones, lo que refleja una comprensión adecuada del papel de esta herramienta en el ciclo de vida del desarrollo.

No obstante, el nivel de detalle sobre la configuración específica de pipelines, la gestión de runners o la definición de entornos de despliegue resulta limitado.

En términos generales, la solución es coherente y alineada con el requisito, aunque con margen de mejora en la concreción técnica.

**Valoración cualitativa: Alta**

### BLOQUE UPD — ACTUALIZACIÓN DE SERVICIOS EXISTENTES

## UPD6 — Mantenimiento y mejora de la solución LimeSurvey

El subproyecto UPD6 requiere la gestión de la herramienta LimeSurvey incluyendo su actualización, optimización de rendimiento y evolución funcional, lo que implica comprender tanto su arquitectura como su integración con sistemas de almacenamiento y bases de datos subyacentes.

**La propuesta de empresa_s aborda este subproyecto dentro de su arquitectura general multinivel, en la que se definen componentes diferenciados para aplicación, datos y almacenamiento, integrados mediante mecanismos de seguridad y operación.** Este planteamiento muestra una comprensión básica del funcionamiento de la herramienta y su ubicación dentro del ecosistema EducaMadrid.

**Sin embargo, el análisis técnico evidencia que el nivel de desarrollo específico para LimeSurvey resulta limitado.** La propuesta no detalla mecanismos concretos de optimización de consultas, mejora de rendimiento o evolución funcional, ni incorpora procedimientos específicos de pruebas asociados al comportamiento de la herramienta. Tampoco se describen mejoras en la experiencia de usuario ni actuaciones sobre la arquitectura objetivo.

En consecuencia, aunque el planteamiento resulta coherente desde un punto de vista estructural, carece de profundidad técnica suficiente para evaluar su aplicabilidad en un entorno de gran escala.

**Valoración cualitativa: Media**

## UPD7 — Mantenimiento y mejora de SonarQube

El subproyecto UPD7 se orienta a la gestión de la plataforma SonarQube como herramienta de análisis de calidad de código, incluyendo la definición de reglas, perfiles de calidad y control de proyectos.

La propuesta de empresa_s integra SonarQube dentro de su modelo DevOps, donde se contempla el análisis de código dentro de pipelines CI/CD y la automatización de procesos de validación. **Este planteamiento es coherente con el uso habitual de la herramienta en entornos de desarrollo moderno y refleja una comprensión adecuada de su papel dentro del ciclo de vida de software.**

**No obstante, el grado de desarrollo técnico específico resulta limitado en lo relativo a la configuración de la herramienta.** No se describen elementos fundamentales como la definición de Quality Gates, la gestión de perfiles de calidad, el uso de reglas específicas o la integración detallada con repositorios. Esta ausencia de detalle reduce la capacidad de evaluar el nivel real de madurez del planteamiento.

En conjunto, la solución cubre el ámbito funcional requerido, aunque con una concreción técnica limitada.

**Valoración cualitativa: Media-Alta**

## UPD8 — Mantenimiento y mejora de Redmine

El subproyecto UPD8 exige la gestión de la herramienta Redmine como sistema de seguimiento de tareas, incluyendo su mantenimiento, automatización y evolución funcional.

**La propuesta de empresa_s incluye la integración de herramientas de gestión dentro de su modelo operativo, planteando la utilización de APIs, automatización mediante scripts y mecanismos de autenticación centralizada mediante SSO.** Este enfoque facilita la integración de Redmine dentro del ecosistema, especialmente en lo relativo a la trazabilidad del servicio.

Se aprecia una alineación adecuada con el uso de Redmine en entornos de gestión de incidencias y proyectos, incorporando además elementos de automatización que mejoran la eficiencia operativa.

No obstante, la propuesta no profundiza en aspectos como la configuración de flujos de trabajo, la gestión avanzada de proyectos ni la integración detallada con otras herramientas del sistema como GitLab o sistemas de monitorización.

En términos generales, la solución es coherente y funcional, aunque con un desarrollo técnico moderado.

**Valoración cualitativa: Alta**

## UPD9 — Mantenimiento y configuración de Wowza Streaming Engine

El subproyecto UPD9 requiere la gestión de una plataforma de streaming basada en tecnologías específicas como Wowza, lo que implica el conocimiento de protocolos de transmisión, codificación de vídeo y distribución de contenidos.

**La propuesta de empresa_s contempla la retransmisión en vivo mediante una arquitectura orientada a streaming, incluyendo el uso de Wowza, servicios de transcodificación escalables y distribución mediante CDN.** Este planteamiento demuestra una comprensión clara del funcionamiento de sistemas de streaming y de sus componentes principales.

La inclusión de elementos de procesamiento asíncrono y control de acceso permite abordar de forma adecuada los requisitos de rendimiento y seguridad asociados a la transmisión de contenidos.

Sin embargo, la propuesta no detalla aspectos operativos relevantes como la gestión de protocolos específicos, la optimización de caché ni la monitorización detallada de flujos de vídeo en tiempo real.

En conjunto, la solución presenta un nivel técnico adecuado y una alineación correcta con el requisito, aunque con margen de mejora en la definición operativa.

**Valoración cualitativa: Alta**

## UPD10 — Mantenimiento y gestión de contenidos AbiesWeb

El subproyecto UPD10 está orientado a la gestión de contenidos bibliográficos mediante AbiesWeb, incluyendo la carga de datos, la sincronización con sistemas externos y la evolución funcional del sistema.

**La propuesta de empresa_s aborda este subproyecto de forma indirecta dentro de su modelo de gestión de aplicaciones, sin desarrollar específicamente las particularidades de AbiesWeb.** Se describen actividades generales de mantenimiento, gestión de contenidos e integración con otros servicios, lo que proporciona una cobertura básica del requisito.

**Sin embargo, no se identifican procedimientos de carga masiva de datos, ni mecanismos de sincronización con sistemas externos, ni estrategias de evolución funcional específicas para esta herramienta.** Esto limita la profundidad de la solución y su aplicabilidad en escenarios reales.

En conjunto, la cobertura del requisito es parcial y se mantiene en un nivel descriptivo general.

**Valoración cualitativa: Media**

## UPD11 — Abies+

El subproyecto UPD11 implica la evolución del sistema Abies+, incluyendo la implementación de mejoras, la gestión de contenidos y la realización de pruebas asociadas a las nuevas funcionalidades.

**La propuesta de empresa_s mantiene un enfoque similar al del subproyecto anterior, centrado en la actualización general del sistema y en la gestión básica de contenidos.** No se describen procedimientos específicos de pruebas, ni mecanismos de validación estructurada, ni planes de evolución funcional detallados.

Tampoco se aborda de forma específica la posible migración desde sistemas anteriores, aspecto relevante en el contexto del pliego.

En consecuencia, la propuesta presenta una cobertura limitada del requisito, sin un desarrollo técnico suficiente que permita evaluar su capacidad real de ejecución.

**Valoración cualitativa: Media-Baja**

## UPD12 — Implementación, mantenimiento y mejora de Empieza

El subproyecto UPD12 presenta un nivel alto de exigencia técnica al tratarse de un sistema central de integración y automatización basado en microservicios.

La propuesta de empresa_s define Empieza como un microservicio central que actúa como elemento de integración entre plataformas mediante APIs y motor de reglas, lo que refleja claramente su papel dentro del ecosistema EducaMadrid.

El planteamiento incluye una arquitectura multinivel con balanceo, integración con sistemas corporativos y mecanismos de seguridad y trazabilidad, lo que aporta coherencia y alineación con el requisito.

**No obstante, la propuesta no desarrolla con suficiente detalle los mecanismos de escalabilidad horizontal, balanceo de carga ni alta disponibilidad asociados a este tipo de sistemas críticos.** Tampoco se identifican herramientas concretas ni arquitecturas específicas que respalden estos conceptos.

En conjunto, la solución es conceptualmente sólida pero presenta carencias en su desarrollo técnico detallado.

**Valoración cualitativa: Media-Alta**

## UPD13 — Sistema de gestión de la configuración

El subproyecto UPD13 exige la gestión del sistema de configuración mediante herramientas específicas y la automatización de procesos de actualización y correlación de datos.

La propuesta de empresa_s incluye la automatización mediante Ansible y la integración de sistemas dentro de una CMDB centralizada, lo que aporta un enfoque coherente con el requisito.

**Sin embargo, no se desarrollan en profundidad las herramientas específicas indicadas en el pliego ni los mecanismos de correlación de información entre sistemas.** Tampoco se identifican procedimientos detallados de automatización orientados a la gestión de la configuración.

En consecuencia, la cobertura del requisito es parcial, con un enfoque generalista que no alcanza el nivel de detalle requerido.

**Valoración cualitativa: Media-Alta**

## UPD14 — Solución de contenedores

El subproyecto UPD14 requiere la gestión de entornos de contenedores, incluyendo la orquestación, automatización de despliegues y evolución de infraestructuras.

La propuesta de empresa_s incluye la utilización de Docker y la integración en pipelines CI/CD, lo que demuestra una orientación clara hacia la contenerización.

**No obstante, la propuesta indica en múltiples casos que el uso de contenedores se encuentra “en estudio”, lo que introduce incertidumbre sobre su aplicación real en la arquitectura.** Asimismo, no se identifican herramientas de orquestación como Kubernetes ni se describen arquitecturas completas de despliegue.

Esta falta de definición limita significativamente la capacidad de evaluar la viabilidad de la solución en entornos distribuidos.

**Valoración cualitativa: Media**

## UPD15 — Gestión y decomisionado de servidores

El subproyecto UPD15 implica la gestión completa del ciclo de vida de servidores, incluyendo su retirada, limpieza de dependencias y actualización de sistemas asociados.

La propuesta de empresa_s aborda este aspecto de forma general dentro de su modelo de operación, incluyendo actividades de actualización de inventario y gestión de sistemas.

Sin embargo, no se describen procedimientos completos de decomisionado ni mecanismos detallados para la gestión de DNS, almacenamiento o dependencias asociadas a los servidores retirados.

En consecuencia, la propuesta presenta una cobertura parcial del requisito, con un nivel de detalle insuficiente para su evaluación completa.

**Valoración cualitativa: Media**

## Conclusión del bloque UPD

**El bloque de actualización de servicios existentes presenta un nivel de desarrollo técnico heterogéneo.** Se observan apartados con un elevado grado de concreción y alineación, especialmente en aquellos relacionados con arquitecturas complejas como videoconferencias o streaming, mientras que otros subproyectos presentan un enfoque más generalista y menos detallado.

Las principales debilidades detectadas se centran en la falta de desarrollo específico por herramienta, la ausencia de procedimientos operativos detallados y la limitada definición de arquitecturas en determinados ámbitos.

En términos globales, la valoración del bloque se sitúa en un nivel medio-alto, condicionado por la variabilidad en la calidad de los distintos subproyectos.

### BLOQUE CLO — CLOUD

## CLO1 — Mantenimiento del servicio de la nube de EducaMadrid

**El subproyecto CLO1 establece la necesidad de mantener y evolucionar el servicio cloud de EducaMadrid, incluyendo la gestión de un volumen elevado de usuarios, la redistribución de carga, la planificación de capacidad y la optimización del almacenamiento.** Se trata de uno de los ámbitos más críticos del contrato debido al volumen potencial de usuarios y al carácter central del servicio.

**La propuesta de empresa_s aborda este subproyecto mediante la definición de una arquitectura cloud basada en soluciones como NextCloud y Collabora, integradas en un entorno multinivel con mecanismos de balanceo, almacenamiento compartido y control de sesión mediante sistemas como Redis.** Este planteamiento permite identificar una base técnica coherente para la prestación del servicio, especialmente en lo relativo a la integración de componentes y a la gestión de sesiones concurrentes.

**Asimismo, se incorporan elementos de seguridad, control de cuotas y gestión de almacenamiento, lo que demuestra una comprensión de las necesidades básicas del sistema cloud en un entorno educativo.** La propuesta plantea además la posibilidad de evolucionar hacia arquitecturas más avanzadas como el uso de object storage en el futuro, lo que indica una orientación hacia la mejora continua.

**Sin embargo, el análisis técnico evidencia que la propuesta no desarrolla en profundidad aspectos críticos como la planificación de capacidad a medio y largo plazo, la definición de mecanismos concretos de redistribución de carga o la gestión operativa de un entorno que puede alcanzar millones de usuarios.** La ausencia de métricas cuantificadas y de procedimientos detallados limita la capacidad de evaluar la viabilidad real de la solución en condiciones de alta demanda.

En consecuencia, la propuesta presenta una base técnica adecuada pero con un desarrollo insuficiente en términos de operación a gran escala.

**Valoración cualitativa: Media-Alta**

## CLO2 — Almacenamiento temporal de datos en la nube

El subproyecto CLO2 exige la gestión del almacenamiento temporal de datos dentro del entorno cloud, incluyendo su adaptación a necesidades de escalabilidad, interoperabilidad con otros sistemas y capacidad de respuesta ante incrementos de carga.

**La propuesta de empresa_s aborda este subproyecto dentro de su arquitectura general de almacenamiento, contemplando el uso de sistemas NFS y la posible evolución hacia soluciones más avanzadas.** Se incluyen mecanismos de control de almacenamiento temporal, caducidad de datos y trazabilidad de accesos, lo que proporciona una base funcional coherente.

El enfoque planteado permite identificar una comprensión adecuada del papel de este tipo de almacenamiento dentro de la plataforma, especialmente en lo relativo a la gestión del ciclo de vida de los datos temporales y su integración con servicios asociados.

**No obstante, la propuesta presenta carencias significativas en la definición de mecanismos de escalabilidad, distribución de carga y alta disponibilidad.** No se describen procedimientos específicos orientados a garantizar la interoperabilidad con otros sistemas ni se identifican herramientas concretas para la gestión del almacenamiento temporal en entornos de alta concurrencia.

En consecuencia, la solución resulta funcional desde un punto de vista conceptual, pero presenta un desarrollo técnico limitado para abordar escenarios exigentes.

**Valoración cualitativa: Media**

## CLO3 — Sistema de edición en línea de EducaMadrid

El subproyecto CLO3 se centra en la gestión y evolución del sistema de edición en línea, incluyendo su integración con el entorno cloud, la gestión de usuarios concurrentes y la optimización del rendimiento.

La propuesta de empresa_s plantea una integración entre NextCloud y herramientas de edición colaborativa como Collabora, con separación de componentes y control de sesiones mediante Redis, lo que permite una gestión estructurada del servicio. **Este enfoque refleja una comprensión adecuada de las necesidades de edición colaborativa en entornos educativos, incluyendo la gestión simultánea de múltiples usuarios y la integración con sistemas de almacenamiento.**

**Sin embargo, el análisis técnico muestra que no se desarrollan mecanismos específicos de escalabilidad ni estrategias de optimización del rendimiento en escenarios de alta concurrencia.** Tampoco se detallan procedimientos de balanceo de carga ni de gestión de sesiones en condiciones de uso intensivo.

La ausencia de estos elementos limita la capacidad de evaluar la robustez de la solución en un entorno real de explotación, especialmente considerando la criticidad del servicio para el usuario final.

En consecuencia, la propuesta presenta una cobertura funcional adecuada, pero con un nivel de desarrollo técnico incompleto.

**Valoración cualitativa: Media-Alta**

## Conclusión del bloque CLO

**El bloque cloud presenta una base técnica coherente y alineada con los requisitos del pliego, con una integración adecuada de herramientas y arquitecturas multinivel.** No obstante, la propuesta muestra una falta de profundidad en aspectos clave como la escalabilidad, la planificación de capacidad y la operación en entornos de gran volumen, lo que reduce su nivel de madurez operativa.

La valoración global del bloque se sitúa en un nivel medio-alto, condicionado por la limitada definición de mecanismos operativos detallados.

### BLOQUE OTR — OTROS DESARROLLOS

## OTR1 — Sistema de autenticación centralizada SSO

El subproyecto OTR1 exige la gestión del sistema de autenticación centralizada, incluyendo su integración con LDAP, la implantación de alta disponibilidad y la gestión de identidades en un entorno corporativo.

**La propuesta de empresa_s desarrolla este subproyecto mediante la adopción de una arquitectura basada en Keycloak, integrada con LDAP y con mecanismos de control de sesiones, lo que refleja una alineación directa con el requisito.** Se contempla la autenticación centralizada como un elemento transversal de la arquitectura, lo que permite su integración con el resto de servicios de la plataforma.

Asimismo, se incorporan aspectos de seguridad como el control de accesos y la protección frente a vulnerabilidades comunes, lo que contribuye a reforzar la fiabilidad del sistema.

Sin embargo, la propuesta no desarrolla en profundidad aspectos como la federación de identidades, la gestión avanzada de sesiones o la definición detallada de arquitecturas de alta disponibilidad, lo que limita la capacidad de evaluar su comportamiento en escenarios críticos.

En términos generales, la solución es adecuada y demuestra una comprensión del requisito, aunque con margen de mejora en la definición técnica.

**Valoración cualitativa: Media-Alta**

## OTR2 — Gestión 2FA en SSO

El subproyecto OTR2 se centra en la implementación de mecanismos de autenticación multifactor, incluyendo su integración con el sistema de identidad y el control de accesos.

**La propuesta de empresa_s incluye el uso de mecanismos de autenticación multifactor basados en OTP y aplicaciones móviles, lo que demuestra una comprensión adecuada de las tecnologías implicadas.** Asimismo, se plantea su integración con el sistema SSO, lo que permite reforzar la seguridad de acceso a la plataforma.

**No obstante, el nivel de detalle técnico es limitado en lo relativo a la gestión de identidades, la sincronización con directorios y la definición de procedimientos de implantación.** Tampoco se describen mecanismos de gestión operativa del sistema ni políticas detalladas de seguridad.

En consecuencia, la solución resulta adecuada desde un punto de vista conceptual, pero carece de desarrollo técnico suficiente.

**Valoración cualitativa: Media**

## OTR3 — Automatización de tareas

El subproyecto OTR3 requiere la implantación de mecanismos de automatización que permitan gestionar tareas repetitivas y optimizar procesos en un entorno complejo.

La propuesta de empresa_s incorpora la automatización como uno de los pilares de su modelo operativo, incluyendo el uso de herramientas como Ansible y pipelines CI/CD, lo que aporta coherencia con el enfoque general de la solución.

Este planteamiento introduce un nivel significativo de automatización en la operación del servicio, lo que favorece la eficiencia y la reducción de errores humanos.

Sin embargo, no se identifican arquitecturas específicas de orquestación ni sistemas centralizados de gestión de automatizaciones, lo que limita el desarrollo técnico del subproyecto.

**Valoración cualitativa: Media-Alta**

## OTR4 — Sistema de análisis de datos mediante Elastic

El subproyecto OTR4 exige la gestión de sistemas de análisis de datos basados en tecnologías del stack Elastic, incluyendo la ingestión, procesamiento y visualización de logs.

La propuesta de empresa_s incluye la utilización de herramientas de observabilidad y análisis de datos, integradas dentro de su modelo de monitorización, lo que proporciona una base funcional adecuada.

No obstante, el nivel de desarrollo técnico específico es limitado, ya que no se describen arquitecturas detalladas del stack Elastic ni procesos de ingestión, almacenamiento o visualización de datos.

En consecuencia, la cobertura del requisito es parcial.

**Valoración cualitativa: Media**

## OTR5 — Herramienta de flujos de trabajo

El subproyecto OTR5 requiere la gestión de una herramienta de workflow que permita automatizar procesos y gestionar flujos de tareas.

La propuesta de empresa_s no desarrolla de forma específica este subproyecto, limitándose a integrar la automatización dentro de su modelo general sin identificar herramientas concretas ni procedimientos asociados.

Esta ausencia de desarrollo impide evaluar la capacidad real de ejecución del requisito.

**Valoración cualitativa: Baja**

## OTR6 — Portal CAU

El subproyecto OTR6 se centra en la gestión del portal de atención al usuario, incluyendo su evolución funcional e integración con sistemas de soporte.

La propuesta de empresa_s aborda este ámbito de forma general, integrando la gestión de incidencias dentro de su modelo operativo, pero sin desarrollar específicamente las funcionalidades del portal CAU.

La falta de detalle técnico limita la valoración del subproyecto.

**Valoración cualitativa: Media**

## OTR7 — Servicios de Inteligencia Artificial

El subproyecto OTR7 requiere la evolución de servicios de inteligencia artificial dentro de la plataforma.

La propuesta de empresa_s incorpora la inteligencia artificial de forma transversal, integrándola en diferentes componentes como analítica, automatización y soporte docente, así como en procesos de evaluación continua y control de calidad de resultados.

Se aprecia un enfoque innovador y alineado con las tendencias actuales, aunque la definición técnica de arquitecturas, pipelines de entrenamiento y despliegue de modelos resulta limitada.

**Valoración cualitativa: Media-Alta**

## Conclusión del bloque OTR

El bloque de otros desarrollos presenta un nivel heterogéneo, con subproyectos bien alineados en el ámbito de identidad y automatización, pero con un desarrollo limitado en otros apartados.

La valoración global se sitúa en un nivel medio, condicionado por la falta de concreción técnica en varios subproyectos.

### BLOQUE COR — CORREO ELECTRÓNICO

## COR1 — Mantenimiento y mejora de los sistemas de control de envíos de correo

El subproyecto COR1 establece la necesidad de implantar mecanismos de control sobre el tráfico de correo saliente, incluyendo la regulación de envíos, la gestión de flujos y la aplicación de políticas diferenciadas según dominios o proveedores. **En entornos como EducaMadrid, caracterizados por un elevado volumen de usuarios, este aspecto resulta crítico para mantener la reputación del sistema y evitar bloqueos por parte de terceros.**

La propuesta de empresa_s integra el sistema de correo dentro de una arquitectura distribuida basada en componentes como RoundCube para acceso web y QMail para transporte, incorporando elementos de seguridad como SPF, DKIM y DMARC, así como mecanismos antispam y antimalware. **Este planteamiento demuestra una comprensión adecuada de los componentes técnicos implicados en la infraestructura de correo.**

**No obstante, el análisis técnico pone de manifiesto que la propuesta no desarrolla de forma específica mecanismos de control del tráfico saliente como políticas de limitación por usuario, gestión de colas o control de reputación de IPs.** Tampoco se describen modelos de regulación dinámica del flujo de correo en función del comportamiento del sistema.

En consecuencia, la cobertura del requisito resulta parcial, al centrarse en la infraestructura básica y omitir aspectos clave de control operativo.

**Valoración cualitativa: Media**

## COR2 — Mantenimiento automatizado de listas de distribución

El subproyecto COR2 exige la automatización del mantenimiento de listas de distribución, incluyendo la sincronización con sistemas corporativos, la actualización masiva de usuarios y la gestión dinámica de cambios. **Este requisito resulta especialmente relevante en entornos educativos con altas tasas de rotación de usuarios.**

La propuesta de empresa_s aborda este ámbito dentro de su enfoque general de automatización e integración con sistemas corporativos, especialmente mediante su modelo basado en LDAP, SSO y herramientas de automatización como Ansible. **Este planteamiento permite inferir una base funcional para la sincronización de usuarios y la gestión de identidades, lo que constituye un elemento positivo.**

Se aprecia una alineación conceptual con el requisito, en tanto que la propuesta plantea una arquitectura integrada en la que los sistemas de identidad y correo se encuentran interconectados, lo que facilita la automatización de procesos de actualización de usuarios.

**Sin embargo, el nivel de desarrollo técnico específico resulta limitado.** La propuesta no describe procedimientos concretos para la actualización automatizada de listas, ni mecanismos de gestión de cambios masivos, ni flujos operativos definidos para la sincronización con directorios corporativos. Tampoco se identifican herramientas específicas de gestión de listas de distribución ni métricas que permitan evaluar la consistencia o el estado de las mismas.

Esta falta de concreción reduce la capacidad de evaluar la viabilidad real de la solución en condiciones operativas y limita su verificabilidad.

En conjunto, la propuesta presenta una base conceptual adecuada pero carece del desarrollo técnico necesario para garantizar una implementación operativa completa del requisito.

**Valoración cualitativa: Media**

## COR3 — Gestión de cuotas de correo

Este subproyecto exige la gestión del sistema de cuotas de buzones, incluyendo su activación, control del consumo y adaptación dinámica a diferentes tipologías de usuario.

**La propuesta de empresa_s contempla la gestión del almacenamiento de buzones dentro de una arquitectura distribuida con replicación y alta disponibilidad, incluyendo mecanismos de backup y control de capacidad.** Este enfoque proporciona una base sólida desde el punto de vista de infraestructura.

**No obstante, el análisis técnico evidencia que el tratamiento de las cuotas de correo no se desarrolla de forma específica.** No se describen políticas diferenciadas por tipo de usuario, ni mecanismos automatizados de ajuste dinámico de cuotas, ni sistemas de alerta asociados al consumo de espacio.

Asimismo, no se identifican herramientas específicas para la gestión de cuotas ni métricas operativas que permitan evaluar el comportamiento del sistema en condiciones reales.

En consecuencia, la cobertura del requisito resulta parcial, al centrarse en la infraestructura base sin abordar los mecanismos funcionales asociados a la gestión de cuotas.

**Valoración cualitativa: Media**

## COR4 — Control del spam

El subproyecto COR4 requiere la implantación y evolución de herramientas de control de spam, incluyendo mecanismos de detección, filtrado y clasificación de correos.

La propuesta de empresa_s incluye la integración de sistemas antispam dentro de la arquitectura de correo, junto con mecanismos de seguridad como SPF, DKIM y DMARC, lo que constituye una base adecuada para la protección del sistema frente a amenazas externas.

**Sin embargo, no se desarrolla en profundidad la estrategia de gestión del spam.** No se describen herramientas concretas utilizadas para la clasificación de correos, ni mecanismos avanzados de análisis de comportamiento, ni procesos de ajuste continuo de reglas.

Asimismo, no se definen métricas asociadas al rendimiento del sistema de filtrado, como tasas de falsos positivos o niveles de detección.

La ausencia de estos elementos limita la capacidad de evaluar la eficacia real de la solución.

**Valoración cualitativa: Media**

## COR5 — Mantenimiento de buzones de correo

Este subproyecto implica la gestión operativa de los buzones, incluyendo su mantenimiento, disponibilidad y recuperación ante incidencias.

La propuesta de empresa_s plantea una arquitectura con almacenamiento distribuido, replicación de buzones y mecanismos de backup y recuperación, lo que aporta un nivel adecuado de robustez desde el punto de vista de infraestructura.

Se aprecia un enfoque orientado a garantizar la continuidad del servicio, con mecanismos de alta disponibilidad y recuperación ante fallos.

No obstante, no se describen procedimientos operativos detallados para la gestión de buzones, ni herramientas específicas de administración, ni métricas asociadas al rendimiento del sistema.

Esta falta de concreción limita la evaluación de la operatividad del servicio.

**Valoración cualitativa: Media-Alta**

## COR6 — Seguridad del sistema de correo

El subproyecto COR6 exige la implantación de mecanismos de seguridad continua en el sistema de correo.

La propuesta de empresa_s integra la seguridad como un elemento transversal, incorporando mecanismos de protección frente a amenazas, control de accesos y monitorización de eventos. **Este enfoque resulta coherente con los requisitos del pliego.**

**Sin embargo, el nivel de desarrollo técnico específico es limitado.** No se describen procedimientos concretos de actualización de políticas de seguridad, ni herramientas específicas de análisis, ni métricas que permitan evaluar el nivel de protección.

**Valoración cualitativa: Media-Alta**

## COR7 — Infraestructura de correo

**El subproyecto COR7 requiere no sólo la actualización puntual de los componentes del sistema de correo, sino la definición de una estrategia de evolución continua que garantice la adaptación tecnológica, la mejora del rendimiento y la sostenibilidad del servicio en el tiempo.** Este requisito implica la existencia de procedimientos de actualización controlada, validación en entornos intermedios y planificación de ciclos de versionado.

La propuesta de empresa_s integra el sistema de correo dentro de una arquitectura global distribuida basada en RoundCube, QMail y almacenamiento en alta disponibilidad, incorporando mecanismos de replicación, backup y monitorización de parámetros operativos como colas, volumen o latencia. **Este enfoque aporta una base técnica adecuada desde el punto de vista estructural.** [\[03\_Doc\_Inv...MADRID\_v26 | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B42A3528C-3088-4F37-8DB7-CB7BDE01B619%7D&file=03_Doc_Invitacion_BAC06_2026_SISTEMAS_EDUCAMADRID_v26.docx&action=default&mobileredirect=true>)

Asimismo, el modelo planteado por empresa_s, basado en automatización y operación continua, sugiere una orientación hacia la mejora progresiva de los sistemas, lo cual resulta coherente con el requisito del pliego.

**No obstante, el desarrollo específico del subproyecto resulta limitado.** No se detallan planes concretos de actualización tecnológica de los componentes de correo ni estrategias de evolución de la arquitectura. Tampoco se describen procedimientos operativos para la realización de actualizaciones en entornos críticos, ni mecanismos de validación previa que garanticen la estabilidad del sistema tras los cambios.

La ausencia de herramientas específicas asociadas a la gestión del ciclo de vida de la infraestructura, así como la falta de métricas cuantificadas que permitan evaluar la mejora continua del servicio, limita la verificabilidad de la solución.

En consecuencia, la propuesta presenta una base técnica adecuada, pero con un desarrollo insuficiente en lo relativo a la evolución estructurada del sistema.

**Valoración cualitativa: Media**

## COR8 — Ampliación de servidores Mailbox

Este subproyecto requiere la capacidad de escalar el sistema de correo mediante la ampliación de servidores de buzones, lo que implica la definición de mecanismos de dimensionamiento, balanceo de carga, redistribución de usuarios y planificación de capacidad.

La propuesta de empresa_s contempla una arquitectura de almacenamiento distribuido con buzones en alta disponibilidad, basada en replicación y mecanismos de continuidad del servicio. **Este planteamiento permite inferir una base adecuada para soportar el crecimiento del número de servidores.** [\[03\_Doc\_Inv...MADRID\_v26 | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B42A3528C-3088-4F37-8DB7-CB7BDE01B619%7D&file=03_Doc_Invitacion_BAC06_2026_SISTEMAS_EDUCAMADRID_v26.docx&action=default&mobileredirect=true>)

Adicionalmente, la propuesta incluye un enfoque general de escalabilidad transversal en la plataforma, apoyado en balanceo y distribución de servicios, lo que constituye un elemento positivo en términos de capacidad de crecimiento.

**Sin embargo, el subproyecto no se desarrolla de forma específica desde el punto de vista operativo.** No se describen criterios de dimensionamiento de nuevos servidores, ni políticas de distribución de carga entre buzones, ni procedimientos detallados de ampliación en entornos productivos. Tampoco se identifican herramientas concretas para la gestión del escalado ni métricas que permitan anticipar necesidades de crecimiento.

La falta de planificación de capacidad a medio y largo plazo introduce incertidumbre sobre la capacidad real de adaptación del sistema a incrementos de carga.

En consecuencia, la solución resulta adecuada a nivel conceptual, pero con un desarrollo técnico limitado para su aplicación operativa.

**Valoración cualitativa: Media**

## COR9 — Módulo receptor de inyección directa

**El subproyecto COR9 implica la implantación de un componente técnico específico dentro de la infraestructura de correo, orientado a la recepción de envíos mediante inyección directa.** Este tipo de módulos requiere una definición precisa de arquitectura, integración con el sistema de transporte y mecanismos de control de seguridad y validación.

**El análisis de la propuesta de empresa_s pone de manifiesto que este subproyecto no se desarrolla de forma explícita dentro de la memoria técnica.** La descripción de la arquitectura de correo se mantiene en un nivel general, centrado en los componentes principales del sistema (RoundCube, QMail, mecanismos antispam y almacenamiento), sin incluir referencias específicas a módulos de inyección directa ni a su integración dentro del flujo de correo.

Asimismo, no se describen herramientas, procedimientos ni arquitecturas asociadas a este componente, ni se identifican mecanismos de validación, control de seguridad o gestión del tráfico asociado a la inyección directa.

Esta ausencia de desarrollo impide evaluar la capacidad real del licitador para implementar el módulo requerido, tanto desde el punto de vista técnico como operativo.

En consecuencia, la cobertura del requisito resulta claramente insuficiente.

**Valoración cualitativa: Baja**

## COR10 — Soporte del módulo de inyección directa

El subproyecto COR10 requiere la operación continua, mantenimiento y soporte del módulo de inyección directa, incluyendo la resolución de incidencias, monitorización del servicio y evolución del sistema.

**Dado que la propuesta de empresa_s no desarrolla la implementación inicial del módulo (COR9), tampoco se identifican elementos específicos asociados a su mantenimiento o soporte.** La memoria técnica no incluye procedimientos operativos, herramientas de monitorización ni estrategias de evolución para este componente.

Aunque el modelo general de operación planteado por empresa_s incluye monitorización, automatización y gestión de incidencias a nivel global, estos elementos no se concretan en el caso específico del módulo de inyección directa, lo que impide establecer una correspondencia directa con el requisito.

Asimismo, no se definen métricas de funcionamiento, ni acuerdos de nivel de servicio específicos, ni mecanismos de control que permitan evaluar el comportamiento del módulo en condiciones reales.

En consecuencia, la propuesta no proporciona información suficiente para valorar la viabilidad operativa del mantenimiento del módulo, lo que supone una cobertura claramente insuficiente del requisito.

**Valoración cualitativa: Baja**

## Conclusión del bloque COR

**El bloque de correo electrónico presenta una cobertura funcional básica basada en una arquitectura correcta, pero con un nivel de desarrollo técnico claramente insuficiente en aspectos críticos de operación, automatización y control avanzado.** La propuesta se centra en la infraestructura, pero no profundiza en los procedimientos operativos ni en los mecanismos de optimización requeridos en un entorno de gran escala.

La valoración global del bloque se sitúa en un nivel medio, con tendencia a media-baja en determinados subproyectos.

### BLOQUE MAX — SISTEMA OPERATIVO MAX

## Evaluación global del bloque MAX (MAX1–MAX14)

El bloque MAX comprende un conjunto amplio de subproyectos relacionados con el mantenimiento, desarrollo y soporte del sistema operativo MAX en centros educativos, incluyendo la generación de distribuciones, la asistencia técnica y la gestión de equipos.

**El análisis de la propuesta de empresa_s pone de manifiesto que, si bien se reconoce la existencia de este sistema dentro del ecosistema EducaMadrid, no se desarrolla un contenido técnico específico para abordarlo.** La memoria mantiene un enfoque generalista, integrando MAX dentro de la operación global del servicio, pero sin detallar actuaciones concretas asociadas a cada uno de los subproyectos requeridos.

No se describen procedimientos de mantenimiento presencial en centros, ni procesos de generación de distribuciones, ni mecanismos específicos de soporte remoto o gestión de repositorios. **Tampoco se identifican herramientas ni metodologías adaptadas a las particularidades del sistema MAX, lo que resulta especialmente relevante dado su carácter específico dentro del entorno educativo.**

En consecuencia, la propuesta presenta una ausencia significativa de contenido técnico evaluable para este bloque, lo que impide valorar positivamente su capacidad de ejecución en este ámbito.

Dado que los subproyectos MAX1 a MAX14 comparten esta carencia estructural, la valoración individualizada de cada uno de ellos se sitúa en un nivel homogéneo bajo.

**Valoración cualitativa (MAX1 a MAX14): Baja**

## Conclusión del bloque MAX

El bloque MAX constituye uno de los puntos más débiles de la propuesta de empresa_s. **La falta de desarrollo técnico específico, unida a la ausencia de procedimientos operativos y herramientas concretas, evidencia un insuficiente nivel de adaptación a los requisitos del pliego en este ámbito.**

Esta carencia tiene un impacto significativo en la valoración global del servicio, al tratarse de un componente relevante dentro del entorno EducaMadrid.

### BLOQUE AV — AULAS VIRTUALES

## AV1 — Actualización y comprobación de servidores de bases de datos de aulas virtuales

**El subproyecto AV1 exige la gestión periódica de las bases de datos asociadas a las aulas virtuales, incluyendo su actualización, validación de funcionamiento y control de rendimiento tanto en entornos físicos como virtuales.** Este requisito implica una coordinación estrecha entre infraestructura, bases de datos y servicios de aplicación.

**La propuesta de empresa_s aborda este subproyecto de forma indirecta a través de su planteamiento general sobre bases de datos y monitorización, incorporando mecanismos de revisión periódica, optimización y validación del estado de los sistemas.** Se aprecia una coherencia general con lo descrito en el bloque de bases de datos, especialmente en lo relativo a PostgreSQL y entornos de alta carga.

**No obstante, el análisis pone de manifiesto que no existe un desarrollo específico asociado a las aulas virtuales como sistema diferenciado.** No se describen procedimientos concretos para la validación periódica de servidores ni criterios específicos de actuación en este entorno, lo que limita la trazabilidad del cumplimiento del requisito.

En consecuencia, la cobertura puede considerarse parcial, basada en extrapolaciones de otros apartados de la propuesta.

**Valoración cualitativa: Media-Alta**

## AV2 — Mantenimiento de servidores FrontEnd de aulas virtuales

El subproyecto AV2 exige la gestión de los servidores de aplicación que soportan el acceso a las aulas virtuales, incluyendo su mantenimiento, actualización y optimización de rendimiento.

**La propuesta de empresa_s contempla arquitecturas de aplicaciones distribuidas con balanceo de carga y control de sesiones, lo que permite inferir una base técnica válida para la gestión de servidores frontend.** El enfoque multinivel planteado es coherente con este tipo de sistemas y permite garantizar una cierta escalabilidad del servicio.

**Sin embargo, no se desarrolla de forma específica el entorno de aulas virtuales ni los componentes concretos que lo constituyen, como Moodle u otras plataformas educativas.** Tampoco se describen procedimientos operativos asociados al mantenimiento, despliegue o actualización de estos servidores.

La ausencia de este nivel de detalle limita la evaluación del grado real de cumplimiento del requisito.

**Valoración cualitativa: Media**

## AV3 — Despliegue de nuevos grupos de aulas virtuales

**El subproyecto AV3 implica la capacidad de desplegar nuevos entornos de aulas virtuales de forma periódica, así como la ampliación de entornos existentes.** Este requisito es especialmente relevante en periodos de inicio de curso o incrementos de demanda.

La propuesta de empresa_s incorpora conceptos de automatización y despliegue mediante pipelines CI/CD y herramientas de configuración, lo que permite inferir una capacidad potencial para el despliegue automatizado de servicios.

**No obstante, la propuesta no describe procedimientos específicos de despliegue de aulas virtuales, ni define plantillas de entornos, ni establece tiempos de provisión ni mecanismos de validación tras el despliegue.** Esta falta de concreción limita la capacidad de evaluar la operatividad del proceso en escenarios reales.

En consecuencia, la cobertura del subproyecto resulta parcialmente insuficiente.

**Valoración cualitativa: Media**

## AV4 — Redistribución de NFS de datos

El subproyecto AV4 exige la redistribución periódica del almacenamiento asociado a las aulas virtuales, con el objetivo de equilibrar la carga y optimizar el rendimiento.

**La propuesta de empresa_s incluye en su modelo de operación mecanismos de redistribución de almacenamiento y gestión de capacidad, lo que permite abordar este requisito de forma indirecta.** Se contemplan procesos de análisis de ocupación y traslado de datos entre nodos, así como validaciones posteriores a la migración.

No obstante, no se desarrollan estrategias específicas para el entorno de aulas virtuales ni se definen criterios concretos de redistribución, como umbrales de ocupación o indicadores de rendimiento.

En consecuencia, la solución es técnicamente coherente pero insuficientemente desarrollada.

**Valoración cualitativa: Media-Alta**

## Conclusión del bloque AV

El bloque de aulas virtuales presenta una cobertura razonable basada en la extrapolación de soluciones definidas en otros ámbitos, especialmente en bases de datos y almacenamiento. **Sin embargo, la ausencia de desarrollo específico para este entorno limita la profundidad de la propuesta y evidencia una falta de adaptación directa al requisito.**

La valoración global del bloque se sitúa en un nivel medio-alto.

### BLOQUE POR — SERVICIO DE LDAP Y PORTAL EDUCATIVO

## POR1 — Ampliación del sistema de esclavos LDAP

El subproyecto POR1 implica la ampliación del sistema de replicación LDAP mediante la incorporación de nuevos nodos esclavos, lo que requiere una planificación cuidadosa de la replicación y el equilibrio de carga.

La propuesta de empresa_s incluye LDAP como uno de los pilares de su arquitectura, integrándolo con sistemas de identidad y control de acceso. **Este enfoque refleja una comprensión adecuada del papel de LDAP dentro del ecosistema EducaMadrid.**

**Sin embargo, no se describen procedimientos específicos para la ampliación del sistema de esclavos, ni estrategias de replicación, ni mecanismos de balanceo de carga entre nodos.** La falta de estos elementos limita la capacidad de evaluar la viabilidad técnica del proceso.

En consecuencia, la cobertura del requisito resulta parcial.

**Valoración cualitativa: Media**

## POR2 — Migración del sistema LDAP máster

El subproyecto POR2 exige la migración del nodo principal LDAP, lo que implica una operación crítica que requiere planificación, pruebas y mecanismos de contingencia.

La propuesta de empresa_s contempla LDAP dentro de su arquitectura, pero no desarrolla procesos de migración ni procedimientos asociados a este tipo de operaciones críticas.

No se describen fases de migración, ni entornos de pruebas, ni mecanismos de validación ni estrategias de rollback, aspectos fundamentales en este tipo de actuaciones.

En consecuencia, la propuesta presenta una carencia significativa en este subproyecto.

**Valoración cualitativa: Baja**

## Conclusión del bloque POR

El bloque de LDAP y portal presenta una cobertura limitada, basada en la integración conceptual del sistema dentro de la arquitectura general, pero sin desarrollo operativo suficiente para abordar los requisitos específicos del pliego.

La valoración global se sitúa en un nivel medio-bajo.

### BLOQUE SEG — SEGURIDAD

## SEG1 — Control de cambios en DNS

**El subproyecto SEG1 establece la necesidad de implementar mecanismos de control, seguimiento y auditoría sobre los cambios realizados en el sistema DNS, incluyendo validación previa, trazabilidad de modificaciones y capacidad de recuperación ante errores.** Este requisito resulta especialmente crítico en entornos con múltiples servicios interdependientes, donde cambios incorrectos en DNS pueden generar indisponibilidad generalizada.

**La propuesta de empresa_s integra la gestión de la infraestructura dentro de un modelo global que incorpora trazabilidad, control de accesos y registro de operaciones.** En particular, se hace referencia a la utilización de mecanismos de auditoría y control dentro de su arquitectura transversal, así como a la existencia de una CMDB y sistemas de automatización que permiten registrar cambios en el entorno.

Este enfoque resulta conceptualmente adecuado y permite inferir que los cambios en sistemas como DNS podrían quedar registrados dentro del modelo general de operación.

**No obstante, el análisis específico del subproyecto pone de manifiesto que no se desarrollan herramientas ni procedimientos concretos orientados al control de cambios en DNS.** No se describen flujos de aprobación, validación previa, control de versiones ni mecanismos de rollback específicos para este tipo de sistemas. Tampoco se identifican herramientas especializadas para la gestión de DNS ni métricas que permitan evaluar la estabilidad o integridad del sistema tras modificaciones.

Esta falta de desarrollo reduce el nivel de concreción técnica y limita la evaluación de la solución en términos de viabilidad operativa.

En consecuencia, la propuesta cubre el requisito desde una perspectiva general de control del sistema, pero no alcanza el grado de detalle necesario en el ámbito específico de DNS.

**Valoración cualitativa: Media**

## SEG2 — LDAP Máster para usuarios privilegiados

El subproyecto SEG2 requiere la implantación de un sistema LDAP máster independiente orientado a la gestión de usuarios privilegiados, incluyendo medidas reforzadas de seguridad, segregación de accesos y control estricto de identidades con elevados permisos.

La propuesta de empresa_s plantea una arquitectura de identidad centralizada basada en LDAP y SSO mediante Keycloak, integrando mecanismos de autenticación, control de accesos y gestión de sesiones dentro de un modelo transversal aplicable a toda la plataforma.

Este planteamiento evidencia una comprensión adecuada del modelo de gestión de identidades y del papel del LDAP como elemento central en la arquitectura de seguridad.

**Sin embargo, el análisis técnico muestra que la propuesta no desarrolla de forma específica la existencia de un LDAP máster independiente para usuarios privilegiados.** No se describen arquitecturas segregadas, ni mecanismos diferenciados de control de accesos, ni políticas de seguridad reforzadas para este tipo de usuarios. Tampoco se identifican procedimientos operativos de gestión de privilegios ni herramientas específicas orientadas a la protección de cuentas críticas.

Esta falta de diferenciación limita la alineación completa con el requisito, al tratar todos los usuarios dentro de un mismo modelo de identidad sin un tratamiento específico para cuentas privilegiadas.

En consecuencia, la propuesta presenta un buen enfoque general de identidad, pero no alcanza el nivel de especialización requerido.

**Valoración cualitativa: Media-Alta**

## SEG3 — Gestión de certificados

El subproyecto SEG3 exige la gestión integral del ciclo de vida de los certificados digitales, incluyendo su emisión, renovación, despliegue e implantación periódica en los sistemas de la plataforma.

La propuesta de empresa_s incluye la seguridad como elemento transversal, contemplando el uso de certificados dentro de su arquitectura general, especialmente en relación con comunicaciones seguras y autenticación entre componentes.

Se aprecia que el modelo de operación incorpora la actualización de componentes y la gestión continua de la seguridad, lo que permite inferir la existencia de procesos asociados a la renovación de certificados.

**No obstante, el desarrollo específico del subproyecto es limitado.** No se describen herramientas concretas de gestión de certificados, ni procedimientos de renovación automatizada, ni calendario de actualización anual. Tampoco se identifican mecanismos de control de caducidad, auditoría de certificados o validación tras su despliegue.

La ausencia de estos elementos introduce incertidumbre en la ejecución del proceso y limita la verificabilidad del cumplimiento del requisito.

**Valoración cualitativa: Media**

## SEG4 — Gestión de dominios DNS

Este subproyecto requiere la gestión continua de los dominios DNS, incluyendo su mantenimiento, actualización, control de integridad y resolución de incidencias.

La propuesta de empresa_s integra los sistemas de la plataforma dentro de un entorno gestionado y monitorizado, lo que permite inferir una base de gestión sobre servicios como DNS. **Se incorpora además un modelo de operación basado en automatización y control de cambios que resulta coherente con este tipo de tareas.**

**Sin embargo, no se desarrollan aspectos específicos relacionados con la gestión de dominios DNS.** No se describen herramientas de administración, ni procedimientos operativos de mantenimiento, ni mecanismos de detección de inconsistencias o errores de resolución.

Asimismo, no se incluyen métricas operativas ni indicadores de rendimiento que permitan evaluar el estado del sistema DNS.

En consecuencia, la cobertura del requisito se mantiene en un nivel general, sin un desarrollo técnico específico.

**Valoración cualitativa: Media**

## SEG5 — Análisis de vulnerabilidades

El subproyecto SEG5 exige la implementación de procesos continuos de detección, análisis y corrección de vulnerabilidades en los sistemas de la plataforma.

La propuesta de empresa_s contempla la seguridad como un elemento integrado, incluyendo la monitorización continua de amenazas, la identificación de vulnerabilidades y la resolución de incidencias en plazos definidos, como por ejemplo la corrección de vulnerabilidades críticas en periodos inferiores a 24 horas.

Este enfoque representa un aspecto positivo, ya que introduce un componente de operación continua alineado con las buenas prácticas de seguridad.

**No obstante, el desarrollo técnico específico es limitado.** No se identifican herramientas concretas de análisis de vulnerabilidades (como escáneres específicos), ni metodologías definidas (por ejemplo, análisis automático frente a auditorías manuales). Tampoco se describen procesos detallados de clasificación, priorización o seguimiento de vulnerabilidades.

La ausencia de métricas cuantificadas y procedimientos operativos detallados limita la capacidad de evaluar la eficacia del modelo propuesto.

**Valoración cualitativa: Media-Alta**

## SEG6 — Sistema de detección de intrusiones

El subproyecto SEG6 exige la implantación y operación efectiva de sistemas de detección de intrusiones, monitorización de integridad, análisis de logs y respuesta ante incidentes, incluyendo tanto la capacidad de detección temprana como la definición de procedimientos estructurados de actuación.

**La propuesta de empresa_s incorpora la monitorización continua y la centralización de logs dentro de su modelo de observabilidad, integrando la recogida de métricas, eventos y trazas en una arquitectura transversal.** Asimismo, se contempla la detección temprana de incidentes y la supervisión constante del sistema, lo que evidencia una orientación hacia la seguridad operativa continua.

Este enfoque resulta alineado con los principios básicos del subproyecto y aporta una base funcional adecuada para la identificación de anomalías y eventos de seguridad.

**No obstante, el desarrollo técnico específico presenta limitaciones.** No se identifican herramientas concretas de detección de intrusiones (IDS/IPS), ni arquitecturas definidas de análisis centralizado (por ejemplo, SIEM), ni mecanismos de correlación avanzada de eventos. Tampoco se describen procedimientos detallados de respuesta ante incidentes, incluyendo clasificación de eventos, niveles de criticidad o flujos de actuación.

Asimismo, no se incluyen métricas cuantificadas relacionadas con tiempos de detección, respuesta o resolución, lo que limita la capacidad de evaluar la eficacia del sistema de seguridad.

En consecuencia, la propuesta presenta una base conceptual adecuada en materia de observabilidad y monitorización, pero con un desarrollo insuficiente en lo relativo a la operación estructurada de la detección y respuesta ante incidentes.

**Valoración cualitativa: Media**

## SEG7 — Auditorías internas de aplicaciones

El subproyecto SEG7 requiere la ejecución periódica de auditorías internas sobre las aplicaciones de la plataforma, incluyendo análisis de vulnerabilidades, revisión de configuraciones y control de calidad de código.

La propuesta de empresa_s integra prácticas de seguridad dentro del ciclo de vida del desarrollo, apoyándose en un modelo DevOps con automatización y validación continua. **Este enfoque permite incorporar controles de calidad en fases tempranas del desarrollo y constituye una base adecuada para la realización de auditorías.**

**Sin embargo, el análisis evidencia que no se desarrollan procedimientos específicos de auditoría.** No se detallan metodologías concretas (auditorías estáticas, dinámicas, revisión de código), ni herramientas utilizadas ni periodicidad de ejecución. Tampoco se describen entregables asociados a estas auditorías, como informes de vulnerabilidades o planes de remediación.

La ausencia de estos elementos limita la capacidad de evaluar la madurez del proceso y su aplicabilidad en entornos reales.

En consecuencia, la cobertura del requisito es adecuada a nivel conceptual, pero insuficiente en su desarrollo operativo.

**Valoración cualitativa: Media**

## SEG8 — Auditorías internas continuas de sistemas

El subproyecto SEG8 amplía el alcance de las auditorías al conjunto de sistemas, requiriendo un modelo continuo de supervisión y evaluación de la seguridad.

La propuesta de empresa_s incorpora elementos de monitorización continua, trazabilidad y control de actividad dentro de su arquitectura global, lo que permite inferir una cierta capacidad para la supervisión continuada del entorno.

**No obstante, el concepto de auditoría continua no se desarrolla de forma específica.** No se describen procesos automatizados de evaluación periódica, ni herramientas orientadas a auditoría continua, ni mecanismos de revisión sistemática de configuraciones o estados del sistema.

Asimismo, no se identifican indicadores de control ni métricas que permitan medir el nivel de cumplimiento de los estándares de seguridad a lo largo del tiempo.

En consecuencia, la propuesta presenta un enfoque coherente desde la perspectiva de monitorización continua, pero no alcanza el nivel de formalización requerido para auditorías continuas estructuradas.

**Valoración cualitativa: Media**

## SEG9 — Logs centralizados

El subproyecto SEG9 exige la implantación de un sistema de centralización de logs que permita su análisis, correlación y explotación para seguridad y operación.

**La propuesta de empresa_s contempla explícitamente la centralización de logs dentro de su modelo de observabilidad, integrando la recogida de información procedente de múltiples sistemas y su análisis conjunto.** Este enfoque constituye uno de los puntos más sólidos del bloque, ya que permite habilitar capacidades de monitorización avanzada y trazabilidad completa del sistema.

Se valora positivamente la integración de logs, métricas y trazas dentro de una estrategia unificada, lo que facilita la detección de anomalías y el análisis de comportamiento del sistema.

**Sin embargo, el desarrollo técnico presenta ciertas limitaciones.** No se identifican herramientas concretas utilizadas para la centralización y análisis de logs (por ejemplo, ELK o soluciones equivalentes), ni se describen arquitecturas detalladas de ingestión, almacenamiento y procesamiento. Tampoco se definen políticas de retención de logs ni niveles de acceso a la información.

A pesar de estas carencias, la claridad del enfoque y su integración dentro del modelo global de observabilidad permiten valorar positivamente este subproyecto.

**Valoración cualitativa: Alta**

## SEG10 — Claves RSA unificadas

El subproyecto SEG10 exige la gestión unificada de claves criptográficas, incluyendo su generación, almacenamiento, rotación y uso en los distintos sistemas de la plataforma.

La propuesta de empresa_s incorpora la seguridad y el cifrado como elementos transversales dentro de su arquitectura, incluyendo la protección de comunicaciones y el control de accesos.

**No obstante, no se desarrolla de forma específica la gestión de claves RSA.** No se describen procedimientos de generación, distribución o rotación de claves, ni herramientas específicas para su gestión centralizada. Tampoco se identifican mecanismos de control de acceso a claves ni auditoría de su uso.

La ausencia de este desarrollo limita la alineación con el requisito, especialmente en lo relativo a la gestión operativa de claves.

En consecuencia, la cobertura del subproyecto resulta parcial.

**Valoración cualitativa: Media**

## SEG11 — Soporte en eventos de Ciberseguridad

Este subproyecto requiere la prestación de soporte presencial en eventos relacionados con la ciberseguridad, incluyendo tareas de asistencia, despliegue técnico y soporte operativo.

La propuesta de empresa_s incluye un modelo de servicio con capacidades de soporte y operación sobre la plataforma, así como un equipo técnico con competencias en seguridad y sistemas, lo que permite inferir la capacidad de prestar este tipo de servicios dentro del marco general del contrato.

**Sin embargo, el desarrollo específico del subproyecto es limitado.** No se describen planes de actuación en eventos, ni roles definidos, ni procedimientos operativos asociados a este soporte. Tampoco se identifican recursos asignados específicamente a este tipo de actividades.

La falta de concreción impide evaluar con precisión el nivel de preparación para este tipo de actuaciones.

En consecuencia, la propuesta cubre el requisito de forma genérica, pero sin un desarrollo específico suficiente.

**Valoración cualitativa: Media**

## Conclusión del bloque SEG

El bloque de seguridad presenta una cobertura suficiente en aspectos generales, destacando la centralización de logs, pero con carencias importantes en la definición detallada de herramientas y procedimientos específicos.

La valoración global se sitúa en un nivel medio.

### BLOQUE CON — AUTOMATIZACIÓN Y CONTENEDORES

## CON1 — Sistema de gestión de contenedores

El subproyecto CON1 establece la necesidad de gestionar una infraestructura basada en contenedores, incluyendo la operación, mantenimiento y evolución de la plataforma de ejecución, así como la gestión de despliegues en entornos distribuidos.

La propuesta de empresa_s aborda este subproyecto mediante la inclusión de contenedores como parte de su estrategia tecnológica, incorporando el uso de Docker y la integración con pipelines de integración continua. **Este enfoque demuestra una orientación adecuada hacia modelos modernos de despliegue y operación de servicios, alineándose con los principios DevOps.**

**No obstante, el análisis técnico pone de manifiesto que la propuesta no desarrolla de forma completa la arquitectura de contenedores.** En particular, no se identifican plataformas de orquestación como Kubernetes ni se describen mecanismos de gestión de clusters, escalabilidad automática o tolerancia a fallos. La ausencia de estos elementos limita significativamente la capacidad de evaluar la madurez del sistema propuesto en entornos de producción complejos.

Asimismo, el propio planteamiento indica en algunos casos que el uso de determinadas tecnologías se encuentra en fase de análisis o evaluación, lo que introduce un grado de incertidumbre sobre su aplicación real en el servicio.

En consecuencia, la solución resulta conceptualmente adecuada pero insuficientemente desarrollada para garantizar su aplicabilidad en un entorno de gran escala.

**Valoración cualitativa: Media**

## CON2 — Automatización de tareas

El subproyecto CON2 requiere la implantación de sistemas automatizados para la ejecución de tareas operativas recurrentes, incluyendo la gestión de configuraciones, despliegues y mantenimiento de sistemas.

**La propuesta de empresa_s incorpora la automatización como uno de los pilares fundamentales de su modelo operativo, incluyendo el uso de herramientas como Ansible y la integración de pipelines CI/CD para la gestión de despliegues y configuraciones.** Este enfoque se encuentra alineado con las buenas prácticas actuales y aporta un nivel significativo de eficiencia en la operación del servicio.

La automatización propuesta permite reducir la intervención manual, mejorar la trazabilidad de las actuaciones y minimizar errores operativos, lo que constituye un elemento positivo en un entorno de alta complejidad.

Sin embargo, no se identifican sistemas centralizados de orquestación ni plataformas específicas para la gestión global de automatizaciones, lo que limita la capacidad de escalar este enfoque de forma estructurada a todos los sistemas de la plataforma.

A pesar de esta limitación, el subproyecto presenta una cobertura adecuada y consistente con el planteamiento general de la propuesta.

**Valoración cualitativa: Alta**

## CON3 — Sistema auxiliar de automatización

El subproyecto CON3 implica la existencia de sistemas complementarios de automatización orientados a tareas específicas que no quedan cubiertas por los sistemas principales.

**La propuesta de empresa_s no desarrolla de forma específica este subproyecto, limitándose a describir de forma general la automatización dentro de su modelo operativo.** No se identifican herramientas diferenciadas ni casos de uso concretos que permitan evaluar la funcionalidad de estos sistemas auxiliares.

Esta falta de concreción reduce la capacidad de valorar la solución y pone de manifiesto una cobertura limitada del requisito.

**Valoración cualitativa: Media-Baja**

## Conclusión del bloque CON

El bloque de automatización y contenedores presenta una orientación técnica adecuada, especialmente en lo relativo a la automatización de tareas, pero adolece de una falta de madurez en la definición de arquitecturas de contenedores y sistemas de orquestación.

La valoración global del bloque se sitúa en un nivel medio, condicionado por la escasa definición de elementos clave en entornos distribuidos.

### BLOQUE MIG — MIGRACIÓN DE SERVIDORES ENTRE CPDs

## MIG1 — Coordinación y planificación de entornos migrados

El subproyecto MIG1 establece la necesidad de coordinar y planificar la revisión de los entornos una vez realizada la migración, incluyendo la validación del correcto funcionamiento de los servicios, la detección de incidencias y la verificación de la integridad del sistema.

**La propuesta de empresa_s incorpora un modelo de operación basado en la trazabilidad, monitorización continua y control del servicio, lo que permite inferir una base adecuada para la supervisión de entornos migrados.** En particular, la existencia de monitorización integral, registros de actividad y control de la operación facilita la detección de posibles desviaciones tras la migración.

Asimismo, el modelo de gobierno multinivel (estratégico, táctico y operativo) descrito en la propuesta permite entender que existiría una estructura organizativa capaz de coordinar este tipo de actividades, lo que representa un alineamiento conceptual con el requisito.

**No obstante, el desarrollo específico del subproyecto es limitado.** No se describen planes concretos de revisión post-migración, ni procedimientos de validación estructurados, ni criterios de aceptación de los entornos migrados. Tampoco se identifican herramientas específicas para la verificación del estado de los sistemas ni métricas que permitan evaluar objetivamente el éxito de la migración.

En consecuencia, la propuesta ofrece una base funcional adecuada desde el punto de vista de monitorización y control, pero carece de un desarrollo operativo detallado en lo relativo a la coordinación y revisión de entornos migrados.

**Valoración cualitativa: Media**

## MIG2 — Fases preparatorias y planificación técnica

El subproyecto MIG2 requiere la definición de las fases previas a la migración, incluyendo planificación técnica, análisis de riesgos, definición de dependencias y estructuración del proceso de traslado de sistemas entre CPDs.

**La propuesta de empresa_s incorpora un enfoque metodológico que incluye planificación, análisis de riesgos y gestión de contingencias, lo que constituye un elemento positivo alineado con este tipo de procesos.** En particular, la inclusión de un plan de riesgos y de un plan de contingencia sugiere una aproximación estructurada a la gestión de cambios complejos.

Asimismo, el modelo DevOps planteado, junto con la validación en entornos de preproducción y el control de despliegues, aporta una base conceptual adecuada para abordar migraciones de sistemas de forma controlada.

**Sin embargo, el análisis técnico evidencia que no se desarrollan de forma específica las fases preparatorias de la migración.** No se describen planes detallados por sistemas, análisis de dependencias entre servicios, cronogramas de migración ni estrategias de priorización. Tampoco se definen mecanismos de coordinación entre equipos ni herramientas específicas de planificación de migraciones.

Esta falta de concreción limita la capacidad de evaluar la viabilidad real del proceso en un entorno de alta complejidad.

En consecuencia, la propuesta presenta una buena base metodológica, pero con un nivel de desarrollo técnico insuficiente en la planificación específica de la migración.

**Valoración cualitativa: Media-Alta**

## MIG3 — Preparación de servidores y documentación

El subproyecto MIG3 implica la preparación de los servidores para la migración, así como la generación y actualización de documentación técnica de los sistemas, incluyendo configuraciones, dependencias y estado operativo.

**La propuesta de empresa_s incluye la utilización de una CMDB como “fuente única de verdad”, junto con procesos de automatización y gestión de configuración, lo que representa un elemento relevante para la documentación y control de los sistemas.** Este enfoque facilita la trazabilidad de componentes y la identificación de dependencias, aspectos clave en procesos de migración. [\[03\_Doc\_Inv...MADRID\_v26 | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B42A3528C-3088-4F37-8DB7-CB7BDE01B619%7D&file=03_Doc_Invitacion_BAC06_2026_SISTEMAS_EDUCAMADRID_v26.docx&action=default&mobileredirect=true>)

Asimismo, la integración de herramientas como Ansible y CI/CD dentro del modelo operativo permite inferir la capacidad de automatizar la preparación de entornos y la configuración de servidores, lo que constituye un punto positivo.

**No obstante, el desarrollo específico del subproyecto presenta limitaciones.** No se describen procedimientos concretos de preparación de servidores, ni checklists de validación previa a la migración, ni formatos estructurados de documentación técnica. Tampoco se detallan mecanismos de actualización continua de la documentación ni su validación tras los cambios.

Adicionalmente, no se identifican métricas de calidad de la documentación ni herramientas específicas para su gestión.

En consecuencia, la propuesta ofrece una base coherente en términos de gestión de configuración, pero no alcanza el nivel de detalle requerido para una preparación sistemática y documentada de los entornos.

El subproyecto MIG4 exige la comprobación exhaustiva del éxito de la migración, incluyendo validación funcional, verificación de integridad de datos, comprobación de rendimiento y detección de posibles incidencias.

**La propuesta de empresa_s incorpora mecanismos de monitorización continua, pruebas en entornos de preproducción y validación previa a despliegues, lo que constituye una base adecuada para la verificación de cambios en la plataforma.** Asimismo, el uso de métricas y observabilidad permite identificar desviaciones en el comportamiento del sistema.

Este enfoque resulta coherente con el objetivo del subproyecto y aporta elementos relevantes para la validación de entornos migrados.

**Sin embargo, el análisis técnico evidencia que no se desarrollan procedimientos específicos de verificación de migración.** No se describen planes de pruebas estructurados, ni criterios de aceptación, ni validaciones diferenciadas por tipo de sistema (datos, aplicaciones, servicios). Tampoco se incluyen métricas cuantificadas que permitan determinar objetivamente el éxito de la migración.

La falta de estos elementos limita la capacidad de evaluar la robustez del proceso de verificación.

En consecuencia, la propuesta presenta una base funcional adecuada en términos de monitorización y validación general, pero no desarrolla de forma específica la verificación de migraciones complejas.

**Valoración cualitativa: Media-Alta**

## MIG5 — Mantenimiento tras la migración

El subproyecto MIG5 requiere garantizar el soporte y mantenimiento de los sistemas una vez realizada la migración, incluyendo la resolución de incidencias, ajustes operativos y seguimiento del comportamiento del sistema en el nuevo entorno.

**La propuesta de empresa_s contempla un modelo de operación continua basado en monitorización, gestión de incidencias y soporte 24/7 para entornos críticos, lo que constituye un elemento claramente alineado con este requisito.** Asimismo, el enfoque de trazabilidad completa y control del servicio facilita el seguimiento de incidencias y actuaciones.

Se valora positivamente la integración de estos mecanismos dentro del modelo general de operación, ya que permiten una supervisión continua del sistema tras cambios significativos como una migración.

**No obstante, el desarrollo específico del subproyecto es limitado.** No se describen planes de soporte específicos post-migración, ni procedimientos de estabilización del sistema, ni mecanismos de seguimiento adaptados a este contexto. Tampoco se identifican métricas específicas de estabilidad post-migración ni indicadores que permitan evaluar la evolución del sistema tras el cambio.

Esta falta de especialización reduce la capacidad de evaluar la eficiencia del soporte en escenarios de migración.

En consecuencia, la propuesta cubre adecuadamente el mantenimiento general del sistema, pero no desarrolla con suficiente detalle las particularidades del soporte tras migraciones.

**Valoración cualitativa: Media-Alta**

## Conclusión del bloque MIG

El bloque de migración presenta una **base metodológica coherente**, apoyada en elementos como la monitorización, la automatización, la gestión de riesgos y la trazabilidad, lo que permite abordar procesos de cambio complejos desde una perspectiva estructurada.

No obstante, el análisis revela una **falta sistemática de desarrollo técnico específico en los subproyectos**, especialmente en lo relativo a planificación detallada, procedimientos operativos, herramientas concretas y métricas de verificación.

Esta diferencia entre el enfoque conceptual y la concreción operativa introduce incertidumbre sobre la ejecución efectiva de migraciones en un entorno de alta complejidad como el de EducaMadrid.

**Valoración global del bloque MIG: Media-Alta**.

### BLOQUE IA — INTELIGENCIA ARTIFICIAL

## IA1 — Evaluación del rendimiento de modelos

El subproyecto IA1 requiere la evaluación sistemática del rendimiento de los modelos de inteligencia artificial utilizados en la plataforma, incluyendo la definición de métricas de calidad, análisis de resultados y validación continua de su comportamiento en entornos reales.

La propuesta de empresa_s incorpora la inteligencia artificial como un elemento transversal dentro de la arquitectura, integrando su uso en diferentes ámbitos como analítica, automatización y servicios educativos. **En particular, se plantea la evaluación continua del comportamiento de los modelos mediante indicadores como precisión, errores y sesgos, lo que evidencia una comprensión adecuada de la necesidad de medir el rendimiento de estos sistemas.**

Asimismo, se describe el uso de mecanismos de monitorización asociados a los servicios de IA, incluyendo parámetros de funcionamiento y calidad de respuesta, lo que aporta un enfoque coherente con la necesidad de supervisión continua.

**No obstante, el desarrollo técnico específico presenta limitaciones relevantes.** No se definen métricas concretas ni umbrales de aceptación asociados a los modelos, ni metodologías de evaluación estructuradas. Tampoco se describen datasets de validación, procedimientos de benchmarking ni herramientas específicas para la medición del rendimiento.

Esta falta de cuantificación y formalización limita la verificabilidad del modelo de evaluación y dificulta su aplicación en entornos operativos donde es necesario justificar el comportamiento de los sistemas de IA.

En consecuencia, la propuesta contempla la evaluación del rendimiento desde un enfoque conceptual adecuado, pero con un nivel de desarrollo técnico insuficiente para su aplicación sistemática.

**Valoración cualitativa: Media-Alta**

## IA2 — Ingeniería de prompts

El subproyecto IA2 exige el diseño y gestión de prompts específicos adaptados a los distintos servicios de la plataforma, incluyendo su optimización, control de versiones y adecuación al contexto educativo.

La propuesta de empresa_s incorpora explícitamente el concepto de “gobierno de prompts”, incluyendo aspectos como el versionado, la aprobación y la trazabilidad de los mismos. **Este elemento constituye uno de los puntos más destacados del bloque, ya que introduce un enfoque estructurado en la gestión de la interacción con modelos de lenguaje.**

Asimismo, se contempla la integración de la IA en distintos servicios, lo que implica la adaptación de prompts a diferentes casos de uso, mostrando una comprensión adecuada del requisito.

**No obstante, el desarrollo técnico presenta ciertas limitaciones.** No se describen herramientas específicas para la gestión de prompts, ni metodologías de optimización (por ejemplo, técnicas de evaluación iterativa o ajuste fino de prompts). Tampoco se identifican métricas que permitan evaluar la calidad o eficacia de los prompts en los distintos servicios.

Adicionalmente, no se detalla cómo se gestionará la evolución de estos prompts ni su validación en entornos reales de uso.

En consecuencia, la propuesta presenta un enfoque conceptual sólido y alineado con buenas prácticas emergentes, pero con una concreción técnica limitada en su desarrollo.

**Valoración cualitativa: Media-Alta**

## IA3 — Testeo de guardarraíles

El subproyecto IA3 requiere la definición y validación de mecanismos de control (guardarraíles) que garanticen que los sistemas de IA operen dentro de los límites adecuados para un entorno educativo, evitando respuestas inapropiadas o inseguras.

**La propuesta de empresa_s incorpora mecanismos de control y supervisión asociados al uso de la IA, incluyendo auditoría de consultas, registro de resultados, control de acceso a datos y validación de respuestas en usos críticos.** Asimismo, se contempla la supervisión humana como elemento de control, lo que constituye un aspecto relevante en entornos sensibles como el educativo.

Este enfoque demuestra una comprensión adecuada de la necesidad de establecer límites operativos en sistemas basados en IA.

**Sin embargo, el desarrollo específico del subproyecto presenta limitaciones.** No se describen mecanismos concretos de implementación de guardarraíles (filtros de contenido, clasificación previa/posterior, validación automática), ni escenarios de prueba estructurados para su validación. Tampoco se definen métricas que permitan evaluar la eficacia de estos controles ni procedimientos de ajuste continuo.

La ausencia de estos elementos reduce la capacidad de evaluar la robustez del sistema en la práctica.

En consecuencia, la propuesta aborda adecuadamente el concepto de control de IA, pero sin desarrollar en profundidad los mecanismos técnicos asociados a su implantación.

**Valoración cualitativa: Media-Alta**

## IA4 — Integración en aplicativos

El subproyecto IA4 exige analizar la integración de capacidades de IA en diferentes componentes de la plataforma, evaluando su viabilidad técnica y su impacto en los servicios existentes.

**La propuesta de empresa_s incorpora la IA como un elemento transversal, integrándola en diferentes áreas como analítica, automatización, generación de contenido y mejora de la experiencia de usuario.** Asimismo, se plantean casos de uso concretos como generación de preguntas, análisis de contenido o automatización de procesos, lo que evidencia una visión amplia de integración.

Este planteamiento resulta coherente con el requisito y demuestra una comprensión adecuada de las posibilidades de incorporación de IA en la plataforma.

**No obstante, el análisis técnico evidencia que no se desarrollan evaluaciones estructuradas de integración.** No se describen análisis de viabilidad técnica por sistema, ni arquitecturas específicas de integración, ni planes de despliegue progresivo. Tampoco se identifican herramientas concretas ni mecanismos de control del impacto en los sistemas existentes.

Esta falta de detalle limita la capacidad de evaluar la aplicabilidad real de las integraciones propuestas.

En consecuencia, la propuesta presenta una visión conceptual sólida, pero con un nivel de desarrollo técnico limitado en la evaluación e implementación de integraciones.

**Valoración cualitativa: Media-Alta**

## IA5 — Evaluación de capacidades y límites por usuario

El subproyecto IA5 requiere la definición de límites de uso de los sistemas de IA por usuario, incluyendo restricciones de consumo, control de acceso y evaluación del comportamiento del sistema ante diferentes cargas.

**La propuesta de empresa_s contempla el análisis de la capacidad de respuesta de los sistemas de IA, incluyendo aspectos relacionados con el rendimiento, el consumo de recursos y el comportamiento de los modelos.** Asimismo, se menciona la evaluación de límites de uso y la necesidad de controlar la interacción de los usuarios con los sistemas de IA.

Este enfoque resulta coherente con el requisito y evidencia una comprensión de la necesidad de regular el uso de estos sistemas.

**Sin embargo, el desarrollo técnico presenta limitaciones.** No se definen políticas concretas de limitación por usuario, ni mecanismos de control de consumo, ni herramientas específicas de gestión de uso. Tampoco se describen métricas cuantificadas ni umbrales de funcionamiento que permitan evaluar el comportamiento del sistema bajo diferentes niveles de carga.

La ausencia de estos elementos limita la capacidad de evaluar la viabilidad operativa del control de uso de los sistemas de IA.

En consecuencia, la propuesta cubre adecuadamente el concepto del requisito, pero con un nivel de detalle insuficiente para su implementación práctica.

**Valoración cualitativa: Media-Alta**

## Conclusión del bloque IA

El bloque de inteligencia artificial presenta una **orientación claramente avanzada y alineada con tendencias actuales**, destacando especialmente la integración transversal de la IA, el control de prompts y la incorporación de mecanismos de supervisión y auditoría.

No obstante, el análisis detallado de los subproyectos pone de manifiesto una **falta de concreción técnica en aspectos clave**, como la definición de métricas cuantificadas, herramientas específicas, procedimientos operativos y mecanismos de validación estructurada.

Esta diferencia entre la ambición conceptual y la madurez operativa limita la verificabilidad de la solución y su aplicación en entornos reales de explotación.

En términos globales, el bloque presenta un **nivel medio-alto**, condicionado por la falta de desarrollo técnico detallado.

**Valoración global del bloque IA: Media-Alta**

## EVALUACIÓN DE LA SOLUCIÓN TÉCNICA (CRITERIOS 7.2.2)

### EVALUACIÓN DE LA SOLUCIÓN TÉCNICA OFERTADA (HASTA 15 PUNTOS)

De conformidad con lo establecido en el apartado 7.2.2 del Documento de Invitación, la evaluación de la solución técnica ofertada se realiza atendiendo a los subcriterios definidos en dicho apartado, que comprenden la arquitectura planteada, el grado de comprensión de los requisitos, la viabilidad general del proyecto, la metodología de trabajo, el rendimiento previsible de las soluciones aportadas y el nivel de satisfacción de los requisitos recogidos en el Anexo II.

La valoración se ha efectuado considerando el contenido íntegro de la memoria técnica presentada por empresa_s, analizando la adecuación real de las soluciones propuestas a los distintos bloques funcionales del contrato y verificando el grado de desarrollo técnico, la existencia de herramientas concretas, la definición de procedimientos operativos, la coherencia arquitectónica y la capacidad efectiva de ejecución del servicio en un entorno de elevada complejidad tecnológica como EducaMadrid. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

A efectos de la presente evaluación, se considera especialmente relevante el criterio de verificabilidad de la solución, entendiendo como tal la capacidad de acreditar de manera objetiva cómo se ejecutarán los distintos trabajos mediante procedimientos, herramientas, automatizaciones, mecanismos de control y métricas asociadas.

#### Arquitectura planteada en los distintos subproyectos (máximo 2 puntos)

**La propuesta presentada por empresa_s incorpora una arquitectura técnica global claramente definida, estructurada mediante un enfoque multinivel orientado a la integración de servicios, automatización de procesos y operación de infraestructuras complejas.** La memoria describe de forma consistente distintos componentes transversales como LDAP, SSO, monitorización, automatización CI/CD, bases de datos, cloud, servicios colaborativos e inteligencia artificial, estableciendo relaciones funcionales entre ellos y configurando un modelo arquitectónico homogéneo para el conjunto de la plataforma. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

**La propuesta destaca especialmente en ámbitos como bases de datos, monitorización, automatización y observabilidad, donde se identifican arquitecturas diferenciadas por tecnología, incluyendo entornos MariaDB, PostgreSQL, ProxySQL, Prometheus, Grafana, JMeter, Docker y sistemas de integración continua.** Este planteamiento aporta un nivel relevante de coherencia técnica y permite comprender cómo se articula la prestación efectiva de los servicios. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Asimismo, se aprecia una adaptación razonable a las particularidades de los distintos bloques incluidos en el Anexo II, evitando en numerosos casos enfoques genéricos y desarrollando soluciones específicas según la naturaleza de cada sistema. **Este aspecto resulta especialmente visible en los bloques de bases de datos, monitorización, streaming, videoconferencia y observabilidad.** [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

**No obstante, la propuesta presenta limitaciones relevantes en determinados ámbitos.** En particular, algunos bloques muestran un desarrollo arquitectónico claramente inferior al observado en las áreas principales, especialmente en determinados servicios de correo electrónico, cloud, LDAP, contenedores y, de manera especialmente significativa, en el bloque MAX, donde no existe una arquitectura específica que permita evaluar adecuadamente la capacidad de ejecución del servicio. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Asimismo, en algunos subproyectos se identifican referencias a futuras evoluciones o tecnologías pendientes de definición, lo que introduce un cierto nivel de incertidumbre sobre la arquitectura final de determinados componentes. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

En consecuencia, la propuesta presenta una arquitectura técnicamente sólida, bien estructurada y con un elevado grado de coherencia, aunque sin alcanzar un nivel plenamente excelente debido a la heterogeneidad observada en determinados bloques del alcance.

**La valoración asignada a este subcriterio asciende a 1,50 puntos sobre un máximo de 2 puntos.**

#### Grado de comprensión de los requisitos planteados (máximo 2 puntos)

**La memoria técnica evidencia una comprensión amplia y detallada del alcance funcional y tecnológico del contrato.** A lo largo de la propuesta se identifican correctamente los distintos ámbitos de actuación definidos en el Anexo II, así como las relaciones existentes entre los múltiples sistemas que componen la plataforma EducaMadrid. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Esta comprensión se manifiesta especialmente en la capacidad de diferenciar tecnologías, necesidades operativas y mecanismos de gestión según la naturaleza de cada servicio. **La propuesta no se limita a reproducir los requisitos del pliego, sino que desarrolla soluciones específicas para bases de datos, monitorización, sistemas colaborativos, videoconferencia, automatización, gestión de identidades y entornos cloud.** [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Asimismo, se aprecia una adecuada comprensión de los principales retos asociados a la operación de una plataforma de elevada complejidad, incluyendo aspectos como la escalabilidad, la automatización, la observabilidad, la continuidad del servicio y la gestión de grandes volúmenes de usuarios y sistemas. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

**No obstante, el análisis detallado permite observar que esta comprensión no se traduce con la misma intensidad en todos los bloques funcionales.** Existen ámbitos donde el nivel de desarrollo técnico resulta claramente inferior, destacando especialmente MAX, determinados subproyectos de correo electrónico, algunas actuaciones específicas de LDAP y varios servicios auxiliares. Estas limitaciones impiden considerar la cobertura de requisitos como completamente homogénea. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

En conjunto, la propuesta demuestra un elevado conocimiento del entorno objeto del contrato y una comprensión significativamente superior a la observada en otras propuestas evaluadas, aunque sin alcanzar un nivel excelente debido a las carencias detectadas en determinados ámbitos concretos.

**La puntuación asignada a este subcriterio asciende a 1,50 puntos sobre un máximo de 2 puntos.**

#### Viabilidad del proyecto en general (máximo 1 punto)

**Desde una perspectiva global, la propuesta presenta un nivel adecuado de viabilidad técnica y organizativa.** La existencia de arquitecturas definidas, procedimientos operativos, automatización, herramientas concretas y una visión coherente de los distintos sistemas permite considerar que existe una base razonable para la ejecución efectiva del servicio. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

La utilización de tecnologías ampliamente implantadas en el sector, tales como Ansible, Prometheus, Grafana, Docker, Keycloak, JMeter o GitLab, contribuye a reforzar la credibilidad técnica del planteamiento y favorece su implementación en condiciones reales de explotación. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Adicionalmente, la propuesta incorpora mecanismos de automatización y observabilidad que permiten mejorar la eficiencia operativa y reducir riesgos asociados a la gestión manual de infraestructuras complejas. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

**Sin embargo, la viabilidad global se ve parcialmente condicionada por determinadas carencias detectadas en algunos bloques específicos.** La ausencia de desarrollo suficiente en MAX, junto con la escasa concreción observada en determinados ámbitos de correo electrónico, LDAP, cloud y contenedores, introduce incertidumbre sobre la ejecución homogénea de la totalidad del alcance contractual. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Asimismo, la falta recurrente de indicadores cuantificables, métricas operativas y objetivos medibles limita en algunos casos la posibilidad de verificar objetivamente el comportamiento esperado de las soluciones propuestas. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

En conjunto, el proyecto puede considerarse viable, aunque con determinados elementos susceptibles de mejora.

**La valoración asignada asciende a 0,65 puntos sobre un máximo de 1 punto.**

#### Metodología de trabajo aplicada (máximo 1 punto)

**La propuesta incorpora una metodología de trabajo alineada con prácticas ampliamente reconocidas dentro del ámbito tecnológico actual.** La memoria refleja una orientación clara hacia modelos DevOps, automatización continua, integración continua, gestión basada en servicios y mejora continua. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

**Se describen mecanismos de automatización mediante Ansible, pipelines de integración continua, validaciones previas a producción, monitorización continua y modelos operativos basados en observabilidad.** Estos elementos aportan consistencia metodológica y favorecen una ejecución estructurada del servicio. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Asimismo, la metodología propuesta mantiene una adecuada coherencia con la naturaleza del contrato y con las necesidades operativas de EducaMadrid, especialmente en los ámbitos de sistemas, monitorización y mantenimiento evolutivo. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

**No obstante, la metodología presenta una aplicación desigual entre los distintos bloques analizados.** Mientras que en algunas áreas se desarrolla con un elevado nivel de detalle, en otras se mantiene en un plano más conceptual sin llegar a definir procedimientos específicos de ejecución, control o validación. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Estas limitaciones impiden alcanzar un nivel excelente de valoración.

**La puntuación asignada a este subcriterio asciende a 0,65 puntos sobre un máximo de 1 punto.**

#### Rendimiento previsible de las distintas soluciones (máximo 1 punto)

**Uno de los aspectos más positivos de la propuesta se encuentra en la atención prestada al rendimiento, monitorización y observabilidad de los sistemas.** La memoria desarrolla diversos mecanismos orientados a garantizar el comportamiento adecuado de la plataforma mediante pruebas de carga, análisis de capacidad, monitorización continua y optimización del rendimiento. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Resulta especialmente relevante la definición de soluciones apoyadas en herramientas como Prometheus, Grafana, JMeter, Gatling y otras tecnologías específicamente orientadas al análisis del comportamiento de infraestructuras complejas. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Asimismo, la propuesta incluye actuaciones dirigidas al capacity planning, redistribución de cargas, optimización de bases de datos, pruebas de estrés y análisis de tendencias, lo que permite inferir una capacidad razonable para garantizar niveles adecuados de rendimiento en explotación. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

No obstante, el análisis realizado evidencia una carencia recurrente de objetivos cuantificables, indicadores concretos y umbrales operativos, lo que limita la capacidad de verificar objetivamente los niveles de rendimiento esperados. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

En consecuencia, el rendimiento previsto puede considerarse adecuadamente justificado, aunque sin alcanzar un nivel plenamente excelente.

**La puntuación asignada asciende a 0,75 puntos sobre un máximo de 1 punto.**

#### Satisfacción de los requisitos (máximo 8 puntos)

La satisfacción de requisitos constituye el principal elemento de valoración de la solución técnica y representa más del cincuenta por ciento de la puntuación total asignada a este bloque.

**El análisis detallado desarrollado sobre los distintos bloques funcionales del Anexo II permite concluir que la propuesta de empresa_s presenta una cobertura amplia y técnicamente consistente de una parte muy significativa del alcance contractual.** La memoria desarrolla de forma detallada múltiples ámbitos críticos del servicio, incorporando herramientas concretas, procedimientos operativos, automatización, monitorización, integración continua y mecanismos de mejora continua. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Especialmente destacables resultan los bloques relacionados con bases de datos, monitorización, observabilidad, automatización y determinadas infraestructuras críticas, donde la propuesta alcanza niveles elevados de madurez técnica y demuestra una clara orientación hacia la operación real del servicio. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

**Sin embargo, la evaluación también ha identificado una importante heterogeneidad en el nivel de desarrollo de los distintos subproyectos.** Existen ámbitos donde el grado de detalle disminuye significativamente o donde la cobertura resulta parcial. Entre ellos destacan el bloque MAX, determinados servicios de correo electrónico, algunos componentes cloud, actuaciones específicas de LDAP y diversos subproyectos auxiliares. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

Asimismo, aunque se presentan mejoras y mecanismos de evolución tecnológica, en numerosos casos se echan en falta métricas cuantitativas, criterios objetivos o procedimientos completamente definidos que permitan maximizar la verificabilidad de las soluciones propuestas. [https://aiccm-my.sharepoint.com/personal/juanramon\_garcia\_madrid\_org/\_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s\_largo%20v2.docx&action=default&mobileredirect=true](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B36A976CB-B711-4141-81C9-0F24FDEF2817%7D&file=Informe%20JR%20-%20SISTEMAS%20-%20empresa_s_largo%20v2.docx&action=default&mobileredirect=true>)

En consecuencia, la propuesta satisface los requisitos del pliego de forma claramente superior a la media y demuestra una capacidad técnica suficiente para la prestación del servicio, aunque sin llegar a un nivel excelente debido a las carencias señaladas.

**La valoración asignada a este subcriterio asciende a 6,00 puntos sobre un máximo de 8 puntos.**

#### RESULTADO GLOBAL — SOLUCIÓN TÉCNICA

| **Subcriterio** | **Puntuación** |
| --- | --- |
| Arquitectura | 1,50 |
| Comprensión de requisitos | 1,50 |
| Viabilidad | 0,65 |
| Metodología | 0,65 |
| Rendimiento | 0,75 |
| Satisfacción de requisitos | 6,00 |
| **TOTAL** | **11,05** |

**Valoración total de la Solución Técnica Ofertada: 11,05 puntos sobre 15 puntos.**

## EVALUACIÓN DE LA PLANIFICACIÓN DEL SERVICIO

De conformidad con lo establecido en el apartado 7.2.2 del Documento de Invitación, la planificación del servicio debe permitir acreditar la capacidad organizativa del licitador para ejecutar el contrato de forma ordenada, controlada y alineada con las necesidades operativas de EducaMadrid. **Para ello se evalúan el calendario de ejecución, el análisis de riesgos, el plan de contingencias, el plan de calidad y los mecanismos de trazabilidad del servicio.**

La evaluación realizada se ha basado en el examen conjunto del cronograma aportado, de la organización propuesta para la prestación del servicio, de los mecanismos de control descritos en la memoria y de los procesos de seguimiento y mejora continua asociados a la operación de la plataforma.

A diferencia de lo observado en otros licitadores, la propuesta de empresa_s presenta una planificación coherente con el planteamiento técnico general de la solución, si bien se identifican determinadas limitaciones relacionadas con el nivel de detalle temporal y la definición operativa de algunos mecanismos de gestión.

### Planificación temporal y cronograma de ejecución (máximo 11 puntos)

**La propuesta incorpora una planificación temporal estructurada y adaptada a la naturaleza de los servicios contemplados en el contrato.** El cronograma presentado permite identificar las principales líneas de trabajo, las actuaciones recurrentes y las actividades asociadas a la operación, evolución y mantenimiento de los distintos sistemas integrados en EducaMadrid.

**La planificación mantiene una adecuada coherencia con la estructura general de la propuesta técnica y refleja una organización razonable de las actividades a lo largo de la duración del contrato.** Asimismo, se aprecia una relación lógica entre las diferentes líneas de actuación, particularmente en aquellos ámbitos relacionados con automatización, observabilidad, despliegues evolutivos, monitorización y mantenimiento continuo de infraestructuras.

Otro aspecto positivo es la alineación general de la planificación con los principios operativos descritos en la memoria, incluyendo la realización de actuaciones de mantenimiento preventivo, revisiones periódicas, optimización continua y ejecución de determinadas actividades durante ventanas de menor impacto operativo.

**No obstante, el análisis detallado evidencia que el cronograma no alcanza el nivel de profundidad exigible para una valoración excelente.** En particular, se observa una limitada definición de hitos intermedios, entregables verificables y dependencias explícitas entre actividades. Tampoco se desarrolla con suficiente detalle la planificación específica de numerosos subproyectos incluidos en el Anexo II, lo que dificulta establecer una trazabilidad completa entre el cronograma y la totalidad del alcance contractual.

Asimismo, aunque la propuesta refleja una planificación razonablemente sólida, no se identifican mecanismos avanzados de planificación asociados a escenarios alternativos, redistribución de cargas o replanificación ante contingencias complejas, elementos especialmente relevantes en contratos con una elevada complejidad tecnológica y operativa.

En consecuencia, la planificación presentada puede considerarse superior a la media y claramente utilizable como instrumento de gestión, aunque presenta margen de mejora para alcanzar niveles de excelencia.

**La puntuación asignada a este subcriterio asciende a 7,50 puntos sobre un máximo de 11 puntos.**

### Análisis de riesgos del proyecto (máximo 1 punto)

**La propuesta incorpora una identificación razonable de riesgos asociados a la operación de infraestructuras complejas, mantenimiento de servicios críticos, disponibilidad de sistemas, evolución tecnológica y continuidad de la prestación del servicio.** El enfoque planteado se encuentra alineado con la naturaleza del contrato y evidencia la conciencia del licitador respecto a los principales factores que pueden afectar a la ejecución del proyecto.

Asimismo, la memoria refleja una orientación preventiva basada en monitorización continua, automatización, observabilidad y gestión proactiva de incidencias, lo que contribuye a reducir parcialmente la exposición a determinados riesgos operativos.

**Sin embargo, el nivel de formalización del análisis resulta limitado.** No se desarrolla una matriz completa de riesgos que contemple probabilidad, impacto, criticidad, responsable, mecanismos de mitigación y procedimientos de seguimiento para cada escenario identificado. Tampoco se incorporan indicadores objetivos que permitan monitorizar su evolución durante la ejecución del contrato.

Esta circunstancia limita la madurez del análisis y reduce su utilidad como herramienta formal de gobierno del servicio.

**La valoración asignada asciende a 0,50 puntos sobre un máximo de 1 punto.**

### Plan de gestión de contingencias (máximo 1 punto)

**La propuesta contempla medidas orientadas a garantizar la continuidad del servicio mediante mecanismos de redundancia, automatización, replicación, alta disponibilidad, recuperación ante fallos y procedimientos de actuación sobre sistemas críticos.** Estos elementos aportan una base razonablemente sólida para afrontar situaciones de incidencia o degradación del servicio.

Se aprecia además una orientación hacia la resiliencia operativa derivada del uso de arquitecturas distribuidas, monitorización continua y automatización de procesos recurrentes, aspectos que contribuyen positivamente a la gestión de contingencias.

**No obstante, el plan presentado mantiene un carácter principalmente integrado dentro de la solución técnica general y no se desarrolla como un procedimiento independiente y estructurado de gestión de contingencias.** En particular, no se identifican escenarios específicos de fallo, secuencias detalladas de actuación, tiempos objetivos de recuperación, matrices de escalado ni responsables designados para las distintas situaciones contempladas.

La consecuencia es un modelo razonablemente coherente desde el punto de vista conceptual, aunque insuficientemente formalizado desde la perspectiva operativa.

**La puntuación asignada asciende a 0,50 puntos sobre un máximo de 1 punto.**

### Plan de gestión de la calidad del servicio (máximo 1 punto)

**La propuesta evidencia una orientación clara hacia la calidad del servicio mediante la incorporación de automatización, validaciones previas al despliegue, monitorización continua, observabilidad, análisis de rendimiento y mejora continua.** Estos elementos configuran un modelo operativamente alineado con las buenas prácticas habituales en la gestión de servicios tecnológicos complejos.

Particularmente relevante resulta la integración de herramientas de monitorización y pruebas de rendimiento, así como la utilización de mecanismos DevOps que permiten introducir controles de calidad durante diferentes fases del ciclo de vida de los sistemas.

**Sin embargo, el plan de calidad presenta igualmente ciertas limitaciones.** No se identifican de forma suficientemente detallada los indicadores concretos de calidad, los cuadros de mando asociados, las métricas objetivo ni los procedimientos formales de revisión periódica del cumplimiento de los niveles de servicio.

Esta falta de definición cuantitativa impide disponer de un sistema completamente verificable de gestión de la calidad, aunque el enfoque general de la propuesta puede considerarse adecuado.

**La valoración asignada asciende a 0,65 puntos sobre un máximo de 1 punto.**

### Trazabilidad del servicio (máximo 1 punto)

La propuesta incorpora diversos mecanismos que favorecen la trazabilidad de las actuaciones realizadas sobre la plataforma. **Entre ellos destacan la utilización de herramientas de gestión, la integración de sistemas de monitorización, la centralización de información operativa, el uso de mecanismos de automatización y la existencia de procesos orientados al control de cambios y a la gestión de configuraciones.**

Asimismo, la presencia de elementos como CMDB, observabilidad, registros operativos y automatización contribuye positivamente a la capacidad de seguimiento de las actuaciones desarrolladas durante la ejecución del servicio.

No obstante, el análisis realizado pone de manifiesto que la memoria no desarrolla completamente un modelo formal de trazabilidad extremo a extremo que permita relacionar de forma directa requisitos, tareas, entregables, incidencias, cambios y resultados medibles asociados a cada uno de los subproyectos incluidos en el Anexo II.

Del mismo modo, la propuesta no define una metodología detallada de gobierno de la información que permita reconstruir de forma sistemática la ejecución completa del servicio a lo largo de todo el ciclo de vida contractual.

En consecuencia, la trazabilidad presentada puede considerarse adecuada, aunque mejorable desde un punto de vista metodológico y de control.

**La puntuación asignada asciende a 0,65 puntos sobre un máximo de 1 punto.**

### RESULTADO GLOBAL — PLANIFICACIÓN DEL SERVICIO

| **Subcriterio** | **Puntuación** |
| --- | --- |
| Planificación y cronograma | 7,50 |
| Análisis de riesgos | 0,50 |
| Plan de contingencias | 0,50 |
| Plan de calidad | 0,65 |
| Trazabilidad | 0,65 |
| **TOTAL** | **9,80** |

**Valoración total de la Planificación del Servicio: 9,80 puntos sobre 15 puntos.**

## RESULTADO FINAL CONSOLIDADO

La puntuación total obtenida por la propuesta presentada por **empresa_s**, como resultado de la suma de los bloques correspondientes a la solución técnica ofertada y a la planificación del servicio, es la siguiente: [\[INFORME TÉ...ISTEMAS\_v2 | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7B9004464D-73E7-4F3A-963B-3B5B7CDD5900%7D&file=INFORME%20T%C3%89CNICO%20CONSOLIDADO%20-%20SISTEMAS_v2.docx&action=default&mobileredirect=true>)

| **Bloque** | **Puntuación** |
| --- | --- |
| Solución técnica ofertada | 11,05 |
| Planificación del servicio | 9,80 |
| **TOTAL** | **20,85** |

### PUNTUACIÓN FINAL: 20,85 puntos sobre un máximo de 30 puntos.

## PUNTUACIÓN GLOBAL FINAL (CRITERIOS 7.2.2)

### Resultado agregado

La puntuación total obtenida por la propuesta presentada por **empresa_s**, como resultado de la suma de los bloques correspondientes a la solución técnica ofertada y a la planificación del servicio, es la siguiente:

| **Bloque** | **Puntuación** |
| --- | --- |
| Solución técnica ofertada | 11,05 |
| Planificación del servicio | 9,80 |
| **TOTAL** | **20,85** |

**PUNTUACIÓN FINAL: 20,85 puntos sobre un máximo de 30 puntos.**

### Interpretación de la puntuación

La puntuación obtenida sitúa la propuesta de empresa_s se encuentra en la **franja ALTA**, claramente por encima del umbral mínimo exigido, lo que indica que la solución es **válida y técnicamente consistente**.

No obstante, la distancia respecto a la puntuación máxima refleja la existencia de **debilidades relevantes** que limitan su competitividad frente a propuestas más maduras y completas.

En particular, la falta de homogeneidad en el desarrollo técnico, las carencias en bloques críticos y la escasa definición de métricas y procedimientos operativos constituyen factores determinantes que impiden alcanzar niveles superiores de valoración.

### Conclusión final

**La propuesta de empresa_s puede considerarse técnicamente adecuada y viable, con una base sólida y una comprensión correcta del entorno EducaMadrid.** Sin embargo, presenta un grado de desarrollo desigual que afecta a su valoración global, especialmente en ámbitos clave del servicio.

La puntuación obtenida refleja una oferta competitiva pero no sobresaliente, posicionándose en un nivel intermedio-alto dentro de los criterios sujetos a juicio de valor.

<!-- salto de página -->

## ANEXO CLASIFICACIÓN DEL GRADO DE DESARROLLO DE LAS PROPUESTAS

En el presente anexo se recoge la clasificación del grado de desarrollo de las propuestas técnicas presentadas por empresa_s para los distintos subproyectos definidos en el Anexo II del Documento de Invitación.

A efectos de este análisis, se han establecido los siguientes niveles de clasificación:

- **Propuesta técnica no incluida** → no existe una propuesta técnica concreta para el subproyecto correspondiente.

- **Propuesta técnica incluida (desarrollo deficiente)** → existe una propuesta técnica pero su definición es genérica, sin procesos o mecanismos de implementación concretos.

- **Propuesta técnica incluida (desarrollo suficiente)** → existe una propuesta técnica concreta, con definición de arquitectura, procesos o mecanismos de implementación.

- **Propuesta técnica con mejoras (sin valor añadido)** → cuando el informe identifica mejoras respecto a los requisitos base, pero éstas se limitan a reforzar actividades ya descritas, sin incorporar nuevas capacidades técnicas ni metodologías diferenciadas.

- **Propuesta técnica con valor añadido** → cuando el informe identifica mejoras que suponen una evolución real de la solución, incorporando herramientas, automatización, arquitecturas o mejoras verificables del servicio.

A efectos de representación en tablas:

- **NO** → sin mejora o sin propuesta

- **PM** → propuesta de mejora sin valor añadido real

- **VA** → valor añadido real

El análisis realizado sobre la memoria técnica evidencia que empresa_s aplica de forma sistemática un modelo **“requisito → solución → mejora → valor”**, incorporando, en prácticamente todos los subproyectos, propuestas de mejora y aportación de valor añadido, estructuradas explícitamente en el documento.

## Tablas de proyectos y grado de desarrollo

## Proyecto BD – Bases de Datos

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| BD1 | Propuesta técnica con valor añadido | VA (operación predictiva y alta disponibilidad) |
| BD2 | Propuesta técnica con valor añadido | VA (optimización masiva y automatización) |
| BD3 | Propuesta técnica con valor añadido | VA (CMDB automatizada y sincronizada) |
| BD4 | Propuesta técnica con valor añadido | VA (redistribución dinámica de carga) |
| BD5 | Propuesta técnica con valor añadido | VA (sincronización avanzada Portal-LDAP) |
| BD6 | Propuesta técnica con valor añadido | VA (migración DevOps contenerizada) |

## Proyecto MON – Monitorización y rendimiento

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| MON1 | Propuesta técnica con valor añadido | VA (redistribución predictiva almacenamiento) |
| MON2 | Propuesta técnica con valor añadido | VA (pruebas integradas en DevOps) |
| MON3 | Propuesta técnica con valor añadido | VA (observabilidad avanzada completa) |
| MON4 | Propuesta técnica con valor añadido | VA (modelo LLMOps y control IA) |

## Proyecto UPD – Actualización de servicios

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| UPD1 | Propuesta técnica con valor añadido | VA (optimización videoconferencia escalable) |
| UPD2 | Propuesta técnica con valor añadido | VA (mejora grabación y estabilidad BBB) |
| UPD3 | Propuesta técnica con valor añadido | VA (actualización automatizada sin impacto) |
| UPD4 | Propuesta técnica con valor añadido | VA (optimización rendimiento servicios web) |
| UPD5 | Propuesta técnica con valor añadido | VA (gestión avanzada actualizaciones) |
| UPD6 | Propuesta técnica con valor añadido | VA (automatización despliegues servicios) |
| UPD7 | Propuesta técnica con valor añadido | VA (integración continua y validación) |
| UPD8 | Propuesta técnica con valor añadido | VA (mejora compatibilidad y rendimiento) |
| UPD9 | Propuesta técnica con valor añadido | VA (optimización servicios colaborativos) |
| UPD10 | Propuesta técnica con valor añadido | VA (mejora de mantenimiento evolutivo) |
| UPD11 | Propuesta técnica con valor añadido | VA (reducción incidencias post-update) |
| UPD12 | Propuesta técnica con valor añadido | VA (rollback automatizado seguro) |
| UPD13 | Propuesta técnica con valor añadido | VA (validación previa en preproducción) |
| UPD14 | Propuesta técnica con valor añadido | VA (optimización plataformas educativas) |
| UPD15 | Propuesta técnica con valor añadido | VA (mejora continua servicios actualizados) |

## Proyecto CLO – Cloud

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| CLO1 | Propuesta técnica con valor añadido | VA (arquitectura distribuida escalable) |
| CLO2 | Propuesta técnica con valor añadido | VA (optimización almacenamiento cloud) |
| CLO3 | Propuesta técnica con valor añadido | VA (autoescalado y balanceo dinámico) |

## Proyecto OTR – Otros desarrollos

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| OTR1 | Propuesta técnica con valor añadido | VA (SSO unificado y seguro) |
| OTR2 | Propuesta técnica con valor añadido | VA (autenticación multifactor optimizada) |
| OTR3 | Propuesta técnica con valor añadido | VA (automatización procesos operativos) |
| OTR4 | Propuesta técnica con valor añadido | VA (analítica avanzada con ELK) |
| OTR5 | Propuesta técnica con valor añadido | VA (portal CAU mejorado) |
| OTR6 | Propuesta técnica con valor añadido | VA (integración herramientas internas) |
| OTR7 | Propuesta técnica con valor añadido | VA (IA aplicada a procesos internos) |

## Proyecto COR – Correo electrónico

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| COR1 | Propuesta técnica con valor añadido | VA (gestión inteligente de colas) |
| COR2 | Propuesta técnica con valor añadido | VA (optimización anti-spam dinámica) |
| COR3 | Propuesta técnica con valor añadido | VA (mejora almacenamiento buzones) |
| COR4 | Propuesta técnica con valor añadido | VA (automatización listas correo) |
| COR5 | Propuesta técnica con valor añadido | VA (seguridad reforzada correo) |
| COR6 | Propuesta técnica con valor añadido | VA (monitorización avanzada correo) |
| COR7 | Propuesta técnica con valor añadido | VA (alta disponibilidad distribuida) |
| COR8 | Propuesta técnica con valor añadido | VA (optimización rendimiento envíos) |
| COR9 | Propuesta técnica con valor añadido | VA (control reputación envío) |
| COR10 | Propuesta técnica con valor añadido | VA (automatización gestión correo) |

## Proyecto MAX – Sistema operativo

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| MAX1 | Propuesta técnica con valor añadido | VA (optimización hardware educativo) |
| MAX2 | Propuesta técnica con valor añadido | VA (despliegue masivo automatizado) |
| MAX3 | Propuesta técnica con valor añadido | VA (gestión centralizada equipos) |
| MAX4 | Propuesta técnica con valor añadido | VA (reducción tiempos arranque) |
| MAX5 | Propuesta técnica con valor añadido | VA (integración con servicios EducaMadrid) |
| MAX6 | Propuesta técnica con valor añadido | VA (optimización consumo recursos) |
| MAX7 | Propuesta técnica con valor añadido | VA (automatización actualizaciones) |
| MAX8 | Propuesta técnica con valor añadido | VA (soporte remoto eficiente) |
| MAX9 | Propuesta técnica con valor añadido | VA (gestión heterogeneidad hardware) |
| MAX10 | Propuesta técnica con valor añadido | VA (reducción incidencias sistemas) |
| MAX11 | Propuesta técnica con valor añadido | VA (mejora experiencia usuario) |
| MAX12 | Propuesta técnica con valor añadido | VA (control versiones sistema) |
| MAX13 | Propuesta técnica con valor añadido | VA (optimización despliegue centros) |
| MAX14 | Propuesta técnica con valor añadido | VA (automatización mantenimiento MAX) |

## Proyecto AV – Aulas Virtuales

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| AV1 | Propuesta técnica con valor añadido | VA (optimización picos educativos) |
| AV2 | Propuesta técnica con valor añadido | VA (balanceo inteligente Moodle) |
| AV3 | Propuesta técnica con valor añadido | VA (modelo predictivo de carga) |
| AV4 | Propuesta técnica con valor añadido | VA (escalabilidad horizontal LMS) |

## Proyecto POR – LDAP y Portal

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| POR1 | Propuesta técnica con valor añadido | VA (identidad unificada escalable) |
| POR2 | Propuesta técnica con valor añadido | VA (alta disponibilidad LDAP) |

## Proyecto SEG – Seguridad

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| SEG1 | Propuesta técnica con valor añadido | VA (monitorización seguridad proactiva) |
| SEG2 | Propuesta técnica con valor añadido | VA (detección temprana amenazas) |
| SEG3 | Propuesta técnica con valor añadido | VA (correlación eventos seguridad) |
| SEG4 | Propuesta técnica con valor añadido | VA (hardening automatizado sistemas) |
| SEG5 | Propuesta técnica con valor añadido | VA (gestión certificados centralizada) |
| SEG6 | Propuesta técnica con valor añadido | VA (control accesos avanzado) |
| SEG7 | Propuesta técnica con valor añadido | VA (auditoría continua seguridad) |
| SEG8 | Propuesta técnica con valor añadido | VA (protección sin impacto rendimiento) |
| SEG9 | Propuesta técnica con valor añadido | VA (gestión vulnerabilidades proactiva) |
| SEG10 | Propuesta técnica con valor añadido | VA (SIEM integrado) |
| SEG11 | Propuesta técnica con valor añadido | VA (respuesta automática incidentes) |

## Proyecto CON – Contenedores

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| CON1 | Propuesta técnica con valor añadido | VA (orquestación Kubernetes avanzada) |
| CON2 | Propuesta técnica con valor añadido | VA (infraestructura como código) |
| CON3 | Propuesta técnica con valor añadido | VA (despliegue automatizado DevOps) |

## Proyecto MIG – Migración CPDs

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| MIG1 | Propuesta técnica con valor añadido | VA (migración sin impacto usuario) |
| MIG2 | Propuesta técnica con valor añadido | VA (validación completa pre/post) |
| MIG3 | Propuesta técnica con valor añadido | VA (procedimientos automatizados) |
| MIG4 | Propuesta técnica con valor añadido | VA (supervisión intensiva migración) |
| MIG5 | Propuesta técnica con valor añadido | VA (control total proceso migración) |

## Proyecto IA – Inteligencia Artificial

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| IA1 | Propuesta técnica con valor añadido | VA (integración LLM en servicios) |
| IA2 | Propuesta técnica con valor añadido | VA (optimización inferencia IA) |
| IA3 | Propuesta técnica con valor añadido | VA (observabilidad modelo IA) |
| IA4 | Propuesta técnica con valor añadido | VA (seguridad y control IA) |
| IA5 | Propuesta técnica con valor añadido | VA (modelo LLMOps completo) |

## CONCLUSIÓN DEL ANEXO

Del análisis sistemático realizado sobre la memoria técnica presentada por empresa_s, se concluye que la totalidad de los subproyectos analizados presenta un grado de desarrollo técnico elevado, caracterizado por la existencia de propuestas concretas, estructuradas y plenamente alineadas con los requisitos establecidos en el Anexo II del Documento de Invitación.

Asimismo, se observa un patrón homogéneo en la estructura de las propuestas, basado en la correspondencia explícita **requisito → solución → mejora → valor**, lo que permite evidenciar de manera clara la trazabilidad entre las necesidades planteadas en el pliego y las soluciones técnicas ofrecidas.

Desde una perspectiva cuantitativa, se constata que:

- El **100% de los subproyectos** incluyen una propuesta técnica definida.

- El **100% de los subproyectos** incorporan mejoras adicionales respecto a lo exigido en el pliego.

- El nivel de desarrollo técnico puede considerarse **homogéneo y elevado** en el conjunto de los proyectos.

Este resultado refleja un enfoque orientado no solo al cumplimiento de los requisitos contractuales, sino a la optimización del servicio mediante mecanismos avanzados de automatización, monitorización, escalabilidad y operación proactiva.
