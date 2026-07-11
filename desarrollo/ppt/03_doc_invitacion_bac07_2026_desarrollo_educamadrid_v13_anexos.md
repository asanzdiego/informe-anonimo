# DESCRIPCIÓN DEL ENTORNO TÉCNICO Y FUNCIONAL EXISTENTE

## ARQUITECTURA SOFTWARE DE EDUCAMADRID

La Plataforma Educativa EducaMadrid (en adelante EducaMadrid) está compuesta por un ecosistema de aplicaciones desarrolladas en distintas tecnologías, con diferentes paradigmas y lenguajes usados por la Comunidad Educativa no universitaria, sostenida con fondos públicos de la Comunidad de Madrid.

La Consejería de Digitalización considera la utilización de las Tecnologías de la Información y la Comunicación como un recurso actualmente imprescindible en los procesos de enseñanza y aprendizaje.

Con esta finalidad proporciona un conjunto de servicios y herramientas a la comunidad educativa a través del portal EducaMadrid: [https://www.educa.madrid.org/](<https://www.educa.madrid.org/>). Estos servicios y herramientas ofrecen los medios necesarios para facilitar el proceso enseñanza-aprendizaje y de comunicación entre los distintos actores que intervienen en el mismo. Por este motivo es necesario dar soporte a sus usuarios y desarrollar, actualizar, evolucionar y mantener los servicios y aplicaciones educativas, herramientas de comunicación entre ellas y sus interfaces, que mantendrán un aspecto y forma de uso comunes para facilitar su uso y para que el usuario identifique todas ellas como componentes de la misma plataforma.

La arquitectura tecnológica software de EducaMadrid está constituida por más de 30 aplicaciones que ofrecen servicios a la Comunidad Educativa a través de un acceso en Cloud (Nube Privada Educativa). Estas aplicaciones deben interactuar entre sí. Algunas de ellas están basadas en adaptaciones de software existente (en su mayoría open-source) y otras se han desarrollado completamente para dar servicios concretos desde EducaMadrid. La mayoría de estas aplicaciones y servicios están en producción y necesitan un mantenimiento; otras están en fase de desarrollo y otras se solicitan en este pliego para comenzar su desarrollo.

Las más relevantes dentro de este contrato son:

- Web principal y Portal Educativo (Liferay + Desarrollo Propio)

- Aulas Virtuales (Moodle)

- Mediateca (Desarrollo Propio)

- Retransmisión en vivo por Internet (Wowza y PeerTube)

- Páginas web de centro (Wordpress)

- Otras páginas web (Wordpress Multisite)

- Servicio de correo electrónico (RoundCube + Adaptaciones Propias)

- Cloud + Edición colaborativa (NextCloud, Collabora)

- Comparti2 (Jirafeau)

- EXeLearning On-line (Adaptación Propia)

- EMPieza (Desarrollo Propio)

- Avisos centralizados (Desarrollo Propio)

- Formularios (LimeSurvey)

- Videoconferencias (Jitsi y BigBlueButton)

- Aplicación de Centros EMLab

- Recursos educativos (Desarrollo Propio)

- Desarrollos Propios WEB

- Aplicaciones de gestión y otras

- Etc.

### Web principal y Portal Educativo

Estas dos páginas web son las entradas principales a los servicios de la plataforma por lo que necesitan estar totalmente aseguradas y actualizadas y mantener una interfaz de acceso homogénea y común al resto de los aplicativos de la plataforma.

Además, este servicio también ofrece un espacio para los docentes en donde albergar sus páginas web personales, blogs, etc.

### Aulas Virtuales

La plataforma Aula Virtual de EducaMadrid está basada en el Software Libre Moodle, proporcionando los siguientes servicios:

- Aula Virtual de Centros. Los profesores pueden crear y gestionar de forma autónoma, íntegra e intuitiva cursos “on-line”. Actualmente los Centros Educativos ofertan más de 220.000 cursos a sus alumnos en esta plataforma.

- Formación Profesional a Distancia. Más de 6.500 alumnos al año de Ciclos Formativos de Grado Superior realizan cada curso escolar sus estudios en la modalidad de distancia con esta plataforma de EducaMadrid.

- Formación en línea del profesorado. Anualmente, más de 8.000 profesores al año realizan su formación permanente a través de esta Aula Virtual.

- Evaluación de alumnos de Institutos de Innovación Tecnológica. Una plataforma específica es utilizada para realizar actividades evaluativas curriculares simultáneas a los alumnos de estos institutos.

### Mediateca

Este servicio de desarrollo propio ofrece un servicio de repositorio multimedia junto con alugnas aplicaciones específicas (Construcción de vídeos interactivos, Creación de Mapas Mentales, etc…).

A través de la Mediateca, cada centro educativo y profesor de la Comunidad de Madrid tiene un espacio para subir, gestionar y compartir sus imágenes, trabajar en sus vídeos educativos, subir sus audios y dar la visibilidad deseada a sus producciones en gran variedad de formatos digitales, siempre dentro de un contexto en el que priman las medidas de seguridad de acceso y reproducción de las mismas.

El servicio cuenta con un sistema de creación automática de subtítulos basado en un modelo de Inteligencia Artificial y admite otras mejoras basadas en estos modelos de aprendizaje automático para mejorar la productividad del profesorado a la hora de publicar medios o materiales para los alumnos.

A través de la integración de la gestión de grupos de EMPieza, también se puede dar acceso a los alumnos para que suban sus propios contenidos a un espacio común gestionado y controlado por el docente.

### Retransmisión “en vivo” por Internet

Este servicio, basado tanto en Software Libre (Red5) como en software propietario (WOWZA), permite que los centros educativos dispongan de su propio canal de retransmisión en vivo (streaming).

También se dispone de una aplicación (PeerTube) que permite retransmitir eventos de interés común a todos los centros y usuarios de la plataforma.

### Wordpress

Este servicio, basado en el conocido Software Libre WordPress, ofrece a los centros la posibilidad de crear sus espacios web.

EducaMadrid ofrece este servicio además de para los centros, para otros cometidos, para lo que cuenta con un despliegue de este gestor de contenidos en modalidad Multisite.

### Correo web

A través de una arquitectura específica y basado en varias piezas de Software Libre (RoundCube y QMail), EducaMadrid pone a disposición de todos los centros educativos, así como de todos los usuarios registrados en el Portal EducaMadrid (profesores, alumnos, PAS, etc.) cuentas de correo educativas para su utilización como una herramienta más dentro de la comunidad educativa. Casi 2.000.000 de usuarios disponen de cuentas de acceso a este servicio, en el que se cuida especialmente la utilización de filtros para evitar la recepción de spam, publicidad o virus en los buzones de los usuarios.

Actualmente, la solución de correo cuenta con una solución de AntiSpam dependiente del departamento de Ciberseguridad que ofrece una protección adicional garantizando la limpieza tanto del correo entrante como del saliente.

En el curso 23/24 se gestionaron en la plataforma de correo electrónico más de 250 millones de mensajes.

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

Esta Adaptación Propia del Software Libre EXeLearning, proporciona un entorno para crear recursos educativos abiertos (REAs) integrado con las propias Aulas Virtuales, pudiendo crear, editar y publicar los trabajos en una misma ubicación.

### EMPieza

Este servicio, de desarrollo propio proporciona a los profesores la capacidad de organizar y automatizar tareas repetitivas en otras aplicaciones de EducaMadrid con sus alumnos, como la creación de grupos de alumnos y profesores en los centros y su propagación a otros aplicativos, la compartición de calendarios, las retransmisiones en directo y otras funcionalidades.

### Avisos centralizados

Este servicio, de desarrollo propio proporciona la capacidad de dar avisos importantes sobre los servicios de EducaMadrid a sus usuarios.

### Formularios

Este servicio, basado en código de fuentes abiertas (LimeSurvey), proporciona la capacidad de poder crear formularios para la recogida de datos por parte de la comunidad educativa.

### Videoconferencias

Este servicio, basado en códigos de fuentes abiertas (Jitsi y BigBlueButton) proporciona a los docentes la posibilidad de retransmitir a través de Internet las clases a sus alumnos cuando estos no pueden acudir a sus centros educativos y a los equipos docentes a llevar a cabo reuniones telemáticas.

### Aplicación de Centros EMLab

Este servicio pretende valorar y promocionar el uso de los servicios de EducaMadrid, ofreciendo a los centros la posibilidad de certificar su uso y obteniendo por ello ventajas en el uso de los servicios de la plataforma.

### Entornos para proporcionar recursos y herramientas educativas

La Plataforma Educativa EducaMadrid proporciona también a los profesores y alumnos varios entornos con recursos y herramientas online:

- Animalandia: Arquitectura con recursos (imágenes y sonidos) sobre la biodiversidad animal que pueden ser libremente utilizados.

- Wiris: Herramienta para la ejercitación de conceptos matemáticos.

- Albor: Sistema experto como asistente en la toma de decisiones sobre adaptaciones de acceso al ordenador en alumnos con necesidades educativas especiales.

- EducaSAAC: Repositorio virtual interactivo de contenidos visuales orientados a centros educativos de Educación Especial, Infantil y Primaria.

### Aplicaciones de gestión y otras tareas

La Plataforma EducaMadrid proporciona otros servicios online relacionados con la gestión de ciertos procesos en las Direcciones Generales, DATs, CTIFs, etc., como, por ejemplo:

- Seguimiento: Aplicación para la gestión y seguimiento de las dotaciones de equipamientos informáticos a los centros.

- Dotaciones TIC: Aplicación para la gestión de las incidencias de los equipos informáticos de los centros.

Por otro lado, la plataforma cuenta con un conjunto de aplicaciones internas que permiten gestionar los datos de la misma, entre las que destacan Mamood, Redmine, Mattermost, GitLab, el SSO (gestión de login) basado en KeyCloack, etc.

## Arquitectura Hardware de EducaMadrid

La arquitectura hardware de la Plataforma Educativa EducaMadrid está constituida por unos 700 servidores físicos y virtuales, con un crecimiento estimado en torno al 15% anual. Además, tenemos 6 grupos de almacenamiento consolidado, distribuidos en una capa de Frontend y otra de Backend. Los servicios se encuentran clusterizados y se distribuyen del siguiente modo, aunque pueden ampliarse:

- Virtualización Principal HP Synergy – RHEV: 20 nodos, 19 de ellos repartidos en 2 frames y un nodo adicional separado para IA.

- Virtualización Secundaria HP Synergy – RHEV: 5 nodos en 1 frame.

- Virtualización Secundaria HP C7000 - RHEV 5 nodos en 1 frame.

- Cabinas de almacenamiento HP, Netapp, EMC Unity y 3 Infinidat.

- 3.500 BBDD aproximadamente (PostgreSQL, Mysql, MariaDB y MongoDB)

- Servidores virtualizados 650 aprox. (RedHat, OpenSuse, Ubuntu, Debian y Windows Server)

Existen varias instancias de cada uno de los servicios en distintos entornos, contando con entornos de desarrollo, testeo, preproducción y producción.

*<!-- salto de página -->*

# DEFINICIÓN Y ALCANCE DE LOS TRABAJOS

Debido a su naturaleza, las tareas relativas al mantenimiento evolutivo y adaptativo de los sistemas y aplicaciones relativas a los proyectos de Desarrollo suponen una gran carga de trabajo.

## DESCRIPCIÓN DEL SERVICIO DE MANTENIMIENTO Y ACTUALIZACIÓN PARA ASEGURAMIENTO DE LA CONTINUIDAD DEL SERVICIO DE LOS SISTEMAS EN ENTORNOS PRODUCTIVOS.

Alcance

El servicio de mantenimiento para el aseguramiento de la continuidad del servicio de los sistemas en entornos productivos cubrirá el conjunto de los sistemas de información y el entorno tecnológico descritos en el Anexo I. El servicio consiste en la corrección del código fuente o de la documentación para resolver o paliar las incidencias que afecten a los citados sistemas de información, así como todas las tareas conexas necesarias para poder realizar dicha corrección.

### MEJORAS Y MANTENIMIENTOS TRANSVERSALES (TRA)

A continuación, se detallan las tareas genéricas comunes a numerosos aplicativos que integran la plataforma educativa EducaMadrid. Estas tareas son cruciales para asegurar la seguridad, estabilidad y accesibilidad de todos los servicios y aplicativos de la plataforma. Todos los servicios y aplicativos requieren un mantenimiento evolutivo que garantice estos aspectos.

Las siguientes tareas son aplicables a todos los servicios enumerados en este Pliego. Dado que se realizan auditorías de seguridad periódicas, es imperativo abordar de manera diligente los problemas detectados. Esta diligencia generalmente se traduce en la implementación de cambios específicos.

- Actualizaciones de Seguridad:

    - Aplicar parches de seguridad.

    - Actualización del “core” base en el que se basa el aplicativo (por ejemplo, WordPress).

    - Actualizar “plugins” usados a versiones compatibles con el nuevo core.

    - Actualizar los “temas/interfaces” usados a versiones compatibles con el nuevo core.

- Actualización de Frameworks y Software de Desarrollo:

    - Actualizar frameworks y versiones de software usados para el desarrollo.

- Mantenimiento de espacios de centro y cuentas de usuario:

    - Se realizarán tareas de cambios de ids de centros o usuarios propagando los cambios a cada servicio.

    - Se realizarán tareas de altas y bajas de cuentas de centros y usuarios en los servicios de la plataforma.

- Cambios en Contraseñas de Acceso:

    - Actualización periódica de contraseñas de acceso entre servicios o a bases de datos.

Estos tipos de cambios exigen:

- Adecuación del código desarrollado por EducaMadrid.

- Revisión de los nuevos interfaces incorporados.

- Testeo de rendimiento de la nueva versión a implantar.

- Testeo unitario de los servicios afectados.

- Actualización de la configuración de los aplicativos.

- Adaptación a la Imagen Institucional:

    - Es relativamente frecuente que cada cierto tiempo se produzcan cambios relacionados con la modernización de la imagen institucional o con la adscripción del proyecto a una consejería determinada. Todos los aplicativos deben adaptar su interfaz a la imagen institucional de EducaMadrid de cada momento: logotipos, enlaces, pie de página, buscador de servicios.

- Accesibilidad:

    - La inclusión de cambios en las interfaces de los aplicativos para mejorar el acceso a los usuarios con distintas capacidades es una tarea transversal que debe ser llevada a cabo, garantizando la accesibilidad a la plataforma.

- Propuestas de Mejora:

    - También se solicitará que se presenten propuestas de aplicativos, plugins o funcionalidades que se requieran con el objetivo de su implantación en el futuro.

### Borrado y cambios de los IDs de usuario (TRA1)

Implementación de un sistema que permita sincronizar cambios en los usuarios provenientes de raíces o el portal educativo con los servicios en la plataforma online, garantizando que los cambios en la información de los usuarios se propaguen de manera automática a todos los servicios.

**Requisitos**

- Sincronización de usuarios con el aplicativo central:

    - El sistema debe poder leer la base de datos del aplicativo central y sincronizar la información de los usuarios con la plataforma online.

    - Debe ser capaz de detectar cambios en la información de los usuarios, incluyendo la baja de un usuario.

- Propagación de cambios a los servicios:

    - El sistema debe poder propagar los cambios en la información de los usuarios a todos los servicios en la plataforma online, incluyendo:

    - Correoweb

    - Aulas virtuales

    - Páginas de centros

    - Formularios

    - Mediateca

    - Empieza

    - Otros

    - Debe ser capaz de propagar los cambios en tiempo real

- Seguridad y autenticación:

    - El sistema debe utilizar métodos seguros para propagar los cambios e impedir que usuarios no autorizados inicien el sistema.

    - Debe ser capaz de cifrar la información de los usuarios para protegerla contra accesos no autorizados.

- Monitorización y reportes:

    - El sistema debe proporcionar monitorización y reportes para garantizar que los cambios se están propagando correctamente a los servicios.

    - Debe ser capaz de generar reportes de errores y excepciones para facilitar la depuración y resolución de problemas.

**Requisitos técnicos**

- Lenguaje de programación:

    - El sistema debe ser implementado en un lenguaje de programación moderno y robusto.

- Bases de datos:

    - El sistema debe utilizar una base de datos relacional como MySQL o PostgreSQL para almacenar la información de los usuarios.

- Cambios en aplicativos:

    - No deben producirse cambios en el core de los aplicativos

- APIs y conectores:

    - El sistema debe utilizar APIs y conectores para interactuar con el aplicativo central y los servicios en la plataforma online.

### Cambios de nombre de centro (TRA2)

Desarrollar un sistema que permita cambiar el nombre de un centro dentro de la plataforma EducaMadrid y propagar este cambio a todos los aplicativos asociados. El cambio de nombre debe incluir la actualización de todas las cuentas institucionales asociadas y, en algunos casos, la modificación de URLs de servicios.

**Requisitos Funcionales**

- Cambio de Nombre del Centro:

    - El sistema debe permitir cambiar el nombre del centro en todos los aplicativos asociados.

    - El cambio de nombre debe propagarse automáticamente a todos los aplicativos sin intervención manual.

- Actualización de Cuentas Institucionales:

    - Todas las cuentas institucionales asociadas al centro deben actualizarse con el nuevo nombre.

    - La información existente en las cuentas (contactos de correo electrónico, ficheros en el cloud, grupos de empieza, etc.) debe mantenerse intacta y asociada a las nuevas cuentas.

- Modificación de URLs:

    - En algunos aplicativos (por ejemplo, aulas virtuales o WordPress), el cambio de nombre del centro puede implicar la modificación de la URL del servicio.

    - El sistema debe gestionar estas modificaciones de URL de manera segura y eficiente.

- Seguridad en Comunicaciones:

    - Las comunicaciones entre los aplicativos para iniciar el cambio de nombre deben ser seguras.

    - Implementar medidas de seguridad como cifrado de datos y autenticación robusta.

- Autonomía de los Aplicativos:

    - Cada aplicativo debe realizar las modificaciones necesarias de manera autónoma.

    - Las modificaciones específicas en cada aplicativo deben ser gestionadas de manera independiente.

**Requisitos No Funcionales**

- Rendimiento:

    - El sistema debe ser capaz de realizar el cambio de nombre y propagarlo a todos los aplicativos en un tiempo razonable.

- Escalabilidad:

    - El sistema debe ser escalable para manejar un gran número de centros y aplicativos.

- Seguridad:

    - Implementar medidas de seguridad robustas para proteger los datos durante el proceso de cambio de nombre.

- Mantenimiento:

    - El sistema debe ser fácil de mantener y actualizar.

**Requisitos Técnicos**

- Tecnologías

    - Lenguaje de Programación: depende de cada aplicativo.

    - Framework: depende de cada aplicativo.

    - Base de Datos: depende de cada aplicativo.

    - Seguridad: Implementación de medidas de seguridad como HTTPS, cifrado de datos, autenticación y autorización robustas.

- Integración

    - Aplicativos: Integración con los siguientes aplicativos para propagar el cambio de nombre:

        - Aulas Virtuales

        - Cloud

        - Mediateca

        - Formularios

        - DTIC

        - Empieza

        - Seguimientos

        - WordPress

        - Otros

<!-- salto de página -->

- Comunicación Segura

    - Cifrado de Datos: Implementación de cifrado de datos en todas las comunicaciones entre los aplicativos.

    - Autenticación: Implementación de mecanismos de autenticación robustos para asegurar que solo los usuarios autorizados puedan iniciar el cambio de nombre.

- Proceso de Cambio de Nombre

    - Iniciación del Cambio:

        - El administrador inicia el cambio de nombre del centro a través del portal educativo.

        - El sistema verifica la autenticidad del administrador y la validez del cambio de nombre.

    - Propagación del Cambio:

        - El sistema envía una solicitud segura a todos los aplicativos asociados para propagar el cambio de nombre.

        - Cada aplicativo realiza las modificaciones necesarias de manera autónoma.

    - Verificación del Cambio:

        - El sistema verifica que el cambio de nombre se ha propagado correctamente a todos los aplicativos.

        - En caso de errores, el sistema notifica al administrador y proporciona detalles sobre los problemas encontrados.

### Tareas tras el traslado del CPD (TRA3)

Estas tareas se derivan del proyecto de traslado del CPD previsto para el verano de 2026.

- Dar cobertura para facilitar un arranque y ejecución de manera segura y eficiente de todos los servicios tras el traslado, incluyendo comprobaciones posteriores para asegurar el servicio una vez que empiece el curso.

- Garantizar que, tras el traslado, no haya afectación en el funcionamiento de los servicios de la plataforma.

- Proporcionar información y soporte a los usuarios durante y después del traslado.

- Identificar y corregir cualquier problema o incompatibilidad que se encuentre como consecuencia del traslado.

- Apoyar y asesorar al equipo de sistemas en sus tareas.

- Realizar paradas y arranques controlados de distintos servicios.

Para verificar los sistemas tras el traslado, es necesario que haya un script (Shell script) que verifique el estado de las máquinas de cada servicio después de trasladar cada servidor físicamente de CPD y que permita comparar los resultados con los datos tomados antes del traslado. El script debe verificar una serie de elementos críticos para asegurarse de que el servidor esté funcionando correctamente.

**Requisitos del Script**

- Verificación de volúmenes montados

    - El script debe verificar que todos los volúmenes montados estén funcionando correctamente

    - El script debe verificar que los volúmenes estén montados en el lugar correcto.

- Verificación de conexión a las bases de datos

    - El script debe verificar que las conexiones a las bases de datos estén funcionando correctamente.

    - El script debe verificar que los datos de las bases de datos estén intactos.

- Verificación de integridad de las bases de datos

    - El script debe verificar que las bases de datos estén intactas y no hayan sufrido daños durante la migración.

    - El script debe verificar que los datos de las bases de datos estén consistentes.

- Verificación de integridad del código de los distintos aplicativos

    - El script debe verificar que el código de cada aplicativo esté intacto y no haya sufrido daños durante la migración.

    - El script debe verificar que el código esté actualizado y no haya errores.

- Verificación de paquetes del sistema

    - El script debe verificar que los paquetes del sistema estén actualizados y no haya errores.

    - El script debe verificar que los paquetes estén instalados correctamente.

- Verificación de funcionamiento de los aplicativos

    - El script debe verificar que los aplicativos estén funcionando correctamente.

    - El script debe verificar que los usuarios puedan acceder a los distintos aplicativos sin problemas.

- Verificación de conexiones a máquinas de otros servicios

    - El script debe verificar que las conexiones a máquinas de otros servicios estén funcionando correctamente por los puertos que les corresponden según cada aplicativo.

    - El script debe verificar que los datos de los servicios estén intactos.

- Verificación del funcionamiento del cron

    - El script debe verificar que el cron de cada aplicativo esté funcionando correctamente.

    - El script debe verificar que las tareas del cron estén completándose correctamente.

- Verificación de otros elementos

    - El script debe verificar que otros elementos críticos estén funcionando correctamente, como:

        - Servidores de correo electrónico

        - Servidores de DNS

        - Servidores de LDAP

        - Servidores de conversión

        - Servidores de generación de subtítulos

        - Servidores de IA

        - otros

**Requisitos**

- Tecnologías utilizadas

    - El script deberá basarse en un lenguaje de Shell Scripting como Bash.

    - El script debe utilizar herramientas de verificación como df, ls, ps, netstat, etc.

- Documentación

    - El script debe incluir documentación para explicar cómo funciona y qué elementos verifica.

    - La documentación debe estar escrita en un lenguaje claro y conciso.

### Adaptación de interfaz para compatibilizar modo oscuro y claro (TRA4)

Mantener los estilos de todos los aplicativos de la plataforma y aplicar la opción de un modo oscuro en cada uno de ellos, incluyendo la barra común superior.

**Objetivos**

- Mantenimiento de los estilos y solución a problemas de accesibilidad, incluso tras evoluciones de aplicativos.

- Implementar un modo oscuro en todos los aplicativos.

- Asegurar una experiencia de usuario coherente y estéticamente agradable en modo oscuro.

**Alcance**

- Análisis de los estilos actuales.

- Diseño de la interfaz de usuario en modo oscuro.

- Implementación del modo oscuro en todos los aplicativos bajo opción.

- Ajustes en la barra común superior.

**Requisitos Funcionales**

- Modo Oscuro

    - Interfaz de Usuario: Diseño legible y estéticamente agradable.

    - Contraste: Adecuado entre texto y fondo.

    - Elementos de Interfaz: Adaptación de botones, iconos, etc.

    - Transiciones Suaves: Cambio entre modos claro y oscuro.

- Aplicativos

    - Aulas Virtuales, Mediateca, WordPress, DTIC, Cloud, Empieza, Videoconferencias y otros: Aplicar modo oscuro a todas las vistas y componentes.

- Barra Común Superior

    - Estilos: Adaptación al modo oscuro.

    - Iconos y Texto: Ajuste para legibilidad.

    - Funcionalidad: Accesibilidad y funcionalidad mantenidas.

**Requisitos No Funcionales**

- Usabilidad

    - Experiencia de Usuario: Intuitiva y agradable.

    - Accesibilidad: Cumplimiento con WCAG.

- Rendimiento

    - Tiempo de Carga: Minimizar impacto.

    - Optimización: Recursos optimizados.

<!-- salto de página -->

### Mejoras y mantenimiento en SSO (TRA5)

##### Integración del SSO

Integración del sistema de Single Sign-On (SSO) en distintos aplicativos de la plataforma, así como la creación de un sistema de detección de cierre de sesión en el aplicativo "Avisos".

**Requisitos**

- Integración del SSO

    - Autenticación: Los aplicativos deben utilizar el sistema SSO existente para la autenticación de usuarios.

    - Redirección: Al intentar acceder a un aplicativo, el usuario debe ser redirigido al sistema SSO para la autenticación.

    - Tokens: Utilizar tokens de acceso (JWT) para mantener la sesión del usuario en los aplicativos integrados.

    - Seguridad: Implementar medidas de seguridad adicionales, como cifrado de datos y protección contra ataques CSRF.

- Detección de Cierre de Sesión en el Aplicativo "Avisos"

    - Detección de Sesión: Crear un sistema dentro del aplicativo "Avisos" que pueda ser llamado desde otros aplicativos para detectar si el usuario ha cerrado sesión en el SSO.

    - Cierre de Sesión: Si se detecta que el usuario ha cerrado sesión en el SSO, el sistema debe provocar el cierre de sesión en el aplicativo en el que se encuentre el usuario y redirigir al usuario a la página de inicio de sesión del SSO.

**Procedimiento de Solicitud**

Las solicitudes de integración del SSO en nuevos aplicativos se harán en función de las necesidades del servicio.

**Pruebas y Validación**

- Se realizarán pruebas exhaustivas para asegurar que la integración del SSO funcione correctamente en todos los aplicativos solicitados.

- Se validará el mecanismo de detección de cierre de sesión del aplicativo "Avisos" para asegurar que el usuario sea redirigido correctamente al cerrar sesión en el SSO.

##### Doble factor de autenticación (2FA)

Implementar un sistema de doble factor de autenticación (2FA) en los distintos aplicativos de la plataforma conectados con el SSO y en el correoweb, que no se encuentra conectado al SSO. El sistema debe funcionar con dispositivos móviles y/o correo electrónico y será optativo para los usuarios.

**Requisitos Técnicos**

- Implementación en SSO y correoweb

    - El sistema de 2FA debe ser implementado tanto en el SSO como en aplicativo de correo.

- Métodos de Autenticación

    - El sistema debe permitir 2FA mediante TOTP (Time-Based One-Time Password) o cuentas de correo externas a EducaMadrid.

- Configuración de TOTP

    - La configuración de TOTP se realizará en el SSO.

    - La misma configuración de TOTP debe permitir el acceso tanto al correo como al SSO.

- Formulario de Gestión de 2FA

    - La aplicación "Empieza" será la encargada de mostrar un formulario de gestión de 2FA a los usuarios.

    - El formulario debe permitir a los usuarios seleccionar si desean 2FA por TOTP (y correo electrónico), correo electrónico o ninguno.

    - El formulario debe permitir seleccionar la cuenta de correo alternativa tras confirmarla con un correo de verificación.

    - Ante cambios de configuración de 2FA, el sistema debe solicitar confirmación con 2FA.

    - Las opciones de configuración de 2FA se mostrarán solamente a los centros indicados y a los roles de usuario que se deseen.

- Gestión de 2FA por Cuentas Institucionales

    - La aplicación "Empieza" también permitirá a las cuentas institucionales gestionar el 2FA de los usuarios de sus centros.

- Gestión de 2FA por Administradores

    - La aplicación "ConsultasLDAP" permitirá a los administradores gestionar el 2FA de cualquier usuario de la plataforma.

- Flujo de Navegación durante el Login con 2FA

    - El flujo de navegación durante el login con 2FA en el SSO y en el correo debe ser igual.

**Consideraciones Adicionales**

- Seguridad: Asegurar que el sistema de 2FA cumpla con las mejores prácticas de seguridad para proteger la información de los usuarios.

- Usabilidad: Diseñar la interfaz de usuario de manera que sea intuitiva y fácil de usar para los usuarios finales.

- Compatibilidad: Garantizar que el sistema de 2FA sea compatible con los dispositivos móviles y correos electrónicos más comunes.

- Documentación: Proveer documentación detallada para la configuración y uso del sistema de 2FA.

### Aplicativo API (TRA6)

Desarrollo del aplicativo "API", cuyo objetivo es gestionar y servir APIs de manera segura y eficiente. El aplicativo se desarrollará utilizando el mismo framework que EducaMadrid está implantando y se centrará en la seguridad, accesibilidad y funcionalidad.

**<!-- salto de página -->**

**Requisitos Generales**

- Framework de Desarrollo

    - El aplicativo se desarrollará utilizando el mismo framework que se utiliza en EducaMadrid en sus nuevos aplicativos.

- Seguridad

    - La seguridad del aplicativo y de las APIs que sirve es de suma importancia. Se deben implementar medidas de seguridad robustas para proteger tanto el aplicativo como las APIs servidas.

- Acceso

    - El acceso al aplicativo estará restringido a administradores a través de LDAP ADM.

**Requisitos Funcionales**

- **Documentación de APIs.** El aplicativo permitirá alimentar y gestionar la documentación de todas las APIs de la plataforma, independientemente de si están alojadas en el aplicativo o no. La documentación debe incluir los siguientes datos:

    - Servicio al que pertenece la API.

    - URL de la API.

    - API pública / privada

    - Tipo de API (REST, SOAP, etc.).

    - Parámetros recibidos.

    - Posibles respuestas.

    - Ejemplos de uso.

- Alojamiento de APIs

    - El aplicativo debe permitir servir APIs directamente desde el mismo. Las APIs desarrolladas deben ser independientes del aplicativo y se debe garantizar su seguridad. Las APIs podrán estar en frontend o backend según la necesidad y la seguridad de los datos manejados.

**Requisitos de Acceso y Gestión**

- Gestión de Accesos

    - El aplicativo debe gestionar accesos a distintas bases de datos y servicios. Se deben implementar mecanismos de autenticación y autorización robustos para asegurar que solo los usuarios autorizados puedan acceder a los recursos necesarios.

- Parte de Documentación

    - La parte de documentación del aplicativo puede estar en backend y no ser accesible desde internet. Esto garantiza que la documentación sensible no esté expuesta a posibles amenazas externas.

**<!-- salto de página -->**

**Requisitos Técnicos**

- Tecnologías

    - Framework: El mismo utilizado en EducaMadrid.

    - Lenguaje de Programación: PHP

    - Base de Datos: MySQL

    - Autenticación: LDAP ADM.

    - Seguridad: Implementación de medidas de seguridad como HTTPS, autenticación y autorización robustas, y protección contra ataques comunes (inyección SQL, XSS, CSRF, etc.).

- Integración

    - LDAP ADM: Integración con LDAP ADM para la autenticación de administradores.

    - Bases de Datos y Servicios: Gestión de accesos a distintas bases de datos y servicios externos.

    - Drupal: debe proporcionarse una API para consulta de datos de usuarios desde el aplicativo de innovación y formación.

### Securización LDAP Plano, BBDD PostgreSQL y MySQL (TRA7)

Implementación de medidas de seguridad adicionales y la optimización de la Base de Datos "ldap plano". Además, se requiere un cambio de usuarios en todas las bases de datos PostgreSQL y MySQL de la plataforma, así como la actualización de datos en la configuración de cada aplicativo.

**Objetivos**

- Implementar medidas de seguridad adicionales en la Base de Datos "ldap plano".

- Optimizar el rendimiento de la Base de Datos "ldap plano".

- Cambiar los usuarios y contraseñas de todas las bases de datos PostgreSQL y MySQL de manera periódica.

- Actualizar la configuración de cada aplicativo con los nuevos datos de usuario.

**Alcance**

- Análisis y evaluación de la seguridad actual de la Base de Datos "ldap plano".

- Implementación de medidas de seguridad adicionales.

- Optimización del rendimiento de la Base de Datos "ldap plano".

- Cambio de usuarios en todas las bases de datos PostgreSQL y MySQL.

- Actualización de la configuración de cada aplicativo con los nuevos datos de usuario.

### Calendario escolar (TRA8)

Creación y gestión de dos calendarios en la cuenta institucional de cada centro educativo: "Calendario Escolar" y "Calendario de Centro". Estos calendarios deben cumplir con ciertos criterios de acceso, alimentación de eventos y sincronización para asegurar una gestión eficiente y sin duplicados de eventos.

**<!-- salto de página -->**

**Objetivos**

- Crear un calendario llamado "Calendario Escolar" en la cuenta institucional de cada centro, alimentado de eventos por los administradores de EducaMadrid.

- Crear un calendario llamado "Calendario de Centro" en la cuenta institucional de cada centro, alimentado por el centro y disponible en modo solo lectura para todas las cuentas de profesores y alumnos.

- Asegurar que la sincronización de calendarios entre las aulas virtuales y las cuentas de los centros no duplique los eventos.

**Alcance**

- Creación de los calendarios "Calendario Escolar" y "Calendario de Centro" en cada cuenta institucional de centro.

- Configuración de permisos de acceso y alimentación para cada calendario.

- Implementación de mecanismos de sincronización que eviten la duplicación de eventos.

**Requisitos Técnicos**

- Calendario Escolar

    - Nombre del Calendario: "Calendario Escolar"

    - Permisos de Acceso: Solo lectura para todas las cuentas institucionales.

    - Alimentación: Realizada por los administradores de EducaMadrid con los eventos del calendario escolar oficial publicado por la Comunidad de Madrid.

    - No Eliminable: El calendario no podrá ser eliminado por las cuentas institucionales.

- Calendario de Centro

    - Nombre del Calendario: "Calendario de Centro"

    - Permisos de Acceso: Solo lectura para todas las cuentas de profesores y alumnos del centro.

    - Alimentación: Realizada por el centro educativo.

    - No Eliminable: El calendario no podrá ser eliminado por los usuarios del centro ni la cuenta institucional.

- Sincronización de Calendarios

    - Mecanismo de Sincronización: Implementar un mecanismo de sincronización que asegure que los eventos no se dupliquen entre las aulas virtuales y las cuentas de los centros.

    - Actualización en Tiempo Real: Asegurar que los eventos se actualicen en tiempo real en todos los calendarios sincronizados.

    - Gestión de Conflictos: Implementar una gestión de conflictos para resolver cualquier duplicación o inconsistencia que pueda surgir durante la sincronización.

### MEJORAS Y MANTENIMIENTO DE LAS AULAS VIRTUALES (AV)

Subida anual de versión del aplicativo Moodle con todos sus temas y plugins a la versión segura más adecuada que publique el desarrollador tanto en los entornos multisite como moodlemisc. Todos los puntos siguientes deben aplicarse tanto al core del aplicativo como a los temas y plugins de ambas plataformas.

### Actualización de la Plataforma Moodle (AV1)

- Realizar la actualización de manera segura y sin interrupciones en el servicio: Se deberá realizar la actualización de manera planificada, utilizando un script de actualización que se ejecute fuera de horas pico. Se recomienda realizar una copia de seguridad de la base de datos y los archivos de configuración antes de realizar la actualización.

### Actualización de PHP y sistema operativo (AV2)

- Actualizar la versión de PHP: Se deberá actualizar la versión de PHP a una versión segura y compatible con la plataforma y versión de Moodle utilizada. Esto incluye la actualización de los archivos de código y la configuración de PHP. Se recomienda utilizar la versión más reciente de PHP compatible con la plataforma.

- Evaluar la necesidad de subir la versión del sistema operativo: Se deberá evaluar la necesidad de subir la versión del sistema operativo para asegurarse de que esté compatible con la versión actualizada de PHP. Esto incluye la actualización de los archivos de configuración y la base de datos.

- Crear nuevos servidores completos si es necesario: Se deberá crear nuevos servidores completos si es necesario para asegurarse de que la plataforma esté disponible y accesible para los usuarios.

### Actualización de aplicativo y complementos (AV3)

- Actualizar la versión de Moodle y todos sus complementos y temas: Se deberá actualizar la versión de Moodle y todos sus complementos y temas a versiones actuales. Esto incluye la actualización de los archivos de código, la base de datos y los archivos de configuración.

- Mantener todas las funcionalidades y modificaciones ya implementadas: Se deberá mantener todas las funcionalidades y modificaciones ya implementadas en la plataforma, asegurándose de que no se pierdan durante la actualización.

- Realizar la actualización de manera segura y sin interrupciones en el servicio: Se deberá realizar la actualización de manera planificada, utilizando un script de actualización que se ejecute fuera de horas pico. Se recomienda realizar una copia de seguridad de la base de datos y los archivos de configuración antes de realizar la actualización.

### Mejoras de seguridad y rendimiento (AV4)

- Activar el antivirus ClamAV: Se deberá activar el antivirus ClamAV para proteger la plataforma contra virus y malware.

- Modificar la presentación del proceso de análisis durante la subida de archivos: Se deberá modificar la presentación del proceso de análisis durante la subida de archivos para informar al usuario que se realizará un análisis en busca de virus.

- Mejorar la seguridad para evitar la inserción de SCRIPTS en campos de tipo texto o TEXTAREA: Se deberá mejorar la seguridad para evitar la inserción de SCRIPTS en campos de tipo texto o TEXTAREA, utilizando técnicas de validación y limpieza de datos.

- Corregir problemas con el banco de preguntas: se deberá aportar una solución al actual problema de volumen en el banco de preguntas y realizar las adaptaciones necesarias para poder actualizar a la futura versión 5 con el nuevo formato de banco de preguntas.

- Implementar un sistema de coloreado de sintaxis para los principales lenguajes de programación: Se deberá implementar un sistema de coloreado de sintaxis para los principales lenguajes de programación, utilizando técnicas de procesamiento de texto y renderizado de código.

### Integración con otros sistemas (AV5)

- Establecer conexión SAML con el aplicativo nube: Se deberá establecer una conexión SAML con la nube de EducaMadrid para permitir la autenticación de usuarios y la integración de servicios.

- Establecer conexión WebAuth entre el aplicativo nube y las aulas virtuales: Se deberá establecer una conexión WebAuth entre la nube de EducaMadrid y las aulas virtuales moodlemisc y multisite para permitir la autenticación de usuarios y la integración de servicios.

- Integrar el Aula Virtual con Avisos: Se deberá integrar el Aula Virtual con el aplicativo Avisos para permitir la notificación de eventos y la integración de servicios.

- Integrar el Aula Virtual con Raíces y el Portal educativo: Se deberá integrar el Aula Virtual con Raíces y el Portal educativo para permitir la generación automática de cohortes y la inserción de alumnos y profesores en las aulas que les correspondan.

### Mejoras de interfaz y usuario (AV6)

- Mejorar la vista del libro de calificaciones en resoluciones bajas: Se deberá mejorar la vista del libro de calificaciones en resoluciones bajas, utilizando técnicas de diseño y renderizado de texto.

- Permitir el desplazamiento horizontal de la tabla en el libro de calificaciones: Se deberá permitir el desplazamiento horizontal de la tabla en el libro de calificaciones, utilizando técnicas de diseño y renderizado de texto.

- Crear un modo examen para utilizar con el navegador "Safe Exam Browser": Se deberá crear un modo examen para utilizar con el navegador "Safe Exam Browser", utilizando técnicas de diseño y renderizado de texto.

### Desarrollo y pruebas (AV7)

- Desarrollar un mecanismo para propagar cambios en la lista de centros que pueden usar la app de Aula Virtual para dispositivos móviles: Se deberá desarrollar un mecanismo para propagar cambios en la lista de centros que pueden usar la app de Aula Virtual para dispositivos móviles, utilizando técnicas de desarrollo y pruebas de software.

### Mantenimiento y soporte (AV8)

- Mantener la recogida de datos estadísticos: Se deberá mantener la recogida de datos estadísticos para permitir la evaluación de la plataforma y la identificación de áreas de mejora.

- Realizar la generación y eliminación de instalaciones de Aulas Virtuales Multisite: Se deberá realizar la generación y eliminación de instalaciones de Aulas Virtuales Multisite para permitir la actualización de la plataforma y la eliminación de instalaciones obsoletas.

- Cambiar la URL de las Aulas Virtuales: Se deberá crear un sistema que perminta automatizar un cambio de URL de las Aulas Virtuales para afrontar cambios de nombres de centros. El sistema debe cambiar URL, cuentas administradoras, nombre del aula, etc.

- Tareas anuales de inicio de curso: cada curso escolar debe realizarse una serie de tareas de mantenimiento y limpieza de la plataforma de cara al nuevo curso: backup de todos los cursos del año anterior (debe estar disponible para los usuarios), reinicio de cursos…

### Otros (AV9)

- Actualizar los scripts de instalación paulatina por "islas" de nuevos plugins o actualizaciones de los mismos: Se deberá actualizar los scripts de instalación paulatina por "islas" de nuevos plugins o actualizaciones de core.

- Actualizar los scripts de AV para que permitan un paso en producción programado de madrugada de cambios en el tema de Moodle, limpiando caches: Se deberá actualizar los scripts de AV para que permitan un paso en producción programado de madrugada de cambios en el tema de Moodle, limpiando caches.

### Plugin eXeLearning 3 (AV10)

Adaptar el plugin de Exelearning para Moodle para que se ajuste a las necesidades actuales del sistema. El objetivo de esta adaptación es asegurar la compatibilidad con la versión 3 de Exelearning y garantizar la seguridad y estabilidad del sistema.

**Requisitos Funcionales**

- Compatibilidad con Exelearning 3

    - El plugin debe ser compatible con la versión 3 de Exelearning.

    - El plugin debe poder comunicarse con la versión 3 de Exelearning sin problemas.

- Funcionamiento con protocolos seguros

    - El plugin debe utilizar protocolos seguros para comunicarse con Exelearning, como HTTPS.

    - El plugin debe poder cifrar y descifrar la información de manera segura.

- Compatibilidad con instalaciones de Exelearning en servidores propios

    - El plugin debe ser compatible con instalaciones de Exelearning en servidores propios.

    - El plugin debe poder comunicarse con la instalación de Exelearning en el servidor propio sin problemas.

**Requisitos de Seguridad**

- Cuidado con problemas de conectividad

    - El plugin debe ser capaz de detectar y manejar problemas de conectividad con Exelearning.

    - El plugin debe poder recuperarse de errores de conectividad y continuar funcionando sin problemas.

**<!-- salto de página -->**

**Requisitos de Desarrollo**

- Uso de tecnologías actuales

    - El plugin debe utilizar tecnologías actuales y seguras, como PHP 8

    - El plugin debe ser capaz de aprovechar las funcionalidades de las tecnologías actuales.

- Documentación y soporte

    - El plugin debe tener documentación clara y completa sobre su funcionamiento y configuración.

    - El plugin debe tener soporte técnico disponible para resolver problemas y preguntas.

### IA en Moodle

##### Generador de preguntas (AV11)

Se solicita la creación de un plugin para Moodle para la generación de preguntas de tipo opción múltiple con inteligencia artificial. Debe cumplir los siguientes requisitos:

- Icono característico de IA

    - El plugin debe mostrar un icono característico de IA en las preguntas generadas para indicar que fueron creadas con inteligencia artificial indicando el modelo utilizado.

- Estructura de la pregunta

    - Las preguntas deben tener la siguiente estructura:

    - Un encabezado con el texto de la pregunta.

    - 4 opciones de respuesta (A, B, C y D) con un texto para cada una.

    - Solo una de las opciones debe ser correcta.

- Funcionalidad con VLLM y modelo de EducaMadrid

    - El plugin debe funcionar con una instalación de VLLM en servidores propios de EducaMadrid.

    - El modelo de VLLM debe ser elegido por EducaMadrid y configurado en el plugin, pudiendo cambiarse si fuera necesario.

- Seguridad

    - El plugin debe funcionar utilizando protocolos seguros (HTTPS) para la comunicación con el servidor de VLLM y el banco de preguntas de Moodle.

- Historial de preguntas y respuestas

    - El plugin debe guardar un historial de preguntas y respuestas generadas en la base de datos del centro.

    - El historial debe incluir el usuario, la fecha y hora de creación, la pregunta, las opciones de respuesta y la respuesta correcta.

- Formato GIFT y importación

    - El plugin debe generar las preguntas en formato GIFT (General Import/Export Format for Test Items).

    - El plugin debe importar las preguntas generadas directamente al banco de preguntas del curso de Moodle.

<!-- salto de página -->

- Acceso restringido a profesores

    - El plugin debe estar disponible únicamente para profesores del curso utilizando los roles de moodle.

    - Los profesores deben tener permisos para generar preguntas y acceder al historial de preguntas y respuestas.

- Intentos de generación de preguntas

    - El plugin debe realizar 10 intentos de generación de preguntas antes de indicar que no se ha podido realizar la tarea.

    - Si se alcanzan los 10 intentos sin éxito, el plugin debe mostrar un mensaje de error y no generar preguntas.

- Barra de progreso

    - El plugin debe mostrar una barra de progreso al usuario mientras las preguntas se generan de manera asíncrona.

    - La barra de progreso debe reflejar el progreso de la generación de preguntas.

- Notificación a los usuarios

    - El plugin debe notificar al usuario mediante mensajería interna de Moodle cuando sus preguntas se encuentren generadas.

    - La notificación debe incluir las preguntas generadas con un enlace al banco de preguntas.

**Requisitos técnicos**

El plugin debe ser desarrollado en PHP y utilizar la API de Moodle para interactuar con el banco de preguntas y el servidor de VLLM.

El plugin debe ser compatible con la versión actual de Moodle y VLLM.

El plugin debe ser testado exhaustivamente para garantizar su funcionalidad y seguridad.

##### Generador de textos (AV12)

Al cumplir con estos requisitos para la Adaptación del Plugin de IA de generación de textos en Moodle, el plugin de IA en Moodle debe ser capaz de proporcionar una experiencia de usuario segura, eficiente y flexible para los profesores de EducaMadrid.

- Funcionalidad con instalación local de VLLM

    - El plugin debe ser compatible con instalaciones locales de VLLM en los servidores de EducaMadrid.

    - El modelo de IA en VLLM debe ser elegido por EducaMadrid y configurado en el plugin.

- Seguridad

    - El plugin debe utilizar protocolos seguros (HTTPS) para la comunicación con la instalación local de VLLM.

    - Todas las transacciones de datos deben ser cifradas y autenticadas.

- Historial de solicitudes disponible para los administradores del aula virtual

    - El plugin debe guardar un historial de solicitudes de la IA, incluyendo:

        - Usuario que realizó la solicitud.

        - Texto pedido a la IA.

        - Respuesta de la IA.

- Marcado de textos de respuesta

    - Los textos de respuesta generados por la IA deben ser marcados con el icono característico de IA indicando el modelo utilizado.

- Acceso restringido a profesores

    - El plugin debe estar disponible únicamente para profesores del curso.

    - Los profesores deben tener el rol adecuado asignado en un curso para utilizar el plugin.

- Progreso en tiempo real

    - El usuario debe poder ver el progreso de la solicitud en tiempo real.

    - El plugin debe mostrar un indicador de progreso mientras la IA genera la respuesta.

- Formato de resultado

    - El resultado generado por la IA debe estar en formato Markdown.

    - El plugin debe realizar una conversión a HTML en el momento de insertar el resultado en el editor de Moodle.

- Opciones de configuración

    - El plugin debe mostrar las siguientes opciones de configuración al usuario:

    - Estilo (por ejemplo, formal, informal, etc.).

    - Longitud (por ejemplo, corto, largo, etc.).

    - Creatividad (por ejemplo, alta, baja, etc.).

    - Idioma (por ejemplo, español, inglés, etc.).

    - El plugin debe modificar los prompts de sistema y usuario para que la IA genere el resultado teniendo en cuenta las opciones seleccionadas.

- Integración con el editor de Moodle

    - El plugin debe integrarse con el editor de Moodle para permitir que los profesores inserten el resultado generado por la IA en sus contenidos.

### POC RAG con chat por curso (AV13 )

Realización de una prueba de concepto para la integración de inteligencia artificial mediante un sistema de Retrieval-Augmented Generation (RAG) en la plataforma educativa EducaMadrid. El sistema debe almacenar los datos de cursos seleccionados y poner a disposición del usuario un chatbot de consulta dentro de las aulas virtuales MoodleMisc y Multisite.

**Requisitos Técnicos**

- Infraestructura Local

    - Toda la infraestructura debe ser local y alojada en los servidores propios de la administración pública.

- Chatbot de Consulta

    - El chatbot debe estar limitado al contexto de un curso específico y permitirá a los docentes seleccionar los recursos a integrar.

    - El chatbot debe comunicarse con la IA mediante el protocolo LTI (Learning Tools Interoperability).

- Base de Datos Vectorizada

    - La base de datos vectorizada debe alimentarse con los datos de los cursos que decida el profesor, no con todos los datos del curso disponibles.

    - Solo algunos cursos dispondrán de este sistema, a petición del usuario.

**Funcionalidades del Sistema**

- Selección de Cursos

    - Los profesores podrán seleccionar qué cursos se integrarán en el sistema de RAG.

    - La integración de cursos en el sistema será a petición del usuario (profesor o administrador).

- Interacción del Chatbot

    - El chatbot debe proporcionar respuestas basadas en los datos del curso seleccionado.

    - Las interacciones del chatbot deben ser seguras y cumplir con las normativas de privacidad y protección de datos.

- Integración con MoodleMisc y Multisite

    - El chatbot debe estar integrado en las aulas virtuales “MoodleMisc” y “Multisite” de la plataforma EducaMadrid.

    - La integración debe ser transparente para el usuario final, proporcionando una experiencia de usuario intuitiva y sin interrupciones.

### Integrar NIA de los alumnos (AV14)

Se requiere implementar un sistema de gestión de información de los alumnos en las aulas virtuales Moodle de los centros. El objetivo es contar con un sistema confiable y seguro que permita guardar y mantener actualizada la información de identificación de los alumnos (NIA, Número de Identificación de Alumno) en las aulas virtuales “Multisite” y “MoodleMisc”.

**Objetivos:**

- Implementar un sistema de gestión de información de los alumnos en el aula virtual Moodle “Multisite” y “MoodleMisc” de EducaMadrid

- Garantizar la seguridad y confidencialidad de la información de los alumnos

- Mantener actualizada la información de los NIAS de los alumnos

**Requisitos técnicos:**

- Sistema de gestión de información: Se proporcionará el dato del NIA de los alumnos en tiempo real según los profesores los alimentan en raíces. También se dispondrá del dato en el LDAP de EducaMadrid.

- Seguridad y confidencialidad: El sistema deberá cumplir con los estándares de seguridad y confidencialidad establecidos por la administración pública.

- Actualización de la información: El sistema deberá permitir la actualización automática de la información del NIA en las aulas virtuales.

- Acceso y permisos: El sistema deberá permitir el acceso controlado a la información de los alumnos, según los permisos asignados a cada usuario.

- Compatibilidad: El sistema deberá ser compatible con los sistemas operativos y hardware actuales de la plataforma, así como con las versiones de Moodle.

**Requisitos funcionales:**

- Registro y actualización de la información: El sistema deberá permitir el registro y actualización de la información de los alumnos (NIA) en Moodle.

- Verificación de la información: El sistema deberá permitir la verificación de la información de los alumnos.

- Notificación de errores: El sistema deberá notificar a la administración pública en caso de errores o problemas en la actualización de la información.

- Informe de actividad: El sistema deberá proporcionar un informe de actividad que permita seguir el historial de cambios y actualizaciones realizadas en la información de los alumnos.

- Escalabilidad: no debe modificarse el core de Moodle para permitir futuras subidas de versión del aplicativo.

**Requisitos de soporte y mantenimiento:**

- Actualizaciones y parches: El proveedor deberá proporcionar actualizaciones y parches para el sistema.

- Mantenimiento preventivo: El proveedor deberá realizar mantenimiento preventivo del sistema para evitar problemas y errores.

### SSO en Moodle  (AV15)

Se solicita conectar todas las aulas virtuales Multisite y MoodleMisc con el sistema de SSO de la plataforma EducaMadrid con los siguientes requisitos:

- Utilización de la instalación de SSO

    - Se utilizará la instalación de SSO disponible actualmente en EducaMadrid.

- Login en el SSO

    - El login del usuario se realizará en el SSO en lugar de hacerlo de manera local en Moodle.

- Recogida de datos del usuario

    - En el momento del login se recogerán los datos del usuario para actualizarlos en Moodle.

    - Los datos del usuario deben ser actualizados en tiempo real.

- Sesión de anónimo

    - El usuario entrará como anónimo en el aula virtual hasta que pulse en "Iniciar sesión" pudiendo navegar por la misma por las zonas habilitadas para visitantes.

    - En este momento, si ya tiene sesión iniciada en el SSO, se tomará la sesión.

    - Si no tiene sesión iniciada en el SSO, se mostrará la pantalla de login del SSO.

- Opción de entrar como invitado

    - Se mantendrá la opción de entrar como invitado en el aula virtual.

- Cierre de sesión

    - Si se cierra sesión en otro aplicativo conectado con el SSO, se cerrará también la sesión en el aula virtual.

    - Esto debe ocurrir de manera automática y sin necesidad de intervención del usuario.

- No modificaciones en el core del aplicativo

    - No se realizarán modificaciones en el core del aplicativo para realizar esta tarea.

    - La integración del SSO se realizará mediante plugins o extensiones que no alteren la estructura básica del aplicativo.

- Compatibilidad con Moodle Multisite y MoodleMisc

    - La integración del SSO debe ser compatible con ambas plataformas (Moodle Multisite y MoodleMisc).

- Pruebas y validación

    - Se realizarán pruebas exhaustivas para asegurarse de que la integración del SSO funcione correctamente en todas las situaciones posibles.

    - La validación de la integración se realizará con un conjunto de usuarios y roles representativos.

### Plugin Kuet (AV16)

Adaptación del Plugin de Kuet para Moodle en la Plataforma de Aulas virtuales de EducaMadrid Multisite y MoodleMisc.

- Funcionamiento con servidores propios

    - El plugin de Kuet debe funcionar con servidores propios alojados en la plataforma EducaMadrid.

    - Los servidores deben cumplir con los requisitos técnicos establecidos por el departamento de sistemas de EducaMadrid.

- Modo carrera con preguntas de diferentes tipos

    - El plugin de Kuet debe funcionar en modo carrera con todos los tipos de preguntas soportados.

    - Esto incluye preguntas de tipo múltiple, preguntas de opción única, preguntas de respuesta corta, preguntas de respuesta larga, etc.

- Integración con instalación multisite y moodlemisc

    - El plugin de Kuet debe integrarse con una instalación multisite y moodlemisc de Moodle.

    - La integración debe permitir que el plugin funcione de manera transparente en ambas plataformas.

- Alta concurrencia de uso

    - El plugin de Kuet debe ser capaz de manejar una alta concurrencia de uso.

    - Esto incluye la capacidad de manejar múltiples usuarios simultáneamente en distintas aulas virtuales y de responder de manera rápida y eficiente.

- Seguridad

    - El plugin de Kuet debe trabajar de manera segura.

    - Esto incluye la implementación de medidas de seguridad como la autenticación y autorización de usuarios, la encriptación de datos, etc.

- Colaboración con el departamento de sistemas

    - El desarrollo del plugin de Kuet debe ser realizado en colaboración con el departamento de sistemas de EducaMadrid.

    - El equipo de desarrollo debe trabajar conjuntamente con el departamento de sistemas para establecer los requisitos y el montaje de los servidores de websocket necesarios.

- Certificados en balanceadores

    - Los certificados deben instalarse en los balanceadores y no en los servidores.

    - Esto permitirá que los servidores puedan conectarse a los balanceadores de manera segura y que los balanceadores puedan distribuir el tráfico de manera eficiente.

- Pruebas y validación

    - Se realizarán pruebas exhaustivas para asegurarse de que el plugin de Kuet funcione correctamente en todas las situaciones posibles.

    - La validación de la integración se realizará con un conjunto de usuarios y roles representativos.

- Documentación y soporte

    - Se debe proporcionar documentación detallada sobre la configuración y el funcionamiento del plugin de Kuet.

    - Se debe ofrecer soporte técnico para ayudar a resolver cualquier problema o inquietud que pueda surgir durante la implementación y el uso del plugin.

### Plugin Offline Quiz (AV17)

Adaptación del plugin OfflineQuiz para las aulas virtuales Multisite y MoodleMisc en la plataforma EducaMadrid. El objetivo es asegurar que el plugin cumpla con las características y funcionalidades requeridas para su correcto funcionamiento en el entorno educativo de EducaMadrid.

**Requisitos Funcionales**

- Incorporación de Marca de Agua

    - El plugin debe incluir una marca de agua con el logotipo de EducaMadrid en todos los formularios a imprimir.

- Compatibilidad con el Banco de Preguntas

    - El plugin debe ser capaz de utilizar preguntas del banco de preguntas de Moodle.

- Extensión de Longitud en Hojas

    - El plugin debe permitir extender la longitud del cuestionario en tantas hojas como sea necesario, asegurando que todas las preguntas se impriman correctamente.

- Identificación del Alumno

    - Cada formulario impreso debe incluir un identificador único para el alumno, que permita reasignarle su calificación durante el proceso de escaneo posterior.

- Soporte para Escaneo mediante Fotos

    - El plugin debe soportar el escaneo de los formularios mediante fotos tomadas con dispositivos móviles.

- Instrucciones de Rellenado

    - Cada formulario impreso debe incluir una leyenda con instrucciones claras sobre cómo rellenar las preguntas.

- Integración con las preguntas del banco de preguntas generadas con IA

    - El plugin debe identificar con el icono característico las preguntas seleccionadas del banco de preguntas que hayan sido generadas con IA.

### Plugin para incorporar calificaciones en raíces (AV18)

Creación de un plugin para Moodle que permita la incorporación de las calificaciones de los alumnos directamente a RAICES desde las aulas virtuales de los centros. El objetivo es facilitar la gestión de calificaciones y asegurar la integridad y seguridad de los datos.

**Requisitos Funcionales**

- Icono en el Libro de Calificaciones

    - El plugin debe mostrar un icono en el libro de calificaciones de los cursos, proporcionando la opción de incorporar una columna de calificaciones a RAICES.

- Modal de Incorporación de Calificaciones

    - Al hacer clic en el icono, se debe abrir un modal que permita al profesor realizar las siguientes acciones mediante el uso de una API proporcionada por Madrid Digital:

- Autenticación

    - El modal debe permitir la autenticación del profesor en RAICES utilizando su cuenta.

    - La API debe devolver una lista de cursos y niveles asignados al profesor.

- Selección de Clase y Nivel

    - El profesor debe poder seleccionar una clase y nivel de la lista proporcionada.

    - La API debe devolver una lista de alumnos correspondientes a la clase y nivel seleccionados.

- Asignación de Calificaciones

    - El profesor debe poder asignar calificaciones a los alumnos seleccionados.

    - Las calificaciones asignadas deben ser enviadas a RAICES mediante la API.

**Requisitos No Funcionales**

- Seguridad

    - La seguridad es una prioridad absoluta. El plugin debe implementar medidas robustas para proteger los datos y las operaciones realizadas a través de la API, evitando intrusiones y errores.

    - Todas las comunicaciones con la API deben estar securizadas (por ejemplo, utilizando HTTPS).

    - Los datos de autenticación y las calificaciones deben ser manejados de manera segura, evitando accesos no autorizados.

- Usabilidad

    - La interfaz del plugin debe ser intuitiva y fácil de usar para los profesores.

    - El modal debe proporcionar instrucciones claras y una navegación sencilla para la incorporación de calificaciones.

- Rendimiento

    - El plugin debe ser eficiente y no afectar negativamente el rendimiento general de la plataforma Moodle.

- Mantenimiento

    - El plugin debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

### Borrado de cursos en segundo plano (AV19)

Implementación de un sistema que permita el borrado asíncrono de cursos en las aulas virtuales Multisite y MoodleMisc mediante el cron de Moodle. El objetivo es mejorar la eficiencia y la experiencia del usuario al programar el borrado de cursos en segundo plano.

**<!-- salto de página -->**

**Requisitos Funcionales**

- Programación del Borrado de Cursos

    - El sistema debe permitir que un usuario marque un curso para su borrado.

    - Al marcar un curso para borrar, este debe quedar programado para su eliminación en segundo plano mediante el cron de Moodle.

- Notificación al Usuario

    - El usuario debe recibir una notificación confirmando que su curso ha sido programado para borrado.

    - La notificación debe indicar que el curso no estará disponible para el usuario hasta que se complete el borrado.

- Acceso al Curso Programado para Borrado

    - El usuario no debe poder acceder al curso una vez que este haya sido programado para borrado.

    - El sistema debe mostrar un mensaje indicando que el curso ha sido programado para borrado y no está disponible.

- Ejecución Asíncrona

    - El borrado de cursos programados debe ejecutarse en segundo plano mediante tareas programadas en el cron de Moodle usando Moosh.

    - El sistema debe manejar múltiples cursos programados para borrado de manera eficiente, evitando conflictos y asegurando que cada curso se elimine correctamente.

- Registro de Actividades

    - El sistema debe registrar todas las actividades relacionadas con la programación y eliminación de cursos, incluyendo la fecha y hora de programación, la fecha y hora de eliminación, y el usuario responsable.

**Requisitos No Funcionales**

- Usabilidad

    - La interfaz del sistema debe ser intuitiva y fácil de usar para los usuarios, proporcionando claras indicaciones sobre el estado de los cursos programados para borrado.

- Seguridad

    - El sistema debe asegurar que solo los usuarios autorizados puedan programar el borrado de cursos.

    - Los datos de los cursos programados para borrado deben ser manejados de manera segura, evitando accesos no autorizados.

- Rendimiento

    - El sistema debe ser capaz de manejar un gran número de cursos programados para borrado sin afectar el rendimiento general de la plataforma.

- Mantenimiento

    - El sistema debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

<!-- salto de página -->

### Moosh (AV20)

Adaptación del script Moosh al entorno de aulas virtuales MoodleMisc y Multisite de EducaMadrid para cambios evolutivos. El objetivo es asegurar que Moosh funcione correctamente en ambos entornos y cumpla con las características requeridas.

**Requisitos Funcionales**

- Uso del Mismo Código

    - El código de Moosh debe ser el mismo para ambos entornos, MoodleMisc y Multisite.

- Modificación para Modo Multisite

    - El aplicativo Moosh debe ser modificado para funcionar en modo multisite tanto dentro del entorno Multisite como MoodleMisc, permitiendo la gestión de múltiples instancias de Moodle desde una única interfaz.

- Parámetros Adicionales

    - Se deben agregar dos parámetros (adicionales a los necesarios del aplicativo) a cada llamada a Moosh:

        - Centro: Indica sobre qué centro se quiere actuar.

        - IP: Indica la dirección IP del servidor en el que se ejecuta.

- Localización de la Base de Datos

    - Moosh debe ser capaz de localizar la base de datos del centro indicado por el parámetro y conectarse a ella para realizar las acciones solicitadas.

### Moodler (AV21)

Adaptación del plugin MOODLER al entorno de aulas virtuales MoodleMisc y Multisite de EducaMadrid para cambios evolutivos. El objetivo es asegurar que el plugin cumpla con las características y funcionalidades requeridas para su correcto funcionamiento en el entorno educativo de EducaMadrid.

**Requisitos Funcionales**

- API Securizada

    - El plugin debe proporcionar una API securizada que permita el acceso a las funciones del core de Moodle de manera segura.

- Campos Sanitizados

    - Todos los campos de entrada y salida de la API deben ser sanitizados para prevenir inyecciones de código y otros ataques comunes.

- Funcionamiento en Modo Multisite

    - El plugin debe ser capaz de funcionar en un entorno multisite, permitiendo la gestión de múltiples sitios desde una única instalación de Moodle.

- Acceso a Funciones del Core

    - La API debe permitir el acceso a las funciones del core de Moodle, facilitando la integración con otras herramientas y servicios educativos.

**<!-- salto de página -->**

**Requisitos No Funcionales**

- Seguridad

    - La seguridad es una prioridad absoluta. El plugin debe implementar medidas robustas para proteger los datos y las operaciones realizadas a través de la API.

- Usabilidad

    - La interfaz del plugin debe ser intuitiva y fácil de usar para los administradores y desarrolladores.

- Rendimiento

    - El plugin debe ser eficiente y no afectar negativamente el rendimiento general de la plataforma Moodle.

- Mantenimiento

    - El plugin debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

### EVOLUCIÓN Y MANTENIMIENTO DE LA MEDIATECA (MED)

### Subtítulos multi idioma (MED1)

La Mediateca de EducaMadrid busca desarrollar un plugin que permita a los usuarios crear y editar subtítulos para los vídeos subidos a la plataforma. El plugin debe utilizar la tecnología de IA para generar subtítulos automáticamente en el idioma nativo del vídeo e inglés. Además, el plugin debe incluir un editor de subtítulos que permita a los usuarios agregar, editar y eliminar subtítulos de manera sencilla y segura.

**Requisitos Funcionales**

- Generación automática de subtítulos:

    - El plugin debe utilizar inteligencia artificial para generar subtítulos automáticos en el idioma nativo del vídeo e inglés para los vídeos subidos a la plataforma.

    - El plugin debe poder adjuntar subtítulos en diferentes idiomas y dialectos mostrando al usuario de los vídeos la opción de ver dichos subtítulos.

- Editor de subtítulos:

    - El editor de subtítulos debe permitir a los usuarios agregar subtítulos mediante fichero (SRT, VTT, etc.).

    - El editor de subtítulos debe permitir a los usuarios solicitar la generación automática de subtítulos mediante IA para el idioma nativo e inglés.

    - El editor de subtítulos debe permitir a los usuarios visualizar el subtítulo actual.

    - El editor de subtítulos debe permitir a los usuarios eliminar el subtítulo y dejar el contenido sin ninguno.

    - El editor de subtítulos debe permitir a los usuarios editar el subtítulo en formato SRT.

- Edición de tramos de subtítulos:

    - El plugin debe permitir a los usuarios editar tramos de subtítulos en tiempo real viendo los cambios sobre el reproductor de vídeo.

    - El plugin debe permitir a los usuarios realizar acciones de edición de un tramo (cortar, pegar, etc.).

    - El plugin debe permitir a los usuarios realizar acciones de eliminación de un tramo.

    - El plugin debe permitir a los usuarios realizar acciones de inserción de un tramo nuevo antes o después de uno existente.

    - El plugin debe permitir a los usuarios realizar acciones de cortar un tramo en dos.

    - El plugin debe indicar mediante código de colores los CPS de un tramo para valorar su facilidad de lectura.

    - El plugin debe adaptar los tiempos a tramos anteriores y siguientes.

- Mecanismos de seguridad:

    - El plugin debe incluir mecanismos de seguridad para evitar la edición de subtítulos sin permiso.

    - El plugin debe incluir mecanismos de seguridad para evitar la eliminación de subtítulos sin permiso.

    - El plugin debe incluir mecanismos de seguridad para evitar la edición de subtítulos por usuarios no autorizados.

**Requisitos No Funcionales**

- Interfaz de usuario:

    - La interfaz de usuario del plugin debe ser intuitiva y fácil de usar.

    - La interfaz de usuario del plugin debe ser compatible con diferentes navegadores y dispositivos.

- Rendimiento:

    - El plugin debe ser capaz de generar subtítulos de manera rápida y eficiente.

    - El plugin debe ser capaz de editar subtítulos de manera rápida y eficiente.

- Compatibilidad:

    - El plugin debe ser compatible con la mediateca.

    - El plugin debe ser compatible con diferentes sistemas operativos.

- Seguridad

    - Los subtítulos no deben ser indexados por los motores de búsqueda.

- Integración

    - Los subtítulos deben indexarse en la plataforma elastic de la mediateca para permitir buscar contenidos usando los subtítulos como criterios de búsqueda.

**Requisitos de Implementación**

- Tecnologías utilizadas:

    - El plugin debe utilizar inteligencia artificial (IA) para generar subtítulos automáticos.

    - El plugin debe utilizar la tecnología de edición de subtítulos de SRT.

    - Debe ser desarrollado en PHP versión compatible con el core de la mediateca.

- Base de datos:

    - El plugin debe utilizar la base de datos de la mediateca y la data de la misma para almacenar los subtítulos.

- Documentación:

    - El plugin debe incluir documentación para los desarrolladores y usuarios.

<!-- salto de página -->

### Elastic en las búsquedas (MED2)

La Mediateca de EducaMadrid busca crear un plugin que permita utilizar Elastic como motor de búsqueda de contenidos en lugar de la base de datos del aplicativo. El plugin debe adaptar la Mediateca para compatibilizarla con las mejoras en el sistema de búsquedas de Medios con Elastic Search y las evoluciones del mismo.

**Requisitos Funcionales**

- Adaptación de la Mediateca

    - El plugin debe llevar a cabo los cambios necesarios para compatibilizar la Mediateca con las mejoras en el sistema de búsquedas de Medios con Elastic Search.

- Indexado de contenido

    - El plugin debe permitir el indexado de los ficheros SRT y PDF en Elastic Search.

    - El plugin debe crear campos de control en la base de datos para almacenar la información necesaria para el indexado.

    - El plugin debe soportar la integración de php-elasticsearch.

- Modificación de consultas

    - El plugin debe modificar las consultas para utilizar Elastic Search en lugar de la base de datos si se activa y si no falla el servicio de elasctic, en caso contrario se utilizará la base de datos local como motor de búsqueda.

- Sistema híbrido

    - El plugin debe crear un sistema híbrido que permita cambiar entre el sistema tradicional de búsqueda basado en SQL y el sistema basado en Elastic Search.

- Registro y panel de mando

    - Implementación de un mecanismo de registro de todas las consultas hacia el entorno de elastic y diseño de un panel donde poder consultar dichos registros. Debe guardarse toda la información relevante: parámetros búsqueda, tiempo empleado, etc.

- Funcionalidades de Elastic

    - El plugin debe integrar las nuevas funcionalidades que proporcione Elastic, como el highlighting.

    - El plugin debe integrar la funcionalidad de búsqueda de Elastic en:

        - El buscador simple

        - El buscador avanzado

        - Los contenidos relacionados

        - Los contenidos del mismo autor

        - La generación de la portada

### Single Sign On (MED3)

La Mediateca de EducaMadrid busca crear un plugin que permita utilizar el sso de EducaMadrid como método de autenticación SSO con las siguientes condiciones:

**<!-- salto de página -->**

**Requisitos Funcionales**

- Integración con SSO

    - El plugin debe permitir la integración con el sso de EducaMadrid como método de autenticación.

    - El plugin debe utilizar la API del sso para autenticar a los usuarios.

- Detección de sesión en otros aplicativos

    - El plugin debe detectar si el usuario ya tiene sesión en el SSO en algún otro aplicativo de EducaMadrid.

    - El plugin debe autenticar directamente al usuario si ya tiene sesión en otro aplicativo.

- Navegación anónima

    - El plugin debe permitir la navegación anónima hasta que el usuario pulse en iniciar sesión.

    - El plugin debe llevar al usuario al login del sso cuando pulse en iniciar sesión.

- Cierre de sesión en otros aplicativos

    - El plugin debe detectar si se cierra sesión en otro aplicativo.

    - El plugin debe cerrar la sesión en la mediateca cuando se cierra sesión en otro aplicativo.

- Excepciones para contenido público

    - El plugin debe no comprobar la sesión para contenido público embebido en otras páginas.

- Actualización de información local del usuario

    - El plugin debe actualizar la información local del usuario como nombre, apellidos o el centro al que pertenece cuando se inicia sesión.

- Soporte para 2FA

    - El plugin debe tener soporte para 2FA en caso de implementarse.

**Requisitos No Funcionales**

- Interfaz de usuario

    - La interfaz de usuario del plugin debe ser intuitiva y fácil de usar.

    - La interfaz de usuario del plugin debe ser compatible con diferentes navegadores y dispositivos.

- Rendimiento

    - El plugin debe ser capaz de realizar autenticaciones de manera rápida y eficiente.

    - El plugin debe ser capaz de manejar un gran volumen de usuarios.

- Compatibilidad

    - El plugin debe ser compatible con la mediateca

**Requisitos de Implementación**

- Tecnologías utilizadas

    - El plugin debe utilizar la API del sso para la autenticación.

- Documentación

    - El plugin debe incluir documentación para los desarrolladores y usuarios.

**<!-- salto de página -->**

**Revisión y pruebas**

- El plugin debe ser revisado y probado por un equipo de desarrollo y pruebas antes de ser considerado aceptado.

### Scratch editor (MED4)

Se solicita que para los tipos de contenido Scratch alojados en la mediateca se disponga de la opción de editar los mismos directamente de manera online. Para ello se requiere modificar el aplicativo “Mediateca” creando un plugin con los siguientes requisitos:

- Compatibilidad con tecnología y servidores

    - El plugin debe ser compatible con la tecnología empleada en el desarrollo de la mediateca y con los servidores que la alojan.

    - Los servidores deben cumplir con los requisitos técnicos establecidos por el departamento de sistemas de la plataforma.

- Instalación del servidor de Scratch

    - El plugin debe trabajar con una instalación del editor de Scratch alojada en los servidores de la plataforma.

    - Se debe trabajar conjuntamente con el departamento de sistemas para instalar el servidor de Scratch, el aplicativo mismo y configurarlo.

- Comunicaciones seguras

    - El plugin debe trabajar de manera segura en las comunicaciones entre mediateca y los servidores de Scratch.

    - Esto incluye la implementación de medidas de seguridad como la autenticación y autorización de usuarios, la encriptación de datos, etc.

- Modificación del aplicativo de editor de Scratch

    - El aplicativo de editor de Scratch debe modificarse para que solo permita trabajar con el mismo si se accede desde la mediateca.

    - Las opciones del editor deben limitarse a las necesarias para el trabajo de dicha manera.

Acceso a la opción de editar un Scratch

    - En la mediateca debe aparecer la opción de editar un Scratch solo al propietario del mismo.

    - Si el propietario es un alumno, la opción de editar solo debe estar disponible si su contenido no ha sido todavía validado.

- Opción de generar un nuevo contenido de tipo Scratch

    - En la mediateca debe aparecer una opción para generar un nuevo contenido de tipo Scratch desde cero.

    - Al pulsar esta opción, el usuario debe ser redirigido al editor de Scratch con una plantilla vacía.

- Integración con la mediateca

    - El plugin debe integrarse con la mediateca de manera que se pueda acceder a los contenidos de tipo Scratch desde la misma.

    - La mediateca debe mostrar los contenidos de tipo Scratch de manera adecuada, incluyendo la opción de editar y generar nuevos contenidos.

<!-- salto de página -->

- Pruebas y validación

    - Se realizarán pruebas exhaustivas para asegurarse de que el plugin funcione correctamente en todas las situaciones posibles.

    - La validación de la integración se realizará con un conjunto de usuarios y roles representativos.

- Documentación y soporte

    - Se debe proporcionar documentación detallada sobre la configuración y el funcionamiento del plugin.

    - Se debe ofrecer soporte técnico para ayudar a resolver cualquier problema o inquietud que pueda surgir durante la implementación y el uso del plugin.

### Exelearning 3 (MED5)

Adaptación de la Mediateca para soportar contenido eXeLearning 3 y conexión con eXeLearning online

**Objetivos**

- **Soporte para contenido eXeLearning 3:** Adaptar la Mediateca para que pueda almacenar, describir y etiquetar sitios web comprimidos en formato zip generados con la herramienta de autor eXeLearning 3.

- **Conexión con eXeLearning online:** Implementar un mecanismo de comunicación en PHP que permita a los usuarios de la Mediateca crear y editar contenidos con la versión online de la herramienta de autor eXeLearning 3 alojada en los servidores de EducaMadrid.

**Requisitos Funcionales**

- Subir, describir y etiquetar contenido eXeLearning 3:

    - Los usuarios podrán subir sitios web comprimidos en formato zip generados con la herramienta de autor eXeLearning 3.

    - Los usuarios podrán describir y etiquetar el contenido.

- Visualizar contenido en IFRAME:

    - Los sitios web comprimidos en formato zip se mostrarán en una página de la Mediateca insertados en un IFRAME.

- Abrir contenido en ventana nueva:

    - Los usuarios podrán abrir el contenido en una ventana nueva.

- Descargar contenido en formato zip y archivo editable:

    - Los usuarios podrán descargar el contenido en formato zip.

    - Si el contenido es editable, los usuarios podrán descargarlo en archivo con extensión .elp.

- Conexión con eXeLearning 3 online:

    - Los usuarios contarán con un botón que les permita crear o editar un contenido.

    - Al pulsar el botón, los usuarios accederán a eXeLearning online y podrán editar el contenido.

    - Una vez finalizada la edición, eXeLearning les enviará de nuevo a la página de la Mediateca.

**<!-- salto de página -->**

**Requisitos de Seguridad**

- Autenticación y autorización:

    - Los usuarios deben ser autenticados y autorizados para acceder a la Mediateca y editar contenidos.

- Protección de contenido:

    - El contenido debe ser protegido contra acceso no autorizado.

**Requisitos de Desarrollo**

- Uso de tecnologías actuales:

    - La Mediateca debe utilizar tecnologías actuales y seguras, como PHP y MySQL.

### Bajas de usuarios (MED6)

Creación de un script en PHP seguro que permita procesar las bajas de los usuarios del portal educativo de EducaMadrid directamente en el aplicativo Mediateca, eliminando sus contenidos y datos.

**Requisitos Funcionales**

- Procesamiento de baja de usuario:

    - El script debe poder procesar la baja de un usuario del portal educativo de EducaMadrid.

    - El script debe poder eliminar los contenidos y datos del usuario de la base de datos de la Mediateca y del disco.

- Validación de permisos:

    - El script debe validar los permisos del usuario que realiza la baja.

    - El script debe verificar si el usuario tiene permisos para eliminar contenidos y datos de la base de datos.

**Requisitos de Seguridad**

- Autenticación y autorización:

    - El script debe requerir autenticación y autorización para proceder a eliminar al usuario.

- Protección de datos:

    - El script debe proteger los datos del usuario que se eliminan.

    - El script debe eliminar los datos de manera segura y no debe dejar rastros de los datos eliminados.

- Validación de entrada:

    - El script debe validar la entrada de datos para evitar inyecciones de código malicioso.

**Requisitos de Desarrollo**

- Uso de tecnologías actuales:

    - El script debe utilizar tecnologías actuales y seguras, como PHP y MySQL

<!-- salto de página -->

- Documentación y soporte:

    - El script debe tener documentación clara y completa sobre su funcionamiento y configuración.

    - El script debe tener soporte técnico disponible para resolver problemas y preguntas.

### Soporte JPEG en subidas masivas de imágenes (MED7)

**Objetivos**

- Soportar formato JPEG:

    - Admitir subidas de imágenes en formato JPEG de la misma manera que se soportan JPG, GIF y PNG.

- Mejorar experiencia del usuario:

    - Permitir a los usuarios subir múltiples imágenes en formato JPEG de manera rápida y eficiente.

**Requisitos Funcionales**

- Soportar formato JPEG:

    - El sistema debe poder reconocer y procesar imágenes en formato JPEG.

    - El sistema debe poder almacenar y mostrar imágenes en formato JPEG de manera correcta.

- Mejorar experiencia del usuario:

    - El sistema debe permitir a los usuarios subir múltiples imágenes en formato JPEG de manera rápida y eficiente.

    - El sistema debe mostrar un mensaje de éxito al usuario después de subir las imágenes.

### Páginas de error personalizadas (MED8)

**Objetivos**

- Crear páginas de error personalizadas:

    - Crear páginas de error personalizadas para los códigos de error 404, 500, etc.

    - Reemplazar las páginas de error propias de Apache por páginas de error personalizadas.

- Mejorar experiencia del usuario:

    - Proporcionar a los usuarios una experiencia de error más amigable y útil.

    - Proporcionar a los usuarios información útil y relevante sobre el error.

**Requisitos Funcionales**

- Crear páginas de error personalizadas:

    - Crear páginas de error personalizadas para los códigos de error 404, 500, etc.

    - Reemplazar las páginas de error propias de Apache por páginas de error personalizadas.

- Personalizar la página de error:

    - Personalizar la página de error con el logotipo y el diseño del aplicativo mediateca.

    - Agregar información útil y relevante sobre el error.

- Redireccionar a la página de error:

    - Redireccionar a la página de error cuando se produzca un error.

### Subtítulos en los audios (MED9)

Permitir que para los tipos de contenido audio en la mediateca se generen subtítulos mediante IA de manera automática durante la subida de los mismos.

**Objetivos**

- Generar subtítulos para contenido audio:

    - Permitir que los tipos de contenido audio en la mediateca se generen subtítulos mediante IA.

    - Incorporar los subtítulos generados al reproductor de audio para lo que será necesario realizar adaptaciones en el reproductor.

- Editar subtítulos generados:

    - Permitir al usuario editar los subtítulos generados mediante el editor de subtítulos que ya existe en la mediateca.

- Crear subtítulos de todos los audios ya subidos

    - Crear un script que, sin afectar a la creación de subtítulos de vídeos o audios nuevos, vaya creando los subtítulos de los audios ya subidos a la mediateca.

**Requisitos Funcionales**

- Generar subtítulos para contenido audio:

    - Utilizar IA para generar subtítulos para contenido audio.

    - Incorporar los subtítulos generados al reproductor de audio.

- Editar subtítulos generados:

    - Permitir al usuario editar los subtítulos generados mediante el editor de subtítulos de la mediateca.

    - Guardar los cambios realizados en los subtítulos.

**Requisitos de Seguridad**

- Validación de contenido:

    - Validar el contenido audio para asegurarse de que sea válido y no contenga errores.

- Protección contra ataques:

    - Proteger el aplicativo contra ataques de seguridad, como inyecciones de código malicioso.

Opción para descargar vídeos

Permitir Descargar Vídeos a sus propietarios en Todas las Resoluciones Disponibles

**Objetivos**

- Permitir descargar vídeos en todas las resoluciones disponibles:

    - Permitir a los propietarios de los vídeos descargarlos en todas las resoluciones disponibles.

- Incluir el ID del vídeo y la resolución descargada en el nombre del archivo:

    - Incluir el ID del vídeo y la resolución descargada en el nombre del archivo descargado.

**Requisitos Funcionales**

- Permitir descargar vídeos en todas las resoluciones disponibles:

    - Permitir a los propietarios de los vídeos descargarlos en todas las resoluciones disponibles.

    - Mostrar las opciones de resolución disponibles para cada vídeo.

- Incluir el ID del vídeo y la resolución descargada en el nombre del archivo:

    - Incluir el ID del vídeo y la resolución descargada en el nombre del archivo descargado.

    - Utilizar un formato de archivo estándar para el nombre del archivo.

**Requisitos de Seguridad**

- Validación de permisos:

    - Validar los permisos del usuario para asegurarse de que tenga permiso para descargar el vídeo.

- Protección contra ataques:

    - Proteger el aplicativo contra ataques de seguridad, como inyecciones de código malicioso.

### IA en mediateca: generar resúmenes de los vídeos (MED10)

Implementación de un sistema que, utilizando inteligencia artificial (IA), realice resúmenes de los subtítulos de los vídeos y recursos de Formación Profesional (FP) subidos a la mediateca de EducaMadrid. Estos resúmenes se adjuntarán a la descripción de cada contenido y se generarán de manera asíncrona.

**Objetivos**

- Implementar un sistema de resúmenes de subtítulos utilizando IA.

- Integrar el sistema de resúmenes en el actual sistema de colas de tareas de la mediateca.

- Asegurar que los resúmenes se generen de manera asíncrona y se notifique al usuario.

- Permitir la eliminación y regeneración de resúmenes a solicitud del usuario.

- Instalar el sistema de IA localmente en los servidores con GPU de la plataforma y asegurar una comunicación segura con la mediateca.

- El modelo seleccionado para la generación de resúmenes debe ser seguro y proporcionar resultados con calidad.

**Alcance**

- Desarrollo e implementación del sistema de resúmenes de subtítulos utilizando IA.

- Integración del sistema de resúmenes en el sistema de colas de tareas de la mediateca.

- Configuración de un cron para gestionar la carga de la máquina de IA.

- Notificación al usuario sobre la disponibilidad de los resúmenes.

- Permitir la eliminación y regeneración de resúmenes a solicitud del usuario.

- Instalación y configuración segura del sistema de IA en los servidores de la plataforma.

**Requisitos Técnicos**

- Sistema de Resúmenes de Subtítulos

    - Tecnología de IA: Utilizar un modelo de IA capaz de generar resúmenes a partir de subtítulos.

    - Generación Asíncrona: Los resúmenes se generarán de manera asíncrona según la disponibilidad de la máquina de IA.

    - Integración con Colas de Tareas: Integrar el sistema de resúmenes en el actual sistema de colas de tareas de la mediateca.

    - Priorización de Tareas: Dar prioridad a los nuevos contenidos subidos a la mediateca sobre los contenidos existentes.

- Gestión de Colas de Tareas

    - Cron de Gestión: Implementar un cron que consulte la carga de la máquina de IA y envíe simultáneamente tantas tareas como sea capaz de soportar.

    - Cola de Tareas Inicial: Meter en la cola de tareas todos los contenidos actuales de la mediateca con subtítulos.

    - Notificación al Usuario: Notificar al usuario cuando el resumen esté disponible.

    - Eliminación y Regeneración: Permitir la eliminación y regeneración de resúmenes a solicitud del usuario.

- Instalación y Configuración del Sistema de IA

    - Instalación Local: Instalar el sistema de IA localmente en los servidores de la plataforma.

    - Comunicación Segura: Asegurar una comunicación segura entre el sistema de IA y la mediateca.

    - Escalabilidad: Asegurar que el sistema de IA pueda escalar según la demanda.

### Refactorizar código (MED11)

Se solicita realizar una refactorización del Código de la Mediateca con versiones de php nuevas y seguras, en servidores con el sistema operativo en su última versión y con los paquetes del sistema actualizados.

**Objetivos**

- Simplificar el código y facilitar la incorporación de nuevos tipos de contenido:

    - Simplificar el código de la Mediateca para facilitar la incorporación de nuevos tipos de contenido.

- Mejorar la seguridad y escalabilidad:

    - Mejorar la seguridad y escalabilidad de la Mediateca para futuras versiones de PHP.

- Actualizar las librerías externas:

    - Actualizar las versiones de las librerías externas utilizadas en la parte cliente (JavaScript y/o CSS) y en el servidor (PHP).

- Incorporar mejoras de búsqueda:

    - Incorporar mejoras de búsqueda mediante Elasticsearch.

- Diseño renovado y accesible:

    - Diseño 100% renovado, accesible y adaptable al dispositivo (responsive design).

**<!-- salto de página -->**

**Requisitos Funcionales**

- Simplificar el código:

    - Simplificar el código de la Mediateca para facilitar la incorporación de nuevos tipos de contenido.

    - Utilizar patrones de diseño y principios de programación orientada a objetos.

- Mejorar la seguridad:

    - Mejorar la seguridad de la Mediateca mediante la validación de entrada y la protección contra ataques de seguridad.

- Actualizar las librerías externas:

    - Actualizar las versiones de las librerías externas utilizadas en la parte cliente (JavaScript y/o CSS) y en el servidor (PHP).

- Incorporar mejoras de búsqueda:

    - Incorporar mejoras de búsqueda mediante Elasticsearch.

- Diseño renovado y accesible:

    - Diseño 100% renovado, accesible y adaptable al dispositivo (responsive design).

### CONSULTAS LDAP (LDAP)

Desarrollo de un aplicativo de uso interno para la consulta y gestión de cuentas de usuarios (LDAP1).

**Objetivos y Funcionalidades**

- La aplicación debe permitir a los usuarios logados realizar consultas al LDAP de usuarios mostrando toda la información disponible de los usuarios consultados.

- La aplicación debe mostrar los siguientes datos:

- Todos los datos disponibles en el LDAP.

- El estado del doble factor de autenticación (2FA) del usuario.

- La aplicación debe realizar consultas a la aplicación de bloqueados para consultar el estado y el histórico de bloqueos del usuario.

- La aplicación debe realizar consultas a la base de datos central de usuarios para ver todos los centros del usuario y su rol en cada uno de ellos, mostrando también información de niveles, clases, carga lectiva, etc.

- La aplicación debe tener una gestión para poner una contraseña temporal a usuarios, que se reestablecerá por la original pasado un tiempo indicado.

- La aplicación debe tener un apartado para comprobar la contraseña de los usuarios.

- La aplicación debe tener roles dentro del aplicativo, donde un administrador podrá determinar que usuarios pueden cambiar la contraseña a cuentas especiales que serán las administradoras de otros aplicativos como aulas virtuales, WordPress, etc.

**Requisitos***.**

- **Requisitos Técnicos.**

    - La aplicación debe ser desarrollada en un lenguaje de programación compatible con la plataforma de desarrollo utilizada por la administración pública.

    - La aplicación debe utilizar una base de datos relacional para almacenar la información de los usuarios de la misma y todas las acciones que estos realizan

    - La aplicación debe utilizar la API del LDAP para realizar consultas a la base de datos de usuarios.

    - La aplicación debe utilizar la API de la aplicación de bloqueados para realizar consultas a la base de datos de bloqueos.

    - La aplicación debe utilizar la API de la base de datos central de usuarios para realizar consultas a la base de datos de centros y roles.

- **Seguridad.**

    - La aplicación debe cumplir con los estándares de seguridad de la administración pública.

    - La aplicación debe utilizar criptografía para proteger la información de los usuarios.

    - La aplicación debe utilizar autenticación y autorización para controlar el acceso a la información de los usuarios.

    - La aplicación debe utilizar un sistema de gestión de sesiones para controlar el acceso a la aplicación.

- **Usabilidad.**

    - La aplicación debe ser fácil de usar y entender para los usuarios.

    - La aplicación debe tener una interfaz de usuario intuitiva y fácil de navegar.

    - La aplicación debe proporcionar información clara y concisa sobre la información de los usuarios.

    - La aplicación debe permitir a los usuarios realizar consultas y acciones de manera rápida y eficiente.

- **Mantenimiento.**

    - La aplicación debe ser fácil de mantener y actualizar.

    - La aplicación debe tener un sistema de gestión de versiones para controlar las actualizaciones y parches.

    - La aplicación debe tener un sistema de gestión de errores para controlar y solucionar problemas.

    - La aplicación debe tener un sistema de gestión de solicitudes de soporte para controlar y solucionar problemas.

- **Documentación.**

    - La aplicación debe tener una documentación clara y concisa que explique cómo funciona y cómo se puede utilizar.

    - La aplicación debe tener una documentación técnica que explique la arquitectura y la implementación de la aplicación.

    - La aplicación debe tener una documentación de seguridad que explique los mecanismos de seguridad utilizados en la aplicación.

- **Pruebas**

    - La aplicación debe ser probada y validada.

    - La aplicación debe ser probada en diferentes entornos y configuraciones.

    - La aplicación debe ser probada con diferentes tipos de usuarios y roles.

    - La aplicación debe ser probada con diferentes escenarios de carga y uso.

<!-- salto de página -->

### MEJORAS Y MANTENIMIENTO DEL SERVICIO EXELEARNING ONLINE (EXE)

Se requiere (EXE1):

- Adaptación de eXeLearning Online a Moodle 4.5.x y superior

    - Se requiere adaptar la versión 3.0, o superior, de eXeLearning Online para que se pueda conectar al Aula Virtual de EducaMadrid (Moodle 4.5.x y superiores) mediante la instalación y configuración de los módulos correspondientes para Moodle.

    - Los módulos deben permitir la creación y edición de actividades de tipo "Sitio web" y "SCORM" en Moodle.

    - La interfaz de gestión de dichos módulos en Moodle debe ser simplificada para que los docentes solo vean las opciones de uso habitual por defecto.

- Actualización a la versión 3.0 o superior de eXeLearning Online

    - Se requiere actualizar la versión base 3.0 o superior de eXeLearning Online a la versión oficial del proyecto.

    - La instalación debe mantenerse actualizada con el código del repositorio oficial del proyecto.

    - El entorno debe quedar preparado para que las Aulas Virtuales de EducaMadrid puedan pasar de una versión a otra de eXeLearning (2.9 a 3.0 o más) sin paradas, únicamente sustituyendo una URL por otra en la configuración de los módulos de Moodle correspondientes (mod\_exeweb, mod\_exescorm).

- Mejoras en la interfaz de eXeLearning Online

    - Se requieren al menos cinco nuevos estilos para la herramienta de autor de eXeLearning Online, compatibles con la nueva versión:

    - EducaMadrid y su versión para presentaciones

    - EducaMadrid MAX y su versión para presentaciones

    - EducaMadrid DUA

    - Los estilos deben cargar el pie de página institucional de la Plataforma Educativa EducaMadrid cuando se encuentren publicados en los servidores de la misma.

    - La interfaz gráfica de usuario de la herramienta debe ser personalizada para adaptarse a la imagen institucional de la Plataforma y limitar el número de estilos disponibles para los usuarios.

- Integración con Moodle 4.x

    - Se requiere integrar eXeLearning Online con Moodle 4.x para permitir la creación y edición de actividades de tipo "Sitio web" y "SCORM" en Moodle.

    - La integración debe ser compatible con la versión 3.0 o superior de eXeLearning Online y debe permitir la sincronización de datos entre eXeLearning Online y Moodle.

- Pruebas y validación

    - Se requieren pruebas y validación para asegurarse de que la integración y personalización de eXeLearning Online con Moodle 4.5.x sean correctas y funcionales.

    - Las pruebas deben incluir la verificación de la compatibilidad con la versión 3.0 o superior de eXeLearning Online y la sincronización de datos entre eXeLearning Online y Moodle.

- Documentación y soporte

    - Se requiere documentación detallada de la integración y personalización de eXeLearning Online con Moodle 4.x.

    - Se requiere soporte técnico para ayudar a resolver problemas y responder a preguntas sobre la integración y personalización.

### MEJORAS Y MANTENIMIENTO EN EL CORREOWEB (COR)

### Adaptaciones a la última versión estable (COR1)

Se solicita adaptar al entorno de EducaMadrid la última versión estable del aplicativo correoweb para que los usuarios puedan gestionar sus cuentas de correo electrónico.

**Requisitos Funcionales**

- Mantenimiento de modificaciones en el código actual: Se deben mantener todas las modificaciones realizadas en el código actual, incluyendo las funcionalidades que proporcionan.

- Configuración de nuevas opciones: las nuevas funcionalidades incorparadas tras la actualización se configurarán según las necesidades del servicio.

- Actualización de temas y plugins: Se deben actualizar todos los temas y plugins instalados en la versión actual para asegurar compatibilidad con la nueva versión.

- Garantía de estabilidad y seguridad: Se deben seleccionar versiones del aplicativo y dependencias que garanticen la estabilidad y seguridad del sistema.

- Verificación de requisitos de servidores: Se debe comprobar si los servidores actuales cumplen los requisitos para la nueva versión del aplicativo. Si no es así, se debe trabajar con el departamento de sistemas para actualizar los paquetes del sistema necesarios o generar nuevos servidores con la última versión de sistema operativo.

- Mantenimiento de configuraciones y datos actuales: Se deben mantener todas las configuraciones actuales, incluyendo correos, contactos, filtros, firmas, claves PGP, etc.

- Sincronización de calendarios: Se debe mantener activa la sincronización de calendarios con las aulas virtuales.

- Compatibilidad con dispositivos móviles: Se debe asegurar que la nueva versión sea compatible con dispositivos móviles y que la aplicación móvil de correo funcione correctamente en diferentes plataformas.

- Integración con otros servicios: Se debe asegurar que la nueva versión se pueda integrar con otros servicios.

**Mejoras Adicionales**

- Reintentos de envíos de correos programados: Se debe implementar la capacidad de reintentar los envíos de correos programados hasta 10 veces antes de marcarlos como error de envío, informando al usuario del estado de su correo.

- API para restaurar contactos eliminados: Se debe crear una API securizada para permitir a los usuarios restaurar contactos eliminados desde Empieza, indicando el usuario y las fechas de borrado.

<!-- salto de página -->

- Aplicación móvil de correo: Se debe crear una aplicación móvil de correo basada en K-9 Thunderbird personalizada con la imagen corporativa, donde los usuarios puedan configurar su correo personal o institucional solo con su usuario y contraseña con posibilidad de ofrecer notificaciones a los usuarios.

- Integración con el cloud de EducaMadrid: Se debe crear un plugin que permita a los usuarios adjuntar ficheros directamente desde la nube de EducaMadrid.

- Seguridad de la cuenta de correo: Se debe implementar la capacidad de bloquear la cuenta de correo si se produce un número excesivo de intentos de acceso fallidos.

- Seguridad de los datos de la cuenta de correo: Se debe implementar la capacidad de cifrar los datos de la cuenta de correo para proteger la seguridad de los usuarios.

**Requisitos de Implementación**

- Plan de implementación: Se debe crear un plan de implementación que incluya los siguientes pasos:

    - Preparación del entorno de prueba

    - Pruebas de la nueva versión

    - Implementación en un servidor de prueba

    - Verificación de la estabilidad y seguridad del sistema

    - Implementación en el entorno de producción

- Documentación de la implementación: Se debe proporcionar documentación detallada de la implementación, incluyendo instrucciones para los usuarios y para los administradores del sistema.

- Pruebas de rendimiento: Se deben realizar pruebas de rendimiento para asegurarse de que la nueva versión se adapte a la demanda de los usuarios.

**Requisitos de Seguridad**

- Seguridad de la API: Se debe garantizar la seguridad de la API creada para restaurar contactos eliminados.

- Seguridad de la aplicación móvil: Se debe garantizar la seguridad de la aplicación móvil de correo.

- Seguridad de la integración con el cloud de EducaMadrid: Se debe garantizar la seguridad de la integración con el cloud de EducaMadrid.

- Seguridad de los datos de la cuenta de correo: Se debe garantizar la seguridad de los datos de la cuenta de correo, incluyendo la protección contra ataques de phishing y contra la pérdida de datos.

**Requisitos de Compatibilidad**

- Compatibilidad con navegadores: Se debe asegurar que la nueva versión  sea compatible con los navegadores más populares.

- Compatibilidad con sistemas operativos: Se debe asegurar que la nueva versión sea compatible con los sistemas operativos más populares.

- Compatibilidad con dispositivos móviles: Se debe asegurar que la nueva versión sea compatible con dispositivos móviles y que la aplicación móvil de correo funcione correctamente en diferentes plataformas.

**<!-- salto de página -->**

**Requisitos de Escalabilidad**

- Escalabilidad del sistema: Se debe asegurar que la nueva versión se pueda escalar para adaptarse a la demanda de los usuarios.

- Escalabilidad de la base de datos: Se debe asegurar que la base de datos se pueda escalar para adaptarse a la demanda de los usuarios.

- Escalabilidad de la infraestructura: Se debe asegurar que la infraestructura se pueda escalar para adaptarse a la demanda de los usuarios.

### IA en correoweb

##### Prueba de generación de resúmenes de correos (COR2)

Implementación de un sistema de generación de resúmenes de correos electrónicos dentro del aplicativo de correo de la plataforma educativa EducaMadrid que permita evaluar su viabilidad de cara a todos los usuarios. El sistema utilizará una instalación de IA local y cumplirá con los siguientes requisitos específicos.

**Requisitos Funcionales**

- Uso de Servidores de IA Locales

    - El sistema debe utilizar los servidores de IA locales para procesar los correos electrónicos y generar resúmenes.

- Modelo de IA Elegido por la Administración

    - La administración de EducaMadrid seleccionará el modelo de IA a utilizar. El sistema debe ser configurable para adaptarse al modelo elegido.

- Acceso Restringido a la Funcionalidad

    - Solo algunos usuarios, previamente autorizados, dispondrán de la funcionalidad de generación de resúmenes. La plataforma debe incluir un mecanismo de control de acceso para habilitar esta funcionalidad únicamente para los usuarios seleccionados.

- Generación Asíncrona  y bajo petición de Resúmenes

    - Los resúmenes de los correos electrónicos se generarán de manera asíncrona y bajo petición. Esto significa que el proceso de generación de resúmenes no debe afectar el rendimiento general del aplicativo de correo.

- Visualización de Resúmenes

    - Los resúmenes generados se mostrarán al principio de cada correo electrónico. Debe haber una indicación clara que identifique el texto como un resumen del correo original.

- Manejo Seguro de Datos

    - Todos los datos procesados y almacenados por el sistema deben manejarse utilizando protocolos seguros. Esto incluye el uso de conexiones cifradas (HTTPS) y el almacenamiento seguro de datos sensibles.

- Almacenamiento y Eliminación de Resúmenes

    - Los resúmenes generados se almacenarán en la base de datos del aplicativo de correo. Los resúmenes deben eliminarse automáticamente pasado un tiempo determinado, que será configurado por la administración.

**<!-- salto de página -->**

**Requisitos No Funcionales**

- Rendimiento

    - El sistema debe ser capaz de generar resúmenes de manera eficiente, sin causar retrasos significativos en la entrega de correos electrónicos.

- Escalabilidad

    - La solución debe ser escalable para manejar un aumento en el número de usuarios y correos electrónicos procesados.

- Seguridad

    - El sistema debe cumplir con las normativas de seguridad de datos aplicables, incluyendo la protección de datos personales y la prevención de accesos no autorizados.

- Mantenimiento

    - La solución debe ser fácil de mantener y actualizar, permitiendo cambios en el modelo de IA o en los parámetros de configuración sin interrupciones significativas en el servicio.

**Interfaz de Usuario**

- Indicación de Resumen

    - En la interfaz de usuario, los resúmenes deben estar claramente marcados con un texto o icono que indique que se trata de un resumen del correo original.

- Configuración de Usuarios

    - La administración debe tener una interfaz para habilitar o deshabilitar la funcionalidad de resúmenes para usuarios específicos.

**Consideraciones Adicionales**

- Documentación

    - Se debe proporcionar documentación completa sobre la implementación, configuración y uso del sistema.

- Soporte Técnico

    - Se debe asegurar el soporte técnico para resolver cualquier problema que surja durante la implementación y operación del sistema.

###### Redacción de correos (COR3)

Se solicita la creación de un plugin que integre la generación de correos electrónicos con IA en el correweb de EducaMadrid.

**Requisitos Funcionales**

- Compatibilidad con el aplicativo actual de correo: El plugin debe ser compatible con la versión actual y futuras del aplicativo de correoweb.

- Integración en el aplicativo: El plugin debe integrarse dentro del aplicativo correoweb, mostrando un botón al usuario en la pantalla de redacción de correo que muestre un modal para recibir las instrucciones para generar el correo con IA.

<!-- salto de página -->

- Modal de generación: El modal de generación debe disponer de las siguientes opciones:

    - Nombre remitente

    - Nombre destinatario

    - Estilo del correo

    - Longitud del correo

    - Creatividad

    - Idioma

- Ejemplos de solicitudes de correos: El modal de generación debe disponer de ejemplos de solicitudes de correos que se activarán según fechas, por ejemplo en navidades propondrá como ejemplo generar una felicitación navideña.

- Modo desarrollador: El plugin debe disponer de un modo desarrollador que muestre a los administradores los prompts de administrador y usuario enviados y la respuesta recibida del servidor.

- Integración con VLLM local: El plugin debe funcionar contra una instalación de VLLM local con el modelo elegido por EducaMadrid en los servidores de la plataforma.

- Almacenamiento de datos estadísticos: el plugin debe guardar en la base de datos del aplicativo todos los datos de las solicitudes de los usuarios.

- Usuarios del plugin: el plugin estará limitado por centros y por usuarios, de manera que se pueda solicitar la activación paulatina del mismo en distintos centros y a distintos grupos, como por ejemplo, para profesores.

- Limitaciones de uso: Existirán limitaciones de uso configurables por el administrador, como:

    - Número de tokens

    - Número de correos generados

    - Longitud del prompt de usuario...

**Requisitos de Interfaz**

- Interfaz de usuario: La interfaz de usuario del plugin debe ser clara y fácil de usar.

- Botón de generación: El botón de generación debe ser visible y fácil de acceder.

- Modal de generación: El modal de generación debe ser visible y fácil de acceder.

- Ejemplos de solicitudes de correos: Los ejemplos de solicitudes de correos deben ser visibles y fácil de acceder.

- Modo desarrollador: El modo desarrollador debe ser visible y fácil de acceder.

**Requisitos de Seguridad**

- Autenticación: El plugin debe requerir autenticación para acceder a los servicios de VLLM local.

- Autorización: El plugin debe requerir autorización para generar correos con IA.

- Cifrado de datos: Los datos generados por el plugin deben ser cifrados para proteger la seguridad de los usuarios.

- Seguridad de la base de datos: La base de datos del plugin debe ser segura y protegida contra ataques.

**Requisitos de Escalabilidad**

- Escalabilidad del plugin: El plugin debe ser escalable para adaptarse a la demanda de los usuarios.

- Escalabilidad de la base de datos: La base de datos del plugin debe ser escalable para adaptarse a la demanda de los usuarios.

- Escalabilidad de la infraestructura: La infraestructura del plugin debe ser escalable para adaptarse a la demanda de los usuarios.

**Requisitos de Compatibilidad**

- Compatibilidad con correoweb: El plugin debe ser compatible con la versión actual y futuras de correoweb.

- Compatibilidad con VLLM local: El plugin debe ser compatible con la instalación de VLLM local en los servidores de la plataforma.

- Compatibilidad con diferentes navegadores: El plugin debe ser compatible con diferentes navegadores y plataformas.

**Requisitos de Calidad**

- Calidad del código: El plugin debe tener código de alta calidad y mantenible.

- Calidad de la documentación: La documentación del plugin debe ser clara y concisa.

- Calidad del soporte: El soporte del plugin debe ser de alta calidad y eficiente.

###### Reescritura de correos (COR4)

Desarrollo de un plugin para el aplicativo de correo que integre inteligencia artificial (IA) en la reescritura de correos electrónicos. Este plugin permitirá a los usuarios mejorar la calidad de sus correos electrónicos mediante diversas opciones de reescritura y corrección.

**Objetivos**

- Desarrollar un plugin para el aplicativo de correo que integre IA en la reescritura de correos electrónicos.

- Asegurar la compatibilidad del plugin con la versión actual y futuras del aplicativo.

- Proporcionar una interfaz de usuario intuitiva y fácil de usar para la reescritura de correos.

- Implementar un modo desarrollador para los administradores.

- Integrar el plugin con una instalación local de VLLM en los servidores de la plataforma.

**Alcance**

- Desarrollo del plugin para el aplicativo de correoweb.

- Integración del plugin con la interfaz de redacción de correos.

- Implementación de opciones de reescritura y corrección de correos.

- Configuración de limitaciones de uso por parte del administrador.

- Implementación de un modo desarrollador para los administradores.

- Integración con una instalación local de VLLM.

**<!-- salto de página -->**

**Requisitos Funcionales**

- Compatibilidad

    - El plugin debe ser compatible con la versión actual del aplicativo de correoweb y futuras versiones.

    - El plugin debe pasar todas las pruebas de compatibilidad y funcionalidad en diferentes versiones del aplicativo de correo.

- Interfaz de Usuario

    - Botón en patalla de Redacción: Mostrar un botón en la pantalla de redacción de correo que abra un modal con el correo escrito y opciones de reescritura.

    - Botón en pantalla de generación con IA: Mostrar un botón dentro del plugin de redacción con IA para ir directamente a la pantalla de reescritura de un correo generado por IA.

    - Modal de Generación: El modal debe incluir las siguientes opciones:

        - Corregir gramática.

        - Corregir ortografía.

        - Reescribir más largo/corto.

        - Escribir con otro estilo (profesional, humano, creativo, etc.).

- Modo Desarrollador

    - Visualización de Prompts: Mostrar a los administradores los prompts de administrador y usuario enviados, así como la respuesta recibida del servidor.

    - Acceso Restringido: El modo desarrollador debe estar restringido a los administradores del sistema.

- Integración con VLLM

    - El plugin debe funcionar contra una instalación local de VLLM en los servidores de la plataforma.

    - El modelo de IA elegido por EducaMadrid debe ser utilizado para la reescritura de correos.

- Limitaciones de Uso

    - Configurables por el Administrador: Las siguientes limitaciones deben ser configurables por el administrador:

        - Número de tokens.

        - Número de reescrituras generadas.

        - Longitud del prompt de usuario.

**Requisitos No Funcionales**

- Rendimiento

    - El plugin debe tener un tiempo de respuesta aceptable para la generación de reescrituras de correos.

    - El plugin debe ser eficiente en el uso de recursos del servidor.

- Seguridad

    - La comunicación entre el plugin y la instalación local de VLLM debe ser segura.

    - Los datos de los usuarios deben ser manejados de acuerdo con las políticas de privacidad y seguridad de la plataforma.

- Usabilidad

    - La interfaz de usuario debe ser intuitiva y fácil de usar.

    - Las opciones de reescritura deben ser claras y accesibles para los usuarios.

### MEJORAS Y MANTENIMIENTO DEL SERVICIO DE WORDPRESS MULTISITE (WPM)

### Mantenimiento y Actualización de WordPress Multisite (WPM1)

**Requisitos**

- Se requiere actualizar la versión del aplicativo WordPress Multisite, incluyendo el core, temas y plugins, con la posibilidad de hacerlo por separado.

- El servicio debe ser parado por un tiempo inferior a 30 minutos.

- Se debe preparar un sistema en el servidor Git de EducaMadrid que permita automatizar las futuras subidas de versión del aplicativo con sus temas y plugins.

- Se debe considerar que hay un plugin que unifica los cambios del core y que los temas no están modificados, sino que cada tema tiene un tema hijo.

- El proceso de actualización debe ser realizado de manera segura y sin afectar la disponibilidad del sitio.

### Incorporación Automatizada de Licencias de Temas y Plugins (WPM2)

**Requisitos:**

- Se requiere trabajar en un sistema que permita incorporar las licencias de temas y plugins adquiridas de manera automatizada sin intervención de los usuarios en el entorno multisite.

- Se deben considerar plugins como PostGrid y Akismet como ejemplo de casos a resolver.

- El sistema debe ser capaz de leer y aplicar las licencias de manera automática, sin requerir intervención humana.

### Configuración del WAF de Forti (WPM3)

**Requisitos:**

- Se requiere trabajar conjuntamente con el departamento de sistemas para encontrar una configuración correcta del WAF de Forti que permita encontrar un equilibrio entre seguridad y experiencia de usuario.

- La configuración debe ser ajustada para permitir una experiencia de usuario óptima sin comprometer la seguridad del sitio.

### Reemplazo del Plugin WCcaptcha (WPM4)

**Requisitos:**

- Se requiere eliminar el plugin WCcaptcha del entorno y sustituirlo por una solución equivalente.

- La solución equivalente debe ser compatible con la versión actual del sitio y no afectar la experiencia de usuario.

<!-- salto de página -->

### Integración con el SSO de EducaMadrid (WPM5)

**Requisitos:**

- Se requiere integrar el aplicativo con el sso de EducaMadrid para el login de los usuarios

- Deberán maneterse todas las funcionalidades originales del aplicativo

- Se detectará el cierre de sesión en otros aplicativos provocando el cierre en el wordpress

- Deberá incorporar los mecanismos de 2FA

### MEJORAS Y MANTENIMIENTO DEL SERVICIO DE FORMULARIOS (FOR)

Adaptar y optimizar el entorno de formularios para mejorar su rendimiento y conectarlo con el SSO de EducaMadrid, asegurando una experiencia de usuario fluida y segura (FOR1).

**Requisitos Técnicos**

- Mantenimiento

    - Adaptar el entorno a la última versión del aplicativo base y todos los complementos instalados.

    - Asegurar la compatibilidad de todas las funcionalidades existentes con la nueva versión.

    - Realizar pruebas exhaustivas para verificar que la actualización no afecte negativamente el funcionamiento del sistema.

    - Adaptar la imagen institucional a la nueva versión del aplicativo.

- Mejora de Rendimiento de la Base de Datos

    - Optimizar el uso de la base de datos (BD) que actualmente incluye miles de tablas.

    - Implementar estrategias de indexación y particionamiento para mejorar el rendimiento de las consultas.

    - Realizar un análisis de rendimiento para identificar y eliminar tablas o datos redundantes.

- Script de Eliminación de Encuestas Antiguas

    - Crear un script que anualmente elimine todas las encuestas de años anteriores que cumplan con los criterios solicitados.

    - Asegurar que el script sea configurable para ajustar los criterios de eliminación según sea necesario.

    - Implementar mecanismos de respaldo antes de la eliminación de datos para evitar pérdidas accidentales.

- Conectar con el SSO de EducaMadrid

    - Integrar con el SSO de EducaMadrid.

    - Utilizar el script del aplicativo "Avisos" para detectar los cierres de sesión en otros aplicativos y reflejar estos cambios en formularios.

    - Asegurar que el flujo de autenticación y cierre de sesión sea coherente y seguro.

**Consideraciones Adicionales**

- Seguridad: Asegurar que todas las actualizaciones y optimizaciones no comprometan la seguridad del sistema.

- Usabilidad: Mantener la interfaz de usuario intuitiva y fácil de usar para los administradores y usuarios finales.

- Documentación: Proveer documentación detallada sobre los cambios realizados, incluyendo guías de actualización y optimización.

- Pruebas: Realizar pruebas exhaustivas para verificar que todas las funcionalidades y mejoras de rendimiento se implementen correctamente.

### MEJORAS Y MANTENIMIENTO EN EMPIEZA (EMP)

Mejorar el aplicativo EMPieza implementando nuevas funcionalidades y optimizando su rendimiento, con el fin de proporcionar una experiencia de usuario más eficiente y completa (EMP1).

**Requisitos Técnicos**

- Alta disponibilidad

    - Debido al uso del aplicativo se requiere cambiar la plataforma a una en alta disponibilidad de frontales del aplicativo. Se debe desacoplar el servicio de websocket para que disponga de su propio servidor al que se conecten los nuevos frontales del servicio.

- Administración de Bloques de Aplicaciones

    - Implementar la capacidad de agregar bloques de aplicaciones en la pantalla principal.

    - Permitir a los usuarios gestionar permisos para agregar bloques.

- Nuevas Funcionalidades y Bloques

    - Favoritos: Permitir a los usuarios añadir, modificar y eliminar enlaces destacados en su página principal de EMPieza.

    - Notas: Permitir a los usuarios añadir, modificar y eliminar notas con título y descripción, seleccionando el color de cada nota. Cada nota mostrará la fecha de creación y estará oculta por defecto.

    - Eventos de Retransmisión: Listar los eventos de retransmisión en los que el usuario está asociado.

    - Avisos: Mostrar el contenido de los avisos publicados desde la aplicación de avisos.

    - Boletines: Mostrar el contenido de los últimos boletines publicados en el canal oficial de EducaMadrid.

- Conexión con Aulas Virtuales

    - Permitir a los profesores consultar y gestionar a los usuarios matriculados en sus cursos, incluyendo sus roles.

    - Mostrar eventos de grupo o curso en el calendario que viene del aula virtual.

- Mejoras en la Gestión de Grupos

    - Dividir en listado de grupos con acciones generales y gestión de integrantes.

    - Permitir la creación de un grupo importando desde un archivo CSV.

    - Permitir buscar usuarios en LDAP aunque no pertenezcan a un centro.

    - Exportación e importación de grupos en CSV.

    - Permitir que un grupo sea público para que otros profesores del centro lo importen.

    - Permitir reutilizar un grupo que comparte otro usuario sin necesidad de importarlo.

<!-- salto de página -->

- Mejoras en el Calendario de EMPieza

    - Mostrar un calendario en la pantalla principal que se conecte con CalDAV y el calendario del correo del usuario.

    - Listado de eventos en calendarios.

    - Mostrar el origen del evento en el calendario de la portada.

    - Creación de eventos personales desde la pantalla principal.

    - Creación de eventos para grupos.

    - Etiquetas de colores para cada evento creado.

    - Nuevo apartado para sincronización de calendarios, permitiendo al usuario seleccionar qué calendario del correo y qué aula virtual sincronizar.

    - Permitir compartir el calendario con un grupo de usuarios con opciones de permisos.

    - Notificar por correo electrónico a un grupo de usuarios cuando se crea un evento en el calendario de ese grupo.

    - La sincronización de calendarios debe funcionar no solo entre las aulas virtuales multisite y el correoweb sino también entre las aulas virtuales moodlemisc y correoweb.

- Conexión con Mediateca

    - Crear una pantalla para consultar y gestionar las autorizaciones de un profesor en la mediateca.

- Mejoras en Retransmisiones

    - Crear un apartado donde los usuarios puedan crear salas de retransmisión de tipo Jitsi o Wowza.

    - Invitar a usuarios o grupos al evento.

    - Notificar a los usuarios por correo y crear un evento en sus calendarios.

    - Crear dinámicamente puntos de publicación en el servidor Wowza y eliminarlos al terminar la transmisión.

    - Tres tipos de interacción con el usuario: chat entre usuarios, formulario de preguntas y ninguna interacción.

    - Revisión completa de la presentación de las retransmisiones en directo.

    - Establecer un límite de tiempo para las videoconferencias de tipo Jitsi.

    - Dar la posibilidad de embeber una retransmisión en vivo tipo Wowza en cualquier página web.

- Mejora en el Rendimiento con Reinicio de Cursos

    - Crear un sistema que permita a los profesores seleccionar cursos en sus aulas virtuales para que no sean reiniciados en las operativas de verano.

- Actualización de Librerías

    - Actualizar y homogeneizar las versiones de jQuery y Bootstrap de toda la aplicación.

    - Revisar la maquetación y funcionalidad de todos los apartados de EMPieza.

- Preparación para IFRAME

    - Adaptar la aplicación para trabajar desde IFRAME en algunos servicios de la Plataforma, mostrando el contenido en modo "maximizado" y ocultando elementos de navegación.

- Mejora en la Comunicación con el Portal

    - Crear un método de API para recibir comunicaciones de cambio de contraseñas desde el Portal, detectando estos cambios en usuarios que hayan registrado credenciales para comunicaciones con otros aplicativos.

- Mensajería Interna del Aula Virtual

    - Mostrar la mensajería interna del aula virtual de un usuario dentro de EMPieza.

- Integración de Antivirus en Comparti2

    - Integrar un antivirus en Comparti2 para verificar los ficheros subidos por los usuarios.

- Log de cambios de contraseña

    - Se usará la bitácora de empieza para guardar un log con los cambios de contraseña de los usuarios

- Log de login en distintos servicios

    - Crear un sistema de logs de login de los usuarios en distintos servicios.

    - El log será consultable por parte de los usuarios

    - Debe crearse un endpoint donde los distintos servicios enviarán los datos de login de los usuarios.

- Crear sistema de notificaciones

    - Se requiere crear un sistema, consultable externamente mediante un endpoint securizado, el cual unifique las alertas relativas al usuario.

- Corrección y mejoras de ciber seguridad:

    - Realizar las tareas de mantenimiento y mejora necesarias para solucionar incidencias relacionadas con ciber seguridad.

- Gestión de Usuarios

    - Preparar el aplicativo para asumir poco a poco la gestión de usuarios que actualmente se realiza desde el portal educativo, permitiendo gestionar a los centros los usuarios que tengan asignados desde raíces.

**Consideraciones Adicionales**

- Seguridad: Asegurar que todas las nuevas funcionalidades y mejoras cumplan con las mejores prácticas de seguridad.

- Usabilidad: Mantener la interfaz de usuario intuitiva y fácil de usar para los administradores y usuarios finales.

- Pruebas: Realizar pruebas exhaustivas para verificar que todas las funcionalidades y mejoras se implementen correctamente.

### MEJORAS Y MANTENIMIENTO EN BUSCADOR DE AULAS Y CURSOS (BUS)

Crear un nuevo aplicativo que integre las funcionalidades de los dos aplicativos existentes: "Buscador de Aulas Virtuales" y "Buscador de Cursos". El nuevo aplicativo permitirá realizar búsquedas combinadas y proporcionar una experiencia de usuario más coherente y eficiente (BUS1).

**Requisitos Técnicos**

- Framework PHP

    - Utilizar el framework PHP que se está implantando en la plataforma para desarrollar el nuevo aplicativo en su versión más reciente.

    - Asegurar que el nuevo aplicativo siga las convenciones y mejores prácticas del framework seleccionado.

<!-- salto de página -->

- Funcionalidades del Nuevo Aplicativo

    - Búsqueda de Aulas Virtuales: Permitir la búsqueda de aulas virtuales por nombre del centro, código de centro, tipo de centro, localidad, etc.

    - Búsqueda de Cursos: Permitir la búsqueda de cursos en abierto por temática o título concreto.

    - Búsqueda Combinada: Permitir búsquedas combinadas que integren criterios de ambos aplicativos existentes. Por ejemplo, buscar un curso de matemáticas en un IES de Móstoles.

- Interfaz de Usuario

    - Diseño Intuitivo: Diseñar una interfaz de usuario intuitiva y fácil de usar que permita a los usuarios realizar búsquedas de manera sencilla.

    - Filtros y Opciones: Proveer filtros y opciones de búsqueda avanzada para permitir a los usuarios refinar sus búsquedas.

    - Resultados de Búsqueda: Mostrar los resultados de búsqueda de manera clara y organizada, permitiendo a los usuarios navegar fácilmente entre los resultados.

- Integración de Datos

    - Fuentes de Datos: Integrar las fuentes de datos de ambos aplicativos existentes para que el nuevo aplicativo pueda acceder a toda la información necesaria.

    - Consultas Eficientes: Optimizar las consultas a la base de datos para asegurar un rendimiento eficiente, especialmente en búsquedas combinadas.

- Seguridad

    - Sanitización de Entradas: Implementar funciones de sanitización para todos los campos de texto que reciben entradas del usuario.

    - Validación de Entradas: Implementar validaciones de entrada para asegurar que los datos recibidos cumplan con los formatos y restricciones esperados.

- Pruebas y Validación

    - Pruebas Funcionales: Realizar pruebas exhaustivas para asegurar que todas las funcionalidades del nuevo aplicativo funcionan correctamente.

    - Pruebas de Rendimiento: Realizar pruebas de rendimiento para asegurar que el nuevo aplicativo puede manejar un alto volumen de búsquedas sin degradar el rendimiento.

    - Pruebas de Seguridad: Realizar pruebas de seguridad para identificar y corregir cualquier vulnerabilidad potencial.

### MEJORAS Y MANTENIMIENTO DE LOS SERVICIOS DE RETRANSMISIÓN Y VIDEOCONFERENCIA (VID)

Mejorar y mantener los servicios de retransmisión y videoconferencia, asegurando un funcionamiento óptimo, una experiencia de usuario mejorada y la integración con otros sistemas de la plataforma EducaMadrid.

Para todos estos servicios hay que tener en cuenta estas consideraciones:

- **Seguridad**:

    - Asegurar que todas las actualizaciones y mejoras cumplan con las mejores prácticas de seguridad.

    - Implementar medidas de seguridad adicionales si es necesario.

- **Usabilidad**:

    - Mantener la interfaz de usuario intuitiva y fácil de usar para los administradores y usuarios finales.

    - Realizar pruebas de usabilidad para asegurar que las mejoras sean accesibles y fáciles de usar.

- **Pruebas**:

    - Realizar pruebas exhaustivas para verificar que todas las funcionalidades y mejoras se implementen correctamente.

    - Incluir pruebas de rendimiento, escalabilidad y seguridad.

### Mantenimiento de Wowza (VID1)

- Eliminar Retransmisiones Integradas en Mediateca:

    - Desactivar y eliminar la funcionalidad de retransmisiones integradas en el aplicativo Mediateca.

    - Asegurar que los usuarios no puedan acceder a esta funcionalidad obsoleta.

- Gestión Dinámica de Puntos de Publicación:

    - Implementar una interfaz en EMPieza que permita a los administradores gestionar dinámicamente los puntos de publicación.

    - Proveer documentación detallada sobre cómo configurar y gestionar estos puntos de publicación.

- Actualización del Aplicativo Wowza:

    - Actualizar Wowza a la última versión disponible.

    - Realizar pruebas exhaustivas para asegurar la compatibilidad y el correcto funcionamiento de todas las funcionalidades.

    - Proveer un informe detallado de los cambios realizados y las mejoras obtenidas.

### Mantenimiento de Jitsi (VID2)

- Actualización de JitsiMeet:

    - Actualizar JitsiMeet a la última versión disponible, conservando todas las funcionalidades actuales.

    - Realizar pruebas de compatibilidad y rendimiento.

- Personalización de Interfaz:

    - Implementar una "mosca" o marca de agua con el logotipo de EducaMadrid.

    - Añadir logotipos y favicon personalizados.

    - Ocultar opciones de grabación para evitar el uso no autorizado.

- Integración con Sistema Centralizado de Avisos:

    - Integrar JitsiMeet con el sistema centralizado de avisos de EducaMadrid para notificar a los usuarios sobre eventos y actualizaciones.

    - Proveer una interfaz para que los administradores puedan gestionar estos avisos.

- Mantenimiento de Instalaciones Diferentes:

    - Privada: Asegurar que solo los usuarios de EducaMadrid puedan acceder a esta instalación.

    - Semi-privada: Permitir el acceso a usuarios de EducaMadrid e invitados, con controles de acceso adecuados.

    - Moodle: Asegurar que el acceso a JitsiMeet desde Moodle sea exclusivo y compatible con el cambio de modo (oscuro/claro) de las Aulas Virtuales de EducaMadrid.

- Renovación de la Página Principal del Servicio (Aplicativo “Balanceador”):

    - Actualizar el aplicativo balanceador a PHP 8.

    - Optimizar el sistema de distribución de carga entre los servidores del aplicativo (instalaciones Privada y Semi-privada).

    - Realizar pruebas de rendimiento y escalabilidad.

- Actualización de Servidores:

    - Realizar cambios de interfaz para mejorar la usabilidad y la experiencia del usuario.

    - Asegurar la conectividad con el balanceador.

    - Actualizar la base de datos del balanceador para reflejar los cambios realizados.

    - Actualizar el plugin Moodle para asegurar la compatibilidad con las nuevas versiones de Moodle.

    - Implementar un sistema de recogida dinámica del estado de carga de cada servidor y guardar esta información en la base de datos.

### Big Blue Button (BBB) (VID3)

- Mantenimiento de la Instalación:

    - Mantener la instalación del sistema de videoconferencias BigBlueButton con Greenlight v3 (Ruby on Rails/React).

    - Realizar actualizaciones de seguridad y mantenimiento regular.

- Adaptación al Entorno EducaMadrid:

    - Dotar al aplicativo del interfaz institucional de EducaMadrid.

    - Limitar las características a las solicitadas por los administradores de EducaMadrid.

- Integración con Moodle:

    - Instalar y configurar el módulo de BigBlueButton en Moodle.

    - Permitir a los usuarios de tipo profesor grabar las conferencias y establecer una fecha de caducidad de las grabaciones por cada centro.

    - Asegurar que los alumnos puedan descargar o consultar las grabaciones de conferencias.

- Personalización de Greenlight:

    - Adaptar la aplicación Greenlight a la imagen institucional de EducaMadrid.

    - Eliminar los enlaces directos a la página de autenticación del panel de administración de Greenlight.

    - Crear elementos personalizados como logotipo específico, PDF general de presentación y favicon.

- Restricciones de Acceso:

    - No permitir el acceso directo a las presentaciones y vídeos de las grabaciones.

    - No permitir el acceso al panel de administración de Greenlight por parte de los usuarios.

    - Asegurar que los usuarios puedan utilizar BigBlueButton únicamente a través de las Aulas Virtuales de EducaMadrid.

- Script de Grabaciones:

    - Añadir un script que permita disponer de las grabaciones de salas con pizarra de un único fichero descargable con la conferencia completa.

### Peertube (VID4)

- Mantenimiento y Monitorización:

    - Mantener y monitorizar la instancia de PeerTube para la realización de emisiones en directo con previsión de alta participación (2000 o más usuarios conectados de manera simultánea).

    - Implementar herramientas de monitorización para asegurar el correcto funcionamiento del servicio.

- Inserción de Retransmisiones mediante IFRAME:

    - Permitir la inserción de retransmisiones desde la plataforma PeerTube mediante IFRAME.

    - Asegurar que solo los administradores puedan acceder directamente a las retransmisiones.

    - Mostrar un reproductor con imagen personalizada (imagen institucional que permita identificar la Plataforma Educativa como origen de la retransmisión).

- Evaluar la necesidad del servicio y proceder a su retirada controlada en caso requerido.

- Entornos de Visualización:

    - Desde el AV (Moodle): Permitir la visualización de retransmisiones de tipo PeerTube desde el Aula Virtual de Moodle.

    - Desde la Mediateca de EducaMadrid: Permitir la visualización de retransmisiones de tipo PeerTube desde la Mediateca de EducaMadrid.

### MEJORAS Y MANTENIMIENTO DEL SERVICIO DE ANIMALANDIA (ANI)

Mejorar la seguridad, rendimiento y funcionalidad del aplicativo Animalandia, desarrollado en PHP, adaptándolo a las últimas versiones y mejores prácticas de desarrollo (ANI1).

**Requisitos Técnicos**

- Mejora de Seguridad: Adaptación a la Última Versión Estable de PHP

    - Actualización de PHP: Adaptar el aplicativo a la última versión estable de PHP.

    - Pruebas de Compatibilidad: Realizar pruebas exhaustivas para asegurar que todas las funcionalidades del aplicativo son compatibles con la nueva versión de PHP.

    - Depuración de Código: Depurar y corregir cualquier error o advertencia que aparezca al ejecutar el aplicativo con la nueva versión de PHP.

- Mejora de Rendimiento: Optimización del Uso de la Base de Datos y Consultas

    - Análisis de Consultas: Realizar un análisis detallado de las consultas a la base de datos para identificar aquellas que pueden ser optimizadas.

    - Índices y Claves: Crear y optimizar índices y claves en la base de datos para mejorar el rendimiento de las consultas.

    - Caché: Implementar mecanismos de caché para almacenar temporalmente los resultados de consultas frecuentes.

    - Consultas Eficientes: Reescribir consultas ineficientes para mejorar su rendimiento.

    - Pruebas de Rendimiento: Realizar pruebas de rendimiento antes y después de las optimizaciones para medir el impacto de los cambios.

<!-- salto de página -->

- Mejora de Seguridad: Sanitización de Campos de Texto

    - Sanitización de Entradas: Implementar funciones de sanitización para todos los campos de texto que reciben entradas del usuario.

    - Escapado de Datos: Asegurar que todos los datos que se insertan en la base de datos sean escapados adecuadamente para evitar inyecciones SQL.

    - Validación de Entradas: Implementar validaciones de entrada para asegurar que los datos recibidos cumplan con los formatos y restricciones esperados.

- Mejora de Seguridad: Control de Cookies y Carga de Scripts Estadísticos

    - Consentimiento del Usuario: Implementar un mecanismo que permita al usuario aceptar o rechazar el uso de cookies y scripts estadísticos.

    - Configuración de Cookies: Configurar las cookies para que solo se carguen si el usuario ha dado su consentimiento explícito.

    - Carga Condicional de Scripts: Asegurar que los scripts estadísticos solo se carguen si el usuario ha aceptado el uso de cookies analíticas.

    - Interfaz de Consentimiento: Crear una interfaz de usuario clara y fácil de usar para que los usuarios puedan gestionar sus preferencias de cookies.

- Mejora de Seguridad: Actualización de jQuery y Cambios de Compatibilidad

    - Actualización de jQuery: Actualizar jQuery a la última versión estable.

    - Depuración de Código: Identificar y corregir cualquier error o advertencia que aparezca al ejecutar el aplicativo con la nueva versión de jQuery.

    - Cambios de Compatibilidad: Realizar los cambios necesarios en el código para asegurar la compatibilidad con la nueva versión de jQuery.

    - Pruebas de Funcionalidad: Realizar pruebas exhaustivas para asegurar que todas las funcionalidades que dependen de jQuery siguen funcionando correctamente.

### MEJORAS Y MANTENIMIENTO EN LA SINCRONIZACIÓN DE USUARIOS (SYN)

Optimizar el proceso actual de sincronización de cuentas de usuarios mediante la mejora de los scripts existentes, la automatización de tareas y la integración de nuevos tipos de usuarios. El objetivo es minimizar la intervención manual y asegurar una sincronización eficiente y precisa. Es muy importante mantener actualizada la BBDD “ldap plano” con los cambios de raíces ya que es la que se emplea para alimentar de usuarios otros aplicativos como cloud o aulas virtuales (SYN1).

**Requisitos Técnicos**

- Optimización de Scripts de Sincronización

    - Análisis de Scripts: Realizar un análisis detallado de los scripts de sincronización existentes para identificar áreas de mejora.

    - Optimización de Código: Optimizar el código de los scripts para mejorar su eficiencia y rendimiento.

    - optimización de la base de datos: Crear los índices necesarios en la BBDD ldap plano para que las consultas se optimicen.

    - Pruebas de Rendimiento: Realizar pruebas de rendimiento para medir el impacto de las optimizaciones.

- Desarrollo de Scripts de Sincronización de Profesores y Alumnos

    - Exportación de Datos: Desarrollar scripts para sincronizar profesores y alumnos con datos provenientes de una exportación periódica de la BD de Raíces.

    - Automatización: Automatizar el proceso de sincronización para que se realice de manera periódica sin intervención manual.

    - Validación de Datos: Implementar mecanismos de validación para asegurar la integridad y precisión de los datos sincronizados.

- Integración con Cohortes de las AV

    - Generación Anual de Cohortes: Desarrollar scripts para generar anualmente las cohortes correspondientes a las AV.

    - Actualización Diaria: Actualizar las cohortes a diario con la información alimentada en la BD de Raíces.

    - Automatización: Automatizar el proceso de actualización para que se realice de manera diaria sin intervención manual.

- Adaptación de Tablas con Vistas para EMPieza y ConsultasLDAP

    - Actualización de Vistas: Adaptar las tablas con vistas para el aplicativo EMPieza y del aplicativo ConsultasLDAP.

    - Consistencia de Datos: Asegurar que las vistas reflejen de manera precisa y consistente los datos sincronizados.

    - Pruebas de Funcionalidad: Realizar pruebas exhaustivas para asegurar que las vistas funcionen correctamente con los datos sincronizados.

- Integración de Entradas al Cloud de EducaMadrid

    - Revisión de Scripts: Revisar el script para buscar fallos cuando se hacen inserciones masivas en el cloud.

    - Optimización de Inserciones: Optimizar el script para manejar inserciones masivas de manera eficiente y sin errores.

    - Pruebas de Inserción: Realizar pruebas exhaustivas para asegurar que las inserciones masivas se realicen correctamente.

    - Actualización Diaria: Actualizar los usuarios a diario con la información alimentada en la BD de Raíces, creando los grupos de los centros si fueran necesarios.

- Integración de Usuarios de Enseñanzas Superiores

    - Identificación de Usuarios: Identificar y sincronizar usuarios de enseñanzas superiores que no constan en Raíces.

    - Automatización: Automatizar el proceso de sincronización para que se realice de manera periódica sin intervención manual.

- Sincronización entre LDAP y Tabla Sincro de Centros Privados

    - Desarrollo de Scripts: Desarrollar scripts para sincronizar entre LDAP y la tabla sincro de centros privados.

    - Automatización: Automatizar el proceso de sincronización para que se realice de manera periódica sin intervención manual.

    - Validación de Datos: Implementar mecanismos de validación para asegurar la integridad y precisión de los datos sincronizados.

- Integración de Docentes/No Docentes sin Horario

    - Web Scrapping: Desarrollar técnicas de web scraping para obtener los datos de docentes/no docentes sin horario desde Raíces.

    - Integración en Plataforma: Integrar estos datos en la Plataforma de EducaMadrid.

    - Automatización: Automatizar el proceso de integración para que se realice de manera periódica sin intervención manual.

- Sincronizador de Catálogos Classrooms, EducationalLevels y Otras Estructuras de Datos Auxiliares

    - Desarrollo de Scripts: Desarrollar scripts para sincronizar catálogos como classrooms, educational levels y otras estructuras de datos auxiliares.

    - Automatización: Automatizar el proceso de sincronización para que se realice de manera periódica sin intervención manual.

    - Validación de Datos: Implementar mecanismos de validación para asegurar la integridad y precisión de los datos sincronizados.

- Sincronización de Cuentas Tic

    - Desarrollo de Scripts: Desarrollar scripts para sincronizar cuentas Tic.

    - Automatización: Automatizar el proceso de sincronización para que se realice de manera periódica sin intervención manual.

    - Validación de Datos: Implementar mecanismos de validación para asegurar la integridad y precisión de los datos sincronizados.

- Carga de Tablas de Centros desde LDAP y CSV

    - Desarrollo de Scripts: Desarrollar scripts para cargar las tablas de centros desde LDAP y CSV.

    - Automatización: Automatizar el proceso de carga para que se realice de manera periódica sin intervención manual.

    - Validación de Datos: Implementar mecanismos de validación para asegurar la integridad y precisión de los datos cargados.

- Borrado Masivo de Relaciones entre Usuarios y Centros

    - Script de Borrado: Desarrollar un script para realizar un borrado masivo de la relación entre usuarios y centros en todos los aplicativos de la plataforma (Aula Virtual, Cloud, EMPieza, etc.).

    - Automatización: Automatizar el proceso de borrado para que se realice al inicio de cada curso sin intervención manual.

    - Validación de Datos: Implementar mecanismos de validación para asegurar que el borrado se realice correctamente sin afectar datos importantes.

- Mejorar el tratamiento de las bajas producido desde el aplicativo Raíces:

    - Desarrollo de Scripts: Desarrollar scripts para identificar las bajas producidas en raíces y tratarlas dentro de la sincronización de usuarios.

    - Automatización: Automatizar el proceso de identificación y tratamiento de bajas.

    - Validación de Datos: Implementar mecanismos de validación para asegurar la integridad y precisión de los datos sincronizados.

- Mejora en el tratamiento de los datos de usuarios en estado ‘leaving’:

    - Desarrollo de Scripts: Desarrollar scripts para el tratamiento de los usuarios marcados en el aplicativo central como leaving y propagar los cambios a todos los aplicativos vinculados.

    - Automatización: Automatizar el proceso de sincronización para que se realice de manera periódica sin intervención manual.

    - Validación de Datos: Implementar mecanismos de validación para asegurar la integridad y precisión de los datos sincronizados.

- Incorporar los IDS de usuarios de EducaMadrid en raíces

    - API de lectura de ids: Desarrollar una api, que se consultará desde raíces, con la que se encontrará el id de un usuario de EducaMadrid partiendo de su NIA o NIF

### MEJORAS Y MANTENIMIENTO DEL PORTAL CAU (CAU)

Actualización y adaptación de la última versión del aplicativo utilizado en el Portal CAU. Esta actualización debe mantener las modificaciones actuales, la imagen institucional, y asegurar que los mecanismos de generación de correos y autoasignación de incidencias sigan funcionando correctamente (CAU1).

**Objetivos**

- Actualizar el aplicativo a la última versión disponible.

- Adaptar la nueva versión del aplicativo al entorno del Portal CAU.

- Mantener todas las modificaciones y personalizaciones actuales.

- Preservar la imagen institucional del Portal CAU.

- Asegurar que los mecanismos de generación de correos y autoasignación de incidencias sigan funcionando correctamente.

**Alcance**

- Actualización a la última versión.

- Adaptación de la nueva versión al entorno del Portal CAU.

- Mantenimiento de las modificaciones y personalizaciones actuales.

- Preservación de la imagen institucional.

- Verificación y ajuste de los mecanismos de generación de correos y autoasignación de incidencias.

**Requisitos Funcionales**

- Actualización

    - Versión Actual: Identificar la versión actual en uso.

    - Última Versión: Descargar e instalar la última versión disponible.

    - Comprobación de requisitos: asegurarse que se cumplan los requisitos de la nueva versión y realizar las actualizaciones del sistema necesarias para cumplir dichos requisitos.

    - Compatibilidad: Asegurar la compatibilidad de la nueva versión con el entorno del Portal CAU.

- Adaptación al Entorno del Portal CAU

    - Mantenimiento de Modificaciones: Mantener todas las modificaciones y personalizaciones actuales realizadas.

    - Imagen Institucional: Preservar la imagen institucional del Portal CAU, incluyendo logotipos, colores y estilos de diseño.

    - Configuración: Ajustar la configuración para que se adapte al entorno del Portal CAU.

- Mecanismos de Generación de Correos

    - Funcionalidad: Asegurar que los mecanismos de generación de correos sigan funcionando correctamente.

    - Pruebas: Realizar pruebas exhaustivas para verificar que todos los correos generados se envíen correctamente.

    - Configuración: Ajustar la configuración de correo en la nueva versión del aplicativo si es necesario.

- Autoasignación de Incidencias

    - Funcionalidad: Asegurar que el mecanismo de autoasignación de incidencias siga funcionando correctamente.

    - Pruebas: Realizar pruebas exhaustivas para verificar que las incidencias se asignen automáticamente a los usuarios correctos.

    - Configuración: Ajustar la configuración de autoasignación en la nueva versión si es necesario.

### MEJORAS Y MANTENIMIENTO DE EDUCASAAC (EDU)

Refactorización del aplicativo EducaSaac con el objetivo de solucionar problemas de seguridad en HTML, PHP y JavaScript. El objetivo es mejorar la seguridad del aplicativo, protegiendo los datos y las operaciones realizadas por los usuarios (EDU1).

**Requisitos Funcionales**

- Sanitización de Entradas

    - Todas las entradas de usuario en HTML, PHP y JavaScript deben ser sanitizadas para prevenir inyecciones de código, XSS (Cross-Site Scripting) y otros ataques comunes.

    - Implementar funciones de sanitización en PHP para limpiar datos de formularios, URLs y otros puntos de entrada.

- Escapado de Salidas

    - Asegurar que todas las salidas de datos en HTML, PHP y JavaScript estén adecuadamente escapadas para prevenir XSS.

    - Utilizar funciones de escapado en PHP para datos que se muestran en la interfaz de usuario.

- Gestión de Sesiones Segura

    - Implementar medidas de seguridad para la gestión de sesiones, incluyendo la regeneración de IDs de sesión y la configuración de cookies seguras.

    - Asegurar que las sesiones expiren después de un período de inactividad razonable.

- Validación de Datos

    - Validar todos los datos de entrada en el servidor (PHP) antes de procesarlos o almacenarlos en la base de datos.

    - Utilizar validaciones tanto en el lado del cliente (JavaScript) como en el lado del servidor (PHP) para asegurar la integridad de los datos.

- Protección contra CSRF (Cross-Site Request Forgery)

    - Implementar tokens CSRF en todas las solicitudes que modifiquen el estado del servidor.

    - Asegurar que los tokens CSRF sean únicos y válidos solo para la sesión actual del usuario.

- Uso de HTTPS

    - Asegurar que todas las comunicaciones entre el cliente y el servidor se realicen a través de HTTPS para proteger los datos en tránsito.

    - Configurar el servidor para redirigir automáticamente todas las solicitudes HTTP a HTTPS.

- Control de Acceso

    - Implementar un sistema de control de acceso basado en roles para asegurar que solo los usuarios autorizados puedan acceder a ciertas funcionalidades y datos.

    - Utilizar permisos y roles en PHP para restringir el acceso a diferentes partes del aplicativo.

### MEJORAS Y MANTENIMIENTO DEL CLOUD (CLO)

### Evolución y actualización del servicio de Cloud (CLO1)

Evolucionar el servicio de cloud instalando versiones actualizadas del aplicativo y del editor colaborativo, mejorando la funcionalidad, seguridad y usabilidad del sistema.

**Requisitos Técnicos**

- Actualización

    - Actualización completa: Migración de todos los datos del sistema previo a la nueva versión del aplicativo, incluyendo archivos, configuraciones, preferencias, modificaciones previas y comparticiones.

    - Script de subida de versión: Crear un script para adaptar los datos de las cuentas de EducaMadrid al nuevo sistema, clasificadas por tipos de usuario y centros. El script debe ser robusto y capaz de manejar grandes volúmenes de datos sin interrupciones.

    - Verificación de Datos: Implementar mecanismos de verificación para asegurar que todos los datos se han actualizado correctamente y sin corrupción.

- Actualización de Paquetes

    - Actualización de PHP: Actualizar PHP a la versión más reciente compatible el aplicativo.

    - Actualización de Apache: Actualizar Apache a la versión más reciente compatible con el aplicativo.

    - Otros Paquetes: Actualizar otros paquetes necesarios (por ejemplo, bases de datos, extensiones PHP) para asegurar la compatibilidad y rendimiento del nuevo sistema.

    - Pruebas de Compatibilidad: Realizar pruebas exhaustivas para asegurar que todas las actualizaciones son compatibles con el nuevo sistema y no introducen nuevos problemas.

- Script para Cambios de Nombres de Centros

    - Script de Cambio de Nombres: Crear un script para cambiar los nombres de los centros, modificando las cuentas institucionales principales y derivadas por las nuevas y migrando sus datos. El script debe ser capaz de manejar cambios en grandes volúmenes de datos sin interrupciones.

    - Verificación de Cambios: Implementar mecanismos de verificación para asegurar que todos los cambios se han realizado correctamente y sin corrupción.

- Script para borrado de usuarios

    - Script de borrado de usuarios: Crear un script para eliminar del aplicativo los usuarios indicados. Debe eliminar todo rastro del usuario en la base de datos y sus ficheros. Si se trata de una cuenta institucional deben eliminarse también sus cuentas secundarias.

- Mecanismo Centralizado de Lanzamiento de Avisos

    - Integración con EducaMadrid: Incluir un mecanismo centralizado de lanzamiento de avisos de EducaMadrid, asegurando que los avisos se envíen de manera oportuna y segura.

- Instalación de Formularios

    - Instalación y Configuración: Instalar y configurar los formularios sencillos dentro del aplicativo para mejorar la funcionalidad del sistema. Los formularios deben ser personalizables y fáciles de usar.

    - Documentación: Proveer documentación detallada sobre el uso de los formularios.

- Mejoras en Estadísticas

    - Nuevas Métricas: Implementar nuevas métricas para proporcionar información más detallada y útil sobre el uso del servicio.

    - Interfaz de Estadísticas: Mejorar la interfaz de estadísticas para hacerla más intuitiva y fácil de usar.

    - Exportación de Datos: Permitir la exportación de datos estadísticos en formatos comunes (CSV, JSON, etc.).

- Mejora de Seguridad

    - Restricciones de Compartición: Evitar que las cuentas de alumnos puedan crear enlaces externos; solo deben compartir con usuarios del aplicativo. Implementar restricciones de compartición en el nivel de usuario y grupo.

- Sistema de Comparticiones por Centro

    - Espacios de Compartición: Crear un sistema que permita que cada centro disponga de un espacio de comparticiones solo entre usuarios de su centro, teniendo una sola instalación del aplicativo. Los espacios deben ser aislados y seguros.

    - Configuración de Grupos: Permitir la configuración de grupos de usuarios por centro para facilitar la gestión de comparticiones. La gestión de los grupos se realizará de manera externa desde empieza.

- Optimización de Rendimiento

    - Problemas de Autocompletar: Buscar soluciones para optimizar los problemas de rendimiento cuando se intenta compartir y se utilizan los campos de tipo autocompletar nombres de usuarios. Implementar mecanismos de caché y optimización de consultas.

    - Pantalla de Gestión de Usuarios: Solucionar problemas de rendimiento en la pantalla de gestión de usuarios. Optimizar las consultas y la carga de datos.

    - Escalabilidad: Adaptar el aplicativo para dar soporte a un número creciente de usuarios. Implementar estrategias de escalabilidad horizontal y vertical.

- Personalización de la Interfaz

    - Elementos Gráficos: Adaptar la interfaz para incluir los elementos gráficos distintivos de la Plataforma Educativa: favicon personalizado, logotipo, colores. La personalización se llevará a cabo tanto en el aplicativo como en el editor colaborativo.

    - Temas Personalizados: Crear temas personalizados para el aplicativo y el editor colaborativo que reflejen la identidad visual de EducaMadrid.

- Limpieza del Repositorio

    - Eliminación de Ficheros: Realizar una limpieza del repositorio y eliminar los ficheros innecesarios correspondientes a la página de inicio previa a la autenticación contra LDAP. Asegurar que no se eliminen datos importantes.

    - Optimización de Espacio: Optimizar el uso del espacio en disco eliminando archivos temporales y duplicados.

- Mejora de la Usabilidad

    - Bloque de Compartir: Evitar en el bloque de compartir elementos que los usuarios compartan sin ser conscientes de ello, contenidos privados alojados en una carpeta compartida. Implementar notificaciones y confirmaciones adicionales.

    - Interfaz Intuitiva: Mejorar la interfaz de usuario para hacerla más intuitiva y fácil de usar, especialmente para usuarios no técnicos.

- Integración con SSO

    - Autenticación Unificada: Integra el aplicativo con el SSO para unificar el proceso de autenticación. Asegurar que la integración sea segura y eficiente.

    - Sincronización de Usuarios: Implementar mecanismos de sincronización de usuarios entre el SSO y el aplicativo para asegurar que los datos de usuario estén siempre actualizados.

- Mantenimiento para conexión con aplicaciones relacionadas

    - Android/IOS App y Desktop Client (Windows, Linux y Macos): Mantener la compatibilidad con el aplicativo móvil con las nuevas versiones del aplicativo web.

### IA en cloud (CLO2)

Integración de inteligencia artificial (IA) en el aplicativo Cloud de la plataforma EducaMadrid. Este proyecto incluye un estudio de viabilidad de la instalación de una solución de IA conveniente, la creación de un Retrieval-Augmented Generation (RAG) con documentos del usuario, y la implementación de un chatbot para realizar consultas y tareas sobre los documentos del usuario.

**Objetivos**

- Realizar un estudio de las posibilidades de implantación de IA en el aplicativo Cloud.

- Instalar la solución de IA más conveniente para el servicio.

- Crear un RAG con los documentos del usuario en una base de datos vectorizada.

- Implementar un chatbot para realizar consultas y tareas sobre los documentos del usuario.

- Asegurar que los usuarios solo puedan hacer consultas sobre sus propios documentos.

- Limitar el acceso a las opciones de IA a ciertos perfiles y centros, con posibilidad de ampliación si fuera necesario.

- Indexar solo los documentos que el usuario solicite en la base de datos vectorizada.

**Alcance**

- Estudio de viabilidad de la integración de IA.

- Selección e instalación de la solución de IA más conveniente.

- Configuración de una base de datos vectorizada para el RAG.

- Desarrollo e implementación del chatbot.

- Configuración de permisos y limitaciones de acceso a las opciones de IA.

- Indexación selectiva de documentos en la base de datos vectorizada.

**Requisitos Funcionales**

- Estudio de Viabilidad

    - Análisis de Necesidades: Realizar un análisis de las necesidades y requisitos específicos de la plataforma EducaMadrid.

    - Evaluación de Soluciones: Evaluar diferentes soluciones de IA disponibles en el mercado y su compatibilidad con el aplicativo.

    - Informe de Viabilidad: Proveer un informe detallado sobre la viabilidad de la integración de IA en el aplicativo.

- Instalación de la Solución de IA

    - Selección de la Solución: Seleccionar la solución de IA más conveniente para el servicio.

    - Instalación en Máquinas con GPU: Instalar el modelo de IA elegido en las máquinas con GPU de la plataforma.

    - Configuración Inicial: Realizar la configuración inicial necesaria para la operación del modelo de IA.

- Creación del RAG

    - Base de Datos Vectorizada: Crear una base de datos vectorizada para almacenar los documentos del usuario.

    - Indexación Selectiva: Permitir que los usuarios soliciten la indexación de sus documentos en la base de datos vectorizada.

    - Seguridad de Datos: Asegurar que los documentos indexados solo sean accesibles por el usuario que los solicitó.

- Implementación del Chatbot

    - Interfaz de Usuario: Desarrollar una interfaz de usuario para el chatbot dentro del aplicativo.

    - Consultas y Tareas: Permitir al chatbot realizar consultas y tareas sobre los documentos del usuario.

    - Seguridad de Acceso: Asegurar que el chatbot solo pueda acceder a los documentos del usuario que lo solicita.

- Limitaciones de Acceso

    - Perfiles y Centros: Limitar el acceso a las opciones de IA a ciertos perfiles y centros.

    - Ampliación de Acceso: Proveer la posibilidad de ampliar el acceso a las opciones de IA si fuera necesario.

    - Control de Carga: Implementar mecanismos de control de carga y rendimiento para evitar sobrecargas en el sistema.

**Requisitos No Funcionales**

- Rendimiento

    - El sistema debe tener un tiempo de respuesta aceptable para las consultas y tareas realizadas por el chatbot.

    - El sistema debe ser eficiente en el uso de recursos del servidor.

- Seguridad

    - La comunicación entre el chatbot y la base de datos vectorizada debe ser segura.

    - Los datos de los usuarios deben ser manejados de acuerdo con las políticas de privacidad y seguridad de la plataforma.

- Usabilidad

    - La interfaz de usuario del chatbot debe ser intuitiva y fácil de usar.

    - Las opciones de consulta y tarea deben ser claras y accesibles para los usuarios.

- Mantenimiento

    - El sistema debe ser fácil de mantener y actualizar.

    - La documentación del sistema debe ser completa y clara.

### MEJORAS Y MANTENIMIENTO DEL SERVICIO BUZON ANÓNIMO (BAN)

Soporte y mantenimiento de la web asociada al Plan Regional contra las Drogas de la Comunidad de Madrid. El objetivo es asegurar que la web cumpla con las necesidades del proyecto, sea segura, y esté alineada con la imagen institucional de EducaMadrid (BAN1).

**Requisitos Funcionales**

- Gestión del Listado de Centros Asociados

    - Implementar un sistema para gestionar el listado de centros asociados al Plan Regional contra las Drogas.

    - Permitir la adición, edición y eliminación de centros según las necesidades del proyecto.

    - Asegurar que la información de los centros sea actualizada y precisa.

- Personalización de la Imagen Institucional

    - Adaptar la web a la imagen institucional de EducaMadrid, incluyendo logotipos, enlaces y pie de página.

    - Asegurar que la web sea compatible con el cambio de modo (claro/oscuro) de la Plataforma Educativa.

    - Mantener la coherencia visual y funcional con el resto de la plataforma EducaMadrid.

**Requisitos No Funcionales**

- Seguridad

    - Realizar mantenimientos preventivos de seguridad para proteger la web contra vulnerabilidades y ataques.

    - Implementar las mejores prácticas de seguridad y aplicar parches de seguridad de manera regular.

    - Realizar pruebas de seguridad periódicas para identificar y corregir posibles vulnerabilidades.

- Usabilidad

    - La interfaz de la web debe ser intuitiva y fácil de usar para los administradores y usuarios finales.

    - Asegurar que la web sea accesible para usuarios con discapacidades, cumpliendo con las normativas de accesibilidad web.

- Mantenimiento

    - La web debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

    - Asegurar que la web esté adaptada a la última versión de PHP y sea compatible con las versiones actuales de otros paquetes del sistema.

- Compatibilidad

    - La web debe ser compatible con diferentes navegadores y dispositivos, asegurando un buen rendimiento y una experiencia de usuario óptima.

### MEJORAS Y MANTENIMIENTO DE DTIC (DTIC)

Corrección de problemas de seguridad, el mantenimiento de incidencias y la incorporación de nuevas funcionalidades en el aplicativo de Dotaciones TIC (DTIC) en la plataforma EducaMadrid. El objetivo es mejorar la seguridad, estabilidad y funcionalidad del aplicativo, asegurando que cumpla con los estándares actuales y las necesidades de la plataforma (DTIC1).

**Requisitos Funcionales**

- Corrección de Problemas de Seguridad

    - Identificar y corregir todas las vulnerabilidades de seguridad presentes en el aplicativo DTIC.

    - Implementar las mejores prácticas de seguridad para proteger el aplicativo contra ataques conocidos y futuros.

    - Realizar pruebas de seguridad y aplicar parches de seguridad de manera regular.

- Mantenimiento de Incidencias

    - Resolver todas las incidencias encontradas en el aplicativo DTIC.

    - Documentar cada incidencia y su correspondiente solución para futuras referencias.

- Nuevas Funcionalidades

    - Mover Componentes de Modalidad

        - Permitir a los administradores mover componentes de una modalidad a otra dentro del aplicativo DTIC.

    - Cambiar Destinatarios de Componentes

        - Permitir a los administradores cambiar los destinatarios de los componentes dentro del aplicativo DTIC.

    - Fusionar Modalidades

        - Permitir a los administradores fusionar dos o más modalidades en una sola dentro del aplicativo DTIC.

    - Destinatarios de correo

        - Cambiar el sistema que identifica los destinatarios de los correos cuando se contestan las incidencias.

**Requisitos No Funcionales**

- Seguridad

    - Implementar las mejores prácticas de seguridad para proteger el aplicativo contra vulnerabilidades y ataques.

    - Realizar pruebas de seguridad y aplicar parches de seguridad de manera regular.

- Usabilidad

    - La interfaz del aplicativo DTIC debe ser intuitiva y fácil de usar para los usuarios, proporcionando una experiencia de usuario coherente con la imagen institucional de EducaMadrid.

- Mantenimiento

    - El aplicativo DTIC debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

- Compatibilidad

    - El aplicativo debe ser compatible con las versiones actuales de PHP, MySQL, y otros paquetes del sistema.

### MEJORAS Y MANTENIMIENTO DE SEGUIMIENTOS (SEG)

Corrección de problemas de seguridad, el mantenimiento de incidencias y la incorporación de nuevas funcionalidades en el aplicativo Seguimientos de la plataforma EducaMadrid. El objetivo es mejorar la compatibilidad, seguridad, y funcionalidad del aplicativo, asegurando que cumpla con los estándares actuales y las necesidades de la plataforma (SEG1).

**Requisitos Funcionales**

- Mantenimiento de Ficheros de Versiones Anteriores

    - Los ficheros de versiones anteriores deben mantenerse funcionales con sus URLs antiguas.

- Seguridad de Ficheros Adjuntos

    - Evitar nombres de ficheros correlativos para mejorar la seguridad de los ficheros adjuntos.

- Mantenimiento de Datos Históricos

    - El aplicativo debe mantener todos los centros, usuarios, notas, empresas, adjuntos y dotaciones de años anteriores.

- Acceso Independiente a Datos de Ediciones Preexistentes

    - El aplicativo debe permitir acceso independiente a los datos de las 20 ediciones preexistentes del aplicativo.

- Generación de Nuevas Ediciones

    - Permitir a los administradores generar una nueva edición del aplicativo de forma integrada.

- Gestión de Usuarios, Modalidades, Centros y Notas

    - La aplicación debe contar con gestión de usuarios (manteniendo los actuales), gestión de modalidades, gestión de centros y gestión de notas.

- Conversión de Enlaces a Ficheros

    - La aplicación debe ser capaz de atender los enlaces a ficheros de los aplicativos anteriores, convirtiendo la URL a una del nuevo aplicativo.

- Adaptación de la Interfaz

    - La interfaz del aplicativo debe ser adaptada a la imagen institucional de EducaMadrid, incluyendo logotipos, enlaces, pie de página y buscador de servicios.

- Corrección de Errores

    - Realizar las correcciones de errores encontradas según los tester las prueben.

**Requisitos No Funcionales**

- Seguridad

    - Implementar las mejores prácticas de seguridad para proteger el aplicativo contra vulnerabilidades y ataques.

    - Realizar pruebas de seguridad y aplicar parches de seguridad de manera regular.

<!-- salto de página -->

- Usabilidad

    - La interfaz del aplicativo Seguimientos debe ser intuitiva y fácil de usar para los usuarios, proporcionando una experiencia de usuario coherente con la imagen institucional de EducaMadrid.

- Mantenimiento

    - El aplicativo Seguimientos debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

- Compatibilidad

    - El aplicativo debe ser compatible con las versiones actuales de PHP, MySQL, y otros paquetes del sistema.

### MEJORAS Y MANTENIMIENTO DE ALBOR (ALB)

Estudio de viabilidad para el desarrollo de un nuevo aplicativo Albor en la plataforma EducaMadrid. Albor es una página donde padres o profesores de alumnos con necesidades especiales podrán realizar consultas acerca de capacidades o dispositivos adaptados. El proyecto piloto utilizará IA mediante una herramienta de tecnología RAG para gestionar y consultar la documentación (ALB1).

**Requisitos Funcionales**

- Evaluación de la adaptación de un entorno RAG al Entorno EducaMadrid

    - Evaluar la posibilidad de gestionar la documentación mediante un RAG para que sea compatible con el entorno de EducaMadrid.

    - Asegurar que el RAG pueda integrarse con los sistemas existentes y cumplir con los estándares de seguridad y rendimiento de la plataforma.

- Interfaz de Gestión de Contenido para Administradores

    - Desarrollar una interfaz accesible para los administradores donde puedan subir y gestionar la documentación.

    - La documentación subida debe ser incorporada a una base de datos vectorizada.

    - La interfaz debe permitir la gestión eficiente del contenido, incluyendo la adición, edición y eliminación de documentos.

- Interfaz Pública para Usuarios de Albor

    - Desarrollar una interfaz pública donde los usuarios (padres y profesores) puedan lanzar sus consultas.

    - La interfaz debe ser intuitiva y fácil de usar, permitiendo a los usuarios realizar consultas de manera sencilla.

    - Los resultados de las consultas deben basarse únicamente en la información proporcionada por los administradores y alimentada en la base de datos vectorizada.

- Modelo de IA Local

    - Implementar un modelo de IA local que se alimente con la base de datos vectorizada.

    - El modelo de IA debe ser capaz de procesar las consultas de los usuarios y ofrecer resultados precisos y relevantes.

**<!-- salto de página -->**

**Requisitos No Funcionales**

- Seguridad

    - Implementar las mejores prácticas de seguridad en todos los desarrollos, asegurando la protección de los datos y la prevención de accesos no autorizados.

    - Realizar pruebas de seguridad y aplicar parches de seguridad de manera regular.

- Usabilidad

    - La interfaz del aplicativo Albor debe ser intuitiva y fácil de usar para los usuarios, proporcionando una experiencia de usuario coherente con la imagen institucional de EducaMadrid.

    - Asegurar que la interfaz sea accesible para usuarios con discapacidades, cumpliendo con las normativas de accesibilidad web.

- Adaptabilidad

    - El aplicativo debe ser adaptativo, asegurando un buen rendimiento y una experiencia de usuario óptima en diferentes dispositivos y tamaños de pantalla.

- Mantenimiento

    - El aplicativo Albor debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

- Imagen Institucional

    - Adaptar la interfaz del aplicativo Albor a la imagen institucional de EducaMadrid, incluyendo logotipos, enlaces, pie de página y buscador de servicios.

### MEJORAS Y MANTENIMIENTO DEL SERVICIO DE AVISOS (AVI)

Mantenimiento y actualización con mejoras de seguridad y usabilidad del aplicativo Avisos en la plataforma EducaMadrid. El objetivo es mejorar la seguridad, la disponibilidad y la funcionalidad del aplicativo, asegurando que cumpla con los estándares actuales y las necesidades de la plataforma (AVI1).

**Requisitos Funcionales**

- Actualización del Desarrollo a la Última Versión de PHP

    - El aplicativo Avisos debe ser actualizado a la última versión estable de PHP para garantizar compatibilidad y seguridad.

- Alta Disponibilidad

    - El aplicativo Avisos debe ser configurado y mantenido dando soporte para alta disponibilidad, asegurando que esté accesible en todo momento y minimizando el tiempo de inactividad.

- Sistema de Programación de Puesta en Producción

    - Implementar un sistema que permita programar la puesta en producción de los sistemas de avisos en los distintos aplicativos con los que opera.

    - El sistema debe permitir la programación de la activación y desactivación de avisos en diferentes momentos y fechas.

- Confirmación de Enlaces

    - Implementar un sistema de confirmación para los enlaces en los contenidos creados por los usuarios en diferentes aplicaciones (Portal Educativo —Liferay—, WordPress, Mediateca, Correo Web).

    - Los enlaces que requieren confirmación son:

        - Cuyo texto sea una URL y no coincida con la URL de destino.

        - Cuyo destino sea una dirección de correo (enlace tipo "mailto:") que no coincida con el texto que se ve en pantalla.

    - Excluir los enlaces que se dirigen al servicio urldefense.com para evitar falsos positivos.

**Requisitos No Funcionales**

- Seguridad

    - Implementar las mejores prácticas de seguridad para proteger el aplicativo contra vulnerabilidades y ataques.

    - Realizar pruebas de seguridad y aplicar parches de seguridad de manera regular.

- Usabilidad

    - La interfaz del aplicativo Avisos debe ser intuitiva y fácil de usar para los usuarios, proporcionando una experiencia de usuario coherente con la imagen institucional de EducaMadrid.

- Mantenimiento

    - El aplicativo Avisos debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

- Actualización de Elementos Institucionales

    - Actualizar los elementos institucionales visibles en todos los servicios, incluyendo:

        - Nombre de los organismos responsables y/o logotipos oficiales.

        - Textos y enlaces a pie de página.

        - Planes Regionales y/o Campañas.

### MEJORAS Y MANTENIMIENTO DEL SERVICIO DE FOROS (FOR)

Actualización del aplicativo y su adaptación al entorno de EducaMadrid. El objetivo es asegurar que el aplicativo foros cumpla con las características y funcionalidades requeridas para su correcto funcionamiento en el entorno educativo de EducaMadrid (FOR1).

**Requisitos Funcionales**

- Autenticación contra LDAP EducaMadrid

    - El aplicativo debe ser capaz de autenticar a los usuarios contra el servidor LDAP de EducaMadrid.

- Imagen Institucional

    - La nueva versión del aplicativo debe incorporar la imagen institucional de EducaMadrid.

    - Si es necesario, se debe crear un nuevo tema que refleje la identidad visual de EducaMadrid.

- Actualización de Dependencias

    - Se debe actualizar la versión de PHP, MySQL, y otros paquetes del sistema según sea necesario para garantizar la compatibilidad con la nueva versión.

    - Si es necesario, se debe actualizar el sistema operativo del servidor.

<!-- salto de página -->

- Actualización de Plugins y Temas

    - Todos los plugins y temas actualmente instalados actualmente deben ser actualizados a sus versiones más recientes compatibles con la nueva versión del aplicativo.

**Requisitos No Funcionales**

- Seguridad

    - Se debe trabajar en garantizar la seguridad del sistema, implementando las mejores prácticas de seguridad y realizando pruebas de vulnerabilidad.

    - Se deben aplicar parches de seguridad y actualizaciones críticas para proteger el sistema contra amenazas conocidas.

- Usabilidad

    - La interfaz del aplicativo debe ser intuitiva y fácil de usar para los usuarios, proporcionando una experiencia de usuario coherente con la imagen institucional de EducaMadrid.

- Compatibilidad

    - El aplicativo foros debe ser compatible con las versiones actuales de PHP, MySQL, y otros paquetes del sistema.

- Mantenimiento

    - El aplicativo foros debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

### MEJORAS Y MANTENIMIENTO DEL SERVICIO DE BOLETINES (BOL)

Mantenimiento en el aplicativo Boletines con el objetivo de mejorar la seguridad, actualizar el código a versiones más recientes de PHP y MySQLi, y añadir nuevas funcionalidades. El objetivo es asegurar que el aplicativo sea seguro, eficiente y compatible con las últimas versiones de tecnologías y con las características de EducaMadrid (BOL1).

**Requisitos Funcionales**

- Mantenimiento y Actualización del Código

    - Actualizar el código del aplicativo para su paso a MySQLi.

    - Actualizar el código para ser compatible con la versión 8+ de PHP.

    - Revisar y corregir cualquier problema de seguridad detectado en el código HTML, PHP y JavaScript.

- Herramienta de Recorte de Imágenes

    - Revisar y mejorar la herramienta de recorte de imágenes para evitar problemas de funcionalidad detectados.

    - Permitir el recorte de imágenes con transparencia.

- Compatibilidad con el Modo Oscuro

    - Asegurar la compatibilidad total del aplicativo con el modo oscuro de EducaMadrid, tanto en las vistas públicas (boletines y canal de usuario) como en la propia aplicación (administración de boletines).

- Sistema de Estadísticas

    - Incorporar un sistema de estadísticas básico que permita conocer el número de usuarios que han accedido a un boletín enviado por correo electrónico.

    - Proveer una interfaz para visualizar estas estadísticas en la administración del aplicativo.

**Requisitos No Funcionales**

- Seguridad

    - Implementar medidas robustas para proteger los datos y las operaciones realizadas a través del aplicativo, evitando intrusiones y errores.

    - Asegurar que todas las comunicaciones y operaciones sean seguras, utilizando prácticas recomendadas como la validación y sanitización de entradas, y el uso de conexiones seguras (HTTPS).

- Usabilidad

    - La interfaz del aplicativo debe ser intuitiva y fácil de usar para los administradores y usuarios finales.

    - Proveer instrucciones claras y una navegación sencilla para todas las funcionalidades del aplicativo.

- Rendimiento

    - El aplicativo debe ser eficiente y no afectar negativamente el rendimiento general de la plataforma.

    - Optimizar el código y las consultas a la base de datos para mejorar el rendimiento.

- Mantenimiento

    - El aplicativo debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

### MEJORAS Y MANTENIMIENTO DE LA AYUDA (AYU)

Actualización del aplicativo que sirve la ayuda de la plataforma. El objetivo es asegurar que la actualización mantenga la integridad de los datos y las URLs actuales, y que incorpore nuevas funcionalidades como un chatbot con IA y la imagen institucional (AYU1).

**Requisitos Funcionales**

- Actualización a la Última Versión

    - El aplicativo ayuda debe ser actualizado a la última versión disponible.

- Mantenimiento de Datos

    - Todos los datos actuales del aplicativo de ayuda deben ser mantenidos durante la actualización.

- Mantenimiento de URLs

    - Las URLs actuales del aplicativo deben ser mantenidas para evitar interrupciones en los enlaces existentes.

- Incorporación de Chatbot con IA

    - Se debe incorporar un chatbot funcional con IA que se alimente de una base de datos vectorizada directamente con la base de datos del aplicativo ayuda.

    - El chatbot debe ser capaz de responder preguntas y proporcionar información basada en el contenido del aplicativo.

    - La solución planteada debe ser basada en tecnología RAG.

    - El chatbot debe actualizarse automáticamente cuando se produzcan cambios en el contenido del aplicativo ayuda.

    - El sistema debe funcionar íntegramente dentro de la plataforma educativa, incluyendo los modelos de IA.

<!-- salto de página -->

- Incorporación de la Imagen Institucional

    - La imagen institucional debe ser incorporada tanto en la nueva versión del aplicativo como en el chatbot.

    - La imagen institucional debe ser visible en todas las páginas del aplicativo y en las interacciones del chatbot.

**Requisitos No Funcionales**

- Seguridad

    - La actualización debe asegurar que todos los datos y operaciones sean manejados de manera segura.

    - Las comunicaciones entre el chatbot y la base de datos vectorizada deben estar securizadas.

- Usabilidad

    - La interfaz del aplicativo y del chatbot debe ser intuitiva y fácil de usar.

    - El chatbot debe proporcionar respuestas claras y precisas basadas en el contenido del aplicativo ayuda.

- Rendimiento

    - La actualización no debe afectar negativamente el rendimiento general del aplicativo ayuda.

    - El chatbot debe responder de manera rápida y eficiente a las consultas de los usuarios.

- Mantenimiento

    - El aplicativo y el chatbot deben ser fáciles de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones.

### MEJORAS Y MANTENIMIENTO DEL PORTAL (POR)

Desarrollo de APIs y mejoras de seguridad en el portal de EducaMadrid. El objetivo es proporcionar funcionalidades para dar de alta profesores interinos, incorporar usuarios a través de APIs, y mejorar la seguridad y la política de contraseñas en el portal (POR1).

**Requisitos Funcionales**

- API para Dar de Alta Profesores Interinos

    - Descripción: API para dar de alta profesores interinos en el portal desde la plataforma de formación.

    - Acciones:

        - Si los datos recibidos son correctos, insertar los datos en una tabla/cola de preprocesamiento.

        - Procesar la solicitud pasados unos minutos desde el portal:

            - Insertar al usuario en el centro 9999.

            - Enviar un email al correo alternativo con el login, password y enlace para restablecer la password.

<!-- salto de página -->

- Evitar HTML en Liferay

    - Descripción: Evitar que se pegue HTML en el editor del blog de Liferay, o al menos no permitir etiquetas no permitidas dentro del cuerpo del HTML, como BODY.

    - Acciones:

        - Implementar un filtro de contenido en el editor del blog de Liferay para eliminar o limpiar etiquetas HTML no permitidas.

- Mejorar Política de Contraseñas

    - Descripción: Obligar a que las contraseñas cumplan con unos requisitos específicos y caducar las contraseñas de forma centralizada.

    - Requisitos de Contraseñas, ejemplos:

        - Longitud mínima de 8 caracteres.

        - Incluir al menos una letra mayúscula y una minúscula.

        - Incluir al menos un número.

        - Incluir al menos un carácter especial.

- Caducidad de Contraseñas, ejemplos:

    - Caducar las contraseñas cada 90 días.

    - Implementar un procedimiento que cuide la experiencia de usuario y, al mismo tiempo, impida seguir usando los servicios con la contraseña caducada.

    - Estudio de la viabilidad de implementar la caducidad de contraseñas en el LDAP en lugar del portal.

**Requisitos No Funcionales**

- Seguridad

    - Autenticación: La API debe estar securizada.

    - Encriptación: Todos los datos sensibles deben ser encriptados durante la transmisión.

    - Validación: Implementar validaciones robustas para todos los parámetros de entrada.

- Usabilidad

    - La interfaz de la API debe ser intuitiva y fácil de usar para los desarrolladores.

    - Proporcionar documentación clara y ejemplos de uso para cada endpoint de la API.

- Mantenimiento

    - La API debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones y extensiones.

    - Implementar un sistema de control de versiones (como Git) para gestionar el desarrollo y las actualizaciones de la API.

### MEJORAS Y MANTENIMIENTO DE LA WEB ESTÁTICA (WES)

Mejora de la web estática del portal EducaMadrid. El objetivo es asegurar que la web sea accesible y multilingüe, cumpliendo con los estándares de accesibilidad definidos para los portales y aplicaciones del sector público (WES1).

**<!-- salto de página -->**

**Requisitos Funcionales**

- Selección de Idioma

    - Mejorar el sistema de selección de idioma en la web estática del portal EducaMadrid.

    - Asegurar que todos los contenidos y funcionalidades estén disponibles en otros idiomas.

    - Proporcionar un selector de idioma intuitivo y accesible en la interfaz de usuario.

- Revisión del Nivel de Accesibilidad Web

    - Realizar una revisión exhaustiva del nivel de accesibilidad web de las páginas del portal EducaMadrid.

    - Asegurar que la web cumpla con los requisitos de accesibilidad definidos en la última versión de la norma UNE-EN 301549:2022.

    - Implementar las mejoras necesarias para alcanzar el nivel de conformidad requerido.

**Requisitos No Funcionales**

- Usabilidad

    - La interfaz de usuario debe ser intuitiva y fácil de usar para todos los visitantes, incluyendo aquellos con discapacidades.

    - Proporcionar una experiencia de usuario coherente y eficiente en otros idiomas.

- Accesibilidad

    - Todos los componentes de la web deben cumplir con las directrices de accesibilidad web (WCAG) y la norma UNE-EN 301549:2022.

    - Realizar pruebas de accesibilidad regulares para identificar y corregir problemas de accesibilidad.

- Mantenimiento

    - La web debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones y extensiones.

    - Implementar un sistema de control de versiones (como Git) para gestionar el desarrollo y las actualizaciones de la web.

- Compatibilidad

    - La web debe ser compatible con las versiones actuales de los navegadores web más comunes (Chrome, Firefox, Safari, Edge) y con los dispositivos móviles.

    - Realizar pruebas de compatibilidad regulares para asegurar que la web funcione correctamente en diferentes entornos.

### MEJORAS Y MANTENIMIENTO DEL FRAMEWORK DE INTERFAZ (IFZ)

Mejora progresiva del framework de interfaz utilizado en EducaMadrid para el desarrollo de aplicaciones propias. El objetivo es actualizar y enriquecer el framework con las últimas versiones de Bootstrap, jQuery y TinyMCE, y proporcionar funcionalidades básicas predefinidas que faciliten el desarrollo de interfaces web en los proyectos de EducaMadrid (IFZ1).

**<!-- salto de página -->**

**Requisitos Funcionales**

- Actualización de Tecnologías

    - Bootstrap: Utilizar la última versión disponible de Bootstrap para asegurar compatibilidad y acceso a las últimas funcionalidades y mejoras.

    - jQuery: Utilizar la última versión disponible de jQuery para asegurar compatibilidad y acceso a las últimas funcionalidades y mejoras.

    - TinyMCE: Utilizar la última versión de TinyMCE para proporcionar un editor WYSIWYG robusto y actualizado.

- Funcionalidades Básicas Predefinidas

- Mensajes de Alerta y Confirmación Personalizados

    - Implementar un sistema de mensajes de alerta y confirmación personalizados utilizando componentes de Bootstrap y jQuery.

    - Permitir la personalización de estilos y comportamientos de los mensajes de alerta y confirmación.

- Paneles (Ventanas Modales) Accesibles

    - Utilizar los componentes de modal de Bootstrap para crear paneles accesibles.

    - Asegurar que las ventanas modales sean navegables mediante teclado y cumplan con las directrices de accesibilidad web (WCAG).

- Galería de Imágenes (Al Estilo Lightbox)

    - Implementar una galería de imágenes utilizando una biblioteca como Lightbox o Fancybox.

    - Proporcionar navegación entre imágenes, cierre fácil y soporte para imágenes de alta resolución.

- Mecanismo Sencillo para la Generación de Pestañas

    - Utilizar los componentes de pestañas de Bootstrap para crear interfaces con múltiples secciones.

    - Permitir la personalización de estilos y comportamientos de las pestañas.

- Bocadillos (Tooltips)

    - Implementar un mecanismo sencillo para la generación de bocadillos utilizando los componentes de tooltip de Bootstrap.

    - Permitir la personalización de estilos y comportamientos de los tooltips.

- Herramienta para el Recorte de Imágenes

    - Incluir una herramienta de recorte de imágenes utilizando una biblioteca como Cropper.js.

    - Proporcionar una interfaz intuitiva para seleccionar y recortar áreas de la imagen.

- Editor WYSIWYG con Dos Modos

    - Implementar TinyMCE con dos modos: básico y avanzado/completo.

    - Configurar TinyMCE para que el modo básico incluya solo las herramientas esenciales y el modo avanzado/completo incluya todas las funcionalidades disponibles.

- Selector de Fechas

    - Utilizar una biblioteca como jQuery UI Datepicker o Flatpickr para crear un selector de fechas intuitivo y accesible.

    - Permitir la personalización de estilos y comportamientos del selector de fechas.

<!-- salto de página -->

- Tablas de Datos (DataTable) con Mecanismo de Búsqueda y Filtrado

    - Implementar DataTables utilizando la biblioteca jQuery DataTables.

    - Proporcionar mecanismos de búsqueda y filtrado integrados para trabajar con datos en el propio HTML o en formato JSON.

    - Permitir la personalización de estilos y comportamientos de las tablas de datos.

**Requisitos No Funcionales**

- Usabilidad

    - La interfaz del framework debe ser intuitiva y fácil de usar para los desarrolladores, proporcionando una experiencia de desarrollo coherente y eficiente.

    - Incluir documentación clara y ejemplos de uso para cada componente del framework.

- Accesibilidad

    - Todos los componentes del framework deben cumplir con las directrices de accesibilidad web (WCAG) para asegurar que las aplicaciones desarrolladas sean accesibles para todos los usuarios.

    - Realizar pruebas de accesibilidad regulares para identificar y corregir problemas de accesibilidad.

- Mantenimiento

    - El framework debe ser fácil de mantener y actualizar, proporcionando documentación adecuada para futuras modificaciones y extensiones.

    - Implementar un sistema de control de versiones (como Git) para gestionar el desarrollo y las actualizaciones del framework.

- Compatibilidad

    - El framework debe ser compatible con las versiones actuales de los navegadores web más comunes (Chrome, Firefox, Safari, Edge) y con los dispositivos móviles.

    - Realizar pruebas de compatibilidad regulares para asegurar que el framework funcione correctamente en diferentes entornos.

### MEJORAS Y MANTENIMIENTO DE ENTORNOS MAX (MAX)

Actualización y mejora del entorno MAX en la plataforma educativa EducaMadrid, con el fin de garantizar un entorno seguro y eficiente para la realización de exámenes a través del Aula Virtual (MAX1).

**Mantenimiento**

- Actualización de Contenidos:

    - Página de Inicio de MAX: Se realizará la actualización de los contenidos en la página de inicio de MAX en el Portal Educativo.

    - Nuevo Contenido Específico: Se crearán nuevos contenidos específicos para las nuevas versiones de MAX.

**<!-- salto de página -->**

**Mejora Funcional**

- Entorno Seguro para Exámenes:

    - Navegador con Opciones Limitadas: Se implementará un navegador con opciones limitadas que mostrará un buscador de Aulas Virtuales, permitiendo al alumno localizar el aula de su centro.

    - Acceso al Aula Virtual: El enlace al Aula Virtual se abrirá en la misma ventana. Tras la autenticación, el alumno podrá realizar el examen.

    - Eliminación de Elementos de Navegación: Las páginas (buscador de Aulas Virtuales integrado en la Web Estática de EducaMadrid, página de acceso al Aula Virtual, y la actividad que constituye el propio examen) carecerán de elementos de navegación que permitan al usuario abandonar la prueba. El objetivo es lograr un comportamiento similar al obtenido al combinar el modo examen de las Aulas Virtuales y el navegador Safe Exam Browser, que de momento no está disponible para sistemas operativos Linux.

**Consideraciones Adicionales**

- Compatibilidad: Asegurar que todas las mejoras y actualizaciones sean compatibles con los sistemas operativos y navegadores utilizados por los usuarios de la plataforma.

- Pruebas y Validación: Realizar pruebas exhaustivas para validar que las mejoras funcionales y las actualizaciones de contenido cumplan con los requisitos de seguridad y accesibilidad.

### MEJORAS Y MANTENIMIENTO DEL PROYECTO GESTIÓN DE TÍTULOS (GES)

Actualización y mejora del aplicativo de Gestión de Títulos en la plataforma educativa EducaMadrid. El objetivo es asegurar la compatibilidad con la última versión de PHP, mejorar la seguridad del código, optimizar la base de datos y sus consultas, y añadir funcionalidades específicas para la generación de archivos de impresión de títulos (GES1).

**Tareas Técnicas**

- Compatibilidad con versiones nuevas de PHP:

    - Actualización de Código: Revisar y actualizar el código fuente para que sea compatible con las últimas versiones de PHP. Esto incluye la actualización de funciones y sintaxis obsoletas.

    - Pruebas de Compatibilidad: Realizar pruebas exhaustivas para asegurar que todas las funcionalidades del aplicativo funcionen correctamente bajo las últimas versiones de PHP.

    - Depuración de Errores: Identificar y corregir cualquier error o advertencia generada por las últimas versiones de PHP durante la ejecución del aplicativo.

<!-- salto de página -->

- Mejora de la Seguridad:

    - Sanitización de Campos: Implementar la sanitización de todos los campos de entrada para prevenir inyecciones de código y otros ataques comunes.

    - Validación de Datos: Asegurar que todos los datos de entrada sean validados adecuadamente antes de su procesamiento.

    - Gestión de Sesiones: manejar las sesiones de usuario de manera segura.

    - Autenticación y Autorización: Implementar mecanismos de autenticación y autorización robustos.

    - Escaneo de Vulnerabilidades: Realizar escaneos de vulnerabilidades para identificar y corregir posibles fallos de seguridad.

- Optimización de la Base de Datos:

    - Optimización de Consultas: Revisar y optimizar las consultas SQL para identificar cuellos de botella y aplicar índices adecuados.

    - Índices y Estructuras: Asegurar que los índices y estructuras de la base de datos estén optimizados para las operaciones más frecuentes.

    - Mantenimiento Rutinario: Establecer tareas de mantenimiento rutinario para la base de datos, incluyendo la limpieza de registros obsoletos y la optimización de tablas.

- Mejora Funcional:

    - Generación de Archivos: Implementar la funcionalidad para generar archivos basados en la tabla de códigos ANSI Windows-1252 a partir de ficheros de entrada en UTF-8.

    - Compatibilidad con Aplicación de Impresión: Garantizar que los archivos generados sean compatibles con la aplicación de impresión de los títulos, asegurando un funcionamiento fluido y sin errores. Esto puede incluir la validación de formatos de archivo y la prueba con diferentes configuraciones de impresión.

    - Manejo de Excepciones: Implementar un manejo de excepciones robusto para capturar y registrar cualquier error que ocurra durante la generación de archivos, proporcionando mensajes de error claros y útiles.

### MEJORAS DEL PROYECTO DE MEDIDAS DE USO DE LAS WEB (USO)

Desarrollar una prueba de concepto basada en tecnologías de software libre que aporte una herramienta robusta y actualizada para recoger datos estadísticos de las páginas web de los centros educativos elaboradas con WordPress, creando un plugin en el entorno WordPress Multisite para una recogida estadística independiente por centro (USO1).

**Tareas Técnicas**

- POC de software libre para la recogida de estadísticas:

    - Descarga e Instalación: Descargar la última versión de aplicativos para la recogida de estadísticas desde el sitio oficial y realizar la instalación en el servidor correspondiente.

    - Migración de Datos: Asegurar la migración de datos estadísticos existentes al nuevo aplicativo sin pérdida de información.

    - Configuración Inicial: Configurar el aplicativo con las opciones básicas necesarias para su funcionamiento, incluyendo la configuración de la base de datos y la creación de usuarios administrativos.

- Actualización de Paquetes del Servidor:

    - Apache: Actualizar Apache a la última versión estable, asegurando que todas las configuraciones necesarias para el funcionamiento del aplicativo estén correctamente implementadas.

    - PHP: Actualizar PHP a la última versión compatible con el nuevo aplicativo, asegurando que todas las extensiones necesarias (como mbstring, curl, gd, zip, etc.) estén habilitadas.

    - Base de Datos: Asegurar que la base de datos esté actualizada a una versión compatible con el aplicativo y optimizada para el rendimiento.

    - Otros Paquetes: Actualizar cualquier otro paquete necesario para el funcionamiento óptimo del aplicativo, como Composer para la gestión de dependencias.

- Creación de Plugin para WordPress Multisite:

    - Creación del Plugin: crear un plugin para la conexión con el aplicativo en el entorno WordPress Multisite.

    - Configuración del Plugin: Configurar el plugin para que cada sitio en la red Multisite tenga su propia subinstalación del aplicativo, permitiendo la recogida estadística independiente.

    - Integración con WordPress: Asegurar que los datos estadísticos se muestren directamente en la zona de administración de cada sitio WordPress, utilizando widgets y paneles personalizados.

    - Autenticación y Autorización: Implementar mecanismos de autenticación y autorización para que solo los administradores de cada sitio puedan acceder a los datos estadísticos correspondientes.

- Recolección de Datos Estadísticos:

    - Navegadores Empleados: Recoger datos sobre los navegadores utilizados por los visitantes, incluyendo versiones y sistemas operativos.

    - Páginas Más Visitadas: Identificar las páginas más visitadas en cada sitio, proporcionando información sobre el contenido más popular.

    - Errores Encontrados: Registrar errores encontrados en las páginas web, como errores 404 y 500, para facilitar la optimización y corrección de problemas.

    - Tiempo de Carga: Medir el tiempo de carga de las páginas para identificar posibles cuellos de botella en el rendimiento.

    - Fuentes de Tráfico: Analizar las fuentes de tráfico, incluyendo referencias, búsquedas orgánicas y campañas de marketing.

    - Comportamiento del Usuario: Recoger datos sobre el comportamiento del usuario, como el tiempo promedio en la página, la tasa de rebote y el número de páginas vistas por sesión.

    - Dispositivos Utilizados: Identificar los dispositivos utilizados por los visitantes, incluyendo móviles, tablets y computadoras de escritorio.

    - Geolocalización: Proporcionar información sobre la geolocalización de los visitantes, ayudando a entender la distribución geográfica del tráfico.

<!-- salto de página -->

- Mejora Funcional:

    - Implementación en un Sitio Piloto: Realizar los cambios necesarios en al menos una web de site.educa.madrid.org para recoger datos estadísticos, registrándose en el servidor.

    - Configuración del Tracking: Configurar el código de seguimiento de en la web piloto, asegurando que todos los eventos y páginas se registren correctamente.

    - Pruebas de Validación: Realizar pruebas exhaustivas para validar que los datos estadísticos se recopilen y muestren correctamente en la zona de administración de WordPress.

**Consideraciones Adicionales**

- Pruebas y Validación: Realizar pruebas exhaustivas para validar que todas las actualizaciones y mejoras cumplan con los requisitos de compatibilidad, seguridad y rendimiento. Esto incluye pruebas unitarias, de integración y de carga.

- Seguridad: Implementar medidas de seguridad adicionales para proteger los datos estadísticos recopilados, incluyendo el uso de HTTPS y la configuración adecuada de permisos de acceso.

### MEJORAS Y MANTENIMIENTO DE WEKAN (WEK)

Adaptar al entorno de la plataforma educativa la última versión disponible del aplicativo Wekan.

- Realizar un análisis de compatibilidad de versiones.

- Actualizar los paquetes del sistema operativo y sus dependencias.

- Configurar y optimizar el servidor web Apache.

- Configurar y optimizar la base de datos MongoDB.

- Instalar y configurar PHP, Java, Node.js, npm, y Yarn.

### Conexión con el SSO de EducaMadrid (WEK1)

**Objetivo:**

Estudiar las posibilidades de integración del aplicativo Wekan con el sistema de autenticación única (SSO) de EducaMadrid para asegurar un acceso seguro y centralizado.

**Detalles Técnicos:**

- Protocolo de Autenticación: Utilizar SAML 2.0 o OAuth 2.0, dependiendo del aplicativo.

- Configuración del Proveedor de Identidad (IdP): Configurar el IdP de EducaMadrid en el aplicativo Wekan.

- Certificados SSL/TLS: Asegurar que todos los certificados SSL/TLS estén actualizados y configurados correctamente.

- Mapeo de Usuarios: Configurar el mapeo de atributos de usuario entre EducaMadrid y Wekan para asegurar una sincronización correcta.

**Acciones:**

- Configurar el módulo de autenticación SAML/OAuth en Wekan.

- Obtener y configurar los certificados SSL/TLS necesarios.

- Realizar pruebas de autenticación y mapeo de usuarios.

- Documentar el proceso de integración y configuración.

### Mantenimiento de las Modificaciones Actuales en Código (WEK2)

**Objetivo:**

Asegurar que todas las modificaciones y personalizaciones actuales en el código fuente de Wekan se mantengan en la nueva versión.

**Detalles Técnicos:**

- Control de Versiones: Utilizar Git para gestionar el control de versiones y asegurar que todas las modificaciones se integren correctamente.

- Pruebas Unitarias: Realizar pruebas unitarias para verificar que las modificaciones funcionen correctamente en la nueva versión.

- Documentación: Actualizar la documentación técnica para reflejar las modificaciones y personalizaciones.

**Acciones**:

- Revisar y documentar todas las modificaciones actuales en el código.

- Integrar las modificaciones en la nueva versión de Wekan.

- Realizar pruebas unitarias y de integración.

- Actualizar la documentación técnica.

### Mantenimiento de las Configuraciones y Funcionalidades Actuales (WEK3)

**Objetivo:**

Asegurar que todas las configuraciones y funcionalidades actuales de Wekan se mantengan en la nueva versión.

**Detalles Técnicos:**

- Configuraciones del Servidor: Asegurar que todas las configuraciones del servidor (PHP, Apache, Base de datos, etc.) se mantengan.

- Funcionalidades Personalizadas: Verificar que todas las funcionalidades personalizadas (plugins, scripts, etc.) funcionen correctamente en la nueva versión.

- Interfaz de Usuario: Asegurar que la interfaz de usuario se mantenga consistente y funcional.

**Acciones**:

- Revisar y documentar todas las configuraciones actuales.

- Verificar que todas las funcionalidades personalizadas funcionen en la nueva versión.

- Realizar pruebas de usuario para asegurar la consistencia de la interfaz de usuario.

- Actualizar la documentación técnica y de usuario.

### Adaptación de la Nueva Versión del Aplicativo a la Imagen Institucional (WEK4)

**Objetivo:**

Asegurar que la nueva versión del aplicativo Wekan se adapte a la imagen institucional de EducaMadrid.

**Detalles Técnicos:**

- Logotipo y Marcas: Incorporar el logotipo y las marcas de EducaMadrid en la interfaz de usuario.

- Colores y Tipografía: Ajustar los colores y la tipografía para que coincidan con la identidad visual de EducaMadrid.

- Mensajes y Notificaciones: Personalizar los mensajes y notificaciones para que reflejen el tono y el estilo de comunicación de EducaMadrid.

- Conexión con avisos: deben mostrarse las notificaciones generadas por este aplicativo.

**Acciones:**

- Diseñar y desarrollar los elementos gráficos necesarios (logotipos, iconos, etc.).

- Ajustar los estilos CSS para reflejar la identidad visual de EducaMadrid.

- Personalizar los mensajes y notificaciones en el aplicativo.

- Realizar pruebas de usuario para asegurar la coherencia con la imagen institucional.

### MEJORAS Y MANTENIMIENTO DE MAMOOD (MAM)

Mantenimiento y mejora del aplicativo MaMood, una herramienta clave en la gestión de la plataforma educativa EducaMadrid. El aplicativo se utiliza internamente para tareas como la gestión de altas, bajas, cambios de nombre de aulas virtuales, gestión de WordPress, y gestión del espacio de los centros, entre otras (MAM1).

**Requisitos Técnicos y Funcionales**

- Mejoras de Seguridad

    - Implementación de mejoras de seguridad en el sistema, incluyendo PHP y el desarrollo general.

    - Eliminación de vulnerabilidades como errores de sanitización, XSS, y otras amenazas comunes.

    - Realización de auditorías de seguridad periódicas y corrección de vulnerabilidades identificadas.

- Evolución del Aplicativo

    - Actualización del aplicativo a la última versión de PHP y del sistema operativo.

    - Adaptación de todos los scripts actualmente disponibles de todos los servicios a la nueva versión de PHP y del sistema operativo.

- Scripts de Aulas Virtuales

    - Evolución de los scripts de aulas virtuales para que funcionen dinámicamente leyendo la base de datos de MaMood.

    - Desarrollo de un shell script para programar cambios de código en las aulas virtuales MoodleMisc y multisite, aplicándolos durante horas no lectivas y limpiando las caches posteriormente.

- Mejora de Rendimiento

    - Optimización de los scripts para mejorar el rendimiento general del aplicativo.

    - Implementación de técnicas de caching y otras optimizaciones para reducir el tiempo de respuesta y mejorar la eficiencia.

### MEJORAS Y MANTENIMIENTO DE EMLab (EML)

Mantenimiento y mejora del aplicativo EMLaB, desarrollado en PHP. El contrato incluye la actualización a la última versión de PHP, la renovación de ciertos módulos, la implementación de mejoras de seguridad y la adaptación del sistema operativo y paquetes necesarios (EML1).

**Requisitos Técnicos**

- Actualización de PHP

    - Actualizar el aplicativo EMLaB a la última versión estable de PHP.

    - Realizar las pruebas necesarias para asegurar la compatibilidad del aplicativo con la nueva versión de PHP.

    - Actualizar la máquina o el sistema operativo, así como los paquetes del sistema, si es necesario para soportar la nueva versión de PHP.

- Renovación de Módulos

    - Renovación completa del apartado de preguntas frecuentes (FAQ).

    - Renovación completa del bloque de inscripción, de cara al lanzamiento de la próxima convocatoria.

- Mejoras de Seguridad

    - Implementar la sanitización de campos de entrada para prevenir inyecciones de código.

    - Protección contra ataques XSS (Cross-Site Scripting) y otras vulnerabilidades comunes en aplicaciones PHP.

    - Realizar auditorías de seguridad periódicas para identificar y corregir posibles vulnerabilidades.

**Funcionalidades del Sistema**

- Mantenimiento Continuo

    - Proporcionar soporte técnico continuo para la resolución de incidencias y problemas que puedan surgir.

    - Realizar actualizaciones y parches de seguridad de manera oportuna.

- Mejora de la Usabilidad

    - Optimizar el rendimiento del aplicativo para mejorar la experiencia del usuario.

    - Implementar mejoras en la interfaz de usuario basadas en el feedback de los usuarios.

### MEJORAS Y MANTENIMIENTO DE ABIESWEB (ABI)

Mantenimiento y mejora del aplicativo AbiesWeb, incluyendo la actualización a la última versión liberada por el Ministerio de Educación y Formación Profesional. Este cambio puede requerir la actualización de paquetes del sistema operativo y PHP, así como modificaciones para aumentar la seguridad del sistema (ABI1).

**Requisitos Técnicos**

- Actualización del Aplicativo

    - Actualizar AbiesWeb a la última versión liberada por el Ministerio de Educación y Formación Profesional.

    - Realizar las actualizaciones necesarias de paquetes del sistema operativo y PHP para asegurar la compatibilidad con la nueva versión del aplicativo.

- Mejora de la Seguridad

    - Implementar modificaciones para aumentar la seguridad del aplicativo y evitar ataques típicos, tales como:

        - Inyección SQL

        - Cross-Site Scripting (XSS)

        - Cross-Site Request Forgery (CSRF)

        - Ataques de fuerza bruta

        - Vulnerabilidades en la configuración del servidor

- Mantenimiento de la Imagen Institucional

    - Actualizar los elementos institucionales en la nueva versión del aplicativo, incluyendo:

    - Nombre de los organismos responsables

    - Logotipos oficiales

**Funcionalidades del Sistema**

- Actualización y Compatibilidad

    - Asegurar que todas las funcionalidades del aplicativo AbiesWeb se mantengan operativas después de la actualización.

    - Realizar pruebas de compatibilidad y rendimiento para garantizar un funcionamiento óptimo.

- Seguridad

    - Implementar medidas de seguridad adicionales para proteger contra ataques comunes.

    - Realizar auditorías de seguridad periódicas para identificar y corregir vulnerabilidades.

- Mantenimiento de la Imagen Institucional

    - Actualizar los elementos institucionales en el aplicativo según las directrices proporcionadas por el Ministerio de Educación y Formación Profesional.

    - Asegurar que la imagen institucional se mantenga coherente y actualizada en todas las versiones del aplicativo.

## Productos resultantes del contrato, incluyendo los requisitos de documentación

En los puntos anteriores se concretan todos los trabajos que se requieren en el desarrollo del contrato describiéndose y enumerándose cada uno de los entregables siguiendo la nomenclatura del apartado III.1.1 del presente documento:

| MEJORAS Y MANTENIMIENTOS TRANSVERSALES (TRA) | 8 |
| --- | --- |
| MEJORAS Y MANTENIMIENTO DE LAS AULAS VIRTUALES (AV) | 21 |
| EVOLUCIÓN Y MANTENIMIENTO DE LA MEDIATECA (MED) | 11 |
| CONSULTAS LDAP (LDAP) | 1 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO EXELEARNING ONLINE (EXE) | 1 |
| MEJORAS Y MANTENIMIENTO EN EL CORREOWEB (COR) | 4 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO DE WORDPRESS MULTISITE (WPM) | 5 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO DE FORMULARIOS (FOR) | 1 |
| MEJORAS Y MANTENIMIENTO EN EMPIEZA (EMP) | 1 |
| MEJORAS Y MANTENIMIENTO EN BUSCADOR DE AULAS Y CURSOS (BUS) | 1 |
| MEJORAS Y MANTENIMIENTO DE LOS SERVICIOS DE RETRANSMISIÓN Y VIDEOCONFERENCIA (VID) | 4 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO DE ANIMALANDIA (ANI) | 1 |
| MEJORAS Y MANTENIMIENTO EN LA SINCRONIZACIÓN DE USUARIOS (SYN) | 1 |
| MEJORAS Y MANTENIMIENTO DEL PORTAL CAU (CAU) | 1 |
| MEJORAS Y MANTENIMIENTO DE EDUCASAAC (EDU) | 1 |
| MEJORAS Y MANTENIMIENTO DEL CLOUD (CLO) | 2 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO BUZON ANÓNIMO (BAN) | 1 |
| MEJORAS Y MANTENIMIENTO DE DTIC (DTIC) | 1 |
| MEJORAS Y MANTENIMIENTO DE SEGUIMIENTOS (SEG) | 1 |
| MEJORAS Y MANTENIMIENTO DE ALBOR (ALB) | 1 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO DE AVISOS (AVI) | 1 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO DE FOROS (FOR) | 1 |
| MEJORAS Y MANTENIMIENTO DEL SERVICIO DE BOLETINES (BOL) | 1 |
| MEJORAS Y MANTENIMIENTO DE LA AYUDA (AYU) | 1 |
| MEJORAS Y MANTENIMIENTO DEL PORTAL (POR) | 1 |
| MEJORAS Y MANTENIMIENTO DE LA WEB ESTÁTICA (WES) | 1 |
| MEJORAS Y MANTENIMIENTO DEL FRAMEWORK DE INTERFAZ (IFZ) | 1 |
| MEJORAS Y MANTENIMIENTO DE ENTORNOS MAX (MAX) | 1 |
| MEJORAS Y MANTENIMIENTO DEL PROYECTO GESTIÓN DE TÍTULOS (GES) | 1 |
| MEJORAS DEL PROYECTO DE MEDIDAS DE USO DE LAS WEB (USO) | 1 |
| MEJORAS Y MANTENIMIENTO DE WEKAN (WEK) | 4 |
| MEJORAS Y MANTENIMIENTO DE MAMOOD (MAM) | 1 |
| MEJORAS Y MANTENIMIENTO DE EMLab (EML) | 1 |
| **TOTAL** | **8***5** |

En total se describen **85 entregables** en este documento.

Se entiende por entregables los elementos desarrollados en el proyecto que constituyen componentes del proyecto o servicio o del producto software objeto de desarrollo, en los que dicho producto software será un entregable más del proyecto.

El total de esfuerzo ordinario en las tareas de mantenimiento y desarrollo evolutivo se estima en **10.487,3***0 horas** a cargo de los diferentes perfiles indicados en el apartado correspondiente.

El total de esfuerzo extraordinario, fuera del horario ordinario, se estima en **619,5 horas**, que podrá llevar a cabo cualquiera de los perfiles del contrato.

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

En general, se exigirá como entregable toda la información necesaria para la correcta instalación, operación, uso, mantenimiento y monitorización de los sistemas desarrollados, así como cualquier producto generado: documentaciones, procedimientos, scripts, configuraciones, etc…

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

Debido a su naturaleza, el mantenimiento correctivo y la gestión de las incidencias de los proyectos incluidos en este pliego supone una carga de trabajo extensa.

## Descripción del servicio de mantenimiento Correctivo y la gestión DE INCIDENCIAS de los sistemas en entornos productivos.

## Alcance

Las tareas de mantenimiento correctivo y la gestión de las incidencias estarán orientadas al aseguramiento de la continuidad del servicio de los sistemas en entornos productivos cubrirá el conjunto de los sistemas de información y el entorno tecnológico descritos en el Anexo I y en el Anexo II.

El servicio consiste en la corrección del código fuente o de la documentación para resolver o paliar las incidencias que afecten a los citados sistemas de información, así como todas las tareas conexas necesarias para poder realizar dicha corrección.

Concretamente el contrato estará centrado en las tareas que se refieren tanto a los Proyectos de Sistemas actualmente alojados en la Plataforma Educativa EducaMadrid como a los que pudieran surgir, de naturaleza similar, a lo largo de la vigencia del contrato.

## Gestión de incidencias

El Responsable del Contrato Específico, o la persona designada por éste para la tarea, clasificará las incidencias que detecte y las que comuniquen los usuarios, comunicándolas a su vez al contratista por escrito, mediante correo electrónico o herramienta de gestión del servicio (en inglés, *ITSM*) según decisión del organismo destinatario, haciendo constar:

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

- Localización y acceso a Recursos Digitales en EducaMadrid (software educativo, Infopitágoras, repositorio Agrega, etc.).

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

El total de esfuerzo ordinario en las tareas de desarrollo correctivo y gestión de incidencias se estima en **10.487,3***0 horas** a cargo de los diferentes perfiles indicados en el apartado correspondiente.

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

Cuando la resolución de la incidencia requiera la realización de desarrollos que por su naturaleza necesitan de un plazo material superior al indicado en la tabla precedente, el contratista estará obligado a presentar al Responsable del Contrato Específico en el organismo destinatario, dentro del plazo de tiempo de resolución inicial, un plan de actuación que incluya la duración prevista de los trabajos para la resolución, la justificación de dicha previsión y la descripción de los trabajos a realizar. Si es necesario, se incluirá la descripción de las medidas paliativas a adoptar hasta la completa resolución de la incidencia. Dicho plan deberá ser aprobado por el Responsable del Contrato Específico.
