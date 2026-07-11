# DESCRIPCIÓN DEL ENTORNO TÉCNICO Y FUNCIONAL EXISTENTE

## Descripción de los sistemas de información existentes

La Plataforma Educativa EducaMadrid (en adelante EducaMadrid) está compuesta por un ecosistema de aplicaciones desarrolladas en distintas tecnologías, con diferentes paradigmas y lenguajes usados por la Comunidad Educativa no universitaria, sostenida con fondos públicos de la Comunidad de Madrid.

La Consejería de Digitalización considera la utilización de las Tecnologías de la Información y la Comunicación como un recurso actualmente imprescindible en los procesos de enseñanza y aprendizaje.

Con esta finalidad proporciona un conjunto de servicios y herramientas a la comunidad educativa a través del portal EducaMadrid: [https://www.educa2.madrid.org/](<https://www.educa2.madrid.org/>). Estos servicios y herramientas ofrecen los medios necesarios para facilitar el proceso enseñanza-aprendizaje y de comunicación entre los distintos actores que intervienen en el mismo. Por este motivo es necesario dar soporte a sus usuarios y desarrollar, actualizar, evolucionar y mantener los servicios y aplicaciones educativas, herramientas de comunicación entre ellas y sus interfaces, que mantendrán un aspecto y forma de uso comunes para facilitar su uso y para que el usuario identifique todas ellas como componentes de la misma plataforma.

La arquitectura tecnológica de EducaMadrid está constituida por más de 25 aplicaciones que ofrecen servicios a la Comunidad Educativa a través de un acceso en Cloud (Nube Privada Educativa). Estas aplicaciones deben interactuar entre sí. Algunas de ellas están basadas en adaptaciones de software existente (en su mayoría OpenSource) y otras se han desarrollado completamente para dar servicios concretos desde EducaMadrid. La mayoría de estas aplicaciones y servicios están en producción y necesitan un mantenimiento; otras están en fase de desarrollo y otras se solicitan en este pliego para comenzar su desarrollo.

Las más relevantes dentro de este contrato son:

- Web principal y Portal Educativo (Liferay + Desarrollo Propio)

- Aulas Virtuales (Moodle)

- Mediateca (Desarrollo Propio)

- Retransmisión en vivo por Internet (Wowza)

- Páginas web de centro (Wordpress)

- Otras páginas web (Wordpress Multisite)

- Servicio de correo electrónico (RoundCube + Adaptaciones Propias)

- Cloud + Edición colaborativa (NextCloud, Collabora)

- Comparti2 (Jirafeau)

- eXeLearning On-line (Adaptación Propia)

- EMPieza (Desarrollo Propio)

- Avisos centralizados (Desarrollo Propio)

- Formularios (LimeSurvey)

- Videoconferencias (Jitsi y BigBlueButton)

- Servicios de Inteligencia Artificial

- Aplicación de Centros EMLab

- Recursos educativos (Desarrollo Propio)

- Desarrollos Propios WEB

- Aplicaciones de gestión y otras

- Etc.

### Web principal y Portal Educativo

Estas dos páginas web son las entradas principales a los servicios de la plataforma por lo que necesitan estar totalmente aseguradas y actualizadas y mantener una interfaz de acceso homogénea y común al resto de los aplicativos de la plataforma.

Además, este servicio también ofrece un espacio para los docentes en donde albergar sus páginas web personales, blogs, etc.

### Aulas Virtuales

La plataforma Aula Virtual de EducaMadrid está basada en el Software Libre MOODLE, proporcionando los siguientes servicios:

- Aula Virtual de Centros. Los profesores pueden crear y gestionar de forma autónoma, íntegra e intuitiva cursos “on-line”. Actualmente los Centros Educativos ofertan más de 295.000 cursos a sus alumnos en esta plataforma.

- Formación Profesional a Distancia. Más de 6.200 alumnos al año de Ciclos Formativos de Grado Superior realizan cada curso escolar sus estudios en la modalidad de distancia con esta plataforma de EducaMadrid.

- Formación en línea del profesorado. Anualmente, más de 7.600 profesores al año realizan su formación permanente a través de esta Aula Virtual.

- Evaluación de alumnos de Institutos de Innovación Tecnológica. Una plataforma específica es utilizada para realizar actividades evaluativas curriculares simultáneas a los alumnos de estos institutos.

<!-- salto de página -->

### Mediateca

Este servicio de desarrollo propio ofrece un servicio de repositorio multimedia junto con algunas aplicaciones específicas (Construcción de vídeos interactivos, Creación de Mapas Mentales, etc.…).

A través de la Mediateca, cada centro educativo y profesor de la Comunidad de Madrid tiene un espacio para subir, gestionar y compartir sus imágenes, trabajar en sus vídeos educativos, subir sus audios y dar la visibilidad deseada a sus producciones en gran variedad de formatos digitales, siempre dentro de un contexto en el que priman las medidas de seguridad de acceso y reproducción de las mismas.

A través de la integración de la gestión de grupos de EMPieza, también se puede dar acceso a los alumnos para que suban sus propios contenidos a un espacio común gestionado y controlado por el docente.

### Retransmisión “en vivo” por Internet

Este servicio, basado tanto en Software Libre (Red5) como en software propietario (WOWZA), permite que los centros educativos dispongan de su propio canal de retransmisión en vivo (streaming).

### Wordpress

Este servicio, basado en el conocido Software Libre WordPress, ofrece a los centros la posibilidad de crear sus espacios web.

EducaMadrid ofrece este servicio además de para los centros, para otros cometidos, para lo que cuenta con un despliegue de este gestor de contenidos en modalidad Multisite.

### Correo web

A través de una arquitectura específica y basado en varias piezas de Software Libre (RoundCube y QMail), EducaMadrid pone a disposición de todos los centros educativos, así como de todos los usuarios registrados en el Portal EducaMadrid (profesores, alumnos, PAS, etc.) cuentas de correo educativas para su utilización como una herramienta más dentro de la comunidad educativa. Casi 2.000.000 de usuarios disponen de cuentas de acceso a este servicio, en el que se cuida especialmente la utilización de filtros para evitar la recepción de spam, publicidad o virus en los buzones de los usuarios.

Actualmente, la solución de correo cuenta con una solución de AntiSpam dependiente del departamento de Ciberseguridad que ofrece una protección adicional garantizando la limpieza tanto del correo entrante como del saliente.

En el curso 23/24 se gestionaron en la plataforma de correo electrónico más de 400 millones de mensajes.

La disponibilidad por parte de los usuarios de la comunidad educativa de sus cuentas de correo de EducaMadrid facilita también disponer de canales informativos ágiles:

- Canal de información institucional desde las diferentes unidades administrativas (Direcciones Generales, Direcciones de Área Territoriales, Consejo Escolar, Inspección, etc.) hacia Centros y docentes, así como otras comunicaciones incluso con los alumnos.

- Canal de información de recursos educativos de EducaMadrid.

- Canal de información de eventos, convocatorias y noticias de interés pedagógico de la Revista Digital.

### Cloud + edición colaborativa

Este servicio, basado en Software Libre (NextCloud, Collabora), proporciona 5GiB de espacio en la nube a todos los profesores y cuentas institucionales que puede ser ampliado a 10GiB si está justificado. También existe la posibilidad de incorporar alumnos al servicio. Además, es posible trabajar en documentos de forma colaborativa.

### Comparti2

Este servicio, gestionado de forma centralizada desde EMPieza, permite compartir grandes archivos de forma temporal para permitir su descarga a miembros de la comunidad educativa.

También se permite que un docente habilite el acceso a esta herramienta a ciertos alumnos para que pueda ser usada por los alumnos que lo necesiten, siempre bajo la supervisión de un profesor o docente.

### eXeLearning on-line

Esta Adaptación Propia del Software Libre eXeLearning, proporciona un entorno para crear recursos educativos abiertos (REAs) integrado con las propias Aulas Virtuales, pudiendo crear, editar y publicar los trabajos en una misma ubicación.

### EMPieza

Este servicio, de desarrollo propio proporciona a los profesores la capacidad de organizar y automatizar tareas repetitivas en otras aplicaciones de EducaMadrid con sus alumnos.

### Avisos centralizados

Este servicio, de desarrollo propio proporciona la capacidad de dar avisos importantes sobre los servicios de EducaMadrid a sus usuarios.

<!-- salto de página -->

### Formularios

Este servicio, basado en código de fuentes abiertas (LimeSurvey), proporciona la capacidad de poder crear formularios para la recogida de datos por parte de la comunidad educativa.

### Videoconferencias

Este servicio, basado en códigos de fuentes abiertas (Jitsi y BigBlueButton) proporciona a los docentes la posibilidad de retransmitir a través de Internet las clases a sus alumnos cuando estos no pueden acudir a sus centros educativos y a los equipos docentes a llevar a cabo reuniones telemáticas.

### Servicios de Inteligencia Artificial

Este servicio, basado en software libre y modelos de lenguaje de gran tamaño (LLM), proporciona un entorno para integrar con los diferentes servicios de la plataforma como son las Aulas Virtuales, el correo web y el Cloud, para dar la capacidad de generar mediante Inteligencia artificial, diferentes actividades y resúmenes de datos por parte de la comunidad educativa.

Actualmente, EducaMadrid se encuentra inmersa en un proceso de integración de la Inteligencia Artificial en otros servicios. Para garantizar la calidad, seguridad y privacidad de los servicios ofrecidos, los modelos usados siempre son locales y basados en software OpenSource. De esta forma todo el tratamiento de la información está alojado en los sistemas de EducaMadrid, sin compartir ningún tipo de información con terceros.

### Aplicación de Centros EMLab

Este servicio pretende valorar y promocionar el uso de los servicios de EducaMadrid, ofreciendo a los centros la posibilidad de certificar su uso y obteniendo por ello ventajas en el uso de los servicios de la plataforma.

### Entornos para proporcionar recursos y herramientas educativas

La Plataforma Tecnológica EducaMadrid proporciona también a los profesores y alumnos varios entornos con recursos y herramientas online:

- Animalandia: Arquitectura con recursos (imágenes y sonidos) sobre la biodiversidad animal que pueden ser libremente utilizados.

- Wiris: Herramienta para la ejercitación de conceptos matemáticos.

- Albor: Sistema experto como asistente en la toma de decisiones sobre adaptaciones de acceso al ordenador en alumnos con necesidades educativas especiales.

- EducaSAAC: Repositorio virtual interactivo de contenidos visuales orientados a centros educativos de Educación Especial, Infantil y Primaria.

### Aplicaciones de gestión y otras tareas

La Plataforma EducaMadrid proporciona otros servicios online relacionados con la gestión de ciertos procesos en las Direcciones Generales, DATs, CTIFs, etc., como, por ejemplo:

- Seguimiento: Aplicación para la gestión y seguimiento de las dotaciones de equipamientos informáticos a los centros.

- Dotaciones TIC: Aplicación para la gestión de las incidencias de los equipos informáticos de los centros.

Por otro lado, la plataforma cuenta con un conjunto de aplicaciones internas que permiten gestionar los datos de la misma, entre las que destacan Mamood, Redmine, Mattermost, GitLab, el SSO (gestión de login) basado en KeyCloack, etc.

## Descripción del entorno tecnológico

La arquitectura hardware de la Plataforma Tecnológica Educativa EducaMadrid está constituida por unos 700 servidores físicos y virtuales, con un crecimiento estimado en torno al 15% anual. Además, tenemos 6 grupos de almacenamiento consolidado, distribuidos en una capa de Frontend y otra de Backend. Los servicios se encuentran clusterizados y se distribuyen del siguiente modo, aunque pueden ampliarse:

- Virtualización Principal HP Synergy – RHEV: 20 nodos, 19 de ellos repartidos en 2 frames y un nodo adicional separado para IA.

- Virtualización Secundaria HP Synergy – RHEV: 5 nodos en 1 frame.

- Virtualización Secundaria HP C7000 - RHEV 5 nodos en 1 frame.

- Cabinas de almacenamiento HP, Netapp, EMC Unity y 3 Infinidat.

- 3.500 BBDD aproximadamente (PostgreSQL, MySQL, MariaDB y MongoDB)

- Servidores virtualizados 650 aprox. (RedHat, OpenSuse, Ubuntu, Debian y Windows Server)

Existen varias instancias de cada uno de los servicios en distintos entornos, contando con entornos de desarrollo, testeo, preproducción y producción.

*<!-- salto de página -->*

# DEFINICIÓN Y ALCANCE DE LOS TRABAJOS

Debido a su naturaleza, las tareas relativas al mantenimiento evolutivo y adaptativo de los sistemas y aplicaciones suponen una gran carga de trabajo.

## Descripción del servicio de mantenimiento y actualización para aseguramiento de la continuidad del servicio de los sistemas en entornos productivos

Las tareas de mantenimiento evolutivo o adaptativo orientadas al aseguramiento de la continuidad del servicio de los sistemas en entornos productivos cubrirán el conjunto de los sistemas de información y el entorno tecnológico descritos en el Anexo I.

El servicio consiste en la corrección del código fuente o de la documentación para evolucionar o adaptar las incidencias que afecten a los citados sistemas de información, así como todas las tareas conexas necesarias para poder realizar dicha corrección, por ejemplo, actualización de las versiones, parcheados de seguridad, adaptaciones preventivas, aclaraciones y ayudas a terceras empresas, etc.…

Concretamente el contrato estará centrado en las tareas que se refieren tanto a los Proyectos de Sistemas actualmente alojados en la Plataforma Educativa EducaMadrid como a los que pudieran surgir, de naturaleza similar, a lo largo de la vigencia del contrato.

En el mantenimiento de los servicios ofrecidos se deben incluir los mantenimientos evolutivos, así como otras tareas de adaptación y actualización de dichos servicios. Estas tareas pueden agruparse en las siguientes áreas:

## Mantenimiento y mejora de entornos de Bases de Datos (BD)

## Mantenimiento y mejora de entornos de Bases de Datos MariaDB y Proxy SQL avanzado

Algunos servicios, necesitan entornos de base de datos MariaDB Cluster, así como en configuración de Proxy Avanzado (BD1).

Para ello se solicita:

- Optimizar, mantener y, en definitiva, adecuar los diferentes nodos de bases de datos del clúster MySQL / MariaDB, y también realizar las tareas de optimización y el mantenimiento del proxy SQL avanzado tanto en los entornos de preproducción como en producción.

- Optimizar los procesos de Monitorización y Mantenimiento del clúster de Base de Datos mediante una herramienta específica, así como el mantenimiento de la misma.

## Mantenimiento y optimización proactiva de las bases de datos de toda la plataforma

Actualmente la plataforma de EducaMadrid utiliza en torno a 3.500 bases de datos entre el portal, las aulas virtuales, la aplicación de cloud y el resto de los servicios. Se necesita la realización de las tareas oportunas para el mantenimiento, mejora y optimización proactiva de las bases de datos de EducaMadrid (BD2).

Se solicita:

- Optimizar de forma continua las diferentes bases de datos, haciendo labores de mantenimiento, mejora y optimización orientadas a mejorar las consultas y de backup para asegurar la información.

- Asegurar una correcta seguridad en las conexiones a las BBDD.

- Realizar tareas de mantenimiento preventivo y proactivo en fechas de una menor carga, planificando dichas tareas con antelación.

Se deben de aprovechar los períodos no lectivos vacaciones de verano, semana santa y/o Navidad. Estas tareas se realizarán periódicamente dos veces al año.

## Mantenimiento de las diferentes Bases de Datos de gestión de la configuración de EducaMadrid

La plataforma de EducaMadrid dispone de Bases de Datos relacionadas con la gestión de la configuración (CMDBuild, …), las cuales necesitan de la realización de las tareas oportunas para el mantenimiento, mejora y optimización proactiva (BD3).

Se solicita:

- Adecuar la Base de Datos para incorporar y comprender todos los elementos actuales a nivel físico y lógico (BBDD, firewalls, hosts, DNS, redes, tamaño de almacenamiento, backups, balanceadores, contenedores), así como las diferentes aplicaciones y las relaciones entre todos estos elementos. Así como tener una relación de los diferentes contenedores y los hosts de los mismos.

- Alimentar de la propia Base de Datos de los datos extraídos de los entornos preferiblemente de manera automatizada o manual en caso de ser necesario.

- Para ello se usarán las herramientas De Software Libre necesarias.

Estas tareas se realizarán periódicamente.

## Mantenimiento de las bases de datos de las Aulas Virtuales

Actualmente EducaMadrid tiene más de 2500 bases de datos de PostgreSQL distribuidas en 20 servidores tanto físicos clusterizados como virtuales (BD4).

Se solicita:

- Realizar un análisis del uso y carga soportada por dichos servidores, con herramientas propias de la BBDD.

- Adaptar la arquitectura actual, actualizando, ampliando, configurando o eliminando servidores de bases de datos PostgreSQL acorde a los datos obtenidos.

- Redistribuir las bases de datos entre todos los servidores, en base a la carga, uso y tamaño.

- Modificar la planificación de los backups de las bases de datos involucradas.

Estas tareas se realizarán periódicamente, en períodos no lectivos.

## Mantenimiento de disparadores y Foreign Data Wrappers en los entornos “Portal” y “LDAP Plano”

Tareas adicionales necesarias en la optimización, actualización y mantenimiento de las Bases de Datos del Portal y el LDAP Plano (BD5).

Se solicita:

- Realizar un análisis pormenorizado de los datos actuales de raíces, así como los diferentes campos, fechas de cambios y modificaciones.

- Adecuar y mantener las diferentes funciones y disparadores en las BBDD, así como la creación de los campos, índices y Foreign Data Wrappers necesarios.

- Adecuar y mantener los scripts necesarios para que de manera recurrente todos los datos de raíces estén sincronizados con la BBDD del Portal y estos a su vez con el LDAP plano.

Estas tareas se realizarán periódicamente, en períodos no lectivos.

## Implementación y Mantenimiento de las Bases de Datos necesarias en entornos de Microservicios

Actualmente EducaMadrid está adaptando algunos de sus aplicativos y servicios a la arquitectura de contenedores y microservicios (BD6).

Se solicita:

- Adecuar las Bases de Datos a una versión actualizada en el entorno correspondiente.

- Realizar las adaptaciones necesarias de BBDD Virtuales a BBDD DevOps de cada nueva versión para asegurar un rendimiento óptimo.

- Realizar mantenimiento correctivo de cada nueva versión instalada.

Estas tareas se realizarán periódicamente, en períodos no lectivos.

<!-- salto de página -->

## Monitorización, testeo y pruebas de rendimiento (MON)

## Mantenimiento periódico del almacenamiento de los centros

EducaMadrid cuenta con un gran número de aplicativos que utilizan NFS para su funcionamiento. De ellos algunos NFS tienen un tamaño que dificulta su control (MON1).

Se solicita:

- Realizar de forma periódica una redistribución de los espacios ocupados por los centros por los distintos NFS atendiendo a la ocupación de estos.

- Para las tareas más pesadas o que requieran de parada del servicio, se deben aprovechar los períodos no lectivos de vacaciones de verano, semana santa y/o Navidad.

Estas tareas se realizarán periódicamente.

## Realización periódica de pruebas de estrés en diferentes entornos de la plataforma

Es necesario determinar de forma continua el comportamiento de las diferentes aplicaciones y entornos funcionales (MON2).

Para ello se solicita:

- Medir el rendimiento de las diferentes aplicaciones y entornos funcionales y analizar todos los datos generados evaluando el desempeño general de la aplicación.

- En caso de encontrar anomalías se debe comenzar un trabajo de investigación para detectar los problemas del sistema y así poder buscar las posibles soluciones.

Estas tareas se realizarán periódicamente.

## Mantener actualizado el sistema de monitorización y estadísticas de uso

EducaMadrid cuenta con multitud de servicios, que necesitan conocer su nivel de uso tanto por el rendimiento como por las mismas estadísticas de uso (MON3).

Para ello se solicita:

- Incorporar de forma continua al sistema de monitorización y estadísticas de todos los servidores y servicios incluidos los de nueva creación o migrados.

- Usar herramientas de código abierto para dicho objetivo.

- Realizar una actualización de la herramienta actual a su última versión.

- Asegurar el correcto funcionamiento de la monitorización adecuando las alertas reactivas a las necesidades de EducaMadrid y adaptando las alertas proactivas a las nuevas necesidades de los servicios.

Estas tareas se realizarán de forma continuada y sincronizada con las modificaciones de servicios.

## Mantener actualizado el sistema de monitorización y estadísticas de servicios basados en IA

EducaMadrid dispone de servicios basados en modelos de lenguaje de gran tamaño (LLM) desplegados sobre infraestructura propia y OpenSource, cuyo uso debe ser monitorizado tanto desde el punto de vista del rendimiento como desde la perspectiva de estadísticas de consumo y calidad del servicio (MON4).

Para ello se solicita:

- Incorporar de forma continua al sistema de monitorización y estadísticas todos los servicios basados en LLM, incluyendo nuevos modelos, endpoints de inferencia.

- Utilizar las herramientas necesarias de código abierto para dicho objetivo.

- Asegurar el correcto funcionamiento del sistema de monitorización, adecuando las alertas reactivas a incidencias en los servicios LLM y definiendo alertas proactivas orientadas a nuevas necesidades.

Estas tareas se realizarán de forma continuada y coordinada con las modificaciones, ampliaciones o migraciones de los servicios basados en modelos de lenguaje.

## Actualización de servicios existentes (UPD)

## Mantenimiento y mejora de los sistemas de videoconferencias de EducaMadrid

EducaMadrid cuenta con una solución De Software Libre para videoconferencias: **Jitsi**. Se necesitan tener esta herramienta actualizada en los tres sistemas, con una periodicidad mínima trimestral manteniendo la compatibilidad con las últimas versiones de los navegadores principales (UPD1).

Se solicita:

- Mantener una versión actualizada abordando sus correspondientes migraciones.

- Realizar las adaptaciones necesarias de cada nueva versión para asegurar un rendimiento óptimo.

- Realizar mantenimiento correctivo de cada nueva versión instalada.

Estas tareas se realizarán periódicamente cuatro veces al año.

<!-- salto de página -->

## Mantenimiento y mejora del sistema secundario de Videoconferencias con opción de grabación

EducaMadrid cuenta con un servicio secundario de videoconferencias basado en la solución de Software Libre BigBlueButton para videoconferencias con opción de grabación (UPD2).

Se solicita:

- Adaptar, mantener y actualizar el entorno a la versión más actualizada con su correspondiente migración.

- Realizar las adaptaciones necesarias de cada nueva versión para asegurar la funcionalidad de grabación y un rendimiento óptimo de la aplicación.

- Realizar mantenimiento correctivo de cada nueva versión instalada.

Estas tareas se realizarán periódicamente cuatro veces al año.

## Mantenimiento y mejora de la herramienta Mattermost

EducaMadrid tiene integrada como plataforma interna de comunicación y colaboración la herramienta Mattermost. Se necesita tener esta herramienta actualizada y funcionando en condiciones óptimas (UPD3).

Se solicita:

- Mantener una versión actualizada con su correspondiente migración.

- Realizar las adaptaciones necesarias de cada nueva versión para asegurar un rendimiento óptimo.

- Realizar mantenimiento correctivo de cada nueva versión instalada.

Esta tarea se realizará periódicamente.

## Mantenimiento y mejora de la solución Kanban

EducaMadrid dispone de una solución de gestión de tareas/proyectos con integración de Kanban. Se necesita tener esta herramienta actualizada y funcionando en condiciones óptimas (UPD4).

Se solicita:

- Mantener una versión actualizada con su correspondiente migración.

- Realizar mantenimiento correctivo de cada nueva versión instalada.

Esta tarea se realizará periódicamente.

## Mantenimiento y mejora de la solución GitLab

Actualmente, EducaMadrid utiliza GitLab como herramienta de control de versiones de código abierto para la gestión de proyectos y colaboración en el desarrollo de software. Se necesita tener esta herramienta actualizada y funcionando en condiciones óptimas (UPD5).

Se solicita:

- Mantener GitLab actualizado a la última versión estable, incluyendo migraciones necesarias entre versiones.

- Realizar mantenimiento correctivo y preventivo de la herramienta, incluyendo parches de seguridad y ajustes de configuración

Esta tarea se realizará periódicamente, al menos dos veces al año.

## Mantenimiento y mejora de la solución LimeSurvey

EducaMadrid dispone de una solución de formularios mediante la herramienta de Software Libre LimeSurvey. Se necesita mantener esta herramienta actualizada, con rendimiento adecuado y con usabilidad adecuada (UPD6).

Se solicita:

- Mantener una versión actualizada con su correspondiente migración si fuera necesaria.

- Mejorar el diseño de las nuevas arquitecturas para el correcto rendimiento de la aplicación.

- Realizar las adaptaciones necesarias de aspecto y usabilidad en la nueva versión actualizada.

- Asegurar el rendimiento haciendo los ajustes necesarios para que la experiencia de usuario sea la esperada por EducaMadrid.

Esta tarea se realizará periódicamente.

## Mantenimiento y mejora de SonarQube

Actualmente EducaMadrid utiliza la herramienta de Software Libre SonarQube para la gestión de la calidad del código (UPD7).

Se solicita:

- Actualizar la herramienta a la última versión estable.

- Realizar todas las tareas necesarias de gestión de usuarios y proyectos, así como las modificaciones necesarias en los proyectos existentes para su integración en SonarQube.

- Implementar las reglas y perfiles de calidad marcados por la Consejería.

Estas tareas se realizarán periódicamente dos veces al año.

<!-- salto de página -->

## Mantenimiento y mejora de Redmine

El equipo de EducaMadrid usa Redmine como herramienta de Software Libre para la gestión de las incidencias y para las solicitudes y seguimiento de las tareas de los técnicos. También se usa esta herramienta para gestionar las incidencias comunicadas por usuarios y centros educativos a través del CAU (UPD8).

Se pide como parte del mantenimiento de Redmine:

- Actualizar la versión de Redmine a la versión estable más reciente, y mantenerlo actualizado según se vayan publicando nuevas versiones.

- Implementación de los scripts necesarios para realizar automatización de carga y actualización de tareas mediante plugins o scripting (vía REST API).

- Implementación mediante plugins o scripts de un sistema de autentificación 2FA.

Estas tareas se realizarán periódicamente.

## Mantenimiento y configuración de Wowza Streaming Engine.

EducaMadrid usa la herramienta Wowza Streaming Engine para retransmisiones en vivo (UPD9).

Se solicita:

- Mantener actualizados los servidores y servicios involucrados en la arquitectura de Wowza Streaming Engine.

- Configurar el entorno para su funcionamiento óptimo.

- Parametrizar los diferentes codificadores RTMP o RTSP/RTP y la salida HLS si fuera necesario, así como cualquier elemento necesario para su adecuación con el resto de los entornos de la plataforma.

## Mantenimiento y gestión de contenidos AbiesWeb

EducaMadrid proporciona soporte a AbiesWeb, la aplicación de bibliotecas escolares (UPD10).

Mientras esta aplicación se siga usando, se solicita:

- Realizar las actualizaciones y parcheado necesarios y gestiones de contenidos del sistema de bibliotecas escolares AbiesWeb.

- Mantener y aplicar las actualizaciones evolutivas y parches que son suministradas por el Ministerio de Educación y Formación Profesional.

- Asistir a las incidencias producidas en el aplicativo y gestionado de la carga de volúmenes de las nuevas bibliotecas mientras sea requerido.

<!-- salto de página -->

## Actualización, Mantenimiento y gestión de contenidos de Abies+

EducaMadrid proporciona soporte a Abies+, la nueva aplicación de bibliotecas escolares que sustituirá en breve a AbiesWeb (UPD11).

Se solicita:

- Realizar las pruebas, mejoras y actualizaciones y parcheados necesarios en la aplicación y los servidores que la soportan.

- Realizar la gestión de contenidos del sistema de las bibliotecas escolares Abies+.

- Mantener y aplicar las actualizaciones evolutivas y parches que son suministrados por el Ministerio de Educación y Formación Profesional.

- Asistir a las incidencias producidas en el aplicativo y en los procesos de carga de volúmenes de las nuevas bibliotecas.

## Implementación, mantenimiento y mejora de Empieza

Se necesita realizar el mantenimiento, las actualizaciones y mejoras del sistema Empieza (servicio de desarrollo propio que proporciona a los profesores la capacidad de organizar y automatizar tareas) incluyendo la configuración para su escalado con alta disponibilidad tanto en la parte Frontend como Backend (UPD12).

Se solicita:

- Mantener, actualizar y mejorar los servidores y aplicaciones que soportan Empieza, asegurando su correcto funcionamiento.

- Configurar y parametrizar la herramienta para permitir escalado horizontal y vertical, garantizando alta disponibilidad y redundancia de los servicios.

- Adaptar la arquitectura de frontend y backend para soportar la distribución de carga, balanceo de peticiones y tolerancia a fallos.

- Supervisar las pruebas de rendimiento y optimización de los componentes para asegurar la estabilidad del sistema ante incrementos de usuarios o cargas de trabajo.

## mantenimiento y mejora del sistema de gestión de la configuración

Actualmente EducaMadrid dispone un sistema de gestión de la configuración IT basada en diferentes aplicaciones de Software Libre: CMDBuild, Ansible, etc. Se necesita la gestión, mantenimiento, actualización y adaptación de los sistemas y aplicaciones que prestan este servicio de gestión de la configuración IT (UPD13).

Para ello se solicita:

- Mantener, actualizar y mejorar tanto el servidor como las aplicaciones necesarias para la gestión de las configuraciones IT.

- Configurar y parametrizar todo el servicio para su correcto funcionamiento.

- Automatizar el entorno para la ingesta de los datos tanto de entrada como de salida. Correlar los datos para asegurar su coherencia y homogeneidad, así como su adecuación e interoperabilidad con el resto de los entornos.

## Mantenimiento, Actualización y mejora de la solución de contenedores

EducaMadrid se encuentra inmerso en un proceso de transición de algunas de sus aplicaciones y servicios a entornos contenerizados y de microservicos. Se necesita tanto la gestión, mantenimiento, actualización y mejora de las aplicaciones de infraestructura que dan soporte a estas tecnologías (Docker, Kubernetes, Podman, …), como la adaptación de las aplicaciones para funcionar en una infraestructura contenerizada. También se necesita mantener, adaptar y mejorar los sistemas de automatización de tareas que facilitan tanto los despliegues como el redimensionamiento de los servicios ofrecidos desde esta plataforma. (UPD14)

Para ello se solicita:

- Gestionar, mantener, mejorar y adaptar los servidores, aplicaciones y servicios necesario para la adecuación del entorno y su usabilidad a las características de los aplicativos y servicios de EducaMadrid.

- Configurar y parametrizar tanto los servidores como las aplicaciones y servicios para su correcto funcionamiento.

- Desarrollar scripts y estrategias de automatización de tareas que permitan aumentar la productividad minimizando los riesgos y el tiempo de despliegue tanto de las aplicaciones existentes como de las futuras que se vayan incorporando al ecosistema de contenedores de EducaMadrid.

## Mantenimiento de gestión y decomisionado de servidores

Se necesita la gestión y mejora en los procesos de decomisionado de cualquier elemento que haya llegado a su fin de vida útil (End Of Life, EOL). Se necesita especial atención a la mejora de los procesos que afectan a elementos críticos como los servidores de forma que tras su desmantelación no queden elementos o configuraciones sin gestionar, tales como IPs, espacios de almacenamiento, hostnames, redireccionamientos DNS, etc. (UPD15)

Para ello se solicita:

- Gestionar la información actual de dichos entornos.

- Actualizar, adaptar y mantener los servicios que se están prestando en servidores modernos, compatibles y seguros.

- Decomisionar los servidores que han llegado al final de su vida útil.

## Cloud (CLO)

## Mantenimiento del servicio de la nube de EducaMadrid

EducaMadrid cuenta con una infraestructura de código abierto para el servicio de nube. Esta infraestructura debe optimizarse, evolucionar y mantenerse para ofrecer mejor servicio (CLO1).

Se solicita:

- Mantener y mejorar la infraestructura de código abierto para el servicio de la nube de EducaMadrid.

- La estructura debe permitir una distribución balanceada de los distintos centros a los que se da servicio, compuestos por un total de 2 millones de usuario aprox.

- Se tendrá que realizar una redistribución de los NFS para su correcta funcionalidad a nivel multicentro y planificar y gestionar su crecimiento a medio y largo plazo.

- Mantener la solución con su debida gestión y corrección de incidencias.

- Mejorar la gestión de cuota del cloud actual que se realiza desde el desarrollo propio de Gestor de Usuarios del portal.

- Realizar las actualizaciones necesarias de versionado del aplicativo de manera recurrente.

## Mantenimiento y adaptación del sistema de almacenamiento temporal de datos de la nube

EducaMadrid dispone de un sistema de almacenamiento temporal de información integrado en su entorno de nube, cuyo objetivo es optimizar el acceso a datos y mejorar el rendimiento global de los servicios prestados. Dicho sistema requiere labores de mantenimiento, adaptación y evolución para garantizar su continuidad operativa, su adecuación a los cambios de carga y su correcta interacción con el conjunto de servicios de la plataforma (CLO2).

Se solicita:

- Mantener el sistema de almacenamiento temporal de datos, asegurando su disponibilidad, estabilidad y correcto funcionamiento, incluyendo las tareas necesarias de gestión, actualización y resolución de incidencias.

- Garantizar que dicho sistema continúe siendo compatible e interoperable con la nube de EducaMadrid y con los servicios que hacen uso de mecanismos de acceso optimizado a información temporal, sin alterar la arquitectura funcional existente.

- El sistema tiene que adecuarse a la carga y se realizarán las tareas necesarias para el escalado del mismo

## Mantenimiento del sistema de edición en línea de EducaMadrid

EducaMadrid cuenta con un servicio de edición en línea de documentos. Este servicio necesita evolucionar y mantenerse para ofrecer mejor servicio (CLO3).

Se solicita:

- Mejorar la infraestructura necesaria para soportar la edición en línea a los usuarios de la plataforma EducaMadrid.

- El sistema debe permitir la integración con la nube de EducaMadrid.

- Mantener y mejorar la solución con su debida gestión y corrección de incidencias.

- El sistema tiene que adecuarse a la carga y se realizarán las tareas necesarias para el escalado del mismo

## Otros desarrollos (OTR)

## Mantenimiento y mejora del sistema de autentificación centralizada Single Sign On (SSO)

Es necesaria el mantenimiento y la mejora del sistema basado en de Software Libre KeyCloak de inicio de sesión único (OTR1).

Se solicita:

- Mantener y mejorar la solución de código abierto de inicio de sesión único (SSO).

- Dicha solución SSO debe sincronizarse con el servicio de autentificación de la plataforma (actualmente LDAP).

- La solución debe incluir los controles necesarios para proporcionar el login automático en los aplicativos donde se implemente y permitir los accesos a estas con un inicio de sesión única, accediendo directamente a las aplicaciones si un usuario se encuentra logado y presentar la página de login cuando no sea así.

- Mantener la solución con su debida gestión.

- Mejorar la solución implementando redundancia a la Solución a través de una configuración en HA.

- Implementar 2FA en los servicios de Administración de la plataforma.

## Mantenimiento, configuración y gestión 2FA en el servicio de Single Sign On (SSO)

Es necesaria la implementación y el mantenimiento de un sistema 2FA en los servicios que utilicen inicio de sesión único (OTR2).

Se solicita:

- Realizar la implementación y el mantenimiento necesaria de la autentificación de dos factores (2FA).

- Dicha solución 2FA debe implementarse en los servicios que utilicen un inicio de sesión única en la plataforma.

- El flujo de autentificación debe permitir el acceso libre en los entornos educativos conectados a la red de Madrid Digital, así como permitir la autentificación mediante OTP, como por correo electrónico alternativo.

- Será obligatorio definir y mapear los correspondientes mapeos LDAP para mantener el correo electrónico EducaMadrid como principal en los diferentes servicios que se autentifiquen mediante SSO.

- La solución debe ser capaz de sincronizar y correlacionar el Token OTP del SSO con el Token OTP del correo electrónico web de la plataforma.

- Mantenimiento de la solución con su debida gestión.

<!-- salto de página -->

## Mantenimiento y mejora de herramientas de automatización de tareas

EducaMadrid necesita actualizar los sistemas de automatización de tareas de los diferentes aplicativos y BBDD (OTR3).

Para ello se solicita:

- Mejorar los sistemas de automatización de tareas de los diferentes aplicativos y BBDD.

- Mantener la solución con su debida gestión y corregir las incidencias.

## Mantenimiento y mejora de un sistema de gestión y análisis de datos mediante el stack de Elastic

EducaMadrid dispone de un sistema de gestión de datos centralizado y escalable adecuado para arquitecturas Big Data basado en el Software Libre Elastik (ELK), el cual se usa para analizar datos, generar informes y auditar las diferentes aplicaciones (OTR4).

Se solicita:

- Actualizar los diferentes servicios asociados al ELK-Stack incluyendo el sistema de almacenamiento distribuido, el motor de búsqueda y de procesamiento y el sistema de visualización.

- Mantener la solución con su debida gestión y corregir las incidencias.

## Mantenimiento y mejora de la herramienta de flujos de trabajo

Se necesita facilitar las tareas del equipo interno de EducaMadrid, así como el registro de las peticiones y progresos del trabajo realizado por cualquier técnico en la infraestructura de EducaMadrid, de forma que redunde en un menor tiempo de respuesta a los usuarios (OTR5).

Para ello se solicita:

- Mejorar la herramienta que permite la gestión de flujos de trabajo, de forma que se puedan recoger los datos de salida de distintas aplicaciones, bases de datos, documentos, etc. y ser procesados como entrada de otras partes de la plataforma.

- Mantener la solución con su debida gestión y corregir las incidencias.

- Actualizar la versión del aplicativo y paso a una base de datos externa dedicada.

## Mantenimiento y mejora del Portal CAU

La plataforma de EducaMadrid pone a disposición de sus usuarios la herramienta “Portal CAU” (portalcau.educa.madrid.org), basada en la solución de Software Libre Redmine, para que cualquiera pueda crear incidencias y seguir el estado de avance en la resolución de las mismas. Se necesita una mejora y mantenimiento (OTR6):

<!-- salto de página -->

Se solicita:

- Mantener, actualizar y mejorar el proyecto, de forma que se optimice el procedimiento de respuesta de las incidencias de nivel uno y el escalado de aquellas incidencias que deban ser tratadas por el nivel dos de soporte.

- Adaptar, mejorar y mantener un sistema que realice de forma automática la asignación de las nuevas incidencias a los distintos trabajadores del CAU de forma consecutiva, para una mayor agilidad de incidencias

- Mejorar, Optimizar y mantener los procesos que permiten detectar si el autor de una incidencia ya ha sido atendido por algún operario en los últimos días para que las nuevas incidencias abiertas por ese mismo autor sean asignadas al mismo operario, por si estuvieran relacionadas.

- Mantener la solución con su debida gestión y corregir las incidencias.

## Mantenimiento y evolución de servicios de Inteligencia Artificial para la plataforma EducaMadrid

EducaMadrid dispone de servicios que incorporan capacidades de Inteligencia Artificial para apoyar y mejorar la prestación de distintos servicios de la plataforma, incluyendo, correo web, aulas virtuales y entornos cloud. Estos servicios requieren labores continuas de supervisión, mantenimiento, mejora y adaptación para garantizar su disponibilidad, eficiencia operativa, interoperabilidad con otros sistemas y adecuación a las necesidades funcionales de la plataforma (OTR7).

Se solicita:

- Mantener, supervisar y mejorar los servicios de Inteligencia Artificial existentes, asegurando su correcto funcionamiento, disponibilidad y continuidad, incluyendo la gestión de incidencias y ajustes operativos que se consideren necesarios.

- Garantizar la integración de los servicios de Inteligencia Artificial con los distintos componentes de la plataforma, de manera que puedan prestar funcionalidades de forma coherente y centralizada a los diferentes servicios que los requieran.

- Realizar las adaptaciones, ajustes y optimizaciones que se consideren oportunas para adecuar los servicios a la carga, al uso previsto y a las necesidades funcionales y operativas, sin que ello implique la definición de un método técnico concreto.

- Llevar a cabo todas las tareas necesarias para la mejora continua, escalabilidad y resiliencia de los servicios, de forma que se asegure su estabilidad, eficiencia y capacidad de respuesta ante cambios en la demanda o en los requisitos funcionales.

- Documentar, reportar y gestionar de manera adecuada los trabajos realizados, manteniendo la trazabilidad de las acciones y asegurando la continuidad del servicio, sin que ello implique un procedimiento técnico único ni limitativo.

<!-- salto de página -->

## Correo electrónico (COR)

## Mantenimiento y mejora de los sistemas de control de envíos de correo

Determinados proveedores de correo, por ejemplo, sólo admiten un envío máximo de correos por hora, otros establecen otros parámetros que implican límites al envío de correos desde la plataforma de EducaMadrid. Para garantizar que se puedan realizar los envíos de los correos necesarios desde nuestra plataforma (tanto puntuales como masivos, p. ej. Boletines) se hace necesario implementar adaptaciones que aseguren que dichos correos lleguen a las direcciones que se desea, impidiendo, al mismo tiempo, el envío de correos no deseados o fraudulentos (COR1).

Se solicita:

- Mejorar el servicio que permite configurar un número máximo de correos/hora que se envíen a determinados proveedores, permitiendo una configuración distinta por cada proveedor.

- Mejorar cualquier otro servicio relacionado con la gestión y control de envíos de correo que disponga EducaMadrid y que sean necesarios para dar un servicio de correo correcto y de calidad a sus usuarios.

- Mantener las soluciones implementadas con su debida gestión y corregir las incidencias.

## Mantenimiento automatizado de listas de distribución de EducaMadrid

EducaMadrid tiene una herramienta de Software Libre que da soporte a un servicio de listas de distribución. En esta herramienta hay definidas muchas listas de distribución, las cuales se necesita tener actualizadas, mantenidas y actualizadas (COR2).

Se solicita:

- Gestionar, mantener y mejorar el sistema de distribución de listas de correo.

- Mantener con especial atención la adaptación que permite a la herramienta realizar una actualización automatizada de las listas de profesores, según nuevas incorporaciones y bajas a lo largo del curso.

Se deben realizar actualizaciones de estas listas de manera periódica (eliminación y carga completa) dos veces por curso coincidiendo con el período previo al comienzo de curso y el período no lectivo de navidad.

## Mantenimiento y mejora del sistema de activación y gestión de cuotas de correo

EducaMadrid, para la gestión del sistema de correo electrónico, necesita mantener los espacios limitados y por lo tanto se necesita un sistema de cuotas para usuarios (COR3).

<!-- salto de página -->

Se solicita:

- Monitorizar que se aplican las cuotas de correo correctas y actualizadas a todos los usuarios de EducaMadrid.

- Actualizar el sistema actual para permitir la gestión de las mismas, aplicando las cuotas correctas dependiendo del tipo de cuenta.

- Mantener y actualizar el desarrollo propio de gestor de usuarios para que en el alta de usuarios se especifique la cuota por defecto.

- Mantener las soluciones implementadas con su debida gestión y corregir las incidencias.

## Mantenimiento y mejora de las herramientas relacionadas con el control del spam

EducaMadrid necesita tener la seguridad de que son adecuados los controles de spam en el sistema de correo electrónico. (COR4).

Para ello, se solicita:

- Mantener, actualizar y mejorar cualquier solución desarrollada desde el departamento de Sistemas relacionada con el control del SPAM las cuales sirven de complemento a las soluciones implementadas desde el departamento de Ciberseguridad.

- Realizar y soportar las simulaciones controladas de ataques mediante phishing, o de cualquier otro tipo, incluyendo cualquier otra tarea relacionada con dichas pruebas.

Esta tarea se realizará periódicamente, como mínimo una vez al año.

## Mantenimiento de buzones de correo

Actualmente EducaMadrid cuenta con cerca de 2 millones de buzones de correo. Se necesita mantener optimizada la gestión de buzones de correo para la mejora continua del servicio (COR5).

Se solicita:

- Mantener los buzones de correo de EducaMadrid.

- Mejorar los procesos de mantenimiento al eliminar la creación del buzón con el alta, y que esta creación se realice en el primer acceso o cuando reciba el primer correo. La asignación de la ubicación de dichos buzones deberá ser realizada por el portal como hasta ahora.

- Modificar periódicamente dicha asignación para que ésta tenga en cuenta los nuevos mailboxes y maildirs disponibles para los usuarios, repartiendo la carga entre los diferentes espacios asignados al servicio.

- Gestionar, mejorar y mantener los procesos de creación, recuperación y eliminación de buzones de correo, así como de los relacionados con el reparto de carga.

- Mejorar y mantener los procesos de alta masiva de buzones de correo.

- Análisis y gestionar las cuentas sin uso o de usuarios borrados, prestando especial atención a la liberación del espacio ocupado por los mailboxes y al reparto de carga tras el borrado.

## Mantenimiento y mejora continua de la seguridad del sistema de correo

Actualmente EducaMadrid da servicio de correo electrónico a cerca de 2 millones de usuarios sobre una infraestructura compuesta por más de 30 servidores entre servidores de mailbox y aplicativos (COR6).

Se solicita:

- Actualizar los servicios manteniendo actualizados los certificados, implementando los accesos mediante la última versión disponible del protocolo seguro TLS.

- Gestionar, mantener, actualizar y mejorar cualquier elemento del sistema de correo de forma que se cumplan los requisitos de seguridad impuestos desde el departamento de Ciberseguridad.

## Actualización y mejora continua de la infraestructura en la que se basa el sistema de correo

Actualmente EducaMadrid da servicio de correo electrónico a cerca de 2 millones de usuarios sobre una infraestructura compuesta por más de 30 servidores entre servidores de mailbox y aplicativos (COR7).

Se solicita:

- Actualizar y mantener los servidores MX Gateway para que se ejecuten en la última versión disponible de RHEL. Esta labor requerirá la migración del entorno a versiones más actuales y soportadas del aplicativo.

- Actualizar, migrar y mantener los servidores Client Access Server (CAS) para que se ejecuten en la última versión disponible de RHEL.

- Actualizar, migrar y mantener todos los servidores Mailbox server para que se ejecuten en la última versión disponible de RHEL.

- Aplicar los parches y correcciones requeridas desde el departamento de Ciberseguridad para resolver las vulnerabilidades críticas detectadas. Las vulnerabilidades no críticas se acumularán para gestionarlas junto con las actualizaciones de versión de los aplicativos relacionados con el servicio.

Las labores de actualización de versiones y corrección de vulnerabilidades no críticas relacionadas con este servicio se realizarán al menos una vez al año aprovechando periodos no lectivos.

## Ampliación del número de servidores Mailbox Server

Actualmente EducaMadrid da servicio de correo electrónico a cerca de 2 millones de usuarios sobre una infraestructura compuesta por más de 30 servidores entre servidores de mailbox y aplicativos (COR8).

<!-- salto de página -->

Se solicita:

- Adecuar el número de servidores Mailbox server, ampliando, manteniendo o reduciendo el número actual, en unidades suficientes para que la carga de los servidores en producción esté situada en torno a un 25%.

## Implementación y mejora de un módulo receptor de inyección directa para la infraestructura de transporte de correo

EducaMadrid solicita disponer de un módulo receptor de inyección directa orientado a la deposición de entidades de mensaje completas en la infraestructura de spool del transporte de correo existente, coexistiendo con los endpoints tradicionales de sesión SMTP, sin sustituirlos ni alterar su comportamiento operativo (COR9).

Se solicita:

- Integrar el Módulo de forma transparente con la arquitectura de transporte y recepción de correo actualmente operativa, coexistiendo con los componentes desplegados sin interferir en su lógica transaccional ni requerir su sustitución.

- Garantizar que el Módulo actúe como complemento de inyección dentro del dominio de transporte, compartiendo la infraestructura de cola y los mecanismos de persistencia existentes, sin modificar las rutas tradicionales de sesión ni los procesos activos de recepción.

- Mantener la definición funcional del Módulo como tubería de ingestión postransaccional para la materialización persistente de entidades de mensaje completas en la capa de spool, preservando la integridad sintáctica y semántica del encabezado SMTP de origen.

- Garantizar la generación de objetos persistentes de spool con los metadatos obligatorios definidos, sin realizar entrega directa a buzones.

## Mantenimiento y soporte del módulo de inyección directa de correo

EducaMadrid necesita que se realice un mantenimiento y soporte especializado del módulo receptor de inyección directa que garantice el cumplimiento de los requisitos técnicos, de rendimiento y de aceptación establecidos, así como su coexistencia estable con los sistemas de correo existentes (COR10).

Se solicita:

- Cumplir y mantener los requisitos técnicos mínimos del sistema, incluyendo la interfaz de recepción TCP con opción de cifrado, la escritura atómica y durable del spool, los mecanismos configurables de back-pressure, la escalabilidad en múltiples instancias y la integración con los sistemas de observabilidad existentes.

- Garantizar que el Módulo actúe como complemento de inyección dentro del dominio de transporte, compartiendo la infraestructura de cola y los mecanismos de persistencia existentes, sin modificar las rutas tradicionales de sesión ni los procesos activos de recepción.

- Realizar las pruebas de validación y aceptación necesarias, incluyendo pruebas de generación correcta del spool, compatibilidad con los procesos existentes de entrega, pruebas de carga, resiliencia y coexistencia con los listeners SMTP activos.

- Garantizar que el despliegue, actualización, parada o retirada del módulo sea reversible y no tenga impacto en los servicios de recepción de correo existentes.

- Gestionar las herramientas de administración del módulo, incluyendo inspección, reintento y gestión de cola, así como la atención y resolución de incidencias relacionadas con el software y los servicios implicados.

- Mantener actualizada la documentación técnica, los procedimientos de operación, los scripts asociados y realizar la transferencia de conocimiento necesaria para la correcta explotación del sistema.

## Sistema Operativo MAX (MAX)

## Mantenimiento y actualización de MAX de forma presencial en centros de forma regular

Se necesita llevar la distribución MAX a los distintos centros educativos (MAX1).

Con este fin se solicita:

- Realizar tareas presenciales en los centros Educativos para el mantenimiento y actualización de las distribuciones Oficiales Soportadas del Sistema Operativo MAX de la Comunidad de Madrid.

- Configurar los diferentes tipos de periféricos adquiridos por el centro siempre y cuando cuenten con soporte para la distribución Linux en la que se basa MAX.

## Mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones

Actualmente MAX cuenta con un servidor de creación de distribuciones MAX basado en Debian. En él se realiza la compilación de las aplicaciones nuevas y actualizadas (MAX2).

Se solicita:

- Realizar el mantenimiento del servidor legacy MAX usado para versiones anteriores. Este servidor es un servidor Debian.

- Resolver las dependencias necesarias para el mantenimiento de las aplicaciones legadas.

- Realizar el mantenimiento del servidor MAX usado para desarrollar la versión actual, así como las posteriores. Este servidor es un servidor Debian. También, se mantendrán las dependencias experimentales para las aplicaciones más recientes y para aquellas que se encuentran en desarrollo.

- Adaptar y optimizar los servidores sobre los que se desarrollan las nuevas distribuciones de MAX para que dejen de depender de Ubuntu (debido a la nueva política de licenciamiento de Canonical a través de Ubuntu Pro), de forma que las nuevas versiones de MAX dependan de otras distribuciones de Software Libre.

## Mantenimiento de aplicaciones basadas en MAX

La Consejería de Digitalización lanza una versión de MAX aproximadamente una vez al año (MAX3).

Por ello se solicita:

- Mantener la configuración específica y el parcheado de aplicaciones.

- Para el mantenimiento de las aplicaciones instaladas en las distribuciones MAX es necesario que se descargue el código fuente y se compile sobre la distribución deseada con el propósito de satisfacer el funcionamiento de las aplicaciones.

Esta tarea se realizará periódicamente.

## Lanzamiento de distribuciones de MAX “Full Equip” anualmente

La Consejería de Digitalización lanza anualmente una nueva versión de MAX o hasta dos actualizaciones de versión (MAX4).

Para cada nuevo lanzamiento, se pide:

- La actualización y adaptación de la nueva versión de MAX.

- Para cada versión lanzada, hay que realizar el mantenimiento periódico, con configuración, actualización de las aplicaciones externas, y mantenimiento y supervisión del parcheado de la distribución.

## Lanzamiento de distribuciones de “MAX lite” y/o “max gestión” anualmente

Históricamente, EducaMadrid ha distribuido una distribución ligera de MAX destinada a equipos antiguos y de bajo consumo. También se dispone de opciones para incluir aplicaciones específicas dirigidas a los equipos directivos y de gestión TIC de los centros (MAX5).

Para ello se solicita:

- Mantener, actualizar y mejorar las distribuciones alternativas que EducaMadrid desea poner a disposición de sus usuarios, ya sea para facilitar su ejecución en equipos menos potentes y sin conexión a Internet, o ya sea para incorporar aplicaciones específicas de gestión que ayuden a los coordinadores TIC o a los miembros de los equipos directivos de los centros educativos de la Comunidad de Madrid, o para cualquier otro cometido que se defina.

- Dado que actualmente el foco está sobre la opción de gestión, habrá que realizar las tareas necesarias para mantener, actualizar, mejorar y parchear la distribución de “MAX Gestión” de forma que se genera una nueva versión y hasta dos actualizaciones de la misma anualmente.

## Integración de aplicaciones externas a los repositorios oficiales

EducaMadrid cuenta con una serie de servicios y aplicaciones en la nube. Se necesita una integración de estos servicios con las aplicaciones de escritorio de MAX (MAX6).

Para ello se solicita:

- Mantener, actualizar y mejorar la integración de aplicaciones externas que cumplan con las necesidades de los profesores en los centros educativos.

- Realizar la integración de las aplicaciones requeridas por la distribución para cumplir con las demandas del servicio ofrecido por EducaMadrid y asegurarse de que puedan ser distribuidas por los repositorios oficiales de MAX.

## Mantenimiento y mejora del servidor de gestión accesos remotos

Es necesario poder ofrecer asistencia personalizada remota para facilitar el uso en centros educativos de MAX, aparte de otros usos que se le pueda dar (MAX7).

Para ello se solicita:

- La mejoras y adaptaciones requeridas por el sistema de gestión del acceso remoto basado a los centros educativos por medio de un servidor propio de EducaMadrid.

- Mantener dicho gestor de acceso remoto.

## Soporte de asistencia telefónica y remota para incidencias de entornos MAX

Se necesita ofrecer un servicio de ayuda a los centros educativos con el sistema operativo MAX (MAX8)

Para ello se solicita:

- La asistencia técnica telefónica y mediante acceso remoto para cubrir las posibles incidencias y solicitudes de mantenimiento de cara al usuario final. Esta asistencia se integra dentro del servicio de soporte que se ofrece desde EducaMadrid a los Sistemas Operativos MAX instalados en los distintos centros de la comunidad de Madrid.

- Con la nueva implantación del sistema de gestión de repositorios de software dinámicos, también se hace necesario el mantenimiento y actualización de dicho sistema.

## Asistencia presencial en los diferentes eventos MAX

En ocasiones es necesaria la asistencia presencial en eventos para ayuda directa con el sistema operativo MAX (MAX9).

<!-- salto de página -->

Por tanto, se pide, cuando sea necesario:

- Visita presencial a los eventos que tengan mayor complejidad.

- Realizar el soporte de sus equipos en el evento.

- Posibles instalaciones y actualizaciones de MAX durante los eventos.

## Soporte presencial en eventos especiales (MAX Install Party)

Se necesita dar a conocer las nuevas versiones y herramientas de MAX, para lo cual EducaMadrid realiza distintos eventos especiales, tales como las Install Party (MAX10).

Para ello se solicita:

- Soporte presencial especializado en la distribución MAX vigente.

- Ofrecer instalación, actualización y configuración de los equipos de los diferentes participantes que atiendan el evento.

Estos eventos se organizarán en distintos momentos del año.

## Gestión, mantenimiento y actualización de equipos MAX en remoto

Una de las grandes problemáticas que existen en algunos centros educativos es la falta de mantenimiento y actualización de los equipos, quedando estos expuestos (MAX11).

Por lo tanto, se solicita:

- Tener un control de gestión de actualización para los centros educativos que lo soliciten.

- Mantenimiento de dicho control de gestión de actualización.

## Instalación y configuración de dispositivos solicitadas por los centros educativos

Se necesita dar soporte de dispositivos a lo largo de cada curso a los diferentes tipos de centros educativos en la Comunidad de Madrid (MAX12).

Por lo tanto, se solicita:

- Instalar y configuración de aplicaciones y dispositivos (pizarras, tabletas, etc.) específicas para el buen desarrollo de sus aulas de clase.

Este soporte se ofrecerá a lo largo del curso escolar, según lo vayan solicitando de los centros educativos.

## Mantenimiento y soporte del servidor de repositorio individual para centros educativos

EducaMadrid ofrece un servidor de repositorio individual para los centros educativos que usen el Sistema Operativo MAX (MAX13).

Por lo tanto, se solicita:

- Llevar a cabo un control de la gestión para los centros educativos que lo soliciten.

- Hacer el mantenimiento y el control de la gestión de las actualizaciones.

- Realizar una auditoría de los sistemas instalados en los centros (hardware y software).

- Monitorizar los errores en los equipos gestionados.

Este mantenimiento y soporte se ofrecerá a lo largo del curso escolar, según lo vayan solicitando de los centros educativos.

## Herramienta de gestión centralizada de maquetas de MAX

EducaMadrid cuenta con una solución interna de gestión centralizada de maquetas para Sistemas Operativos MAX basada en el Software Libre Migasfree. Como solución para los centros se necesita configurar y mantener la herramienta para que también permita la gestión centralizada y remota de los equipos desplegados en los diferentes centros (MAX14).

Por lo tanto, se solicita:

- Mantener y mejorar la solución implementada en EducaMadrid permitiendo su uso por parte de los centros educativos facilitando así una solución de gestión remota y centralizada de plataformas de Sistema Operativo MAX.

- Mantener, actualizar y dar soporte a la solución completa, incluyendo tanto a la parte que afecta a los equipos internos como a la o que afecta a los equipos MAX de los centros educativos que lo hayan solicitado.

Este soporte se ofrecerá a lo largo del curso escolar, según lo vayan solicitando de los centros educativos.

## Aulas Virtuales (AV)

## Actualización y comprobación periódicas de servidores físicos y virtuales de BBDD de los entornos de aulas virtuales

Actualmente EducaMadrid tiene más más de 2500 bases de datos de las diferentes aulas virtuales y otros sistemas de formación en línea, alojadas en distintos servidores tanto físicos en clúster como virtuales. La mayor parte de ellas son PostgreSQL, pero también MariaDB y MongoDB (AV1).

Se solicita:

- Realizar de forma periódica actualizaciones de versión necesarias de los distintos servidores de base de datos, teniendo en cuenta la compatibilidad con la versión de las Aulas Virtuales que tengan en cada momento.

- Comprobar el correcto funcionamiento y la estabilidad de los aplicativos en los entornos de desarrollo y preproducción, así como un correcto rendimiento de estos.

## Mantenimiento de los servidores virtuales FrontEnd de los entornos de aulas virtuales

Se necesita la realización de las tareas para la migración y mantenimiento del entorno actual frontend del aplicativo de las aulas virtuales para guardar compatibilidad con las nuevas versiones de Moodle (AV2).

Para ello se solicita:

- Realizar de forma periódica actualizaciones de versión mediante reinstalación de todos los frontales que haya, manteniendo también los aplicativos necesarios actualizados a la última versión.

- Realizar la parametrización y optimización de los mismos, así como su mantenimiento.

## Despliegue periódico de nuevos grupos de aulas virtuales y ampliación de los actuales

Actualmente EducaMadrid tiene más de 1.900 instancias de Moodle distribuidas en 8 grupos o islas (AV3).

Se solicita:

- Realizar las ampliaciones de los grupos (islas) actuales acorde a la demanda.

- Creación de nuevas islas de aulas virtuales para mantener la demanda creciente poniendo especial atención al balanceo y reparto de la carga.

- Realizar las labores necesarias de monitorización del rendimiento de los frontales en función de la carga de los centros.

Estas tareas se realizarán periódicamente.

## Redistribución periódica de los NFS de datos de las aulas virtuales

EducaMadrid cuenta con un gran número de aplicativos que utilizan NFS para su funcionamiento. Algunos de estos NFS tienen un tamaño que dificulta su control (AV4).

Se solicita:

- Realizar de forma periódica una redistribución de los espacios ocupados por los centros por los distintos NFS atendiendo a la ocupación de estos.

Para la realización de estas tareas se deben aprovechar los períodos no lectivos, tales como vacaciones de verano, Semana Santa y/o Navidad. Estas tareas se realizarán periódicamente.

<!-- salto de página -->

## Servicio de LDAP y Portal Educativo (POR)

## Ampliación periódica del sistema de esclavos LDAP de EducaMadrid

EducaMadrid cuenta con un servidor principal de LDAP y numerosos secundarios/esclavos (POR1).

Se solicita:

- Mantener, ampliar y adaptar el número de servidores LDAP de forma que se mantengan cubiertas las necesidades de todos los servicios ofrecidos por EducaMadrid.

- Analizar, estudiar las posibilidades y aplicar una redistribución de estos servidores, dividiéndolos por servicios, para optimizar su rendimiento.

Estas tareas se realizarán periódicamente.

## Migración del sistema LDAP máster de EducaMadrid

EducaMadrid cuenta con un servidor principal de LDAP y numerosos secundarios/esclavos (POR2).

Se solicita:

- Realizar las tareas de mantenimiento y actualización sobre los LDAP Master físicos yendo a una versión LDAP Master virtualizada que se ejecute sobre la última versión de sistema operativo compatible con el esquema actual de LDAP.

- Mejorar la funcionalidad del sistema de correo configurándolo para que pueda integrarse con el sistema de acceso a EducaMadrid por SSO, permitiendo adicionalmente el uso de 2FA.

Estas tareas se realizarán periódicamente para mantener los LDAP Master lo más actualizados posible, tanto en versiones como en funcionalidades.

## Seguridad (SEG)

## Mantenimiento y mejora del sistema de control de cambios en DNS

Actualmente EducaMadrid cuenta con un servicio DNS de cierto tamaño y que necesita un sistema de revisión (SEG1).

Se solicita:

- Realizar las labores de mejora continua del sistema de control de modificaciones del DNS público, para securizar el control de cambios.

- Realizar el mantenimiento periódico de dicha aplicación, para asegurar su correcto funcionamiento.

## Mantenimiento y mejora de un LDAP Máster independiente para usuarios privilegiados

Actualmente EducaMadrid cuenta con LDAP Master donde se guardan los usuarios que de alguna forma tienen privilegios especiales sobre los sistemas TI de EducaMadrid. (SEG2).

Se solicita:

- Gestionar, mantener y actualizar el sistema LDAP independiente al que se conectan los servidores para permitir el login de los usuarios privilegiados del sistema, poniendo especial cuidado en su correlación con el PAM de EDUCAMADRID

- Mantener de forma periódica dicho LDAP, para asegurar su correcto funcionamiento.

## Gestión, mantenimiento e implantación anual de los certificados de EducaMadrid

EducaMadrid cuenta con certificados de seguridad instalados para la gestión de su seguridad (SEG3).

Se solicita:

- Comprobar activamente los estados y fechas de caducidad y de renovación de los certificados, la integridad del no repudio y el cumplimiento de la robustez y fortaleza de los mismos.

- Actualizar mediante sustitución antes del plazo de caducidad y aplicar las renovaciones y nuevas inclusiones de nuevos certificados, aplicando el control habitual sobre el estado de los mismos.

- Realizar la gestión, mantenimiento, e implantación anual de los certificados de EducaMadrid instalados, tanto en la electrónica de red como en los diferentes servidores para su correcto funcionamiento.

Estas tareas se realizarán periódicamente. Las actualizaciones de los certificados de toda la plataforma se realizarán, al menos, una vez al año.

## Gestión y mantenimiento periódico de dominios DNS

Se necesita en EducaMadrid realizar la gestión y el mantenimiento periódico de los Dominios DNS con el fin de evitar vulnerabilidades. (SEG4).

Para ello se solicita:

- Supervisar y auditar de forma continua los dominios existentes en busca de permutaciones de control, detección de phishing, control de subdominios y verificando los certificados y protocolos vigentes sobre los mismos.

## Análisis y corrección de vulnerabilidades

Es necesaria la gestión de seguridad mediante el análisis y corrección de vulnerabilidades en los servicios de EducaMadrid (SEG5).

Para ello se solicita:

- Colaborar con el SOC para la detección y resolución de vulnerabilidades.

- Supervisar y auditar continuamente los activos, realizar el escaneo de servidores, la detección de vulnerabilidades, la solicitud y recomendaciones de corrección, las correlaciones con notificaciones de vulnerabilidades de organismos oficiales, la clasificación de criticidades y la categorización según estándares NIST CVE.

- Hacer seguimiento y comprobación de las posibles correcciones de los activos y chequeo de evoluciones de estado.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad.

## Gestión, mantenimiento y ajuste de la herramienta para la detección de intrusiones, monitorización de la integridad, análisis de logs y respuesta ante incidentes.

Para ello se solicita (SEG6):

- Supervisar de forma continua y automática los activos

- Revisar el estado e integridad de los logs

- Detectar intrusiones y establecer alertas de diversos tipos y alarmas prioritarias

- Ejecutar acciones de respuesta a los incidentes y notificación de los mismos a los responsables de EducaMadrid.

- Calibrar, adecuar e implementar mejoras en los desarrollos con el fin de mejorar su seguridad.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad.

## Realización de auditorías internas de aplicaciones

Para chequear su seguridad y prevenir ataques, EducaMadrid necesita realizar auditorías internas de seguridad en sus aplicaciones. (SEG7).

Para ello se solicita:

- Auditar el estado y detectar las posibles vulnerabilidades según los estándares OWASP, tanto de los aplicativos propios como de los usados en EducaMadrid.

- Realizar pruebas de clasificación y explotación de vulnerabilidades.

- Ejecutar las correcciones pertinentes en función de las anomalías detectadas.

- Hacer seguimiento y comprobación de la corrección de los aplicativos y chequear las evoluciones de estado.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad.

<!-- salto de página -->

## Realización de auditorías internas continuas de los sistemas

Para chequear su propia seguridad y prevenir ataques, EducaMadrid necesita realizar auditorías internas de seguridad en sus sistemas. (SEG8).

Para ello se solicita:

- Auditar de forma continua los sistemas, según los estándares vigentes.

- Cotejar los resultados con el cumplimiento de los requisitos exigidos en el ENS.

- Clasificar los resultados y evaluar la estrategia y pasos necesarios para la corrección de las anomalías encontradas

- Ejecutar las correcciones pertinentes a los problemas, comprobando la remediación de las anomalías y chequear continuamente la evolución del estado de los problemas encontrados.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad.

## Mantenimiento y uso de logs centralizados

Se solicita (SEG9):

- Almacenar de forma centralizada los logs de los sistemas.

- Controlar y supervisar continuamente la integridad y calibración de los logs.

- Gestionar el almacenamiento de la información en unidades externas, por sistema rotatorio, durante el periodo que fija el ENS relativos a tiempo de conservación de los mismos para posteriores comprobaciones de posibles incidentes y realización de análisis de tipo forense si fuera requerido.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad.

## Implementación y mantenimiento de claves RSA unificadas

Para garantizar la seguridad, coherencia e integridad de los servicios de EducaMadrid, se requiere la gestión unificada de las claves RSA utilizadas en los distintos entornos y aplicaciones. La intervención sobre dichas claves queda condicionada a la observación de los flujos de comunicación entre servicios, cuya falta de visibilidad puede invalidar la actuación (SEG10).

Se solicita:

- Establecer un régimen de gestión y supervisión de claves RSA, garantizando coherencia y seguridad de los procesos que las utilizan, considerando que la ausencia de información sobre comunicaciones puede limitar o invalidar la intervención.

- Supervisar de forma periódica el estado y la validez de las claves, identificando potenciales riesgos, vulnerabilidades o situaciones que puedan afectar a la integridad de los servicios.

- Ejecutar las acciones correctivas o preventivas necesarias para garantizar el funcionamiento seguro de los sistemas que dependen de dichas claves.

- Mantener un seguimiento de los cambios, actualizaciones o migraciones de claves, asegurando que los servicios continúan operando de forma coherente y segura

Estas tareas se realizarán de manera periódica y cada vez que se identifique la necesidad.

## Asistencia y soporte presencial en los diferentes eventos de Ciberseguridad de EducaMadrid

EducaMadrid es pionero en su estrategia de concienciación y transmisión de la información a sus equipos en materias de seguridad. Como base de su estrategia están los “Ciberjueves” que son eventos que, con una periodicidad mensual (aproximadamente), reúnen a todo el equipo de EducaMadrid para actualizarles sobre asuntos relativos a la Ciberseguridad y las ciberamenazas. Suele contar con ponentes experimentados en los ámbitos de la ciberseguridad para, en una charla de una hora aproximadamente, hablen a todo el equipo acerca de asuntos de actualidad y novedades en el sector (SEG11).

Para ello se solicita:

- Realizar acciones de concienciación en ciberseguridad con la periodicidad establecida en el departamento de Ciberseguridad de EducaMadrid.

- Proponer ciber consejos y acciones de difusión de la Ciberseguridad.

- Preparar y coordinar todo lo relativo a los “Ciberjueves”: organizar, controlar y supervisar los diferentes eventos, así como gestionar asistentes y espacios.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad.

## Automatización y contenedores (CON)

## Mantenimiento y mejora del sistema de gestión de contenedores

Actualmente EducaMadrid se encuentra en proceso de migración de algunas de sus aplicaciones a entornos contenerizados.(CON1).

Se solicita:

- Realizar las labores de mejora continua del sistema de control y gestión de contenedores.

- Realizar el mantenimiento periódico de dicho entorno, para asegurar su correcto funcionamiento.

<!-- salto de página -->

## Mantenimiento y mejora de los scripts y sistemas de automatización de tareas

Actualmente EducaMadrid dispone de cientos de scripts de automatización de tareas, así como de herramientas específicas para automatizar determinadas acciones sobre su infraestructura de sistemas. (CON2).

Se solicita:

- Gestionar, mantener y actualizar el sistema de scripts, modificando y actualizando aquellos que sean necesarios.

- Gestionar, mantener y actualizar las aplicaciones de automatización integradas en la infraestructura de EducaMadrid.

- Realizar los mantenimientos periódicos, tanto reactivos como proactivos, de estos elementos, incluyendo la aplicación de parches de seguridad y las configuraciones que, desde el departamento de ciberseguridad, sean requeridas.

## Mantenimiento y mejora del sistema auxiliar de automatización

Actualmente, EducaMadrid dispone de un sistema auxiliar de automatización basado en llamadas HTTP (POST/GET) que permite automatizar distintos servicios y procesos internos. Se solicita garantizar su correcto funcionamiento mediante mantenimiento, actualización y optimización. (CON3).

Se solicita:

- Mantener, actualizar y mejorar los scripts y flujos que interactúan con el sistema auxiliar, asegurando compatibilidad con la infraestructura y servicios existentes.

- Realizar mantenimientos periódicos, tanto proactivos como reactivos, incluyendo aplicación de parches de seguridad y ajustes de configuración según indicaciones de ciberseguridad y operaciones.

- Documentar los endpoints, flujos y dependencias del sistema auxiliar, asegurando trazabilidad, coherencia de datos y facilidad de mantenimiento futuro.

## Gestión de la migración de servidores entre CPDs (MIG)

## Coordinación y planificación de la revisión de los entornos migrados

Se requiere una coordinación y planificación para asegurar que todos los equipos implicados actúen de forma alineada y que se minimicen los riesgos tanto durante la migración como después de la migración desde el punto de vista de los sistemas y servicios. (MIG1).

Se solicita:

- Participar en reuniones de coordinación con el personal del CPD y del proveedor de servicio de Infraestructuras.

- Documentar las decisiones, los diferentes riesgos y las recomendaciones.

- Asegurar la comunicación y el seguimiento de las acciones que afecten a sistemas y aplicaciones entre los equipos implicados.

## Fases preparatorias y planificación técnica de la migración

En relación con la migración, será necesario realizar tareas de análisis y planificación técnica que permitan al equipo de sistemas disponer de una visión clara del entorno y de la secuencia de actuación después de la migración. (MIG2).

Se solicita:

- Analizar y documentar los mapas del CPD desde el punto de vista lógico de sistemas y servicios (servidores, aplicaciones, dependencias y relaciones entre servicios).

- Revisar el Plan de Migración, aportando la visión funcional de los sistemas y aplicaciones.

- Validar el Plan de Migración definitivo en lo relativo a sistemas y servicios tanto para el traslado (si fuera necesario) como para las comprobaciones posteriores.

- Coordinar con el equipo responsable de infraestructura la idoneidad del CPD de destino desde el punto de vista de la disponibilidad y correcta ubicación de los sistemas y servicios.

## Preparación de servidores y documentación de sistemas

Se necesita una preparación de servidores y la documentación asociada que permita conocer el estado de los sistemas y definir procedimientos claros para la gestión de los servicios durante la migración (MIG3).

Se solicita:

- Comprobar la información técnica que se tiene de los servidores desde el punto de vista de sistemas y servicios (CPU, memoria, almacenamiento lógico, servicios y aplicaciones).

- Elaborar y revisar la documentación de procedimientos de parada y arranque lógicos y validación de servicios.

- Preparar y revisar los listados de comprobación para la verificación de servicios y aplicaciones antes y después de la migración.

## verificación de la migración

Durante la ejecución de la migración, el equipo de sistemas y soporte se encarga de supervisar el estado de los servicios y validar el correcto funcionamiento de las aplicaciones. (MIG4).

Se solicita:

- Ejecutar scripts de recopilación de información y diagnóstico para verificar el estado de los sistemas después del traslado, una vez estabilizados los sistemas, y comparar esos datos con los mismos datos recogidos antes y durante el traslado de CPD.

- Supervisar la disponibilidad de servicios y aplicaciones, detectando incidencias relacionadas con software o configuración.

- Registrar y documentar incidencias de sistemas y servicios, coordinando su resolución con los equipos responsables de infraestructura cuando sea necesario.

- Verificar la integridad de datos, configuraciones y funcionamiento de aplicaciones desde el punto de vista del sistema operativo y los servicios.

## Mantenimiento y soporte tras la migración

Después de la ejecución de la migración, el equipo de sistemas y soporte se encargará de supervisar el estado de los servicios y validar el correcto funcionamiento de las aplicaciones. (MIG5).

Se solicita:

- Supervisar la disponibilidad de servicios y aplicaciones, detectando incidencias relacionadas con software o configuración.

- Verificar la integridad de datos, configuraciones y funcionamiento de aplicaciones desde el punto de vista de los sistemas y los servicios.

Supervisar la estabilidad de los servicios tras la migración y documentar las acciones correctivas realizadas.

## Inteligencia Artificial (IA)

Identificar y evaluar diferentes modelos de inteligencia artificial (IA) que puedan ser adaptados a los servicios de la plataforma educativa EducaMadrid. Para ello es necesario realizar una investigación exhaustiva de modelos de IA, evaluar los modelos seleccionados según los criterios establecidos y documentar los resultados y recomendaciones.

## EVALUAR el rendimiento de los modelos seleccionados

Evaluar el rendimiento de los modelos de IA seleccionados en un entorno de prueba que simule las condiciones operativas de la plataforma EducaMadrid (IA1). Para ello se requiere estudiar:

- Métricas de Rendimiento: Utilizar métricas como la precisión, recall, F1-score, tiempo de respuesta, y consumo de recursos (CPU, GPU, memoria) para evaluar el rendimiento.

- Escenarios de Prueba: Diseñar escenarios de prueba que representen las diferentes funcionalidades y cargas de trabajo de la plataforma EducaMadrid.

- Herramientas de Evaluación: Utilizar herramientas de benchmarking y análisis de rendimiento para medir y comparar el rendimiento de los modelos.

Se solicita:

- Diseñar y ejecutar pruebas de rendimiento.

- Recopilar y analizar los datos de rendimiento.

- Generar informes de rendimiento comparativo.

## Ingeniería de Prompts adaptados para cada servicio

Desarrollar y optimizar prompts (instrucciones) específicos para cada servicio de la plataforma EducaMadrid, asegurando que los modelos de IA respondan de manera precisa y relevante (IA2). Para ello se requiere:

- Analizar Requisitos: Identificar los requisitos específicos de cada servicio y las expectativas de los usuarios.

- Diseñar Prompts: Crear prompts detallados y claros que guíen a los modelos de IA para generar respuestas adecuadas.

- Pruebas y Ajustes: Realizar pruebas iterativas para ajustar y optimizar los prompts en función de los resultados obtenidos.

Se solicita:

- Analizar los requisitos de cada servicio.

- Diseñar y desarrollar prompts específicos.

- Realizar pruebas y ajustes iterativos.

## Testeo de los guardarraíles para el entorno educativo

Asegurar que los modelos de IA implementados en la plataforma EducaMadrid cumplan con las normativas y políticas educativas, incluyendo la protección de datos y la ética en el uso de la IA. (IA3). Para ello se requiere:

- Normativas y Políticas: Revisar las normativas y políticas educativas relevantes, incluyendo la protección de datos personales (GDPR, LOPDGDD) y las directrices éticas.

- Guardarraíles Técnicos: Implementar mecanismos de control y monitoreo para asegurar que los modelos de IA no generen respuestas inapropiadas o perjudiciales.

- Pruebas de Seguridad: Realizar pruebas de seguridad y privacidad para identificar y mitigar posibles vulnerabilidades.

Se solicita:

- Revisar y documentar las normativas y políticas relevantes.

- Implementar y configurar los guardarraíles técnicos.

- Realizar pruebas de seguridad y privacidad.

## Evaluar Posibilidades de Integración en Distintos Aplicativos

Evaluar la viabilidad de integrar los modelos de IA en diferentes aplicativos y servicios de la plataforma EducaMadrid (IA4). Para ello se requiere:

- Compatibilidad Técnica: Evaluar la compatibilidad técnica de los modelos de IA con los diferentes aplicativos y servicios.

- Interfaz de Integración: Diseñar y desarrollar interfaces de integración que permitan la comunicación y el intercambio de datos entre los modelos de IA y los aplicativos.

- Pruebas de Integración: Realizar pruebas de integración para asegurar que los modelos de IA funcionen correctamente en el contexto de los diferentes aplicativos.

Se solicita:

- Evaluar la compatibilidad técnica de los modelos de IA.

- Diseñar y desarrollar interfaces de integración.

- Realizar pruebas de integración.

## Evaluación de Capacidades de Respuesta y Límites por Usuario

Evaluar las capacidades de respuesta de los modelos de IA y establecer límites razonables para el uso por parte de los usuarios, asegurando un rendimiento óptimo y una experiencia de usuario satisfactoria (IA5). Para ello se requiere:

- Capacidades de Respuesta: Medir el tiempo de respuesta de los modelos de IA bajo diferentes condiciones de carga y uso.

- Límites por Usuario: Establecer límites en función del número de solicitudes por usuario y el tiempo de inactividad para evitar sobrecargas y asegurar un uso equitativo.

- Pruebas de Estrés: Realizar pruebas de estrés para evaluar el comportamiento de los modelos de IA bajo condiciones de alta demanda.

Se solicita:

- Medir y analizar las capacidades de respuesta de los modelos de IA.

- Establecer y documentar los límites por usuario.

- Realizar pruebas de estrés y ajustar los límites según sea necesario.

## Productos resultantes del contrato, incluyendo los requisitos de documentación

En los puntos anteriores se concretan todos los trabajos que se requieren en el desarrollo del contrato describiéndose y enumerándose cada uno de los entregables siguiendo la nomenclatura del apartado III.1.1 del presente documento:

| BASES DE DATOS (BD) | 6 |
| --- | --- |
| MONITORIZACIÓN, TESTEO Y PRUEBAS DE RENDIMIENTO (MON) | 4 |
| ACTUALIZACIÓN DE SERVICIOS EXISTENTES (UPD) | 15 |
| CLOUD (CLO) | 3 |
| OTROS DESARROLLOS (OTR) | 7 |
| CORREO ELECTRÓNICO (COR) | 10 |
| SISTEMA OPERATIVO MAX (MAX) | 14 |
| AULAS VIRTUALES (AV) | 4 |
| SERVICIO DE LDAP Y PORTAL EDUCATIVO (POR) | 2 |
| SEGURIDAD (SEG) | 11 |
| AUTOMATIZACIÓN Y CONTENEDORES (CON) | 3 |
| GESTIÓN DE LA MIGRACIÓN DE SERVIDORES ENTRE CPDS (MIG) | 5 |
| INTELIGENCIA ARTIFICIAL | 5 |
| **TOTAL** | **89** |

En total se describen **89 entregables** en este documento.

Se entiende por entregables los elementos desarrollados en el proyecto que constituyen componentes del proyecto o servicio o del producto software objeto de desarrollo, en los que dicho producto software será un entregable más del proyecto.

El total de esfuerzo ordinario anual en las tareas de desarrollo correctivo y gestión de incidencias se estima en **10.929,8***0 horas** a cargo de los diferentes perfiles indicados en el apartado correspondiente.

El total de esfuerzo extraordinario anual fuera del horario ordinario se estima en **619,5***0 horas**, que podrá llevar a cabo cualquiera de los perfiles del contrato.

El adjudicatario se compromete a que los técnicos registren periódicamente el desarrollo y avance de los trabajos realizados en la herramienta que designe EducaMadrid (actualmente Redmine). La información registrada será suficiente para que EducaMadrid pueda informarse acerca de las tareas que se están realizando y del estado de avance de dichos trabajos, y será completa hasta el punto de que, en caso de baja, cese o sustitución de alguno de los técnicos, el técnico que le sustituya pueda continuar desde el punto en el que se encuentre.

Asimismo, EducaMadrid establecerá las prioridades de los trabajos y tareas a realizar en función de su propia estrategia, o de las necesidades o requisitos de los usuarios y de los servicios que ofrece. El establecimiento de prioridades y estrategias se podrá llevar a cabo en cualquier momento y a través del medio o herramienta que EducaMadrid indique al adjudicatario.

Con el fin de verificar tanto la seguridad de los sistemas como el cumplimiento de las prioridades, tareas y dedicación comprometidas a través del servicio contratado, el adjudicatario informará tanto del trabajo realizado como de las tareas específicas en las que ha estado involucrado cada uno de sus técnicos. EducaMadrid indicará al adjudicatario, la forma, herramienta, medio y periodicidad con la que se requerirá esta información. Dado que, en la actualidad, se pide que se refleje esta información de forma diaria y con el objetivo de minimizar la burocracia del proceso, EducaMadrid admite que dicha información sea facilitada por cada técnico directamente al finalizar su jornada, siempre y cuando así lo estimara conveniente el adjudicatario.

El adjudicatario se compromete a generar toda la documentación que sea aplicable como resultado de la prestación de los servicios y la ejecución de cada uno de los entregables, entregando la documentación correspondiente en el formato electrónico que se determine.

El adjudicatario pondrá a disposición de EducaMadrid en todo momento la documentación que se vaya generando durante el proceso de desarrollo del proyecto y de cada uno de los entregables.

Para cada entregable, según las características del mismo y la planificación acordada, se aportará la información que aplique, desarrollándose los contenidos necesarios según los puntos siguientes:

- Estudios Previos

- Catálogo de requisitos

- Análisis funcional (descripción funcional, casos de uso, diagramas de estados, modelo conceptual de datos, sistemas externos, etc.)

- Diseño funcional y técnico (arquitectura, soluciones técnicas utilizadas, patrones de diseño, modelos de datos, interfaces, diagramas de clases, de secuencia, etc.)

- Planes de pruebas funcionales

- Resultados del plan de pruebas funcionales

- Configuración de las pruebas de rendimiento

- Requerimientos mínimos de instalación

- Plan de gestión del cambio (material de comunicación y formación, presentaciones, material divulgativo, etc.)

- Informe de situación e incidencias

- Documentos de seguimiento (planificaciones, actas de reunión, informes de seguimiento, etc.)

- El adjudicatario se compromete, en su caso, a la entrega final de los productos resultantes de los trabajos de desarrollo:

- Fuentes: programas, scripts, archivos de instalación y configuración, etc.

- Documentaciones técnicas y funcionales (catálogo de requisitos, diseño funcional y técnico, modelo de datos, manual de instalación, manual de operación/explotación, notas de versiones, manuales de usuario, material de formación, etc.)

En general, se exigirá como entregable toda la información necesaria para la correcta instalación, operación, uso, mantenimiento y monitorización de los sistemas desarrollados, así como cualquier producto generado: documentaciones, procedimientos, scripts, configuraciones, etc.…

Toda la documentación deberá entregarse actualizada. EducaMadrid determinará si la documentación aportada debe ser mejorada, completada, ampliada o elaborada de otro modo para su mejor aprovechamiento por la organización.

Se asegurará la calidad en las entregas de las mejoras y/o desarrollos de software antes de su paso al entorno de producción, conforme a las políticas y estándares definidos y a través de los procedimientos y herramientas implantados.

Las entregas de software (documentación y software) deberán cumplir con los estándares de calidad, pudiéndose realizar validaciones y pruebas del tipo siguiente:

- Validación del estilo de codificación (uniforme, claro y ajustado a estándares).

- Pruebas unitarias y de regresión automatizadas que permitan validar el correcto funcionamiento de los módulos de la aplicación. Pruebas funcionales automatizadas para verificar que el producto entregado cumple con los requisitos y necesidades establecidos, mediante el uso de herramientas que permitan la grabación y almacenamiento de pruebas de usuario para posteriores pruebas de regresión y para su ejecución y certificación en distintos entornos.

- Pruebas de rendimiento para el aseguramiento de que el software cumple con las cargas de trabajo previstas.

- Monitorización técnica de aplicaciones, para obtener información del funcionamiento y consumo de recursos de la aplicación en el tiempo y detectar las causas de los errores una vez producidos.

- Pruebas de seguridad automatizadas, como la explotación de vulnerabilidades típicas de las aplicaciones Web, y verificación de *checklists* asociadas a la normativa de desarrollo seguro de software basadas en guías de estándares y metodologías OpenSource Security Testing Methodology Manual (OSSTMM), Open Web Application Security Project (OWASP), o equivalentes.

<!-- salto de página -->

# SERVICIOS DE MANTENIMIENTO BAJO ANS

Corresponden a los servicios para el mantenimiento correctivo de las aplicaciones en funcionamiento en entornos en producción de usuarios finales conforme a lo descrito en el Anexo I y en el Anexo II.

Debido a su naturaleza, el mantenimiento correctivo y la gestión de las incidencias de los proyectos exteriores supone la carga de trabajo extensa.

## Descripción del servicio de mantenimiento correctivo y la gestión de incidencias de los sistemas en entornos productivos.

## Alcance

Las tareas de mantenimiento correctivo y la gestión de las incidencias estarán orientadas al aseguramiento de la continuidad del servicio de los sistemas en entornos productivos cubrirá el conjunto de los sistemas de información y el entorno tecnológico descritos en el Anexo I y en el Anexo II.

El servicio consiste en la corrección del código fuente o de la documentación para resolver o paliar las incidencias que afecten a los citados sistemas de información, así como todas las tareas conexas necesarias para poder realizar dicha corrección.

Concretamente el contrato estará centrado en las tareas que se refieren tanto a los Proyectos de Sistemas actualmente alojados en la Plataforma Educativa EducaMadrid como a los que pudieran surgir, de naturaleza similar, a lo largo de la vigencia del contrato.

## Gestión de incidencias

El responsable del Contrato Específico, o la persona designada por éste para la tarea, clasificará las incidencias que detecte y las que comuniquen los usuarios, comunicándolas a su vez al contratista por escrito, mediante correo electrónico o herramienta de gestión del servicio (en inglés, *ITSM*) según decisión del organismo destinatario, haciendo constar:

- Fecha y hora;

- Sistema, módulo o componente en el que se perciben los efectos de la incidencia;

- Gravedad de la incidencia, clasificada como Leve, Grave o Crítica;

- Descripción de los efectos observados como consecuencia de la incidencia.

En ningún caso los usuarios del sistema de información se dirigirán directamente al personal asignado por la adjudicataria a la ejecución del presente contrato específico.

Así mismo se atenderán incidencias por teléfono, correo electrónico u otros medios electrónicos relacionados con toda la plataforma de EducaMadrid, especialmente las relativas a los servicios aquí expuestos.

<!-- salto de página -->

Existen 2 niveles de incidencia:

- Nivel 1, que será llevada a cabo por técnicos de soporte de nivel 1, que tendrán que conocer la plataforma de EducaMadrid a nivel funcional.

- Nivel 2, que será llevada a cabo por los analistas programadores o por los técnicos de sistemas. Estas incidencias serán de carácter técnico.

Las áreas más funcionales incluyen, entre otras:

- Configuración de clientes de correo y gestión del correo web y sus calendarios.

- Uso del portal educativo (LIFERAY): escritorio, comunidades, contenidos.

- Procedimientos de las funcionalidades de la Gestión de usuarios en el portal educativo.

- Creación, modificación y actualización de las páginas web de centros (asistentes, ftp, páginas dinámicas, contenidos…)

- Creación, modificación y actualización de páginas web personales del profesorado.

- Localización y acceso a Recursos Digitales en EducaMadrid.

- Gestión del Aula Virtual (Moodle), creación de cursos virtuales, desarrollo de plugins, matriculación de alumnos, calificaciones, etc.

- Gestión de la Mediateca de EducaMadrid: incorporación de vídeos, audios e imágenes de valor educativo, catalogación, creación de listas de reproducción, etc.

- Gestión de los sistemas de video llamada integrados en la Plataforma EducaMadrid.

- Información sobre los procedimientos de gestión de usuarios (altas, bajas, modificaciones, etc.) por los centros educativos.

- Uso de las demás herramientas de la Plataforma EducaMadrid.

En este sentido, se considera "Gestión de incidencias" al conjunto de servicios colaterales que la firma adjudicataria deberá realizar para garantizar el correcto funcionamiento de los aplicativos que se mencionan en el presente pliego, de acuerdo con ANS definidos, así como para proporcionar la información periódica necesaria.

## Horario de servicio

Se considera horario de servicio a la franja horaria diaria en la que la empresa contratista está en disposición tanto de recibir una comunicación como de acometer la resolución de la misma.

El contratista estará obligado a contemplar un horario de servicio mínimo que comprenderá de 8:00 h a 18:00 h de lunes a viernes.

Excepcionalmente podrán realizar trabajos extraordinarios programados fuera de ese horario y también en días no laborables para labores de configuración e instalación que no pueda llevarse a cabo en el horario ordinario.

*<!-- salto de página -->*

## Soporte continuo 24/7

Fuera del horario de servicio, podrán surgir incidencias, y las más críticas deberán solucionarse incluso fuera del horario de servicio. Se realizará pues un soporte continuado para que los diferentes proyectos funcionen **las 24 horas al día, los 7 días de la semana**. La mayoría de los proyectos tienen una dependencia importante con diversos componentes internos y externos y esto requiere un soporte adicional que entienda lo que se requiere para asegurar una interrupción mínima del proyecto.

## Dimensionamiento del servicio

El total de esfuerzo ordinario anual en las tareas de desarrollo correctivo y gestión de incidencias se estima en **10.929,8***0 horas** a cargo de los diferentes perfiles indicados en el apartado correspondiente.

## Clasificación de las incidencias

| **Categoría** | **Descripción** |
| --- | --- |
| Leve | No interrumpen el funcionamiento del sistema de información. Los usuarios finales pueden realizar el trabajo, aunque éste se ve dificultado o ralentizado. Se resuelven con un esfuerzo inferior a 1 día de todo/parte del equipo de trabajo mínimo. |
| Grave | Interrupción parcial significativa en la operatividad del sistema de información. Algunas funciones no están disponibles, pero otras sí. Algunas funciones provocan errores en los datos o los flujos de trabajo, pero son subsanables con un esfuerzo razonable. Interrumpe parcialmente el trabajo. Se resuelven con un esfuerzo de 1 a 3 días de todo/parte del equipo de trabajo mínimo. |
| Crítica | Interrupción completa de la operatividad del sistema de información; corrupción de datos importantes para los usuarios; errores en el funcionamiento o los datos difíciles o imposibles de subsanar; es imposible hacer el trabajo, o los errores son de tal naturaleza que es preferible detener la aplicación. Se resuelven con un esfuerzo de 3 días o más de todo/parte del equipo de trabajo mínimo. |

## Acuerdos de nivel de servicio

Se definen ANS correspondientes al tiempo de respuesta ante una incidencia y el tiempo de resolución de un problema.

## Tiempo de respuesta

Se considera tiempo de respuesta al que transcurre desde la comunicación al contratista, por parte de la Vicepresidencia, Consejería de Educación y Universidades, de un problema, hasta la recepción de la contestación del contratista, con la planificación de su solución.

El contratista estará obligado a contemplar un tiempo de respuesta de 2 horas computables en el horario de servicio.

## Tiempo de resolución de un problema

Se considera tiempo de resolución de un problema al que transcurre desde la comunicación al contratista, por parte de la Vicepresidencia, Consejería de Educación y Universidades del problema hasta la resolución del mismo.

La resolución de las incidencias incluirá la realización de pruebas de regresión, con el objetivo de eliminar el efecto onda, es decir, comprobar que los cambios sobre un componente de un sistema no introducen un comportamiento no deseado o errores adicionales en otros componentes no modificados.

El adjudicatario estará obligado a resolver la incidencia en un plazo máximo de tiempo de jornada laboral de lunes a viernes, fijado según el nivel de la incidencia (ver tabla), a contar desde la comunicación del problema.

| **Criticidad** | **Grado de inoperatividad del sistema** |
| --- | --- |
| Leve | Tiempo de resolución no superior a 24 horas |
| Grave | Tiempo de resolución no superior a 12 horas |
| Crítica | Tiempo de resolución no superior a 6 horas |

Cuando la resolución de la incidencia requiera la realización de desarrollos que por su naturaleza necesitan de un plazo material superior al indicado en la tabla precedente, el contratista estará obligado a presentar al Responsable del Contrato Específico en el organismo destinatario, dentro del plazo de tiempo de resolución inicial, un plan de actuación que incluya la duración prevista de los trabajos para la resolución, la justificación de dicha previsión y la descripción de los trabajos a realizar. Si es necesario, se incluirá la descripción de las medidas paliativas a adoptar hasta la completa resolución de la incidencia. Dicho plan deberá ser aprobado por el responsable del Contrato Específico.
