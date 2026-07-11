# DESCRIPCIÓN DEL ENTORNO TÉCNICO Y FUNCIONAL EXISTENTE

## Descripción de los sistemas de información existentes

La Plataforma Educativa EducaMadrid (en adelante EducaMadrid) está compuesta por un ecosistema de aplicaciones desarrolladas en distintas tecnologías, con diferentes paradigmas y lenguajes usados por la Comunidad Educativa no universitaria, sostenida con fondos públicos de la Comunidad de Madrid.

La Consejería de Digitalización considera la utilización de las Tecnologías de la Información y la Comunicación como un recurso actualmente imprescindible en los procesos de enseñanza y aprendizaje.

Con esta finalidad proporciona un conjunto de servicios y herramientas a la comunidad educativa a través de EducaMadrid https://www.educa2.madrid.org/. Estos servicios y herramientas ofrecen los medios necesarios para facilitar el proceso enseñanza-aprendizaje y de comunicación entre los distintos actores que intervienen en el mismo. Por este motivo es necesario dar soporte a sus usuarios y desarrollar, actualizar, evolucionar y mantener los servicios y aplicaciones educativas, herramientas de comunicación entre ellas y sus interfaces, que mantendrán un aspecto y forma de uso comunes para facilitar su uso y para que el usuario identifique todas ellas como componentes de la misma plataforma.

La arquitectura tecnológica software de EducaMadrid está constituida por más de 25 aplicaciones que ofrecen servicios a la Comunidad Educativa a través de un acceso en Cloud (Nube Privada Educativa). Estas aplicaciones deben interactuar entre sí. Algunas de ellas están basadas en adaptaciones de software existente (en su mayoría open-source) y otras se han desarrollado completamente para dar servicios concretos desde EducaMadrid. La mayoría de estas aplicaciones y servicios están en producción y necesitan un mantenimiento; otras están en fase de desarrollo, otras están en fase de desarrollo.

Además de todo lo antedicho, la Plataforma EducaMadrid, como se ha explicado en el apartado 2, aloja un elevado número de Proyectos Exteriores.

Las aplicaciones existentes en la plataforma más directamente afectadas por los Proyectos Exteriores, objeto de este contrato, son:

            - Páginas Web Liferay.

            - Desarrollos en Drupal.

            - Proyectos de Dinámicas.

            - Proyectos Moodle Misc.

            - Páginas web Wordpress Multisite.

Además, hay que contemplar el alojamiento de otros Proyectos Exteriores que se integran en más o menos medida con otros productos existentes.

## Descripción del entorno tecnológico

La arquitectura hardware de la Plataforma Educativa EducaMadrid está constituida por más de 650 servidores físicos y virtuales, con un crecimiento estimado en torno a 650 en 2024, así como 5 grupos de almacenamiento consolidado, distribuidos en una capa de Frontend y otra de Backend. Los servicios se distribuyen del siguiente modo, aunque pueden ampliarse:

            - Virtualización Principal HP Synergy – RHEV, 27 nodos repartidos en 3 frames.

            - Virtualización Secundaria HP C7000 – RHEV, 5 nodos en 1 chasis.

            - Cabinas de almacenamiento Netapp, EMC Unity y 3 Infinidat.

            - 3.750 BBDD aproximadamente repartidas entre 120 Servidores con SGBD (PostgreSQL, Mysql, MariaDB, cluster Galera, MSSQL, MongoDB, redis y Elastic)

            - Servidores virtualizados 650 aproximadamente (RedHat, OpenSuse, Ubuntu, Debian y Windows Server)

Existen varias instancias de cada uno de los servicios en distintos entornos, contando con entornos de desarrollo, testeo, preproducción y producción.

Los Proyectos Externos se integran dentro de esta estructura, bien apoyándose en máquinas compartidas con otro tipo de proyectos o bien disponiendo de máquinas dedicadas a ellos.

## Descripción del entorno funcional

La realización de las tareas necesarias para el mantenimiento correctivo y evolutivo, así como las tareas de soporte relacionados con los Proyectos Exteriores, entendiendo como tales aquellos “proyectos que no sirven al objetivo principal de la plataforma EducaMadrid, pero que se apoyan en los recursos de esta”.

Podemos dividir los Proyectos Exteriores en tres grandes grupos:

## PROYECTOS DE BAJA REPERCUSIÓN

## CENTROS VIRTUALES

Son centros virtuales que se han integrado en el entorno de Aulas Virtuales EducaMadrid y que utilizan sus servicios. Al no ser centros educativos generan más incidencias de las habituales para un recurso de este tipo y su resolución no suele ser la estándar.

A fecha de publicación del pliego encontramos los siguientes:

| **Nombre del Proyecto** | **Unidad responsable del Proyecto** |
| --- | --- |
| Aulas Virtuales SG Inspección | SG Inspección Educativa |
| Escuela de animación | DG Juventud |
| AV Actividades y juventud | DG Juventud |
| AV Infancia, familias y natalidad | S.G. Infancia y Adolescencia |
| AV SGI de cualificación… | SGl de Cualificación y Acreditación Profesional. |

Esta lista podría variar a lo largo del pliego.

## PROYECTOS WEB LIFERAY

Son páginas web que se han integrado dentro de las ofrecidas por el servicio de páginas web de EducaMadrid. Igualmente, al no ser webs estándar generan más incidencias y su resolución no suele ser la estándar.

Entre ellos encontramos:

| **Nombre del Proyecto** | **Unidad responsable del Proyecto** |
| --- | --- |
| C. Formación en TIC de Madrid | Consejería de Economía, Hacienda y Empleo |
| C. Formación en Edificación y Obra Civil | Consejería de Economía, Hacienda y Empleo |
| C. Formación en Electricidad, Electrónica y Aeronáutica | Consejería de Economía, Hacienda y Empleo |
| C. Formación en Administración, Seguros y Finanzas | Consejería de Economía, Hacienda y Empleo |
| C. Formación en Tecnologías del Frío y la Climatización. | Consejería de Economía, Hacienda y Empleo |
| Revista de TIC y NEE | Subdirección General de Centros de Educación Infantil, Primaria y Especial |
| Programa del Enriquecimiento educativo para Alumnado con Altas Capacidades | Subdirección General de Centros de Educación Infantil, Primaria y Especial |
| Web de la SG de Inspección Educativa | SG Inspección Educativa |
| Web de Convivencia | SG Inspección Educativa |
| Títulos académicos no universitarios | SG Técnica |
| Delegación de Protección de Datos: | SG Técnica |
| Procesos de obtención de estadísticas | Subdirección General de Evaluación y Análisis |
| Bilingüismo, Actividades culturales y Premios Extraordinarios | Subdirección General de Bilingüismo |
| Web Interna del Servicio de Inspección Educativa DAT Madrid-Capital | Viceconsejería de Organización Educativa |

Esta lista podría variar a lo largo del pliego.

## CENTROS DE MENORES

Estos servidores se han integrado dentro del ecosistema de EducaMadrid para ofrecer acceso WiFi. Al no ser servidores estándar generan pocas incidencias, pero su resolución no suele ser la estándar y requiere de mayor esfuerzo.

Entre ellos encontramos:

| **Nombre del Proyecto** | **Unidad responsable del Proyecto** |
| --- | --- |
| Centros de Menores | Consejería de Políticas Sociales, Familias, Igualdad y Natalidad |
| Menores Protegidos | Consejería de Políticas Sociales, Familias, Igualdad y Natalidad |

Esta lista podría variar a lo largo del pliego.

## PROYECTOS DE REPERCUSIÓN MEDIA

## PROYECTOS MOODLE MISC

Estos proyectos son Aulas Virtuales que no se han integrado en nuestro sistema principal de Aulas Virtuales, sino en un sistema especial ya que tienen necesidades específicas y requieren configuraciones no estándar.

Entre ellos encontramos:

| **Nombre del Proyecto** | **Unidad responsable del Proyecto** |
| --- | --- |
| AV Formación para el empleo | Consejería de Economía, Hacienda y Empleo |
| AV RRHH | DG Recursos Humanos |
| Aulatest | DG Bilingüismo y Calidad de la Enseñanza |
| Bachillerato a Distancia | Consejería de Educación, Ciencia y Universidades |
| Campus Innovación | Consejería de Educación, Ciencia y Universidades |
| ISMIE | DG Bilingüismo y Calidad de la Enseñanza |
| FP a Distancia | DG de Educación Secundaria, Formación Profesional y Régimen Especial |
| Innovamooc | DG Bilingüismo y Calidad de la Enseñanza |
| Bomberos Madrid | Consejería de Medio Ambiente, Agricultura e Interior |

Esta lista podría variar a lo largo del pliego.

## PROYECTOS DE ALTA REPERCUSIÓN

Son proyectos que requieren máquinas dedicadas y recursos adicionales. Muchos de ellos integran desarrollos de empresas externas y conllevan el acceso a las máquinas de la plataforma por entidades externas o incluso desconocidas por la Subdirección. Se subdividen en dos grupos:

## PROYECTOS DE DINÁMICAS

Son proyectos que, para implantarse, requirieron el aprovisionamiento de máquinas especiales (que denominamos “dinámicas”) porque presentaban necesidades y configuraciones especiales.

Son entornos en donde otras unidades tienen una Base de Datos independiente y donde pueden subir desarrollos realizados en PHP. El problema de estos entornos es que desde la propia subdirección no sabemos que desarrollos se están realizando en esos espacios de dinámicas, lo que al final se traduce en una ampliación del perímetro de seguridad de la propia plataforma. Además, tenemos que preocuparnos por las actualizaciones el software base de los sistemas, que implican siempre una migración de los desarrollos y no siempre es fácil.

Entre ellos encontramos:

| **Nombre del Proyecto** | **Unidad responsable del Proyecto** |
| --- | --- |
| Animalandia |  |
| Clasificación Idiomas | Unidad Técnica de Ordenación Académica de Enseñanzas de Régimen Especial |
| Gestordinamicas | Herramienta de gestión interna del resto de proyectos. |
| Web de la DG de Bilingüismo y Calidad de la Enseñanza | DG de Bilingüismo y Calidad de la Enseñanza |
| GestionDGSecundaria | DG de Educación Secundaria, Formación Profesional y Régimen Especial |

Esta lista podría variar a lo largo del pliego.

## PROYECTOS WEB LIFERAY INDEPENDIENTES

Son proyectos Liferay independientes que no solo cambian el tema, si no que necesitan una instalación independiente, y requieren especial atención a su desarrollo y despliegue.

Entre ellos encontramos:

| **Nombre del Proyecto** | **Unidad responsable del Proyecto** |
| --- | --- |
| Formación Profesorado mejora convivencia | Inspección - Unidad Técnica de convivencia contra el acoso escolar |
| Fondos de los institutos históricos | DG de Bilingüismo y Calidad de la Enseñanza |
| Orientación Académica y Profesional. Cuaderno Informativo. | DG de Bilingüismo y Calidad de la Enseñanza |
| Guía para familias | DG de Bilingüismo y Calidad de la Enseñanza |

Esta lista podría variar a lo largo del pliego.

## PROYECTOS DE INTEGRACIÓN CON LA PLATAFORMA DE EDUCAMADRID

La mayor parte de los Proyectos Exteriores, tienden a integrarse de alguna forma u otra con la Plataforma de EducaMadrid, y a veces hay que modificar o desarrollar pequeños plugins en los entornos principales de la misma para realizar estas operaciones de integración.

Entre ellos encontramos:

| **Nombre del Proyecto** | **Nº de plugins** | **Unidad responsable del Proyecto** |
| --- | --- | --- |
| Aula Planeta (plugin en Moodle) | 4 | Subdirección General de Programas de Innovación y Formación del Profesorado |
| Smile&Learn (servidores para el servicio y plugin en Moodle) | 1 | Subdirección General de Programas de Innovación y Formación del Profesorado |
| EDEBE (plugin en Moodle) | 3 | Subdirección General de Programas de Innovación y Formación del Profesorado |

Esta lista podría variar a lo largo del pliego.

## PROYECTOS DE SISTEMAS EXTERNOS

Son proyectos variados, que pueden contener aplicaciones externas y que usan una o varias máquinas de la plataforma.

Entre ellos encontramos:

| **Nombre del Proyecto** | **Unidad responsable del Proyecto** |
| --- | --- |
| MadREAD (BiblioMAD) | DG de Bilingüismo y Calidad de la Enseñanza |
| Accede (PROXY) | DG de Bilingüismo y Calidad de la Enseñanza |
| Innovación y Formación (PROXY\_NO\_ENS) | DG de Bilingüismo y Calidad de la Enseñanza |
| Evalum | DG de Bilingüismo y Calidad de la Enseñanza |
| Evalum2 | DG de Bilingüismo y Calidad de la Enseñanza |
| SSO de Google (PROXY\_NO\_ENS) | DG de Bilingüismo y Calidad de la Enseñanza |
| SSO de Microsoft (PROXY\_NO\_ENS) | DG de Bilingüismo y Calidad de la Enseñanza |
| Inscripción en estudios superiores | DG de Educación Secundaria, Formación Profesional y Régimen Especial |

Esta lista podría variar a lo largo del pliego.

*<!-- salto de página -->*

# DEFINICIÓN Y ALCANCE DE LOS TRABAJOS

En este apartado se describirán las prestaciones que consistirán en trabajos de **consultoría, planificación, estudio de viabilidad, análisis, diseño, construcción e implantación de sistemas de información**, y los mantenimientos evolutivos o adaptativos que permitan la incorporación a un producto software de nuevas características funcionales con objeto de cubrir la ampliación o el cambio de las necesidades de usuario.

Debido a su naturaleza, las tareas relativas al mantenimiento evolutivo y adaptativo de los sistemas y aplicaciones de los proyectos exteriores suponen una carga de trabajo importante equiparable a las correspondientes tareas relativas al mantenimiento correctivo (descritas en el Anexo III).

## DESCRIPCIÓN DEL SERVICIO DE MANTENIMIENTO PARA ASEGURAMIENTO DE LA CONTINUIDAD DEL SERVICIO DE LOS SISTEMAS EN ENTORNOS PRODUCTIVOS.

## ALCANCE

Las tareas de mantenimiento evolutivo o adaptativo orientadas al aseguramiento de la continuidad del servicio de los sistemas en entornos productivos cubrirán el conjunto de los sistemas de información y el entorno tecnológico descritos en el Anexo I.

El servicio consiste en la corrección del código fuente o de la documentación para evolucionar o adaptar las incidencias que afecten a los citados sistemas de información, así como todas las tareas conexas necesarias para poder realizar dicha corrección, por ejemplo, actualización de las versiones, parcheados de seguridad, adaptaciones preventivas, aclaraciones y ayudas a terceras empresas, etc…

Concretamente el contrato estará centrado en las tareas que se refieren tanto a los Proyectos Exteriores actualmente alojados en la Plataforma Educativa EducaMadrid como a los que pudieran surgir, de naturaleza similar, a lo largo de la vigencia del contrato.

En el mantenimiento de los servicios ofrecidos se deben incluir los mantenimientos evolutivos, así como otras tareas de adaptación y actualización de dichos servicios. Estas tareas pueden agruparse en las siguientes áreas:

- Mantenimiento evolutivo y adaptativo de Proyectos web Liferay (ELIF)

- Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado (IFP)

- Proyectos Moodle Misc (EMOM)

- Proyectos de Dinámicas (EDIN)

- Proyectos de Integración con la Plataforma de EducaMadrid (EIPE)

- Proyectos de Sistemas Externos (ESIS)

- Seguridad de aplicaciones WEB (ESEG)

- Realización de pruebas de desarrollo seguro de aplicaciones WEB (EDSA)

- Mantenimiento y gestión del programa de Bug Bounty (EBBO)

<!-- salto de página -->

## MANTENIMIENTO EVOLUTIVO Y ADAPTATIVO PARA LOS PROYECTOS EXTERIORES

Debido a que los Proyectos exteriores se encuentran agrupados por áreas, aplicaciones y servicios, tal y como se describen en el capítulo 2, tanto los requisitos como los entregables relacionados se han repartido siguiendo la misma estructura.

A continuación, se enumeran los distintos trabajos a desarrollar en el ámbito del contrato, así como la lista de los entregables (EXXXN) clasificados por áreas o aplicaciones/servicios según la nomenclatura indicada en el apartado anterior.

## Proyectos Web Liferay

Se pide llevar a cabo las tareas enumeradas a continuación relativas a las entradas principales de usuarios a la plataforma de EducaMadrid.

## Adaptaciones de las páginas web Liferay

Se solicita la revisión y adaptación de las vistas públicas y de edición del gestor de contenidos utilizado en el Portal Educativo (Scribe CMS) de páginas externas alojadas actualmente en este entorno (ELIF1).

## Barra de herramientas y pie de EducaMadrid

Se solicita la revisión y adaptación de la barra de herramientas común para todos los servicios web de la Plataforma EducaMadrid, y su incorporación en todos los servicios externos a la plataforma, así como un pie común a la misma (ELIF2).

## Mejoras de presentación

Se solicita evolucionar las partes relativas a la presentación, en las diferentes páginas y plantillas desarrolladas en JSP/JSTL, siendo imprescindible el cumplimento de estándares (HTML5) en las vistas finales de los contenidos, así como su adaptación para el cumplimento, al margen de los contenidos introducidos por los usuarios, de los niveles de accesibilidad web aplicables a los servicios ofrecidos por la Administración Pública (ELIF3).

## Mejoras de usabilidad y accesibilidad

Se solicita mejorar la usabilidad y accesibilidad en diferentes espacios institucionales del Portal Educativo, así como mejorar la presentación de los boletines (ELIF4).

## Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado (IFP)

Actualización de la plataforma de Innovación y Formación del Profesorado, basada en Drupal. Este documento abarca desde la migración de la plataforma a una nueva versión de Drupal hasta la implementación de nuevas funcionalidades y la optimización del rendimiento (IFP1).

**<!-- salto de página -->**

**Objetivos**

- Migrar la plataforma actual basada en Drupal a la versión 11.

- Integración de nuevas funcionalidades que asuman desarrollos externos desplegados actualmente de forma independiente en producción.

- Continuar la eliminación de formularios con Vue para facilitar el mantenimiento.

- Mejorar el rendimiento separando los registros de inscripciones en actividades.

- Crear una zona de "Intranet" para usuarios administradores.

- Desacoplar aplicaciones de terceros no integrables mediante la generación de APIs.

- Migrar las inscripciones a entidades para mejorar el rendimiento.

- Migrar el entorno a nuevos servidores con acceso de administración exclusivo desde Educamadrid.

- Lanzar consultas de actualización de datos contra la BBDD ‘LDAP plano’

**Alcance**

- Migración de la plataforma Drupal a la versión 11.

- Eliminación de formularios con Vue.

- Optimización del rendimiento de la base de datos.

- Creación de una zona de "Intranet".

- Incorporación paulatina de funcionalidades nuevas en la zona de intranet.

- Generación de APIs para desacoplar aplicaciones de terceros no integrables.

- Migración de inscripciones a entidades.

- Migración del entorno a nuevos servidores.

- Camibar la fuente de actualización de datos del LDAP al LDAP plano

**Requisitos Técnicos**

- Migración a Drupal 11

    - Compatibilidad: Asegurar que toda la funcionalidad actual se mantenga en la nueva versión.

    - Actualización de Dependencias: Actualizar la versión de PHP, Apache y el sistema operativo si es necesario.

    - Pruebas: Realizar pruebas exhaustivas para verificar que la migración no afecte el funcionamiento de la plataforma.

- Integración de aplicativos de terceros (GIFP, Ponentes, …)

    - Incorporación paulatina de nuevas funcionalidades dentro de la nueva intranet del aplicativo para ir desvinculando drupal de aplicativos de terceros: actualmente algunos aplicativos de terceros realizan consultas o inserciones directamente en la bbdd drupal. Es necesario incorporar las funcionalidades de dichos aplicativos al core de drupal para evitar dichas consultas.

    - Los aplicativos más importantes para migrar serán GIFP y Ponentes, y se estudiarán otros aplicativos para integrarse paulatinamente.

    - Validación: Implementar validaciones para asegurar que las funcionalidades integradas sean correctas y no se pierdan capacidades en la migración.

- Mantenimiento: Eliminación de Formularios con Vue

    - Revisión: Revisar y eliminar formularios con Vue que ya no sean necesarios.

        - Análisis de Uso: Evaluar el uso actual de cada formulario.

    - Sustitución: Sustituir formularios con Vue por alternativas más mantenibles si es necesario.

        - Formularios Alternativos: Utilizar formularios nativos de Drupal o módulos compatibles.

    - Pruebas: Realizar pruebas para asegurar que la eliminación de formularios no afecte la funcionalidad de la plataforma.

        - Pruebas de Funcionalidad: Verificar que todas las funcionalidades sigan operando correctamente.

        - Pruebas de Rendimiento: Evaluar el impacto en el rendimiento de la plataforma.

- Mejora de Rendimiento: Separación de Registros de Inscripciones

    - Optimización: Separar los registros de inscripciones en actividades de la entidad Actividad.

        - Nueva Entidad: Crear una nueva entidad "Inscripciones" en la base de datos.

        - Relaciones: Definir relaciones entre las entidades "Actividad" e "Inscripción".

    - Índices: Crear y optimizar índices para mejorar el rendimiento de las consultas.

        - Índices de Búsqueda: Crear índices en campos de búsqueda frecuente.

        - Índices de Relación: Crear índices en campos que relacionen entidades.

    - Pruebas: Realizar pruebas de rendimiento para verificar la mejora.

        - Pruebas de Carga: Simular cargas de trabajo para evaluar el rendimiento.

        - Análisis de Consultas: Analizar el tiempo de respuesta de las consultas más comunes.

- Mejora Funcional: Zona de "Intranet"

    - Acceso: Crear una zona de "Intranet" accesible solo para usuarios administradores.

        - Autenticación: Implementar mecanismos de autenticación robustos.

        - Autorización: Definir roles y permisos específicos para el acceso a la zona de "Intranet".

    - Funcionalidades: Diseñar la zona para albergar futuras funcionalidades actualmente implementadas en plataformas externas.

        - Modularidad: Diseñar la zona de "Intranet" de manera modular para facilitar la adición de nuevas funcionalidades.

        - Interfaz de Usuario: Crear una interfaz de usuario intuitiva y fácil de navegar.

    - Seguridad: Implementar medidas de seguridad para proteger el acceso a la zona de "Intranet".

        - Encriptación: Encriptar los datos sensibles tanto en tránsito como en reposo.

        - Auditoría: Configurar auditorías y monitoreo continuo para detectar actividades sospechosas.

- Desacoplamiento de Aplicaciones de Terceros no integrables

    - APIs: Generar APIs dentro de Drupal para que los aplicativos de terceros puedan acceder a la información sin leer la base de datos de Drupal.

        - RESTful APIs: Crear APIs RESTful para acceder a los datos de Drupal.

        - Autenticación: Implementar mecanismos de autenticación para las APIs (OAuth, JWT, etc.).

    - Cambio de Consultas: Cada aplicativo deberá cambiar la forma de consulta de la base de datos a las APIs generadas.

    - Pruebas: Realizar pruebas exhaustivas para asegurar que las aplicaciones de terceros funcionen correctamente con las nuevas APIs.

        - Pruebas de Integración: Verificar la integración entre las aplicaciones de terceros y las nuevas APIs.

        - Pruebas de Rendimiento: Evaluar el impacto en el rendimiento de las aplicaciones de terceros.

- Migración de Inscripciones a Entidades

    - Revisión: Revisar y migrar las inscripciones a entidades para mejorar el rendimiento.

        - Análisis de Datos: Evaluar el estado actual de los registros de inscripciones.

        - Plan de Migración: Crear un plan detallado para la migración de datos.

    - Optimización: Optimizar las consultas y la estructura de la base de datos para reducir el crecimiento desmedido de registros.

        - Índices: Crear y optimizar índices en la nueva entidad "Inscripción".

        - Consultas: Revisar y optimizar las consultas SQL para mejorar el rendimiento.

    - Pruebas: Realizar pruebas para asegurar que la migración no afecte la funcionalidad de la plataforma.

Pruebas de Funcionalidad: Verificar que todas las funcionalidades sigan operando correctamente.

        - Pruebas de Rendimiento: Evaluar el impacto en el rendimiento de la plataforma.

- Migración del Entorno a Nuevos Servidores

    - Servidores: Crear servidores para preproducción y producción exclusivamente para las instalaciones de Drupal.

        - Configuración: Configurar los servidores con las versiones necesarias de PHP, Apache y Drupal.

    - Acceso: Asegurar que el acceso de administración sea exclusivo desde Educamadrid.

        - Control de Acceso: Implementar mecanismos de control de acceso (firewalls, VPNs, etc.).

        - Autenticación: Utilizar sistemas de autenticación robustos

    - APIs: Restringir el acceso a los datos al resto de aplicativos mediante llamadas a APIs si necesitan información de Drupal.

        - Documentación de APIs: Proveer documentación detallada sobre las APIs y su uso.

        - Guía de Integración: Instrucciones para los desarrolladores de aplicaciones de terceros sobre cómo integrarse con las nuevas APIs.

    - Seguridad: Implementar medidas de seguridad para proteger los nuevos servidores.

        - Encriptación: Encriptar los datos sensibles tanto en tránsito como en reposo.

        - Auditoría: Configurar auditorías y monitoreo continuo para detectar actividades sospechosas.

- Utilización de la BBDD LDAP plano como origen de datos

    - Se utilizará la API del LDAP PLANO para actualización de datos: se cambiará la fuente de datos del LDAP al LDAP plano para solucionar problemas de rendimiento y timeouts.

## Proyectos Moodle Misc

Actualmente EducaMadrid dispone de unas 2.300 Aulas Virtuales de Centros Educativos sostenidos con fondos públicos independientes entre sí pero que comparten el mismo código Moodle. Estas Aulas Virtuales se disponen en varias “islas” o agrupamientos que comparten servidores con una versión de código estable.

Por otro lado, el Aula Virtual de EducaMadrid cuenta ya con varios plugin, pero es una plataforma que debe adaptarse a las necesidades crecientes de sus usuarios, con lo que se pide la adaptación de varios plugin durante el trascurso del contrato también enumerados a continuación.

Es importante resaltar que EducaMadrid ofrece este servicio de Aulas Virtuales no sólo a los Centros Educativos al uso, sino a otros Centros, cada uno con ciertas peculiaridades, haciendo necesario contar con instalaciones especiales en otros servidores. Se denominan instalaciones “MoodleMisc” (miscelánea) y es necesario llevar a cabo sobre ellas todas las labores de actualización y mejoras descritas en este epígrafe, adaptadas a las necesidades de cada uno de estos Centros especiales.

Se pide llevar a cabo las tareas necesarias de actualización enumeradas a continuación sobre todas las instalaciones de Moodle.

## Actualización de la plataforma MoodleMisc

El Aula Virtual de EducaMadrid cuenta con una versión de Moodle contrastada. Todos los años se hace una actualización de este. Se pide actualizar dicho código a la última versión estable disponible y llevar dicha actualización en el entorno MoodleMisc. Dicha versión actualizada debe implantarse a su vez tanto en todos los servidores encargados de los backups y ejecuciones de cron como en todos los servidores de otros entornos de la plataforma como preproducción y test. (EMOM1)

Es necesario aplicar todas las tareas llevadas a cabo en el aula virtual Multisite sobre la plataforma MoodleMisc como pueden ser las siguientes:

- Aplicar actualizaciones en todos los frontales de la versión de PHP.

- Aplicar actualizaciones periódicas del aplicativo Moodle y todos sus complementos a versiones actuales y seguras manteniendo todas las funcionalidades y modificaciones ya implementadas. Estudiar las nuevas funcionalidades y configurarlas según necesidades de la plataforma.

- Aplicar actualizaciones de seguridad según solicitudes del departamento de ciber seguridad en todos los elementos del aula virtual e infraestructura (PHP, Moodle, plugin, librerías…)

- Aplicar actualizaciones periódicas del tema EducaMadrid compatible con los elementos comunes de EducaMadrid: buscador de servicios y pie de página común. El Theme incluirá un modo oscuro de desarrollo propio que se podrá activar/desactivar desde la barra superior de la aplicación.

- Evolucionar las actividades HVP hacia la actividad Core H5P de Moodle.

- Actualizar los scripts de AV para que permitan un paso en producción programado de madrugada de cambios en el tema de moodle, limpiando caches.

## Adaptación de la plataforma MoodleMisc

Es necesario aplicar todas las tareas llevadas a cabo en el aula virtual Multisite sobre la plataforma MoodleMisc como pueden ser las siguientes (EMOM2):

- Mantener las conectividades con otros servicios de la plataforma:

                - Conexión SAML con NextCloud.

                - Conexión WebAuth entre Nextcloud y Moodle.

                - Conexión de BigBlueButton con Moodle.

                - Otras futuras implantaciones: aplicaciones de IA, Kuet, CodeRunner, etc

- Efectuar un reinicio anual preventivo de los cursos respetando las preferencias de los usuarios.

- Mantener la modificación de la opción de descarga del listado de participantes del curso en formato PDF.

- Propagar cambios en la configuración de los distintos centros.

- Recoger datos estadísticos.

- Evolucionar la integración de calendarios con la aplicación Empieza.

- Permitir un crecimiento horizontal de servidores en caso de necesidad por cuestiones de rendimiento. El código debe permitir incrementar el número de servidores que atiendan el servicio de manera transparente para los centros.

- Adaptar a la nueva versión el script de copias de seguridad de bases de datos PostgreSQL y del código de Moodle. En caso de migrar una base de datos de servidor, el script debe guardar solo las bases de datos activas y referenciadas en los ficheros de configuración de cada centro.

## Mantenimiento de la plataforma MoodleMisc

Es necesario aplicar todas las tareas llevadas a cabo en el aula virtual multisite sobre la plataforma MoodleMisc como pueden ser las siguientes (EMOM3):

- Incidencias comunes AV (restauración de cursos, roles y permisos, etc)

- Instalar y configurar los distintos plugin procedentes de Madrid5e en Moodle (AulaPlaneta, Edebe, Smile&Learn), incluyendo a nuevas altas de AV.

- Solucionar errores de assignment a assign en Moodle.

- Crear sistema de gestión rápida por línea de comandos para el mantenimiento de la plataforma: Instalación y actualización de Moosh en cada frontal y adaptación al entorno MoodleMisc

- Mantener al día y adaptar a las nuevas versiones de PHP y Moodle los entornos de los siguientes plugin:

                - Plugin de conexión con mediateca (desarrollo propio)

                - Plugin de cuestionarios rápidos para Moodle

                - Plugin de MRBS para Moodle

                - Plugin de Reserva de aulas

                - Plugin de rol (desarrollo propio)

                - Plugin de quota (desarrollo propio)

                - Otros plugin ya disponibles o solicitudes futuras

- Desinstalar de forma controlada los plugins no activos u obsoletos.

- Mantener al día la Integración del Aula Virtual con el aplicativo Avisos.

- Mantener al día la Integración del Aula Virtual con Jitsi.

- Mantener al día la Integración del Aula Virtual con BigBlueButton.

- Mantener al día los datos publicados en el buscador de AV unificado.

- Integrar de forma paulatina el servicio en varios centros exteriores tanto del entorno MoodleMisc como del Multisite:

                - Bomberos Madrid.

                - Dirección General Bilingüismo y Calidad (multisite).

                - Otras.

- Adaptar la tarea periódica en Moodle a las distintas opciones para el borrado de grabaciones BBB.

- Resolución de incidencias derivadas del uso de la plataforma MoodleMisc, adoptando las medidas correctivas publicadas por el desarrollador del aplicativo Moodle.

- Realizar el mantenimiento evolutivo en el desarrollo del bloque de buscador de cursos

- Testear el rendimiento.

- Mantener al día el antivirus ClamAV y Modificar la presentación del proceso de análisis durante la subida de archivos. Se informará al usuario de que se realizará un análisis en busca de virus al finalizar la subida, y finalizada ésta, y mientras dura dicho proceso de análisis, se mostrará un mensaje informativo.

- Mantener al día el desarrollo que permite la funcionalidad para la recuperación de contraseña por parte de los usuarios y Revisar la interfaz de la recuperación de contraseña por parte de los usuarios para adaptarla a la imagen institucional de la Plataforma Educativa.

- Realizar el mantenimiento evolutivo de los editores de texto en la plataforma MoodleMisc. Deberán contar con configuración personalizada (menú y barra de tareas), y no permitirán la inserción de código JavaScript ni el pegado de contenidos en formato HTML. Deberán ser compatibles con el cambio de modo (oscuro/claro) de EducaMadrid.

- Evolucionar el desarrollo que evita la inserción de SCRIPTS en campos de tipo texto o TEXTAREA adaptándolo a las nuevas versiones de la plataforma.

- Realizar las adaptaciones de las Mejoras necesarias en la presentación en el libro de calificaciones de Moodle.

- Mantener al día el sistema de coloreado de sintaxis adaptándolo para los principales lenguajes de programación (Markup, CSS, JavaScript, Python, PHP, Java, C ...)

- Mantener al día los scripts necesarios para la gestión de bajas y cambios de nombre de usuarios, propagando dichos cambios a la plataforma MoodleMisc.

- Mantener al día el sistema de copias de seguridad anual de todos los cursos de todas las aulas virtuales de MoodleMisc, ofreciendo durante un año la posibilidad de ser recuperadas.

## Mejora de la Ciberseguridad en Moodle Misc

Es necesario aplicar todas las tareas llevadas a cabo en el aula virtual multisite sobre la plataforma MoodleMisc como pueden ser las siguientes (EMOM4):

- Modificar el mecanismo de autenticación para que los usuarios de Aulas virtuales con usuarios locales puedan acceder mediante correo electrónico. Es decir: sin cuenta de EducaMadrid .

- Realizar las siguientes tareas de ciberseguridad para el entorno:

                - Aplicar configuraciones seguras y actualizadas en base a la versión especifica de PHP implementada.

                - Ocultar información sensible de los hosts en cada versión implementada.

                - Actualizar cabeceras en el motor web para permitir marcos con origen único desde la propia página.

## Solución de problemas conocidos en Moodle Misc

Con las actualizaciones de Moodle pueden surgir ciertos problemas derivados de como usamos Moodle en EducaMadrid. Se pide llevar a cabo el desarrollo correctivo de los problemas que pudiesen sobrevenir en el entorno Moodle Misc, entre ellos, algunos recurrentes suelen ser: (EMOM5):

- Analizar y corregir el error con las fórmulas de Wiris.

- Subir la versión de todas las actividades HP5.

- Evitar el problema de repeticiones de eventos en calendarios.

- Arreglar problemas de definición del texto en las fórmulas Latex.

- Realizar el estudio y corrección de los errores de borrado de competencias.

- Aplicar correcciones relacionas con problemas de incompatibilidad con los plugin de las editoriales

## Tareas sobre las configuraciones para las conexiones externas

Existen diversas configuraciones de Moodle que deben llevarse a cabo en Moodle Misc. Se pide la realización de las siguientes tareas relacionadas con las configuraciones (EMOM6):

- Adaptar la nueva versión del plugin Marsupial y posteriormente personalizar para permitir conexiones entre los centros y editoriales que se soliciten, manteniendo las ya existentes.

- Configurar conexión LTI de manera personalizada para la conexión con Editoriales.

- Estudiar la viabilidad de habilitar los glosarios.

## Otras tareas específicas para la actualización y procedimiento en Moodle Misc

Actualmente hay algunas tareas de actualización en Moodle Misc que requieren varios pasos. Se pide la protocolización, automatización o actualización de estas tareas (EMOM7):

- Si la versión de Moodle disponible requiere una versión de PHP superior a la disponible en los frontales deberán generarse nuevos frontales, lo que implica:

                - Montar los nuevos frontales para Servicio de Aulas Virtuales.

                - Revisar las conexiones de los frontales con los distintos servicios necesarios:

                    - LDAP

                    - Base de datos

                    - MoodleData

                    - Volúmenes de datos

                - Actualizar Libre Office y Unoconv. Generar un demonio para unoconv.

                - Actualizar scripts de cron y monitorización de unoconv.

- Modificar los scripts de gestión de los centros:

                - Consulta

                - Gestión roles

                - Purgar caches

- Crear nuevos servidores de base de datos. Crear procedimientos de migración de bases de datos.

- Actualizar el script que instala todas las ‘actividades recomendadas’ del plugin H5P.

- Desarrollar scripts adicionales necesarios para la automatización de procesos.

- Generar un script que permita obtener algún dato sobre la configuración.

## ProyectoS de Dinámicas

La Plataforma de EducaMadrid dispone de un servicio web de páginas dinámicas que se ha quedado para sólo unos pocos centros con ciertas necesidades especiales. Se han alojado todas estas páginas en un único servidor, donde cada centro ejecuta sus páginas y aplicaciones web de forma independiente. En este servidor los aplicativos de terceros se sirven mediante centros ficticios de manera que tengan su espacio FTP, base datos y dominio independiente; de este modo se les proporciona una metodología de trabajo “auto gestionable” con sus espacios actualizables y gestionados de modo autónoma. El acceso FTP está habilitado con el id de usuario asignado en el LDAP.

Es necesario realizar el mantenimiento, la actualización y mejora tanto de este servidor como de las funciones necesarias para el acceso a las páginas, así como las tareas necesarias de ciberseguridad y adaptabilidad a la normativa ENS del entorno para evitar riesgos de nivel medio y altos (EDIN1).

Es necesario realizar también el mantenimiento, la actualización y mejora del espacio FTP para cumplir con la normativa ENS (EDIN2).

## Proyectos de Integración con la Plataforma de EducaMadrid

La mayor parte de los Proyectos Exteriores, tienden a integrarse de alguna forma u otra con la Plataforma de EducaMadrid, y a veces hay que modificar el core de algunas aplicaciones o desarrollar pequeños plugins y/o scripts en los entornos principales de la misma para realizar estas operaciones de integración.

Estas modificaciones en el core de algunas aplicaciones, el desarrollo de plugins y/o scripts, se realiza fundamentalmente en PHP, Python, Ruby, Java y/o Shell Script.

Se pide la posible modificación del core de algunas aplicaciones o desarrollar pequeños plugins y/o scripts en los entornos principales de la misma para realizar operaciones de mantenimiento e integración (EIPE1).

Así mismo, a veces hay que modificar el front de algunas aplicaciones mediate HTML/CSS/JS, se pide pues la posible modificación de pequeñas páginas de algunas de las aplicaciones de la Plataforma EducaMadrid para adecuar dicha integración (EIPE2).

## Proyectos de Sistemas Externos

## Servicio de actualización del software base

Por motivos fundamentalmente de seguridad y compatibilidad es necesario adaptar y mantener al día todo el software base del que dependen los aplicativos tales como PHP, Apache, WordPress, Moodle, etc… Estos cambios pueden impactar sobre los aplicativos, con lo que es necesario realizar los cambios necesarios para garantizar la funcionalidad de todas las aplicaciones una vez se han cambiado el software base. El ámbito de este pliego no contempla la actualización de aplicativos de proyectos exteriores, pero sí la sincronización con los responsables de los mismos para realizar la actualización necesaria del software base (ESIS1).

## Servicio de actualización del bases de datos

Así mismo, por motivos fundamentalmente de seguridad y compatibilidad es necesario mantener al día las bases de datos de la que dependen los aplicativos tales como MariaDB, PostgreSQL, MongoDB, etc… Estos cambios pueden impactar sobre los aplicativos, con lo que es necesario realizar los cambios necesarios para garantizar la funcionalidad de todas las aplicaciones una vez se han cambiado el software base. El ámbito de este pliego no contempla la actualización de aplicativos de proyectos exteriores, pero sí la sincronización con los responsables de los mismos para realizar la actualización necesaria de las bases de datos (ESIS2).

## Consultoría de integración

Actualmente la plataforma de EducaMadrid integra un conjunto de aplicaciones independientes que cooperan entre sí y usan datos y servicios comunes puestos a disposición de los usuarios de las distintas aplicaciones. Esto permite ofrecer un servicio transversal y homogéneo a la comunidad educativa.

Todas estas aplicaciones usan algunos o todos estos datos y servicios integrados de EducaMadrid. Las aplicaciones externas desplegadas en la plataforma también necesitan usar estos servicios, por lo que es necesario dotar a la plataforma de recursos para que las aplicaciones externas puedan usarlos sin impactar en las otras aplicaciones existentes.

Todas las aplicaciones externas añadidas que usen estos servicios transversales pueden impactar de forma general en el rendimiento de la plataforma. Para que el impacto sea sostenible es necesario estudiar cada caso concreto. Se responderán y aclararán las dudas y consultas tanto técnicas como funcionales de los desarrolladores de los aplicativos externos (ESIS3)

## Consultoría de ciberseguridad

Así mismo se les asesorará para que conozcan las formas de interactuación con los servicios que deben conectar con ellos e incluso se ayudará a la optimización de los accesos a los servicios existentes, al bastionado de la seguridad, con el desarrollo de conectores y con la adaptación de la información y los formatos a los sistemas existentes (ESIS4).

## Actualización de la autenticación centralizada de usuarios

La identidad de los usuarios de la comunidad educativa de la Comunidad de Madrid está definida mediante cuentas existentes en los servidores de EducaMadrid. Mediante SSO o LDAP los aplicativos externos necesitan utilizar y validar las identidades y credenciales de docentes, alumnos, PAS y centros. Para ello es necesario el mantener y adaptar y actualizar los conectores, así como adaptar los datos para prepararlos a la medida de las aplicaciones externas. (ESIS5).

## Mantenimiento de la autenticación centralizada de usuarios

Además, será imprescindible:

- Actualizar periódicamente las versiones de los componentes implicados, tanto del lado del software de identidad (servidores LDAP, SSO, etc.) como de los conectores y librerías utilizadas por los servicios externos.

- Adaptar la infraestructura para dar soporte a nuevos requerimientos funcionales, de rendimiento o de seguridad derivados de las actualizaciones tecnológicas o de normativas.

- Garantizar que todas las integraciones cumplen con las nuevas normativas vigentes, incluyendo los requisitos del Esquema Nacional de Seguridad (ENS) y las directrices técnicas de EducaMadrid.

- Planificar y validar previamente cualquier cambio de versión o tecnología, asegurando la compatibilidad con los servicios educativos ya integrados y minimizando el impacto en la experiencia de los usuarios finales.

Esta evolución será continua y coordinada con los responsables de las plataformas externas, buscando siempre mantener la interoperabilidad, la trazabilidad y la seguridad en el acceso a los recursos educativos.  (ESIS6)

## Gestión de servicios para la sincronización de usuarios

En el marco de la integración de servicios externos con la infraestructura de EducaMadrid, resulta imprescindible disponer de una herramienta que permita validar y, si es necesario, sincronizar bajo demanda los datos de identidad y atributos de los usuarios (docentes, alumnos, PAS y cuentas institucionales) con dichos servicios (ESIS7).

## Supervisión de usuarios de aplicaciones externas

Además, de cara a los usuarios de aplicaciones externas, hay que mantener actualizado y operativo un aplicativo web de uso restringido, con interfaz segura y autenticada, que permite (ESIS8):

- Comprobar la existencia y estado de una identidad en los servicios de EducaMadrid a partir de identificadores clave.

- Visualizar los atributos asociados al usuario de forma segura y controlada.

- Contemplar la posibilidad de sincronización bajo demanda de usuarios.

- Aplicar una integración segura con el sistema de identidad centralizado.

- Garantizar el cumplimiento del principio de mínimo privilegio, limitando el uso del aplicativo únicamente a perfiles autorizados y delegados por los responsables del servicio.

- Facilitar el uso del sistema a través de una interfaz web accesible y usable, sin comprometer los aspectos de seguridad y privacidad.

## Soporte técnico en entornos de preproducción

Es necesario dar soporte a los desarrolladores externos para (ESIS9):

- Instalar los aplicativos externos (independientes, plugins, bases de datos, etc…) en los servidores de la plataforma en los entornos de preproducción.

- Establecer las configuraciones iniciales.

## Despliegue de aplicaciones externas en producción

Asimismo, es necesario dar soporte a los desarrolladores externos para (ESIS10):

- Desplegar en producción los aplicativos.

- Testar las funcionalidades y evaluar el impacto en el entorno dónde se integra.

## Integración en el Gestor de Servidores de Bases de Datos

EducaMadrid dispone de un Gestor de Servidores de Bases de Datos que integra todos los servidores de bases de datos de todas las aplicaciones, con lo que hay que registrar todos los servidores de las aplicaciones externas para gestionar y mantener sus bases de datos (ESIS11).

## Estudio de los recursos solicitados

Como base para los servicios de mantenimiento y soporte futuros hay que realizar una tarea de “estudio de los recursos solicitados” para cada uno de los Proyectos Exteriores existentes (ESIS12).

Esta tarea consistirá en elaborar un análisis previo de los diferentes componentes hardware/software necesarios, así como los aplicativos que correrán en estos y su impacto en la plataforma, lo que incluye:

- Estudiar los Sistema Operativos, así como la versión necesaria de instalación de los mismos.

- Estudiar las BBDD necesarias, así como su versión para su posterior instalación.

- Estudiar los aplicativos necesarios a instalar incluidas todas sus dependencias.

- Estudiar las características de red necesarias.

- Estudiar las necesidades de almacenamiento, capacidad y performance del mismo.

- Estudiar el impacto con el resto de los componentes de la plataforma EducaMadrid.

## Solicitud de los recursos necesarios

Una vez realizada y validada la fase de estudio, se procederá a realizar una “solicitud de los recursos necesarios” (ESIS13), que consiste en:

- Trasladar la petición para la creación y configuración de las máquinas virtuales, así como el despliegue de todos los componentes necesarios.

- Se deberá tener en cuenta si el servicio solicitado está en Backend, FrontEnd o en ambos. Eso se traduce en peticiones de apertura de puertos tanto en los servidores como en los equipos de electrónica de red.

- Se tendrá que tener en cuenta tanto las necesidades actuales como el posible crecimiento y escalabilidad del mismo, para asignar los recursos, de CPU, memoria, red y almacenamiento.

## Bastionado de los recursos solicitados

Una vez solicitados los recursos es necesario (ESIS14):

- Aplicar las políticas de bastionado del sistema (tanto para entornos virtualizados como Dockerizados), incluyendo la desactivación de servicios innecesarios, aplicación de configuraciones seguras y el endurecimiento de imágenes base mediante guías STIC o equivalentes.

## Instalación de la paquetería y gestión de dependencias

Con los servidores provisionados, se procede a realizar las labores propias de “instalación de paquetería y gestión de las dependencias” (ESIS15).

Dicha instalación se realizará en paralelo a la documentación de los nuevos entornos. La fase de instalación se divide en las siguientes tareas:

- Instalar Software base (requerimientos previos aprobados en el análisis de recursos)

- Instalar repositorios necesarios y opcionales.

- Instalar el SGBD necesario (si fuera el caso).

- Instalar el aplicativo requerido.

- Instalar librerías o módulos necesarios.

- Configurar el almacenamiento necesario, así como la configuración de puntos de montaje solicitados.

- Configurar módulos web.

- Aplicar de las actuales medidas de ciberseguridad básicas, como la configuración de permisos mínimos, creación de usuarios de servicio sin privilegios, desactivación de servicios innecesarios, y preparación del sistema para su integración en el sistema de monitorización y alertas.

- Configurar el sistema operativo acorde a las políticas de la plataforma: configuración de logs y afinado de parámetros de rendimiento.

<!-- salto de página -->

## Configuración del entorno

Así mismo hay que realizar las siguientes tareas de configuración (ESIS16):

- Configurar el almacenamiento necesario, así como la configuración de puntos de montaje solicitados.

- Configurar módulos web.

- Aplicar de las actuales medidas de ciberseguridad básicas, como la configuración de permisos mínimos, creación de usuarios de servicio sin privilegios, desactivación de servicios innecesarios, y preparación del sistema para su integración en el sistema de monitorización y alertas.

- Configurar el sistema operativo acorde a las políticas de la plataforma: configuración de logs y afinado de parámetros de rendimiento.

## Soporte para la integración con el LDAP de la plataforma EducaMadrid

Cada vez que se produce un aprovisionamiento, se procede a realizar las labores propias de “integración con los diferentes componentes estándar de la plataforma” como puede ser la integración con el LDAP de la plataforma o incluso realizar una integración en un LDAP esclavo, con los requerimientos especificados en las anteriores fases (ESIS17).

## Soporte para la integración con el sistema de correo de la plataforma EducaMadrid

Adicionalmente, en los nuevos proyectos, se tiene que realizar una configuración de los estándares de correo smtp para, por un lado, dar soporte de correo a los nuevos proyectos y por otro asegurar el correcto funcionamiento de los mismos asegurando el relay smtp (ESIS18).

## Soporte para la integración con distintas BBDD de la plataforma EducaMadrid

En los casos que se requiera, se llevan a cabo las labores propias de interconexión entre BBDD instaladas en otros proyectos, así como tener el control de la seguridad de las mismas y la gestión del control de cambios (ESIS19).

## Soporte para la integración del CMDB de la plataforma EducaMadrid

Para poder adaptarse a las tareas específicas del entorno de Educamadrid, será también necesario realizar las modificaciones oportunas en la base de datos de la gestión de la configuración (CMDB) de manera recurrente (ESIS20)

## Documentación del proyecto externo

Una vez se implementan las fases anteriores se debe documentar el proyecto (ESIS21):

Para ello se definirá y generará:

- Documentación del proyecto:

                - Entorno y funcionalidad.

                - Accesos internos, Externos.

- Documentación del sistema:

                - Máquinas.

                - Redes internas y conexiones al exterior.

## Gestión del riesgo del proyecto externo

Una vez se implementan las fases anteriores se procede a la “gestión del riesgo” del proyecto (ESIS22)

Para ello se definirá y generará:

- Puntos de acceso al proyecto/sistema (vpn, ftp, consolas de administración).

- Esquema de red y seguridad del mismo.

                - Puntos de interconexión a otros sistemas o a otras redes de dentro o fuera de EducaMadrid.

                - Cortafuegos y DMZ.

## Implementación de sistemas de Backups y procedimiento de Disaster Recovery

Una vez se implementan las fases anteriores se procederá a identificar los principales riesgos a lo que se encuentra expuesto el proyecto, realizando una selección de los servicios críticos y el alcance de los mismos. (ESIS23)

Esto lleva a “definir el RTO y RPO necesarios para la implementación de los backups” necesario, continuando con la especificación de los requerimientos técnicos con base a los estándares definidos por el proyecto.

Se propondrá la mejor opción de salvaguarda a nivel de Sistemas, realizando la implementación y la automatización necesaria de tecnología para la implementación del backup y el disaster recovery que soporte cada uno de los proyectos externos.

Se establecerá un procedimiento anual de verificación y restauración de copias de seguridad, con el fin de garantizar la integridad, disponibilidad y funcionalidad de los datos salvaguardados, cumpliendo con los requisitos del ENS y las buenas prácticas de continuidad de negocio.

## Implementación de monitorización básica

Se realizará como parte de la labor de mantenimiento y gestión del servicio una “implementación básica de monitorización” (ESIS24).

Incluirá información de monitorización de los diferentes componentes de la infraestructura del proyecto, una vez que dicho proyecto pase al entorno productivo.

- Dicha monitorización básica en muchos casos se solicita de una manera específica que pase a ser una monitorización avanzada para tener en cuenta monitorización del tipo SEO o de ciberseguridad para verificar accesos externos al proyecto, así como accesos web.

- Dentro de la monitorización estándar también se realizará una monitorización del performance del host, así como la monitorización diaria de los backups realizados.

## Implementación de monitorización avanzada

Los entornos que así lo soliciten tendrán una monitorización externa en la que se detecten anomalías y problemas tanto de conectividad, como de performance, dicha monitorización tendrá que ser gestionada de manera independiente a la monitorización de infraestructura (ESIS25).

## Implementación de servicios de ciberseguridad básicos

Como parte del proceso de mantenimiento y seguridad de la plataforma, se tiene que llevar a cabo una “implantación de medidas de ciberseguridad” básicos alineada con los requisitos del Esquema Nacional de Seguridad y las mejores prácticas en seguridad (ESIS26).

- Control de accesos a los servidores, incluyendo la implantación de mecanismos de autenticación robusta (doble factor de autenticación para cuentas privilegiadas y acceso remoto).

- Gestión centralizada de certificados digitales, con auditoría del estado actual y planificación de renovaciones automáticas.

- Corrección de vulnerabilidades y debilidades en los dominios gestionados por EducaMadrid.

## Implementación de servicios de ciberseguridad avanzados

Como parte del proceso de mantenimiento y  seguridad de la plataforma, se tiene que llevar a cabo una “implantación de medidas de ciberseguridad” avanzados alineada con los requisitos del Esquema Nacional de Seguridad y las mejores prácticas en seguridad (ESIS27).

- Protección de servicios no web, aplicando medidas específicas para accesos a protocolos como SMTP, IMAP, POP3 o SSH.

- Generación de alertas ante eventos de seguridad relevantes, como cambios de contraseñas, creación/eliminación de usuarios, o modificaciones en el sistema de identidad centralizado.

- Supervisión de cambios en configuraciones DNS de los dominios de EducaMadrid, con alertas ante modificaciones no autorizadas.

- Otras acciones de refuerzo y control que se consideren necesarias tras el análisis inicial, incluyendo integración con herramientas SIEM, escaneos automatizados y hardening adicional de los entornos.

## Actualización de los sistemas operativos

Los técnicos del contratista realizarán las actuaciones preventivas necesarias para tener actualizados los sistemas Operativos de los entornos de los proyectos exteriores, así como el software base, las BBDD y los diferentes componentes de los mismos para que se encuentren en todo momento dentro de la matriz de compatibilidad y soporte y nunca estar fuera del EOL. (ESIS28)

## Gestión y seguimiento del proyecto

Una vez finaliza la fase de puesta en producción, en ningún caso se dará por finalizado el proyecto, ya que quedará por hacer la labor más importante que consiste en realizar un desarrollo evolutivo y adaptativo continuado que se puede dividir en las siguientes funciones a realizar:

- Priorización, coordinación, supervisión y seguimiento general de los sistemas de los proyectos.

- Coordinación con los diferentes actores involucrados en los proyectos.

- Coordinación y supervisión de integraciones y estándares del proyecto.

- Documentación continuada y gestión del conocimiento.

Se incluyen en esta línea de trabajo las actividades relativas a la gestión y seguimiento del propio proyecto, cuyos indicadores e informes deben ser reportados al Jefe de Servicio de EducaMadrid para su aprobación y control. (ESIS29)

## Segmentación de la actual red de servidores

Dentro de las labores de mantenimiento y con el objeto de mantener el servicio con los estándares de calidad actuales, tras las últimas ampliaciones y en previsión del futuro crecimiento, es necesario mejorar la segmentación de la actual red de servidores, de modo que los servidores dedicados a los Proyectos Exteriores queden separados del resto. Algunos proyectos han sido migrados a ese nuevo segmento de red, pero es necesario continuar con la migración hasta que todos estén en ella. También será necesario mantener al día y mejorar el sistema de control de acceso y bastionado de la nueva red de Proyectos Exteriores.

Esto incluye (ESIS30):

- Mantener al día en este segmento de red un sistema de gestión según el modelo Zero Trust.

- Preparar un servidor de VPN específico para esa red. Migrar todas las cuentas de acceso por VPN de los Proyectos Exteriores al nuevo segmento de red.

- Poner en marcha un sistema de MFA, para el acceso y uso de esos servidores. Sería deseable que el acceso a la administración de los servidores se haga a través de certificados.

## Optimización de la infraestructura de virtualización del entorno

Como parte de las labores de mantenimiento evolutivo y mejora continua del servicio, y teniendo en cuenta tanto las ampliaciones recientes como las nuevas demandas de rendimiento, seguridad y disponibilidad, se hace necesaria una optimización de sistemas sobre la infraestructura en la que se sustentan los servidores y servicios de los Proyectos Exteriores.

Esta actualización tendrá como objetivo garantizar un rendimiento óptimo, facilitar las tareas de mantenimiento, actualización y escalado, y cumplir con las normativas técnicas y de seguridad actuales.

Para ello será necesario (ESIS31):

- Evaluar el hardware cuando sea necesario, especialmente en lo relativo a servidores con carga crítica.

- Reorganizar la infraestructura asegurando un diseño eficiente de los recursos asignados (vCPU, RAM, almacenamiento).

- Establecer pools de recursos dedicados para los Proyectos Exteriores, que permitan aislar la carga de trabajo de estos entornos del resto de servicios internos.

- Adoptar un modelo de escalado flexible, que permita crecer horizontal o verticalmente en función de las necesidades de cada proyecto, reduciendo los tiempos de aprovisionamiento y respuesta.

- Incorporar soporte para carga de trabajo con GPU, permitiendo la ejecución eficiente de entornos dependientes de inteligencia artificial (IA).

## Seguridad de Aplicaciones Web

A continuación, se enumeran los distintos trabajos a desarrollar en el ámbito del contrato, así como la lista de los entregables clasificados por áreas o aplicaciones/servicios según la nomenclatura indicada en el apartado anterior.

## Realización de Auditorías/Pentesting Web

Como parte del mantenimiento evolutivo de seguridad de la plataforma, se pide llevar a cabo las tareas necesarias para conocer el estado de la seguridad de las aplicaciones Web alojadas en la plataforma de EducaMadrid, así como las recomendaciones de resolución de los problemas de seguridad encontrados. (ESEG1)

## Gestión de logs de las aplicaciones Web

Se solicita el mantenimiento evolutivo y la gestión de los logs de las aplicaciones web alojadas en la plataforma de EducaMadrid, su integración con Wazuh y el análisis de los mismos para integrarlo dentro de la visión del estado de la Seguridad de las Aplicaciones Web. (ESEG2)

## Análisis y protección de la superficie de ataque

Se solicitan las tareas necesarias para realizar el mantenimiento evolutivo de la Superficie de Exposición, a nivel web, de la plataforma EducaMadrid, lo que incluye la supervisión de los dominios DNS y del estado de los certificados asociados a los mismos. (ESEG3)

## Realización de pruebas de desarrollo seguro de aplicaciones web

A continuación, se enumeran los distintos trabajos a desarrollar en el ámbito del contrato, así como la lista de los entregables clasificados por áreas o aplicaciones/servicios según la nomenclatura indicada en el apartado anterior.

## Análisis de Código Web

Se solicita el mantenimiento evolutivo y la supervisión del estado de la Seguridad del Código de las Aplicaciones Web, de la plataforma EducaMadrid, lo que incluye el análisis del código de las aplicaciones. (EDSA1)

## Ayuda al Desarrollo Seguro de Código Web

Se solicita la gestión de incidencias respuesta a preguntas y dudas que se planteen desde el equipo de Desarrollo para mejorar la posición del estado de la Seguridad del Código de las Aplicaciones Web, de la plataforma EducaMadrid. (EDSA2)

## Gestión del programa de Bug Bounty

A continuación, se enumeran los distintos trabajos a desarrollar en esta área en el ámbito del contrato, así como la lista de los entregables clasificados por áreas o aplicaciones/servicios según la nomenclatura indicada en el apartado anterior.

## Mantenimiento y gestión del programa de Bug Bounty

Se solicita la revisión y gestión del programa de Bug Bounty, recibiendo y procesando los posibles informes recibidos a través de dicho programa y coordinando la actualización de la información disponible en la web creada para el programa. (EBBO1)

## PRODUCTOS RESULTANTES DEL CONTRATO, INCLUYENDO LOS REQUISITOS DE DOCUMENTACIÓN.

En los puntos anteriores se concretan todos los trabajos que se requieren en el desarrollo del contrato describiéndose y enumerándose cada uno de los entregables siguiendo la nomenclatura del apartado 1 del presente documento.

| Mantenimiento evolutivo y adaptativo de Proyectos web Liferay (ELIF) | 4 |
| --- | --- |
| Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado (IFP) | 1 |
| Proyectos Moodle Misc (EMOM) | 7 |
| Proyectos de Dinámicas (EDIN) | 2 |
| Proyectos de Integración con la Plataforma de EducaMadrid (EIPE) | 2 |
| Proyectos de Sistemas Externos (ESIS) | 31 |
| Seguridad de aplicaciones WEB (ESEG) | 3 |
| Realización de pruebas de desarrollo seguro de aplicaciones WEB (EDSA) | 2 |
| Mantenimiento y gestión del programa de Bug Bounty (EBBO) | 1 |
| **TOTAL** | **53** |

En total se describen **53 entregables** en este documento.

Se entiende por entregables los elementos desarrollados en el desarrollo de las tareas del servicio que constituyen componentes del servicio o del producto software objeto de desarrollo, en los que dicho producto software será un entregable más del proyecto.

El adjudicatario se compromete a que los técnicos registren periódicamente el desarrollo y avance de los trabajos realizados en la herramienta que designe EducaMadrid (actualmente Redmine). La información registrada será suficiente para que EducaMadrid pueda informarse acerca de las tareas que se están realizando y del estado de avance de dichos trabajos, y será completa hasta el punto de que, en caso de baja, cese o sustitución de alguno de los técnicos, el técnico que le sustituya pueda continuar desde el punto en el que se encuentre.

Asimismo, EducaMadrid establecerá las prioridades de los trabajos y tareas a realizar en función de su propia estrategia, o de las necesidades o requisitos de los usuarios y de los servicios que ofrece. El establecimiento de prioridades y estrategias se podrá llevar a cabo en cualquier momento y a través del medio o herramienta que EducaMadrid indique al adjudicatario.

Con el fin de verificar tanto la seguridad de los sistemas como el cumplimiento de las prioridades, tareas y dedicación comprometidas a través del servicio contratado, el adjudicatario informará tanto del trabajo realizado como de las tareas específicas en las que ha estado involucrado cada uno de sus técnicos. EducaMadrid indicará al adjudicatario, la forma, herramienta, medio y periodicidad con la que se requerirá esta información. Dado que, en la actualidad, se pide que se refleje esta información de forma diaria y con el objetivo de minimizar la burocracia del proceso, EducaMadrid admite que dicha información sea facilitada por cada técnico directamente al finalizar su jornada, siempre y cuando así lo estimara conveniente el adjudicatario.

El adjudicatario se compromete a generar toda la documentación que sea aplicable como resultado de la prestación de los servicios y el desarrollo de cada uno de los entregables, entregando la documentación correspondiente en el formato electrónico que se determine.

El adjudicatario pondrá a disposición de EducaMadrid en todo momento la documentación que se vaya generando durante el proceso de desarrollo del proyecto y de cada uno de los entregables.

Para cada entregable, según las características del mismo y siguiendo la planificación acordada, se aportará la información que aplique, desarrollándose los contenidos necesarios según los puntos siguientes:

- Estudios Previos

- Catálogo de requisitos

- Análisis funcional (descripción funcional, casos de uso, diagramas de estados, modelo conceptual de datos, sistemas externos, etc.)

- Diseño funcional y técnico (arquitectura, soluciones técnicas utilizadas, patrones de diseño, modelos de datos, interfaces, diagramas de clases, de secuencia, etc.)

- Planes de pruebas funcionales

Resultados del plan de pruebas funcionales

- Configuración de las pruebas de rendimiento

- Requerimientos mínimos de instalación

- Plan de gestión del cambio (material de comunicación y formación, presentaciones, material divulgativo, etc.)

Informe de situación e incidencias

- Documentos de seguimiento (planificaciones, actas de reunión, informes de seguimiento, etc.)

- El adjudicatario se compromete, en su caso, a la entrega final de los productos resultantes de los trabajos de desarrollo:

- Fuentes: programas, scripts, archivos de instalación y configuración, etc.

- Documentaciones técnicas y funcionales (catálogo de requisitos, diseño funcional y técnico, modelo de datos, manual de instalación, manual de operación/explotación, notas de versiones, manuales de usuario, material de formación, etc.)

En general, se exigirá como entregable toda la información necesaria para la correcta instalación, operación, uso, mantenimiento y monitorización de los sistemas desarrollados.

Toda la documentación deberá entregarse actualizada. El organismo peticionario determinará si la documentación aportada debe ser mejorada, completada, ampliada o elaborada de otro modo para su mejor aprovechamiento por la organización.

En caso de existir, se asegurará la calidad en las entregas de desarrollos de software antes de su paso al entorno de producción, conforme a las políticas y estándares definidos y a través de los procedimientos y herramientas implantados.

Las entregas de software (documentación y software) deberán cumplir con los estándares de calidad, pudiéndose realizar validaciones y pruebas del tipo siguiente:

- Validación del estilo de codificación (uniforme, claro y ajustado a estándares).

- Pruebas de seguridad automatizadas, como la explotación de vulnerabilidades típicas de las aplicaciones Web, y verificación de checklists asociadas a la normativa de desarrollo seguro de software basadas en guías de estándares y metodologías OpenSource Security Testing Methodology Manual (OSSTMM), Open Web Application Security Project (OWASP), o equivalentes. el estilo de codificación (uniforme, claro y ajustado a estándares).

- Pruebas unitarias y de regresión automatizadas que permitan validar el correcto funcionamiento de los módulos de la aplicación. Pruebas funcionales automatizadas para verificar que el producto entregado cumple con los requisitos y necesidades establecidos, mediante el uso de herramientas que permitan la grabación y almacenamiento de pruebas de usuario para posteriores pruebas de regresión y para su ejecución y certificación en distintos entornos.

- Pruebas de rendimiento para el aseguramiento de que el software cumple con las cargas de trabajo previstas.

- Monitorización técnica de aplicaciones, para obtener información del funcionamiento y consumo de recursos de la aplicación en el tiempo y detectar las causas de los errores una vez producidos.

Pruebas de seguridad automatizadas, como la explotación de vulnerabilidades típicas de las aplicaciones Web, y verificación de checklists asociadas a la normativa de desarrollo seguro de software basadas en guías de estándares y metodologías OpenSource Security Testing Methodology Manual (OSSTMM), Open Web Application Security Project (OWASP), o equivalentes.

## ESFUERZO ESTIMADO

El total de esfuerzo ordinario en las tareas de mantenimiento evolutivo y adaptativo se estima en **5.357,79 horas al año** (10.715,58 horas en los dos años de contrato) a cargo de los diferentes perfiles indicados en el apartado correspondiente.

El total de **esfuerzo extraordinario fuera del horario ordinario y para el servicio de guardia** se estima en **531 horas al año** (1.062 horas en los dos años de contrato), que podrá llevar a cabo cualquiera de los perfiles del contrato.

<!-- salto de página -->

# SERVICIOS DE MANTENIMIENTO BAJO ANS

Corresponden a los servicios para el mantenimiento de las aplicaciones en funcionamiento en entornos en producción de usuarios finales conforme a lo descrito en el Anexo I y en el Anexo II.

Debido a su naturaleza, el mantenimiento correctivo y la gestión de las incidencias de los proyectos exteriores supone una carga de trabajo equivalente a la reflejada en el ANEXO II.

## Descripción del servicio de mantenimiento

## Alcance

Las tareas de mantenimiento correctivo y la gestión de las incidencias de los proyectos exteriores estarán orientadas al aseguramiento de la continuidad del servicio de los sistemas en entornos productivos cubrirá el conjunto de los sistemas de información y el entorno tecnológico descritos en el Anexo I y en el Anexo II.

El servicio consiste en la corrección del código fuente o de la documentación para resolver o paliar las incidencias que afecten a los citados sistemas de información, así como todas las tareas conexas necesarias para poder realizar dicha corrección.

Concretamente el contrato estará centrado en las tareas que se refieren tanto a los Proyectos Exteriores actualmente alojados en la Plataforma Educativa EducaMadrid como a los que pudieran surgir, de naturaleza similar, a lo largo de la vigencia del contrato.

En el mantenimiento de los servicios ofrecidos se deben incluir tanto las tareas relativas al mantenimiento correctivo como la gestión de incidencias de las distintas aplicaciones y sistemas implicados en los Proyectos Exteriores.

## Gestión de incidencias

El Responsable del Contrato Específico, o la persona designada por éste para la tarea, clasificará las incidencias que detecte y las que comuniquen los usuarios, comunicándolas a su vez al contratista por escrito, mediante correo electrónico o herramienta de gestión del servicio (en inglés, *ITSM*) según decisión del organismo destinatario, haciendo constar:

- Fecha y hora;

- Sistema, módulo o componente en el que se perciben los efectos de la incidencia;

- Gravedad de la incidencia, clasificada como Leve, Grave o Crítica;

- Descripción de los efectos observados como consecuencia de la incidencia.

En ningún caso los usuarios del sistema de información se dirigirán directamente al personal asignado por la adjudicataria a la ejecución del presente contrato específico.

Para gestionar las incidencias y restaurar el nivel del servicio la metodología sigue los siguientes pasos que abarcan todo el ciclo de vida de los incidentes.

- Detectar. Ya sea usando un sistema de monitorización o a través de las tareas propias de revisión de los técnicos se deben detectar las incidencias.

- Registrar. Todo incidente quedará registrado en la herramienta de ticketing de EducaMadrid.

- Categorizar. La categorización implica asignar en nivel del incidente para priorizar y realizar un seguimiento de este de la manera más precisa posible.

- Priorizar. Se evaluará si un incidente puede ser solucionado inmediatamente, si se puede solucionar más adelante o si es necesario la intervención de otras partes.

- Resolver. Dentro de las tareas de resolución de las incidencias se realizarán varias fases que consisten en:

    - Investigación y diagnóstico de la incidencia.

    - Resolución y recuperación de esta.

- Cierre. Esta será la etapa final del ciclo de vida de la incidencia. El cierre se categoriza y la incidencia se cumplimenta con todas las tareas realizadas.

Dentro de las labores de desarrollo correctivo y gestión de incidencias se generará nueva documentación (ya sea en formato texto, o en formato audiovisual) y se corregirá la existente de la Plataforma EducaMadrid, necesaria para la correcta utilización de los servicios y aplicaciones de la plataforma.

Asimismo, se atenderán incidencias por teléfono, correo electrónico u otros medios electrónicos relacionados con toda la plataforma de EducaMadrid, especialmente las relativas a los servicios aquí expuestos.

Existen 2 niveles de incidencia:

- Nivel 1, que es llevada a cabo por técnicos de soporte de nivel 1, que conocen la plataforma de EducaMadrid a nivel funcional, y que no pertenecen al ámbito de este pliego.

- Nivel 2, que será llevada a cabo por los analistas programadores o por los técnicos de sistemas. Estas incidencias serán de carácter técnico.

## Concepto de Incidencia

Se considera "Gestión de incidencias" al conjunto de servicios colaterales que la firma adjudicataria deberá realizar para garantizar el correcto funcionamiento de los aplicativos que se mencionan en el presente pliego, de acuerdo con ANS definidos, así como para proporcionar la información periódica necesaria.

## Horario de servicio

Se considera horario de servicio a la franja horaria diaria en la que la empresa contratista está en disposición tanto de recibir una comunicación como de acometer la resolución de la misma.

El contratista estará obligado a contemplar un horario de servicio mínimo que comprenderá de 8:00 h a 18:00 h, de lunes a viernes.

Excepcionalmente podrán realizar trabajos extraordinarios programados fuera de ese horario y también en días no laborables para labores de configuración e instalación que no pueda llevarse a cabo en el horario ordinario.

**Soporte continuo**

Fuera del horario de servicio, podrán surgir incidencias, y las más críticas deberán solucionarse incluso fuera del horario de servicio. Se realizará pues un soporte continuado para que los diferentes proyectos funcionen **las 24 horas al día, los 7 días de la semana**. La mayoría de los proyectos exteriores tienen una dependencia importante con diversos componentes internos y externos y esto requiere un soporte adicional que entienda lo que se requiere para asegurar una interrupción mínima del proyecto.

## Esfuerzo estimado

El total de esfuerzo ordinario en las tareas de mantenimiento correctivo y gestión de incidencias se estima en **5.357,79 horas al año** (10.715,58 horas en dos años) a cargo de los diferentes perfiles indicados en el apartado correspondiente.

## Clasificación de las incidencias

| **Criticidad** | **Grado de inoperatividad del sistema** |
| --- | --- |
| Leve | Aquellas anomalías en el funcionamiento de las aplicaciones en explotación que no supongan una interrupción en la operatividad de la aplicación, pero puedan afectar a funciones no básicas o a su rendimiento. |
| Grave | Aquellas anomalías en el funcionamiento de las aplicaciones en explotación que suponen una interrupción parcial significativa en la operatividad de la aplicación, de forma que no permitan la ejecución de una o más funciones básicas ofrecidas por el aplicativo. |
| Crítica | Aquellas anomalías en el funcionamiento que suponen una interrupción completa de la operatividad de las aplicaciones. |

## Dimensionamiento del servicio

En función de la experiencia anterior con los módulos ya en producción y atendiendo a la complejidad de este sistema, el adjudicatario deberá dimensionar el servicio de manera que se puedan resolver mensualmente el siguiente número de incidencias de cada tipo (según clasificación descrita en el apartado anterior):

- Categoría leve: 20

- Categoría grave: 8

- Categoría crítica: 2

## Acuerdos de nivel de servicio

A efectos de cálculo del cumplimiento de los ANS, sólo computa el tiempo transcurrido dentro del horario de prestación del servicio descrito en el apartado anterior y atendiendo al dimensionamiento anterior.

Se definen ANS correspondientes al tiempo de respuesta ante una incidencia y al tiempo de resolución de un problema.

## Tiempo de respuesta

Se considera tiempo de respuesta al que transcurre desde la comunicación al contratista, por parte de la Consejería de Digitalización, de un problema, hasta la recepción de la contestación del contratista, con la planificación de su solución.

El contratista estará obligado a contemplar un tiempo de respuesta de **2 horas** computables en el horario de servicio.

## Tiempo de resolución de un problema

Se considera tiempo de resolución de un problema al que transcurre desde la comunicación al contratista, por parte la Consejería de Digitalización del problema hasta la resolución del mismo.

La resolución de las incidencias incluirá la realización de pruebas de regresión, con el objetivo de eliminar el efecto onda, es decir, comprobar que los cambios sobre un componente de un sistema no introducen un comportamiento no deseado o errores adicionales en otros componentes no modificados.

El adjudicatario estará obligado a resolver la incidencia en un plazo máximo de tiempo de **1 jornada laboral** de lunes a viernes, fijado según el nivel de la incidencia (ver tabla), a contar desde la comunicación del problema.

| **Criticidad** | **Tiempo de resolución de la incidencia** |
| --- | --- |
| Leve | Tiempo de resolución no superior a 24 horas |
| Grave | Tiempo de resolución no superior a 12 horas |
| Crítica | Tiempo de resolución no superior a 6 horas |

Cuando la resolución de la incidencia requiera la realización de desarrollos que por su naturaleza necesitan de un plazo material superior al indicado en la tabla precedente, el contratista estará obligado a presentar al Responsable del Contrato Específico en el organismo destinatario, dentro del plazo de tiempo de resolución inicial, un **P***lan de A***ctuación** que incluya la duración prevista de los trabajos para la resolución, la justificación de dicha previsión y la descripción de los trabajos a realizar. Si es necesario, se incluirá la descripción de las medidas paliativas a adoptar hasta la completa resolución de la incidencia. Dicho plan deberá ser aprobado por el responsable del Contrato Específico.
