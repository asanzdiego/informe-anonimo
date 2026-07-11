# 1. MEMORIA TÉCNICA “DESARROLLO EVOLUTIVO Y CORRECTIVO DE LAS AULAS VIRTUALES, LA MEDIATECA, LAS WEBS DE CENTRO, EL CORREO WEB, EMPIEZA Y OTRAS APLICACIONES DE EDUCAMADRID”

Número de Expediente: BAC07\_2026 (PLACSP Nº 2021/16)

Sobre 1: Documentación relativa a los criterios de adjudicación cuya ponderación está sujeta a un juicio de valor

Este documento es propiedad de empresa_s y su contenido es confidencial. Este documento no puede ser reproducido, en su totalidad o parcialmente, ni mostrado a terceros, ni utilizado para otros propósitos que los que han originado su entrega, sin el previo permiso escrito de empresa_s . En el caso de ser entregado en virtud de un contrato, su utilización y difusión estarán limitadas a lo expresamente autorizado en dicho contrato. empresa_s no podrá ser considerada responsable de eventuales errores u omisiones en la edición del presente documento.

Rev A




Contenido

1 IDENTIFICACIÓN DE LA EMPRESA....................................................................... 3
2 RESUMEN EJECUTIVO ........................................................................................ 5
3 MEMORIA TÉCNICA ............................................................................................ 9
3.1 SOLUCIÓN TÉCNICA OFERTADA ......................................................................... 9
3.1.1 ARQUITECTURA PLANTEADA EN LOS DISTINTOS SUBPROYECTOS .............. 9
3.1.2 GRADO DE COMPRENSIÓN DE LOS REQUISITOS PLANTEADOS ................... 12
3.1.3 VIABILIDAD DEL PROYECTO EN GENERAL................................................... 25
3.1.4 METODOLOGÍA DE TRABAJO APLICADA ..................................................... 39
3.1.5 RENDIMIENTO PREVISIBLE DE LAS DISTINTAS SOLUCIONES ..................... 42
3.1.6 SATISFACCIÓN DE LOS REQUISITOS .......................................................... 49
3.1.6.1 DEFINICIÓN Y ALCANCE DE LOS TRABAJOS ............................................ 49
3.1.6.2 SERVICIO DE MANTENIMIENTO 24/7 Y CAU ........................................... 154
3.2 PLANIFICACIÓN DEL SERVICIO ....................................................................... 160
3.2.1 CALENDARIO DE LOS TRABAJOS A DESARROLLAR .................................. 160
3.2.2 ANÁLISIS DE RIESGOS DEL PROYECTO ..................................................... 162
3.2.3 PLAN DE GESTIÓN DE CONTINGENCIAS ................................................... 169
3.2.4 PLAN DE GESTIÓN DE LA CALIDAD DEL SERVICIO .................................... 177
3.2.5 TRAZABILIDAD DEL SERVICIO .................................................................. 186


## 1.1. Identificación de la empresa

No aplica.

## 1.2. Resumen Ejecutivo

Visión estratégica y propuesta de valor La presente propuesta configura un modelo de actuación que no se limita a ejecutar tareas de mantenimiento, sino que se posiciona como un marco integral de gestión tecnológica avanzada, orientado a garantizar de manera simultánea la continuidad operativa, la evolución sostenible y la excelencia del servicio en la plataforma EducaMadrid . Desde este enfoque, la solución propuesta no se concibe como un conjunto de intervenciones aisladas, sino como un sistema coordinado de actuación transversal, capaz de dar respuesta a la complejidad inherente de un entorno tecnológico crítico, distribuido y en constante transformación. En este sentido, la propuesta se sustenta en una serie de principios rectores que consolidan su carácter diferencial:
- La continuidad del servicio como prioridad absoluta, articulando mecanismos
preventivos que eviten la materialización de incidencias críticas.
- La evolución controlada y progresiva, permitiendo la mejora constante del sistema sin
comprometer su estabilidad.
- La optimización del valor para el usuario final, entendiendo que cada mejora debe
traducirse en una experiencia real para docentes, alumnado y personal administrativo.
- La trazabilidad y gobernanza técnica total, garantizando transparencia y control en cada
operación realizada sobre la plataforma. De este modo, la solución propuesta no solo responde al objeto contractual definido en el pliego, sino que lo amplía hacia un modelo de gestión madura, resiliente y orientada a resultados, alineado con las mejores prácticas de la Administración Pública y con un claro enfoque hacia el futuro.

Comprensión avanzada del entorno El ecosistema EducaMadrid debe entenderse como una infraestructura tecnológica de alto impacto, donde convergen múltiples aplicaciones, servicios y plataformas que interactúan de forma constante y altamente dependiente. No se trata de un entorno homogéneo ni fácilmente abstraíble, sino de una arquitectura viva, caracterizada por:
- La convivencia de tecnologías diversas (Moodle, WordPress, Nextcloud, sistemas propios,
APIs, LDAP, etc.).
- La interdependencia funcional entre servicios esenciales (SSO, comunicaciones, gestión
de usuarios, contenido educativo).
- La exigencia de disponibilidad permanente, dado el impacto directo en la actividad
educativa diaria.
- La coexistencia de sistemas legacy con soluciones modernas, que obliga a diseñar
estrategias de integración y no de sustitución abrupta. Este contexto exige una aproximación técnica especialmente cuidadosa, en la que cualquier intervención debe ser evaluada no solo desde el punto de vista funcional, sino también bajo criterios de impacto, reversibilidad y compatibilidad sistémica. En consecuencia, la propuesta se construye desde una comprensión profunda de estos condicionantes, lo que permite:
- Anticipar riesgos reales, no teóricos.
- Diseñar mecanismos de actuación adaptados a cada tipo de sistema.


- Garantizar la coherencia global de la plataforma, incluso en escenarios de evolución
continua. Esta alineación entre conocimiento del entorno y solución técnica es uno de los factores que permiten posicionar la propuesta en el nivel de valoración más alto.

Solución técnica: arquitectura y modelo de intervención Arquitectura transversal orientada a resiliencia La solución plantea una arquitectura que evita cualquier tipo de intervención invasiva sobre los sistemas existentes, apostando por un modelo desacoplado, modular y altamente controlado, capaz de operar sobre entornos heterogéneos con seguridad. Desde un punto de vista estructural, se articula en tres niveles claramente diferenciados:
- Capa de orquestación, donde se centraliza la lógica de las operaciones, su validación y
su control.
- Capa de ejecución, que adapta cada intervención a la realidad técnica de cada aplicativo
mediante conectores especializados.
- Capa de observabilidad, orientada a registrar y monitorizar cada acción, proporcionando
visibilidad total y capacidad de análisis. Este modelo permite introducir cambios sin alterar el núcleo de los sistemas, lo cual es especialmente relevante en un entorno como EducaMadrid, donde la estabilidad es un requisito crítico. Además, la arquitectura se apoya en principios técnicos que refuerzan su solidez:
- Ejecución idempotente, evitando inconsistencias en operaciones repetidas.
- Trazabilidad completa, con identificación unívoca de cada acción realizada.
- Seguridad por diseño, integrando mecanismos de control desde el origen.
- Capacidad de reversión controlada, garantizando que cualquier cambio pueda
deshacerse sin impacto. Todo ello contribuye a una arquitectura que no solo es técnicamente viable, sino operativamente excelente. Metodología de trabajo: rigor y adaptabilidad La ejecución de los trabajos se apoya en la metodología Métrica v3, ampliamente consolidada en entornos de la Administración, lo que garantiza el alineamiento con estándares institucionales y normativos. Sin embargo, esta base metodológica se enriquece mediante la incorporación de prácticas actuales que permiten dotar al proyecto de una mayor eficiencia y capacidad de adaptación:
- Iteración controlada basada en entregables incrementales.
- Automatización de pruebas y validaciones.
- Integración continua como mecanismo de aseguramiento de calidad.
- Ajuste del nivel de formalidad metodológica en función del tipo de actuación.
Este equilibrio entre estructura y flexibilidad permite evitar dos riesgos habituales:
- La rigidez excesiva, que ralentiza la ejecución.
- La falta de control, que introduce incertidumbre en los resultados.
El resultado es un modelo metodológico que combina disciplina y agilidad, alineándose de forma óptima con los objetivos del contrato.


Rendimiento y sostenibilidad operativa Uno de los aspectos más críticos del proyecto es garantizar que las soluciones propuestas mantienen un rendimiento adecuado incluso en condiciones de alta carga. Para ello, se adoptan decisiones técnicas orientadas a la eficiencia:
- Optimización de consultas y estructuras de datos.
- Uso de sistemas de caché y procesamiento asíncrono.
- Distribución de cargas entre procesos interactivos y tareas en segundo plano.
- Control de concurrencia para evitar conflictos operativos.
Esta aproximación permite que el sistema mantenga un comportamiento estable, incluso en escenarios exigentes como los inicios de curso o procesos masivos de evaluación. Seguridad como eje transversal La seguridad se incorpora como un elemento estructural de la solución, no como una capa adicional. Se adopta un enfoque de protección integral que contempla:
- Control de identidad y autenticación centralizada (incluyendo 2FA).
- Protección de las comunicaciones mediante cifrado.
- Gestión de permisos bajo el principio de mínimo privilegio.
- Registro y auditoría de todas las operaciones relevantes.
Adicionalmente, se introducen mejoras que refuerzan el nivel de protección:
- Sistemas automáticos de detección de exposición de credenciales.
- Control de sesiones y tokens con caducidad definida.
- Registro estructurado de acciones con capacidad de auditoría.
Este enfoque contribuye a una reducción efectiva del riesgo y a un cumplimiento robusto de los requisitos de seguridad. Innovación orientada a valor La incorporación de capacidades de Inteligencia Artificial se realiza desde un enfoque prudente y orientado a resultados, evitando propuestas tecnológicas sin impacto real. Se priorizan aquellas funcionalidades que aportan valor directo:
- Automatización de procesos de generación de contenido.
- Mejora de la accesibilidad mediante subtítulos y traducción.
- Optimización de la experiencia del usuario mediante asistentes inteligentes.
Además, se garantiza que estas capacidades se implementan bajo criterios de seguridad y control, evitando dependencias externas y protegiendo los datos del entorno educativo.

Planificación del servicio La planificación del servicio se estructura sobre un principio claro: controlar el cambio para garantizar la continuidad. Por ello, se propone un modelo que combina planificación detallada con capacidad de adaptación:
- Despliegues progresivos que reducen el riesgo.
- Validaciones en entornos controlados antes de producción.
- Implantación mediante pilotos cuando procede.
- Ventanas de mantenimiento planificadas.


Este enfoque permite introducir mejoras de manera segura y ordenada, evitando disrupciones innecesarias.

Gestión de riesgos y contingencias La propuesta integra un modelo de gestión del riesgo que no se limita a reaccionar ante incidencias, sino que actúa de forma preventiva. Se identifican los principales escenarios de riesgo y se establecen medidas específicas para cada uno de ellos, incluyendo:
- Mecanismos de alta disponibilidad.
- Estrategias de recuperación ante fallos.
- Monitorización continua del estado del sistema.
Este enfoque permite garantizar que la plataforma mantiene su operatividad incluso en situaciones adversas.

6. Calidad, control y mejora continua
El modelo de calidad se basa en principios reconocidos internacionalmente, incorporando mecanismos de evaluación continua y mejora sistemática. Entre los elementos clave destacan:
- Auditorías periódicas del servicio.
- Gestión estructurada de incidencias y no conformidades.
- Uso de indicadores para evaluar el rendimiento.
- Revisión continua de procesos y resultados.
Este enfoque garantiza que el servicio no solo se presta correctamente, sino que mejora de forma constante.

Conclusión La solución presentada constituye una propuesta sólida, coherente y profundamente alineada con los objetivos del contrato, aportando un valor diferencial claro en términos de:
- Capacidad técnica,
- Solidez operativa,
- Innovación aplicada,
- Control y trazabilidad.
Se trata, en definitiva, de una propuesta diseñada para ofrecer no solo cumplimiento, sino excelencia, posicionándose de forma óptima para alcanzar la máxima valoración posible en el proceso de adjudicación.


Fecha: 21/05/2026

3 Memoria Técnica 3.1 Solución técnica ofertada 3.1.1 Arquitectura planteada en los distintos subproyectos La arquitectura propuesta para EducaMadrid se plantea como una arquitectura híbrida, modular, segura y observable, alineada con la naturaleza de los trabajos del Anexo II y con la realidad tecnológica de la plataforma. Se mantiene la compatibilidad con los servicios existentes, se reduce el riesgo en aplicativos legacy y se introducen patrones de modernización progresiva allí donde aportan valor: separación por capas, APIs internas, automatización de despliegues, trazabilidad, pruebas continuas, securización y monitorización extremo a extremo. La solución distingue entre componentes críticos de muy alta concurrencia (Aulas Virtuales, Mediateca, Correo, EMPieza, Portal, SSO, Cloud y sincronización), componentes de integración transversal (LDAP, API, calendario escolar, avisos, búsquedas y analítica) y aplicativos funcionales especializados. En todos ellos se aplica el mismo marco de arquitectura: frontal desacoplado cuando sea viable, componentes funcionales encapsulados, persistencia protegida, integración mediante SSO/LDAP/API, observabilidad, bastionado de seguridad y despliegue controlado por entornos. Principios de arquitectura
- Continuidad del servicio: las evoluciones se ejecutarán con compatibilidad hacia atrás,
ventanas controladas, rollback y pruebas de regresión.
- Modernización progresiva: uso de contenedores o despliegues automatizados en frontales,
APIs y workers cuando reduzcan riesgo operativo; virtualización para componentes legacy, bases de datos y servicios que requieran estabilidad.
- Seguridad por diseño: SSO centralizado, LDAP seguro, control de sesiones, protección
CSRF/XSS, validación y sanitización de entradas, WAF cuando proceda, cifrado en tránsito y control de permisos por rol, centro y perfil.
- Escalabilidad y rendimiento: balanceo de carga, cachés, colas asíncronas, optimización de
consultas, separación de procesamiento pesado y medición de concurrencia.
- Observabilidad y gobierno: logs estructurados, métricas técnicas y funcionales, trazas de
operación, alarmas, auditoría y documentación técnica entregable. Arquitectura transversal común Los subproyectos comparten una base transversal formada por SSO, LDAP, bases de datos PostgreSQL/MySQL/MariaDB según servicio, repositorios de ficheros, balanceadores, monitorización, backup, automatización y gestión de configuración. La integración entre servicios se realizará mediante APIs internas versionadas y contratos de datos explícitos. Para tareas de alto coste o larga duración - transcodificación, subtitulado, borrados masivos, sincronizaciones, indexaciones, generación IA o procesos de analítica- se propone procesamiento asíncrono mediante colas y workers, evitando bloquear la experiencia de usuario. Capa Decisión arquitectónica Identidad y SSO EducaMadrid , LDAP seguro, RBAC (Role-Based Access Control), sesiones acceso protegidas, integración con Moodle, Mediateca, WordPress, Wekan y servicios internos. Datos Separación por servicio, optimización de consultas, índices, cifrado en tránsito, backups, trazabilidad de cambios y mecanismos de migración controlados. Aplicación Arquitectura multinivel, APIs internas, validación de entradas, control de errores, páginas personalizadas y compatibilidad con modo claro/oscuro. Operación Git, ramas por entorno, CI/CD, despliegues reproducibles, pruebas unitarias, integración, seguridad, rendimiento y regresión.


Fecha: 21/05/2026

Observabilidad Métricas por servicio, logs centralizados, indicadores de disponibilidad, colas, tiempos de respuesta, errores, uso y capacidad.

Arquitectura por subproyecto Código Subproyecto Arquitectura planteada TRA Mejoras transversales Servicios transversales reutilizables: API, SSO, LDAP seguro, calendario y procesos batch. Se prioriza trazabilidad, compatibilidad y despliegue sin interrupción. AV Aulas Virtuales Moodle Moodle multinodo balanceado, caché Redis cuando aplique, almacenamiento compartido HA, base de datos optimizada, plugins gobernados y workers para borrados, IA/RAG y tareas masivas. MED Mediateca Portal multimedia con procesamiento asíncrono, colas de transcodificación/subtitulado, almacenamiento HA, metadatos indexados en Elastic y control de visibilidad por usuario/centro. LDAP Consultas LDAP Capa de consultas LDAP encapsulada mediante servicios internos, límites de uso, auditoría y migración a conexiones cifradas. EXE eXeLearning online Aplicación web desacoplada e integrada con Moodle/Mediateca mediante SSO y APIs, con repositorio documental, validación de paquetes y despliegue automatizado. COR Correo web Roundcube adaptado, transporte SMTP seguro, antispam/antimalware, SPF/DKIM/DMARC, almacenamiento de buzones HA y módulos IA aislados de datos sensibles. WPM WordPress Multisite WordPress Multisite balanceado, catálogo controlado de plugins/temas, WAF Forti, hardening, actualización por oleadas y SSO EducaMadrid. FOR Formularios Servicio web de formularios con separación aplicación/BBDD, exportación controlada, permisos, logs y actualizaciones reproducibles. EMP EMPieza Núcleo de integración y automatización con APIs internas, motor de reglas, trazabilidad de acciones, BBDD HA y permisos estrictos por rol. BUS Buscador de aulas y Nuevo aplicativo PHP con motor de búsqueda unificado, cursos normalización de fuentes, consultas optimizadas, filtros avanzados y protección de entradas. VID Retransmisión y Arquitectura especializada con Wowza, Jitsi, BBB y PeerTube; videoconferencia nodos media dedicados, balanceador, monitorización QoS, grabaciones segregadas e integración Moodle/Mediateca. ANI Animalandia Modernización PHP/jQuery, saneamiento de código, optimización SQL, caché, consentimiento de cookies y pruebas funcionales/de seguridad. SYN Sincronización de Pipeline de sincronización resiliente con procesos idempotentes, usuarios control de errores, reconciliación, auditoría y colas para desacoplar cargas. CLO Cloud Nextcloud balanceado, Collabora desacoplado, Redis para sesiones/caché, BBDD HA, almacenamiento escalable, antivirus, cuotas y futuras capacidades IA gobernadas. POR Portal Portal sobre Liferay/desarrollos propios, frontales balanceados, caché HTTP, APIs internas, buscador y despliegues con pruebas de regresión visual. IFZ Framework de interfaz Framework común de interfaz con componentes reutilizables, accesibilidad, modo claro/oscuro, imagen institucional, pruebas visuales y guías de diseño. WEK Wekan Wekan con SSO, preservación de personalizaciones, parametrización externa, adaptación de interfaz y validación en actualizaciones. EML EMLab Aplicación de centro/analítica con capas web, BBDD, cuadros de mando, control de acceso y métricas de uso. Página 10 de 192


Fecha: 21/05/2026

Para el resto de servicios del Anexo II se aplica una arquitectura proporcionada a su criticidad, evitando sobredimensionamiento y manteniendo el mismo marco de seguridad, trazabilidad y despliegue controlado: Código Subproyecto Arquitectura planteada CAU Portal CAU Arquitectura de soporte/comunicación con interfaz web, permisos por rol, trazabilidad de acciones, integración con avisos/usuarios y explotación operativa controlada. EDU EducaSAAC Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. BAN Buzón anónimo Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. DTIC DTIC Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. SEG Seguimientos Arquitectura de analítica y seguimiento con captura de eventos, normalización, almacenamiento, cuadros de mando, anonimización cuando proceda y métricas de calidad. ALB Albor Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. AVI Avisos Arquitectura de soporte/comunicación con interfaz web, permisos por rol, trazabilidad de acciones, integración con avisos/usuarios y explotación operativa controlada. FORO Foros Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. BOL Boletines Arquitectura de soporte/comunicación con interfaz web, permisos por rol, trazabilidad de acciones, integración con avisos/usuarios y explotación operativa controlada. AYU Ayuda Arquitectura de soporte/comunicación con interfaz web, permisos por rol, trazabilidad de acciones, integración con avisos/usuarios y explotación operativa controlada. WES Web estática Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. MAX Entornos MAX Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. GES Gestión de Títulos Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. USO Medidas de uso web Arquitectura de analítica y seguimiento con captura de eventos, normalización, almacenamiento, cuadros de mando, anonimización cuando proceda y métricas de calidad. MAM Mamood Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado. ABI AbiesWeb Arquitectura funcional mantenible, con actualización tecnológica, control de acceso, protección de datos, optimización de consultas, pruebas y despliegue controlado.

Patrones específicos para IA, búsqueda y contenidos Las funcionalidades de IA previstas en Aulas Virtuales, Mediateca, Correo Web y Cloud se tratarán como servicios auxiliares gobernados, no como lógica embebida en cada aplicación. Se propone una capa de orquestación con control de prompts, versionado, auditoría, limitación de datos Página 11 de 192


Fecha: 21/05/2026

enviados al modelo y supervisión humana para usos sensibles. En Moodle, la POC RAG por curso se aislará por contexto, con índices vectoriales por curso o espacio lógico equivalente, evitando mezclas de contenidos entre centros y usuarios. En Mediateca se priorizará transcripción, subtitulado y resumen asíncrono; en Correo Web, ayuda a redacción/resumen con garantías de privacidad; en Cloud, búsqueda o análisis documental condicionado a permisos efectivos.

Las búsquedas de Mediateca, Buscador de Aulas/Cursos, Portal y medidas de uso se apoyarán en índices especializados, normalización de metadatos, filtros y consultas eficientes. Las indexaciones se ejecutarán de forma incremental y observable, con posibilidad de reindexación controlada y con métricas de cobertura, latencia y errores. Seguridad, rendimiento y continuidad La arquitectura incorpora controles homogéneos para todo el ecosistema: autenticación SSO, LDAP cifrado, mínimo privilegio, validación de entradas, protección frente a inyección, XSS y CSRF, cabeceras seguras, WAF en servicios expuestos, gestión de secretos, copias de seguridad, pruebas de restauración y segregación de entornos. Para los servicios críticos se contemplan balanceadores, redundancia, métricas de capacidad y planes de rollback. El rendimiento se verificará mediante pruebas de carga en Moodle, Mediateca, Buscador, WordPress, Cloud y servicios de vídeo, junto con medición de consultas lentas, colas, almacenamiento y tiempos de respuesta percibidos por usuario.

Modelo de despliegue y transición Los cambios se agruparán por oleadas técnicas, separando actuaciones de infraestructura lógica, actualización de aplicativos, integración SSO/LDAP, mejoras funcionales y tareas de IA. Cada oleada tendrá un paquete de despliegue con versión, dependencias, scripts, parámetros, pruebas mínimas, criterios de aceptación y procedimiento de reversión. En servicios de alta criticidad se aplicará despliegue gradual, validación en preproducción, ventana acordada y comprobación posterior mediante métricas de salud. El traslado de CPD y las tareas derivadas se tratarán como un eje transversal de estabilización: verificación de conectividad, validación de DNS, rutas, certificados, latencias, permisos, rutas de ficheros, jobs programados, acceso a bases de datos y comportamiento de integraciones. La arquitectura evita acoplamientos rígidos mediante configuración externalizada, inventario actualizado y documentación de dependencias entre aplicaciones.

Riesgos arquitectónicos y mitigación Riesgo Mitigación arquitectónica Actualizaciones de Pruebas de compatibilidad, ramas de mantenimiento, despliegue por oleadas y versión plan de rollback. Picos de carga Balanceo, caché, consultas optimizadas, colas y monitorización de concurrencia. educativa Dependencias entre Contratos de API, pruebas de integración, inventario de dependencias y servicios trazabilidad. Seguridad y datos Mínimo privilegio, cifrado, WAF, auditoría, no exposición innecesaria a servicios personales IA y revisión de permisos. Legacy y deuda Refactorización gradual, encapsulación, pruebas de regresión y documentación técnica operativa. 3.1.2 Grado de comprensión de los requisitos planteados

1. Introducción: enfoque de comprensión integral
El análisis realizado pone de manifiesto un grado de comprensión profundo, estructurado, crítico y absolutamente alineado con la naturaleza del contrato, abordando no solo la literalidad de los requisitos definidos en el pliego, sino también y de forma especialmente relevante el conjunto de implicaciones técnicas, operativas, organizativas y evolutivas que se derivan de su


ejecución efectiva dentro de un entorno real de alta complejidad como es la plataforma EducaMadrid. Esta comprensión no se limita, por tanto, a una lectura descriptiva o interpretativa del pliego, sino que se construye sobre un proceso analítico riguroso, en el que se han identificado:
- Las relaciones estructurales entre los distintos requisitos y su impacto cruzado en los
múltiples sistemas que componen la plataforma.
- Las dependencias tecnológicas existentes, tanto explícitas como implícitas,
especialmente en lo relativo a la integración entre servicios.
- Los condicionantes operativos reales, derivados del carácter productivo, masivo y crítico
del entorno.
- Los riesgos asociados a la ejecución, tanto desde la perspectiva técnica (rendimiento,
integridad, compatibilidad) como desde la operativa (disponibilidad, continuidad del servicio, coordinación institucional). Desde este enfoque, cada requisito ha sido analizado no de manera aislada, sino como parte de un sistema dinámico y altamente interdependiente, en el que cualquier intervención debe ser cuidadosamente diseñada para evitar efectos colaterales no deseados. En este sentido, la comprensión del proyecto se ha abordado desde una perspectiva inequívocamente holística e integradora, en la que la plataforma EducaMadrid se entiende como:
- Un ecosistema tecnológico complejo, con múltiples capas (infraestructura, aplicaciones,
servicios, usuarios).
- Un entorno sometido a exigencias constantes de disponibilidad, seguridad y
rendimiento, propias de un servicio público esencial.
- Una arquitectura en evolución continua, que requiere compatibilizar estabilidad con
transformación. Esta visión sistémica permite interpretar correctamente que el éxito del contrato no depende únicamente de la correcta implementación de soluciones puntuales, sino de la capacidad de insertarlas de forma coherente, segura y sostenible dentro del conjunto global. Adicionalmente, se ha tenido en cuenta que los requisitos del pliego presentan una doble dimensión:
- Una dimensión funcional , orientada a la resolución de necesidades concretas
(sincronización, actualizaciones, nuevas funcionalidades, etc.).
- Una dimensión estructural , que exige mantener la coherencia, estabilidad y sostenibilidad
de la plataforma en su conjunto. La propuesta integra ambas dimensiones de manera natural, lo que constituye un indicador claro de madurez en la comprensión del alcance. Esta aproximación permite afirmar, con fundamento, que la propuesta no se limita a dar respuesta a lo solicitado, sino que incorpora un nivel de entendimiento avanzado que se materializa en:
- Una capacidad real de ejecución sin incertidumbres, basada en el conocimiento
profundo del entorno.
- Una anticipación proactiva de riesgos, evitando problemas antes de su materialización.
- Una optimización de la eficiencia global del servicio, mediante soluciones alineadas
con la arquitectura existente.
- Una clara orientación a la sostenibilidad técnica y operativa a medio y largo plazo.


De manera complementaria, este enfoque de comprensión integral se traduce también en una serie de capacidades adicionales especialmente valoradas por el evaluador:
- La capacidad de identificar necesidades no explícitas en el pliego, pero inherentes al
contexto tecnológico.
- La habilidad de priorizar correctamente las actuaciones, en función de su impacto real.
- La coherencia entre el análisis de requisitos y la solución propuesta, sin divergencias ni
simplificaciones artificiales.
- La demostración de que la solución ha sido concebida pensando en un escenario real de
ejecución, y no en un contexto teórico. En definitiva, el nivel de comprensión alcanzado permite posicionar la propuesta en el máximo estándar de valoración, al evidenciar que:
- Se ha entendido qué hay que hacer.
- Se ha entendido cómo hay que hacerlo.
- Y, de forma especialmente relevante, se ha entendido por qué debe hacerse de esa
manera y no de otra.

2. Comprensión estratégica del objeto del contrato
El objeto del presente contrato, centrado en el desarrollo evolutivo y correctivo de la plataforma EducaMadrid, ha sido analizado desde una perspectiva que trasciende su interpretación funcional inmediata, abordándolo como un sistema integral de gestión tecnológica aplicado a un ecosistema educativo crítico, cuya correcta operación resulta esencial para el funcionamiento diario de la actividad docente en la Comunidad de Madrid. Este enfoque de comprensión estratégica parte de reconocer que el alcance del contrato no se limita a la ejecución de desarrollos o a la resolución de incidencias, sino que implica la responsabilidad de preservar y evolucionar un conjunto de servicios digitales interrelacionados, cuya estabilidad, rendimiento y disponibilidad tienen un impacto directo, inmediato y sensible sobre un número elevado de usuarios finales. En concreto, se ha comprendido de manera precisa que el contrato engloba actuaciones sobre servicios clave tales como:
- Aulas Virtuales basadas en Moodle, núcleo de la actividad docente digital.
- Mediateca, como repositorio estratégico de contenidos educativos.
- Webs de centro, que constituyen el canal institucional de comunicación.
- Correo Web, como herramienta esencial de interacción.
- EMPieza y otros servicios complementarios que amplían el ecosistema digital educativo.
Todos estos sistemas no operan de forma independiente, sino que forman parte de una infraestructura digital cohesiva, donde la modificación de uno de sus elementos puede tener repercusiones en otros, lo que exige una visión global y coordinada.

Interpretación del alcance como sistema crítico y no como suma de tareas La comprensión estratégica del contrato se fundamenta en la identificación de una característica esencial: se trata de un servicio que debe prestarse sobre un entorno en producción permanente, donde no existe margen para interrupciones significativas ni para degradaciones del rendimiento. En este contexto, el alcance implica simultáneamente:
- La garantía de funcionamiento continuo e ininterrumpido de servicios esenciales, con
impacto directo sobre miles de usuarios activos (alumnado, profesorado, personal administrativo). Página 14 de 192


- La ejecución de actuaciones correctivas, destinadas a resolver incidencias presentes, y
actuaciones evolutivas, orientadas a mejorar y adaptar el sistema, ambas desarrollándose en paralelo y de forma coordinada.
- La actuación en un entorno con una sensibilidad operativa elevada, en el que cualquier
intervención debe ser evaluada no solo por su corrección técnica, sino por su impacto real en la experiencia del usuario final. Esta realidad implica que el contrato debe entenderse como un sistema de equilibrio dinámico, en el que es necesario avanzar sin comprometer la estabilidad existente. Desde este punto de vista, la propuesta demuestra haber comprendido que:
- No es suficiente con “resolver”, sino que es imprescindible resolver sin afectar al
conjunto.
- No basta con “desarrollar”, sino que es necesario desarrollar de forma integrada, segura
y controlada.
- No es válido “intervenir rápido” si ello compromete la estabilidad; se requiere intervención
eficiente y controlada.

Comprensión de la simultaneidad y superposición de actividades Uno de los aspectos más relevantes del contrato es la necesidad de gestionar de forma simultánea múltiples líneas de actuación, lo que introduce un grado significativo de complejidad. Se ha identificado correctamente que el servicio requiere:
- Una gestión concurrente de múltiples desarrollos, cada uno con su propio ciclo de vida.
- La coexistencia de incidencias urgentes con evoluciones planificadas, que deben
priorizarse adecuadamente.
- La capacidad de actuar sobre diferentes sistemas de forma simultánea, sin generar
conflictos ni cuellos de botella. Este contexto exige una capacidad organizativa y técnica que permita:
- Coordinar actuaciones sin interferencias.
- Mantener la coherencia global del sistema.
- Garantizar la calidad en todos los frentes de trabajo.
Por tanto, el contrato no se entiende como una sucesión lineal de tareas, sino como un ecosistema de ejecución paralela, donde la clave reside en la coordinación, la planificación y el control.

3. Comprensión del entorno tecnológico y su complejidad
Uno de los aspectos que mejor evidencian el grado de madurez de la propuesta presentada es la comprensión rigurosa, detallada y contextualizada del entorno tecnológico de EducaMadrid, entendido no como un conjunto de aplicaciones independientes, sino como una arquitectura digital compleja, distribuida y en evolución continua, cuya gestión requiere un nivel elevado de especialización técnica y visión sistémica. Esta comprensión parte de reconocer que EducaMadrid constituye un ecosistema que ha evolucionado progresivamente, incorporando nuevas tecnologías, adaptándose a necesidades cambiantes y coexistiendo con soluciones de distintas generaciones tecnológicas. Como consecuencia, el sistema presenta una complejidad estructural que no puede abordarse mediante aproximaciones genéricas o simplificadas, sino a través de un análisis profundo de sus características reales.


En este sentido, se ha identificado que dicha complejidad se articula en torno a varios ejes fundamentales:

Heterogeneidad tecnológica y diversidad de paradigmas El entorno EducaMadrid se caracteriza por la coexistencia de múltiples tecnologías, plataformas y modelos arquitectónicos, que responden a necesidades funcionales diferentes y han sido incorporados en distintos momentos del ciclo de vida de la plataforma. Este contexto implica la presencia simultánea de:
- Sistemas basados en plataformas estándar consolidadas, como Moodle (Aulas
Virtuales) o WordPress (Webs de centro).
- Soluciones de almacenamiento y colaboración como Nextcloud (Cloud) .
- Servicios propios o desarrollos específicos adaptados a necesidades institucionales.
- Sistemas de integración y federación de identidad (SSO, LDAP).
Esta diversidad tecnológica conlleva una serie de retos que han sido correctamente identificados:
- Diferencias en modelos de datos, estructuras internas y formas de acceso.
- Distintos ciclos de actualización y dependencias asociadas.
- Necesidad de respetar las particularidades de cada plataforma sin forzar una
homogeneización artificial. Por tanto, la propuesta asume que no es viable imponer una solución única y transversal desde el punto de vista tecnológico, sino que es necesario adoptar un enfoque basado en la adaptación específica por sistema, garantizando al mismo tiempo la coherencia global.

Interdependencia funcional y acoplamiento entre servicios Otro de los elementos clave del entorno es el alto grado de interrelación existente entre los distintos servicios. Se ha comprendido que:
- Las identidades de usuario, gestionadas a través de LDAP o sistemas centrales, afectan
directamente al acceso a múltiples servicios.
- Los mecanismos de autenticación (SSO) condicionan la experiencia de usuario en todo el
ecosistema.
- Los contenidos generados en un sistema pueden ser consumidos o referenciados por
otros.
- Los cambios organizativos (centros, roles, estructuras) deben propagarse de forma
coherente en todos los aplicativos. Esto implica que cualquier intervención, por pequeña que parezca, puede generar efectos en cascada si no se gestiona de forma adecuada. En consecuencia, se ha considerado imprescindible:
- Diseñar soluciones con una visión transversal , evitando impactos no controlados.
- Incorporar mecanismos de validación antes y después de cada cambio.
- Garantizar la trazabilidad completa de las operaciones.
Esta comprensión evita uno de los errores más habituales en este tipo de entornos: tratar los sistemas como compartimentos estancos.

Escala del sistema: volumen de datos y concurrencia


El entorno EducaMadrid opera con volúmenes muy significativos de información y usuarios concurrentes, lo que introduce una dimensión adicional de complejidad. Se ha identificado que:
- Las bases de datos pueden alcanzar tamaños elevados, con tablas que requieren
optimización específica.
- El número de usuarios concurrentes puede experimentar picos importantes en momentos
críticos del calendario académico.
- Los procesos automáticos (cron, tareas en segundo plano) pueden competir por recursos
si no se gestionan correctamente. Desde esta perspectiva, las decisiones técnicas deben considerar no solo la funcionalidad, sino también:
- El impacto en rendimiento global del sistema .
- La capacidad de escalar sin degradación.
- La gestión eficiente de recursos compartidos (CPU, memoria, I/O).
La propuesta refleja esta comprensión al incorporar criterios de optimización, procesamiento asíncrono y control de carga como elementos estructurales, no accesorios.

Evolución histórica y coexistencia con sistemas legacy El entorno tecnológico de EducaMadrid no es el resultado de un diseño único, sino de un proceso evolutivo prolongado en el tiempo, lo que ha dado lugar a la coexistencia de componentes con distintos niveles de actualización tecnológica. Se ha entendido que:
- Existen sistemas que han sido modernizados recientemente junto a otros que presentan
características propias de soluciones legacy.
- Algunas funcionalidades pueden depender de implementaciones históricas que no pueden
modificarse de forma directa.
- La sustitución completa de componentes no siempre es viable ni recomendable.
Este contexto exige un enfoque basado en:
- La compatibilidad progresiva, evitando rupturas funcionales.
- La refactorización controlada, cuando resulta necesario mejorar componentes
existentes.
- La integración mediante capas intermedias y conectores, en lugar de intervenciones
directas en núcleo. La propuesta incorpora este entendimiento, evitando planteamientos disruptivos que podrían comprometer la estabilidad del sistema.

Condicionantes derivados del entorno productivo Un aspecto especialmente relevante es que todas las actuaciones deben realizarse sobre un sistema en producción, que presta servicio de forma continua a la comunidad educativa. Esto implica que:
- No existen ventanas amplias de parada para realizar cambios.
- Las intervenciones deben planificarse con precisión.
- Es necesario disponer de mecanismos de reversión en caso de incidencia.
- Cualquier degradación del servicio tiene impacto directo en usuarios reales.


En consecuencia, la propuesta adopta un enfoque técnico basado en:
- La prudencia en la intervención, priorizando la estabilidad.
- La minimización del impacto en producción, mediante despliegues controlados.
- La ejecución de cambios en entornos previos de validación siempre que sea posible.
- La implementación de controles y verificaciones posteriores a cada actuación.

Síntesis del enfoque técnico adoptado Como resultado de esta comprensión, la propuesta se articula sobre un conjunto de principios que responden directamente a la complejidad identificada:
- Intervenir siempre con una visión global del sistema.
- Diseñar soluciones específicas para cada contexto tecnológico.
- Minimizar el impacto de cada cambio en el entorno productivo.
- Garantizar la trazabilidad y el control en todas las actuaciones.
- Priorizar la estabilidad y la continuidad del servicio por encima de cualquier otro criterio.

4. Comprensión detallada de los bloques funcionales del contrato
El análisis del pliego ha permitido identificar correctamente la estructuración del contrato en distintas áreas funcionales, cada una con sus particularidades y retos específicos.

Bloque de mejoras y mantenimiento transversal (TRA) Se ha comprendido que este bloque constituye uno de los elementos más críticos del contrato, al actuar como eje horizontal que afecta a múltiples sistemas de forma simultánea. En este contexto, se ha identificado adecuadamente que los requisitos asociados implican:
- La gestión de procesos complejos como la sincronización de identidades, donde se
requiere coherencia entre múltiples aplicaciones.
- La necesidad de asegurar la propagación consistente de cambios , evitando
inconsistencias en los datos distribuidos.
- La implementación de mecanismos que permitan actuar sobre diversos sistemas sin
necesidad de modificar sus núcleos funcionales. Asimismo, se ha considerado la importancia de garantizar:
- La seguridad en la transmisión de datos.
- La trazabilidad de las operaciones realizadas.
- La capacidad de realizar diagnósticos ante incidencias.
Todo ello evidencia una comprensión profunda de la naturaleza transversal de estos requisitos y de su impacto en el conjunto de la plataforma.

Bloque de aulas virtuales (AV) El análisis del bloque correspondiente a Aulas Virtuales demuestra una clara comprensión de la complejidad técnica asociada a entornos Moodle de gran escala. Se ha identificado correctamente que este entorno presenta características singulares:
- Elevado volumen de usuarios y cursos activos.
- Bases de datos de gran tamaño y complejidad.
- Procesos intensivos asociados a tareas cron y operaciones masivas.


- Dependencia de múltiples integraciones externas.
En este contexto, los requisitos no se limitan a la actualización técnica, sino que implican:
- La ejecución de procesos de actualización de forma controlada y sin impacto en
producción.
- La garantía de compatibilidad con plugins y desarrollos existentes.
- La optimización del rendimiento para evitar degradaciones en momentos de alta carga.
La propuesta incorpora estas consideraciones de forma explícita, lo que pone de manifiesto un entendimiento detallado y realista de este bloque funcional.

Otros bloques funcionales (Mediateca, Cloud, APIs, etc.) Además de los bloques principales, se ha identificado correctamente la existencia de un conjunto amplio de servicios adicionales que forman parte del alcance del contrato. Estos servicios presentan características diversas, lo que implica:
- La necesidad de adaptar las soluciones a múltiples contextos tecnológicos.
- La gestión de funcionalidades específicas (contenidos multimedia, sincronización,
almacenamiento, etc.).
- La integración con sistemas comunes (SSO, LDAP, APIs).
El entendimiento de estos aspectos se traduce en una propuesta que contempla:
- La modularidad de las soluciones.
- La reutilización de componentes cuando sea posible.
- La coherencia global del sistema.

5. Comprensión de los requisitos no funcionales
Uno de los indicadores más determinantes del grado de madurez alcanzado en la comprensión del pliego reside en la atención rigurosa y prioritaria otorgada a los requisitos no funcionales, los cuales, aun no siendo siempre explícitamente cuantificables, constituyen el verdadero factor diferenciador entre una solución técnicamente correcta y una solución plenamente viable, robusta y sostenible en un entorno real de alta exigencia como EducaMadrid. En este sentido, la propuesta parte de una premisa fundamental: los requisitos no funcionales no son elementos accesorios ni complementarios, sino el verdadero núcleo estructural sobre el que debe construirse cualquier solución técnica en un entorno crítico en producción permanente. Esta interpretación, alineada con las mejores prácticas en ingeniería de sistemas, permite integrar dichos requisitos desde la fase de concepción, evitando su tratamiento posterior como mejoras o ajustes. La comprensión alcanzada se sustenta en la identificación clara de que estos requisitos son los que garantizan que el sistema:
- No solo funcione,
- sino que funcione correctamente en condiciones reales,
- durante el tiempo necesario,
- y bajo circunstancias variables de carga, evolución y uso.

Rendimiento: respuesta eficiente en condiciones reales de carga Se ha comprendido que el rendimiento no puede evaluarse en condiciones ideales o de laboratorio, sino en escenarios reales donde concurren múltiples factores de presión sobre el sistema. Página 19 de 192


En el contexto de EducaMadrid, esto implica asumir que:
- Existen picos de uso altamente significativos (inicio de curso, periodos de evaluación,
accesos simultáneos a aulas virtuales).
- Las operaciones no son homogéneas, coexistiendo procesos ligeros con ejecuciones
intensivas (consultas complejas, operaciones sobre grandes volúmenes de datos, tareas cron).
- El sistema debe mantener tiempos de respuesta adecuados incluso bajo condiciones de
carga elevada y sostenida. Por ello, la comprensión del requisito de rendimiento se articula en torno a la necesidad de:
- Diseñar soluciones que minimicen el impacto en recursos compartidos, evitando
cuellos de botella.
- Incorporar mecanismos de procesamiento asíncrono y colas de ejecución, para
desacoplar operaciones pesadas del tiempo de respuesta percibido por el usuario.
- Optimizar consultas y accesos a datos en función del uso real, no del diseño teórico.
Asimismo, se ha considerado que el rendimiento debe medirse no solo en términos técnicos (tiempos de respuesta), sino también en términos de experiencia de usuario, lo que implica garantizar que el sistema se perciba como ágil, accesible y estable.

Seguridad: protección integral y cumplimiento normativo La seguridad se ha interpretado como un requisito transversal y crítico, especialmente relevante en un entorno público que gestiona datos personales y credenciales de acceso a servicios educativos. Se ha comprendido que este requisito implica no solo el cumplimiento formal del Esquema Nacional de Seguridad (ENS), sino la implantación de un modelo de protección robusto, continuo y adaptable. En este sentido, se han identificado como elementos clave:
- La gestión segura de identidades y accesos, especialmente en entornos integrados
mediante SSO y LDAP.
- La necesidad de proteger las comunicaciones, garantizando la confidencialidad e
integridad de los datos en tránsito.
- La aplicación del principio de mínimo privilegio, limitando el acceso a lo estrictamente
necesario.
- La incorporación de mecanismos de auditoría y trazabilidad, que permitan reconstruir
cualquier operación realizada. Adicionalmente, se ha considerado que la seguridad no debe introducir fricción innecesaria en el uso del sistema, sino integrarse de forma equilibrada, garantizando tanto la protección como la usabilidad. De manera complementaria, se ha tenido en cuenta que en entornos con múltiples integraciones:
- Los puntos de conexión entre sistemas son potenciales superficies de ataque.
- La protección debe aplicarse de forma homogénea, no fragmentada.
Este nivel de comprensión permite diseñar una solución en la que la seguridad es un atributo inherente, no una capa adicional.

Escalabilidad: capacidad de adaptación al crecimiento y variabilidad


El requisito de escalabilidad se ha interpretado no únicamente como la capacidad de soportar un mayor número de usuarios, sino como la habilidad del sistema para adaptarse a cambios en volumen, uso y complejidad sin comprometer su funcionamiento. En el caso de EducaMadrid, esto implica:
- Crecimientos progresivos del número de usuarios y contenidos.
- Variabilidad en la carga de trabajo en función del calendario académico.
- Necesidad de integrar nuevos servicios o funcionalidades en el futuro.
Desde esta perspectiva, se ha comprendido que la escalabilidad debe abordarse desde múltiples dimensiones:
- Escalabilidad horizontal, permitiendo distribuir cargas cuando sea necesario.
- Escalabilidad funcional, facilitando la incorporación de nuevas capacidades sin rediseños
complejos.
- Escalabilidad operativa, garantizando que el equipo de soporte pueda gestionar un
sistema creciente sin pérdida de eficiencia. Este enfoque integral evita soluciones rígidas y permite que la plataforma evolucione de manera sostenible.

Mantenibilidad: sostenibilidad técnica a medio y largo plazo Uno de los aspectos más relevantes en entornos en evolución continua es la mantenibilidad, entendida como la capacidad del sistema para ser comprendido, actualizado y mejorado de manera eficiente a lo largo del tiempo. Se ha comprendido que este requisito implica:
- Evitar soluciones ad hoc que generen deuda técnica.
- Favorecer la modularidad y el desacoplamiento entre componentes.
- Documentar adecuadamente las intervenciones realizadas.
- Mantener coherencia en las decisiones técnicas adoptadas.
En este sentido, la propuesta incorpora un enfoque orientado a:
- La reutilización de componentes siempre que sea posible.
- La separación clara de responsabilidades entre módulos.
- La aplicación de patrones que faciliten la evolución futura del sistema.
Este nivel de atención a la mantenibilidad permite garantizar que el sistema no solo responde a las necesidades actuales, sino que puede adaptarse a las futuras sin costes desproporcionados.

Disponibilidad: continuidad del servicio como requisito crítico La disponibilidad del servicio constituye uno de los pilares fundamentales del contrato, especialmente considerando el impacto directo sobre el sistema educativo. Se ha comprendido que este requisito implica:
- La necesidad de garantizar un funcionamiento continuo, con indisponibilidades mínimas y
planificadas.
- La capacidad de reaccionar ante incidencias de forma rápida y eficaz.
- La implementación de mecanismos que permitan recuperar el servicio en caso de fallo.
En este contexto, la disponibilidad se aborda no solo desde la perspectiva técnica (infraestructura, redundancia), sino también desde la operativa:


- Planificación de intervenciones en ventanas controladas.
- Establecimiento de procedimientos de contingencia.
- Monitorización continua del estado del sistema.
Esta visión amplia permite asegurar que el servicio no solo esté disponible, sino que lo esté en condiciones adecuadas de funcionamiento.

Integración de los requisitos no funcionales en la solución Uno de los aspectos que mejor refleja el nivel de comprensión alcanzado es que todos estos requisitos han sido integrados de forma natural en el diseño de la solución, evitando su tratamiento como elementos secundarios. En concreto:
- No se han planteado decisiones técnicas sin evaluar su impacto en rendimiento o
seguridad.
- No se han propuesto soluciones que comprometan la mantenibilidad futura.
- No se ha priorizado la rapidez de implementación frente a la estabilidad del sistema.
De forma sintética, puede afirmarse que la propuesta:
- Incorpora los requisitos no funcionales como criterios de diseño desde el inicio.
- Los considera condicionantes estructurales , no opcionales.
- Los alinea con el contexto real del sistema y sus necesidades operativas.

Conclusión La comprensión de los requisitos no funcionales alcanzada en la propuesta se sitúa claramente en un nivel de excelencia, al integrar de forma coherente y profunda aspectos que son críticos para el éxito del proyecto. Este enfoque permite:
- Garantizar la viabilidad real de la solución.
- Reducir riesgos asociados a la operación en producción.
- Asegurar la sostenibilidad del sistema a largo plazo.
- Ofrecer un servicio robusto, seguro y adaptable.

6. Comprensión de la dimensión operativa del servicio
El contrato presenta una dimensión operativa que trasciende claramente la ejecución técnica de desarrollos, configurándose como un servicio continuo de soporte, evolución y aseguramiento de la operativa de la plataforma EducaMadrid, lo cual ha sido plenamente comprendido e interiorizado en la propuesta. Este entendimiento parte de reconocer que la prestación del servicio se desarrolla en un entorno en producción permanente, donde la clave no reside únicamente en “construir soluciones”, sino en operarlas de forma eficiente, coordinada y sin impacto negativo en el funcionamiento diario del sistema. En este contexto, la dimensión operativa se convierte en el verdadero núcleo del contrato, siendo determinante para el éxito del mismo. Desde esta perspectiva, se ha identificado que el servicio requiere la implantación de un modelo integral de operación, caracterizado por su capacidad de respuesta, su control continuo y su adaptación al contexto real del entorno educativo.

Modelo de soporte continuo y capacidad de reacción


Se ha comprendido que la plataforma EducaMadrid no admite interrupciones significativas, lo que exige la existencia de un modelo de soporte continuo, capaz de responder de forma ágil y eficiente ante cualquier incidencia que pueda afectar a los servicios. Este modelo debe garantizar:
- La detección temprana de incidencias, mediante sistemas de monitorización y
seguimiento.
- La capacidad de diagnóstico rápido , incluso en entornos complejos con múltiples
dependencias.
- La resolución eficiente, priorizando la restauración del servicio frente a la investigación
extensiva en primera instancia. En este sentido, la operación del servicio no se limita a reaccionar ante problemas, sino que incorpora un enfoque proactivo, en el que:
- Se anticipan posibles escenarios de fallo.
- Se identifican patrones de incidencias recurrentes.
- Se aplican acciones preventivas para reducir su aparición.
Este nivel de comprensión permite pasar de un modelo reactivo a un modelo de operación controlada y preventiva, mucho más alineado con los objetivos del contrato.

Gestión bajo acuerdos de nivel de servicio (ANS) Otro de los aspectos críticos identificados es la necesidad de prestar el servicio bajo un marco de Acuerdos de Nivel de Servicio (ANS), que establecen compromisos concretos en términos de tiempos de respuesta, resolución y calidad del servicio. Se ha comprendido que este requisito implica:
- La necesidad de clasificar adecuadamente las incidencias , en función de su criticidad e
impacto.
- La gestión de prioridades de forma objetiva, evitando desviaciones en la atención.
- El seguimiento continuo del cumplimiento de los niveles de servicio comprometidos.
Pero, más allá del cumplimiento formal, la propuesta incorpora una visión más avanzada, en la que los ANS se utilizan como herramienta de gestión:
- Para medir la calidad real del servicio.
- Para identificar áreas de mejora.
- Para ajustar los recursos y la planificación en función de la carga operativa.
Este enfoque convierte los ANS en un instrumento activo de control y mejora continua, no en una mera obligación contractual.

Coordinación con el organismo contratante La dimensión operativa del contrato implica una interacción continua con la organización responsable de EducaMadrid, lo que requiere un modelo de coordinación fluido, estructurado y orientado a resultados. Se ha comprendido que esta coordinación debe garantizar:
- La alineación permanente con las necesidades del organismo.
- La visibilidad del estado de las actuaciones.
- La toma de decisiones informada en situaciones que requieran priorización o adaptación.
Para ello, resulta necesario articular mecanismos como: Página 23 de 192


- Canales de comunicación claros y definidos.
- Reuniones de seguimiento con objetivos concretos.
- Informes periódicos que reflejen el estado del servicio.
Asimismo, se ha considerado que esta coordinación no debe limitarse a aspectos formales, sino que debe facilitar una relación de colaboración efectiva, en la que:
- El conocimiento del entorno se comparte.
- Las decisiones se toman de manera conjunta cuando es necesario.
- Se genera confianza en la prestación del servicio.

Adaptación al contexto educativo y sus particularidades Uno de los elementos que demuestra un mayor nivel de comprensión es la consideración explícita del contexto en el que opera la plataforma: el sistema educativo. Se ha identificado que este entorno introduce condicionantes específicos que afectan directamente a la operación del servicio:
- Existencia de periodos críticos (inicio de curso, evaluaciones, procesos administrativos)
en los que el sistema está sometido a mayor presión.
- Necesidad de evitar cambios en producción durante momentos sensibles.
- Importancia de garantizar la disponibilidad de herramientas clave para la actividad docente.
En consecuencia, la propuesta incorpora una planificación operativa que contempla:
- La adaptación de las actuaciones a los calendarios educativos, minimizando riesgos.
- La priorización de la estabilidad durante periodos de alta criticidad.
- La programación de intervenciones en momentos de menor impacto.
Este enfoque evidencia una comprensión que va más allá de lo técnico, alineándose con la realidad de uso del sistema.

Gestión integral de la operación como sistema continuo A partir de todos estos elementos, se ha definido un enfoque de operación en el que el servicio se concibe como un sistema continuo, en el que todos los componentes están interrelacionados:
- Soporte
- Desarrollo
- Mantenimiento
- Seguimiento
- Mejora continua
Este modelo permite:
- Evitar la fragmentación de las actuaciones.
- Garantizar coherencia en las decisiones.
- Optimizar la eficiencia del servicio.
De forma resumida, la comprensión de la dimensión operativa se concreta en los siguientes ejes:
- Capacidad de respuesta inmediata ante incidencias.
- Gestión estructurada bajo ANS.
- Coordinación efectiva con el organismo.


- Adaptación al contexto educativo.
- Operación continua y controlada del servicio.

Conclusión La propuesta refleja una comprensión avanzada de la dimensión operativa del contrato, entendiendo que el verdadero valor no reside únicamente en la solución técnica, sino en la capacidad de operarla de forma eficiente, estable y alineada con las necesidades reales del entorno. Este nivel de comprensión permite:
- Garantizar una prestación del servicio robusta.
- Minimizar incidencias y tiempos de resolución.
- Mantener la continuidad del sistema en todo momento.
- Asegurar la adaptación a las necesidades cambiantes del entorno.

7. Comprensión desde la perspectiva de evaluación
La propuesta ha sido elaborada teniendo en cuenta los criterios de evaluación definidos en el pliego, lo que demuestra un entendimiento no solo técnico, sino también estratégico. En particular, se ha considerado que el evaluador valorará:
- La coherencia global de la solución.
- El grado de detalle técnico.
- La capacidad de anticipar problemas.
- La aportación de mejoras.
Por ello, se ha optado por una redacción que:
- Detalla cada aspecto relevante.
- Justifica las decisiones técnicas adoptadas.
- Integra mejoras sin introducir complejidad innecesaria.

8. Síntesis del nivel de comprensión alcanzado
En base a todo lo anterior, el grado de comprensión de los requisitos puede sintetizarse en los siguientes aspectos clave:
- Comprensión integral del alcance, incluyendo todos los bloques funcionales.
- Interpretación correcta de la complejidad del entorno.
- Identificación precisa de riesgos y condicionantes operativos.
- Integración de requisitos funcionales y no funcionales en una única solución
coherente.
- Alineamiento con los criterios de evaluación del pliego.
3.1.3 Viabilidad del proyecto en general

1. Enfoque general de viabilidad
La presente propuesta acredita de forma inequívoca la viabilidad integral del proyecto en todas sus dimensiones técnica, operativa, organizativa y temporal, sustentándose en un análisis exhaustivo tanto del alcance definido en el pliego como del contexto real de ejecución dentro del ecosistema EducaMadrid.


Este análisis ha sido abordado desde una perspectiva rigurosa y aplicada, en la que la viabilidad no se ha tratado como un elemento formal o declarativo, sino como un principio estructural que condiciona y orienta todas las decisiones de diseño, planificación y ejecución. En consecuencia, cada solución propuesta ha sido evaluada no únicamente desde su corrección funcional, sino desde su capacidad efectiva de desplegarse en producción con garantías de estabilidad, seguridad y continuidad. En este sentido, la propuesta incorpora desde su concepción un enfoque orientado a la ejecución real, en el que se han integrado de manera coherente todos los factores que condicionan la correcta implementación del contrato, destacando especialmente:
- La complejidad del entorno tecnológico, caracterizado por la coexistencia de múltiples
plataformas heterogéneas, interdependientes y en evolución constante, lo que exige soluciones adaptativas, específicas y no invasivas.
- La criticidad de los servicios prestados, cuyo correcto funcionamiento tiene un impacto
directo sobre la actividad educativa diaria, lo que implica un nivel de exigencia máximo en términos de estabilidad, rendimiento y disponibilidad.
- La necesidad de continuidad operativa, dado que el sistema se encuentra en producción
permanente y no admite interrupciones significativas ni degradaciones perceptibles para el usuario final.
- La coexistencia simultánea de actuaciones correctivas y evolutivas, que deben
gestionarse en paralelo sin interferencias, asegurando que la mejora del sistema no compromete su funcionamiento actual. Estos factores no han sido considerados como elementos externos que condicionan la ejecución, sino como variables internas del diseño de la solución, lo que permite alinearla desde el inicio con la realidad del entorno en el que debe desplegarse.

Viabilidad como principio de diseño y no como validación posterior Uno de los aspectos que refuerza el carácter diferencial de la propuesta es que la viabilidad no se ha verificado a posteriori, sino que ha sido incorporada como criterio de diseño desde las fases iniciales. Esto implica que:
- No se han planteado soluciones cuya implementación dependa de transformaciones
profundas o inciertas del sistema.
- Se han descartado enfoques teóricos que, aun siendo técnicamente posibles, no resultan
realistas en un entorno en producción.
- Se ha priorizado la adopción de mecanismos de integración compatibles con las
arquitecturas existentes. De este modo, cada decisión técnica se ha tomado evaluando previamente su impacto en:
- La estabilidad del sistema
- La facilidad de despliegue
- La capacidad de mantenimiento posterior
- El riesgo operativo asociado
Este enfoque garantiza que la solución no solo es correcta desde el punto de vista conceptual, sino viable en términos reales de implantación.

Alineación con las condiciones reales de ejecución


La viabilidad del proyecto se ve reforzada por una clara alineación con las condiciones reales de ejecución del contrato, entre las que destacan:
- La necesidad de intervenir sobre sistemas activos, sin margen para actuaciones
disruptivas.
- La coexistencia de múltiples actores y servicios que requieren coordinación.
- La variabilidad de carga y uso en función del calendario académico.
En este contexto, la propuesta ha sido diseñada considerando explícitamente que:
- Las actuaciones deben ser graduales, controladas y reversibles.
- Las soluciones deben integrarse sin generar dependencia crítica entre componentes.
- El sistema debe mantenerse operativo durante todo el ciclo de ejecución.
Esta alineación evita uno de los principales riesgos en este tipo de proyectos: diseñar soluciones técnicamente correctas pero operativamente inviables.

Gestión de la complejidad como factor de viabilidad Lejos de simplificar el entorno, la propuesta asume y gestiona su complejidad como un elemento intrínseco, integrándolo en el modelo de ejecución. Se ha comprendido que la viabilidad no depende de reducir la complejidad del sistema, sino de:
- Controlarla mediante estructuras de decisión claras
- Descomponer las actuaciones en unidades manejables
- Aplicar modelos de intervención progresivos
- Establecer mecanismos de verificación en cada fase
En este sentido, la viabilidad se construye sobre la capacidad de:
- Anticipar escenarios complejos
- Reducir la incertidumbre en la ejecución
- Mantener el control en contextos dinámicos

Garantía de viabilidad a lo largo de todo el ciclo de vida del contrato Otro elemento diferencial es que la viabilidad no se limita a las fases iniciales del proyecto, sino que se extiende a todo su ciclo de vida. La propuesta contempla:
- Una fase de arranque controlada, orientada a reducir incertidumbre inicial.
- Una fase de ejecución continua, con capacidad de adaptación a cambios.
- Una evolución progresiva del sistema, sin acumulación de deuda técnica.
Este enfoque permite asegurar que la solución:
- Es viable en su implantación inicial
- Es sostenible durante su ejecución
- Y sigue siendo válida en escenarios futuros

Síntesis del enfoque de viabilidad De forma integrada, el enfoque general de viabilidad se articula sobre los siguientes principios clave:
- Integración de la viabilidad en el diseño desde el inicio


- Alineación total con la arquitectura y condiciones del entorno
- Gestión activa de la complejidad
- Minimización del riesgo en ejecución
- Garantía de continuidad operativa
- Capacidad de adaptación a evolución del sistema

Conclusión El enfoque adoptado permite afirmar que la propuesta no solo es viable en términos teóricos, sino que ha sido concebida específicamente para ser ejecutable en condiciones reales de producción, con un alto grado de control, previsibilidad y garantía de éxito desde el inicio hasta la finalización del contrato.

2. Viabilidad técnica de la solución
Desde el punto de vista técnico, la viabilidad del proyecto se fundamenta en la adopción de un modelo de intervención rigurosamente alineado con la arquitectura actual de EducaMadrid , evitando de forma consciente cualquier aproximación disruptiva o de alto riesgo que pudiera comprometer la estabilidad del sistema o introducir incertidumbre en su ejecución. Este posicionamiento no responde únicamente a un criterio de prudencia, sino a una comprensión madura de cómo deben abordarse entornos tecnológicos en producción permanente, en los que la evolución debe construirse sobre lo existente y no contra ello. En consecuencia, la propuesta parte de un principio esencial: toda solución debe ser compatible, integrable y progresiva, garantizando en todo momento la continuidad del servicio.

Comprensión de la realidad técnica del ecosistema Se ha entendido de forma precisa que el entorno EducaMadrid no responde a un modelo homogéneo ni monolítico, sino a una arquitectura distribuida compuesta por múltiples sistemas heterogéneos e interdependientes, cada uno con sus propias particularidades tecnológicas, modelos de datos y ciclos de evolución. En este contexto, la viabilidad técnica se apoya en la identificación clara de que las soluciones deben:
- Integrarse en ecosistemas donde coexisten plataformas como Moodle, WordPress,
Nextcloud o desarrollos propios, sin imponer modelos artificiales que no encajen con su naturaleza.
- Respetar las diferencias en paradigmas tecnológicos (frameworks, lenguajes, estructuras
de persistencia y modelos de autenticación).
- Abordar las integraciones como procesos controlados, no como dependencias rígidas o
acoplamientos fuertes. Esta comprensión evita uno de los riesgos más habituales: diseñar soluciones técnicamente correctas en abstracto pero incompatibles con la realidad del entorno.

Integración no intrusiva y preservación del core de los sistemas Uno de los pilares fundamentales de la viabilidad técnica es la decisión explícita de evitar modificaciones innecesarias en el núcleo de los aplicativos existentes. Se ha comprendido que intervenir sobre el core de sistemas como Moodle o WordPress:
- Incrementa exponencialmente el riesgo en actualizaciones futuras.
- Introduce dependencias difíciles de mantener.


- Compromete la sostenibilidad técnica del sistema a medio y largo plazo.
En consecuencia, la propuesta apuesta por un modelo basado en:
- La extensión funcional mediante mecanismos estándar (plugins, APIs, conectores).
- La adaptación de comportamientos sin alteración de la lógica interna de los aplicativos.
- La separación clara entre la lógica de integración y la lógica interna de cada sistema.
Este enfoque garantiza que:
- Las soluciones son compatibles con ciclos de actualización futuros.
- Se reduce la probabilidad de regresiones funcionales.
- Se mantiene la estabilidad estructural del ecosistema.

Arquitectura desacoplada como mecanismo de control de riesgos La viabilidad técnica se apoya de manera determinante en un modelo de arquitectura desacoplada, concebido no solo como una buena práctica, sino como un mecanismo activo de control del riesgo. En este enfoque:
- Cada sistema conserva su autonomía funcional.
- La comunicación entre sistemas se realiza mediante interfaces controladas.
- Las dependencias se gestionan de forma explícita y trazable.
Este desacoplamiento permite:
- Reducir el impacto de cualquier cambio a un ámbito controlado.
- Evitar fallos en cascada entre servicios interdependientes.
- Facilitar la evolución progresiva del sistema.
Además, este modelo permite que distintos componentes evolucionen a velocidades diferentes sin comprometer la coherencia global, lo que resulta especialmente relevante en un entorno en constante cambio.

Uso de conectores especializados y adaptación contextual Otro de los elementos clave que sustentan la viabilidad técnica es el uso de conectores específicos por sistema, diseñados para adaptarse a las características concretas de cada plataforma. Este planteamiento parte de una idea fundamental: en entornos heterogéneos, la uniformidad forzada genera más problemas que soluciones. En consecuencia, la propuesta contempla:
- El desarrollo de mecanismos de integración adaptados a cada tecnología.
- La utilización de APIs, servicios web o procesos intermediarios según corresponda.
- La gestión diferenciada de operaciones en función de las capacidades de cada sistema.
Este enfoque permite:
- Garantizar la compatibilidad sin imponer restricciones artificiales.
- Optimizar la ejecución en función del contexto concreto.
- Reducir la complejidad innecesaria en las integraciones.

Aplicación de principios técnicos avanzados La viabilidad técnica se refuerza mediante la aplicación de principios que incrementan la robustez del sistema y facilitan su operación en entornos complejos:


- Idempotencia
Las operaciones se diseñan de manera que su ejecución repetida no genere efectos secundarios, lo que permite reintentos controlados y reduce el riesgo de inconsistencias.
- Trazabilidad completa
Cada actuación queda registrada, permitiendo su seguimiento, auditoría y análisis posterior, lo que resulta fundamental en entornos distribuidos.
- Reversibilidad
Todas las intervenciones contemplan mecanismos de rollback, permitiendo volver a un estado anterior en caso de incidencia, lo que reduce drásticamente el riesgo operativo. Estos principios no solo mejoran la calidad de la solución, sino que son determinantes para garantizar su viabilidad en entornos reales con incertidumbre operativa.

Implementación progresiva y controlada La propuesta garantiza que las actuaciones pueden desplegarse de manera progresiva, evitando la necesidad de transformaciones estructurales complejas o cambios masivos que incrementen el riesgo. Esto implica:
- Dividir las actuaciones en unidades gestionables.
- Desplegar de forma incremental, validando cada paso.
- Monitorizar el comportamiento tras cada implantación.
Este enfoque permite:
- Detectar problemas en fases tempranas.
- Corregir desviaciones sin impacto global.
- Mantener el control absoluto del proceso de implantación.

Conclusión La viabilidad técnica de la solución se sustenta en una combinación equilibrada de comprensión profunda del entorno, decisiones arquitectónicas prudentes y aplicación de principios avanzados de ingeniería, lo que garantiza que las soluciones propuestas no solo son correctas desde el punto de vista conceptual, sino plenamente ejecutables en el contexto real de EducaMadrid. Este enfoque permite asegurar que:
- Las soluciones se integran de manera natural en el ecosistema existente.
- Se minimizan los riesgos técnicos y operativos.
- Se garantiza la sostenibilidad del sistema a largo plazo.
- La evolución se produce de forma controlada y sin disrupciones.

3. Viabilidad operativa en entorno productivo
Uno de los factores más determinantes para asegurar la viabilidad global del proyecto es la capacidad de ejecutar todas las actuaciones previstas sin comprometer en ningún momento el funcionamiento del sistema en producción, un aspecto especialmente crítico en el contexto de EducaMadrid, dado su carácter de servicio esencial y su uso intensivo por parte de la comunidad educativa. La propuesta parte de una premisa fundamental: el entorno productivo no es un espacio de experimentación, sino un entorno de alta sensibilidad operativa en el que cualquier intervención debe realizarse bajo criterios estrictos de control, previsión y minimización del Página 30 de 192


riesgo. Esta concepción implica que el éxito del proyecto no se mide únicamente por la correcta implementación funcional de las soluciones, sino por la capacidad de integrarlas sin afectar a la continuidad ni a la calidad del servicio.

Comprensión de las condiciones de operación en producción Se ha identificado con precisión que la plataforma EducaMadrid opera bajo condiciones que imponen restricciones claras y no negociables:
- La plataforma debe mantenerse activa de forma continua , sin ventanas amplias de
indisponibilidad.
- Los usuarios finales, fundamentalmente docentes y alumnado, dependen del sistema para
su actividad diaria, lo que implica que cualquier degradación tiene un impacto inmediato.
- Los ciclos de uso del sistema no son uniformes, existiendo picos de carga altamente
exigentes en momentos concretos del calendario académico. Esta realidad conduce a una conclusión clave: toda actuación debe diseñarse pensando en su comportamiento en producción, no únicamente en su validez funcional o técnica. En consecuencia, se ha comprendido que:
- Las intervenciones deben ser prácticamente transparentes para el usuario final, evitando
alteraciones perceptibles en la experiencia de uso.
- Los errores potenciales no pueden trasladarse a producción sin control previo, lo que exige
mecanismos de validación robustos.
- El sistema debe ser capaz de absorber cambios sin comprometer su estabilidad estructural.

Modelo de intervención basado en control operativo Para garantizar esta viabilidad en entorno productivo, la propuesta adopta un modelo operativo basado en el principio de control extremo del ciclo de intervención, en el que cada actuación se gestiona como un proceso completo que incluye preparación, validación, despliegue y verificación. Este modelo se articula en torno a varios mecanismos clave: Despliegues progresivos y controlados Se evita cualquier enfoque de despliegue masivo o de alto impacto, optando por una estrategia incremental que permite:
- Introducir cambios de forma gradual.
- Limitar el alcance de posibles incidencias.
- Validar el comportamiento del sistema tras cada intervención.
Este enfoque no solo reduce el riesgo, sino que permite mantener un control continuo sobre el estado del sistema.

Validación previa en entornos no productivos Se ha integrado la necesidad de validar las actuaciones antes de su paso a producción, siempre que el contexto lo permita. Esto implica:
- Reproducir escenarios representativos del entorno real.
- Verificar la compatibilidad con los sistemas existentes.
- Detectar posibles efectos colaterales antes de su impacto real.


Esta fase actúa como un filtro crítico que evita trasladar errores o comportamientos no deseados al entorno productivo.

Monitorización posterior a cada actuación La viabilidad no se limita al momento del despliegue, sino que se extiende a la fase posterior, en la que resulta imprescindible confirmar que el sistema mantiene su comportamiento esperado. La propuesta contempla:
- Seguimiento activo de indicadores clave tras cada intervención.
- Verificación del rendimiento, estabilidad y funcionamiento funcional.
- Identificación temprana de posibles desviaciones.
Este enfoque permite actuar de forma inmediata ante cualquier anomalía, evitando su propagación o agravamiento.

Capacidad de rollback inmediato Uno de los elementos que más refuerza la viabilidad operativa es la capacidad de revertir cambios de forma controlada en caso de incidencia. Se ha considerado imprescindible que:
- Cada intervención disponga de un mecanismo de reversión definido.
- El proceso de rollback sea rápido y seguro.
- La recuperación del estado anterior no genere inconsistencias.
Este principio introduce un nivel adicional de seguridad que reduce significativamente el riesgo asociado a cualquier despliegue.

Reducción del riesgo operativo La combinación de estos mecanismos permite construir un modelo operativo que transforma la intervención en producción en un proceso controlado, reduciendo significativamente los riesgos asociados. En concreto, este enfoque garantiza que:
- Las actuaciones se integran sin necesidad de interrupciones del servicio, manteniendo
la operatividad en todo momento.
- El sistema conserva su estabilidad estructural, evitando degradaciones progresivas o
efectos acumulativos.
- Se minimiza la probabilidad de introducir incidencias derivadas de cambios no controlados
o insuficientemente validados. Además, este modelo permite gestionar eficazmente la incertidumbre inherente a cualquier entorno complejo, ya que:
- Cada cambio se valida en contexto antes de ampliarse.
- Los fallos potenciales se limitan a ámbitos controlados.
- Se dispone de mecanismos de reacción inmediata.

Orientación preventiva frente a reactiva Un aspecto especialmente relevante es que la propuesta no se limita a gestionar incidencias cuando ocurren, sino que adopta una clara orientación preventiva. Esto implica:


- Diseñar las actuaciones para evitar errores desde su origen.
- Analizar cada intervención en términos de impacto potencial.
- Aplicar controles antes, durante y después del despliegue.
De este modo, la operación en producción deja de ser un proceso reactivo para convertirse en un sistema previsible, trazable y controlado.

4. Viabilidad organizativa y de ejecución simultánea
El proyecto presenta una complejidad organizativa significativa derivada de la necesidad de gestionar de forma simultánea múltiples líneas de trabajo, cada una de ellas con características, prioridades y dependencias propias (TRA, AV, MED, Cloud, Webs, etc.). Esta simultaneidad no constituye un elemento accesorio del contrato, sino una de sus condiciones estructurales, lo que exige un modelo organizativo sólido, flexible y altamente coordinado. La propuesta demuestra una comprensión avanzada de esta realidad, abordando la ejecución no como una secuencia lineal de tareas, sino como un ecosistema de actuación concurrente , en el que distintos procesos deben desarrollarse en paralelo sin generar conflictos, solapamientos ni desviaciones en la calidad del servicio.

Comprensión de la simultaneidad como factor crítico de complejidad Se ha identificado que la ejecución simultánea de múltiples líneas de trabajo implica una serie de retos organizativos que deben gestionarse de forma explícita:
- La coexistencia de actuaciones de distinta naturaleza (correctivas, evolutivas,
adaptativas), cada una con su propio nivel de urgencia.
- La necesidad de atender incidencias críticas mientras se desarrollan mejoras planificadas.
- La aparición de dependencias cruzadas entre actuaciones , que deben ser identificadas
y gestionadas con antelación. En este contexto, la viabilidad organizativa depende directamente de la capacidad de:
- Coordinar equipos y actuaciones sin interferencias.
- Adaptar la planificación a cambios en la prioridad de las tareas.
- Mantener una visión global del estado del sistema en todo momento.
Se trata, por tanto, de un entorno donde la complejidad no se reduce, sino que se gestiona de forma activa y controlada.

Modelo organizativo estructurado por líneas de actuación Para dar respuesta a esta complejidad, la propuesta adopta un modelo organizativo basado en la estructuración del trabajo por líneas funcionales, lo que permite ordenar la ejecución sin perder coherencia global. Este modelo se materializa en:
- La definición de ámbitos de actuación diferenciados, alineados con los bloques del
contrato.
- La asignación clara de responsabilidades dentro de cada línea.
- La existencia de mecanismos de coordinación transversal entre dichas líneas.
Este enfoque permite mantener un equilibrio entre:
- Especialización técnica, al permitir que cada equipo profundice en su ámbito.
- Visión global, al asegurar la coherencia entre actuaciones.


Asimismo, evita la dispersión de esfuerzos y facilita la trazabilidad de las actividades realizadas.

Gestión dinámica de prioridades y toma de decisiones Uno de los elementos más críticos en entornos de ejecución simultánea es la gestión de prioridades, que no pueden considerarse estáticas, sino que evolucionan en función de:
- La aparición de incidencias imprevistas.
- Los cambios en las necesidades del organismo contratante.
- El impacto relativo de cada actuación sobre el sistema.
La propuesta incorpora un enfoque de priorización dinámica que permite:
- Ajustar la planificación en tiempo real.
- Garantizar la atención inmediata a actuaciones críticas.
- Mantener el equilibrio entre mantenimiento correctivo y evolutivo.
Para ello, se consideran criterios como:
- Impacto en el usuario final
- Criticidad del servicio afectado
- Dependencias con otras actuaciones
Este modelo asegura que los recursos se orientan siempre hacia las tareas de mayor valor e impacto.

Coordinación continua y control transversal La viabilidad organizativa se refuerza mediante un modelo de coordinación continua, que evita la fragmentación del proyecto y garantiza la coherencia en la ejecución. Se ha comprendido que en un entorno de estas características:
- La falta de coordinación es uno de los principales riesgos de fallo.
- Las decisiones deben tomarse con visibilidad global del sistema.
- Es necesario mantener una comunicación fluida entre todos los actores implicados.
En este sentido, la propuesta contempla:
- Mecanismos de seguimiento periódico del estado de las actuaciones.
- Canales de comunicación definidos entre equipos técnicos y responsables del contrato.
- Espacios de coordinación para la toma de decisiones en situaciones complejas.
Este modelo permite asegurar que:
- Todas las actuaciones avanzan en la misma dirección.
- Se evitan duplicidades o inconsistencias.
- Se mantiene el control sobre el conjunto del proyecto.

Gestión de la carga de trabajo y eficiencia operativa Otro factor clave para la viabilidad es la capacidad de mantener el control sobre la carga de trabajo en un contexto de alta concurrencia de tareas. Se ha identificado que la eficiencia operativa depende de:
- Distribuir adecuadamente los recursos disponibles.
- Evitar la sobrecarga en determinados equipos o momentos.


- Mantener un ritmo de ejecución sostenible.
En este sentido, la propuesta contempla:
- La planificación equilibrada de tareas.
- La monitorización de la carga operativa.
- La redistribución dinámica del trabajo cuando es necesario.
Este enfoque permite garantizar que el proyecto avanza de forma constante, evitando tanto picos de saturación como periodos de infrautilización.

Prevención de conflictos y aseguramiento de coherencia En entornos de ejecución simultánea, uno de los principales riesgos es la aparición de conflictos entre actuaciones, especialmente cuando afectan a sistemas interdependientes. La propuesta aborda este riesgo mediante:
- La identificación previa de dependencias entre tareas.
- La secuenciación controlada de actuaciones cuando es necesario.
- La validación de compatibilidad entre cambios concurrentes.
Este enfoque permite evitar:
- Incompatibilidades técnicas entre desarrollos.
- Bloqueos operativos derivados de conflictos de ejecución.
- Reprocesos innecesarios.

Síntesis del modelo organizativo De forma integrada, la viabilidad organizativa y de ejecución simultánea se sustenta en los siguientes pilares:
- Estructuración del trabajo por líneas funcionales
- Gestión dinámica de prioridades
- Coordinación continua entre equipos
- Control de carga de trabajo
- Prevención de conflictos y dependencias

5. Viabilidad temporal y planificación realista
El proyecto contempla un horizonte de ejecución claramente definido, estructurado en una fase inicial de arranque y un periodo sostenido de prestación del servicio de 12 meses, lo que exige la adopción de un modelo de planificación que no solo sea coherente con el alcance, sino plenamente alineado con la realidad operativa del entorno EducaMadrid. La propuesta parte de un principio fundamental: la viabilidad temporal no depende únicamente de la duración del proyecto, sino de la calidad de la planificación con la que se articula su ejecución, especialmente en contextos caracterizados por la simultaneidad de actuaciones, la existencia de prioridades dinámicas y la necesidad de operar en entornos productivos sin interrupción. En este sentido, la planificación ha sido concebida como un instrumento activo de control, orientado a garantizar que el proyecto avance de forma ordenada, predecible y adaptable, evitando desviaciones, cuellos de botella o acumulaciones de carga en fases críticas.

Comprensión de los condicionantes temporales del proyecto


Se ha comprendido que la viabilidad temporal está directamente condicionada por una serie de factores propios del entorno y del contrato:
- La coexistencia de actuaciones correctivas y evolutivas que deben ejecutarse de forma
paralela.
- La necesidad de priorizar incidencias urgentes sin desatender desarrollos planificados.
- La existencia de ciclos de uso condicionados por el calendario académico, que impactan
en la capacidad de introducir cambios.
- La dependencia entre determinadas actuaciones, que obliga a una correcta secuenciación
para evitar bloqueos. Estos condicionantes implican que la planificación no puede ser rígida ni lineal, sino que debe concebirse como un sistema dinámico capaz de adaptarse a la evolución del proyecto.

Secuenciación lógica y controlada de actuaciones Uno de los pilares fundamentales de la viabilidad temporal es la correcta secuenciación de las actividades, entendida como la organización lógica de las tareas en función de:
- Sus dependencias técnicas
- Su criticidad operativa
- Su impacto en el sistema
La propuesta incorpora este principio mediante:
- La descomposición de las actuaciones en unidades manejables.
- La identificación explícita de dependencias entre tareas.
- La planificación de ejecuciones en un orden que minimice riesgos y maximice eficiencia.
Este enfoque permite evitar situaciones habituales en proyectos complejos:
- Bloqueos por dependencias no identificadas.
- Retrabajo derivado de secuencias incorrectas.
- Ineficiencias en la utilización de recursos.

Priorización como mecanismo de control temporal La viabilidad temporal no se limita a planificar, sino que requiere la capacidad de decidir correctamente en cada momento qué debe ejecutarse y con qué urgencia. Se ha comprendido que esta priorización debe basarse en criterios objetivos, tales como:
- Impacto en el servicio
- Número de usuarios afectados
- Criticidad funcional de la incidencia o desarrollo
- Relación con otras actuaciones en curso
Este enfoque permite:
- Garantizar la atención inmediata a tareas críticas.
- Evitar la dispersión de esfuerzos en actividades de bajo impacto.
- Mantener el control sobre la evolución global del proyecto.
Asimismo, la priorización se concibe como un proceso continuo, no puntual, lo que permite adaptar la planificación en función de la realidad operativa.


Modelo iterativo de ejecución y entrega progresiva Para garantizar la viabilidad del proyecto en un contexto dinámico, la propuesta adopta un enfoque iterativo basado en entregas progresivas, lo que supone un cambio respecto a modelos tradicionales basados en grandes bloques de entrega. Este modelo implica:
- Desarrollar e implantar soluciones en ciclos cortos y controlados.
- Validar resultados de forma continua.
- Ajustar la planificación en función de la experiencia obtenida en cada iteración.
Las ventajas de este enfoque son claras:
- Reduce el riesgo de desviaciones acumuladas.
- Permite detectar problemas en fases tempranas.
- Proporciona valor tangible de forma continua al organismo contratante.
Además, este modelo es especialmente adecuado en entornos donde las necesidades pueden evolucionar durante la ejecución del contrato.

Planificación estructurada por hitos y bloques funcionales La propuesta organiza la planificación en torno a hitos y bloques funcionales, lo que permite introducir niveles adicionales de control y seguimiento. Este enfoque facilita:
- La segmentación del proyecto en unidades claramente identificables.
- El seguimiento del avance de forma objetiva.
- La evaluación del cumplimiento en cada fase.
Asimismo, permite:
- Identificar desviaciones de forma temprana.
- Aplicar medidas correctoras sin afectar al conjunto del proyecto.
- Mantener la trazabilidad de las actuaciones realizadas.

Flexibilidad y capacidad de replanificación Uno de los elementos diferenciales de la propuesta es la incorporación explícita de mecanismos de flexibilidad, entendidos no como improvisación, sino como capacidad estructurada de adaptación. Se ha comprendido que en un entorno como EducaMadrid:
- Las prioridades pueden cambiar.
- Pueden surgir incidencias imprevistas.
- Determinadas actuaciones pueden requerir ajustes en su planificación.
Por ello, la propuesta contempla:
- La revisión periódica de la planificación.
- La adaptación de cargas de trabajo en función de necesidades reales.
- La replanificación controlada cuando sea necesario.
Este enfoque permite mantener la viabilidad temporal incluso en escenarios dinámicos y cambiantes.


Fecha: 21/05/2026

Prevención de riesgos temporales El modelo adoptado permite prevenir de manera efectiva los riesgos más habituales en la planificación de proyectos complejos:
- Sobrecarga en fases iniciales, al evitar concentrar un volumen excesivo de trabajo al
inicio del contrato.
- Acumulación de tareas en fases finales, mediante la distribución equilibrada de la carga
de trabajo a lo largo del tiempo.
- Retrasos derivados de dependencias no gestionadas, gracias a su identificación previa
y correcta secuenciación. Adicionalmente, el enfoque iterativo permite absorber desviaciones menores sin comprometer el proyecto en su conjunto.

6. Viabilidad en términos de riesgos y contingencias
La viabilidad del proyecto está íntimamente ligada a la capacidad de identificar y gestionar riesgos. Se ha realizado una interpretación avanzada del pliego en este aspecto, considerando escenarios como:
- Fallos en despliegues
- Saturación de sistemas en momentos críticos
- Incidencias derivadas de integraciones complejas
- Problemas de sincronización entre sistemas
Para cada uno de estos escenarios, la propuesta incorpora:
- Medidas preventivas (validaciones, pruebas, monitorización)
- Planes de contingencia (rollback, redundancia, procedimientos de emergencia)
- Seguimiento continuo del estado del sistema
Este enfoque permite transformar la incertidumbre en riesgo controlado, garantizando la viabilidad incluso en situaciones adversas.

7. Viabilidad basada en la experiencia y enfoque probado
La propuesta refleja un enfoque claramente orientado a la ejecución real, sustentado en prácticas consolidadas y modelos de trabajo contrastados. Esto se traduce en:
- Uso de metodologías reconocidas en la Administración (Métrica v3).
- Aplicación de buenas prácticas en entornos complejos.
- Priorización de soluciones realistas frente a propuestas teóricas.
El diseño evita:
- Dependencias tecnológicas innecesarias.
- Introducción de herramientas no probadas.
- Cambios estructurales de alto riesgo.
Esta prudencia técnica refuerza la viabilidad global del proyecto.

8. Síntesis de factores de viabilidad


De forma sintética, la viabilidad del proyecto se sustenta en los siguientes elementos:
- Alineación total con la arquitectura existente.
- Enfoque no invasivo y desacoplado.
- Modelo operativo adaptado a entorno productivo.
- Gestión estructurada de múltiples líneas de trabajo.
- Planificación realista y flexible.
- Control riguroso de riesgos.

9. Conclusión
La propuesta presentada demuestra de forma clara y fundamentada la viabilidad completa del proyecto en todas sus dimensiones: técnica, operativa, organizativa y temporal. Este nivel de viabilidad permite:
- Ejecutar el contrato con garantías desde su inicio.
- Minimizar riesgos durante todo el ciclo de vida.
- Asegurar la continuidad del servicio.
- Mantener la coherencia y estabilidad del sistema.
3.1.4 Metodología de trabajo aplicada Para la ejecución del presente proyecto, empresa_s adoptará la metodología Métrica v3 como marco de referencia para la gestión, desarrollo y mantenimiento de los sistemas de información. Esta metodología, ampliamente consolidada en entornos de la Administración Pública, garantiza un enfoque estructurado, trazable y alineado con estándares internacionales, facilitando la correcta evolución de todo el ciclo de vida del software. empresa_s no solo aplicará Métrica v3 como marco metodológico, sino que la enriquecerá con buenas prácticas actuales (enfoques ágiles, automatización de pruebas, integración continua), garantizando así un equilibrio óptimo entre rigor metodológico y capacidad de adaptación. A continuación, se describen los aspectos más relevantes de Métrica v3 aplicables a este proyecto. Objetivos La aplicación de la metodología Métrica v3 permitirá a la Consejería de Digitalización disponer de un marco metodológico sólido orientado a:
- Definir y evolucionar sistemas de información alineados con los objetivos estratégicos de
la Organización, dentro de un contexto estructurado y planificado.
- Garantizar el desarrollo de soluciones software que respondan eficazmente a las
necesidades de los usuarios, reforzando especialmente la calidad del análisis de requisitos.
- Incrementar la eficiencia y productividad de los equipos TIC, favoreciendo la reutilización
de componentes y la adaptación ágil a cambios organizativos o tecnológicos.
- Mejorar la comunicación entre todos los agentes implicados en el ciclo de vida del software,
clarificando roles, responsabilidades y expectativas.
- Facilitar la operación, mantenimiento y evolución de los sistemas implementados,
asegurando su sostenibilidad en el tiempo. Enfoque y estructura de Métrica v3 Métrica v3 se articula conforme a los principios establecidos en la norma ISO/IEC 12207 sobre procesos del ciclo de vida del software, diferenciando claramente entre:
- Procesos principales: planificación, desarrollo y mantenimiento.


- Procesos de apoyo e interfaz: orientados a la integración con el entorno organizativo.
Uno de los aspectos clave de esta metodología es su flexibilidad, permitiendo adaptar su aplicación a las características específicas del proyecto, optimizando el esfuerzo en función de su alcance, complejidad y contexto organizativo. Procesos principales Métrica v3 se fundamenta en un enfoque orientado a procesos, alineado con estándares internacionales, e incorpora tres grandes bloques:
- Planificación de Sistemas de Información (PSI).
- Desarrollo de Sistemas de Información (DSI).
- Mantenimiento de Sistemas de Información (MSI).
Este enfoque amplía versiones anteriores, incorporando la planificación estratégica como un elemento clave para asegurar la coherencia entre la tecnología y los objetivos del negocio. (PSI) Planificación de Sistemas de Información El proceso de planificación tiene como objetivo proporcionar una visión estratégica y global de los sistemas de información, estableciendo una hoja de ruta que garantice su alineación con las necesidades actuales y futuras de la Organización. En un entorno caracterizado por la rápida evolución tecnológica y la creciente externalización de servicios, este proceso adquiere especial relevancia, permitiendo:
- Adaptar los sistemas a escenarios de cambio continuo.
- Evaluar adecuadamente la adopción de soluciones estándar frente a desarrollos a medida.
- Controlar los riesgos derivados de la externalización de servicios TIC.
- Definir modelos de información integrados que faciliten la explotación avanzada de datos.
Como resultado, se obtiene un Plan de Sistemas de Información que define la arquitectura tecnológica, el mapa de sistemas y la cartera de proyectos necesarios para soportar la estrategia corporativa. (DSI) Desarrollo de Sistemas de Información El proceso de desarrollo se estructura en distintas fases que cubren íntegramente el ciclo de vida del software:
- Estudio de Viabilidad (EVS).
- Análisis del Sistema (ASI).
- Diseño del Sistema (DSI).
- Construcción (CSI).
- Implantación y Aceptación (IAS).
- Mantenimiento (MSI).
Este enfoque garantiza la trazabilidad completa desde los requisitos hasta la puesta en producción, combinando prácticas de desarrollo estructurado y orientado a objetos, e incorporando técnicas de modelado estándar como UML. Estudio de Viabilidad del Sistema (EVS) En esta fase se analizan las necesidades planteadas y se definen posibles soluciones desde un punto de vista técnico, económico, operativo y legal. Se evaluarán distintas alternativas (desarrollo a medida, soluciones comerciales o mixtas), seleccionando la más adecuada en base a su impacto, coste y riesgos asociados. El resultado de este análisis servirá como base para la toma de decisiones y la definición del alcance del proyecto. Página 40 de 192


Análisis del Sistema de Información (ASI) Esta fase tiene como finalidad definir en detalle los requisitos del sistema, tanto funcionales como no funcionales, garantizando su correcta comprensión y trazabilidad. Se elaborarán modelos de análisis (casos de uso, modelo de datos, procesos, etc.) y se definirán las interfaces de usuario, asegurando que el sistema responde a las necesidades reales de los usuarios. El resultado principal será la Especificación de Requisitos de Software (ERS) , que actuará como referencia contractual y técnica para el desarrollo posterior. Diseño del Sistema de Información (DSI) En esta fase se define la arquitectura técnica del sistema y el diseño detallado de sus componentes, incluyendo:
- Estructura modular del sistema.
- Entorno tecnológico.
- Seguridad y control de accesos.
- Requisitos de operación y administración.
- Plan de pruebas.
- Estrategia de migración de datos (si aplica).
Este diseño garantiza la coherencia, escalabilidad y mantenibilidad de la solución. Construcción del Sistema de Información (CSI) Durante esta fase se lleva a cabo la implementación del sistema, incluyendo:
- Desarrollo de código.
- Pruebas unitarias e integración.
- Preparación de entornos.
- Elaboración de documentación técnica y de usuario.
Se asegura que cada componente cumple con las especificaciones definidas y que el sistema funciona de forma integrada. Implantación y Aceptación (IAS) Esta fase contempla la puesta en producción del sistema y su validación final por parte de los usuarios. Incluye:
- Ejecución del plan de implantación.
- Pruebas de aceptación.
- Formación de usuarios.
- Definición de niveles de servicio.
- Elaboración del plan de mantenimiento.
El objetivo es garantizar una transición controlada y exitosa al entorno productivo. Mantenimiento del Sistema de Información (MSI) El proceso de mantenimiento asegura la evolución continua del sistema tras su puesta en producción, gestionando las solicitudes de cambio y mejora. Se contemplan distintos tipos de mantenimiento:
- Correctivo: resolución de incidencias.


- Evolutivo: incorporación de nuevas funcionalidades.
- Adaptativo: ajustes por cambios tecnológicos.
- Perfectivo: mejoras de rendimiento y calidad.
Se establecerá un sistema de gestión de incidencias y evolución que permita el seguimiento, control y análisis de todas las actuaciones realizadas. 3.1.5 Rendimiento previsible de las distintas soluciones El rendimiento previsible de las soluciones propuestas se fundamenta en un enfoque técnico sólido basado en la optimización estructural, el desacoplamiento arquitectónico, la ejecución asíncrona y la gestión eficiente de la concurrencia, elementos que, combinados, permiten garantizar un comportamiento estable, escalable y resiliente incluso en escenarios de máxima carga propios del ecosistema EducaMadrid A continuación, se detalla de forma pormenorizada el rendimiento esperado en cada uno de los bloques funcionales.
1. MEJORAS Y MANTENIMIENTOS TRANSVERSALES (TRA)
Las actuaciones transversales presentan un rendimiento altamente predecible al apoyarse en una arquitectura desacoplada que evita intervenciones directas sobre los núcleos de los sistemas. Este enfoque permite ejecutar operaciones de gran impacto como sincronizaciones masivas, cambios de identidad o ajustes en SSO mediante procesos asíncronos orquestados por lotes, reduciendo significativamente la presión sobre los sistemas productivos. El uso de mecanismos idempotentes elimina la duplicidad de operaciones y garantiza que cualquier reintento no introduce inconsistencias, lo que se traduce en una ejecución eficiente incluso en condiciones de fallo o alta carga.
2. AULAS VIRTUALES (AV)
En el caso de Moodle, el rendimiento se prevé excelente incluso en los momentos más exigentes (inicio de curso, entregas, evaluaciones), gracias a la combinación de:

- Optimización de consultas SQL críticas.
- Sistemas avanzados de caché (MUC, Redis).
- Distribución de carga entre frontend y tareas cron.
El uso intensivo de procesamiento en segundo plano para operaciones pesadas (copias, borrados, IA, indexaciones) permite aislar estas cargas del usuario final, garantizando una experiencia fluida incluso cuando el sistema se encuentra sometido a alta concurrencia
3. MEDIATECA (MED)
El rendimiento de la Mediateca se sustenta en un modelo híbrido que combina almacenamiento estructurado y motores de indexación (ElasticSearch), permitiendo resolver consultas complejas en tiempos muy reducidos. Las operaciones intensivas en cómputo, como la generación de subtítulos o resúmenes mediante IA, se ejecutan de forma diferida mediante colas de procesamiento, asegurando que el usuario nunca perciba latencias asociadas a estas tareas.
4. CONSULTAS LDAP (LDAP)


El sistema LDAP se beneficia de consultas optimizadas y estructuras indexadas, lo que permite gestionar grandes volúmenes de autenticaciones y consultas de identidad con tiempos de respuesta mínimos. El control de concurrencia y el uso de caches de sesión permiten además reducir la carga en los sistemas centrales.
5. EXELEARNING ONLINE (EXE)
El rendimiento del servicio eXeLearning se ve reforzado por su integración eficiente con Moodle y Nextcloud, evitando duplicidades y reduciendo tiempos de transferencia de contenidos. La arquitectura de servicios permite distribuir la carga sin concentrarla en un único punto, mejorando la escalabilidad.
6. CORREOWEB (COR)
La actualización de Roundcube y la racionalización de plugins permiten una gestión más eficiente de grandes volúmenes de correo, reduciendo tiempos de carga en bandejas y mejorando la respuesta en operaciones frecuentes. La optimización de consultas y almacenamiento reduce cuellos de botella habituales en sistemas de mensajería web.
7. WORDPRESS MULTISITE (WPM)
El rendimiento del multisite se garantiza mediante un enfoque de actualización controlada, optimización de base de datos y uso de cachés, permitiendo gestionar miles de sitios con tiempos de carga homogéneos y mínimos. El uso de despliegues progresivos minimiza impactos en producción.
8. FORMULARIOS (FOR)
El rendimiento del servicio de formularios se sustenta en un conjunto coordinado de optimizaciones orientadas tanto a la capa de persistencia como al procesamiento de respuestas. En primer lugar, la indexación selectiva de tablas críticas permite resolver de forma eficiente consultas de lectura intensiva, como el acceso a resultados agregados o filtrados, incluso en entornos donde se registran miles de respuestas concurrentes. Adicionalmente, la implantación de procesos de mantenimiento periódico (limpieza de tablas temporales, archivado de históricos, compactación de índices) evita la degradación progresiva típica de sistemas de encuestas masivas. Esto permite que el sistema mantenga un comportamiento estable a lo largo del tiempo, sin penalizaciones por crecimiento de datos. Desde el punto de vista de ejecución, los procesos más costosos como generación de informes complejos o exportaciones se realizan mediante procesamiento diferido o asincrónico, evitando bloqueos en operaciones interactivas. En consecuencia, se garantiza una experiencia de usuario fluida incluso en escenarios de alta participación simultánea (ej. encuestas institucionales a gran escala).
9. EMPIEZA (EMP)
EMPieza presenta un modelo de rendimiento especialmente robusto gracias a su arquitectura desacoplada y modular, que permite la ejecución independiente de servicios sin interferencia entre ellos. Este diseño se ve reforzado por el uso de replicación de bases de datos (como Galera Cluster), lo que garantiza tanto alta disponibilidad como capacidad de absorción de carga en entornos de uso intensivo.


El sistema está optimizado para gestionar simultáneamente operaciones de acceso a contenidos, interacción con aulas virtuales y consumo de servicios multimedia, manteniendo tiempos de respuesta homogéneos. La separación entre lógica de negocio y persistencia permite escalar componentes según necesidad, evitando la saturación de recursos críticos. Gracias a su arquitectura modular y replicación de bases de datos, EMPieza puede absorber alta concurrencia manteniendo estabilidad, especialmente en servicios integrados con aulas virtuales y contenidos dinámicos.
10. BUSCADOR (BUS)
El buscador se beneficia de un diseño orientado a rendimiento, basado en el uso de tablas materializadas e índices compuestos adaptados a consultas reales de usuario. Este enfoque permite precalcular resultados frecuentes, reduciendo drásticamente el coste computacional en tiempo de ejecución. Además, las consultas complejas se optimizan mediante estrategias de filtrado progresivo y paginación eficiente, evitando cargas innecesarias en el sistema. Esto permite garantizar una experiencia de búsqueda ágil incluso en momentos de uso intensivo o ante consultas con múltiples criterios combinados.
11. VIDEOCONFERENCIA (VID)
El rendimiento de los servicios de videoconferencia se sustenta en una arquitectura distribuida que evita puntos únicos de fallo. La coexistencia de plataformas como Jitsi, BigBlueButton o Wowza permite segmentar la carga en función del tipo de sesión, distribuyendo los recursos de forma eficiente. El sistema incorpora mecanismos avanzados de control de admisión y balanceo dinámico, que ajustan en tiempo real la asignación de recursos en función de la carga detectada. Esto permite mantener la calidad de servicio en retransmisiones de alta audiencia, evitando degradaciones en audio y vídeo incluso en escenarios extremos. A ello se suma la capacidad de aplicar reglas dinámicas para evitar saturaciones, priorizando sesiones críticas.
12. ANIMALANDIA (ANI)
El rendimiento en Animalandia mejora sustancialmente mediante la modernización del código legacy, eliminando prácticas obsoletas como consultas no parametrizadas o estructuras redundantes. La introducción de caché en capas de acceso y optimización de consultas SQL reduce significativamente los tiempos de respuesta, especialmente en páginas de alto tráfico. La actualización tecnológica permite además aprovechar mejoras en los motores PHP modernos, reduciendo tiempos de ejecución y mejorando la eficiencia global.
13. SINCRONIZACIÓN DE USUARIOS (SYN)
El pipeline de sincronización se diseña específicamente para gestionar grandes volúmenes de datos mediante procesamiento incremental. Esto evita la necesidad de recalcular estados completos, reduciendo tiempos de ejecución y consumo de recursos. Las diferentes fases (ingesta, normalización, reconciliación y publicación) están desacopladas, lo que permite ejecutar cada una de ellas de forma independiente y controlada. El uso de checkpoints


y control de cambios garantiza un rendimiento estable incluso en escenarios de alta variabilidad de datos.
14. PORTAL CAU (CAU)
El portal CAU obtiene mejoras de rendimiento mediante la optimización de consultas a base de datos, el uso de cachés para consultas frecuentes y la reducción de operaciones redundantes en la gestión de incidencias. El sistema responde de forma eficiente incluso en picos de solicitudes, gracias a la priorización inteligente de operaciones y a la estructuración de datos orientada a consulta rápida.
15. EDUCASAAC (EDU)
La refactorización del sistema elimina sobrecargas innecesarias derivadas de código no optimizado, introduciendo una estructura más eficiente y ligera. La securización también contribuye al rendimiento al evitar validaciones redundantes y mejorar los flujos de ejecución.
16. CLOUD (CLO)
Nextcloud optimizado permite operar con grandes volúmenes de datos manteniendo tiempos de respuesta bajos tanto en carga como en descarga de archivos. La optimización del sistema de archivos, junto con la mejora de índices y caché, permite ofrecer una experiencia fluida incluso en escenarios de uso intensivo.
17. BUZÓN ANÓNIMO (BAN)
El diseño ligero del sistema garantiza tiempos de respuesta prácticamente inmediatos, al minimizar el número de operaciones necesarias y evitar dependencias complejas.
18. DTIC (DTIC)
El rendimiento del sistema DTIC se ve notablemente incrementado mediante una optimización estructural tanto en la capa de presentación como en la capa de persistencia. En particular, se aborda la mejora de formularios mediante la reducción de validaciones redundantes en cliente y servidor, así como la simplificación de flujos de procesamiento, lo que minimiza el número de operaciones necesarias para completar cada transacción. Desde el punto de vista de acceso a datos, la optimización de consultas —mediante indexación adecuada y uso de consultas preparadas— reduce significativamente la latencia en operaciones críticas. Asimismo, se evita el acceso repetitivo a información no cambiante mediante técnicas de cacheado selectivo, lo que contribuye a mantener tiempos de respuesta homogéneos incluso ante un elevado número de peticiones simultáneas. El resultado es un sistema ágil, con una experiencia de usuario fluida y sin bloqueos perceptibles.
19. SEGUIMIENTOS (SEG)
El rendimiento del módulo de Seguimientos se articula en torno a la gestión eficiente de grandes volúmenes de datos históricos. Para ello, se implementa un modelo de paginación avanzada que evita la carga masiva de registros en memoria, asegurando tiempos de respuesta constantes independientemente del tamaño del repositorio.


En paralelo, la gestión de adjuntos se optimiza mediante almacenamiento desacoplado y recuperación bajo demanda, lo que evita penalizaciones en consultas estándar. Esta separación entre metadatos y contenido permite mantener una navegación ágil, incluso en escenarios con alta densidad de información acumulada. Todo ello se traduce en un comportamiento estable y predecible, clave para sistemas con crecimiento continuo de datos.
20. ALBOR (ALB)
El sistema ALBOR incorpora un modelo de recuperación de información basado en técnicas RAG (Retrieval-Augmented Generation), cuyo rendimiento se optimiza mediante la indexación previa de contenidos relevantes y la limitación controlada del ámbito de consulta. Este enfoque evita el procesamiento exhaustivo de grandes volúmenes de información en tiempo real, sustituyéndolo por un acceso rápido a estructuras previamente indexadas. Además, la arquitectura modular del sistema permite desacoplar la fase de indexación de la fase de consulta, lo que garantiza que el rendimiento en la interacción con el usuario no se vea afectado por la complejidad del corpus documental. El resultado es un sistema con tiempos de respuesta bajos y comportamiento consistente incluso en escenarios de uso intensivo.
21. AVISOS (AVI)
El módulo de avisos se diseña bajo un principio de desacoplamiento total respecto a los sistemas principales, lo que permite gestionar envíos masivos sin impacto en el rendimiento global de la plataforma. El uso de cacheado permite evitar recalculaciones innecesarias en la presentación de avisos, mientras que la programación diferida de envíos distribuye la carga a lo largo del tiempo, evitando picos de consumo de recursos. Adicionalmente, la existencia de mecanismos de validación previa minimiza errores que podrían generar reprocesamientos, contribuyendo a la eficiencia global del sistem.
22. FOROS (FOR)
La optimización de phpBB se centra en la mejora de rendimiento en dos áreas clave: navegación y búsqueda. Para ello, se implementa una estrategia de indexación específica sobre mensajes, hilos y usuarios, lo que permite resolver consultas de forma rápida incluso en foros con alta actividad. Asimismo, se reduce la carga en base de datos mediante el uso de cache para contenidos frecuentemente accedidos, evitando consultas repetitivas. Esta combinación de optimización estructural y cacheado permite mantener tiempos de respuesta bajos incluso en escenarios de uso intensivo, garantizando una experiencia de usuario fluida.
23. BOLETINES (BOL)
La modernización tecnológica del sistema de boletines introduce mejoras significativas en la eficiencia de generación y envío de contenidos. La migración a versiones modernas del lenguaje y las bibliotecas permite aprovechar optimizaciones a nivel de ejecución, reduciendo tiempos de procesamiento.


La gestión de contenido, especialmente de imágenes, se optimiza mediante técnicas de compresión y tratamiento previo, lo que reduce el peso de los envíos y mejora su velocidad. Además, la posibilidad de validar previamente los boletines evita errores en producción, eliminando reprocesamientos innecesarios. En conjunto, el sistema es capaz de gestionar envíos masivos de forma rápida y eficiente.
24. AYUDA (AYU)
El sistema de ayuda basado en RAG se construye sobre un modelo de indexación previa, lo que permite ofrecer respuestas prácticamente inmediatas a las consultas de los usuarios. Al desacoplar la fase de procesamiento del contenido de la fase de consulta, se elimina la necesidad de analizar grandes volúmenes de información en tiempo real. Además, el motor de consulta se limita a fuentes previamente validadas, lo que reduce el espacio de búsqueda y mejora la eficiencia. Este enfoque garantiza tanto rapidez como calidad en las respuestas, sin generar carga adicional significativa sobre el backend.
25. PORTAL (POR)
El rendimiento del portal se apoya en una capa de APIs optimizadas, diseñadas específicamente para minimizar latencias en operaciones de integración. Estas APIs utilizan mecanismos de cacheado, control de versiones y optimización de consultas para garantizar tiempos de respuesta reducidos. La separación entre capa de presentación y capa de servicios permite además escalar de forma independiente cada componente, evitando cuellos de botella y mejorando la resiliencia del sistema. Este enfoque es especialmente relevante en un entorno donde múltiples aplicaciones consumen servicios de forma concurrente.
26. WEB ESTÁTICA (WES)
La naturaleza estática de este componente permite alcanzar el máximo nivel de rendimiento posible. El contenido se sirve directamente desde sistemas optimizados para entrega de recursos, eliminando prácticamente cualquier tiempo de procesamiento dinámico. El uso de cache a diferentes niveles (servidor, navegador, CDN cuando aplica) permite tiempos de carga prácticamente instantáneos, incluso en escenarios de alta demanda. Este comportamiento convierte a la web estática en uno de los elementos más eficientes de la plataforma.
27. FRAMEWORK DE INTERFAZ (IFZ)
El framework de interfaz contribuye directamente al rendimiento mediante el uso de componentes reutilizables, optimizados y de baja carga. La estandarización de elementos evita duplicidades de código y reduce el peso de las páginas. Asimismo, la optimización en el renderizado — tanto en cliente como en servidor— permite ofrecer una experiencia de usuario fluida, con tiempos de respuesta reducidos y menor consumo de recursos. Este enfoque mejora no solo el rendimiento técnico, sino también la percepción de velocidad por parte del usuario.


28. ENTORNOS MAX (MAX)
El rendimiento de los entornos MAX se basa en su carácter controlado y aislado. Al limitar el número de variables externas, se elimina la incertidumbre en el comportamiento del sistema, garantizando tiempos de respuesta constantes. Este tipo de entorno es especialmente eficiente para escenarios críticos como evaluaciones, donde la estabilidad y la predictibilidad del rendimiento son factores determinantes.
29. GESTIÓN DE TÍTULOS (GES)
El sistema de gestión de títulos implementa un modelo de procesamiento por lotes, lo que permite ejecutar operaciones sobre grandes volúmenes de datos sin bloquear el sistema. La ejecución diferida de tareas intensivas asegura que estas no interfieran con otras operaciones, mientras que la optimización de acceso a datos reduce los tiempos de generación de resultados. Este enfoque permite mantener un rendimiento constante incluso en procesos masivos.
30. MEDIDAS DE USO (USO)
El sistema de medidas de uso está diseñado específicamente para ser no intrusivo, empleando mecanismos ligeros de recogida de datos que no interfieren con la operación de los sistemas principales. El procesamiento de métricas se realiza de forma desacoplada y, en su caso, diferida, lo que garantiza un impacto prácticamente nulo en el rendimiento global de la plataforma.
31. WEKAN (WEK)
El despliegue de Wekan en contenedores permite escalar horizontalmente en función de la demanda, garantizando estabilidad incluso en escenarios de alta concurrencia. La independencia de instancias y la posibilidad de replicación facilitan la distribución de carga, evitando saturaciones y manteniendo tiempos de respuesta homogéneos.
32. MAMOOD (MAM)
El sistema MAMOOD destaca por su capacidad de orquestar procesos de forma eficiente, controlando la concurrencia y evitando ejecuciones simultáneas conflictivas. El uso de mecanismos de bloqueo y planificación garantiza que los recursos se utilicen de forma óptima. Además, la monitorización de ejecuciones permite detectar y corregir desviaciones de rendimiento, manteniendo un comportamiento estable incluso en operaciones complejas.
33. EMLAB (EML)
La optimización de módulos y formularios reduce el número de operaciones necesarias en cada interacción, mejorando tiempos de carga y procesamiento. La estructuración eficiente del código y la optimización de accesos a base de datos permiten ofrecer una experiencia fluida, incluso en escenarios con alta interacción de usuarios .
34. ABIESWEB (ABI)


La actualización tecnológica de AbiesWeb introduce mejoras significativas en el motor de consultas, permitiendo búsquedas más rápidas y precisas. La optimización de índices y la mejora en la gestión de caracteres y datos permiten reducir significativamente la latencia en operaciones habituales, especialmente en catálogos de gran tamaño. Esto se traduce en una mejora tangible en la experiencia de los usuarios finales.

## 1.3. Memoria Técnica

### 1.3.1. Solución técnica ofertada

#### 1.3.1.1. Satisfacción de los requisitos

3.1.6 Satisfacción de los requisitos 3.1.6.1 Definición y Alcance de los trabajos
##### 1.3.1.1.1. APARTADO: MEJORAS Y MANTENIMIENTOS TRANSVERSALES (TRA)
Propuesta técnica de empresa_s La solución se concibe como una capa transversal de evolución y aseguramiento de la continuidad de EducaMadrid, orientada a resolver cambios comunes sobre usuarios, centros, seguridad, interfaz, autenticación, APIs y calendarios sin introducir dependencias innecesarias en el núcleo de los aplicativos existentes. El enfoque evita modificaciones en el core de productos y servicios cuando no sean imprescindibles, prioriza conectores desacoplados, trazabilidad operativa, reversibilidad de cambios y pruebas específicas por servicio afectado. Cada apartado se aborda como una pieza independiente y desplegable de forma controlada, aunque se apoya en principios comunes: integración segura, ejecución idempotente, auditoría de operaciones, tratamiento prudente de datos personales, compatibilidad con el ecosistema heterogéneo de EducaMadrid y bajo impacto en producción. La solución técnica no introduce información económica ni condicionantes ajenos al sobre técnico.

Enfoque técnico transversal para REQUISITO: II.1. 1 El bloque TRA se trata como una línea de trabajo horizontal que debe convivir con aplicaciones desarrolladas en tecnologías distintas, bases de datos y mecanismos de autenticación variados, así como servicios que dependen de sincronizaciones de identidad, correo, contenidos, calendarios y espacios de centro. Para que el mantenimiento evolutivo no se convierta en intervenciones manuales repetitivas, se propone una arquitectura de servicios auxiliares, scripts verificables, conectores por aplicativo y registros de auditoría que permitan saber qué se ha cambiado, cuándo, por qué servicio y con qué resultado. La arquitectura se apoya en tres capas. La primera es una capa de orquestación, responsable de recibir solicitudes desde los sistemas de referencia, validar permisos, normalizar datos y generar una operación única con identificador trazable. La segunda es una capa de ejecución por conectores, donde cada aplicación aplica el cambio conforme a su modelo interno sin forzar una solución uniforme que no encaje con su tecnología. La tercera es una capa de observabilidad, que registra estados, errores, métricas de duración, intentos de reintento y evidencias técnicas de finalización. Diseño idempotente: una operación repetida con los mismos datos no provoca duplicados ni cambios inesperados. Seguridad por defecto: autenticación entre servicios, autorización por rol, cifrado en tránsito y secretos fuera del código fuente. Compatibilidad progresiva: los aplicativos con menor capacidad de integración pueden incorporarse inicialmente mediante tareas programadas o colas controladas.


Trazabilidad: cada operación generará un estado global y estados parciales por servicio, permitiendo diagnóstico sin acceder manualmente a todos los sistemas. Pruebas de regresión específicas: se probarán los flujos críticos de usuario, centro, sesión, calendario e interfaz antes de cada despliegue. Como criterio de ejecución, se separan los cambios de configuración, los cambios de datos y los cambios de código. Esta separación permite aplicar validaciones distintas: pruebas unitarias para código, comprobaciones de integridad para datos y verificación de conectividad para configuración. En servicios críticos se habilitarán despliegues reversibles, con respaldo de configuración y ejecución inicial en entornos no productivos antes de activar la operación en producción. Mejora propuesta: Se incorporará un “registro único de operación transversal” con identificador legible, por ejemplo TRA-2026- 000145, que permita seguir una misma operación aunque afecte a correo, mediateca, WordPress, formularios, cloud o servicios internos. REQUISITO: II.1.1.1. Borrado y cambios de los IDs de usuario (TRA1) Requerimiento EducaMadrid Implementación de un sistema que permita sincronizar cambios en los usuarios provenientes de raíces o el portal educativo con los servicios en la plataforma online, garantizando que los cambios en la información de los usuarios se propaguen de manera automática a todos los servicios. Requisitos:
- Sincronización de usuarios con el aplicativo central:
o El sistema debe poder leer la base de datos del aplicativo central y sincronizar la información de los usuarios con la plataforma online. o Debe ser capaz de detectar cambios en la información de los usuarios, incluyendo a baja de un usuario.
- Propagación de cambios a los servicios:
o El sistema debe poder propagar los cambios en la información de los usuarios a todos los servicios en la plataforma online, incluyendo: o Correoweb. o Aulas virtuales. o Páginas de centros. o Formularios. o Mediateca. o Empieza. o Otros. o Debe ser capaz de propagar los cambios en tiempo real.
- Seguridad y autenticación:
o El sistema debe utilizar métodos seguros para propagar los cambios e impedir que usuarios no autorizados inicien el sistema. o Debe ser capaz de cifrar la información de los usuarios para protegerla contra accesos no autorizados.
- Monitorización y reportes:
o El sistema debe proporcionar monitorización y reportes para garantizar que los cambios se están propagando correctamente a los servicios. o Debe ser capaz de generar reportes de errores y excepciones para facilitar la depuración y resolución de problemas. Página 50 de 192


Fecha: 21/05/2026

Requisitos técnicos

- Lenguaje de programación:
o El sistema debe ser implementado en un lenguaje de programación moderno y robusto.
- Bases de datos:
o El sistema debe utilizar una base de datos relacional como MySQL o PostgreSQL para almacenar la información de los usuarios.
- Cambios en aplicativos:
o No deben producirse cambios en el core de los aplicativos
- APIs y conectores:
o El sistema debe utilizar APIs y conectores para interactuar con el aplicativo central y los servicios en la plataforma online. Propuesta técnica de empresa_s El objetivo de TRA1 es disponer de un mecanismo que detecte cambios procedentes del aplicativo central, raíces o portal educativo y los propague a los servicios de EducaMadrid sin intervención manual ordinaria. La solución propuesta no se limita a copiar datos: interpreta eventos de ciclo de vida de usuario, diferencia entre cambio de identificador, baja lógica, baja definitiva, modificación de atributos y corrección administrativa, y aplica a cada servicio la operación que corresponda según su modelo de datos. Para evitar inconsistencias, se define un repositorio de sincronización con una tabla de eventos de usuario y una tabla de estado por conector. El repositorio puede implementarse sobre PostgreSQL y contendrá únicamente la información necesaria para ejecutar y auditar la operación: identificador anterior, identificador nuevo, tipo de cambio, fecha de origen, sistema emisor, huella de datos y estado de cada servicio. No se almacenarán credenciales ni información sensible innecesaria. Los datos personales se tratarán con minimización y se cifrarán los campos que puedan requerir persistencia temporal. La sincronización se ejecutará con un patrón mixto. Para cambios que admitan procesamiento inmediato se utilizará un evento en cola o llamada API firmada. Para servicios que requieran ventanas de seguridad o procesos internos se utilizarán trabajos programados con bloqueo distribuido, de forma que no haya dos ejecuciones concurrentes sobre el mismo usuario. El conector de cada servicio confirmará el resultado con un código normalizado: aplicado, no aplicable, pendiente, error recuperable o error bloqueante.

Elemento Tratamiento propuesto Resultado esperado Cambio de ID Mapa de equivalencias El usuario conserva vínculos, temporal entre ID antiguo e ID contenidos y permisos sin nuevo, con actualización en cuentas duplicadas. servicios y comprobación de referencias. Baja de usuario Baja lógica inicial, revocación Se evita acceso no autorizado de acceso y activación de y se mantiene trazabilidad reglas específicas por para auditoría. servicio.


Fecha: 21/05/2026

Propagación Conectores con API, La plataforma recibe cambios consultas seguras o tareas de de forma homogénea sin aplicación según capacidad modificar cores. del servicio. Errores Reintentos con backoff, cola Los fallos quedan localizados de incidencias técnicas y por servicio y no bloquean reporte de excepciones. toda la operación.

Un ejemplo de flujo sería el cambio de ID de un docente que ha sido corregido en el sistema central. El motor detecta el cambio, crea el evento, bloquea temporalmente operaciones simultáneas sobre ese usuario, actualiza el correo o alias cuando aplique, propaga el nuevo identificador a formularios, mediateca y otros, conserva la titularidad de recursos y finalmente emite un informe de operación con los servicios actualizados y los que no requerían actuación. evento = leer\_cambio\_usuario(origen="portal", id\_antiguo="u123", id\_nuevo="u987") validar\_firma(evento) && abrir\_operacion(evento) for servicio in servicios\_activos(usuario): ejecutar\_conector(servicio, evento) cerrar\_operacion\_si\_todos\_estados\_finales(evento.uuid) La seguridad se resuelve mediante autenticación entre servicios, listas de autorización por origen, control de permisos de ejecución y firma de mensajes. Los conectores no expondrán operaciones genéricas de administración, sino acciones acotadas y parametrizadas. Cada operación quedará asociada a un origen funcional, usuario técnico o proceso autorizado, y a un resultado verificable. Propuesta de mejora Añadir un modo “simulación” que calcule qué servicios se verían afectados antes de ejecutar el cambio real. Esta mejora facilita validaciones previas y reduce errores operativos sin comprometer el desarrollo principal. REQUISITO: II.1.1.2. Cambios de nombre de centro (TRA2) Requerimiento EducaMadrid Desarrollar un sistema que permita cambiar el nombre de un centro dentro de la plataforma EducaMadrid y propagar este cambio a todos los aplicativos asociados. El cambio de nombre debe incluir la actualización de todas las cuentas institucionales asociadas y, en algunos casos, la modificación de URLs de servicios. Requisitos Funcionales:

- Cambio de Nombre del Centro:
o El sistema debe permitir cambiar el nombre del centro en todos los aplicativos asociados. o El cambio de nombre debe propagarse automáticamente a todos los aplicativos sin intervención manual.
- Actualización de Cuentas Institucionales:
o Todas las cuentas institucionales asociadas al centro deben actualizarse con el nuevo nombre. o La información existente en las cuentas (contactos de correo electrónico, ficheros en el cloud, grupos de empieza, etc.) debe mantenerse intacta y asociada a las nuevas cuentas.


- Modificación de URLs:
o En algunos aplicativos (por ejemplo, aulas virtuales o WordPress), el cambio de nombre del centro puede implicar la modificación de la URL del servicio. o El sistema debe gestionar estas modificaciones de URL de manera segura y eficiente.
- Seguridad en Comunicaciones:
o Las comunicaciones entre los aplicativos para iniciar el cambio de nombre deben ser seguras. o Implementar medidas de seguridad como cifrado de datos y autenticación robusta.
- Autonomía de los Aplicativos:
o Cada aplicativo debe realizar las modificaciones necesarias de manera autónoma. o Las modificaciones específicas en cada aplicativo deben ser gestionadas de manera independiente. Requisitos No Funcionales:
- Rendimiento: El sistema debe ser capaz de realizar el cambio de nombre y propagarlo a
todos los aplicativos en un tiempo razonable.
- Escalabilidad: El sistema debe ser escalable para manejar un gran número de centros y
aplicativos.
- Seguridad: Implementar medidas de seguridad robustas para proteger los datos durante el
proceso de cambio de nombre.
- Mantenimiento: El sistema debe ser fácil de mantener y actualizar.
Propuesta técnica de empresa_s El cambio de nombre de un centro tiene más impacto que una modificación textual: puede afectar a cuentas institucionales, grupos, rutas, URLs, alias, nombres visibles, calendarios, espacios compartidos y referencias guardadas en servicios que no comparten el mismo esquema de datos. La solución se plantea como una operación de renombrado coordinado, no como una edición directa en cada base de datos. El portal educativo actuará como punto de inicio de la solicitud. Antes de ejecutar el cambio, se realizará una validación de precondiciones: existencia del centro, autorización de la persona o proceso solicitante, ausencia de otra operación abierta sobre el mismo centro, comprobación de nombres reservados, detección de colisiones de URL y generación de un plan de ejecución. Este plan indicará qué componentes deben actuar: aulas virtuales si existe URL dependiente del nombre, WordPress para sitios de centro, Cloud para espacios compartidos, Mediateca para titularidad o etiquetas, DTIC, EMPieza, Seguimientos, Formularios y los demás servicios integrados. Cada aplicativo será autónomo en la modificación interna, pero recibirá una solicitud uniforme con el identificador estable del centro, nombre anterior, nombre nuevo, metadatos de operación y reglas de URL. La autonomía evita imponer una estructura común irrealista y permite que cada tecnología ejecute lo necesario: actualización de registros, recálculo de rutas, regeneración de cachés, cambio de alias o creación de redirecciones. Preparación: construcción del plan de cambio y detección de colisiones en cuentas, alias y URLs. Ejecución controlada: envío de solicitudes firmadas a los aplicativos, con orden de dependencias cuando haya relación entre URL, contenido y autenticación.


Compatibilidad: conservación de alias o redirecciones temporales cuando el cambio pueda afectar a enlaces existentes. Verificación: consulta posterior a cada servicio para confirmar que el nombre nuevo es visible y que los recursos siguen asociados al identificador estable del centro. El criterio técnico principal es distinguir entre “identidad estable” y “nombre visible”. El identificador interno del centro debe mantenerse como referencia maestra; el nombre se tratará como atributo mutable. Si una URL depende del nombre, se mantendrá una tabla de rutas históricas y redirecciones 301/302 según el caso, evitando enlaces rotos en webs de centro, recursos publicados o comunicaciones previas. Para la actualización de cuentas institucionales, el proceso conservará buzones, contactos, ficheros, permisos, grupos y relaciones. La operación no recreará cuentas si puede renombrarlas o actualizar alias de forma segura. En caso de sistemas que exijan recreación, se definirá un procedimiento con exportación, reasignación y comprobación posterior de elementos críticos. REQUISITO: II.1.1.3. Tareas tras el traslado del CPD (TRA3) Requerimiento EducaMadrid Estas tareas se derivan del proyecto de traslado del CPD previsto para el verano de 2026.
- Dar cobertura para facilitar un arranque y ejecución de manera segura y eficiente de todos
los servicios tras el traslado, incluyendo comprobaciones posteriores para asegurar el servicio una vez que empiece el curso.
- Garantizar que, tras el traslado, no haya afectación en el funcionamiento de los servicios
de la plataforma.
- Proporcionar información y soporte a los usuarios durante y después del traslado.
- Identificar y corregir cualquier problema o incompatibilidad que se encuentre como
consecuencia del traslado.
- Apoyar y asesorar al equipo de sistemas en sus tareas.
- Realizar paradas y arranques controlados de distintos servicios.
Para verificar los sistemas tras el traslado, es necesario que haya un script (Shell script) que verifique el estado de las máquinas de cada servicio después de trasladar cada servidor físicamente de CPD y que permita comparar los resultados con los datos tomados antes del traslado. El script debe verificar una serie de elementos críticos para asegurarse de que el servidor esté funcionando correctamente. Requisitos del Script
- Verificación de volúmenes montados
o El script debe verificar que todos los volúmenes montados estén funcionando correctamente o El script debe verificar que los volúmenes estén montados en el lugar correcto.
- Verificación de conexión a las bases de datos
o El script debe verificar que las conexiones a las bases de datos estén funcionando correctamente. o El script debe verificar que los datos de las bases de datos estén intactos.
- Verificación de integridad de las bases de datos
o El script debe verificar que las bases de datos estén intactas y no hayan sufrido daños durante la migración.


o El script debe verificar que los datos de las bases de datos estén consistentes.
- Verificación de integridad del código de los distintos aplicativos
o El script debe verificar que el código de cada aplicativo esté intacto y no haya sufrido daños durante la migración. o El script debe verificar que el código esté actualizado y no haya errores.
- Verificación de paquetes del sistema
o El script debe verificar que los paquetes del sistema estén actualizados y no haya errores. o El script debe verificar que los paquetes estén instalados correctamente.
- Verificación de funcionamiento de los aplicativos
o El script debe verificar que los aplicativos estén funcionando correctamente. o El script debe verificar que los usuarios puedan acceder a los distintos aplicativos sin problemas.
- Verificación de conexiones a máquinas de otros servicios
o El script debe verificar que las conexiones a máquinas de otros servicios estén funcionando correctamente por los puertos que les corresponden según cada aplicativo. o El script debe verificar que los datos de los servicios estén intactos.
- Verificación del funcionamiento del cron
o El script debe verificar que el cron de cada aplicativo esté funcionando correctamente. o El script debe verificar que las tareas del cron estén completándose correctamente.
- Verificación de otros elementos
o El script debe verificar que otros elementos críticos estén funcionando correctamente, como:  Servidores de correo electrónico  Servidores de DNS  Servidores de LDAP  Servidores de conversión  Servidores de generación de subtítulos  Servidores de IA  otros Requisitos
- Tecnologías utilizadas
o El script deberá basarse en un lenguaje de Shell Scripting como Bash. o El script debe utilizar herramientas de verificación como df, ls, ps, netstat, etc.
- Documentación
o El script debe incluir documentación para explicar cómo funciona y qué elementos verifica. o La documentación debe estar escrita en un lenguaje claro y conciso. Propuesta técnica de empresa_s TRA3 se aborda como una verificación técnica de continuidad de servicio posterior al traslado físico del CPD previsto para verano de 2026. El objetivo es disponer de evidencias comparables antes y después del traslado, no solo comprobar que una máquina responde. Para ello se propone un kit de verificación compuesto por scripts Bash, ficheros de inventario por servicio, pruebas de conectividad, comprobaciones de integridad y salidas en formato legible y procesable.


Fecha: 21/05/2026

Antes del traslado se ejecutará una línea base por servidor y servicio. Esta línea base incluirá volúmenes montados, rutas esperadas, puertos activos, procesos críticos, versiones de paquetes relevantes, conectividad con bases de datos, conectividad con LDAP, estado de cron, permisos clave, checksums de código desplegado y pruebas funcionales HTTP/HTTPS cuando el servicio disponga de endpoint. Tras el traslado se ejecutará el mismo conjunto de pruebas y se compararán resultados, clasificando las diferencias como esperadas, advertencias o incidencias. El script no será un único bloque rígido difícil de mantener, sino una herramienta modular. Cada servicio tendrá un fichero de definición con sus checks: bases de datos a probar, puertos esperados, rutas de código, volúmenes, endpoints y tareas cron. Así se evita editar el script principal cada vez que se añade un servicio o cambia una ruta. La salida se generará en consola para intervención rápida y en JSON/CSV para su archivo, comparación y análisis posterior. ./em-check.sh --servicio mediateca --fase pre -- salida /var/log/em-check/pre- mediateca.json ./em-check.sh --servicio mediateca -- fase post --comparar /var/log/em-check/premediateca.json RESULTADO: OK=42 WARN=2 ERROR=0 \| diferencias esperadas: cambio de IP interna Las comprobaciones de bases de datos incluirán conexión con credenciales de solo lectura cuando sea posible, ejecución de consulta mínima, validación de esquema esperado y comprobación de latencia. Para integridad de código se utilizarán checksums de directorios críticos excluyendo cachés, logs y ficheros temporales. Para paquetes del sistema se compararán versiones de paquetes relevantes y estado de servicios systemd. Para cron se comprobará existencia, permisos, última ejecución y ausencia de errores recientes en logs. La verificación de aplicativos se diseñará con pruebas sintéticas de bajo impacto: acceso a portada, login técnico cuando exista usuario de prueba autorizado, consulta de endpoint de salud, subida de fichero de prueba en entornos habilitados o consulta de recursos públicos. Las pruebas que puedan modificar datos estarán desactivadas por defecto y requerirán parámetro explícito. Bloque de verificación Ejemplos de comprobación Criterio de aceptación Sistema df, mount, systemctl, permisos Coincidencia con línea base o de rutas, espacio disponible. diferencia justificada. Red Puertos internos, DNS, LDAP, Conectividad por puerto y correo, conversión, IA, latencia dentro de umbrales. subtítulos. Datos Conexión DB, consulta Conexión válida y esquema mínima, integridad básica, accesible sin errores. usuario correcto. Aplicación Endpoint HTTP, proceso, cron, Servicio operativo y sin logs recientes. errores críticos posteriores al arranque.

REQUISITO: II.1.1.4. Adaptación de interfaz para compatibilizar modo oscuro y claro (TRA4)

Requerimiento EducaMadrid Mantener los estilos de todos los aplicativos de la plataforma y aplicar la opción de un modo oscuro en cada uno de ellos, incluyendo la barra común superior. Objetivos Página 56 de 192


- Mantenimiento de los estilos y solución a problemas de accesibilidad, incluso tras
evoluciones de aplicativos.
- Implementar un modo oscuro en todos los aplicativos.
- Asegurar una experiencia de usuario coherente y estéticamente agradable en modo
oscuro. Alcance
- Análisis de los estilos actuales.
- Diseño de la interfaz de usuario en modo oscuro.
- Implementación del modo oscuro en todos los aplicativos bajo opción.
- Ajustes en la barra común superior.
Requisitos Funcionales
- Modo Oscuro
o Interfaz de Usuario: Diseño legible y estéticamente agradable. o Contraste: Adecuado entre texto y fondo. o Elementos de Interfaz: Adaptación de botones, iconos, etc. o Transiciones Suaves: Cambio entre modos claro y oscuro.
- Aplicativos
o Aulas Virtuales, Mediateca, WordPress, DTIC, Cloud, Empieza, Videoconferencias y otros: Aplicar modo oscuro a todas las vistas y componentes.
- Barra Común Superior
o Estilos: Adaptación al modo oscuro. o Iconos y Texto: Ajuste para legibilidad. o Funcionalidad: Accesibilidad y funcionalidad mantenidas. Requisitos No Funcionales
- Usabilidad
o Experiencia de Usuario: Intuitiva y agradable. o Accesibilidad: Cumplimiento con WCAG.
- Rendimiento
o Tiempo de Carga: Minimizar impacto. o Optimización: Recursos optimizados. Propuesta técnica de empresa_s La compatibilidad entre modo claro y oscuro debe resolverse como un sistema de diseño transversal, no como un conjunto de parches CSS independientes por aplicación. La propuesta parte de definir tokens visuales comunes: color de fondo, superficie, texto principal, texto secundario, borde, foco, enlaces, avisos, errores, éxito, iconografía y estados interactivos. Cada aplicativo traducirá esos tokens a su tecnología concreta, conservando su interfaz propia pero alineada con la imagen común de EducaMadrid y con la barra superior compartida. La solución contempla un inventario inicial de componentes: cabeceras, menús, formularios, tablas, botones, tarjetas, modales, mensajes de error, selectores, pies, buscadores, iconos y elementos de navegación. Sobre ese inventario se definirá una matriz de contraste para modo claro y modo oscuro, verificando legibilidad y accesibilidad. El cambio entre modos se implementará preferentemente mediante atributo raíz, por ejemplo data-theme="dark", variables CSS y carga diferida de recursos cuando resulte necesario.


Para evitar impacto en rendimiento, no se duplicarán hojas de estilo completas si puede resolverse con variables. Los iconos se adaptarán mediante SVG con currentColor o variantes controladas. Las imágenes institucionales se tratarán con versiones adecuadas o contenedores que garanticen contraste. La barra común superior incorporará los mismos tokens y un comportamiento estable en todos los aplicativos, de modo que el usuario perciba continuidad al moverse entre servicios. El modo se podrá activar por preferencia de usuario, preferencia del navegador o configuración del servicio, según lo permita cada aplicativo. Los formularios conservarán estados de foco visibles en ambos modos, requisito crítico para accesibilidad por teclado. Los mensajes de aviso y error no dependerán solo del color; se apoyarán en icono, texto y contraste suficiente. Las tablas alternarán filas y cabeceras con tokens específicos para no perder lectura en pantallas de baja calidad. Las pruebas incluirán navegación real por páginas representativas y validación automática de contraste en componentes clave. Un ejemplo de implementación en una aplicación PHP con frontend clásico sería incorporar un fichero de variables común y adaptar las reglas existentes progresivamente. No se sustituye toda la interfaz: se identifican estilos con valores fijos y se reemplazan por variables. Así se reduce el riesgo y se permite convivir con código histórico. :root { -- em-bg:#ffffff; --em -text:#1f1f1f; --em-link:#005ea8; } \[data-theme="dark"\] { -- em-bg:#111827; --em -text:#f5f7fa; --em-link:#8cc8ff; } .em-header { background:var(--em-bg); color:var(--em -text); }

REQUISITO: II.1.1.5. Mejoras y mantenimiento en SSO (TRA5)

Requerimiento EducaMadrid Integración del SSO: Integración del sistema de Single Sign- On (SSO) en distintos aplicativos de la plataforma, así como la creación de un sistema de detección de cierre de sesión en el aplicativo "Avisos". Doble factor de autenticación (2FA): Implementar un sistema de doble factor de autenticación (2FA) en los distintos aplicativos de la plataforma conectados con el SSO y en el correoweb, que no se encuentra conectado al SSO. El sistema debe funcionar con dispositivos móviles y/o correo electrónico y será optativo para los usuarios. Propuesta técnica de empresa_s TRA5 combina dos necesidades relacionadas pero distintas: integrar nuevos aplicativos con el SSO existente y mejorar el cierre de sesión transversal, además de introducir 2FA optativo en SSO y correoweb. La solución se plantea en torno a flujos de autenticación consistentes, tokens con vida útil controlada, validación de sesión centralizada y experiencia de usuario homogénea en servicios conectados y no conectados al SSO. Para nuevas integraciones, cada aplicativo incorporará un módulo de autenticación compatible con el SSO de EducaMadrid. El acceso a una zona protegida redirigirá al SSO, recibirá un token o aserción validable, creará sesión local con los mínimos atributos necesarios y aplicará reglas de


Fecha: 21/05/2026

autorización propias del servicio. La sesión local no será una copia indefinida de la sesión central: tendrá caducidad, validación periódica y capacidad de cierre remoto mediante el mecanismo definido en Avisos. El componente de detección de cierre de sesión en Avisos actuará como punto ligero de comprobación. Los aplicativos podrán consultarlo para saber si la sesión SSO sigue activa. Si el usuario ha cerrado sesión en el SSO, el aplicativo invalidará su sesión local, limpiará cookies propias y redirigirá al inicio de sesión. Para reducir carga, la comprobación podrá cachearse durante intervalos breves y ajustables, sin comprometer la coherencia de seguridad. Flujo Decisión técnica Control de seguridad Entrada a aplicativo Redirección al SSO si no hay Validación de origen y retorno sesión local válida. permitido. Recepción de token Validación de firma, Rechazo de tokens expirados caducidad, audiencia y o no destinados al servicio. emisor. Sesión local Creación con atributos Cookie segura, HttpOnly, mínimos y renovación SameSite y expiración. controlada. Cierre SSO Consulta a Avisos e Evita sesiones huérfanas tras invalidación local si procede. logout central.

El 2FA se implementará con un diseño gradual y optativo por usuario, centro o rol. El método TOTP será el principal para usuarios que utilicen aplicaciones móviles autenticadoras, y el correo alternativo verificado será el mecanismo complementario. La configuración se realizará desde SSO y será reutilizable por correoweb. EMPieza ofrecerá la interfaz de gestión para usuarios y cuentas institucionales, mientras ConsultasLDAP permitirá la administración por perfiles autorizados. El flujo de cambio de configuración de 2FA exigirá confirmación adicional para evitar secuestros de cuenta. Por ejemplo, si un usuario desea cambiar su correo alternativo, se le pedirá un código TOTP vigente o una verificación equivalente. Las opciones de 2FA se mostrarán solo en los centros y roles definidos, permitiendo una implantación por fases sin afectar a toda la comunidad educativa desde el primer día. Para correoweb, al no estar conectado al SSO, se replicará el flujo visual y funcional de segundo factor: tras contraseña válida se solicitará el código TOTP o el código enviado al correo alternativo. El backend consultará la configuración común de 2FA por usuario, evitando mantener configuraciones divergentes entre correo y SSO. Propuesta de mejora Incorporar códigos de recuperación de un solo uso generados bajo demanda y visibles una única vez. Es una mejora de seguridad y soporte que reduce bloqueos de usuarios sin requerir una plataforma compleja adicional. REQUISITO: II.1.1.6. Aplicativo API (TRA6) Requerimiento EducaMadrid


Desarrollo del aplicativo "API", cuyo objetivo es gestionar y servir APIs de manera segura y eficiente. El aplicativo se desarrollará utilizando el mismo framework que EducaMadrid está implantando y se centrará en la seguridad, accesibilidad y funcionalidad. Propuesta técnica de empresa_s El aplicativo API se concibe como un catálogo y punto de gobierno de APIs de EducaMadrid , con capacidad adicional para alojar APIs propias cuando sea conveniente. Su valor técnico está en ordenar el ecosistema de integraciones: documentar qué API existe, a qué servicio pertenece, si es pública o privada, qué parámetros acepta, qué respuestas devuelve, quién puede utilizarla y bajo qué condiciones de seguridad. La aplicación se desarrollará en PHP sobre el framework implantado para nuevos aplicativos de EducaMadrid, manteniendo coherencia con las prácticas internas de desarrollo, autenticación, estilos y despliegue. El acceso de administración se restringirá mediante LDAP ADM. La parte de documentación sensible podrá residir en backend no expuesto a internet, de forma que se diferencie entre documentación pública, documentación interna y configuración técnica de acceso a servicios o bases de datos. El modelo de datos del catálogo incluirá entidades para servicio, API, versión, endpoint, método, parámetros, ejemplos, respuestas, clasificación de exposición, propietario funcional, propietario técnico, estado de ciclo de vida y dependencias. La gestión de versiones evitará sobrescribir documentación histórica: una API podrá estar en borrador, vigente, obsoleta o retirada. Esto permite preparar cambios sin romper integraciones existentes. Documentación estructurada con ejemplos de petición y respuesta, no solo campos de texto libre. Control de APIs privadas para que no aparezcan en vistas públicas ni se expongan rutas internas. Gestión de permisos por rol: administrador global, mantenedor de servicio, lector técnico y auditor. Separación entre catálogo de documentación y ejecución de APIs alojadas. Protecciones frente a inyección SQL, XSS, CSRF, enumeración de endpoints y fuga de mensajes de error. Cuando el aplicativo sirva APIs directamente, cada API se implementará como módulo independiente, con validación de entrada, control de autorización y registro de uso. Las APIs de backend que accedan a datos sensibles no se expondrán directamente si no es necesario; se utilizarán rutas internas, tokens de servicio y consultas parametrizadas. Las APIs de frontend estarán limitadas a datos públicos o protegidos por sesión validada. La API solicitada para consulta de datos de usuarios desde el aplicativo de innovación y formación se resolverá como endpoint específico con contrato cerrado: parámetros permitidos, datos devueltos mínimos, paginación si procede, control de tasa y auditoría. Se evitarán consultas amplias que permitan enumerar usuarios. Por ejemplo, se devolverá solo la información necesaria para el caso funcional autorizado y se registrará el consumidor que realiza la llamada. GET /api/v1/usuarios?uid=xxxx Authorization: Bearer \<token- de- servicio\> Respuesta 200: { "uid":"xxxx", "centro":"28000000", "roles":\["docente"\] } Propuesta de mejora


Fecha: 21/05/2026

Añadir generación automática de una especificación OpenAPI para las APIs alojadas o documentadas con suficiente detalle. Esta mejora facilita pruebas, clientes futuros y validación técnica sin imponer un cambio funcional complejo. REQUISITO: II.1.1.7. Securización LDAP Plano, BBDD PostgreSQL y MySQL (TRA7) Requerimiento EducaMadrid Implementación de medidas de seguridad adicionales y la optimización de la Base de Datos "ldap plano". Además, se requiere un cambio de usuarios en todas las bases de datos PostgreSQL y MySQL de la plataforma, así como la actualización de datos en la configuración de cada aplicativo. Propuesta técnica de empresa_s TRA7 se trata como una actuación de endurecimiento y operación segura sobre dos ámbitos: la base de datos “ldap plano” y la rotación periódica de usuarios y contraseñas en bases de datos PostgreSQL y MySQL, incluyendo la actualización coordinada de configuraciones de aplicativos. El objetivo es reducir exposición, mejorar rendimiento y evitar credenciales estáticas mantenidas durante largos periodos. La primera fase será de diagnóstico. Se revisarán permisos, usuarios existentes, privilegios efectivos, conexiones autorizadas, cifrado de comunicaciones, exposición de puertos, consultas pesadas, índices, tamaño de tablas, bloqueos y logs de error. Sobre “ldap plano” se analizarán patrones de lectura y escritura para proponer medidas de optimización que no alteren la semántica del servicio. Las acciones de seguridad se aplicarán con respaldo y ventana controlada cuando puedan afectar a producción. Para la rotación de credenciales de PostgreSQL y MySQL se propone un procedimiento en dos pasos que reduzca indisponibilidad. Primero se crea el nuevo usuario o se cambia la credencial manteniendo temporalmente compatibilidad, se actualiza la configuración del aplicativo, se valida conexión y se despliega. Después se revoca el usuario anterior cuando se confirme que no existen conexiones activas legítimas. Este patrón evita cortes por desincronización entre base de datos y aplicación.

Control Aplicación práctica Evidencia Mínimo privilegio Usuarios por aplicativo con Listado de grants permisos estrictamente antes/después. necesarios. Rotación Cambio periódico de usuarios Acta técnica de rotación y y contraseñas con validación pruebas de conexión. previa. Cifrado Preferencia por conexiones Parámetros de conexión y TLS cuando el entorno lo prueba de canal. permita. Rendimiento Índices y consultas críticas Comparativa de tiempos y sobre ldap plano. plan de ejecución. Configuración Secretos fuera de repositorios Hash de ficheros y ubicación y backups de configuración. segura de secretos.

La actualización de configuración se hará mediante plantillas y variables de entorno o almacén de secretos cuando esté disponible. En aplicativos históricos que dependan de ficheros locales, se


Fecha: 21/05/2026

realizará copia previa, sustitución controlada, validación de sintaxis y reinicio ordenado si es necesario. En todos los casos se registrará qué versión de configuración quedó activa y cómo revertirla. La optimización de “ldap plano” (bbdd PostgreSQL) se abordará sin comprometer su función como fuente de consulta. Se identificarán columnas de filtrado frecuentes, se revisarán índices, se propondrán particiones o vistas si proceden y se programarán tareas de mantenimiento de estadísticas. Los cambios se validarán con consultas representativas para evitar mejoras aparentes que perjudiquen casos reales de uso. Propuesta de mejora Incluir un verificador automático de secretos expuestos en repositorios y ficheros de configuración antes de cada despliegue. Es una mejora de bajo coste que previene fugas accidentales de credenciales. REQUISITO: II.1.1.8. Calendario escolar (TRA8) Requerimiento EducaMadrid Creación y gestión de dos calendarios en la cuenta institucional de cada centro educativo: "Calendario Escolar" y "Calendario de Centro". Estos calendarios deben cumplir con ciertos criterios de acceso, alimentación de eventos y sincronización para asegurar una gestión eficiente y sin duplicados de eventos. Propuesta técnica de empresa_s TRA8 propone crear y gestionar dos calendarios diferenciados en la cuenta institucional de cada centro: “Calendario Escolar”, alimentado por administradores de EducaMadrid con eventos oficiales, y “Calendario de Centro”, alimentado por el propio centro y disponible en solo lectura para profesorado y alumnado. La clave técnica es distinguir claramente titularidad, permisos, sincronización y prevención de duplicados. El aprovisionamiento de calendarios se ejecutará mediante un proceso idempotente por centro. Si el calendario no existe, se crea con nombre, descripción, permisos y marca interna. Si existe, se verifica que conserva la configuración obligatoria y se corrige cuando sea necesario. Para impedir eliminaciones no deseadas, el sistema realizará comprobaciones periódicas y recreará o restaurará calendarios conforme a las reglas definidas, siempre dejando evidencia de la actuación. El “Calendario Escolar” tendrá permisos de solo lectura para cuentas institucionales y será alimentado desde los eventos oficiales publicados por la Comunidad de Madrid. Los administradores de EducaMadrid gestionarán altas, modificaciones y bajas de eventos. El “Calendario de Centro” tendrá permisos de escritura para la cuenta o roles autorizados del centro y lectura para profesores y alumnos. La solución evitará que usuarios no autorizados modifiquen o eliminen calendarios obligatorios. Para la sincronización con aulas virtuales y cuentas de centro se utilizará una clave única de evento compuesta por origen, centro, calendario, identificador externo y fecha de última modificación. Antes de crear un evento se comprobará si ya existe un evento con esa clave o con una huella equivalente. Si existe, se actualiza; si no existe, se crea. Este mecanismo evita duplicados incluso cuando se repite una sincronización o se produce una recuperación tras error.

Calendario Alimentación Permisos Control contra duplicados


Fecha: 21/05/2026

Calendario Escolar Administradores de Solo lectura para UID de evento oficial y EducaMadrid con cuentas huella de contenido. eventos oficiales. institucionales. Calendario de Centro educativo Lectura para UID por centro y Centro mediante cuenta o rol profesores y alumnos origen, con autorizado. del centro. actualización si cambia el evento. Sincronización con Proceso automático o Según integración Mapa de aulas conector específico. autorizada. correspondencia entre evento AV y evento calendario.

La gestión de conflictos se basará en reglas explícitas. Si un evento oficial cambia de fecha, se actualizará el evento existente y se dejará traza del cambio. Si el centro crea un evento con mismo título y fecha que un evento sincronizado, no se fusionará automáticamente salvo coincidencia de identificador; se marcará como posible duplicado para revisión o se aplicará una regla de prioridad previamente acordada. Esta prudencia evita borrar eventos legítimos del centro. La actualización en tiempo real se interpretará como propagación inmediata dentro de las capacidades de cada sistema, complementada con reconciliación periódica. Esta combinación es más robusta que depender solo de eventos instantáneos: si una notificación falla, la tarea de reconciliación detecta diferencias y las corrige. Los logs de sincronización permitirán conocer cuántos eventos se han creado, actualizado, omitido por duplicado o rechazado por conflicto. Propuesta de mejora Los eventos de centro o del calendario escolar se mostrarán de un modo identificativos únicos para no confundirlos con el resto.
##### 1.3.1.1.2. APARTADO: MEJORAS Y MANTENIMIENTO DE LAS AULAS VIRTUALES (AV)
Propuesta técnica de empresa_s

Enfoque general de la solución para Aulas Virtuales La solución se plantea como una evolución controlada de dos ecosistemas Moodle con criticidad alta: Multisite, orientado a aulas virtuales de centros, y MoodleMisc, destinado a usos específicos o no encajables en el modelo de centro. La premisa técnica es que cualquier cambio debe convivir con una plataforma de tamaño muy superior al de una instalación Moodle convencional: muchas instancias, bases de datos con tablas históricas de gran tamaño, un filepool de moodledata con millones de objetos, tareas cron intensivas, picos de uso al inicio de curso y una dependencia directa de sistemas corporativos como SSO, LDAP, Raíces, Portal educativo, Avisos, nube de EducaMadrid y servicios de IA alojados en infraestructura propia. Para evitar que la memoria sea una colección de funcionalidades aisladas, todos los apartados AV se resuelven bajo una arquitectura de operación común: despliegues reproducibles, compatibilidad estricta con la API pública de Moodle, ausencia de modificaciones en core, pruebas con copias anonimizadas de gran volumen, monitorización técnica antes y después del cambio, y separación clara entre procesos interactivos y procesos pesados en segundo plano. En Moodle a gran escala no basta con que una funcionalidad funcione; debe hacerlo sin bloquear tablas, sin disparar el tamaño de la base de datos, sin saturar moodledata, sin romper cachés distribuidas y


Fecha: 21/05/2026

sin introducir tareas cron que compitan con procesos críticos de curso, matriculación, backup o calificación. Eje técnico Aplicación en AV Resultado esperado Actualización segura Ensayos completos en Cambios aplicados con preproducción, scripts mínima interrupción y idempotentes, ventanas trazabilidad técnica. nocturnas, validación por islas y plan de reversión. Escalabilidad Moodle Optimización de cron, colas, Comportamiento estable en locks, cachés, consultas, alta concurrencia y datos sesiones, filepool y procesos masivos. CLI. Integración corporativa SSO, SAML/WebAuth, Raíces, Experiencia unificada y Avisos, Portal, nube, LDAP y control de identidad sin APIs securizadas. duplicidades. Seguridad y ENS HTTPS, Reducción de superficie de validación/sanitización, ataque y control de permisos Moodle, auditoría, operaciones sensibles. logs, mínimos privilegios y aislamiento de datos. Mantenibilidad Plugins versionados, Evolución sostenible hacia configuración externa, futuras versiones de Moodle. documentación operativa, pruebas automatizadas y sin cambios en core.

Principios de diseño aplicados a Moodle de gran escala La solución prioriza decisiones que evitan deuda técnica. Los desarrollos se implementarán mediante plugins locales, tareas programadas, servicios web, observers, capacidades y componentes estándar de Moodle. Las adaptaciones se aislarán por funcionalidad y se acompañarán de pruebas unitarias, behat o pruebas funcionales equivalentes cuando proceda. En consultas sobre tablas críticas -por ejemplo, context, role\_assignments, grade\_grades, question, question\_references, files, task\_adhoc o logstore\_standard\_log- se revisarán índices, cardinalidad, filtros y planes de ejecución para impedir barridos completos sobre bases de datos grandes. En moodledata se tratará el almacenamiento como un componente crítico: no se programarán operaciones masivas de lectura/escritura sin control de ritmo; las eliminaciones se harán por lotes, con comprobación de referencias y limpieza diferida; las tareas de backup se organizarán para no competir con picos de subida de archivos; y las integraciones que generen contenidos -IA, RAG, OfflineQuiz, eXeLearning- incluirán límites de tamaño, retención y trazabilidad. El objetivo es que los cambios sean compatibles con la realidad operativa de EducaMadrid: muchos centros, muchos cursos, mucho histórico y necesidades de soporte rápido. REQUISITO: II.1.2.1. Actualización de la Plataforma Moodle (AV1)

Requerimiento EducaMadrid


Realizar la actualización de manera segura y sin interrupciones en el servicio: Se deberá realizar la actualización de manera planificada, utilizando un script de actualización que se ejecute fuera de horas pico. Se recomienda realizar una copia de seguridad de la base de datos y los archivos de configuración antes de realizar la actualización. Propuesta técnica de empresa_s La actualización anual de Moodle se ejecutará como un proceso industrializado y no como una actuación manual sobre servidores. El primer paso será construir una línea base de versión para Multisite y MoodleMisc: versión actual, versión objetivo, plugins instalados, temas activos, modificaciones existentes, dependencias de PHP, tareas cron, integraciones y estado de las bases de datos. Con esa línea base se generará una matriz de compatibilidad que permitirá decidir la versión segura más adecuada, no necesar iamente la más reciente si existiera incompatibilidad relevante con un plugin crítico.

El cambio se ensayará en un entorno de preproducción con copia representativa de base de datos y moodledata. En instalaciones grandes, las pruebas con una base de datos vacía no detectan el coste real de los upgrades: migraciones de esquemas, conversiones de datos del banco de preguntas, recalculo de cachés, índices nuevos o actualización de configuración pueden tardar horas. Por ello se medirá cada paso con tiempos, consumo de CPU, I/O de disco, crecimiento de logs y bloqueos detectados. El script de actua lización será idempotente, registrará el estado de cada instancia y podrá reanudarse con seguridad si una isla falla. En producción se aplicará una estrategia por islas o grupos de centros. La ventana de paso se programará en horario de bajo uso, con bloqueo controlado de acceso, copia previa de configuración y verificación posterior: versión, cron, tareas adhoc pendientes, integridad de plugins, acceso de usuarios, carga del tema, edición de curso, cuestionarios, libro de calificaciones, subida de archivo, mensajería y restauración de curso. La reversión no se basará únicamente en restaurar ficheros; incluirá criterio claro sobre cuándo restaurar BBDD, cuándo detener el avance y cómo preservar trazabilidad. Propuesta de mejora Incorporar un “informe de salud post -upgrade” por isla, con tiempos reales de migración, errores de cron, tareas pendientes y comprobaciones funcionales clave, para detectar degradaciones antes de extender el cambio al resto de aulas. REQUISITO: II.1.2.2. Actualización de PHP y sistema operativo (AV2)

Requerimiento EducaMadrid Actualizar la versión de PHP: Se deberá actualizar la versión de PHP a una versión segura y compatible con la plataforma y versión de Moodle utilizada. Esto incluye la actualización de los archivos de código y la configuración de PHP. Se recomienda utilizar la versión más reciente de PHP compatible con la plataforma. Evaluar la necesidad de subir la versión del sistema operativo: Se deberá evaluar la necesidad de subir la versión del sistema operativo para asegurarse de que esté compatible con la versión actualizada de PHP. Esto incluye la actualización de los archivos de configuración y la base de datos. Crear nuevos servidores completos si es necesario: Se deberá crear nuevos servidores completos si es necesario para asegurarse de que la plataforma esté disponible y accesible para los usuarios. Página 65 de 192


Propuesta técnica de empresa_s La actualización de PHP y del sistema operativo se abordará como una renovación de plataforma de ejecución, no solo como cambio de paquete. Se inventariarán extensiones PHP usadas por Moodle y plugins -intl, mbstring, xml, soap, zip, gd, curl, ldap, sodium, opcache, redis, pgsql o mysqli según entorno-, parámetros de FPM, límites de memoria, tamaño máximo de subida, timeouts, configuración de sesiones, certificados, librerías del sistema y herramientas CLI invocadas por cron o por scripts auxiliares. Cuando la subida de versión implique riesgo operativo, se crearán nuevos servidores completos y se probará el tráfico contra ellos con una estrategia de conmutación progresiva. El enfoque recomendado es generar imágenes o plantillas reproducibles, desplegar nodos paralelos, validar compatibilidad y mover tráfico mediante balanceadores. En Moodle con alta concurrencia, esta aproximación reduce la exposición frente a actualizaciones in- place y permite comparar métricas entre nodos antiguos y nuevos. Se ajustará OPcache con parámetros coherentes para Moodle y despliegues frecuentes: memoria suficiente, invalidación controlada en pasos a producción, JIT desactivado si no aporta beneficio real al patrón PHP de Moodle, y separación entre configuración web y CLI. Los procesos de cron, backups, borrados y tareas IA deben ejecutarse con límites diferentes a los del tráfico interactivo, porque un timeout razonable para una petición web puede ser insuficiente para una tarea programada de gran volumen. Validación técnica: php - m, php - i, comprobación de versión Moodle, ejecución de cron, prueba de subida de archivos grandes, sesiones, caché, autenticación y llamadas a servicios externos. Criterio de seguridad: solo versiones soportadas, paquetes del repositorio corporativo o repositorio autorizado, TLS actualizado y eliminación de módulos PHP no necesarios. Criterio de rendimiento: comparación antes/después de tiempos de respuesta, uso de FPM workers, tasa de errores 5xx, cola de cron y operaciones de lectura/escritura sobre moodledata. Propuesta de mejora Separar perfiles para tráfico web y tareas internas, evitando que procesos pesados consuman la misma bolsa de workers que los usuarios conectados.

REQUISITO: II.1.2.3. Actualización de aplicativo y complementos (AV3)

Requerimiento EducaMadrid
- Actualizar la versión de Moodle y todos sus complementos y temas: Se deberá actualizar
la versión de Moodle y todos sus complementos y temas a versiones actuales. Esto incluye la actualización de los archivos de código, la base de datos y los archivos de configuración.
- Mantener todas las funcionalidades y modificaciones ya implementadas: Se deberá
mantener todas las funcionalidades y modificaciones ya implementadas en la plataforma, asegurándose de que no se pierdan durante la actualización.
- Realizar la actualización de manera segura y sin interrupciones en el servicio: Se deberá
realizar la actualización de manera planificada, utilizando un script de actualización que se ejecute fuera de horas pico. Se recomienda realizar una copia de seguridad Propuesta técnica de empresa_s


Fecha: 21/05/2026

La actualización de complementos y temas se realizará con un catálogo vivo que identifique para cada componente: origen, versión instalada, versión disponible, criticidad, dependencia de Moodle, modificaciones locales, riesgos de seguridad, uso real y alternativa de retirada. En plataformas con muchas aulas, mantener plugins no usados aumenta superficie de ataque y coste de actualización; por ello se propondrá revisar su uso antes de subirlos de versión. Los temas institucionales se tratarán como software crítico. Se verificará compatibilidad con Boost, cambios de plantillas Mustache, AMD/ES modules, SCSS, iconografía, navegación, accesibilidad y comportamiento responsive. La actualización no debe limitarse a “que cargue la página”; debe comprobar edición de curso, banco de preguntas, libro de calificaciones, cuestionarios, tareas, modales, app móvil y páginas con usuarios invitados. Las modificaciones existentes se conservarán mediante ramas versionadas y parches explícitos. Si se detecta código local aplicado directamente sobre core o plugins de terceros, se encapsulará en plugins propios, callbacks, observers o renderers cuando sea técnicamente posible. Esto es especialmente importante para llegar a Moodle 5 y versiones posteriores con menor fricción y menor dependencia de parches manuales. Tipo de componente Tratamiento propuesto Control de calidad Core Moodle Actualización mediante CLI y Smoke test funcional, cron, script por isla. Revisión de tareas adhoc, logs y notas de versión y breaking rendimiento. changes. Plugins de terceros Compatibilidad, revisión de Pruebas de rol, permisos, mantenimiento, CVE y formularios, eventos y pruebas sobre datos reales. borrado. Plugins propios Refactorización mínima para PHPUnit/Behat cuando APIs soportadas, sin core proceda, revisión de hacks. seguridad y documentación. Tema institucional Adaptación visual y Revisión responsive, accesibilidad en claro/oscuro y contraste, navegación y baja resolución. componentes críticos.

Propuesta de mejora Añadir una ficha técnica por plugin con “decisión de ciclo de vida”: actualizar, sustituir, aislar, mantener temporalmente o retirar de forma planificada. REQUISITO: II.1.2.4. Mejoras de seguridad y rendimiento (AV4)

Requerimiento EducaMadrid

- Activar el antivirus ClamAV: Se deberá activar el antivirus ClamAV para proteger la
plataforma contra virus y malware.
- Modificar la presentación del proceso de análisis durante la subida de archivos: Se deberá
modificar la presentación del proceso de análisis durante la subida de archivos para informar al usuario que se realizará un análisis en busca de virus.
- Mejorar la seguridad para evitar la inserción de SCRIPTS en campos de tipo texto o
TEXTAREA: Se deberá mejorar la seguridad para evitar la inserción de SCRIPTS en campos de tipo texto o TEXTAREA, utilizando técnicas de validación y limpieza de datos.


- Corregir problemas con el banco de preguntas: se deberá aportar una solución al actual
problema de volumen en el banco de preguntas y realizar las adaptaciones necesarias para poder actualizar a la futura versión 5 con el nuevo formato de banco de preguntas.
- Implementar un sistema de coloreado de sintaxis para los principales lenguajes de
programación: Se deberá implementar un sistema de coloreado de sintaxis para los principales lenguajes de programación, utilizando técnicas de procesamiento de texto y renderizado de código. Propuesta técnica de empresa_s La activación de ClamAV se diseñará para no convertir la subida de archivos en un cuello de botella. En Moodle de gran tamaño, el antivirus debe integrarse con límites de tamaño, colas y mensajes claros para el usuario. Se validará el comportamiento con archivos pequeños, grandes, comprimidos y múltiples subidas simultáneas. La interfaz informará de que el fichero está siendo analizado, pero la operación debe evitar esperas indefinidas y dejar registros técnicos útiles si el motor no responde. La protección contra scripts en campos de texto y TEXTAREA se realizará respetando la política de formatos de Moodle. Se reforzarán validaciones de entrada, limpieza de HTML, uso de PARAM\_\* adecuados, sesskey, capability checks y escape de salida. No se aplicará una limpieza indiscriminada que rompa recursos docentes legítimos; se revisarán los puntos de entrada reales y se aplicarán reglas según contexto y rol. El problema de volumen en el banco de preguntas exige una actuación específica. Se analizarán tablas del subsistema de preguntas, categorías, referencias, versiones, intentos, uso real e histórico. La solución combinará limpieza de huérfanos, revisión de índices, paginación efectiva, búsqueda más selectiva y preparación para el nuevo modelo de Moodle 5. También se revisará el impacto de plugins de IA y OfflineQuiz, que pueden incrementar el número de preguntas generadas y sus metadatos. Para rendimiento general se revisarán consultas lentas, cachés MUC, Redis o backend equivalente, sesiones, locks, cron, tareas adhoc, backup/restore, generación de miniaturas, logs y procesos que accedan a moodledata. Se propondrán umbrales de alerta específicos: crecimiento de task\_adhoc, fallos de cron, tamaño de logstore, tiempo medio de backup, número de archivos en filepool, latencia de base de datos y errores de bloqueo. Propuesta de mejora Crear un cuadro de mando técnico de salud Moodle con señales tempranas de saturación: cola de cron, tareas fallidas, consultas lentas, locks, crecimiento de moodledata y tiempos de respuesta por endpoint crítico. También se realizará un estudio de posibilidad de actualizar las cachés de Moodle de APC al sistema REDIS definiendo una arquitectura de servidores paralela.

REQUISITO: II.1. 2.5. Integración con otros sistemas (AV5)

Requerimiento EducaMadrid
- Establecer conexión SAML con el aplicativo nube: Se deberá establecer una conexión
SAML con la nube de EducaMadrid para permitir la autenticación de usuarios y la integración de servicios.
- Establecer conexión WebAuth entre el aplicativo nube y las aulas virtuales: Se deberá
establecer una conexión WebAuth entre la nube de EducaMadrid y las aulas virtuales


moodlemisc y multisite para permitir la autenticación de usuarios y la integración de servicios.
- Integrar el Aula Virtual con Avisos: Se deberá integrar el Aula Virtual con el aplicativo Avisos
para permitir la notificación de eventos y la integración de servicios.
- Integrar el Aula Virtual con Raíces y el Portal educativo: Se deberá integrar el Aula Virtual
con Raíces y el Portal educativo para permitir la generación automática de cohortes y la inserción de alumnos y profesores en las aulas que les correspondan. Propuesta técnica de empresa_s La integración con nube, Avisos, Raíces y Portal educativo se planteará con contratos de servicio explícitos: autenticación, autorización, formato de datos, errores esperados, reintentos, trazabilidad y límites de consumo. En entornos de gran volumen, las integraciones deben ser tolerantes a fallos parciales; un problema puntual de un sistema externo no debe bloquear el acceso general a Moodle ni dejar procesos inconsistentes. La conexión SAML y WebAuth con la nube se diseñará para no duplicar identidades ni generar usuarios técnicos innecesarios. Se revisará el mapeo de atributos, persistencia de identificadores, expiración de sesiones, tratamiento de usuarios invitados, sincronización de datos del perfil y comportamiento en logout. Las integraciones con Avisos se implementarán mediante eventos Moodle y colas, evitando envíos síncronos desde pantallas críticas. Para Raíces y Portal educativo, la creación automática de cohortes y la inserción de alumnado y profesorado se ejecutará con procesos diferenciales. En lugar de recalcular todo el universo de usuarios, se aplicarán altas, bajas y cambios detectados, con registro de resultados por centro, curso y grupo. La operación deberá manejar duplicados, cambios de centro, usuarios sin correspondencia, inconsistencias temporales y picos de carga de inicio de curso. Definir identificadores maestros: usuario EducaMadrid, NIA cuando proceda, centro, enseñanza, grupo y curso Moodle. Implementar sincronizaciones por lotes con ventanas de ejecución y límites de concurrencia. Registrar trazabilidad funcional comprensible para soporte: qué se esperaba, qué se recibió y qué se aplicó. Aislar fallos: un centro con datos inconsistentes no debe detener la sincronización del resto. REQUISITO: II.1.2.6. Mejoras de interfaz y usuario (AV6)

Requerimiento EducaMadrid
- Mejorar la vista del libro de calificaciones en resoluciones bajas: Se deberá mejorar la vista
del libro de calificaciones en resoluciones bajas, utilizando técnicas de diseño y renderizado de texto.
- Permitir el desplazamiento horizontal de la tabla en el libro de calificaciones: Se deberá
permitir el desplazamiento horizontal de la tabla en el libro de calificaciones, utilizando técnicas de diseño y renderizado de texto.
- Crear un modo examen para utilizar con el navegador "Safe Exam Browser": Se deberá
crear un modo examen para utilizar con el navegador "Safe Exam Browser", utilizando técnicas de diseño y renderizado de texto. Propuesta técnica de empresa_s


La mejora del libro de calificaciones en resoluciones bajas se abordará como un problema de usabilidad con tablas densas, no como un simple ajuste CSS. Se revisará el comportamiento con muchos alumnos, muchas actividades, nombres largos, categorías anidadas y dispositivos de pantalla reducida. La solución aplicará desplazamiento horizontal controlado, cabeceras persistentes cuando sea viable, anchuras mínimas razonables, reducción de columnas auxiliares y foco visual sobre la celda editada. El modo examen con Safe Exam Browser se integrará respetando las configuraciones propias de Moodle y añadiendo ayudas para centros. Se validará activación por cuestionario, mensajes de acceso, comportamiento en roles, compatibilidad con plantillas institucionales y registro de eventos relevantes. No se convertirá en un bloqueo global del curso; será una opción configurable y verificable por el docente antes de publicar una prueba. Las mejoras de interfaz se probarán con perfiles reales: profesor que corrige desde portátil pequeño, docente que revisa calificaciones en monitor de aula, administrador que accede a informes extensos y alumnado en dispositivos diversos. Se prestará especial atención a accesibilidad, contraste, navegación por teclado y compatibilidad con tema claro/oscuro si el marco institucional lo requiere. Propuesta de mejora Incluir un “modo compacto” del libro de calificaciones activable por usuario, que reduzca densidad visual sin cambiar datos ni permisos, útil para portátiles de baja resolución. REQUISITO: II.1.2.7. Desarrollo y pruebas (AV7)

Requerimiento EducaMadrid Desarrollar un mecanismo para propagar cambios en la lista de centros que pueden usar la app de Aula Virtual para dispositivos móviles: Se deberá desarrollar un mecanismo para propagar cambios en la lista de centros que pueden usar la app de Aula Virtual para dispositivos móviles, utilizando técnicas de desarrollo y pruebas de software. Propuesta técnica de empresa_s El mecanismo para propagar cambios en la lista de centros que pueden usar la app móvil se diseñará como una fuente de configuración centralizada, versionada y cacheable. La lista no debe depender de cambios manuales en cada aula ni de despliegues completos para altas o bajas de centros. La solución publicará el estado de disponibilidad por centro, entorno y plataforma, con fecha de activación y trazabilidad de quién realizó el cambio. En un ecosistema Multisite, la app móvil puede sufrir problemas de cacheo o descubrimiento si los cambios no se propagan correctamente. Por ello se implementará invalidación controlada de caché y comprobaciones automáticas: centro visible, URL correcta, certificado válido, endpoint móvil accesible y autenticación compatible con SSO. Las pruebas incluirán centros activos, centros deshabilitados, cambios de URL y centros recién incorporados. El desarrollo se apoyará en pruebas de contrato sobre el formato de configuración que consume la app. Si mañana cambia el modo de exposición de centros o se añaden atributos, la compatibilidad se preservará mediante versionado del esquema y valores por defecto. REQUISITO: II.1.2.8. Mantenimiento y soporte (AV8)

Requerimiento EducaMadrid


- Mantener la recogida de datos estadísticos: Se deberá mantener la recogida de datos
estadísticos para permitir la evaluación de la plataforma y la identificación de áreas de mejora.
- Realizar la generación y eliminación de instalaciones de Aulas Virtuales Multisite: Se
deberá realizar la generación y eliminación de instalaciones de Aulas Virtuales Multisite para permitir la actualización de la plataforma y la eliminación de instalaciones obsoletas.
- automatizar un cambio de URL de las Aulas Virtuales para afrontar cambios de nombres
de centros. El sistema debe cambiar URL, cuentas administradoras, nombre del aula, etc.
- Tareas anuales de inicio de curso: cada curso escolar debe realizarse una serie de tareas
de mantenimiento y limpieza de la plataforma de cara al nuevo curso: backup de todos los cursos del año anterior (debe estar disponible para los usuarios), reinicio de cursos . Propuesta técnica de empresa_s El mantenimiento de las Aulas Virtuales combinará soporte funcional, operación técnica y tareas anuales de curso. La recogida de estadísticas se mantendrá con criterios de utilidad: accesos, cursos activos, actividad por tipo de módulo, uso de recursos, ocupación de moodledata, evolución de backup, número de usuarios matriculados, tareas de cron y errores. Se evitará recolectar datos que generen carga sin aportar información operativa. La generación y eliminación de instalaciones Multisite se automatizará con plantillas: creación de base de datos o esquema según arquitectura, configuración inicial, directorios de moodledata, URL, tema, plugins, tareas programadas, integración SSO, certificados si aplica, cuenta administradora y registro en inventario. La eliminación no será un borrado inmediato: pasará por fases de desactivación, retención, backup, verificación y purga para prevenir pérdida accidental. El cambio de URL por cambio de nombre de centro se resolverá con un procedimiento automatizado que actualice configuración Moodle, nombre visible, cuentas administradoras, enlaces internos, cachés, configuración de app móvil, SSO y referencias externas conocidas. En moodledata no se harán sustituciones masivas innecesarias; se analizarán las referencias reales y se usarán herramientas seguras para reemplazos en base de datos cuando proceda. Las tareas de inicio de curso se planificarán como una campaña: backup de cursos anteriores disponible para usuarios, reinicio de cursos, limpieza controlada, comprobación de cohortes, altas de nuevas aulas y monitorización reforzada durante los primeros días lectivos. El backup anual se ejecutará con ventanas y límites de concurrencia para no saturar disco, base de datos ni CPU. Propuesta de mejora Publicar un calendario técnico de “campaña de inicio de curso” con hitos de backup, reinicio, sincronización, pruebas de acceso y control de ocupación, facilitando coordinación con centros y soporte. REQUISITO: II.1.2.9. Otros (AV9)

Requerimiento EducaMadrid
- Actualizar los scripts de instalación paulatina por "islas" de nuevos plugins o
actualizaciones de los mismos: Se deberá actualizar los scripts de instalación paulatina por "islas" de nuevos plugins o actualizaciones de core.
- Actualizar los scripts de AV para que permitan un paso en producción programado de
madrugada de cambios en el tema de Moodle, limpiando caches: Se deberá actualizar los


Fecha: 21/05/2026

scripts de AV para que permitan un paso en producción programado de madrugada de cambios en el tema de Moodle, limpiando caches. Propuesta técnica de empresa_s Los scripts de instalación por islas se actualizarán para actuar sobre grupos controlados de aulas, con selección por centro, versión, estado, tamaño de base de datos, criticidad y dependencias. Esta granularidad permite iniciar cambios en islas de bajo riesgo, medir impacto real y ampliar progresivamente. Cada ejecución registrará versión anterior, versión nueva, comandos lanzados, duración, salida, errores, rollback disponible y validaciones realizadas.

Los pasos nocturnos de tema y core limpiarán cachés de forma ordenada. En Moodle, purgar cachés en instalaciones con muchos usuarios y muchos nodos puede provocar picos de CPU y latencia si todos los procesos regeneran caché a la vez. Por ello se aplicará precalentamiento selectivo de páginas críticas y coordinación con cachés compartidas. El despliegue evitará dejar nodos con versiones mixtas de código y caché incompatible. El sistema también controlará exclusiones: aulas en periodo de exámenes, centros con incidencia abierta, bases de datos en mantenimiento o nodos con métricas anómalas no entrarán en una oleada hasta su validación.

Fase Acción técnica Criterio de avance Preparación Inventario, bloqueo de versión, Sin dependencias críticas copia de configuración y pendientes. selección de islas. Ejecución Despliegue, upgrade CLI, Errores cero o aceptados con purga y precalentamiento de justificación. cachés. Validación Login, curso, tema, cron, logs, Pruebas superadas y métricas subida de archivo, estables. calificaciones. Expansión Siguiente oleada de centros. No hay regresiones en la oleada anterior. Propuesta de mejora Añadir un modo “dry -run” que simule qué aulas se verían afectadas, qué comandos se lanzarían y qué dependencias bloquearían el despliegue antes de tocar producción. REQUISITO: II.1.2.10. Plugin eXeLearning 3 (AV10)

Requerimiento EducaMadrid Adaptar el plugin de Exelearning para Moodle para que se ajuste a las necesidades actuales del sistema. El objetivo de esta adaptación es asegurar la compatibilidad con la versión 3 de Exelearning y garantizar la seguridad y estabilidad del sistema.

Propuesta técnica de empresa_s La adaptación del plugin eXeLearning se realizará garantizando compatibilidad con eXeLearning 3 y 4, comunicación segura y operación en servidores propios. La integración utilizará HTTPS, validación de certificados, tokens o credenciales con mínimos privilegios y control de tiempo de


espera. Cuando eXeLearning no esté disponible, Moodle no debe quedar bloqueado: el plugin mostrará un mensaje claro, registrará la incidencia y permitirá reintentos sin duplicar recursos. La comunicación entre Moodle y eXeLearning se encapsulará en una capa de servicio para aislar cambios futuros de API. Se controlarán tamaños máximos de paquetes, formatos aceptados, tipos MIME, codificación y errores de conversión. Dado que los recursos generados pueden terminar en moodledata, se aplicará validación previa para evitar objetos corruptos o excesivamente grandes. El plugin se desarrollará con PHP 8 compatible con la versión Moodle objetivo, sin llamadas obsoletas y con configuración administrable por aula o por plataforma según proceda. La documentación incluirá parámetros de conexión, pruebas de salud, mensajes de error y procedimiento de actualización. Propuesta de mejora Incorporar una prueba automática de conectividad desde la administración del plugin que verifique URL, certificado, autenticación, versión de eXeLearning y creación de un recurso de prueba no persistente. REQUISITO: II.1.2.11. IA en Moodle - Generador de preguntas (AV11)

Requerimiento EducaMadrid Se solicita la creación de un plugin para Moodle para la generación de preguntas de tipo opción múltiple con inteligencia artificial. Propuesta técnica de empresa_s El generador de preguntas se implementará como un plugin Moodle restringido a profesores del curso mediante capabilities. La llamada al modelo VLLM alojado en servidores de EducaMadrid se realizará por HTTPS, con configuración del modelo administrable y posibilidad de cambio sin redespliegue. El plugin generará preguntas de opción múltiple con cuatro respuestas, una correcta, y las importará en formato GIFT al banco de preguntas del curso. La generación será asíncrona. El usuario enviará la solicitud, el sistema creará una tarea adhoc o una cola controlada y mostrará barra de progreso. Si el modelo falla o devuelve una estructura inválida, se aplicarán hasta diez intentos con validación estricta: número de opciones, unicidad de respuesta correcta, ausencia de HTML peligroso, longitud máxima y formato GIFT válido. Al finalizar, el profesor recibirá notificación interna con enlace al banco de preguntas. En instalaciones grandes, el riesgo no está solo en llamar a la IA, sino en multiplicar preguntas sin control y agravar el volumen del banco. Por ello se añadirá límite configurable por usuario, curso y franja temporal; registro de historial con usuario, fecha, modelo, pregunta, opciones y resultado; y marcado con icono IA indicando el modelo utilizado. La importación al banco evitará categorías genéricas masivas, proponiendo categorías específicas por curso o tema.

Propuesta de mejora Se notificará por correo al docente que crea las preguntas una vez generadas mostrando un enlace independiente por cada una de ellas para ser revisadas. También se incorporará un selector de la categoría donde se quieran integrar las preguntas generadas. REQUISITO: II.1.2.1 2. IA en Moodle - Generador de textos (AV12)

Requerimiento EducaMadrid Página 73 de 192


Al cumplir con estos requisitos para la Adaptación del Plugin de IA de generación de textos en Moodle, el plugin de IA en Moodle debe ser capaz de proporcionar una experiencia de usuario segura, eficiente y flexible para los profesores de EducaMadrid. Propuesta técnica de empresa_s El generador de textos se integrará en el editor de Moodle para que el profesor pueda solicitar contenidos y decidir si los inserta. La respuesta de VLLM se recibirá en Markdown y se convertirá a HTML seguro antes de incorporarse al editor. Se aplicará limpieza de HTML, eliminación de scripts, control de enlaces, límites de longitud y marcado visible con icono IA y modelo utilizado. El formulario de generación permitirá seleccionar estilo, longitud, creatividad e idioma. Estas opciones se traducirán a prompts de sistema y usuario controlados desde configuración, evitando que cada pantalla improvise instrucciones. Se registrará el historial para administradores del aula virtual: usuario, texto solicitado, respuesta, modelo, fecha, curso y estado. El historial será consultable con permisos adecuados y con retención definida para no hacer crecer indefinidamente la base de datos. La experiencia de usuario se diseñará con progreso en tiempo real o pseudo- progreso cuando el backend no permita streaming, y mensajes de error comprensibles. Si la IA no responde, el profesor conservará su contenido en el editor y podrá reintentar sin perder trabajo. La llamada a IA no se ejecutará desde la petición interactiva si puede exceder tiempos razonables; se desacoplará con cola cuando sea necesario. Propuesta de mejora Se dará la opción de generar textos en distintos idiomas directamente con IA. REQUISITO: II.1.2.1 3. POC RAG con chat por curso (AV13)

Requerimiento EducaMadrid Realización de una prueba de concepto para la integración de inteligencia artificial mediante un sistema de Retrieval-Augmented Generation (RAG) en la plataforma educativa EducaMadrid. El sistema debe almacenar los datos de cursos seleccionados y poner a disposición del usuario un chatbot de consulta dentro de las aulas virtuales MoodleMisc y Multisite. Propuesta técnica de empresa_s La prueba de concepto RAG se diseñará con infraestructura local en servidores propios de la administración. El alcance se limitará a cursos seleccionados a petición del docente o administrador, evitando indexar todo el Moodle de forma indiscriminada. El profesor elegirá recursos concretos -por ejemplo, páginas, archivos PDF, etiquetas, libros o contenidos eXeLearning- y el sistema generará representaciones vectoriales solo de esos materiales. La integración del chatbot se realizará mediante LTI o mecanismo equivalente previsto, de forma que Moodle mantenga el control de identidad, curso, rol y contexto. El chatbot no responderá con conocimiento general de la plataforma, sino con el corpus autorizado del curso. Cada petición incluirá contexto mínimo, comprobación de permisos y trazabilidad. No se enviarán datos a servicios externos no autorizados. La arquitectura propuesta separa cuatro piezas: extractor de contenidos del curso, pipeline de normalización y troceado, base vectorial local y servicio de chat. Para no sobrecargar moodledata ni la base de datos principal, los embeddings y metadatos RAG se almacenarán fuera de las tablas críticas de Moodle, referenciando únicamente identificadores de curso, recurso y versión. Se Página 74 de 192


definirá una tarea de reindexación incremental cuando cambie un recurso, y una purga automática cuando el docente retire un material o se cierre la POC. La POC deberá medir calidad y coste operativo: tiempo de indexación por tipo de recurso, tamaño del índice, latencia de respuesta, tasa de errores, satisfacción docente y casos donde el chatbot no debe contestar. El resultado será una recomendación técnica para escalar o acotar la funcionalidad. REQUISITO: II.1.2.1 4. Integrar NIA de los alumnos (AV14)

Requerimiento EducaMadrid Se requiere implementar un sistema de gestión de información de los alumnos en las aulas virtuales Moodle de los centros. El objetivo es contar con un sistema confiable y seguro que permita guardar y mantener actualizada la información de identificación de los alumnos (NIA, Número de Identificación de Alumno) en las aulas virtuales “Multisite” y “MoodleMisc”. Propuesta técnica de empresa_s La incorporación del NIA en Moodle se tratará como dato identificativo sensible y se implementará sin modificar core. Se creará un campo de perfil o estructura equivalente gestionada por plugin, con permisos estrictos de lectura y escritura. El dato llegará en tiempo real desde Raíces según lo alimenten los profesores y también podrá estar disponible en LDAP; la solución priorizará la fuente maestra definida por EducaMadrid y registrará discrepancias. La actualización será automática y diferencial. En cada login, sincronización programada o evento definido, se verificará si el NIA ha cambiado y se aplicará solo cuando corresponda. Se evitarán operaciones masivas innecesarias sobre user y tablas relacionadas. Para grandes volúmenes, las sincronizaciones se harán por lotes, con paginación, control de errores y reintentos. Los casos sin NIA, NIA duplicado o formato inválido se enviarán a un informe de actividad, no a un fallo silencioso. El acceso al NIA se limitará a roles y contextos con justificación funcional. En listados, exportaciones e integraciones se evitará exponerlo salvo necesidad. Los logs técnicos no incluirán el dato completo; se usarán identificadores internos o enmascaramiento. Cualquier API asociada requerirá autenticación fuerte, autorización por capability y registro de acceso. Propuesta de mejora Mostrar el NIA parcialmente enmascarado en pantallas de verificación cuando no sea imprescindible verlo completo, reduciendo exposición de datos personales. REQUISITO: II.1.2.1 5. SSO en Moodle (AV15)

Requerimiento EducaMadrid Se solicita conectar todas las aulas virtuales Multisite y MoodleMisc con el sistema de SSO de la plataforma EducaMadrid. Propuesta técnica de empresa_s La conexión de todas las aulas Multisite y MoodleMisc con el SSO de EducaMadrid se implementará mediante plugin de autenticación o extensión compatible, sin alterar el core. El login local dejará de ser el punto principal para usuarios corporativos; el usuario navegará como


anónimo por zonas habilitadas y al pulsar “Iniciar sesión” se tomará la sesión SSO existente o se redirigirá a la pantalla del SSO. Se mantendrá la entrada como invitado cuando el aula lo permita. La sincronización de datos del usuario en el momento del login actualizará atributos relevantes en Moodle sin sobrescribir información local que deba conservarse. Se cuidará especialmente el identificador estable: no se usará un atributo que pueda cambiar con el nombre del centro o del usuario. Para cierres de sesión, se implementará propagación de logout con pruebas en varios aplicativos, considerando que algunos navegadores bloquean cookies de terceros o cambian políticas de sesión. El SSO se validará en escenarios representativos: docente, alumno, administrador, usuario invitado, usuario con sesión ya abierta, usuario sin sesión, cierre de sesión en otro aplicativo, usuario desactivado, cambio de atributos, centro con URL modificada y acceso desde app móvil si procede. La integración será compatible con balanceadores y sesiones distribuidas; no dependerá de afinidad de nodo salvo que la arquitectura lo imponga. Propuesta de mejora Se realizarán las tareas técnicas necesarias para que el sso sea funcional también desde el aplicativo móvil. REQUISITO: II.1.2.1 6. Plugin Kuet (AV16)

Requerimiento EducaMadrid Adaptación del Plugin de Kuet para Moodle en la Plataforma de Aulas virtuales de EducaMadrid Multisite y MoodleMisc. Propuesta técnica de empresa_s La adaptación de Kuet se abordará teniendo en cuenta su naturaleza de actividad interactiva y potencialmente concurrente. El modo carrera con preguntas de distintos tipos exige baja latencia y comunicación estable mediante websocket u otro canal en tiempo real. La infraestructura de servidores propios se dimensionará junto al departamento de sistemas, ubicando certificados en balanceadores y manteniendo nodos backend sin gestión directa de certificados. La integración con Multisite y MoodleMisc se realizará con configuración por plataforma y, si es necesario, por isla. El plugin debe reconocer el contexto del curso, roles, permisos, banco de preguntas y actividad. La concurrencia se probará con sesiones simultáneas de varias aulas virtuales, no solo con usuarios de un único curso. Se medirán latencia, reconexiones, consumo de memoria, mensajes por segundo y comportamiento ante caída de un nodo websocket. La seguridad incluirá autenticación de sesión Moodle, autorización por actividad, tokens temporales, protección contra reutilización de conexiones, validación de payloads y limitación de frecuencia. Ningún cliente debe poder enviar eventos de otra partida, curso o usuario. La documentación recogerá topología, puertos, balanceo, logs y procedimiento de reinicio. Mejora diferencial propuesta: añadir una prueba de carga específica para Kuet antes de campañas de uso intensivo, con un informe de capacidad por número de partidas simultáneas y usuarios por partida.

REQUISITO: II.1.2.17 . Plugin Offline Quiz (AV17) Requerimiento EducaMadrid


Adaptación del plugin OfflineQuiz para las aulas virtuales Multisite y MoodleMisc en la plataforma EducaMadrid. El objetivo es asegurar que el plugin cumpla con las características y funcionalidades requeridas para su correcto funcionamiento en el entorno educativo de EducaMadrid Propuesta técnica de empresa_s La adaptación de OfflineQuiz cubrirá impresión, identificación del alumno, escaneo mediante fotos y reintegración de calificaciones. El formulario impreso incluirá marca de agua con logotipo de EducaMadrid, instrucciones claras de rellenado y un identificador único que permita reasignar la calificación en el escaneo posterior. El identificador no debe exponer datos personales en claro si no es imprescindible; puede codificar una referencia controlada al intento, curso y alumno. El plugin trabajará con el banco de preguntas de Moodle, incluyendo preguntas generadas con IA, que deberán identificarse con el icono característico. Se revisará el impacto de cuestionarios muy largos, permitiendo múltiples hojas y evitando cortes de contenido. Para el escaneo con fotografías, se definirá tolerancia a rotación, sombras, baja calidad y diferentes dispositivos, así como mensajes de validación cuando el formulario no pueda procesarse. En términos de escala, la generación masiva de PDFs o formularios no debe saturar el servidor web. Las operaciones pesadas se podrán derivar a tareas en segundo plano, con descarga posterior. Los archivos temporales se almacenarán con caducidad y limpieza programada para no incrementar indefinidamente moodledata. Mejora diferencial propuesta: añadir un modo de previsualización de una página antes de generar todo el lote, para detectar errores de maquetación o instrucciones antes de imprimir decenas de formularios.

REQUISITO: II.1.2.18 . Plugin para incorporar calificaciones en raíces (AV18) Requerimiento EducaMadrid Creación de un plugin para Moodle que permita la incorporación de las calificaciones de los alumnos directamente a RAICES desde las aulas virtuales de los centros. El objetivo es facilitar la gestión de calificaciones y asegurar la integridad y seguridad de los datos. Propuesta técnica de empresa_s El plugin añadirá un icono en el libro de calificaciones para iniciar la incorporación de una columna a Raíces. La interacción se concentrará en un modal guiado: autenticación del profesor en Raíces, recuperación de cursos y niveles asignados, selección de clase y nivel, obtención de alumnos y asignación de calificaciones. La llamada a la API proporcionada por Madrid Digital se realizará siempre por canal seguro y con gestión explícita de errores. La dificultad principal está en la correspondencia entre libro de calificaciones Moodle y estructura académica de Raíces. Se implementará una validación previa que muestre qué alumnos coinciden, cuáles faltan y cuáles presentan ambigüedad. No se enviarán calificaciones de forma ciega. El profesor confirmará el conjunto final y el sistema guardará un recibo técnico con fecha, usuario, curso, columna, número de calificaciones enviadas y resultado por alumno. Para proteger rendimiento, la operación se ejecutará por lotes si la clase es numerosa o si la API limita peticiones. Se evitará bloquear la vista del libro de calificaciones durante una espera larga. Los datos de autenticación no se almacenarán salvo que el mecanismo oficial lo permita y, en todo caso, se tratarán con mínimos privilegios y expiración corta.


Mejora diferencial propuesta: incorporar una simulación previa “validar sin enviar” que permita al docente comprobar correspondencias con Raíces antes de realizar la incorporación definitiva.

REQUISITO: II.1.2.19 . Borrado de cursos en segundo plano (AV19) Requerimiento EducaMadrid Implementación de un sistema que permita el borrado asíncrono de cursos en las aulas virtuales Multisite y MoodleMisc mediante el cron de Moodle. El objetivo es mejorar la eficiencia y la experiencia del usuario al programar el borrado de cursos en segundo plano. Propuesta técnica de empresa_s El borrado asíncrono de cursos es crítico en una instalación con moodledatas muy grandes. El usuario autorizado marcará un curso para borrado; desde ese momento el curso quedará inaccesible y se mostrará un mensaje de estado. La eliminación real se programará mediante cron de Moodle y se ejecutará con Moosh, en segundo plano, registrando usuario solicitante, fecha de programación, fecha de ejecución, servidor, resultado y errores. La eliminación no se lanzará como una operación monolítica sin control. Se aplicará una cola con estados: solicitado, bloqueado, en validación, en borrado, finalizado, fallido, pendiente de reintento o cancelado. Antes de borrar se comprobarán permisos, estado del curso, backups pendientes, tamaño estimado, dependencias y existencia de tareas relacionadas. Para evitar impacto, se limitará el número de cursos borrados simultáneamente por isla y se programarán lotes fuera de horas pico. Moodle almacena ficheros en filepool con referencias desde la base de datos. Un borrado de curso puede liberar referencias, pero la limpieza física de archivos puede depender de tareas de basura y retención. Por ello se medirá no solo el fin del comando de borrado, sino la evolución real de moodledata. El sistema informará de que la recuperación de espacio puede no ser inmediata y quedará sujeta a las tareas de limpieza configuradas. El proceso debe ser robusto ante fallos a mitad de ejecución. Si un curso falla, no debe bloquear la cola completa. El sistema almacenará logs por curso y causa de fallo, y permitirá reintentos controlados. Los cursos en borrado no podrán restaurarse ni duplicarse por usuarios ordinarios mientras el proceso esté en curso. Mejora diferencial propuesta: añadir una estimación previa de impacto -tamaño del curso, número de ficheros, actividades, logs y backups asociados- para ordenar la cola y evitar que cursos enormes bloqueen eliminaciones pequeñas.

REQUISITO: II.1.2. 20. Moosh (AV20) Requerimiento EducaMadrid Adaptación del script Moosh al entorno de aulas virtuales MoodleMisc y Multisite de EducaMadrid para cambios evolutivos. El objetivo es asegurar que Moosh funcione correctamente en ambos entornos y cumpla con las características requeridas. Propuesta técnica de empresa_s La adaptación de Moosh a MoodleMisc y Multisite se realizará manteniendo un mismo código base, pero añadiendo resolución contextual de centro e IP. Cada llamada incorporará los parámetros requeridos: centro sobre el que se actúa e IP del servidor de ejecución. Con esos


datos, el wrapper localizará la configuración correcta, la base de datos correspondiente, el directorio de moodledata y el contexto de ejecución. No se expondrá Moosh como una herramienta libre de ejecución. Se creará una capa de control que valide comandos permitidos, parámetros, usuario técnico, entorno y ventana de ejecución. Las acciones peligrosas - borrado, restauración, cambios masivos- requerirán confirmación o ejecución desde procesos autorizados. La salida del comando se normalizará para que los procesos de Moodle puedan interpretar éxito, error recuperable o error fatal. En entornos de gran escala, Moosh debe convivir con cron, backups y operaciones de base de datos. El wrapper usará locks para impedir que dos procesos actúen simultáneamente sobre el mismo curso o centro. También registrará duración, consumo aproximado, código de salida y fragmentos relevantes de log, evitando volcar información sensible.

REQUISITO: II.1.2.21. Moodler (AV21) Requerimiento EducaMadrid Adaptación del plugin MOODLER al entorno de aulas virtuales MoodleMisc y Multisite de EducaMadrid para cambios evolutivos. El objetivo es asegurar que el plugin cumpla con las características y funcionalidades requeridas para su correcto funcionamiento en el entorno educativo de EducaMadrid. Propuesta técnica de empresa_s La adaptación de Moodler proporcionará una API securizada para acceder a funciones del core de Moodle desde herramientas autorizadas. La API se diseñará con autenticación fuerte, autorización por permisos, sanitización completa de entradas y salidas, control de tasa, logs de auditoría y separación de operaciones de lectura y escritura. No se expondrán funciones genéricas del core sin una capa de validación específica. El funcionamiento en modo multisite requiere resolver correctamente a qué aula, centro, base de datos y moodledata pertenece cada petición. La API no confiará únicamente en parámetros enviados por el cliente; contrastará el centro, la IP, el token y el ámbito autorizado. Las respuestas estarán paginadas para evitar consultas masivas y se aplicarán límites de tamaño. En operaciones que puedan tardar, Moodler devolverá un identificador de tarea y permitirá consultar estado, en lugar de mantener una conexión abierta. La mantenibilidad se garantizará con documentación OpenAPI o equivalente, ejemplos de llamada, códigos de error estables, pruebas automatizadas y versionado de endpoints. Las futuras versiones podrán coexistir temporalmente para que integraciones externas migren sin interrupción. Mejora diferencial propuesta: añadir scopes de API por tipo de operación - lectura, administración, curso, usuario, calificaciones- para reducir el impacto si una credencial queda comprometida.
##### 1.3.1.1.3. APARTADO: EVOLUCIÓN Y MANTENIMIENTO DE LA MEDIATECA (MED)
Propuesta técnica de empresa_s Enfoque técnico general de la Mediateca La Mediateca se abordará como un desarrollo propio y consolidado de EducaMadrid, construido en PHP sin framework generalista y con una evolución funcional acumulada durante años. La solución no plantea una reescritura disruptiva, sino una intervención progresiva y controlada sobre el código existente, combinando mantenimiento evolutivo, refactorización selectiva, Página 79 de 192


Fecha: 21/05/2026

endurecimiento de seguridad, mejora de rendimiento y nuevas capacidades funcionales. Esta aproximación es la más adecuada para un servicio en producción, con gran volumen de contenidos multimedia, usuarios docentes y alumnos, integraciones con otros servicios de la plataforma y dependencias operativas con almacenamiento, transcodificación, subtitulado, búsqueda, SSO y procesos asíncronos. El criterio técnico principal será preservar la continuidad del servicio mientras se reduce la complejidad interna. En la situación actual, la existencia de tratamientos diferenciados para cada tipo de contenido ha generado duplicidad de código, dispersión de reglas de negocio y mayor coste de mantenimiento. Por ello, se propone evolucionar hacia un núcleo común de gestión de contenidos, capaz de resolver de forma homogénea operaciones como alta, validación, edición, metadatos, visibilidad, permisos, indexación, eliminación, auditoría, descarga y relación con ficheros. Sobre ese núcleo se mantendrán adaptadores específicos para las particularidades de vídeo, audio, imagen, PDF, Scratch, eXeLearning y futuros tipos de contenido. La arquitectura funcional de la solución se organizará en capas ligeras compatibles con el carácter actual de la aplicación: controladores PHP existentes saneados, servicios de dominio reutilizables, repositorios de acceso a datos con consultas parametrizadas, componentes de integración para sistemas externos y trabajos de fondo gestionados mediante cola y cron. No se impondrá un cambio tecnológico brusco que incremente el riesgo, pero sí se introducirán patrones de diseño sencillos y mantenibles: factorías para tipos de contenido, estrategias para procesos específicos, validadores reutilizables, clases de permisos centralizadas y servicios de indexación desacoplados. Para asegurar rendimiento en una Mediateca de gran tamaño, la solución separará claramente las operaciones síncronas de las operaciones pesadas. La subida, la edición visible para el usuario, la autenticación y la búsqueda deben responder con tiempos bajos; en cambio, subtitulado, resumen por IA, indexación masiva, regeneración de metadatos, limpieza de ficheros, tratamiento de contenidos históricos y generación de miniaturas se ejecutarán en segundo plano con control de carga. Cada proceso de fondo tendrá trazabilidad, reintentos limitados, bloqueo anti-ejecución duplicada y métricas de duración. Eje Decisión técnica Efecto esperado Código PHP legacy Refactorización incremental Menor riesgo, mejora continua por zonas funcionales, sin y despliegues asumibles reescritura total Tipos de contenido Núcleo común más Menos duplicidad, adaptadores específicos incorporación más rápida de nuevos formatos Búsqueda Capa híbrida Mejor respuesta en consultas SQL/Elasticsearch con fallback y resiliencia ante controlado indisponibilidad de Elastic IA y subtítulos Procesamiento asíncrono con Escalabilidad sin bloquear la colas, cupos y revisión experiencia de usuario humana Seguridad Validación centralizada, Reducción de vectores de permisos por acción y auditoría ataque en funcionalidades críticas


La metodología de trabajo será iterativa por entregables MED, pero con una disciplina transversal: antes de tocar cada funcionalidad se realizará una lectura del flujo real en código, identificación de puntos duplicados, definición de pruebas de regresión y diseño de la intervención mínima que deje el sistema mejor que antes. El objetivo no es solo cumplir cada requisito, sino que cada cambio deje una pieza reutilizable para los siguientes apartados.

REQUISITO: II.1.3.1. Subtítulos multi idioma (MED1) Requerimiento EducaMadrid La Mediateca de EducaMadrid busca desarrollar un plugin que permita a los usuarios crear y editar subtítulos para los vídeos subidos a la plataforma. El plugin debe utilizar la tecnología de IA para generar subtítulos automáticamente en el idioma nativo del vídeo e inglés. Además, el plugin debe incluir un editor de subtítulos que permita a los usuarios agregar, editar y eliminar subtítulos de manera sencilla y segura. Propuesta técnica de empresa_s La evolución de la Mediateca incorporará un mecanismo de generación, edición y publicación de subtítulos multi idioma para los contenidos audiovisuales, orientado a mejorar la accesibilidad, la reutilización educativa de los vídeos y el cumplimiento de buenas prácticas en materia de inclusión digital. La solución se apoyará en un flujo de tratamiento asíncrono, de forma que la generación de subtítulos no afecte a la experiencia de usuario ni al rendimiento general de la plataforma. Cuando un usuario suba un vídeo, o cuando se solicite la generación de subtítulos sobre un contenido ya existente, se registrará una tarea en una cola de procesamiento. Esta tarea extraerá el audio del vídeo, normalizará el formato cuando sea necesario y lanzará el proceso de transcripción automática mediante un modelo de inteligencia artificial basado en Whisper, adecuado para reconocimiento de voz y generación de texto a partir de audio. El uso de Whisper se planteará como un componente desacoplado del núcleo de la Mediateca, evitando introducir dependencias rígidas en el código PHP existente. Para ello se desarrollará una capa de integración específica, invocable desde los procesos batch o workers, que permita enviar el audio al motor de transcripción y recibir como resultado un fichero de subtítulos en formato estándar, el SRT . Esta separación facilitará cambiar la modalidad de despliegue del modelo —por ejemplo, ejecución local, servicio interno o integración con una API autorizada— sin reescribir la lógica funcional de la Mediateca. El tratamiento de los subtítulos se diseñará teniendo en cuenta que la Mediateca es un desarrollo propio en PHP vanilla con años de evolución. Por ello, no se añadirá lógica duplicada en cada tipo de contenido, sino que se incorporará un servicio común de subtitulado asociado al recurso multimedia. Este servicio gestionará las operaciones principales: solicitud de generación, seguimiento del estado, almacenamiento del fichero de subtítulos, asociación al idioma correspondiente, revisión manual, activación o desactivación y publicación en el reproductor. A nivel funcional, cada vídeo podrá disponer de una o varias pistas de subtítulos. La primera pista podrá generarse automáticamente a partir del idioma detectado o indicado por el usuario. Posteriormente, se podrán añadir versiones en otros idiomas mediante procesos de traducción asistida o carga manual de ficheros. La interfaz permitirá identificar claramente si un subtítulo ha sido generado automáticamente, revisado por un usuario o cargado manualmente, evitando que el usuario final confunda una transcripción automática sin revisar con una versión validada.


Desde el punto de vista técnico, el proceso contemplará controles específicos para contenidos de gran tamaño. Los vídeos largos se podrán dividir en fragmentos de audio para facilitar su tratamiento, reducir errores por timeout y permitir reintentos parciales. El sistema registrará el estado de cada tarea —pendiente, procesando, finalizada, finalizada con avisos o fallida— y conservará trazas técnicas suficientes para diagnosticar problemas sin exponer información sensible. Por ejemplo, si un vídeo contiene audio con baja calidad, silencios prolongados o varios interlocutores solapados, la tarea podrá completarse indicando advertencias para revisión posterior. La integración con el reproductor de la Mediateca se realizará mediante formatos estándar, de forma que los subtítulos puedan activarse desde el propio visor del vídeo sin soluciones propietarias. Se revisará el tratamiento actual de los distintos tipos de contenido para evitar que la funcionalidad quede limitada a una única ruta de visualización. Siempre que el recurso tenga naturaleza audiovisual, la gestión de subtítulos se resolverá desde el mismo bloque funcional común, con las particularidades necesarias para vídeos publicados, vídeos embebidos, recursos educativos derivados o contenidos reutilizados en otros servicios de EducaMadrid. También se incorporarán mecanismos de administración para controlar el consumo de recursos. La generación automática de subtítulos mediante IA puede ser costosa en CPU, GPU o tiempo de proceso, por lo que se definirán límites por tamaño, duración, prioridad y número de tareas concurrentes. Las tareas de mayor peso podrán ejecutarse en horarios de menor carga o en workers separados del frontal web. Esta aproximación permite incorporar IA sin comprometer la estabilidad de la Mediateca ni penalizar operaciones críticas como la navegación, búsqueda, reproducción o subida de contenidos. Como ejemplo, un docente podría subir un vídeo explicativo de diez minutos. La Mediateca registraría el contenido, generaría una tarea de subtitulado, extraería el audio, lo procesaría con Whisper y asociaría al vídeo un fichero VTT en español. Una vez generado, el docente podría revisar el texto, corregir términos propios de la materia y publicar la pista de subtítulos. Si posteriormente se requiere una versión en otro idioma, el sistema permitiría añadirla como pista adicional sin duplicar el vídeo ni alterar el contenido original. Como mejora de valor añadido, se propone incorporar todos los subtítulos multiidioma en las búsquedas por elastic de modo que un usuario encuentre coincidencias en sus búsquedas en las traducciones de los subtítulos.

REQUISITO: II.1.3.2. Elastic en las búsquedas (MED2) Requerimiento EducaMadrid La Mediateca de EducaMadrid busca crear un plugin que permita utilizar Elastic como motor de búsqueda de contenidos en lugar de la base de datos del aplicativo. El plugin debe adaptar la Mediateca para compatibilizarla con las mejoras en el sistema de búsquedas de Medios con Elastic Search y las evoluciones del mismo. Propuesta técnica de empresa_s La integración de Elasticsearch se planteará como una sustitución progresiva del mecanismo de búsqueda basado en SQL, manteniendo un sistema híbrido para garantizar continuidad. La Mediateca no debe quedar acoplada rígidamente a Elastic: se creará una capa de búsqueda con una interfaz común y dos implementaciones, una SQL y otra Elastic. La decisión de uso dependerá de configuración, disponibilidad del servicio, tipo de consulta y estado de indexación.


El índice se diseñará alrededor del concepto de contenido unificado. Cada documento incluirá identificador, tipo, título, descripción, etiquetas, autor, centro, visibilidad, fechas, idioma, texto extraído de PDF, texto de subtítulos, metadatos técnicos y campos preparados para relevancia. Los tipos de contenido seguirán aportando campos específicos, pero sin obligar a duplicar toda la lógica de búsqueda. Esta decisión encaja con la necesidad de reducir repetición: la búsqueda se implementa una vez y cada contenido aporta únicamente su bloque de datos indexable. La indexación tendrá dos vías. La primera será incremental, disparada por cambios de contenido: alta, edición, publicación, baja, generación de subtítulos, modificación de etiquetas o cambio de permisos. La segunda será masiva y controlada, útil para reconstrucciones del índice, incorporación de nuevos campos o recuperación ante incidencias. Los procesos masivos se ejecutarán con paginación por identificador, lotes configurables, checkpoints y reintentos, evitando consultas que recorran tablas completas sin índice. El fallback a SQL no será un simple “si falla Elastic”. Se definirá un circuito de degradación: si Elastic no responde, responde lento o devuelve errores repetidos, la aplicación usará SQL durante un periodo configurable y registrará el cambio de modo. El usuario no verá un error técnico; verá resultados con menor riqueza funcional si fuera necesario. En el panel de mando se mostrarán latencias, número de consultas, parámetros de búsqueda, motor usado, errores, timeouts y ratio de fallback. El highlighting se incorporará de forma segura, escapando siempre fragmentos y evitando inyección de HTML. Los contenidos relacionados, contenidos del mismo autor y portada podrán consultar Elastic con perfiles de consulta específicos, pero se protegerán con caché de corta duración para no recalcular bloques de portada en cada visita. Las búsquedas avanzadas validarán filtros y ordenaciones mediante listas blancas, nunca concatenando parámetros de usuario en consultas. Mejora propuesta: añadir un “modo explicación” solo para administradores, que muestre por qué un contenido aparece en los resultados: coincidencia en título, etiqueta, descripción, subtítulo o PDF. También se mostrará un dashboard con estadísticas de uso del cluster elastic.

REQUISITO: II.1.3.3. Single Sign On (MED3) Requerimiento EducaMadrid La Mediateca de EducaMadrid busca crear un plugin que permita utilizar el sso de EducaMadrid como método de autenticación SSO. Propuesta técnica de empresa_s La autenticación SSO se integrará respetando la navegación anónima de la Mediateca. La aplicación seguirá permitiendo consultar contenidos públicos sin sesión, especialmente los contenidos embebidos en páginas externas, pero cuando el usuario pulse “iniciar sesión” se delegará la autenticación en el SSO de EducaMadrid. Si el usuario ya dispone de sesión válida en otro aplicativo, la Mediateca lo reconocerá y creará o actualizará la sesión local sin pedir credenciales de nuevo. La sesión local no duplicará innecesariamente la identidad. Se almacenará solo lo necesario para operar: identificador estable, nombre visible, apellidos, centro o centros relevantes, roles y fecha de sincronización. En cada login se actualizarán los datos locales que puedan haber cambiado. Para minimizar impacto sobre el SSO, se aplicará caché de sesión y se evitarán llamadas repetidas en cada carga de contenido público.


El cierre de sesión se tratará con especial cuidado. Si el usuario cierra sesión en otro servicio conectado al SSO, la Mediateca deberá invalidar su sesión local en la siguiente comprobación o mediante mecanismo disponible de notificación/sincronización. Para contenidos embebidos públicos no se forzará comprobación de sesión, evitando que un vídeo público insertado en una web provoque redirecciones o llamadas innecesarias al SSO. El soporte futuro para doble factor se dejará preparado separando autenticación, creación de sesión y autorización. La Mediateca no debe implementar el segundo factor por su cuenta, sino aceptar el resultado del SSO y adaptar mensajes, redirecciones y estados. Los flujos de error contemplarán credenciales inválidas, usuario bloqueado, sesión caducada, segundo factor pendiente, falta de atributos obligatorios y usuario sin permisos suficientes. En términos de seguridad, se revisarán cookies de sesión, flags Secure, HttpOnly y SameSite, regeneración de identificador tras login, protección CSRF en acciones autenticadas y control de redirecciones para evitar open redirects. Las URLs de retorno se validarán contra dominios y rutas permitidas. Mejora propuesta: en casos no necesarios, como contenidos públicos, no se comprobará si el usuario tiene sesión activa para evitar sobrecarga en el sso.

REQUISITO: II.1.3.4. Scratch editor (MED4) Requerimiento EducaMadrid Se solicita que para los tipos de contenido Scratch alojados en la mediateca se disponga de la opción de editar los mismos directamente de manera online. Para ello se requiere modificar el aplicativo “Mediateca” creando un plugin. Propuesta técnica de empresa_s La edición de contenidos Scratch se diseñará como una integración controlada entre la Mediateca y una instalación propia del editor Scratch en servidores de la plataforma. No se planteará como una redirección abierta a un editor genérico, sino como un flujo con token temporal, permisos verificados y retorno seguro. El usuario accederá al editor desde la ficha del contenido o desde la acción de crear un nuevo contenido Scratch; el editor solo aceptará sesiones iniciadas desde la Mediateca. El flujo de edición partirá de una comprobación de propiedad. Un docente propietario podrá editar sus contenidos. Un alumno propietario solo podrá editar si el contenido no ha sido validado todavía, tal como exige el pliego. Al abrir el editor, la Mediateca generará un identificador de operación con caducidad, contenido asociado, usuario, permisos concedidos y URL de retorno. El editor consultará ese identificador y cargará el proyecto correspondiente, o una plantilla vacía si se trata de un contenido nuevo. La comunicación entre ambos sistemas se realizará por HTTPS y con firma de las operaciones relevantes. No se enviarán rutas físicas de ficheros ni permisos en claro. Al guardar, el editor devolverá el paquete o la referencia del proyecto a un endpoint de Mediateca, que validará el token, comprobará que no se ha reutilizado indebidamente, almacenará la nueva versión y actualizará metadatos. Si falla la operación, el contenido anterior seguirá disponible. Para no introducir una excepción más dentro del código legacy, Scratch se incorporará al modelo común de contenido. Tendrá adaptador específico para editor, previsualización y empaquetado, pero compartirá permisos, etiquetas, visibilidad, indexación básica, trazabilidad y ciclo de


validación. Este enfoque evita crear otra rama paralela de código y prepara la incorporación de futuros contenidos interactivos. Las pruebas cubrirán perfiles de docente, alumno, administrador y usuario anónimo; creación desde cero; edición de contenido validado y no validado; pérdida de sesión; token caducado; guardado concurrente; cancelación de edición; y visualización posterior. También se probará el comportamiento del editor con navegadores habituales y dispositivos de uso educativo. Mejora propuesta: guardar una versión anterior del proyecto antes de sobrescribirlo, permitiendo restauración administrativa simple ante un guardado accidental o proyecto corrupto.

REQUISITO: II.1.3.5. Exelearning 3 (MED5) Requerimiento EducaMadrid Adaptación de la Mediateca para soportar contenido eXeLearning 3 y conexión con eXeLearning online. Propuesta técnica de empresa_s El soporte para eXeLearning 3 (o 4) se tratará como un nuevo tipo de contenido empaquetado, compuesto por un ZIP publicable y, cuando exista, un fichero editable .elp. La Mediateca almacenará ambos elementos de forma relacionada pero diferenciada: el ZIP se orienta a visualización y descarga del recurso publicado; el .elp se orienta a edición y continuidad del trabajo por parte del autor. La ficha del contenido mostrará claramente qué acciones están disponibles según permisos y existencia del editable. La visualización en IFRAME se implementará con controles de seguridad. Se validará que el ZIP contiene una estructura esperada, que el punto de entrada es seguro y que no introduce rutas relativas peligrosas o ficheros no permitidos. El contenido se desplegará en un área controlada del almacenamiento de Mediateca, evitando sobrescrituras entre contenidos y generando rutas no predecibles. La apertura en ventana nueva usará la misma URL controlada, con cabeceras adecuadas para reducir riesgos. La conexión con eXeLearning online seguirá un flujo de ida y vuelta. Desde la Mediateca, el usuario autenticado seleccionará crear o editar. La aplicación generará una operación firmada con contenido, usuario, acción permitida y retorno. eXeLearning online abrirá el recurso; al finalizar, devolverá el nuevo ZIP y, en su caso, el .elp actualizado. La Mediateca validará la operación, almacenará nueva versión, recalculará metadatos y conservará trazabilidad de la edición. La descripción y etiquetado del contenido se integrarán en el modelo común de metadatos. eXeLearning 3 aportará particularidades como tipo de paquete, versión de herramienta, existencia de editable, tamaño, número aproximado de páginas y estado de validación. La búsqueda podrá indexar título, descripción, etiquetas y, si técnicamente se habilita extracción segura de texto, contenido textual interno del paquete. El desarrollo utilizará PHP compatible con el core de Mediateca y MySQL, pero evitando añadir lógica repetida en múltiples pantallas. Se creará un servicio de gestión de paquetes eXeLearning responsable de validar, desplegar, versionar y limpiar ficheros temporales. Las operaciones pesadas se podrán diferir a cola si el tamaño del ZIP lo aconseja. Mejora propuesta: añadir una comprobación previa del ZIP que informe al usuario de problemas detectados antes de publicar: ausencia de index.html, tamaño excesivo, extensiones no permitidas o estructura inválida.


REQUISITO: II.1.3.6. Bajas de usuarios (MED6) Requerimiento EducaMadrid Creación de un script en PHP seguro que permita procesar las bajas de los usuarios del portal educativo de EducaMadrid directamente en el aplicativo Mediateca, eliminando sus contenidos y datos. Propuesta técnica de empresa_s El procesamiento de bajas de usuarios se implementará como un procedimiento controlado, auditable y recuperable durante la fase operativa definida por EducaMadrid. La baja no debe consistir en lanzar borrados directos dispersos sobre tablas y disco, porque la Mediateca contiene múltiples relaciones: contenidos, ficheros derivados, miniaturas, subtítulos, resúmenes, comentarios si existieran, favoritos, estadísticas, permisos, colas pendientes e índices de búsqueda. El script PHP seguro recibirá un identificador de usuario validado y ejecutará un plan de baja. Primero resolverá todos los elementos asociados al usuario; después clasificará acciones: eliminar contenido privado, retirar o anonimizar autoría cuando proceda, borrar ficheros físicos, cancelar tareas pendientes, eliminar subtítulos y resúmenes, desindexar en Elastic y registrar el resultado. La ejecución se realizará por lotes para evitar timeouts y permitir reanudación si el volumen de contenidos es alto. La validación de permisos será estricta. Solo perfiles autorizados o procesos internos invocados desde canales confiables podrán ejecutar la baja. Cada ejecución quedará registrada con usuario o proceso solicitante, fecha, identificador afectado, número de contenidos tratados, número de ficheros eliminados, errores y estado final. No se guardará más información personal de la necesaria en el log. Para proteger datos, la eliminación de disco se hará desde un servicio centralizado que conozca las rutas permitidas. Se evitarán borrados construidos con concatenación de parámetros. Antes de eliminar, se verificará que la ruta pertenece al área de Mediateca y que el fichero está asociado al contenido previsto. Cuando existan réplicas, miniaturas o versiones transcodificadas, se tratarán como dependencias del contenido. La integración con Elastic contemplará desindexación inmediata o tarea de desindexación si el servicio no está disponible. El sistema no debe quedar inconsistente: un contenido eliminado no debe seguir apareciendo en resultados por un fallo temporal del motor de búsqueda. Para ello se registrarán pendientes de desindexación y se reintentarán hasta confirmar. Mejora propuesta: incorporar un modo “simulación” que calcule qué se eliminaría sin ejecutar el borrado, generando un informe previo útil para validar bajas complejas o masivas.

REQUISITO: II.1.3.7. Soporte JPEG en subidas masivas de imágenes (MED7) Requerimiento EducaMadrid
- Soportar formato JPEG: Admitir subidas de imágenes en formato JPEG de la misma
manera que se soportan JPG, GIF y PNG.
- Mejorar experiencia del usuario: Permitir a los usuarios subir múltiples imágenes en
formato JPEG de manera rápida y eficiente. Propuesta técnica de empresa_s


El soporte JPEG se incorporará revisando la lógica real de detección de imágenes, no solo añadiendo una extensión a una lista. En aplicaciones con años de evolución es frecuente que JPG, JPEG, GIF y PNG se comprueben en varios puntos: formulario, validación de servidor, generación de miniaturas, almacenamiento, mensajes de error, subidas masivas y visualización. La intervención localizará todos esos puntos y los consolidará en un validador único de imágenes. La validación aceptará extensión .jpeg y MIME type correcto, pero no dependerá únicamente de ellos. Se comprobará el contenido real del fichero con funciones seguras de inspección de imagen, límites de tamaño, dimensiones máximas y tratamiento de errores. En subidas masivas se procesará cada fichero de forma independiente, mostrando resultado individual: subido, rechazado por formato, rechazado por tamaño, error de lectura o error de almacenamiento. El almacenamiento y la visualización tratarán JPEG y JPG como variantes del mismo tipo lógico. Esto evita duplicar ramas de código y facilita que futuras extensiones de imagen se añadan de forma controlada. La generación de miniaturas reutilizará el mismo servicio de tratamiento de imágenes, con normalización opcional de orientación EXIF para evitar imágenes giradas incorrectamente. En términos de experiencia de usuario, la subida masiva debe ser tolerante a errores parciales. Si un lote contiene veinte imágenes y una falla, las diecinueve válidas deben conservarse y el usuario debe recibir un resumen claro. No se debería abortar todo el lote salvo error global de permisos o almacenamiento. Mejora propuesta: mostrar antes de enviar una validación ligera en cliente para extensiones admitidas, manteniendo la validación fuerte en servidor como control definitivo.

REQUISITO: II.1.3.8. Páginas de error personalizadas (MED8) Requerimiento EducaMadrid

- Crear páginas de error personalizadas:
o Crear páginas de error personalizadas para los códigos de error 404, 500, etc. o Reemplazar las páginas de error propias de Apache por páginas de error personalizadas.
- Mejorar experiencia del usuario:
o Proporcionar a los usuarios una experiencia de error más amigable y útil. o Proporcionar a los usuarios información útil y relevante sobre el error. Propuesta técnica de empresa_s Las páginas de error se diseñarán como parte de la experiencia de la Mediateca y también como mecanismo de seguridad. Reemplazar páginas genéricas de Apache por páginas personalizadas evita exponer detalles técnicos, rutas, versiones o mensajes internos. Se contemplarán al menos errores 404, 403, 500 y situaciones de mantenimiento o indisponibilidad temporal si el entorno lo permite. La página 404 orientará al usuario: indicará que el contenido no existe, ha sido retirado o no está disponible, y ofrecerá retorno a la portada o al buscador. La página 403 será distinta: explicará que el usuario no tiene permisos o necesita iniciar sesión, evitando revelar si un contenido privado existe. La página 500 será prudente, sin trazas, nombres de clases ni consultas; incluirá un identificador de error correlacionable con logs internos. La integración técnica se realizará tanto en configuración de servidor como en la propia aplicación. Los errores capturados por PHP se derivarán a plantillas de Mediateca; los errores de servidor se Página 87 de 192


redirigirán a recursos estáticos o rutas seguras. En ambos casos se mantendrá imagen institucional, responsive design y accesibilidad básica: estructura semántica, foco visible, contraste y mensajes comprensibles. Para soporte, cada error relevante generará una entrada de log con timestamp, URL, código, identificador de correlación y, si existe sesión, identificador técnico del usuario. No se incluirán datos personales innecesarios. Este diseño permite resolver incidencias sin mostrar al usuario información sensible. Mejora propuesta: incorporar un bloque de “qué puedo hacer ahora” adaptado al error: buscar contenido, volver a inicio, iniciar sesión o contactar con soporte con el código de incidencia.

REQUISITO: II.1.3.9. Subtítulos en los audios (MED9) Requerimiento EducaMadrid Permitir que para los tipos de contenido audio en la mediateca se generen subtítulos mediante IA de manera automática durante la subida de los mismos. Propuesta técnica de empresa_s La generación de subtítulos para audios se apoyará en los componentes definidos para vídeo, pero con adaptaciones propias del reproductor de audio y del tratamiento de contenidos históricos. El audio no tiene imagen, por lo que la presentación del subtítulo debe integrarse como transcripción sincronizada o panel de texto con resaltado del tramo actual. Esta decisión mejora la accesibilidad y facilita el consumo educativo de podcasts, explicaciones y materiales orales. Durante la subida de nuevos audios, la Mediateca registrará una tarea de transcripción por IA. El usuario no tendrá que esperar a que termine para completar la publicación; el contenido podrá quedar en estado “transcripción pendiente”. Cuando la tarea finalice, el usuario recibirá aviso y podrá revisar o editar los tramos mediante el editor de subtítulos. El formato de almacenamiento será compatible con SRT/VTT para reutilizar validadores, editor y mecanismos de indexación. Para audios ya existentes se creará un script de carga inicial que encole contenidos por lotes. Se priorizarán audios recientes o más consultados si existen métricas, y se limitará la concurrencia según disponibilidad del sistema de IA. El script no debe competir con las transcripciones de nuevos contenidos: las tareas nuevas tendrán prioridad para que la funcionalidad percibida por el usuario sea ágil. La adaptación del reproductor considerará navegación por tramos, búsqueda dentro de la transcripción y descarga del texto si los permisos del contenido lo permiten. Los subtítulos generados se indexarán en Elastic, permitiendo encontrar audios por las palabras pronunciadas. La revisión humana seguirá siendo importante, por lo que el estado de la transcripción distinguirá generado automáticamente, revisado y publicado. Mejora propuesta: se incorporarán los cambios necesarios para no solo mostrar la trascripción, sino para que ésta sea multi idioma.

REQUISITO: II.1.3.10. IA en mediateca: generar resúmenes de los vídeos (MED10) Requerimiento EducaMadrid


Implementación de un sistema que, utilizando inteligencia artificial (IA), realice resúmenes de los subtítulos de los vídeos y recursos de Formación Profesional (FP) subidos a la mediateca de EducaMadrid. Estos resúmenes se adjuntarán a la descripción de cada contenido y se generarán de manera asíncrona. Objetivos
- Implementar un sistema de resúmenes de subtítulos utilizando IA.
- Integrar el sistema de resúmenes en el actual sistema de colas de tareas de la mediateca.
- Asegurar que los resúmenes se generen de manera asíncrona y se notifique al usuario.
- Permitir la eliminación y regeneración de resúmenes a solicitud del usuario.
- Instalar el sistema de IA localmente en los servidores con GPU de la plataforma y asegurar
una comunicación segura con la mediateca.
- El modelo seleccionado para la generación de resúmenes debe ser seguro y proporcionar
resultados con calidad. Propuesta técnica de empresa_s La generación de resúmenes mediante IA se implementará sobre subtítulos existentes, no directamente sobre el vídeo, reduciendo coste computacional y mejorando trazabilidad. El resumen será un artefacto asociado al contenido, con estado, fecha, modelo usado, versión de prompt, idioma, longitud aproximada y usuario que solicitó regeneración si aplica. Se añadirá a la descripción del contenido de forma controlada, evitando sobrescribir manualmente información aportada por el autor sin registro. El procesamiento será asíncrono y se integrará con el sistema de colas de la Mediateca. Las tareas de nuevos contenidos tendrán prioridad sobre el backfill histórico. El cron consultará la carga del sistema local de IA con GPU y enviará tantas tareas como pueda soportar sin saturar el servicio. Esta regulación es clave: la IA no debe degradar subida, búsqueda, reproducción ni administración de contenidos. La instalación local del sistema de IA en servidores de la plataforma exige una comunicación segura. La Mediateca se comunicará con el servicio de inferencia por red interna o canal protegido, autenticando las peticiones y limitando el tamaño de entrada. No se enviarán datos a servicios externos. Se registrarán errores de generación, tiempos, tamaño del subtítulo y resultado, pero evitando conservar prompts completos con datos personales cuando no sea necesario. La calidad del resumen se controlará con plantillas de generación específicas para contenido educativo. Por ejemplo, para un vídeo de FP se puede producir un resumen breve, conceptos clave y advertencia si los subtítulos son insuficientes o de baja confianza. El usuario podrá eliminar o regenerar el resumen. La regeneración no será ilimitada: se podrán aplicar límites razonables para evitar consumo innecesario de GPU. La incorporación a la descripción se hará de manera visible y reversible. Se recomienda separar el texto generado por IA en un bloque identificado como resumen automático, para que el autor conserve su descripción original. Si el resumen se edita manualmente, quedará marcado como revisado. Mejora propuesta: incluir un indicador interno de confianza basado en longitud del subtítulo, idioma detectado y errores del proceso, para no publicar automáticamente resúmenes de baja calidad.

REQUISITO: II.1.3.11. Refactorizar código (MED11) Requerimiento EducaMadrid Página 89 de 192


Fecha: 21/05/2026

Se solicita realizar una refactorización del Código de la Mediateca con versiones de php nuevas y seguras, en servidores con el sistema operativo en su última versión y con los paquetes del sistema actualizados. Objetivos

- Simplificar el código y facilitar la incorporación de nuevos tipos de contenido: Simplificar el
código de la Mediateca para facilitar la incorporación de nuevos tipos de contenido.
- Mejorar la seguridad y escalabilidad: Mejorar la seguridad y escalabilidad de la Mediateca
para futuras versiones de PHP.
- Actualizar las librerías externas: Actualizar las versiones de las librerías externas utilizadas
en la parte cliente (JavaScript y/o CSS) y en el servidor (PHP).
- Incorporar mejoras de búsqueda: Incorporar mejoras de búsqueda mediante Elasticsearch.
- Diseño renovado y accesible: Diseño 100% renovado, accesible y adaptable al dispositivo
(responsive design). Propuesta técnica de empresa_s La refactorización es el elemento que da coherencia al resto de actuaciones MED. La Mediateca ha crecido incorporando tipos de contenido y funcionalidades que inicialmente no estaban previstas, lo que ha provocado código repetido, reglas dispersas y cambios que obligan a tocar múltiples sitios. La solución propuesta consiste en transformar gradualmente la aplicación hacia una arquitectura interna más ordenada, compatible con PHP moderno y con la forma actual de despliegue, pero sin una reescritura total que ponga en riesgo el servicio. La primera fase será un inventario técnico. Se identificarán módulos, pantallas, scripts, puntos de entrada, consultas críticas, librerías externas, funciones duplicadas, tratamiento de permisos, rutas de ficheros y lógica específica por tipo de contenido. A partir de ese mapa se priorizarán zonas por impacto: seguridad, duplicidad, frecuencia de cambio y relación con los nuevos MED. Cada intervención tendrá pruebas de regresión antes y después. El cambio estructural más importante será el modelo común de contenido. En lugar de que vídeo, audio, imagen, Scratch, eXeLearning o PDF resuelvan todo de forma independiente, se definirá una entidad lógica común con operaciones compartidas. Los adaptadores de tipo se limitarán a lo diferencial: cómo se previsualiza, qué ficheros derivados genera, qué validaciones específicas aplica, qué metadatos adicionales necesita y qué acciones particulares ofrece. Este patrón permite añadir un nuevo tipo de contenido creando un adaptador y no replicando formularios, permisos, búsquedas, borrado e indexación. Área actual con riesgo Refactorización propuesta Beneficio práctico Validaciones repetidas por Servicio común de validación Menos errores y criterios pantalla por tipo de contenido homogéneos Permisos repartidos en Autorizador central por acción Auditoría y seguridad más condicionales y contenido claras Consultas SQL Repositorios con parámetros y Reducción de SQL injection y concatenadas o duplicadas métodos reutilizables mantenimiento más simple Gestión de ficheros Servicio de almacenamiento Borrados y descargas más dispersa con rutas controladas seguros Búsquedas separadas por Capa de búsqueda común Evolución funcional sin caso SQL/Elastic duplicar lógica


La actualización de librerías externas se realizará con análisis de compatibilidad. En cliente, se revisarán JavaScript y CSS para sustituir versiones obsoletas, eliminar dependencias no usadas y evitar conflictos visuales. En servidor, se validará compatibilidad con versiones seguras de PHP, sustituyendo funciones eliminadas o desaconsejadas. Cada actualización de librería se acompañará de prueba funcional sobre subida, reproducción, edición, búsqueda, autenticación y administración. La seguridad se integrará en la refactorización. Se centralizará el filtrado de entrada, escaping de salida, protección CSRF, control de sesión, validación de ficheros, listas blancas de extensiones, consultas parametrizadas y comprobación de permisos. No se tratará como una capa añadida al final, sino como parte de cada servicio común. Esto es especialmente relevante en una aplicación PHP vanilla, donde el marco de seguridad depende en gran medida de disciplina de código y reutilización de componentes correctos. El rediseño responsive y accesible se abordará de forma compatible con la imagen institucional. No se limitará a cambiar estilos: se revisarán patrones de navegación, formularios, mensajes, reproductores, tablas de resultados y acciones frecuentes. Se buscará consistencia entre tipos de contenido, de modo que el usuario no perciba comportamientos distintos para operaciones equivalentes. La accesibilidad incluirá estructura semántica, etiquetas de formulario, contraste, navegación por teclado y textos alternativos cuando proceda. Para mantener viabilidad, no se refactorizará todo a la vez. Se aplicará la técnica de “estrangulamiento” del código legacy: los nuevos componentes comunes se usarán primero en las funcionalidades MED nuevas y después se irán conectando a funcionalidades existentes. Así se reduce el riesgo y se obtienen beneficios desde los primeros entregables. Cuando una zona legacy quede sustituida, se retirará el código duplicado y se documentará la nueva vía. Mejora propuesta: entregar un mapa vivo de deuda técnica MED, clasificado por seguridad, rendimiento, duplicidad y obsolescencia, que permita decidir futuras evoluciones con criterio técnico y no solo por incidencias.
##### 1.3.1.1.4. APARTADO: CONSULTAS LDAP (LDAP)
Requerimiento EducaMadrid Desarrollo de un aplicativo de uso interno para la consulta y gestión de cuentas de usuarios
###### 1.3.1.1.4.1. (LDAP1).
Objetivos y Funcionalidades:
- La aplicación debe permitir a los usuarios logados realizar consultas al LDAP de usuarios
mostrando toda la información disponible de los usuarios consultados.
- La aplicación debe mostrar los siguientes datos:
- Todos los datos disponibles en el LDAP.
- El estado del doble factor de autenticación (2FA) del usuario.
- La aplicación debe realizar consultas a la aplicación de bloqueados para consultar el
estado y el histórico de bloqueos del usuario.
- La aplicación debe realizar consultas a la base de datos central de usuarios para ver todos
los centros del usuario y su rol en cada uno de ellos, mostrando también información de niveles, clases, carga lectiva, etc.
- La aplicación debe tener una gestión para poner una contraseña temporal a usuarios, que
se reestablecerá por la original pasado un tiempo indicado.
- La aplicación debe tener un apartado para comprobar la contraseña de los usuarios.


Fecha: 21/05/2026

- La aplicación debe tener roles dentro del aplicativo, donde un administrador podrá
determinar que usuarios pueden cambiar la contraseña a cuentas especiales que serán las administradoras de otros aplicativos como aulas virtuales, WordPress, etc. Propuesta técnica de empresa_s Naturaleza del aplicativo y objetivo operativo Consultas LDAP se tratará como una herramienta interna de administración y diagnóstico de identidades de EducaMadrid. Al ser un desarrollo propio en PHP y estar protegido por acceso exclusivo bajo VPN, la propuesta no lo orienta como un portal general de usuario, sino como una consola controlada para personal autorizado. Esto condiciona la arquitectura: menos foco en exposición pública y más foco en trazabilidad, control de permisos, seguridad de operaciones privilegiadas y consistencia con los directorios corporativos. El aplicativo permitirá consultar toda la información disponible en el LDAP de usuarios, el estado del doble factor de autenticación, el histórico de bloqueos, los centros asociados, roles, niveles, clases y carga lectiva cuando proceda. Las consultas se resolverán mediante conectores diferenciados para LDAP, aplicación de bloqueados y base de datos central de usuarios, evitando mezclar lógica de presentación con lógica de acceso a datos. Se mantendrá una base de datos relacional propia del aplicativo para registrar usuarios autorizados, perfiles internos, configuración de permisos, acciones realizadas, resultados técnicos relevantes y operaciones sensibles. Esta base no duplicará el directorio corporativo; actuará como repositorio de auditoría y parametrización.

Autenticación contra LDAP de administración La autenticación de entrada al aplicativo se realizará contra el LDAP de administración, no contra el LDAP de usuarios. Esta mejora separa el universo de identidades administradoras del universo consultado, reduce la superficie de error y evita que una cuenta ordinaria de usuario pueda convertirse en vector de acceso a una herramienta interna. El LDAP de usuarios quedará reservado como fuente de consulta y operación controlada, no como mecanismo de login de la aplicación. El flujo será el siguiente: el usuario accede desde la red permitida o VPN, introduce sus credenciales, el backend valida la cuenta contra el LDAP de administración, recupera los grupos o atributos de autorización, crea una sesión PHP endurecida y asigna un rol aplicativo. A partir de ese momento, cada acción se valida en dos niveles: permiso funcional en la aplicación y permiso operativo sobre el tipo de cuenta consultada o modificada. Capa Control previsto Resultado esperado Red Acceso restringido a VPN, El aplicativo no queda listas de origen y TLS interno expuesto fuera del perímetro autorizado Identidad Login contra LDAP de Solo personal administrativo administración autorizado inicia sesión Autorización Roles internos y permisos Diferenciación entre consulta, sobre operaciones sensibles comprobación, cambio temporal y cuentas especiales


Fecha: 21/05/2026

Auditoría Registro de acción, cuenta Trazabilidad de actuaciones afectada, fecha, resultado y sobre identidades origen

Se configurarán sesiones con cookies HttpOnly y Secure, rotación de identificador tras login, caducidad por inactividad y bloqueo de sesión ante cambios de rol. La aplicación no almacenará contraseñas de los operadores; únicamente conservará identificadores, roles y trazas de actividad.

Modelo de consulta y presentación de información La pantalla de consulta se diseñará para responder a la necesidad real de soporte: localizar rápidamente una cuenta, entender su estado y decidir la acción correcta. La búsqueda permitirá filtrar por identificador de usuario, correo, nombre visible, centro u otros atributos autorizados. El resultado se presentará en bloques funcionales: identidad LDAP, pertenencia a centros, estado de 2FA, bloqueos, roles educativos y acciones disponibles. Para evitar pantallas inmanejables con todos los atributos LDAP en bruto, la interfaz diferenciará entre vista resumida y vista técnica. La vista resumida mostrará los datos operativos más relevantes. La vista técnica, accesible solo a perfiles autorizados, desplegará todos los atributos disponibles, incluyendo nombres técnicos, valores múltiples y fecha de última actualización si el origen la proporciona. Ejemplo corto: al consultar una cuenta docente, el operador verá si tiene 2FA activo, si se encuentra bloqueada, a qué centros pertenece, qué rol mantiene en cada centro y si puede aplicarse contraseña temporal. Si el usuario pertenece a varios centros, la información se agrupará por centro para no mezclar roles ni niveles. Contraseña temporal y gestión controlada de 2FA mediante emaux1 (mejora propuesta) La operación de contraseña temporal se implementará como una transacción funcional con estado, no como un simple cambio directo de atributo. Antes de aplicar la contraseña temporal se leerá y conservará de forma segura la información necesaria para restaurar la situación anterior: valor de contraseña o mecanismo equivalente permitido por el entorno, valor original del atributo emaux1, duración seleccionada, operador responsable, motivo y cuenta afectada. Durante el periodo en que la cuenta mantenga una contraseña temporal, el campo LDAP emaux1 se establecerá a none para deshabilitar temporalmente el 2FA. Esta acción es coherente con el objetivo operativo de permitir el acceso de recuperación cuando el usuario no puede completar el segundo factor. Finalizado el tiempo seleccionado, un proceso programado restaurará la contraseña original y repondrá el valor anterior de emaux1, dejando la cuenta en su estado previo. Estado Acción técnica Control de seguridad Solicitud El operador autorizado indica Validación de rol y usuario, duración y motivo comprobación de cuenta especial si aplica Preparación Lectura de estado actual de Registro de hash de control y contraseña y emaux1 cifrado de datos reversibles si el entorno lo permite Activación Cambio a contraseña Auditoría inmediata y aviso temporal y emaux1 = none visual de 2FA deshabilitado temporalmente


Fecha: 21/05/2026

Vigencia La tarea queda pendiente de Monitorización de caducidad y restauración reintento en caso de error Restauración Reposición de contraseña y Cierre de operación con emaux1 original resultado técnico y evidencia

El diseño contemplará fallos parciales. Si se cambia la contraseña pero falla la escritura de emaux1, la operación se marcará como incompleta y se revertirá o bloqueará la finalización según las capacidades del LDAP. Si el proceso de restauración falla, segenerará una alerta interna y la operación quedará en estado pendiente de intervención, evitando que una deshabilitación temporal de 2FA quede sin control. Mejora propuesta: incorporar un panel de “contraseñas temporales activas” con temporizador, cuenta afectada, operador y estado de restauración. Esta mejora facilita la supervisión sin añadir complejidad funcional y reduce el riesgo de olvidar operaciones abiertas. Comprobación de contraseña y cuentas especiales La comprobación de contraseña se realizará sin almacenar ni mostrar el secreto introducido. El aplicativo recibirá la contraseña en una petición protegida, realizará una validación bind o mecanismo equivalente contra el directorio correspondiente y devolverá únicamente un resultado de verificación: correcta, incorrecta, cuenta bloqueada, cuenta no encontrada o error técnico. Se evitará registrar el valor introducido en logs de aplicación, servidor web o trazas de depuración. Las cuentas especiales, como administradoras de Aulas Virtuales, WordPress u otros aplicativos, tendrán una política de permisos más restrictiva. Un administrador del aplicativo podrá definir qué operadores pueden actuar sobre estas cuentas, pero no bastará con tener permiso general de cambio de contraseña. La interfaz mostrará claramente que se trata de una cuenta especial y solicitará confirmación explícita antes de ejecutar cualquier operación sensible. Las pruebas incluirán usuarios ordinarios, usuarios con múltiples centros, usuarios bloqueados, cuentas con 2FA habilitado, cuentas sin 2FA, cuentas especiales y escenarios de error de conectividad con LDAP, base de datos central y aplicación de bloqueados. Además, se preparará una batería de pruebas específicas para validar que ninguna operación de diagnóstico modifica atributos por error. Las consultas de lectura se ejecutarán con credenciales técnicas de solo lectura cuando sea posible, y las operaciones de cambio de contraseña o modificación de emaux1 utilizarán una cuenta de servicio distinta, con permisos limitados a los atributos imprescindibles. Esta separación facilita auditorías posteriores y reduce el impacto de una credencial comprometida. La explotación diaria se acompañará de indicadores sencillos: número de consultas, operaciones temporales abiertas, restauraciones correctas, restauraciones con error, intentos denegados por rol y accesos fallidos. Estos indicadores no buscan fiscalizar usuarios finales, sino controlar el uso de una herramienta administrativa sensible y anticipar problemas de integración con LDAP o con servicios dependientes.
##### 1.3.1.1.5. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO EXELEARNING ONLINE
(EXE) Propuesta técnica de empresa_s


Fecha: 21/05/2026

Evolución de versión: de producción 2.9 a eXeLearning 4 El punto de partida será la versión 2.9 actualmente en producción. Aunque el pliego menciona la evolución a la versión 3.0 o superior, la solución propone orientar el trabajo hacia eXeLearning 4, al tratarse de una rama con reescritura profunda del código y mayor recorrido técnico. Esta decisión evita invertir esfuerzo principal en una versión intermedia y permite preparar una plataforma más limpia para integraciones futuras con Moodle, repositorios y servicios cloud. La migración no se planteará como sustitución brusca. Se mantendrá la versión 2.9 operativa mientras se instala, configura y valida eXeLearning 4 en un entorno paralelo. Los módulos de Moodle se parametrizarán para que la conmutación entre versiones pueda realizarse mediante cambio de URL o configuración, manteniendo la estrategia indicada en el pliego de evitar paradas. En caso de incidencia, el retorno a la versión anterior se limitará a restaurar el endpoint configurado y conservar evidencias del error.

Fase Trabajo principal Resultado Inventario Revisión de configuración 2.9, Mapa de compatibilidad y estilos, contenidos tipo y riesgos reales módulos Moodle en uso Instalación paralela Despliegue de eXeLearning 4 Entorno validable sin afectar con configuración institucional producción Adaptación Ajuste de módulos Moodle, Creación y edición desde estilos y publicación Moodle 4.5+ SCORM/sitio web Convivencia Pruebas con URL separada y Paso progresivo sin parada conmutación controlada Estabilización Corrección de incidencias y Servicio mantenible y soporte documentación de operación preparado

Integración con Moodle 4.5 y actividades Sitio web / SCORM La integración con Moodle 4.5.x y superiores se abordará desde la experiencia docente. El objetivo no es exponer toda la complejidad de eXeLearning dentro de Moodle, sino permitir crear y editar recursos de tipo Sitio web y SCORM con una interfaz de configuración simplificada. Las opciones habituales quedarán visibles por defecto; los parámetros avanzados se agruparán en secciones desplegables para no penalizar al usuario que solo necesita publicar un recurso educativo. Los módulos Moodle mod\_exeweb y mod\_exescorm se validarán frente a autenticación, permisos de curso, edición por roles docentes, almacenamiento del identificador de recurso, apertura del editor, retorno al curso, republicación y visualización por estudiantes. Se comprobará también el comportamiento con copias de seguridad y restauración de cursos, ya que los recursos enlazados no deben quedar apuntando a entornos obsoletos o URLs temporales. Ejemplo corto: un docente crea una actividad SCORM en Moodle, pulsa “editar con eXeLearning”, construye el recurso en eXeLearning 4, publica y vuelve al curso. Moodle conserva el enlace y los metadatos de actividad; eXeLearning conserva el proyecto editable; el alumno accede sin conocer la separación técnica entre ambos sistemas. Estilos institucionales y personalización de interfaz Se desarrollarán y adaptarán los estilos institucionales requeridos: EducaMadrid, EducaMadrid para presentaciones, EducaMadrid MAX, EducaMadrid MAX para presentaciones y Página 95 de 192


EducaMadrid DUA. En eXeLearning 4 se revisará la estructura real de temas y plantillas para no limitarse a trasladar CSS de versiones anteriores. La adaptación incluirá cabeceras, tipografías, espaciados, pie institucional, comportamiento responsive, contraste y presentación correcta en contenido exportado. La interfaz de la herramienta de autor se personalizará para reducir estilos visibles a los autorizados por EducaMadrid, aligerar opciones no necesarias y mantener consistencia visual. El pie institucional se cargará cuando el contenido se publique en servidores de la plataforma, evitando incrustar rutas rígidas o dependencias que impidan mover contenidos entre entornos. Mejora propuesta: añadir una plantilla “DUA ligero” orientada a contenidos accesibles de baja complejidad visual. No exige nuevas capacidades del motor, pero ofrece a los docentes una base clara con navegación simple, contraste adecuado y bloques preparados para texto alternativo, audio o apoyos visuales.

Reproductor integrado en la nube Nextcloud de EducaMadrid (mejora propuesta) Como mejora adicional se integrará el reproductor de eXeLearning directamente en la nube Nextcloud de EducaMadrid. La finalidad es que los materiales almacenados en el cloud puedan previsualizarse o reproducirse sin obligar al usuario a descargar paquetes, descomprimirlos o abandonar el entorno de trabajo. Esta integración aumenta la reutilización de contenidos y conecta la herramienta de autor con el espacio natural de almacenamiento docente. La solución se diseñará como una integración desacoplada: Nextcloud detectará paquetes o recursos eXeLearning mediante extensión, metadatos o estructura interna, y ofrecerá una acción de visualización. El visor cargará el recurso en modo seguro, con control de permisos de Nextcloud, sin copiar innecesariamente el contenido a otro repositorio. Cuando el recurso no pueda abrirse, se mostrará un mensaje claro y se conservará la opción de descarga. Para evitar riesgos de seguridad, el reproductor aplicará aislamiento mediante cabeceras adecuadas, restricciones de contenido activo cuando proceda y validación de rutas internas del paquete. Se revisará especialmente la ejecución de JavaScript incluido en contenidos educativos, la carga de recursos externos y el acceso a ficheros relativos dentro del paquete. Mejora propuesta: generar una miniatura o portada del contenido eXeLearning en Nextcloud para facilitar su identificación en listados. Es una mejora sencilla de experiencia de usuario y evita que todos los paquetes aparezcan como ficheros indistinguibles.

Pruebas, soporte y documentación La validación de EXE1 combinará pruebas funcionales, compatibilidad de contenidos y pruebas docentes guiadas. Se probarán recursos nuevos, recursos importados desde 2.9, publicación como sitio web, publicación SCORM, edición posterior, cambios de URL, permisos desde Moodle, visualización en navegadores habituales y reproducción desde Nextcloud. La documentación incluirá guía de instalación, guía de configuración de módulos Moodle, guía de estilos, procedimiento de conmutación 2.9/4, plan de reversión, incidencias conocidas y manual breve para soporte. El soporte se estructurará con un primer nivel capaz de identificar errores habituales de publicación, permisos o URL, y un nivel técnico para incidencias de integración. Se prestará especial atención a la compatibilidad de contenidos heredados. No todos los proyectos creados en 2.9 tendrán el mismo comportamiento en una rama reescrita. Por ello se seleccionará una muestra representativa de materiales reales: recursos con navegación simple, recursos con actividades interactivas, SCORM con seguimiento, contenidos con vídeos, materiales DUA y


Fecha: 21/05/2026

paquetes con estilos personalizados. Cada caso tendrá una ficha de resultado para diferenciar incidencias de contenido, limitaciones de la nueva versión y errores corregibles en la integración. El paso a eXeLearning 4 se acompañará de un criterio claro de aceptación: creación de recursos desde Moodle, edición posterior, publicación, visualización por alumnado, exportación, reproducción desde cloud y reversión controlada. Esta definición evita que la actualización se considere terminada solo por instalar la nueva versión.
##### 1.3.1.1.6. APARTADO: MEJORAS Y MANTENIMIENTO EN EL CORREOWEB (COR)
CorreoWeb se abordará como un servicio crítico de comunicación basado en Roundcube 1.6.9, con personalizaciones propias de EducaMadrid, plugins instalados, configuraciones de usuario y dependencias con otros servicios como calendarios, cloud, Empieza y sistemas de autenticación. La prioridad será mantener continuidad, datos y experiencia de usuario, evitando actualizaciones que rompan contactos, filtros, firmas, claves PGP o integraciones existentes.

REQUISITO: II.1.6.1. Adaptaciones a la última versión estable (COR1) Requerimiento EducaMadrid Se solicita adaptar al entorno de EducaMadrid la última versión estable del aplicativo correoweb para que los usuarios puedan gestionar sus cuentas de correo electrónico. Propuesta técnica de empresa_s La adaptación se ejecutará con un inventario previo de Roundcube 1.6.9: plugins activos, tema institucional, modificaciones locales, hooks utilizados, configuración IMAP/SMTP, libreta de direcciones, filtros, firmas, calendarios, claves PGP y tareas programadas. Este inventario permitirá distinguir qué debe mantenerse, qué puede reemplazarse por funcionalidad estándar y qué requiere adaptación específica. Se preparará una rama de actualización en la que cada modificación local se clasifique como configuración, plugin, tema, parche de núcleo o integración externa. La solución buscará sacar del núcleo todo lo posible. Cuando un cambio pueda implementarse como plugin o configuración, se evitará tocar código base de Roundcube. Cuando un parche sea inevitable, se documentará con diff, motivo, fichero afectado y prueba asociada. La verificación de servidores incluirá versión de PHP, extensiones requeridas, servidor web, base de datos, librerías criptográficas, límites de subida, sesiones, permisos de ficheros, colas o cron, conectividad IMAP/SMTP y conexión con servicios internos. Si el servidor actual no cumple requisitos, se trabajará con sistemas para generar un entorno actualizado y reproducible antes de migrar producción.

Requisito COR1 Cómo se resolverá Evidencia de validación Modificaciones actuales Inventario y migración a Matriz de cambios plugins/configuración cuando conservados sea viable Datos de usuario Pruebas de correos, Casos de prueba por perfil contactos, filtros, firmas y PGP Calendarios con aulas Validación de sincronización y Prueba de evento virtuales autenticación creado/modificado Cloud EducaMadrid Plugin de adjuntos desde Adjunto seleccionado sin Nextcloud descarga previa


Fecha: 21/05/2026

Seguridad Bloqueo por intentos, cifrado Informe de hardening de datos sensibles y revisión de cabeceras

Se implementarán los reintentos de correos programados con un estado persistente por envío: pendiente, en proceso, reintentando, enviado o error. El usuario podrá consultar el estado sin tener que interpretar trazas técnicas. Tras diez intentos fallidos, el mensaje quedará marcado como error de envío y el sistema conservará la causa técnica para soporte. La API securizada para restaurar contactos eliminados desde Empieza se diseñará con autenticación fuerte entre servicios, autorización por usuario afectado, validación de fechas y registro de auditoría. La API no permitirá recuperar datos de otros usuarios ni rangos temporales no autorizados. La respuesta diferenciará entre contactos restaurados, contactos no encontrados y errores de validación. La aplicación móvil basada en K-9/Thunderbird se personalizará con imagen corporativa y configuración simplificada. El usuario introducirá usuario y contraseña, y la aplicación precargará servidores, puertos, protocolos y seguridad. Se validará en Android y se documentarán límites respecto a notificaciones, certificados, políticas de bloqueo y convivencia con clientes de correo existentes. Mejora propuesta: añadir una pantalla de diagnóstico de cuenta para soporte, accesible solo a administradores, que verifique IMAP, SMTP, cuota, estado de bloqueo, último error de envío programado y estado de sincronización de calendarios. Reduce tiempos de resolución sin cambiar la experiencia de usuario final. El despliegue de COR1 se organizará mediante una doble validación: técnica y funcional. La validación técnica revisará instalación, librerías, permisos, logs, sesiones, rendimiento de base de datos y conectividad con servicios de correo. La funcional se centrará en operaciones de usuario: leer, responder, adjuntar, buscar, firmar, gestionar contactos, usar calendarios, programar envíos y acceder desde móvil. Cualquier diferencia frente al comportamiento actual se clasificará como cambio aceptado, mejora o incidencia a corregir antes de producción. Para proteger la continuidad, la actualización se realizará inicialmente sobre copia de configuración y datos de prueba anonimizada o acotada. La ventana de puesta en producción incluirá copia de seguridad previa, validación posterior y criterio de vuelta atrás. Si se detectan errores graves en autenticación, acceso a buzones, contactos o envío, el procedimiento de reversión tendrá prioridad sobre cualquier corrección en caliente.

REQUISITO: II.1.6.2. IA en correoweb - Prueba de generación de resúmenes de correos (COR2) Requerimiento EducaMadrid Se solicita adaptar al entorno de EducaMadrid la última versión estable del aplicativo correoweb para que los usuarios puedan gestionar sus cuentas de correo electrónico. Propuesta técnica de empresa_s La generación de resúmenes se implementará como funcionalidad bajo petición, asíncrona y limitada a usuarios autorizados. Se evitará procesar automáticamente el buzón completo o intervenir en la entrega de correo. El usuario solicitará el resumen desde la vista del mensaje y el sistema enviará una tarea al componente de IA, mostrando un estado de generación y, al finalizar, Página 98 de 192


el resumen al principio del correo con una marca visible que indique que se trata de texto generado automáticamente. La Consejería dispone de licencia del plugin xai; la propuesta lo utilizará como base funcional, adaptándolo a las necesidades de EducaMadrid y sustituyendo o parametrizando su backend de inferencia para apuntar a la instalación local vLLM con modelo Mistral. Esta aproximación reduce el esfuerzo de desarrollo desde cero y, al mismo tiempo, mantiene el control de datos dentro de la infraestructura de la plataforma. El conector con vLLM encapsulará URL interna, autenticación de servicio, parámetros de modelo, límites de tokens, temperatura, timeout, reintentos y tratamiento de errores. El plugin no conocerá detalles de infraestructura más allá de una configuración administrada; de este modo, el modelo Mistral o sus parámetros podrán ajustarse sin modificar la interfaz de Roundcube. El resumen se almacenará en la base de datos de CorreoWeb con caducidad configurable. Se guardará el identificador del mensaje, usuario, fecha de generación, versión de prompt, modelo utilizado y estado. No se almacenará más contenido del necesario y se permitirá borrar automáticamente resúmenes antiguos. Si el mensaje cambia, se reenvía o desaparece del buzón, el resumen se tratará como información derivada y no como sustituto del contenido original. Ejemplo corto: un docente abre un correo largo de coordinación, pulsa “Generar resumen”, el sistema crea una tarea, envía a vLLM el contenido normalizado con instrucciones de resumen, recibe la respuesta de Mistral y la muestra en una caja superior con el texto “Resumen generado por IA”. Si el servicio IA no responde, el correo se sigue leyendo con normalidad y se informa del error sin bloquear la pantalla. Mejora propuesta: incluir un botón “el resumen no es correcto” que registre una valoración simple. No requiere entrenar el modelo ni compromete al desarrollo, pero aporta señales útiles para ajustar prompts, límites y casos de uso. Se mostrarán por lo tanto botones de eliminar el resumen o rehacerlo. El tratamiento previo del correo será determinante. Antes de enviarlo al modelo se eliminarán cabeceras no necesarias, firmas repetidas, cadenas citadas si el usuario solicita resumir solo el último mensaje y elementos HTML sin valor semántico. Esta normalización reduce tokens, mejora calidad de respuesta y evita que el resumen dedique espacio a información irrelevante. La administración dispondrá de parámetros de control: tamaño máximo de correo resumible, número de resúmenes por usuario, caducidad de resúmenes, habilitación por centros y mensaje de aviso legal. Estos parámetros se documentarán para que el servicio pueda ajustar la funcionalidad conforme aumente el piloto sin necesidad de nuevos despliegues.

REQUISITO: II.1.6. 3. IA en correoweb - Redacción de correos (COR3) Requerimiento EducaMadrid Implementación de un sistema de generación de resúmenes de correos electrónicos dentro del aplicativo de correo de la plataforma educativa EducaMadrid que permita evaluar su viabilidad de cara a todos los usuarios. El sistema utilizará una instalación de IA local y cumplirá con los siguientes requisitos específicos. Propuesta técnica de empresa_s La redacción asistida se integrará en la pantalla de composición mediante un botón visible pero no invasivo. Al pulsarlo se abrirá un modal en el que el usuario podrá indicar instrucciones, nombre


Fecha: 21/05/2026

del remitente, nombre del destinatario, estilo, longitud, creatividad e idioma. La respuesta de IA se insertará como borrador editable, nunca como envío automático. El usuario conservará el control final sobre el contenido enviado. También aquí se partirá del plugin xai licenciado, adaptándolo para utilizar vLLM local con Mistral. Se revisarán los puntos de integración con Roundcube 1.6.9, especialmente hooks de composición, carga de JavaScript/CSS, internacionalización, permisos por usuario y persistencia estadística. El modo desarrollador mostrará a administradores los prompts de sistema y usuario, parámetros enviados y respuesta recibida, con acceso restringido y evitando exponer datos a perfiles no autorizados. Los ejemplos de solicitudes se gestionarán mediante configuración fechada o reglas simples. Por ejemplo, en diciembre se podrá sugerir “redactar felicitación navideña para familias”; al inicio de curso, “redactar bienvenida al alumnado”; y en periodos de evaluación, “redactar aviso de entrega de tareas”. Estos ejemplos serán ayudas de uso, no plantillas cerradas. Se aplicarán límites por centro, grupo y usuario: número de correos generados por periodo, longitud máxima de prompt, tokens de salida, frecuencia de peticiones y disponibilidad por colectivos. Esto permite un despliegue paulatino, empezando por grupos piloto de profesorado y ampliando en función de resultados y capacidad del servicio vLLM. Elemento del modal Tratamiento técnico Ejemplo de uso Estilo Parámetro controlado que Formal, cercano, breve, ajusta el prompt institucional Longitud Límite de salida y orientación Tres párrafos o respuesta semántica corta Creatividad Temperatura o instrucción Más conservador para equivalente comunicaciones oficiales Idioma Instrucción explícita al modelo Español, inglés u otro idioma autorizado Modo desarrollador Vista restringida para Depurar prompt o respuesta administradores inesperada

Mejora propuesta: añadir una opción “mantener tono institucional” activada por defecto para cuentas de centro o comunicaciones masivas. Es una mejora pequeña de prompt y configuración que reduce salidas demasiado informales. También la generación en distintos idiomas de los correos. La redacción asistida incluirá mensajes de ayuda que recuerden al usuario que debe revisar la respuesta antes de enviarla. También se evitará que el plugin tome destinatarios reales como única fuente de contexto: el usuario podrá indicar destinatario o propósito, pero la IA no enviará ni seleccionará direcciones. Esta separación entre asistencia de escritura y acción de envío reduce riesgos operativos. En términos de mantenimiento, los prompts se versionarán de manera independiente al código. Cada versión incluirá fecha, finalidad y cambios introducidos. Si una modificación empeora la calidad de los textos, se podrá volver a una versión anterior del prompt sin reinstalar el plugin.

REQUISITO: II.1.6. 4. IA en correoweb - Reescritura de correos (COR4) Requerimiento EducaMadrid


Desarrollo de un plugin para el aplicativo de correo que integre inteligencia artificial (IA) en la reescritura de correos electrónicos. Este plugin permitirá a los usuarios mejorar la calidad de sus correos electrónicos mediante diversas opciones de reescritura y corrección. Propuesta técnica de empresa_s La reescritura se orientará a mejorar un texto ya existente. A diferencia de COR3, no parte de una instrucción vacía, sino del contenido redactado por el usuario. El botón de reescritura abrirá un modal con el texto actual y opciones claras: corregir gramática, corregir ortografía, hacer más largo, hacer más corto o cambiar estilo. La respuesta reemplazará o copiará el texto según decisión del usuario, evitando pérdida accidental de contenido. La integración con xai, vLLM local y Mistral se reutilizará, pero con prompts específicos para edición. La solución separará plantillas de prompt para resumen, redacción y reescritura, ya que cada caso tiene riesgos distintos. En reescritura se indicará al modelo que respete nombres propios, fechas, cifras, direcciones de correo y datos administrativos, minimizando cambios semánticos no solicitados. La interfaz ofrecerá comparación antes/después cuando el cambio sea amplio. Para correcciones simples se podrá insertar directamente la propuesta, pero cuando se solicite “reescribir con otro estilo” se mostrará una vista previa. Esta decisión mejora la confianza y evita que el usuario sustituya un texto sensible sin revisarlo. Los límites de uso se compartirán con COR3 pero se contabilizarán por tipo de acción. Esto permitirá conocer si el consumo viene de generación completa o de corrección de textos existentes. La base de datos almacenará estadísticas de uso y metadatos técnicos, no el contenido completo de los correos salvo que sea imprescindible para depuración autorizada y con medidas de protección. Mejora propuesta: incorporar una opción “no cambiar información factual” junto a la reescritura. Técnicamente se implementa como instrucción de prompt y reduce uno de los riesgos principales de la IA generativa en comunicaciones educativas. Se contemplará un comportamiento específico para textos largos. Si el correo supera el límite configurado, el plugin propondrá reescribir por fragmentos o acortar primero el texto. Esto evita timeouts, respuestas incompletas o costes innecesarios de inferencia. La interfaz informará de forma clara de la causa y no presentará un fallo genérico. La comparación antes/después podrá resolverse inicialmente con una vista en dos bloques, sin implementar un diff complejo palabra por palabra. Esta solución es suficiente para que el usuario evalúe el resultado y mantiene bajo control el esfuerzo de desarrollo.
##### 1.3.1.1.7. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO DE WORDPRESS
MULTISITE (WPM)
El servicio WordPress debe abordarse como una instalación de gran tamaño, con aproximadamente 1.000 centros o instalaciones, código compartido y bases de datos independientes por centro. Esta arquitectura exige separar cuidadosamente las actuaciones sobre el código común, los plugins y temas compartidos, las configuraciones globales y las particularidades de cada centro. Cualquier actualización debe diseñarse para ser repetible, reversible y observable antes de afectar al conjunto de sedes. La solución se organizará en torno a una cadena de actualización controlada: inventario, empaquetado, validación sobre centros piloto, despliegue escalonado, verificación posterior y


cierre documental. El hecho de que los temas se apoyen en temas hijo permite preservar personalizaciones sin modificar temas base. Se revisará también el plugin que unifica cambios de core para integrarlo en el flujo de actualización y evitar divergencias entre lo desplegado en Git y lo realmente activo en producción.

REQUISITO: II.1.7.1. Mantenimiento y Actualización de WordPress Multisite (WPM1) Requerimiento EducaMadrid

- Se requiere actualizar la versión del aplicativo WordPress Multisite, incluyendo el core,
temas y plugins, con la posibilidad de hacerlo por separado.
- El servicio debe ser parado por un tiempo inferior a 30 minutos.
- Se debe preparar un sistema en el servidor Git de EducaMadrid que permita automatizar
las futuras subidas de versión del aplicativo con sus temas y plugins.
- Se debe considerar que hay un plugin que unifica los cambios del core y que los temas no
están modificados, sino que cada tema tiene un tema hijo.
- El proceso de actualización debe ser realizado de manera segura y sin afectar la
disponibilidad del sitio. Propuesta técnica de empresa_s Para actualizar WordPress Multisite sin superar una parada de 30 minutos, se preparará un procedimiento de despliegue por fases. La actualización no se ejecutará como una operación manual sobre producción, sino como una promoción de artefactos versionados desde el servidor Git de EducaMadrid. El repositorio contendrá el core, plugins, temas base, temas hijo, scripts de comprobación y un manifiesto de versiones que permita saber exactamente qué componente se ha desplegado en cada liberación. Antes de cada actualización se generará una matriz de compatibilidad entre versión de WordPress, versión de PHP, plugins críticos, temas activos y dependencias externas. La validación se realizará sobre una copia representativa de centros: un centro con baja personalización, otro con elevado volumen de contenidos, otro con formularios o plugins intensivos y otro con tema hijo altamente personalizado. Esta selección permite detectar errores que no aparecerían en una instalación limpia. Prechequeo automático: versión PHP, permisos de escritura, integridad de plugins, estado de cron, tamaño de cada BBDD y disponibilidad del almacenamiento compartido. Modo de mantenimiento corto y planificado, con despliegue de código previamente preparado y migraciones de BBDD ejecutadas solo cuando sean imprescindibles. Postchequeo por centro: carga de portada, acceso a administración, renderizado de tema hijo, verificación de plugins clave y registro de errores PHP. Ejemplo: si se actualiza un plugin usado por todos los centros, el pipeline desplegará primero el paquete en preproducción, ejecutará pruebas sobre una muestra de bases de datos anonimizadas, comprobará que no aparecen errores fatales y solo entonces permitirá promoverlo al entorno productivo. En producción, el despliegue se realizará sobre código compartido, reduciendo la duración de la ventana y evitando repetir una operación por centro. Mejora propuesta: incorporar un panel técnico interno de versiones por componente, que muestre core, plugins, temas y última verificación por centro. Esta mejora no modifica la experiencia de usuario y facilita localizar rápidamente centros con incidencias después de una actualización.


Fecha: 21/05/2026

REQUISITO: II.1.7.2. Incorporación Automatizada de Licencias de Temas y Plugins (WPM2) Requerimiento EducaMadrid
- Se requiere trabajar en un sistema que permita incorporar las licencias de temas y plugins
adquiridas de manera automatizada sin intervención de los usuarios en el entorno multisite.
- Se deben considerar plugins como PostGrid y Akismet como ejemplo de casos a resolver.
- El sistema debe ser capaz de leer y aplicar las licencias de manera automática, sin requerir
intervención humana. Propuesta técnica de empresa_s La gestión de licencias de temas y plugins se resolverá mediante un almacén seguro de licencias y un adaptador por producto. El objetivo no es que cada usuario o centro introduzca claves, sino que el sistema pueda aplicarlas de forma centralizada, trazable y sin exponer secretos. Para productos como PostGrid o Akismet se implementará un mecanismo que detecte el plugin, consulte la licencia correspondiente y la aplique mediante la API, opción de configuración o mecanismo interno soportado por cada componente. La solución tendrá una capa de normalización porque no todos los plugins tratan las licencias del mismo modo. Algunos almacenan claves en opciones globales, otros por sitio, otros validan contra servidores externos y otros exigen activación por dominio. Se documentará cada caso y se evitarán modificaciones directas no controladas en tablas de WordPress cuando el plugin ofrezca una vía estable. Elemento Tratamiento técnico previsto Control Licencias Almacenamiento cifrado y aplicación No exposición a usuarios globales desde tarea administrativa. ni logs. Licencias por Resolución por site\_id/dominio y Auditoría de altas, bajas y centro activación selectiva. cambios. Plugins con Adaptador específico para validar y Registro de código de API propia renovar. respuesta y fecha. Plugins sin Configuración asistida documentada y Revisión manual API clara prueba de no regresión. controlada.

Mejora propuesta: crear una tarea programada que avise de licencias próximas a caducar o pendientes de activación. Es una mejora de bajo riesgo, pero evita incidencias masivas por expiraciones no detectadas.

REQUISITO: II.1.7.3. Configuración del WAF de Forti (WPM3) Requerimiento EducaMadrid
- Se requiere trabajar conjuntamente con el departamento de sistemas para encontrar una
configuración correcta del WAF de Forti que permita encontrar un equilibrio entre seguridad y experiencia de usuario.
- La configuración debe ser ajustada para permitir una experiencia de usuario óptima sin
comprometer la seguridad del sitio. Propuesta técnica de empresa_s


La configuración del WAF se trabajará junto con sistemas con un enfoque de ajuste fino. En una red de unos 1.000 centros no basta con activar reglas genéricas: hay que distinguir tráfico legítimo de administración, edición de entradas, subidas de imágenes, constructores visuales, llamadas Ajax de plugins y tráfico potencialmente malicioso. Se propondrá un periodo de observación en modo detección para recopilar falsos positivos antes de pasar a bloqueo efectivo en reglas sensibles. Se definirá un catálogo de rutas WordPress con tratamiento diferenciado: login, administración, wp-json, admin-ajax, subida de ficheros, carga de recursos estáticos y llamadas de plugins. Las reglas del WAF se ajustarán para proteger frente a patrones típicos -inyección SQL, XSS, path traversal, abuso de login, subida de ficheros no permitidos- sin bloquear la operativa docente ordinaria. Mejora propuesta: crear un procedimiento de correlación entre eventos del WAF y logs de WordPress, de forma que un bloqueo pueda vincularse a site\_id, usuario autenticado, URL y regla aplicada. Esto reduce tiempos de diagnóstico y evita desactivar reglas de seguridad por falta de contexto.

REQUISITO: II.1.7.4. Reemplazo del Plugin WCcaptcha (WPM4) Requerimiento EducaMadrid
- Se requiere eliminar el plugin WCcaptcha del entorno y sustituirlo por una solución
equivalente.
- La solución equivalente debe ser compatible con la versión actual del sitio y no afectar la
experiencia de usuario. Propuesta técnica de empresa_s La retirada de WCcaptcha se realizará con una evaluación previa de todos los puntos donde se utiliza: formularios de login, comentarios, recuperación de contraseña, formularios de plugins y pantallas de administración expuestas. La sustitución debe ser compatible con el entorno multisite, no introducir dependencias externas innecesarias y mantener una experiencia accesible para usuarios de centros educativos. Se valorará una solución de captcha o antispam que permita configuración centralizada y activación selectiva por sitio, preferentemente con mecanismos de bajo impacto visual, control de tasa, honeypot y validación de comportamiento. Antes del cambio se ejecutará un inventario de hooks y shortcodes asociados a WCcaptcha para eliminar dependencias residuales y evitar errores al desactivar el plugin. Mejora propuesta: complementar la sustitución del captcha con limitación de intentos y protección progresiva por IP/usuario en formularios críticos. Así se reduce el abuso sin cargar al usuario con desafíos innecesarios en todos los accesos.

REQUISITO: II.1.7.5. Integración con el SSO de EducaMadrid (WPM5) Requerimiento EducaMadrid

- Se requiere integrar el aplicativo con el sso de EducaMadrid para el login de los usuarios.
- Deberán maneterse todas las funcionalidades originales del aplicativo.
- Se detectará el cierre de sesión en otros aplicativos provocando el cierre en el wordpress.
- Deberá incorporar los mecanismos de 2FA.


Propuesta técnica de empresa_s La integración con el SSO se diseñará respetando las funcionalidades nativas de WordPress y el modelo multisite. El inicio de sesión se delegará en EducaMadrid, pero se mantendrán los roles, permisos y capacidades de WordPress. El sistema deberá mapear la identidad autenticada con el usuario local correspondiente, resolver su pertenencia al centro o sitio y aplicar la autorización sin crear cuentas duplicadas. El cierre de sesión se tratará como parte del ciclo completo de autenticación. WordPress deberá detectar cierres realizados desde otros aplicativos y finalizar la sesión local, evitando estados inconsistentes donde el usuario figure desconectado en la plataforma pero mantenga una sesión activa en WordPress. Para ello se integrará la lógica de logout centralizado con limpieza de cookies, tokens y sesiones PHP/WordPress. La incorporación de SSO permitirá además ofrecer mecanismos de 2FA a los usuarios de WordPress, apoyándose en las capacidades de autenticación central de EducaMadrid . Esta mejora es especialmente valiosa en perfiles de administración de centro, donde una cuenta comprometida podría afectar a la web institucional del centro. Mapeo de atributos SSO a usuario WordPress: identificador único, centro, correo y roles permitidos. Conservación de permisos existentes: no se reemplazará el modelo de capacidades de WordPress, sino que se alimentará de la identidad central. Activación progresiva: piloto en centros seleccionados, coexistencia temporal con login local controlado y retirada posterior de accesos no necesarios. Mejora propuesta: habilitar una política de 2FA obligatoria para administradores y editores con permisos elevados, dejando perfiles de menor riesgo sujetos a la política general de EducaMadrid. La mejora aumenta seguridad sin imponer fricción innecesaria a todos los usuarios.
##### 1.3.1.1.8. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO DE FORMULARIOS
(FOR) Requerimiento EducaMadrid Adaptar y optimizar el entorno de formularios para mejorar su rendimiento y conectarlo con el SSO de EducaMadrid, asegurando una experiencia de usuario fluida y segura (FOR1). Propuesta técnica de empresa_s El servicio de Formularios se abordará como una instalación de LimeSurvey 6.14.1, con una base de datos que puede acumular miles de tablas por el propio modelo de encuestas, respuestas, tokens, archivos asociados y encuestas históricas. El objetivo será mantener el aplicativo actualizado, conectado al SSO de EducaMadrid y optimizado para que el crecimiento de tablas no degrade consultas, administración ni tareas programadas. El mantenimiento comenzará con una fotografía técnica del entorno: versión exacta de LimeSurvey, plugins activos, plantillas modificadas, tamaño de base de datos, número de encuestas activas e inactivas, tablas huérfanas, índices existentes y tiempos de respuesta de consultas habituales. Esta foto será la base para separar actuaciones de actualización, limpieza y rendimiento. La conexión con SSO se integrará preservando los permisos internos del aplicativo. El flujo de login deberá reconocer usuarios de EducaMadrid y mantener la gestión de permisos sobre Página 105 de 192


encuestas, grupos y administración. Para el cierre de sesión se reutilizará el mecanismo del aplicativo Avisos, tal como solicita el pliego, de manera que un cierre central se refleje también en Formularios. La optimización de BBDD tendrá un enfoque conservador. En LimeSurvey no se pueden eliminar tablas solo por antigüedad sin conocer el estado de la encuesta, la necesidad de conservación de respuestas y la existencia de exportaciones pendientes. Se diseñará un script anual parametrizable que actúe sobre criterios acordados: año, estado de encuesta, última modificación, existencia de copias de seguridad y exclusiones manuales. Inventariar encuestas y tablas asociadas, diferenciando encuestas activas, expiradas, archivadas y huérfanas. Generar copia de seguridad selectiva antes de eliminar, con registro de tablas incluidas, tamaño liberado y responsable de ejecución. Ejecutar limpieza en modo simulación, mostrando impacto estimado antes de la eliminación real. Aplicar eliminación controlada y validar integridad del panel de administración y del histórico conservado. En rendimiento, se revisarán índices de tablas de respuestas y metadatos, consultas lentas, tablas temporales y configuración de motor MySQL/MariaDB. Las mejoras se probarán con volúmenes representativos, no solo sobre encuestas pequeñas. Por ejemplo, una encuesta anual con miles de respuestas y múltiples preguntas de texto largo se usará para comprobar exportación, listado de respuestas y filtros administrativos. La adaptación de imagen institucional se implementará en plantillas compatibles con LimeSurvey 6.14.1, separando estilos propios de código del core para facilitar futuras actualizaciones. No se modificarán ficheros base si existe una vía de tema o extensión soportada. Mejora propuesta: añadir un informe de salud de Formularios con número de encuestas activas, encuestas cerradas, tablas candidatas a limpieza, tamaño total de BBDD y últimas tareas ejecutadas. Esta mejora facilita operación y evita que el mantenimiento sea reactivo.
##### 1.3.1.1.9. APARTADO: MEJORAS Y MANTENIMIENTO EN EMPIEZA (EMP)
Requerimiento EducaMadrid Mejorar el aplicativo EMPieza implementando nuevas funcionalidades y optimizando su rendimiento, con el fin de proporcionar una experiencia de usuario más eficiente y completa (EMP1). Propuesta técnica de empresa_s EMPieza es un desarrollo propio en PHP con frameworks, por lo que la solución combina evolución funcional, revisión arquitectónica y refuerzo de disponibilidad. El aplicativo actúa como punto de entrada a servicios de EducaMadrid y concentra integraciones con aulas virtuales, calendario, correo, mediateca, retransmisiones, grupos, avisos, boletines y gestión de usuarios. La intervención debe mantener la continuidad de uso y evitar que nuevas funcionalidades conviertan la portada en un bloque rígido difícil de mantener. La alta disponibilidad se abordará separando responsabilidades. Los frontales PHP deberán poder escalar horizontalmente detrás del balanceador, mientras que el servicio de websocket quedará desacoplado en un componente propio, con configuración explícita de sesiones, canales, timeouts


Fecha: 21/05/2026

y reconexión. La aplicación no deberá depender de almacenamiento local de sesión en un único frontal; se revisará el uso de sesiones compartidas, cachés y colas. Como mejora técnica se propone llevar la base de datos a una arquitectura de alta disponibilidad con Galera Cluster, siempre que las características del motor y el patrón de escritura del aplicativo lo permitan tras una fase de validación. El objetivo no es introducir complejidad innecesaria, sino eliminar puntos únicos de fallo y preparar el servicio para crecer. Se revisarán transacciones, bloqueos, claves primarias, uso de AUTO\_INCREMENT y escrituras concurrentes antes de proponer el paso a Galera en producción. Área de EMPieza Solución planteada Ejemplo de implementación Bloques de Modelo modular con permisos Bloque Favoritos editable por portada por bloque y configuración por usuario y bloque Avisos perfil. alimentado desde servicio central. Calendario Agregación de CalDAV, Etiqueta de origen: Correo, AV calendario de correo y eventos multisite, AV moodlemisc o de aulas virtuales. grupo EMPieza. Grupos Gestión separada de listado, Profesor comparte grupo público integrantes, importación CSV y de centro sin duplicar miembros. reutilización. Retransmisiones Creación guiada de salas Alta de punto Wowza al iniciar y Jitsi/Wowza y eventos baja automática al finalizar. asociados. Logs de Registro consultable por el Histórico de accesos a correo, seguridad usuario y endpoint para aulas virtuales y EMPieza. servicios.

Las nuevas funcionalidades de favoritos, notas, eventos, boletines y avisos se desarrollarán como módulos independientes. Cada módulo tendrá permisos, datos propios, endpoint documentado y pruebas funcionales. De esta manera se evita que la portada sea una página monolítica con lógica mezclada de todos los servicios. La conexión con aulas virtuales exigirá diferenciar Moodle multisite y moodlemisc. Los eventos de curso o grupo se normalizarán antes de mostrarse en EMPieza, de modo que el usuario vea un calendario coherente sin depender de detalles internos de cada Moodle. En la mensajería interna se aplicará un criterio de lectura segura: EMPieza mostrará mensajes relevantes sin asumir funciones de administración que correspondan al aula virtual. La gestión de retransmisiones se resolverá como un flujo completo: selección de tipo, invitación a usuarios o grupos, creación de evento, notificación por correo, alta dinámica de punto de publicación si aplica, selección de interacción y cierre con limpieza de recursos. Para Jitsi se incorporará límite temporal y para Wowza se contemplará la posibilidad de embeber retransmisiones en páginas externas con control de permisos. En ciberseguridad se revisará sanitización, autorización por endpoint, CSRF, XSS, logs de cambios de contraseña, trazas de login y tratamiento de credenciales registradas para comunicación con otros aplicativos. La API para recibir cambios de contraseña desde el Portal


deberá validar origen, firma o token, idempotencia y almacenamiento mínimo de información sensible. Mejora propuesta: además de Galera para la BBDD, incorporar una pantalla de estado interno para administradores con salud de websocket, latencia de BBDD, estado de colas, últimos errores de integración y versión de librerías jQuery/Bootstrap cargadas. Aporta operación diaria sin afectar al usuario final.
##### 1.3.1.1.10. APARTADO: MEJORAS Y MANTENIMIENTO EN BUSCADOR DE AULAS Y CURSOS
(BUS) Requerimiento EducaMadrid Crear un nuevo aplicativo que integre las funcionalidades de los dos aplicativos existentes: "Buscador de Aulas Virtuales" y "Buscador de Cursos". El nuevo aplicativo permitirá realizar búsquedas combinadas y proporcionar una experiencia de usuario más coherente y eficiente (BUS1). Mejorar y mantener los servicios de retransmisión y videoconferencia, asegurando un funcionamiento óptimo, una experiencia de usuario mejorada y la integración con otros sistemas de la plataforma EducaMadrid. Propuesta técnica de empresa_s El nuevo Buscador debe integrar dos visiones que hoy existen separadas: búsqueda de aulas virtuales y búsqueda de cursos. Actualmente está desarrollado en PHP con base de datos MySQL dentro del aplicativo MaMood, por lo que la solución debe tratarlo como una extracción/evolución funcional desde un entorno de gestión interna hacia un aplicativo más claro, mantenible y preparado para consultas combinadas. La propuesta consiste en construir el buscador sobre el framework PHP que se está implantando en la plataforma, definiendo una capa de acceso a datos que lea de las fuentes actuales sin acoplar la interfaz a las tablas internas de MaMood. Esto permitirá evolucionar la UI, los filtros y el motor de búsqueda sin arrastrar toda la lógica de administración de MaMood al nuevo aplicativo. La búsqueda combinada se diseñará mediante un modelo de índices funcionales. Las aulas virtuales tendrán atributos como centro, código, tipo, localidad, etapa o visibilidad. Los cursos abiertos tendrán título, temática, centro, descripción, etiquetas, disponibilidad y origen. Con estos datos normalizados será posible resolver casos como: buscar cursos de matemáticas disponibles en centros de una localidad concreta o localizar aulas abiertas asociadas a un tipo de centro determinado. Capa de consulta eficiente sobre MySQL, con índices adecuados y paginación obligatoria en resultados. Validación estricta de parámetros de búsqueda para evitar inyección SQL y consultas no acotadas. Resultados agrupados por tipo, con explicación clara del origen: aula virtual, curso abierto o coincidencia combinada. Separación entre filtros de usuario y filtros técnicos internos, evitando exponer identificadores sensibles. Para rendimiento se evitarán consultas con LIKE indiscriminado sobre campos grandes cuando el volumen crezca. Se planteará una tabla materializada o índice de búsqueda regenerable que


contenga los campos necesarios para consulta pública. Esta tabla se actualizará mediante tareas programadas o eventos de cambio desde MaMood, reduciendo carga sobre las tablas operativas. Ejemplo: ante la búsqueda “matemáticas IES Móstoles”, el buscador no lanzará consultas independientes sin límite, sino que normalizará términos, aplicará filtros de localidad/tipo si se detectan, consultará el índice y devolverá resultados ordenados por relevancia funcional: cursos abiertos con coincidencia de título, aulas de centros de Móstoles y resultados parciales relacionados. Mejora propuesta: incorporar un modo de “búsquedas frecuentes sin resultados” para administradores. Registrar de forma agregada qué términos no devuelven resultados ayuda a mejorar etiquetas, títulos y datos publicados, sin almacenar información personal del usuario.
##### 1.3.1.1.11. APARTADO: MEJORAS Y MANTENIMIENTO DE LOS SERVICIOS DE
RETRANSMISIÓN Y VIDEOCONFERENCIA (VID)
Los servicios de retransmisión y videoconferencia se tratarán como un ecosistema de tecnologías distintas, no como una única aplicación. Wowza, Jitsi, BigBlueButton y PeerTube tienen objetivos, arquitectura, escalabilidad y riesgos diferentes. La solución será independiente para cada servicio, manteniendo una visión común de seguridad, monitorización, integración con Moodle/EMPieza/Mediateca e imagen institucional.

REQUISITO: II.1.11.1. Mantenimiento de Wowza (VID1) Requerimiento EducaMadrid
- Eliminar Retransmisiones Integradas en Mediateca:
o Desactivar y eliminar la funcionalidad de retransmisiones integradas en el aplicativo Mediateca. o Asegurar que los usuarios no puedan acceder a esta funcionalidad obsoleta.
- Gestión Dinámica de Puntos de Publicación:
o Implementar una interfaz en EMPieza que permita a los administradores gestionar dinámicamente los puntos de publicación. o Proveer documentación detallada sobre cómo configurar y gestionar estos puntos de publicación.
- Actualización del Aplicativo Wowza:
o Actualizar Wowza a la última versión disponible. o Realizar pruebas exhaustivas para asegurar la compatibilidad y el correcto funcionamiento de todas las funcionalidades. o Proveer un informe detallado de los cambios realizados y las mejoras obtenidas. Propuesta técnica de empresa_s En Wowza se priorizará la estabilidad de emisiones en directo y la gestión dinámica de puntos de publicación desde EMPieza. La funcionalidad obsoleta de retransmisiones integradas en Mediateca se retirará de forma controlada: primero ocultación, después bloqueo de acceso y finalmente limpieza de rutas o componentes no usados, validando que los usuarios no queden con enlaces rotos sin mensaje explicativo. La actualización de Wowza se ejecutará con pruebas de compatibilidad sobre flujos reales: creación de punto de publicación, emisión, reproducción, finalización, eliminación y comportamiento ante corte de señal. Los puntos creados dinámicamente deberán tener nombre normalizado, caducidad, propietario, estado y limpieza automática. Se evitará que queden puntos huérfanos consumiendo recursos o generando confusión operativa. Página 109 de 192


Mejora propuesta: añadir un recolector de métricas por emisión -estado, duración, errores, audiencia estimada y bitrate- para que los administradores puedan diagnosticar incidencias de directo sin revisar manualmente logs dispersos.

REQUISITO: II.1.11.2. Mantenimiento de Jitsi (VID2) Requerimiento EducaMadrid
- Actualización de JitsiMeet:
o Actualizar JitsiMeet a la última versión disponible, conservando todas las funcionalidades actuales. o Realizar pruebas de compatibilidad y rendimiento.
- Personalización de Interfaz:
o Implementar una "mosca" o marca de agua con el logotipo de EducaMadrid. o Añadir logotipos y favicon personalizados. o Ocultar opciones de grabación para evitar el uso no autorizado.
- Integración con Sistema Centralizado de Avisos:
o Integrar JitsiMeet con el sistema centralizado de avisos de EducaMadrid para notificar a los usuarios sobre eventos y actualizaciones. o Proveer una interfaz para que los administradores puedan gestionar estos avisos.
- Mantenimiento de Instalaciones Diferentes:
o Privada: Asegurar que solo los usuarios de EducaMadrid puedan acceder a esta instalación. o Semi-privada: Permitir el acceso a usuarios de EducaMadrid e invitados, con controles de acceso adecuados. Propuesta técnica de empresa_s La actualización de Jitsi Meet se realizará conservando las tres instalaciones con comportamiento diferenciado: privada, semiprivada y Moodle. La privada quedará restringida a usuarios de EducaMadrid, la semiprivada permitirá invitados bajo control y la integración Moodle mantendrá acceso exclusivo desde aulas virtuales, con compatibilidad visual con modo claro y oscuro. La personalización institucional incluirá logotipos, favicon, marca de agua y ocultación de opciones de grabación no autorizadas. El balanceador se actualizará a PHP 8 y recogerá dinámicamente el estado de carga de cada servidor para distribuir sesiones con criterios objetivos, no solo roundrobin. La BBDD del balanceador registrará estado, capacidad y última señal de vida de cada nodo. Mejora propuesta: incorporar una regla de admisión progresiva para salas con invitados: sala de espera, moderador EducaMadrid obligatorio y expiración automática del enlace. Mejora la seguridad sin cambiar la base tecnológica.

REQUISITO: II.1.11.3. Big Blue Button (BBB) (VID3) Requerimiento EducaMadrid
- Mantenimiento de la Instalación:
o Mantener la instalación del sistema de videoconferencias BigBlueButton con Greenlight v3 (Ruby on Rails/React). o Realizar actualizaciones de seguridad y mantenimiento regular.
- Adaptación al Entorno EducaMadrid:
o Dotar al aplicativo del interfaz institucional de EducaMadrid.


o Limitar las características a las solicitadas por los administradores de EducaMadrid.
- Integración con Moodle:
o Instalar y configurar el módulo de BigBlueButton en Moodle. o Permitir a los usuarios de tipo profesor grabar las conferencias y establecer una fecha de caducidad de las grabaciones por cada centro. o Asegurar que los alumnos puedan descargar o consultar las grabaciones de conferencias.
- Personalización de Greenlight:
o Adaptar la aplicación Greenlight a la imagen institucional de EducaMadrid. o Eliminar los enlaces directos a la página de autenticación del panel de administración de Greenlight. o Crear elementos personalizados como logotipo específico, PDF general de presentación y favicon.
- Restricciones de Acceso:
o No permitir el acceso directo a las presentaciones y vídeos de las grabaciones. o No permitir el acceso al panel de administración de Greenlight por parte de los usuarios. o Asegurar que los usuarios puedan utilizar BigBlueButton únicamente a través de las Aulas Virtuales de EducaMadrid.
- Script de Grabaciones:
o Añadir un script que permita disponer de las grabaciones de salas con pizarra de un único fichero descargable con la conferencia completa. Propuesta técnica de empresa_s BigBlueButton se mantendrá como servicio orientado a integración con Moodle, grabaciones y sesiones docentes. La instalación con Greenlight v3, basada en Ruby on Rails y React, se adaptará a la imagen institucional de EducaMadrid y se restringirá para evitar accesos directos no deseados al panel de administración o a recursos internos de grabación. La integración Moodle incluirá instalación y configuración del módulo, permisos para que profesores puedan grabar y definir caducidad de grabaciones por centro, y disponibilidad de consulta o descarga para alumnos según política acordada. Las grabaciones se tratarán como activos con ciclo de vida: creación, procesado, publicación, caducidad y retirada. El script de grabaciones generará un único fichero descargable para conferencias con pizarra, evitando que el usuario tenga que reconstruir manualmente una sesión a partir de piezas separadas. Se controlarán tiempos de procesado, errores y consumo de almacenamiento. Mejora propuesta: incorporar una tarea de aviso previo a la caducidad de grabaciones para responsables de centro. Es una mejora sencilla que evita pérdidas no esperadas y ordena el uso del almacenamiento.

REQUISITO: II.1.11.4. Peertube (VID4) Requerimiento EducaMadrid

- Mantenimiento y Monitorización:
o Mantener y monitorizar la instancia de PeerTube para la realización de emisiones en directo con previsión de alta participación (2000 o más usuarios conectados de manera simultánea).


o Implementar herramientas de monitorización para asegurar el correcto funcionamiento del servicio.
- Inserción de Retransmisiones mediante IFRAME:
o Permitir la inserción de retransmisiones desde la plataforma PeerTube mediante
###### 1.3.1.1.11.1. IFRAME.
o Asegurar que solo los administradores puedan acceder directamente a las retransmisiones. o Mostrar un reproductor con imagen personalizada (imagen institucional que permita identificar la Plataforma Educativa como origen de la retransmisión).
- Evaluar la necesidad del servicio y proceder a su retirada controlada en caso requerido.
- Entornos de Visualización:
o Desde el AV (Moodle): Permitir la visualización de retransmisiones de tipo PeerTube desde el Aula Virtual de Moodle. o Desde la Mediateca de EducaMadrid: Permitir la visualización de retransmisiones de tipo PeerTube desde la Mediateca de EducaMadrid. Propuesta técnica de empresa_s PeerTube se mantendrá y monitorizará como solución para emisiones en directo con previsión de alta participación, incluyendo escenarios de 2.000 o más usuarios simultáneos. La solución se centrará en observabilidad, control de acceso administrativo y consumo mediante iframe desde Moodle o Mediateca. El reproductor embebido mostrará imagen personalizada de EducaMadrid y evitará que usuarios finales accedan directamente a zonas administrativas. Se validará el comportamiento del iframe en Moodle y Mediateca, prestando atención a cabeceras de seguridad, CSP, permisos de reproducción, compatibilidad móvil y tratamiento de errores cuando la retransmisión todavía no haya comenzado. La evaluación de necesidad del servicio se documentará con métricas: número de eventos, concurrencia, incidencias, consumo de recursos y alternativas disponibles. Si se decide retirar el servicio, se hará de forma controlada, con inventario de integraciones, comunicación y sustitución de enlaces embebidos. Mejora propuesta: definir una plantilla de “evento de alta audiencia” con checklist técnico previo, prueba de carga ligera, página de espera y mensaje de contingencia. Aporta fiabilidad a actos institucionales sin desarrollo complejo.
##### 1.3.1.1.12. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO DE ANIMALANDIA
(ANI) Requerimiento EducaMadrid Mejorar la seguridad, rendimiento y funcionalidad del aplicativo Animalandia, desarrollado en PHP, adaptándolo a las últimas versiones y mejores prácticas de desarrollo (ANI1). Propuesta técnica de empresa_s Animalandia es un desarrollo PHP muy antiguo que se ha ido adaptando a nuevas versiones del lenguaje. La intervención debe reconocer esta naturaleza legacy: no conviene abordar una reescritura completa dentro de una actuación de mantenimiento, pero sí realizar una revisión profunda y ordenada que reduzca riesgos, elimine incompatibilidades y mejore seguridad y rendimiento.


La adaptación a la última versión estable de PHP se realizará en dos capas. Primero se ejecutará una fase de compatibilidad, activando niveles de error y advertencias en entorno controlado para identificar funciones obsoletas, cambios de comportamiento, problemas de tipado y dependencias antiguas. Después se aplicarán correcciones agrupadas por módulo, evitando cambios aislados que resuelvan un warning pero introduzcan incoherencias en otras pantallas. La seguridad se reforzará especialmente en entradas de usuario, consultas a BBDD, cookies y carga de scripts estadísticos. En un aplicativo antiguo es frecuente encontrar concatenación directa de SQL, validaciones dispersas y escapado solo en algunas salidas. Se propondrá una capa común de acceso a datos o, al menos, funciones centralizadas de consulta parametrizada para sustituir progresivamente patrones inseguros. Sanitización de entrada según tipo: texto libre, identificadores, filtros de búsqueda, selección de especie, paginación y parámetros de administración. Escapado de salida en HTML para prevenir XSS persistente o reflejado en fichas, buscadores y listados. Consultas parametrizadas en operaciones con datos de usuario, priorizando formularios y buscadores expuestos. Gestión de consentimiento de cookies antes de cargar scripts estadísticos no estrictamente necesarios. En rendimiento se revisarán las consultas más costosas, los listados con paginación deficiente, los filtros sobre campos sin índice y las pantallas que repitan consultas por cada elemento mostrado. Se medirán tiempos antes y después para justificar cambios. La caché se aplicará a datos de baja variación, como catálogos o fichas consultadas frecuentemente, evitando cachear respuestas personalizadas o dependientes de permisos. La actualización de jQuery se hará con pruebas funcionales específicas: menús, buscadores, galerías, formularios, validaciones de cliente y componentes dinámicos. Se identificará código dependiente de APIs retiradas y se corregirá sin mezclar estilos nuevos innecesarios. Mejora propuesta: crear un pequeño “mapa de deuda técnica” de Animalandia con módulos, riesgos, funciones obsoletas, consultas críticas y prioridad de intervención. No compromete una reescritura completa, pero deja una guía útil para futuras evoluciones y evita que cada ajuste se haga sin visión global.
##### 1.3.1.1.13. APARTADO: MEJORAS Y MANTENIMIENTO EN LA SINCRONIZACIÓN DE USUARIOS
(SYN) Requerimiento EducaMadrid Optimizar el proceso actual de sincronización de cuentas de usuarios mediante la mejora de los scripts existentes, la automatización de tareas y la integración de nuevos tipos de usuarios. El objetivo es minimizar la intervención manual y asegurar una sincronización eficiente y precisa. Es muy importante mantener actualizada la BBDD “ldap plano” con los cambios de raíces ya que es la que se emplea para alimentar de usuarios otros aplicativos como cloud o aulas virtuales (SYN1). Propuesta técnica de empresa_s Interpretación técnica del alcance


Fecha: 21/05/2026

La sincronización de usuarios se tratará como un proceso crítico de gobierno de identidades y no como un conjunto de cargas aisladas. El servicio debe mantener actualizada la base de datos denominada internamente "ldap plano" con los cambios procedentes de Raíces, porque esa información alimenta servicios como Cloud, Aulas Virtuales, EMPieza y ConsultasLDAP. La aclaración técnica relevante es que el "ldap plano" no es un árbol LDAP ni un servicio de directorio, sino una base de datos PostgreSQL que recibe ese nombre por razones históricas. Por ello, las decisiones de rendimiento, seguridad, indexación, auditoría y recuperación se diseñarán como actuaciones sobre PostgreSQL. El alcance se organizará alrededor de los flujos actuales: sincronización de profesores y alumnos, generación y actualización diaria de cohortes para Aulas Virtuales, vistas para EMPieza y ConsultasLDAP, inserciones masivas en Cloud, usuarios de enseñanzas superiores no presentes en Raíces, centros privados, docentes y no docentes sin horario, catálogos auxiliares, cuentas TIC, carga de tablas de centros desde fuentes LDAP y CSV, borrado masivo de relaciones usuariocentro, tratamiento de bajas y propagación de estados leaving. Modelo de proceso y control de estados Cada ejecución de sincronización tendrá un identificador único y quedará descompuesta en fases: ingesta, normalización, validación, reconciliación, publicación y verificación. La ingesta leerá los ficheros o fuentes disponibles; la normalización convertirá cada origen en entidades homogéneas; la validación comprobará claves, duplicados, fechas y relaciones; la reconciliación comparará el estado recibido con el estado persistido en PostgreSQL; y la publicación aplicará cambios por lotes controlados. Fase Función Control técnico Ingesta Lectura de exportaciones de Control de fecha, tamaño, Raíces, tablas auxiliares, codificación, duplicados y LDAP/CSV y fuentes completitud. complementarias. Normalización Conversión a entidades Unificación de claves homogéneas de usuario, funcionales como NIA, NIF, centro, relación, grupo, identificador EducaMadrid y enseñanza y estado. código de centro. Reconciliación Detección de altas, Ejecución idempotente para modificaciones, bajas, que un reproceso no duplique cambios de centro y cambios registros ni genere relaciones de estado. residuales. Publicación Escritura en PostgreSQL "ldap Transacciones por lote, plano", vistas, tablas de puntos de reanudación, integración y colas de métricas y trazas por fase. propagación. La publicación se realizará con mecanismos de seguridad operacional. Antes de ejecutar bajas masivas, cambios de centro o eliminación de relaciones se calcularán umbrales de anomalía. Si una carga indica, por ejemplo, un porcentaje inusual de bajas docentes, desaparición de grupos completos o pérdida de relaciones de un centro, el proceso quedará en estado pendiente de revisión en lugar de propagar automáticamente un error de origen al conjunto de servicios consumidores. Optimización de PostgreSQL "ldap plano"


La optimización se basará en el análisis de consultas reales, no en la creación indiscriminada de índices. Se revisarán planes de ejecución, bloqueos, cardinalidad, consultas por usuario, consultas por centro, joins sobre relaciones usuario- centro, búsquedas por enseñanza/grupo y accesos recurrentes desde vistas de EMPieza y ConsultasLDAP. Los índices propuestos se validarán en preproducción con volúmenes representativos para evitar que una mejora de lectura penalice de forma excesiva las cargas nocturnas o los procesos de inicio de curso. Se propondrá una separación clara entre tablas de carga, tablas normalizadas, tablas efectivas de publicación y vistas de consumo. Esta separación permite validar datos antes de hacerlos visibles, facilita rollback lógico y reduce la probabilidad de que una ejecución parcial deje información inconsistente. Las vistas para EMPieza y ConsultasLDAP se revisarán para asegurar que reflejan datos ya consolidados, evitando que un consumidor lea estados intermedios de una carga. Ejemplo: una sincronización recibe un cambio de centro de 500 alumnos. El proceso normaliza la información, valida que el centro destino existe, compara la relación actual en PostgreSQL, prepara los cambios y publica solo las relaciones modificadas, registrando cuántas pertenencias se han cerrado y cuántas se han creado. Sincronización de colectivos y operaciones específicas Los scripts de profesores y alumnos se revisarán para reducir acoplamientos y reutilizar funciones comunes de validación. En lugar de duplicar lógica en cada script, se dispondrá de utilidades compartidas para lectura, validación de identificadores, conexión a PostgreSQL, gestión de errores, ejecución por lotes y escritura de métricas. Esta mejora reduce riesgo en futuras modificaciones y facilita que un cambio de regla funcional se aplique de forma uniforme. La generación anual de cohortes para Aulas Virtuales se diseñará como un proceso diferenciado de la actualización diaria. La generación anual construirá el mapa completo de cohortes y relaciones esperadas; la actualización diaria aplicará variaciones incrementales. Esto permite reducir tiempos, detectar diferencias y evitar que un pequeño cambio diario desencadene una regeneración innecesaria del conjunto completo. Para Cloud se revisarán las inserciones masivas y la creación de grupos de centro. Se aplicarán lotes con tamaños configurables, reintentos controlados, comprobación previa de existencia y registro de errores por usuario. El objetivo es que un usuario problemático no bloquee una carga completa y que el resultado pueda auditarse sin revisar manualmente logs extensos. Los usuarios de enseñanzas superiores, centros privados, docentes/no docentes sin horario, catálogos auxiliares y cuentas TIC se tratarán como subflujos con reglas propias. Cada subflujo tendrá criterios de entrada, transformación y salida, pero usará la misma infraestructura de ejecución y trazabilidad. En el caso de web scraping sobre Raíces, se incorporarán controles de fragilidad: detección de cambios en estructura, límites de frecuencia, logs específicos y posibilidad de desactivar el subflujo sin afectar al resto de la sincronización. Bajas, leaving y borrado de relaciones El tratamiento de bajas se resolverá como transición de estado y no como eliminación inmediata. Se distinguirá entre baja recibida desde Raíces, usuario en estado leaving, eliminación de relación con centro y borrado definitivo cuando corresponda. Esta distinción evita pérdidas de información prematuras y permite propagar a cada servicio el efecto adecuado: desactivación, retirada de permisos, cierre de pertenencia, bloqueo de acceso o limpieza diferida. El borrado masivo de relaciones usuario- centro al inicio de curso se ejecutará con prevalidación, simulación y confirmación técnica. La simulación generará un informe con número de relaciones Página 115 de 192


Fecha: 21/05/2026

afectadas por servicio, centros con mayor impacto, usuarios sin relación resultante y relaciones que se conservarán por reglas específicas. Tras la ejecución se realizará una verificación comparando el estado esperado y el estado final en PostgreSQL y en los principales aplicativos afectados. Mejora propuesta: evolución hacia API de Raíces Como mejora, se propone trabajar junto con los equipos responsables de Raíces en la definición de requisitos de una API de integración que permita a la sincronización de EducaMadrid consultar cambios de usuarios, centros, matrículas, relaciones académicas y estados sin depender exclusivamente de descargas diarias de ficheros. Esta API no se planteará como sustitución brusca del modelo actual, sino como evolución progresiva y compatible. La primera fase podría utilizar la API para contrastar información crítica, resolver identificadores o recuperar cambios recientes. En una segunda fase se podrían consumir deltas diarios con paginación, control de versión del contrato de datos y marcas temporales. En una fase madura, la sincronización reduciría la dependencia de ficheros completos, acortaría el tiempo entre el cambio en origen y su disponibilidad en EducaMadrid y permitiría un diagnóstico más preciso ante inconsistencias. Capacidad API Descripción Valor técnico Consulta por usuario Obtener datos por NIA, NIF o Resolver incidencias identificador EducaMadrid. puntuales sin esperar al fichero diario. Cambios desde fecha Recuperar altas, Sincronización incremental y modificaciones y bajas desde menor carga nocturna. una marca temporal. Relaciones académicas Consultar centro, grupo, Mejor consistencia en enseñanza y vigencia de la cohortes, Cloud y permisos. relación. Contrato versionado Publicar esquema, códigos de Menor dependencia de error, límites y semántica de interpretación de ficheros. estados. Mejora de bajo riesgo: cuadro técnico de sincronización con estado de últimas ejecuciones, registros tratados, errores, avisos, duración por fase y detección de umbrales anómalos. Aporta visibilidad inmediata sin alterar la lógica funcional. Relación con aplicativos consumidores La sincronización se validará pensando en los consumidores, no únicamente en la tabla final. Cloud, Aulas Virtuales, EMPieza y ConsultasLDAP pueden interpretar de manera distinta una baja, un cambio de centro o una relación caducada. Por ello se documentará para cada consumidor qué campos utiliza, con qué frecuencia los consulta, qué vistas o tablas necesita y qué efecto produce cada estado. Esta matriz evita que una corrección en un origen provoque efectos colaterales en un aplicativo que esperaba una semántica diferente. Las vistas destinadas a EMPieza y ConsultasLDAP se considerarán contratos de lectura. Cuando haya que modificar una vista, se analizará compatibilidad hacia atrás y se habilitará, si procede, una vista temporal de transición. Esta técnica permite evolucionar el modelo de datos sin obligar a modificar simultáneamente todos los aplicativos dependientes.


Fecha: 21/05/2026

Consumidor Dependencia principal Control propuesto Cloud Usuarios, grupos de centro, Inserciones por lote y altas masivas y restricciones comprobación de grupos de compartición. creados. Aulas Virtuales Cohortes, pertenencias y Generación anual más delta actualización diaria. diario. EMPieza Vistas de usuario, centro y Contrato estable de lectura. relación. Consultas LDAP Consultas administrativas Vistas consistentes y sobre datos sincronizados. optimizadas. Pruebas y criterios de aceptación Las pruebas incluirán ejecuciones completas e incrementales, cargas con datos inconsistentes, reprocesos, reinicio tras fallo, simulación de bajas masivas, usuarios leaving, centros sin correspondencia, creación de cohortes, actualización diaria y escritura en vistas de consumo. Se aceptará la solución cuando los procesos sean idempotentes, trazables, repetibles y capaces de explicar cada diferencia entre dato de origen y dato publicado. Operación diaria, alertas y recuperación La ejecución diaria deberá ser observable sin necesidad de entrar en cada servidor. Se propondrá un registro estructurado por ejecución con resumen funcional y técnico: origen de datos utilizado, fecha de fichero o marca de API, número de registros leídos, registros aceptados, registros rechazados, relaciones creadas, relaciones cerradas, errores recuperables y errores bloqueantes. Este registro permitirá diferenciar problemas de dato, problemas de conectividad, fallos de permisos o degradación de rendimiento en PostgreSQL. Los errores se clasificarán por severidad. Un error de un usuario aislado no debe impedir que se complete el resto del lote, pero un error de estructura, una exportación incompleta o una variación de esquema sí debe detener la publicación. Para cada clase de error se definirá si procede reintento automático, cuarentena de registros, parada de proceso o intervención manual. De esta forma se evita tanto la fragilidad de procesos que se detienen ante cualquier dato defectuoso como el riesgo de procesos que continúan publicando datos no fiables. La recuperación tras fallo se resolverá mediante checkpoints. Cada lote confirmado quedará marcado, de forma que una interrupción de red, un timeout o un reinicio del servidor no obligue a empezar desde cero. En procesos pesados de inicio de curso, esta capacidad es esencial para completar cargas dentro de ventanas operativas razonables y para reducir el trabajo manual de repetición y conciliación. Ámbito Ejemplo de incidencia Tratamiento Conectividad con origen Fichero no disponible, API No publicar cambios y inaccesible o credencial conservar último estado caducada. válido. Calidad de datos Identificadores duplicados, Aislar registros y emitir centro inexistente, campos informe de corrección. obligatorios vacíos. Rendimiento Consulta lenta, bloqueo, lote Reducir lote, reintentar y excesivo o índice no utilizado. revisar plan de ejecución.


Fecha: 21/05/2026

Publicación Error en escritura o en servicio Reanudar desde checkpoint y consumidor. no duplicar cambios.
##### 1.3.1.1.14. APARTADO: MEJORAS Y MANTENIMIENTO DEL PORTAL CAU (CAU)
Requerimiento EducaMadrid Actualización y adaptación de la última versión del aplicativo utilizado en el Portal CAU. Esta actualización debe mantener las modificaciones actuales, la imagen institucional, y asegurar que los mecanismos de generación de correos y autoasignación de incidencias sigan funcionando correctamente (CAU1). Propuesta técnica de empresa_s Actualización conservadora del aplicativo El Portal CAU se actualizará a la última versión disponible del aplicativo manteniendo las personalizaciones actuales, la imagen institucional y los mecanismos de generación de correos y autoasignación de incidencias. La intervención se abordará como una actualización con preservación funcional: antes de aplicar la nueva versión se inventariarán módulos, plantillas, reglas de asignación, configuración de correo, roles, colas, estados, campos personalizados, integraciones y cambios locales no estándar. La actualización se ejecutará primero en un entorno de réplica. Se comprobarán requisitos de sistema, versión de PHP, motor de base de datos, extensiones, librerías, permisos de ficheros, tareas programadas, configuración de correo y compatibilidad de temas. Las diferencias entre versión actual y versión destino se documentarán como una matriz de impacto para saber qué funcionalidades se migran, cuáles se reconfiguran y cuáles requieren adaptación de código. Preservación de personalizaciones y reglas operativas Las personalizaciones actuales se aislarán respecto al núcleo del producto. Cuando sea posible se trasladarán a configuración, plantillas, extensiones o capas de tema para reducir modificaciones directas sobre código base. Las reglas de autoasignación se probarán con casos reales: incidencias por categoría, centro, perfil, criticidad, cola de soporte y usuario asignable. La generación de correos se comprobará con plantillas, remitente, destinatarios, codificación, enlaces, adjuntos y trazabilidad de envío. Elemento Tratamiento Validación Imagen institucional Cabecera, logotipos, colores, Comparativa visual pie, estilos y coherencia con antes/después y validación EducaMadrid. responsive. Correo Plantillas, eventos Pruebas de envío por tipo de disparadores, SMTP, incidencia y registro de codificación y enlaces. resultado. Autoasignación Reglas de distribución y Batería de casos con usuarios prioridades. destino esperados. Configuración Parámetros, roles, estados y Exportación previa, revisión y campos personalizados. restauración en entorno de pruebas. Despliegue y reducción de riesgos


Fecha: 21/05/2026

El despliegue se realizará con copia de seguridad completa, plan de reversión y ventana acordada. Antes del paso a producción se congelarán cambios de configuración, se ejecutará una migración de ensayo y se verificará que la versión resultante permite abrir, actualizar, asignar, comentar, cerrar y notificar incidencias. El plan de rollback incluirá restauración de base de datos y ficheros, así como comprobación de correos pendientes para evitar duplicidades. Se evitará introducir cambios funcionales simultáneos a la actualización salvo que sean imprescindibles. Esta separación permite distinguir una incidencia propia de la nueva versión de una incidencia derivada de una mejora adicional. Tras la implantación se mantendrá una vigilancia reforzada de logs, cola de correo, tiempos de respuesta y volumen de incidencias sin asignar. Mejora propuesta Panel de verificación postactualización para administradores técnicos, con pruebas guiadas de correo, autoasignación, permisos, plantilla institucional y conectividad. La mejora se limita a comprobaciones internas, pero reduce significativamente el tiempo de validación tras cada actualización. Criterios de rendimiento y experiencia de soporte La actualización del CAU deberá preservar la agilidad de uso de los técnicos. Se revisarán tiempos de carga de listados, filtros, búsquedas, apertura de incidencias, cambios de estado y envío de comentarios. Cuando una pantalla dependa de muchas incidencias históricas se propondrá paginación, filtrado por defecto o índices de base de datos si el producto lo permite. El objetivo es que la actualización no mejore solo la seguridad, sino también la operativa diaria del soporte. Las plantillas de correo se revisarán con una perspectiva funcional: asunto comprensible, cuerpo claro, enlaces correctos, identificación de incidencia y ausencia de información técnica innecesaria. Se mantendrá coherencia con la imagen institucional y se comprobará que las notificaciones resulten útiles tanto para usuarios finales como para equipos de soporte. Gestión de compatibilidad y mantenimiento futuro La actualización del Portal CAU dejará una base mantenible para futuras versiones. Se documentarán los cambios locales en un registro de personalizaciones con ubicación, finalidad, dependencia y alternativa de configuración si existe. Este registro evita que en una actualización posterior se pierdan modificaciones importantes o se mantengan parches que ya no son necesarios en la versión nueva. Se prestará atención a las dependencias de correo porque suelen ser críticas en portales de soporte: TLS, autenticación, remitente autorizado, colas, reintentos, codificación UTF- 8, plantillas HTML/texto plano y enlaces generados. También se validará que los correos no incluyan información técnica innecesaria y que las notificaciones permitan al usuario entender el estado de la incidencia sin tener que acceder a pantallas internas. Momento Acción Beneficio Antes de migrar Inventario de configuración, Migración reproducible. copia de seguridad, extracción de personalizaciones y ensayo. Durante la migración Aplicación controlada de Sistema coherente con versión, adaptación de tema y EducaMadrid. configuración de correo.


Fecha: 21/05/2026

Después de migrar Pruebas de roles, estados, Servicio validado antes de correos, autoasignación y apertura. rendimiento.

##### 1.3.1.1.15. APARTADO: MEJORAS Y MANTENIMIENTO DE EDUCASAAC (EDU)
Requerimiento EducaMadrid Refactorización del aplicativo EducaSaac con el objetivo de solucionar problemas de seguridad en HTML, PHP y JavaScript. El objetivo es mejorar la seguridad del aplicativo, protegiendo los datos y las operaciones realizadas por los usuarios (EDU1). Propuesta técnica de empresa_s Refactorización enfocada a seguridad EducaSAAC requiere una refactorización orientada a corregir problemas de seguridad en HTML, PHP y JavaScript, protegiendo datos y operaciones de usuario. La actuación se realizará de forma incremental para no reescribir el aplicativo de una sola vez ni alterar comportamientos funcionales consolidados. El primer paso será elaborar un mapa de superficies de entrada: formularios, parámetros GET/POST, subida de ficheros si existe, URLs dinámicas, llamadas AJAX, cookies, sesiones y puntos de administración. Cada entrada se clasificará según riesgo: entrada pública, entrada autenticada, entrada administrativa, datos persistentes que luego se renderizan en HTML y parámetros que afectan a consultas o rutas. Con esa clasificación se aplicarán medidas concretas de sanitización, validación, escape de salida, control de sesión y protección frente a CSRF. La refactorización no se limitará a añadir filtros genéricos, sino que diferenciará validación de datos de negocio y escape según contexto de salida. Medidas técnicas en PHP, HTML y JavaScript Plano Actuación Resultado esperado PHP Validación tipada, consultas Evitar inyección SQL, accesos preparadas, control de sesión, indebidos y exposición de permisos por rol, tratamiento trazas. seguro de errores. HTML Escape de salida por contexto, Evitar XSS reflejado y atributos seguros, etiquetas almacenado. permitidas y control de contenido persistente. JavaScript Evitar construcción insegura Reducir XSS DOM y errores de HTML, validar respuestas, en cliente. reducir uso de eval o patrones equivalentes. HTTP HTTPS, cabeceras de Proteger sesión y operaciones seguridad, cookies seguras y con cambio de estado. tokens CSRF. Las consultas a base de datos se revisarán para sustituir concatenaciones por consultas preparadas. Los formularios que modifican estado incorporarán token CSRF ligado a sesión. Los mensajes de error visibles al usuario serán funcionales y no revelarán rutas, consultas, trazas ni


Fecha: 21/05/2026

nombres internos. En administración se reforzará el control de acceso para que cada operación verifique permisos en servidor, aunque la interfaz oculte botones a perfiles no autorizados. Estrategia de refactorización sin ruptura Se trabajará con una rama técnica específica y cambios pequeños revisables. Primero se introducirán funciones comunes de validación y escape. Después se migrarán pantallas por prioridad de riesgo: autenticación, formularios públicos, administración y páginas con contenido persistente. Esta secuencia permite obtener mejoras tempranas sin esperar a que todo el aplicativo esté revisado. Cuando una pantalla tenga mucho código mezclado de presentación y lógica, se propondrá una separación mínima: carga de datos, validación, operación y renderizado. No se pretende imponer un framework nuevo, sino hacer que el PHP existente sea mantenible y seguro. La prioridad será eliminar duplicidad peligrosa, centralizar utilidades críticas y dejar documentado el patrón que debe seguir cualquier evolución futura. Pruebas de seguridad Las pruebas incluirán entradas con caracteres especiales, scripts embebidos, parámetros manipulados, ausencia o repetición de token CSRF, intentos de acceso a rutas no autorizadas, manipulación de identificadores y uso de sesiones caducadas. También se comprobará que la aplicación funciona correctamente sobre HTTPS y que los cambios no rompen navegación, validaciones de negocio ni mensajes informativos. Ejemplo: un campo descriptivo que antes se imprimía directamente se almacenará normalizado y se mostrará escapado como texto. Si el usuario introduce una etiqueta script, el contenido no se ejecutará en el navegador y quedará registrado como texto inocuo. Mejora propuesta Biblioteca interna ligera de seguridad para EducaSAAC, con funciones de validación, escape, generación/verificación CSRF y respuesta de error segura. Es una mejora contenida que evita repetir soluciones parciales en cada pantalla. Mantenimiento de código y deuda técnica La revisión de seguridad se aprovechará para reducir deuda técnica localizada. Cuando se detecten bloques repetidos de validación, generación de HTML o control de sesión, se sustituirán por funciones comunes. Esto no convierte EducaSAAC en un desarrollo nuevo, pero evita que cada pantalla resuelva de manera distinta problemas idénticos. La mejora es especialmente útil en aplicaciones PHP que han crecido por ampliaciones sucesivas. También se revisará la organización de recursos JavaScript y CSS. Los scripts que solo sean necesarios en una pantalla no deberían cargarse globalmente, y los eventos de cliente deben validar sin sustituir las comprobaciones de servidor. El servidor seguirá siendo la autoridad para aceptar o rechazar operaciones, de forma que la manipulación del navegador no pueda saltarse reglas funcionales. Problema detectado Actuación Impacto Validación duplicada Crear funciones comunes de Menos errores y mismo criterio limpieza, tipado y mensajes de en todo el aplicativo. error.


Fecha: 21/05/2026

HTML mezclado con lógica Separar preparación de datos Código más revisable y menos y renderizado cuando sea propenso a XSS. viable. JavaScript antiguo Revisar eventos, construcción Menos riesgo de XSS DOM y de DOM y dependencias fallos de compatibilidad. obsoletas.

##### 1.3.1.1.16. APARTADO: MEJORAS Y MANTENIMIENTO DEL CLOUD (CLO)

REQUISITO: II.1.16.1. Evolución y actualización del servicio de Cloud (CLO1) Requerimiento EducaMadrid Evolucionar el servicio de cloud instalando versiones actualizadas del aplicativo y del editor colaborativo, mejorando la funcionalidad, seguridad y usabilidad del sistema. Propuesta técnica de empresa_s El Cloud de EducaMadrid se tratará como una instalación Nextcloud de uso intensivo, con ficheros, comparticiones, clientes móviles y de escritorio, editor colaborativo, usuarios de distintos perfiles y reglas propias de la plataforma. La actualización no se limitará a subir versión: deberá preservar datos, preferencias, comparticiones, configuraciones, modificaciones previas, integraciones, personalización visual y compatibilidad con clientes Android, iOS, Windows, Linux y macOS. El proceso comenzará con una auditoría de versión actual, apps instaladas, apps críticas, apps incompatibles, tamaño de almacenamiento, volumen de usuarios, configuración de cron, colas, bases de datos, cache, locking, sistema de ficheros, editor colaborativo, integraciones de autenticación y reglas de compartición. Con esta información se definirá la ruta de actualización soportada y se descartarán saltos no compatibles. Migración de datos y scripts masivos El script de subida de versión y adaptación de datos se diseñará para trabajar por lotes reanudables. Clasificará cuentas por tipo de usuario y centro, registrará progreso y permitirá continuar después de una interrupción sin repetir operaciones ya completadas. Incluirá validación de integridad antes y después de ejecutar cambios: existencia de ficheros, correspondencia de cuentas, comparticiones, grupos, preferencias y datos del editor colaborativo. Los cambios de nombre de centro se resolverán mediante un script específico que modifique cuentas institucionales principales y derivadas, migre datos, conserve comparticiones legítimas y genere un informe de equivalencias. El borrado de usuarios se diseñará con extrema cautela: identificación inequívoca, previsualización del impacto, tratamiento de cuentas institucionales y secundarias, eliminación de registros en base de datos y limpieza de ficheros, respetando las reglas de conservación que indique EducaMadrid. Actuación Cómo se ejecuta Resultado Subida de versión Ruta soportada, apps Nextcloud actualizado sin compatibles, backup, ensayo pérdida de datos ni y verificación. configuración crítica.


Fecha: 21/05/2026

Cambio de centros Renombrado de cuentas y Cuentas consistentes y migración de datos comparticiones preservadas institucionales. cuando proceda. Borrado de usuarios Previsualización, eliminación Limpieza trazable y segura. de BBDD y ficheros, cuentas secundarias. Avisos centralizados Integración con mecanismo de Comunicación visible de EducaMadrid. mantenimientos e incidencias. Seguridad, comparticiones y rendimiento Las restricciones de compartición se aplicarán diferenciando perfiles. Las cuentas de alumnos no podrán crear enlaces externos y compartirán únicamente con usuarios del aplicativo según las reglas definidas. El sistema de comparticiones por centro se configurará para que cada centro disponga de un espacio de intercambio entre sus usuarios dentro de una única instalación. La gestión de grupos por centro se apoyará en procesos externos desde EMPieza, evitando administración manual dentro de Nextcloud. Los problemas de rendimiento en autocompletado de usuarios al compartir se abordarán reduciendo consultas masivas, limitando ámbitos de búsqueda, usando caché y aplicando índices o configuraciones adecuadas. La pantalla de gestión de usuarios se revisará para evitar listados completos innecesarios y para paginar, filtrar o consultar bajo demanda. Estas mejoras son especialmente relevantes en una instalación educativa con muchos usuarios, centros y relaciones. La limpieza del repositorio eliminará ficheros innecesarios de páginas previas a autenticación LDAP, temporales y duplicados, con una comprobación previa que evite borrar activos necesarios. Se revisarán permisos de escritura, logs, temporales, cache, papelera, versiones de ficheros y cuotas para reducir consumo de disco sin afectar a datos útiles. Personalización y experiencia de usuario La interfaz se adaptará con elementos gráficos de la Plataforma Educativa: favicon, logotipo, colores, textos y tema. La personalización abarcará el aplicativo y el editor colaborativo. También se revisará el bloque de compartir para evitar que los usuarios compartan sin ser conscientes contenidos privados alojados dentro de una carpeta compartida; se añadirán confirmaciones o avisos cuando la acción pueda ampliar el acceso a terceros. La integración con SSO se planteará como autenticación unificada y sincronización coherente de usuarios. El objetivo es que el usuario acceda de forma homogénea al ecosistema EducaMadrid y que las cuentas mantengan sus datos actualizados sin duplicidades ni desajustes entre directorio, Cloud y servicios relacionados.

REQUISITO: II.1.16.2. IA en cloud (CLO2) Requerimiento EducaMadrid Integración de inteligencia artificial (IA) en el aplicativo Cloud de la plataforma EducaMadrid . Este proyecto incluye un estudio de viabilidad de la instalación de una solución de IA conveniente, la creación de un Retrieval-Augmented Generation (RAG) con documentos del usuario, y la implementación de un chatbot para realizar consultas y tareas sobre los documentos del usuario. Objetivos

- Realizar un estudio de las posibilidades de implantación de IA en el aplicativo Cloud.


Fecha: 21/05/2026

- Instalar la solución de IA más conveniente para el servicio.
- Crear un RAG con los documentos del usuario en una base de datos vectorizada.
- Implementar un chatbot para realizar consultas y tareas sobre los documentos del usuario.
- Asegurar que los usuarios solo puedan hacer consultas sobre sus propios documentos.
- Limitar el acceso a las opciones de IA a ciertos perfiles y centros, con posibilidad de
ampliación si fuera necesario.
- Indexar solo los documentos que el usuario solicite en la base de datos vectorizada.
Propuesta técnica de empresa_s Para la IA en Cloud se propone estudiar e integrar el sistema actual de Nextcloud orientado a Assistant y Context Chat. Nextcloud documenta Context Chat como una funcionalidad de asistente formada por una app PHP y un backend ExternalApp escrito en Python, capaz de trabajar con proveedores de texto a texto y configurable para ejecutarse con modelos open source en infraestructura propia. También documenta que las External Apps permiten instalar aplicaciones como contenedores mediante AppAPI y un Deploy Daemon. Este encaje resulta adecuado para una aproximación privada, gobernada y desplegable por fases en EducaMadrid. La solución se diseñará con tres planos independientes: interfaz Nextcloud, backend de IA en contenedores y almacén vectorial para RAG. El usuario solicitará la indexación de documentos o carpetas concretas; el sistema extraerá texto, fragmentará contenido, generará embeddings y asociará cada fragmento a metadatos de propietario, ruta, permisos y fecha. Las consultas del chatbot recuperarán contexto solo de documentos que el usuario tenga derecho efectivo a consultar en Nextcloud. No se indexará de forma indiscriminada todo el Cloud. La indexación será selectiva, reversible y limitada por perfiles o centros piloto. Esta decisión reduce consumo de CPU/GPU, memoria y almacenamiento vectorial, y se ajusta al requisito de que los usuarios solo puedan consultar sus propios documentos. El backend se desplegará en contenedores con límites de recursos, control de concurrencia y colas de indexación para no interferir con sincronización de ficheros, comparticiones o navegación habitual. Componente Diseño Resultado Interfaz Nextcloud Assistant / Context Chatbot accesible sin salir del Chat integrado en la Cloud. experiencia de usuario. Backend ExternalApp en contenedor, Despliegue aislado, gestionada por AppAPI y actualizable y con recursos Deploy Daemon. controlados. RAG Extracción, fragmentación, Consultas sobre documentos embeddings y base vectorial. indexados por el usuario. Permisos Comprobación de acceso El usuario no obtiene antes de recuperar contexto. información de documentos ajenos. Ejemplo: un docente selecciona una carpeta con programaciones y solicita indexarla. El proceso genera vectores solo de esos documentos. Después pregunta al asistente por actividades de evaluación de un trimestre. El chatbot recupera fragmentos de esa carpeta, responde con contexto y no utiliza documentos de otros usuarios ni carpetas no indexadas. Si el docente elimina la indexación, se retiran los vectores asociados.


Fecha: 21/05/2026

Control de carga y pruebas La IA incorporará límites de concurrencia, cuotas por usuario o centro, pausa de indexación en horas punta, priorización de consultas interactivas, métricas de documentos indexados, tiempos de respuesta, errores por formato y consumo de recursos. Las pruebas incluirán documentos grandes, formatos no indexables, permisos cambiantes, eliminación de ficheros, carpetas compartidas, revocación de acceso y consultas simultáneas. La comunicación interna entre Nextcloud, backend y base vectorial se protegerá y se evitará registrar contenido documental en logs técnicos. Mejora propuesta: piloto de RAG privado en Nextcloud para centros seleccionados, basado en Assistant/Context Chat y backend en contenedores, con indexación selectiva de carpetas, control de permisos y métricas de consumo desde el primer día. Integración con editor colaborativo y clientes externos El editor colaborativo se validará como parte del Cloud y no como un componente accesorio. Se probará apertura, edición simultánea, guardado, bloqueo, recuperación tras desconexión, documentos grandes, permisos de solo lectura y comportamiento en carpetas compartidas. Cualquier actualización de Nextcloud deberá comprobar compatibilidad con la versión del editor y con las extensiones PHP o servicios que utilice. Los clientes de escritorio y móviles se verificarán con escenarios reales: sincronización inicial, modificación simultánea, conflicto, renombrado de carpetas, revocación de compartición, cuotas, borrado y restauración. En instalaciones con muchos usuarios, una incompatibilidad de cliente puede generar gran volumen de incidencias aunque el frontal web funcione correctamente. Por eso, la validación se realizará antes de abrir el servicio actualizado al conjunto de usuarios. Gobierno del dato en la IA del Cloud El RAG se diseñará con eliminación explícita de índices. Cuando un usuario retire una carpeta del ámbito de IA, elimine un fichero o pierda permiso sobre un documento compartido, el índice vectorial deberá actualizarse para que ese contenido no pueda recuperarse en consultas posteriores. La base vectorial no se tratará como una copia opaca de documentos, sino como un derivado sujeto a las mismas reglas de acceso y ciclo de vida. Se definirán límites iniciales prudentes: tamaño máximo de documento, extensiones admitidas, número de documentos por usuario, número de carpetas indexables, concurrencia de indexación y caducidad de índices piloto. Estos límites podrán ampliarse con datos reales de uso. La implantación empezará por centros o perfiles controlados para medir consumo y ajustar el dimensionamiento antes de una extensión general. Caso Tratamiento Objetivo Cambio de permisos Recalcular accesibilidad de Evitar respuestas con fragmentos indexados. información ya revocada. Borrado de fichero Eliminar vectores asociados o Ciclo de vida coherente con marcarlos como no Nextcloud. recuperables. Documento grande Fragmentación controlada y Indexación estable sin límite configurable. bloquear workers. Piloto por centro Activación limitada y métricas Escalado basado en datos separadas. reales.


Fecha: 21/05/2026

Métricas de explotación del Cloud Se incorporará una visión técnica de explotación para que las decisiones de mantenimiento se basen en datos. Se medirán usuarios activos, volumen almacenado, evolución de cuotas, número de comparticiones, enlaces externos bloqueados por política, errores de clientes, duración de tareas de mantenimiento, consumo de papelera/versiones y tiempos de respuesta de operaciones críticas. Estas métricas ayudarán a planificar limpieza, ampliaciones y ventanas de actualización. En el caso de IA, se medirán documentos indexados, tamaño procesado, tiempo de extracción, tiempo de embedding, consultas por perfil, errores por formato y latencia de respuesta. Las métricas no incluirán contenido de los documentos ni prompts completos si no es imprescindible para soporte, y se aplicará minimización para evitar almacenar información sensible en logs de explotación. Métrica Qué observa Uso operativo Almacenamiento Crecimiento por centro, Planificación de capacidad. cuotas, papelera y versiones. Comparticiones Internas, por centro, Control de seguridad y bloqueadas y revocadas. usabilidad. Clientes Errores de sincronización por Anticipación de incidencias versión y plataforma. masivas. IA/RAG Indexación, latencia, errores y Escalado controlado del consumo. piloto.

##### 1.3.1.1.17. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO BUZON ANÓNIMO (BAN)
Requerimiento EducaMadrid Soporte y mantenimiento de la web asociada al Plan Regional contra las Drogas de la Comunidad de Madrid. El objetivo es asegurar que la web cumpla con las necesidades del proyecto, sea segura, y esté alineada con la imagen institucional de EducaMadrid (BAN1). Propuesta técnica de empresa_s Mantenimiento funcional de la web El Buzón Anónimo es la web asociada al Plan Regional contra las Drogas de la Comunidad de Madrid. La actuación se centrará en mantener una web segura, sencilla de administrar, alineada con la imagen de EducaMadrid y compatible con navegadores y dispositivos actuales. Por la naturaleza del servicio, se priorizará la minimización de datos, la claridad de mensajes, la accesibilidad y la ausencia de exposición técnica en errores públicos. Se revisará la estructura del aplicativo, versión de PHP, dependencias, rutas públicas, formularios, zona de administración, almacenamiento del listado de centros, plantillas, estilos, imágenes, enlaces, pie de página y comportamiento responsive. La revisión permitirá distinguir tareas de mantenimiento preventivo, correcciones de compatibilidad y mejoras puntuales de administración. Gestión del listado de centros asociados El listado de centros asociados se gestionará mediante operaciones de alta, edición, baja o desactivación. Se validarán códigos, nombres, localidad, estado y datos visibles. Para evitar errores se incorporarán controles de duplicidad, campos obligatorios y normalización de nombres.


Fecha: 21/05/2026

Cuando exista información histórica vinculada a un centro, se priorizará la desactivación lógica frente al borrado físico para no perder trazabilidad. Operación Control Resultado Alta de centro Validación de código, nombre Centro disponible con datos y datos mínimos. consistentes. Edición Control de campos Actualización segura sin modificables y registro de duplicados. cambios relevantes. Baja/desactivación Retirada de visibilidad No aparecen centros manteniendo trazabilidad si obsoletos en la web. procede. Revisión periódica Detección de duplicados, Listado fiable para usuarios y incompletos o inconsistentes. administradores. Imagen institucional, modo claro/oscuro y accesibilidad La web se adaptará a la imagen institucional de EducaMadrid incorporando logotipos, enlaces, pie de página, tipografías, colores y estilos coherentes. La compatibilidad con modo claro y oscuro se resolverá evitando valores fijos que pierdan contraste. Se utilizarán variables CSS o clases de tema cuando sea viable, revisando botones, enlaces, mensajes, formularios, iconos y tablas. La accesibilidad se comprobará en navegación por teclado, foco visible, contraste, jerarquía de encabezados, textos alternativos, etiquetas de formulario, mensajes de error y adaptación a móvil. Las páginas deberán ser comprensibles para usuarios finales y manejables para administradores sin conocimientos técnicos. Seguridad, compatibilidad y mantenimiento Se realizarán mantenimientos preventivos de seguridad: actualización a una versión compatible de PHP, revisión de paquetes, validación de entradas, protección CSRF si existen formularios, cabeceras de seguridad, control de sesiones administrativas, permisos de escritura, tratamiento de errores y eliminación de ficheros obsoletos. Los errores públicos no mostrarán rutas internas, trazas ni detalles de configuración. La compatibilidad se verificará en navegadores actuales y dispositivos de escritorio y móvil. También se revisará el rendimiento de recursos estáticos, optimización de imágenes, carga de CSS/JS y tamaño de páginas. La documentación final incluirá procedimiento de actualización, estructura del aplicativo, parámetros principales, mantenimiento de centros y lista de comprobaciones posteriores a despliegue. Mejora propuesta Panel de comprobación previa de publicación del listado de centros, con detección de duplicados, campos incompletos, enlaces inválidos y avisos de contraste en modo claro/oscuro. Es una mejora acotada que reduce errores visibles y facilita la administración. Pruebas de aceptación Se comprobarán altas, ediciones y bajas de centros; visualización en modo claro y oscuro; navegación responsive; accesibilidad básica; ausencia de errores técnicos visibles; funcionamiento en navegadores actuales; y mantenimiento de la imagen institucional. La solución se considerará aceptada cuando la web permita gestionar centros con seguridad, mantenga


Fecha: 21/05/2026

coherencia visual con EducaMadrid y pueda actualizarse sin intervención manual sobre datos internos. Administración segura y trazabilidad mínima La administración del Buzón Anónimo se diseñará con permisos mínimos y trazabilidad suficiente para mantener el servicio sin convertirlo en un sistema de seguimiento de usuarios finales. Las operaciones administrativas sobre centros quedarán registradas con fecha, usuario administrador y acción realizada. En cambio, no se incorporarán registros innecesarios sobre navegación o contenido que pudieran comprometer la naturaleza del servicio. El tratamiento de formularios, si existen, se revisará desde la minimización: solo se recogerán los campos necesarios, se validará el formato, se protegerá el envío y se definirá una política clara de conservación. La web no debe acumular datos obsoletos ni ficheros temporales no controlados. La limpieza periódica formará parte del mantenimiento preventivo.

Área Tratamiento Beneficio Administración Acceso restringido, Control sin complejidad trazabilidad de cambios y excesiva. validaciones. Privacidad Minimización de datos y Menor exposición de revisión de temporales. información. Compatibilidad Pruebas en navegadores y Experiencia estable. dispositivos. Mantenimiento Documentación de Evolución sencilla del actualización y checklist. servicio.

##### 1.3.1.1.18. APARTADO: MEJORAS Y MANTENIMIENTO DE DTIC (DTIC)
Requerimiento EducaMadrid Corrección de problemas de seguridad, el mantenimiento de incidencias y la incorporación de nuevas funcionalidades en el aplicativo de Dotaciones TIC (DTIC) en la plataforma EducaMadrid . El objetivo es mejorar la seguridad, estabilidad y funcionalidad del aplicativo, asegurando que cumpla con los estándares actuales y las necesidades de la plataforma (DTIC1). Propuesta técnica de empresa_s El mantenimiento de DTIC se abordará como una intervención sobre un aplicativo operativo de gestión de dotaciones TIC, donde las acciones funcionales tienen impacto directo sobre componentes, modalidades, destinatarios e incidencias. La revisión inicial separará las incidencias correctivas de las mejoras evolutivas, identificando pantallas, formularios, scripts, consultas SQL, operaciones administrativas y dependencias con otros servicios. Esta lectura técnica permitirá actuar sobre funcionalidades concretas sin alterar reglas de negocio consolidadas. La seguridad se reforzará desde la entrada de datos hasta la persistencia. Se revisarán formularios de administración, parámetros recibidos por GET y POST, validaciones de tipo y longitud, operaciones de modificación masiva, tratamiento de ficheros si existieran, sesiones y permisos. En consultas a base de datos se priorizará el uso de consultas parametrizadas y se eliminarán concatenaciones de parámetros no validados. Además, se revisará la exposición de errores para evitar que mensajes técnicos revelen rutas, nombres de tablas o trazas internas.


La fusión de modalidades se implementará como una operación transaccional y auditable. Antes de modificar datos se ejecutará una validación de consistencia que compruebe la existencia de modalidad origen y destino, relaciones con componentes, destinatarios, incidencias, históricos y tablas auxiliares. Si alguna validación falla, la operación no se aplicará parcialmente. El resultado dejará un registro técnico con el número de elementos movidos, la modalidad sustituida, la modalidad final, el usuario administrador y la fecha de ejecución. El cambio de destinatarios de componentes se tratará con la misma cautela. No se propondrán actualizaciones directas sin control, sino un flujo que muestre al operador el impacto previsto, permita confirmar la operación y registre el estado anterior. Cuando existan componentes asociados a incidencias o entregas previas, la modificación conservará la trazabilidad histórica para que los datos ya consolidados sigan siendo interpretables. Se creará el script de bajas de usuarios que anonimizará a los usuarios solicitados. El objetivo no será borrar indiscriminadamente datos, sino sustituir información identificativa por valores neutros manteniendo la integridad referencial. El script localizará apariciones del usuario en incidencias, asignaciones, comentarios, históricos, destinatarios y trazas funcionales; posteriormente sustituirá nombre, correo, identificadores visibles y cualquier dato personal equivalente por valores anonimizados. El script contará con modo simulación, ejecución real y registro de auditoría. En modo simulación generará un informe con tablas afectadas, número de registros, campos que se modificarían y posibles advertencias. En ejecución real trabajará preferentemente dentro de una transacción o por bloques controlados, de forma que los errores puedan revertirse o aislarse. Este enfoque evita intervenciones manuales sobre base de datos y reduce el riesgo de dejar datos incoherentes. Para facilitar el mantenimiento posterior se documentará el mapa de entidades de DTIC afectadas por cada operación. Esta documentación incluirá qué tablas contienen datos personales, qué campos se consideran identificativos, qué relaciones deben preservarse y qué pruebas deben ejecutarse después de una anonimización o fusión de modalidad. También se dejarán ejemplos de uso del script con parámetros ficticios, rutas de logs y criterios para interpretar avisos. Las pruebas incluirán casos unitarios sobre funciones de validación, pruebas funcionales con modalidades de ejemplo, pruebas de permisos con usuarios autorizados y no autorizados, y pruebas de regresión sobre la consulta de incidencias históricas. Un ejemplo concreto sería ejecutar una anonimización en preproducción sobre un usuario de prueba que haya intervenido en varias incidencias, verificando que las incidencias siguen visibles, pero sin mostrar datos identificativos del usuario original. La anonimización se diseñará con una política de campos por categoría: identificadores visibles, datos de contacto, nombres completos, observaciones libres y referencias técnicas. Los identificadores internos que no permitan identificar a una persona podrán mantenerse si son necesarios para integridad, pero los campos visibles se sustituirán por valores neutros homogéneos. Esta distinción evita perder capacidad de auditoría funcional mientras se atiende la baja solicitada. Antes de cada operación se realizará copia lógica de los registros afectados o se generará una huella verificable del estado anterior, según el volumen y las posibilidades del entorno. El objetivo no es crear un sistema paralelo de backup, sino disponer de evidencia suficiente para analizar incidencias de ejecución. Las operaciones de mayor impacto se realizarán en ventanas acordadas y con validación posterior.


Fecha: 21/05/2026

El mantenimiento de DTIC también incorporará revisión de mensajes de error y confirmación. Las acciones de administración deben informar con claridad de qué se va a modificar y qué no. Por ejemplo, si una fusión de modalidades no afecta a componentes archivados, el sistema deberá indicarlo expresamente. Esto reduce decisiones erróneas por interpretación incompleta de la pantalla. Como criterio de aceptación, una operación de anonimización no se considerará finalizada hasta comprobar tres aspectos: ausencia de datos personales visibles del usuario, conservación de las relaciones históricas necesarias y existencia de un registro técnico que permita demostrar cuándo y cómo se ejecutó la acción. Propuesta de mejora Añadir un informe previo en HTML y CSV para las operaciones críticas, con semáforo de riesgo, número de registros afectados y advertencias por integridad, de forma que la Administración pueda validar el alcance antes de confirmar cambios irreversibles.
- Anonimización con usuario de prueba presente en comentarios, incidencias e históricos.
- Fusión de modalidades con rollback validado en preproducción.
- Cambio de destinatarios con registro del valor anterior y posterior.
- Revisión de permisos para impedir operaciones administrativas no autorizadas.
Operación Control técnico Resultado esperado Anonimización Modo simulación, Datos personales sustituidos transacción, informe de sin romper históricos campos afectados Fusión de modalidades Validación de referencias y Consolidación coherente de rollback modalidad origen y destino Cambio de destinatarios Registro de valor anterior y Trazabilidad completa de la posterior operación

##### 1.3.1.1.19. APARTADO: MEJORAS Y MANTENIMIENTO DE SEGUIMIENTOS (SEG)
Requerimiento EducaMadrid Corrección de problemas de seguridad, el mantenimiento de incidencias y la incorporación de nuevas funcionalidades en el aplicativo Seguimientos de la plataforma EducaMadrid. El objetivo es mejorar la compatibilidad, seguridad, y funcionalidad del aplicativo, asegurando que cumpla con los estándares actuales y las necesidades de la plataforma (SEG1). Propuesta técnica de empresa_s Seguimientos requiere preservar ediciones históricas, URLs antiguas, adjuntos y datos asociados a centros, usuarios, empresas, notas y dotaciones. La solución tratará cada edición como un ámbito lógico independiente, pero gestionado por una capa común de acceso a datos y navegación. De esta forma, las veinte ediciones existentes podrán seguir consultándose sin reproducir código por edición ni introducir reglas diferentes para cada anualidad. La compatibilidad de enlaces antiguos será un objetivo prioritario. Se diseñará un resolvedor de URLs capaz de recibir rutas heredadas, identificar la edición y el recurso asociado, y redirigir o servir el fichero actual aplicando controles de autorización. Esto evita romper enlaces publicados en comunicaciones, documentación o correos antiguos. La solución deberá ser tolerante con


variaciones de formato, nombres de fichero históricos y rutas que se hayan generado con criterios no homogéneos. La conversión de enlaces a ficheros se acompañará de una tabla de equivalencias interna. Las nuevas rutas no expondrán nombres correlativos ni información sensible, sino identificadores opacos. El sistema mantendrá la correspondencia entre el enlace histórico, el fichero físico y el recurso lógico, de forma que se pueda auditar qué fichero se entrega y desde qué edición. Esta capa también facilitará detectar adjuntos huérfanos o enlaces que apuntan a recursos inexistentes. La creación de nuevas ediciones se diseñará como un proceso administrativo asistido. El operador podrá clonar estructura base, fechas, modalidades, permisos y plantillas, pero el sistema validará que no queden campos obligatorios sin configurar. Se evitará que la apertura de una edición dependa de copiar manualmente registros o modificar código. Cuando haya cambios en formularios, estados o informes, se versionarán para que las ediciones antiguas mantengan su comportamiento. La gestión de adjuntos incorporará controles de tipo, tamaño, ubicación, permisos y nombre de descarga. Los adjuntos nuevos se almacenarán con identificadores no predecibles, pero se presentarán al usuario con nombres legibles. Se revisará la posibilidad de generar miniaturas o metadatos cuando aporte valor, sin convertir el servicio en un gestor documental completo. En todo caso, se priorizará la seguridad de la descarga y la preservación del histórico. En rendimiento, se revisarán las consultas que cargan listados de centros, dotaciones, empresas y notas. Las ediciones antiguas pueden acumular muchos registros, por lo que se aplicarán paginaciones reales, filtros indexables y consultas limitadas. Las operaciones de búsqueda se diseñarán para no recorrer grandes volúmenes sin filtros. Si existen informes pesados, se podrán generar en segundo plano o con exportaciones controladas. El modelo de permisos distinguirá administración, consulta, edición y descarga. No todos los usuarios que acceden a una edición deben poder modificar ficheros o alterar datos maestros. Las acciones sensibles quedarán registradas. Cuando se modifiquen permisos de una edición, el sistema deberá evitar que por error se expongan datos de campañas anteriores. La validación se centrará en regresión histórica: abrir ediciones antiguas, resolver enlaces previos, descargar adjuntos, consultar notas, filtrar por centro y crear una nueva edición. Como ejemplo, una URL antigua a un documento de la edición 2018 deberá seguir resolviendo correctamente aunque el fichero físico haya sido renombrado o movido a una estructura de almacenamiento nueva. La capa de compatibilidad de enlaces se diseñará de forma transparente para usuarios finales. Cuando un enlace antiguo se resuelva correctamente, el usuario no deberá conocer la nueva estructura interna. Cuando no sea posible resolverlo, se mostrará un mensaje controlado que permita reportar el caso, evitando errores 404 genéricos que dificulten el diagnóstico. Para las nuevas ediciones se propondrá una separación entre configuración común y datos específicos. La configuración común incluirá estados, permisos, formatos de adjunto y plantillas; los datos específicos contendrán centros, convocatorias, notas y ficheros. Esta separación facilitará abrir campañas futuras sin multiplicar tablas o ramas de código innecesarias. En adjuntos se revisará además la política de almacenamiento: ubicación física, permisos del servidor web, limpieza de temporales, nombres visibles y trazabilidad de descarga. Si se detectan adjuntos en rutas públicas no controladas, se propondrá moverlos detrás de un controlador de descarga que aplique permisos y registre accesos cuando proceda.


La explotación de datos se realizará con consultas paginadas y filtros claros. En lugar de generar listados completos por defecto, se guiará al usuario hacia búsquedas por edición, centro, estado o rango. Esto mejora rendimiento y hace más manejable la información para los administradores. Propuesta de mejora Incorporar un panel de salud de edición que muestre enlaces no resueltos, adjuntos huérfanos, diferencias de configuración y permisos anómalos antes de abrir una nueva edición o cerrar una ya existente.

- Resolvedor de URL antigua con recurso migrado.
- Creación de edición nueva sin copiar código.
- Prueba de descarga con permisos insuficientes.
- Exportación de informe pesado sin bloquear la navegación.
##### 1.3.1.1.20. APARTADO: MEJORAS Y MANTENIMIENTO DE ALBOR (ALB)
Estudio de viabilidad para el desarrollo de un nuevo aplicativo Albor en la plataforma EducaMadrid. Albor es una página donde padres o profesores de alumnos con necesidades especiales podrán realizar consultas acerca de capacidades o dispositivos adaptados. El proyecto piloto utilizará IA mediante una herramienta de tecnología RAG para gestionar y consultar la documentación (ALB1). Propuesta técnica de empresa_s Albor se planteará como un servicio especializado de consulta para familias y profesorado sobre necesidades especiales, capacidades y dispositivos adaptados. La solución se apoyará en un RAG cerrado, de forma que el asistente responda únicamente con documentos propios alimentados y validados para este servicio. No se permitirá que el modelo responda desde conocimiento general cuando no exista contexto documental suficiente. La arquitectura separará cuatro piezas: repositorio documental validado, proceso de extracción y troceado, índice de búsqueda semántica y componente conversacional. El repositorio mantendrá documentos, versiones, etiquetas temáticas, fecha de vigencia y responsable. El proceso de extracción convertirá los documentos a texto, limpiará elementos irrelevantes y generará fragmentos con contexto suficiente. El índice almacenará vectores y metadatos. El componente conversacional recuperará fragmentos y construirá respuestas con referencias. Podrá valorarse LAMB, Onyx u otra solución equivalente siempre que permita un funcionamiento controlado, desplegable en entorno autorizado y restringido a fuentes propias. La selección no se basará únicamente en la capacidad del modelo, sino en la trazabilidad de fuentes, facilidad de administración, control de permisos, operación en local o en infraestructura autorizada y capacidad para impedir respuestas no fundamentadas. El chatbot de Albor deberá incorporar una política de respuesta restrictiva. Cuando los documentos recuperados no contengan información suficiente, devolverá una respuesta de insuficiencia de contexto y propondrá revisar documentación relacionada o canales de ayuda. Esta decisión es especialmente importante al tratar contenidos sensibles, donde una respuesta inventada o demasiado general podría inducir a error a familias o docentes. La carga documental se realizará mediante una interfaz administrativa. Cada documento tendrá estado borrador, publicado, retirado o pendiente de revisión. La reindexación podrá ejecutarse al publicar o modificar un documento, y quedará registrado qué versión alimentó el índice. Si se retira


Fecha: 21/05/2026

un documento, sus fragmentos dejarán de estar disponibles para nuevas respuestas, preservando si procede una traza técnica de la operación. La interfaz de consulta tendrá lenguaje claro, accesibilidad y diseño responsive. Se evitarán respuestas largas sin estructura y se mostrarán enlaces o referencias a los documentos utilizados. Para usuarios no técnicos, el sistema podrá reformular la pregunta si detecta ambigüedad. Por ejemplo, ante una consulta sobre un dispositivo adaptado, el asistente podrá pedir si la pregunta se refiere a solicitud, uso, compatibilidad o criterios de selección. La seguridad se reforzará evitando el envío de datos personales al modelo cuando no sean necesarios. Se controlarán logs para no almacenar preguntas con información sensible de menores. Las métricas se registrarán de forma agregada: volumen de consultas, temas más consultados, consultas sin respuesta y documentos más recuperados. Estos datos permitirán mejorar la documentación sin comprometer privacidad. Las pruebas incluirán preguntas con respuesta exacta en la documentación, preguntas ambiguas, preguntas fuera de ámbito, documentos retirados y actualización de versiones. Un ejemplo de prueba será cargar una guía de dispositivos, consultar por un término presente, verificar que la respuesta referencia el fragmento correcto y después retirar el documento para comprobar que ya no se utiliza en respuestas nuevas. El proceso de troceado documental tendrá especial cuidado con documentos normativos o guías extensas. Los fragmentos no deben ser tan pequeños que pierdan contexto ni tan grandes que incorporen información irrelevante. Se podrá conservar una ventana de contexto alrededor de títulos y apartados para que las respuestas identifiquen correctamente el tema consultado. La administración del corpus incluirá una vista de documentos indexados, documentos pendientes, errores de extracción y fecha de última actualización. Así, si una respuesta no aparece, el responsable podrá comprobar si el documento estaba publicado, si se indexó correctamente o si fue retirado. Esta visibilidad es necesaria para operar un RAG de forma fiable. El modelo utilizado se encapsulará detrás de una interfaz de servicio. De este modo se podrá probar LAMB, Onyx u otro motor sin cambiar la interfaz pública de Albor. El contrato interno se basará en pregunta, contexto recuperado, respuesta, referencias y estado de confianza, lo que permite evolucionar el componente IA con menor acoplamiento. La evaluación no se limitará a comprobar que el chatbot responde. Se preparará un conjunto de preguntas de referencia con respuesta esperada, preguntas ambiguas y preguntas fuera del corpus. Cada actualización del corpus o del motor deberá superar estas pruebas para evitar regresiones en un servicio sensible. Propuesta de mejora Añadir una consola de revisión de respuestas sin datos personales, donde personal autorizado pueda marcar respuestas útiles, insuficientes o incorrectas y detectar documentación que necesita ampliación.
- Respuesta fundamentada solo en documentos publicados.
- Bloqueo de respuesta cuando el contexto no es suficiente.
- Reindexación tras cambio de versión documental.
- Retirada de documento y eliminación del índice activo.
Elemento RAG Tratamiento propuesto Garantía


Fecha: 21/05/2026

Documentos Carga con versión, estado y Solo fuentes validadas responsable Respuestas Citas internas y bloqueo por Sin invenciones fuera del falta de contexto corpus Métricas Consultas agregadas y temas Mejora continua sin datos sin respuesta personales

##### 1.3.1.1.21. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO DE AVISOS (AVI)
Requerimiento EducaMadrid Mantenimiento y actualización con mejoras de seguridad y usabilidad del aplicativo Avisos en la plataforma EducaMadrid. El objetivo es mejorar la seguridad, la disponibilidad y la funcionalidad del aplicativo, asegurando que cumpla con los estándares actuales y las necesidades de la plataforma (AVI1). Propuesta técnica de empresa_s Avisos es un servicio transversal y de alta visibilidad. Su evolución debe priorizar seguridad, disponibilidad, control de publicación y compatibilidad con los servicios consumidores. La actualización se realizará revisando el núcleo de publicación, la administración de mensajes, la programación temporal, la exposición de avisos y los mecanismos de integración con otras aplicaciones. La funcionalidad de programación de puesta en producción incorporará activación y desactivación temporizada, control de zona horaria, validación previa y estados explícitos. Un aviso no pasará directamente de borrador a publicado sin comprobar fechas, canal, contenido, enlaces y permisos. El sistema deberá diferenciar entre aviso pendiente, programado, publicado, caducado, retirado y fallido, permitiendo entender en todo momento qué se mostrará a los usuarios. El refuerzo de seguridad será uno de los ejes principales. Se revisará la sanitización del HTML permitido, el tratamiento de enlaces, la subida de imágenes si existiera, los permisos de administración, CSRF en formularios, XSS almacenado, cabeceras HTTP, protección de sesiones y exposición de endpoints. En un servicio de avisos, un XSS almacenado tendría impacto transversal, por lo que se aplicará una política estricta de contenido permitido. La integración con servicios consumidores se diseñará de forma resiliente. Si un servicio consumidor no puede obtener avisos en un momento dado, no debe bloquear su carga principal. Se podrá aplicar cacheado con tiempos cortos, firma o validación de origen cuando proceda, y formato estable de respuesta. Los avisos deberán poder filtrarse por ámbito, canal, fecha, prioridad y servicio destino. La administración ofrecerá previsualización antes de publicar. Esta previsualización deberá mostrar cómo se verá el aviso en los canales principales, incluyendo modo claro y oscuro si aplica. También permitirá detectar enlaces externos, contenido no permitido, imágenes demasiado pesadas o textos excesivamente largos. La validación previa reducirá errores de publicación en comunicaciones importantes. La trazabilidad registrará creación, modificación, programación, publicación, retirada y cambios de estado. Cada acción debe asociarse a usuario, fecha y contenido afectado. Para cambios sobre avisos ya publicados se conservará versión anterior, al menos en términos de auditoría, para poder reconstruir qué mensaje estuvo visible en un momento dado.


El rendimiento se cuidará especialmente en la entrega pública. Las consultas de avisos activos serán ligeras, indexadas por fechas y canales, y podrán cachearse. No se debe consultar un conjunto grande de avisos históricos en cada petición. Los avisos caducados podrán archivarse o separarse funcionalmente sin impedir consultas administrativas posteriores. Las pruebas incluirán publicación inmediata, programación futura, caducidad, retirada manual, aviso con HTML no permitido, aviso con enlace externo, visualización en modo oscuro y fallo simulado del servicio consumidor. Por ejemplo, un aviso programado para las 08:00 debe aparecer solo a partir de esa hora, no duplicarse y dejar de mostrarse al alcanzar su fecha de caducidad. La clasificación de avisos permitirá distinguir avisos informativos, avisos críticos, incidencias, mantenimientos programados y comunicaciones de servicio. Cada tipo podrá tener reglas de caducidad, prioridad y canal. Esta taxonomía evita que todos los mensajes se traten igual y facilita que los servicios consumidores decidan cómo presentarlos. Se revisará el formato de integración para que los consumidores reciban datos suficientes: título, cuerpo, prioridad, fechas, ámbito, enlaces, identificador estable y versión. Incluir versión es útil cuando un aviso publicado se corrige, ya que los consumidores pueden invalidar caché y mostrar la versión actual. El editor de avisos deberá evitar que contenido inseguro se introduzca por pegado desde procesadores de texto. Muchos XSS o estilos no deseados entran por HTML copiado. Se aplicará limpieza automática y una previsualización que muestre el resultado real, no el HTML original pegado. La operación contemplará escenarios de emergencia. Para avisos críticos se podrá priorizar publicación rápida, pero manteniendo controles mínimos de seguridad y auditoría. Se definirá quién puede publicar avisos críticos y cómo se registra la actuación. Propuesta de mejora Incorporar una validación de seguridad previa a la publicación que marque enlaces externos, HTML no permitido y recursos no seguros, impidiendo publicar avisos con contenido potencialmente peligroso sin revisión.

- Programación futura con activación exacta.
- Aviso con HTML no permitido y bloqueo de publicación.
- Entrega cacheada a servicio consumidor.
- Auditoría de cambios sobre aviso ya publicado.
##### 1.3.1.1.22. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO DE FOROS (FOR)
Requerimiento EducaMadrid Actualización del aplicativo y su adaptación al entorno de EducaMadrid . El objetivo es asegurar que el aplicativo foros cumpla con las características y funcionalidades requeridas para su correcto funcionamiento en el entorno educativo de EducaMadrid (FOR1). Propuesta técnica de empresa_s La actualización del servicio de Foros (phpBB) se realizará como una adaptación funcional y técnica al ecosistema EducaMadrid. Se revisará autenticación contra LDAP, imagen institucional, versión de PHP, MySQL, plugins, temas y paquetes del sistema. El objetivo es mantener la continuidad de los hilos existentes, evitar pérdida de adjuntos y reforzar seguridad en contenido generado por usuarios.


La autenticación contra LDAP se validará con distintos estados de usuario: activo, deshabilitado, sin atributos requeridos, con cambio de identificador y con pertenencias distintas. El sistema no debe crear cuentas inconsistentes ni permitir acceso a usuarios no válidos. Se revisará el mapeo de atributos para nombre visible, correo, identificador interno y roles, evitando depender de campos no garantizados. La imagen institucional se aplicará mediante tema o capa de personalización mantenible. Se evitarán modificaciones invasivas en el núcleo del aplicativo que dificulten futuras actualizaciones. Los elementos visuales se revisarán en páginas de listado, detalle, respuesta, edición, búsqueda, perfil, mensajes de error y administración. También se comprobará accesibilidad y comportamiento responsive. La seguridad del contenido será crítica. Los foros reciben texto de usuarios, por lo que se revisarán filtros de HTML, tratamiento de enlaces, adjuntos, imágenes, previsualizaciones y menciones. Se aplicarán listas blancas de etiquetas permitidas, validación de extensiones, límites de tamaño y protección frente a XSS almacenado. Los mensajes antiguos se revisarán con herramientas de detección para identificar contenido potencialmente problemático antes de una migración. Se creará el script de bajas de usuarios que anonimizará los usuarios solicitados. La operación deberá conservar la coherencia de hilos y respuestas, pero sustituirá datos personales por valores neutros. No se borrarán mensajes si ello rompe la conversación o afecta a documentación histórica, salvo que exista una instrucción específica. El script debe procesar autoría, perfiles, correos, firmas, adjuntos asociados y referencias visibles. La actualización de plugins y temas incluirá inventario previo, compatibilidad con la nueva versión, análisis de vulnerabilidades conocidas y pruebas funcionales. Los plugins no mantenidos o con riesgos se sustituirán o aislarán. En caso de dependencia funcional imprescindible, se valorará parche controlado, pero documentando claramente la desviación para no crear deuda técnica invisible. El rendimiento se abordará revisando búsquedas, listados con muchos hilos, paginación y carga de adjuntos. Si el histórico es amplio, no se deben cargar conversaciones completas sin límites. Los índices sobre campos de búsqueda y ordenación se revisarán antes de poner en producción la nueva versión. Se prestará atención a consultas de administración, que a menudo se prueban menos pero pueden operar sobre mucho volumen. Las pruebas incluirán login LDAP, creación de tema, respuesta con HTML permitido, intento de XSS, adjunto no permitido, búsqueda de hilos antiguos, anonimización de usuario y comprobación de permisos. Un ejemplo concreto será anonimizar un usuario con varios hilos iniciados y respuestas intermedias, verificando que el flujo de conversación sigue siendo comprensible pero sin datos personales visibles. La migración de Foros se planificará con una copia de datos en preproducción. Se revisará si la nueva versión transforma esquemas, índices, permisos o formatos de adjuntos. Los hilos antiguos se abrirán en muestra representativa, verificando que autoría, fechas, citas, enlaces y adjuntos siguen siendo coherentes. La moderación y administración se revisarán desde el punto de vista funcional. Los perfiles que puedan borrar, editar, cerrar o destacar hilos deberán quedar claros. Si se detectan permisos demasiado amplios, se propondrá una configuración de menor privilegio. La trazabilidad de acciones de moderación será especialmente importante.


El script de anonimización incorporará una política para mensajes citados o menciones textuales. Aunque se anonimice el perfil de un usuario, puede existir su nombre escrito dentro de mensajes de otros usuarios. Se propondrá un informe de posibles menciones para revisión, evitando modificaciones automáticas que alteren el contenido de terceros sin criterio. En rendimiento, se medirá el comportamiento de búsquedas por texto y listados de hilos con muchos mensajes. Si la búsqueda nativa no escala, se limitarán resultados, se aplicarán índices o se estudiará una mejora posterior de búsqueda, manteniendo el alcance de la actualización principal controlado. Propuesta de mejora Incorporar autencitación contra SSO.
##### 1.3.1.1.23. APARTADO: MEJORAS Y MANTENIMIENTO DEL SERVICIO DE BOLETINES (BOL)
Requerimiento EducaMadrid Mantenimiento en el aplicativo Boletines con el objetivo de mejorar la seguridad, actualizar el código a versiones más recientes de PHP y MySQLi, y añadir nuevas funcionalidades. El objetivo es asegurar que el aplicativo sea seguro, eficiente y compatible con las últimas versiones de tecnologías y con las características de EducaMadrid (BOL1). Propuesta técnica de empresa_s Boletines combina edición de contenidos, administración, envío por correo y vistas públicas. La evolución se centrará en actualizar el código a PHP 8+ y MySQLi, corregir problemas de seguridad y mejorar funcionalidades de edición, recorte de imágenes y compatibilidad con modo oscuro. Se tratará como un servicio con impacto público, donde un fallo de contenido o envío puede afectar a muchos usuarios. La migración a MySQLi no se limitará a sustituir funciones obsoletas. Se revisará la forma de construir consultas, la validación de parámetros, la codificación de caracteres, el tratamiento de errores y el uso de transacciones cuando exista modificación de varios registros relacionados. Las consultas de administración, listados y búsqueda se revisarán para evitar inyección SQL y para mejorar rendimiento. La compatibilidad con PHP 8+ exigirá revisar tipos, warnings convertidos en errores, dependencias antiguas, uso de funciones retiradas y tratamiento de valores nulos. Se ejecutarán pruebas con datos reales representativos para detectar errores que solo aparecen con boletines antiguos, imágenes heredadas o campos opcionales. Los ajustes se documentarán para que futuras actualizaciones no dependan de conocimiento informal. La herramienta de recorte de imágenes se revisará para permitir transparencias. Se controlarán formatos PNG, JPEG y otros admitidos, tamaño máximo, orientación EXIF, relación de aspecto y calidad final. El recorte deberá mantener canal alfa cuando corresponda y no convertir imágenes transparentes en fondos negros o blancos inesperados. También se validará que no se puedan subir ficheros camuflados con extensión de imagen. La compatibilidad con modo oscuro se tratará en dos ámbitos: administración y vistas públicas. Se revisarán colores de fondo, texto, enlaces, bordes, botones, tablas, imágenes con transparencia y plantillas de boletines. En boletines enviados por correo se tendrá especial cuidado, ya que los clientes de correo interpretan el modo oscuro de forma distinta. Se propondrán estilos robustos y pruebas en clientes representativos.


El incremento de seguridad incluirá protección CSRF en acciones de administración, saneamiento de HTML, control de adjuntos, limitación de tamaño de imágenes, cabeceras seguras, sesiones, permisos y validación de destinatarios. Se revisará el flujo de envío para evitar envíos accidentales: confirmación previa, prueba a destinatario interno, resumen de destinatarios y bloqueo de envío si faltan campos críticos. El rendimiento se atenderá en listados de boletines, generación de vistas previas y envíos masivos. Los envíos no deberán bloquear una petición web durante mucho tiempo; se propondrá cola o proceso controlado cuando el volumen lo justifique. El estado del envío registrará pendientes, enviados, fallidos y reintentos, permitiendo diagnosticar incidencias sin reenviar de forma indiscriminada. Las pruebas cubrirán edición de boletín, imagen con transparencia, vista pública en modo claro y oscuro, envío de prueba, HTML no permitido, migración de boletín antiguo y revisión de enlaces. Un ejemplo será cargar un PNG transparente, recortarlo, insertarlo en un boletín y comprobar que se visualiza correctamente tanto en la web como en una previsualización de correo. El saneamiento de HTML en Boletines será más estricto en administración que en visualización pública. El editor podrá permitir cierto formato, pero al guardar se normalizará el contenido a un conjunto seguro de etiquetas. Esto evita que un boletín antiguo o copiado desde una fuente externa introduzca estilos que rompan la página o ejecuten código. La migración tecnológica incluirá revisión de librerías JavaScript asociadas a edición, recorte y previsualización. Las librerías obsoletas o sin mantenimiento son un riesgo frecuente en aplicaciones históricas. Se propondrá sustituir componentes vulnerables por versiones mantenidas o por implementaciones simples cuando el uso sea limitado. Para el envío por correo se diferenciará entre composición, prueba, programación y envío real. Un boletín no debería pasar a difusión masiva sin una prueba previa. Se conservará el resultado de los envíos de prueba y se mostrará al operador un resumen con asunto, remitente, destinatarios estimados y enlaces detectados. La compatibilidad de modo oscuro se comprobará en plantillas con imágenes transparentes y fondos no blancos. Se evitará depender exclusivamente de colores inline difíciles de mantener. Donde sea posible, se aplicarán clases y variables que puedan reutilizarse en la web pública y en administración. Propuesta de mejora Añadir una validación previa al envío que revise enlaces rotos, imágenes externas, contraste en modo oscuro, tamaño total del boletín y etiquetas HTML no permitidas antes de autorizar la difusión.
- Migración a MySQLi con consultas parametrizadas.
- Recorte de PNG con transparencia conservada.
- Boletín en modo oscuro y cliente de correo.
- Envío de prueba antes de difusión final.
##### 1.3.1.1.24. APARTADO: MEJORAS Y MANTENIMIENTO DE LA AYUDA (AYU)
Requerimiento EducaMadrid


Actualización del aplicativo que sirve la ayuda de la plataforma. El objetivo es asegurar que la actualización mantenga la integridad de los datos y las URLs actuales, y que incorpore nuevas funcionalidades como un chatbot con IA y la imagen institucional (AYU1). Propuesta técnica de empresa_s La Ayuda se actualizará preservando páginas, URLs, contenidos y enlaces existentes, ya que muchas referencias pueden estar integradas en comunicaciones, portales, servicios y respuestas del CAU. La actuación combinará actualización tecnológica, mejora de mantenimiento de contenidos y creación de un chatbot con IA basado en RAG cerrado sobre las páginas de ayuda. La actualización de la aplicación comenzará con inventario de páginas, categorías, plantillas, enlaces internos, imágenes, adjuntos y rutas públicas. Se identificarán páginas obsoletas, duplicadas o huérfanas, pero no se eliminarán sin validación funcional. Cuando sea necesario reorganizar contenido, se conservarán redirecciones para no romper enlaces publicados. El chatbot se construirá como un RAG alimentado únicamente con las páginas de la Ayuda. Podrá implementarse con LAMB, Onyx u otra solución equivalente, siempre que permita restringir fuentes, mostrar referencias y bloquear respuestas sin contexto suficiente. El sistema no debe responder con conocimiento general ni inventar procedimientos. Su función será localizar, resumir y explicar información ya publicada por EducaMadrid. La indexación se realizará a partir del contenido publicado, no de borradores. Cada fragmento del índice mantendrá metadatos de página, título, URL, fecha de actualización y categoría. Cuando una página cambie, se reindexará solo el contenido afectado. Cuando una página se despublique, dejará de estar disponible para el chatbot. Esto garantiza coherencia entre lo que se puede leer en la web y lo que responde la IA. Las respuestas del chatbot incluirán enlaces a las páginas fuente y, cuando sea posible, indicarán la sección concreta utilizada. Si la pregunta es ambigua, el asistente pedirá concreción. Si no encuentra contexto suficiente, indicará que no dispone de respuesta validada. Este comportamiento será especialmente importante en temas de cuentas, seguridad, aulas virtuales, correo o procedimientos administrativos. La interfaz se integrará en la Ayuda sin sustituir la navegación clásica. El buscador tradicional seguirá siendo útil para usuarios que prefieren explorar contenidos. El chatbot se presentará como apoyo conversacional, con mensajes claros sobre el alcance de las respuestas. Se cuidará accesibilidad, navegación por teclado, contraste y lectura por tecnologías de apoyo. Para el personal de soporte, se podrá habilitar un modo de borrador de respuesta. En este modo, la IA propondrá una contestación fundamentada en páginas de ayuda, pero el operador la revisará antes de enviarla a un usuario. Esto reduce tiempos de respuesta del CAU sin delegar completamente la comunicación en un modelo. Las pruebas incluirán modificación de una página y reindexación, consulta con respuesta directa, pregunta fuera de ámbito, pregunta ambigua, página retirada y comparación entre respuesta generada y contenido fuente. Un ejemplo será actualizar una guía de recuperación de contraseña, reindexarla y comprobar que el chatbot responde con la versión nueva y enlaza a la página correcta. La calidad del RAG de Ayuda dependerá de la calidad de las páginas fuente. Por ello se propondrá una revisión de contenidos duplicados, páginas obsoletas y respuestas demasiado largas. El chatbot no corrige una base documental confusa; la hace más visible. La actuación incluirá recomendaciones de estructura para que la ayuda sea más recuperable. Página 139 de 192


El índice del chatbot conservará jerarquía de navegación: categoría, página, subtítulo y URL. Esta jerarquía permitirá que la respuesta no solo cite una página, sino que oriente al usuario dentro del bloque correcto. En consultas frecuentes, esto será más útil que devolver una respuesta aislada. Se controlará la inyección de prompt por contenido. Si una página de ayuda o un texto indexado contiene instrucciones que podrían alterar el comportamiento del modelo, el sistema deberá tratarlas como contenido documental y no como instrucciones. Esta medida es importante en cualquier RAG expuesto a contenido editable. Para soporte, se podrán registrar consultas sin respuesta de forma anonimizada. Esta lista permitirá priorizar nuevas páginas o aclarar contenidos existentes. El objetivo es que la IA ayude a mejorar la documentación oficial, no sustituirla por respuestas no gobernadas.
##### 1.3.1.1.25. APARTADO: MEJORAS Y MANTENIMIENTO DEL PORTAL (POR)
Requerimiento EducaMadrid Desarrollo de APIs y mejoras de seguridad en el portal de EducaMadrid. El objetivo es proporcionar funcionalidades para dar de alta profesores interinos, incorporar usuarios a través de APIs, y mejorar la seguridad y la política de contraseñas en el portal (POR1). Propuesta técnica de empresa_s Las mejoras del Portal se centran en APIs, seguridad, política de contraseñas y adaptación de componentes visibles. La intervención se realizará con especial atención a la convivencia entre Liferay, servicios de identidad, formularios de alta y aplicaciones que consumen información del Portal. Cada cambio deberá mantener compatibilidad con integraciones existentes y con la imagen institucional. El alta de profesores interinos desde la plataforma de formación se implementará mediante una API controlada. La API validará identificadores, correo alternativo, datos mínimos, centro 9999, estado inicial y reglas de creación. Se definirá respuesta estructurada para éxito, duplicado, datos incompletos, usuario no permitido o error técnico. Esta respuesta permitirá que la plataforma cliente informe correctamente sin depender de mensajes libres. La gestión de credenciales temporales se diseñará con caducidad, registro de entrega y política de seguridad. No se almacenarán contraseñas en claro ni se expondrán en logs. El usuario deberá completar el flujo de cambio de contraseña conforme a la política de EducaMadrid. Los errores se registrarán de forma técnica, pero los mensajes al usuario serán comprensibles y no revelarán información sensible. La limpieza de HTML en Liferay se resolverá mediante lista blanca de etiquetas y atributos permitidos. Se eliminarán etiquetas BODY, scripts, eventos JavaScript, estilos peligrosos y estructuras que puedan alterar la página completa. El objetivo es permitir contenido enriquecido razonable sin exponer el Portal a XSS o roturas visuales. La limpieza se aplicará tanto al guardar como al renderizar cuando proceda. La página de recuperación de contraseña de Cloud se adaptará a la imagen institucional, pero respetando los requisitos de seguridad del flujo. Se revisarán textos, logotipos, mensajes de error, compatibilidad móvil, accesibilidad y coherencia con el resto de EducaMadrid. No se introducirán cambios que permitan enumerar usuarios o revelar si una cuenta existe. Los web services se documentarán con rutas, métodos, parámetros, códigos de respuesta, autenticación, ejemplos y límites de uso. La documentación deberá permitir mantener la


integración sin revisar código. También se propondrá un entorno de pruebas o simulación para validar clientes antes de utilizar datos reales. El rendimiento se controlará en endpoints que puedan recibir muchas solicitudes. Se aplicarán validaciones tempranas, límites de frecuencia si procede, logs agregados y métricas de error. Las operaciones de alta o modificación deberán ser idempotentes cuando tenga sentido, para que un reintento no cree duplicados. Las pruebas cubrirán alta correcta, duplicado, identificador incorrecto, correo alternativo inválido, limpieza de HTML con contenido peligroso, recuperación de contraseña en móvil y error del servicio de identidad. Un ejemplo será enviar dos veces la misma solicitud de alta y verificar que la segunda devuelve un estado controlado sin crear otra cuenta. Los endpoints del Portal se diseñarán con versionado. Una ruta versionada permite evolucionar campos o reglas sin romper integraciones existentes. Cuando se introduzca una versión nueva, se documentará el periodo de convivencia y los cambios respecto a la anterior. La seguridad de APIs incorporará autenticación de sistema a sistema, límites de uso, validación de origen y registros de auditoría. No se expondrán endpoints administrativos sin protección reforzada. Las respuestas de error distinguirán entre errores funcionales y técnicos, pero sin revelar información interna. En el alta de interinos se revisará especialmente el tratamiento de duplicados. Un mismo usuario podría existir por otra vía o haber cambiado de estado. La API deberá resolver estas situaciones con estados claros: ya existe activo, existe deshabilitado, alta pendiente, datos inconsistentes o alta realizada. La adaptación visual de recuperación de contraseña se probará también en situaciones de error: token caducado, usuario no encontrado, contraseña no válida y servicio no disponible. Estos casos suelen descuidarse y son los que más tickets generan cuando los mensajes no son claros. Propuesta de mejora Añadir un endpoint de validación previa para que los sistemas consumidores comprueben si una solicitud sería aceptada antes de ejecutar el alta definitiva, reduciendo errores operativos y tickets de soporte.
- Alta de interino con centro 9999.
- Reintento idempotente sin duplicidad.
- Sanitización de HTML con script embebido.
- Recuperación de contraseña sin enumeración de usuarios.
##### 1.3.1.1.26. APARTADO: MEJORAS Y MANTENIMIENTO DE LA WEB ESTÁTICA (WES)
Requerimiento EducaMadrid Mejora de la web estática del portal EducaMadrid. El objetivo es asegurar que la web sea accesible y multilingüe, cumpliendo con los estándares de accesibilidad definidos para los portales y aplicaciones del sector público (WES1). Propuesta técnica de empresa_s La mejora de la Web Estática se orientará a accesibilidad, multilingüismo y mantenimiento seguro de contenidos. La revisión comenzará con un inventario de páginas, plantillas, componentes, menús, recursos estáticos, enlaces, metadatos, idiomas disponibles y dependencias de


publicación. La solución no buscará rehacer el sitio, sino mejorar puntos concretos sin romper estructura ni posicionamiento. El selector de idioma se diseñará como un componente accesible, visible y coherente. Deberá indicar el idioma actual, permitir cambio sin perder contexto cuando exista página equivalente y comportarse correctamente con teclado y lector de pantalla. La preferencia podrá persistir sin impedir que el usuario elija otro idioma. Cuando una página no exista en el idioma solicitado, se mostrará un mensaje claro y se ofrecerá alternativa. La accesibilidad se revisará en navegación, encabezados, enlaces, contraste, foco visible, textos alternativos, formularios si existieran y estructura semántica. Se priorizarán páginas críticas y componentes reutilizados, ya que corregir una plantilla común puede mejorar muchas páginas a la vez. Las validaciones automáticas se complementarán con revisión manual de navegación por teclado. La revisión de enlaces detectará enlaces rotos, redirecciones innecesarias, recursos mixtos HTTP/HTTPS, enlaces externos sin aviso cuando proceda y documentos pesados. Los resultados se clasificarán por criticidad. Un enlace roto en una página informativa principal tendrá prioridad sobre enlaces antiguos de baja visibilidad. En rendimiento se revisarán imágenes, hojas de estilo, JavaScript, caché y recursos no utilizados. Las páginas estáticas deben cargar rápido incluso en dispositivos modestos. Se propondrán optimizaciones conservadoras: compresión, tamaños adecuados de imagen, eliminación de recursos duplicados y revisión de cabeceras de caché. La publicación de cambios incluirá validación previa. Antes de desplegar, se ejecutará una comprobación de enlaces, accesibilidad básica, metadatos, visualización responsive y presencia de textos traducidos. Este control evita que una corrección de contenido introduzca errores visuales o de navegación. La documentación indicará cómo crear una página multilingüe, cómo enlazar documentos, cómo usar el selector de idioma y qué criterios de accesibilidad deben respetarse. La idea es reducir errores futuros y no depender únicamente de revisión técnica posterior. Las pruebas incluirán cambio de idioma desde una página con equivalente, cambio desde una página sin equivalente, navegación por teclado, revisión de contraste, enlace roto simulado y carga en móvil. Un ejemplo será acceder a una página en español, cambiar a inglés y comprobar que se conserva el contexto y que el selector anuncia correctamente el idioma activo. El multilingüismo deberá contemplar metadatos y no solo texto visible. Títulos de página, descripciones, etiquetas de idioma, atributos lang y enlaces alternativos son relevantes para accesibilidad y buscadores. El selector de idioma deberá integrarse con esta información. La revisión de contenidos estáticos incluirá documentos enlazados, no solo HTML. Si una página accesible enlaza a PDFs antiguos, documentos pesados o ficheros sin descripción, se reflejará en la matriz de revisión. Esto ayuda a priorizar una mejora real de experiencia. Se propondrá una validación automática en el proceso de publicación. Cuando se incorporen cambios, el sistema podrá ejecutar comprobación de enlaces y reglas básicas de accesibilidad. No sustituye a revisión humana, pero evita errores evidentes antes de publicar. La mejora se realizará sin introducir dependencias complejas. En una web estática, añadir demasiado JavaScript para resolver el idioma o los componentes puede empeorar rendimiento y accesibilidad. Se priorizarán soluciones simples, semánticas y mantenibles.


Propuesta de mejora Crear una matriz de páginas críticas con estado de traducción, puntuación de accesibilidad, enlaces rotos y fecha de revisión, útil para priorizar actuaciones sin rehacer todo el portal estático.
- Selector de idioma con teclado.
- Página sin traducción disponible.
- Detección de enlace roto.
- Revisión de contraste en componentes comunes.
##### 1.3.1.1.27. APARTADO: MEJORAS Y MANTENIMIENTO DEL FRAMEWORK DE INTERFAZ (IFZ)
Requerimiento EducaMadrid Mejora progresiva del framework de interfaz utilizado en EducaMadrid para el desarrollo de aplicaciones propias. El objetivo es actualizar y enriquecer el framework con las últimas versiones de Bootstrap, jQuery y TinyMCE, y proporcionar funcionalidades básicas predefinidas que faciliten el desarrollo de interfaces web en los proyectos de EducaMadrid (IFZ1). Propuesta técnica de empresa_s El Framework de Interfaz debe actuar como base común para aplicaciones propias de EducaMadrid. Su evolución se abordará como una librería interna documentada y versionada, no como un conjunto de estilos dispersos. El objetivo es ofrecer componentes reutilizables que reduzcan duplicidad, mejoren accesibilidad y faciliten la coherencia visual entre aplicaciones. Los componentes solicitados se diseñarán con accesibilidad desde origen. Los modales controlarán foco, cierre por teclado, etiquetado ARIA y retorno del foco al elemento invocador. Las alertas serán anunciables por lectores de pantalla. Las pestañas permitirán navegación por teclado. Los menús serán comprensibles en móvil y escritorio. Las tablas tendrán encabezados adecuados, estados vacíos y comportamiento responsive. La compatibilidad con modo claro y oscuro se resolverá mediante variables de diseño, no duplicando estilos completos. Colores, fondos, bordes, sombras y estados de interacción se definirán como tokens reutilizables. Esto permitirá que las aplicaciones adopten el framework sin crear soluciones específicas para cada una. También facilitará cambios futuros de imagen institucional. La documentación será parte del entregable. Cada componente tendrá ejemplo funcional, parámetros admitidos, eventos JavaScript, estructura HTML esperada, recomendaciones de uso y casos no recomendados. Se incluirán fragmentos de código copiable y una página de demostración interna. Esta documentación es clave para que el framework no quede infrautilizado. La integración con aplicaciones existentes se hará de forma progresiva. No se impondrá una sustitución completa en servicios legacy, sino que se identificarán puntos de mayor valor: formularios, mensajes, botones, tablas, modales y navegación. En aplicaciones PHP antiguas se facilitarán fragmentos compatibles con renderizado servidor. La calidad se garantizará con pruebas visuales y de accesibilidad. Se comprobarán componentes en diferentes anchos de pantalla, navegadores actuales, modo claro, modo oscuro y navegación por teclado. Los cambios en el framework deberán evaluarse contra una galería de ejemplos para evitar regresiones en componentes existentes. El versionado permitirá que una aplicación consuma una versión estable mientras otra prueba una actualización. Se documentarán cambios incompatibles y pautas de migración. En la medida de lo


posible, las nuevas versiones mantendrán compatibilidad hacia atrás para no obligar a actualizar todos los servicios simultáneamente. Un ejemplo de aplicación sería sustituir mensajes de error dispersos en varias aplicaciones por un componente común de alerta con nivel, icono, texto, enlace de ayuda y accesibilidad. Esto mejora coherencia y reduce código duplicado sin exigir reescribir la aplicación completa. El framework deberá ofrecer criterios de uso, no solo componentes. Por ejemplo, cuándo usar un modal frente a una página completa, cuándo usar una alerta persistente o cuándo evitar pestañas. Esto mejora la coherencia funcional entre aplicaciones y evita abuso de componentes. Se definirá una nomenclatura común para clases, variables y estados. Nombres consistentes reducen errores al integrar el framework en aplicaciones PHP, Liferay u otros entornos. La documentación incluirá ejemplos con HTML mínimo y variantes frecuentes. El control de regresión visual se apoyará en una galería de componentes. Cada cambio en CSS o JavaScript se probará contra la galería para detectar alteraciones inesperadas. Esto es especialmente útil cuando varios servicios consumen el mismo framework. El framework facilitará mensajes de validación accesibles para formularios. Muchos aplicativos propios repiten código de errores; un patrón común permitirá asociar error, campo y resumen de validación de manera consistente. Propuesta de mejora Entregar un catálogo vivo de componentes desplegado internamente, con ejemplos funcionales, código copiable y validación de modo claro/oscuro, para acelerar adopción por los equipos técnicos.

- Modal con foco controlado.
- Tabla responsive con encabezados accesibles.
- Componente validado en modo oscuro.
- Cambio de versión sin romper aplicaciones consumidoras.
##### 1.3.1.1.28. APARTADO: MEJORAS Y MANTENIMIENTO DE ENTORNOS MAX (MAX)
Requerimiento EducaMadrid Actualización y mejora del entorno MAX en la plataforma educativa EducaMadrid, con el fin de garantizar un entorno seguro y eficiente para la realización de exámenes a través del Aula Virtual (MAX1). Propuesta técnica de empresa_s La actualización de Entornos MAX se orientará a proporcionar un entorno seguro y eficiente para exámenes a través del Aula Virtual. La actuación combinará actualización de contenidos, revisión del sistema operativo, mejora del navegador con opciones limitadas y adaptación a la realidad de equipos de centros educativos. La página web de MAX se revisará para ofrecer información clara sobre descarga, instalación, uso en exámenes, requisitos y resolución de incidencias frecuentes. Se cuidará que los enlaces sean actuales y que las instrucciones distingan entre usuarios docentes, alumnado y administradores técnicos de centro. La documentación debe evitar ambigüedades en momentos sensibles como pruebas o evaluaciones.


El navegador con opciones limitadas se diseñará para reducir distracciones y accesos no deseados durante exámenes. Mostrará un buscador de Aulas Virtuales de EducaMadrid que permita localizar rápidamente el entorno correspondiente, pero limitará navegación fuera de los dominios permitidos. Las restricciones se definirán de forma configurable para facilitar ajustes sin recompilar todo el entorno. La seguridad se abordará desde configuración del navegador, políticas de red, bloqueo de funciones no necesarias, gestión de certificados, control de descargas y comportamiento ante ventanas emergentes. No se buscará una falsa invulnerabilidad, sino un entorno razonablemente controlado, documentado y adecuado para evaluación en centros. La compatibilidad con Moodle y con configuraciones reales de centros será clave. Se probará acceso a login, navegación por curso, cuestionarios, recursos, entregas, temporizadores, ventanas de confirmación y cierre de sesión. También se revisarán escenarios con conectividad limitada, certificados corporativos y equipos con hardware modesto. El proceso de actualización del sistema operativo y paquetes se realizará en una imagen controlada. Se documentarán versiones, dependencias, cambios relevantes y procedimiento de generación. Se mantendrá capacidad de reproducir la imagen y de comparar una versión con la anterior, evitando actualizaciones manuales no documentadas. La página de autodiagnóstico previa al examen permitirá comprobar versión, conectividad, acceso al aula y restricciones básicas antes del inicio de una prueba. Esta comprobación ayuda a detectar problemas antes de que afecten a un grupo completo de alumnos. Las pruebas incluirán instalación en equipo representativo, acceso a Aula Virtual, cuestionario con temporizador, bloqueo de navegación externa, descarga no permitida, cambio de red y autodiagnóstico. Un ejemplo será ejecutar una simulación de examen con un aula de prueba, verificando que el alumno puede acceder al cuestionario pero no navegar libremente a sitios no autorizados. El navegador limitado deberá registrar información diagnóstica no personal: versión, configuración aplicada y resultado de pruebas de conectividad. Esta información puede mostrarse al docente o técnico de centro para resolver incidencias antes del examen sin recoger datos innecesarios del alumno. La lista de dominios permitidos se gestionará de forma controlada. No debe requerir reconstruir todo el entorno para un ajuste menor, pero tampoco debe poder modificarse por usuarios no autorizados. Se propondrá una configuración firmada o distribuida por canal controlado. La documentación para centros incluirá una secuencia de preparación: actualizar imagen, ejecutar autodiagnóstico, probar aula de ejemplo, revisar conectividad y confirmar versión. Esta guía operativa reducirá incidencias de última hora. Las pruebas de examen se realizarán con distintos tipos de actividad de Moodle, no solo con una página de acceso. Cuestionarios, entregas, recursos embebidos y ventanas de confirmación pueden comportarse de forma distinta dentro de un navegador restringido.
##### 1.3.1.1.29. APARTADO: MEJORAS Y MANTENIMIENTO DEL PROYECTO GESTIÓN DE
TÍTULOS (GES)
Requerimiento EducaMadrid Actualización y mejora del aplicativo de Gestión de Títulos en la plataforma educativa EducaMadrid. El objetivo es asegurar la compatibilidad con la última versión de PHP, mejorar la Página 145 de 192


seguridad del código, optimizar la base de datos y sus consultas, y añadir funcionalidades específicas para la generación de archivos de impresión de títulos (GES1). Propuesta técnica de empresa_s La intervención en Gestión de Títulos se centrará en revisar el código y mejorar el sistema de generación de ficheros, especialmente para producir archivos en formato DBF con codificación UTF-8 o CP850 según requiera el circuito administrativo. Al tratarse de un proceso que puede alimentar aplicaciones externas o impresión, la prioridad será la exactitud de datos y la trazabilidad de cada generación. La revisión comenzará identificando entradas, transformaciones y salidas. Se documentará qué campos recibe el sistema, qué validaciones aplica, qué campos son obligatorios, qué transformaciones de caracteres se realizan y cómo se genera el fichero final. Esta lectura permitirá detectar reglas implícitas que actualmente puedan estar dispersas en el código. La generación de DBF se encapsulará en un módulo específico, con una interfaz clara desde el resto de la aplicación. Este módulo controlará longitudes de campo, tipos, codificación, caracteres no representables, valores nulos y formato de fechas. Cuando un carácter no pueda convertirse correctamente, el sistema lo registrará y aplicará una política definida, evitando sustituciones silenciosas que puedan alterar nombres o datos oficiales. Se añadirá una validación previa de datos antes de generar el fichero. Esta validación comprobará campos obligatorios, caracteres incompatibles, longitudes máximas, formatos de fecha, códigos esperados y duplicados si procede. Los errores se presentarán en un informe claro para corregirlos antes de emitir el fichero definitivo. El proceso de generación conservará evidencias: fecha, usuario, parámetros, número de registros, codificación utilizada y resultado. Si se repite una generación, será posible distinguir si se trata de una regeneración idéntica o de una emisión con datos modificados. Esta trazabilidad es importante en procedimientos administrativos donde el fichero tiene valor operativo. La compatibilidad con aplicaciones consumidoras se verificará con ficheros de prueba. No basta con que el DBF se genere sin error; debe poder abrirse en la aplicación destino y mostrar los caracteres correctamente. Se probarán nombres con tildes, eñes, caracteres especiales, campos largos y registros límite. La actualización de código revisará también seguridad y mantenimiento: validación de parámetros, permisos de generación, exposición de ficheros, limpieza de temporales y logs. Los ficheros generados no deberán quedar accesibles públicamente ni permanecer indefinidamente en ubicaciones temporales. Un ejemplo de prueba será generar un DBF con nombres que contengan “Ñ”, tildes y apellidos compuestos, abrirlo en la aplicación destino y comparar registro por registro con los datos origen. Si se detecta una conversión problemática, el informe deberá señalar el campo y el registro afectado. La conversión de codificación se probará con un catálogo de caracteres representativos. No se limitará a nombres simples; se incluirán tildes, eñes, diéresis, apóstrofos, guiones, caracteres extranjeros y campos al límite de longitud. El informe previo mostrará qué registros requieren atención.


El módulo de generación separará validación de emisión. Primero se validan datos y se corrigen errores; después se genera el fichero. Esta separación evita generar ficheros parcialmente válidos que luego fallan en la aplicación destino. La gestión de temporales se controlará para que los ficheros no queden en rutas accesibles ni se acumulen indefinidamente. Se aplicará limpieza programada o eliminación al finalizar la descarga, según el flujo que defina el entorno. La documentación incluirá una ficha de formato DBF: campos, longitudes, codificación, origen de datos y reglas especiales. Esta ficha será útil para soporte y para futuras adaptaciones si cambia la aplicación consumidora. Propuesta de mejora Mejora propuesta: añadir un validador previo de ficheros que simule la conversión de codificación y muestre sustituciones o caracteres problemáticos antes de generar el DBF definitivo.
- Generación DBF en UTF- 8 y CP850.
- Detección de carácter no convertible.
- Control de longitud máxima de campo.
- Validación con aplicación consumidora.
##### 1.3.1.1.30. APARTADO: MEJORAS DEL PROYECTO DE MEDIDAS DE USO DE LAS WEB
(USO) Requerimiento EducaMadrid Desarrollar una prueba de concepto basada en tecnologías de software libre que aporte una herramienta robusta y actualizada para recoger datos estadísticos de las páginas web de los centros educativos elaboradas con WordPress, creando un plugin en el entorno WordPress Multisite para una recogida estadística independiente por centro (USO1). Propuesta técnica de empresa_s La prueba de concepto de Medidas de Uso se planteará con software libre y orientada a webs de centros en WordPress Multisite. La solución deberá separar datos por centro, facilitar consulta desde la administración de cada sitio y aportar métricas útiles sin introducir una carga excesiva en las páginas. La POC tendrá un alcance controlado, pero suficientemente realista para validar seguridad, rendimiento y utilidad funcional. El plugin de WordPress se diseñará como una integración ligera. Gestionará configuración por sitio, activación o desactivación, inserción del código de seguimiento, permisos de consulta y presentación de paneles resumidos. Se evitará que cada centro tenga que configurar manualmente parámetros técnicos complejos. La configuración central podrá definir valores por defecto. Las métricas incluirán navegadores, páginas más visitadas, errores 404 y 500, tiempos de carga, fuentes de tráfico, dispositivos y datos agregados de geolocalización cuando proceda. Se priorizarán indicadores accionables para los centros. Por ejemplo, una lista de enlaces rotos o páginas lentas puede ser más útil que un panel estadístico excesivamente complejo. La privacidad se tendrá en cuenta desde el diseño. La recogida de datos será proporcional, con anonimización o minimización cuando sea posible. Se revisará qué datos se almacenan, durante


cuánto tiempo, quién puede consultarlos y cómo se separan los datos de cada centro. La solución no debe permitir que un centro vea estadísticas de otro. La POC se desplegará en un sitio piloto de site.educa.madrid.org. Se validará que el código de seguimiento carga correctamente, que no degrada tiempos de respuesta, que los eventos se registran y que los paneles muestran información coherente. También se comprobará comportamiento con caché, usuarios autenticados, páginas públicas y errores simulados. La arquitectura contemplará un servicio estadístico separado de WordPress cuando resulte adecuado, de modo que el plugin actúe como cliente y no convierta el WordPress Multisite en almacén de grandes volúmenes de analítica. Esta separación facilita escalar, mantener y actualizar el sistema sin tocar cada sitio individualmente. Los permisos dentro de WordPress se mapearán con roles existentes. Un administrador de sitio podrá ver sus métricas, pero no modificar configuración global ni acceder a otros centros. La administración central podrá consultar estado de despliegue, sitios activos y errores de integración. Las pruebas incluirán sitio piloto, página inexistente para generar 404, medición de tiempos, acceso por rol autorizado y no autorizado, revisión de separación de datos y desactivación del plugin. Un ejemplo será publicar una página de prueba, visitarla desde distintos navegadores y confirmar que aparece en el panel del centro correcto sin datos de otros sitios. La POC deberá medir el coste añadido al frontal de WordPress. Aunque el plugin sea ligero, cada página pública puede recibir tráfico. Se comprobará tamaño del script, tiempos de carga, comportamiento con caché y errores cuando el servicio estadístico no esté disponible. Se definirá claramente qué datos son visibles para cada centro. Un administrador de un sitio no debe ver métricas globales ni de otros centros. La administración central, en cambio, podrá ver indicadores agregados para evaluar el estado del servicio. La integración con WordPress Multisite se realizará respetando la arquitectura compartida de código. El plugin debe desplegarse de forma central, pero permitir configuración por sitio. Esto evita mantener copias o variantes por centro. El piloto se cerrará con una evaluación técnica y funcional: utilidad de métricas, carga generada, incidencias, calidad de datos y esfuerzo de operación. Solo después se propondrá una extensión progresiva a más centros. Propuesta de mejora Se realizará una instalación de rybbit como sorftware opensource conectándolo contra el sso de la plataforma y creando un script para generar entornos para los centros solicitados, de modo que se generen códigos para insertar directamente en wordpress o Moodle y poder recoger estadísticas de estos centros consultables directamente por el propio centro.
##### 1.3.1.1.31. APARTADO: MEJORAS Y MANTENIMIENTO DE WEKAN (WEK)
Requerimiento EducaMadrid Adaptar al entorno de la plataforma educativa la última versión disponible del aplicativo Wekan.
- Realizar un análisis de compatibilidad de versiones.
- Actualizar los paquetes del sistema operativo y sus dependencias.
- Configurar y optimizar el servidor web Apache.
- Configurar y optimizar la base de datos MongoDB.


- Instalar y configurar PHP, Java, Node.js, npm, y Yarn.
Propuesta técnica de empresa_s Wekan se actualizará a la última versión disponible compatible con el entorno EducaMadrid , priorizando un despliegue reproducible mediante Docker. La actuación partirá de un inventario de la instalación actual: versión, base de datos, variables de entorno, personalizaciones, autenticación, tableros, adjuntos, notificaciones, configuración SMTP y modificaciones en código. El despliegue con Docker se definirá mediante una composición versionada, con contenedor de aplicación, MongoDB, volúmenes persistentes, configuración de red, variables de entorno y estrategia de backup. El objetivo es que el entorno pueda reconstruirse de forma controlada en preproducción y producción. Se documentará claramente qué datos son persistentes y qué elementos pertenecen a la imagen. La migración a la nueva versión se ensayará en preproducción con copia controlada de datos. Se revisarán cambios de esquema, compatibilidad de tableros, tarjetas, listas, comentarios, adjuntos, usuarios y permisos. No se desplegará directamente una nueva imagen sin verificar que el arranque, la migración interna y el uso funcional son correctos. La conexión con el SSO de EducaMadrid se estudiará mediante SAML 2.0 u OAuth 2.0 según encaje con la instalación. Se revisarán certificados, URL de retorno, mapeo de atributos, creación de usuarios, desactivación, cambios de correo, roles y comportamiento ante usuarios que ya existen localmente. El objetivo es integrar autenticación sin perder datos históricos. Las modificaciones actuales en código se inventariarán y se portarán de forma controlada. Se distinguirá entre cambios imprescindibles, cambios que pueden resolverse por configuración y cambios que conviene retirar por deuda técnica. Cuando sea necesario mantener una personalización, se integrará en un repositorio versionado y documentado, evitando parches manuales sobre contenedores en ejecución. Se creará el script de bajas de usuarios que anonimizará a los usuarios solicitados. El proceso sustituirá nombre, correo, alias y datos personales por valores neutros, preservando la integridad de tableros, tarjetas, comentarios y actividad histórica. El script tendrá modo simulación e informe de impacto. Se verificará especialmente que no se rompan referencias en tarjetas o menciones. La adaptación a imagen institucional se aplicará en logotipos, colores, mensajes, notificaciones y conexión con avisos. Se evitará crear una bifurcación profunda del producto; siempre que sea posible se utilizarán variables, configuración, temas o recursos externos. La coherencia visual no debe comprometer la capacidad de actualizar Wekan en el futuro. La operación diaria incluirá backups, restauración probada, logs, métricas de disponibilidad y procedimiento de rollback. Una actualización con Docker debe poder revertirse a una imagen anterior si la migración no se ha consolidado. Se documentarán pasos de parada, copia, despliegue, validación y vuelta atrás. Las pruebas incluirán login SSO, usuario existente, creación de tablero, movimiento de tarjeta, comentario, adjunto, notificación, anonimización de usuario y restauración desde backup. Un ejemplo será actualizar en preproducción, anonimizar un usuario con actividad en varios tableros y comprobar que las tarjetas siguen siendo utilizables. El proceso Docker incluirá gestión de secretos. Las credenciales no se dejarán hardcodeadas en ficheros versionados. Se utilizarán variables protegidas, ficheros de entorno con permisos restrictivos o mecanismo equivalente aprobado por el entorno.


Fecha: 21/05/2026

Los backups de Wekan incluirán base de datos y adjuntos. Una copia de MongoDB sin adjuntos, o adjuntos sin coherencia con base de datos, puede no ser suficiente. La restauración se probará en un entorno aislado y se documentará el tiempo estimado. La integración con Avisos se validará como funcionalidad visible. No bastará con que Wekan arranque; se comprobará que notificaciones generadas por el aplicativo se muestran donde corresponde y con formato institucional. La anonimización deberá revisar también actividad y notificaciones históricas. Si el usuario aparece en menciones, asignaciones o suscripciones, el script deberá sustituir datos visibles sin romper relaciones funcionales de tablero. Propuesta de mejora Entregar un Docker Compose versionado con procedimiento de backup y rollback probado, de forma que la actualización de Wekan sea repetible y no dependa de ajustes manuales.

- Arranque de nueva versión con datos migrados.
- SSO con usuario ya existente localmente.
- Anonimización conservando tarjetas y comentarios.
- Rollback probado desde backup anterior.
Ámbito Acción Precaución Docker Compose versionado con Backup antes de migración volúmenes persistentes SSO Mapeo de atributos y usuarios Evitar duplicidades existentes Bajas Anonimización de usuarios Conservar tableros y tarjetas

##### 1.3.1.1.32. APARTADO: MEJORAS Y MANTENIMIENTO DE MAMOOD (MAM)
Requerimiento EducaMadrid Mantenimiento y mejora del aplicativo MaMood, una herramienta clave en la gestión de la plataforma educativa EducaMadrid. El aplicativo se utiliza internamente para tareas como la gestión de altas, bajas, cambios de nombre de aulas virtuales, gestión de WordPress, y gestión del espacio de los centros, entre otras (MAM1). Propuesta técnica de empresa_s MaMood se tratará como una herramienta interna crítica de operación de la plataforma EducaMadrid. Es un aplicativo de código propio basado en PHP y shell scripts, securizado bajo acceso por VPN, desde el que se controlan servicios como altas, bajas, cambios de nombre de aulas virtuales, gestión de WordPress, gestión de espacio de centros y otras operaciones internas. Su naturaleza obliga a extremar control, trazabilidad y validación. La revisión del aplicativo comenzará con un mapa funcional de pantallas, scripts y servicios afectados. Se identificará qué acciones son informativas, cuáles modifican datos internos, cuáles lanzan comandos de sistema y cuáles impactan en servicios externos como Moodle, WordPress o almacenamiento. Esta clasificación permitirá aplicar controles diferentes según riesgo. La actualización a la última versión de PHP y sistema operativo se acompañará de revisión de compatibilidad. Se buscarán funciones obsoletas, cambios de tipos, dependencias de shell, rutas absolutas, permisos de ejecución, variables de entorno y supuestos sobre el sistema operativo


anterior. Los scripts no se actualizarán en bloque sin pruebas, porque cada uno puede tener efectos sobre servicios distintos. Los scripts de aulas virtuales evolucionarán para funcionar dinámicamente leyendo la base de datos de MaMood. Esto reducirá dependencias de listados manuales y errores por desalineación entre configuración y realidad. La lectura dinámica se hará con consultas controladas, filtros por estado, validación de instancia y límites para evitar lanzar operaciones sobre entornos no previstos. El nuevo shell script para programar cambios de código en aulas virtuales MoodleMisc y multisite se diseñará con planificación, bloqueo de concurrencia, ejecución en horas no lectivas, limpieza de cachés y registro detallado. Cada ejecución tendrá identificador, usuario solicitante, instancias afectadas, comandos ejecutados, salida, errores y resultado final. El script no ejecutará parámetros arbitrarios sin validación. La seguridad se reforzará en tres capas: acceso bajo VPN, permisos de aplicación y seguridad de ejecución de scripts. Que el servicio esté bajo VPN no sustituye a un control fino de roles. Se limitarán acciones por perfil, se registrarán operaciones críticas y se evitará que una entrada web pueda convertirse en comando shell no validado. Los scripts se ejecutarán con usuarios del sistema de permisos mínimos. Para mejorar operación, se propondrá un orquestador ligero interno que muestre estados de ejecución. No es necesario convertir MaMood en una plataforma compleja, pero sí facilitar que un operador vea si un script está pendiente, en curso, finalizado, fallido o parcialmente completado. Esta visibilidad reduce intervenciones manuales y llamadas entre equipos. El rendimiento se revisará en scripts que recorren múltiples instancias o grandes volúmenes de datos. Se aplicarán ejecuciones por lotes, tiempos máximos, reintentos controlados y paralelismo solo cuando sea seguro. Una operación que limpia cachés en muchas aulas virtuales, por ejemplo, deberá evitar saturar servidores en horario lectivo. Las pruebas incluirán ejecución en modo simulación, lectura dinámica de instancias desde base de datos, programación en horario no lectivo, bloqueo de doble ejecución, limpieza de caché y revisión de logs. Un ejemplo será programar un cambio sobre un subconjunto de aulas de prueba, comprobar salida por instancia y confirmar que una segunda ejecución simultánea queda bloqueada. MaMood incorporará una separación clara entre acciones de consulta y acciones de cambio. Las primeras podrán ejecutarse con menor restricción; las segundas requerirán confirmación, registro y, en algunos casos, ventana horaria. Esta distinción es necesaria porque el aplicativo opera sobre múltiples servicios. Los shell scripts se normalizarán con cabecera común: descripción, parámetros, prerequisitos, usuario de ejecución, logs, códigos de salida y ejemplos. Esta normalización no cambia la función del script, pero mejora mantenimiento y soporte. Se revisarán dependencias de rutas, binarios y variables del sistema operativo. Tras una actualización de sistema, un script puede fallar por cambios en rutas o permisos. La revisión preventiva evita que esos errores aparezcan en producción durante una operación urgente. El acceso bajo VPN se complementará con auditoría de aplicación. Se registrará quién ejecuta qué acción y sobre qué servicio. En herramientas internas, la trazabilidad es tan importante como el perímetro de red.


Fecha: 21/05/2026

Propuesta de mejora Incorporar un orquestador ligero de scripts, accesible solo bajo VPN, que permita lanzar operaciones aprobadas, consultar estado, revisar logs por servicio y repetir únicamente tareas fallidas.

- Script con modo simulación y ejecución real.
- Bloqueo de concurrencia para cambios en aulas.
- Lectura dinámica de instancias desde MaMood.
- Limpieza de cachés con resumen por instancia.
Tipo de script Riesgo principal Medida Aulas Virtuales Impacto masivo por instancia Lectura dinámica y validación errónea previa WordPress/centros Operación sobre centro Confirmación y logs por centro incorrecto Sistema Comando no validado Lista blanca y usuario de mínimos permisos

##### 1.3.1.1.33. APARTADO: MEJORAS Y MANTENIMIENTO DE EMLab (EML)
Requerimiento EducaMadrid Mantenimiento y mejora del aplicativo EMLaB, desarrollado en PHP. El contrato incluye la actualización a la última versión de PHP, la renovación de ciertos módulos, la implementación de mejoras de seguridad y la adaptación del sistema operativo y paquetes necesarios (EML1). Propuesta técnica de empresa_s EMLab se actualizará a la última versión estable de PHP y se revisarán sistema operativo, paquetes y dependencias necesarias. La intervención se centrará en mantener continuidad del servicio, renovar módulos funcionales y facilitar la preparación de la próxima convocatoria. Se tratará como una aplicación de gestión donde la claridad del flujo de inscripción y la fiabilidad de datos son prioritarias. La revisión inicial identificará páginas públicas, administración, preguntas frecuentes, formularios de inscripción, validaciones, correos, estados y datos históricos. Se comprobará qué elementos son configurables y cuáles están codificados. La evolución buscará que una nueva convocatoria pueda prepararse con cambios de configuración y contenido, no con modificaciones de código. El módulo de preguntas frecuentes se renovará para permitir edición sencilla, orden, categorización, publicación y despublicación. Las FAQ deben ser localizables y útiles para usuarios no técnicos. Se revisará la posibilidad de incorporar búsqueda básica, enlaces internos y mensajes claros cuando no haya resultados. También se validará accesibilidad en navegación y lectura. El bloque de inscripción se preparará para la próxima convocatoria con control de fechas, campos obligatorios, mensajes de validación, confirmación de envío y tratamiento de errores. El sistema debe impedir inscripciones fuera de plazo, duplicadas o incompletas. Los mensajes deben orientar al usuario sin revelar información técnica. La seguridad cubrirá sanitización de campos, validación de servidor, protección CSRF, control de sesiones, permisos de administración, límites de tamaño si hay adjuntos y exposición de errores.


Se revisará que los datos de inscripción no queden accesibles públicamente y que las exportaciones administrativas requieran permisos adecuados. La actualización a PHP actual se realizará con pruebas sobre formularios y datos históricos. Muchos errores de migración aparecen en campos opcionales, fechas, valores nulos o formatos antiguos. Por ello, se utilizarán datos de prueba representativos y se revisarán logs de advertencias antes de producción. La experiencia de usuario se cuidará reduciendo pasos innecesarios, agrupando campos relacionados y mostrando confirmaciones claras. En dispositivos móviles, los formularios deberán ser usables sin desplazamientos excesivos ni campos difíciles de completar. La accesibilidad se validará con etiquetas, foco, mensajes de error y contraste. Las pruebas incluirán apertura de convocatoria, cierre por fecha, inscripción correcta, inscripción duplicada, FAQ publicada, FAQ retirada, usuario sin permisos de administración y exportación. Un ejemplo será configurar una convocatoria futura en preproducción, simular el cambio de fecha y comprobar que el formulario se habilita y se cierra automáticamente. El módulo de inscripción deberá permitir parametrizar textos legales, instrucciones, fechas y correos de confirmación. La convocatoria siguiente no debería obligar a editar código para cambiar mensajes o plazos. Las FAQ se organizarán por categorías y podrán ordenarse manualmente. Las preguntas más frecuentes deben aparecer de forma visible. Cuando una FAQ se retire, no debe desaparecer sin control si estaba enlazada desde una comunicación; se podrá mostrar una redirección o aviso. La seguridad del formulario contemplará protección frente a envíos automatizados si el flujo está expuesto públicamente. Se aplicarán controles proporcionados para no dificultar el uso legítimo, pero evitando spam o sobrecarga. La explotación administrativa tendrá filtros y exportaciones controladas. Si se exportan inscripciones, el fichero deberá generarse solo para usuarios autorizados y no quedar expuesto en rutas temporales públicas.
##### 1.3.1.1.34. APARTADO: MEJORAS Y MANTENIMIENTO DE ABIESWEB (ABI)
Requerimiento EducaMadrid Mantenimiento y mejora del aplicativo AbiesWeb, incluyendo la actualización a la última versión liberada por el Ministerio de Educación y Formación Profesional. Este cambio puede requerir laactualización de paquetes del sistema operativo y PHP, así como modificaciones para aumentar la seguridad del sistema (ABI1). Propuesta técnica de empresa_s AbiesWeb se actualizará a la última versión liberada por el Ministerio de Educación y Formación Profesional, considerando posibles cambios en PHP, paquetes del sistema operativo, configuración y dependencias. La actuación comenzará con una instalación de referencia en preproducción, comparación con la versión actual y revisión del impacto sobre bibliotecas, usuarios, catálogos, préstamos e imagen institucional. La actualización se planificará como un proceso repetible. Se documentarán versión de origen, versión destino, requisitos, cambios de configuración, pasos de migración, comprobaciones y criterios de aceptación. Antes de actuar sobre producción se ensayará la actualización con una copia controlada y se validará que los datos principales permanecen íntegros.


La seguridad incluirá revisión frente a SQL injection, XSS, CSRF, fuerza bruta, sesiones, cabeceras HTTP, exposición de errores y permisos de administración. Se prestará atención a formularios de búsqueda, login, préstamos, administración de catálogos y cualquier campo que pueda mostrar contenido en páginas posteriores. Los mensajes de error no deberán revelar rutas ni trazas internas. La adaptación a imagen institucional se aplicará conforme a las directrices indicadas. Se actualizarán logotipos, textos, organismos responsables, colores y elementos visibles. La personalización se mantendrá de forma separada siempre que sea posible, para no dificultar futuras actualizaciones ministeriales. Si es necesario modificar plantillas, se documentará cada cambio. La compatibilidad funcional se probará en operaciones bibliotecarias esenciales: búsqueda en catálogo, consulta de ejemplares, autenticación, préstamos, devoluciones, reservas si existen, administración y generación de listados. La validación debe realizarse con datos representativos, no solo con una instalación vacía. El rendimiento se revisará en búsquedas y listados. En catálogos grandes, las consultas sin filtros o con ordenaciones no indexadas pueden degradar la experiencia. Se analizarán índices, tiempos de respuesta y paginación. Si la nueva versión introduce cambios en consultas, se medirá antes y después. La operación incluirá backup previo, procedimiento de restauración, ventana de despliegue y lista de comprobación postactualización. Se definirá qué pruebas mínimas deben superarse antes de dar por finalizada la intervención. Esto reducirá el riesgo de detectar incidencias funcionales cuando el servicio ya esté en uso por centros. Un ejemplo de validación será actualizar preproducción, buscar un título con caracteres acentuados, realizar un préstamo de prueba, devolverlo, revisar el histórico y comprobar que la imagen institucional se muestra correctamente. Después se repetirá la secuencia tras el despliegue en producción con datos controlados. La comparación entre versión actual y versión ministerial se documentará con una matriz de cambios. Esta matriz indicará cambios funcionales, cambios técnicos, personalizaciones afectadas y pruebas asociadas. Así se evita que la actualización se reduzca a sustituir ficheros sin entender impacto. La personalización institucional se mantendrá en una capa separada o en un conjunto documentado de plantillas. Si un futuro paquete del Ministerio actualiza el aplicativo, la personalización podrá reaplicarse con menor esfuerzo y menor riesgo. Se comprobará la gestión de caracteres y búsquedas en catálogo. En bibliotecas escolares pueden existir títulos, autores y editoriales con tildes, caracteres especiales o nombres compuestos. La actualización no debe degradar estas búsquedas. La lista de comprobación postactualización se dejará como entregable operativo. Incluirá pruebas mínimas, responsable de validación, resultado esperado y espacio para observaciones. Esto facilitará repetir actualizaciones futuras sin partir de cero.

3.1.6.2 Servicio de Mantenimiento 24/ 7 y CAU Dentro de las labores de desarrollo correctivo y gestión de incidencias, empresa_s no sólo garantizará la resolución técnica de los problemas detectados, sino que también llevará a cabo una actualización continua de la documentación funcional y técnica de la plataforma EducaMadrid.


Esta documentación, que podrá generarse tanto en formato textual como audiovisual, estará orientada a facilitar la correcta utilización de los servicios por parte de la comunidad educativa (docentes, alumnado y familias), así como a mejorar la capacidad de autoservicio del usuario a través del portal CAU. En este contexto, el servicio se prestará conforme a un modelo integral que combina:
- Un modelo de mantenimiento correctivo con soporte continuo 24x7 para incidencias
críticas, orientado a garantizar la disponibilidad ininterrumpida de los sistemas en entornos productivos.
- Un modelo CAU (Centro de Atención a Usuarios) que canaliza la atención a centros
educativos mediante mecanismos estructurados de soporte, trazabilidad y gestión de la demanda.
1. Gestión de incidencias y modelo de atención
La gestión de incidencias comprenderá el registro, clasificación, análisis, seguimiento y resolución de todas las incidencias detectadas en la plataforma, tanto las comunicadas por los usuarios como las identificadas por el propio servicio. Estas serán comunicadas al adjudicatario por el responsable del contrato, o persona designada, a través de los canales habilitados (correo electrónico, herramienta ITSM o portal CAU), incluyendo siempre:

- Fecha y hora de notificación.
- Sistema, módulo o componente afectado.
- Nivel de gravedad (Leve, Grave o Crítica).
- Descripción detallada de los efectos observados.
De acuerdo con el pliego, los usuarios finales no interactuarán directamente con el personal técnico asignado por empresa_s, sino que todas las comunicaciones se articularán a través del modelo CAU, asegurando así la correcta trazabilidad, priorización y control del servicio. El CAU actuará como punto único de contacto, atendiendo incidencias y consultas a través de diversos canales (teléfono, correo electrónico, portal CAU u otros medios electrónicos), proporcionando un servicio homogéneo y alineado con las necesidades de los centros educativos.

2. Modelo de soporte multinivel
El servicio se organizará en dos niveles claramente diferenciados:
- Nivel 1 (CAU / Helpdesk funcional): Atendido por técnicos de soporte con conocimiento
funcional de EducaMadrid, responsables de la resolución de incidencias de primer nivel, atención a consultas, asistencia a usuarios y canalización de incidencias.
- Nivel 2/3 (Soporte técnico especializado): Integrado por analistas programadores y
técnicos de sistemas, que abordarán incidencias de carácter técnico o aquellas que requieran intervención en código, arquitectura o infraestructuras. Este modelo garantiza una atención eficiente, escalable y especializada, optimizando los tiempos de resolución y asegurando la calidad del servicio.

3. Cobertura funcional y soporte a usuarios. Modelo CAU
El Centro de Atención a Usuarios (CAU) constituye el eje central del servicio de soporte de EducaMadrid, actuando como punto único de contacto (Single Point of Contact – SPOC) para la gestión de incidencias, consultas, solicitudes y comunicaciones con los usuarios finales (docentes, alumnado y familias). Página 155 de 192


Su diseño responde a un modelo estructurado, trazable y orientado a servicio, que garantiza la calidad, eficiencia y control en la atención a los centros educativos. Principios del modelo CAU El modelo CAU se basa en los siguientes principios fundamentales:
- Centralización de la atención: todos los usuarios acceden al soporte a través del CAU,
evitando contactos directos con los equipos técnicos.
- Trazabilidad completa: todas las incidencias y solicitudes se registran, monitorizan y
documentan en herramientas ITSM o en el portal CAU.
- Orientación al usuario: soporte adaptado a perfiles no técnicos del entorno educativo.
- Estandarización de procesos: clasificación, priorización, escalado y resolución conforme
a ANS definidos.
- Integración con mantenimiento: conexión directa con el modelo de resolución técnica
(nivel 2) y con el mantenimiento evolutivo/correctivo. Canales de acceso al CAU El CAU articula la atención a través de múltiples canales, permitiendo accesibilidad y flexibilidad:
- Portal CAU (principal canal estructurado).
- Correo electrónico.
- Teléfono.
- Otros medios electrónicos o plataformas corporativas.
El portal CAU es el canal prioritario, ya que permite:
- Registro automático de incidencias.
- Autoasignación y categorización.
- Seguimiento en tiempo real.
- Histórico de incidencias y consultas.
- Integración con el sistema de gestión ITSM.
Tipología de servicios del CAU El CAU no se limita a la gestión de incidencias, sino que cubre un conjunto amplio de servicios: Gestión de incidencias:
- Registro, clasificación y priorización.
- Diagnóstico inicial.
- Resolución en primer nivel o escalado.
- Seguimiento hasta cierre.
- Comunicación con el usuario.
Atención de consultas:
- Dudas funcionales sobre herramientas EducaMadrid.
- Uso de servicios (correo, Moodle, Liferay, Mediateca, etc.).
- Procedimientos administrativos o técnicos.
Gestión de solicitudes:
- Peticiones de configuración.
- Altas/bajas/modificaciones de usuarios.


- Solicitudes de creación de recursos (webs, cursos, etc.).
Soporte proactivo:
- Publicación de contenidos de ayuda.
- Respuestas en foros.
- Elaboración de guías, boletines y píldoras formativas.
Gestión operativa del CAU Registro y clasificación Toda solicitud será registrada con información estructurada:
- Fecha y hora.
- Sistema afectado.
- Nivel de criticidad.
- Descripción del problema.
Priorización Las incidencias se clasifican según:
- Leves (sin impacto crítico).
- Graves (impacto parcial).
- Críticas (interrupción total del servicio).
Asignación
- Asignación automática o manual a técnicos de nivel 1.
- Escalado a nivel 2 si es necesario.
Seguimiento y comunicación
- Comunicación continua con el usuario.
- Información del estado de la incidencia.
- Notificación de resolución.
Modelo multinivel de soporte El CAU se articula en dos niveles integrados: Nivel 1 (CAU / Helpdesk)
- Atención directa al usuario.
- Resolución de incidencias funcionales.
- Diagnóstico inicial.
- Registro y documentación.
- Escalado.
Nivel 2 (Especialistas técnicos)
- Resolución técnica avanzada.
- Intervención en código o sistemas.
- Análisis profundo de fallos.
Este modelo permite:
- Mayor eficiencia.


- Reducción de tiempos de resolución.
- Especialización del equipo.
Relación con el modelo 24/7 El CAU se integra con el modelo de mantenimiento de la siguiente forma:
- Horario ordinario (CAU): atención funcional y gestión general de incidencias.
- Soporte extendido: actuaciones fuera de horario laboral cuando sea necesario.
- Soporte 24/7 para incidencias críticas:
o Activación inmediata. o Resolución prioritaria. o Garantía de continuidad del servicio. El CAU actúa como puerta de entrada, mientras que el soporte 24/7 garantiza la intervención técnica continua. Áreas Funcionales Las áreas funcionales cubiertas por el CAU y el servicio de mantenimiento incluirán, entre otras:
- Configuración y uso de servicios de correo y calendarios.
- Uso del portal educativo (Liferay).
- Gestión de usuarios y procedimientos asociados.
- Creación y mantenimiento de webs de centros y profesorado.
- Acceso a recursos digitales y repositorios educativos.
- Gestión del Aula Virtual (Moodle).
- Gestión de la Mediateca.
- Soporte a sistemas de videoconferencia.
- Uso del resto de herramientas de la plataforma.

4. Modelo de mantenimiento 24/7
En línea con los requisitos del pliego, el servicio contemplará un modelo de operación que combine:

- Horario ordinario de atención (CAU): cobertura en horario laboral para atención a
usuarios, gestión de incidencias y soporte funcional.
- Soporte extendido y guardias: realización de tareas fuera del horario ordinario para
actuaciones planificadas o necesidades excepcionales.
- Soporte continuo 24/7 para incidencias críticas: garantizando la resolución de
incidentes que comprometan la disponibilidad total del servicio, con intervención fuera de horario y en días no laborables cuando sea necesario.

5. Acuerdos de nivel de servicio (ANS)
El servicio se regirá por ANS que aseguran la calidad y continuidad del servicio:

- Tiempo de respuesta: máximo de 2 horas en horario de servicio.
- Tiempo de resolución: en función de la criticidad (Leve, Grave o Crítica),
- Soporte prioritario a incidencias críticas en régimen 24/7
- Aplicación de pruebas de regresión para evitar efectos colaterales en otros sistemas .


En caso de incidencias que requieran desarrollos complejos, empresa_s elaborará un plan de actuación detallado, incluyendo medidas paliativas hasta la resolución definitiva. En conjunto, este modelo integrado de mantenimiento correctivo, soporte 24/7 y atención mediante CAU permitirá garantizar no solo la estabilidad técnica de la plataforma EducaMadrid, sino también una experiencia de usuario eficiente, estructurada y orientada a la comunidad educativa.

3.2 Planificación del servicio 3.2.1 Calendario de los trabajos a desarrollar

![Imagen de la página 160](<oferta_tecnica_desarrollo_empresa_s_assets/pagina-0160-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0160-imagen-003.png -->
- Leyenda general de un cronograma técnico, dividida en perfiles, responsables principales, niveles de participación, tipos de tarea y referencias de bloques.
- Los perfiles representados son dirección de proyecto, liderazgo técnico, sistemas, desarrollo, bases de datos, seguridad, diseño UX/UI, pruebas y operación o soporte; cada responsable dispone de una abreviatura entre corchetes.
- La participación se clasifica desde muy alta hasta muy baja mediante colores, y las tareas se distinguen como planificación, ejecución, mantenimiento continuo, finalización o hito.
- La referencia de bloques enumera abreviaturas de numerosos servicios, entre ellos aulas virtuales, mediateca, LDAP, correo web, WordPress, formularios, videoconferencia, nube, portal, Wekan y AbiesWeb.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0160-imagen-003.png -->

![Imagen de la página 160](<oferta_tecnica_desarrollo_empresa_s_assets/pagina-0160-imagen-004.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0160-imagen-004.png -->
- Primera parte de un cronograma de doce meses, desde septiembre de 2026 hasta agosto de 2027, con responsables, barras de actividad e hitos.
- Abarca mejoras transversales, aulas virtuales, evolución de la mediateca y consultas LDAP, detallando tareas como actualizaciones, integraciones, seguridad, soporte, inteligencia artificial y nuevas funciones.
- Los colores separan inicio o planificación, ejecución principal, mantenimiento continuo y cierre; los triángulos marcan hitos.
- A la derecha se fijan hitos de cierre en agosto de 2027 para tareas transversales, Moodle, mediateca y LDAP.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0160-imagen-004.png -->


![Imagen de la página 161](<oferta_tecnica_desarrollo_empresa_s_assets/pagina-0161-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0161-imagen-003.png -->
- Segunda parte de un cronograma de doce meses, entre septiembre de 2026 y agosto de 2027.
- Planifica mejoras del servicio eXeLearning Online, correo web, WordPress Multisite, formularios, Empieza, buscador de aulas y cursos y servicios de retransmisión y videoconferencia.
- Cada fila combina responsable principal, fase inicial, ejecución, mantenimiento continuo y cierre; los hitos de la derecha sitúan la puesta en operación u optimización en agosto de 2027.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0161-imagen-003.png -->

![Imagen de la página 161](<oferta_tecnica_desarrollo_empresa_s_assets/pagina-0161-imagen-004.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0161-imagen-004.png -->
- Tercera parte de un cronograma de doce meses, entre septiembre de 2026 y agosto de 2027.
- Incluye Animalandia, sincronización de usuarios, Portal CAU, EducaSaaC, cloud, buzón anónimo, DITIC, seguimientos, Albor, avisos, foros, boletines, ayuda, portal, web estática, framework de interfaz, entornos MAX, gestión de títulos, medidas de uso web, Wekan, MaMMod, EMLab y AbiesWeb.
- Las barras diferencian planificación, ejecución, mantenimiento continuo y cierre; varios triángulos señalan hitos de evolución de la nube, optimización de servicios corporativos e integración de Wekan en agosto de 2027.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_desarrollo_empresa_s_assets/pagina-0161-imagen-004.png -->

3.2.2 Análisis de riesgos del proyecto La propuesta de empresa_s articula un modelo avanzado de gestión de riesgos, integral, predictivo y orientado a servicio, específicamente diseñado para entornos tecnológicos de alta criticidad y gran escala como EducaMadrid. El modelo propuesto transforma la gestión de riesgos en un activo estratégico del servicio , garantizando no solo la mitigación de amenazas, sino la resiliencia, estabilidad y excelencia operativa de la plataforma EducaMadrid en escenarios de alta criticidad. Este modelo no se limita a un enfoque reactivo tradicional, sino que se basa en una capacidad anticipativa y de resiliencia operativa, orientada a:
- Garantizar la continuidad ininterrumpida del servicio en entornos 24x7.
- Minimizar la probabilidad de incidencias críticas.
- Reducir de forma significativa el impacto real y contractual (ANS) de los eventos adversos.
- Proteger los activos tecnológicos y la información conforme al Esquema Nacional de
Seguridad (ENS) nivel MEDIO.
- Asegurar la estabilidad operativa en picos de demanda propios del entorno educativo
(inicio de curso, evaluaciones, etc.) El enfoque adoptado responde a un principio clave:
- “El riesgo no se gestiona cuando ocurre, sino cuando se anticipa e integra en la operación
diaria.” Para ello, la gestión de riesgos se concibe como un proceso transversal plenamente integrado en:
- La operación técnica diaria.
- La gestión del servicio (Redmine) .
- La toma de decisiones estratégicas del contrato.
- Los mecanismos de control de ANS.
- Los procesos de seguridad y cumplimiento (ENS).

Marco metodológico y alineamiento normativo La metodología propuesta se basa en las mejores prácticas internacionales, adaptadas al contexto del pliego:
- Gestión de riesgos.
- Análisis de riesgos de seguridad.
- ITIL / ITSM (gestión de servicios TI).
- Cumplimiento del ENS (categoría MEDIA).
El modelo garantiza:
- Repetibilidad y auditabilidad.
- Trazabilidad completa del riesgo.
- Integración con indicadores de servicio (ANS).
- Evolución continua basada en datos reales.

Alcance del Plan de Gestión de Riesgos El Plan cubre de forma exhaustiva todos los elementos del ecosistema EducaMadrid, incorporando una visión end- to-end:


Fecha: 21/05/2026

Servicios críticos Se consideran de máxima prioridad:
- Portal Educativo (Liferay).
- Aulas Virtuales (Moodle).
- Plataforma de correo (≈2 millones de usuarios).
- Cloud corporativo (Nextcloud).
- Sistemas de identidad (LDAP / SSO).
- MAX Linux.
- Plataformas de Inteligencia Artificial y analítica.

Infraestructura tecnológica
- Aproximadamente 700 servidores.
- Más de 3.500 bases de datos.
- Sistemas de almacenamiento, virtualización y red.

Procesos críticos
- Mantenimiento evolutivo y correctivo.
- Despliegues continuos.
- Migraciones entre CPDs.
- Operación bajo ANS.
- Gestión de seguridad y auditorías ENS.

Modelo de gobierno del riesgo Se define un modelo organizativo robusto, orientado a la responsabilidad efectiva y toma de decisiones ágil.

Roles y responsabilidades Rol Responsabilidad Jefe de Proyecto (empresa_s) Liderazgo estratégico y operativo del riesgo Responsable del contrato (EducaMadrid) Validación, priorización y supervisión Responsable de Seguridad Gestión de riesgos ENS y ciberseguridad Equipo técnico Identificación, análisis y mitigación Propietario del riesgo Ejecución directa de medidas

Todos los riesgos críticos tendrán propietario nominal, con responsabilidad directa sobre su mitigación y seguimiento.

Modelo de gobernanza
- Comité mensual de riesgos (nivel estratégico).
- Comité técnico semanal (nivel operativo).
- Comités extraordinarios (activación inmediata ante incidencias críticas).
Este modelo garantiza:


- Visión continua del estado del riesgo.
- Toma de decisiones informada.
- Capacidad de reacción inmediata.

Metodología de gestión de riesgos La gestión se estructura en un ciclo continuo de seis fases:

1. Planificación: Definición de contexto, criterios de evaluación y políticas de riesgo.
2. Identificación: Detección continua basada en múltiples fuentes (operativas, históricas y
predictivas).
3. Análisis cualitativo: Priorización mediante matrices estructuradas.
4. Análisis cuantitativo: Aplicado a riesgos críticos para estimar impacto real.
5. Planificación de respuesta: Definición de estrategias y planes de contingencia.
6. Seguimiento y control: Monitorización continua y mejora iterativa.

Identificación avanzada de riesgos El modelo se basa en una identificación continua, distribuida y basada en datos, apoyada en:
- Históricos de Redmine.
- Métricas de servicio.
- Incidencias ANS.
- Auditorías ENS.
- Experiencia operativa en entornos similares.

Categorías de riesgo
- Operacionales.
- Tecnológicos.
- Seguridad / ENS.
- Datos.
- Recursos humanos.
- Cumplimiento normativo.
- Dependencias externas.

Catálogo inicial de riesgos Se incorpora un catálogo alineado con el contexto real del servicio: Los riesgos críticos incluyen:
- Caídas de servicios clave.
- Fallos de autenticación.
- Brechas de seguridad.
- Corrupción de datos.
- Incumplimiento ANS.


El catálogo no es estático, sino un registro vivo y evolutivo, alimentado continuamente.

Análisis de riesgos

Análisis cualitativo Se emplea una matriz Probabilidad × Impacto (5x5) con evaluación multidimensional:
- Impacto en servicio.
- Impacto en usuarios.
- Impacto en seguridad.
- Impacto contractual (ANS).
- Impacto reputacional.
Se incorporan factores adicionales:
- Detectabilidad.
- Urgencia.
- Relevancia ENS.
- Riesgo reputacional.
Clasificación: � Crítico → actuación inmediata � Alto → mitigación planificada � Medio → control activo � Bajo → monitorización

Análisis cuantitativo Se aplica a riesgos de mayor criticidad mediante:
- Simulación de escenarios.
- Análisis de disponibilidad vs SLA.
- Modelos predictivos de carga.
- Árboles de decisión.
Permite cuantificar:
- Impacto económico.
- Impacto en ANS.
- Tiempo estimado de recuperación (RTO/RPO).

Estrategia de respuesta a riesgos Se aplican las cuatro estrategias estándar:
- Evitar.
- Mitigar.
- Transferir.
- Aceptar.

Planes de mitigación avanzados


Cada riesgo crítico dispone de planes estructurados que incluyen:
- Arquitecturas de alta disponibilidad.
- Replicación y backup avanzado.
- Procedimientos de rollback automatizados.
- Entornos de contingencia.
- Escalado N2/N3.
- Protocolos de comunicación institucional.
Los planes no son teóricos: están integrados en la operación real y probados mediante simulaciones.

Seguimiento y control continuo El modelo incorpora una monitorización proactiva del riesgo en tiempo real, basada en:
- Herramientas de monitorización.
- Logs centralizados.
- Observabilidad de sistemas.

KPIs de riesgo
- Nº de incidencias críticas.
- MTTR (tiempo medio de resolución).
- % cumplimiento ANS.
- Vulnerabilidades abiertas.
- Disponibilidad por servicio.

Revisión continua
- Evaluación mensual formal.
- Reevaluación tras incidentes críticos.
- Auditorías ENS periódicas.

Integración con ENS El plan está totalmente alineado con el ENS nivel MEDIO, incorporando:
- Principio de mínimo privilegio.
- Seguridad desde el diseño.
- Defensa en profundidad.
Incluye:
- Gestión de vulnerabilidades.
- Auditorías periódicas.
- Monitorización de intrusiones.
- Gestión de identidades y accesos.

Integración con ANS La gestión de riesgos es la base del cumplimiento de ANS:


Fecha: 21/05/2026

- Identificación → origen de SLA .
- Mitigación → procedimientos operativos .
- Seguimiento → control contractual .

Compromisos
- Respuesta ≤ 2h.
- Resolución:
o Crítico ≤ 6h. o Grave ≤ 12h. o Leve ≤ 24h.

Herramientas de soporte
- Redmine (gestión y trazabilidad de riesgos).
- CMDB (impacto sobre activos).
- Monitorización avanzada.
- Sistemas de ticketing.

Entregables
- Registro vivo de riesgos.
- Informes mensuales ejecutivos.
- Informes post-incidente.
- Cuadro de mando de riesgos.
- Actualización continua del plan.

Valor diferencial La propuesta de empresa_s aporta un enfoque claramente superior en:

1. Anticipación del riesgo: Modelo predictivo basado en datos y monitorización continua.
2. Integración real en operación: El riesgo no es documental, sino operativo.
3. Alineación total con ENS y ANS: Punto crítico de valoración en el pliego.
4. Responsabilidad clara (ownership): Cada riesgo crítico tiene un responsable designado.
5. Madurez metodológica: Uso combinado de análisis cualitativo + cuantitativo.
6. Orientación a continuidad educativa: Especialmente adaptado a picos de demanda del
entorno docente.

Escala de valoración

Probabilidad

Nivel Descripción

Muy baja Evento excepcional


Fecha: 21/05/2026

Baja Evento poco probable

Media Evento ocasional

Alta Evento frecuente

Muy alta Evento recurrente

Impacto

Nivel Ejemplo en EducaMadrid

Muy alto Caída total del portal o correo

Alto Degradación grave de aulas virtuales

Medio Incidencias parciales

Bajo Impacto limitado

Muy bajo Sin impacto relevante

Ejemplo aplicado

Caso 1: Caída del Portal Educativo:
- Probabilidad: Media.
- Impacto: Muy alto.
Clasificación: � Riesgo Crítico Interpretación:
- Afecta a toda la comunidad educativa.
- Impacto directo en ANS.
- Alta visibilidad institucional.
Acción:
- Arquitectura HA activa-activa.
- Balanceo inteligente.
- Monitorización en tiempo real.

Caso 2: Saturación de infraestructura en picos
- Probabilidad: Alta (inicio de curso).
- Impacto: Alto.
Clasificación: � Riesgo Crítico


Acción:
- Autoescalado.
- Capacity planning predictivo.
- Pruebas de carga periódicas.

Caso 3: Pérdida de personal clave
- Probabilidad: Media.
- Impacto: Medio.
Clasificación: � Riesgo Medio Acción:
- Plan de continuidad de equipo.
- Documentación intensiva.
- Backups de conocimiento (shadowing).

Capa adicional: Factores de corrección Además de la matriz clásica, empresa_s introduce un ajuste avanzado del riesgo, considerando:
- Detectabilidad (¿se detecta antes de impactar?).
- Tiempo de reacción disponible.
- Dependencia externa.
- Impacto en ENS.
- Efecto cascada en otros sistemas.
Esto permite refinar la prioridad real, evitando infravalorar riesgos complejos. La utilización de matrices visuales, modelos cuantitativos y cuadros de mando permite transformar la gestión de riesgos en un proceso objetivo, medible y orientado a la toma de decisiones, reduciendo significativamente la incertidumbre operativa en un entorno de alta criticidad como EducaMadrid. 3.2.3 Plan de gestión de contingencias El presente Plan de Gestión de Contingencias se establece como un instrumento estratégico y operativo cuyo propósito es garantizar de forma integral la continuidad, disponibilidad, integridad y seguridad de todos los sistemas que conforman la plataforma EducaMadrid ante cualquier evento adverso, ya sea de origen técnico, organizativo, funcional o de ciberseguridad. Este Plan no se limita a la reacción ante contingencias, sino que establece un modelo integral basado en:
- Prevención inteligente.

- Respuesta rápida y automatizada.

- Recuperación garantizada.

- Mejora continua.

Asegurando así que la plataforma EducaMadrid mantenga en todo momento los más altos niveles de calidad, seguridad y disponibilidad exigidos en el pliego.


Dada la criticidad de la plataforma que presta servicio a millones de usuarios de la comunidad educativa y soporta procesos clave de enseñanza, comunicación y gestión este plan se diseña bajo un enfoque de resiliencia operativa avanzada, orientado no sólo a la recuperación, sino a la anticipación, mitigación y adaptación dinámica frente a situaciones de riesgo. En este sentido, el plan persigue:
- Minimizar el impacto de cualquier interrupción en los servicios.

- Garantizar el cumplimiento estricto de los ANS y requisitos del ENS.

- Reducir los tiempos de recuperación (RTO) y pérdida de datos (RPO).

- Asegurar una respuesta coordinada, rápida y eficaz ante incidentes.

Asimismo, este plan se encuentra completamente alineado con:
- El modelo de prestación del servicio (TIPO A, B y C).

- Los requerimientos de continuidad del servicio en entornos productivos.

- La necesidad de soporte 24/7 y gestión de incidencias bajo SLA definidos.

Cobertura del Plan El plan se articula en torno a cuatro grandes ejes de actuación que cubren de manera transversal toda la operación del servicio:

##### 1.3.1.1.35. Mantenimiento correctivo, evolutivo y adaptativo

Este eje contempla la gestión integral del ciclo de vida de los sistemas, asegurando su estabilidad, evolución tecnológica y adaptación continua a necesidades funcionales y cambios del entorno. Alcance ampliado Mantenimiento correctivo:
- Identificación y resolución de defectos en producción.

- Corrección de errores en código, configuraciones y despliegues.

- Restauración del servicio ante fallos funcionales o técnicos.
Mantenimiento evolutivo:
- Incorporación de nuevas funcionalidades.

- Mejoras de rendimiento y escalabilidad.

- Optimización de la experiencia de usuario.
Mantenimiento adaptativo:
- Adecuación a cambios tecnológicos (versionado, upgrades).

- Adaptación a nuevas normativas (ENS, protección de datos).

- Integración con nuevos sistemas o servicios.

Enfoque de contingencia Página 170 de 192


Diseño de entornos de preproducción y pruebas para evitar impactos en producción.
- Uso de estrategias de despliegue seguro (blue/green, rolling updates).

- Definición de procedimientos rollback automáticos.

- Validación mediante pruebas funcionales, de rendimiento y seguridad antes de producción.

Este enfoque reduce el riesgo de introducción de fallos y garantiza la continuidad del servicio durante cualquier cambio.

##### 1.3.1.1.36. Gestión de incidencias bajo ANS (Acuerdos de Nivel de Servicio)

Este eje establece un modelo robusto y estructurado de gestión de incidencias alineado con los ANS definidos en el pliego, garantizando una respuesta rápida, controlada y medible. Capacidades clave:
- Disponibilidad de soporte 24x7 para incidencias críticas.

- Clasificación automática y manual de incidencias (leve, grave, crítica).

- Registro completo en herramientas de ticketing (Redmine/ITSM).

- Monitorización proactiva para detección temprana.

Proceso ampliado:
- Detección automática o reporte.

- Registro y categorización.

- Asignación al equipo especializado.

- Resolución dentro de SLA.

- Validación del servicio.

- Cierre documentado.

Garantía de cumplimiento ANS:
- Tiempo de respuesta ≤ 2 horas.

- Tiempos de resolución adaptados a criticidad (hasta 6 h en críticos).

Medidas avanzadas:
- Cuadro de mando de SLA en tiempo real.

- Análisis de causa raíz (RCA) sistemático.

- Automatización de resolución de incidencias recurrentes.

- Generación de knowledge base reutilizable .
Este enfoque no sólo asegura cumplimiento contractual, sino mejora continua del servicio.
3. Continuidad operativa de sistemas críticos


Este eje se centra en mantener la operatividad de los sistemas esenciales incluso en situaciones adversas, garantizando que los servicios educativos no se vean interrumpidos. Estrategia de continuidad
- Arquitectura basada en:

o Alta disponibilidad (HA). o Redundancia de componentes.

o Escalabilidad horizontal y vertical.

- Sistemas priorizados:

o Portal educativo.

o Aulas virtuales. o Cloud educativo.

o Correo electrónico.

o LDAP/SSO.

- Medidas implementadas:

o Balanceadores de carga. o Clustering de servicios críticos.

o Replicación de bases de datos.

o Redistribución dinámica de cargas.

- Optimización para entorno educativo:

o Planificación de tareas críticas fuera de periodos lectivos. o Adaptación a picos de demanda (inicio de curso, evaluaciones).

o Monitorización específica de servicios masivos (Moodle, correo, cloud). Beneficio clave: La continuidad no depende de un único sistema, sino de un ecosistema resiliente distribuido, reduciendo significativamente el riesgo de interrupciones globales.
4. Recuperación ante desastres técnicos, funcionales y de seguridad
Este eje define los mecanismos de recuperación estructurada frente a escenarios de alto impacto, garantizando la restauración completa del servicio en el menor tiempo posible.
- Tipos de desastre contemplados:

o Fallos de infraestructura (CPD, almacenamiento, red).

o Corrupción de datos. o Fallos masivos en sistemas.

o Ciberataques (DDoS, intrusión, ransomware).


o Errores humanos críticos.

- Plan de recuperación:
o Definición de:

- RTO (Recovery Time Objective)

- RPO (Recovery Point Objective)

- Procedimientos:
o Restauración desde backups.

o Activación de sistemas redundantes. o Failover automático o manual.

o Validación post-recuperación.

- Capacidades avanzadas:
o Backups:

- Incrementales diarios.

- Completos semanales.

o Almacenamiento seguro y aislado. o Entornos de recuperación alternativos (CPD backup).

- Seguridad integrada:
o Cumplimiento del ENS (nivel MEDIO):

- Mínimo privilegio.

- Desarrollo seguro.

- Seguridad desde el diseño.

- Validación tras recuperación:

o Pruebas funcionales completas. o Verificación de integridad de datos.

o Confirmación de disponibilidad del servicio. Catálogo de riesgos y su integración con contingencias A continuación se presenta el núcleo del modelo integrado:

Riesgo 1: Caída de sistemas críticos (Portal, Moodle, Cloud)
- Impacto: Muy alto.

- Probabilidad: Media.


Medidas preventivas:

- Arquitectura HA con balanceo y replicación.

- Monitorización continua.

- Pruebas de carga periódicas.

Plan de contingencia:

- Activación de failover automático.

- Redistribución de carga.

- Escalado de recursos.

Riesgo 2: Saturación por picos de usuarios
- Impacto: Alto.

- Probabilidad: Alta (inicio de curso, exámenes).
Prevención:

- Dimensionamiento dinámico.

- Test de estrés programados.

Contingencia:

- Escalado horizontal inmediato.

- Limitación de recursos no críticos.

- Priorización de servicios clave.

Riesgo 3: Fallos en bases de datos
- Impacto: Muy alto.

- Probabilidad: Media.

Prevención:

- Replica de BBDD.

- Optimización continua.

Contingencia:

- Restauración desde backup.

- Activación de nodo secundario.

Riesgo 4: Ciberataques
- Impacto: Crítico

- Probabilidad: Media


Prevención:

- IDS/IPS.

- Auditorías de seguridad.

- Gestión de vulnerabilidades.

Contingencia:

- Aislamiento del sistema afectado.

- Activación de protocolos de seguridad.

- Recuperación controlada.

Riesgo 5: Errores en despliegues (mantenimiento evolutivo)
- Impacto: Alto.

- Probabilidad: Media.
Prevención:

- Entornos preproductivos.

- Validación QA completa.

Contingencia:

- Rollback automático.

- Restauración a versión estable.
Riesgo 6: Fallo en migraciones CPD

- Impacto: Muy alto.

- Probabilidad: Baja- media.
Prevención:

- Planificación detallada.

- Validación previa.

Contingencia:

- Plan rollback completo.

- Restauración en origen.
Riesgo 7: Fallos en sistemas de autenticación (LDAP/SSO)
- Impacto: Crítico.

- Probabilidad: Media.


Fecha: 21/05/2026

Prevención:

- Replicación LDAP.

- Monitorización.

Contingencia:

- Activación de nodo secundario.

- Caché de autenticación temporal.
Riesgo 8: Problemas en IA (modelos o privacidad)
- Impacto: Medio- alto.

- Probabilidad: Media.

Prevención:

- Evaluación continua de modelos.

- Control de datos (on-premise).

Contingencia:

- Desactivación del servicio IA.

- Fallback a procesos tradicionales.

Integración operativa riesgos ↔ contingencias El modelo se materializa mediante la siguiente correspondencia: Gestión de riesgos Gestión de contingencias Identificación Protocolos definidos Evaluación Prioridad de actuación Prevención Medidas arquitectónicas Riesgo materializado Activación contingencia Seguimiento Mejora continua

La integración entre el Plan de Riesgos y el Plan de Contingencias permite:
- Anticipar problemas antes de que ocurran.

- Reducir drásticamente el impacto de incidentes.

- Garantizar la continuidad de servicios críticos.
- Cumplir estrictamente ANS y ENS.
En definitiva, se establece un modelo que no solo gestiona incidencias, sino que controla el riesgo estructural del servicio, posicionando la operación de EducaMadrid en un nivel de madurez y excelencia operativa superior. Monitorización y detección temprana Página 176 de 192


Elemento clave de integración:

- Monitorización técnica (infraestructura).

- Monitorización funcional (servicio).
- Monitorización de seguridad (logs, IDS).
Permite detectar riesgos antes de que se conviertan en incidencias. Gobierno y roles
- Jefe de Proyecto: supervisión global.

- Arquitecto Software: gestión de riesgos técnicos.

- Equipo desarrollo: contingencias operativas.
- Ciberseguridad: riesgos de seguridad.

- Data/IA: riesgos analíticos.
Mejora continua El modelo se retroalimenta mediante:

- Análisis post-incidencia (RCA).
- Actualización del mapa de riesgos.

- Mejora de procedimientos de contingencia.

- Evolución del sistema de monitorización.
3.2.4 Plan de gestión de la calidad del servicio empresa_s apuesta firmemente por ofrecer servicios de alto valor añadido, enfocados tanto a la innovación como al desarrollo tecnológico. En este contexto, la Dirección mantiene un compromiso sólido con la calidad del servicio, promoviendo la mejora continua del sistema integrado de gestión y garantizando el cumplimiento de todos los requisitos aplicables, así como de aquellos adicionales que la organización adopte. La gestión de la calidad en empresa_s se fundamenta en varios principios clave:
- Orientación al cliente: se analizan de forma constante sus necesidades actuales y futuras,
se comunican internamente y se establecen objetivos vinculados a ellas, evaluando además su nivel de satisfacción.
- Liderazgo: se define una visión estratégica que integra los intereses de las partes
implicadas, estableciendo una política de gestión y objetivos claros. Asimismo, se proporcionan recursos adecuados y se fomenta un entorno que impulse el compromiso del equipo.
- Implicación del personal: se promueve que cada empleado comprenda la relevancia de su
aportación, asuma responsabilidades, participe en la resolución de problemas y continúe desarrollando sus competencias.
- Gestión por procesos: se estructuran las actividades de forma sistemática, definiendo sus
interrelaciones, responsabilidades y métricas, tal como se recoge en los procedimientos del sistema de gestión.
- Enfoque sistémico de la gestión: se coordinan los procesos siguiendo el mapa de procesos
establecido, evaluando el desempeño global y potenciando la mejora mediante el seguimiento continuo.


- Mejora continua: se impulsa mediante formación, establecimiento de objetivos específicos
y reconocimiento de los avances logrados.
- Toma de decisiones basada en datos: se garantiza la calidad y disponibilidad de la
información, utilizando su análisis para orientar las decisiones.
- Relación con proveedores: se establecen vínculos equilibrados y transparentes,
seleccionando proveedores clave y fomentando la colaboración para la mejora conjunta. El modelo de gestión se basa en tres pilares principales: procesos, servicios y personas. Pensamiento basado en riesgos empresa_s considera fundamental la integración del enfoque basado en riesgos como elemento clave para garantizar la eficacia, solidez y capacidad de adaptación del Sistema de Gestión de la Calidad. Este enfoque permite anticipar posibles desviaciones antes de que se materialicen, así como identificar oportunidades de mejora que aporten un valor añadido al servicio. En este sentido, la organización adopta una visión proactiva de la gestión, basada en la identificación sistemática de riesgos e incertidumbres asociados a los procesos, actividades y entregables. Esto implica no solo reaccionar ante incidencias una vez producidas, sino también establecer medidas preventivas orientadas a minimizar su probabilidad de ocurrencia o mitigar su impacto. Durante todo el ciclo de vida del servicio, se aplicará un procedimiento estructurado para la gestión de riesgos y oportunidades, que incluye las siguientes actividades: identificación, análisis, evaluación, planificación de respuestas, seguimiento y revisión continua. Este proceso permitirá priorizar los riesgos en función de su criticidad, asignar responsables y definir acciones concretas para su tratamiento. Asimismo, se contemplará la gestión de oportunidades como parte integral del sistema, promoviendo la identificación de mejoras potenciales en los procesos, la optimización de recursos y la innovación en la prestación del servicio. En este contexto, cada oportunidad será evaluada considerando también los riesgos asociados a su implementación, asegurando una toma de decisiones equilibrada y fundamentada. Para reforzar la eficacia de este enfoque, se utilizarán herramientas de apoyo como matrices de riesgos, análisis cualitativos y cuantitativos, indicadores de seguimiento y mecanismos de control integrados en los procesos operativos. Todo ello permitirá disponer de información fiable y actualizada para la toma de decisiones. Este enfoque basado en riesgos se encuentra plenamente integrado en el ciclo PHVA y en la gestión por procesos, lo que garantiza su aplicación transversal en todas las fases del proyecto. De este modo, se contribuye a mejorar el rendimiento global del sistema, incrementar la calidad de los resultados y reforzar la capacidad de la organización para adaptarse a entornos cambiantes. En definitiva, la adopción de este enfoque no solo permite prevenir incidencias y asegurar el cumplimiento de los requisitos, sino que también impulsa una cultura organizativa orientada a la anticipación, la mejora continua y la excelencia en la prestación del servicio. Enfoque por procesos y mejora continua La organización adopta un enfoque de gestión basado en procesos como pilar fundamental de su sistema de calidad, estructurando todas sus actividades mediante procesos claramente definidos, documentados y gestionados de forma interrelacionada. Este modelo permite garantizar la coherencia, eficiencia y trazabilidad de todas las actuaciones, asegurando su alineación tanto con la política de calidad como con la estrategia global de la organización. Cada proceso se concibe como un conjunto de actividades interconectadas que transforman entradas en resultados, con responsabilidades, recursos y criterios de control previamente


establecidos. Esta visión facilita una gestión integral que va más allá de áreas funcionales aisladas, promoviendo la coordinación entre equipos, la optimización de recursos y la eliminación de ineficiencias. Asimismo, se definen indicadores específicos para cada proceso, lo que permite evaluar su desempeño de manera objetiva y continua. El enfoque por procesos se complementa con una gestión activa de sus interrelaciones, garantizando que las salidas de un proceso constituyan entradas adecuadas para los siguientes. Esto contribuye a asegurar la calidad global del servicio, minimizando errores derivados de descoordinaciones o falta de alineamiento entre actividades. Sobre esta base, se integra de forma transversal el principio de mejora continua , entendido como un proceso sistemático y permanente orientado a incrementar la eficacia y eficiencia del sistema de gestión. Para ello, se establecen mecanismos de seguimiento, revisión y retroalimentación que permiten identificar oportunidades de mejora, implementar acciones correctivas y preventivas, y consolidar las lecciones aprendidas. Este modelo se sustenta en la aplicación rigurosa del ciclo PHVA (Planificar, Hacer, Verificar y Actuar), que proporciona una metodología estructurada para la gestión y optimización de los procesos. A través de este ciclo, la organización planifica sus actuaciones, ejecuta las actividades definidas, evalúa los resultados obtenidos y adopta medidas de mejora que se integran nuevamente en el sistema, generando un proceso continuo de evolución y aprendizaje. Adicionalmente, el enfoque incorpora de manera explícita una visión basada en riesgos y oportunidades, lo que permite anticipar posibles desviaciones antes de que se materialicen, así como identificar aquellas áreas donde se puede generar un mayor valor. Este análisis se integra en todas las fases del proceso, desde la planificación hasta la evaluación, reforzando la capacidad de anticipación y la resiliencia del sistema. En conjunto, este enfoque por procesos, apoyado en el ciclo PHVA y en la gestión de riesgos, permite disponer de un sistema de calidad robusto, dinámico y orientado a resultados, que no solo garantiza el cumplimiento de los requisitos, sino que impulsa de manera constante la mejora continua, la innovación y la excelencia en la prestación del servicio. Ciclo PHVA El ciclo PHVA constituye el eje fundamental sobre el que se articula el sistema de gestión de la calidad de empresa_s , permitiendo asegurar un enfoque sistemático, estructurado y orientado a la mejora continua en la ejecución de los servicios. Su aplicación garantiza no solo el cumplimiento de los requisitos establecidos, sino también la capacidad de adaptación y optimización constante del desempeño del proyecto. Este modelo se aplica de manera transversal a todos los procesos y actividades del servicio, integrando el enfoque basado en riesgos y la orientación a resultados, lo que permite anticipar desviaciones, maximizar oportunidades y reforzar la eficiencia operativa. El ciclo se desarrolla a través de las siguientes fases:
- Planificar (Plan): En esta fase se establecen las bases del sistema de calidad, definiendo
los objetivos específicos del proyecto, alineados con las necesidades del cliente y la estrategia de la organización. Se identifican y asignan los recursos necesarios (humanos, técnicos y organizativos), así como los indicadores clave de rendimiento (KPIs) que permitirán evaluar el grado de cumplimiento. Asimismo, se realiza un análisis exhaustivo de riesgos y oportunidades, diseñando planes de acción orientados a prevenir posibles incidencias y a potenciar aquellos factores que puedan generar valor añadido. También se definen los procedimientos, metodologías y controles que regirán la ejecución del servicio, garantizando una planificación robusta, coherente y orientada a resultados.


- Hacer (Do): Esta fase corresponde a la implementación de lo planificado, asegurando que
todos los procesos se ejecutan conforme a los procedimientos definidos y a los estándares de calidad establecidos. Durante esta etapa, se coordina el trabajo de los equipos, se gestionan los recursos asignados y se aplican las herramientas y metodologías previstas. Se garantiza, además, la adecuada comunicación entre los distintos actores implicados, así como la correct a gestión de la información y la documentación generada. Todo ello se realiza bajo un enfoque de control continuo que permite mantener la alineación con los objetivos definidos.
- Verificar (Check): En esta fase se lleva a cabo el seguimiento y evaluación del desempeño
del proyecto mediante la medición sistemática de los indicadores definidos. Se analizan los resultados obtenidos, comparándolos con los objetivos establecidos, con el fin de detectar posibles desviaciones, no conformidades o áreas de mejora. Este proceso de verificación se apoya en herramientas de control, auditorías internas, revisiones periódicas y análisis de datos, lo que permite disponer de una visión objetiva y actualizada del estado del servicio. Asimismo, facilita la identificación de tendencias y la evaluación de la eficacia de las acciones implementadas.
- Actuar (Act): En función de los resultados obtenidos en la fase de verificación, se definen
e implementan las acciones necesarias para corregir desviaciones, prevenir su recurrencia y mejorar el desempeño global del sistema. Estas acciones pueden incluir ajustes en los procesos, optimización de recursos, revisión de metodologías o actualización de los objetivos establecidos. Además, las lecciones aprendidas y las mejoras identificadas se integran en el sistema de gestión, garantizando su aplicación en futuros proyectos y consolidando así un proceso de aprendizaje organizativo continuo. En conjunto, la aplicación rigurosa del ciclo PHVA permite establecer un modelo de gestión dinámico, orientado a la excelencia y basado en la mejora continua, asegurando la calidad del servicio, la satisfacción del cliente y la optimización permanente de los resultados. Auditorías empresa_s dispone de un proceso estructurado de auditoría interna alineado con los requisitos de la norma ISO 9001, cuyo objetivo es garantizar el cumplimiento de los estándares de calidad definidos, así como verificar la eficacia del sistema de gestión a lo largo de todo el ciclo de vida del proyecto. Este proceso se configura como una herramienta clave para la mejora continua, la detección de desviaciones y el aseguramiento del servicio prestado. Para cada proyecto, se designan de forma expresa dos figuras fundamentales: un auditor interno, responsable de la planificación, ejecución y seguimiento de las auditorías, y un responsable de calidad del proyecto, encargado de coordinar las acciones necesarias y asegurar la correcta implementación de las mejoras derivadas de las auditorías. Esta separación de funciones garantiza la objetividad, independencia y rigor del proceso. El modelo de auditoría contempla tres tipologías principales, diseñadas para cubrir todas las fases del servicio:
- Auditoría inicial (o de arranque): Se realiza en las etapas iniciales del proyecto con el
objetivo de validar la correcta puesta en marcha del servicio. Permite analizar la adecuación de los procesos definidos, la correcta interpretación de los requisitos de calidad y la disponibilidad de los recursos necesarios. Asimismo, facilita la identificación temprana de posibles áreas de mejora o riesgos que puedan afectar al desarrollo del proyecto.
- Auditorías periódicas de seguimiento: Se llevan a cabo con una frecuencia establecida
(cada cuatro meses) y tienen como finalidad evaluar de forma continua el grado de cumplimiento de los procedimientos, estándares y objetivos de calidad. Estas auditorías permiten detectar posibles desviaciones, no conformidades o ineficiencias, así como verificar la correcta implementación de las acciones correctoras previamente definidas. Página 180 de 192


Constituyen, además, un mecanismo clave para asegurar la estabilidad y control del servicio.
- Auditoría final: Se realiza en la fase de cierre del proyecto y está orientada a verificar que
todos los entregables cumplen con los requisitos establecidos, tanto desde el punto de vista técnico como de calidad. Asimismo, evalúa el grado de cumplimiento de los objetivos del proyecto y confirma que la prestación del servicio se ha realizado conforme a los estándares definidos. Durante las auditorías, se analizan de forma exhaustiva diferentes ámbitos clave para la calidad del proyecto, entre los que destacan:

- Gestión de la configuración, verificando que los elementos del proyecto están
correctamente identificados, controlados y versionados.
- Gestión documental, asegurando la correcta elaboración, revisión, almacenamiento y
trazabilidad de la documentación generada.
- Calidad del software o de los entregables, evaluando su adecuación a los requisitos
funcionales y técnicos, así como a los estándares de calidad establecidos.

- Gestión de riesgos, comprobando la correcta identificación, evaluación y tratamiento de
los mismos a lo largo del proyecto.

- Gestión de incidencias y no conformidades, verificando su adecuado registro,
tratamiento y resolución.
- Procesos de validación y verificación, asegurando que los productos entregados han
sido sometidos a los controles necesarios antes de su aceptación.

- Cumplimiento metodológico, garantizando que las actividades del proyecto se
desarrollan conforme al marco metodológico definido. Adicionalmente, los resultados de las auditorías se documentan en informes detallados que incluyen hallazgos, evidencias, posibles no conformidades y recomendaciones de mejora. Estos informes sirven como base para la definición de planes de acción específicos, cuyo seguimiento se realiza de manera sistemática hasta su completa resolución. En conjunto, este enfoque de auditoría no solo asegura el cumplimiento normativo y contractual, sino que también aporta valor añadido al proyecto, al favorecer la transparencia, reforzar la confianza del cliente y promover una cultura de mejora continua orientada a la excelencia. Gestión de no conformidades La gestión de no conformidades constituye un pilar esencial del sistema de control de calidad, orientado a asegurar la detección temprana de desviaciones, su adecuada resolución y la prevención de su recurrencia. Este proceso se basa en un enfoque sistemático, proactivo y alineado con los principios de mejora continua, garantizando la calidad del servicio a lo largo de todo su ciclo de vida. Para ello, se establecen sesiones periódicas de revisión y seguimiento en las que participan las distintas partes implicadas en el proyecto, incluyendo responsables técnicos, de calidad y representantes del cliente. Estas sesiones permiten evaluar de forma conjunta el estado del servicio, identificar incidencias de manera temprana y priorizar su tratamiento en función de su impacto y criticidad. Asimismo, se contempla la posibilidad de convocar sesiones extraordinarias ante la detección de no conformidades de carácter crítico, asegurando una respuesta ágil y eficaz. El proceso de gestión de no conformidades se articula en las siguientes fases:
- Identificación: Se lleva a cabo la detección sistemática de no conformidades reales o
potenciales a través de diferentes mecanismos, como revisiones internas, auditorías,


controles de calidad, seguimiento de indicadores o feedback del cliente. Este enfoque integral permite no solo detectar incidencias ya materializadas, sino también anticiparse a posibles desviaciones antes de que impacten en el servicio.
- Análisis y definición de acciones correctoras: Una vez identificada la no conformidad,
se realiza un análisis detallado de sus causas raíz mediante técnicas específicas (como análisis causa- efecto o metodologías de resolución de problemas). A partir de este análisis, se definen las acciones correctoras necesarias para resolver la incidencia y evitar su repetición. Estas acciones incluyen la asignación de responsables, la definición de plazos y la priorización en función del nivel de riesgo asociado.
- Implementación: Se ejecutan las acciones correctoras y, en su caso, preventivas,
asegurando su correcta integración en la operativa del proyecto. Esta fase incluye la coordinación de los equipos implicados, la asignación de recursos necesarios y la adecuada comunicación de las medidas adoptadas.
- Seguimiento y verificación: Se realiza un seguimiento continuo de las acciones
implementadas con el fin de verificar su eficacia. Para ello, se utilizan indicadores de control y mecanismos de validación que permiten comprobar si la no conformidad ha sido resuelta de manera definitiva y si las medidas aplicadas han evitado su reaparición.
- Actualización y mejora del sistema: En función de los resultados obtenidos, se procede
a la actualización de los registros de riesgos, procedimientos y documentación del sistema de gestión de calidad, si fuera necesario. De este modo, las lecciones aprendidas se integran en la operativa habitual, fortaleciendo el sistema y contribuyendo a la mejora continua. Adicionalmente, todas las no conformidades y las acciones asociadas quedan registradas en herramientas de gestión específicas, lo que permite garantizar su trazabilidad completa, facilitar su análisis agregado y generar conocimiento reutilizable para futuros proyectos. En conjunto, este enfoque estructurado y orientado a resultados permite no solo corregir incidencias de manera eficaz, sino también transformar cada no conformidad en una oportunidad de mejora, incrementando la madurez del sistema de calidad y reforzando la confianza del cliente. Enfoque a productos y servicios La gestión de calidad se aplica a todas las fases del servicio mediante procesos específicos. Planificación La fase de planificación de la calidad constituye un elemento clave para garantizar el éxito del proyecto, ya que permite establecer de forma anticipada los criterios, mecanismos y herramientas necesarios para asegurar el cumplimiento de los niveles de excelencia requeridos. En este sentido, se identificarán de manera exhaustiva todos los estándares de calidad aplicables, tanto normativos (como ISO 9001 u otros marcos de referencia) como específicos del cliente y del propio proyecto. A partir de este análisis, se definirán métricas e indicadores de rendimiento (KPIs) que permitan evaluar de forma objetiva el grado de cumplimiento de los requisitos establecidos. Estos indicadores estarán alineados con los objetivos estratégicos del servicio y cubrirán aspectos como la calidad técnica, la eficiencia operativa, la satisfacción del cliente y el cumplimiento de plazos. Asimismo, durante esta fase se diseñarán los mecanismos de seguimiento y control que permitirán medir de forma continua el desempeño del proyecto, facilitando la detección temprana de desviaciones y la adopción de medidas correctoras. Para ello, se establecerán cuadros de mando y sistemas de reporting adaptados a las necesidades de los distintos niveles de gestión. Con el fin de optimizar la toma de decisiones, se emplearán diversas herramientas y técnicas de análisis, entre las que destacan:


- Análisis coste- beneficio, que permitirá evaluar la viabilidad de las acciones de calidad,
garantizando un equilibrio adecuado entre la inversión realizada y el Valor aportado.

- Benchmarking o estudios comparativos, mediante los cuales se contrastarán prácticas,
metodologías y resultados con proyectos similares o referentes del sector, identificando oportunidades de mejora y factores de éxito.
- Diseño de experimentos, enfocado a determinar de manera objetiva qué variables
influyen en la calidad del producto o servicio, permitiendo optimizar procesos y minimizar riesgos.
- Técnicas de análisis y priorización, como matrices de decisión, análisis multicriterio o
metodologías colaborativas (tormentas de ideas, análisis de afinidad, etc.), que facilitarán la identificación y priorización de las acciones más relevantes. Adicionalmente, se integrará un enfoque preventivo basado en riesgos, mediante el cual se identificarán posibles amenazas y oportunidades desde el inicio del proyecto, definiendo planes de acción específicos para su mitigación o aprovechamiento. Esto permite no solo mejorar la calidad final, sino también incrementar la capacidad de anticipación y adaptación del equipo. En conjunto, esta planificación proporciona un marco estructurado, medible y orientado a resultados, que sirve como base para asegurar la calidad a lo largo de todo el ciclo de vida del servicio y fomentar una mejora continua sólida y sostenible. Apoyo La fase de apoyo resulta fundamental para asegurar la correcta implantación, mantenimiento y evolución del Sistema de Gestión de la Calidad, al garantizar que la organización dispone en todo momento de los recursos adecuados y alineados con los objetivos del proyecto. En este contexto, se llevará a cabo una planificación detallada de los recursos necesarios, abarcando tanto los recursos humanos como los técnicos, tecnológicos y organizativos. Se definirá la estructura del equipo de trabajo, asegurando la asignación de perfiles con la cualificación, experiencia y competencias adecuadas para cada una de las funciones del proyecto. Asimismo, se promoverá el desarrollo continuo del equipo mediante acciones formativas específicas que permitan mantener y mejorar sus capacidades en materia de calidad, metodologías y herramientas. Por otro lado, se garantizará la disponibilidad de los medios técnicos y tecnológicos necesarios para el correcto desempeño de las actividades, incluyendo herramientas de gestión, plataformas de seguimiento, sistemas de control de calidad y entornos de desarrollo adecuados. Todo ello estará orientado a facilitar la eficiencia operativa, la trazabilidad de las actuaciones y la estandarización de los procesos. Un aspecto diferencial de esta fase es la implicación activa del cliente, que participará de forma directa en los principales hitos del proyecto, tales como la validación de entregables, la definición de requisitos de calidad, el seguimiento del servicio y la evaluación de resultados. Esta colaboración continua permitirá alinear las expectativas, mejorar la comunicación y garantizar que el servicio evoluciona conforme a las necesidades reales. Asimismo, se establecerán canales de comunicación fluidos y mecanismos de coordinación eficaces, que aseguren la transparencia en la gestión, la rápida resolución de incidencias y la adecuada toma de decisiones. Estos mecanismos incluirán reuniones periódicas de seguimiento, informes de estado y cuadros de mando compartidos. La fase de apoyo integrará, además, un enfoque de mejora continua, mediante la revisión periódica del desempeño del sistema, la identificación de oportunidades de optimización y la implantación de acciones correctivas y preventivas. De este modo, no solo se garantiza la


estabilidad del sistema de gestión, sino también su capacidad de adaptación y evolución a lo largo del tiempo. En definitiva, esta fase asegura que todos los elementos necesarios personas, recursos, herramientas y colaboración con el cliente estén perfectamente coordinados para sostener un sistema de calidad robusto, eficiente y orientado a la excelencia. Operación La fase de operación constituye el núcleo de la ejecución del servicio, donde se materializan los procesos definidos y se aplican los mecanismos necesarios para garantizar el cumplimiento de los niveles de calidad establecidos. En esta etapa, empresa_s despliega un enfoque sistemático y basado en datos, apoyado en herramientas avanzadas de análisis y control que permiten supervisar de manera continua el desempeño del servicio y asegurar su alineación con los requisitos del cliente. Para ello, se emplea un conjunto integrado de técnicas de control de calidad que facilitan tanto la detección temprana de incidencias como la identificación de sus causas raíz. Entre estas herramientas destacan:

- Diagramas de causa- efecto (Ishikawa), que permiten analizar de forma estructurada los
factores que influyen en posibles desviaciones o problemas, facilitando la identificación de causas origen y la definición de acciones correctivas eficaces.

- Control estadístico de procesos, que proporciona una visión cuantitativa del
comportamiento del servicio, permitiendo determinar su estabilidad y predecibilidad, así como detectar variaciones significativas que requieran intervención.

- Flujogramas o diagramas de proceso, utilizados para representar de forma clara las
actividades, decisiones e interrelaciones, ayudando a identificar puntos críticos, ineficiencias o riesgos operativos.

- Histogramas, que permiten analizar la distribución de datos relevantes del proceso,
facilitando la identificación de patrones, dispersiones o anomalías en el comportamiento del servicio.

- Diagramas de Pareto, orientados a priorizar la resolución de incidencias, focalizando los
esfuerzos en aquellos factores que generan un mayor impacto, siguiendo el principio 80/20.

- Análisis de tendencias, mediante el cual se estudia la evolución de los indicadores a lo
largo del tiempo, permitiendo anticipar desviaciones, evaluar mejoras implementadas y apoyar la toma de decisiones estratégicas.

- Inspecciones y revisiones sistemáticas, que aseguran que los entregables cumplen con
los requisitos definidos, tanto a nivel técnico como funcional, antes de su validación por parte del cliente. Estas herramientas no se utilizan de forma aislada, sino integradas dentro de un modelo de seguimiento continuo que permite obtener una visión global y en tiempo real del estado del servicio. Este enfoque facilita la toma de decisiones basada en evidencias, incrementa la capacidad de respuesta ante incidencias y refuerza la prevención frente a posibles desviaciones. Asimismo, durante la fase de operación se fomenta una cultura de calidad proactiva, en la que el equipo participa activamente en la identificación de mejoras, la optimización de procesos y la mejora del rendimiento global. Todo ello se complementa con mecanismos de comunicación y coordinación que garantizan la transparencia y el alineamiento continuo con el cliente. En definitiva, la fase de operación no solo asegura la correcta ejecución del servicio conforme a los estándares establecidos, sino que también actúa como motor de mejora continua, contribuyendo a maximizar la calidad, la eficiencia y la satisfacción del cliente. Página 184 de 192


Producción y provisión La fase de producción y provisión tiene como objetivo garantizar que todos los productos y servicios comprometidos se generan y entregan cumpliendo estrictamente los requisitos de calidad, alcance y plazos establecidos. Para ello, empresa_s establece un conjunto de mecanismos de control, seguimiento y aseguramiento que permiten supervisar de forma integral la ejecución del servicio. En primer lugar, se definen y documentan de manera detallada los procesos de producción y prestación del servicio, asegurando que cada actividad se realiza conforme a procedimientos estandarizados y previamente validados. Esto incluye la identificación de responsables, la asignación de tareas y la definición de criterios de aceptación claros para cada entregable, lo que permite garantizar la trazabilidad completa a lo largo de todo el ciclo de ejecución. Asimismo, se implantan mecanismos de planificación y control que permiten gestionar de forma efectiva los tiempos y recursos, asegurando el cumplimiento de los hitos definidos en el cronograma. Estos mecanismos incluyen herramientas de seguimiento continuo, revisión periódica del avance y evaluación de desviaciones, lo que facilita la adopción temprana de medidas correctoras en caso necesario. Con el fin de reforzar la calidad en la ejecución, se establecen controles intermedios a lo largo de las distintas fases de producción, que permiten validar los entregables de forma progresiva antes de su aceptación final. Estos puntos de control aseguran que cualquier posible desviación se detecte y subsane en fases tempranas, reduciendo riesgos y evitando reprocesos. De igual forma, se garantiza una adecuada gestión de la configuración y de la documentación asociada, asegurando que todos los entregables se generan, identifican, versionan y almacenan conforme a los estándares establecidos. Esto contribuye a mantener la coherencia, integridad y accesibilidad de la información en todo momento. Un elemento clave en esta fase es la coordinación continua con el cliente, quien participa activamente en la validación de los resultados y en el seguimiento del servicio. Esta colaboración permite ajustar la producción a las necesidades reales y asegurar que los entregables cumplen plenamente con las expectativas. Adicionalmente, se integran mecanismos de aseguramiento de la calidad, como revisiones internas, validaciones técnicas y controles de conformidad, que verifican que los productos y servicios cumplen con los requisitos definidos antes de su entrega. En conjunto, este enfoque permite no solo garantizar la correcta ejecución y provisión del servicio en tiempo y forma, sino también asegurar un alto nivel de calidad de los entregables, minimizar riesgos operativos y mantener una orientación constante a la satisfacción del cliente. Evaluación
- La fase de evaluación representa un elemento clave dentro del ciclo de gestión de la
calidad, ya que permite realizar un análisis integral del desempeño del proyecto, identificar áreas de mejora y consolidar el conocimiento adquirido para futuros servicios. Este proceso no se limita a una revisión final, sino que constituye una oportunidad estratégica para reforzar la mejora continua y aumentar el Valor aportado al cliente.

- Al cierre del proyecto, se llevará a cabo una evaluación estructurada basada en diferentes
técnicas complementarias, que permiten obtener una visión objetiva, contrastada y multidimensional de los resultados obtenidos. Entre estas técnicas destacan:


- Encuestas de satisfacción del cliente, diseñadas para recoger de forma sistemática la
percepción de los distintos interlocutores implicados en el proyecto. Estas encuestas evaluarán aspectos clave como la calidad técnica, el cumplimiento de plazos, la comunicación, la capacidad de respuesta y el grado de adecuación a las expectativas. Los resultados serán analizados mediante indicadores específicos que permitirán identificar fortalezas y áreas de mejora.

- Sesiones de lecciones aprendidas, en las que participarán tanto el equipo de proyecto
como los responsables del cliente. Estas sesiones se orientan a analizar en profundidad el desarrollo del servicio, identificando buenas prácticas, factores de éxito y posibles desviaciones. Este ejercicio fomenta la reflexión conjunta, la mejora del trabajo colaborativo y la madurez organizativa.

- Definición de acciones correctivas y de mejora, a partir de los resultados obtenidos en
las fases anteriores. Estas acciones estarán orientadas no solo a corregir incidencias detectadas, sino también a optimizar procesos, prevenir riesgos futuros y reforzar los aspectos que han demostrado mayor eficacia. Se establecerán responsables, plazos y mecanismos de seguimiento para garantizar su correcta implantación.

- Registro y gestión del conocimiento, mediante la incorporación de toda la información
relevante en una base de datos corporativa de experiencias. Este repositorio incluirá tanto las lecciones aprendidas como los indicadores de desempeño, las soluciones aplicadas y las recomendaciones identificadas. Su objetivo es facilitar la reutilización del conocimiento en proyectos futuros, reduciendo tiempos de arranque, evitando la repetición de errores y promoviendo la mejora continua a nivel organizativo. Adicionalmente, se elaborará un informe final de evaluación que integrará los principales resultados del proyecto, el grado de cumplimiento de los objetivos de calidad y las conclusiones más relevantes. Este documento servirá como referencia tanto para el cliente como para la propia organización, consolidando la transparencia y la orientación a resultados. En conjunto, esta fase permite no solo valorar el éxito del proyecto, sino también transformar la experiencia adquirida en un activo estratégico, impulsando la excelencia operativa y la evolución continua de los servicios prestados. 3.2.5 Trazabilidad del servicio Con el objetivo de garantizar el control integral del servicio, la visibilidad completa del estado del proyecto y el cumplimiento de los niveles de calidad exigidos, empresa_s implantará un modelo avanzado de trazabilidad y seguimiento continuo, basado en gobierno multinivel, control operativo diario y mecanismos formales de reporte y validación. Este modelo permite asegurar la alineación constante con las prioridades de la Consejería de Digitalización, facilitando la toma de decisiones, la gestión de riesgos y la mejora continua del servicio. Enfoque de seguimiento continuo y comunicación estructurada El Jefe de Proyecto de empresa_s asumirá la responsabilidad global del seguimiento del servicio, realizando una supervisión continua de todas las actividades, hitos y entregables . Se establecerá un sistema de comunicación fluido con los responsables designados por la Consejería de Digitalización, garantizando:

- Información periódica sobre el estado del servicio.

- Visibilidad de avances, desviaciones e incidencias.


- Anticipación de riesgos y necesidades futuras.

- Toma ágil de decisiones.
Para ello, se celebrarán reuniones periódicas de seguimiento, de las que se generará acta formal, asegurando la trazabilidad completa de acuerdos, acciones y decisiones. Asimismo, se utilizarán las herramientas y metodologías que determine la Consejería , integrando la planificación, seguimiento y control en un ecosistema común de gestión. Modelo de Gobierno del servicio empresa_s implantará un modelo de gobierno estructurado en tres niveles, que aseguran una gestión eficaz desde la estrategia hasta la operación, alineado con las buenas prácticas en gestión de servicios TI:

- Nivel estratégico.

- Nivel táctico.
- Nivel operativo.
Este modelo se ajustará durante la fase inicial del proyecto (kick-off), adaptándose a las necesidades específicas de la Consejería de Digitalización. La organización se articulará mediante una estructura jerárquica coordinada, donde los responsables de ambas partes dirigirán el proyecto a nivel estratégico, apoyados por los responsables de proyecto en la gestión táctica y la coordinación del equipo. Niveles de relación y responsabilidades Nivel estratégico Orienta la dirección global del proyecto y el alineamiento con los objetivos de la Consejería. Principales funciones:

- Definición y supervisión de la estrategia.
- Alineación con prioridades y necesidades del servicio.

- Validación del cumplimiento del plan global.

- Aprobación de cambios de alto impacto.
- Resolución de conflictos y decisiones críticas.

- Seguimiento del rendimiento global y evolución del servicio.
En este nivel se asegurarán decisiones coherentes con la estrategia definida, garantizando la sostenibilidad del servicio a medio y largo plazo. Nivel táctico (seguimiento y control) Responsable de transformar la estrategia en acciones concretas. Funciones clave:

- Planificación detallada de actividades.
- Seguimiento del avance del proyecto.

- Supervisión técnica de los trabajos.

- Gestión de riesgos y planes de mitigación.


- Control de calidad del servicio.

- Validación de entregables.

- Propuesta de mejoras y optimización del servicio.
- Coordinación con terceros y otros equipos.
Este nivel constituye el núcleo de control del proyecto, asegurando el cumplimiento de plazos, alcance y calidad. Nivel operativo Responsable de la ejecución diaria del servicio. Incluye:
- Desarrollo de tareas técnicas.

- Seguimiento diario de actividades.

- Gestión del equipo de trabajo.
- Control de incidencias y evolución de tareas.

- Ajuste continuo de la planificación.
Se realizarán reuniones internas periódicas para garantizar la eficiencia operativa y la correcta ejecución del servicio. Comités de seguimiento y gobernanza Cada nivel se materializa en un comité específico, con reuniones periódicas, actas formales y seguimiento de acuerdos. Comité Estratégico Focalizado en la evolución del contrato y la alineación global del servicio. Responsabilidades:

- Validación del cumplimiento del plan.
- Aprobación de cambios estratégicos y ANS.

- Evaluación del rendimiento del servicio.

- Resolución de incidencias críticas.
- Gestión de recursos clave.

- Aprobación de modificaciones de alcance.
Previo a cada reunión, empresa_s elaborará un informe ejecutivo de situación, incluyendo:

- Estado global del servicio.

- Cumplimiento de ANS.
- Análisis de riesgos.

- Previsión de necesidades futuras.
Comité de Seguimiento y Control (táctico) Centrado en la ejecución del servicio. Responsabilidades: Página 188 de 192


- Revisión del estado de actividades.

- Seguimiento de objetivos y plazos.

- Gestión de incidencias relevantes.
- Análisis y mitigación de riesgos.

- Supervisión de la calidad.

- Validación de entregables.
- Coordinación técnica y operativa.
Este comité actúa como punto clave para asegurar la correcta ejecución del proyecto. Comité Operativo Orientado al día a día del servicio. Funciones:
- Seguimiento del avance de tareas.

- Evaluación continua de riesgos.

- Propuesta de medidas correctoras.
- Control del rendimiento operativo.
Se apoyará en informes periódicos que reflejen la situación actual y posibles desviaciones. Sistema de trazabilidad integral empresa_s implantará un modelo de trazabilidad completa, continua y auditable , que permitirá el seguimiento exhaustivo de todas las actividades, decisiones y entregables del proyecto a lo largo de todo su ciclo de vida. Este sistema de trazabilidad constituye un elemento central del modelo de prestación, garantizando transparencia total, control operativo y capacidad de auditoría en cualquier momento, en línea con los requisitos del pliego. Trazabilidad end- to-end del ciclo de vida La trazabilidad cubrirá de manera integral todas las fases del servicio:

- Origen de la necesidad: registro de solicitudes, requisitos y decisiones iniciales.
- Planificación: vinculación de tareas, hitos y recursos asociados .

- Ejecución: seguimiento detallado del estado de cada actividad.
- Validación: registro de pruebas, controles de calidad y aprobaciones.

- Entrega: control de versiones y documentación asociada.

- Operación y mantenimiento: seguimiento de incidencias, evoluciones y mejoras .
Cada elemento del proyecto estará identificado de forma única, versionado y relacionado con el resto de componentes, permitiendo reconstruir en todo momento su historial completo. Registro estructurado y control de la información Se garantizará el registro sistemático y estructurado de:

- Tareas y actividades realizadas (con detalle de responsable, estado y evolución)


- Incidencias, problemas y solicitudes de cambio

- Decisiones adoptadas en los distintos niveles de gobierno

- Riesgos identificados y acciones de mitigación
- Entregables generados y sus versiones

- Configuraciones, despliegues y cambios en sistemas

- Evidencias de pruebas funcionales, técnicas y de seguridad
Este enfoque permite una trazabilidad cruzada, donde cada elemento (tarea, incidencia, entregable, requisito) está vinculado con el resto. Trazabilidad de entregables y control de versiones Todos los productos generados durante el proyecto estarán sujetos a un sistema de control que asegura:
- Identificación única de cada entregable

- Versionado completo (histórico de modificaciones)

- Registro de autoría y validación
- Asociación con requisitos y tareas origen

- Evidencias de revisión y aprobación
Esto garantiza que cada entregable puede ser trazado desde su definición hasta su aceptación final, incluyendo todas sus modificaciones intermedias. Trazabilidad de incidencias y ANS Se implantará un modelo de registro que permita seguir cada incidencia desde su detección hasta su resolución, incluyendo:

- Clasificación por criticidad

- Tiempos de respuesta y resolución
- Acciones ejecutadas

- Responsables implicados

- Validación de cierre
Este sistema permitirá verificar de forma objetiva el cumplimiento de los Acuerdos de Nivel de Servicio (ANS) y aportar evidencias ante cualquier revisión o auditoría . Trazabilidad de decisiones y gobierno Todas las decisiones adoptadas en los distintos niveles (estratégico, táctico y operativo) quedarán registradas mediante:
- Actas formales de reuniones

- Registro de acuerdos y responsables

- Seguimiento de acciones derivadas
- Estado de cumplimiento de compromisos
De este modo, se asegura la trazabilidad completa de la gobernanza del proyecto, evitando pérdida de información y asegurando coherencia en la toma de decisiones.


Trazabilidad técnica y de cambios Se garantizará la trazabilidad de todos los cambios técnicos realizados en la plataforma, incluyendo:
- Cambios en configuración de sistemas

- Actualizaciones de software y despliegues

- Modificaciones en bases de datos
- Automatizaciones e integraciones

- Ajustes derivados de seguridad o rendimiento
Cada cambio estará documentado, versionado y vinculado a su causa (incidencia, mejora, evolución), permitiendo un control total del entorno. Soporte a auditoría, continuidad y transferencia El modelo de trazabilidad permitirá:

- Auditorías completas del servicio en cualquier momento

- Continuidad operativa ante cambios de equipo
- Transferencia de conocimiento estructurada

- Reducción del riesgo operativo
Toda la información estará centralizada, actualizada y accesible, lo que garantiza que cualquier elemento del servicio puede ser analizado, replicado o revisado sin dependencia de personas concretas. Factor diferencial El enfoque propuesto no se limita a registrar actividad, sino que establece una trazabilidad relacional completa, donde:

- Todo está conectado (requisitos → tareas → entregables → incidencias → decisiones)
- Todo está versionado y fechado

- Todo es auditable
Esto permite alcanzar un nivel de control superior al estándar y alineado con lo que el pliego considera máximo nivel de detalle en trazabilidad. Gestión de trabajos y aseguramiento de calidad El Jefe de Proyecto de empresa_s será el responsable de:

- Planificación y organización del servicio.

- Seguimiento de tareas y entregables.
- Gestión de incidencias y problemas.

- Garantía de calidad de los productos.

- Coordinación con la Consejería .
Todos los entregables estarán sujetos a un proceso formal de control de calidad, previo a su presentación, asegurando su adecuación a los requisitos definidos. Por su parte, la Consejería de Digitalización :


- Designará un responsable de supervisión del servicio.

- Validará los trabajos realizados.

- Podrá aceptar o rechazar entregables según los criterios de calidad.
- Actuará como interlocutor con otras áreas.
La validación final de los productos corresponderá a la Consejería, garantizando el cumplimiento de los estándares exigidos. Mejora continua y anticipación El modelo propuesto no solo permite controlar el servicio, sino también anticiparse a necesidades futuras, mediante:
- Análisis proactivo del servicio.

- Evaluación continua del rendimiento.
- Propuestas de mejora.

- Adaptación a cambios tecnológicos y funcionales.
Esto asegura un enfoque evolutivo alineado con la naturaleza del contrato y el entorno tecnológico de EducaMadrid.
