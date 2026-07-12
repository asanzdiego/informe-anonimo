# INTRODUCCIÓN

## Objeto del informe

El presente informe tiene por objeto la evaluación técnica de la propuesta presentada por la empresa **empresa_n** en el procedimiento de contratación relativo al desarrollo evolutivo y correctivo del portal educativo, LDAP, cloud, sistema operativo MAX y otros sistemas integrados en la plataforma EducaMadrid, en el marco del expediente BAC06_2026: **Desarrollo evolutivo y correctivo del portal educativo, LDAP, cloud, MAX y otros sistemas de EducaMadrid**

La evaluación se realiza conforme a los criterios establecidos en el Documento de Invitación, en particular los definidos en el apartado 7.2 relativos a criterios sujetos a juicio de valor.

## Alcance de la evaluación

La evaluación comprende el análisis integral de la memoria técnica presentada por el licitador analizando el desarrollo por subproyectos así como la planificación del servicio con el objetivo de verificar:

- el grado de cobertura de los requisitos del Anexo II

- la calidad técnica de la solución propuesta

- la capacidad real de ejecución en un entorno de alta complejidad

- la coherencia entre planteamiento teórico y operativa real

A efectos de garantizar la trazabilidad y objetividad del análisis, la evaluación se ha reestructurado conforme a los 89 subproyectos definidos en el Anexo II del Documento de Invitación, identificados mediante los códigos usados en dicho Anexo.

## Contexto técnico del servicio

La plataforma EducaMadrid constituye un entorno tecnológico complejo que integra múltiples servicios interdependientes, incluyendo portales web, sistemas de aula virtual, soluciones cloud, correo electrónico, herramientas colaborativas, sistemas de inteligencia artificial y una infraestructura distribuida con más de 700 servidores y aproximadamente 3.500 bases de datos.

Este ecosistema exige soluciones altamente especializadas, con capacidad de gestión a gran escala, mecanismos sólidos de automatización y control, y un enfoque operativo alineado con altos requisitos de disponibilidad, seguridad y rendimiento.

## Metodología de evaluación

El análisis se ha realizado mediante una revisión técnica exhaustiva de la memoria presentada, contrastando cada subproyecto con los requisitos del Documento de Invitación, evaluando el grado de concreción técnica, la existencia de metodologías, la identificación de herramientas y la capacidad real de ejecución.

Se ha prestado especial atención a la verificabilidad de la solución, entendida como la capacidad de demostrar objetivamente su funcionamiento mediante métricas, procedimientos y evidencia técnica.

Una vez evaluada la capacidad técnica subproyecto a subproyecto se ha procedido a hacer una evaluación completa de la propuesta según los requisitos del apartado 7.2.2 del Documento de Invitación, considerando especialmente las carencias técnicas, la ausencia de procedimientos, las inconsistencias y el nivel de concreción de la propuesta.

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

En este capítulo se analizará el grado de cobertura formal de la propuesta técnica de empresa_n respecto a los requisitos establecidos para cada subproyecto recogido en el Anexo II del PPT. Dicho análisis se hará subproyecto a subproyecto

### BLOQUE BD — BASES DE DATOS

## BD1 — Mantenimiento y mejora de entornos de Bases de Datos MariaDB y ProxySQL avanzado

**El subproyecto BD1 define un conjunto de requisitos técnicos claramente orientados a la operación avanzada de entornos MariaDB en configuración clusterizada, incluyendo la optimización de nodos, la gestión de ProxySQL como elemento de balanceo y la monitorización del sistema mediante herramientas específicas.** Este tipo de entornos exige la definición de arquitecturas distribuidas, control de replicación, gestión de tráfico de lectura y escritura y mecanismos automatizados de alta disponibilidad.

La propuesta presentada por empresa_n aborda este subproyecto mediante una descripción general de tareas de mantenimiento, entre las que se incluyen la comprobación del estado de los servidores, la revisión de configuraciones, la validación del balanceo y la verificación de conectividad. **No obstante, el análisis técnico evidencia que no se desarrolla ningún procedimiento específico asociado a la optimización de entornos clusterizados, ni se describen mecanismos de replicación, ni configuraciones avanzadas de ProxySQL, ni estrategias de balanceo dinámico.** Asimismo, no se identifican herramientas concretas de monitorización, siendo sustituido este elemento por referencias genéricas a soluciones no especificadas.

En relación con las propuestas de mejora, éstas se limitan a reforzar las actividades ya descritas, como la revisión y seguimiento del estado del sistema, sin introducir elementos técnicos adicionales ni metodologías específicas, lo que impide identificar un valor diferencial respecto a las tareas base.

**Valoración cualitativa: Baja**

## BD2 — Mantenimiento y optimización proactiva de las bases de datos de toda la plataforma

**El subproyecto BD2 se centra en la optimización continua de un entorno compuesto por miles de bases de datos, incluyendo la mejora de consultas, la seguridad de conexiones, el mantenimiento preventivo y la planificación de actuaciones en períodos no lectivos.** Este requisito implica necesariamente la utilización de métricas, herramientas de análisis de rendimiento y estrategias de automatización adaptadas a gran escala.

La propuesta de empresa_n plantea actividades como la revisión de consultas, la aplicación de ajustes, la ejecución de copias de seguridad y la planificación de intervenciones en horarios de baja actividad. **Sin embargo, el análisis revela la ausencia de métricas de rendimiento, herramientas de análisis de consultas, planes de indexación o mecanismos de análisis estadístico.** Tampoco se define una estrategia específica para la gestión de aproximadamente 3.500 bases de datos ni se detallan mecanismos de seguridad asociados al cifrado de conexiones o la gestión de certificados.

Las propuestas de mejora identificadas se basan en la ampliación de las tareas de revisión y mantenimiento ya descritas, sin aportar elementos técnicos adicionales ni metodologías diferenciadas, lo que limita su impacto real sobre el rendimiento del sistema.

**Valoración cualitativa: Baja**

## BD3 — Mantenimiento de las bases de datos de gestión de la configuración de EducaMadrid

**Este subproyecto exige el desarrollo de una CMDB avanzada, incluyendo la incorporación de relaciones físicas y lógicas, el modelado de dependencias, la automatización de la carga de información y el uso de herramientas de software libre.** Se trata de un requisito clave para la gestión integral de la infraestructura.

**La propuesta de empresa_n se limita a describir actividades como la revisión de elementos registrados, la actualización de información y la importación de datos, sin desarrollar mecanismos de descubrimiento automático, inventariado dinámico ni integración con otras plataformas.** Tampoco se describen modelos de relaciones ni estructuras de dependencias entre sistemas, ni se identifican herramientas concretas de software libre, como exige el Documento de Invitación.

Las propuestas de mejora siguen el mismo patrón observado en el resto del bloque, consistiendo en la ampliación de las tareas de revisión y actualización, sin incorporar automatización ni evolución funcional del sistema.

**Valoración cualitativa: Baja**

## BD4 — Mantenimiento de las bases de datos de las Aulas Virtuales

El Documento de Invitación establece que este subproyecto debe abordar la gestión de un entorno de alta complejidad, con miles de bases de datos distribuidas en múltiples servidores, incluyendo el análisis de carga, la redistribución de información y la adaptación arquitectónica.

**La propuesta de empresa_n describe actividades como la revisión de carga, el seguimiento de rendimiento y la incorporación o eliminación de servidores, manteniéndose en un nivel descriptivo.** No se identifican herramientas de análisis de rendimiento, ni metodologías de redistribución, ni mecanismos de balanceo o replicación orientados a entornos de gran escala. Tampoco se desarrolla una estrategia específica para gestionar el volumen de bases de datos indicado en el Documento de Invitación.

Las mejoras propuestas consisten en reforzar las labores de seguimiento y control, sin introducir procedimientos técnicos adicionales, lo que no permite identificar una evolución real de la solución.

**Valoración cualitativa: Baja**

## BD5 — Mantenimiento de disparadores y Foreign Data Wrappers en los entornos Portal y LDAP Plano

Este subproyecto requiere la implementación de mecanismos de sincronización entre sistemas, incluyendo el mantenimiento de disparadores, la gestión de FDW y el análisis de consistencia de la información entre Portal y LDAP.

**La propuesta de empresa_n se limita a mencionar la revisión de registros, la comprobación de triggers y la verificación de conectividad, sin desarrollar mecanismos de sincronización, planificación de ejecuciones ni procedimientos de validación de datos.** Tampoco se abordan aspectos como la resolución de conflictos, la consistencia de información o la auditoría de datos entre sistemas.

Las propuestas de mejora se centran en ampliar las tareas de revisión, sin aportar mecanismos técnicos que permitan garantizar la sincronización efectiva de los sistemas implicados.

**Valoración cualitativa: Baja**

## BD6 — Implementación y mantenimiento de bases de datos en entornos de microservicios

El subproyecto BD6 introduce un contexto tecnológico basado en arquitecturas de microservicios, incluyendo la adopción de entornos DevOps, la gestión del ciclo de vida de los servicios y la adaptación de las bases de datos a arquitecturas distribuidas.

**La propuesta de empresa_n plantea actividades centradas en la instalación de versiones, la verificación de funcionamiento y el mantenimiento correctivo, lo que refleja un enfoque propio de entornos tradicionales.** No se describen mecanismos de orquestación, ni integración con contenedores, ni estrategias de persistencia de datos en entornos distribuidos. Tampoco se abordan aspectos como la automatización de despliegues o la observabilidad del sistema.

Las propuestas de mejora consisten en la ampliación de tareas de mantenimiento general, sin introducir elementos propios de arquitecturas modernas basadas en microservicios.

**Valoración cualitativa: Baja**

### BLOQUE MON — MONITORIZACIÓN, TESTEO Y PRUEBAS DE RENDIMIENTO

## MON1 — Mantenimiento periódico del almacenamiento de los centros

**El subproyecto MON1 establece como requisito la redistribución periódica de la ocupación entre distintos sistemas de almacenamiento NFS, el análisis de la ocupación real, la reorganización del almacenamiento y la ejecución de estas tareas en periodos no lectivos.** Se trata de un requisito claramente orientado a la gestión activa de capacidad y a la optimización del uso del almacenamiento en un entorno distribuido.

La propuesta de empresa_n describe actividades como la revisión de la ocupación, la identificación de posibles desequilibrios, el movimiento de información entre sistemas y la reorganización del almacenamiento. **Sin embargo, el análisis técnico evidencia que no se define ninguna metodología concreta para realizar la redistribución de datos, ni se establecen criterios objetivos de balanceo, ni se identifican métricas de ocupación o crecimiento.** Tampoco se describen procedimientos de migración de datos, automatización de procesos ni análisis de rendimiento específico del sistema NFS. [\[Informe\_Pr...S\_Análisis | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7BA0561E17-6D69-4687-8B6F-0F30E59C70FD%7D&file=Informe_Propuesta_empresa_n_SISTEMAS_An%C3%A1lisis.docx&action=default&mobileredirect=true>)

Las propuestas de mejora se limitan a reforzar las tareas de supervisión y reorganización, sin incorporar mecanismos adicionales que permitan determinar cómo se gestionará de forma efectiva la redistribución periódica exigida.

**Valoración cualitativa: Muy baja**

## MON2 — Realización periódica de pruebas de estrés en diferentes entornos de la plataforma

**El subproyecto MON2 requiere la ejecución de pruebas de carga y estrés orientadas a la medición del rendimiento, el análisis de resultados, la identificación de anomalías y la determinación de sus causas, así como la propuesta de soluciones.** Este requisito implica la definición de metodologías de ingeniería de rendimiento y el uso de herramientas específicas.

**La propuesta presentada por empresa_n menciona la realización de pruebas de carga mediante simulación de accesos concurrentes, así como el análisis general de resultados y la revisión del rendimiento.** No obstante, el análisis detallado muestra que no se describen procedimientos concretos para la ejecución de pruebas de carga avanzadas, resistencia o degradación controlada. Tampoco se identifican herramientas de testeo, ni se establecen escenarios de carga, ni se definen modelos de análisis de resultados o correlación con sistemas de monitorización. [\[Informe\_Pr...S\_Análisis | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7BA0561E17-6D69-4687-8B6F-0F30E59C70FD%7D&file=Informe_Propuesta_empresa_n_SISTEMAS_An%C3%A1lisis.docx&action=default&mobileredirect=true>)

Las propuestas de mejora se basan en ampliar la ejecución de pruebas y la revisión de resultados, sin introducir metodologías estructuradas ni procesos de análisis profundo, lo que limita significativamente el alcance técnico del planteamiento.

**Valoración cualitativa: Muy baja**

## MON3 — Mantener actualizado el sistema de monitorización y estadísticas de uso

**El subproyecto MON3 exige la actualización continua del sistema de monitorización, la incorporación de nuevos servicios, el uso de herramientas open source y la redefinición de alertas tanto reactivas como proactivas.** Este requisito implica la definición de una arquitectura de monitorización, métricas concretas y una estrategia de alertado.

La propuesta de empresa_n incluye la incorporación de nuevos sistemas, la actualización de herramientas, el seguimiento de alertas y la elaboración de informes. **Sin embargo, el análisis técnico pone de manifiesto la ausencia de una arquitectura definida de monitorización, así como la no identificación de herramientas específicas.** No se describen métricas, umbrales, clasificación de alertas ni mecanismos de correlación de eventos. [\[Informe\_Pr...S\_Análisis | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7BA0561E17-6D69-4687-8B6F-0F30E59C70FD%7D&file=Informe_Propuesta_empresa_n_SISTEMAS_An%C3%A1lisis.docx&action=default&mobileredirect=true>)

Las propuestas de mejora se centran en ampliar la monitorización y el seguimiento, manteniéndose en un nivel genérico y sin aportar elementos técnicos que permitan evaluar la evolución del sistema.

**Valoración cualitativa: Baja**

## MON4 — Mantener actualizado el sistema de monitorización y estadísticas de servicios basados en IA

**El subproyecto MON4 introduce la monitorización específica de servicios basados en inteligencia artificial, incluyendo modelos de lenguaje, endpoints de inferencia, estadísticas de consumo y alertas específicas.** Este requisito tiene un carácter especializado y requiere la definición de métricas y herramientas adaptadas a plataformas de IA.

La propuesta de empresa_n describe actividades como el alta de modelos, la revisión de conectividad, la monitorización general y la generación de informes. **No obstante, no se identifican métricas específicas para modelos de IA, ni mecanismos de observabilidad, ni análisis de consumo, ni sistemas de alertado adaptados a este tipo de servicios.** [\[Informe\_Pr...S\_Análisis | Word\]](<https://aiccm-my.sharepoint.com/personal/juanramon_garcia_madrid_org/_layouts/15/Doc.aspx?sourcedoc=%7BA0561E17-6D69-4687-8B6F-0F30E59C70FD%7D&file=Informe_Propuesta_empresa_n_SISTEMAS_An%C3%A1lisis.docx&action=default&mobileredirect=true>)

Las propuestas de mejora se limitan a extender los procesos generales de monitorización, sin introducir elementos diferenciales asociados a la naturaleza específica de los sistemas de inteligencia artificial.

**Valoración cualitativa: Muy baja**

### BLOQUE UPD — ACTUALIZACIÓN DE SERVICIOS EXISTENTES

## UPD1 — Mantenimiento y mejora de los sistemas de videoconferencias de EducaMadrid

**El subproyecto UPD1 exige la actualización periódica de plataformas de videoconferencia, incluyendo migraciones de versión, adaptación de componentes, optimización del rendimiento y compatibilidad con navegadores.** Se trata de un entorno complejo que requiere gestión de arquitecturas distribuidas y control de concurrencia.

La propuesta de empresa_n plantea actividades como la instalación de versiones, la validación de compatibilidad y el mantenimiento correctivo. **Sin embargo, no se desarrollan aspectos técnicos relacionados con la arquitectura del sistema, la escalabilidad, la gestión de sesiones concurrentes ni la optimización del rendimiento en entornos de alta carga.**

Las propuestas de mejora consisten en reforzar las tareas de validación y seguimiento, sin introducir mecanismos técnicos adicionales que permitan evaluar la evolución de la plataforma.

**Valoración cualitativa: Muy baja**

## UPD2 — Mantenimiento y mejora del sistema secundario de videoconferencias con opción de grabación

Este subproyecto introduce funcionalidades específicas de grabación y procesamiento de sesiones, lo que implica la gestión de almacenamiento, procesamiento y escalabilidad.

**La propuesta presentada resulta prácticamente idéntica a la del subproyecto anterior, sin adaptarse a las particularidades del sistema de grabación.** No se mencionan componentes específicos como el procesamiento de grabaciones, la gestión de almacenamiento ni los mecanismos asociados al sistema BigBlueButton.

Las propuestas de mejora mantienen el mismo enfoque genérico, sin incorporar elementos diferenciados asociados a la funcionalidad de grabación.

**Valoración cualitativa: Baja**

## UPD3 — Mantenimiento y mejora de la herramienta Mattermost

El subproyecto exige la gestión de una plataforma de comunicación interna con dependencias en bases de datos, sistemas de indexación y mecanismos de alta disponibilidad.

**La propuesta de empresa_n describe tareas de actualización y mantenimiento, incorporando algunas fases de validación, pero no desarrolla los componentes técnicos de la plataforma.** No se mencionan elementos como bases de datos, integración LDAP, ni arquitecturas de alta disponibilidad.

Las propuestas de mejora se limitan a reforzar las tareas existentes sin aportar desarrollo técnico adicional.

**Valoración cualitativa: Baja**

## UPD4 — Mantenimiento y mejora de la solución Kanban

El subproyecto plantea la gestión de una herramienta de tipo Kanban, incluyendo su mantenimiento, actualización y evolución funcional.

**La propuesta presentada por empresa_n se limita a describir actividades genéricas como actualización, validación y gestión de incidencias.** No se identifica la herramienta concreta utilizada, ni se desarrollan funcionalidades específicas relacionadas con la gestión de proyectos o automatización de tareas.

Las propuestas de mejora no incorporan elementos adicionales y mantienen el mismo nivel de generalidad.

**Valoración cualitativa: Muy baja**

## UPD5 — Mantenimiento y mejora de la solución GitLab

El subproyecto UPD5 exige la gestión de una plataforma compleja de desarrollo colaborativo, incluyendo pipelines, repositorios y herramientas de integración continua.

**La propuesta de empresa_n aborda este subproyecto como si se tratara de una aplicación convencional, describiendo tareas de actualización y mantenimiento preventivo.** No se desarrollan componentes propios de la plataforma ni se identifican elementos específicos de su arquitectura.

Las propuestas de mejora mantienen el mismo enfoque y no aportan elementos técnicos diferenciados.

**Valoración cualitativa: Baja**

## UPD6 — Mantenimiento y mejora de la solución LimeSurvey

**El subproyecto UPD6 establece como requisito la actualización de la herramienta LimeSurvey, la mejora de su arquitectura, la optimización del rendimiento y la evolución funcional del sistema.** Se trata de un entorno que requiere una comprensión clara de su arquitectura, de la gestión de bases de datos subyacentes y de la experiencia de usuario.

La propuesta presentada por empresa_n describe actuaciones relacionadas con la revisión de la apariencia, la aplicación de ajustes y la validación del rendimiento general. **Sin embargo, no se desarrollan aspectos técnicos relacionados con la arquitectura objetivo, la escalabilidad del sistema ni la optimización de las consultas asociadas.** Tampoco se identifican mecanismos de mejora de experiencia de usuario ni se describen procedimientos de prueba orientados a validar el rendimiento en escenarios reales.

Las propuestas de mejora identificadas mantienen el mismo enfoque descriptivo, centrado en ajustes generales y revisiones, sin introducir elementos técnicos adicionales que permitan evaluar una evolución real del sistema.

**Valoración cualitativa: Muy baja**

## UPD7 — Mantenimiento y mejora de SonarQube

El subproyecto UPD7 exige el mantenimiento y mejora de la plataforma SonarQube, incluyendo la gestión de calidad de código, reglas de análisis, perfiles de calidad y control de calidad de proyectos.

En la propuesta de empresa_n se detecta una **desviación relevante**, ya que el contenido asociado a este subproyecto no corresponde con SonarQube, sino que hace referencia a Redmine, evidenciando una reutilización de contenido no adaptada al requisito. Como consecuencia, desaparecen elementos fundamentales como los perfiles de calidad, las reglas específicas de análisis de código, los Quality Gates o la gestión de proyectos en SonarQube.

Las propuestas de mejora asociadas a este subproyecto se encuentran igualmente afectadas por esta incongruencia, al basarse en un contenido que no corresponde con la tecnología requerida.

**Valoración cualitativa: Muy baja**

## UPD8 — Mantenimiento y mejora de Redmine

El subproyecto UPD8 plantea la gestión de la herramienta Redmine, incluyendo automatización, mantenimiento evolutivo y mejora funcional.

La propuesta de empresa_n presenta en este caso un mayor grado de alineación con el requisito, identificando elementos como la API REST, la automatización mediante scripts y la incorporación de mecanismos de autenticación adicional. **No obstante, el desarrollo técnico continúa siendo limitado, ya que no se describen arquitecturas, estrategias de despliegue ni integración con otros sistemas como LDAP o SSO.**

Las propuestas de mejora se centran en reforzar los elementos ya descritos, sin introducir nuevas líneas de evolución técnica, manteniéndose dentro de un enfoque incremental.

**Valoración cualitativa: Alta**

## UPD9 — Mantenimiento y configuración de Wowza Streaming Engine

El subproyecto UPD9 requiere la gestión de una plataforma de streaming basada en tecnologías como Wowza, incluyendo protocolos de transmisión, codificación de vídeo y distribución de contenidos.

La propuesta presentada por empresa_n **no responde al requisito**, ya que el contenido asociado a este subproyecto describe nuevamente aspectos relacionados con SonarQube, repitiendo un contenido no aplicable a la tecnología solicitada. Como consecuencia, no se identifican elementos propios de streaming como protocolos RTMP, RTSP, HLS ni componentes de codificación o distribución de vídeo.

Las propuestas de mejora se encuentran afectadas por la misma desviación, al no estar vinculadas al subproyecto requerido.

**Valoración cualitativa: Muy baja**

## UPD10 — Mantenimiento y gestión de contenidos AbiesWeb

El subproyecto UPD10 está orientado a la gestión de contenidos bibliográficos mediante AbiesWeb, incluyendo la carga masiva de datos, la sincronización con sistemas externos y la gestión de catálogos.

La propuesta de empresa_n presenta una respuesta parcial, centrada en tareas de mantenimiento básico y gestión general de contenidos. **Sin embargo, no se desarrollan procedimientos de carga masiva, ni se describen mecanismos de integración con sistemas externos, ni se abordan aspectos relacionados con la sincronización de información.**

Las propuestas de mejora se limitan a reforzar las actividades de gestión ya descritas, sin introducir elementos adicionales que permitan evaluar una mejora significativa del sistema.

**Valoración cualitativa: Baja**

## UPD11 — Actualización, mantenimiento y gestión de contenidos de Abies+

Este subproyecto exige la evolución del sistema Abies+, incluyendo la realización de pruebas, la implementación de mejoras y la gestión de contenidos.

La propuesta de empresa_n se centra fundamentalmente en tareas de actualización y resolución de incidencias, incluyendo una gestión básica de contenidos. **No obstante, no se desarrollan procedimientos de prueba, ni mecanismos de validación, ni planes de evolución funcional del sistema.** Tampoco se aborda la posible migración desde sistemas previos.

Las propuestas de mejora se mantienen en el mismo nivel de generalidad, limitándose a ampliar tareas existentes sin introducir mecanismos de evolución estructurada.

**Valoración cualitativa: Baja**

## UPD12 — Implementación, mantenimiento y mejora de Empieza

El subproyecto UPD12 presenta un alto nivel de exigencia técnica, incluyendo la necesidad de escalado horizontal y vertical, alta disponibilidad, balanceo de carga y optimización del rendimiento.

La propuesta de empresa_n menciona aspectos como ajustes de alta disponibilidad, configuración de balanceo y revisión de arquitectura. **Sin embargo, no identifica mecanismos concretos ni herramientas específicas asociadas a estos conceptos.** No se describen balanceadores, ni arquitecturas de clustering ni mecanismos de replicación, manteniéndose en un nivel conceptual sin desarrollo técnico.

Las propuestas de mejora se centran en reforzar estas ideas, sin concretar los elementos técnicos necesarios para su implementación.

**Valoración cualitativa: Muy baja**

## UPD13 — Mantenimiento y mejora del sistema de gestión de la configuración

El subproyecto UPD13 exige el uso de herramientas específicas como CMDBuild y Ansible, así como la automatización de procesos y la correlación de datos.

La propuesta de empresa_n incluye referencias a automatización básica y revisión de datos, pero omite las herramientas específicas indicadas en el Documento de Invitación. **No se desarrollan mecanismos de correlación de información ni integración entre sistemas, lo que limita la capacidad del sistema de gestión de configuración.**

Las propuestas de mejora no introducen las herramientas ni los mecanismos requeridos, manteniéndose en un enfoque generalista.

**Valoración cualitativa: Muy baja**

## UPD14 — Mantenimiento, actualización y mejora de la solución de contenedores

Este subproyecto requiere la gestión de entornos de contenedores, incluyendo tecnologías específicas como Docker, Kubernetes o Podman, así como la automatización de despliegues y la gestión de infraestructuras.

**La propuesta de empresa_n describe tareas de actualización de plataformas y ejecución de scripts generales, sin identificar las tecnologías concretas ni los mecanismos de orquestación.** No se desarrollan arquitecturas de contenedores ni procesos de despliegue automatizado.

Las propuestas de mejora se mantienen en el mismo nivel de generalidad, sin introducir herramientas ni arquitecturas específicas.

**Valoración cualitativa: Muy baja**

## UPD15 — Mantenimiento de gestión y decomisionado de servidores

El subproyecto UPD15 exige la gestión completa del ciclo de vida de servidores, incluyendo su retirada, gestión de DNS, direcciones IP, almacenamiento y eliminación de dependencias.

**La propuesta de empresa_n se limita a describir la eliminación de servidores y la actualización del inventario, sin desarrollar procedimientos completos de decomisionado.** No se abordan aspectos como la gestión de DNS, la limpieza de almacenamiento ni la retirada de configuraciones asociadas.

Las propuestas de mejora consisten en ampliar las tareas de revisión, sin introducir procedimientos completos de gestión del ciclo de vida.

**Valoración cualitativa: Muy baja**

### BLOQUE CLO — CLOUD

## CLO1 — Mantenimiento del servicio de la nube de EducaMadrid

**El subproyecto CLO1 requiere la mejora y evolución de la infraestructura cloud, incluyendo la distribución de carga para un entorno de aproximadamente dos millones de usuarios, la redistribución del almacenamiento, la planificación de capacidad a medio y largo plazo y la gestión de cuotas.** Se trata de un requisito claramente orientado a entornos de alta escalabilidad y gestión avanzada de infraestructura.

La propuesta presentada por empresa_n no desarrolla este subproyecto de forma específica, limitándose a referencias genéricas al mantenimiento del entorno cloud. No se describen procedimientos concretos de distribución de carga ni planificación de capacidad, ni se identifican mecanismos de escalabilidad, ni estrategias de redistribución de almacenamiento o gestión de cuotas. **La falta de desarrollo resulta especialmente significativa considerando el volumen de usuarios indicado en el Documento de Invitación, ya que no se define cómo se abordaría este requisito en términos operativos.**

Las propuestas de mejora mantienen el mismo nivel de generalidad, sin introducir elementos técnicos adicionales ni procedimientos concretos, lo que impide identificar un planteamiento operativo para la evolución del servicio.

**Valoración cualitativa: Muy baja**

## CLO2 — Mantenimiento y adaptación del sistema de almacenamiento temporal de datos de la nube

**Este subproyecto exige el mantenimiento del sistema de almacenamiento temporal, su interoperabilidad con el entorno cloud y su adaptación a necesidades de escalabilidad y carga.** Se trata de un componente crítico en el funcionamiento de la plataforma.

La propuesta de empresa_n describe actuaciones como la revisión del sistema, la realización de ajustes básicos, la supervisión y la adaptación progresiva de recursos. **Sin embargo, no se definen mecanismos concretos de escalabilidad ni estrategias de distribución de carga, ni se desarrollan aspectos relacionados con la persistencia de datos o la alta disponibilidad.** Tampoco se identifican procedimientos para garantizar la interoperabilidad con el resto de los sistemas de la plataforma.

Las propuestas de mejora reproducen el mismo enfoque, basándose en ajustes progresivos y supervisión, sin incorporar mecanismos técnicos adicionales que permitan evaluar la adaptación del sistema a escenarios de alta demanda.

**Valoración cualitativa: Baja**

## CLO3 — Mantenimiento del sistema de edición en línea de EducaMadrid

El subproyecto CLO3 establece la necesidad de mantener y evolucionar el sistema de edición en línea, incluyendo la mejora de infraestructura, la integración con la nube y la capacidad de adaptación a múltiples usuarios.

La propuesta de empresa_n describe tareas de mantenimiento, actualización y comprobación de accesos, así como la integración básica con el almacenamiento. **Sin embargo, no se desarrollan mecanismos específicos de escalabilidad, ni estrategias de gestión de sesiones concurrentes, ni procedimientos de optimización del rendimiento.** Tampoco se identifican actuaciones orientadas a la mejora arquitectónica del sistema.

Las propuestas de mejora se limitan a reforzar el mantenimiento y la adaptación básica a múltiples usuarios, sin incorporar elementos técnicos que permitan evaluar la evolución del sistema hacia un modelo escalable.

**Valoración cualitativa: Muy baja**

### BLOQUE OTR — OTROS DESARROLLOS

## OTR1 — Mantenimiento y mejora del sistema de autentificación centralizada Single Sign On (SSO)

El subproyecto OTR1 requiere la gestión del sistema de autenticación centralizada, incluyendo la integración SSO entre aplicaciones, la sincronización con LDAP, la implantación de alta disponibilidad y la incorporación de mecanismos de autenticación reforzada.

La propuesta de empresa_n identifica correctamente los elementos principales del sistema, mencionando tecnologías como Keycloak, LDAP, mecanismos de alta disponibilidad y autenticación multifactor. **No obstante, el análisis técnico pone de manifiesto la ausencia de desarrollo de mecanismos concretos de federación de identidades, gestión de sesiones, sincronización avanzada o arquitectura detallada de alta disponibilidad.**

Las propuestas de mejora se centran en reforzar aspectos ya descritos, como el balanceo o la autenticación adicional, sin aportar mecanismos específicos que permitan evaluar el funcionamiento real del sistema.

**Valoración cualitativa: Media**

## OTR2 — Mantenimiento, configuración y gestión 2FA en el servicio de Single Sign On

El subproyecto OTR2 se centra en la gestión de la autenticación multifactor, incluyendo la integración con sistemas existentes, la correlación con directorios LDAP y la configuración de métodos de verificación.

La propuesta de empresa_n incluye referencias a OTP, TOTP, Google Authenticator y LDAP, lo que indica un conocimiento general del ámbito. Sin embargo, se detecta una **inconsistencia relevante** al hacer referencia a la sincronización con Directorio Activo, lo que no se corresponde con el entorno descrito en el Documento de Invitación, basado en LDAP/OpenLDAP.

Las propuestas de mejora mantienen este enfoque general, sin corregir la inconsistencia identificada ni desarrollar mecanismos concretos de integración y correlación de identidades.

**Valoración cualitativa: Baja**

## OTR3 — Mantenimiento y mejora de herramientas de automatización de tareas

Este subproyecto exige la gestión de herramientas de automatización en un entorno complejo, incluyendo la ejecución de tareas repetitivas, la integración entre sistemas y la optimización de procesos.

**La propuesta de empresa_n describe la automatización de tareas mediante scripts y la revisión de procesos, sin identificar herramientas concretas ni desarrollar arquitecturas de automatización.** No se definen sistemas de orquestación ni mecanismos de gestión centralizada de automatizaciones.

Las propuestas de mejora se limitan a ampliar las tareas automatizadas existentes, sin introducir herramientas ni metodologías específicas.

**Valoración cualitativa: Baja**

## OTR4 — Mantenimiento y mejora del sistema de gestión y análisis de datos mediante Elastic

El subproyecto OTR4 requiere la gestión de sistemas de análisis de datos basados en el stack Elastic, incluyendo la ingestión, procesamiento y análisis de logs.

La propuesta de empresa_n hace referencia a la gestión de logs y análisis de datos, pero no desarrolla los componentes específicos del stack Elastic, ni describe arquitecturas, ni procesos de ingestión o visualización de datos.

Las propuestas de mejora mantienen el mismo enfoque general, sin aportar elementos técnicos que permitan evaluar la capacidad analítica del sistema.

**Valoración cualitativa: Baja**

## OTR5 — Mantenimiento y mejora de la herramienta de flujos de trabajo

El subproyecto OTR5 establece la gestión de una herramienta de workflow, incluyendo la automatización de procesos y la gestión de flujos de trabajo.

La propuesta de empresa_n describe tareas de mantenimiento y gestión de incidencias, sin identificar la herramienta concreta ni desarrollar los mecanismos de definición de flujos, automatización o integración con otros sistemas.

Las propuestas de mejora consisten en ampliar las tareas de mantenimiento sin introducir elementos adicionales.

**Valoración cualitativa: Muy baja**

## OTR6 — Mantenimiento y mejora del Portal CAU

El subproyecto OTR6 requiere la gestión del portal de atención al usuario, incluyendo su evolución funcional, integración y mejora de usabilidad.

La propuesta de empresa_n incluye tareas de mantenimiento y actualización, sin desarrollar aspectos relacionados con la arquitectura del sistema, la integración con herramientas de soporte ni la mejora funcional del portal.

Las propuestas de mejora se limitan a reforzar las tareas descritas, sin aportar mecanismos de evolución del sistema.

**Valoración cualitativa: Baja**

## OTR7 — Mantenimiento y evolución de servicios de Inteligencia Artificial

Este subproyecto requiere la evolución de servicios de inteligencia artificial dentro de la plataforma, incluyendo el entrenamiento, despliegue y gestión de modelos.

**La propuesta de empresa_n aborda este apartado de forma conceptual, sin desarrollar arquitecturas, herramientas ni procedimientos técnicos asociados a la gestión de modelos de IA.** No se identifican pipelines, entornos de entrenamiento ni sistemas de despliegue.

Las propuestas de mejora se limitan a extender este enfoque conceptual, sin introducir elementos técnicos que permitan evaluar su aplicabilidad.

**Valoración cualitativa: Muy baja**

### BLOQUE COR — CORREO ELECTRÓNICO

## COR1 — Mantenimiento y mejora de los sistemas de control de envíos de correo

**El subproyecto COR1 exige la implantación y evolución de mecanismos de control de envío de correo, incluyendo limitaciones según proveedores, control de flujos y regulación del tráfico saliente.** Se trata de un ámbito que requiere una definición clara de políticas de envío, gestión de colas y control de reputación.

La propuesta de empresa_n describe actividades como la supervisión del sistema, el análisis del comportamiento de los envíos y la realización de ajustes progresivos. **Sin embargo, no se desarrollan mecanismos concretos de control del tráfico, ni políticas diferenciadas por dominio o proveedor, ni estrategias de gestión de colas o limitación de envíos.**

Las propuestas de mejora se basan en reforzar la supervisión y el ajuste de parámetros, sin introducir mecanismos técnicos adicionales que permitan evaluar el control efectivo del sistema.

**Valoración cualitativa: Baja**

## COR2 — Mantenimiento automatizado de listas de distribución de EducaMadrid

Este subproyecto requiere la automatización del mantenimiento de listas de distribución, incluyendo su actualización periódica, sincronización con sistemas corporativos y gestión de altas y bajas masivas.

**La propuesta de empresa_n describe tareas relacionadas con la gestión de listas y la incorporación de usuarios, pero no desarrolla mecanismos de automatización ni procesos de sincronización entre sistemas.** No se identifican procedimientos de actualización masiva ni herramientas específicas orientadas a la gestión automatizada.

Las propuestas de mejora mantienen el mismo enfoque general, centrado en la revisión y actualización manual, sin incorporar mecanismos adicionales de automatización.

**Valoración cualitativa: Baja**

## COR3 — Mantenimiento y mejora del sistema de activación y gestión de cuotas de correo

El subproyecto COR3 implica la definición de políticas de cuotas por usuario y su gestión automatizada, incluyendo la activación de límites y el control del uso del sistema.

**La propuesta de empresa_n menciona la revisión del almacenamiento y la aplicación de ajustes generales, pero no define mecanismos de asignación de cuotas ni estrategias de gestión automatizada.** Tampoco se describe la integración con sistemas de gestión de usuarios ni el control del consumo en tiempo real.

Las propuestas de mejora reproducen este enfoque general, sin incorporar sistemas de control más avanzados.

**Valoración cualitativa: Baja**

## COR4 — Mantenimiento y mejora de las herramientas de control del spam

El subproyecto COR4 exige la gestión avanzada de sistemas antispam, incluyendo la realización de campañas de phishing controladas y la mejora de los mecanismos de detección.

**La propuesta de empresa_n se limita a describir la revisión de filtros y la supervisión del sistema de protección, sin desarrollar campañas de pruebas ni mecanismos específicos de análisis de amenazas.** No se identifican herramientas concretas ni estrategias de concienciación de usuarios.

Las propuestas de mejora se centran en ampliar la supervisión del sistema, sin introducir nuevos mecanismos técnicos de detección o prevención.

**Valoración cualitativa: Baja**

## COR5 — Mantenimiento de buzones de correo

Este subproyecto requiere la gestión masiva de buzones, incluyendo su creación, eliminación, redistribución y mantenimiento operativo.

**La propuesta de empresa_n describe actividades básicas de administración de buzones, sin desarrollar procesos automatizados ni estrategias de gestión a gran escala.** No se identifican mecanismos de balanceo ni de redistribución de carga entre servidores.

Las propuestas de mejora mantienen el mismo enfoque, sin introducir elementos adicionales que permitan gestionar el sistema en volumen.

**Valoración cualitativa: Baja**

## COR6 — Mantenimiento y mejora de la seguridad del sistema de correo

El subproyecto COR6 establece la necesidad de garantizar la seguridad del sistema de correo, incluyendo la gestión de certificados, cifrado y mecanismos de protección.

**La propuesta de empresa_n menciona la revisión de certificados y ajustes generales, pero no desarrolla estrategias de seguridad ni procedimientos avanzados de protección.** No se definen mecanismos de cifrado, rotación de claves o control de accesos.

Las propuestas de mejora no introducen elementos adicionales en este ámbito.

**Valoración cualitativa: Baja**

## COR7 — Actualización y mejora continua de la infraestructura de correo

Este subproyecto exige la evolución de la infraestructura de correo, diferenciando componentes y mejorando su rendimiento y escalabilidad.

**La propuesta presenta el sistema como un bloque único, sin diferenciar componentes ni desarrollar la arquitectura subyacente.** No se describen mecanismos de mejora de infraestructura ni estrategias de escalabilidad.

Las propuestas de mejora mantienen este mismo enfoque generalista.

**Valoración cualitativa: Baja**

## COR8 — Ampliación del número de servidores Mailbox Server

El subproyecto COR8 implica la ampliación de infraestructura en función de la carga, lo que requiere la definición de métricas y criterios de escalado.

La propuesta de empresa_n no define umbrales ni criterios de ampliación, ni se identifican mecanismos de análisis de carga que permitan justificar la evolución de la infraestructura.

Las propuestas de mejora no aportan mecanismos adicionales.

**Valoración cualitativa: Baja**

## COR9 — Implementación de un módulo receptor de inyección directa de correo

Este subproyecto exige la implementación de un sistema de recepción de correo mediante inyección directa, incluyendo su integración con la infraestructura existente.

**La propuesta de empresa_n describe de forma genérica la recepción de mensajes, sin desarrollar el sistema completo ni su integración.** No se describen mecanismos de persistencia ni gestión de colas.

Las propuestas de mejora mantienen el mismo nivel de generalidad.

**Valoración cualitativa: Baja**

## COR10 — Mantenimiento y soporte del módulo de inyección directa de correo

El subproyecto COR10 implica el mantenimiento del sistema de inyección directa, incluyendo soporte, monitorización y mejora del rendimiento.

**La propuesta describe actividades básicas de soporte, sin desarrollar mecanismos de mejora ni sistemas de control del rendimiento.** No se identifican herramientas ni métricas específicas.

Las propuestas de mejora no introducen cambios relevantes.

**Valoración cualitativa: Baja**

En la propuesta de empresa_n referente al bloque COR se detecta una **desviación relevante**, ya que al final del bloque se incluye con una imagen que representa una arquitectura de Active Directory en Cluster activo/pasivo. Esta arquitectura no corresponde con la que tiene EducaMadrid en producción actualmente, evidenciando desconocimiento de la plataforma real de EducaMadrid, y una falta de comprensión de los requisitos planteados en el Anexo II del Documento de Invitación, en donde se especifican las tecnologías usadas por EducaMadrid.

### BLOQUE MAX — SISTEMA OPERATIVO MAX

## MAX1 a MAX14 — Evaluación global del bloque

El bloque MAX incluye un conjunto amplio de subproyectos relacionados con el sistema operativo MAX, abarcando mantenimiento, desarrollo de distribuciones, soporte a centros educativos, gestión de repositorios y asistencia técnica.

El análisis de la memoria técnica de empresa_n pone de manifiesto que **no se presenta contenido técnico evaluable para este bloque completo**. Los apartados correspondientes se limitan a reproducir o reformular los requisitos del Documento de Invitación sin aportar nada adicional.

**Valoración cualitativa: Muy baja en todos los subproyectos del bloque MAX**

### BLOQUE AV — AULAS VIRTUALES

## AV1 — Actualización y comprobación periódica de servidores de BBDD de aulas virtuales

El subproyecto AV1 requiere la actualización y comprobación de servidores físicos y virtuales que soportan las bases de datos de aulas virtuales, lo que implica tareas de revisión técnica, control de estado y validación de funcionamiento en entornos de alta carga.

**La propuesta de empresa_n plantea actividades de revisión periódica, comprobación de estado y mantenimiento general, manteniéndose en un nivel descriptivo.** No se identifican procedimientos específicos de validación, ni herramientas de diagnóstico, ni mecanismos de análisis del rendimiento asociados a los servidores de bases de datos. Tampoco se desarrollan estrategias para garantizar la estabilidad en escenarios de alta concurrencia.

Las propuestas de mejora se limitan a reforzar las tareas de revisión y seguimiento sin introducir mecanismos técnicos adicionales.

**Valoración cualitativa: Baja**

## AV2 — Mantenimiento de los servidores FrontEnd de aulas virtuales

Este subproyecto exige el mantenimiento de los servidores de front-end, incluyendo la gestión de accesos, la disponibilidad del servicio y la optimización del rendimiento.

**La propuesta describe tareas generales de mantenimiento y supervisión, sin desarrollar arquitecturas de despliegue ni mecanismos de balanceo o escalabilidad.** No se identifican herramientas de gestión de tráfico ni estrategias para la distribución de carga entre servidores.

Las propuestas de mejora mantienen el mismo enfoque, centrado en la supervisión sin aportar elementos técnicos adicionales.

**Valoración cualitativa: Baja**

## AV3 — Despliegue de nuevos grupos de aulas virtuales

El subproyecto AV3 requiere el despliegue periódico de nuevos entornos de aulas virtuales, incluyendo la ampliación de infraestructuras existentes.

**La propuesta de empresa_n menciona la creación de nuevos entornos y la ampliación de los existentes, pero no desarrolla procedimientos de despliegue, ni automatización, ni estrategias de escalado.** No se describen dependencias ni secuencias de despliegue.

Las propuestas de mejora se limitan a reforzar la ampliación de entornos sin definir los mecanismos técnicos asociados.

**Valoración cualitativa: Baja**

## AV4 — Redistribución periódica de NFS de aulas virtuales

Este subproyecto establece la redistribución periódica de almacenamiento NFS en el entorno de aulas virtuales.

**La propuesta describe la reorganización del almacenamiento y la revisión de ocupación, sin definir criterios de redistribución ni herramientas de análisis.** No se identifican métricas ni procedimientos de migración de datos.

Las propuestas de mejora no aportan elementos adicionales.

**Valoración cualitativa: Baja**

### BLOQUE POR — LDAP Y PORTAL

## POR1 — Ampliación periódica del sistema de esclavos LDAP de EducaMadrid

**El subproyecto POR1 establece la ampliación del sistema LDAP mediante la incorporación de nuevos nodos esclavos, lo que implica la gestión de replicación del directorio, la sincronización continua de datos y la garantía de consistencia entre nodos en un entorno distribuido.** Se trata de una operación que requiere definir claramente la arquitectura LDAP, los mecanismos de replicación y los procedimientos de validación de integridad del sistema.

**La propuesta presentada por empresa_n plantea la ampliación del sistema mediante la incorporación de nuevos servidores y la revisión general de su estado, sin desarrollar los mecanismos técnicos asociados a la replicación ni a la sincronización de datos.** No se describen configuraciones específicas, ni procedimientos de control de divergencias, ni mecanismos de validación del estado del directorio entre nodos.

Las propuestas de mejora se limitan a reforzar la ampliación y supervisión del sistema, sin introducir elementos técnicos adicionales que permitan evaluar la gestión efectiva del entorno LDAP distribuido.

**Valoración cualitativa: Baja**

## POR2 — Migración del sistema LDAP máster de EducaMadrid

El subproyecto POR2 implica la migración del nodo maestro LDAP, operación crítica que requiere planificación, ejecución controlada y validación de integridad del sistema, así como la minimización del impacto sobre los servicios dependientes.

**La propuesta de empresa_n aborda la migración mediante una descripción general del proceso, haciendo referencia a su ejecución y comprobación posterior, sin definir fases concretas ni procedimientos técnicos asociados.** No se describen mecanismos de traslado de datos, validación de consistencia ni herramientas de soporte a la migración.

Las propuestas de mejora mantienen el mismo enfoque, reforzando la revisión del proceso sin incorporar metodologías adicionales que permitan garantizar la correcta ejecución de la migración en un entorno crítico.

**Valoración cualitativa: Baja**

### BLOQUE SEG — SEGURIDAD

## SEG1 — Mantenimiento y mejora del sistema de control de cambios en DNS

El subproyecto SEG1 exige la implantación de mecanismos de control de cambios en DNS que permitan auditar modificaciones, mantener trazabilidad y garantizar la estabilidad de la configuración en el tiempo.

**La propuesta de empresa_n describe la revisión y control general del sistema DNS sin desarrollar procedimientos específicos de control de cambios ni definir herramientas de auditoría o versionado.** No se identifican flujos de validación ni mecanismos de aprobación de modificaciones.

Las propuestas de mejora se centran en reforzar la supervisión del sistema sin incorporar mecanismos adicionales que permitan garantizar la trazabilidad de los cambios.

**Valoración cualitativa: Baja**

## SEG2 — LDAP Máster independiente para usuarios privilegiados

Este subproyecto establece la necesidad de separar los usuarios privilegiados en un entorno LDAP independiente, con el objetivo de reforzar la seguridad y el control de accesos.

**La propuesta presentada describe de forma general la gestión del sistema sin desarrollar una arquitectura diferenciada ni mecanismos específicos de control de accesos.** No se identifican políticas de segregación ni procedimientos de gestión de privilegios.

Las propuestas de mejora mantienen este enfoque general sin aportar elementos técnicos que permitan evaluar la implantación efectiva de un entorno segregado.

**Valoración cualitativa: Baja**

## SEG3 — Gestión, mantenimiento e implantación de certificados

El subproyecto SEG3 requiere la gestión completa del ciclo de vida de certificados, incluyendo su generación, distribución, renovación y revocación.

**La propuesta de empresa_n se limita a mencionar la gestión y revisión de certificados sin desarrollar procedimientos específicos asociados a su ciclo de vida.** No se describen mecanismos de automatización ni herramientas de gestión centralizada.

Las propuestas de mejora se centran en reforzar la revisión del sistema, sin introducir nuevos elementos técnicos.

**Valoración cualitativa: Baja**

## SEG4 — Gestión y mantenimiento de dominios DNS

Este subproyecto implica la administración de dominios DNS, incluyendo su mantenimiento, actualización y control de consistencia.

La propuesta describe tareas generales de gestión de dominios sin definir procedimientos específicos ni herramientas asociadas. **No se desarrollan mecanismos de automatización ni control de errores.**

Las propuestas de mejora reproducen el mismo planteamiento sin aportar elementos adicionales.

**Valoración cualitativa: Baja**

## SEG5 — Análisis y corrección de vulnerabilidades

El subproyecto SEG5 exige la identificación y mitigación de vulnerabilidades mediante el uso de herramientas y metodologías específicas.

La propuesta plantea la revisión de sistemas y la corrección de vulnerabilidades sin identificar herramientas ni procesos de análisis. **No se definen metodologías de evaluación ni clasificación de riesgos.**

Las propuestas de mejora mantienen este enfoque general sin introducir mecanismos técnicos adicionales.

**Valoración cualitativa: Baja**

## SEG6 — Detección de intrusiones y análisis de logs

Este subproyecto requiere la implantación de mecanismos de detección de intrusiones basados en el análisis de logs y la correlación de eventos.

**La propuesta describe la revisión de logs sin definir sistemas SIEM ni arquitecturas de detección avanzada.** No se contemplan procesos de correlación ni respuestas automatizadas.

Las propuestas de mejora se limitan a reforzar el seguimiento, sin aportar elementos técnicos adicionales.

**Valoración cualitativa: Baja**

## SEG7 — Auditorías internas de aplicaciones

El subproyecto SEG7 exige la realización de auditorías de seguridad en aplicaciones siguiendo metodologías estructuradas.

**La propuesta menciona la ejecución de auditorías sin definir metodologías ni estándares de referencia.** No se identifican herramientas ni procesos de evaluación detallados.

Las propuestas de mejora mantienen este mismo nivel de generalidad.

**Valoración cualitativa: Baja**

## SEG8 — Auditorías internas continuas de sistemas

Este subproyecto amplía el anterior al conjunto de sistemas, requiriendo un enfoque continuo de auditoría.

**La propuesta describe revisiones periódicas sin desarrollar mecanismos de monitorización continua ni procesos estructurados.** No se identifican herramientas ni métricas de control.

Las propuestas de mejora reproducen el mismo patrón.

**Valoración cualitativa: Baja**

## SEG9 — Mantenimiento y uso de logs centralizados

El subproyecto SEG9 exige la centralización de logs para su análisis y gestión.

**La propuesta menciona la recopilación de logs sin definir arquitectura, almacenamiento ni explotación de información.** No se desarrollan procesos de análisis ni correlación de eventos.

Las propuestas de mejora no incorporan elementos adicionales.

**Valoración cualitativa: Baja**

## SEG10 — Implementación y mantenimiento de claves RSA unificadas

Este subproyecto implica la gestión de claves criptográficas, incluyendo su creación, distribución y renovación.

**La propuesta se limita a mencionar la gestión de claves sin describir procedimientos técnicos ni herramientas específicas.** No se identifican mecanismos de control ni protección del ciclo de vida.

Las propuestas de mejora no aportan contenido adicional.

**Valoración cualitativa: Baja**

## SEG11 — Asistencia en eventos de ciberseguridad

Este subproyecto contempla la participación en eventos y el soporte técnico asociado.

**La propuesta describe la asistencia de forma general sin desarrollar la prestación técnica ni definir tareas concretas.** No se identifican procedimientos asociados al soporte.

Las propuestas de mejora mantienen este enfoque descriptivo.

**Valoración cualitativa: Baja**

### BLOQUE CON — AUTOMATIZACIÓN Y CONTENEDORES

## CON1 — Mantenimiento y mejora del sistema de gestión de contenedores

El subproyecto CON1 requiere la gestión de plataformas de contenedores, incluyendo su mantenimiento, actualización y evolución mediante herramientas específicas.

**La propuesta de empresa_n describe la actualización de sistemas y el uso de scripts generales sin identificar tecnologías concretas ni arquitecturas de contenedores.** No se desarrollan mecanismos de orquestación ni despliegue.

Las propuestas de mejora se limitan a reforzar las tareas descritas, sin introducir elementos técnicos adicionales.

**Valoración cualitativa: Muy baja**

## CON2 — Mantenimiento y mejora de scripts y automatización de tareas

Este subproyecto exige la automatización de tareas mediante scripts en un entorno complejo.

**La propuesta menciona la automatización sin identificar herramientas ni arquitecturas de gestión centralizada.** No se describen procesos ni control de ejecución.

Las propuestas de mejora mantienen el mismo enfoque general.

**Valoración cualitativa: Muy baja**

## CON3 — Mantenimiento del sistema auxiliar de automatización

El subproyecto requiere la gestión de sistemas auxiliares de automatización de procesos.

**La propuesta describe el mantenimiento de sistemas sin desarrollar componentes ni procedimientos técnicos.** No se identifican herramientas ni mecanismos de integración.

Las propuestas de mejora no aportan elementos adicionales.

**Valoración cualitativa: Muy baja**

### BLOQUE MIG — GESTIÓN DE LA MIGRACIÓN DE SERVIDORES ENTRE CPDs

## MIG1 — Coordinación y planificación de la revisión de los entornos migrados

**El subproyecto MIG1 establece la necesidad de coordinar y planificar la revisión de los entornos tras los procesos de migración, lo que implica la verificación del estado de los sistemas, la comprobación de los servicios afectados y la coordinación entre los distintos equipos técnicos implicados.** Este tipo de tareas requiere una metodología estructurada que permita validar la correcta transición de los sistemas entre entornos.

La propuesta de empresa_n aborda este subproyecto mediante referencias generales a la coordinación de equipos y a la revisión de los entornos migrados, sin definir un marco metodológico concreto. No se describen procedimientos de validación, ni criterios de aceptación, ni mecanismos de comprobación de dependencias entre sistemas. **Las propuestas de mejora se limitan a reforzar la revisión posterior a la migración sin incorporar herramientas, fases ni controles adicionales que permitan evaluar la ejecución del proceso de forma estructurada.**

**Valoración cualitativa: Baja**

## MIG2 — Fases preparatorias y planificación técnica de la migración

Este subproyecto exige la definición de las fases previas a la migración, incluyendo la planificación técnica, el análisis de dependencias y la preparación de los sistemas, lo que requiere una estructuración clara del proceso.

**La propuesta de empresa_n menciona la planificación de las migraciones de forma general, sin definir fases ni cronogramas, ni establecer una secuencia de actuaciones.** No se identifican análisis de dependencias ni mecanismos de coordinación entre sistemas. Las propuestas de mejora reproducen este mismo enfoque, sin aportar elementos adicionales que permitan estructurar el proceso de migración en fases claramente definidas.

**Valoración cualitativa: Baja**

## MIG3 — Preparación de servidores y documentación de sistemas

El subproyecto MIG3 implica la preparación de los servidores antes de la migración, incluyendo la revisión de configuraciones, la estandarización de sistemas y la generación de documentación técnica.

**La propuesta de empresa_n describe la preparación de servidores y la elaboración de documentación de forma genérica, sin desarrollar procedimientos concretos ni herramientas de automatización.** No se definen plantillas, criterios de validación ni mecanismos de estandarización. Las propuestas de mejora se centran en reforzar estas tareas sin incorporar mecanismos adicionales que permitan evaluar la preparación de sistemas en un entorno complejo.

**Valoración cualitativa: Baja**

## MIG4 — Verificación de la migración

Este subproyecto requiere la validación del proceso de migración mediante la comprobación de la integridad de los sistemas, la disponibilidad de los servicios y la correcta transferencia de los datos.

La propuesta de empresa_n menciona la verificación del proceso tras la migración, sin definir procedimientos específicos ni criterios de validación. No se describen mecanismos de comprobación de integridad ni herramientas de validación de servicios. **Las propuestas de mejora refuerzan la revisión posterior sin incorporar metodologías adicionales que permitan verificar el resultado de la migración de forma objetiva.**

**Valoración cualitativa: Baja**

## MIG5 — Mantenimiento y soporte tras la migración

El subproyecto MIG5 establece la necesidad de proporcionar soporte posterior a la migración, incluyendo la resolución de incidencias y la estabilización del sistema.

La propuesta de empresa_n describe el soporte de forma general, haciendo referencia a la resolución de incidencias y seguimiento del sistema, sin definir mecanismos de monitorización ni procedimientos de estabilización. No se identifican métricas ni indicadores de estado. **Las propuestas de mejora se limitan a reforzar el seguimiento sin aportar elementos adicionales que permitan evaluar la fase post-migración.**

**Valoración cualitativa: Baja**

### BLOQUE IA — INTELIGENCIA ARTIFICIAL

## IA1 a IA5 — Evaluación global del bloque

El bloque IA incluye un conjunto de subproyectos orientados a la incorporación y gestión de capacidades de inteligencia artificial dentro de la plataforma EducaMadrid, abarcando la evaluación de modelos, la ingeniería de prompts, la implantación de mecanismos de control, la integración con otros sistemas y la gestión del consumo por usuario.

El análisis de la memoria técnica presentada por empresa_n pone de manifiesto que no se presenta contenido técnico evaluable para este bloque en su conjunto. **Los apartados correspondientes se limitan a reproducir o reformular los enunciados de los requisitos definidos en el Anexo II del Documento de Invitación, sin desarrollar propuestas técnicas, metodologías, herramientas ni procedimientos operativos asociados a estos subproyectos.** No se identifican arquitecturas de integración, métricas de evaluación, mecanismos de control ni elementos de despliegue que permitan valorar la capacidad real de ejecución en este ámbito.

Como consecuencia, no es posible realizar una evaluación técnica individualizada de los subproyectos incluidos en este bloque, al no existir un desarrollo específico que permita analizar su adecuación a los requisitos planteados.

**Valoración cualitativa: Muy baja en todos los subproyectos del bloque IA**

### CONCLUSIÓN GLOBAL DEL CAPÍTULO 2

El análisis detallado de los subproyectos incluidos en el Anexo II permite constatar que la propuesta presentada por empresa_n presenta una cobertura formal amplia de los requisitos, en el sentido de que identifica los distintos ámbitos funcionales del servicio. **Sin embargo, dicha cobertura se materializa fundamentalmente a través de descripciones genéricas basadas en actividades habituales de mantenimiento, revisión y seguimiento, sin un desarrollo técnico suficiente.**

**De forma reiterada a lo largo de todos los bloques analizados, se observa que las propuestas de mejora no constituyen una evolución real de la solución, sino que se limitan a reforzar o ampliar las tareas ya descritas.** Estas mejoras se formulan en términos generales, sin definición de herramientas, metodologías ni procedimientos diferenciados, lo que impide considerarlas como aportaciones de valor relevante dentro de la propuesta técnica.

Asimismo, se identifican carencias estructurales significativas. Destaca especialmente la **ausencia de desarrollo técnico en bloques completos** como el sistema operativo **MAX** y el ámbito de inteligencia artificial (**IA**), donde la propuesta se mantiene en un nivel meramente descriptivo o conceptual. Esta circunstancia supone una limitación crítica en la evaluación del conjunto de la propuesta.

Por otra parte, la propuesta **evidencia en distintos apartados una falta de adecuación tecnológica**, incluyendo referencias incorrectas a sistemas o reutilización de contenidos no adaptados al subproyecto analizado. Este tipo de inconsistencias reduce la confianza en el grado de conocimiento del entorno EducaMadrid, en la adecuación real de la solución planteada.

**En conjunto, la propuesta técnica presenta un carácter marcadamente descriptivo, con escaso nivel de detalle técnico, ausencia de arquitecturas definidas y falta de identificación de herramientas y metodologías.** Estas circunstancias limitan de forma significativa la capacidad de evaluar la viabilidad real de la solución, así como su adecuación a un entorno de alta complejidad como el que constituye la plataforma EducaMadrid.

Las deficiencias técnicas identificadas de forma reiterada en los distintos bloques, en particular la ausencia de desarrollo operativo, la falta de herramientas y metodologías, así como la inexistencia de contenido técnico evaluable en determinados ámbitos, tienen un impacto directo en la valoración realizada conforme a los criterios del apartado 7.2.2 del Documento de Invitación, justificando las puntuaciones asignadas en el capítulo 3 del presente informe.

## EVALUACIÓN CONFORME A LOS CRITERIOS DEL APARTADO 7.2.2 DEL Documento de Invitación

### EVALUACIÓN DE LA SOLUCIÓN TÉCNICA OFERTADA (HASTA 15 PUNTOS)

De conformidad con lo establecido en el apartado 7.2.2 del Documento de Invitación, la evaluación de la solución técnica ofertada se realiza atendiendo a los subcriterios definidos en dicho apartado, que incluyen la arquitectura planteada, el grado de comprensión de los requisitos, la viabilidad del proyecto, la metodología de trabajo, el rendimiento previsible de las soluciones y, de forma especialmente relevante, la satisfacción de los requisitos establecidos en el Anexo II.

**La valoración se ha llevado a cabo aplicando de forma estricta la escala cualitativa recogida en el propio Documento de Invitación, conforme a la cual los distintos subcriterios se clasifican en los niveles de excelente, alta, media, baja o muy baja, siendo estos niveles posteriormente transformados en puntuaciones cuantitativas proporcionales al peso de cada subcriterio.** Para la aplicación de dicha escala se han considerado como elementos determinantes el nivel de concreción técnica de la propuesta, su verificabilidad, la existencia de procedimientos operativos definidos, la identificación de herramientas específicas y la coherencia global entre los distintos componentes de la solución planteada.

#### Arquitectura planteada en los distintos subproyectos (máximo 2 puntos)

La propuesta presentada por empresa_n incluye una descripción amplia del ecosistema tecnológico de EducaMadrid, en la que se identifican los principales sistemas, su carácter distribuido y la interrelación entre los diferentes componentes que configuran la plataforma. **Este aspecto evidencia una adecuada comprensión del entorno tecnológico en el que se desarrollará el servicio, así como de su complejidad y criticidad.**

**Sin embargo, desde el punto de vista de los criterios establecidos en el Documento de Invitación, la evaluación de la arquitectura no se limita a la correcta identificación del entorno existente, sino que exige la definición de una arquitectura propia, específica y técnicamente desarrollada que permita verificar cómo se implementará la solución propuesta.** En este sentido, el análisis detallado permite constatar que la propuesta no incorpora una arquitectura técnica definida, sino que se limita en gran medida a describir el estado actual del sistema o a reproducir elementos ya existentes en el entorno.

**Se observa, en particular, la ausencia de diagramas arquitectónicos desarrollados por el licitador que representen la solución propuesta, la falta de definición de relaciones entre componentes y la inexistencia de modelos concretos de distribución de servicios, escalabilidad o alta disponibilidad.** Asimismo, no se identifican arquitecturas específicas por subproyecto ni se definen mecanismos técnicos asociados a elementos críticos como balanceo de carga, replicación, segmentación funcional o resiliencia del sistema.

**Estas carencias adquieren una especial relevancia en bloques tecnológicos que, por su naturaleza, requieren un desarrollo arquitectónico detallado, como son los ámbitos de bases de datos, cloud, inteligencia artificial o el sistema operativo MAX.** En estos casos, la propuesta se mantiene en un plano conceptual o descriptivo, sin aportar diseño técnico alguno que permita evaluar su aplicabilidad real.

**Adicionalmente, se han detectado algunos elementos que no se ajustan adecuadamente al entorno tecnológico de EducaMadrid, como la inclusión de arquitecturas no alineadas con el modelo real del sistema o la reutilización de esquemas no adaptados al contexto específico del contrato.** Este tipo de inconsistencias reduce la credibilidad de la propuesta y añade incertidumbre respecto a su adecuación técnica.

**Como consecuencia de todo lo anterior, no resulta posible evaluar adecuadamente aspectos esenciales exigidos por el Documento de Invitación, tales como la capacidad de escalado del sistema, su comportamiento ante situaciones de alta carga, la distribución eficiente de los servicios o la resiliencia frente a fallos.** En consecuencia, la arquitectura presentada debe considerarse identificada a nivel conceptual, pero no definida ni desarrollada a nivel técnico, lo que limita de forma significativa su verificabilidad.

De acuerdo con la escala de valoración establecida en el Documento de Invitación, esta situación se corresponde con un nivel de evaluación medio, en tanto existe una comprensión general del entorno, pero no una propuesta arquitectónica definida y verificable.

En consecuencia, la valoración asignada a este subcriterio asciende a 0,90 puntos sobre un máximo de 2 puntos.

#### Grado de comprensión de los requisitos planteados (máximo 2 puntos)

**La memoria técnica presentada por empresa_n incluye un desarrollo extenso de la comprensión de los requisitos del Documento de Invitación, en el que se identifican adecuadamente el objeto del contrato, su carácter evolutivo y correctivo, la criticidad del entorno y la necesidad de garantizar la continuidad del servicio junto con elevados niveles de disponibilidad, rendimiento y seguridad.** Esta exposición evidencia un esfuerzo significativo por parte del licitador en la interpretación global del alcance del contrato.

**Asimismo, se reconoce de forma adecuada la estructura del Documento de Invitación por bloques funcionales y se identifican los distintos ámbitos tecnológicos implicados, lo que permite afirmar que la comprensión conceptual del servicio es correcta desde un punto de vista teórico.** No obstante, el análisis conjunto de la memoria técnica y del desarrollo por subproyectos realizado en el capítulo 2 pone de manifiesto una diferencia significativa entre dicha comprensión declarada y su traducción efectiva en soluciones técnicas concretas.

**En particular, se observa que la identificación de requisitos no se acompaña de una definición de procedimientos específicos que permitan su cumplimiento, ni de la selección de herramientas técnicas que soporten su ejecución.** Del mismo modo, en numerosos subproyectos no se desarrollan mecanismos operativos que permitan materializar las necesidades identificadas, lo que evidencia una limitación en la capacidad de trasladar la comprensión conceptual a una solución técnica efectiva.

**Esta situación resulta especialmente visible en ámbitos como la monitorización, donde se identifica la necesidad de disponer de sistemas avanzados pero no se definen métricas ni herramientas; en el ámbito de bases de datos, donde se reconoce la importancia de la optimización sin desarrollar metodologías concretas; o en el caso de las migraciones, donde no se establecen fases ni procedimientos detallados.** Asimismo, en bloques completos como inteligencia artificial o sistema MAX, la comprensión teórica no se traduce en ningún contenido técnico evaluable.

**A estas limitaciones se añaden determinadas inconsistencias técnicas detectadas en la propuesta, tales como la inclusión de referencias a tecnologías no alineadas con el entorno del Documento de Invitación o la reutilización de contenidos no adaptados a los subproyectos correspondientes.** Estas circunstancian afectan de forma directa a la valoración de la comprensión real del servicio, al evidenciar una falta de ajuste en determinados aspectos técnicos.

**En consecuencia, si bien la comprensión del Documento de Invitación puede considerarse adecuada en términos conceptuales, su aplicación práctica resulta limitada, lo que condiciona su valoración global.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel medio, dado que la comprensión es correcta pero no se materializa de forma suficiente en la solución técnica.

La puntuación asignada a este subcriterio asciende, por tanto, a 1,00 puntos sobre un máximo de 2 puntos.

#### Viabilidad del proyecto en general (máximo 1 punto)

**La propuesta presentada por empresa_n plantea una viabilidad general coherente desde un punto de vista estructural, en la medida en que se articula en torno a los distintos bloques funcionales definidos en el Documento de Invitación y recoge, al menos a nivel descriptivo, las principales líneas de actuación requeridas para la prestación del servicio.** Esta aproximación permite identificar una cierta lógica interna en la organización del documento, así como una alineación formal con el alcance del contrato.

**No obstante, el análisis técnico detallado evidencia que la viabilidad real del proyecto se encuentra condicionada por la falta de desarrollo de los elementos necesarios para su ejecución efectiva.** En particular, se constata que la propuesta no define procedimientos operativos concretos que permitan determinar cómo se llevarán a cabo las actuaciones descritas, ni identifica herramientas específicas que sirvan de base tecnológica para la prestación del servicio. Asimismo, no se desarrollan arquitecturas que permitan comprender cómo se integran los distintos componentes del sistema ni cómo se gestionarán aspectos críticos como la disponibilidad, la escalabilidad o la distribución de cargas.

**Estas carencias se refuerzan al analizar determinados bloques en los que la propuesta no presenta contenido técnico evaluable, como ocurre en el caso del sistema operativo MAX o en el ámbito de inteligencia artificial, donde se limita a reproducir los requisitos del Documento de Invitación sin aportar soluciones.** Esta ausencia de desarrollo técnico en ámbitos completos introduce una incertidumbre relevante respecto a la capacidad global de ejecución del servicio.

**Adicionalmente, la presencia de determinadas inconsistencias técnicas, derivadas de la reutilización de contenidos no adaptados o de la inclusión de referencias tecnológicas incorrectas, reduce la confianza en la adecuación real de la propuesta al entorno específico de EducaMadrid.** Estas circunstancias, en conjunto, impiden evaluar con precisión la capacidad operativa del licitador, así como la viabilidad efectiva de la solución planteada.

**En consecuencia, si bien la propuesta presenta coherencia desde un punto de vista formal, la falta de concreción técnica y de elementos verificables limita de forma significativa su viabilidad real.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel de valoración medio, al existir una cobertura general del alcance pero sin acreditación suficiente de la capacidad de ejecución.

La puntuación asignada a este subcriterio asciende a 0,40 puntos sobre un máximo de 1 punto.

#### Metodología de trabajo aplicada (máximo 1 punto)

La propuesta de empresa_n incorpora como marco metodológico la metodología Métrica V3, junto con referencias a estándares reconocidos en el ámbito de la gestión de servicios y del desarrollo de sistemas de información. **Este planteamiento constituye un elemento positivo en la medida en que se apoya en metodologías consolidadas y ampliamente utilizadas en el sector.**

**Sin embargo, el análisis detallado pone de manifiesto que la utilización de estos marcos metodológicos se realiza a un nivel fundamentalmente teórico, reproduciendo en gran medida la estructura de los estándares sin adaptarlos de manera específica al objeto del contrato ni a las particularidades del entorno EducaMadrid.** En este sentido, no se identifican procedimientos concretos de aplicación de la metodología en los distintos subproyectos, ni se definen mecanismos de control, seguimiento o validación asociados a su implantación.

Asimismo, la propuesta no establece una integración clara entre la metodología descrita y la operativa real del servicio, especialmente en ámbitos como la gestión de incidencias, la ejecución de tareas recurrentes o la gestión de cambios. **Tampoco se identifican herramientas que soporten la aplicación efectiva de la metodología, lo que limita su capacidad para ser utilizada como un instrumento operativo dentro del servicio.**

Esta falta de adaptación al contexto específico del contrato implica que la metodología se presenta como un marco conceptual de referencia, pero no como un modelo de trabajo directamente aplicable. **Como consecuencia, su impacto en la calidad y en la ejecución del servicio resulta limitado desde el punto de vista de los criterios del Documento de Invitación.**

De acuerdo con la escala establecida en el Documento de Invitación, esta situación se corresponde con un nivel de valoración medio, al existir una referencia a metodologías reconocidas pero sin un desarrollo operativo concreto que permita su aplicación efectiva.

La valoración asignada a este subcriterio asciende a 0,50 puntos sobre un máximo de 1 punto.

#### Rendimiento previsible de las distintas soluciones (máximo 1 punto)

La propuesta de empresa_n incluye diversas referencias al rendimiento esperado de la solución, indicando que este se basará en un enfoque de monitorización continua, mantenimiento proactivo y optimización progresiva del sistema. **Estas afirmaciones reflejan una intención de garantizar un adecuado comportamiento de la plataforma desde el punto de vista operativo.**

**No obstante, el análisis técnico evidencia que dichas afirmaciones no se sustentan en elementos verificables que permitan evaluar de forma objetiva el rendimiento propuesto.** En particular, no se definen indicadores de rendimiento que permitan medir la calidad del servicio, tales como tiempos de respuesta, latencias, niveles de disponibilidad o capacidad de procesamiento. Tampoco se establecen umbrales de funcionamiento ni objetivos cuantificables que permitan determinar cuándo el sistema cumple o no con los requisitos de rendimiento establecidos.

Del mismo modo, no se identifican herramientas específicas de monitorización ni sistemas de medición que permitan obtener datos operativos sobre el comportamiento de la plataforma. **La propuesta se limita a mencionar de forma genérica la existencia de mecanismos de supervisión, sin detallar su naturaleza ni su funcionamiento.** Asimismo, no se describen escenarios de prueba que permitan evaluar el comportamiento del sistema ante situaciones de carga elevada o ante condiciones de estrés.

**Estas carencias son especialmente relevantes en un entorno como el de EducaMadrid, caracterizado por un elevado número de usuarios y por la necesidad de garantizar un funcionamiento continuo y estable.** La ausencia de un modelo de evaluación del rendimiento impide verificar la adecuación de la solución propuesta a estos requisitos.

**En consecuencia, el rendimiento planteado presenta un carácter declarativo, basado en afirmaciones generales que no pueden ser contrastadas mediante elementos técnicos objetivos.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel de valoración bajo, al no existir evidencia suficiente que permita evaluar el rendimiento de la solución.

La puntuación asignada a este subcriterio asciende a 0,25 puntos sobre un máximo de 1 punto.

#### Satisfacción de los requisitos (máximo 8 puntos)

**El subcriterio de satisfacción de los requisitos constituye el elemento de mayor ponderación dentro de la evaluación de la solución técnica, por lo que su análisis resulta determinante para la valoración global de la propuesta.** Este criterio no se limita a verificar la cobertura formal de los subproyectos incluidos en el Anexo II, sino que exige evaluar el grado en que la solución presentada permite satisfacer de manera efectiva los requisitos técnicos planteados, incluyendo la existencia de procedimientos, herramientas, metodologías y capacidades operativas que garanticen su ejecución.

A efectos de la presente evaluación, se entiende por solución técnica adecuada aquella que incorpore elementos verificables, tales como procedimientos definidos, herramientas identificadas y mecanismos de ejecución contrastables, de conformidad con el criterio de verificabilidad implícito en el apartado 7.2.2 del Documento de Invitación.

El análisis realizado en el capítulo 2 permite concluir que la propuesta de empresa_n presenta una cobertura formal amplia de los subproyectos, en el sentido de que identifica los distintos ámbitos funcionales del servicio y desarrolla descripciones asociadas a cada uno de ellos. **No obstante, esta cobertura formal no se traduce en una satisfacción técnica efectiva de los requisitos, ya que en la mayoría de los casos las propuestas se limitan a describir actividades genéricas de mantenimiento, supervisión o revisión, sin aportar desarrollo técnico suficiente.**

De forma generalizada, las soluciones planteadas no incorporan procedimientos operativos concretos, ni identifican herramientas específicas que permitan su ejecución. **Tampoco se desarrollan arquitecturas, metodologías o mecanismos de automatización que aporten valor añadido al cumplimiento de los requisitos.** Esta situación impide considerar que la propuesta satisface los requisitos desde un punto de vista técnico, al no demostrar cómo se llevarán a cabo las actuaciones en un entorno real.

Asimismo, se identifican bloques completos en los que no existe contenido técnico evaluable, como ocurre en el caso del sistema operativo MAX o en el ámbito de inteligencia artificial. **En estos casos, la propuesta se limita a reproducir los requisitos del Documento de Invitación sin aportar soluciones, lo que supone una deficiencia estructural que afecta de manera directa a la valoración del conjunto.**

**A estas carencias se añaden determinadas inconsistencias, derivadas de la reutilización de contenidos no adaptados o de la inclusión de referencias incorrectas, que reducen la adecuación de la propuesta a los requisitos planteados.** Del mismo modo, las denominadas propuestas de mejora no introducen elementos técnicos adicionales, sino que se limitan a reforzar las tareas ya descritas, sin aportar metodologías ni herramientas que permitan considerarlas como un valor diferencial.

**En consecuencia, la propuesta presenta una cobertura formal de los requisitos, pero una satisfacción técnica limitada, caracterizada por un reducido nivel de desarrollo, una baja verificabilidad y una ausencia de elementos críticos en ámbitos relevantes del servicio.** Conforme a la escala del Documento de Invitación, esta situación se corresponde con un nivel de valoración bajo, al situarse claramente por debajo de los niveles exigidos para considerar la solución como adecuada desde un punto de vista técnico.

La valoración asignada a este subcriterio asciende a 2,00 puntos sobre un máximo de 8 puntos.

#### RESULTADO GLOBAL — SOLUCIÓN TÉCNICA

La suma de las valoraciones obtenidas en los distintos subcriterios permite establecer el resultado global de la solución técnica ofertada, que se recoge en la siguiente tabla:

| **Subcriterio** | **Puntuación** |
| --- | --- |
| Arquitectura | 0,90 |
| Comprensión de requisitos | 1,00 |
| Viabilidad | 0,40 |
| Metodología | 0,50 |
| Rendimiento | 0,25 |
| Satisfacción de requisitos | 2,00 |

**Valoración Total para la Solución Técnica Ofertada: 5,***05 puntos sobre 15 puntos**

### EVALUACIÓN DE LA PLANIFICACIÓN DEL SERVICIO (HASTA 15 PUNTOS)

De conformidad con lo establecido en el apartado 7.2.2 del Documento de Invitación, la planificación del servicio se evalúa atendiendo a la calidad, coherencia y nivel de detalle del modelo organizativo y temporal propuesto por el licitador, incluyendo el calendario de ejecución, el análisis de riesgos, el plan de contingencias, el modelo de calidad y los mecanismos de trazabilidad.

En el caso analizado, la propuesta de empresa_n incorpora un diagrama de Gantt como elemento central de planificación temporal, tal y como se recoge en la documentación técnica presentada.

El análisis conjunto de ambos diagramas, junto con el contenido descriptivo asociado, pone de manifiesto una serie de deficiencias estructurales que afectan de forma directa a la capacidad de evaluar la planificación operativa del servicio.

#### Planificación temporal y cronograma de ejecución (máximo 11 puntos)

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

En consecuencia, la puntuación asignada a este subcriterio se fija en **5,00 puntos** sobre un máximo de 11 puntos.

#### Análisis de riesgos del proyecto (máximo 1 punto)

**La propuesta de empresa_n incluye un apartado dedicado al análisis de riesgos en el que se identifican distintos factores que podrían afectar a la prestación del servicio, tales como incidencias técnicas, problemas operativos o situaciones derivadas de la complejidad del entorno.** Este enfoque permite constatar que el licitador ha considerado la existencia de riesgos asociados al desarrollo del contrato.

**Sin embargo, el análisis presentado se mantiene en un nivel general, sin desarrollar una metodología específica de gestión del riesgo que permita su aplicación efectiva.** En particular, no se observa una cuantificación de los riesgos identificados ni una evaluación de su probabilidad de ocurrencia o de su impacto potencial sobre el servicio. Del mismo modo, no se establece una priorización de los riesgos que permita focalizar la gestión en aquellos con mayor relevancia.

**Asimismo, los riesgos identificados no se vinculan de forma directa con los subproyectos concretos definidos en el Anexo II, lo que limita la capacidad de trasladar este análisis a un contexto operativo real.** Tampoco se definen mecanismos específicos de seguimiento o indicadores que permitan monitorizar la evolución de los riesgos a lo largo del tiempo.

**En consecuencia, el análisis de riesgos presentado puede considerarse adecuado desde un punto de vista conceptual, pero insuficiente desde una perspectiva operativa, al no proporcionar las herramientas necesarias para una gestión efectiva del riesgo.** Conforme a la escala del Documento de Invitación, esta situación se corresponde con un nivel medio.

La valoración asignada a este subcriterio asciende a **0,***25 puntos** sobre un máximo de 1 punto.

#### Plan de gestión de contingencias (máximo 1 punto)

**El plan de contingencias presentado por empresa_n incluye referencias a la adopción de medidas generales para garantizar la continuidad del servicio ante posibles incidencias, así como a la existencia de mecanismos de recuperación y de coordinación en situaciones de fallo.** Este planteamiento evidencia la consideración de la necesidad de contar con procedimientos de respuesta ante eventos adversos.

**No obstante, el análisis detallado pone de manifiesto que dichas medidas no se desarrollan con el nivel de concreción necesario para su aplicación efectiva.** En particular, no se definen procedimientos específicos asociados a escenarios concretos de fallo, ni se establecen tiempos de recuperación que permitan evaluar la capacidad de respuesta del sistema ante incidencias relevantes. Tampoco se identifican responsables, recursos asociados o secuencias de actuación que permitan estructurar el plan de contingencias de manera operativa.

**Asimismo, no se establece una relación directa entre el plan de contingencias y los riesgos previamente identificados, lo que limita la coherencia global del modelo de gestión propuesto.** Esta falta de integración reduce la eficacia del plan y dificulta su aplicación en situaciones reales.

**En consecuencia, el plan de contingencias presenta un carácter generalista, basado en principios de actuación comunes, pero sin un desarrollo técnico suficiente que permita su implantación.** De acuerdo con la escala del Documento de Invitación, esta situación se corresponde con un nivel medio-bajo.

La puntuación asignada a este subcriterio asciende a **0,***25 puntos** sobre un máximo de 1 punto.

#### Plan de gestión de la calidad del servicio (máximo 1 punto)

El plan de calidad presentado por empresa_n incorpora referencias generales a acuerdos de nivel de servicio, clasificación de incidencias y seguimiento del servicio, lo que evidencia una orientación inicial hacia la gestión de la calidad. **No obstante, el análisis detallado pone de manifiesto que este planteamiento se mantiene en un nivel fundamentalmente conceptual, sin el desarrollo operativo necesario para su aplicación efectiva.**

En particular, no se definen indicadores cuantificables que permitan medir el rendimiento del servicio ni se establecen métricas asociadas a los objetivos del contrato. **Esta ausencia impide verificar el cumplimiento de los niveles de servicio y limita la capacidad de control del sistema desde un punto de vista objetivo.**

**Adicionalmente, no se describen herramientas ni sistemas de monitorización del cumplimiento de los ANS, ni se establece un modelo de seguimiento continuo basado en la recogida y análisis de datos.** Esta carencia resulta especialmente relevante a la vista del diagrama de Gantt presentado, en el que tampoco se integran mecanismos que permitan relacionar la planificación temporal con la medición de la calidad del servicio.

Asimismo, no se observa la existencia de procesos estructurados de mejora continua basados en resultados medibles, lo que limita la capacidad evolutiva del modelo propuesto.

En consecuencia, el plan de calidad presenta un carácter generalista, con un nivel de desarrollo insuficiente para su aplicación efectiva, lo que justifica su valoración en un nivel medio-bajo conforme a la escala del Documento de Invitación.

La valoración asignada a este subcriterio asciende a **0,***5***0 puntos** sobre un máximo de 1 punto.

#### Trazabilidad del servicio (máximo 1 punto)

**La propuesta contempla mecanismos generales de seguimiento y registro de las actuaciones realizadas, incluyendo referencias a la documentación de intervenciones y al uso de herramientas de gestión.** Este planteamiento permite identificar una intención inicial de dotar al servicio de trazabilidad.

**Sin embargo, el análisis detallado pone de manifiesto que estos mecanismos no se desarrollan hasta constituir un sistema completo y verificable de trazabilidad.** En particular, no se define un modelo que permita relacionar de forma directa los requisitos del Documento de Invitación con las actividades ejecutadas, ni se establecen vínculos claros entre los subproyectos del Anexo II y la planificación temporal del servicio.

**Esta carencia resulta especialmente evidente al analizar el diagrama de Gantt, en el que no existe una correspondencia estructurada entre las tareas planificadas y los subproyectos definidos en el Documento de Invitación, ni se proporciona una codificación o sistema de referencia que permita realizar dicha vinculación.** Como consecuencia, no es posible determinar con precisión qué actividades se ejecutan para cada requisito ni en qué momento temporal.

Asimismo, no se identifican herramientas concretas ni procedimientos específicos de gestión de la trazabilidad que permitan garantizar el seguimiento de las actuaciones a lo largo del ciclo de vida del servicio.

En consecuencia, la trazabilidad propuesta presenta un nivel de desarrollo insuficiente y un carácter fundamentalmente declarativo, lo que limita su aplicabilidad real y justifica su valoración en un nivel bajo conforme a la escala del Documento de Invitación.

La puntuación asignada a este subcriterio asciende a **0,***4***0 puntos** sobre un máximo de 1 punto.

### RESULTADO GLOBAL — PLANIFICACIÓN DEL SERVICIO

La suma de las puntuaciones obtenidas en los distintos subcriterios permite establecer el resultado global de la planificación del servicio, que se recoge en la siguiente tabla:

| **Subcriterio** | **Puntuación** |
| --- | --- |
| Planificación y cronograma | 5,00 |
| Análisis de riesgos | 0,25 |
| Plan de contingencias | 0,25 |
| Plan de calidad | 0,50 |
| Trazabilidad | 0,40 |

**Total Planificación del Servicio: 6,40 puntos sobre 15 puntos**

## RESULTADO FINAL CONSOLIDADO

La puntuación total obtenida por la propuesta como resultado de la suma de los bloques de solución técnica y planificación del servicio es la siguiente:

| **Bloque** | **Puntuación** |
| --- | --- |
| Solución técnica ofertada | 5,05 |
| Planificación del servicio | 6,40 |

**PUNTUACIÓN FINAL: 1***1***,***45 puntos sobre un máximo de 30 puntos**

## RESUMEN DE LA VALORACIÓN

### Valoración de la solución técnica ofertada

El análisis de la solución técnica ofertada por la empresa empresa_n, realizado conforme a los criterios establecidos en el apartado 7.2.2 del Documento de Invitación, pone de manifiesto que la propuesta presenta un adecuado grado de estructuración formal y una correcta identificación del entorno tecnológico de EducaMadrid, si bien adolece de una falta significativa de desarrollo técnico en los aspectos clave exigidos para la prestación del servicio.

**En este sentido, la propuesta evidencia un nivel adecuado de comprensión conceptual del objeto del contrato, reflejado en la identificación del carácter evolutivo, correctivo y adaptativo del servicio, así como en la descripción de los distintos bloques funcionales que integran la plataforma.** No obstante, dicha comprensión no se traduce de manera efectiva en el desarrollo de soluciones técnicas concretas, lo que constituye un elemento esencial en la evaluación conforme al Documento de Invitación.

El análisis detallado realizado permite concluir que la solución técnica se apoya fundamentalmente en descripciones generales, en muchos casos coincidentes con la propia redacción del Documento de Invitación, sin incorporar elementos suficientes de concreción tales como arquitecturas técnicas definidas, herramientas específicas, procedimientos operativos o metodologías aplicadas a los distintos subproyectos. **Esta circunstancia limita de manera significativa la verificabilidad de la solución y su aplicabilidad en un entorno real.**

**Asimismo, se han detectado carencias relevantes en la definición de la arquitectura técnica de la solución, que no se desarrolla más allá de una descripción del entorno existente, sin aportar un diseño propio que permita evaluar aspectos fundamentales como la escalabilidad, la resiliencia o la distribución de cargas.** Esta limitación se ve reforzada por la ausencia de métricas de rendimiento, indicadores operativos y modelos de validación que permitan verificar el comportamiento de la solución.

Especial relevancia adquiere el análisis del subcriterio de satisfacción de los requisitos, que constituye el elemento de mayor peso dentro de la valoración de la solución técnica. En este ámbito, si bien la propuesta presenta una cobertura formal de los subproyectos definidos en el Anexo II, no se acredita un grado suficiente de desarrollo técnico que permita concluir que dichos requisitos se encuentran efectivamente satisfechos. **La falta de procedimientos específicos, la ausencia de herramientas identificadas y la inexistencia de desarrollo técnico en determinados bloques, como inteligencia artificial o sistema MAX, limitan de forma significativa la valoración de este subcriterio.**

Hay que tener en cuenta que, a efectos de la evaluación realizada, se entiende por solución técnica adecuada aquella que incorpore elementos verificables, tales como procedimientos definidos, herramientas identificadas y mecanismos de ejecución contrastables, de conformidad con el criterio de verificabilidad implícito en el apartado 7.2.2 del Documento de Invitación.

**En consecuencia, la solución técnica ofertada presenta un nivel de desarrollo limitado desde el punto de vista técnico, con una elevada componente descriptiva y una reducida capacidad de acreditación de la ejecución real del servicio.** De acuerdo con la aplicación de la escala cualitativa establecida en el Documento de Invitación, la valoración global de este bloque se sitúa en un nivel medio-bajo.

La puntuación asignada a la solución técnica ofertada asciende a 5,05 puntos sobre un máximo de 15 puntos.

### Valoración de la planificación del servicio

El análisis del bloque correspondiente a la planificación del servicio pone de manifiesto la existencia de deficiencias estructurales de especial relevancia, que afectan de manera directa a la capacidad del licitador para garantizar una ejecución adecuada del contrato en términos operativos.

La propuesta incorpora un diagrama de Gantt como elemento principal de planificación temporal. **Sin embargo, el examen detallado de dicho diagrama evidencia que el cronograma presentado no se ajusta al concepto de planificación operativa exigido en el Documento de Invitación, ya que presenta un carácter híbrido que dificulta su interpretación y limita su utilidad como herramienta de gestión del servicio.** En particular, el diagrama combina la representación temporal de actividades con valores numéricos y códigos de color cuya naturaleza no se define, ya que no se proporciona una leyenda o modelo interpretativo que permita comprender su significado.

Esta ausencia de definición impide determinar si dichos valores representan cargas de trabajo, niveles de prioridad, dedicación de recursos u otros parámetros, lo que impide, no solo la interpretación del cronograma, sino también su evaluación objetiva conforme a los criterios del Documento de Invitación, al no ser posible determinar el alcance real, intensidad ni naturaleza de las actividades planificadas, viéndose, por tanto, comprometida la verificabilidad del cronograma en su conjunto y su adecuación a los criterios de evaluación establecidos en el Documento de Invitación.

Asimismo, se observa que la planificación no refleja una secuencia temporal estructurada de las actividades, sino que presenta la activación puntual de tareas en determinados meses sin continuidad ni definición clara de su duración. **Esta circunstancia resulta incoherente con la naturaleza del servicio, que se basa en actividades recurrentes y continuas, especialmente en ámbitos como el mantenimiento de sistemas, la gestión de infraestructuras o la seguridad de la plataforma.**

**A ello se suma la ausencia total de dependencias entre tareas, lo que impide identificar relaciones de precedencia, secuencias lógicas de ejecución o posibles caminos críticos.** Esta carencia limita de manera significativa la capacidad de evaluar la coherencia temporal del proyecto y de analizar el impacto de posibles desviaciones en la ejecución del servicio.

El cronograma tampoco incorpora asignación de recursos ni permite vincular las actividades con los perfiles técnicos necesarios para su ejecución, lo que dificulta la evaluación del dimensionamiento del servicio. **Del mismo modo, no se establece una correspondencia clara entre la planificación temporal y los subproyectos definidos en el Anexo II, lo que impide garantizar la trazabilidad de las actuaciones y su alineación con los requisitos del contrato.**

**Estas deficiencias afectan de manera transversal al resto de subcriterios de planificación, en particular al análisis de riesgos y al plan de contingencias, que no se integran de forma efectiva en la planificación temporal.** En concreto, la ausencia de buffers, márgenes de adaptación o escenarios alternativos en el cronograma evidencia una planificación rígida que no contempla la gestión de incidencias ni la reconfiguración operativa en situaciones adversas.

Del mismo modo, el modelo de calidad y los mecanismos de trazabilidad presentan un carácter generalista, sin el desarrollo necesario en términos de indicadores, herramientas o procedimientos que permitan su aplicación efectiva en el contexto del servicio.

En consecuencia, la planificación del servicio, si bien cumple formalmente con los requisitos del Documento de Invitación, presenta un nivel de desarrollo insuficiente desde el punto de vista técnico y operativo, lo que limita su capacidad para garantizar una ejecución eficaz del contrato.

La puntuación asignada a este bloque asciende a **6,40 puntos sobre un máximo de 15 puntos**.

### Tabla resumen de valoración

La valoración conjunta de los distintos subcriterios evaluados mediante juicio de valor se recoge en la siguiente tabla resumen:

<table>
  <tr>
    <th><strong>Bloque</strong></th>
    <th><strong>Subcriterio</strong></th>
    <th><strong>Puntuación máxima</strong></th>
    <th><strong>Puntuación obtenida</strong></th>
  </tr>
  <tr>
    <td rowspan="6">Solución técnica ofertada</td>
    <td>Arquitectura</td>
    <td>2,00</td>
    <td>0,90</td>
  </tr>
  <tr>
    <td>Comprensión de requisitos</td>
    <td>2,00</td>
    <td>1,00</td>
  </tr>
  <tr>
    <td>Viabilidad</td>
    <td>1,00</td>
    <td>0,40</td>
  </tr>
  <tr>
    <td>Metodología</td>
    <td>1,00</td>
    <td>0,50</td>
  </tr>
  <tr>
    <td>Rendimiento</td>
    <td>1,00</td>
    <td>0,25</td>
  </tr>
  <tr>
    <td>Satisfacción de requisitos</td>
    <td>8,00</td>
    <td>2,00</td>
  </tr>
  <tr>
    <td rowspan="5">Planificación del servicio</td>
    <td>Cronograma</td>
    <td>11,00</td>
    <td>5,00</td>
  </tr>
  <tr>
    <td>Riesgos</td>
    <td>1,00</td>
    <td>0,25</td>
  </tr>
  <tr>
    <td>Contingencias</td>
    <td>1,00</td>
    <td>0,25</td>
  </tr>
  <tr>
    <td>Calidad</td>
    <td>1,00</td>
    <td>0,50</td>
  </tr>
  <tr>
    <td>Trazabilidad</td>
    <td>1,00</td>
    <td>0,40</td>
  </tr>
</table>

**TOTAL SOLUCIÓN TÉCNICA: 5,***05 puntos sobre 15 puntos**

**TOTAL PLANIFICACIÓN DEL SERVICIO: 6,40 puntos sobre 15 puntos**

### Conclusión del análisis

De acuerdo con el análisis técnico efectuado y la aplicación de los criterios de valoración establecidos en el apartado 7.2.2 del Documento de Invitación, la propuesta presentada por la empresa empresa_n alcanza una puntuación total de **1***1***,***45 puntos sobre un máximo de 30 puntos**, lo que representa un **3***8,17***% de la puntuación máxima posible** en los criterios evaluables mediante juicio de valor.

Este resultado refleja un nivel de adecuación insuficiente tanto en la solución técnica ofertada como en la planificación del servicio, motivado principalmente por la falta de concreción técnica de la propuesta y por las deficiencias estructurales identificadas en el modelo de planificación, particularmente en el diagrama de Gantt presentado, que no permite verificar la viabilidad operativa del servicio ni su correcta organización temporal.

En conjunto, la propuesta presenta un enfoque predominantemente descriptivo, con una limitada capacidad de acreditación técnica, lo que condiciona de manera significativa su valoración global y su adecuación a las exigencias del Documento de Invitación.

Estas deficiencias afectan de forma significativa a la viabilidad real del servicio y justifican la puntuación obtenida.

## CONCLUSIONES FINALES Y PROPUESTA

### Conclusiones finales

El análisis técnico efectuado sobre la propuesta presentada por la empresa empresa_n, llevado a cabo conforme a los criterios establecidos en el apartado 7.2.2 del Documento de Invitación de Prescripciones Técnicas Particulares, permite concluir que la propuesta evaluada presenta un nivel de adecuación insuficiente para garantizar el cumplimiento efectivo de los requisitos del contrato.

**En relación con la solución técnica ofertada, se ha constatado que, si bien la propuesta presenta una estructura formal alineada con el contenido del Documento de Invitación y una adecuada comprensión conceptual del entorno de EducaMadrid, el desarrollo técnico de la misma resulta limitado.** En concreto, se ha identificado una carencia significativa de elementos fundamentales como arquitecturas técnicas definidas, procedimientos operativos específicos, herramientas concretas y metodologías aplicadas de forma efectiva a los distintos subproyectos. Esta circunstancia impide verificar de manera objetiva la capacidad del licitador para ejecutar el servicio en las condiciones exigidas.

Especial relevancia presenta el subcriterio de satisfacción de los requisitos, en el que, pese a existir una cobertura formal de los ámbitos definidos en el Anexo II, no se acredita un grado suficiente de desarrollo técnico que permita concluir que dichos requisitos se encuentran efectivamente satisfechos. **La ausencia de contenido técnico evaluable en determinados bloques, unida a la falta de concreción en el resto, refleja una propuesta con un enfoque predominantemente descriptivo y con limitada capacidad de ejecución real.**

**Por lo que respecta a la planificación del servicio, el análisis realizado ha puesto de manifiesto deficiencias de carácter estructural que afectan directamente a la viabilidad operativa de la propuesta.** En particular, el diagrama de Gantt presentado como eje central de la planificación temporal evidencia una serie de limitaciones que condicionan de manera significativa su utilización como herramienta de gestión.

**El cronograma no responde a un modelo de planificación operativa en sentido estricto, al carecer de un sistema de interpretación que permita comprender el significado de los valores representados, no reflejar una secuencia temporal coherente de las actividades, no incorporar dependencias entre tareas ni establecer mecanismos de asignación de recursos.** Asimismo, no se observa una adecuada correspondencia entre la planificación temporal y los subproyectos definidos en el Documento de Invitación, lo que impide garantizar la trazabilidad de las actuaciones.

Estas deficiencias, de carácter transversal, afectan a la totalidad del bloque de planificación, incluyendo el análisis de riesgos, el plan de contingencias, el modelo de calidad y los mecanismos de trazabilidad, que presentan un desarrollo insuficiente y un carácter fundamentalmente declarativo, sin que se integren de manera efectiva en la planificación operativa del servicio.

Como resultado de la aplicación de los criterios establecidos en el Documento de Invitación, la propuesta ha obtenido una puntuación de 5,05 puntos sobre 15 en el bloque de solución técnica y de 6,40 puntos sobre 15 en el bloque de planificación del servicio, alcanzando una puntuación total de 11,45 puntos sobre un máximo de 30 puntos, lo que representa un 38,17% de la puntuación máxima posible en los criterios evaluables mediante juicio de valor.

Este nivel de puntuación se sitúa claramente por debajo del umbral mínimo exigible para considerar que la propuesta presenta un grado de calidad técnica suficiente en relación con las exigencias del contrato, evidenciando una insuficiente acreditación de la capacidad del licitador para ejecutar el servicio con el nivel requerido.

### Propuesta de exclusión

De conformidad con los resultados de la valoración técnica expuestos en el apartado anterior, y en aplicación de la normativa vigente en materia de contratación pública, procede analizar la adecuación de la propuesta a los requisitos mínimos establecidos para la continuación en el procedimiento.

En este sentido, debe señalarse que el Acuerdo de Contratación Centralizada correspondiente al **Sistema Dinámico de Adquisición SDA 26/2021**, en el marco del cual se desarrolla el presente procedimiento, establece la posibilidad de fijar umbrales mínimos de puntuación en los criterios evaluables mediante juicio de valor, como condición necesaria para la admisión de las ofertas en fases posteriores del proceso de adjudicación.

**Asimismo, el artículo 146.3 de la Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público, dispone expresamente que, cuando se establezcan criterios cuya cuantificación dependa de un juicio de valor, el órgano de contratación podrá fijar una puntuación mínima que deban obtener las ofertas en dichos criterios para continuar en el proceso selectivo.** Esta previsión tiene como finalidad garantizar que únicamente aquellas ofertas que alcancen un nivel mínimo de calidad técnica puedan ser objeto de valoración en fases posteriores, salvaguardando así el interés público y la correcta ejecución del contrato.

La fijación de dicho umbral y su aplicación en el presente procedimiento tienen carácter objetivo y automático, de modo que su no superación determina la imposibilidad de continuar en el proceso de adjudicación, sin que exista margen de apreciación discrecional por parte del órgano de contratación en esta fase.

**En el presente caso, la normativa aplicable establece un umbral mínimo equivalente al 50% de la puntuación máxima posible en los criterios evaluables mediante juicio de valor.** Teniendo en cuenta que la puntuación máxima en este bloque asciende a 30 puntos, dicho umbral se sitúa en 15 puntos. La aplicación de este umbral se realiza de manera homogénea a todas las ofertas presentadas, en cumplimiento de los principios de igualdad de trato, transparencia y proporcionalidad recogidos en la normativa de contratación pública, garantizando que todas ellas son evaluadas bajo los mismos criterios y condiciones.

**La propuesta presentada por la empresa empresa_n ha obtenido una puntuación total de 11,45 puntos, lo que representa un 38,17% de la puntuación máxima, situándose de manera clara por debajo del umbral mínimo exigido.** Esta circunstancia no constituye una mera diferencia cuantitativa, sino que responde a deficiencias técnicas relevantes identificadas en el análisis de la propuesta, que afectan a aspectos esenciales de la solución técnica y de la planificación del servicio.

En particular, la falta de desarrollo técnico de la propuesta, la insuficiente acreditación de la satisfacción de los requisitos, la ausencia de elementos operativos verificables y las deficiencias estructurales en la planificación temporal, evidenciadas en el diagrama de Gantt presentado, ponen de manifiesto que la propuesta no alcanza el nivel mínimo de calidad necesario para garantizar una ejecución adecuada del contrato.

De acuerdo con lo anterior, y en aplicación de lo dispuesto en el artículo 146.3 de la LCSP, así como de las previsiones establecidas en el Acuerdo de Contratación Centralizada SDA 26/2021, procede proponer la exclusión de la propuesta presentada por la empresa empresa_n del procedimiento de adjudicación, al no haber alcanzado la puntuación mínima exigida en los criterios evaluables mediante juicio de valor.

Esta propuesta de exclusión se fundamenta en criterios objetivos, previamente establecidos en el Documento de Invitación y aplicados de manera homogénea en el proceso de evaluación, garantizando en todo momento los principios de transparencia, igualdad de trato y no discriminación que rigen la contratación pública.

Además, la exclusión propuesta no se fundamenta exclusivamente en la puntuación obtenida, sino en las deficiencias técnicas sustantivas identificadas durante el proceso de evaluación, las cuales se traducen en la puntuación final obtenida y evidencian la insuficiencia de la propuesta para cumplir adecuadamente con los requisitos del contrato.

En consecuencia, se propone al órgano de contratación la exclusión de la propuesta presentada por la empresa empresa_n, continuando el procedimiento con aquellas ofertas que hayan superado el umbral mínimo establecido.

<!-- salto de página -->

## ANEXO CLASIFICACIÓN DEL GRADO DE DESARROLLO DE LAS PROPUESTAS (empresa_n)

## Introducción y criterios de clasificación

En el presente anexo se recoge la clasificación del grado de desarrollo de las propuestas técnicas presentadas por empresa_n para los distintos subproyectos definidos en el Anexo II del Documento de Invitación.

A efectos de este análisis, se han establecido los siguientes niveles de clasificación:

- **Propuesta técnica no incluida** → no existe una propuesta técnica concreta para el subproyecto correspondiente.

- **Propuesta técnica incluida (desarrollo deficiente)** → existe una propuesta técnica pero su definición es genérica, sin procesos o mecanismos de implementación concretos.

- **Propuesta técnica incluida (desarrollo suficiente)** → existe una propuesta técnica concreta, con definición de arquitectura, procesos o mecanismos de implementación.

- **Propuesta técnica con mejoras (sin valor añadido)** → cuando el informe identifica mejoras respecto a los requisitos base, pero éstas se limitan a reforzar actividades ya descritas, sin incorporar nuevas capacidades técnicas ni metodologías diferenciadas.

- **Propuesta técnica con valor añadido** → cuando el informe identifica mejoras que suponen una evolución real de la solución, incorporando herramientas, automatización, arquitecturas o mejoras verificables del servicio.

A efectos de representación en tablas:

- **No** → sin mejora o subproyecto sin propuesta técnica

- **PM** → propuesta de mejora sin valor añadido real

- **VA** → valor añadido real

El análisis evidencia que las propuestas de mejora de empresa_n siguen un patrón reiterado consistente en **reforzar tareas ya descritas sin introducir elementos técnicos adicionales**.

## Tablas de proyectos y grado de desarrollo

### Proyecto BD – Bases de Datos

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| BD1 | Propuesta técnica incluida (desarrollo deficiente) | PM (refuerzo de revisiones sin técnicas nuevas) |
| BD2 | Propuesta técnica incluida (desarrollo deficiente) | PM (ampliación mantenimiento sin herramientas) |
| BD3 | Propuesta técnica incluida (desarrollo deficiente) | PM (actualización CMDB sin automatización) |
| BD4 | Propuesta técnica incluida (desarrollo deficiente) | PM (seguimiento carga sin metodología) |
| BD5 | Propuesta técnica incluida (desarrollo deficiente) | PM (verificación sin sincronización avanzada) |
| BD6 | Propuesta técnica incluida (desarrollo deficiente) | PM (mantenimiento sin enfoque microservicios) |

### Proyecto MON – Monitorización

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| MON1 | Propuesta técnica incluida (desarrollo deficiente) | PM (supervisión ampliada sin criterios técnicos) |
| MON2 | Propuesta técnica incluida (desarrollo deficiente) | PM (más pruebas sin metodología definida) |
| MON3 | Propuesta técnica incluida (desarrollo deficiente) | PM (monitorización ampliada sin métricas) |
| MON4 | Propuesta técnica incluida (desarrollo deficiente) | PM (extensión genérica a IA sin especialización) |

### Proyecto UPD – Actualización de servicios

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| UPD1 | Propuesta técnica incluida (desarrollo deficiente) | PM (validaciones adicionales sin arquitectura) |
| UPD2 | Propuesta técnica incluida (desarrollo deficiente) | PM (repetición del modelo anterior) |
| UPD3 | Propuesta técnica incluida (desarrollo deficiente) | PM (tareas ampliadas sin integración técnica) |
| UPD4 | Propuesta técnica incluida (desarrollo deficiente) | PM (gestión genérica sin herramienta definida) |
| UPD5 | Propuesta técnica incluida (desarrollo suficiente) | PM (mantenimiento convencional sin pipelines) |
| UPD6 | Propuesta técnica incluida (desarrollo deficiente) | PM (ajustes básicos sin optimización técnica) |
| UPD7 | Propuesta técnica incluida (desarrollo deficiente) | PM (contenido incorrecto sin valor) |
| UPD8 | Propuesta técnica incluida (desarrollo suficiente) | VA (uso API y automatización básica) |
| UPD9 | No incluida | No |
| UPD10 | Propuesta técnica incluida (desarrollo deficiente) | PM (gestión básica sin integración) |
| UPD11 | Propuesta técnica incluida (desarrollo deficiente) | PM (incidencias sin evolución funcional) |
| UPD12 | Propuesta técnica incluida (desarrollo deficiente) | PM (HA conceptual sin implementación) |
| UPD13 | Propuesta técnica incluida (desarrollo deficiente) | PM (sin uso herramientas exigidas) |
| UPD14 | Propuesta técnica incluida (desarrollo deficiente) | PM (contenedores sin tecnología definida) |
| UPD15 | Propuesta técnica incluida (desarrollo deficiente) | PM (decomisionado incompleto) |

### Proyecto CLO – Cloud

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| CLO1 | No incluida | No |
| CLO2 | Propuesta técnica incluida (desarrollo deficiente) | PM (ajustes progresivos sin escalabilidad) |
| CLO3 | Propuesta técnica incluida (desarrollo deficiente) | PM (uso concurrente sin arquitectura) |

### Proyecto OTR – Otros desarrollos

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| OTR1 | Propuesta técnica incluida (desarrollo deficiente) | PM (SSO genérico sin federación técnica) |
| OTR2 | Propuesta técnica incluida (desarrollo deficiente) | PM (2FA genérico con inconsistencias) |
| OTR3 | Propuesta técnica incluida (desarrollo deficiente) | PM (scripts sin orquestación) |
| OTR4 | Propuesta técnica incluida (desarrollo deficiente) | PM (analítica genérica sin stack definido) |
| OTR5 | Propuesta técnica incluida (desarrollo deficiente) | PM (workflow sin herramienta identificada) |
| OTR6 | Propuesta técnica incluida (desarrollo deficiente) | PM (portal sin evolución funcional) |
| OTR7 | Propuesta técnica incluida (desarrollo deficiente) | PM (IA conceptual sin implementación) |

### Proyecto COR – Correo electrónico

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| COR1 | Propuesta técnica incluida (desarrollo deficiente) | PM (supervisión sin control de tráfico) |
| COR2 | Propuesta técnica incluida (desarrollo deficiente) | PM (gestión manual sin automatización) |
| COR3 | Propuesta técnica incluida (desarrollo deficiente) | PM (revisión sin política de cuotas) |
| COR4 | Propuesta técnica incluida (desarrollo deficiente) | PM (control básico sin estrategia antispam) |
| COR5 | Propuesta técnica incluida (desarrollo deficiente) | PM (gestión manual de buzones) |
| COR6 | Propuesta técnica incluida (desarrollo deficiente) | PM (seguridad genérica sin técnicas) |
| COR7 | Propuesta técnica incluida (desarrollo deficiente) | PM (infraestructura sin modularidad) |
| COR8 | Propuesta técnica incluida (desarrollo deficiente) | PM (sin criterios de escalado) |
| COR9 | Propuesta técnica incluida (desarrollo deficiente) | PM (inyección sin arquitectura definida) |
| COR10 | Propuesta técnica incluida (desarrollo deficiente) | PM (soporte básico sin optimización) |

### Proyecto MAX – Sistema operativo

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| MAX1 | No incluida | No |
| MAX2 | No incluida | No |
| MAX3 | No incluida | No |
| MAX4 | No incluida | No |
| MAX5 | No incluida | No |
| MAX6 | No incluida | No |
| MAX7 | No incluida | No |
| MAX8 | No incluida | No |
| MAX9 | No incluida | No |
| MAX10 | No incluida | No |
| MAX11 | No incluida | No |
| MAX12 | No incluida | No |
| MAX13 | No incluida | No |
| MAX14 | No incluida | No |

### Proyecto AV – Aulas Virtuales

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| AV1 | Propuesta técnica incluida (desarrollo deficiente) | PM (revisión sin herramientas) |
| AV2 | Propuesta técnica incluida (desarrollo deficiente) | PM (supervisión sin balanceo) |
| AV3 | Propuesta técnica incluida (desarrollo deficiente) | PM (despliegue sin automatización) |
| AV4 | Propuesta técnica incluida (desarrollo deficiente) | PM (redistribución sin criterios) |

### Proyecto POR – LDAP y Portal

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| POR1 | Propuesta técnica incluida (desarrollo deficiente) | PM (ampliación sin replicación técnica) |
| POR2 | Propuesta técnica incluida (desarrollo deficiente) | PM (migración sin procedimientos) |

### Proyecto SEG – Seguridad

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| SEG1 | Propuesta técnica incluida (desarrollo deficiente) | PM (control básico sin auditoría) |
| SEG2 | Propuesta técnica incluida (desarrollo deficiente) | PM (segregación sin arquitectura) |
| SEG3 | Propuesta técnica incluida (desarrollo deficiente) | PM (gestión sin ciclo de vida) |
| SEG4 | Propuesta técnica incluida (desarrollo deficiente) | PM (gestión DNS sin automatización) |
| SEG5 | Propuesta técnica incluida (desarrollo deficiente) | PM (vulnerabilidades sin herramientas) |
| SEG6 | Propuesta técnica incluida (desarrollo deficiente) | PM (logs sin correlación SIEM) |
| SEG7 | Propuesta técnica incluida (desarrollo deficiente) | PM (auditorías sin metodología) |
| SEG8 | Propuesta técnica incluida (desarrollo deficiente) | PM (control continuo sin métricas) |
| SEG9 | Propuesta técnica incluida (desarrollo deficiente) | PM (logs sin explotación técnica) |
| SEG10 | Propuesta técnica incluida (desarrollo deficiente) | PM (claves sin gestión avanzada) |
| SEG11 | Propuesta técnica incluida (desarrollo deficiente) | PM (soporte sin procedimientos) |

### Proyecto CON – Contenedores

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| CON1 | Propuesta técnica incluida (desarrollo deficiente) | PM (scripts sin orquestación) |
| CON2 | Propuesta técnica incluida (desarrollo deficiente) | PM (automatización sin herramientas) |
| CON3 | Propuesta técnica incluida (desarrollo deficiente) | PM (sistema auxiliar sin definición) |

### Proyecto MIG – Migraciones

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| MIG1 | Propuesta técnica incluida (desarrollo deficiente) | PM (coordinación sin metodología) |
| MIG2 | Propuesta técnica incluida (desarrollo deficiente) | PM (planificación sin fases definidas) |
| MIG3 | Propuesta técnica incluida (desarrollo deficiente) | PM (preparación sin automatización) |
| MIG4 | Propuesta técnica incluida (desarrollo deficiente) | PM (verificación sin criterios claros) |
| MIG5 | Propuesta técnica incluida (desarrollo deficiente) | PM (soporte sin indicadores) |

### Proyecto IA – Inteligencia Artificial

| **Proyecto** | **Clasificación** | **Propuesta de Mejora o Valor añadido** |
| --- | --- | --- |
| IA1 | No incluida | No |
| IA2 | No incluida | No |
| IA3 | No incluida | No |
| IA4 | No incluida | No |
| IA5 | No incluida | No |

## CONCLUSIÓN DEL ANEXO

El análisis evidencia que la propuesta de empresa_n presenta un grado de desarrollo técnico limitado y predominantemente descriptivo, caracterizado por la ausencia de metodologías, herramientas y arquitecturas definidas.

En particular:

- La mayoría de los subproyectos incluyen **propuestas de mejora de carácter incremental**, que no suponen una evolución real de la solución, al limitarse a reforzar tareas existentes.

- Existen bloques completos sin desarrollo técnico evaluable (**MAX e IA**).

- La presencia de valor añadido real es **residual y aislada**.

Desde una perspectiva cuantitativa:

- Alto predominio de **PM (mejoras sin valor)**

- Presencia relevante de **NO (ausencia de propuesta)**

- **Valor añadido (VA): marginal**

## SÍNTESIS FINAL

La propuesta de empresa_n presenta un nivel de desarrollo técnico bajo y heterogéneo en la práctica totalidad de los proyectos, con especial debilidad en los bloques **MAX, IA, CON y CLO**.

De forma sintética:

- **Predominio de propuestas de mejora sin valor añadido (PM)**

- **Presencia significativa de subproyectos sin propuesta (NO)**

- **Valor añadido residual y no estructural (VA)**

El nivel global puede calificarse como **desarrollo técnico bajo, descriptivo y con escasa capacidad de acreditación operativa**.

**Este anexo refuerza de forma objetiva la valoración técnica obtenida por la oferta, al evidenciar la ausencia de una traducción efectiva del Anexo II en soluciones técnicas concretas, verificables y operativas.**
